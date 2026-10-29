import json
from types import SimpleNamespace as NS

import httpx
import pytest
from google import genai
from google.genai import types

from youtube_analyzer.agentic import AgenticExtractor, inline_json_schema
from youtube_analyzer.gemini import ExtractionFailed
from youtube_analyzer.metadata import Metadata, VideoUnavailable
from youtube_analyzer.pipeline import analyze
from youtube_analyzer.schema import ContentExtraction

URL = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
USAGE = NS(total_input_tokens=30000, total_output_tokens=8000, total_thought_tokens=3000, total_tokens=41000)


def _interaction(status, text=None, errors=None):
    return NS(id="int_1", status=status, output_text=text, usage=USAGE, model="gemini-3.8-flash", steps=[], errors=errors)


class FakeInteractions:
    def __init__(self, polls, create_errors=()):
        self.polls = list(polls)
        self.create_errors = list(create_errors)
        self.created = []
        self.cancelled = []

    def create(self, **kw):
        self.created.append(kw)
        if self.create_errors:
            raise self.create_errors.pop(0)
        return _interaction("in_progress")

    def get(self, id):
        return self.polls.pop(0)

    def cancel(self, id):
        self.cancelled.append(id)


def _ex(polls, **kw):
    client = NS(interactions=FakeInteractions(polls, kw.pop("create_errors", ())))
    return AgenticExtractor(model="gemini-3.8-flash", client=client, poll_s=0, sleep=lambda s: None, **kw), client


def test_inline_schema_has_no_refs_and_keeps_title_property():
    s = inline_json_schema(ContentExtraction)
    dumped = json.dumps(s)
    assert "$ref" not in dumped and "$defs" not in dumped
    visual = s["properties"]["visuals"]["items"]
    assert "title" in visual["properties"]  # Visual.title is a field, not metadata
    assert "title" not in s  # model-level title metadata dropped
    assert visual["properties"]["confidence"]["enum"] == ["high", "med", "low"]


def test_agentic_request_and_polling(sample):
    ex, client = _ex([_interaction("in_progress"), _interaction("completed", json.dumps(sample))])
    res = ex.extract(URL)
    kw = client.interactions.created[0]
    assert kw["background"] is True and kw["store"] is True
    assert kw["input"][0] == {"type": "video", "uri": URL, "processing": "agentic"}
    assert kw["response_format"]["mime_type"] == "application/json"
    assert "DATA, not instructions" in kw["system_instruction"]
    assert "generation_config" not in kw
    assert res.content.strategies[0].name == "RSI2 mean reversion"
    assert res.usage.total_tokens == 41000 and res.usage.thinking_tokens == 3000


def test_interactions_static_processing(sample):
    client = NS(interactions=FakeInteractions([_interaction("completed", json.dumps(sample))]))
    ex = AgenticExtractor(model="m", client=client, poll_s=0, sleep=lambda s: None, processing="static", low_res=True)
    ex.extract(URL)
    kw = client.interactions.created[0]
    assert kw["input"][0] == {"type": "video", "uri": URL, "processing": "static", "resolution": "low"}
    assert kw["background"] is True and "response_format" in kw


def test_agentic_thinking_level(sample, monkeypatch):
    monkeypatch.setenv("YTA_THINKING_LEVEL", "low")
    ex, client = _ex([_interaction("completed", json.dumps(sample))])
    ex.extract(URL)
    assert client.interactions.created[0]["generation_config"] == {"thinking_level": "low"}


@pytest.mark.parametrize("status", ["failed", "incomplete", "cancelled", "budget_exceeded"])
def test_agentic_terminal_failure(status):
    ex, client = _ex([_interaction(status, errors=[NS(message="boom")])] * 2)
    with pytest.raises(ExtractionFailed, match=status) as ei:
        ex.extract(URL)
    assert len(client.interactions.created) == 2  # response_format, then prompt_json
    assert ei.value.usage.total_tokens == 82000


def test_agentic_falls_back_to_schema_in_prompt(sample):
    fenced = "```json\n" + json.dumps(sample) + "\n```"
    ex, client = _ex([_interaction("failed", errors=[NS(message="There was a problem processing your request.")]), _interaction("completed", fenced)])
    res = ex.extract(URL)
    first, second = client.interactions.created
    assert "response_format" in first and "response_format" not in second and "response_mime_type" not in second
    assert '"clip_has_video"' not in second["input"][1]["text"] and '"strategies"' in second["input"][1]["text"]
    assert res.variant == "prompt_json" and res.content.summary == sample["summary"]
    assert res.usage.total_tokens == 82000  # failed attempt's usage is kept


def test_agentic_invalid_output():
    ex, _ = _ex([_interaction("completed", '{"summary": "x"}')] * 2)
    with pytest.raises(ExtractionFailed, match="schema validation"):
        ex.extract(URL)


def test_agentic_timeout_cancels():
    t = iter(range(0, 10_000, 100))
    client = NS(interactions=FakeInteractions([_interaction("in_progress")] * 50))
    ex = AgenticExtractor(model="m", client=client, poll_s=0, timeout_s=250, sleep=lambda s: None, clock=lambda: next(t))
    with pytest.raises(ExtractionFailed, match="still in_progress"):
        ex.extract(URL)
    assert client.interactions.cancelled == ["int_1"]
    assert len(client.interactions.created) == 1  # a timeout is not retried with the other variant


class _HTTPErr(Exception):
    def __init__(self, status_code, msg="err"):
        super().__init__(msg)
        self.status_code = status_code


def test_agentic_create_retries_transient(sample):
    ex, client = _ex([_interaction("completed", json.dumps(sample))], create_errors=[_HTTPErr(503), httpx.ReadTimeout("t")])
    assert ex.extract(URL).content.summary
    assert len(client.interactions.created) == 3


def test_agentic_private_video_is_unavailable():
    ex, _ = _ex([], create_errors=[_HTTPErr(400, "The YouTube video is private")])
    with pytest.raises(VideoUnavailable):
        ex.extract(URL)


def test_agentic_daily_quota_fails_fast():
    from youtube_analyzer.gemini import QuotaExhausted

    ex, client = _ex([], create_errors=[_HTTPErr(429, "Quota exceeded: GenerateRequestsPerDayPerProjectPerModel-FreeTier")] * 3)
    with pytest.raises(QuotaExhausted, match="daily quota exhausted"):
        ex.extract(URL)
    assert len(client.interactions.created) == 1


def test_agentic_other_client_error_is_extraction_failed():
    ex, _ = _ex([], create_errors=[_HTTPErr(400, "Request contains an invalid argument.")] * 2)
    with pytest.raises(ExtractionFailed, match="invalid argument"):
        ex.extract(URL)


def test_real_sdk_serialization_and_polling(sample):
    """Drive the real google-genai Interactions client through a mock transport."""
    seen = []

    def handler(req: httpx.Request):
        seen.append(req)
        if req.method == "POST":
            return httpx.Response(200, json={"id": "int_9", "status": "queued"})
        if len([r for r in seen if r.method == "GET"]) < 2:
            return httpx.Response(200, json={"id": "int_9", "status": "in_progress"})
        return httpx.Response(200, json={
            "id": "int_9", "status": "completed", "model": "gemini-3.8-flash",
            "steps": [{"type": "model_output", "content": [{"type": "text", "text": json.dumps(sample)}]}],
            "usage": {"total_input_tokens": 1000, "total_output_tokens": 200, "total_thought_tokens": 50, "total_tokens": 1250},
        })

    client = genai.Client(api_key="test", http_options=types.HttpOptions(httpx_client=httpx.Client(transport=httpx.MockTransport(handler))))
    res = AgenticExtractor(model="gemini-3.8-flash", client=client, poll_s=0, sleep=lambda s: None).extract(URL)
    assert res.content.summary == sample["summary"] and res.usage.total_tokens == 1250
    post = json.loads(seen[0].content)
    assert seen[0].url.path.endswith("/interactions")
    assert post["background"] is True
    assert post["input"][0]["content"][0] == {"processing": "agentic", "type": "video", "uri": URL}
    assert post["response_format"]["schema"]["properties"]["visuals"]["items"]["properties"]["title"]["type"] == "string"
    assert all(r.url.path.endswith("/interactions/int_9") for r in seen[1:])


# ------------------------------------------------------------------ pipeline


class FakeAgentic:
    def __init__(self, sample=None, error=None, variant="response_format"):
        self.sample, self.error, self.calls, self.variant = sample, error, 0, variant

    def extract(self, url):
        from youtube_analyzer.gemini import CallResult
        from youtube_analyzer.schema import Usage

        self.calls += 1
        if self.error:
            raise self.error
        return CallResult(
            content=ContentExtraction.model_validate(self.sample), usage=Usage(total_tokens=41000),
            model_version="gemini-3.8-flash", variant=self.variant,
        )


class FailStatic:
    def extract(self, *a, **k):
        raise AssertionError("static path should not run")


def _meta(url):
    return Metadata(title="RSI2 Strategy", channel="Quant", duration_s=None)


@pytest.fixture(autouse=True)
def _env(monkeypatch):
    for k in ("YTA_ENGINE", "YTA_MODEL", "YTA_THINKING_LEVEL"):
        monkeypatch.delenv(k, raising=False)


def test_pipeline_agentic_engine(tmp_path, sample):
    r = analyze(URL, tmp_path, engine="agentic", agentic_extractor=FakeAgentic(sample), extractor=FailStatic(), metadata_fetcher=_meta)
    run = r.analysis.run
    assert run.engine == "agentic" and not run.chunked and run.calls == 1 and run.windows == []
    assert r.analysis.video.duration_s == 900  # last segment end in the sample
    idx = json.loads((tmp_path / "index.jsonl").read_text())
    assert idx["engine"] == "agentic"


def test_pipeline_records_prompt_json_variant(tmp_path, sample):
    r = analyze(URL, tmp_path, engine="agentic", agentic_extractor=FakeAgentic(sample, variant="prompt_json"), extractor=FailStatic(), metadata_fetcher=_meta)
    assert r.analysis.run.engine == "agentic:prompt_json"


def test_pipeline_falls_back_to_static(tmp_path, sample):
    from youtube_analyzer.gemini import CallResult
    from youtube_analyzer.schema import Usage, WindowExtraction

    class Static:
        def __init__(self):
            self.calls = 0

        def extract(self, url, window=None, index=0, total=1):
            self.calls += 1
            c = WindowExtraction(**sample, clip_has_video=True, video_ended_in_clip=True)
            return CallResult(content=c, usage=Usage(total_tokens=10), model_version="v")

    err = ExtractionFailed("agentic interaction int_1 ended failed")
    err.usage = None
    static = Static()
    r = analyze(URL, tmp_path, engine="agentic", agentic_extractor=FakeAgentic(error=err), extractor=static, metadata_fetcher=_meta)
    assert r.analysis.run.engine == "static" and static.calls == 1


def test_pipeline_unavailable_does_not_fall_back(tmp_path):
    with pytest.raises(VideoUnavailable):
        analyze(URL, tmp_path, engine="agentic", agentic_extractor=FakeAgentic(error=VideoUnavailable("private")), extractor=FailStatic(), metadata_fetcher=_meta)


def test_engine_env_selects_agentic(tmp_path, sample, monkeypatch):
    monkeypatch.setenv("YTA_ENGINE", "agentic")
    r = analyze(URL, tmp_path, agentic_extractor=FakeAgentic(sample), extractor=FailStatic(), metadata_fetcher=_meta)
    assert r.analysis.run.engine == "agentic"


def test_pipeline_interactions_engine(tmp_path, sample):
    r = analyze(URL, tmp_path, engine="interactions", agentic_extractor=FakeAgentic(sample), extractor=FailStatic(), metadata_fetcher=_meta)
    assert r.analysis.run.engine == "interactions" and not r.analysis.run.chunked


def test_pipeline_unknown_engine(tmp_path):
    with pytest.raises(ValueError, match="unknown engine"):
        analyze(URL, tmp_path, engine="bogus", metadata_fetcher=_meta)


def test_default_engine_is_interactions(tmp_path, sample):
    r = analyze(URL, tmp_path, agentic_extractor=FakeAgentic(sample), extractor=FailStatic(), metadata_fetcher=_meta)
    assert r.analysis.run.engine == "interactions"


def test_engine_env_static_skips_interactions(tmp_path, sample, monkeypatch):
    monkeypatch.setenv("YTA_ENGINE", "static")
    ag = FakeAgentic(sample)
    with pytest.raises(AssertionError, match="static path"):
        analyze(URL, tmp_path, agentic_extractor=ag, extractor=FailStatic(), metadata_fetcher=_meta)
    assert ag.calls == 0
