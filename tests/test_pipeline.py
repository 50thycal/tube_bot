import json
from datetime import datetime, timezone

import pytest

from youtube_analyzer import cli
from youtube_analyzer.gemini import CallResult, ExtractionFailed, PastEnd, TooLong
from youtube_analyzer.metadata import Metadata
from youtube_analyzer.pipeline import analyze
from youtube_analyzer.schema import ContentExtraction, Usage, Window, WindowExtraction

VID = "dQw4w9WgXcQ"
URL = f"https://youtu.be/{VID}?t=30&list=PL1"
NOW = lambda: datetime(2026, 10, 29, 12, 0, tzinfo=timezone.utc)  # noqa: E731


class FakeExtractor:
    """Stands in for GeminiExtractor over a video of `duration` seconds.

    `too_long(window)` decides which calls raise TooLong. Window responses carry
    the clip flags the real model is asked to set.
    """

    def __init__(self, sample, too_long=lambda window: False, duration=3000, past_end_error=False):
        self.sample = sample
        self.too_long = too_long
        self.duration = duration
        self.past_end_error = past_end_error
        self.calls = []

    def _usage(self):
        return Usage(prompt_tokens=10, output_tokens=5, total_tokens=15)

    def extract(self, url, window=None, index=0, total=1):
        self.calls.append(("extract", url, window))
        if self.too_long(window):
            e = TooLong("too long")
            e.usage = None
            raise e
        if window is None:
            content = ContentExtraction.model_validate(self.sample)
        elif window.start_s >= self.duration:
            if self.past_end_error:
                raise PastEnd("start_offset exceeds video duration")
            empty = {k: [] for k in self.sample if k != "summary"}
            content = WindowExtraction(summary="", clip_has_video=False, video_ended_in_clip=True, **empty)
        else:
            content = WindowExtraction(
                **self.sample, clip_has_video=True, video_ended_in_clip=window.end_s >= self.duration
            )
        return CallResult(content=content, usage=self._usage(), model_version="v-001")


def _meta(duration=None):
    return lambda url: Metadata(title="RSI2 Strategy", channel="Quant", duration_s=duration)


@pytest.fixture(autouse=True)
def _env(monkeypatch):
    for k in ("YTA_MODEL", "YTA_MAX_WINDOWS"):
        monkeypatch.delenv(k, raising=False)
    monkeypatch.setenv("YTA_ENGINE", "static")  # agentic engine is covered in test_agentic.py
    # Tests below are written against these sizes; defaults are checked separately.
    monkeypatch.setenv("YTA_CHUNK_MINUTES", "15")
    monkeypatch.setenv("YTA_SINGLE_PASS_MAX_MINUTES", "20")


def test_default_window_sizes(tmp_path, sample, monkeypatch):
    monkeypatch.delenv("YTA_CHUNK_MINUTES")
    monkeypatch.delenv("YTA_SINGLE_PASS_MAX_MINUTES")
    ex = FakeExtractor(sample, duration=420)
    analyze(URL, tmp_path, extractor=ex, metadata_fetcher=_meta(420), now=NOW)
    assert ex.calls[0][2] is None  # <= 7 min: single pass
    ex = FakeExtractor(sample, duration=1030)
    analyze(URL, tmp_path, extractor=ex, metadata_fetcher=_meta(None), now=NOW, force=True)
    assert [c[2].start_s for c in ex.calls] == [0, 420, 840]  # 7-min windows, stops when the video ends


def test_last_walked_window_trimmed_to_video_end(tmp_path, sample):
    sample["segments"][-1]["end_ts"] = "00:02:10"  # clip-relative: video ends 2:10 into the last window
    ex = FakeExtractor(sample, duration=1030)
    r = analyze(URL, tmp_path, extractor=ex, metadata_fetcher=_meta(None), now=NOW)
    assert [(w.start_s, w.end_s) for w in r.analysis.run.windows] == [(0, 900), (900, 1030)]
    assert r.analysis.video.duration_s == 1030
    assert "[00:15:00–00:17:10]" in r.analysis.summary


def test_single_pass(tmp_path, sample):
    ex = FakeExtractor(sample)
    r = analyze(URL, tmp_path, extractor=ex, metadata_fetcher=_meta(900), now=NOW, model="m")
    assert r.status == "created"
    assert r.path.name == f"2026-10-29_{VID}_rsi2-strategy"
    assert ex.calls == [("extract", f"https://www.youtube.com/watch?v={VID}", None)]
    raw = json.loads((r.path / "raw.json").read_text())
    assert raw["schema_version"] == "1.0"
    assert raw["video"] == {"id": VID, "url": f"https://www.youtube.com/watch?v={VID}", "title": "RSI2 Strategy", "channel": "Quant", "duration_s": 900}
    assert raw["run"]["model"] == "m" and raw["run"]["model_version"] == "v-001"
    assert raw["run"]["calls"] == 1 and raw["run"]["usage"]["total_tokens"] == 15
    assert not raw["run"]["chunked"]
    idx = [json.loads(line) for line in (tmp_path / "index.jsonl").read_text().splitlines()]
    assert idx[0]["id"] == VID and idx[0]["model"] == "m" and idx[0]["usage"]["total_tokens"] == 15


def test_dedupe_skip_and_force(tmp_path, sample):
    analyze(URL, tmp_path, extractor=FakeExtractor(sample), metadata_fetcher=_meta(900), now=NOW)
    ex = FakeExtractor(sample)
    r = analyze(f"https://www.youtube.com/watch?v={VID}", tmp_path, extractor=ex, metadata_fetcher=_meta(900), now=NOW)
    assert r.status == "skipped" and ex.calls == []
    r = analyze(URL, tmp_path, extractor=ex, metadata_fetcher=_meta(900), now=NOW, force=True)
    assert r.status == "created" and len(ex.calls) == 1
    assert len((tmp_path / "index.jsonl").read_text().splitlines()) == 1


def test_unknown_duration_walks_windows(tmp_path, sample):
    ex = FakeExtractor(sample, duration=2500)
    r = analyze(URL, tmp_path, extractor=ex, metadata_fetcher=_meta(None), now=NOW)
    # never a whole-video request; stops when the model says the video ended in the clip
    assert [c[2] for c in ex.calls] == [Window(start_s=0, end_s=900), Window(start_s=900, end_s=1800), Window(start_s=1800, end_s=2700)]
    run = r.analysis.run
    assert run.chunked and run.calls == 3 and run.usage.total_tokens == 45
    # sample timestamps were clip-relative; they are shifted to absolute time
    assert [c.ts for c in r.analysis.claims] == ["00:01:05", "00:16:05", "00:31:05"]
    assert r.analysis.summary.count("[") == 3
    assert r.analysis.video.duration_s == 1800 + 15 * 60  # last segment end, shifted


def test_unknown_duration_exact_multiple_stops_on_empty_window(tmp_path, sample):
    ex = FakeExtractor(sample, duration=1800)
    ex_calls_end = []
    orig = ex.extract

    def extract(url, window=None, index=0, total=1):
        res = orig(url, window, index, total)
        if window is not None and res.content.clip_has_video:
            res.content.video_ended_in_clip = False  # model didn't notice the end
        ex_calls_end.append(window)
        return res

    ex.extract = extract
    r = analyze(URL, tmp_path, extractor=ex, metadata_fetcher=_meta(None), now=NOW)
    assert len(ex_calls_end) == 3  # third window is empty -> stop
    assert len(r.analysis.run.windows) == 2


def test_unknown_duration_past_end_error_stops(tmp_path, sample):
    ex = FakeExtractor(sample, duration=1800, past_end_error=True)
    orig = ex.extract

    def extract(url, window=None, index=0, total=1):
        res = orig(url, window, index, total)
        res.content.video_ended_in_clip = False
        return res

    ex.extract = extract
    r = analyze(URL, tmp_path, extractor=ex, metadata_fetcher=_meta(None), now=NOW)
    assert len(r.analysis.run.windows) == 2


def test_max_windows_cap(tmp_path, sample, monkeypatch):
    monkeypatch.setenv("YTA_MAX_WINDOWS", "3")
    ex = FakeExtractor(sample, duration=100 * 3600)
    r = analyze(URL, tmp_path, extractor=ex, metadata_fetcher=_meta(None), now=NOW)
    assert len(ex.calls) == 3 and len(r.analysis.run.windows) == 3


def test_short_known_duration_single_pass(tmp_path, sample):
    ex = FakeExtractor(sample, duration=600)
    r = analyze(URL, tmp_path, extractor=ex, metadata_fetcher=_meta(600), now=NOW)
    assert [c[2] for c in ex.calls] == [None] and not r.analysis.run.chunked
    assert r.analysis.video.duration_s == 600


def test_reactive_fallback_when_single_pass_too_long(tmp_path, sample, monkeypatch):
    monkeypatch.setenv("YTA_CHUNK_MINUTES", "5")
    ex = FakeExtractor(sample, duration=900, too_long=lambda w: w is None)
    r = analyze(URL, tmp_path, extractor=ex, metadata_fetcher=_meta(900), now=NOW)
    assert [c[0] for c in ex.calls] == ["extract"] * 4
    assert [(w.start_s, w.end_s) for w in r.analysis.run.windows] == [(0, 300), (300, 600), (600, 900)]


def test_single_pass_boundary(tmp_path, sample):
    ex = FakeExtractor(sample, duration=1200)
    analyze(URL, tmp_path, extractor=ex, metadata_fetcher=_meta(1200), now=NOW)
    assert ex.calls[0][2] is None
    ex = FakeExtractor(sample, duration=1201)
    analyze(URL, tmp_path, extractor=ex, metadata_fetcher=_meta(1201), now=NOW, force=True)
    assert ex.calls[0][2] is not None


def test_proactive_chunking_when_duration_known(tmp_path, sample):
    ex = FakeExtractor(sample, duration=3 * 3600)
    r = analyze(URL, tmp_path, extractor=ex, metadata_fetcher=_meta(3 * 3600), now=NOW)
    assert all(c[2] is not None for c in ex.calls)
    assert len(r.analysis.run.windows) == 12


def test_window_split_when_still_too_long(tmp_path, sample):
    ex = FakeExtractor(sample, duration=1800, too_long=lambda w: w is None or (w.end_s - w.start_s) > 450)
    r = analyze(URL, tmp_path, extractor=ex, metadata_fetcher=_meta(None), now=NOW)
    spans = [(w.start_s, w.end_s) for w in r.analysis.run.windows]
    assert spans == [(0, 450), (450, 900), (900, 1350), (1350, 1800)]


def test_default_seven_minute_window_can_be_split(tmp_path, sample, monkeypatch):
    monkeypatch.delenv("YTA_CHUNK_MINUTES")
    monkeypatch.delenv("YTA_SINGLE_PASS_MAX_MINUTES")
    sample["segments"][-1]["end_ts"] = "00:03:00"
    ex = FakeExtractor(sample, duration=420, too_long=lambda w: w is None or (w.end_s - w.start_s) > 300)
    r = analyze(URL, tmp_path, extractor=ex, metadata_fetcher=_meta(None), now=NOW)
    assert [w.start_s for w in r.analysis.run.windows] == [0, 210]  # 7-min window halved, not aborted
    assert [c[2].end_s - c[2].start_s for c in ex.calls if c[2]] == [420, 210, 210]


def test_nothing_extracted_fails(tmp_path, sample):
    ex = FakeExtractor(sample, duration=0)
    with pytest.raises(ExtractionFailed, match="no window"):
        analyze(URL, tmp_path, extractor=ex, metadata_fetcher=_meta(None), now=NOW)
    assert not (tmp_path / "index.jsonl").exists()


def test_cli_invalid_url(capsys):
    assert cli.main(["analyze", "https://vimeo.com/1"]) == 2
    assert "not a YouTube URL" in capsys.readouterr().err


def test_cli_render(tmp_path, sample):
    r = analyze(URL, tmp_path, extractor=FakeExtractor(sample), metadata_fetcher=_meta(900), now=NOW)
    (r.path / "digest.md").unlink()
    assert cli.main(["render", str(r.path / "raw.json")]) == 0
    assert (r.path / "digest.md").read_text().startswith("# RSI2 Strategy")
