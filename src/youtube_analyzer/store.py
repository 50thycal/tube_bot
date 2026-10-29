"""Output layout, index.jsonl and dedupe.

    <root>/videos/<YYYY-MM-DD>_<videoId>_<slug>/raw.json
    <root>/videos/<YYYY-MM-DD>_<videoId>_<slug>/digest.md
    <root>/index.jsonl
"""

from __future__ import annotations

import json
import re
import shutil
import unicodedata
from pathlib import Path

from .digest import render
from .schema import IndexEntry, VideoAnalysis

VIDEOS_DIR = "videos"
INDEX_FILE = "index.jsonl"


def slugify(text: str, max_len: int = 60) -> str:
    s = unicodedata.normalize("NFKD", text or "").encode("ascii", "ignore").decode()
    s = re.sub(r"[^a-zA-Z0-9]+", "-", s).strip("-").lower()
    s = s[:max_len].rstrip("-")
    return s or "untitled"


def dir_name(date: str, video_id: str, title: str) -> str:
    return f"{date}_{video_id}_{slugify(title)}"


class Store:
    def __init__(self, root: Path | str):
        self.root = Path(root)
        self.videos = self.root / VIDEOS_DIR
        self.index_path = self.root / INDEX_FILE

    # -------------------------------------------------------------- index

    def read_index(self) -> list[IndexEntry]:
        if not self.index_path.exists():
            return []
        out = []
        for line in self.index_path.read_text(encoding="utf-8").splitlines():
            if line.strip():
                out.append(IndexEntry.model_validate_json(line))
        return out

    def _write_index(self, entries: list[IndexEntry]) -> None:
        self.index_path.write_text(
            "".join(e.model_dump_json() + "\n" for e in entries),
            encoding="utf-8",
        )

    # -------------------------------------------------------------- dedupe

    def existing_dirs(self, video_id: str) -> list[Path]:
        if not self.videos.exists():
            return []
        # Ids may contain '-' and '_', so match the id at its exact position
        # ("YYYY-MM-DD_" is 11 chars) rather than with a loose glob.
        n = len(video_id)
        return sorted(
            p
            for p in self.videos.iterdir()
            if p.is_dir() and p.name[11 : 11 + n] == video_id and p.name[11 + n : 12 + n] == "_"
        )

    def exists(self, video_id: str) -> bool:
        return bool(self.existing_dirs(video_id)) or any(e.id == video_id for e in self.read_index())

    def remove(self, video_id: str) -> None:
        for d in self.existing_dirs(video_id):
            shutil.rmtree(d)
        entries = self.read_index()
        kept = [e for e in entries if e.id != video_id]
        if len(kept) != len(entries):
            self._write_index(kept)

    # -------------------------------------------------------------- write

    def save(self, a: VideoAnalysis) -> Path:
        """Write raw.json + digest.md and upsert the index line. Returns the video dir."""
        date = a.run.analyzed_at[:10]
        self.remove(a.video.id)
        d = self.videos / dir_name(date, a.video.id, a.video.title)
        d.mkdir(parents=True, exist_ok=True)
        (d / "raw.json").write_text(a.model_dump_json(indent=2) + "\n", encoding="utf-8")
        (d / "digest.md").write_text(render(a), encoding="utf-8")

        entry = IndexEntry(
            id=a.video.id,
            url=a.video.url,
            title=a.video.title,
            channel=a.video.channel,
            date=date,
            path=d.relative_to(self.root).as_posix(),
            model=a.run.model,
            model_version=a.run.model_version,
            schema_version=a.schema_version,
            duration_s=a.video.duration_s,
            engine=a.run.engine,
            chunked=a.run.chunked,
            calls=a.run.calls,
            usage=a.run.usage,
        )
        entries = self.read_index() + [entry]
        self._write_index(entries)
        return d


def load_analysis(path: Path | str) -> VideoAnalysis:
    return VideoAnalysis.model_validate(json.loads(Path(path).read_text(encoding="utf-8")))
