import pytest

from youtube_analyzer.urls import InvalidYouTubeURL, canonical_url, extract_video_id, normalize

VID = "dQw4w9WgXcQ"


@pytest.mark.parametrize(
    "url",
    [
        f"https://www.youtube.com/watch?v={VID}",
        f"https://youtube.com/watch?v={VID}",
        f"http://m.youtube.com/watch?v={VID}",
        f"https://music.youtube.com/watch?v={VID}&feature=share",
        f"www.youtube.com/watch?v={VID}",
        f"https://www.youtube.com/watch?v={VID}&t=123s",
        f"https://www.youtube.com/watch?v={VID}&t=1h2m3s",
        f"https://www.youtube.com/watch?t=45&v={VID}",
        f"https://www.youtube.com/watch?v={VID}&list=PLx0sYbCqOb8TBPRdmBHs5Iftvv9TPboYG&index=3",
        f"https://www.youtube.com/watch?list=PLx0sYbCqOb8TBPRdmBHs5Iftvv9TPboYG&v={VID}",
        f"https://youtu.be/{VID}",
        f"https://youtu.be/{VID}?t=42",
        f"https://youtu.be/{VID}?si=AbCdEfGh123&t=10",
        f"https://youtu.be/{VID}?list=PLx0sYbCqOb8TBPRdmBHs5Iftvv9TPboYG",
        f"https://www.youtube.com/shorts/{VID}",
        f"https://youtube.com/shorts/{VID}?feature=share",
        f"https://www.youtube.com/live/{VID}",
        f"https://www.youtube.com/live/{VID}?si=xyz&t=300",
        f"https://www.youtube.com/embed/{VID}?start=30",
        f"https://www.youtube-nocookie.com/embed/{VID}",
        f"https://www.youtube.com/v/{VID}",
        f"  https://www.youtube.com/watch?v={VID}  ",
        VID,
        f"https://www.youtube.com/attribution_link?u=/watch%3Fv%3D{VID}%26feature%3Dshare",
    ],
)
def test_extract_video_id(url):
    assert extract_video_id(url) == VID


def test_ids_with_dash_and_underscore():
    assert extract_video_id("https://youtu.be/a-b_c-d_e-f") == "a-b_c-d_e-f"


def test_normalize_strips_params():
    vid, canon = normalize(f"https://www.youtube.com/watch?v={VID}&t=99&list=PL123")
    assert vid == VID
    assert canon == f"https://www.youtube.com/watch?v={VID}"


@pytest.mark.parametrize(
    "url",
    [
        "",
        "not a url",
        "https://vimeo.com/123456",
        "https://evil.com/watch?v=dQw4w9WgXcQ",
        "https://youtube.com.evil.com/watch?v=dQw4w9WgXcQ",
        "https://www.youtube.com/watch?v=short",
        "https://www.youtube.com/playlist?list=PL123",
        "https://www.youtube.com/@channel",
        "https://youtu.be/",
        "javascript:alert(1)",
        "ftp://youtube.com/watch?v=dQw4w9WgXcQ",
    ],
)
def test_rejects(url):
    with pytest.raises(InvalidYouTubeURL):
        extract_video_id(url)


def test_canonical_rejects_bad_id():
    with pytest.raises(InvalidYouTubeURL):
        canonical_url("bad")
