"""End-to-end: URL -> metadata -> Gemini extraction (single pass or windowed) -> store."""

from __future__ import annotations

import logging
import os
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Callable

from . import __version__
from .gemini import CallResult, ExtractionFailed, GeminiExtractor, TooLong, resolve_model
from .merge import merge, normalize_window, plan_windows
from .metadata import Metadata, fetch_metadata
from .schema import ContentExtraction, RunInfo, Usage, VideoAnalysis, VideoInfo, Window
from .store import Store
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

    # Every request is kept to roughly one window of video: a ~30 min video sent
    # whole has been seen to run ~4.5 min server-side and then get dropped.
    window_s = _env_int("YTA_CHUNK_MINUTES", 20) * 60
    max_single_s = _env_int("YTA_SINGLE_PASS_MAX_MINUTES", 25) * 60
    duration = meta.duration_s
    if not duration:
        # The watch page is often a bot check on CI runners; ask Gemini instead (cheap: low res, 0.1 fps).
        try:
            probe = ex.probe_duration(canon)
            run.record(probe)
            duration = probe.content.duration_s if probe.content.duration_s > 0 else None
            log.info("probed duration: %ss", duration)
        except TooLong as e:
            run.record_failure(e)
            log.warning("duration probe failed (%s); trying a single pass", e)

    windows: list[Window] = []
    content: ContentExtraction | None = None
    chunk = bool(duration and duration > max_single_s)
    if chunk:
        log.info("duration %ss > %ss; extracting in %d-min windows", duration, max_single_s, window_s // 60)
    else:
        try:
            res = ex.extract(canon)
            run.record(res)
            content = normalize_window(res.content, None)
        except TooLong as e:
            run.record_failure(e)
            if not duration:
                raise ExtractionFailed(f"single pass failed ({e}) and video duration is unknown, so it cannot be chunked") from e
            log.warning("single pass too long (%s); falling back to %d-min windows", e, window_s // 60)
            chunk = True

    if chunk:
        parts: list[tuple[Window, ContentExtraction]] = []
        planned = plan_windows(duration, window_s)
        for i, w in enumerate(planned):
            parts += _extract_window(ex, canon, w, i, len(planned), run)
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


def _extract_window(
    ex: GeminiExtractor, url: str, w: Window, i: int, total: int, run: _Run
) -> list[tuple[Window, ContentExtraction]]:
    """Extract one window; if it is still too long, split it in half (down to MIN_WINDOW_S)."""
    log.info("window %d/%d %ss-%ss", i + 1, total, w.start_s, w.end_s)
    try:
        res = ex.extract(url, w, i, total)
    except TooLong as e:
        run.record_failure(e)
        span = w.end_s - w.start_s
        if span < 2 * MIN_WINDOW_S:
            raise
        mid = w.start_s + span // 2
        log.warning("window %ss-%ss too long; splitting at %ss", w.start_s, w.end_s, mid)
        return _extract_window(ex, url, Window(start_s=w.start_s, end_s=mid), i, total, run) + _extract_window(
            ex, url, Window(start_s=mid, end_s=w.end_s), i, total, run
        )
    run.record(res)
    return [(w, normalize_window(res.content, w))]
