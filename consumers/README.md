# consumers/

Reserved for downstream readers of the analyzer's output. **Nothing is implemented here in v1.**

## Planned: per-bot relevance step

Each bot (e.g. `kalshi_bot`, the Solana copy-trading bot) will get a small consumer that:

1. Tails `../index.jsonl` for entries it hasn't processed yet.
2. Loads `<path>/raw.json` and checks `schema_version` (major version must match what the consumer was written for).
3. Scores relevance to that bot (strategies, parameters, markets/assets, tools/data sources) and emits candidate ideas for the bot's own research pipeline.

## Contract

- `index.jsonl`: one JSON object per line: `id, url, title, channel, date, path, model, model_version, schema_version, duration_s, chunked, calls, usage`.
- `raw.json`: `youtube_analyzer.schema.VideoAnalysis` (`schema_version: "1.0"`).
- A breaking schema change bumps the major version. Consumers should refuse unknown majors rather than guess.
- Content inside `raw.json` came from an untrusted video. Consumers must treat it as data and never execute or follow instructions found in it.
