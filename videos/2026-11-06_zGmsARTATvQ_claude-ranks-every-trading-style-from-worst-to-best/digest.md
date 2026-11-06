# Claude Ranks Every Trading Style From Worst to Best

**Channel:** AI Pathways  
**URL:** https://www.youtube.com/watch?v=zGmsARTATvQ  
**Duration:** 00:15:03

<sub>schema 1.0 · model gemini-3.8-flash (gemini-3.6-flash) · static · analyzed 2026-11-06T08:57:13Z · 3 windows · 121,594 tokens</sub>

## Summary

[00:00:00–00:07:00] In this video clip, Brendan presents a backtested ranking of trading styles from worst to best based on 16 years of high-frequency and daily market data across two core strategy families (Donchian breakout and Bollinger fade) while factoring in real-world execution costs. After introducing his methodology and cost model, he details ranks #9 (Scalping, 1-minute timeframe), #8 (Fast Day Trading, 5-minute timeframe), and #7 (Day Trading, 15-minute timeframe), demonstrating how transaction fees and slippage heavily erode or eliminate profitability on faster timeframes.

[00:07:00–00:14:00] In this clip (00:07:00 to 00:14:00), the video concludes its ranking of trading and investing styles from rank 6 down to rank 1 based on a 16-year backtest (2008–2024/2026). It evaluates Hourly trading (#6), Premium Selling (#5), Position Trading (#4), Swing Trading (#3), SPY Buy & Hold (#2), and QQQ Buy & Hold (#1). The analysis demonstrates that higher timeframes consistently outperform lower timeframes across all tested market regimes due to lower trade frequency and reduced cost drag, while distinguishing between growth and income objectives.

[00:14:00–00:15:03] This clip presents a structured, multi-layer prompt framework (trading_styles_lab) designed for Claude or Claude Code to build a quantitative trading research environment. The framework evaluates trading frequency, cost degradation, tax impact, and strategy robustness across two distinct signal families—a Donchian channel breakout (trend) and a Bollinger Band fade (mean reversion)—over six timeframes ranging from 1-minute intraday to daily holding periods.

## Segments

### [00:00:00](https://www.youtube.com/watch?v=zGmsARTATvQ&t=0s)–00:01:00 · Introduction and Study Overview

- Brendan uses Claude to structure a backtesting engine ranking trading styles from worst to best.
- Styles covered include scalping, day trading, swing trading, option selling, and buy-and-hold.
- The test incorporates 16 years of 1-minute futures data (MNQ, MES) and daily data for SPY and QQQ.
- Simulations cover over 100,000 trades including commissions, slippage, and Section 1256 taxes.
- Brendan studied math and economics at UCLA, spent 3 years in investment banking, and 2 years building client trading systems managing millions.

### [00:01:00](https://www.youtube.com/watch?v=zGmsARTATvQ&t=60s)–00:02:41 · Methodology, Strategy Families, and Cost Model

- The study keeps strategy rules and costs identical across six execution speeds (1 min, 5 min, 15 min, 60 min, daily 33-day hold, daily 63-day hold).
- Two strategy families tested: Donchian breakout (trend: buy 20-bar high, exit 10-bar low) and Bollinger fade (mean reversion: buy below 2-SD lower band, exit at 20-bar mean).
- Cost model parameters: E-mini commission $4.00 round turn, Micro commission $1.20 round turn, 1 tick entry slippage, 1 tick exit slippage, $0.00 ETF commission, 1 bp SPY/QQQ spread, Section 1256 futures tax (60% LT / 40% ST).
- Total round-turn break-even cost is $11.00 on Micro Nasdaq futures (MNQ) and $10.00 on ETF positions.
- Results reflect the performance of an average trader following systematic rules rather than top discretionary traders.

### [00:02:41](https://www.youtube.com/watch?v=zGmsARTATvQ&t=161s)–00:04:35 · Rank #9: Scalping (1-Minute Timeframe)

- Scalping takes ~10 trades per day with an average hold time of 14 minutes (1,838 trades/year).
- Mean reversion on MNQ 1-minute chart yields a positive gross Sharpe ratio of +0.575.
- After costs, net Sharpe drops to -2.865 with an annual net return of -15.9%.
- Execution costs represent 5.98x the entire gross P&L.
- A $100,000 account starting in 2010 hits zero equity on August 15, 2013, reaching -$178,052 by 2026.
- Annual transaction friction costs $20,218 per year on scalping versus $61 per year on swing trading.
- Scalping only suits institutional accounts with exchange fee rebates and dedicated infrastructure.

### [00:04:35](https://www.youtube.com/watch?v=zGmsARTATvQ&t=275s)–00:05:39 · Rank #8: Fast Day Trading (5-Minute Timeframe)

- Fast day trading takes 2 trades per day with an average hold time of 70 minutes (504 trades/year).
- The 5-minute mean reversion model produces a gross Sharpe ratio of +0.242, but net Sharpe is -0.613 with a net annual return of -3.0%.
- Transaction costs consume 3.55x the gross P&L.
- Suits traders with large account sizes where average trade size outweighs round-trip fixed costs, or prop firm capital.

### [00:05:39](https://www.youtube.com/watch?v=zGmsARTATvQ&t=339s)–00:07:00 · Rank #7: Day Trading (15-Minute Timeframe)

- Patient day trading takes 1 trade per day on 15-minute bars with an average hold time of 3 hours (208 trades/year).
- Achieves a positive net Sharpe ratio of +0.141 and a net annual return of +2.0% (gross Sharpe +0.483).
- Costs eat 0.71x (71%) of total gross P&L.
- To make 1-minute scalping profitable through discretionary filtering, a trader would need to accurately skip 1,579 losing trades out of 42,914 1-minute setup points, compared to skipping just 2 losing trades over 16 years in swing trading.

### [00:07:00](https://www.youtube.com/watch?v=zGmsARTATvQ&t=420s)–00:07:56 · Rank 6: Hourly Trading

- Hourly trading uses a 60-minute Donchian channel breakout strategy on Micro E-mini Nasdaq futures (MNQ).
- Positions are allowed to be held overnight across session breaks, averaging about 1 day per hold (~132 trades/year).
- Achieved a Net Sharpe of +0.628, 6.0% annual net return, cost/gross P&L ratio of 0.23x, and max drawdown of -13%.
- Trading 40% less frequently than the 15-minute timeframe allows retaining roughly 75% of the total edge after transaction costs.

### [00:07:56](https://www.youtube.com/watch?v=zGmsARTATvQ&t=476s)–00:09:03 · Rank 5: Premium Selling

- Options premium selling involves selling options to collect income by taking on downside market risk (benchmarked against CBOE PUT index).
- Achieved a Net Sharpe of +0.685 and 9.2% annual return over 16 years, but experienced a -29% drawdown during the 2020 crash.
- While it lagged SPY buy & hold over the full 16-year period, premium selling outperformed SPY in 9 out of 20 tested sub-periods.
- Suits large accounts seeking steady cash flow rather than capital growth, provided they can handle occasional steep drawdowns.

### [00:09:03](https://www.youtube.com/watch?v=zGmsARTATvQ&t=543s)–00:09:48 · Rank 4: Position Trading

- Position trading uses a 55-bar Donchian channel breakout on daily QQQ candles (QQQ/D55 [donc]).
- Averages ~3 trades per year with an average hold time of 63 days per trade.
- Generated a Net Sharpe of +0.714 and 9.2% annual net return with a cost/gross ratio of 0.00x and max drawdown of -12%.
- Suits full-time workers and small account sizes willing to sit through long stretches of inactivity.

### [00:09:48](https://www.youtube.com/watch?v=zGmsARTATvQ&t=588s)–00:10:47 · Rank 3: Swing Trading

- Swing trading utilizes a 20-bar Donchian channel breakout on daily SPY candles (SPY/D20 [donc]).
- Averages ~6 trades per year with an average hold time of 33 days.
- Achieved a Net Sharpe of +0.797, 8.0% annual net return, cost/gross ratio of 0.01x, and a maximum drawdown of just -7%.
- Recorded the lowest max drawdown of any active trading strategy in the study, making it ideal for most active traders with full-time jobs.

### [00:10:47](https://www.youtube.com/watch?v=zGmsARTATvQ&t=647s)–00:11:43 · Rank 2: SPY Buy & Hold

- SPY Buy & Hold requires zero trades/year and no screen time.
- Achieved a Net Sharpe of +0.848 and 15.5% annual return, growing $100,000 into $951,061 over 16 years.
- Max drawdown reached -34%.
- Serves as the core benchmark for long-term capital growth, but does not provide steady income unless assets are liquidated.

### [00:11:43](https://www.youtube.com/watch?v=zGmsARTATvQ&t=703s)–00:12:03 · Rank 1: QQQ Buy & Hold

- QQQ Buy & Hold took top overall rank with a Net Sharpe of +0.938 and 20.4% annual return.
- Grew $100,000 into $1,873,048 over the 16-year test period with zero trading costs.
- Exhibited deeper drawdowns (-35%) than SPY, particularly during 2022.

### [00:12:03](https://www.youtube.com/watch?v=zGmsARTATvQ&t=723s)–00:13:22 · Rank Stability & Timeframe Consistency

- Evaluated all strategy rankings across 20 sub-periods (17 calendar years plus 3 market regimes: bull, chop, down).
- Slowing down trade frequency yielded superior net performance at every single step: Daily > 60m > 15m > 5m > 1m.
- 1-minute and 5-minute timeframes finished at the bottom in every market condition tested due to transaction costs.
- High trade frequency intraday trading provides a high performance ceiling for skilled discretionary traders, but performs worst on average for rule-based systems.

### [00:13:22](https://www.youtube.com/watch?v=zGmsARTATvQ&t=802s)–00:14:00 · Two Objectives: Growth vs. Income

- Growth objective benchmark is buy-and-hold (SPY/QQQ); active strategies must beat this benchmark to justify the effort.
- Income objective requires active trading, but reducing trade frequency (swing/hourly trading) is not the same as avoiding trading.
- Higher timeframe active trading provides income generation while avoiding the severe cost drag of ultra-fast day trading.

### [00:14:00](https://www.youtube.com/watch?v=zGmsARTATvQ&t=840s)–00:14:07 · Growth vs Income Objectives

- Reducing trading frequency is not the same as not trading.
- Trading lower frequency allows traders to generate income and take setups while taking on less risk than daily intraday trading.

### [00:14:07](https://www.youtube.com/watch?v=zGmsARTATvQ&t=847s)–00:14:32 · Prompting Layer 1: Data and Costs

- Layer 1 of trading_styles_lab focuses exclusively on data ingestion and cost modeling, avoiding trading engine code at this stage.
- 1-minute Parquet datasets for SPY, QQQ, GLD, TLT, IWM, and VXX are ingested and categorized into unadjusted front month, back-adjusted, and roll calendar formats.
- Daily history is fetched via yfinance with auto-adjust ON for total return, along with price-only SPY to serve as the benchmark equity (yielding ~1.5% to 2% dividend return).
- Risk-free rate is pulled from FRED (DTB3), and options benchmarks use CBOE PUT and BXM published index history.
- Cost specifications include $4.00 RT per futures contract ($1.25 RT micros), 1 tick slippage on entry and exit, 10 bps execution penalty, 50c commission + 15 bps spread RT on ETF/QQQ, and 50 bps per year short borrow rate.
- Taxes are configured at 40% short-term / 20% long-term for futures (60/40 rule) and 37% short-term / 20% long-term for ETFs.

### [00:14:32](https://www.youtube.com/watch?v=zGmsARTATvQ&t=872s)–00:14:37 · Prompting Layer 2: The Signal Engine

- Layer 2 tests a single signal family across six speeds/horizons: 1-minute, 5-minute, 15-minute, 1-hour intraday (flat by close), daily short lookback (swing), and daily long lookback (position).
- The signal engine uses a Donchian channel breakout (enter long on N-bar high break, exit on M-bar low break or session close).
- Parameters must not be optimized; standard settings (e.g. 20-period entry, 10-period exit) are held constant to isolate frequency degradation.
- Trade frequencies must be measured from the actual execution output rather than hardcoded.

### [00:14:37](https://www.youtube.com/watch?v=zGmsARTATvQ&t=877s)–00:14:53 · Prompting Layer 3: Mean Reversion and Stability

- Layer 3 introduces a second signal family: Bollinger Band fade mean reversion (enter long when price closes below lower band, exit when price closes above moving average; default 20-period, 2.0 std dev).
- Mean reversion is evaluated at identical horizons to test if cost degradation is signal-dependent or universal.
- Sub-period window stability testing splits data into non-overlapping periods and regime buckets (bull, chop, drawdown) derived from SPY.
- Cost sensitivity re-runs rankings at 0.5, 1.0, and 1.5 ticks of entry slippage.

### [00:14:53](https://www.youtube.com/watch?v=zGmsARTATvQ&t=893s)–00:15:03 · Outro and Community Call to Action

- Encourages viewers to like, comment, and subscribe.
- Invites viewers to join the AI-focused trading community on Skool via the description link.

## Claims

| ts | claim | evidence | caveats |
|---|---|---|---|
| [00:03:02](https://www.youtube.com/watch?v=zGmsARTATvQ&t=182s) | 1-minute scalping has a positive gross edge (+0.575 gross Sharpe) but loses -15.9% annually after trading costs. | backtest | Applies to retail cost structures; institutional traders receive fee rebates. |
| [00:03:43](https://www.youtube.com/watch?v=zGmsARTATvQ&t=223s) | Transaction costs for 1-minute scalping consume 5.98x the gross strategy P&L, costing $20,218 per year on a $100,000 account. | backtest | Based on $1.20 round-turn micro commission and 1 tick slippage on entry and exit. |
| [00:04:46](https://www.youtube.com/watch?v=zGmsARTATvQ&t=286s) | 5-minute fast day trading loses -3.0% annually after costs, with costs eating 3.55x gross profit. | backtest | Evaluated on systematic rules without discretionary setup filtering. |
| [00:05:58](https://www.youtube.com/watch?v=zGmsARTATvQ&t=358s) | 15-minute day trading achieves a positive net Sharpe of +0.141 and +2.0% annual net return. | backtest | Transaction costs still consume 71% of total gross P&L. |
| [00:07:27](https://www.youtube.com/watch?v=zGmsARTATvQ&t=447s) | Moving from a 15-minute to a 60-minute chart reduces trading frequency by ~40% while preserving ~75% of the gross trading edge. | data | Based on backtesting data on MNQ futures from 2008 to 2024/2026. |
| [00:08:26](https://www.youtube.com/watch?v=zGmsARTATvQ&t=506s) | Options premium selling underperforms SPY buy and hold on absolute return over 16 years, but beats SPY in 9 of 20 tested sub-periods. | data | Exposes traders to rare but deep tail-risk drawdowns (-29% in 2020). |
| [00:10:08](https://www.youtube.com/watch?v=zGmsARTATvQ&t=608s) | Daily 20-bar Donchian swing trading on SPY achieved the lowest maximum drawdown (-7%) among all active trading strategies in the 16-year study. | data | Generates lower annualized return (8.0%) compared to passive index buy and hold. |
| [00:12:22](https://www.youtube.com/watch?v=zGmsARTATvQ&t=742s) | Higher trading timeframes (Daily > 60m > 15m > 5m > 1m) consistently beat lower timeframes across every tested calendar year and market regime. | data | Applies strictly to mechanical/rule-based systems; top discretionary traders may achieve higher performance on lower timeframes. |
| [00:14:01](https://www.youtube.com/watch?v=zGmsARTATvQ&t=841s) | Reducing trade frequency allows traders to capture income while taking on significantly less risk than daily intraday trading. | none | Requires taking high-conviction setups fewer times per year. |
| [00:14:14](https://www.youtube.com/watch?v=zGmsARTATvQ&t=854s) | The prompt framework can be executed inside Claude or using Claude Code for advanced usage. | anecdote |  |
| [00:14:38](https://www.youtube.com/watch?v=zGmsARTATvQ&t=878s) | Trend breakout strategies naturally improve in performance as holding periods lengthen. | none |  |

## Visuals

### [00:00:05](https://www.youtube.com/watch?v=zGmsARTATvQ&t=5s) · screen · untitled (confidence: high)

**Values (as shown):**

- `Day Trading`
- `Swing`
- `Momentum`
- `Selling Options`
- `Buy & Hold`

**Argues:** Previews trading style categories evaluated in the video.

### [00:00:11](https://www.youtube.com/watch?v=zGmsARTATvQ&t=11s) · screen · Good evening, AI Pathways (confidence: high)

**Values (as shown):**

- `What is the best trading style?`
- `Opus 3.5 Medium Auto`

**Argues:** Shows the Claude interface used to structure the backtest evaluation.

### [00:00:22](https://www.youtube.com/watch?v=zGmsARTATvQ&t=22s) · screen · 16 yrs 1-MINUTE + DAILY (confidence: high)

**Values (as shown):**

- `ES`
- `NQ`
- `SPY`
- `QQQ`

**Argues:** Displays the 16-year dataset assets used for backtesting.

### [00:00:26](https://www.youtube.com/watch?v=zGmsARTATvQ&t=26s) · diagram · 2 STRATEGY FAMILIES (confidence: high)

**Values (as shown):**

- `Trend`
- `Revert`

**Argues:** Shows the two strategy archetypes: trend following and mean reversion.

### [00:00:32](https://www.youtube.com/watch?v=zGmsARTATvQ&t=32s) · chart · Costs ON EVERY TRADE (confidence: high)

**Axes / columns:** Gross; Fees; Slippage; Tax; Net

**Values (as shown):**

- `Gross`
- `Fees`
- `Slippage`
- `Tax`
- `Net`

**Argues:** Shows how transaction friction components reduce gross trade returns to net profits.

### [00:00:35](https://www.youtube.com/watch?v=zGmsARTATvQ&t=35s) · screen · 95,194 SIMULATED TRADES (confidence: high)

**Values (as shown):**

- `58,123 SIMULATED TRADES`
- `95,194 SIMULATED TRADES`

**Argues:** Demonstrates backtest scale across tens of thousands of simulated executions.

### [00:00:50](https://www.youtube.com/watch?v=zGmsARTATvQ&t=50s) · slide · Disclaimer: (confidence: high)

**Values (as shown):**

- `NO FINANCIAL ADVICE - The Information on this Channel is provided for education and informational purposes only...`

**Argues:** Standard financial disclaimer.

### [00:01:00](https://www.youtube.com/watch?v=zGmsARTATvQ&t=60s) · slide · Six speeds (confidence: high)

**Values (as shown):**

- `1 min, hold 14 min, 2,568 trades / yr`
- `5 min, hold 70 min, 504 trades / yr`
- `15 min, hold 3 hrs, 208 trades / yr`
- `60 min, hold 1 day, 132 trades / yr`
- `Daily, hold 33 days, 6 trades / yr`
- `Daily, hold 63 days, 2 trades / yr`

**Argues:** Outlines the six trade timeframes and holding periods evaluated.

### [00:01:23](https://www.youtube.com/watch?v=zGmsARTATvQ&t=83s) · diagram · The two families (confidence: high)

**Values (as shown):**

- `Donchian breakout`
- `buy on a break of the 20-bar high, exit on a break of the 10-bar low`
- `entry 3523.38`
- `20-bar high`
- `10-bar low`
- `Bollinger fade`
- `buy below the 2-SD lower band, exit above the mean`
- `entry 3542.88`
- `20-bar mean`
- `lower band`

**Argues:** Defines rules for Donchian breakout and Bollinger fade strategies.

### [00:01:51](https://www.youtube.com/watch?v=zGmsARTATvQ&t=111s) · chart · The cost model (confidence: high)

**Axes / columns:** Symbol; Dollar Cost

**Values (as shown):**

- `MES: $22.20`
- `MNQ: $11.00`
- `SPY: $10.00`
- `QQQ: $10.00`
- `E-mini commission, round turn: $4.00`
- `Micro commission, round turn: $1.20`
- `Entry slippage: 1 tick`
- `Exit slippage: 1 tick`
- `ETF commission: $0.00`
- `SPY / QQQ spread: 1 bp round trip`
- `Market impact: 0 bp`
- `Futures tax, Section 1256: 60% LT / 40% ST`
- `Short-term rate: UNREADABLE`
- `Long-term rate: UNREADABLE`
- `Blended 1256 rate: UNREADABLE`

**Argues:** Breaks down fixed commissions, slippage, and tax assumptions applied to each asset class.

### [00:02:52](https://www.youtube.com/watch?v=zGmsARTATvQ&t=172s) · diagram · Scalping (confidence: high)

**Values (as shown):**

- `in and out, over and over`
- `HOLD: 14 min`
- `TRADES: 10 a day`
- `OVERNIGHT: never`

**Argues:** Defines scalping execution parameters.

### [00:03:02](https://www.youtube.com/watch?v=zGmsARTATvQ&t=182s) · chart · #9 Scalping (confidence: high)

**Axes / columns:** Year (2012 to 2026); Equity ($k)

**Values (as shown):**

- `MNQ/1m [boll] 1-minute`
- `net Sharpe: -2.865`
- `net return / yr: -15.9%`
- `trades / yr: 1,838`
- `cost ÷ gross P&L: 5.98x`
- `gross vs net Sharpe: gross +0.575, net -2.865`
- `zero: 2013-08-15`
- `-$178,052`
- `$100k`
- `-100%`

**Argues:** Presents equity curve showing how high transaction costs turn 1-minute scalping into severe cumulative losses.

### [00:03:58](https://www.youtube.com/watch?v=zGmsARTATvQ&t=238s) · chart · Cost per year (confidence: high)

**Axes / columns:** Style; Cost ($)

**Values (as shown):**

- `scalping - 1,838 round turns: $20,218`
- `swing - 6 round turns: $61`
- `$11.00 to break even on one micro Nasdaq round turn`
- `$10.00 on an ETF round turn`

**Argues:** Compares total annual friction costs of scalping vs swing trading on a $100k account.

### [00:04:13](https://www.youtube.com/watch?v=zGmsARTATvQ&t=253s) · table · Who each style suits (confidence: high)

**Axes / columns:** rank; style; account size; screen time; suits

**Values (as shown):**

- `9 | scalping | institutional | whole session | cost structure, not setups`
- `8 | fast day trading | large | whole session | trade size vs round trip`
- `7 | day trading | large | whole session | one decision a day`
- `6 | hourly | any | most of session | willing to hold overnight`
- `5 | premium selling | large | none | cash flow, tolerant of one hole`
- `4 | position trading | any | once a day | long stretches of nothing`
- `3 | swing trading | any | once a day | full-time job, small account`
- `2 | SPY buy and hold | any | none | growth, not income`
- `1 | QQQ buy and hold | any | none | growth, not income`

**Argues:** Summary matrix matching each trading style to optimal account size, required screen time, and trade-off suitability.

### [00:04:39](https://www.youtube.com/watch?v=zGmsARTATvQ&t=279s) · diagram · Fast day trading (confidence: high)

**Values (as shown):**

- `a few setups, flat by the close`
- `HOLD: 70 min`
- `TRADES: 2 a day`
- `OVERNIGHT: never`

**Argues:** Defines 5-minute fast day trading parameters.

### [00:04:46](https://www.youtube.com/watch?v=zGmsARTATvQ&t=286s) · chart · #8 Fast day trading (confidence: high)

**Axes / columns:** Year (2012 to 2026); Equity ($k)

**Values (as shown):**

- `MNQ/5m [donc] 5-minute`
- `net Sharpe: -0.613`
- `net return / yr: -3.0%`
- `trades / yr: 504`
- `cost ÷ gross P&L: 3.55x`
- `gross vs net Sharpe: gross +0.242, net -0.613`

**Argues:** Shows equity curve for 5-minute fast day trading losing 3% annually due to friction.

### [00:05:43](https://www.youtube.com/watch?v=zGmsARTATvQ&t=343s) · diagram · Day trading (confidence: high)

**Values (as shown):**

- `wait for one setup`
- `HOLD: 3 hours`
- `TRADES: 1 a day`
- `OVERNIGHT: never`

**Argues:** Defines patient 15-minute day trading parameters.

### [00:05:57](https://www.youtube.com/watch?v=zGmsARTATvQ&t=357s) · chart · #7 Day trading (confidence: high)

**Axes / columns:** Year (2012 to 2026); Equity ($k)

**Values (as shown):**

- `MNQ/15m [donc] 15-minute`
- `net Sharpe: +0.141`
- `net return / yr: 2.0%`
- `trades / yr: 208`
- `cost ÷ gross P&L: 0.71x`
- `gross vs net Sharpe: gross +0.483, net +0.141`
- `$116,629`

**Argues:** Shows 15-minute day trading producing a positive net equity curve.

### [00:06:11](https://www.youtube.com/watch?v=zGmsARTATvQ&t=371s) · diagram · Skipping losing trades (confidence: high)

**Values (as shown):**

- `2 trades - swing - over sixteen years`
- `1,579 trades - scalping - picked in advance`
- `Each dot is a one minute trade. The dark ones are the 5 percent that would need to be identified in advance, out of 42,914.`

**Argues:** Illustrates the heavy burden placed on human discretionary judgment as trade frequency increases.

### [00:07:00](https://www.youtube.com/watch?v=zGmsARTATvQ&t=420s) · table · Who each style suits (confidence: high)

**Axes / columns:** style; account size; screen time; suits

**Values (as shown):**

- `9 scalping | institutional | whole session | cost structure, not setups`
- `8 fast day trading | large | whole session | trade size vs round trip`
- `7 day trading | large | whole session | one decision a day`
- `6 hourly | any | most of session | willing to hold overnight`
- `5 premium selling | large | none | cash flow, tolerant of one hole`
- `4 position trading | any | once a day | long stretches of nothing`
- `3 swing trading | any | once a day | full-time job, small account`
- `2 SPY buy and hold | any | none | growth, not income`
- `1 QQQ buy and hold | any | none | growth, deeper drawdown`

**Argues:** Summarizes the suitability of each trading style by account size, screen time required, and target trader profile.

### [00:07:21](https://www.youtube.com/watch?v=zGmsARTATvQ&t=441s) · chart · THE COUNTDOWN #6 Hourly (confidence: high)

**Axes / columns:** Year (2012 to 2026); Equity ($100k to $197,701); Drawdown (-13%)

**Values (as shown):**

- `MNQ/60m [donc] - 60-minute`
- `net Sharpe: +0.628`
- `net return / yr: 6.0%`
- `trades / yr: 132`
- `cost ÷ gross P&L: 0.23x`
- `gross Sharpe: +0.822`
- `net Sharpe: +0.628`
- `Ending equity: $197,701`
- `Max drawdown: -13%`

**Argues:** Presents backtest performance for 60-minute Donchian breakout trading on MNQ.

### [00:08:16](https://www.youtube.com/watch?v=zGmsARTATvQ&t=496s) · chart · THE COUNTDOWN #5 Premium selling (confidence: high)

**Axes / columns:** Year (2012 to 2026); Equity ($100k to $391,805); Drawdown (-29%)

**Values (as shown):**

- `CBOE PUT - published index`
- `net Sharpe: +0.685`
- `net return / yr: 9.2%`
- `trades / yr: 0.00`
- `cost ÷ gross P&L: 0.00x`
- `Ending equity: $391,805`
- `Max drawdown: -29%`

**Argues:** Displays long-term equity growth and drawdown curve for options premium selling benchmarked by CBOE PUT index.

### [00:09:18](https://www.youtube.com/watch?v=zGmsARTATvQ&t=558s) · chart · THE COUNTDOWN #4 Position trading (confidence: high)

**Axes / columns:** Year (2012 to 2026); Equity ($100k to $240,210); Drawdown (-12%)

**Values (as shown):**

- `QQQ/D55 [donc] - daily 55-bar`
- `net Sharpe: +0.714`
- `net return / yr: 9.2%`
- `trades / yr: 3`
- `cost ÷ gross P&L: 0.00x`
- `gross Sharpe: +0.717`
- `net Sharpe: +0.714`
- `Ending equity: $240,210`
- `Max drawdown: -12%`

**Argues:** Presents backtest metrics for 55-bar daily Donchian breakout position trading on QQQ.

### [00:10:03](https://www.youtube.com/watch?v=zGmsARTATvQ&t=603s) · chart · THE COUNTDOWN #3 Swing trading (confidence: high)

**Axes / columns:** Year (2012 to 2026); Equity ($100k to $222,425); Drawdown (-7%)

**Values (as shown):**

- `SPY/D20 [donc] - daily 20-bar`
- `net Sharpe: +0.797`
- `net return / yr: 8.0%`
- `trades / yr: 6`
- `cost ÷ gross P&L: 0.01x`
- `gross Sharpe: +0.805`
- `net Sharpe: +0.797`
- `Ending equity: $222,425`
- `Max drawdown: -7%`

**Argues:** Demonstrates backtest results for daily 20-bar Donchian breakout swing trading on SPY showing minimal drawdown.

### [00:10:50](https://www.youtube.com/watch?v=zGmsARTATvQ&t=650s) · chart · THE COUNTDOWN #2 SPY buy and hold (confidence: high)

**Axes / columns:** Year (2012 to 2026); Equity ($100k to $951,061); Drawdown (-34%)

**Values (as shown):**

- `SPY B&H - buy and hold`
- `net Sharpe: +0.848`
- `net return / yr: 15.5%`
- `trades / yr: 0.00`
- `cost ÷ gross P&L: 0.00x`
- `Ending equity: $951,061`
- `Max drawdown: -34%`

**Argues:** Shows 16-year performance of passive SPY buy and hold.

### [00:11:48](https://www.youtube.com/watch?v=zGmsARTATvQ&t=708s) · chart · THE COUNTDOWN #1 QQQ buy and hold (confidence: high)

**Axes / columns:** Year (2012 to 2026); Equity ($100k to $1,873,048); Drawdown (-35%)

**Values (as shown):**

- `QQQ B&H - buy and hold`
- `net Sharpe: +0.938`
- `net return / yr: 20.4%`
- `trades / yr: 0.00`
- `cost ÷ gross P&L: 0.00x`
- `Ending equity: $1,873,048`
- `Max drawdown: -35%`

**Argues:** Shows top-ranked 16-year backtest performance for passive QQQ buy and hold.

### [00:12:03](https://www.youtube.com/watch?v=zGmsARTATvQ&t=723s) · chart · Rank stability (confidence: high)

**Axes / columns:** Sub-period / Regime (2012 to 2026, bull, chop, down); Rank (#1 to #18)

**Values (as shown):**

- `MNQ/60m [donc]`
- `MNQ/15m [donc]`
- `QQQ B&H`
- `SPY B&H`
- `CBOE PUT`
- `MNQ/5m [donc]`
- `MNQ/1m [boll]`

**Argues:** Illustrates that timeframe rankings remain stable across 20 distinct sub-periods and market regimes, with daily/60m timeframes consistently beating 1m/5m.

### [00:13:22](https://www.youtube.com/watch?v=zGmsARTATvQ&t=802s) · slide · TWO OBJECTIVES Growth and income (confidence: high)

**Values (as shown):**

- `growth: holding is the benchmark, the rest have to clear`
- `income: still trading, fewer times a year`
- `Reducing frequency is not the same as not trading.`

**Argues:** Frames trading styles based on whether the trader's goal is capital growth (benchmark is buy-and-hold) or income (active trading with reduced frequency).

### [00:14:00](https://www.youtube.com/watch?v=zGmsARTATvQ&t=840s) · slide · Growth and income (confidence: high)

**Values (as shown):**

- `TWO OBJECTIVES`
- `Growth and income`
- `growth`
- `holding is the benchmark`
- `the rest have to clear`
- `income`
- `still trading`
- `fewer times a year`
- `Reducing frequency is not the same as not trading.`

**Argues:** Differentiates growth objectives from income trading objectives based on execution frequency and risk.

### [00:14:07](https://www.youtube.com/watch?v=zGmsARTATvQ&t=847s) · slide · Data and costs (confidence: high)

**Values (as shown):**

- `LAYER 1 | PART 1 OF 3`
- `Data and costs`
- `Build the foundation first`
- `Build layer 1 of a new research project called trading_styles_lab. This layer is DATA AND COSTS ONLY. Do not build trading, backtest, or engine code yet.`
- `GOAL: Context only, do not build it yet.`
- `Compare different trading styles on a per dollar of capital at risk, after realistic costs and taxes. The rungs are scalping, fast day trading, day trading, hourly, premium selling, position trading, swing trading, and buy and hold. Later layers hold one strategy per rung on the same underlying asset and holding period, so this layer must provide data access and one shared cost model that every rung will use.`
- `TASK 1: INSPECT THE PARQUET FILES IN THIS FOLDER`
- `Inspect the parquet files in data/ to find files containing 1-minute data for SPY, QQQ, GLD, TLT, IWM, and VXX, converted to three forms: unadjusted front month, back-adjusted, and a roll calendar.`
- `Find every parquet file and inspect each one. For each report: filename, size, row count, column schema with dtypes, first and last timestamp, and any missing ranges or gaps. Do not assume or guess based on the contents, not the filename, and say which file is which.`
- `Then move them into data/futures, print the layout, and write a summary report. If anything is missing, note it. If anything is ambiguous, list it as an open question and keep going. Do not invent data, and do not download future data.`

**Argues:** Specifies Layer 1 prompt rules for setting up dataset inspection and directory organization without writing trading logic.

### [00:14:23](https://www.youtube.com/watch?v=zGmsARTATvQ&t=863s) · slide · Data and costs (confidence: high)

**Values (as shown):**

- `LAYER 1 | PART 2 OF 3`
- `Data and costs`
- `TASK 2: FREE DAILY DATA`
- `Pull daily history with yfinance, auto-adjust ON so prices are total-return. Also pull SPY price-only (auto-adjust OFF); buy and hold is the benchmark everything else is ranked against, and price-only gives an equity roughly 1.5 to 2 percent a year.`
- `SPY, QQQ, TLT, IWM, VXX, GLD, DBC, VNQ, EFA, EEM, VNQI.`
- `Use FRED DTB3 for the risk-free rate. Save these as parquet under data/daily/. Print first date, last date and row count for each, and flag any ticker starting after 2000.`
- `TASK 3: PREMIUM SELLING BENCHMARK`
- `Do not build an options backtest. Retrieve CBOE's published PUT and BXM index history. Report which source worked, the date range, and whether the history goes back far enough. If you can only get part history, describe how to interpolate.`
- `TASK 4: THE COST MODEL`
- `Build one module, costs.py, that every later rung imports. No rung may hardcode its own costs. Every number is a named constant in one config block at the top.`

**Argues:** Details tasks for fetching free daily data, options benchmark indices, and creating a unified cost module costs.py.

### [00:14:31](https://www.youtube.com/watch?v=zGmsARTATvQ&t=871s) · slide · Data and costs (confidence: high)

**Values (as shown):**

- `LAYER 1 | PART 3 OF 3`
- `Data and costs`
- `continued`
- `$4.00 round turn per contract, $1.25 round turn micros`
- `1 tick slippage on entry, 1 tick on exit`
- `10 bps round-trip execution penalty`
- `50 commission, 15bp spread round trip on ETF/QQQ`
- `Short borrow rate: 50 bps per year on long/short strategies`
- `Taxes: 40% short-term, 20% long-term for futures (60/40 rule applies); 37% short-term on etf and under a year size, long-term default 37% short, 20% long, switchable`
- `FUTURES RUNGS TRAIN MICRO CONTRACTS SIZED IN WHOLE CONTRACTS.`
- `Micro contracts trade 1/10 size, allowing $100k to $1M even on 0-29 contracts and most backtests then charge 29% of a commission; charge full $1.25 micro RT.`
- `Then write required_gross_edge(), which takes a style's trade frequency and target net return on capital and returns the gross per-trade edge needed to break even after all of the above. This is the spine of the whole study. Write a unit test for this with hand-checkable cases.`
- `TASK 5: RUN AND VERIFY`
- `Verify gaps, duplicate timestamps, timezone handling, trading-day alignment across assets. Write a single run_layer1.py report.hd covering what was loaded, what range each series spans, the risk-free rate history summary, and the cost structure table.`
- `When layer 1 runs cleanly without errors, and all tests pass run the checks and the test output. Do not process past Layer 1.`

**Argues:** Outlines explicit cost values, tax assumptions, micro futures contract sizing, and verification requirements.

### [00:14:32](https://www.youtube.com/watch?v=zGmsARTATvQ&t=872s) · slide · The engine (confidence: high)

**Values (as shown):**

- `LAYER 2 | PART 1 OF 2`
- `The engine`
- `one signal family, six speeds, measured frequency`
- `Continue trading_styles_lab. Layer 1 is complete. This is Layer 2.`
- `RULE OF THE LAB: One signal family across all rungs.`
- `Every rung in the ranking must be measured over the IDENTICAL data and under the identical cost model. Rungs can vary in speed, but not signal parameters. Only the intraday data varies.`
- `PRIMARY WINDOW: The first date your 1-minute data covers, through the last date all symbols share. State both dates explicitly.`
- `DATA PANELS: 1-minute data is NOT used in the primary ranking. Build a separate robustness panel for the rungs that have more history, and run the 1-minute panel only as a secondary check.`
- `THE SIGNAL ENGINE`
- `Parameters are held constant and vary only the holding period.`
- `SIGNAL: Donchian channel breakout. Enter long on a break of the N-bar high, exit on a break of the M-bar low, or at the session close for the intraday rungs. Long only.`
- `CRITICAL: Do NOT optimize or search parameters. Pick one fixed set and run it. The goal is not to find a good strategy; it is to measure frequency degradation. If a strategy is eventual-ly monotonic at every horizon, the single point is that signal parameter optimization masks frequency loss. Standard parameters: e.g. 20-period entry, 10-period exit for daily, or for intraday 20/10 for the long daily rungs, because those are standard. Write down why each was chosen.`

**Argues:** Defines Layer 2 signal rules, prohibiting parameter optimization to isolate trade frequency degradation.

### [00:14:36](https://www.youtube.com/watch?v=zGmsARTATvQ&t=876s) · slide · The engine (confidence: high)

**Values (as shown):**

- `LAYER 2 | PART 2 OF 2`
- `The engine`
- `continued`
- `HORIZONS`
- `1-minute intraday, flat by close`
- `5-minute intraday, flat by close`
- `15-minute intraday, flat by close`
- `1-hour intraday, flat by close`
- `daily short lookback (swing)`
- `daily long lookback (position)`
- `Intraday runs on Micro futures. Daily runs on both futures and ETFs. Note: futures vs ETF cost difference is visible at short horizons.`
- `WHAT TO REPORT, per horizon, over the common window`
- `MEASURED trades per year`
- `AVERAGE holding period`
- `gross return, gross Sharpe`
- `net return and net Sharpe after costs from costs.py`
- `after-tax net`
- `required gross edge per trade to break even`
- `percentage of gross profit consumed by costs`
- `The trade frequencies MUST be MEASURED from the signal, not typed in as a target. The fact that high-frequency trading is an assumption dressed as a result. This is the single most important thing in Layer 2.`
- `Also compute the passive benchmarks over the same window: SPY and QQQ buy and hold, and the CBOE index.`

**Argues:** Specifies the six target time horizons and key performance metrics to be computed and reported.

### [00:14:37](https://www.youtube.com/watch?v=zGmsARTATvQ&t=877s) · slide · The second family (confidence: high)

**Values (as shown):**

- `LAYER 3 | PART 2 OF 4`
- `The second family`
- `Continuous trading_styles_lab. Layer 2 is accepted. This is Layer 3.`
- `Three jobs: test a second signal family, fix the ranking metric, and test how stable the ranking is across time. Do not change costs.py or the data. Keep the exact same window where stated.`
- `PART A: THE SECOND SIGNAL FAMILY`
- `Layer 2 tested a TREND BREAKOUT, which is a trend-following rule, and trend rules are structurally expected to improve as the holding period lengthens. So the ladder may be measuring the signal family rather than the cost of speed. This is the steepest hole in the study and it has to be closed.`
- `Add a MEAN REVERSION family and run it at the identical six horizons, under identical conditions, through the identical cost module.`
- `RULE: Bollinger Band fade. Enter long when price closes below the lower band, exit when it closes back above the moving average. Default: 20-period, 2.0 standard deviations, scaled by bar count. Long only, flat by close intraday.`
- `SAME CONSTRAINT AS LAYER 2: Do not optimize, search, or compare parameters. One fixed rule, standard values.`

**Argues:** Introduces Bollinger Band fade (mean reversion) to determine if performance decay is signal-specific or universal.

### [00:14:39](https://www.youtube.com/watch?v=zGmsARTATvQ&t=879s) · slide · The second family (confidence: high)

**Values (as shown):**

- `LAYER 3 | PART 3 OF 4`
- `The second family`
- `continued`
- `The question this answers: mean reversion is supposed to FAVOR fast trading. If the ladder is still monotonic under a family that should favor speed, the finding is about costs and not the rule. If the ladder breaks, say so plainly. A broken ladder is a more interesting result and I would rather know.`
- `Report the two families side by side at every horizon and state explicitly whether the ordering is the same under both.`

**Argues:** Explains why testing mean reversion at high frequencies isolates cost structure effects from signal mechanics.

### [00:14:40](https://www.youtube.com/watch?v=zGmsARTATvQ&t=880s) · slide · The second family (confidence: high)

**Values (as shown):**

- `LAYER 3 | PART 4 OF 4`
- `The second family`
- `continued`
- `PART C: WINDOW STABILITY`
- `Split the primary window into non-overlapping sub-periods. Use calendar years or regime buckets. Define regime buckets you derive from SPY's price: bull, chop, and drawdown. Define them by a stated rule, and write the rule down.`
- `For every rung report its rank within each sub-period and compute a rank-stability measure across sub-periods.`
- `Then the key output: which findings hold IN EVERY sub-period, which hold in most, and which are artifacts of the full-window average. Give me a plain list of claims sorted by how well they survive, because only the survivors are worth stating.`
- `PART D: SENSITIVITY TO COSTS`
- `Re-run the ranking at 0.5, 1.0, and 1.5 ticks of entry slippage and state plainly whether the order changes. That matters more than the default value itself.`
- `SUMMARIZE: Take all these results, then tell me in plain language what the final ranking is, which claims I can state without qualification, and which I cannot.`

**Argues:** Specifies regime bucket analysis, rank stability metrics, and slippage sensitivity testing for Layer 3.

### [00:14:54](https://www.youtube.com/watch?v=zGmsARTATvQ&t=894s) · screen · THANKS FOR WATCHING (confidence: high)

**Values (as shown):**

- `THANKS FOR WATCHING`
- `DON'T FORGET TO LIKE, COMMENT, SHARE`
- `SUBSCRIBE`

**Argues:** Closing end screen prompting user engagement.

## Formulas

- [00:03:02](https://www.youtube.com/watch?v=zGmsARTATvQ&t=182s) `Cost Ratio = Total Friction / Gross PnL`
  - `Cost Ratio`: Multiplier representing transaction friction relative to gross trading profits
  - `Total Friction`: Sum of round-turn commissions, entry/exit slippage, and taxes paid
  - `Gross PnL`: Raw profit generated by trading strategy before accounting for costs

## Strategies

### Scalping (Bollinger Fade / Mean Reversion - 1-min) ([00:02:41](https://www.youtube.com/watch?v=zGmsARTATvQ&t=161s))

**Logic:** Mean reversion strategy on 1-minute MNQ futures. Buys when price drops below lower Bollinger Band and sells when price returns to 20-bar average.

**Entry rules:**
- Buy when price closes below the 20-bar, 2-standard-deviation lower Bollinger Band.

**Exit rules:**
- Exit when price reaches the 20-bar mean or average holding time of 14 minutes is reached.

| parameter | value |
|---|---|
| Timeframe | 1-minute |
| Average Hold Time | 14 minutes |
| Trade Frequency | 10 trades/day (1,838 trades/year) |
| Bollinger Period | 20 bars |
| Bollinger StdDev | 2.0 |

**Markets/assets:** MNQ (Micro E-mini Nasdaq-100 futures)

**Stated performance:** Gross Sharpe +0.575; Net Sharpe -2.865; Net Return -15.9%/yr; Cost ÷ Gross P&L 5.98x; Max loss -$178,052 on $100k account.

**Costs/slippage mentioned:** yes — Micro commission $1.20 round turn + 1 tick entry slippage + 1 tick exit slippage = $11.00 total break-even cost per trade ($20,218 annual friction).

### Fast Day Trading (5-min) ([00:04:35](https://www.youtube.com/watch?v=zGmsARTATvQ&t=275s))

**Logic:** Fast day trading setup executed on 5-minute charts holding positions for around 70 minutes and closing flat before market close.

**Entry rules:**
- Enter trade setup on 5-minute chart upon trigger.

**Exit rules:**
- Exit after ~70 minutes holding period or flat by market close; no overnight holding.

| parameter | value |
|---|---|
| Timeframe | 5-minute |
| Average Hold Time | 70 minutes |
| Trade Frequency | 2 trades/day (504 trades/year) |

**Markets/assets:** MNQ (Micro E-mini Nasdaq-100 futures)

**Stated performance:** Gross Sharpe +0.242; Net Sharpe -0.613; Net Return -3.0%/yr; Cost ÷ Gross P&L 3.55x.

**Costs/slippage mentioned:** yes — Micro commission $1.20 round turn plus 1 tick entry and exit slippage.

### Patient Day Trading (Donchian Breakout - 15-min) ([00:05:39](https://www.youtube.com/watch?v=zGmsARTATvQ&t=339s))

**Logic:** Patient day trading strategy waiting for 1 high-conviction setup per day on 15-minute bars using Donchian channels.

**Entry rules:**
- Buy on a break above the 20-bar high.

**Exit rules:**
- Exit on a break below the 10-bar low or flat at close (holding ~3 hours).

| parameter | value |
|---|---|
| Timeframe | 15-minute |
| Average Hold Time | 3 hours |
| Trade Frequency | 1 trade/day (208 trades/year) |
| Donchian High Period | 20 bars |
| Donchian Low Period | 10 bars |

**Markets/assets:** MNQ (Micro E-mini Nasdaq-100 futures)

**Stated performance:** Gross Sharpe +0.483; Net Sharpe +0.141; Net Return +2.0%/yr; Cost ÷ Gross P&L 0.71x; Ending account equity $116,629 on $100k capital.

**Costs/slippage mentioned:** yes — Transaction costs consume 71% of gross profit.

### Hourly Donchian Breakout (Rank 6) ([00:07:11](https://www.youtube.com/watch?v=zGmsARTATvQ&t=431s))

**Logic:** 60-minute Donchian channel breakout strategy held across overnight sessions.

**Entry rules:**
- Enter on 60-minute Donchian channel upper/lower channel breakout on MNQ futures

**Exit rules:**
- Exit on opposite channel breakout or system signal

| parameter | value |
|---|---|
| timeframe | 60-minute |
| asset | MNQ (Micro E-mini Nasdaq-100) |

**Markets/assets:** MNQ

**Stated performance:** Net Sharpe: +0.628, Net Return/yr: 6.0%, ~132 trades/yr, Cost/gross P&L: 0.23x, Max Drawdown: -13%

**Costs/slippage mentioned:** yes — Transaction cost drag eats 23% of gross P&L.

### Options Premium Selling (Rank 5) ([00:07:57](https://www.youtube.com/watch?v=zGmsARTATvQ&t=477s))

**Logic:** Systematic option selling strategy collecting option premium for taking market risk.

**Entry rules:**
- Systematic short option / index put selling (benchmarked to CBOE PUT Index)

**Exit rules:**
- Option expiration or periodic index roll

| parameter | value |
|---|---|
| benchmark_index | CBOE PUT Index |

**Markets/assets:** CBOE PUT / S&P 500 Options

**Stated performance:** Net Sharpe: +0.685, Net Return/yr: 9.2%, Max Drawdown: -29% (2020 crash), outperformed SPY in 9 of 20 sub-periods

**Costs/slippage mentioned:** no

### Position Trading Donchian Breakout (Rank 4) ([00:09:03](https://www.youtube.com/watch?v=zGmsARTATvQ&t=543s))

**Logic:** Daily 55-bar Donchian channel trend following breakout on QQQ.

**Entry rules:**
- 55-bar high daily breakout on QQQ

**Exit rules:**
- 55-bar low trailing channel exit

| parameter | value |
|---|---|
| lookback_period | 55 bars |
| timeframe | daily |

**Markets/assets:** QQQ

**Stated performance:** Net Sharpe: +0.714, Net Return/yr: 9.2%, ~3 trades/yr, avg hold 63 days, Cost/gross: 0.00x, Max Drawdown: -12%

**Costs/slippage mentioned:** yes — Cost ratio is ~0.00x due to extremely low trade frequency (~3 trades/yr).

### Swing Trading Donchian Breakout (Rank 3) ([00:09:48](https://www.youtube.com/watch?v=zGmsARTATvQ&t=588s))

**Logic:** Daily 20-bar Donchian channel trend following breakout on SPY.

**Entry rules:**
- 20-bar high daily breakout on SPY

**Exit rules:**
- 20-bar low trailing channel exit

| parameter | value |
|---|---|
| lookback_period | 20 bars |
| timeframe | daily |

**Markets/assets:** SPY

**Stated performance:** Net Sharpe: +0.797, Net Return/yr: 8.0%, ~6 trades/yr, avg hold 33 days, Cost/gross: 0.01x, Max Drawdown: -7%

**Costs/slippage mentioned:** yes — Cost ratio is 0.01x.

### SPY Buy & Hold (Rank 2) ([00:10:47](https://www.youtube.com/watch?v=zGmsARTATvQ&t=647s))

**Logic:** Passive long-term allocation holding S&P 500 ETF.

**Entry rules:**
- Buy SPY at inception

**Exit rules:**
- None (Hold indefinitely)

**Markets/assets:** SPY

**Stated performance:** Net Sharpe: +0.848, Net Return/yr: 15.5%, turned $100k into $951,061 over 16 years, Cost/gross: 0.00x, Max Drawdown: -34%

**Costs/slippage mentioned:** yes — Cost ratio is 0.00x.

### QQQ Buy & Hold (Rank 1) ([00:11:43](https://www.youtube.com/watch?v=zGmsARTATvQ&t=703s))

**Logic:** Passive long-term allocation holding Nasdaq-100 ETF.

**Entry rules:**
- Buy QQQ at inception

**Exit rules:**
- None (Hold indefinitely)

**Markets/assets:** QQQ

**Stated performance:** Net Sharpe: +0.938, Net Return/yr: 20.4%, turned $100k into $1,873,048 over 16 years, Cost/gross: 0.00x, Max Drawdown: -35%

**Costs/slippage mentioned:** yes — Cost ratio is 0.00x.

### Donchian Channel Breakout ([00:14:32](https://www.youtube.com/watch?v=zGmsARTATvQ&t=872s))

**Logic:** Trend-following breakout strategy. Enters long when price breaks the N-bar high and exits when price drops below the M-bar low (or at session close for intraday).

**Entry rules:**
- Enter long on a break of the N-bar high (e.g. 20-period high).

**Exit rules:**
- Exit on a break of the M-bar low (e.g. 10-period low).
- For intraday horizons, exit at session close.

| parameter | value |
|---|---|
| Entry lookback N | 20 periods |
| Exit lookback M | 10 periods |

**Markets/assets:** SPY, QQQ, GLD, TLT, IWM, VXX, Micro futures

**Stated performance:** _none stated_

**Costs/slippage mentioned:** yes — $4.00 RT standard contracts / $1.25 RT micros, 1 tick entry/exit slippage, 10 bps execution penalty, 50c commission + 15 bps spread RT on ETF/QQQ, 50 bps per year short borrow rate.

### Bollinger Band Fade ([00:14:37](https://www.youtube.com/watch?v=zGmsARTATvQ&t=877s))

**Logic:** Mean reversion fade strategy. Enters long when price drops below lower Bollinger Band and exits when price closes back above moving average.

**Entry rules:**
- Enter long when price closes below the lower Bollinger Band.

**Exit rules:**
- Exit when price closes back above the moving average.
- For intraday horizons, exit flat by close.

| parameter | value |
|---|---|
| Lookback period | 20 periods |
| Standard deviations | 2.0 |

**Markets/assets:** SPY, QQQ, GLD, TLT, IWM, VXX, Micro futures

**Stated performance:** _none stated_

**Costs/slippage mentioned:** yes — Evaluated using the costs.py configuration module shared across all strategies.

## Tools & data

| name | type | how used |
|---|---|---|
| Claude (Opus 3.5) | api | Used to design, program, and structure the layered backtesting framework. |
| 1-Minute Futures Data | dataset | 16 years of continuous 1-minute historical price bars for ES and NQ/MNQ futures. |
| Daily ETF Data | dataset | Daily historical price data for SPY and QQQ ETFs. |
| CBOE PUT Index | dataset | Used as the published benchmark data source for evaluating options premium selling performance. |
| Donchian Channel | other | Technical indicator rule used for breakout entries and trailing exits across hourly, position, and swing trading tests. |
| Claude / Claude Code | platform | LLM platform used to execute multi-layered prompts for building trading backtests, cost models, and robustness analyses. |
| yfinance | library | Python library specified in prompts to pull daily total-return ETF price history and SPY benchmark data. |
| FRED | api | Federal Reserve Economic Data API used to retrieve DTB3 (3-month Treasury bill rate) for risk-free interest rates. |
| CBOE | dataset | Published PUT and BXM index history retrieved for premium-selling benchmark comparisons. |
| Parquet | other | File format used to store 1-minute intraday futures/ETF datasets and daily price series. |

## Open questions

- [00:02:00](https://www.youtube.com/watch?v=zGmsARTATvQ&t=120s) **A mechanical backtest accurately reflects average trader performance across different trading timeframes.** — Does not account for customized stop-loss/take-profit mechanics, discretionary timing, or alternative order types used by human traders.
- [00:06:12](https://www.youtube.com/watch?v=zGmsARTATvQ&t=372s) **Discretionary traders can turn high-frequency day trading profitable by identifying and skipping the worst 5% of losing trades in advance.** — Assumes human discretionary judgment can select 1,579 specific losing trades out of 42,914 1-minute dots without empirical validation of human accuracy.
- [00:08:44](https://www.youtube.com/watch?v=zGmsARTATvQ&t=524s) **Options premium selling requires sitting out during volatility spikes.** — No explicit volatility filter rule or market timing indicator was provided for when to sit out during market spikes.
- [00:13:00](https://www.youtube.com/watch?v=zGmsARTATvQ&t=780s) **Top discretionary intraday traders achieve a higher performance ceiling than buy-and-hold benchmarks on 1-minute and 5-minute charts.** — No empirical data, track record, or sample size of discretionary traders was provided to substantiate the high discretionary performance ceiling claim.
- [00:14:32](https://www.youtube.com/watch?v=zGmsARTATvQ&t=872s) **High-frequency intraday trading performance systematically degrades relative to lower-frequency trading purely due to transaction costs.** — The video presents prompt templates to test this hypothesis, but does not display backtest empirical results or output data in this clip.
