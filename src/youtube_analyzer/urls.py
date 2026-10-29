"""YouTube URL parsing.

Every accepted input is reduced to an 11-char video id and re-emitted as a
canonical watch URL. Timestamps (t=, start=), playlist params (list=, index=)
and tracking params (si=, feature=, pp=) are dropped. Only the canonical URL
is ever passed downstream, so arbitrary user-supplied URLs never reach Gemini.
"""

from __future__ import annotations

import re
from urllib.parse import parse_qs, urlparse

VIDEO_ID_RE = re.compile(r"^[A-Za-z0-9_-]{11}$")

_HOSTS = {
    "youtube.com",
    "www.youtube.com",
    "m.youtube.com",
    "music.youtube.com",
    "youtube-nocookie.com",
    "www.youtube-nocookie.com",
}
_SHORT_HOSTS = {"youtu.be", "www.youtu.be"}
# Path prefixes whose next segment is the video id.
_PATH_PREFIXES = ("shorts", "live", "embed", "v", "e")


class InvalidYouTubeURL(ValueError):
    pass


def extract_video_id(url: str) -> str:
    """Return the 11-char video id for any supported YouTube URL form.

    Accepts a bare id too. Raises InvalidYouTubeURL otherwise.
    """
    raw = (url or "").strip()
    if VIDEO_ID_RE.match(raw):
        return raw
    if "://" not in raw:
        raw = "https://" + raw

    parsed = urlparse(raw)
    if parsed.scheme not in ("http", "https"):
        raise InvalidYouTubeURL(f"unsupported scheme: {url!r}")
    host = (parsed.hostname or "").lower()
    segments = [s for s in parsed.path.split("/") if s]

    candidate: str | None = None
    if host in _SHORT_HOSTS:
        candidate = segments[0] if segments else None
    elif host in _HOSTS:
        if segments[:1] == ["watch"]:
            candidate = parse_qs(parsed.query).get("v", [None])[0]
        elif len(segments) >= 2 and segments[0] in _PATH_PREFIXES:
            candidate = segments[1]
        elif segments[:1] == ["attribution_link"]:
            # /attribution_link?u=/watch%3Fv%3D<id>%26feature%3Dshare
            inner = parse_qs(parsed.query).get("u", [""])[0]
            return extract_video_id("https://www.youtube.com" + inner)
    else:
        raise InvalidYouTubeURL(f"not a YouTube URL: {url!r}")

    if candidate and VIDEO_ID_RE.match(candidate):
        return candidate
    raise InvalidYouTubeURL(f"could not find a video id in: {url!r}")


def canonical_url(video_id: str) -> str:
    if not VIDEO_ID_RE.match(video_id):
        raise InvalidYouTubeURL(f"invalid video id: {video_id!r}")
    return f"https://www.youtube.com/watch?v={video_id}"


def normalize(url: str) -> tuple[str, str]:
    """Return (video_id, canonical_url)."""
    vid = extract_video_id(url)
    return vid, canonical_url(vid)
