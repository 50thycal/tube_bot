# Claude Tested 100,000 Price Action Strategies (Here’s What Works)

**Channel:** AI Pathways  
**URL:** https://www.youtube.com/watch?v=z97PnFIPoFg  
**Duration:** 00:17:10

<sub>schema 1.0 · model gemini-3.8-flash · analyzed 2026-10-29T11:15:43Z · 4 windows · 129,600 tokens</sub>

## Summary

[00:00:00–00:05:00] This video clip introduces a large-scale quantitative backtest of classical price action trading concepts using Claude to build and run test systems. Analyzing five years of one-minute data across NQ and ES futures representing over 327 million simulated trades across 101,345 system configurations, the presenter defines key price action mechanics (support/resistance levels, trend break of structure, change of character, sweeps, confirmation, stops, and targets), examines how subjective discretionary chart interpretations are formalized into objective testable rules, and highlights initial findings such as the strength of the change of character setup and the 50% reversal rate of liquidity sweeps.

[00:05:00–00:10:00] This clip evaluates price action trading concepts using backtests across 5 years of 1-minute NQ and ES futures data covering 327 million simulated trades across 101,345 rule variations. The analysis demonstrates that win rate does not track overall profitability (correlation 0.27), trading lower timeframes like the 1-minute chart is penalized heavily by costs (46% of gross profit), support and resistance levels demonstrably hold better than random lines (51.1% vs 42.4%), more touches do not make a level stronger, and flip zones provide significant positive predictive edge (+11.5 percentage points).

[00:10:00–00:15:00] This clip evaluates price action trading concepts using backtests on historical and unseen locked-forward futures data (NQ and ES). The author analyzes trend setups, trigger mechanisms, stop-loss types, context filters, and timeframe performance, finding that higher timeframes (4-hour and daily), 4-hour change-of-character (CHoCH) reversals without sweeps, hard stops, New York trading hours, and confirmation candles produce positive results, while close-based stops and daily trend alignment filters detract from edge.

[00:15:00–00:17:10] In this final segment, the presenter emphasizes that across extensive backtesting—including 9,000 algorithmic strategies, ICT sweep fades, and price action 4-hour change-of-character setups—mean reversion consistently emerges as the sole foundational principle that holds up. He then shares the five sequential prompts of his 'Price Action Lab' architecture, allowing viewers to build, automate, and rigorously backtest these systems in Python using LLMs like Claude Code or ChatGPT without look-ahead bias or overfitting.

## Segments

### [00:00:00](https://www.youtube.com/watch?v=z97PnFIPoFg&t=0s)–00:01:05 · Overview of the 100,000+ Price Action Concept Test

- Tested over 100,000 price action concept variations using Claude to determine what actually works versus fancy indicators.
- Ran 40,000 exploratory samples plus thousands of common configurations across nearly 5 years of 1-minute data on NQ and ES futures.
- Simulated over 327 million trades to eliminate reliance on anecdotal single-trader claims.
- Presenter background: studied Math and Econ at UCLA, worked in investment banking at Raymond James for 3+ years, and spent 2 years building trading systems.

### [00:01:05](https://www.youtube.com/watch?v=z97PnFIPoFg&t=65s)–00:03:24 · Core Price Action Concepts and Preliminary Findings

- Price action is defined as trading directly off the chart itself without secondary indicators.
- Levels (support and resistance) beat random lines on timeframes from 5-minute to daily.
- Trend is defined as series of higher highs and higher lows; a break of structure occurs when price closes above the last high.
- Trend continuation showed no statistically meaningful follow-through on any chart timeframe tested.
- Change of Character (CHoCH) occurs when price breaks and closes below the last higher low; this held up as the best-performing setup, especially on the 4-hour timeframe.
- Sweeps (wicking past a key high or low where stop-losses sit and closing back inside) reversed only about half the time (~50%), meaning it functions as a secondary signal rather than a standalone edge.
- Confirmation (e.g., waiting for a candle close rather than entering with a limit order at the level) beat limit entries on NQ.
- Hard stops beat close-based stops; on the profit-target side, there was no measurable edge across variations.
- Higher timeframes consistently yielded more profitable strategy variations.

### [00:03:24](https://www.youtube.com/watch?v=z97PnFIPoFg&t=204s)–00:03:59 · The Ten Price Action Setups Tested

- Identified 10 primary setups: Level bounce, Breakout, Flip zone, Trend pullback, Trend line, Break of structure, Change of character, Sweep and reclaim, Supply and demand, and Fair value gap.
- Promotion of the presenter's AI trading community on Skool covering stocks, options, crypto, and futures, and 1-on-1 trading system development.

### [00:03:59](https://www.youtube.com/watch?v=z97PnFIPoFg&t=239s)–00:05:00 · Testing Methodology: Overcoming 'Drawn By Eye' Discretion

- Traditional price action trading suffers from subjectivity ('drawn by eye') where different traders draw different levels on the exact same chart.
- Algorithmic rules applied to define discretionary elements: Level requires 2+ swings within 0.25 ATR; Touch defined as within 0.25 ATR of the level; Confirmation defined as a close back across it.
- Parameter space spans 20.3 trillion theoretical combinations across specific 'dials': touches, line vs. zone, confirmation, stop logic, target logic, chart timeframe, and filters.
- Tested 40,000 dial spreads (4,000 per setup) plus 61,345 common configurations (0 to 2 filters) totaling 101,345 tested model versions.
- Evaluation gauntlet includes real transaction costs, slippage on every stop, treating ambiguous candles as losses, benchmarking against random lines and random trades, cross-checking on ES, and a 2-year locked-away out-of-sample dataset.

### [00:05:00](https://www.youtube.com/watch?v=z97PnFIPoFg&t=300s)–00:06:59 · Backtest Setup and Testing Scale

- Parameter space contains 20.3 trillion possible versions across different dials (touches, line/zone, confirmation, stop, target, chart, filters).
- Ran 40,000 randomized versions (4,000 per setup across 10 setups) plus 61,345 common versions (usual settings, 0 to 2 filters), totaling 101,345 tested strategy versions.
- Data consists of 5 years of 1-minute bars on NQ and ES futures (3.6 million bars, 327 million simulated trades).
- Backtesting system built in Python via Claude with 'The Gauntlet': real costs, slippage on every trade/step, ambiguous bars treated as losses, comparisons against random lines and random trades, and a 2-year out-of-sample lock on ES.

### [00:06:59](https://www.youtube.com/watch?v=z97PnFIPoFg&t=419s)–00:07:24 · Discovery Funnel Results

- Out of 101,345 tested versions, 88,986 generated enough trades (30+) to be graded.
- 24,879 of 101,345 versions (~24.5%) made money after trading costs in NQ discovery.
- 8,310 versions (~8.2%) cleared a Sharpe ratio threshold of 0.5+.

### [00:07:24](https://www.youtube.com/watch?v=z97PnFIPoFg&t=444s)–00:07:52 · Win Rate vs Profit Analysis

- Claims of 80%+ win rates in price action trading are largely unfounded; only 138 of 40,000 strategies reached an 80%+ win rate.
- 67 of the 138 strategies achieving an 80%+ win rate relied on a 1R profit target.
- Across all 40,000 strategies, win rate showed weak correlation with profit (correlation coefficient of 0.27).

### [00:07:52](https://www.youtube.com/watch?v=z97PnFIPoFg&t=472s)–00:08:29 · Timeframe Performance and Cost Friction

- Costs eat up 46.0% of gross profit on the 1-minute timeframe versus only 3.9% on the Daily timeframe.
- Percentage of profitable versions increases from 32% on 1-minute to 47% on Daily.
- Median annual PnL per contract is -$428k on 1m, -$308k on 5m, -$210k on 15m, -$4k on 1h, +$3k on 4h, and +$6k on Daily.
- Trading higher timeframes (1h, 4h, Daily) requires less trading edge because overhead costs and slippage represent a much smaller percentage of gross gains.

### [00:08:29](https://www.youtube.com/watch?v=z97PnFIPoFg&t=509s)–00:09:41 · Support & Resistance Validity and Touch Count Myth

- Real horizontal support/resistance levels held 51.1% of touches across 5m to Daily charts compared to 42.4% for random lines (+8.7 points outperformance on NQ, +8.5 points on ES).
- Testing the myth that 'more touches equal stronger levels': 1 touch beat random lines by +9.0 points, 2 touches by +7.8 points, 3 touches by +8.2 points, and 4 touches by +6.1 points.
- Levels touched 3+ times bounced less frequently (19.2% vs 20.5%) and broke through more often (27.8% vs 26.1%) compared to 1 touch.

### [00:09:41](https://www.youtube.com/watch?v=z97PnFIPoFg&t=581s)–00:10:00 · Level Rules and Flip Zones Edge

- Testing various level rules: Touch count showed -1.1 pts effect; Wall at 3+ touches showed -1.3 pts; Weaker pushes showed +0.4 pts; Box vs line showed +0.5 pts.
- Flip zones (prior resistance becoming support or vice versa) outperformed random baselines by +11.5 percentage points on NQ and +10.9 percentage points on ES.

### [00:10:00](https://www.youtube.com/watch?v=z97PnFIPoFg&t=600s)–00:10:11 · Level Rules and Flip Zones

- Flip zones outperformed other level rules, adding +11.5 percentage points overall and +10.9 points on ES.
- Touch count (-1.1 pts) and wall at 3+ touches (-1.3 pts) reduced performance.
- The speaker concludes flip zones are the strongest and most important concept in price action besides basic support and resistance.

### [00:10:11](https://www.youtube.com/watch?v=z97PnFIPoFg&t=611s)–00:10:33 · Trend Setups: BOS vs CHoCH and Sweeps

- Break of structure (-0.04 ATR) and change of character (-0.05 ATR) do not predict price follow-through on their own.
- Among trend setups, only change of character (CHoCH) reversal had a positive median profit (+$61), while BOS continuation (-$328), sweep and reclaim (-$368), and trend line (-$479) were negative.
- Testing the conventional rule of waiting for a sweep before a change of character lost -$834 on unseen locked data, whereas taking the CHoCH without a sweep made +$903.

### [00:10:34](https://www.youtube.com/watch?v=z97PnFIPoFg&t=634s)–00:10:59 · Trigger: Confirmation Tax vs Limit Orders

- Waiting for a candle confirmation gives up 4.3 points of price entry relative to a limit order at the touch.
- Despite worse execution price, waiting for confirmation increased edge by +$719 per year on Nasdaq futures (-$373 loss vs -$1,093 loss for limit at touch).

### [00:10:59](https://www.youtube.com/watch?v=z97PnFIPoFg&t=659s)–00:11:19 · Exit Types: Hard Stop vs Close-Based Stop

- Close-based stops (exiting only when a candle closes beyond the level) win more frequently (40% vs 29%), but result in larger losses.
- Overall, close-based stops cost $132 more per year (-$290 vs -$158 for hard stops), meaning a plain hard stop performs better.

### [00:11:19](https://www.youtube.com/watch?v=z97PnFIPoFg&t=679s)–00:11:29 · Context Filters: Trading Hours, Run Skips, and Daily Trend

- Trading only during New York session hours (8:00 AM to 4:00 PM ET) improved performance by +$270 per year on unseen NQ.
- Skipping trades after 3+ day directional runs improved performance by +$246.
- Filtering trades to align with the daily trend hurt performance significantly (-$587).

### [00:11:29](https://www.youtube.com/watch?v=z97PnFIPoFg&t=689s)–00:11:55 · Consistency Check: Setups Passing Both NQ and ES

- Across 40,000 tested variants and common versions, only the 4-hour change of character (CHoCH) passed in both NQ and ES markets across all sets.
- On NQ, 4h CHoCH returned +$4,025/year (original) and +$4,884/year (common versions). On ES, it returned +$4,146/year (original) and +$3,374/year (common versions).

### [00:11:55](https://www.youtube.com/watch?v=z97PnFIPoFg&t=715s)–00:12:31 · Timeframe Ladder in Final Locked Window

- The final test window (2025-2026) experienced a 22.5% selloff and a 74.5% rally.
- Strategy profitability correlates directly with higher timeframes: 1m made money on 9.2% of versions, 5m on 20.3%, 15m on 28.8%, 1h on 37.7%, 4h on 45.1%, and Daily on 47.9%.
- On NQ specifically, 45% of 4h versions made money versus only 9% of 1m versions.

### [00:12:31](https://www.youtube.com/watch?v=z97PnFIPoFg&t=751s)–00:13:15 · Best 4h Setup Performance on Locked Data

- The best version (4h CHoCH, no sweep, candle close entry, hard stop past last swing, 1:1 risk-to-reward) earned +$62,179 on 1 NQ contract and +$39,284 on ES over 2 locked years.
- NQ locked-period stats: 61 trades, 54% win rate.
- Robustness test: 39 of 48 usual setting versions (81%) and 66% of 314 common versions made money on NQ; 54.5% made money on ES.
- Average New York session version made +$17,041 per contract and remained profitable even excluding the 10 best days.

### [00:13:16](https://www.youtube.com/watch?v=z97PnFIPoFg&t=796s)–00:15:00 · Summary of Surviving Price Action Principles and Example Trade

- Seven rules survived: (1) 4h CHoCH, (2) higher timeframe charts, (3) New York session only, (4) skip trades into 3+ day runs, (5) confirmation candle on NQ, (6) hard stop instead of close-based, (7) no sweep required before the change.
- Walkthrough of an example trade on NQ 4h from July 11, 2024 showing entry at close, swing-high stop, and 1:1 target.
- Comparison with previous channel studies: 9,000 strategies (mean reversion), ICT (fading the sweep), and price action (4h CHoCH).

### [00:15:00](https://www.youtube.com/watch?v=z97PnFIPoFg&t=900s)–00:15:56 · What Kept Working: Mean Reversion as the Baseline

- In the 9,000 strategies test, mean reversion was the only strategy type that held up across thousands of variations.
- In the ICT test, the only version that held up was fading the sweep, which is fundamentally a mean-reversion strategy.
- The 4-hour change-of-character setup is a reversal setup that also operates as a mean-reversion strategy.
- The core concept is that when price stretches too high or too low, it reverts.
- These test results represent 'the floor, not the ceiling'—a foundational baseline averaged across one contract per trade, meant to have risk management and position sizing layered on top.

### [00:15:56](https://www.youtube.com/watch?v=z97PnFIPoFg&t=956s)–00:16:49 · Build It Yourself: The Five Prompts Framework

- Viewers can replicate the entire testing framework by running five sequential prompts in Claude Code or ChatGPT.
- Prompt 1 (Data and dials): sets up Python venv, data ingestion (NQ/ES 1-minute continuous front-month data, sha256 hashing), cleaning, warm-up (2021-10-01 to 2021-12-31), discovery (2022-01-03 to 2024-07-31), and sealed out-of-sample window (from 2024-08-01 onward), plus multi-timeframe bar creation and dial specifications (over 20 trillion combinations).
- Prompt 2 (Engine and level tests): builds the single-contract trade engine with explicit costs ($4 commission per round trip, 1 tick slippage on market/stops), checks (including 20,000 random entries losing ~$9.80/trade), and behavior tests on levels and patterns against random baselines.
- Prompt 3 (The funnel): tests 40,000 random configurations, 14,016 grid versions, and 47,320 trader-style samples across a 5-step filter (trade count >= 30, win rate > 50%, Sharpe >= 0.5, beat 10,000 twin random trades at p < 0.05, hold on ES with Sharpe >= 0.3).
- Prompt 4 (The final test): unseals the held-out test data once with an access log guard, verifying hashed configurations and evaluating final candidates without modifying any dials.
- Prompt 5 (The dashboard): generates a 1920x1080 static HTML presentation dashboard with full data provenance checks where every on-screen number traces to a saved file.

### [00:16:49](https://www.youtube.com/watch?v=z97PnFIPoFg&t=1009s)–00:17:10 · Conclusion and Outro

- The presenter emphasizes that any trading style based on intuition can be codified into rules and tested at scale with real data.
- Channel outro call to action (like, comment, subscribe, community link, and 1-on-1 booking link).

## Claims

| ts | claim | evidence | caveats |
|---|---|---|---|
| [00:00:29](https://www.youtube.com/watch?v=z97PnFIPoFg&t=29s) | Trend continuation (break of structure) shows no statistically valid follow-through on any chart timeframe. | backtest |  |
| [00:02:02](https://www.youtube.com/watch?v=z97PnFIPoFg&t=122s) | Change of character (CHoCH) held up the best out of all tested price action concepts, performing best on the 4-hour chart. | backtest | Specific Sharpe ratio, win rate, and return numbers are not detailed in this introductory segment. |
| [00:02:24](https://www.youtube.com/watch?v=z97PnFIPoFg&t=144s) | Liquidity sweeps reverse only about half the time (~50%) and lack standalone edge without additional confluence. | backtest | Can be helpful as a confluence signal but not as an independent core entry system. |
| [00:03:00](https://www.youtube.com/watch?v=z97PnFIPoFg&t=180s) | Support and resistance levels beat random lines across timeframes from the 5-minute to daily charts. | backtest |  |
| [00:07:28](https://www.youtube.com/watch?v=z97PnFIPoFg&t=448s) | Price action strategies rarely achieve 80%+ win rates, and win rate is poorly correlated with total profit. | backtest | 67 of the 138 high win-rate strategies used 1R targets, which skew win rate at the expense of payoff ratio. |
| [00:08:03](https://www.youtube.com/watch?v=z97PnFIPoFg&t=483s) | Friction from trading costs and slippage severely impairs 1-minute strategies compared to higher timeframes. | backtest | Assumes standard futures commissions and slippage on every trade step. |
| [00:08:42](https://www.youtube.com/watch?v=z97PnFIPoFg&t=522s) | Support and resistance levels have genuine statistical validity over random lines. | backtest | Tested across timeframes from 5-minute to Daily on NQ and ES futures. |
| [00:09:01](https://www.youtube.com/watch?v=z97PnFIPoFg&t=541s) | Repeated touches do not make a support or resistance level stronger; levels with 4 touches hold less frequently than levels with 1 touch. | backtest | Specific individual setups may succeed, but the aggregate tendency over 300M+ trades shows diminished holding rates with additional touches. |
| [00:09:53](https://www.youtube.com/watch?v=z97PnFIPoFg&t=593s) | Flip zones hold significantly better on first retest than ordinary support and resistance levels. | backtest | Evaluated on first retest after a breakout. |
| [00:10:04](https://www.youtube.com/watch?v=z97PnFIPoFg&t=604s) | Flip zones are the strongest and most effective price action level concept. | backtest |  |
| [00:10:15](https://www.youtube.com/watch?v=z97PnFIPoFg&t=615s) | Break of structure and change of character on their own do not move price or predict price direction. | backtest |  |
| [00:10:26](https://www.youtube.com/watch?v=z97PnFIPoFg&t=626s) | Requiring a liquidity sweep before a change of character setup loses money in out-of-sample data. | backtest | Tested over two locked out-of-sample years on index futures. |
| [00:10:46](https://www.youtube.com/watch?v=z97PnFIPoFg&t=646s) | Waiting for a confirmation candle rather than entering at the touch with a limit order improves net performance despite giving up 4.3 points of price. | backtest | Observed specifically on Nasdaq futures (NQ). |
| [00:11:08](https://www.youtube.com/watch?v=z97PnFIPoFg&t=668s) | Close-based stops achieve a higher win rate (40% vs 29%) but result in larger losses and poorer overall performance than hard stops. | backtest |  |
| [00:11:26](https://www.youtube.com/watch?v=z97PnFIPoFg&t=686s) | Filtering trades to align with the daily trend significantly hurts price action setup performance. | backtest |  |
| [00:12:06](https://www.youtube.com/watch?v=z97PnFIPoFg&t=726s) | Price action strategies have a substantially higher likelihood of being profitable on higher timeframes (4h, Daily) than on 1m or 5m charts. | backtest |  |
| [00:15:01](https://www.youtube.com/watch?v=z97PnFIPoFg&t=901s) | Mean reversion was the only strategy style that held up across 9,000 strategy variations, ICT sweep fading, and price action change-of-character tests. | backtest | Performance figures represent the baseline 'floor' averaged across all unoptimized versions with 1 contract per trade, before adding sizing or risk management. |
| [00:16:18](https://www.youtube.com/watch?v=z97PnFIPoFg&t=978s) | A random entry baseline of 20,000 trades with a 1R ATR stop and 2R target loses approximately -$9.80 per trade after costs. | backtest | Measured on discovery data with $4 commission and 1 tick slippage applied. |

## Visuals

### [00:00:16](https://www.youtube.com/watch?v=z97PnFIPoFg&t=16s) · slide · The Price Action Setup (confidence: high)

**Axes / columns:** Concept; Finding / Annotation

**Values (as shown):**

- `2 / 66`
- `levels, trend, entry, exit`
- `1 level - beat random lines, 5m to daily`
- `2 trend - x no follow-through, any chart`
- `break of structure`
- `3 change of character - best setup, on the 4h`
- `4 sweep - x reversed about half the time`
- `5 confirmation - beat a limit at the level (NQ)`
- `6 stop and target - hard stop beat close-based, target side: no edge`
- `THE SIX CHARTS: 1m, 5m, 15m, 1h, 4h, daily`
- `higher chart, more versions made money`

**Argues:** Summarizes the high-level findings across the 6 major components of classical price action setups.

### [00:00:29](https://www.youtube.com/watch?v=z97PnFIPoFg&t=29s) · slide · How We Tested It (confidence: high)

**Axes / columns:** Category; Parameters / Metrics

**Values (as shown):**

- `6 / 66`
- `THE DIALS: touches, line or zone, confirmation, stop, target, chart, filters`
- `20.3 trillion possible versions`
- `WHAT WE RAN: 40,000 spread across every dial, 4,000 per setup`
- `61,345 common versions: usual settings, 0 to 2 filters`
- `101,345 total`
- `THE NAMED VERSIONS: Bare Minimum, Checklist, Entry Model, Zone System, Sweep System, Daily Version`
- `THE DATA: 5 years, 3.6M 1-minute bars, NQ + ES, 327M simulated trades`
- `THE GAUNTLET: real costs, every trade; slippage on every stop; ambiguous candle = a loss; vs random lines; vs random trades; checked on ES; 2 years locked away`

**Argues:** Shows the backtesting scale, parameter permutation scope (20.3T), executed sample sizes (101,345), and robustness checks applied.

### [00:00:37](https://www.youtube.com/watch?v=z97PnFIPoFg&t=37s) · slide · The Ten Setups (confidence: high)

**Axes / columns:** Setup Number; Setup Name; Description

**Values (as shown):**

- `3 / 66`
- `the ten we tested`
- `1. Level bounce - buy support, sell resistance`
- `2. Breakout - trade the close through a level`
- `3. Flip zone - old resistance becomes support`
- `4. Trend pullback - buy the first dip in an uptrend`
- `5. Trend line - buy a touch of the rising line`
- `6. Break of structure - go with the break of the last swing`
- `7. Change of character - the first break against the trend`
- `8. Sweep and reclaim - a wick through a low, closed back above`
- `9. Supply and demand - the first return to an impulse's base`
- `10. Fair value gap - the first return into a three-candle gap`

**Argues:** Defines the 10 standard price action patterns subjected to systematic backtesting.

### [00:04:12](https://www.youtube.com/watch?v=z97PnFIPoFg&t=252s) · slide · Drawn By Eye (confidence: high)

**Axes / columns:** Chart Label; Rule Category; Algorithmic Rule

**Values (as shown):**

- `5 / 66`
- `same chart, different lines`
- `NQ 15m, Jul 7, 2023, discovery`
- `AS RULES`
- `Level: 2+ swings within 0.25 ATR`
- `Touch: within 0.25 ATR of the level`
- `Confirmation: a close back across it`
- `Trader A: limit at the touch`
- `Trader B: close back across`

**Argues:** Illustrates how subjective human line drawing leads to conflicting trades and demonstrates the mathematical ATR-based rules used to formalize levels.

### [00:05:00](https://www.youtube.com/watch?v=z97PnFIPoFg&t=300s) · slide · How We Tested It (confidence: high)

**Axes / columns:** THE DIALS; WHAT WE RAN; THE DATA; THE GAUNTLET

**Values (as shown):**

- `6 / 55`
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
- `THE DATA: 5 years, 3.6M 1-minute bars, NQ + ES, 327M simulated trades`
- `THE GAUNTLET: real costs, every trade; slippage on every step; ambiguous candle = a loss; vs random lines; vs random trades; checked on ES; 2 years locked away`

**Argues:** Summarizes the rigorous quantitative methodology and parameter space used to test price action trading rules at institutional scale.

### [00:06:59](https://www.youtube.com/watch?v=z97PnFIPoFg&t=419s) · chart · Funnel (confidence: high)

**Axes / columns:** Funnel Stage; Original 40,000; Common versions

**Values (as shown):**

- `8 / 55`
- `All 101,346 versions through each stage, NQ discovery`
- `All: 101,345`
- `Enough trades to grade (30+): 88,986`
- `Profitable: 24,879`
- `Sharpe 0.5+: 8,310`
- `101,345 TESTED`
- `24,879 MADE MONEY AFTER COSTS`
- `24,879 of the 101,345 versions made money after costs in discovery, and 8,310 had a Sharpe of 0.5+`

**Argues:** Demonstrates the proportion of price action strategies that remain profitable and produce viable risk-adjusted returns after trade costs.

### [00:07:24](https://www.youtube.com/watch?v=z97PnFIPoFg&t=444s) · chart · Win Rate And Profit (confidence: high)

**Axes / columns:** X-axis: WIN RATE; Y-axis: Result per contract per year (k$)

**Values (as shown):**

- `9 / 55`
- `40,000 strategies by win rate and result per contract per year, NQ discovery`
- `5R`
- `4R`
- `3R`
- `Next`
- `2R`
- `1.5R`
- `1R`
- `Y-axis ticks: -$20k, -$10k, $0, $10k, $20k, $30k`
- `X-axis ticks: 0%, 20%, 40%, 60%, 80%, 100%`
- `138 WIN 80%+`
- `0.27 CORRELATION`
- `67 of the 138 use a 1R target`
- `138 strategies won 80%+ of their trades; across all 40,000 win rate barely tracks profit (correlation 0.27)`

**Argues:** Proves that win rate has very low correlation with annual net profit and that 80%+ win rates are rare anomalies that mostly stem from small 1R targets.

### [00:07:52](https://www.youtube.com/watch?v=z97PnFIPoFg&t=472s) · chart · Timeframes (confidence: high)

**Axes / columns:** Timeframe (1m, 5m, 15m, 1h, 4h, Daily); PROFITABLE VERSIONS; COSTS / GROSS PROFIT; MEDIAN PER YEAR

**Values (as shown):**

- `10 / 55`
- `All 40,000 by setup chart, NQ discovery`
- `PROFITABLE VERSIONS: 1m: 32%, 5m: 36%, 15m: 44%, 1h: 46%, 4h: 47%, Daily: 47%`
- `COSTS / GROSS PROFIT: 1m: 46%, 5m: 38%, 15m: 24%, 1h: 9%, 4h: 6%, Daily: 4%`
- `MEDIAN PER YEAR: 1m: -$428k, 5m: -$308k, 15m: -$210k, 1h: -$4k, 4h: +$3k, Daily: +$6k`
- `46.0% COSTS ON 1M`
- `3.9% COSTS ON DAILY`
- `Costs take 46.0% of gross profit on the 1m chart and 3.9% on daily`

**Argues:** Shows that lower timeframes fail largely because execution friction and transaction costs consume a huge fraction of gross profits.

### [00:08:29](https://www.youtube.com/watch?v=z97PnFIPoFg&t=509s) · chart · Random Lines (confidence: high)

**Axes / columns:** Chart timeframe (All, 5m, 15m, 1h, 4h, Daily); Real levels; Random lines; Share of touches that hold (%)

**Values (as shown):**

- `11 / 55`
- `Share of touches that hold, real levels vs random lines, NQ discovery`
- `All: Real levels 51%, Random lines 42%`
- `5m: Real levels 52%, Random lines 43%`
- `15m: Real levels 50%, Random lines 43%`
- `1h: Real levels 48%, Random lines 40%`
- `4h: Real levels 47%, Random lines 38%`
- `Daily: Real levels 51%, Random lines 33%`
- `+8.7 pts NQ`
- `+8.5 pts ES`
- `SURVIVED REAL levels hold 51.1% of touches against 42.4% for random lines, on every chart from 5m to daily`

**Argues:** Provides empirical evidence that horizontal support and resistance levels hold significantly better than chance across all tested timeframes.

### [00:08:50](https://www.youtube.com/watch?v=z97PnFIPoFg&t=530s) · chart · Touch Count (confidence: high)

**Axes / columns:** Number of touches (1 touch, 2 touches, 3 touches, 4 touches); Holding advantage vs random lines (percentage points)

**Values (as shown):**

- `12 / 55`
- `How much better than random lines a level holds, by number of touches`
- `1 touch: +9.0 pts`
- `2 touches: +7.8 pts`
- `3 touches: +8.2 pts`
- `4 touches: +6.1 pts`
- `+9.0 pts ONE TOUCH`
- `+6.1 pts FOUR TOUCHES`
- `DIDN'T SURVIVE A level touched four times held no better than a level touched once; levels touched 3+ times bounced a bit less and broke through a bit more`
- `3+ touches vs 1 touch: bounced 19.2% vs 20.5%, broke and kept going 27.8% vs 26.1%`

**Argues:** Disproves the common price action heuristic that more touches make support/resistance stronger.

### [00:09:42](https://www.youtube.com/watch?v=z97PnFIPoFg&t=582s) · chart · Level Rules (confidence: high)

**Axes / columns:** Rule; Percentage points vs comparison (95% intervals)

**Values (as shown):**

- `13 / 55`
- `Each rule against its comparison, percentage points, 95% intervals`
- `Touch count: -1.1 pts`
- `Wall at 3+ touches: -1.3 pts`
- `Weaker pushes: +0.4 pts`
- `Box vs line: +0.5 pts`
- `Flip zones: +11.5 pts`
- `+11.5 pts FLIP ZONES`
- `+10.9 pts FLIP ZONES, ES`
- `Flip zones hold; touch count, walls and weaker pushes do not`

**Argues:** Isolates the predictive power of various level rules, showing flip zones provide strong statistical edge while touch-count rules degrade performance.

### [00:10:00](https://www.youtube.com/watch?v=z97PnFIPoFg&t=600s) · chart · Level Rules (confidence: high)

**Axes / columns:** Rule; Percentage points, 95% intervals (-5 to +10)

**Values (as shown):**

- `Touch count: -1.1 pts`
- `Wall at 3+ touches: -1.3 pts`
- `Weaker pushes: +0.4 pts`
- `Box vs line: +0.5 pts`
- `Flip zones: +11.5 pts`
- `+11.5 pts FLIP ZONES`
- `+10.9 pts FLIP ZONES, ES`
- `Flip zones hold; touch count, walls and weaker pushes do not`
- `13 / 67`

**Argues:** Flip zones provide a massive statistical advantage over touch counts and walls at support/resistance.

### [00:10:11](https://www.youtube.com/watch?v=z97PnFIPoFg&t=611s) · chart · Follow-Through (confidence: high)

**Axes / columns:** Break type; ATR (-0.40 to +0.40)

**Values (as shown):**

- `Break of structure: -0.04 ATR`
- `Change of character: -0.05 ATR`
- `-0.04 ATR BREAK OF STRUCTURE`
- `-0.05 ATR CHANGE OF CHARACTER`
- `DIDN'T SURVIVE Neither break moved price on its own`
- `15 / 67`

**Argues:** Neither BOS nor CHoCH alone yields positive directional follow-through measured in ATR.

### [00:10:18](https://www.youtube.com/watch?v=z97PnFIPoFg&t=618s) · chart · Trend Setups (confidence: high)

**Axes / columns:** Setup; Median Profit/Loss ($)

**Values (as shown):**

- `BOS continuation: -$328`
- `CHoCH reversal: +$61`
- `Sweep and reclaim: -$368`
- `Trend line: -$479`
- `+$61, +$47 CHOCH MEDIAN`
- `Only the change of character had a positive median`
- `16 / 67`

**Argues:** Only CHoCH reversal had a positive median among classic trend trading setups.

### [00:10:22](https://www.youtube.com/watch?v=z97PnFIPoFg&t=622s) · chart · Trend Trades As Taught (confidence: high)

**Axes / columns:** Setup variation; Performance ($)

**Values (as shown):**

- `Trend line, first to second low: -$586`
- `Reversal flip: -$417`
- `Sweep, then change: -$834`
- `Change, no sweep needed: +$903`
- `Late entry on a 5m break: -$2,608`
- `+$903 NO SWEEP, UNSEEN`
- `-$834 AFTER A SWEEP`
- `Only the change of character without a sweep made money`
- `17 / 67`

**Argues:** Conventional teachings that require a liquidity sweep before a trend reversal underperform simple CHoCH entries without a sweep.

### [00:10:34](https://www.youtube.com/watch?v=z97PnFIPoFg&t=634s) · chart · Confirmation Tax (confidence: high)

**Axes / columns:** Entry method; Performance ($)

**Values (as shown):**

- `Limit at the touch: -$1,093`
- `After confirmation: -$373`
- `+$719 EDGE PER YEAR`
- `4.3 POINTS GIVEN UP`
- `SURVIVED Waiting for confirmation lost less than a limit at the touch`
- `18 / 67`

**Argues:** Waiting for confirmation improves performance by $719/year despite giving up 4.3 index points.

### [00:10:59](https://www.youtube.com/watch?v=z97PnFIPoFg&t=659s) · chart · Stops (confidence: high)

**Axes / columns:** Stop method; Performance ($)

**Values (as shown):**

- `Hard stop: -$158`
- `Close-based stop: -$290`
- `-$132 CLOSE STOPS, PER YEAR`
- `DIDN'T SURVIVE Close-based stops cost $132 a year more`
- `19 / 67`

**Argues:** Close-based stops cost more money annually than conventional hard stops.

### [00:11:19](https://www.youtube.com/watch?v=z97PnFIPoFg&t=679s) · chart · Context (confidence: high)

**Axes / columns:** Filter condition; Performance ($)

**Values (as shown):**

- `New York only (8am to 4pm ET): +$270`
- `Skip 3+ day runs: +$246`
- `Daily trend agrees: -$587`
- `+$270 NEW YORK ONLY, UNSEEN NQ`
- `-$587 DAILY TREND, UNSEEN NQ`
- `New York hours and skipping 3+ day runs helped. The daily trend filter hurt`
- `22 / 67`

**Argues:** New York session filtering and avoiding multi-day extended runs improve returns, while filtering by daily trend drastically hurts returns.

### [00:11:29](https://www.youtube.com/watch?v=z97PnFIPoFg&t=689s) · table · Passed On Both Markets (confidence: high)

**Axes / columns:** Market (NQ, ES); Subset (Original 40,000, Common Versions); Strategy Name; A YEAR ($)

**Values (as shown):**

- `NQ / Original 40,000 / change of character 1h: +$1,208`
- `NQ / Original 40,000 / change of character 4h: +$4,025`
- `NQ / Common versions / change of character 4h: +$4,884`
- `NQ / Common versions / flip zone daily: +$9,093`
- `ES / Original 40,000 / change of character 4h: +$4,146`
- `ES / Common versions / change of character 4h: +$3,374`
- `ES / Common versions / breakout daily: +$1,734`
- `4 of 4 CHOCH 4H PASSED IN EACH SET AND ON EACH MARKET`
- `Only the 4h change of character passed on both markets`
- `23 / 67`

**Argues:** The 4h change of character was the only setup that consistently passed across both NQ and ES in all tested sets.

### [00:11:55](https://www.youtube.com/watch?v=z97PnFIPoFg&t=715s) · chart · Final Window (confidence: high)

**Axes / columns:** Time (2025 - 2026); Price (16,000 to 30,000)

**Values (as shown):**

- `22,235`
- `17,232`
- `30,078`
- `-22.5% SELLOFF`
- `+74.5% RALLY`
- `The locked years held a 22.5% drop and a 74.5% rally`
- `24 / 67`

**Argues:** The locked forward test window was a rigorous testing ground containing both a severe selloff (-22.5%) and a large rally (+74.5%).

### [00:12:02](https://www.youtube.com/watch?v=z97PnFIPoFg&t=722s) · chart · Timeframe Ladder (confidence: high)

**Axes / columns:** Timeframe (1m, 5m, 15m, 1h, 4h, Daily); Percentage making money (0% to 50%)

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
- `25 / 67`

**Argues:** Profitability rate increases monotonically with higher timeframes.

### [00:12:31](https://www.youtube.com/watch?v=z97PnFIPoFg&t=751s) · chart · Best Version (confidence: high)

**Axes / columns:** Time (2023 - 2026); Account Equity ($0k to $300k)

**Values (as shown):**

- `+$62,179 LOCKED YEARS, NQ`
- `+$39,284 LOCKED YEARS, ES`
- `61 trades on NQ, 54% winners`
- `Picked in discovery, it made money on both markets in the locked years`
- `29 / 67`

**Argues:** The best 4h CHoCH model produced stable equity curves in out-of-sample locked data across both NQ and ES.

### [00:13:06](https://www.youtube.com/watch?v=z97PnFIPoFg&t=786s) · table · The 4h Setup (confidence: high)

**Axes / columns:** Metric / Segment; Result

**Values (as shown):**

- `39 of 48 versions on its usual settings made money, NQ`
- `66% of all 314 common versions made money, NQ`
- `+$17,041 New York session versions, average per contract (original 40,000, NQ), still made money without their 10 best days`
- `54.5% of the common versions made money on ES`
- `In the original 40,000, most of the gain came from a few big days`
- `30 / 67`

**Argues:** The 4h CHoCH setup demonstrates robust performance across a large swath of parameter variations.

### [00:13:16](https://www.youtube.com/watch?v=z97PnFIPoFg&t=796s) · slide · What Survived (confidence: high)

**Axes / columns:** Rule Number; Rule Description

**Values (as shown):**

- `1 Change of character, 4h chart`
- `2 Higher charts (made money: 9% on 1m, 48% on daily (common versions, unseen NQ))`
- `3 New York session only`
- `4 Skip trades into a 3+ day run`
- `5 Confirmation candle (NQ)`
- `6 Hard stop, not close-based`
- `7 No sweep before the change`
- `33 / 67`

**Argues:** Summarizes the seven robust price action trading rules identified by the study.

### [00:14:22](https://www.youtube.com/watch?v=z97PnFIPoFg&t=862s) · chart · Example Trade (confidence: high)

**Axes / columns:** Time (Jul 2 - Jul 18, 2024); Price (19,600 to 21,000)

**Values (as shown):**

- `NQ 4h, July 11, 2024`
- `Trend`
- `Change of character`
- `Stop`
- `Entry`
- `Target`
- `34 / 67`

**Argues:** Visual demonstration of the exact 4h CHoCH execution: trend break, entry at candle close, hard stop at swing high, and 1:1 risk-to-reward target.

### [00:14:50](https://www.youtube.com/watch?v=z97PnFIPoFg&t=890s) · slide · What We Keep Finding (confidence: high)

**Axes / columns:** Study; Finding

**Values (as shown):**

- `9,000 strategies: mean reversion`
- `ICT: fading the sweep`
- `Price action: the 4h change of character`
- `the floor, not the ceiling`
- `35 / 67`

**Argues:** The empirical findings across various trading styles consistently point to mean reversion and reversal behaviors as robust baseline edges.

### [00:15:00](https://www.youtube.com/watch?v=z97PnFIPoFg&t=900s) · slide · WHAT SURVIVED / What We Keep Finding (confidence: high)

**Values (as shown):**

- `35 / 67`
- `9,000 strategies / mean reversion`
- `ICT / fading the sweep`
- `Price action / the 4h change of character`
- `the floor, not the ceiling`

**Argues:** Summarizes the consistent finding across all tests that mean-reversion setups survive backtesting.

### [00:15:56](https://www.youtube.com/watch?v=z97PnFIPoFg&t=956s) · slide · PRICE ACTION LAB · THE FIVE PROMPTS / Build it yourself (confidence: high)

**Axes / columns:** Prompt Number; Title; Page

**Values (as shown):**

- `1 / 16`
- `1 Data and dials page 2`
- `2 Engine and level tests page 6`
- `3 The funnel page 10`
- `4 The final test page 13`
- `5 The dashboard page 15`
- `screenshot these and run them in order, one at a time`
- `paste each block into Claude Code, in order, one at a time`

**Argues:** Provides the overview structure of the five prompts required to build the automated price action lab.

### [00:16:02](https://www.youtube.com/watch?v=z97PnFIPoFg&t=962s) · slide · PROMPT 1 OF 5 / Data and dials (confidence: high)

**Values (as shown):**

- `2 / 16`
- `WHAT THIS BUILDS: A Python research lab that turns price action trading rules into exact rules a computer can test on NQ and ES futures...`
- `RULES: Work in one project folder with a Python virtual environment. Save every result as a file, and log each decision and its reason in decisions.md. Fix a master seed... The final window stays sealed... Never move a threshold after seeing a result...`
- `INPUTS: 1-minute NQ and ES continuous front-month futures... Copy each unchanged into data/raw/ and record its sha256... ts_event, open, high, low, close, volume, contract...`

**Argues:** Specifies environment setup, data ingestion rules, and cryptographic hashing for Prompt 1.

### [00:16:09](https://www.youtube.com/watch?v=z97PnFIPoFg&t=969s) · slide · PROMPT 1 OF 5 · CONTINUED (confidence: high)

**Values (as shown):**

- `3 / 16`
- `CLEAN AND CHECK: Convert to America/New_York. Session 18:00 to 17:00 ET dated by end day. Audit duplicates, inverted high/low, missing minutes, 17:00 halt hour drop. Back-adjusted bars for signals/fills. No entries 60m before roll. News calendar of CPI, Jobs report, FOMC.`
- `WINDOWS: Warm-up: 2021-10-01 to 2021-12-31; Discovery: 2022-01-03 to 2024-07-31 (Era 1: 2022, Era 2: 2023 to July 2024); Final: 2024-08-01 to latest (data 2026-10-16 here) sealed with sha256 manifest and file reader guard.`

**Argues:** Specifies data cleaning protocols, session times, and strict train/discovery/sealed out-of-sample date windows.

### [00:16:11](https://www.youtube.com/watch?v=z97PnFIPoFg&t=971s) · slide · PROMPT 1 OF 5 · CONTINUED (confidence: high)

**Values (as shown):**

- `4 / 16`
- `CHARTS: Build 5m, 15m, 1h, 4h and daily bars from 1-minute bars from 18:00 open. 4h bars: 18-22, 22-02, 02-06, 06-10, 10-14, 14-17 ET. Higher timeframe bar usable only from its close. ATR is Wilder's 14-bar ATR.`
- `THE DIALS: Ten setups: level bounce, breakout, flip zone, trend pullback, trend line, break of structure continuation, change of character reversal, sweep and reclaim, supply and demand zone, fair value gap.`
- `Six setup charts (5m, 15m, 1h, 4h, daily) with trigger charts. Swing strength 2, 3, 5, 8. Level clusters within 0.1, 0.25, 0.5 ATR (1-4 touches). Supply/demand zones 2-5 candles covering 1.5-3 ATR. Three-candle FVG.`

**Argues:** Defines multi-timeframe bar creation and parameterizes 10 price action setups into granular dials.

### [00:16:13](https://www.youtube.com/watch?v=z97PnFIPoFg&t=973s) · slide · PROMPT 1 OF 5 · CONTINUED (confidence: high)

**Values (as shown):**

- `5 / 16`
- `Shared dials: direction (confirmation, none, close back, rejection wick, engulfing, either candle, lower-chart break of structure); entry (close of trigger bar, limit, stop, closed-base stop); buffer 0, 0.1, 0.25 ATR; target 1R, 1.5R, 2R, 3R, 5R, 10R, next swing, hold, CHoCH; time exit 16:00, 16:40, 24 or 96 bars.`
- `Filters: trend agrees, skip choppy days, skip direction of 3/5 day run, fresh breakouts, news days, session (all, London/NY, NY open 08:30-11:00, NY open 09:30-11:00), pullback depth, gap confluence.`
- `Total valid combinations: 20,265,402,668,000.`

**Argues:** Details shared execution dials and filters, showing the theoretical search space spans 20.26 trillion valid versions.

### [00:16:14](https://www.youtube.com/watch?v=z97PnFIPoFg&t=974s) · slide · PROMPT 2 OF 5 / Engine and level tests (confidence: high)

**Values (as shown):**

- `6 / 16`
- `WHAT THIS BUILDS: Trade engine and behavior tests asking whether price respects levels, flips, breaks, sweeps, gaps, zones more than chance.`
- `INPUTS: Cleaned 1m bars of NQ and ES in discovery window, derived MTF bars with ATR, roll times, news days, detectors.`
- `RULES: Master seed, no look-ahead bias (unit test: mock detector run on cut data must equal full run).`

**Argues:** Sets requirements for the backtesting engine and anti-lookahead unit tests.

### [00:16:16](https://www.youtube.com/watch?v=z97PnFIPoFg&t=976s) · slide · PROMPT 2 OF 5 · CONTINUED (confidence: high)

**Values (as shown):**

- `7 / 16`
- `THE ENGINE: 1 contract per trade (half-size on news, 1 position at a time per strategy). No overnight hold unless flat at 16:00. Every fill/exit checked on 1m bars.`
- `Costs: $4 commission round trip, 1 tick slippage on market entries, hard stops, close stops, structure exits. No slippage on limits, targets, time exits, roll exits.`
- `Limit fills only when 1m bar trades 1 tick through. Hard stop exits 1 tick worse than stop or open. Ambiguous candle (stop and target hit in same 1m bar) counts as loss.`
- `Tick sizes: NQ: $20/point; ES: 0.25 tick, $50/point. Sharpe is mean over standard deviation of daily P&L times sqrt(252).`

**Argues:** Defines explicit fill logic, execution constraints, transaction costs, and tick math for realistic backtesting.

### [00:16:18](https://www.youtube.com/watch?v=z97PnFIPoFg&t=978s) · slide · PROMPT 2 OF 5 · CONTINUED (confidence: high)

**Values (as shown):**

- `8 / 16`
- `ENGINE CHECKS: Unit tests on made-up price paths; 20,000 market entries at random discovery minutes with 1R ATR stop and 2R target lose -$9.80/trade after costs; intentional look-ahead cheat test makes money.`
- `BEHAVIOR TESTS: Measure price action after events vs random stand-in on NQ and ES (5m, 15m, 1h, 4h, daily). Swing strength 3, 0.25 ATR tolerance.`
- `Random lines: move real levels up/down 1 to 3 ATR (>=0.5 ATR from real level); random remedies with 20 random bars.`

**Argues:** Establishes sanity-check benchmarks and behavior statistical tests against randomized levels.

### [00:16:20](https://www.youtube.com/watch?v=z97PnFIPoFg&t=980s) · slide · PROMPT 2 OF 5 · CONTINUED (confidence: high)

**Values (as shown):**

- `9 / 16`
- `THE TESTS: real levels against random lines; hold rate by touch count; shrinking bounces; wick vs close through level; flip zones; follow-through at 10, 20, 50 bars; sweeps; trend lines; FVG; supply/demand zones; pullback depth; rejection candles.`
- `Intervals: 2,000 bootstrap resamples of whole sessions, 95% intervals.`
- `Verdict: true when NQ interval excludes zero, ES agrees in sign, and both eras agree; split when partly holds; false otherwise.`

**Argues:** Defines statistical bootstrapping and multi-era criteria to evaluate whether price action concepts have an edge.

### [00:16:22](https://www.youtube.com/watch?v=z97PnFIPoFg&t=982s) · slide · PROMPT 3 OF 5 / The funnel (confidence: high)

**Values (as shown):**

- `10 / 16`
- `WHAT THIS BUILDS: Funnel filtering hundreds of thousands of strategy versions.`
- `THE VERSIONS: Random set of 40,000 versions (4,000 per setup), requiring >=40 signals on NQ discovery.`

**Argues:** Outlines candidate generation across the search space.

### [00:16:23](https://www.youtube.com/watch?v=z97PnFIPoFg&t=983s) · slide · PROMPT 3 OF 5 · CONTINUED (confidence: high)

**Values (as shown):**

- `11 / 16`
- `Six named versions: Bare Minimum, Daily Version, Checklist, Sweep System, Trend System, Ultra-Safe.`
- `Grid of usual settings: 14,016 versions.`
- `Trader sample: 47,320 versions (40% no filter, 40% 1 filter, 20% 2 filters).`
- `THE FUNNEL: 1. Trades >= 30; 2. Win rate > 50%; 3. Sharpe >= 0.5.`

**Argues:** Defines the test batches and initial filter thresholds.

### [00:16:25](https://www.youtube.com/watch?v=z97PnFIPoFg&t=985s) · slide · PROMPT 3 OF 5 · CONTINUED (confidence: high)

**Values (as shown):**

- `12 / 16`
- `4. Beat matched random trades: 10,000 sets of twin random trades; pass when <5% of sets match performance.`
- `5. Hold on ES: profitable on ES discovery with Sharpe >= 0.3.`
- `Final-test candidate: passes 1 to 4, profitable in both eras (2022 and 2023-2024), holds on ES.`
- `JUDGE SETUP: Average daily P&L across all versions with equal weight; profitable per year, Sharpe >= 0.5, profitable in 2022 and 2023-24.`

**Argues:** Defines advanced filter steps (Monte Carlo twin test and cross-asset validation on ES) to eliminate curve-fitting.

### [00:16:26](https://www.youtube.com/watch?v=z97PnFIPoFg&t=986s) · slide · PROMPT 4 OF 5 / The final test (confidence: high)

**Values (as shown):**

- `13 / 16`
- `WHAT THIS BUILDS: Final test on sealed data (NQ and ES 1m bars from 2024-08-01).`
- `RULES: No dial or threshold changes. Check sha256 hashes. Rehearse on shifted last month of discovery. Single logged unlock.`

**Argues:** Specifies strict out-of-sample testing protocols preventing data snooping.

### [00:16:27](https://www.youtube.com/watch?v=z97PnFIPoFg&t=987s) · slide · PROMPT 4 OF 5 · CONTINUED (confidence: high)

**Values (as shown):**

- `14 / 16`
- `THE RUN: Warm up detectors from 2024-05-01. Score on NQ and ES over final window with identical costs and fill logic.`
- `WHAT HELD UP: Version held up if profitable after costs with Sharpe >= 0.5. Setup held up if equal-weight average made money per year with Sharpe >= 0.5.`

**Argues:** Specifies execution and success criteria on the held-out final test period.

### [00:16:29](https://www.youtube.com/watch?v=z97PnFIPoFg&t=989s) · slide · PROMPT 5 OF 5 / The dashboard (confidence: high)

**Values (as shown):**

- `15 / 16`
- `WHAT THIS BUILDS: Presentation dashboard with full provenance tracking.`
- `RULES: Every number on screen must trace to a saved file. Provenance file records source file, row, column, format, and displayed text. Double read verification. Facecam cutout 520x368 px.`
- `PAGE: Offline static HTML, 1920x1080 stage, navy background (#0b0f1a), cyan and amber accents.`

**Argues:** Details UI dashboard generation and data integrity verification for results presentation.

### [00:16:31](https://www.youtube.com/watch?v=z97PnFIPoFg&t=991s) · slide · PROMPT 5 OF 5 · CONTINUED (confidence: high)

**Values (as shown):**

- `16 / 16`
- `Each finding gets a page: eyebrow section, title, one-line subtitle, 1 chart, max 2 big stats, conclusion badge ('survived, split or didn't survive').`
- `Checks in headless Chrome at 1920x1080 and 1280x720. Provenance check must pass on every number.`

**Argues:** Specifies automated QA testing for visual presentation slides.

## Formulas

- [00:16:16](https://www.youtube.com/watch?v=z97PnFIPoFg&t=976s) `Sharpe = (mean(daily P&L) / std(daily P&L)) * sqrt(252)`
  - `mean(daily P&L)`: Mean of daily strategy profit and loss across trading sessions
  - `std(daily P&L)`: Standard deviation of daily strategy profit and loss
  - `sqrt(252)`: Annualization factor corresponding to the square root of 252 trading days per year

## Strategies

### Change of Character (CHoCH) ([00:01:53](https://www.youtube.com/watch?v=z97PnFIPoFg&t=113s))

**Logic:** Identifies the first structural break against an established trend (e.g. price closing below the prior higher low in an uptrend) to enter in the direction of the trend reversal.

**Entry rules:**
- In an uptrend, wait for price to close below the most recent higher low swing level.
- Enter on candle confirmation closing past the level.

**Exit rules:**
- Hard stop-loss placed beyond the swing high.

| parameter | value |
|---|---|
| Timeframe | 4h (noted as best setup timeframe) |

**Markets/assets:** NQ, ES

**Stated performance:** Identified as holding up the best out of all price action findings.

**Costs/slippage mentioned:** yes — Backtested with real costs on every trade and slippage on every stop.

### Algorithmic Level Support/Resistance Bounce ([00:04:12](https://www.youtube.com/watch?v=z97PnFIPoFg&t=252s))

**Logic:** Identifies horizontal support/resistance levels mathematically using ATR cluster rules and trades the bounce upon confirmation.

**Entry rules:**
- Identify level where 2 or more swings occur within 0.25 ATR of each other.
- Price touches within 0.25 ATR of the level.
- Confirmation candle closes back across the level.

**Exit rules:**
- Hard stop-loss beat close-based stop; profit targets showed no edge.

| parameter | value |
|---|---|
| Swing proximity threshold | 0.25 ATR |
| Touch proximity threshold | 0.25 ATR |

**Markets/assets:** NQ, ES

**Stated performance:** Beat random lines from 5m to daily timeframes; confirmation entry beat limit orders on NQ.

**Costs/slippage mentioned:** yes — Tested against gauntlet with real costs, slippage on every stop, and ambiguous candles counted as losses.

### Price Action Support/Resistance & Flip Zones ([00:05:00](https://www.youtube.com/watch?v=z97PnFIPoFg&t=300s))

**Logic:** Trading bounces or breakouts from identified horizontal support/resistance levels and flip zones (broken resistance becoming support or vice versa).

**Entry rules:**
- Price touches a defined support/resistance level or flip zone.
- Optional confirmation candle or filter as parameterized.

**Exit rules:**
- Stop-loss placed past the level or last swing.
- Target exit based on fixed R-multiple (e.g. 1R, 1.5R, 2R, 3R, 4R, 5R) or next structure level.

| parameter | value |
|---|---|
| Touches | 1 to 4+ touches |
| Level representation | Line or Zone (box) |
| Chart timeframes | 1m, 5m, 15m, 1h, 4h, Daily |
| Profit Target | 1R to 5R or Next structure level |

**Markets/assets:** NQ (Nasdaq futures), ES (S&P 500 futures)

**Stated performance:** 24,879 of 101,345 versions were profitable after costs; flip zones hold +11.5 pts over random on NQ and +10.9 pts on ES.

**Costs/slippage mentioned:** yes — Full trading commissions deducted on every trade, slippage applied on every execution step, ambiguous intraday bars counted as full losses.

### 4-Hour Change of Character Reversal (Best Version) ([00:12:31](https://www.youtube.com/watch?v=z97PnFIPoFg&t=751s))

**Logic:** Enter a mean reversion/reversal trade following a Change of Character (CHoCH) on a 4-hour chart without requiring a preceding liquidity sweep.

**Entry rules:**
- Identify an established trend on the 4-hour chart.
- Wait for a Change of Character (first candle close in the opposite direction breaking market structure).
- No prior liquidity sweep required.
- Enter at the close of the confirming 4-hour candle (optionally restricted to New York session: 8:00 AM - 4:00 PM ET; avoid trading in the direction of an extended 3+ day run).

**Exit rules:**
- Place a hard stop immediately beyond the last swing extreme (e.g., swing high for a short setup). Do not use a close-based stop.
- Set profit target at 1:1 risk-to-reward (target size equals risk size).

| parameter | value |
|---|---|
| Timeframe | 4h |
| Risk-to-Reward Ratio | 1:1 |
| Session Filter | New York session only (8:00 AM to 4:00 PM ET) |
| Trend Run Filter | Skip trades into a 3+ day run |

**Markets/assets:** NQ (Nasdaq 100 E-mini futures), ES (S&P 500 E-mini futures)

**Stated performance:** +$62,179 on NQ (61 trades, 54% win rate) and +$39,284 on ES over 2 locked years per contract.

**Costs/slippage mentioned:** no

### 4h Change of Character Reversal (Mean Reversion) ([00:15:00](https://www.youtube.com/watch?v=z97PnFIPoFg&t=900s))

**Logic:** Reversal mean-reversion setup where price stretches excessively on the 4-hour chart and triggers an entry upon a change of character (first close past the last swing high/low).

**Entry rules:**
- Price stretches too high or too low.
- Change of character confirmed by the first close past the last swing on the 4-hour chart (or lower trigger chart).

**Exit rules:**
- Take profit targets set at 1R, 1.5R, 2R, 3R, 5R, 10R or next swing.
- Stop loss set beyond the level or swing point with 0 to 0.25 ATR buffer.
- Time exit at 16:00, 16:40, or after 24/96 bars.

| parameter | value |
|---|---|
| chart_timeframe | 4h |
| swing_strength | 3 |
| atr_level_tolerance | 0.25 ATR |

**Markets/assets:** NQ futures, ES futures

**Stated performance:** Serves as an average baseline ('floor') that held up across thousands of tested iterations.

**Costs/slippage mentioned:** yes — $4 commission per round trip, 1 tick slippage on market entries and stop exits.

## Tools & data

| name | type | how used |
|---|---|---|
| Claude | other | Used to generate and build out the code and backtesting engine infrastructure to systematically test 101,345 price action parameter configurations.; Used as the LLM coding agent to build the multi-layer backtesting engine and process large-scale trading simulations. |
| CME E-mini S&P 500 (ES) & E-mini Nasdaq-100 (NQ) 1-Minute Historical Data | dataset | 5 years of historical 1-minute bar data (3.6 million bars) used to simulate 327 million trades across backtest iterations, including a 2-year locked out-of-sample period. |
| Skool | platform | Community platform hosting the presenter's AI trading community covering stocks, options, crypto, and futures. |
| NQ 1-minute historical data | dataset | 5 years of historical 1-minute futures bars (approx. 3.6 million bars) used as the discovery dataset for testing strategy variations. |
| ES 1-minute historical data | dataset | Used for out-of-sample validation and testing, including a 2-year locked-away out-of-sample partition. |
| E-mini Nasdaq-100 Futures (NQ) | dataset | Used for backtesting and out-of-sample forward evaluation of price action rules and setups. |
| E-mini S&P 500 Futures (ES) | dataset | Used for cross-market validation of price action setups across discovery and locked-out years. |
| Claude Code | platform | CLI tool/LLM interface into which the five prompts are pasted sequentially to generate the backtesting codebase. |
| ChatGPT / Claude | platform | Alternative LLM platforms mentioned for running the prompt sequence. |
| NQ & ES continuous front-month 1-minute futures data | dataset | Raw 1-minute parquet/csv price series used for backtesting, bar aggregation, and out-of-sample validation. |
| Python virtual environment (venv) | other | Project workspace isolation to run backtesting scripts, logging, and data audits. |
| Headless Chrome | other | Automated visual check of the dashboard at 1920x1080 and 1280x720 resolutions. |

## Open questions

- [00:00:29](https://www.youtube.com/watch?v=z97PnFIPoFg&t=29s) **Trend continuation (break of structure) shows no follow-through on any chart.** — The specific metric used to measure 'follow-through' (e.g., MFE/MAE ratio, fixed R-multiple, or forward bar return) is not detailed.
- [00:02:06](https://www.youtube.com/watch?v=z97PnFIPoFg&t=126s) **Change of character (CHoCH) performed the best out of all setups, specifically on the 4-hour timeframe.** — No exact numerical win rate, profit factor, Sharpe ratio, or drawdown metrics are provided in this clip.
- [00:02:28](https://www.youtube.com/watch?v=z97PnFIPoFg&t=148s) **Sweeps reverse only about half the time (~50%).** — The exact definition of a reversal (in terms of tick distance, ATR multiple, or timeframe) is not specified.
- [00:05:46](https://www.youtube.com/watch?v=z97PnFIPoFg&t=346s) **Specific parameter definitions for 'checklist', 'entry model', 'zone system', and 'sweep system' named versions.** — Exact quantitative threshold definitions for the named versions shown on the slide are not detailed in this clip.
- [00:08:34](https://www.youtube.com/watch?v=z97PnFIPoFg&t=514s) **How random lines were generated and calibrated relative to volatility and price range.** — The specific algorithmic distribution used to draw and score the random comparison lines is not fully specified.
- [00:12:31](https://www.youtube.com/watch?v=z97PnFIPoFg&t=751s) **The 4h CHoCH setup produced +$62,179 on NQ and +$39,284 on ES over two locked years.** — Transaction costs, exchange fees, and execution slippage are not explicitly stated or factored into the dollar results shown.
- [00:13:06](https://www.youtube.com/watch?v=z97PnFIPoFg&t=786s) **In the original 40,000 variations, most of the gain came from a few big days.** — No detailed distribution or kurtosis metrics of returns are provided to evaluate the dependency on outlier events.
