"""Deterministic Markdown rendering of a VideoAnalysis (no LLM call)."""

from __future__ import annotations

from .schema import VideoAnalysis
from .timestamps import fmt_ts, parse_ts


def _cell(s: str) -> str:
    """Make a string safe for a Markdown table cell."""
    return (s or "").replace("\\", "\\\\").replace("|", "\\|").replace("\r", "").replace("\n", "<br>")


def _ts_link(url: str, ts: str) -> str:
    sec = parse_ts(ts)
    if sec is None:
        return _cell(ts)
    return f"[{ts}]({url}&t={sec}s)"


def _table(headers: list[str], rows: list[list[str]]) -> list[str]:
    out = ["| " + " | ".join(headers) + " |", "|" + "|".join("---" for _ in headers) + "|"]
    out += ["| " + " | ".join(r) + " |" for r in rows]
    return out


def render(a: VideoAnalysis) -> str:
    v, r = a.video, a.run
    url = v.url
    L: list[str] = []
    L.append(f"# {v.title or v.id}")
    L.append("")
    meta = [
        f"**Channel:** {v.channel or 'unknown'}",
        f"**URL:** {url}",
        f"**Duration:** {fmt_ts(v.duration_s) if v.duration_s else 'unknown'}",
    ]
    L.append("  \n".join(meta))
    L.append("")
    L.append(
        f"<sub>schema {a.schema_version} · model {r.model}"
        + (f" ({r.model_version})" if r.model_version and r.model_version != r.model else "")
        + f" · analyzed {r.analyzed_at}"
        + (f" · {len(r.windows)} windows" if r.chunked else "")
        + (" · low-res" if r.low_res else "")
        + f" · {r.usage.total_tokens:,} tokens</sub>"
    )
    L.append("")

    L += ["## Summary", "", a.summary.strip() or "_none_", ""]

    L += ["## Segments", ""]
    if not a.segments:
        L += ["_none_", ""]
    for s in a.segments:
        L.append(f"### {_ts_link(url, s.start_ts)}–{s.end_ts} · {s.topic}")
        L.append("")
        L += [f"- {p}" for p in s.key_points] or ["_no key points_"]
        L.append("")

    L += ["## Claims", ""]
    if a.claims:
        L += _table(
            ["ts", "claim", "evidence", "caveats"],
            [[_ts_link(url, c.ts), _cell(c.claim), c.evidence_shown, _cell(c.caveats)] for c in a.claims],
        )
    else:
        L.append("_none_")
    L.append("")

    L += ["## Visuals", ""]
    if not a.visuals:
        L += ["_none_", ""]
    for vis in a.visuals:
        L.append(f"### {_ts_link(url, vis.ts)} · {vis.type} · {vis.title or 'untitled'} (confidence: {vis.confidence})")
        L.append("")
        if vis.axes_or_columns:
            L.append("**Axes / columns:** " + "; ".join(vis.axes_or_columns))
            L.append("")
        if vis.values_readable:
            L.append("**Values (as shown):**")
            L.append("")
            L += [f"- `{x}`" if "`" not in x else f"- {x}" for x in vis.values_readable]
            L.append("")
        L.append(f"**Argues:** {vis.what_it_argues or '_n/a_'}")
        L.append("")

    L += ["## Formulas", ""]
    if not a.formulas:
        L += ["_none_", ""]
    for f in a.formulas:
        L.append(f"- {_ts_link(url, f.ts)} `{f.expression}`" if "`" not in f.expression else f"- {_ts_link(url, f.ts)} {f.expression}")
        L += [f"  - `{var.symbol}`: {var.meaning}" for var in f.variables]
    if a.formulas:
        L.append("")

    L += ["## Strategies", ""]
    if not a.strategies:
        L += ["_none_", ""]
    for s in a.strategies:
        L.append(f"### {s.name}" + (f" ({_ts_link(url, s.ts)})" if s.ts else ""))
        L.append("")
        L.append(f"**Logic:** {s.logic or '_n/a_'}")
        L.append("")
        for label, items in (("Entry", s.entry_rules), ("Exit", s.exit_rules)):
            L.append(f"**{label} rules:**")
            L += [f"- {x}" for x in items] or ["- _none stated_"]
            L.append("")
        if s.parameters:
            L += _table(["parameter", "value"], [[_cell(p.name), _cell(p.value)] for p in s.parameters])
            L.append("")
        L.append(f"**Markets/assets:** {', '.join(s.markets_assets) or '_none stated_'}")
        L.append("")
        L.append(f"**Stated performance:** {s.stated_performance or '_none stated_'}")
        L.append("")
        costs = "yes" if s.costs_slippage_mentioned else "no"
        if s.costs_slippage_detail:
            costs += f" — {s.costs_slippage_detail}"
        L.append(f"**Costs/slippage mentioned:** {costs}")
        L.append("")

    L += ["## Tools & data", ""]
    if a.tools_and_data:
        L += _table(["name", "type", "how used"], [[_cell(t.name), t.type, _cell(t.how_used)] for t in a.tools_and_data])
    else:
        L.append("_none_")
    L.append("")

    L += ["## Open questions", ""]
    if a.open_questions:
        L += [f"- {_ts_link(url, q.ts)} **{q.assertion}** — {q.missing_support}" for q in a.open_questions]
    else:
        L.append("_none_")
    L.append("")
    return "\n".join(L)
