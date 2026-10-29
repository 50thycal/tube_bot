"""End-to-end: URL -> metadata -> Gemini extraction (single pass or windowed) -> store."""

from __future__ import annotations

import logging
import os
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Callable

from . import __version__
from .gemini import CallResult, ExtractionFailed, GeminiExtractor, PastEnd, TooLong, resolve_model
from .merge import merge, normalize_window, plan_windows
from .metadata import Metadata, fetch_metadata
from .schema import ContentExtraction, RunInfo, Usage, VideoAnalysis, VideoInfo, Window
from .store import Store
from .timestamps import parse_ts
from .urls import normalize

log = logging.getLogger(__name__)

MIN_WINDOW_S = 5 * 60


def _env_int(name: str, default: int) -> int:
    v = os.environ.get(name)
    return int(v) if v else default


@dataclass
class Result:
    status: str  # "created" | "skipped"
    video_id: str
    path: Path | None = None
    analysis: VideoAnalysis | None = None


@dataclass
class _Run:
    usage: Usage = field(default_factory=Usage)
    calls: int = 0
    model_version: str = ""

    def record(self, res: CallResult) -> None:
        self.usage = self.usage.add(res.usage)
        self.calls += 1
        self.model_version = res.model_version or self.model_version

    def record_failure(self, e: Exception) -> None:
        u = getattr(e, "usage", None)
        if u is not None:
            self.usage = self.usage.add(u)
            self.calls += 1


def analyze(
    url: str,
    root: Path | str = ".",
    *,
    force: bool = False,
    model: str | None = None,
    low_res: bool = False,
    extractor: GeminiExtractor | None = None,
    metadata_fetcher: Callable[[str], Metadata] = fetch_metadata,
    now: Callable[[], datetime] = lambda: datetime.now(timezone.utc),
) -> Result:
    video_id, canon = normalize(url)
    store = Store(root)
    if store.exists(video_id) and not force:
        log.info("%s already analyzed; skipping (use --force to redo)", video_id)
        return Result(status="skipped", video_id=video_id)

    meta = metadata_fetcher(canon)
    model = resolve_model(model)
    ex = extractor or GeminiExtractor(model=model, low_res=low_res)
    run = _Run()

    # Every request is kept to roughly one window of video. Observed: whole-video
    # requests (even a low-res duration probe) were dropped by the server after
    # ~4.5 min, so a video of unknown length is never sent whole.
    window_s = _env_int("YTA_CHUNK_MINUTES", 15) * 60
    max_single_s = _env_int("YTA_SINGLE_PASS_MAX_MINUTES", 20) * 60
    max_windows = _env_int("YTA_MAX_WINDOWS", 16)
    duration = meta.duration_s

    windows: list[Window] = []
    content: ContentExtraction | None = None
    chunk = True
    if duration and duration <= max_single_s:
        try:
            res = ex.extract(canon)
            run.record(res)
            content = normalize_window(res.content, None)
            chunk = False
        except TooLong as e:
            run.record_failure(e)
            log.warning("single pass too long (%s); falling back to %d-min windows", e, window_s // 60)

    if chunk:
        if duration:
            planned = plan_windows(duration, window_s)
            log.info("duration %ss: %d windows of %d min", duration, len(planned), window_s // 60)
            parts: list[tuple[Window, ContentExtraction]] = []
            for i, w in enumerate(planned):
                parts += _extract_window(ex, canon, w, i, len(planned), run)
        else:
            log.info("duration unknown: walking %d-min windows until the video ends", window_s // 60)
            parts = _walk_windows(ex, canon, window_s, max_windows, run)
            ends = [parse_ts(s.end_ts) for _, c in parts for s in c.segments]
            duration = max((e for e in ends if e is not None), default=None)
        if not parts:
            raise ExtractionFailed("no window returned any video content")
        windows = [w for w, _ in parts]
        content = merge(parts)

    analysis = VideoAnalysis(
        **content.model_dump(),
        video=VideoInfo(id=video_id, url=canon, title=meta.title, channel=meta.channel, duration_s=duration),
        run=RunInfo(
            model=model,
            model_version=run.model_version,
            analyzed_at=now().strftime("%Y-%m-%dT%H:%M:%SZ"),
            low_res=low_res,
            chunked=chunk,
            windows=windows,
            calls=run.calls,
            usage=run.usage,
            tool_version=__version__,
        ),
    )
    path = store.save(analysis)
    return Result(status="created", video_id=video_id, path=path, analysis=analysis)


def _walk_windows(
    ex: GeminiExtractor, url: str, window_s: int, max_windows: int, run: _Run
) -> list[tuple[Window, ContentExtraction]]:
    """Extract consecutive windows from 0:00 until the model reports the video has ended."""
    parts: list[tuple[Window, ContentExtraction]] = []
    for i in range(max_windows):
        w = Window(start_s=i * window_s, end_s=(i + 1) * window_s)
        got = _extract_window(ex, url, w, i, None, run)
        parts += got
        if not got or any(getattr(c, "video_ended_in_clip", False) for _, c in got):
            return parts
    log.warning("stopped after YTA_MAX_WINDOWS=%d windows; video may be longer", max_windows)
    return parts


def _extract_window(
    ex: GeminiExtractor, url: str, w: Window, i: int, total: int | None, run: _Run
) -> list[tuple[Window, ContentExtraction]]:
    """Extract one window, dropping it if it lies past the end of the video.

    If it is still too long, split it in half (down to MIN_WINDOW_S).
    """
    log.info("window %d/%s %ss-%ss", i + 1, total or "?", w.start_s, w.end_s)
    try:
        res = ex.extract(url, w, i, total)
    except PastEnd as e:
        log.info("window %ss-%ss is past the end of the video (%s)", w.start_s, w.end_s, e)
        return []
    except TooLong as e:
        run.record_failure(e)
        span = w.end_s - w.start_s
        if span < 2 * MIN_WINDOW_S:
            raise
        mid = w.start_s + span // 2
        log.warning("window %ss-%ss too long; splitting at %ss", w.start_s, w.end_s, mid)
        first = _extract_window(ex, url, Window(start_s=w.start_s, end_s=mid), i, total, run)
        if not first or any(getattr(c, "video_ended_in_clip", False) for _, c in first):
            return first
        return first + _extract_window(ex, url, Window(start_s=mid, end_s=w.end_s), i, total, run)
    run.record(res)
    if not getattr(res.content, "clip_has_video", True):
        log.info("window %ss-%ss has no video (past the end)", w.start_s, w.end_s)
        return []
    return [(w, normalize_window(res.content, w))]
