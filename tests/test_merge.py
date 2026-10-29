import pytest

from youtube_analyzer.merge import detect_offset, merge, normalize_window, plan_windows
from youtube_analyzer.schema import ContentExtraction, Window
from youtube_analyzer.timestamps import fmt_ts, normalize_ts, parse_ts


@pytest.mark.parametrize("ts,sec", [("00:00:00", 0), ("1:02:03", 3723), ("02:03", 123), ("2:3", 123), ("00:01:05.5", 65), ("abc", None), ("", None)])
def test_parse_ts(ts, sec):
    assert parse_ts(ts) == sec


def test_fmt_and_normalize():
    assert fmt_ts(3723) == "01:02:03"
    assert normalize_ts("5:00", 1200) == "00:25:00"
    assert normalize_ts("n/a", 1200) == "n/a"


def test_plan_windows():
    assert plan_windows(3000, 1200) == [Window(start_s=0, end_s=1200), Window(start_s=1200, end_s=2400), Window(start_s=2400, end_s=3000)]
    # tiny tail folds into previous window
    assert plan_windows(2500, 1200) == [Window(start_s=0, end_s=1200), Window(start_s=1200, end_s=2500)]
    assert plan_windows(600, 1200) == [Window(start_s=0, end_s=600)]


def _content(sample, shift_to=None):
    c = ContentExtraction.model_validate(sample)
    return c


def test_detect_relative_timestamps(sample):
    c = ContentExtraction.model_validate(sample)  # all ts within 00:00-00:15
    assert detect_offset(c, Window(start_s=1200, end_s=2400)) == 1200
    assert detect_offset(c, Window(start_s=0, end_s=1200)) == 0


def test_absolute_timestamps_left_alone(sample):
    c = normalize_window(ContentExtraction.model_validate(sample), Window(start_s=1200, end_s=2400))
    assert c.claims[0].ts == "00:21:05"
    again = normalize_window(c, Window(start_s=1200, end_s=2400))
    assert again.claims[0].ts == "00:21:05"  # already absolute: not shifted twice


def test_merge_windows(sample):
    w1, w2 = Window(start_s=0, end_s=1200), Window(start_s=1200, end_s=2400)
    a = normalize_window(ContentExtraction.model_validate(sample), w1)
    s2 = ContentExtraction.model_validate(sample).model_dump()
    s2["summary"] = "Part two."
    s2["strategies"][0]["exit_rules"] = ["Close > 5 SMA", "Time stop 10 days"]
    s2["strategies"][0]["parameters"].append({"name": "time stop", "value": "10 days"})
    s2["strategies"][0]["costs_slippage_mentioned"] = True
    s2["strategies"][0]["costs_slippage_detail"] = "$0.005/share"
    s2["tools_and_data"][0]["how_used"] = "alerts"
    b = normalize_window(ContentExtraction.model_validate(s2), w2)

    m = merge([(w2, b), (w1, a)])  # out of order on purpose
    assert m.summary.startswith("[00:00:00–00:20:00] A mean-reversion")
    assert "[00:20:00–00:40:00] Part two." in m.summary
    assert [s.start_ts for s in m.segments] == ["00:00:00", "00:02:10", "00:20:00", "00:22:10"]
    assert [c.ts for c in m.claims] == ["00:01:05", "00:21:05"]
    assert len(m.visuals) == 2 and len(m.formulas) == 2
    assert len(m.strategies) == 1
    st = m.strategies[0]
    assert st.exit_rules == ["Close > 5 SMA", "Time stop 10 days"]
    assert [p.name for p in st.parameters] == ["RSI period", "entry threshold", "time stop"]
    assert st.costs_slippage_mentioned and st.costs_slippage_detail == "$0.005/share"
    assert len(m.tools_and_data) == 1 and m.tools_and_data[0].how_used == "charting; alerts"
    assert len(m.open_questions) == 1  # same assertion de-duplicated
