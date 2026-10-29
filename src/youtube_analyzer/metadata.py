"""Video metadata without an API key.

- title/channel: YouTube oEmbed.
- duration + playability: best-effort scrape of the public watch page
  (`lengthSeconds`, `playabilityStatus`). YouTube may serve a consent or bot
  page to datacenter IPs; every failure here degrades to "unknown" rather than
  aborting the run.
"""

from __future__ import annotations

import json
import logging
import re
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass

log = logging.getLogger(__name__)

_UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130 Safari/537.36"
_TIMEOUT = 15


class VideoUnavailable(RuntimeError):
    """Video is private, removed, age-gated, or otherwise not analyzable."""


@dataclass
class Metadata:
    title: str = ""
    channel: str = ""
    duration_s: int | None = None


def _get(url: str) -> tuple[int, str]:
    req = urllib.request.Request(url, headers={"User-Agent": _UA, "Accept-Language": "en-US,en;q=0.9"})
    try:
        with urllib.request.urlopen(req, timeout=_TIMEOUT) as resp:
            return resp.status, resp.read().decode("utf-8", errors="replace")
    except urllib.error.HTTPError as e:
        return e.code, ""


def fetch_oembed(canonical: str) -> tuple[str, str]:
    """Return (title, channel). Raises VideoUnavailable on 404 (missing/private)."""
    url = "https://www.youtube.com/oembed?" + urllib.parse.urlencode({"url": canonical, "format": "json"})
    try:
        status, body = _get(url)
    except (urllib.error.URLError, TimeoutError, OSError) as e:
        log.warning("oEmbed request failed (%s); continuing without title", e)
        return "", ""
    if status == 404:
        raise VideoUnavailable(f"{canonical}: not found, removed, or private (oEmbed 404)")
    if status != 200:
        # 401/403 = embedding disabled or private. Gemini will give the final word.
        log.warning("oEmbed returned HTTP %s; continuing without title", status)
        return "", ""
    data = json.loads(body)
    return data.get("title", ""), data.get("author_name", "")


_LENGTH_RE = re.compile(r'"lengthSeconds"\s*:\s*"(\d+)"')
_PLAYABILITY_RE = re.compile(r'"playabilityStatus"\s*:\s*\{\s*"status"\s*:\s*"([A-Z_]+)"(?:\s*,\s*"reason"\s*:\s*"([^"]*)")?')
_BLOCKING_STATUSES = {"LOGIN_REQUIRED", "UNPLAYABLE", "ERROR", "AGE_CHECK_REQUIRED", "CONTENT_CHECK_REQUIRED"}


def parse_watch_page(html: str) -> tuple[int | None, str | None, str]:
    """Return (duration_s, playability_status, reason) from watch-page HTML."""
    m = _LENGTH_RE.search(html)
    duration = int(m.group(1)) if m else None
    p = _PLAYABILITY_RE.search(html)
    if not p:
        return duration, None, ""
    return duration, p.group(1), p.group(2) or ""


def fetch_watch_page(canonical: str) -> int | None:
    """Return duration in seconds, or None if unknown.

    Raises VideoUnavailable when the page explicitly says the video is private,
    age-restricted or unplayable.
    """
    try:
        status, html = _get(canonical)
    except (urllib.error.URLError, TimeoutError, OSError) as e:
        log.warning("watch page request failed (%s); duration unknown", e)
        return None
    if status != 200 or not html:
        log.warning("watch page returned HTTP %s; duration unknown", status)
        return None
    duration, play_status, reason = parse_watch_page(html)
    if play_status in _BLOCKING_STATUSES:
        # A bot-check page also reports LOGIN_REQUIRED ("Sign in to confirm you're
        # not a bot"); that is about our IP, not the video, so don't treat it as fatal.
        if "bot" in reason.lower():
            log.warning("watch page served a bot check; duration unknown")
            return None
        hint = " (age-restricted)" if "age" in reason.lower() or play_status == "AGE_CHECK_REQUIRED" else ""
        raise VideoUnavailable(f"{canonical}: {play_status}{hint}: {reason or 'video not playable'}")
    return duration


def fetch_metadata(canonical: str) -> Metadata:
    title, channel = fetch_oembed(canonical)
    duration = fetch_watch_page(canonical)
    return Metadata(title=title, channel=channel, duration_s=duration)
