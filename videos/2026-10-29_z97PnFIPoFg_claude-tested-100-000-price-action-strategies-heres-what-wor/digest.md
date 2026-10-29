# Claude Tested 100,000 Price Action Strategies (Here’s What Works)

**Channel:** AI Pathways  
**URL:** https://www.youtube.com/watch?v=z97PnFIPoFg  
**Duration:** 00:17:10

<sub>schema 1.0 · model gemini-3.8-flash · analyzed 2026-10-29T04:19:13Z · 2 windows · 114,299 tokens</sub>

## Summary

[00:00:00–00:15:00] The video presents an extensive quantitative backtest of over 101,000 algorithmic variations of classical price action trading concepts across five years of 1-minute futures data (NQ and ES), covering 327 million simulated executions. By testing 10 core price action setups across parameters including timeframe, touches, confirmation, and stop-loss mechanisms, the presenter tests standard retail trading beliefs against rigorous out-of-sample data with realistic transaction costs and slippage. The findings indicate that most price action setups fail or lose edge on lower timeframes (e.g., 1-minute), high touch counts degrade level reliability, and close-based stops increase losses. Only about 8% of tested variations cleared a Sharpe ratio of 0.5+, with the most robust edge found in a 4-hour 'Change of Character' (CHoCH) reversal without requiring a liquidity sweep.

[00:15:00–00:22:30] In this concluding segment, the speaker highlights that mean reversion is the consistent winning pattern across massive testing batches (including 9,000 previous strategy variations, ICT sweeps, and price action 4-hour change-of-character setups). He presents a five-prompt framework for viewers to replicate and automate the complete price action backtesting lab using Claude or ChatGPT, covering data cleaning, the simulation engine with slippage and commissions, multi-stage filtering funnels, out-of-sample testing, and an HTML results dashboard.

## Segments

### [00:00:00](https://www.youtube.com/watch?v=z97PnFIPoFg&t=0s)–00:01:05 · Introduction and Experiment Overview

- Tested over 100,000 price action concepts using Claude to build an automated testing system.
- Dataset spans nearly 5 years of 1-minute bars on NQ (Nasdaq) and ES (S&P 500) futures, comprising over 300 million simulated trades.
- Goal is to replace anecdotal trading claims with empirical, quantitative evidence.
- Presenter background: studied math and economics at UCLA, worked in investment banking at Raymond James for over 3 years, spent 2 years building trading systems.

### [00:01:05](https://www.youtube.com/watch?v=z97PnFIPoFg&t=65s)–00:03:59 · Core Price Action Concepts and the Ten Tested Setups

- Price action relies purely on chart mechanics rather than external technical indicators.
- Defined key mechanics: levels (support/resistance), trend (break of structure / higher highs and higher lows), change of character (reversal below higher low), liquidity sweep, confirmation candles, and stop/target placement.
- Outlined the ten primary setups tested: 1. Level bounce, 2. Breakout, 3. Flip zone, 4. Trend pullback, 5. Trend line, 6. Break of structure, 7. Change of character, 8. Sweep and reclaim, 9. Supply and demand, 10. Fair value gap.
- Noted that 'change of character' held up best across all tests, while 'sweeps' reversed only about half the time on their own.

### [00:03:59](https://www.youtube.com/watch?v=z97PnFIPoFg&t=239s)–00:06:59 · Backtesting Methodology and The Gauntlet

- Traditional price action is subjective ('drawn by eye'), so testing requires parameterizing visual rules into explicit dials.
- Dials tested: touches, line vs zone, confirmation, stop placement, target placement, chart timeframe, and contextual filters, representing 20.3 trillion theoretical combinations.
- Executed 101,345 total variations: 40,000 parameter-spread tests (4,000 per setup) plus 61,345 common/retail setting combinations.
- Used 5 years (3.6 million 1-minute bars) of NQ and ES futures data across 327 million simulated executions.
- The evaluation gauntlet enforced real trading costs, slippage on every stop, treat ambiguous within-bar high/low hits as full losses, comparison against random lines and random trades, cross-validation on ES, and a 2-year locked out-of-sample dataset.

### [00:06:59](https://www.youtube.com/watch?v=z97PnFIPoFg&t=419s)–00:07:52 · Funnel Results and Win Rate vs Profitability

- Funnel results on NQ discovery data: 101,345 tested; 88,986 had >=30 trades; 24,879 were profitable after transaction costs; 8,310 achieved a Sharpe ratio of 0.5+ (~8% of total).
- Examined the claim of 80%+ win rates: 138 variations achieved >=80% win rate, but across all 40,000 runs, win rate had only a 0.27 correlation to net profit.
- 67 of the 138 high-win-rate strategies relied on a small 1R target.

### [00:07:52](https://www.youtube.com/watch?v=z97PnFIPoFg&t=472s)–00:08:29 · Timeframe Performance and Cost Drag

- Trading friction heavily penalizes lower timeframes: costs consume 46.0% of gross profit on the 1-minute chart, compared to 3.9% on the daily chart.
- Percentage of profitable versions increases monotonically with timeframe: 9% on 1m, 32% on 5m, 36% on 15m, 44% on 1h, 47% on 4h, and 48% on daily.
- Median annual performance remains negative across all baseline timeframes (-$306 to -$428), emphasizing that higher timeframes reduce cost drag rather than providing an automatic edge without setup selection.

### [00:08:29](https://www.youtube.com/watch?v=z97PnFIPoFg&t=509s)–00:10:11 · Level Testing, Touch Count, and Flip Zones

- Real horizontal support/resistance levels held 51.1% of the time, beating random lines (42.4%) by +8.7 points on NQ and +8.5 points on ES.
- The popular belief that 'more touches equal stronger levels' failed: 1-touch levels outperformed random by +9.0 points, while 4 touches outperformed by only +6.1 points.
- Levels with 3+ touches bounced less (19.2% vs 20.5%) and broke through more often (27.8% vs 26.1%).
- Flip zones (old resistance becoming support after a break) was the strongest level concept, holding 11.5 percentage points better than random lines on NQ and 10.9 points on ES.

### [00:10:11](https://www.youtube.com/watch?v=z97PnFIPoFg&t=611s)–00:11:19 · Trend Setups, Confirmation, and Stop Mechanics

- Trend continuation concepts alone showed negative follow-through: break of structure (-0.04 ATR) and change of character (-0.05 ATR).
- Among trend trade setups, only Change of Character (CHoCH) reversal generated a positive median outcome (+$61), whereas BOS continuation (-$328), sweep and reclaim (-$368), and trendlines (-$478) lost money.
- CHoCH performed best without requiring a preceding sweep (+$903 without sweep vs -$834 with sweep).
- Waiting for a candle confirmation gave up 4.3 points of entry price but added +$719 in annual edge by avoiding falling knives.
- Close-based stops underperformed hard stops, costing $132 more per year due to tail losses despite a higher win rate (40% vs 29%).

### [00:11:19](https://www.youtube.com/watch?v=z97PnFIPoFg&t=679s)–00:13:15 · Contextual Filters, Out-of-Sample Results, and Final Performance

- Trading only during New York session hours (8am - 4pm ET) added +$270/year; skipping trades into a 3+ day run added +$246/year; daily trend agreement filter hurt by -$587/year.
- The 4-hour CHoCH setup was the only setup to pass all tests across both NQ and ES in both initial discovery and the locked out-of-sample window.
- Out-of-sample 2-year locked test (covering a 22.5% market drawdown and a 74.5% rally): 4-hour CHoCH made +$62,179 on 1 NQ contract and +$39,284 on ES (61 trades on NQ, 54% win rate).
- 39 of 48 versions of the 4h setup were profitable on NQ; 66% of common versions were profitable on NQ and 54.5% on ES.

### [00:13:15](https://www.youtube.com/watch?v=z97PnFIPoFg&t=795s)–00:15:00 · Summary of Surviving Rules and Trade Example

- Seven surviving rules: 1. 4-hour CHoCH, 2. Higher timeframe charts, 3. New York session only, 4. Skip trades into 3+ day runs, 5. Confirmation candle on NQ, 6. Hard stop instead of close-based stop, 7. No sweep requirement before reversal.
- Walkthrough of an actual trade example from July 11, 2024 on NQ 4-hour.
- Observed recurring theme across prior research: mean reversion and fading exhaustion consistently outperform trend-following breakout concepts.

### [00:15:00](https://www.youtube.com/watch?v=z97PnFIPoFg&t=900s)–00:15:56 · Core Finding: Mean Reversion Across Large-Scale Tests

- Across 9,000 strategy variations tested previously, mean reversion was the only strategy type that held up.
- In ICT testing, fading the liquidity sweep held up, which is also a mean reversion style strategy.
- The price action test found that the 4-hour change of character (reversal setup) held up, reinforcing that mean reversion is the foundational trading dynamic.
- All reported results reflect the floor rather than the ceiling, based on a single contract per trade averaged across versions without custom position sizing or risk management.

### [00:15:56](https://www.youtube.com/watch?v=z97PnFIPoFg&t=956s)–00:16:49 · The Five Prompts to Build the Testing Lab

- Viewers are given 5 prompt templates to copy into LLMs (like Claude or ChatGPT) to build the identical test infrastructure layer by layer.
- Prompt 1 (Data and dials): Ingests 1-minute NQ and ES futures data, back-adjusts bars, handles news filters (CPI, jobs, FOMC), formats multiple timeframes (5m, 15m, 1h, 4h, daily), and defines dial combinations.
- Prompt 2 (Engine and level tests): Implements the execution engine ($4 commission per round trip, 1 tick slippage, $20/pt for NQ, $50/pt for ES), unit tests, and bootstrap behavioral validation against randomized levels.
- Prompt 3 (The funnel): Screens tens of thousands of rule variations on discovery data requiring at least 30 trades, positive P&L, Sharpe ratio >= 0.5, beating random trades, and transferability to ES.
- Prompt 4 (The final test): Evaluates surviving versions strictly on locked, sealed out-of-sample data.
- Prompt 5 (The dashboard): Compiles results, charts, and provenance logs into a standalone HTML dashboard.

### [00:16:49](https://www.youtube.com/watch?v=z97PnFIPoFg&t=1009s)–00:17:10 · Outro and Community Resources

- Encourages traders to codify discretionary 'feel' into rules and test them at scale.
- Prompts viewers to like, comment, subscribe, and access links for community and 1-on-1 calls.

## Claims

| ts | claim | evidence | caveats |
|---|---|---|---|
| [00:02:27](https://www.youtube.com/watch?v=z97PnFIPoFg&t=147s) | Liquidity sweeps reverse only about half the time on their own, meaning they have no edge as standalone entry signals. | backtest | Can serve as contextual information or a secondary filter, but not as an isolated trigger. |
| [00:07:05](https://www.youtube.com/watch?v=z97PnFIPoFg&t=425s) | Only approximately 8% of price action strategy variations achieve a Sharpe ratio of 0.5 or better after accounting for transaction costs. | backtest | Tested on NQ discovery dataset over 101,345 variations. |
| [00:07:47](https://www.youtube.com/watch?v=z97PnFIPoFg&t=467s) | Win rate has a very weak correlation with overall profitability in price action trading. | data | Correlation coefficient between win rate and net profit was measured at 0.27 across 40,000 strategies. |
| [00:08:06](https://www.youtube.com/watch?v=z97PnFIPoFg&t=486s) | Transaction costs consume nearly half of gross profits on 1-minute price action trading, whereas they account for less than 4% on daily charts. | backtest | Assumes standard futures commission and fixed slippage model per trade. |
| [00:08:43](https://www.youtube.com/watch?v=z97PnFIPoFg&t=523s) | Real price action support and resistance levels hold significantly better than random benchmark lines. | backtest | Real levels held 51.1% of touches versus 42.4% for random lines across 5m to daily timeframes. |
| [00:09:01](https://www.youtube.com/watch?v=z97PnFIPoFg&t=541s) | Levels that are touched more frequently do not become stronger; multiple touches actually decrease the likelihood of a bounce. | backtest | Levels with 3+ touches bounced 19.2% vs 20.5% for single touch, and broke through 27.8% vs 26.1%. |
| [00:09:53](https://www.youtube.com/watch?v=z97PnFIPoFg&t=593s) | Flip zones (resistance turning into support and vice versa) provide the highest statistical edge among level-based concepts. | backtest | Held 11.5 percentage points better than random on NQ and 10.9 percentage points better on ES on first retest. |
| [00:10:30](https://www.youtube.com/watch?v=z97PnFIPoFg&t=630s) | Requiring a liquidity sweep before trading a change of character significantly degrades net profitability. | backtest | In out-of-sample testing, CHoCH without sweep generated +$903/year vs -$834/year when requiring a sweep. |
| [00:10:46](https://www.youtube.com/watch?v=z97PnFIPoFg&t=646s) | Waiting for a candle confirmation at a level produces higher net edge than entering immediately with a limit order. | backtest | Gives up an average of 4.3 points of entry price but added $719 in net edge per year on NQ. |
| [00:11:12](https://www.youtube.com/watch?v=z97PnFIPoFg&t=672s) | Close-based stops underperform standard hard stops because rare large runaway candles create excessive losses. | backtest | Close-based stops achieved a higher win rate (40% vs 29%) but lost $132/year more on average. |
| [00:15:01](https://www.youtube.com/watch?v=z97PnFIPoFg&t=901s) | Mean reversion was the only strategy type that held up across 9,000 tested strategy variations. | data | Reflects systematic automated rules tested on futures data. |
| [00:15:08](https://www.youtube.com/watch?v=z97PnFIPoFg&t=908s) | In ICT methodology testing, fading the sweep was the only setup version that held up. | data | Categorized specifically as a mean-reversion archetype. |
| [00:15:26](https://www.youtube.com/watch?v=z97PnFIPoFg&t=926s) | When price stretches too high or too low, mean reversion is the primary baseline tendency. | anecdote |  |

## Visuals

### [00:00:29](https://www.youtube.com/watch?v=z97PnFIPoFg&t=29s) · slide · How We Tested It (confidence: high)

**Axes / columns:** THE DIALS; WHAT WE RAN; THE DATA; THE GAUNTLET

**Values (as shown):**

- `touches`
- `line or zone`
- `confirmation`
- `stop`
- `target`
- `chart`
- `filters`
- `20.3 trillion possible versions`
- `40,000 spread across every dial, 4,000 per setup`
- `61,345 common versions: usual settings, 0 to 2 filters`
- `101,345 total`
- `THE NAMED VERSIONS: Bare Minimum, Checklist, Entry Model, Zone System, Sweep System, Daily Version`
- `5 years, 3.6M 1-minute bars, NQ + ES, 327M simulated trades`
- `real costs, every trade`
- `slippage on every stop`
- `ambiguous candle = a loss`
- `vs random lines`
- `vs random trades`
- `checked on ES`
- `2 years locked away`

**Argues:** Summarizes the rigorous quantitative framework used to parameterize and test over 101,000 versions of price action across multi-million trade datasets.

### [00:00:37](https://www.youtube.com/watch?v=z97PnFIPoFg&t=37s) · diagram · The Ten Setups (confidence: high)

**Axes / columns:** Setup Name; Description

**Values (as shown):**

- `1 Level bounce: buy support, sell resistance`
- `2 Breakout: trade the close through a level`
- `3 Flip zone: old resistance becomes support`
- `4 Trend pullback: buy the first dip in an uptrend`
- `5 Trend line: buy a touch of the rising line`
- `6 Break of structure: go with the break of the last swing`
- `7 Change of character: the first break against the trend`
- `8 Sweep and reclaim: a wick through a low, closed back above`
- `9 Supply and demand: the first return to an impulse's base`
- `10 Fair value gap: the first return into a three-candle gap`

**Argues:** Displays the ten standard retail price action patterns that were programmatically codified and tested.

### [00:01:05](https://www.youtube.com/watch?v=z97PnFIPoFg&t=65s) · chart · The Price Action Setup (confidence: high)

**Axes / columns:** X: Time; Y: Price; Timeframes: 1m, 5m, 15m, 1h, 4h, daily

**Values (as shown):**

- `1 level: beat random lines, 5m to daily`
- `2 trend: no follow-through, any chart`
- `3 change of character: best setup, on the 4h`
- `4 sweep: reversed about half the time`
- `5 confirmation: beat a limit at the level (NQ)`
- `6 stop and target: hard stop beat close-based, target size: no edge`
- `break of structure`
- `higher chart, more versions made money`

**Argues:** Annotates an exemplary price chart with the six core price action components and indicates which ones empirical backtesting validated.

### [00:04:12](https://www.youtube.com/watch?v=z97PnFIPoFg&t=252s) · chart · Drawn By Eye (confidence: high)

**Axes / columns:** X: Time (NQ 15m, Jul 7, 2023); Y: Price (16,050 to 16,300)

**Values (as shown):**

- `Trader A: limit at the touch`
- `Trader B: close back across`
- `AS RULES: Level: 2+ swings within 0.25 ATR`
- `Touch: within 0.25 ATR of the level`
- `Confirmation: a close back across it`

**Argues:** Shows how subjective charting causes different traders to draw different support levels and enter differently, necessitating objective mathematical rules.

### [00:06:59](https://www.youtube.com/watch?v=z97PnFIPoFg&t=419s) · chart · Funnel (confidence: high)

**Axes / columns:** Stage; Count of versions

**Values (as shown):**

- `All: 101,345`
- `Enough trades to grade (30+): 88,986`
- `Profitable: 24,879`
- `Sharpe 0.5+: 8,310`
- `24,879 of the 101,345 versions made money after costs in discovery, and 8,310 had a Sharpe of 0.5+`

**Argues:** Demonstrates the step-by-step attrition rate of price action strategies from theoretical existence down to those with acceptable risk-adjusted returns.

### [00:07:24](https://www.youtube.com/watch?v=z97PnFIPoFg&t=444s) · chart · Win Rate And Profit (confidence: high)

**Axes / columns:** X: WIN RATE (0% to 100%); Y: Profit per contract per year (-$20k to $30k)

**Values (as shown):**

- `138 WIN 80%+`
- `0.27 CORRELATION`
- `67 of the 138 use a 1R target`
- `138 strategies won 80%+ of their trades; across all 40,000 win rate barely tracks profit (correlation 0.27)`
- `Targets: 5R, 4R, 3R, 2R, Next, 2R, 1.5R, 1R`

**Argues:** Shows a scatter plot demonstrating that high win rate is not strongly correlated with net profitability in price action systems.

### [00:07:52](https://www.youtube.com/watch?v=z97PnFIPoFg&t=472s) · chart · Timeframes (confidence: high)

**Axes / columns:** Category; 1m; 5m; 15m; 1h; 4h; Daily

**Values (as shown):**

- `PROFITABLE VERSIONS: 1m: 9%, 5m: 32%, 15m: 36%, 1h: 44%, 4h: 47%, Daily: 48%`
- `COSTS / GROSS PROFIT: 1m: 46%, 5m: 38%, 15m: 34%, 1h: 24%, 4h: 7%, Daily: 4%`
- `MEDIAN PER YEAR: 1m: -$306, 5m: -$310, 15m: -$310, 1h: -$428, 4h: -$428, Daily: -$306`
- `46.0% COSTS ON 1M`
- `3.9% COSTS ON DAILY`
- `Costs take 46.0% of gross profit on the 1m chart and 3.9% on daily`

**Argues:** Illustrates how trading costs destroy profitability on low timeframes, while higher timeframes produce far higher proportions of profitable strategies.

### [00:08:29](https://www.youtube.com/watch?v=z97PnFIPoFg&t=509s) · chart · Random Lines (confidence: high)

**Axes / columns:** Timeframe (All, 5m, 15m, 1h, 4h, Daily); Share of touches that hold (%)

**Values (as shown):**

- `All: Real 51%, Random 42%`
- `5m: Real 52%, Random 43%`
- `15m: Real 50%, Random 43%`
- `1h: Real 48%, Random 40%`
- `4h: Real 47%, Random 39%`
- `Daily: Real 51%, Random 33%`
- `+8.7 pts NQ`
- `+8.5 pts ES`
- `SURVIVED: Real levels hold 51.1% of touches against 42.4% for random lines, on every chart from 5m to daily`

**Argues:** Validates that horizontal support and resistance levels hold significantly better than randomly placed lines across all analyzed timeframes.

### [00:08:50](https://www.youtube.com/watch?v=z97PnFIPoFg&t=530s) · chart · Touch Count (confidence: high)

**Axes / columns:** Touches (1 touch, 2 touches, 3 touches, 4 touches); Points better than random lines

**Values (as shown):**

- `1 touch: +9.0 pts`
- `2 touches: +7.8 pts`
- `3 touches: +8.2 pts`
- `4 touches: +6.1 pts`
- `DIDN'T SURVIVE: A level touched four times held no better than a level touched once; levels touched 3+ times bounced a bit less and broke through a bit more`
- `3+ touches vs 1 touch: bounced 19.2% vs 20.5%, broke and kept going 27.8% vs 26.1%`

**Argues:** Disproves the conventional trading rule that support/resistance levels become stronger as touch count increases.

### [00:09:42](https://www.youtube.com/watch?v=z97PnFIPoFg&t=582s) · chart · Level Rules (confidence: high)

**Axes / columns:** Rule; Percentage points, 95% intervals (-2 to +12)

**Values (as shown):**

- `Touch count: -1.1 pts`
- `Wall at 3+ touches: -1.3 pts`
- `Weaker pushes: +0.4 pts`
- `Box vs line: +0.5 pts`
- `Flip zones: +11.5 pts`
- `+11.5 pts FLIP ZONES NQ`
- `+10.9 pts FLIP ZONES ES`
- `Flip zones hold; touch count, walls and weaker pushes do not`

**Argues:** Demonstrates that flip zones provide massive statistical edge over random benchmarks, while touch counts and walls actively detract performance.

### [00:10:11](https://www.youtube.com/watch?v=z97PnFIPoFg&t=611s) · chart · Follow-Through (confidence: high)

**Axes / columns:** Setup; Follow-through in ATR (-0.20 to +0.40)

**Values (as shown):**

- `Break of structure: -0.04 ATR`
- `Change of character: -0.05 ATR`
- `DIDN'T SURVIVE: Neither break moved price on its own`

**Argues:** Shows that structural trend breaks do not possess standalone directional momentum without further criteria.

### [00:10:18](https://www.youtube.com/watch?v=z97PnFIPoFg&t=618s) · chart · Trend Setups (confidence: high)

**Axes / columns:** Setup; Median result ($)

**Values (as shown):**

- `BOS continuation: -$328`
- `CHoCH reversal: +$61`
- `Sweep and reclaim: -$368`
- `Trend line: -$478`
- `+$61 CHOCH MEDIAN`
- `Only the change of character had a positive median`

**Argues:** Compares trend setups and shows CHoCH reversal is the only concept with a positive median return.

### [00:10:22](https://www.youtube.com/watch?v=z97PnFIPoFg&t=622s) · chart · Trend Trades As Taught (confidence: high)

**Axes / columns:** Trade variation; Performance ($)

**Values (as shown):**

- `Trend line, first to second low: -$586`
- `Reversal flip: -$417`
- `Sweep, then change: -$834`
- `Change, no sweep needed: +$903`
- `Late entry on a 5m break: -$2,608`
- `+$903 NO SWEEP, UNSEEN`
- `-$834 AFTER A SWEEP`
- `Only the change of character without a sweep made money`

**Argues:** Shows that entering a change of character without waiting for a prior sweep is profitable, whereas waiting for a sweep loses money.

### [00:10:34](https://www.youtube.com/watch?v=z97PnFIPoFg&t=634s) · chart · Confirmation Tax (confidence: high)

**Axes / columns:** Method; Result ($)

**Values (as shown):**

- `Limit at the touch: -$1,093`
- `After confirmation: -$373`
- `+$719 EDGE PER YEAR`
- `4.3 POINTS GIVEN UP`
- `SURVIVED: Waiting for confirmation lost less than a limit at the touch`

**Argues:** Demonstrates that waiting for a confirmation candle gives up 4.3 points of price but gains $719 in edge per year over limit orders at the touch.

### [00:10:59](https://www.youtube.com/watch?v=z97PnFIPoFg&t=659s) · chart · Stops (confidence: high)

**Axes / columns:** Stop type; Result ($)

**Values (as shown):**

- `Hard stop: -$158`
- `Close-based stop: -$290`
- `-$132 CLOSE STOPS, PER YEAR`
- `DIDN'T SURVIVE: Close-based stops cost $132 a year more`

**Argues:** Demonstrates that waiting for a candle close to exit a stop-loss costs more net money due to runaway candles.

### [00:11:19](https://www.youtube.com/watch?v=z97PnFIPoFg&t=679s) · chart · Context (confidence: high)

**Axes / columns:** Context filter; Impact on edge ($)

**Values (as shown):**

- `New York only (8am to 4pm ET): +$270`
- `Skip 3+ day runs: +$246`
- `Daily trend agrees: -$587`
- `+$270 NEW YORK ONLY, UNSEEN NQ`
- `-$587 DAILY TREND, UNSEEN NQ`
- `New York hours and skipping 3+ day runs helped. The daily trend filter hurt`

**Argues:** Shows that session filtering and mean-reversion filters increase edge, while higher-timeframe trend alignment degrades performance.

### [00:11:29](https://www.youtube.com/watch?v=z97PnFIPoFg&t=689s) · slide · Passed On Both Markets (confidence: high)

**Axes / columns:** Market (NQ, ES); Category (Original 40,000, Common Versions); Setup; Return/Year

**Values (as shown):**

- `NQ Original 40,000: change of character 1h (+$1,208), change of character 4h (+$4,025)`
- `NQ Common Versions: change of character 4h (+$4,884), flip zone daily (+$9,093)`
- `ES Original 40,000: change of character 4h (+$4,146)`
- `ES Common Versions: change of character 4h (+$3,374), breakout daily (+$1,734)`
- `4 of 4: CHOCH 4H PASSED IN EACH SET AND ON EACH MARKET`
- `Only the 4h change of character passed on both markets`

**Argues:** Identifies 4h Change of Character as the unique robust setup passing all tests across both NQ and ES assets.

### [00:11:55](https://www.youtube.com/watch?v=z97PnFIPoFg&t=715s) · chart · Final Window (confidence: high)

**Axes / columns:** X: Year (2025 to 2026); Y: Index points (17,232 to 30,078)

**Values (as shown):**

- `Peak: 22,235`
- `Trough: 17,232`
- `End: 30,078`
- `-22.5% SELLOFF`
- `+74.5% RALLY`
- `The locked years held a 22.5% drop and a 74.5% rally`

**Argues:** Demonstrates the severe two-sided market conditions contained in the 2-year out-of-sample locked test window.

### [00:12:02](https://www.youtube.com/watch?v=z97PnFIPoFg&t=722s) · chart · Timeframe Ladder (confidence: high)

**Axes / columns:** Timeframe (1m, 5m, 15m, 1h, 4h, Daily); Share of versions profitable (%)

**Values (as shown):**

- `1m: 9.2%`
- `5m: 20.3%`
- `15m: 28.8%`
- `1h: 37.7%`
- `4h: 45.1%`
- `Daily: 47.9%`
- `9% MADE MONEY, 1M, NQ`
- `45% MADE MONEY, 4H, NQ`
- `The higher the chart, the more versions made money`

**Argues:** Proves across out-of-sample data that higher timeframes consistently yield higher strategy success rates.

### [00:12:31](https://www.youtube.com/watch?v=z97PnFIPoFg&t=751s) · chart · Best Version (confidence: high)

**Axes / columns:** X: Year (2023, 2024, 2025, 2026); Y: Cumulative Profit ($0 to $300k)

**Values (as shown):**

- `+$62,179 LOCKED YEARS`
- `+$62,179 LOCKED YEARS, NQ`
- `+$39,284 LOCKED YEARS, ES`
- `61 trades on NQ, 54% winners`
- `Picked in discovery, it made money on both markets in the locked years`

**Argues:** Displays the cumulative equity curve of the 4h Change of Character strategy, highlighting out-of-sample profitability on both NQ and ES.

### [00:13:06](https://www.youtube.com/watch?v=z97PnFIPoFg&t=786s) · slide · The 4h Setup (confidence: high)

**Axes / columns:** Metric; Value

**Values (as shown):**

- `39 of 48 versions on its usual settings made money, NQ`
- `66% of all 314 common versions made money, NQ`
- `+$17,041 New York session versions, average per contract (original 40,000, NQ); still made money without their 10 best days`
- `54.5% of the common versions made money on ES`
- `In the original 40,000, most of the gain came from a few big days`

**Argues:** Provides robustness statistics for the 4-hour CHoCH setup across multiple variations and out-of-sample data.

### [00:13:16](https://www.youtube.com/watch?v=z97PnFIPoFg&t=796s) · slide · What Survived (confidence: high)

**Axes / columns:** Rule Number; Description

**Values (as shown):**

- `1 Change of character, 4h chart`
- `2 Higher charts: made money: 9% on 1m, 48% on daily (common versions, unseen NQ)`
- `3 New York session only`
- `4 Skip trades into a 3+ day run`
- `5 Confirmation candle (NQ)`
- `6 Hard stop, not close-based`
- `7 No sweep before the change`

**Argues:** Summarizes the final seven validated principles that survived the complete multi-stage test.

### [00:14:22](https://www.youtube.com/watch?v=z97PnFIPoFg&t=862s) · chart · Example Trade (confidence: high)

**Axes / columns:** X: Time (NQ 4h, July 11, 2024); Y: Price (19,800 to 21,000)

**Values (as shown):**

- `Trend`
- `Change of character`
- `Stop`
- `Entry`
- `Target`

**Argues:** Illustrates the exact execution of a surviving 4h CHoCH short trade setup on NQ from July 2024.

### [00:14:50](https://www.youtube.com/watch?v=z97PnFIPoFg&t=890s) · slide · What We Keep Finding (confidence: high)

**Axes / columns:** Study; Finding

**Values (as shown):**

- `9,000 strategies: mean reversion`
- `ICT: fading the sweep`
- `Price action: the 4h change of character`
- `the floor, not the ceiling`

**Argues:** Synthesizes conclusions across multiple backtesting projects showing that mean reversion and reversal concepts consistently outperform trend breakouts.

### [00:15:00](https://www.youtube.com/watch?v=z97PnFIPoFg&t=900s) · slide · What We Keep Finding (confidence: high)

**Values (as shown):**

- `WHAT SURVIVED`
- `35 / 67`
- `9,000 strategies: mean reversion`
- `ICT: fading the sweep`
- `Price action: the 4h change of character`
- `the floor, not the ceiling`

**Argues:** Shows that large-scale quantitative evaluations across different trading paradigms repeatedly identify mean reversion / reversal setups as the only survivors.

### [00:15:56](https://www.youtube.com/watch?v=z97PnFIPoFg&t=956s) · slide · Build it yourself (confidence: high)

**Axes / columns:** Number; Name; Page

**Values (as shown):**

- `PRICE ACTION LAB / THE FIVE PROMPTS`
- `screenshot these and run them in order, one at a time`
- `1 Data and dials: page 2`
- `2 Engine and level tests: page 6`
- `3 The funnel: page 10`
- `4 The final test: page 13`
- `5 The dashboard: page 15`
- `pause each block until Claude Done, in order, one at a time`
- `1 / 16`

**Argues:** Outlines the five-prompt architecture for reproducing the entire price action lab.

### [00:16:02](https://www.youtube.com/watch?v=z97PnFIPoFg&t=962s) · slide · Data and dials (confidence: high)

**Values (as shown):**

- `PROMPT 1 OF 5`
- `2 / 16`
- `WHAT THIS BUILDS: A data pipeline that turns price action trading rules into exact rules a computer can test on NQ and ES futures...`
- `RULES: Work in one project folder with a Python virtual environment. Save every result as a file, and log each decision and its reasons in decisions.md. Pick a single seed for every random draw... The final window stays sealed...`
- `INPUTS: 1-minute NQ and ES continuous front-month futures... copy into data/raw/ and record its sha256: raw_NQ_1m04-24.feather... UTC time, open, high, low, close, volume, contract and spread...`

**Argues:** Defines Prompt 1 setup: directory structure, reproducibility, sealing out-of-sample data, and raw bar inputs.

### [00:16:10](https://www.youtube.com/watch?v=z97PnFIPoFg&t=970s) · slide · Data and dials (Continued - Windows & Cleaning) (confidence: high)

**Values (as shown):**

- `PROMPT 1 OF 5 - CONTINUED`
- `3 / 16`
- `CLEAN AND CHECK: Convert to America/New_York. A session runs 18:00 to 17:00 ET...`
- `US news calendar of CPI, jobs report and FOMC days from the official sources.`
- `WINDOWS: Warm-up: 2021-10-01 to 2021-12-31; builds detector state only, never traded.`
- `Discovery: 2022-01-03 to 2024-07-31; every rule is found and judged here. Era 1 is 2022, era 2 is 2023 to July 2024.`
- `Sealed: 2024-08-01 to the date of the data (2026-10-16 here)... guard every read with an unlock step...`

**Argues:** Specifies strict data partition rules and chronological isolation between discovery and sealed validation data.

### [00:16:11](https://www.youtube.com/watch?v=z97PnFIPoFg&t=971s) · slide · Data and dials (Continued - Charts & Dials) (confidence: high)

**Values (as shown):**

- `PROMPT 1 OF 5 - CONTINUED`
- `4 / 16`
- `CHARTS: Build 5m, 15m, 1h, 4h and daily bars from the 1-minute bars... ATR is Wilder's 14-bar ATR...`
- `THE DIALS: Ten setups: level bounce, breakout, flip zone, trend pullback, trend line, break of structure continuation, change of character reversal, sweep and reclaim, supply and demand zone, fair value gap.`
- `Six setup charts: (3m, 5m, 15m, 1h, 4h, daily)...`
- `Shared dials for levels: swing definition of strength 2, 3, 5 or 8; trend lines... levels as clusters of swings within 0.1, 0.25 or 0.5 ATR... supply and demand zones from runs of 2 to 5 candles covering 1.5 to 3 ATR; three-candle fair value gaps.`

**Argues:** Defines technical chart bars, timeframe options, setup categories, and dial parameters for rule generation.

### [00:16:12](https://www.youtube.com/watch?v=z97PnFIPoFg&t=972s) · slide · Data and dials (Continued - Execution & Combinations) (confidence: high)

**Values (as shown):**

- `PROMPT 1 OF 5 - CONTINUED`
- `5 / 16`
- `Shared dials: direction (confirmation, none, close back, rejection wick, engulfing, either candle, a lower-chart break of structure); entry at the close or limit... stop loss... targets (1R, 2R, 3R, the next swing)...`
- `Filters: the trend agrees... skip trades in direction of 3 or 5 day run, fresh breakouts only, news days (trade, skip or half size), session (all, London and New York, New York morning 08:30 to 11:00, the New York open 09:30 to 11:00), pullback depth, and gap confluence.`
- `Remove combinations that make no sense... The lab count 20,265,402,686 combinations; then count every valid version...`

**Argues:** Details entry/exit permutations and filters, noting a total possible combination space of over 20 billion setups.

### [00:16:15](https://www.youtube.com/watch?v=z97PnFIPoFg&t=975s) · slide · Engine and level tests (Continued - The Engine) (confidence: high)

**Values (as shown):**

- `PROMPT 2 OF 5 - CONTINUED`
- `7 / 16`
- `THE ENGINE: One contract per trade ('half-size on news') and one position at a time per strategy; positions can be held overnight unless the time exit is flat at 16:00.`
- `Costs on every trade: $4 commission per round trip, plus 1 tick of slippage against the trade on market entries, hard stops, close-based stops and structure exits. No slippage on limit entries, targets, time exits or roll exits.`
- `NQ: 0.25 a point, $20 a point; ES: 0.25 tick, $50 a point.`
- `Sharpe is the annualized mean over the standard deviation of daily P&L, times the square root of 252.`

**Argues:** Codifies exact execution engine mechanics, friction costs, tick sizes, point values, and performance calculations.

### [00:16:22](https://www.youtube.com/watch?v=z97PnFIPoFg&t=982s) · slide · The funnel (confidence: high)

**Values (as shown):**

- `PROMPT 3 OF 5`
- `10 / 16`
- `WHAT THIS BUILDS: Runs tens of thousands strategy versions run through the engine on discovery data, a funnel that filters them, and a judgment of each setup as a whole.`
- `THE VERSIONS: Stratified set: 40,000 versions, 4,000 per setup, spread across every dial so that each value appears about as often as random draws would give it...`
- `Fill each setup greedily: draw 400 candidates at a time and add the one that brings the dial shares closest to target.`

**Argues:** Describes sampling methodology for testing a representative subset of 40,000 strategy versions.

### [00:16:23](https://www.youtube.com/watch?v=z97PnFIPoFg&t=983s) · slide · The funnel (Continued - Gate Criteria) (confidence: high)

**Values (as shown):**

- `PROMPT 3 OF 5 - CONTINUED`
- `11 / 16`
- `Six named versions inside it, each a full system built exactly as it is usually taught (the Bare Minimum, the Daily Version, the Checklist, the Sweep System, the Trend Hunter, the Swing Machine)...`
- `The lab grid had 14,016 versions... The draw 47,329.`
- `THE FUNNEL: Pass every version on NQ discovery and on ES discovery. Then, on NQ:`
- `1. Enough trades: 30 or more.`
- `2. A positive P&L.`
- `3. A Sharpe of 0.5 or more.`

**Argues:** Outlines quantitative hurdle rates for strategies to survive discovery filtering.

### [00:16:24](https://www.youtube.com/watch?v=z97PnFIPoFg&t=984s) · slide · The funnel (Continued - Random & ES Validation) (confidence: high)

**Values (as shown):**

- `PROMPT 3 OF 5 - CONTINUED`
- `12 / 16`
- `4. Beat matched random trades... Give each real trade a twin: the same direction, a random entry minute in the same 30 minutes of the day... Beat its twin on profit factor, trade count, win rate... 90% of twins; the version passes when fewer than 5% of the sets make as much as it did.`
- `5. Held on ES: the same version on ES discovery made money with a Sharpe of 0.3 or more.`
- `A version is a final-test candidate when it passes 1 to 4, makes money in both eras, and holds on ES.`

**Argues:** Details statistical significance testing against synthetic random entries and cross-market validation on ES.

### [00:16:25](https://www.youtube.com/watch?v=z97PnFIPoFg&t=985s) · slide · The final test (confidence: high)

**Values (as shown):**

- `PROMPT 4 OF 5`
- `13 / 16`
- `WHAT THIS BUILDS: The final test on data no rule has seen.`
- `INPUTS: From Prompt 1: the sealed final window (NQ and ES 1-minute bars from 2024-08-01 forward)... guard checks...`
- `RULES: Nothing chosen in discovery changes now: no configuration, rule, threshold or dial can move.`
- `Check hashes... Fix any bug that breaks while the seal is still closed.`

**Argues:** Establishes strict blind out-of-sample execution protocols.

### [00:16:27](https://www.youtube.com/watch?v=z97PnFIPoFg&t=987s) · slide · The final test (Continued - Out of Sample Criteria) (confidence: high)

**Values (as shown):**

- `PROMPT 4 OF 5 - CONTINUED`
- `14 / 16`
- `THE RUN: Join the discovery bars from 2024-05-01 to warm up the detectors... trade daily with a bar apron, close open positions at 15:59 ET... Run on NQ and ES over final window, with same costs...`
- `WHAT HELD UP: A version held up on a market when it made money after costs with a Sharpe of 0.5 or more on that market's final window.`
- `A setup held up when the equal-weight average of its versions made money per year with a Sharpe of 0.5 or more.`

**Argues:** Defines what constitutes passing out-of-sample testing on individual versions and setup families.

### [00:16:28](https://www.youtube.com/watch?v=z97PnFIPoFg&t=988s) · slide · The dashboard (confidence: high)

**Values (as shown):**

- `PROMPT 5 OF 5`
- `15 / 16`
- `WHAT THIS BUILDS: A standalone HTML dashboard to record the video from: a page per finding, plus slides for the concept beats, with every number tracked to a saved file.`
- `INPUTS: The saved result tables from Prompts 2 to 4... Read only these files, never the raw or sealed data.`
- `DATA AUDIT: Every number on screen comes from a saved file. Record each one in a provenance file... re-read every value with a second, independent reader before writing the page...`

**Argues:** Specifies audit trail and HTML presentation generation requirements.

## Formulas

- [00:04:12](https://www.youtube.com/watch?v=z97PnFIPoFg&t=252s) `Level tolerance = 0.25 * ATR`
  - `ATR`: Average True Range used to define proximity tolerance for swings and touches to qualify as a valid level
- [00:16:15](https://www.youtube.com/watch?v=z97PnFIPoFg&t=975s) `Sharpe = (mean(daily_pnl) / std(daily_pnl)) * sqrt(252)`
  - `mean(daily_pnl)`: Arithmetic mean of daily strategy profit and loss
  - `std(daily_pnl)`: Sample standard deviation of daily strategy profit and loss
  - `sqrt(252)`: Square root of 252 trading days per calendar year for annualization

## Strategies

### 4-Hour Change of Character (CHoCH) Reversal ([00:01:53](https://www.youtube.com/watch?v=z97PnFIPoFg&t=113s))

**Logic:** Enters a reversal trade when price breaks structure against the prevailing trend (e.g., in an uptrend, closes below the most recent higher low) on a high timeframe, without requiring a liquidity sweep.

**Entry rules:**
- Identify an established trend (higher highs and higher lows for an uptrend).
- Wait for the first candle close against the trend breaking the previous swing point (CHoCH).
- Do not wait for or require a liquidity sweep before the change of character.
- Wait for candle confirmation on NQ.
- Enter at the candle close of the confirmation bar during New York session hours (8am - 4pm ET).
- Skip trade entry if the preceding trend run has persisted for 3 or more consecutive days in that direction.

**Exit rules:**
- Place a hard stop-loss past the most recent swing high (for short) or swing low (for long).
- Do not use close-based stops.
- Set the profit target equal to the distance of the risk (1:1 R/R) or exit at opposite swing levels.

| parameter | value |
|---|---|
| Timeframe | 4-hour |
| Trading Hours | 8:00 AM to 4:00 PM Eastern Time |
| Confirmation requirement | Candle close confirmation on NQ |
| Stop-loss type | Hard stop |
| Consecutive day filter | Skip trades into 3+ day runs |

**Markets/assets:** NQ (E-mini Nasdaq-100 Futures), ES (E-mini S&P 500 Futures)

**Stated performance:** +$62,179 per single NQ contract and +$39,284 per ES contract in the 2-year locked out-of-sample window (61 trades on NQ, 54% win rate). 39 of 48 parameter versions profitable on NQ.

**Costs/slippage mentioned:** yes — Backtested with simulated trading commissions on every trade, slippage on every stop execution, and treating within-bar ambiguous candles as losses.

### Price Action 4-Hour Change of Character Reversal ([00:15:18](https://www.youtube.com/watch?v=z97PnFIPoFg&t=918s))

**Logic:** Mean reversion reversal strategy identifying when price reaches overextended levels on higher timeframes and produces a change of character setup.

**Entry rules:**
- Detect overextension / exhaustion at high or low extremes on 4-hour timeframe.
- Enter on confirmation / change of character trigger.

**Exit rules:**
- Close-based stop loss or target exit (1R to 3R or next swing extreme).

| parameter | value |
|---|---|
| Timeframe | 4-hour |
| Contract Size | 1 contract |

**Markets/assets:** NQ futures, ES futures

**Stated performance:** Identified as the primary surviving setup across tested variations; forms a profitable baseline floor.

**Costs/slippage mentioned:** yes — $4 commission per round trip and 1 tick slippage modeled on market entries, hard stops, and structure exits.

## Tools & data

| name | type | how used |
|---|---|---|
| Claude | other | Used as the programming and system-building AI assistant to generate, structure, and orchestrate the backtesting code across 101,345 strategy variations. |
| CME Futures 1-minute historical data (NQ and ES) | dataset | 5 years of historical 1-minute bar data (3.6 million bars) on NQ and ES used to run 327 million simulated trade executions, with 2 years reserved exclusively for out-of-sample locked testing. |
| Skool | platform | Online community platform run by the presenter covering AI-assisted trading systems. |
| NQ Continuous Front-Month Futures | dataset | 1-minute bar historical dataset used as the primary instrument for discovery and sealed out-of-sample testing. |
| ES Continuous Front-Month Futures | dataset | 1-minute bar historical dataset used for cross-market robustness verification. |
| Claude / ChatGPT | platform | LLMs used to generate the Python backtesting engine, data parsers, and statistical testing harness using the provided prompts. |
| Python venv | platform | Virtual environment used to isolate execution of data ingestion, trade engine, funnel filtering, and dashboard creation scripts. |
| Feather / Parquet | dataset | File format storing historical 1-minute OHLCV tick and bar data. |

## Open questions

- [00:04:29](https://www.youtube.com/watch?v=z97PnFIPoFg&t=269s) **Claude built an entire custom testing system that evaluated 327 million trades across 101,345 variations.** — The underlying programming language, backtesting engine framework, and specific code implementation details are not shown or specified.
- [00:06:33](https://www.youtube.com/watch?v=z97PnFIPoFg&t=393s) **Real costs and slippage were applied to every trade.** — The exact dollar or tick amounts assumed for commissions and slippage per contract on NQ and ES are not explicitly stated.
- [00:13:06](https://www.youtube.com/watch?v=z97PnFIPoFg&t=786s) **Most of the strategy gain in the original 40,000 runs came from a few big days.** — Specific distribution curves, kurtosis, or trade-by-trade logs demonstrating the exact impact of excluding outlier winning days are not provided.
