import copy

import pytest

SAMPLE = {
    "summary": "A mean-reversion strategy on SPY using RSI(2), backtested 2010-2024.",
    "segments": [
        {"start_ts": "00:00:00", "end_ts": "00:02:10", "topic": "Intro", "key_points": ["Claims 72% win rate"]},
        {"start_ts": "00:02:10", "end_ts": "00:15:00", "topic": "Rules", "key_points": ["Buy when RSI(2) < 10"]},
    ],
    "claims": [
        {"ts": "00:01:05", "claim": "72% win rate", "evidence_shown": "backtest", "caveats": "no costs | pre-2020"},
    ],
    "visuals": [
        {
            "ts": "00:05:30",
            "type": "chart",
            "title": "Equity curve",
            "axes_or_columns": ["Date", "Equity ($)"],
            "values_readable": ["2024: $48,210", "Max DD: UNREADABLE"],
            "what_it_argues": "Steady growth",
            "confidence": "med",
        }
    ],
    "formulas": [
        {"ts": "00:07:00", "expression": "RSI = 100 - 100/(1+RS)", "variables": [{"symbol": "RS", "meaning": "avg gain / avg loss"}]}
    ],
    "strategies": [
        {
            "name": "RSI2 mean reversion",
            "ts": "00:02:10",
            "logic": "Buy short-term oversold dips in an uptrend",
            "entry_rules": ["Close > 200 SMA", "RSI(2) < 10"],
            "exit_rules": ["Close > 5 SMA"],
            "parameters": [{"name": "RSI period", "value": "2"}, {"name": "entry threshold", "value": "10"}],
            "markets_assets": ["SPY"],
            "stated_performance": "72% win rate, 9.1% CAGR",
            "costs_slippage_mentioned": False,
            "costs_slippage_detail": "",
        }
    ],
    "tools_and_data": [{"name": "TradingView", "type": "platform", "how_used": "charting"}],
    "open_questions": [{"ts": "00:12:00", "assertion": "Works on all ETFs", "missing_support": "Only SPY shown"}],
}


@pytest.fixture
def sample():
    return copy.deepcopy(SAMPLE)
