# Claude Tested Over 25,000 ICT Strategies (Here's What Works)

**Channel:** AI Pathways  
**URL:** https://www.youtube.com/watch?v=KML09tRtHM8  
**Duration:** 00:19:35

<sub>schema 1.0 · model gemini-3.8-flash · interactions · analyzed 2026-11-06T08:52:55Z · 118,517 tokens</sub>

## Summary

Brendan systematically tests Michael Huddleston's Inner Circle Trader (ICT) Silver Bullet strategy using Claude-assisted Python scripts across 16 years (2010–2026) of 1-minute futures data (NQ and ES). Testing 25,003 sampled parameter configurations out of an enumerated 257.8M combinatorial space, the study evaluates the strategy through a multi-stage gauntlet incorporating commissions, slippage, conservative fill logic, multiple testing luck correction (Benjamini-Hochberg FDR), out-of-market testing on ES, and a 2-year locked holdout. The analysis finds that while the raw textbook versions struggle or fail, a high-frequency variant and 420 parameter survivor sets pass validation. Crucially, ablation reveals that the liquidity sweep drives virtually all strategy edge (operating as a short-term mean-reversion mechanism), whereas the celebrated killzone windows and higher-timeframe directional bias filters actually degrade performance.

## Segments

### [00:00:00](https://www.youtube.com/watch?v=KML09tRtHM8&t=0s)–00:01:11 · Introduction and Dataset Overview

- Used Claude to execute over 25,000 backtests of the ICT Silver Bullet day trading strategy.
- Dataset encompasses 16 years of 1-minute futures data on NQ (Nasdaq) and ES (S&P 500), totaling 11.1 million bars and nearly 10 million simulated trades.
- 420 configurations out of 25,003 survived all validation gauntlet stages.
- Disclaimer: Content is educational and not financial advice.

### [00:01:11](https://www.youtube.com/watch?v=KML09tRtHM8&t=71s)–00:04:30 · The ICT Silver Bullet Setup and Discretion Problem

- The Silver Bullet setup consists of six core components: (1) liquidity level, (2) liquidity sweep, (3) displacement, (4) fair value gap (FVG), (5) entry on retrace into FVG, and (6) target at opposing liquidity.
- Strategy is strictly restricted to three 60-minute windows: London 3:00–4:00 AM NY time, New York AM 10:00–11:00 AM NY time, and New York PM 2:00–3:00 PM NY time.
- Promoters claim 70% to 80% win rates and daily predictable income.
- Testing difficulty stems from subjective definitions: different traders interpret sweeps, gap sizes, and biases differently without explicit quantitative rules.
- Using Claude to translate subjective visual chart rules into explicit code allows systematic evaluation.

### [00:04:30](https://www.youtube.com/watch?v=KML09tRtHM8&t=270s)–00:07:35 · Combinatorial Space and Testing Gauntlet

- Parameter dials (liquidity, timeframe, stop, window, gap size, entry, target, bias) produce 257,891,040 possible combinations.
- A uniform random sample of 25,003 configurations was tested alongside three specific named benchmarks: as_taught_5m, as_taught_1m, and as_traded.
- The Gauntlet includes: real trading costs on every trade ($4.00 round turn commission + 1 tick slippage on stops), ambiguous 1-minute bars touching stop and target treated as losses, comparisons against coin-flip null distributions, Benjamini-Hochberg FDR luck correction at 10%, zero-adjustment cold testing on ES, and a 2-year locked out-of-sample holdout.

### [00:07:35](https://www.youtube.com/watch?v=KML09tRtHM8&t=455s)–00:09:15 · Validation Funnel Results

- Out of 25,003 initial population: 9,481 (37.9%) generated >= 100 trades.
- 6,190 (24.8%) achieved Net PnL > 0 after costs.
- 2,191 (8.8%) achieved Net Sharpe > 0.5.
- 1,614 (6.5%) passed the Benjamini-Hochberg False Discovery Rate (BH-FDR) 10% filter.
- 420 (1.7%) passed cold validation on ES futures.
- as_taught_5m survived >= 100 trades and Net PnL > 0, but failed at Net Sharpe > 0.5.
- as_taught_1m reached the final stage but failed the ES cold test.
- as_traded passed every stage including ES cold validation.

### [00:09:15](https://www.youtube.com/watch?v=KML09tRtHM8&t=555s)–00:10:58 · Debunking Claims: Win Rate and Killzone Hours

- The claimed 70%–80% win rate was refuted: only 5 out of 25,003 configurations achieved 70%+ win rates (all taking ~1R quick targets ~20 times/year).
- Named versions produced win rates between 34% and 48% (as_taught_5m: 46% NQ / 48% ES; as_taught_1m: 37% NQ / 34% ES; as_traded: 42% NQ / 42% ES).
- Median win rate among the 420 survivors was 52%.
- Evaluating hourly windows showed the designated Silver Bullet killzones do not outrank ordinary hours: London 3-4 AM and NY PM 2-3 PM are average, while NY AM 10-11 AM posted a slightly negative net Sharpe.

### [00:10:58](https://www.youtube.com/watch?v=KML09tRtHM8&t=658s)–00:12:27 · Ablation Ladder: What Rules Drive Edge

- Ablation ladder starting with FVG-only entries scored Net Sharpe 0.33.
- Adding the liquidity sweep requirement surged Net Sharpe to 0.69 (+0.36 improvement).
- Adding the displacement filter reduced Net Sharpe to 0.59.
- Restricting trading to the 3 Silver Bullet hours dropped Net Sharpe to 0.56.
- Adding the 15-minute bias requirement plummeted Net Sharpe to 0.16.
- A hypothetical 'perfect lookahead' bias achieved a Net Sharpe of 1.02.
- The sweep is the single component providing statistical edge; subsequent ICT filters progressively destroy edge.

### [00:12:27](https://www.youtube.com/watch?v=KML09tRtHM8&t=747s)–00:14:08 · Trading Frequency and Income Quality

- as_taught_5m generates only 34 trades/year; as_taught_1m generates 133 trades/year; as_traded executes 1,906 trades/year (~6–8 trades/day).
- Neither textbook version functioned as an 'income replacement': as_taught_5m had 46% positive days, 44% positive weeks, 43% positive months, with an average of $10/day and worst day of -$2,054.
- as_taught_1m had 39% positive days, 46% positive weeks, 48% positive months, averaging $27/day with worst day -$1,284.
- as_traded achieved 52% positive days, 59% positive weeks, 62% positive months, averaging $133/day, but suffered a worst day of -$5,406 (equivalent to 40 average days) and a 12-day losing streak.
- Best survivor averaged $228/day, 62% positive days, 67% positive weeks, 68% positive months, but experienced a 19-day consecutive losing streak.

### [00:14:08](https://www.youtube.com/watch?v=KML09tRtHM8&t=848s)–00:16:30 · Holdout Test Results and Equity Curves

- In the final 2-year out-of-sample holdout (2024–2026), best survivor produced +$455,089 on NQ (Sharpe 13.09, 6804 trades, 66% win, 100% positive months, max DD $3,553) and +$186,170 on ES (Sharpe 10.34).
- as_traded generated +$251,311 on NQ (Sharpe 5.64, 4171 trades, 44% win, 96% positive months, max DD $6,549) and +$72,424 on ES (Sharpe 2.31).
- Full 16-year cumulative PnL: best survivor reached +$1,281,370; as_traded reached +$735,623; as_taught_5m reached only +$17,125.
- Key caveats: The holdout period coincided with a massive bull market favorable to dip-buying, and backtests assume theoretical limit order fills without adverse selection modeling.

### [00:16:30](https://www.youtube.com/watch?v=KML09tRtHM8&t=990s)–00:18:02 · The Discretion Premium and What Survived

- Calculated the 'discretion premium': a trader would need to accurately skip 17.2% of losing trades in advance to turn the textbook version into a profitable system.
- Summary recipe of surviving edge: (1) require liquidity sweep, (2) trade opposite to the sweep direction, (3) enter on 1m FVG after reversal, (4) trade frequently, (5) drop the 15m bias, (6) stop restricting to killzone hours.
- The underlying mechanism is classic mean reversion wrapped in proprietary ICT terminology.

### [00:18:02](https://www.youtube.com/watch?v=KML09tRtHM8&t=1082s)–00:19:35 · Building the Backtest Engine and Community Invitation

- Displays the exact multi-prompt architecture to build the system via Claude Code across Layers 1 through 6.
- Layer 1: Data ingestion and session labeling.
- Layer 2: ICT feature detection (FVG, sweeps, market structure shifts).
- Layer 3: Execution engine and order fill simulator.
- Prompt 4: Configuration definition, frequencies, and verification.
- Prompt 5: Statistical sweeps, null tests, FDR, and ablation.
- Prompt 6: Single-page HTML dashboard generation.
- Invites viewers to join his trading community on Skool for data scripts and full system guides.

## Claims

| ts | claim | evidence | caveats |
|---|---|---|---|
| [00:03:07](https://www.youtube.com/watch?v=KML09tRtHM8&t=187s) | ICT Silver Bullet generates a 70% to 80% win rate. | backtest | Only 5 out of 25,003 parameter configurations achieved 70%+ win rates, each making only ~20 low-R trades/year; the median win rate across 420 survivors was 52%, and textbook versions achieved 34% to 48%. |
| [00:03:01](https://www.youtube.com/watch?v=KML09tRtHM8&t=181s) | Silver Bullet is an everyday model providing consistent, steady daily income. | backtest | Textbook versions only trade 34 to 133 times per year and lose money more days/weeks/months than they win; even high-frequency variants suffer severe multi-week losing streaks (up to 19 days in a row) and single-day losses wiping out 40 days of average gains. |
| [00:10:52](https://www.youtube.com/watch?v=KML09tRtHM8&t=652s) | The designated ICT killzone windows (London 3-4am, NY AM 10-11am, NY PM 2-3pm) provide distinct statistical trading edge. | backtest | Hourly ablation shows killzone hours rank average compared to all other trading hours; NY AM 10-11am registered a slightly negative net Sharpe ratio. |
| [00:11:19](https://www.youtube.com/watch?v=KML09tRtHM8&t=679s) | The liquidity sweep is the only component in the ICT Silver Bullet setup that adds positive alpha. | backtest | Evaluated on 16 years of NQ data; adding subsequent rules like displacement, killzone restrictions, and 15-minute bias progressively degraded Net Sharpe from 0.69 to 0.16. |
| [00:14:53](https://www.youtube.com/watch?v=KML09tRtHM8&t=893s) | Top surviving Silver Bullet configurations generated over $250k–$455k during the 2024–2026 holdout period. | backtest | Holdout period occurred during an exceptionally strong bull market ideal for dip-buying, and fills were modeled as passive limit orders without accounting for queue position or adverse selection. |

## Visuals

### [00:00:09](https://www.youtube.com/watch?v=KML09tRtHM8&t=9s) · screen · The Silver Bullet, Tested (confidence: high)

**Axes / columns:** 16 yrs 1-minute data; 11.1M 1m bars NQ+ES; 258M CANONICAL SPACE; 25,003 TESTED; 9.98M SIMULATED TRADES; 420 SURVIVE EVERYTHING

**Values (as shown):**

- `Validation funnel: population 25,003`
- `>=100 trades: 9,481 (37.9%)`
- `net PnL > 0: 6,190 (24.8%)`
- `net Sharpe > 0.5: 2,191 (8.8%)`
- `BH-FDR 10%: 1,614 (6.5%)`
- `ES cold validation: 420 (1.7%)`
- `source: funnel_counts.json, es_validation.csv`

**Argues:** Summarizes the overall testing scale and shows that only 1.7% of 25,003 sampled configurations survived the complete quantitative validation funnel.

### [00:00:25](https://www.youtube.com/watch?v=KML09tRtHM8&t=25s) · diagram · How we tested it (confidence: high)

**Axes / columns:** THE DIALS; WHAT WE RAN; THE GAUNTLET

**Values (as shown):**

- `THE DIALS: liquidity, timeframe, stop, window, gap size, entry, target, bias`
- `257,891,040 possible versions`
- `WHAT WE RAN: 25,003 random sample`
- `THE NAMED VERSIONS: as_taught_5m, as_taught_1m, as_traded`
- `THE GAUNTLET: real costs, every trade; ambiguous candle = a loss; vs coin flips; luck-corrected; run cold on the S&P; graded as income`

**Argues:** Illustrates how subjective ICT concepts were discretized into combinatorial parameters, sampled, and put through strict quantitative evaluation rules.

### [00:01:11](https://www.youtube.com/watch?v=KML09tRtHM8&t=71s) · diagram · The Silver Bullet setup (confidence: high)

**Axes / columns:** Setup Steps; The Three Windows (New York Time)

**Values (as shown):**

- `1. liquidity`
- `2. sweep`
- `3. displacement`
- `4. fair value gap`
- `5. entry`
- `6. target`
- `LONDON: 3-4am`
- `NEW YORK AM: 10-11am`
- `NEW YORK PM: 2-3pm`
- `tagline: run the stops, then fill the gap`

**Argues:** Defines the mechanical candlestick sequence and killzone timing of the ICT Silver Bullet strategy.

### [00:09:16](https://www.youtube.com/watch?v=KML09tRtHM8&t=556s) · chart · The 70-80% win-rate claim (confidence: high)

**Axes / columns:** Version / Asset; Win Rate (%)

**Values (as shown):**

- `CLAIMED 70-80%`
- `5 of 25,003 configs reached the band (1R target dinner, $2.5k-$12k lifetime)`
- `taught 5m NQ: 46%`
- `taught 5m ES: 48%`
- `taught 1m NQ: 37%`
- `taught 1m ES: 34%`
- `traded NQ: 42%`
- `traded ES: 42%`
- `Survivors (median): 52%`
- `source: named_configs_report.md, results_configs.csv, prerecord_verification.log`

**Argues:** Demonstrates that actual win rates for standard and surviving versions fall between 34% and 52%, thoroughly debunking the 70-80% win rate claim.

### [00:09:16](https://www.youtube.com/watch?v=KML09tRtHM8&t=556s) · chart · Every session hour, ranked (confidence: high)

**Axes / columns:** Session Hour (NY Time); net Sharpe per hour

**Values (as shown):**

- `NY PM KZ 14:00: positive (~0.12)`
- `London KZ 03:00: positive (~0.05)`
- `NY AM KZ 10:00: negative (-0.04)`
- `Range: -0.6 to +0.4 net Sharpe per hour`
- `source: null_by_hr (via deterministic evaluator, null_summary.md)`

**Argues:** Compares performance across all 24 hours to show that the ICT killzones offer no superior edge, with the 10-11 AM window showing negative Sharpe.

### [00:10:59](https://www.youtube.com/watch?v=KML09tRtHM8&t=659s) · chart · Ablation ladder (NQ) (confidence: high)

**Axes / columns:** Feature Stage; net Sharpe

**Values (as shown):**

- `FVG only: 0.33`
- `+ sweep: 0.69`
- `+ displ.: 0.59`
- `+ SB hours: 0.56`
- `+ 15m bias (as taught): 0.16`
- `PERFECT LOOKAHEAD: 1.02`
- `annotation: only the sweep earns its place; the taught bias subtracts`
- `source: ablation_ladder.csv`

**Argues:** Proves that the liquidity sweep is the sole beneficial component, while displacement, trading windows, and higher timeframe bias reduce strategy Sharpe.

### [00:10:59](https://www.youtube.com/watch?v=KML09tRtHM8&t=659s) · table · Null tests (NQ) (confidence: high)

**Axes / columns:** Version; vs RANDOM ENTRY; vs SHUFFLED DIRECTION

**Values (as shown):**

- `as_taught_5m: = RANDOM (p84), BEATS NULL (p100)`
- `as_taught_1m: BEATS NULL (p96), BEATS NULL (p100)`
- `as_traded: BEATS NULL (p100), BEATS NULL (p100)`
- `best_survivor: BEATS NULL (p100), BEATS NULL (p100)`
- `median_config: = RANDOM (p80), BEATS NULL (p100)`
- `source: null_summary.md`

**Argues:** Compares strategy configurations against synthetic random entry and shuffled direction null distributions to verify non-randomness.

### [00:12:27](https://www.youtube.com/watch?v=KML09tRtHM8&t=747s) · chart · How often do they trade? (confidence: high)

**Axes / columns:** Configuration; Trades per year

**Values (as shown):**

- `as_taught_5m: 34 / yr`
- `as_taught_1m: 133 / yr`
- `as_traded: 1,906 / yr`
- `source: results_configs.csv`

**Argues:** Shows textbook versions trade very infrequently, while the version traded in practice trades at a high frequency of ~1,906 trades per year.

### [00:13:05](https://www.youtube.com/watch?v=KML09tRtHM8&t=785s) · table · Income quality (NQ, non-holdout) (confidence: high)

**Axes / columns:** config; +days; +weeks; +months; worst streak; avg $/day; worst day; notes

**Values (as shown):**

- `as_taught_5m | 46% | 44% | 43% | 9 days | $10 | -$2,054 | loses more months than it wins`
- `as_taught_1m | 39% | 46% | 48% | 12 days | $27 | -$1,284 | 37.5% green days`
- `as_traded | 52% | 59% | 62% | 12 days | $133 | -$5,406 | worst day = 40 average days`
- `best_survivor | 62% | 67% | 68% | 19 days | $228 | -$2,168 | 19 straight losing days`
- `source: income_quality.csv`

**Argues:** Demonstrates that the strategy exhibits poor income stability, high drawdown risk, and significant multi-day losing streaks.

### [00:14:09](https://www.youtube.com/watch?v=KML09tRtHM8&t=849s) · chart · Does it transfer? NQ -> ES & Era split - survivors (confidence: high)

**Axes / columns:** NQ Net Sharpe (discovery); ES Net Sharpe (cold)

**Values (as shown):**

- `420 passed ES (cold >= 0.5)`
- `1,194 failed ES (cold < 0.5)`
- `Era split - survivors: 0.65 -> 0.69 (median survivor net Sharpe, 2010-2021 vs 2022-2023)`
- `75% of survivors keep Sharpe >= 0.5 post-2022 -- not an artifact of the early years`
- `roll days move survivor Sharpe by -0.004 (negligible); 1,035 of 1,614 survivors hold Sharpe >= 0.5 at 3-tick stop + 2-tick time-exit slippage`

**Argues:** Analyzes whether parameters discovered on NQ retain profitability when tested cold on ES and across different historical regimes.

### [00:14:34](https://www.youtube.com/watch?v=KML09tRtHM8&t=874s) · table · The holdout - one run, numbers are final (confidence: high)

**Axes / columns:** config; NQ Net; NQ Sharpe; NQ trades; NQ win; ES Net; ES Sharpe

**Values (as shown):**

- `best survivor | +$455,089 | 13.09 | 6804 | 66% | +$186,170 | 10.34`
- `survivor 2 | +$124,142 | 8.18 | 2672 | 63% | +$50,008 | 2.11`
- `survivor 3 | +$125,757 | 7.91 | 2542 | 64% | +$48,913 | 2.01`
- `as_traded | +$251,311 | 5.64 | 4171 | 44% | +$72,424 | 2.31`
- `as_taught_1m | +$12,364 | 1.01 | 79 | 54% | +$1,276 | 0.14`
- `as_taught_5m | +$33,949 | 1.89 | 264 | 43% | +$12,547 | 1.83`
- `all 420 frozen survivors, one run: 96% positive on NQ, median +$10.3k, median Sharpe 2.19, 91% positive on ES`

**Argues:** Presents final 2-year locked out-of-sample holdout metrics, showing top survivors and as_traded performing strongly during 2024–2026.

### [00:16:13](https://www.youtube.com/watch?v=KML09tRtHM8&t=973s) · chart · Equity, 2010 -> holdout end (NQ, net) (confidence: high)

**Axes / columns:** Year (2010 - 2030); Cumulative Net Profit ($M)

**Values (as shown):**

- `best survivor: +$1,281,370`
- `as_traded: +$735,623`
- `as_taught_5m: +$17,125`
- `random-entry null band (5-95%)`
- `HOLDOUT vertical dashed line at ~2024`

**Argues:** Displays 16-year equity growth, showing best survivor and as_traded significantly beating the textbook version and null band.

### [00:16:30](https://www.youtube.com/watch?v=KML09tRtHM8&t=990s) · screen · The discretion premium & The receipts (confidence: high)

**Axes / columns:** Metric; Value

**Values (as shown):**

- `The discretion premium: 17.2%`
- `The share of losing trades you must skip IN ADVANCE to make the taught setup hit Net Sharpe >= 1.0`
- `+ stop-first rule on ambiguous bars -- <=0.5% of trades on named configs; up to 9.5% on the worst holdout survivor`
- `+ $4.00 round turn + 1-tick stop slippage on every simulated trade`
- `+ slippage stress: 1,035 of 1,614 survivors keep Sharpe >= 0.5 at 3-tick stops + 2-tick time exits`
- `+ Sharpe = annualized daily net PnL, no-trade days count as zeros`
- `+ roll days: excluding them moves survivor Sharpe by -0.004`
- `+ entries fill only on TRADE-THROUGH, a touch is never a fill`
- `UNPRICED: adverse selection on limit fills -- the next test is live execution, not a backtest`

**Argues:** Quantifies the exact degree of subjective discretion required to make textbook ICT work, while listing conservative backtest safeguards.

### [00:16:57](https://www.youtube.com/watch?v=KML09tRtHM8&t=1017s) · slide · What survived: the recipe (confidence: high)

**Axes / columns:** Rule Number; Guideline

**Values (as shown):**

- `1. Require the liquidity sweep (the one gate that adds: 0.33 -> 0.70 Sharpe)`
- `2. Take direction FROM the sweep (beats shuffled direction at p100 on every surviving config)`
- `3. Enter on the 1m FVG after it (the 5m version cannot beat random entries [p84])`
- `4. Trade every setup, trade often (survivors are high-frequency, the median swept config managed 46 trades in 14 years)`
- `5. Drop the 15m bias (it subtracts: 0.56 -> 0.16)`
- `6. Stop worshipping the windows (the famous hours sit inside the pack of all 24)`
- `* The entire recipe is priced on paper fills - adverse selection on limit entries is unpriced; the next test is live execution.`

**Argues:** Summarizes the six empirical rules distilled from 25,000 backtests that explain all surviving performance.

### [00:18:04](https://www.youtube.com/watch?v=KML09tRtHM8&t=1084s) · code · Build it yourself - Prompt layers (confidence: high)

**Axes / columns:** Prompt Layer; Description

**Values (as shown):**

- `LAYER 1: Data and sessions (load 1-minute backadjusted parquet, sessions, verify timestamp alignment)`
- `LAYER 2: ICT feature detectors (FVGs, liquidity levels, sweeps, displacement, MSS, HTF bias)`
- `LAYER 3: Execution engine (fills, costs, stop slippage, ambiguous candle logic)`
- `PROMPT 4: Taught configs, frequency, verification (multi-trades, 15m liquidity, multi-window configs)`
- `PROMPT 5: The sweep, nulls, and statistics (canonicalization, grid, BH-FDR, null tests, holdout)`
- `PROMPT 6: Results dashboard (single-page HTML dashboard generation)`

**Argues:** Provides the complete prompt template sequence to reproduce the study in Claude Code.

## Formulas

- [00:16:30](https://www.youtube.com/watch?v=KML09tRtHM8&t=990s) `Discretion Premium = (Losing Trades Skipped in Advance) / (Total Losing Trades) = 17.2%`
  - `Discretion Premium`: The exact proportion of losing trades a discretionary trader must filter out prior to entry to elevate the textbook ICT strategy to Net Sharpe >= 1.0
- [00:07:18](https://www.youtube.com/watch?v=KML09tRtHM8&t=438s) `BH-FDR: P_(i) <= (i / m) * Q`
  - `P_(i)`: Individual p-value of a tested parameter configuration ranked in ascending order
  - `i`: Rank of the p-value
  - `m`: Total number of tested hypotheses/configurations (25,003)
  - `Q`: False Discovery Rate threshold set at 10% (0.10)

## Strategies

### ICT Silver Bullet (Textbook 5-minute / as_taught_5m) ([00:01:11](https://www.youtube.com/watch?v=KML09tRtHM8&t=71s))

**Logic:** Waits for a liquidity sweep of a prior session high or low during one of three 1-hour killzone windows, seeks displacement creating a Fair Value Gap on the 5-minute chart aligned with 15-minute directional bias, enters on a retracement to the gap, and targets opposing liquidity.

**Entry rules:**
- Identify key liquidity level (prior session high/low or swing high/low).
- Wait for price to sweep liquidity during specific windows (London 3-4am, NY AM 10-11am, NY PM 2-3pm).
- Confirm displacement moving in the opposite direction.
- Confirm 5-minute Fair Value Gap (FVG) creation.
- Enter limit order at proximal edge or 50% midpoint of the 5-minute FVG on retracement.

**Exit rules:**
- Stop loss placed beyond the swing high/low that caused the sweep.
- Take profit set at opposing liquidity target or fixed R:R.

| parameter | value |
|---|---|
| Timeframe | 5-minute |
| Trading Windows | London 3-4 AM, NY AM 10-11 AM, NY PM 2-3 PM (NY time) |
| Target | Opposing liquidity or 2R |

**Markets/assets:** NQ (Nasdaq 100 Futures), ES (E-mini S&P 500 Futures)

**Stated performance:** Generates only 34 trades/year; 46% win rate on NQ (48% on ES); fails Sharpe > 0.5 hurdle; produced only +$17,125 net over 14 years.

**Costs/slippage mentioned:** yes — $4.00 round turn commission per contract plus 1 tick slippage on stops.

### ICT Silver Bullet (Textbook 1-minute / as_taught_1m) ([00:06:01](https://www.youtube.com/watch?v=KML09tRtHM8&t=361s))

**Logic:** Identical logic to as_taught_5m but operates on 1-minute bars for FVG detection and entry execution, filtering by 15-minute bias and killzone windows.

**Entry rules:**
- Liquidity sweep during London 3-4am, NY AM 10-11am, or NY PM 2-3pm.
- Displacement creating 1-minute FVG in direction of 15-minute bias.
- Limit entry at proximal edge or 50% midpoint of the 1-minute FVG.

**Exit rules:**
- Stop loss placed at swing extremity.
- Take profit target at opposing liquidity or fixed 2R.

| parameter | value |
|---|---|
| Timeframe | 1-minute |
| Trading Windows | London 3-4 AM, NY AM 10-11 AM, NY PM 2-3 PM (NY time) |

**Markets/assets:** NQ (Nasdaq 100 Futures), ES (E-mini S&P 500 Futures)

**Stated performance:** 133 trades/year; 37% win rate on NQ (34% on ES); Net Sharpe 1.01 in holdout on NQ (+$12,364), but fails ES cold validation (Sharpe 0.14).

**Costs/slippage mentioned:** yes — $4.00 round turn commission per contract plus 1 tick slippage on stops.

### ICT Silver Bullet ('as_traded' / High-Frequency Mean-Reversion Variant) ([00:06:12](https://www.youtube.com/watch?v=KML09tRtHM8&t=372s))

**Logic:** A looser, practical implementation: removes 15-minute bias, considers any recent swing high/low as liquidity, enters on 1-minute FVG immediately after a sweep across multiple windows, allowing re-entries after exits.

**Entry rules:**
- Price sweeps any recent swing high/low.
- Direction set opposite to the sweep (fading the swept level).
- Enter on 1-minute FVG after reversal.
- No higher-timeframe bias filter required.
- Permit multiple entries per session.

**Exit rules:**
- Stop loss beyond displacement swing.
- Target next opposing liquidity level or fixed 2R.

| parameter | value |
|---|---|
| Timeframe | 1-minute |
| Bias | None |
| Trade Frequency | 1,906 trades/year (~6-8 trades/day) |

**Markets/assets:** NQ (Nasdaq 100 Futures), ES (E-mini S&P 500 Futures)

**Stated performance:** Passes all funnel stages; Holdout NQ Net PnL +$251,311 (Sharpe 5.64, 44% win rate, 4,171 trades); ES Net PnL +$72,424 (Sharpe 2.31); 16-year cumulative PnL +$735,623.

**Costs/slippage mentioned:** yes — $4.00 round turn commission per contract plus 1 tick slippage on stops.

## Tools & data

| name | type | how used |
|---|---|---|
| Claude Code / Claude AI (Anthropic) | other | Used to generate the backtesting framework, automate Python scripts, parse ICT rules into deterministic code, and build the analytics dashboard. |
| NQ (Nasdaq 100 Index Futures) Data | dataset | 16 years (2010–2026) of 1-minute backadjusted continuous futures data used as the primary discovery and backtesting dataset. |
| ES (E-mini S&P 500 Futures) Data | dataset | 16 years of 1-minute continuous futures data used for cold out-of-sample asset transferability validation. |
| pandas / pyarrow | library | Data engineering libraries specified in Layer 1 prompts to process parquet files and manage high-speed tabular time series. |
| Benjamini-Hochberg False Discovery Rate (BH-FDR) | other | Statistical algorithm applied at a 10% FDR threshold to eliminate strategies whose outperformance could be explained by multi-testing luck across 25,003 configurations. |
| Skool | platform | Community platform hosting the author's code templates, scripts, and full trading system backtesting guides. |

## Open questions

- [00:15:50](https://www.youtube.com/watch?v=KML09tRtHM8&t=950s) **Limit order execution fills in backtests reflect achievable real-world performance.** — The author explicitly concedes adverse selection is unpriced: real-world limit orders get filled when price crashes through the level (disproportionately capturing losers) and often fail to fill when price merely touches and bounces (missing winners).
- [00:15:35](https://www.youtube.com/watch?v=KML09tRtHM8&t=935s) **Holdout outperformance validates that the strategy will remain highly profitable in the future.** — The 2-year holdout (2024–2026) occurred during an aggressive multi-year equity bull market, which naturally flatters long-side dip-buying strategies; performance during prolonged bear or choppy sideways markets was not separately broken out for the holdout period.
