"""`yta` command line."""

from __future__ import annotations

import argparse
import logging
import sys
from pathlib import Path

from dotenv import load_dotenv

from . import __version__
from .digest import render
from .gemini import ExtractionFailed, QuotaExhausted, TooLong
from .metadata import VideoUnavailable
from .store import load_analysis
from .urls import InvalidYouTubeURL


def _build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="yta", description="Structured extraction of YouTube videos via Gemini.")
    p.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    p.add_argument("-v", "--verbose", action="store_true")
    sub = p.add_subparsers(dest="cmd", required=True)

    a = sub.add_parser("analyze", help="analyze a YouTube URL")
    a.add_argument("url")
    a.add_argument("--force", action="store_true", help="re-analyze even if already in index")
    a.add_argument("--model", help="Gemini model id (default: $YTA_MODEL or built-in default)")
    a.add_argument("--low-res", action="store_true", help="low media resolution (static engine; ~3x fewer video tokens)")
    a.add_argument(
        "--engine",
        choices=["agentic", "static"],
        help="static: generate_content over clipped windows (default); "
        "agentic: one Interactions API call, model navigates the video (experimental, falls back to static) "
        "(default: $YTA_ENGINE or static)",
    )
    a.add_argument("--root", default=".", help="output root containing videos/ and index.jsonl (default: .)")

    r = sub.add_parser("render", help="re-render digest.md from a raw.json (no API call)")
    r.add_argument("raw_json")
    return p


def main(argv: list[str] | None = None) -> int:
    load_dotenv()
    args = _build_parser().parse_args(argv)
    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(levelname)s %(name)s: %(message)s",
    )
    # The SDK's HTTP client is chatty at INFO.
    logging.getLogger("httpx").setLevel(logging.WARNING)

    if args.cmd == "render":
        raw = Path(args.raw_json)
        out = raw.with_name("digest.md")
        out.write_text(render(load_analysis(raw)), encoding="utf-8")
        print(out)
        return 0

    from .pipeline import analyze

    try:
        res = analyze(args.url, args.root, force=args.force, model=args.model, low_res=args.low_res, engine=args.engine)
    except InvalidYouTubeURL as e:
        print(f"error: {e}", file=sys.stderr)
        return 2
    except VideoUnavailable as e:
        print(f"error: video unavailable: {e}", file=sys.stderr)
        return 3
    except QuotaExhausted as e:
        print(f"error: {e}", file=sys.stderr)
        return 5
    except (TooLong, ExtractionFailed) as e:
        print(f"error: extraction failed: {e}", file=sys.stderr)
        return 4

    if res.status == "skipped":
        print(f"skipped: {res.video_id} already analyzed (use --force to redo)")
        return 0
    a = res.analysis
    u = a.run.usage
    print(f"created: {res.path}")
    print(
        f"engine={a.run.engine} model={a.run.model} version={a.run.model_version or '?'} calls={a.run.calls} "
        f"chunked={a.run.chunked} tokens: prompt={u.prompt_tokens} output={u.output_tokens} "
        f"thinking={u.thinking_tokens} total={u.total_tokens}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
