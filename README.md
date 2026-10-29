# youtube-analyzer (`yta`)

Give it a YouTube URL and it produces a structured, schema-validated extraction of the video: spoken content, on-screen text, charts and tables, formulas, strategy parameters, and the tools and data sources mentioned.

The extractor is Gemini. Gemini accepts a public YouTube URL directly as a `file_data` part, so nothing is downloaded (no yt-dlp) and YouTube's datacenter-IP bot checks don't get in the way. Output uses Gemini structured output (`response_schema` built from Pydantic models), so every `raw.json` is valid against the schema.

v1 is extraction only. There are no bot integrations and no second LLM pass.

## Setup

```bash
python -m venv .venv && source .venv/bin/activate
pip install -e '.[dev]'
cp .env.example .env     # then set GEMINI_API_KEY (https://aistudio.google.com/apikey)
pytest
```

| env var | default | purpose |
|---|---|---|
| `GEMINI_API_KEY` | required | Gemini API key (`.env` locally, repo secret in Actions) |
| `YTA_MODEL` | `gemini-3.8-flash` | Gemini model id. The default is the current Flash model in Google's video-understanding docs and cookbook. |
| `YTA_CHUNK_MINUTES` | `20` | window size for long videos |
| `YTA_SINGLE_PASS_TOKEN_BUDGET` | `600000` | estimated input tokens above which a video is chunked up front |
| `YTA_MAX_OUTPUT_TOKENS` | model max | cap on output tokens |

## CLI

```bash
yta analyze <url> [--force] [--model X] [--low-res] [--root DIR]
yta render videos/<dir>/raw.json      # re-render digest.md, no API call
```

- Accepts `watch?v=`, `youtu.be/`, `/shorts/`, `/live/`, `/embed/`, `m.`/`music.` hosts, a bare 11-character id, and URLs with `&t=`, `&list=`, `&index=` or `?si=` (those params are stripped). Only the canonical `https://www.youtube.com/watch?v=<id>` is sent to Gemini.
- Results are deduplicated on video id: an already-analyzed video is skipped unless you pass `--force`, which replaces its directory and its index line.
- `--low-res` sets `MEDIA_RESOLUTION_LOW`, which uses about 3x fewer video tokens. Use it for talking-head videos; skip it when small chart labels matter.
- Exit codes: `0` ok/skipped, `2` bad URL, `3` video unavailable (private, age-gated or removed), `4` extraction failed.

## Output

```
videos/<YYYY-MM-DD>_<videoId>_<slug>/
  raw.json     # full schema-validated extraction (VideoAnalysis, schema_version "1.0")
  digest.md    # deterministic human-readable render of raw.json
index.jsonl    # one line per video
```

Each `index.jsonl` line has these fields: `id, url, title, channel, date, path, model, model_version, schema_version, duration_s, chunked, calls, usage{prompt_tokens, output_tokens, thinking_tokens, total_tokens}`.

### Schema (`src/youtube_analyzer/schema.py`, v1.0)

- `video`: id, url, title, channel (from YouTube oEmbed, no key needed), duration_s (best-effort from the watch page)
- `summary`: the video's thesis in a short paragraph
- `segments[]`: start_ts, end_ts, topic, key_points[]
- `claims[]`: ts, claim, evidence_shown (`none|anecdote|backtest|live_results|data`), caveats
- `visuals[]`: ts, type (`chart|table|code|slide|diagram|screen`), title, axes_or_columns[], values_readable[], what_it_argues, confidence (`high|med|low`)
- `formulas[]`: ts, expression, variables[{symbol, meaning}]
- `strategies[]`: name, ts, logic, entry_rules[], exit_rules[], parameters[{name, value}], markets_assets[], stated_performance, costs_slippage_mentioned, costs_slippage_detail
- `tools_and_data[]`: name, type (`api|library|dataset|platform|other`), how_used
- `open_questions[]`: ts, assertion, missing_support
- `run`: model, model_version (what Gemini actually served), analyzed_at, low_res, chunked, windows[], calls, usage

Timestamps are absolute `HH:MM:SS`. Values on visuals are transcribed exactly as shown. Anything unreadable is written as `UNREADABLE` with low confidence, and values are never estimated.

## How long videos are handled

1. If the duration is known and the estimated input tokens (duration × ~300 tok/s, or ~100 at low res) exceed `YTA_SINGLE_PASS_TOKEN_BUDGET`, the video is chunked up front.
2. Otherwise one request covers the whole video. If it fails on input length, or the output is truncated (`MAX_TOKENS`), the run falls back to chunking. When the duration is unknown, a cheap low-res probe fetches it first.
3. Chunking uses `video_metadata` start/end offsets in ~20-minute windows, with one structured extraction per window. A window that is still too long is split in half, down to 5 minutes.
4. The windows are merged. Timestamps stay absolute: if the model reported clip-relative times, they are detected and shifted. Lists are concatenated in time order, strategies and tools are deduplicated by name, and the summary is the per-window summaries labelled by window (deterministic, no extra LLM call).

Retries: HTTP 408/429/5xx get exponential backoff with jitter, up to 5 retries. Private, age-gated and removed videos fail with a clear error, raised from oEmbed, the watch page's `playabilityStatus`, or Gemini's own error.

## GitHub Action

`.github/workflows/analyze.yml` runs `yta analyze` and commits `videos/` and `index.jsonl` back to the repo. Runs are serialized so index commits never race.

Setup: add the **`GEMINI_API_KEY`** repository secret (Settings → Secrets and variables → Actions). You can optionally add a `YTA_MODEL` repository variable.

Triggers (both only work once the workflow is on the default branch):

- **workflow_dispatch**: Actions → *analyze* → *Run workflow* → paste the URL. Optional `force`, `low_res` and `model` inputs. This also works from the GitHub mobile app.
- **repository_dispatch**: `event_type: analyze`.

  ```bash
  curl -X POST https://api.github.com/repos/50thycal/tube_bot/dispatches \
    -H "Authorization: Bearer $GITHUB_TOKEN" \
    -H "Accept: application/vnd.github+json" \
    -d '{"event_type":"analyze","client_payload":{"url":"https://youtu.be/VIDEO_ID"}}'
  ```

  `client_payload` also accepts `"force": "true"` and `"low_res": "true"`.

`ci.yml` runs `pytest` on pushes to main and on PRs.

### iOS Shortcut (share sheet → analyze)

1. Create a fine-grained PAT that covers only this repository, with **Contents: Read and write** permission. That is the permission `repository_dispatch` needs.
2. In Shortcuts, create a new shortcut and enable **Show in Share Sheet**, accepting **URLs** and **Text**.
3. Add a **Get Contents of URL** action:
   - URL: `https://api.github.com/repos/50thycal/tube_bot/dispatches`
   - Method: `POST`
   - Headers: `Authorization: Bearer <PAT>`, `Accept: application/vnd.github+json`
   - Request Body (JSON): `event_type` = `analyze`, `client_payload` (Dictionary) → `url` = *Shortcut Input*
4. Optionally, add **Show Notification** with the text "Queued".

In the YouTube app, tap Share → *your shortcut*. A successful dispatch returns HTTP 204, and the commit shows up a few minutes later.

## Cost and limits

These figures come from Google's docs at the time of writing; check the current [pricing](https://ai.google.dev/gemini-api/docs/pricing) and [video docs](https://ai.google.dev/gemini-api/docs/video-understanding).

- Video tokens are roughly **~300 tokens/s** at default resolution (1 fps frames plus audio) and **~100 tokens/s** at low resolution. A 30-minute video is ~540k input tokens at default and ~180k at low res. Cost ≈ input tokens × the model's input price + output and thinking tokens × the output price. Every run records the actual usage in `raw.json` and `index.jsonl`.
- YouTube URL input supports **public videos only**. Private videos and some restricted (age-gated or region-locked) videos fail. The free tier caps the amount of YouTube video per day (8 h at the time of writing), and the paid tier has no such cap.
- Long videos cost proportionally more. `--low-res` is the main cost lever.

## Security

Video content is untrusted input. Transcripts and on-screen text are stored as data only. Nothing in the pipeline executes, follows, or acts on instructions found in the video. The system prompt tells the model to treat such instructions as content, and the output is constrained to a fixed schema. See the note at the top of `src/youtube_analyzer/prompt.py`. The Action passes inputs through env vars (no `${{ }}` interpolation into shell), and the URL is re-validated and canonicalized before use.

## Layout

```
src/youtube_analyzer/
  urls.py        URL → video id → canonical URL
  metadata.py    oEmbed title/channel, watch-page duration/playability
  prompt.py      system + task prompts (security note lives here)
  schema.py      Pydantic schema (versioned)
  gemini.py      Gemini calls, structured output, retries, error mapping
  merge.py       window planning, timestamp normalization, merge
  digest.py      raw.json → digest.md
  store.py       videos/ layout, index.jsonl, dedupe
  pipeline.py    orchestration
  cli.py         `yta`
consumers/       reserved for per-bot relevance steps (not implemented)
```
