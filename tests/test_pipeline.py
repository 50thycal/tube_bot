import json
from datetime import datetime, timezone

import pytest

from youtube_analyzer import cli
from youtube_analyzer.gemini import CallResult, TooLong
from youtube_analyzer.metadata import Metadata
from youtube_analyzer.pipeline import analyze
from youtube_analyzer.schema import ContentExtraction, DurationProbe, Usage

VID = "dQw4w9WgXcQ"
URL = f"https://youtu.be/{VID}?t=30&list=PL1"
NOW = lambda: datetime(2026, 10, 29, 12, 0, tzinfo=timezone.utc)  # noqa: E731


class FakeExtractor:
    """Stands in for GeminiExtractor. `too_long` decides which calls raise TooLong."""

    def __init__(self, sample, too_long=lambda window: False, duration=3000):
        self.sample = sample
        self.too_long = too_long
        self.duration = duration
        self.calls = []

    def _usage(self):
        return Usage(prompt_tokens=10, output_tokens=5, total_tokens=15)

    def extract(self, url, window=None, index=0, total=1):
        self.calls.append(("extract", url, window))
        if self.too_long(window):
            e = TooLong("too long")
            e.usage = None
            raise e
        return CallResult(content=ContentExtraction.model_validate(self.sample), usage=self._usage(), model_version="v-001")

    def probe_duration(self, url):
        self.calls.append(("probe", url, None))
        return CallResult(content=DurationProbe(duration_s=self.duration), usage=self._usage(), model_version="v-001")


def _meta(duration=None):
    return lambda url: Metadata(title="RSI2 Strategy", channel="Quant", duration_s=duration)


@pytest.fixture(autouse=True)
def _env(monkeypatch):
    for k in ("YTA_MODEL", "YTA_CHUNK_MINUTES", "YTA_SINGLE_PASS_TOKEN_BUDGET"):
        monkeypatch.delenv(k, raising=False)


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


def test_fallback_to_windows_on_too_long(tmp_path, sample):
    ex = FakeExtractor(sample, too_long=lambda w: w is None)
    r = analyze(URL, tmp_path, extractor=ex, metadata_fetcher=_meta(None), now=NOW)
    kinds = [c[0] for c in ex.calls]
    assert kinds == ["extract", "probe", "extract", "extract", "extract"]  # 3000s / 20min windows
    run = r.analysis.run
    assert run.chunked and [(w.start_s, w.end_s) for w in run.windows] == [(0, 1200), (1200, 2400), (2400, 3000)]
    assert r.analysis.video.duration_s == 3000
    # sample timestamps were clip-relative; they are shifted to absolute time
    assert [c.ts for c in r.analysis.claims] == ["00:01:05", "00:21:05", "00:41:05"]
    assert r.analysis.summary.count("[") == 3


def test_proactive_chunking_when_duration_known(tmp_path, sample):
    ex = FakeExtractor(sample)
    r = analyze(URL, tmp_path, extractor=ex, metadata_fetcher=_meta(3 * 3600), now=NOW)
    assert all(c[2] is not None for c in ex.calls)  # never tried single pass
    assert len(r.analysis.run.windows) == 9


def test_low_res_raises_single_pass_ceiling(tmp_path, sample):
    ex = FakeExtractor(sample)
    analyze(URL, tmp_path, extractor=ex, metadata_fetcher=_meta(3600), now=NOW, low_res=True)
    assert ex.calls[0][2] is None


def test_window_split_when_still_too_long(tmp_path, sample, monkeypatch):
    monkeypatch.setenv("YTA_CHUNK_MINUTES", "20")
    ex = FakeExtractor(sample, too_long=lambda w: w is None or (w.end_s - w.start_s) > 600)
    r = analyze(URL, tmp_path, extractor=ex, metadata_fetcher=_meta(None), now=NOW)
    spans = [(w.start_s, w.end_s) for w in r.analysis.run.windows]
    assert spans == [(0, 600), (600, 1200), (1200, 1800), (1800, 2400), (2400, 3000)]


def test_cli_invalid_url(capsys):
    assert cli.main(["analyze", "https://vimeo.com/1"]) == 2
    assert "not a YouTube URL" in capsys.readouterr().err


def test_cli_render(tmp_path, sample):
    r = analyze(URL, tmp_path, extractor=FakeExtractor(sample), metadata_fetcher=_meta(900), now=NOW)
    (r.path / "digest.md").unlink()
    assert cli.main(["render", str(r.path / "raw.json")]) == 0
    assert (r.path / "digest.md").read_text().startswith("# RSI2 Strategy")
