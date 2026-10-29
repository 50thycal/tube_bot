"""Timestamp helpers. Canonical form is HH:MM:SS."""

from __future__ import annotations

import re

_TS_RE = re.compile(r"^\s*(?:(\d+):)?(\d{1,2}):(\d{1,2})(?:\.\d+)?\s*$")


def parse_ts(ts: str) -> int | None:
    """'1:02:03' / '02:03' / '2:3' -> seconds. Returns None if unparseable."""
    if ts is None:
        return None
    m = _TS_RE.match(str(ts))
    if not m:
        return None
    h, mnt, s = m.groups()
    return int(h or 0) * 3600 + int(mnt) * 60 + int(s)


def fmt_ts(seconds: int) -> str:
    seconds = max(0, int(seconds))
    return f"{seconds // 3600:02d}:{seconds % 3600 // 60:02d}:{seconds % 60:02d}"


def normalize_ts(ts: str, offset_s: int = 0) -> str:
    """Reformat to HH:MM:SS (shifted by offset_s). Unparseable values pass through."""
    sec = parse_ts(ts)
    if sec is None:
        return ts
    return fmt_ts(sec + offset_s)


def sort_key(ts: str) -> tuple[int, int]:
    sec = parse_ts(ts)
    return (0, sec) if sec is not None else (1, 0)
