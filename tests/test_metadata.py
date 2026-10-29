import pytest

from youtube_analyzer import metadata
from youtube_analyzer.metadata import VideoUnavailable, parse_watch_page

URL = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"


def test_parse_watch_page_ok():
    html = '..."playabilityStatus":{"status":"OK","playableInEmbed":true}..."lengthSeconds":"1834",...'
    assert parse_watch_page(html) == (1834, "OK", "")


def test_parse_watch_page_age_gated():
    html = '"playabilityStatus":{"status":"LOGIN_REQUIRED","reason":"Sign in to confirm your age"}'
    assert parse_watch_page(html) == (None, "LOGIN_REQUIRED", "Sign in to confirm your age")


def test_parse_watch_page_nothing():
    assert parse_watch_page("<html></html>") == (None, None, "")


def _fake_get(responses):
    def get(url):
        for k, v in responses.items():
            if k in url:
                return v
        raise AssertionError(url)

    return get


def test_fetch_metadata(monkeypatch):
    monkeypatch.setattr(
        metadata,
        "_get",
        _fake_get({"oembed": (200, '{"title": "T", "author_name": "C"}'), "watch": (200, '"lengthSeconds":"60"')}),
    )
    m = metadata.fetch_metadata(URL)
    assert (m.title, m.channel, m.duration_s) == ("T", "C", 60)


def test_oembed_404_is_unavailable(monkeypatch):
    monkeypatch.setattr(metadata, "_get", _fake_get({"oembed": (404, "")}))
    with pytest.raises(VideoUnavailable):
        metadata.fetch_metadata(URL)


def test_oembed_401_degrades(monkeypatch):
    monkeypatch.setattr(metadata, "_get", _fake_get({"oembed": (401, ""), "watch": (200, "")}))
    m = metadata.fetch_metadata(URL)
    assert (m.title, m.duration_s) == ("", None)


def test_age_gated_raises(monkeypatch):
    page = '"playabilityStatus":{"status":"LOGIN_REQUIRED","reason":"Sign in to confirm your age"}'
    monkeypatch.setattr(metadata, "_get", _fake_get({"oembed": (200, '{"title":"T"}'), "watch": (200, page)}))
    with pytest.raises(VideoUnavailable, match="age-restricted"):
        metadata.fetch_metadata(URL)


def test_private_raises(monkeypatch):
    page = '"playabilityStatus":{"status":"LOGIN_REQUIRED","reason":"This video is private"}'
    monkeypatch.setattr(metadata, "_get", _fake_get({"oembed": (200, '{"title":"T"}'), "watch": (200, page)}))
    with pytest.raises(VideoUnavailable, match="private"):
        metadata.fetch_metadata(URL)


def test_bot_check_is_not_fatal(monkeypatch):
    page = '"playabilityStatus":{"status":"LOGIN_REQUIRED","reason":"Sign in to confirm you’re not a bot"}'
    monkeypatch.setattr(metadata, "_get", _fake_get({"oembed": (200, '{"title":"T"}'), "watch": (200, page)}))
    assert metadata.fetch_metadata(URL).duration_s is None


def test_network_error_degrades(monkeypatch):
    def boom(url):
        raise OSError("blocked")

    monkeypatch.setattr(metadata, "_get", boom)
    m = metadata.fetch_metadata(URL)
    assert (m.title, m.duration_s) == ("", None)
