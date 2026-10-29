import json

import pytest
from google import genai
from google.genai import _transformers
from pydantic import ValidationError

from youtube_analyzer.schema import SCHEMA_VERSION, ContentExtraction, RunInfo, VideoAnalysis, VideoInfo


def _analysis(sample):
    return VideoAnalysis(
        **sample,
        video=VideoInfo(id="dQw4w9WgXcQ", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ", title="T", channel="C"),
        run=RunInfo(model="m", analyzed_at="2026-10-29T00:00:00Z"),
    )


def test_valid_extraction(sample):
    c = ContentExtraction.model_validate(sample)
    assert c.strategies[0].parameters[0].value == "2"


def test_roundtrip_json(sample):
    a = _analysis(sample)
    data = json.loads(a.model_dump_json())
    assert data["schema_version"] == SCHEMA_VERSION == "1.0"
    assert VideoAnalysis.model_validate(data) == a


@pytest.mark.parametrize(
    "path,value",
    [
        (("claims", 0, "evidence_shown"), "vibes"),
        (("visuals", 0, "type"), "photo"),
        (("visuals", 0, "confidence"), "medium"),
        (("tools_and_data", 0, "type"), "website"),
        (("strategies", 0, "costs_slippage_mentioned"), "maybe"),
    ],
)
def test_rejects_bad_enums(sample, path, value):
    obj = sample
    for k in path[:-1]:
        obj = obj[k]
    obj[path[-1]] = value
    with pytest.raises(ValidationError):
        ContentExtraction.model_validate(sample)


@pytest.mark.parametrize("field", ["summary", "segments", "claims", "visuals", "formulas", "strategies", "tools_and_data", "open_questions"])
def test_requires_every_section(sample, field):
    del sample[field]
    with pytest.raises(ValidationError):
        ContentExtraction.model_validate(sample)


def test_schema_version_is_pinned(sample):
    a = _analysis(sample).model_dump()
    a["schema_version"] = "2.0"
    with pytest.raises(ValidationError):
        VideoAnalysis.model_validate(a)


def test_gemini_accepts_response_schema():
    """The SDK converts the Pydantic model to a Gemini Schema offline; must not raise
    and must not use features the Gemini response_schema rejects."""
    client = genai.Client(api_key="test")
    s = _transformers.t_schema(client._api_client, ContentExtraction)
    dumped = json.dumps(s.model_dump(exclude_none=True))
    assert "additional_properties" not in dumped
    assert '"default"' not in dumped
    assert set(s.required) == set(ContentExtraction.model_fields)
