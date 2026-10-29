"""End-to-end: URL -> metadata -> Gemini extraction (agentic, or static single pass / windows) -> store."""

from __future__ import annotations

import logging
import os
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Callable

from . import __version__
from .agentic import AgenticExtractor
from .gemini import CallResult, ExtractionFailed, GeminiExtractor, PastEnd, TooLong, resolve_model
from .merge import merge, normalize_window, plan_windows
from .metadata import Metadata, fetch_metadata
from .schema import ContentExtraction, RunInfo, Usage, VideoAnalysis, VideoInfo, Window
from .store import Store
from .timestamps import parse_ts
from .urls import normalize

log = logging.getLogger(__name__)

# Floor for halving a dropped window. Must be well under the default window
# (7 min) or windows could never be split (a 5-min floor made 7-min windows unsplittable).
MIN_WINDOW_S = 2 * 60


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
    engine: str | None = None,
    extractor: GeminiExtractor | None = None,
    agentic_extractor: AgenticExtractor | None = None,
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
    run = _Run()
    # Agentic is opt-in: on the first live video it failed 3/3 ("There was a problem
    # processing your request", 0 tokens) with and without response_format.
    engine = engine or os.environ.get("YTA_ENGINE") or "static"
    if engine not in ("agentic", "static"):
        raise ValueError(f"unknown engine {engine!r} (agentic|static)")
    duration = meta.duration_s
    windows: list[Window] = []
    chunk = False
    content: ContentExtraction | None = None

    if engine == "agentic":
        # One call over the whole video; the model navigates the timeline itself.
        ag = agentic_extractor or AgenticExtractor(model=model)
        try:
            res = ag.extract(canon)
            run.record(res)
            if res.variant and res.variant != "response_format":
                engine = f"agentic:{res.variant}"
            content = normalize_window(res.content, None)
            duration = duration or _last_segment_end([content])
        except ExtractionFailed as e:
            run.record_failure(e)
            log.warning("agentic extraction failed (%s); falling back to static windows", e)
            engine = "static"

    if content is None:
        ex = extractor or GeminiExtractor(model=model, low_res=low_res)
        content, windows, chunk, duration = _static_extract(ex, canon, duration, run)

    analysis = VideoAnalysis(
        **content.model_dump(),
        video=VideoInfo(id=video_id, url=canon, title=meta.title, channel=meta.channel, duration_s=duration),
        run=RunInfo(
            model=model,
            model_version=run.model_version,
            analyzed_at=now().strftime("%Y-%m-%dT%H:%M:%SZ"),
            low_res=low_res,
            engine=engine,
            chunked=chunk,
            windows=windows,
            calls=run.calls,
            usage=run.usage,
            tool_version=__version__,
        ),
    )
    path = store.save(analysis)
    return Result(status="created", video_id=video_id, path=path, analysis=analysis)


def _last_segment_end(contents: list[ContentExtraction]) -> int | None:
    ends = [parse_ts(s.end_ts) for c in contents for s in c.segments]
    return max((e for e in ends if e is not None), default=None)


def _static_extract(
    ex: GeminiExtractor, canon: str, duration: int | None, run: _Run
) -> tuple[ContentExtraction, list[Window], bool, int | None]:
    """generate_content over the URL: one pass for short videos, else clipped windows.

    Every request is kept to about one window of video: the server drops requests
    still processing after ~255-270 s, and a video of unknown length is never sent
    whole (even a low-res full-video probe was dropped).
    """
    # Live success rate by window length: 5 min 4/4, 7.5 min 6/6 (<=249 s),
    # 10 min 0/2, 15 min 1/6 (the rest dropped at ~255-270 s).
    window_s = _env_int("YTA_CHUNK_MINUTES", 7) * 60
    max_single_s = _env_int("YTA_SINGLE_PASS_MAX_MINUTES", 7) * 60
    max_windows = _env_int("YTA_MAX_WINDOWS", 16)

    if duration and duration <= max_single_s:
        try:
            res = ex.extract(canon)
            run.record(res)
            return normalize_window(res.content, None), [], False, duration
        except TooLong as e:
            run.record_failure(e)
            log.warning("single pass too long (%s); falling back to %d-min windows", e, window_s // 60)

    if duration:
        planned = plan_windows(duration, window_s)
        log.info("duration %ss: %d windows of %d min", duration, len(planned), window_s // 60)
        parts: list[tuple[Window, ContentExtraction]] = []
        for i, w in enumerate(planned):
            parts += _extract_window(ex, canon, w, i, len(planned), run)
    else:
        log.info("duration unknown: walking %d-min windows until the video ends", window_s // 60)
        parts = _walk_windows(ex, canon, window_s, max_windows, run)
        duration = _last_segment_end([c for _, c in parts])
        if duration:  # trim the last window to where the video actually ends
            parts = [(Window(start_s=w.start_s, end_s=min(w.end_s, max(duration, w.start_s + 1))), c) for w, c in parts]
    if not parts:
        raise ExtractionFailed("no window returned any video content")
    return merge(parts), [w for w, _ in parts], True, duration


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
