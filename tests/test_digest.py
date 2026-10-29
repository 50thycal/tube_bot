from youtube_analyzer.digest import render
from youtube_analyzer.schema import RunInfo, Usage, VideoAnalysis, VideoInfo


def _analysis(sample, **kw):
    return VideoAnalysis(
        **sample,
        video=VideoInfo(id="dQw4w9WgXcQ", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ", title="RSI2 Strategy", channel="Quant Guy", duration_s=900),
        run=RunInfo(model="gemini-x", analyzed_at="2026-10-29T12:00:00Z", usage=Usage(total_tokens=12345), **kw),
    )


def test_render_contains_all_sections(sample):
    md = render(_analysis(sample))
    assert md.startswith("# RSI2 Strategy\n")
    for h in ["## Summary", "## Segments", "## Claims", "## Visuals", "## Formulas", "## Strategies", "## Tools & data", "## Open questions"]:
        assert h in md
    assert "**Duration:** 00:15:00" in md
    assert "12,345 tokens" in md
    # timestamps link into the video
    assert "[00:05:30](https://www.youtube.com/watch?v=dQw4w9WgXcQ&t=330s)" in md
    # values are reproduced verbatim
    assert "`2024: $48,210`" in md
    assert "`Max DD: UNREADABLE`" in md
    assert "`RSI = 100 - 100/(1+RS)`" in md
    assert "| RSI period | 2 |" in md
    assert "**Costs/slippage mentioned:** no" in md


def test_render_escapes_table_cells(sample):
    md = render(_analysis(sample))
    assert "no costs \\| pre-2020" in md


def test_render_is_deterministic(sample):
    assert render(_analysis(sample)) == render(_analysis(sample))


def test_render_empty_sections(sample):
    for k in ["segments", "claims", "visuals", "formulas", "strategies", "tools_and_data", "open_questions"]:
        sample[k] = []
    md = render(_analysis(sample))
    assert md.count("_none_") == 7


def test_render_chunked_note(sample):
    md = render(_analysis(sample, chunked=True, windows=[{"start_s": 0, "end_s": 600}, {"start_s": 600, "end_s": 900}]))
    assert "2 windows" in md
