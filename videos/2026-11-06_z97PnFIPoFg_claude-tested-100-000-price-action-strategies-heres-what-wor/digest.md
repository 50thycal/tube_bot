# Claude Tested 100,000 Price Action Strategies (Here’s What Works)

**Channel:** AI Pathways  
**URL:** https://www.youtube.com/watch?v=z97PnFIPoFg  
**Duration:** 00:17:11

<sub>schema 1.0 · model gemini-3.8-flash · interactions · analyzed 2026-11-06T03:33:16Z · 105,022 tokens</sub>

## Summary

Brendan presents a large-scale algorithmic evaluation of classical price action trading concepts coded and backtested using Claude across 5 years of 1-minute futures data (NQ and ES, totaling 327M simulated trades). Testing over 101,345 rule variations across 10 setups, the study reveals that most price action setups fail on lower timeframes due to transaction costs and lack of edge, while higher timeframes (4h and Daily) show viability. The single most robust configuration surviving locked out-of-sample data is a 4-hour Change of Character (CHoCH) reversal trade with a hard stop, fixed 1:1 risk-to-reward target, New York session filtering, and no pre-condition sweep.

## Segments

### [00:00:00](https://www.youtube.com/watch?v=z97PnFIPoFg&t=0s)–00:01:05 · Introduction and Scope of the Price Action Test

- Tested over 100,000 price action concepts using Claude to build an automated testing harness.
- Evaluated 40,000 sampled parameter variations plus 61,345 common configurations (101,345 total tested) across 5 years of 1-minute data on NQ and ES futures, generating 327 million simulated trades.
- Presenter background: UCLA math/econ graduate, former Raymond James investment banker for 3+ years, full-time algorithmic trading system builder for 2 years.

### [00:01:05](https://www.youtube.com/watch?v=z97PnFIPoFg&t=65s)–00:03:59 · Core Price Action Concepts and the 10 Setups

- Core mechanics explained: Support/Resistance levels, Trend (higher highs/lows, break of structure), Change of character (CHoCH), Sweeps, Confirmation candles, and Timeframes (1m to Daily).
- The 10 major price action setups tested: Level bounce, Breakout, Flip zone, Trend pullback, Trend line, Break of structure (BOS), Change of character (CHoCH), Sweep and reclaim, Supply and demand, and Fair value gap (FVG).
- Previewed that Change of Character (CHoCH) held up best, while Sweeps alone reversed only about half the time (~50%).

### [00:03:59](https://www.youtube.com/watch?v=z97PnFIPoFg&t=239s)–00:06:59 · Testing Methodology, Funnel, and Data Gauntlet

- Addressed subjectivity in manual chart drawing by turning visual rules into quantifiable dials (touches, line vs. zone, confirmation, stop, target, chart, filters), creating 20.3 trillion theoretical combinations.
- Tested 101,345 concrete versions: 40,000 spread across dials (4,000 per setup) and 61,345 common settings.
- Backtest engine factored in $4 commission per round trip, 1 tick of slippage on entry/market orders, slippage on stops, ambiguous bar losses (if stop and target touched in same minute), and compared against random lines/trades.
- Two full years of ES data were kept completely locked away out-of-sample.
- Funnel results: Out of 101,345 tested, 88,986 had >=30 trades; 24,879 (24.5%) were profitable after costs; only 8,310 (~8.2%) achieved a Sharpe ratio of 0.5+.

### [00:06:59](https://www.youtube.com/watch?v=z97PnFIPoFg&t=419s)–00:08:29 · Win Rate vs. Profit and Timeframe Scaling

- Win rate has a very weak correlation with net annual profit (correlation coefficient = 0.27); only 138 strategies won >=80% of trades, and 67 of those used a tiny 1R or sub-1R target.
- Timeframe analysis shows trading costs consume 46.0% of gross profits on 1-minute charts versus only 3.9% on daily charts.
- Percentage of profitable versions increases from 9.2% on 1m to 47.9% on daily charts.

### [00:08:29](https://www.youtube.com/watch?v=z97PnFIPoFg&t=509s)–00:10:11 · Level Bounce, Touch Counts, and Flip Zones

- Real horizontal support/resistance levels held 51.1% of touches versus 42.4% for random lines (+8.7 pts edge on NQ, +8.5 pts on ES).
- Touching a level more times degraded performance: 1 touch outperformed random by +9.0 pts, while 4 touches only outperformed by +6.1 pts (levels touched 3+ times bounced 19.2% vs 20.5% and broke through 27.8% vs 26.1%).
- Flip zones (old resistance becoming support after a break) were the strongest level rule, beating random lines by +11.5 percentage points on NQ and +10.9 percentage points on ES.

### [00:10:11](https://www.youtube.com/watch?v=z97PnFIPoFg&t=611s)–00:11:55 · Trend Setups, Confirmation, and Stop Types

- Neither Break of Structure (-0.04 ATR) nor CHoCH (-0.05 ATR) produced net follow-through drift on their own.
- As a trade setup, CHoCH was the only trend setup with positive median annual P&L (+$61/yr median vs -$328 for BOS, -$368 for sweep/reclaim, -$478 for trendline).
- Pairing CHoCH with a sweep lost -$834/yr in unseen data, whereas CHoCH without a sweep made +$903/yr.
- Waiting for a confirmation candle gave up 4.3 points of price entry but improved net annual edge by +$719 on NQ.
- Hard stops beat close-based stops: close-based stops cost $132 more per year because the larger tail losses outweighed the slightly higher win rate (40% vs 29%).

### [00:11:55](https://www.youtube.com/watch?v=z97PnFIPoFg&t=715s)–00:15:56 · Final Out-of-Sample Test, Best Strategy, and General Findings

- Context filters: Trading only during New York session (8 AM - 4 PM ET) added +$270/yr; skipping trades into a 3+ day run added +$246/yr; filtering with daily trend hurt performance (-$587/yr).
- In the 2-year locked test (which experienced a -22.5% drawdown and a +74.5% rally), only the 4h CHoCH setup survived across both NQ and ES in 4 of 4 trials.
- The best configuration (4h CHoCH, hard stop, 1:1 risk/reward target, no sweep) made +$62,179 on 1 NQ contract (61 trades, 54% win rate) and +$39,284 on ES over the 2 locked years.
- Reiterated overall pattern: across past testing of 9,000 standard strategies, ICT concepts, and price action, mean-reversion style mechanics (like fading extremes or CHoCH reversals) consistently produce the baseline positive expectancy.

### [00:15:56](https://www.youtube.com/watch?v=z97PnFIPoFg&t=956s)–00:17:11 · System Prompts and Conclusion

- Showed the exact 5-prompt layered specification provided to Claude to construct the data processing engine, behavioral level checks, combinatorial backtester, locked verification window, and visual dashboard.
- Emphasized that visual, discretionary concepts must be converted into programmatic rules and stress-tested across out-of-sample market regimes.

## Claims

| ts | claim | evidence | caveats |
|---|---|---|---|
| [00:07:05](https://www.youtube.com/watch?v=z97PnFIPoFg&t=425s) | Only ~24.5% of tested price action rule sets made money after transaction costs, and only ~8.2% achieved a Sharpe ratio of 0.5 or higher. | backtest | Discovery window on NQ 1-minute data over ~3 years before locked evaluation. |
| [00:07:45](https://www.youtube.com/watch?v=z97PnFIPoFg&t=465s) | Win rate has little correlation to overall strategy profitability (correlation of 0.27). | data | Calculated across 40,000 price action strategy backtests on NQ. |
| [00:08:05](https://www.youtube.com/watch?v=z97PnFIPoFg&t=485s) | Transaction costs consume 46.0% of gross profits on 1-minute bars but only 3.9% on daily bars. | backtest | Assumes $4 round-trip commission and 1 tick slippage per execution. |
| [00:08:42](https://www.youtube.com/watch?v=z97PnFIPoFg&t=522s) | Real support and resistance levels hold 51.1% of touches, outperforming randomly placed horizontal lines which hold 42.4%. | backtest | Measured across 5-minute to daily timeframes on NQ. |
| [00:09:15](https://www.youtube.com/watch?v=z97PnFIPoFg&t=555s) | A level touched 4 or more times holds worse than a level touched only once. | data | Levels touched 3+ times bounced 19.2% vs 20.5% for 1 touch, and broke through 27.8% vs 26.1%. |
| [00:09:55](https://www.youtube.com/watch?v=z97PnFIPoFg&t=595s) | Flip zones hold 11.5 percentage points better than random lines on NQ and 10.9 points better on ES. | data | Based on the first retest of broken prior resistance/support. |
| [00:10:30](https://www.youtube.com/watch?v=z97PnFIPoFg&t=630s) | Requiring a liquidity sweep prior to a Change of Character (CHoCH) entry harms performance (-$834/yr vs +$903/yr without sweep). | backtest | Tested on out-of-sample locked data on NQ. |
| [00:11:00](https://www.youtube.com/watch?v=z97PnFIPoFg&t=660s) | Close-based stops cost $132 more per year than hard stops despite having a higher win rate (40% vs 29%). | backtest | Holding until candle close results in significantly larger tail drawdowns when levels fail cleanly. |
| [00:12:20](https://www.youtube.com/watch?v=z97PnFIPoFg&t=740s) | 45% of price action configurations were profitable on 4-hour charts versus only 9% on 1-minute charts during the locked out-of-sample window. | backtest | Tested over a 2-year locked period containing both a 22.5% drop and a 74.5% rally. |

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
- `5 years, 3.6M 1-minute bars, NQ + ES`
- `327M simulated trades`
- `real costs, every trade`
- `slippage on every stop`
- `ambiguous candle = a loss`
- `vs random lines`
- `vs random trades`
- `checked on ES`
- `2 years locked away`

**Argues:** Summarizes the backtest architecture, combinatorial scope, sample sizing, execution friction assumptions, and validation protocol.

### [00:00:37](https://www.youtube.com/watch?v=z97PnFIPoFg&t=37s) · slide · The Ten Setups (confidence: high)

**Axes / columns:** Setup #; Name; Description

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

**Argues:** Displays the 10 standard price action trade setups codified into rules for the automated test.

### [00:04:12](https://www.youtube.com/watch?v=z97PnFIPoFg&t=252s) · chart · Drawn By Eye (confidence: high)

**Axes / columns:** Price (16,000 to 16,350); Time (03:45 to 09:45); AS RULES

**Values (as shown):**

- `NQ 15m, Jul 7, 2023, discovery`
- `Trader A: limit at the touch`
- `Trader B: close back across`
- `Level: 2+ swings within 0.25 ATR`
- `Touch: within 0.25 ATR of the level`
- `Confirmation: a close back across it`

**Argues:** Demonstrates why discretionary chart drawing leads to conflicting trades and how parameterizing levels into ATR thresholds standardizes testing.

### [00:07:00](https://www.youtube.com/watch?v=z97PnFIPoFg&t=420s) · chart · Funnel (confidence: high)

**Axes / columns:** Stage; Count

**Values (as shown):**

- `All: 101,345`
- `Enough trades to grade (30+): 88,986`
- `Profitable: 24,879`
- `Sharpe 0.5+: 8,310`
- `101,345 TESTED`
- `24,879 MADE MONEY AFTER COSTS`
- `24,879 of the 101,345 versions made money after costs in discovery, and 8,310 had a Sharpe of 0.5+`

**Argues:** Visualizes the steep drop-off in strategy viability as basic filtering, profitability after costs, and risk-adjusted return hurdles are applied.

### [00:07:24](https://www.youtube.com/watch?v=z97PnFIPoFg&t=444s) · chart · Win Rate And Profit (confidence: high)

**Axes / columns:** Win Rate (0% to 100%); Result per contract per year ($0k to $15k); Target multiple (5R to 1R)

**Values (as shown):**

- `138 WIN 80%+`
- `0.27 CORRELATION`
- `67 of the 138 use a 1R target`
- `138 strategies won 80%+ of their trades; across all 40,000 win rate barely tracks profit (correlation 0.27)`

**Argues:** Shows a scatter plot of 40,000 strategies demonstrating that high win rate does not equal high profitability.

### [00:07:52](https://www.youtube.com/watch?v=z97PnFIPoFg&t=472s) · chart · Timeframes (confidence: high)

**Axes / columns:** Metric; Timeframe (1m, 5m, 15m, 1h, 4h, Daily)

**Values (as shown):**

- `PROFITABLE VERSIONS: 1m: 11%, 5m: 32%, 15m: 36%, 1h: 44%, 4h: 46%, Daily: 47%`
- `COSTS / GROSS PROFIT: 1m: 46%, 5m: 40%, 15m: 29%, 1h: 24%, 4h: 9%, Daily: 4%`
- `MEDIAN PER YEAR: 1m: -$306, 5m: -$310, 15m: -$438, 1h: -$420, 4h: -$24, Daily: +$36`
- `46.0% COSTS ON 1M`
- `3.9% COSTS ON DAILY`
- `Costs take 46.0% of gross profit on the 1m chart and 3.9% on daily`

**Argues:** Proves that higher timeframes have drastically lower cost drag and much higher proportions of profitable configurations.

### [00:08:29](https://www.youtube.com/watch?v=z97PnFIPoFg&t=509s) · chart · Random Lines (confidence: high)

**Axes / columns:** Timeframe (All, 5m, 15m, 1h, 4h, Daily); Share of touches that hold (%)

**Values (as shown):**

- `All: Real 51%, Random 42%`
- `5m: Real 52%, Random 43%`
- `15m: Real 50%, Random 43%`
- `1h: Real 48%, Random 40%`
- `4h: Real 47%, Random 38%`
- `Daily: Real 51%, Random 33%`
- `+8.7 pts NQ`
- `+8.5 pts ES`
- `SURVIVED: Real levels hold 51.1% of touches against 42.4% for random lines, on every chart from 5m to daily`

**Argues:** Demonstrates that technical support/resistance levels have genuine statistical persistence over random price levels.

### [00:08:50](https://www.youtube.com/watch?v=z97PnFIPoFg&t=530s) · chart · Touch Count (confidence: high)

**Axes / columns:** Touches (1 touch, 2 touches, 3 touches, 4 touches); Points better than random lines

**Values (as shown):**

- `1 touch: +9.0 pts`
- `2 touches: +7.8 pts`
- `3 touches: +8.2 pts`
- `4 touches: +6.1 pts`
- `3+ touches vs 1 touch: bounced 19.2% vs 20.5%, broke and kept going 27.8% vs 26.1%`
- `DIDN'T SURVIVE: A level touched four times held no better than a level touched once; levels touched 3+ times bounced a bit less and broke through a bit more`

**Argues:** Refutes the conventional technical analysis belief that levels become stronger the more times they are tested.

### [00:09:42](https://www.youtube.com/watch?v=z97PnFIPoFg&t=582s) · chart · Level Rules (confidence: high)

**Axes / columns:** Rule comparison; Percentage points diff (95% intervals)

**Values (as shown):**

- `Touch count: -1.1 pts`
- `Wall at 3+ touches: -1.3 pts`
- `Weaker pushes: +0.4 pts`
- `Box vs line: +0.5 pts`
- `Flip zones: +11.5 pts`
- `+11.5 pts FLIP ZONES, NQ`
- `+10.9 pts FLIP ZONES, ES`
- `Flip zones hold; touch count, walls and weaker pushes do not`

**Argues:** Compares level-trading rules and highlights Flip Zones as the only strongly positive edge.

### [00:10:11](https://www.youtube.com/watch?v=z97PnFIPoFg&t=611s) · chart · Follow-Through (confidence: high)

**Axes / columns:** Break Type; Follow-through (ATR)

**Values (as shown):**

- `Break of structure: -0.04 ATR`
- `Change of character: -0.05 ATR`
- `DIDN'T SURVIVE: Neither break moved price on its own`

**Argues:** Shows that trend breaks do not produce positive forward drift unconditionally.

### [00:10:18](https://www.youtube.com/watch?v=z97PnFIPoFg&t=618s) · chart · Trend Setups (confidence: high)

**Axes / columns:** Setup; Annual Median P&L ($)

**Values (as shown):**

- `BOS continuation: -$328`
- `CHoCH reversal: +$61`
- `Sweep and reclaim: -$368`
- `Trend line: -$478`
- `+$61 CHOCH MEDIAN`
- `Only the change of character had a positive median`

**Argues:** Change of character (reversal) is the only trend-based setup that generates positive median returns across tested variants.

### [00:10:22](https://www.youtube.com/watch?v=z97PnFIPoFg&t=622s) · chart · Trend Trades As Taught (confidence: high)

**Axes / columns:** Setup Variant; P&L ($)

**Values (as shown):**

- `Trend line, first to second low: -$586`
- `Reversal flip: -$417`
- `Sweep, then change: -$834`
- `Change, no sweep needed: +$903`
- `Late entry on a 5m break: -$2,608`
- `+$903 NO SWEEP, UNSEEN`
- `-$834 AFTER A SWEEP`
- `Only the change of character without a sweep made money`

**Argues:** Disproves the common ICT/price action advice to wait for a liquidity sweep prior to trading a change of character.

### [00:10:34](https://www.youtube.com/watch?v=z97PnFIPoFg&t=634s) · chart · Confirmation Tax (confidence: high)

**Axes / columns:** Trigger Type; Edge ($ per year)

**Values (as shown):**

- `Limit at the touch: -$1,093`
- `After confirmation: -$373`
- `+$719 EDGE PER YEAR`
- `4.3 POINTS GIVEN UP`
- `SURVIVED: Waiting for confirmation lost less than a limit at the touch`

**Argues:** Waiting for candle confirmation sacrifices 4.3 points of price entry but yields a net +$719 per year advantage over blind limit orders.

### [00:10:59](https://www.youtube.com/watch?v=z97PnFIPoFg&t=659s) · chart · Stops (confidence: high)

**Axes / columns:** Stop Type; P&L per year ($)

**Values (as shown):**

- `Hard stop: -$158`
- `Close-based stop: -$290`
- `-$132 CLOSE STOPS, PER YEAR`
- `DIDN'T SURVIVE: Close-based stops cost $132 a year more`

**Argues:** Shows hard stops strictly beat close-based stops on price action trades.

### [00:11:19](https://www.youtube.com/watch?v=z97PnFIPoFg&t=679s) · chart · Context (confidence: high)

**Axes / columns:** Filter; P&L difference ($)

**Values (as shown):**

- `New York only (8am to 4pm ET): +$270`
- `Skip 3+ day runs: +$246`
- `Daily trend agrees: -$587`
- `+$270 NEW YORK ONLY, UNSEEN NQ`
- `-$587 DAILY TREND, UNSEEN NQ`
- `New York hours and skipping 3+ day runs helped. The daily trend filter hurt`

**Argues:** Shows that session timing and run-skipping improve edge, while filtering by the daily trend hurts performance.

### [00:11:29](https://www.youtube.com/watch?v=z97PnFIPoFg&t=689s) · slide · Passed On Both Markets (confidence: high)

**Axes / columns:** Market; Version Category; Setup; P&L / Year

**Values (as shown):**

- `NQ Original 40,000: change of character 1h (+$1,208), change of character 4h (+$4,025)`
- `ES Original 40,000: change of character 4h (+$4,146)`
- `NQ Common Versions: change of character 4h (+$4,884), flip zone daily (+$9,093)`
- `ES Common Versions: change of character 4h (+$3,374), breakout daily (+$1,734)`
- `4 of 4: CHOCH 4H PASSED IN EACH SET AND ON EACH MARKET`
- `Only the 4h change of character passed on both markets`

**Argues:** Identifies the 4h change of character as the sole setup robust across both instruments and parameter sets.

### [00:11:55](https://www.youtube.com/watch?v=z97PnFIPoFg&t=715s) · chart · Final Window (confidence: high)

**Axes / columns:** Time (2025 to 2026); NQ Price (16,000 to 30,000+)

**Values (as shown):**

- `22,235`
- `17,232`
- `30,078`
- `-22.5% SELLOFF`
- `+74.5% RALLY`
- `The locked years held a 22.5% drop and a 74.5% rally`

**Argues:** Demonstrates the severe stress test conditions in the locked out-of-sample data.

### [00:12:02](https://www.youtube.com/watch?v=z97PnFIPoFg&t=722s) · chart · Timeframe Ladder (confidence: high)

**Axes / columns:** Timeframe (1m, 5m, 15m, 1h, 4h, Daily); % Profitable in locked years

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

**Argues:** Re-confirms in out-of-sample locked data that strategy profitability scales directly with timeframe.

### [00:12:31](https://www.youtube.com/watch?v=z97PnFIPoFg&t=751s) · chart · Best Version (confidence: high)

**Axes / columns:** Date (2023 to 2026); Cumulative P&L ($0k to $300k)

**Values (as shown):**

- `+$62,179 LOCKED YEARS, NQ`
- `+$39,284 LOCKED YEARS, ES`
- `61 trades on NQ, 54% winners`
- `Picked in discovery, it made money on both markets in the locked years`

**Argues:** Shows the equity curve of the 4h CHoCH model through discovery and the 2 locked out-of-sample years.

### [00:13:06](https://www.youtube.com/watch?v=z97PnFIPoFg&t=786s) · slide · The 4h Setup (confidence: high)

**Axes / columns:** Category; Metric / Outcome

**Values (as shown):**

- `39 of 48 versions on its usual settings made money, NQ`
- `66% of all 314 common versions made money, NQ`
- `+$17,041 New York session versions, average per contract (original 40,000, NQ) - still made money without its 10 best days`
- `54.5% of the common versions made money on ES`
- `In the original 40,000, most of the gain came from a few big days`

**Argues:** Demonstrates the statistical robustness of the 4h CHoCH setup across diverse variations and markets.

### [00:13:16](https://www.youtube.com/watch?v=z97PnFIPoFg&t=796s) · slide · What Survived (confidence: high)

**Axes / columns:** Rank / Item; Rule Description

**Values (as shown):**

- `1 Change of character, 4h chart`
- `2 Higher charts (made money: 9% on 1m, 48% on daily, common versions, unseen NQ)`
- `3 New York session only`
- `4 Skip trades into a 3+ day run`
- `5 Confirmation candle (NQ)`
- `6 Hard stop, not close-based`
- `7 No sweep before the change`

**Argues:** Consolidates the 7 surviving principles and configuration rules derived from the 100,000+ tests.

### [00:14:22](https://www.youtube.com/watch?v=z97PnFIPoFg&t=862s) · chart · Example Trade (confidence: high)

**Axes / columns:** NQ 4h price (19,800 to 21,000); Date (Jul 2 - Jul 18, 2024)

**Values (as shown):**

- `Trend`
- `Change of character`
- `Entry`
- `Stop`
- `Target`
- `NQ 4h, July 11, 2024`

**Argues:** Illustrates the exact execution of the winning 4h CHoCH short setup without a prior sweep.

### [00:14:50](https://www.youtube.com/watch?v=z97PnFIPoFg&t=890s) · slide · What We Keep Finding (confidence: high)

**Axes / columns:** Test Project; Winning Core Mechanism

**Values (as shown):**

- `9,000 strategies: mean reversion`
- `ICT: fading the sweep`
- `Price action: the 4h change of character`
- `the floor, not the ceiling`

**Argues:** Synthesizes across multiple video studies that mean reversion and reversal dynamics consistently provide positive trading expectancy.

### [00:15:56](https://www.youtube.com/watch?v=z97PnFIPoFg&t=956s) · code · Build it yourself (confidence: high)

**Axes / columns:** Prompt Step; Description; Page

**Values (as shown):**

- `1 Data and dials - page 2`
- `2 Engine and level tests - page 6`
- `3 The funnel - page 10`
- `4 The final test - page 13`
- `5 The dashboard - page 15`

**Argues:** Table of contents outlining the 5 Claude prompts used to replicate the backtesting pipeline.

## Formulas

- [00:04:12](https://www.youtube.com/watch?v=z97PnFIPoFg&t=252s) `Level tolerance = 0.25 * ATR`
  - `ATR`: Average True Range (Wilder's 14-bar ATR) used to define proximity for swings, touches, and levels
- [00:07:49](https://www.youtube.com/watch?v=z97PnFIPoFg&t=469s) `Correlation(Win Rate, Net Profit) = 0.27`
  - `Correlation`: Pearson correlation coefficient between strategy win rate and annual net P&L per contract
- [00:16:16](https://www.youtube.com/watch?v=z97PnFIPoFg&t=976s) `Sharpe = mean(daily P&L) / std(daily P&L) * sqrt(252)`
  - `daily P&L`: Total dollar profit and loss recorded for each active trading day
  - `Sharpe`: Annualized daily Sharpe ratio excluding days without trading activity

## Strategies

### 4-Hour Change of Character (CHoCH) Reversal ([00:01:53](https://www.youtube.com/watch?v=z97PnFIPoFg&t=113s))

**Logic:** In an existing trend with higher highs and higher lows (or lower highs and lower lows), wait for the price to close beyond the last swing point in the opposite direction (Change of Character). Enter immediately on the candle close without requiring a prior liquidity sweep.

**Entry rules:**
- Identify an uptrend (or downtrend) with 2+ swings.
- Wait for a 4-hour candle close below the most recent higher low (for short) or above the most recent lower high (for long).
- Do NOT require a prior liquidity sweep.
- Enter at the close of the confirming 4-hour bar.
- Restrict entries to New York session hours (8:00 AM - 4:00 PM ET).
- Skip entries if trading in the direction of a 3+ day consecutive run.

**Exit rules:**
- Place a hard stop 1 tick beyond the last swing high/low.
- Do not use close-based stops.
- Set profit target at 1R (equal in points to the initial stop distance).
- Exit flat at Friday close (16:00 ET) or after 24 to 96 bars.

| parameter | value |
|---|---|
| Timeframe | 4-hour |
| Target Multiple | 1R |
| Stop Type | Hard stop |
| Trading Hours | 8:00 AM to 4:00 PM ET (New York session) |
| Sweep Required | False |

**Markets/assets:** NQ (E-mini Nasdaq-100 futures), ES (E-mini S&P 500 futures)

**Stated performance:** +$62,179 on NQ (61 trades, 54% win rate) and +$39,284 on ES across 2 locked out-of-sample years; 66% of 314 common versions were profitable on NQ and 54.5% on ES.

**Costs/slippage mentioned:** yes — $4 commission per round trip, 1 tick slippage on entry and stop orders; ambiguous minute bars counted as complete losses.

### Flip Zone Retest ([00:09:45](https://www.youtube.com/watch?v=z97PnFIPoFg&t=585s))

**Logic:** Identify a confirmed resistance level broken to the upside (or support broken to the downside). When price retests the broken level from the opposite side, enter expecting the former resistance to act as new support.

**Entry rules:**
- Identify level formed by 2+ swing points within 0.25 ATR.
- Wait for price to close cleanly beyond the level.
- On first return/retest within 0.25 ATR of the level, enter long (if broken upward) or short (if broken downward).

**Exit rules:**
- Hard stop placed past the prior swing.
- Target set at fixed R-multiple or opposite structural level.

| parameter | value |
|---|---|
| Retest tolerance | 0.25 ATR |
| Chart timeframe | Daily / 4-hour |

**Markets/assets:** NQ, ES

**Stated performance:** +11.5 percentage points above random lines on NQ; +10.9 percentage points on ES; common daily version produced +$9,093/yr in NQ discovery.

**Costs/slippage mentioned:** yes — Subjected to $4 round trip commission and 1 tick slippage per execution.

## Tools & data

| name | type | how used |
|---|---|---|
| Claude | other | Used to generate Python backtesting scripts, parse price action concepts into parameterized dials, build execution engines, run combinatorial tests, and compile the report dashboard. |
| CME Futures 1-minute historical data (NQ and ES) | dataset | Five years of 1-minute front-month continuous futures data (3.6 million bars, 327M simulated trade executions) split into discovery (2021-2024) and sealed out-of-sample (2024-2026) windows. |
| Wilder's 14-period ATR | other | Standard indicator used to parameterize level thickness, swing significance, and touch tolerances across timeframes. |
| Skool | platform | Platform hosting Brendan's trading community for sharing code and custom systems. |

## Open questions

- [00:13:12](https://www.youtube.com/watch?v=z97PnFIPoFg&t=792s) **In the original 40,000 versions of the 4h setup, most of the gain came from a few big days.** — The video asserts this phenomenon without providing the distribution curve, trade log breakdown, or impact of removing the top 10 days on ES.
- [00:14:48](https://www.youtube.com/watch?v=z97PnFIPoFg&t=888s) **A fixed 1R target and hard stop is mathematically optimal across all market regimes.** — The testing engine tested multiple R targets (1R to 5R), but the video does not present the full comparative table showing whether 1.5R or 2R had better risk-adjusted return (Sharpe) than 1R on 4h CHoCH.
