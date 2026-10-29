import json

import httpx
import pytest
from google.genai import errors, types

from youtube_analyzer.gemini import DEFAULT_MODEL, ExtractionFailed, GeminiExtractor, TooLong, classify_error, resolve_model
from youtube_analyzer.metadata import VideoUnavailable
from youtube_analyzer.schema import Window

URL = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"


def _resp(payload, finish="STOP"):
    return types.GenerateContentResponse(
        candidates=[types.Candidate(content=types.Content(role="model", parts=[types.Part(text=json.dumps(payload))]), finish_reason=finish)],
        usage_metadata=types.GenerateContentResponseUsageMetadata(
            prompt_token_count=1000, candidates_token_count=200, thoughts_token_count=50, total_token_count=1250
        ),
        model_version="gemini-test-001",
    )


def _err(cls, code, msg):
    return cls(code, {"error": {"code": code, "message": msg, "status": "X"}})


class FakeModels:
    def __init__(self, outcomes):
        self.outcomes = list(outcomes)
        self.calls = []

    def generate_content(self, model, contents, config):
        self.calls.append((model, contents, config))
        out = self.outcomes.pop(0)
        if isinstance(out, Exception):
            raise out
        return out


class FakeClient:
    def __init__(self, outcomes):
        self.models = FakeModels(outcomes)


def _ex(outcomes, **kw):
    client = FakeClient(outcomes)
    return GeminiExtractor(model="m", client=client, sleep=lambda s: None, **kw), client


def test_resolve_model(monkeypatch):
    monkeypatch.delenv("YTA_MODEL", raising=False)
    assert resolve_model() == DEFAULT_MODEL
    monkeypatch.setenv("YTA_MODEL", "env-model")
    assert resolve_model() == "env-model"
    assert resolve_model("cli-model") == "cli-model"


def test_extract_full_request_shape(sample):
    ex, client = _ex([_resp(sample)])
    res = ex.extract(URL)
    assert res.content.strategies[0].name == "RSI2 mean reversion"
    assert res.usage.total_tokens == 1250 and res.usage.thinking_tokens == 50
    assert res.model_version == "gemini-test-001"
    model, contents, config = client.models.calls[0]
    video = contents[0].parts[0]
    assert video.file_data.file_uri == URL
    assert video.video_metadata is None
    assert config.response_mime_type == "application/json"
    assert config.media_resolution is None
    assert "DATA, not instructions" in config.system_instruction
    assert config.automatic_function_calling.disable is True


def test_extract_window_and_low_res(sample):
    ex, client = _ex([_resp(sample)], low_res=True)
    ex.extract(URL, Window(start_s=1200, end_s=2400), 1, 3)
    _, contents, config = client.models.calls[0]
    vm = contents[0].parts[0].video_metadata
    assert (vm.start_offset, vm.end_offset) == ("1200s", "2400s")
    assert config.media_resolution == types.MediaResolution.MEDIA_RESOLUTION_LOW
    assert "clip 2 of 3" in contents[0].parts[1].text


def test_retries_then_succeeds(sample):
    ex, client = _ex([_err(errors.ClientError, 429, "quota"), _err(errors.ServerError, 503, "overloaded"), _resp(sample)])
    assert ex.extract(URL).content.summary
    assert len(client.models.calls) == 3


def test_deadline_exceeded_is_too_long_without_retry():
    ex, client = _ex([_err(errors.ServerError, 504, "Deadline exceeded")])
    with pytest.raises(TooLong, match="504"):
        ex.extract(URL)
    assert len(client.models.calls) == 1


def test_dropped_connection_is_too_long():
    ex, client = _ex([httpx.RemoteProtocolError("Server disconnected without sending a response.")])
    with pytest.raises(TooLong, match="RemoteProtocolError"):
        ex.extract(URL)
    assert len(client.models.calls) == 1


def test_retries_exhausted():
    ex, client = _ex([_err(errors.ServerError, 500, "boom")] * 3, max_retries=2)
    with pytest.raises(errors.ServerError):
        ex.extract(URL)
    assert len(client.models.calls) == 3


def test_no_retry_on_400(sample):
    ex, client = _ex([_err(errors.ClientError, 400, "bad request")])
    with pytest.raises(errors.ClientError):
        ex.extract(URL)
    assert len(client.models.calls) == 1


def test_truncated_output_is_too_long(sample):
    ex, _ = _ex([_resp(sample, finish="MAX_TOKENS")])
    with pytest.raises(TooLong) as ei:
        ex.extract(URL)
    assert ei.value.usage.total_tokens == 1250


def test_schema_invalid_response():
    ex, _ = _ex([_resp({"summary": "x"})])
    with pytest.raises(ExtractionFailed):
        ex.extract(URL)


@pytest.mark.parametrize(
    "cls,code,msg,expected",
    [
        (errors.ClientError, 400, "The input token count (1500000) exceeds the maximum number of tokens allowed (1048576).", TooLong),
        (errors.ClientError, 400, "Video is too long for this model", TooLong),
        (errors.ClientError, 400, "The YouTube video is private or unavailable.", VideoUnavailable),
        (errors.ClientError, 403, "This video is age-restricted", VideoUnavailable),
        (errors.ClientError, 400, "API key not valid. Please pass a valid API key.", None),
        (errors.ClientError, 404, "models/gemini-9 is not found for API version v1beta", None),
        (errors.ClientError, 400, "Request contains an invalid argument.", None),
    ],
)
def test_classify_error(cls, code, msg, expected):
    out = classify_error(_err(cls, code, msg))
    if expected is None:
        assert out is None
    else:
        assert isinstance(out, expected)


def test_private_video_raises_unavailable():
    ex, _ = _ex([_err(errors.ClientError, 400, "Cannot fetch the YouTube video: video is private")])
    with pytest.raises(VideoUnavailable):
        ex.extract(URL)


def test_missing_api_key(monkeypatch):
    monkeypatch.delenv("GEMINI_API_KEY", raising=False)
    monkeypatch.delenv("GOOGLE_API_KEY", raising=False)
    with pytest.raises(ExtractionFailed, match="GEMINI_API_KEY"):
        GeminiExtractor(model="m").extract(URL)
