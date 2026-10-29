"""Versioned extraction schema.

`ContentExtraction` is what Gemini is asked to produce (passed as
`response_schema`). `VideoAnalysis` is what gets written to raw.json: the
content plus `schema_version`, `video` (from oEmbed) and `run` metadata.

Downstream consumers (see consumers/README.md) should key on
`schema_version`. Bump the major version on any breaking change: removing or
renaming a field, or narrowing an enum. Adding optional fields is a minor bump.

LLM-facing models deliberately avoid default values and Optional fields:
"not present" is expressed as an empty string / empty list, which keeps the
response schema simple and always fully populated.
"""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, Field

SCHEMA_VERSION = "1.0"

TS_DESC = "Timestamp in the full video as HH:MM:SS."

EvidenceShown = Literal["none", "anecdote", "backtest", "live_results", "data"]
VisualType = Literal["chart", "table", "code", "slide", "diagram", "screen"]
Confidence = Literal["high", "med", "low"]
ToolType = Literal["api", "library", "dataset", "platform", "other"]


class _Model(BaseModel):
    # No extra="forbid": the SDK would emit additionalProperties=false, which
    # the Gemini response_schema has historically rejected. Unknown keys are
    # dropped on validation instead.
    pass


# --------------------------------------------------------------------------
# LLM-facing content
# --------------------------------------------------------------------------


class Segment(_Model):
    start_ts: str = Field(description=TS_DESC)
    end_ts: str = Field(description=TS_DESC)
    topic: str
    key_points: list[str] = Field(
        description="Everything substantive said in this segment, including exact numbers."
    )


class Claim(_Model):
    ts: str = Field(description=TS_DESC)
    claim: str
    evidence_shown: EvidenceShown = Field(
        description="What evidence is actually shown on screen or stated for this claim."
    )
    caveats: str = Field(description="Caveats stated in the video; empty string if none.")


class Visual(_Model):
    ts: str = Field(description=TS_DESC)
    type: VisualType
    title: str = Field(description="Title exactly as shown; empty string if untitled.")
    axes_or_columns: list[str] = Field(
        description="Axis labels (with units/scale) for charts, column headers for tables."
    )
    values_readable: list[str] = Field(
        description=(
            "Numbers, labels, code lines and on-screen text transcribed exactly as shown. "
            "Write 'UNREADABLE' for anything that cannot be read. Never estimate."
        )
    )
    what_it_argues: str
    confidence: Confidence = Field(description="Confidence in the transcription of values.")


class Variable(_Model):
    symbol: str
    meaning: str


class Formula(_Model):
    ts: str = Field(description=TS_DESC)
    expression: str = Field(description="Formula exactly as written or spoken.")
    variables: list[Variable]


class Parameter(_Model):
    name: str
    value: str = Field(description="Value exactly as stated, including units.")


class Strategy(_Model):
    name: str
    ts: str = Field(description="First mention. " + TS_DESC)
    logic: str
    entry_rules: list[str]
    exit_rules: list[str]
    parameters: list[Parameter]
    markets_assets: list[str]
    stated_performance: str = Field(description="As stated; empty string if none.")
    costs_slippage_mentioned: bool
    costs_slippage_detail: str = Field(description="Empty string if not mentioned.")


class ToolOrData(_Model):
    name: str
    type: ToolType
    how_used: str


class OpenQuestion(_Model):
    ts: str = Field(description=TS_DESC)
    assertion: str = Field(description="What the video asserts.")
    missing_support: str = Field(description="What evidence or detail is missing.")


class ContentExtraction(_Model):
    summary: str = Field(description="Thesis of the video in a short paragraph.")
    segments: list[Segment]
    claims: list[Claim]
    visuals: list[Visual]
    formulas: list[Formula]
    strategies: list[Strategy]
    tools_and_data: list[ToolOrData]
    open_questions: list[OpenQuestion]


class DurationProbe(_Model):
    duration_s: int = Field(description="Total duration of the video in seconds.")


# --------------------------------------------------------------------------
# Stored document
# --------------------------------------------------------------------------


class VideoInfo(_Model):
    id: str
    url: str
    title: str
    channel: str
    duration_s: int | None = None


class Usage(_Model):
    prompt_tokens: int = 0
    output_tokens: int = 0
    thinking_tokens: int = 0
    total_tokens: int = 0

    def add(self, other: "Usage") -> "Usage":
        return Usage(
            prompt_tokens=self.prompt_tokens + other.prompt_tokens,
            output_tokens=self.output_tokens + other.output_tokens,
            thinking_tokens=self.thinking_tokens + other.thinking_tokens,
            total_tokens=self.total_tokens + other.total_tokens,
        )


class Window(_Model):
    start_s: int
    end_s: int


class RunInfo(_Model):
    model: str
    model_version: str = ""
    analyzed_at: str
    low_res: bool = False
    chunked: bool = False
    windows: list[Window] = Field(default_factory=list)
    calls: int = 0
    usage: Usage = Field(default_factory=Usage)
    tool_version: str = ""


class VideoAnalysis(ContentExtraction):
    schema_version: Literal["1.0"] = SCHEMA_VERSION
    video: VideoInfo
    run: RunInfo


class IndexEntry(_Model):
    id: str
    url: str
    title: str
    channel: str
    date: str
    path: str
    model: str
    model_version: str = ""
    schema_version: str
    duration_s: int | None = None
    chunked: bool = False
    calls: int = 0
    usage: Usage = Field(default_factory=Usage)
