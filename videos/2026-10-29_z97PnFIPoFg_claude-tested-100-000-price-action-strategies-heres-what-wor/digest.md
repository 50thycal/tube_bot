# Claude Tested 100,000 Price Action Strategies (Here’s What Works)

**Channel:** AI Pathways  
**URL:** https://www.youtube.com/watch?v=z97PnFIPoFg  
**Duration:** 00:17:10

<sub>schema 1.0 · model gemini-3.8-flash · static · analyzed 2026-10-29T13:24:18Z · 3 windows · 122,113 tokens</sub>

## Summary

[00:00:00–00:07:30] Brendan details a large-scale backtesting study conducted using Claude to programmatically evaluate price action concepts across 5 years of 1-minute futures data (NQ and ES, covering 3.6 million bars and 327 million simulated trades). By formalizing subjective visual chart concepts into parameterized quantitative rules across 10 core setups (such as level bounces, break of structure, change of character, and fair value gaps), the study tests 101,345 strategy variations, finding that while 24,879 versions were profitable after transaction costs, only 8,310 met a baseline risk-adjusted performance hurdle of Sharpe 0.5+.

[00:07:30–00:15:00] This video segment evaluates common price action trading concepts using quantitative backtests across tens of thousands of strategy variations on NQ and ES futures, including out-of-sample locked test data. It demonstrates that win rate has weak correlation to profitability (0.27) and lower timeframes suffer severely from transaction costs (consuming 46% of gross profit on the 1m). The test shows that support and resistance levels beat random lines (holding 51.1% vs 42.4%), flip zones provide substantial statistical edge (+11.5 pts on NQ), and touch count does not strengthen levels. The single setup that robustly survived out-of-sample testing across both markets was a 4-hour change of character (CHoCH) without requiring a prior liquidity sweep, using a hard stop and trading during New York session hours.

[00:15:00–00:17:10] In the concluding segment of the presentation, the speaker explains that across thousands of tested variations, mean-reversion setups (such as ICT's fading the sweep and the 4-hour change of character reversal) consistently form the baseline floor of viable trading edges. The speaker then presents the exact five-prompt framework used with LLMs (Claude/ChatGPT) to build an end-to-end Python research lab covering data ingestion, trade engine execution, multi-stage funnel filtering, out-of-sample sealed testing, and automated HTML dashboard generation.

## Segments

### [00:00:00](https://www.youtube.com/watch?v=z97PnFIPoFg&t=0s)–00:01:05 · Introduction and Project Overview

- Tested over 100,000 price action concepts using Claude to determine which trading mechanics actually work versus traditional indicators.
- The testing framework evaluated 40,000 sampled parameter variations plus over 61,000 common settings across nearly 5 years of 1-minute futures data on NQ and ES.
- Over 327 million simulated trades were executed across the test matrix.
- Speaker background: Brendan studied Math and Economics at UCLA, worked in investment banking at Raymond James for over 3 years, and has spent the past 2 years building trading systems.

### [00:01:05](https://www.youtube.com/watch?v=z97PnFIPoFg&t=65s)–00:03:59 · Core Price Action Setup Components and the 10 Setups

- Price action trading relies on direct chart structure without lagging indicators.
- Level: Horizontal support and resistance areas where price bounces; tested whether levels beat random lines from 1-minute to daily charts.
- Trend: Higher highs and higher lows; price breaking past a previous high is defined as a 'break of structure' (BOS). Backtests indicated trend continuation rules often have no follow-through across arbitrary charts.
- Change of Character (CHoCH): Occurs when price breaks in the opposite direction (e.g., closing below the last higher low); held up as the best performing setup, particularly on the 4-hour timeframe.
- Sweep: Occurs when price momentarily breaches a high or low to trigger stops before reversing; data showed sweeps only reversed about half the time, making them useful as a filter rather than a standalone entry.
- Confirmation: Requiring a candle to close back beyond the level before entering, rather than entering on a blind limit order.
- The 10 major setups tested: Level bounce, Breakout, Flip zone, Trend pullback, Trend line, Break of structure, Change of character, Sweep and reclaim, Supply and demand, and Fair value gap.

### [00:03:59](https://www.youtube.com/watch?v=z97PnFIPoFg&t=239s)–00:06:59 · Testing Methodology and Execution Engine

- Traditional price action is drawn by eye and subjective; different traders draw levels differently based on feeling without verifying historical performance.
- Algorithmic definition applied for testing: Level defined as 2+ swings within 0.25 ATR; touch defined as within 0.25 ATR of the level; confirmation defined as a close back across it.
- Dial parameters tested include touches, line vs. zone, confirmation candle type, stop placement, profit target, chart timeframe, and trend/regime filters, creating 20.3 trillion theoretical combinations.
- Backtest dataset: 5 years, 3.6 million 1-minute bars on NQ and ES futures.
- The Gauntlet backtest rules: real exchange costs applied to every trade, slippage on every stop, ambiguous intra-candle touch of both stop and target counted as a full loss, and compared against random trade benchmarks.
- Validation process: Out-of-sample testing on ES with 2 years of locked data that the testing engine never observed during initial NQ discovery.

### [00:06:59](https://www.youtube.com/watch?v=z97PnFIPoFg&t=419s)–00:07:30 · Overall Results Funnel and Win Rate Distribution

- Out of 101,345 total versions tested, 88,986 generated at least 30 trades (enough trades to be graded).
- 24,879 versions (approximately 24.5%) made money after accounting for trading costs in the NQ discovery period.
- 8,310 versions (around 8.2%) achieved a Sharpe ratio of 0.5 or greater.
- Scatter plot of 40,000 strategies shows win rate and profit per contract per year on NQ discovery.
- 138 strategies achieved an 80%+ win rate, but overall correlation between win rate and profit was only 0.27; 67 of the 138 high win-rate strategies used a 1R target.

### [00:07:30](https://www.youtube.com/watch?v=z97PnFIPoFg&t=450s)–00:07:52 · Win Rate vs Profitability

- Analyzed 40,000 strategies by win rate and annual result per contract on NQ discovery data.
- Win rate rarely clears 80%; only 138 strategies achieved an 80%+ win rate, with 67 using a 1R target.
- Win rate has a very low correlation (0.27) to overall net profit.

### [00:07:52](https://www.youtube.com/watch?v=z97PnFIPoFg&t=472s)–00:08:29 · Timeframe Performance and Trading Costs

- Trading costs consume 46.0% of gross profit on the 1-minute chart, but only 3.9% on the daily chart.
- Profitable strategy share increases with timeframe: 32% on 1m, 36% on 5m, 44% on 15m, 47% on 1h, 48% on 4h, and 47% on Daily.
- Higher timeframes (1h, 4h) trade less frequently, requiring less extreme edge to overcome friction and commissions.

### [00:08:29](https://www.youtube.com/watch?v=z97PnFIPoFg&t=509s)–00:09:41 · Support/Resistance Levels and Touch Count Analysis

- Real support/resistance levels held 51.1% of touches compared to 42.4% for random lines across timeframes from 5m to daily (+8.7 pts NQ, +8.5 pts ES).
- Tested the price action belief that more touches strengthen a level; evidence showed the opposite.
- A level touched once outperformed random lines by +9.0 pts, whereas a level touched 4 times outperformed by +6.1 pts.
- Levels touched 3+ times bounced slightly less often (19.2% vs 20.5%) and broke through more often (27.8% vs 26.1%).

### [00:09:41](https://www.youtube.com/watch?v=z97PnFIPoFg&t=581s)–00:10:11 · Level Rules and Flip Zones

- Flip zones (prior resistance turning into support after breakout on first retest) held +11.5 percentage points better than random lines on NQ and +10.9 points on ES.
- Touch count (-1.1 pts) and walls at 3+ touches (-1.3 pts) showed negative impact.
- Flip zones are identified as one of the strongest price action concepts.

### [00:10:11](https://www.youtube.com/watch?v=z97PnFIPoFg&t=611s)–00:10:33 · Trend Setups: BOS vs CHoCH and Sweeps

- Raw Break of Structure (-0.04 ATR) and Change of Character (-0.05 ATR) alone did not move price.
- Among trend setups, only CHoCH reversal had a positive median result (+$61), whereas BOS continuation (-$328), sweep and reclaim (-$368), and trend line (-$479) were negative.
- Testing trend setups as taught showed that requiring a liquidity sweep before a CHoCH lost money (-$834), while CHoCH without a sweep made +$903.

### [00:10:33](https://www.youtube.com/watch?v=z97PnFIPoFg&t=633s)–00:11:19 · Execution Mechanics: Confirmation Tax and Stop Types

- Waiting for confirmation candle gave up 4.3 points of entry price but improved net annual edge by +$719 (-$373 loss vs -$1,093 loss for limit orders at the touch).
- Close-based stops had a higher win rate (40% vs 29%) but larger losses, resulting in -$132 worse performance per year compared to hard stops (-$290 vs -$158).

### [00:11:19](https://www.youtube.com/watch?v=z97PnFIPoFg&t=679s)–00:12:30 · Context Filters and Timeframe Ladder Out-of-Sample

- Trading only New York session (8am to 4pm ET) added +$270 per year; skipping trades into 3+ day runs added +$246 per year; filtering by daily trend agreement hurt performance (-$587).
- The 4h CHoCH setup was the only setup to pass consistency checks on both NQ and ES across original and common sets.
- Tested on a 2-year locked out-of-sample dataset containing a 22.5% market drop and a 74.5% rally.
- Out-of-sample profitability increased monotonically by timeframe: 9.2% on 1m, 20.3% on 5m, 28.8% on 15m, 37.7% on 1h, 45.1% on 4h, and 47.9% on daily.

### [00:12:30](https://www.youtube.com/watch?v=z97PnFIPoFg&t=750s)–00:14:22 · Best Performing Strategy Rules and Robustness

- Best version: 4h Change of Character with no sweep, entry at candle close, hard stop past last swing, and 1:1 risk-to-reward target.
- In the locked 2-year out-of-sample window, generated +$62,179 on 1 NQ contract (61 trades, 54% win rate) and +$39,284 on ES.
- 39 of 48 versions made money on NQ; 66% of all 314 common versions made money on NQ, and 54.5% on ES.
- Average New York session version made +$17,041 per contract on NQ and remained profitable even excluding its 10 best days.
- 7 surviving rules summarized: 1) 4h CHoCH, 2) Higher timeframes, 3) NY session only, 4) Skip trades into 3+ day run, 5) Confirmation candle on NQ, 6) Hard stop, 7) No sweep before change.

### [00:14:22](https://www.youtube.com/watch?v=z97PnFIPoFg&t=862s)–00:15:00 · Example Trade Walkthrough and Common Findings

- Walkthrough of an actual short trade on NQ 4h from July 11, 2024: uptrend, CHoCH candle close, entry at close, stop above swing high, 1R target hit.
- Noted consistent conclusions across 9,000 strategy tests (mean reversion), ICT tests (fading sweeps), and price action tests (4h CHoCH).

### [00:15:00](https://www.youtube.com/watch?v=z97PnFIPoFg&t=900s)–00:15:56 · What Survived: Mean Reversion as the Core Baseline

- In the 9,000-strategy test, mean reversion was the only strategy family that consistently held up across thousands of variations.
- In the ICT test, fading the sweep held up, which is fundamentally a mean-reversion style strategy.
- In price action testing, the reversal setup (specifically the 4-hour change of character) functioned as a mean-reversion setup.
- The core concept is that when price stretches too high or too low, it tends to revert.
- These test results represent the floor (baseline foundation) rather than the ceiling, averaged at 1 contract per trade before customized risk management or sizing.

### [00:15:56](https://www.youtube.com/watch?v=z97PnFIPoFg&t=956s)–00:16:14 · The Five Prompts: Prompt 1 - Data and Dials

- Prompt 1 builds the data pipeline, time conversions (New York session 18:00-17:00 ET), data audits, and higher timeframe candle aggregation (5m, 15m, 1h, 4h, daily).
- It establishes the testing windows: Warm-up (2021-10-01 to 2021-12-31), Discovery (2022-01-03 to 2024-07-31), and Sealed Final Window (2024-08-01 to 2024-10-16).
- The sealed data is protected by a sha256 manifest and programmatic guard that logs access.
- The prompt parametrizes 10 setups, 6 setup charts, 10 detector dials, and shared dials, counting 20,265,402,666,000 valid unique strategy parameter combinations.

### [00:16:14](https://www.youtube.com/watch?v=z97PnFIPoFg&t=974s)–00:16:22 · The Five Prompts: Prompt 2 - Engine and Level Tests

- Prompt 2 builds the execution engine checking 1-minute bars and behavior tests comparing price action to random lines.
- Engine specifications: 1 contract per trade, 1 position at a time per strategy, flat at 16:00 unless overnight holding allowed.
- Transaction costs: $4 commission per round trip, 1 tick slippage on market entries, hard stops, close-based stops, and structure exits (no slippage on limits, targets, time/roll exits).
- Tick sizes: NQ tick 0.25 ($20/point), ES tick 0.25 ($50/point). Ambiguous 1-minute bars hitting stop and target are counted as losses.
- Random entries (20,000 trades) must average -$9.80 per trade after costs.
- Behavioral tests perform 2,000 bootstrap resamples on 95% confidence intervals across NQ and ES.

### [00:16:22](https://www.youtube.com/watch?v=z97PnFIPoFg&t=982s)–00:16:26 · The Five Prompts: Prompt 3 - The Funnel

- Prompt 3 filters tens of thousands of versions across a multi-stage funnel on discovery data.
- Sample sets: 40,000 random versions (4,000 per setup), 6 named versions, 14,016 usual-settings versions, and 47,329 versions mirroring typical trader habits.
- Funnel filter criteria on NQ: at least 38 trades, positive net P&L, Sharpe ratio >= 0.5, beating matched random trade sets (less than 5% of 10,000 twin sets beat it), and holding on ES with Sharpe >= 0.3.

### [00:16:26](https://www.youtube.com/watch?v=z97PnFIPoFg&t=986s)–00:16:32 · The Five Prompts: Prompts 4 & 5 - Final Test and Dashboard

- Prompt 4 executes the single-run test on the sealed data window (2024-08-01 to 2024-10-16).
- A setup holds up if it makes money after costs with a Sharpe ratio of 0.5 or higher on the sealed window.
- Prompt 5 builds an automated 1920x1080 offline HTML presentation dashboard, enforcing full data provenance for every number shown.

### [00:16:32](https://www.youtube.com/watch?v=z97PnFIPoFg&t=992s)–00:17:10 · Generalization and Closing

- The five-prompt method applies to any trading system or discretionary concept to test viability at scale with real data.
- Closing call to like, comment, subscribe, and join the community link.

## Claims

| ts | claim | evidence | caveats |
|---|---|---|---|
| [00:02:02](https://www.youtube.com/watch?v=z97PnFIPoFg&t=122s) | Change of character (CHoCH) held up the best out of all price action setups tested, particularly on the 4-hour timeframe. | backtest | Stated that higher timeframe charts yielded more consistent edge than lower timeframes. |
| [00:02:24](https://www.youtube.com/watch?v=z97PnFIPoFg&t=144s) | Liquidity sweeps reverse back inside the level only about half the time, making them ineffective as a standalone entry signal. | backtest | Can still be useful as a secondary filter or confirmation signal rather than an isolated trigger. |
| [00:07:05](https://www.youtube.com/watch?v=z97PnFIPoFg&t=425s) | Only ~8% (8,310 out of 101,345) of tested price action rule sets achieved a Sharpe ratio of 0.5+ after realistic transaction costs and slippage. | backtest | Results from NQ discovery period on 5 years of 1-minute bar data. |
| [00:07:27](https://www.youtube.com/watch?v=z97PnFIPoFg&t=447s) | Win rate has a very weak correlation (0.27) to overall net profitability across 40,000 tested price action strategies. | data | 138 strategies achieved over 80% win rates, but nearly half (67) relied on small 1R profit targets. |
| [00:07:47](https://www.youtube.com/watch?v=z97PnFIPoFg&t=467s) | Win rate has very low correlation (0.27) with strategy profit across 40,000 strategies. | data | Tested on NQ discovery dataset. |
| [00:08:06](https://www.youtube.com/watch?v=z97PnFIPoFg&t=486s) | Trading costs consume 46% of gross profit on the 1-minute chart, compared to only 3.9% on the daily chart. | data | Reflects futures contract costs and commissions on NQ discovery tests. |
| [00:08:42](https://www.youtube.com/watch?v=z97PnFIPoFg&t=522s) | Real support and resistance levels hold 51.1% of touches, outperforming random lines (42.4%). | data | Tested on timeframes from 5m to daily on NQ and ES. |
| [00:09:02](https://www.youtube.com/watch?v=z97PnFIPoFg&t=542s) | Levels touched multiple times do not become stronger; 1-touch levels beat random lines by +9.0 pts while 4-touch levels beat random lines by +6.1 pts. | data |  |
| [00:09:54](https://www.youtube.com/watch?v=z97PnFIPoFg&t=594s) | Flip zones held 11.5 percentage points better than random lines on NQ and 10.9 points better on ES. | data | Evaluated on the first retest. |
| [00:10:26](https://www.youtube.com/watch?v=z97PnFIPoFg&t=626s) | Waiting for a liquidity sweep before a change of character lost $834, while trading CHoCH without a sweep gained $903. | backtest | Tested on unseen 2-year locked data. |
| [00:10:46](https://www.youtube.com/watch?v=z97PnFIPoFg&t=646s) | Waiting for confirmation gives up 4.3 points of price entry but reduces losses by $719 per year compared to limit orders at touch. | backtest | Tested specifically on Nasdaq futures (NQ). |
| [00:11:08](https://www.youtube.com/watch?v=z97PnFIPoFg&t=668s) | Close-based stops cost $132 more per year than hard stops despite having a higher win rate (40% vs 29%). | backtest |  |
| [00:12:53](https://www.youtube.com/watch?v=z97PnFIPoFg&t=773s) | A plain 4h CHoCH strategy generated $62,179 on NQ and $39,284 on ES across a 2-year locked out-of-sample period. | backtest | Single contract per market, 61 trades on NQ. |
| [00:15:01](https://www.youtube.com/watch?v=z97PnFIPoFg&t=901s) | Mean reversion was the only strategy style that held up out of thousands of variations tested in previous large-scale experiments. | data | Represents baseline performance on 1 contract without custom risk management. |
| [00:16:13](https://www.youtube.com/watch?v=z97PnFIPoFg&t=973s) | The lab's full combinatorial space of valid parameter dial settings totals 20,265,402,666,000 variations. | data | Nonsensical combinations (such as a 16:00 flat exit on a 4-hour setup) were removed. |
| [00:16:18](https://www.youtube.com/watch?v=z97PnFIPoFg&t=978s) | 20,000 random market entries with a 1R stop and 2R target in the discovery period lost an average of -$9.80 per trade after costs. | backtest | Evaluated on discovery window minutes. |

## Visuals

### [00:00:16](https://www.youtube.com/watch?v=z97PnFIPoFg&t=16s) · diagram · The Price Action Setup (confidence: high)

**Values (as shown):**

- `1 level - beat random lines, 1m to daily`
- `2 trend - x no follow-through, any chart`
- `3 change of character - best setup, on the 4h`
- `4 sweep - x reversed about half the time`
- `5 confirmation - beat a limit at the level (NQ)`
- `6 stop and target - hard stop beat close-based, target size: no edge`
- `THE SIX CHARTS: 1m, 5m, 15m, 1h, 4h, daily`
- `higher chart, more versions made money`
- `break of structure`
- `levels, trend, entry, exit`
- `2 / 66`

**Argues:** Illustrates the visual components of a price action trade setup and summarizes key preliminary backtest takeaways for each component.

### [00:00:29](https://www.youtube.com/watch?v=z97PnFIPoFg&t=29s) · diagram · How We Tested It (confidence: high)

**Values (as shown):**

- `THE DIALS: touches, line or zone, confirmation, stop, target, chart, filters`
- `20.3 trillion possible versions`
- `WHAT WE RAN: 40,000 spread across every dial, 4,000 per setup`
- `61,345 common versions: usual settings, 0 to 2 filters`
- `101,345 total`
- `THE NAMED VERSIONS: Bare Minimum, Checklist, Entry Model, Zone System, Sweep System, Daily Version`
- `THE DATA: 5 years, 3.6M 1-minute bars, NQ + ES, 327M simulated trades`
- `THE GAUNTLET: real costs, every trade; slippage on every stop; ambiguous candle = a loss; vs random times; vs random trades; checked on ES; 2 years locked away`
- `6 / 66`

**Argues:** Details the experimental design, dataset scale, combinatorial space, and execution constraints used in the automated testing framework.

### [00:00:37](https://www.youtube.com/watch?v=z97PnFIPoFg&t=37s) · diagram · The Ten Setups (confidence: high)

**Values (as shown):**

- `1 Level bounce - buy support, sell resistance`
- `2 Breakout - trade the close through a level`
- `3 Flip zone - old resistance becomes support`
- `4 Trend pullback - buy the first dip in an uptrend`
- `5 Trend line - buy a touch of the rising line`
- `6 Break of structure - go with the break of the last swing`
- `7 Change of character - the first break against the trend`
- `8 Sweep and reclaim - a wick through a low, closed back above`
- `9 Supply and demand - the first return to an impulse's base`
- `10 Fair value gap - the first return into a three-candle gap`
- `the ten we tested`
- `3 / 66`

**Argues:** Visual overview of the ten canonical price action patterns formalized and tested across the dataset.

### [00:04:12](https://www.youtube.com/watch?v=z97PnFIPoFg&t=252s) · chart · Drawn By Eye (confidence: high)

**Axes / columns:** Time; NQ Price (16,200 to 16,350)

**Values (as shown):**

- `NQ 15m, Jul 7, 2023, discovery`
- `Trader A - limit at the touch`
- `Trader B - close back across`
- `AS RULES: Level: 2+ swings within 0.25 ATR, Touch: within 0.25 ATR of the level, Confirmation: a close back across it`
- `same chart, different lines`
- `5 / 66`

**Argues:** Demonstrates why discretionary price action trading lacks consistency and how mathematical rules (ATR tolerance) were applied to standardize subjective interpretations.

### [00:06:59](https://www.youtube.com/watch?v=z97PnFIPoFg&t=419s) · chart · FUNNEL (confidence: high)

**Axes / columns:** Stage; Count of Strategy Versions

**Values (as shown):**

- `All 101,346 versions through each stage, NQ discovery`
- `Original 40,000`
- `Common versions`
- `All: 101,345`
- `Enough trades to grade (30+): 88,986`
- `Profitable: 24,879`
- `Sharpe 0.5+: 8,310`
- `101,345 TESTED`
- `24,879 MADE MONEY AFTER COSTS`
- `24,879 of the 101,345 versions made money after costs in discovery, and 8,310 had a Sharpe of 0.5+`
- `8 / 66`

**Argues:** Presents attrition rates of price action strategies from raw tested models down to those meeting minimum trade count, net profitability after costs, and Sharpe > 0.5.

### [00:07:24](https://www.youtube.com/watch?v=z97PnFIPoFg&t=444s) · chart · Win Rate And Profit (confidence: high)

**Axes / columns:** Win Rate (%); Result Per Contract Per Year ($0 to $40k)

**Values (as shown):**

- `40,000 strategies by win rate and result per contract per year, NQ discovery`
- `5R`
- `4R`
- `3R`
- `2R`
- `Next`
- `2R`
- `1.5R`
- `1R`
- `80%+`
- `138 WIN 80%+`
- `0.27 CORRELATION`
- `67 of the 138 use a 1R target`
- `138 strategies won 80%+ of their trades; across all 40,000 win rate barely tracks profit (correlation 0.27)`
- `9 / 66`

**Argues:** Scatter plot showing that win rate has negligible correlation (0.27) with annual dollar return per contract, dispelling high win-rate marketing claims.

### [00:07:30](https://www.youtube.com/watch?v=z97PnFIPoFg&t=450s) · chart · Win Rate And Profit (confidence: high)

**Axes / columns:** X: WIN RATE (0% to 100%); Y: Result per contract per year ($0k, $5k, $10k, $15k)

**Values (as shown):**

- `40,000 strategies by win rate and result per contract per year, NQ discovery`
- `138 WIN 80%+`
- `0.27 CORRELATION`
- `67 of the 138 use a 1R target`
- `80%+`
- `138 strategies won 80%+ of their trades; across all 40,000 win rate barely tracks profit (correlation 0.27)`

**Argues:** High win rates are rare and win rate does not correlate strongly with net profitability.

### [00:07:52](https://www.youtube.com/watch?v=z97PnFIPoFg&t=472s) · chart · Timeframes (confidence: high)

**Axes / columns:** Timeframe (1m, 5m, 15m, 1h, 4h, Daily); PROFITABLE VERSIONS (%); COSTS / GROSS PROFIT (%); MEDIAN PER YEAR ($)

**Values (as shown):**

- `PROFITABLE VERSIONS: 1m: 32%, 5m: 36%, 15m: 44%, 1h: 47%, 4h: 48%, Daily: 47%`
- `COSTS / GROSS PROFIT: 1m: 46%, 5m: 38%, 15m: 24%, 1h: 11%, 4h: 6%, Daily: 4%`
- `MEDIAN PER YEAR: 1m: -$306, 5m: -$310, 15m: -$309, 1h: -$418, 4h: -$426, Daily: -$405`
- `46.0% COSTS ON 1M`
- `3.9% COSTS ON DAILY`
- `Costs take 46.0% of gross profit on the 1m chart and 3.9% on daily`

**Argues:** Transaction costs heavily erode profitability on lower timeframes like 1m, whereas higher timeframes preserve gross profits.

### [00:08:29](https://www.youtube.com/watch?v=z97PnFIPoFg&t=509s) · chart · Random Lines (confidence: high)

**Axes / columns:** Timeframes (All, 5m, 15m, 1h, 4h, Daily); Share of touches that hold, real levels vs random lines, NQ discovery (%)

**Values (as shown):**

- `Real levels (cyan) vs Random lines (grey)`
- `All: 51% vs 42%`
- `5m: 52% vs 43%`
- `15m: 50% vs 43%`
- `1h: 48% vs 40%`
- `4h: 47% vs 38%`
- `Daily: 51% vs 33%`
- `+8.7 pts NQ`
- `+8.5 pts ES`
- `SURVIVED Real levels hold 51.1% of touches against 42.4% for random lines, on every chart from 5m to daily`

**Argues:** Technical support and resistance levels hold significantly more frequently than randomly placed horizontal lines.

### [00:08:50](https://www.youtube.com/watch?v=z97PnFIPoFg&t=530s) · chart · Touch Count (confidence: high)

**Axes / columns:** Number of touches (1 touch, 2 touches, 3 touches, 4 touches); Points better than random lines

**Values (as shown):**

- `1 touch: +9.0 pts`
- `2 touches: +7.8 pts`
- `3 touches: +8.2 pts`
- `4 touches: +6.1 pts`
- `+9.0 pts ONE TOUCH`
- `+6.1 pts FOUR TOUCHES`
- `3+ touches vs 1 touch: bounced 19.2% vs 20.5%, broke and kept going 27.8% vs 26.1%`
- `DIDN'T SURVIVE A level touched four times held no better than a level touched once; levels touched 3+ times bounced a bit less and broke through a bit more`

**Argues:** Repeatedly touching a support/resistance level weakens it rather than strengthens it.

### [00:09:42](https://www.youtube.com/watch?v=z97PnFIPoFg&t=582s) · chart · Level Rules (confidence: high)

**Axes / columns:** Rule; Percentage points relative to comparison (95% intervals)

**Values (as shown):**

- `Touch count: -1.1 pts`
- `Wall at 3+ touches: -1.3 pts`
- `Weaker pushes: +0.4 pts`
- `Box vs line: +0.5 pts`
- `Flip zones: +11.5 pts`
- `+11.5 pts FLIP ZONES, NQ`
- `+10.9 pts FLIP ZONES, ES`
- `Flip zones hold; touch count, walls and weaker pushes do not`

**Argues:** Flip zones provide substantial edge over random lines, whereas touch counts and wall rules detract from performance.

### [00:10:11](https://www.youtube.com/watch?v=z97PnFIPoFg&t=611s) · chart · Follow-Through (confidence: high)

**Axes / columns:** Setup; Follow-through (ATR)

**Values (as shown):**

- `Break of structure: -0.04 ATR`
- `Change of character: -0.05 ATR`
- `-0.04 ATR BREAK OF STRUCTURE`
- `-0.05 ATR CHANGE OF CHARACTER`
- `DIDN'T SURVIVE Neither break moved price on its own`

**Argues:** Raw break of structure and change of character signals do not generate positive price follow-through in isolation.

### [00:10:18](https://www.youtube.com/watch?v=z97PnFIPoFg&t=618s) · chart · Trend Setups (confidence: high)

**Axes / columns:** Setup; Median result ($)

**Values (as shown):**

- `BOS continuation: -$328`
- `CHoCH reversal: +$61`
- `Sweep and reclaim: -$368`
- `Trend line: -$479`
- `+$61 CHOCH MEDIAN`
- `Only the change of character had a positive median`

**Argues:** Change of character reversal is the only trend setup tested with a positive median annual outcome.

### [00:10:22](https://www.youtube.com/watch?v=z97PnFIPoFg&t=622s) · chart · Trend Trades As Taught (confidence: high)

**Axes / columns:** Setup variant; Annual performance ($)

**Values (as shown):**

- `Trend line, first to second low: -$586`
- `Reversal flip: -$417`
- `Sweep, then change: -$834`
- `Change, no sweep needed: +$903`
- `Late entry on a 5m break: -$2,608`
- `+$903 NO SWEEP, UNSEEN`
- `-$834 AFTER A SWEEP`
- `Only the change of character without a sweep made money`

**Argues:** Conventional teaching that requires a liquidity sweep before trading a change of character destroys performance.

### [00:10:34](https://www.youtube.com/watch?v=z97PnFIPoFg&t=634s) · chart · Confirmation Tax (confidence: high)

**Axes / columns:** Entry style; Annual edge ($)

**Values (as shown):**

- `Limit at the touch: -$1,093`
- `After confirmation: -$373`
- `+$719 EDGE PER YEAR`
- `4.3 POINTS GIVEN UP`
- `SURVIVED Waiting for confirmation lost less than a limit at the touch`

**Argues:** Waiting for a confirmation candle gives up 4.3 points of entry but outperforms blind limit orders by $719/year.

### [00:10:59](https://www.youtube.com/watch?v=z97PnFIPoFg&t=659s) · chart · Stops (confidence: high)

**Axes / columns:** Stop type; Performance per year ($)

**Values (as shown):**

- `Hard stop: -$158`
- `Close-based stop: -$290`
- `-$132 CLOSE STOPS, PER YEAR`
- `DIDN'T SURVIVE Close-based stops cost $132 a year more`

**Argues:** Hard stops outperform close-based stops because close-based stops incur much larger tail losses.

### [00:11:19](https://www.youtube.com/watch?v=z97PnFIPoFg&t=679s) · chart · Context (confidence: high)

**Axes / columns:** Context filter; Performance per year ($)

**Values (as shown):**

- `New York only (8am to 4pm ET): +$270`
- `Skip 3+ day runs: +$246`
- `Daily trend agrees: -$587`
- `+$270 NEW YORK ONLY, UNSEEN NQ`
- `-$587 DAILY TREND, UNSEEN NQ`
- `New York hours and skipping 3+ day runs helped. The daily trend filter hurt`

**Argues:** Session timing and run filters improve returns, while daily trend alignment reduces edge.

### [00:11:29](https://www.youtube.com/watch?v=z97PnFIPoFg&t=689s) · table · Passed On Both Markets (confidence: high)

**Axes / columns:** Market; Setup Group; Setup Name; Annual Return ($)

**Values (as shown):**

- `NQ Original 40,000: change of character 1h (+$1,208), change of character 4h (+$4,025)`
- `NQ Common Versions: change of character 4h (+$4,884), flip zone daily (+$9,093)`
- `ES Original 40,000: change of character 4h (+$4,146)`
- `ES Common Versions: change of character 4h (+$3,374), breakout daily (+$1,734)`
- `4 of 4 CHOCH 4H PASSED IN EACH SET AND ON EACH MARKET`
- `Only the 4h change of character passed on both markets`

**Argues:** The 4-hour change of character is the only price action setup that consistently succeeded across both NQ and ES in both discovery and common version sets.

### [00:11:55](https://www.youtube.com/watch?v=z97PnFIPoFg&t=715s) · chart · Final Window (confidence: high)

**Axes / columns:** X: Year (2025, 2026); Y: Price (14,000 to 30,000)

**Values (as shown):**

- `High 22,235`
- `Low 17,232`
- `Peak 30,078`
- `-22.5% SELLOFF`
- `+74.5% RALLY`
- `The locked years held a 22.5% drop and a 74.5% rally`

**Argues:** The 2-year out-of-sample test window provided diverse market regimes, including a major selloff and rally.

### [00:12:02](https://www.youtube.com/watch?v=z97PnFIPoFg&t=722s) · chart · Timeframe Ladder (confidence: high)

**Axes / columns:** Timeframe (1m, 5m, 15m, 1h, 4h, Daily); Profitable versions (%)

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

**Argues:** Out-of-sample robustness rises directly with timeframe from 9% on 1m to 48% on daily.

### [00:12:31](https://www.youtube.com/watch?v=z97PnFIPoFg&t=751s) · chart · Best Version (confidence: high)

**Axes / columns:** X: Time (2023, 2024, 2025, 2026); Y: Cumulative Profit ($0k to $300k)

**Values (as shown):**

- `+$62,179 LOCKED YEARS, NQ`
- `+$39,284 LOCKED YEARS, ES`
- `61 trades on NQ, 54% winners`
- `Picked in discovery, it made money on both markets in the locked years`

**Argues:** The 4h CHoCH strategy remained profitable out-of-sample on both NQ and ES without overfitting.

### [00:13:06](https://www.youtube.com/watch?v=z97PnFIPoFg&t=786s) · table · The 4h Setup (confidence: high)

**Axes / columns:** Metric; Value

**Values (as shown):**

- `39 of 48 versions on its usual settings made money, NQ`
- `66% of all 314 common versions made money, NQ`
- `+$17,041 New York session versions, average per contract (original 40,000, NQ); still made money without their 10 best days`
- `54.5% of the common versions made money on ES`
- `the two locked years`
- `In the original 40,000, most of the gain came from a few big days`

**Argues:** The 4h setup displays high parameter stability and broad profitability across hundreds of variations.

### [00:13:16](https://www.youtube.com/watch?v=z97PnFIPoFg&t=796s) · slide · What Survived (confidence: high)

**Axes / columns:** Rule Number; Description

**Values (as shown):**

- `1. Change of character, 4h chart`
- `2. Higher charts (made money: 9% on 1m, 48% on daily; common versions, unseen NQ)`
- `3. New York session only`
- `4. Skip trades into a 3+ day run`
- `5. Confirmation candle (NQ)`
- `6. Hard stop, not close-based`
- `7. No sweep before the change`

**Argues:** Summary of the 7 quantitative principles that survived rigorous in-sample and out-of-sample backtesting.

### [00:14:22](https://www.youtube.com/watch?v=z97PnFIPoFg&t=862s) · chart · Example Trade (confidence: high)

**Axes / columns:** X: Date (Jul 2, Jul 4, Jul 9, Jul 11, Jul 16, Jul 18); Y: Price (19,800 to 21,000)

**Values (as shown):**

- `NQ 4h, July 11, 2024`
- `Trend`
- `Change of character`
- `Stop`
- `Entry`
- `Target`

**Argues:** Illustration of the surviving strategy execution on a 4-hour NQ short trade.

### [00:14:50](https://www.youtube.com/watch?v=z97PnFIPoFg&t=890s) · slide · What We Keep Finding (confidence: high)

**Axes / columns:** Study; Finding

**Values (as shown):**

- `9,000 strategies: mean reversion`
- `ICT: fading the sweep`
- `Price action: the 4h change of character`
- `the floor, not the ceiling`

**Argues:** Independent testing across multiple trading frameworks converges on similar core principles.

### [00:15:00](https://www.youtube.com/watch?v=z97PnFIPoFg&t=900s) · slide · WHAT SURVIVED / What We Keep Finding (confidence: high)

**Values (as shown):**

- `35 / 67`
- `9,000 strategies: mean reversion`
- `ICT: fading the sweep`
- `Price action: the 4h change of character`
- `the floor, not the ceiling`

**Argues:** Mean reversion and reversal mechanics are the recurring survivors across disparate trading methodology backtests.

### [00:15:56](https://www.youtube.com/watch?v=z97PnFIPoFg&t=956s) · slide · PRICE ACTION LAB / THE FIVE PROMPTS / Build it yourself (confidence: high)

**Values (as shown):**

- `1 / 16`
- `screenshot these and run them in order, one at a time`
- `1 Data and dials page 2`
- `2 Engine and level tests page 6`
- `3 The funnel page 10`
- `4 The final test page 13`
- `5 The dashboard page 15`

**Argues:** Outlines the five-prompt architecture for building the research lab.

### [00:16:02](https://www.youtube.com/watch?v=z97PnFIPoFg&t=962s) · slide · PROMPT 1 OF 5 / Data and dials (confidence: high)

**Values (as shown):**

- `2 / 16`
- `WHAT THIS BUILDS`
- `A python research lab that turns price action trading rules into exact rules a computer can test on NQ and ES futures...`
- `RULES`
- `Work in one project folder with a Python virtual environment. Save every result as a file, and log each decision and its reason in decisions.md.`
- `Write a master seed for every random draw...`
- `The final window stays sealed...`
- `Never move a threshold after seeing a result...`
- `INPUTS`
- `1-minute NQ and ES continuous front-month futures...`
- `sha256`
- `ts_event, open, high, low, close, volume, contract`
- `tick-size file per market with roll_time_utc, old_contract, new_contract and spread`

**Argues:** Defines Prompt 1 system setup, reproducibility rules, and raw data inputs.

### [00:16:10](https://www.youtube.com/watch?v=z97PnFIPoFg&t=970s) · slide · PROMPT 1 OF 5 - CONTINUED (confidence: high)

**Values (as shown):**

- `3 / 16`
- `CLEAN AND CHECK`
- `Convert to America/New_York. A session runs 18:00 to 17:00 ET...`
- `Audit every file... duplicate timestamps, time jumps of more than 1 minute during liquid hours (09:30-16:00 ET)...`
- `WINDOWS`
- `Warm-up: 2021-10-01 to 2021-12-31`
- `Discovery: 2022-01-03 to 2024-07-31 (Era 1: 2022, era 2: 2023 to July 2024)`
- `Sealed: 2024-08-01 to the last day of the data (2024-10-16 here)`

**Argues:** Defines strict chronological data windows and cleaning procedures.

### [00:16:11](https://www.youtube.com/watch?v=z97PnFIPoFg&t=971s) · slide · PROMPT 1 OF 5 - CONTINUED (confidence: high)

**Values (as shown):**

- `4 / 16`
- `CHARTS`
- `Build 5m, 15m, 1h, 4h and daily bars from 1-minute bars...`
- `Wilder's 14-bar ATR`
- `THE DIALS`
- `Ten setups: level bounce, breakout, flip zone, trend pullback, trend line, break of structure continuation, change of character reversal, sweep and reclaim, supply and demand zone, fair value gap.`
- `Six setup charts: 5m, 15m, 1h, 4h, daily...`
- `Ten detector dials: peak and valley strength of 2, 3, 5 or 8...`
- `clusters of swings within 0.1, 0.25 or 0.5 ATR, needing 1 to 4 touches...`
- `supply and demand zones from runs of 2 to 5 candles covering 1.5 to 3 ATR`

**Argues:** Lists the technical dials and timeframe definitions for all price action rules.

### [00:16:13](https://www.youtube.com/watch?v=z97PnFIPoFg&t=973s) · slide · PROMPT 1 OF 5 - CONTINUED (confidence: high)

**Values (as shown):**

- `5 / 16`
- `Shared dials: direction; confirmation... stop: touch wick, last swing or gap's middle candle (buffer 0, 0.1, 0.25 ATR); target: 1R, 2R, 3R, next level, last swing...`
- `Filters: trend agrees, skip choppy days, skip 3 or 5 day run...`
- `The lab counted 20,265,402,666,000.`
- `DONE WHEN: The audit, session counts per window, sealed manifest and guard tests all pass...`

**Argues:** Details shared trade dials, filters, and total combinatorial space count.

### [00:16:14](https://www.youtube.com/watch?v=z97PnFIPoFg&t=974s) · slide · PROMPT 2 OF 5 / Engine and level tests (confidence: high)

**Values (as shown):**

- `6 / 16`
- `WHAT THIS BUILDS: The trade engine, and the behavior tests...`
- `RULES: One master seed for every draw... No look-ahead: a trigger bar sees only setup-chart bars that have closed.`

**Argues:** Specifies execution engine rules and verification tests against look-ahead bias.

### [00:16:16](https://www.youtube.com/watch?v=z97PnFIPoFg&t=976s) · slide · PROMPT 2 OF 5 - CONTINUED (confidence: high)

**Values (as shown):**

- `7 / 16`
- `THE ENGINE:`
- `One contract per trade... one position at a time per strategy...`
- `Costs on every trade: $4 commission per round trip, plus 1 tick of slippage...`
- `NQ 0.25: point $20, point ES: 0.25 tick, $50 a point.`
- `Sharpe is the mean over the standard deviation of daily P&L, times the square root of 252.`

**Argues:** Specifies execution pricing, transaction costs, slippage, and Sharpe calculation.

### [00:16:18](https://www.youtube.com/watch?v=z97PnFIPoFg&t=978s) · slide · PROMPT 2 OF 5 - CONTINUED (confidence: high)

**Values (as shown):**

- `8 / 16`
- `ENGINE CHECKS: 20,000 market entries at random discovery minutes with a 1R stop and a 2R target: after costs they should lose a little (the lab got -$9.80 a trade).`
- `BEHAVIOR TESTS: swing strength 3 and 0.25 ATR level tolerance... Random lines: move each real level up or down by 1 to 3 ATR...`

**Argues:** Specifies empirical benchmark tests for trade engine integrity and level significance.

### [00:16:20](https://www.youtube.com/watch?v=z97PnFIPoFg&t=980s) · slide · PROMPT 2 OF 5 - CONTINUED (confidence: high)

**Values (as shown):**

- `9 / 16`
- `The tests: real levels against random lines; hold rate by touch count...`
- `Intervals: 2,000 bootstrap resamples of whole sessions, 95% intervals.`
- `Verdict: true when NQ pooled points the claimed way with an interval that excludes zero, ES has the same sign and both eras agree...`

**Argues:** Defines bootstrap validation criteria for statistical significance of price patterns.

### [00:16:22](https://www.youtube.com/watch?v=z97PnFIPoFg&t=982s) · slide · PROMPT 3 OF 5 / The funnel (confidence: high)

**Values (as shown):**

- `10 / 16`
- `WHAT THIS BUILDS: The funnel that runs tens of thousands of strategy versions...`
- `THE VERSIONS: A random sample: 40,000 versions, 4,000 per setup... Only keep versions with at least 40 signals on NQ discovery.`

**Argues:** Specifies sample sizes and minimum signal constraints for initial testing.

### [00:16:23](https://www.youtube.com/watch?v=z97PnFIPoFg&t=983s) · slide · PROMPT 3 OF 5 - CONTINUED (confidence: high)

**Values (as shown):**

- `11 / 16`
- `Six named versions inside it... The lab's grid had 14,016 versions.`
- `A sample of versions as people trade them... The lab drew 47,329.`
- `THE FUNNEL:`
- `1. Enough trades: 38 or more.`
- `2. Made money: net P&L > $0.`
- `3. A Sharpe of 0.5 or more.`

**Argues:** Outlines exact funnel criteria for passing strategies on discovery data.

### [00:16:25](https://www.youtube.com/watch?v=z97PnFIPoFg&t=985s) · slide · PROMPT 3 OF 5 - CONTINUED (confidence: high)

**Values (as shown):**

- `12 / 16`
- `4. Beat matched random trades... 10,000 sets of twins; version passes when fewer than 5% of sets make as much as it did.`
- `5. Held on ES: Sharpe of 0.3 or more.`
- `JUDGE EACH SETUP AS A WHOLE: average daily P&L of all its versions... Sharpe of 0.5 or more...`

**Argues:** Defines twin random trade matching and cross-market verification thresholds.

### [00:16:26](https://www.youtube.com/watch?v=z97PnFIPoFg&t=986s) · slide · PROMPT 4 OF 5 / The final test (confidence: high)

**Values (as shown):**

- `13 / 16`
- `WHAT THIS BUILDS: The final test on data no rule has seen.`
- `INPUTS: sealed final window (2024-08-01 to 2024-10-16)...`
- `RULES: Nothing chosen in discovery changes now... Run once.`

**Argues:** Outlines out-of-sample final test protocol on untouched sealed data.

### [00:16:27](https://www.youtube.com/watch?v=z97PnFIPoFg&t=987s) · slide · PROMPT 4 OF 5 - CONTINUED (confidence: high)

**Values (as shown):**

- `14 / 16`
- `THE RUN: Join discovery bars from 2024-05-01 to warm up detectors...`
- `WHAT HELD UP: Sharpe of 0.5 or more on that market's final window... equal-weight average Sharpe of 0.5 or more.`

**Argues:** Defines success criteria for out-of-sample validation on sealed data.

### [00:16:28](https://www.youtube.com/watch?v=z97PnFIPoFg&t=988s) · slide · PROMPT 5 OF 5 / The dashboard (confidence: high)

**Values (as shown):**

- `15 / 16`
- `WHAT THIS BUILDS: The complete presenter dashboard... every number traced to a saved file.`
- `A single HTML file that works offline... 1920x1080 stage... navy background (#080f1a), cyan and amber accents`

**Argues:** Specifies design and data provenance architecture of the reporting dashboard.

### [00:16:30](https://www.youtube.com/watch?v=z97PnFIPoFg&t=990s) · slide · PROMPT 5 OF 5 - CONTINUED (confidence: high)

**Values (as shown):**

- `16 / 16`
- `CHECKS: A layout check in headless Chrome at 1920x1080 and 1280x720...`
- `Confirm the provenance of every page... DONE WHEN: The provenance check passes on every number...`

**Argues:** Establishes validation checks for dashboard layout and data accuracy.

## Formulas

- [00:16:16](https://www.youtube.com/watch?v=z97PnFIPoFg&t=976s) `Sharpe = (mean(daily_pnl) / std(daily_pnl)) * sqrt(252)`
  - `mean(daily_pnl)`: Mean of daily profit and loss
  - `std(daily_pnl)`: Standard deviation of daily profit and loss
  - `sqrt(252)`: Square root of 252 trading days for annualization

## Strategies

### Quantitative Price Action Framework ([00:01:05](https://www.youtube.com/watch?v=z97PnFIPoFg&t=65s))

**Logic:** Systematizes 10 visual price action setups by standardizing support/resistance levels, trend swings, change of character reversals, and breakout/pullbacks using objective ATR thresholds and candle confirmation rules.

**Entry rules:**
- Level detected when 2 or more price swing points occur within 0.25 ATR.
- Touch registered when price enters within 0.25 ATR of the level.
- Confirmation entry requires a candle close back across the designated level rather than entering on a limit touch.

**Exit rules:**
- Hard stop loss placed past the level or previous swing point (hard stop beat close-based stop in backtesting).
- Target placed based on fixed R-multiples (1R, 1.5R, 2R, 3R, 4R, 5R) or structural swing points.

| parameter | value |
|---|---|
| level_tolerance | 0.25 ATR |
| touch_tolerance | 0.25 ATR |
| tested_timeframes | 1m, 5m, 15m, 1h, 4h, daily |

**Markets/assets:** NQ (Nasdaq 100 futures), ES (E-mini S&P 500 futures)

**Stated performance:** Out of 101,345 tested configurations, 24,879 were profitable after transaction costs, and 8,310 achieved a Sharpe ratio of 0.5 or greater on NQ discovery data.

**Costs/slippage mentioned:** yes — Included real exchange fees and commissions on every trade, slippage modeled on every stop loss, and intra-bar ambiguous target/stop hits treated as full losses.

### 4h Change of Character (CHoCH) Strategy ([00:11:49](https://www.youtube.com/watch?v=z97PnFIPoFg&t=709s))

**Logic:** Enters on a trend reversal signaled by a 4-hour change of character candle close without requiring a prior liquidity sweep.

**Entry rules:**
- Identify trend reversal (CHoCH) on the 4-hour chart
- Enter at the candle close of the CHoCH candle (confirmation candle)
- Do not require a prior liquidity sweep before the change
- Trade only during the New York session (8:00 AM to 4:00 PM ET)
- Skip trades entered directly into an opposing 3+ day run

**Exit rules:**
- Hard stop placed past the last swing high/low
- Target set at 1R (equal in size to the risk taken)

| parameter | value |
|---|---|
| Timeframe | 4-hour |
| Session window | 8:00 AM to 4:00 PM ET |
| Risk to reward ratio | 1:1 (1R) |
| Stop mechanism | Hard stop |

**Markets/assets:** NQ (Nasdaq futures), ES (E-mini S&P 500 futures)

**Stated performance:** +$62,179 on NQ (61 trades, 54% win rate) and +$39,284 on ES across 2 locked out-of-sample years; average NY session version made +$17,041 on NQ.

**Costs/slippage mentioned:** yes — Trading costs and commissions modeled per contract; 4h timeframe incurs ~6% costs relative to gross profit.

### Price Action Mean Reversion / Reversal (4h Change of Character / Sweep & Reclaim) ([00:15:00](https://www.youtube.com/watch?v=z97PnFIPoFg&t=900s))

**Logic:** Enters a trade when price is overstretched beyond swing levels, key zones, or swept liquidity, anticipating reversion to the mean.

**Entry rules:**
- Identified change of character or sweep on 4h/trigger chart.
- Enter at close of trigger candle, limit at level, or stop beyond level upon confirmation (close back, rejection wick, or engulfing).

**Exit rules:**
- Stop loss: touch wick, last swing, or gap middle candle with 0, 0.1, or 0.25 ATR buffer.
- Target: 1R, 2R, 3R, next level, or last swing.
- Exit on opposite change of character or time exit at 16:00.

| parameter | value |
|---|---|
| ATR Length | 14 |
| Swing Peak/Valley Strength | 2, 3, 5, or 8 |
| Level Tolerance | 0.1, 0.25, or 0.5 ATR |

**Markets/assets:** NQ futures, ES futures

**Stated performance:** Described as the only core strategy type that consistently held up across thousands of variations and survived discovery and sealed testing with Sharpe >= 0.5.

**Costs/slippage mentioned:** yes — $4 commission per round trip; 1 tick slippage on market entries, hard stops, close-based stops, and structure exits.

## Tools & data

| name | type | how used |
|---|---|---|
| Claude | platform | Used to generate the quantitative backtesting architecture, translate visual discretionary price action rules into parameterized programmatic code, and orchestrate the testing runs across millions of bars. |
| NQ and ES 1-minute historical futures data | dataset | 5 years of historical 1-minute OHLCV data comprising 3.6 million bars on NQ and ES futures used for backtesting 101,345 strategy versions, including a 2-year out-of-sample holdout on ES. |
| Skool | platform | Host platform for the creator's trading community focusing on AI-assisted algorithmic trading systems. |
| NQ (E-mini / Micro Nasdaq 100 Futures) | dataset | Primary discovery and out-of-sample locked backtesting dataset. |
| ES (E-mini S&P 500 Futures) | dataset | Secondary out-of-sample testing market for cross-market validation. |
| Python | platform | Scripting language and virtual environment used to build the data pipeline, backtest engine, and tests. |
| ChatGPT / Claude | platform | LLMs used to ingest sequential prompts and generate the Python research lab code. |
| NQ & ES Continuous Futures | dataset | 1-minute continuous front-month futures bars from 2021-10-01 to 2024-10-16 for warm-up, discovery, and sealed evaluation. |
| Headless Chrome | other | Used for automated layout checks of the HTML dashboard at 1920x1080 and 1280x720 resolutions. |

## Open questions

- [00:06:20](https://www.youtube.com/watch?v=z97PnFIPoFg&t=380s) **Over 327 million simulated trades were run across 3.6M 1-minute bars with realistic slippage and execution costs in a few sessions.** — The exact computational execution stack, programming language/backtester code, and specific dollar amounts assumed for commissions and slippage ticks are not detailed.
- [00:07:10](https://www.youtube.com/watch?v=z97PnFIPoFg&t=430s) **8,310 versions achieved a Sharpe ratio of 0.5+.** — The clip does not yet report whether these 8,310 profitable versions retained profitability and Sharpe performance when evaluated on the out-of-sample 2-year ES holdout data.
- [00:08:34](https://www.youtube.com/watch?v=z97PnFIPoFg&t=514s) **Random lines were drawn and scored the exact same way as real support/resistance levels.** — The precise mathematical algorithm used to generate the random lines and determine touches is not detailed in the clip.
- [00:10:41](https://www.youtube.com/watch?v=z97PnFIPoFg&t=641s) **Waiting for a confirmation candle provided a +$719 edge per year on NQ.** — The specific definition of what constitutes a valid 'confirmation candle' is not formally specified.
