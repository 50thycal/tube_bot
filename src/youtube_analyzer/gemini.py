"""Gemini calls: one structured extraction per video or per time window.

The YouTube URL is passed directly as a `file_data` part, so nothing is
downloaded locally and YouTube's datacenter bot checks are not in the path.
"""

from __future__ import annotations

import logging
import os
import random
import time
from dataclasses import dataclass
from typing import Callable, TypeVar

import httpx
from google import genai
from google.genai import errors, types
from pydantic import BaseModel, ValidationError

from . import prompt
from .metadata import VideoUnavailable
from .schema import ContentExtraction, Usage, Window, WindowExtraction

log = logging.getLogger(__name__)

# Current Flash model per Google's video-understanding docs/cookbook (Oct 2026).
DEFAULT_MODEL = "gemini-3.8-flash"

RETRYABLE_CODES = {408, 429, 500, 502, 503}
# Server gave up on the request: retrying the same heavy request rarely helps, so
# these surface as TooLong and the pipeline retries with smaller windows instead.
HEAVY_CODES = {504}
# Successful static calls have all finished within ~255 s; a streamed request that
# stalls is cut off here instead of hanging (one hung ~10 min, twice).
HTTP_TIMEOUT_MS = 6 * 60 * 1000

_PAST_END_HINTS = ("offset", "video duration", "out of range", "beyond the end")

_TOO_LONG_HINTS = (
    "token count",
    "tokens",
    "too long",
    "too large",
    "exceeds",
    "exceeded",
    "context window",
    "longer than",
    "maximum duration",
)
_UNAVAILABLE_HINTS = (
    "private",
    "unavailable",
    "not available",
    "age-restricted",
    "age restricted",
    "age verification",
    "sign in",
    "cannot be accessed",
    "could not be accessed",
    "unable to access",
    "unable to process",
    "not found",
    "permission",
    "restricted",
)

M = TypeVar("M", bound=BaseModel)


class TooLong(RuntimeError):
    """Input exceeded the context window, or output was truncated."""


class ExtractionFailed(RuntimeError):
    pass


class PastEnd(RuntimeError):
    """A clip was requested beyond the end of the video."""


@dataclass
class CallResult:
    content: BaseModel
    usage: Usage
    model_version: str
    variant: str = ""  # agentic: "response_format" | "prompt_json"


def resolve_model(cli_value: str | None = None) -> str:
    return cli_value or os.environ.get("YTA_MODEL") or DEFAULT_MODEL


def classify_error(e: Exception) -> Exception | None:
    """Map a non-retryable API error to a domain error, or None to re-raise as-is."""
    msg = (getattr(e, "message", None) or str(e)).lower()
    code = getattr(e, "code", None) or getattr(e, "status_code", None)  # generate_content / Interactions errors
    if code == 400 and any(h in msg for h in _PAST_END_HINTS):
        return PastEnd(str(e))
    if code == 400 and any(h in msg for h in _TOO_LONG_HINTS):
        return TooLong(str(e))
    # Config problems (bad key, unknown model id) are surfaced as-is.
    if "api key" in msg or "api_key" in msg or "models/" in msg:
        return None
    if code in (400, 403, 404) and any(h in msg for h in _UNAVAILABLE_HINTS):
        return VideoUnavailable(
            f"Gemini could not access the video (private, age-gated, region-locked "
            f"or removed?): {e}"
        )
    return None


def _usage(resp: types.GenerateContentResponse) -> Usage:
    um = resp.usage_metadata
    if um is None:
        return Usage()
    return Usage(
        prompt_tokens=um.prompt_token_count or 0,
        output_tokens=um.candidates_token_count or 0,
        thinking_tokens=um.thoughts_token_count or 0,
        total_tokens=um.total_token_count or 0,
    )


def _join_chunks(chunks: list[types.GenerateContentResponse]) -> types.GenerateContentResponse:
    """Fold a streamed response back into a single response."""
    if not chunks:
        raise ExtractionFailed("empty stream from Gemini")
    text = "".join(c.text or "" for c in chunks)
    finish = next((c.candidates[0].finish_reason for c in reversed(chunks) if c.candidates and c.candidates[0].finish_reason), None)
    return types.GenerateContentResponse(
        candidates=[types.Candidate(content=types.Content(role="model", parts=[types.Part(text=text)] if text else []), finish_reason=finish)],
        usage_metadata=next((c.usage_metadata for c in reversed(chunks) if c.usage_metadata), None),
        model_version=next((c.model_version for c in chunks if c.model_version), None),
        prompt_feedback=next((c.prompt_feedback for c in chunks if c.prompt_feedback), None),
    )


class GeminiExtractor:
    def __init__(
        self,
        model: str,
        low_res: bool = False,
        client: genai.Client | None = None,
        max_retries: int = 5,
        drop_retries: int = 1,
        sleep: Callable[[float], None] = time.sleep,
    ):
        self.model = model
        self.low_res = low_res
        self._client = client
        self.max_retries = max_retries
        self.drop_retries = drop_retries
        self._sleep = sleep
        mot = os.environ.get("YTA_MAX_OUTPUT_TOKENS")
        self.max_output_tokens = int(mot) if mot else None

    @property
    def client(self) -> genai.Client:
        if self._client is None:
            if not (os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")):
                raise ExtractionFailed("GEMINI_API_KEY is not set (put it in .env or the environment)")
            self._client = genai.Client(http_options=types.HttpOptions(timeout=HTTP_TIMEOUT_MS))
        return self._client

    # ------------------------------------------------------------------ public

    def extract(self, url: str, window: Window | None = None, index: int = 0, total: int | None = 1) -> CallResult:
        """Whole video (window=None) -> ContentExtraction; a clip -> WindowExtraction."""
        if window is None:
            return self._call(url, prompt.full_prompt(), ContentExtraction, None)
        text = prompt.window_prompt(window.start_s, window.end_s, index, total)
        return self._call(url, text, WindowExtraction, window)

    # ---------------------------------------------------------------- internal

    def _video_part(self, url: str, window: Window | None) -> types.Part:
        part = types.Part(file_data=types.FileData(file_uri=url))
        if window is not None:
            part.video_metadata = types.VideoMetadata(start_offset=f"{window.start_s}s", end_offset=f"{window.end_s}s")
        return part

    def _config(self, schema: type[BaseModel]) -> types.GenerateContentConfig:
        cfg = types.GenerateContentConfig(
            system_instruction=prompt.SYSTEM_INSTRUCTION,
            response_mime_type="application/json",
            response_schema=schema,
            automatic_function_calling=types.AutomaticFunctionCallingConfig(disable=True),
        )
        if self.low_res:
            cfg.media_resolution = types.MediaResolution.MEDIA_RESOLUTION_LOW
        if self.max_output_tokens:
            cfg.max_output_tokens = self.max_output_tokens
        return cfg

    def _call(
        self,
        url: str,
        text: str,
        schema: type[M],
        window: Window | None,
    ) -> CallResult:
        contents = [types.Content(role="user", parts=[self._video_part(url, window), types.Part(text=text)])]
        config = self._config(schema)
        label = f"{window.start_s}-{window.end_s}s" if window else "full video"
        t0 = time.monotonic()
        try:
            resp = self._with_retries(lambda: self._generate(contents, config))
        except Exception as e:
            log.warning("gemini %s failed after %.0fs: %s", label, time.monotonic() - t0, type(e).__name__)
            raise
        usage = _usage(resp)
        log.info("gemini %s took %.0fs (%d tokens)", label, time.monotonic() - t0, usage.total_tokens)
        try:
            content = self._parse(resp, schema)
        except (TooLong, ExtractionFailed) as e:
            e.usage = usage  # truncated responses are still billed; let the caller account for them
            raise
        return CallResult(content=content, usage=usage, model_version=resp.model_version or "")

    def _generate(self, contents: list[types.Content], config: types.GenerateContentConfig) -> types.GenerateContentResponse:
        # Streamed so the connection carries data as soon as the model produces any;
        # a long silent non-streaming request was dropped by the server (~4.5 min).
        chunks = list(self.client.models.generate_content_stream(model=self.model, contents=contents, config=config))
        return _join_chunks(chunks)

    def _with_retries(self, fn: Callable[[], types.GenerateContentResponse]) -> types.GenerateContentResponse:
        attempt = 0
        drops = 0
        while True:
            try:
                return fn()
            except httpx.TransportError as e:
                # Seen in practice: requests dropped without a response after ~255-270 s,
                # largely independent of clip length. Retry the same request once (as
                # tubetell does) before treating it as too heavy and splitting.
                if drops < self.drop_retries:
                    drops += 1
                    log.warning("connection dropped (%s); retrying same request (%d/%d)", type(e).__name__, drops, self.drop_retries)
                    self._sleep(4.0)
                    continue
                raise TooLong(f"connection dropped/timed out ({type(e).__name__}: {e}); request likely too heavy") from e
            except errors.APIError as e:
                code = getattr(e, "code", None)
                if code in HEAVY_CODES:
                    raise TooLong(f"server deadline exceeded (HTTP {code}): {e}") from e
                if code in RETRYABLE_CODES and attempt < self.max_retries:
                    delay = min(60.0, 2.0 * 2**attempt) + random.uniform(0, 1)
                    log.warning("Gemini HTTP %s, retrying in %.1fs (%d/%d)", code, delay, attempt + 1, self.max_retries)
                    self._sleep(delay)
                    attempt += 1
                    continue
                mapped = classify_error(e)
                if mapped is not None:
                    raise mapped from e
                raise

    @staticmethod
    def _parse(resp: types.GenerateContentResponse, schema: type[M]) -> M:
        cand = resp.candidates[0] if resp.candidates else None
        finish = cand.finish_reason if cand else None
        if finish == types.FinishReason.MAX_TOKENS:
            raise TooLong("output truncated (finish_reason=MAX_TOKENS)")
        text = resp.text
        if not text:
            block = getattr(resp.prompt_feedback, "block_reason", None) if resp.prompt_feedback else None
            raise ExtractionFailed(f"empty response (finish_reason={finish}, block_reason={block})")
        try:
            return schema.model_validate_json(text)
        except ValidationError as e:
            raise ExtractionFailed(f"response failed schema validation: {e}") from e
