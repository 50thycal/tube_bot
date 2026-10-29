import json

from youtube_analyzer.schema import RunInfo, VideoAnalysis, VideoInfo
from youtube_analyzer.store import Store, dir_name, load_analysis, slugify

VID = "dQw4w9WgXcQ"


def _a(sample, vid=VID, title="RSI(2): The Best Strategy?! 🚀", date="2026-10-29"):
    return VideoAnalysis(
        **sample,
        video=VideoInfo(id=vid, url=f"https://www.youtube.com/watch?v={vid}", title=title, channel="C"),
        run=RunInfo(model="m", analyzed_at=f"{date}T10:00:00Z"),
    )


def test_slugify():
    assert slugify("RSI(2): The Best Strategy?! 🚀") == "rsi-2-the-best-strategy"
    assert slugify("Ünïcödé — test") == "unicode-test"
    assert slugify("") == "untitled"
    assert len(slugify("x" * 200)) == 60


def test_dir_name():
    assert dir_name("2026-10-29", VID, "Hello World") == f"2026-10-29_{VID}_hello-world"


def test_save_layout_and_index(tmp_path, sample):
    s = Store(tmp_path)
    d = s.save(_a(sample))
    assert d == tmp_path / "videos" / f"2026-10-29_{VID}_rsi-2-the-best-strategy"
    assert (d / "raw.json").exists() and (d / "digest.md").exists()
    assert load_analysis(d / "raw.json").video.id == VID
    lines = (tmp_path / "index.jsonl").read_text().splitlines()
    assert len(lines) == 1
    e = json.loads(lines[0])
    for k in ["id", "url", "title", "channel", "date", "path", "model", "schema_version", "usage"]:
        assert k in e
    assert e["path"] == f"videos/2026-10-29_{VID}_rsi-2-the-best-strategy"
    assert e["schema_version"] == "1.0"


def test_dedupe(tmp_path, sample):
    s = Store(tmp_path)
    assert not s.exists(VID)
    s.save(_a(sample))
    assert s.exists(VID)
    assert not s.exists("aaaaaaaaaaa")


def test_dedupe_does_not_confuse_ids(tmp_path, sample):
    s = Store(tmp_path)
    # A title whose slug looks like another video id must not count as that video.
    s.save(_a(sample, vid="abc_def-123", title="zzzzzzzzzzz"))
    s.index_path.unlink()  # check directory matching on its own
    assert s.exists("abc_def-123")
    assert not s.exists("zzzzzzzzzzz")
    assert not s.exists("bc_def-123x")


def test_resave_replaces(tmp_path, sample):
    s = Store(tmp_path)
    s.save(_a(sample, vid="aaaaaaaaaaa", title="Other"))
    s.save(_a(sample, date="2026-10-01", title="Old title"))
    s.save(_a(sample, date="2026-10-29", title="New title"))
    dirs = sorted(p.name for p in (tmp_path / "videos").iterdir())
    assert dirs == ["2026-10-29_aaaaaaaaaaa_other", f"2026-10-29_{VID}_new-title"]
    ids = [e.id for e in s.read_index()]
    assert sorted(ids) == ["aaaaaaaaaaa", VID]
