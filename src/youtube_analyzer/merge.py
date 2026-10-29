"""Window planning and merging of per-window extractions."""

from __future__ import annotations

from .schema import ContentExtraction, Window
from .timestamps import fmt_ts, normalize_ts, parse_ts, sort_key

# Tolerance before we decide a window's timestamps are clip-relative.
_RELATIVE_SLACK_S = 30


def plan_windows(duration_s: int, window_s: int) -> list[Window]:
    if duration_s <= 0 or window_s <= 0:
        raise ValueError("duration_s and window_s must be positive")
    windows = []
    start = 0
    while start < duration_s:
        end = min(start + window_s, duration_s)
        windows.append(Window(start_s=start, end_s=end))
        start = end
    # Fold a tiny tail (< 1/4 window) into the previous window.
    if len(windows) > 1 and windows[-1].end_s - windows[-1].start_s < window_s // 4:
        tail = windows.pop()
        windows[-1] = Window(start_s=windows[-1].start_s, end_s=tail.end_s)
    return windows


def _all_ts(c: ContentExtraction) -> list[str]:
    out = []
    for s in c.segments:
        out += [s.start_ts, s.end_ts]
    out += [x.ts for x in c.claims] + [x.ts for x in c.visuals] + [x.ts for x in c.formulas]
    out += [x.ts for x in c.strategies] + [x.ts for x in c.open_questions]
    return out


def detect_offset(c: ContentExtraction, window: Window) -> int:
    """Return the shift to apply to this window's timestamps.

    The prompt asks for absolute timestamps, but models sometimes report time
    relative to the clip start. If most parseable timestamps fall before the
    window start, treat them as relative and shift by window.start_s.
    """
    if window.start_s == 0:
        return 0
    secs = [s for s in (parse_ts(t) for t in _all_ts(c)) if s is not None]
    if not secs:
        return 0
    before = sum(1 for s in secs if s < window.start_s - _RELATIVE_SLACK_S)
    return window.start_s if before * 2 > len(secs) else 0


def normalize_window(c: ContentExtraction, window: Window | None) -> ContentExtraction:
    """Return a copy with timestamps in canonical HH:MM:SS, absolute to the full video."""
    off = detect_offset(c, window) if window is not None else 0
    c = c.model_copy(deep=True)

    def n(ts: str) -> str:
        return normalize_ts(ts, off)

    for s in c.segments:
        s.start_ts, s.end_ts = n(s.start_ts), n(s.end_ts)
    for group in (c.claims, c.visuals, c.formulas, c.strategies, c.open_questions):
        for item in group:
            item.ts = n(item.ts)
    return c


def _key(name: str) -> str:
    return " ".join(name.lower().split())


def merge(parts: list[tuple[Window, ContentExtraction]]) -> ContentExtraction:
    """Merge normalized per-window extractions into one document.

    List sections are concatenated in time order. Strategies and tools are
    de-duplicated by name (first mention wins; later windows contribute extra
    rules/parameters/markets). The merged summary is the per-window summaries,
    labelled by window: deterministic, no extra LLM call.
    """
    parts = sorted(parts, key=lambda p: p[0].start_s)
    out = ContentExtraction(
        summary="",
        segments=[],
        claims=[],
        visuals=[],
        formulas=[],
        strategies=[],
        tools_and_data=[],
        open_questions=[],
    )
    summaries = []
    strategies: dict[str, object] = {}
    tools: dict[str, object] = {}
    seen_q: set[str] = set()

    for window, c in parts:
        if c.summary.strip():
            summaries.append(f"[{fmt_ts(window.start_s)}–{fmt_ts(window.end_s)}] {c.summary.strip()}")
        out.segments += c.segments
        out.claims += c.claims
        out.visuals += c.visuals
        out.formulas += c.formulas
        for q in c.open_questions:
            k = _key(q.assertion)
            if k not in seen_q:
                seen_q.add(k)
                out.open_questions.append(q)
        for s in c.strategies:
            k = _key(s.name)
            if k not in strategies:
                strategies[k] = s.model_copy(deep=True)
                continue
            m = strategies[k]
            for field in ("entry_rules", "exit_rules", "markets_assets"):
                cur = getattr(m, field)
                cur += [x for x in getattr(s, field) if x not in cur]
            names = {p.name for p in m.parameters}
            m.parameters += [p for p in s.parameters if p.name not in names]
            if s.stated_performance and s.stated_performance not in m.stated_performance:
                m.stated_performance = "; ".join(x for x in (m.stated_performance, s.stated_performance) if x)
            if s.costs_slippage_mentioned:
                m.costs_slippage_mentioned = True
                if s.costs_slippage_detail and s.costs_slippage_detail not in m.costs_slippage_detail:
                    m.costs_slippage_detail = "; ".join(
                        x for x in (m.costs_slippage_detail, s.costs_slippage_detail) if x
                    )
        for t in c.tools_and_data:
            k = _key(t.name)
            if k not in tools:
                tools[k] = t.model_copy(deep=True)
            elif t.how_used and t.how_used not in tools[k].how_used:
                tools[k].how_used = f"{tools[k].how_used}; {t.how_used}"

    out.summary = "\n\n".join(summaries)
    out.strategies = list(strategies.values())
    out.tools_and_data = list(tools.values())
    out.segments.sort(key=lambda s: sort_key(s.start_ts))
    for group in (out.claims, out.visuals, out.formulas, out.open_questions):
        group.sort(key=lambda x: sort_key(x.ts))
    return out
