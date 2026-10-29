"""Agentic video understanding via the Gemini Interactions API.

With `processing: "agentic"` the model navigates the video timeline itself
(transcript, frames, resolution on demand) instead of decoding every frame up
front. One call covers the whole video, so there are no windows to merge.

The call runs with `background=True` and is polled. This avoids holding one HTTP
request open while the server works: in practice, long synchronous
generate_content requests on YouTube URLs were dropped after ~255-270 s.
"""

from __future__ import annotations

import logging
import os
import random
import time
from typing import Any, Callable

import httpx
from pydantic import ValidationError

from . import prompt
from .gemini import CallResult, ExtractionFailed, classify_error
from .metadata import VideoUnavailable
from .schema import ContentExtraction, Usage

log = logging.getLogger(__name__)

RETRYABLE_STATUS = {408, 429, 500, 502, 503, 504}
PENDING = {"queued", "in_progress"}


def inline_json_schema(model: type) -> dict[str, Any]:
    """Pydantic JSON schema with $refs inlined and title metadata dropped.

    The Interactions API accepts "a subset of JSON Schema"; a flat, ref-free
    schema is the conservative choice.
    """
    schema = model.model_json_schema()
    defs = schema.pop("$defs", {})

    def walk(node: Any) -> Any:
        if isinstance(node, dict):
            if "$ref" in node:
                return walk(defs[node["$ref"].rsplit("/", 1)[-1]])
            # "title" is metadata when its value is a string; a *property* named
            # title (e.g. Visual.title) maps to a dict and is kept.
            return {k: walk(v) for k, v in node.items() if not (k == "title" and isinstance(v, str))}
        if isinstance(node, list):
            return [walk(v) for v in node]
        return node

    return walk(schema)


def _status_code(e: Exception) -> int | None:
    code = getattr(e, "status_code", None) or getattr(e, "code", None)
    return code if isinstance(code, int) else None


class AgenticExtractor:
    def __init__(
        self,
        model: str,
        client: Any = None,
        poll_s: float = 5.0,
        timeout_s: float | None = None,
        max_retries: int = 5,
        sleep: Callable[[float], None] = time.sleep,
        clock: Callable[[], float] = time.monotonic,
    ):
        self.model = model
        self._client = client
        self.poll_s = poll_s
        self.timeout_s = timeout_s or float(os.environ.get("YTA_AGENTIC_TIMEOUT_S", 1800))
        self.max_retries = max_retries
        self._sleep = sleep
        self._clock = clock
        self.thinking_level = os.environ.get("YTA_THINKING_LEVEL") or None

    @property
    def client(self) -> Any:
        if self._client is None:
            if not (os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")):
                raise ExtractionFailed("GEMINI_API_KEY is not set (put it in .env or the environment)")
            from google import genai

            self._client = genai.Client()
        return self._client

    def extract(self, url: str) -> CallResult:
        """Try schema-constrained output first, then schema-in-prompt.

        First live run: agentic processing ran (processing_call/result steps) and
        then the interaction ended "failed" with 0 tokens while response_format
        was set; no public example combines agentic video with response_format.
        Failed interactions are not billed, so the fallback costs nothing.
        """
        spent = Usage()
        last: ExtractionFailed | None = None
        for variant in ("response_format", "prompt_json"):
            try:
                res = self._run_once(url, structured=(variant == "response_format"))
            except ExtractionFailed as e:
                spent = spent.add(getattr(e, "usage", None) or Usage())
                if getattr(e, "timed_out", False):
                    raise
                log.warning("agentic (%s) failed: %s", variant, e)
                last = e
                continue
            res.usage = res.usage.add(spent)
            res.variant = variant
            return res
        last.usage = spent
        raise last

    def _run_once(self, url: str, structured: bool) -> CallResult:
        t0 = self._clock()
        schema = inline_json_schema(ContentExtraction)
        text = prompt.full_prompt()
        if not structured:
            text += prompt.json_schema_instruction(schema)
        kwargs: dict[str, Any] = dict(
            model=self.model,
            input=[
                {"type": "video", "uri": url, "processing": "agentic"},
                {"type": "text", "text": text},
            ],
            system_instruction=prompt.SYSTEM_INSTRUCTION,
            background=True,
            store=True,  # background interactions are retrieved by id
        )
        if structured:
            kwargs["response_format"] = {"type": "text", "mime_type": "application/json", "schema": schema}
            kwargs["response_mime_type"] = "application/json"
        if self.thinking_level:
            kwargs["generation_config"] = {"thinking_level": self.thinking_level}

        interaction = self._retry("create", lambda: self.client.interactions.create(**kwargs))
        iid = interaction.id
        log.info("agentic interaction %s (%s): %s", iid, "response_format" if structured else "prompt_json", interaction.status)
        while interaction.status in PENDING:
            if self._clock() - t0 > self.timeout_s:
                self._cancel(iid)
                err = ExtractionFailed(f"agentic interaction {iid} still {interaction.status} after {self.timeout_s:.0f}s")
                err.timed_out = True
                raise err
            self._sleep(self.poll_s)
            interaction = self._retry("get", lambda: self.client.interactions.get(id=iid))

        elapsed = self._clock() - t0
        usage = _usage(interaction)
        steps = _step_counts(interaction)
        log.info(
            "agentic %s %s after %.0fs (%d tokens; steps: %s)", iid, interaction.status, elapsed, usage.total_tokens, steps
        )
        if interaction.status != "completed":
            errs = "; ".join(str(getattr(e, "message", e)) for e in (interaction.errors or []))
            err = ExtractionFailed(f"agentic interaction {iid} ended {interaction.status}: {errs or 'no error detail'}")
            err.usage = usage
            raise err
        out = interaction.output_text or ""
        if not out.strip():
            err = ExtractionFailed(f"agentic interaction {iid} completed with no output")
            err.usage = usage
            raise err
        try:
            content = ContentExtraction.model_validate_json(out if structured else _json_object(out))
        except ValidationError as e:
            err = ExtractionFailed(f"agentic output failed schema validation: {e}")
            err.usage = usage
            raise err from e
        return CallResult(content=content, usage=usage, model_version=str(interaction.model or self.model))

    # ---------------------------------------------------------------- internal

    def _retry(self, what: str, fn: Callable[[], Any]) -> Any:
        attempt = 0
        while True:
            try:
                return fn()
            except Exception as e:  # Interactions raises its own GenAiError family, plus httpx errors
                if isinstance(e, (ExtractionFailed, VideoUnavailable)):
                    raise
                code = _status_code(e)
                transient = isinstance(e, httpx.TransportError) or code in RETRYABLE_STATUS
                if transient and attempt < self.max_retries:
                    delay = min(60.0, 2.0 * 2**attempt) + random.uniform(0, 1)
                    log.warning("agentic %s failed (%s %s), retrying in %.1fs", what, code or type(e).__name__, e, delay)
                    self._sleep(delay)
                    attempt += 1
                    continue
                mapped = classify_error(e) if code else None
                if isinstance(mapped, VideoUnavailable):
                    raise mapped from e
                raise ExtractionFailed(f"agentic {what} failed: {type(e).__name__}: {e}") from e

    def _cancel(self, iid: str) -> None:
        try:
            self.client.interactions.cancel(id=iid)
        except Exception as e:  # best effort
            log.warning("could not cancel interaction %s: %s", iid, e)


def _json_object(text: str) -> str:
    """The outermost {...} of a free-text reply (tolerates ```json fences or prose)."""
    start, end = text.find("{"), text.rfind("}")
    return text[start : end + 1] if start != -1 and end > start else text


def _usage(interaction: Any) -> Usage:
    u = getattr(interaction, "usage", None)
    if u is None:
        return Usage()
    return Usage(
        prompt_tokens=u.total_input_tokens or 0,
        output_tokens=u.total_output_tokens or 0,
        thinking_tokens=u.total_thought_tokens or 0,
        total_tokens=u.total_tokens or 0,
    )


def _step_counts(interaction: Any) -> dict[str, int]:
    counts: dict[str, int] = {}
    for s in getattr(interaction, "steps", None) or []:
        t = getattr(s, "type", type(s).__name__)
        counts[t] = counts.get(t, 0) + 1
    return counts
