# Claude Tested 100,000 Price Action Strategies (Here’s What Works)

**Channel:** AI Pathways  
**URL:** https://www.youtube.com/watch?v=z97PnFIPoFg  
**Duration:** 00:17:11

<sub>schema 1.0 · model gemini-3.6-flash · interactions · analyzed 2026-10-29T16:29:17Z · 107,585 tokens</sub>

## Summary

This video conducts a massive quantitative backtest of over 100,000 price action strategy variations across nearly five years of 1-minute NQ and ES futures data (327 million simulated trades) using Claude to generate the backtesting infrastructure. The study evaluates ten classic price action concepts across multiple timeframes (1m to Daily), accounting for real commissions, slippage, and out-of-sample locked data testing. The results demonstrate that higher timeframes (4-hour and Daily) outperform lower timeframes, flip zones provide the strongest support/resistance edge, hard stops outperform close-based stops, and the 4-hour 'Change of Character' reversal strategy without liquidity sweeps generated the most consistent out-of-sample profits ($62,179 on NQ and $39,284 on ES per contract over two locked years).

## Segments

### [00:00:00](https://www.youtube.com/watch?v=z97PnFIPoFg&t=0s)–00:01:05 · Introduction & Author Background

- Tested over 100,000 price action trading strategy variations using Claude to write code.
- Backtest used 5 years of 1-minute futures data for NQ (Nasdaq) and ES (S&P 500), totaling 3.6 million bars and 327 million simulated trades.
- Author credentials: Math and Economics degree at UCLA, 3+ years in investment banking at Raymond James, and 2 years building automated trading systems for clients.

### [00:01:05](https://www.youtube.com/watch?v=z97PnFIPoFg&t=65s)–00:03:24 · Core Price Action Concepts & Timeframes

- Price action relies on trading chart structure directly: support/resistance levels, trend (break of structure), change of character (CHoCH), sweeps, and confirmation candles.
- Change of Character (CHoCH) represents the first time price breaks structural trend in the opposite direction (e.g., closing below a higher low in an uptrend).
- Sweeps occur when price briefly exceeds a high or low to trigger stop losses before reversing; backtest data shows sweeps reverse only about half the time.
- Tested across six chart timeframes: 1m, 5m, 15m, 1h, 4h, and daily.

### [00:03:24](https://www.youtube.com/watch?v=z97PnFIPoFg&t=204s)–00:03:59 · The Ten Core Price Action Setups Tested

- Tested 10 core price action setups: Level bounce, Breakout, Flip zone, Trend pullback, Trend line, Break of structure, Change of character, Sweep and reclaim, Supply and demand, Fair value gap.

### [00:03:59](https://www.youtube.com/watch?v=z97PnFIPoFg&t=239s)–00:06:59 · Testing Methodology & System Architecture

- Quantified subjective 'eye-drawn' chart decisions into explicit parameter 'dials': touch count, line vs zone, confirmation style, stop loss location, profit target, timeframe, and context filters.
- Total theoretical search space encompasses 20.3 trillion possible parameter combinations.
- Backtested 40,000 baseline versions (4,000 per setup) plus 61,345 common trader setups, totaling 101,345 strategy variations.
- Applied a strict 'gauntlet' test: $4 round-trip commission + 1 tick slippage per stop/market order, ambiguous candles (where high/low hit stop and target in same 1-min bar) treated as losses.
- Locked away 2 full years of ES/NQ data for strict out-of-sample validation.

### [00:06:59](https://www.youtube.com/watch?v=z97PnFIPoFg&t=419s)–00:07:24 · Funnel Analysis Results

- Out of 101,345 tested versions: 88,986 generated enough trades (>=30) to evaluate.
- 24,879 versions were net profitable after accounting for trading costs in discovery.
- 8,310 versions achieved a Sharpe ratio of 0.5 or higher (~8% of total tested versions).

### [00:07:24](https://www.youtube.com/watch?v=z97PnFIPoFg&t=444s)–00:08:29 · Win Rate Myth & Timeframe Performance

- Claims of 80%+ win rates in price action trading are rarely supported by data; win rate has low correlation (0.27) with actual profit.
- On 1-minute charts, transaction costs consume 46.0% of gross profits, compared to only 3.9% on daily charts.
- Trading higher timeframes (1h, 4h, Daily) makes achieving profitability significantly easier due to reduced friction per trade.

### [00:08:29](https://www.youtube.com/watch?v=z97PnFIPoFg&t=509s)–00:09:41 · Level Rules: Touches and Flip Zones

- Real support/resistance levels held 51.1% of touches vs 42.4% for random lines (+8.7 pts NQ, +8.5 pts ES).
- A level touched 4 times held no better (+6.1 pts over random) than a level touched once (+9.0 pts over random). Levels touched 3+ times bounced less and broke through more often.
- Flip zones (old resistance turning into new support) were the single strongest level rule, holding +11.5 percentage points better than random on NQ and +10.9 points on ES.

### [00:09:41](https://www.youtube.com/watch?v=z97PnFIPoFg&t=581s)–00:10:33 · Trend and Trigger Rules Evaluation

- Break of structure (-0.04 ATR) and Change of Character (-0.05 ATR) on their own do not move price predictably.
- Among all trend setups, only Change of Character (CHoCH) reversal achieved a positive median profit (+$61).
- CHoCH setups without a preceding liquidity sweep made +$903/year vs -$834/year with a sweep.

### [00:10:33](https://www.youtube.com/watch?v=z97PnFIPoFg&t=633s)–00:11:55 · Confirmation, Stops, Context, and Multi-Market Tests

- Waiting for candle confirmation vs limit order at touch: limit lost -$1,093/year while confirmation lost -$373/year (a +$719/year improvement in edge, despite giving up 4.3 points of entry).
- Hard stops (-$158/yr) outperformed close-based stops (-$290/yr), saving $132/year.
- Filtering for New York session only (8am-4pm ET) added +$270/year; skipping trades into a 3+ day directional run added +$246/year.
- In consistency tests across both NQ and ES, only the 4-hour Change of Character setup passed on both markets in both setup groups.

### [00:11:55](https://www.youtube.com/watch?v=z97PnFIPoFg&t=715s)–00:13:16 · Out-of-Sample Final Window Results

- In the 2-year locked out-of-sample dataset (which included a 22.5% market selloff and 74.5% rally): 9.2% of 1m versions were profitable vs 45.1% of 4h versions.
- The best overall strategy variation (4h CHoCH, no sweep, enter at close, hard stop at previous swing, 1:1 risk-reward) generated +$62,179 on NQ and +$39,284 on ES per contract over the 2 locked years with 61 NQ trades and 54% win rate.
- 66% of all 314 common 4h CHoCH versions made money on NQ and 54.5% made money on ES.

### [00:13:16](https://www.youtube.com/watch?v=z97PnFIPoFg&t=796s)–00:14:21 · 7 Key Rules That Survived & Market Insights

- Seven rules survived testing: 1. 4h Change of Character; 2. Higher chart timeframes; 3. New York session only; 4. Skip trades into 3+ day run; 5. Confirmation candle on NQ; 6. Hard stops; 7. No sweep before CHoCH.
- Across 9,000 strategy tests, ICT backtests, and Price Action backtests, mean-reversion/reversal strategies consistently represent the core edge in futures markets.

### [00:14:21](https://www.youtube.com/watch?v=z97PnFIPoFg&t=861s)–00:17:11 · Prompt Architecture for Replicating in Claude

- Provided 5 modular prompts to build the backtesting stack in Python with Claude: Prompt 1 (Data & Dials), Prompt 2 (Engine & Level Tests), Prompt 3 (The Funnel), Prompt 4 (The Final Test), Prompt 5 (The Dashboard).

## Claims

| ts | claim | evidence | caveats |
|---|---|---|---|
| [00:07:25](https://www.youtube.com/watch?v=z97PnFIPoFg&t=445s) | Price action trading strategies reliably achieve 80%+ win rates. | data | Only 138 out of 40,000 tested strategies reached an 80%+ win rate, and win rate had a very low correlation (0.27) with overall profitability. |
| [00:08:29](https://www.youtube.com/watch?v=z97PnFIPoFg&t=509s) | Real price action support and resistance levels hold significantly better than random lines. | data | Real levels held 51.1% of touches compared to 42.4% for random lines (+8.7 pts NQ, +8.5 pts ES), but touching a level 3+ times slightly decreased its hold probability. |
| [00:09:42](https://www.youtube.com/watch?v=z97PnFIPoFg&t=582s) | Flip zones (resistance turning into support) are the strongest level concept in price action. | backtest | Held +11.5 percentage points better than random on NQ and +10.9 points on ES across out-of-sample tests. |
| [00:10:34](https://www.youtube.com/watch?v=z97PnFIPoFg&t=634s) | Waiting for candle confirmation improves net trading edge over entering at the level touch. | backtest | Gives up 4.3 points of price entry, but reduces net annual loss by +$719 on NQ. |
| [00:10:59](https://www.youtube.com/watch?v=z97PnFIPoFg&t=659s) | Hard stop losses outperform close-based candle stops. | backtest | Close-based stops achieved a higher win rate (40% vs 29%), but average losses were substantially larger, costing $132 more per year. |
| [00:12:02](https://www.youtube.com/watch?v=z97PnFIPoFg&t=722s) | Higher timeframes (4h/Daily) drastically outperform lower timeframes (1m/5m) for price action. | backtest | Transaction costs consume 46% of gross profit on 1m charts versus 3.9% on daily charts. 45% of 4h strategy versions were profitable out-of-sample vs 9% on 1m. |

## Visuals

### [00:00:16](https://www.youtube.com/watch?v=z97PnFIPoFg&t=16s) · slide · The Price Action Setup (confidence: high)

**Values (as shown):**

- `1. level (beat random lines, 5m to daily)`
- `2. trend (x no follow-through, any chart)`
- `3. change of character (best setup, on the 4h)`
- `4. sweep (x reversed about half the time)`
- `5. confirmation (beat a limit at the level NQ)`
- `6. stop and target (hard stop beat close-based, target size: no edge)`
- `THE SIX CHARTS: 1m, 5m, 15m, 1h, 4h, daily`

**Argues:** Illustrates the main components of price action setups and summarizes backtest findings for each.

### [00:00:29](https://www.youtube.com/watch?v=z97PnFIPoFg&t=29s) · slide · How We Tested It (confidence: high)

**Values (as shown):**

- `20.3 trillion possible versions`
- `WHAT WE RAN: 40,000 spread across every dial, 4,000 per setup; 61,345 common versions; 101,345 total`
- `NAMED VERSIONS: Bare Minimum, Checklist, Entry Model, Zone System, Sweep System, Daily Version`
- `THE DATA: 5 years, 3.6M 1-minute bars, NQ + ES, 327M simulated trades`
- `THE GAUNTLET: real costs, every trade; slippage on every stop; ambiguous candle = a loss; vs random lines; vs random trades; checked on ES; 2 years locked away`

**Argues:** Summarizes backtest parameters, dataset scope, and testing controls.

### [00:00:37](https://www.youtube.com/watch?v=z97PnFIPoFg&t=37s) · slide · The Ten Setups (confidence: high)

**Values (as shown):**

- `1. Level bounce (Buy support, sell resistance)`
- `2. Breakout (Trade the close through a level)`
- `3. Flip zone (Old resistance becomes support)`
- `4. Trend pullback (Buy the first dip in an uptrend)`
- `5. Trend line (Buy a touch of the rising line)`
- `6. Break of structure (Go with the break of the last swing)`
- `7. Change of character (The first break against the trend)`
- `8. Sweep and reclaim (A wick through a low, closed back above)`
- `9. Supply and demand (The first return to an impulse's base)`
- `10. Fair value gap (The first return into a three-candle gap)`

**Argues:** Defines the 10 core price action setup types tested in the study.

### [00:04:12](https://www.youtube.com/watch?v=z97PnFIPoFg&t=252s) · chart · Drawn By Eye (confidence: high)

**Axes / columns:** X-axis: Time (02:45 to 11:45); Y-axis: NQ 15m Price (16,100 to 16,350)

**Values (as shown):**

- `Trader A: Limit at the touch`
- `Trader B: Close back across`
- `AS RULES: Level: 2+ swings within 0.25 ATR; Touch: within 0.25 ATR of the level; Confirmation: a close back across it`

**Argues:** Demonstrates why subjective eye-drawn support levels vary between traders and shows how rules were formalized.

### [00:06:59](https://www.youtube.com/watch?v=z97PnFIPoFg&t=419s) · chart · Funnel (confidence: high)

**Axes / columns:** Y-axis: Stage (All, Enough trades to grade 30+, Profitable, Sharpe 0.5+); X-axis: Count of strategy variations

**Values (as shown):**

- `All: 101,345`
- `Enough trades to grade (30+): 88,986`
- `Profitable: 24,879`
- `Sharpe 0.5+: 8,310`

**Argues:** Shows the survival funnel from 101k raw setups down to 8,310 profitable, risk-adjusted strategies.

### [00:07:24](https://www.youtube.com/watch?v=z97PnFIPoFg&t=444s) · chart · Win Rate And Profit (confidence: high)

**Axes / columns:** X-axis: Win Rate (%); Y-axis: Profit per contract per year ($)

**Values (as shown):**

- `80%+ region highlight`
- `138 strategies won 80%+ of their trades`
- `0.27 correlation`
- `67 of the 138 use a 1R target`

**Argues:** Shows scatter plot of 40,000 strategies proving win rate has low correlation (0.27) with profit.

### [00:07:52](https://www.youtube.com/watch?v=z97PnFIPoFg&t=472s) · chart · Timeframes (confidence: high)

**Axes / columns:** Subcharts: Profitable Versions (%), Costs / Gross Profit (%), Median Per Year ($)

**Values (as shown):**

- `Profitable Versions: 1m 9.2%, 5m 20.3%, 15m 28.8%, 1h 37.7%, 4h 45.1%, Daily 47.9%`
- `Costs / Gross Profit: 1m 46.0%, Daily 3.9%`

**Argues:** Proves higher timeframes yield a higher proportion of profitable versions and lower transaction cost friction.

### [00:08:29](https://www.youtube.com/watch?v=z97PnFIPoFg&t=509s) · chart · Random Lines (confidence: high)

**Axes / columns:** X-axis: Timeframes (All, 5m, 15m, 1h, 4h, Daily); Y-axis: Share of touches that hold (%)

**Values (as shown):**

- `All: Real levels 51.1% vs Random lines 42.4%`
- `+8.7 pts NQ`
- `+8.5 pts ES`

**Argues:** Demonstrates real support/resistance levels outperform random lines on every chart timeframe.

### [00:08:50](https://www.youtube.com/watch?v=z97PnFIPoFg&t=530s) · chart · Touch Count (confidence: high)

**Axes / columns:** X-axis: Touch count (1 touch, 2 touches, 3 touches, 4 touches); Y-axis: Hold performance vs random lines (points)

**Values (as shown):**

- `1 touch: +9.0 pts`
- `2 touches: +7.8 pts`
- `3 touches: +8.2 pts`
- `4 touches: +6.1 pts`
- `DIDN'T SURVIVE: A level touched four times held no better than a level touched once`

**Argues:** Disproves the concept that additional touches make a level stronger.

### [00:09:42](https://www.youtube.com/watch?v=z97PnFIPoFg&t=582s) · chart · Level Rules (confidence: high)

**Axes / columns:** Y-axis: Level rules; X-axis: Percentage point improvement vs comparison

**Values (as shown):**

- `Touch count: -1.1 pts`
- `Wall at 3+ touches: -1.3 pts`
- `Weaker pushes: +0.4 pts`
- `Box vs line: +0.5 pts`
- `Flip zones: +11.5 pts (NQ), +10.9 pts (ES)`

**Argues:** Shows flip zones are by far the single most effective level rule in price action.

### [00:10:11](https://www.youtube.com/watch?v=z97PnFIPoFg&t=611s) · chart · Follow-Through (confidence: high)

**Axes / columns:** X-axis: Trend concept; Y-axis: ATR movement

**Values (as shown):**

- `Break of structure: -0.04 ATR`
- `Change of character: -0.05 ATR`

**Argues:** Shows trend break events alone without setup context do not drive price move follow-through.

### [00:10:18](https://www.youtube.com/watch?v=z97PnFIPoFg&t=618s) · chart · Trend Setups (confidence: high)

**Axes / columns:** Y-axis: Setup type; X-axis: Median Profit ($)

**Values (as shown):**

- `BOS continuation: -$328`
- `CHoCH reversal: +$61`
- `Sweep and reclaim: -$368`
- `Trend line: -$478`

**Argues:** Only CHoCH reversal achieved a positive median annual PnL among trend setup categories.

### [00:10:22](https://www.youtube.com/watch?v=z97PnFIPoFg&t=622s) · chart · Trend Trades As Taught (confidence: high)

**Axes / columns:** Y-axis: Setup variation; X-axis: Profit per contract per year ($)

**Values (as shown):**

- `Change, no sweep needed: +$903`
- `Sweep, then change: -$834`
- `Reversal flip: -$417`
- `Trend line, first to second low: -$586`
- `Late entry on a 5m break: -$2,608`

**Argues:** Shows CHoCH without requiring a sweep performed far better than with a sweep.

### [00:10:34](https://www.youtube.com/watch?v=z97PnFIPoFg&t=634s) · chart · Confirmation Tax (confidence: high)

**Axes / columns:** Y-axis: Trigger style; X-axis: Loss per year ($)

**Values (as shown):**

- `Limit at the touch: -$1,093`
- `After confirmation: -$373`
- `+$719 Edge per year`
- `4.3 Points given up`

**Argues:** Waiting for confirmation candle reduced annual losses by $719 compared to entering via limit order at touch.

### [00:10:59](https://www.youtube.com/watch?v=z97PnFIPoFg&t=659s) · chart · Stops (confidence: high)

**Axes / columns:** Y-axis: Stop style; X-axis: Cost per year ($)

**Values (as shown):**

- `Hard stop: -$158`
- `Close-based stop: -$290`
- `-$132 Close stops, per year`

**Argues:** Hard stops outperform close-based stops because close-based stops result in significantly larger losses.

### [00:11:19](https://www.youtube.com/watch?v=z97PnFIPoFg&t=679s) · chart · Context (confidence: high)

**Axes / columns:** Y-axis: Filter type; X-axis: Annual PnL impact ($)

**Values (as shown):**

- `New York only (8am to 4pm ET): +$270`
- `Skip 3+ day runs: +$246`
- `Daily trend agrees: -$587`

**Argues:** Restricting trades to NY session and avoiding extended 3+ day runs increased edge, while daily trend alignment hurt performance.

### [00:11:29](https://www.youtube.com/watch?v=z97PnFIPoFg&t=689s) · table · Passed On Both Markets (confidence: high)

**Axes / columns:** Market; Original 40,000; Common Versions

**Values (as shown):**

- `NQ Original 40,000: change of character 1h (+$1,208), change of character 4h (+$4,025)`
- `NQ Common Versions: change of character 4h (+$4,884), flip zone daily (+$9,093)`
- `ES Original 40,000: change of character 4h (+$4,146)`
- `ES Common Versions: change of character 4h (+$3,374), breakout daily (+$1,734)`
- `4 of 4: CHoCH 4H passed in each set and on each market`

**Argues:** 4h CHoCH was the only setup that passed consistency checks across both NQ and ES markets in all test sets.

### [00:11:55](https://www.youtube.com/watch?v=z97PnFIPoFg&t=715s) · chart · Final Window (confidence: high)

**Axes / columns:** X-axis: Year (2025 - 2026); Y-axis: Price level (17,232 to 30,078)

**Values (as shown):**

- `-22.5% Selloff`
- `+74.5% Rally`
- `Points: 22,235 -> 17,232 -> 30,078`

**Argues:** Displays the market trajectory during the 2-year locked out-of-sample test period.

### [00:12:02](https://www.youtube.com/watch?v=z97PnFIPoFg&t=722s) · chart · Timeframe Ladder (confidence: high)

**Axes / columns:** X-axis: Timeframe (1m, 5m, 15m, 1h, 4h, Daily); Y-axis: Percentage of profitable versions (%)

**Values (as shown):**

- `1m: 9.2%`
- `5m: 20.3%`
- `15m: 28.8%`
- `1h: 37.7%`
- `4h: 45.1%`
- `Daily: 47.9%`
- `9% made money on 1m, NQ vs 45% on 4h, NQ`

**Argues:** Proves out-of-sample profitability increases monotonically with higher chart timeframes.

### [00:12:31](https://www.youtube.com/watch?v=z97PnFIPoFg&t=751s) · chart · Best Version (confidence: high)

**Axes / columns:** X-axis: Year (2023 to 2026); Y-axis: Equity Curve ($0 to $300k)

**Values (as shown):**

- `+$62,179 locked years, NQ`
- `+$39,284 locked years, ES`
- `61 trades on NQ, 54% winners`

**Argues:** Displays the out-of-sample equity curve for the best surviving 4h CHoCH setup.

### [00:13:06](https://www.youtube.com/watch?v=z97PnFIPoFg&t=786s) · table · The 4h Setup (confidence: high)

**Values (as shown):**

- `39 of 48 versions on usual settings made money, NQ`
- `66% of all 314 common versions made money, NQ`
- `+$17,041 New York session versions, average per contract`
- `54.5% of common versions made money on ES`

**Argues:** Shows high baseline profitability rate across most 4h CHoCH parameter variations in locked test.

### [00:13:16](https://www.youtube.com/watch?v=z97PnFIPoFg&t=796s) · slide · What Survived (confidence: high)

**Values (as shown):**

- `1. Change of character, 4h chart`
- `2. Higher charts (9% on 1m vs 48% on daily)`
- `3. New York session only`
- `4. Skip trades into a 3+ day run`
- `5. Confirmation candle (NQ)`
- `6. Hard stop, not close-based`
- `7. No sweep before the change`

**Argues:** Lists the 7 specific price action rules that consistently improved backtest performance.

### [00:14:22](https://www.youtube.com/watch?v=z97PnFIPoFg&t=862s) · chart · Example Trade (confidence: high)

**Axes / columns:** X-axis: Date (July 2, 2024 to July 18, 2024); Y-axis: NQ 4h Price (19,800 to 21,000)

**Values (as shown):**

- `NQ 4h, July 11, 2024`
- `Trend line shown going up`
- `Change of character close at ~20,600`
- `Entry on close`
- `Stop at swing high (~20,950)`
- `Target equal to risk (~20,250)`

**Argues:** Illustrates an actual trade setup executed by the winning 4h CHoCH strategy on NQ futures.

### [00:14:50](https://www.youtube.com/watch?v=z97PnFIPoFg&t=890s) · slide · What We Keep Finding (confidence: high)

**Values (as shown):**

- `9,000 strategies: mean reversion`
- `ICT: fading the sweep`
- `Price action: the 4h change of character`
- `the floor, not the ceiling`

**Argues:** Connects price action findings to previous strategy tests, emphasizing that mean reversion / fading extremes is the primary market edge.

### [00:15:56](https://www.youtube.com/watch?v=z97PnFIPoFg&t=956s) · slide · Build it yourself - The Five Prompts (confidence: high)

**Values (as shown):**

- `1. Data and dials (page 2)`
- `2. Engine and level tests (page 6)`
- `3. The funnel (page 10)`
- `4. The final test (page 13)`
- `5. The dashboard (page 15)`

**Argues:** Outlines the 5-part prompt sequence to replicate the testing stack using Claude.

## Formulas

_none_

## Strategies

### 4h Change of Character (CHoCH) Reversal Strategy ([00:12:31](https://www.youtube.com/watch?v=z97PnFIPoFg&t=751s))

**Logic:** Reversal trading system that enters when a 4-hour candle closes past the prior swing structure (higher low in an uptrend or lower high in a downtrend), signaling a shift in trend direction without requiring a preceding liquidity sweep.

**Entry rules:**
- Identify 4-hour trend structure (higher highs and higher lows).
- Wait for a 4-hour candle to close past the previous swing low (CHoCH).
- Do NOT require a liquidity sweep before the change of character.
- Enter at the candle close upon confirmation (NQ).

**Exit rules:**
- Place a hard stop loss at the previous swing high (for short) or swing low (for long).
- Set take profit target at 1:1 risk-to-reward ratio matching the stop loss distance.

| parameter | value |
|---|---|
| Timeframe | 4-hour (4h) |
| Session Filter | New York Session only (8:00 AM - 4:00 PM ET) |
| Run Filter | Skip trades into a 3+ day directional run |
| Risk Reward Ratio | 1:1 |
| Stop Loss Type | Hard stop at last swing high/low |

**Markets/assets:** NQ (Nasdaq Futures), ES (E-mini S&P 500 Futures)

**Stated performance:** +$62,179 on NQ and +$39,284 on ES per contract over 2-year locked out-of-sample window; 61 trades on NQ with 54% win rate.

**Costs/slippage mentioned:** yes — $4 commission per round trip + 1 tick slippage on all stop/market orders ($5.00/contract on NQ, $12.50/contract on ES per tick).

## Tools & data

| name | type | how used |
|---|---|---|
| Claude (Anthropic) | platform | Used to write Python code for data ingestion, price action dial definition, trade engines, backtesting funnel, out-of-sample tests, and visual dashboard generation. |
| NQ 1-minute futures dataset | dataset | 5 years of 1-minute bar data for NQ futures (3.6 million bars) used for discovery backtesting and locked out-of-sample validation. |
| ES 1-minute futures dataset | dataset | 5 years of 1-minute bar data for ES futures used for cross-market out-of-sample testing. |
| Python | other | Programming language used to run the simulated trade engines and process 327M simulated backtest trades. |

## Open questions

- [00:12:31](https://www.youtube.com/watch?v=z97PnFIPoFg&t=751s) **The 4-hour CHoCH strategy generates $62,179 per NQ contract over two years.** — Maximum drawdown, required capital/margin, and position sizing details are not specified for the $62k return figure.
