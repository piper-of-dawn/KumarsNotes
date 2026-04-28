### MODULE 2: SECURITY MARKET INDEXES

```table-of-contents
```

#### Index Weighting Methods

1. **Price return vs total return**: A price return index reflects only changes in constituent prices, while a total return index assumes all dividends and interest are reinvested. The headline **S&P 500** is a price return index, while **Germany's DAX** is quoted as a total return index, which is why naive comparisons are misleading. ==At inception PRI = TRI.==

2. **Price return index level**
$$  V_{PRI}=\frac{\sum_{i=1}^{N} n_i P_i}{D}$$
  The **divisor (D)** is **defined at inception** to scale the index to a base value. Its **numerical value is later adjusted only to maintain continuity** when mechanical events occur (stock splits, spin-offs, constituent changes), so the index does not show artificial gains or losses. Real-world hook: in the **Dow Jones Industrial Average**, Apple's stock split changed its price but not its economic value; the adjusted divisor prevented the Dow from falsely jumping.
3. **Price return (security or index)**: Measures only price change.

$$PR_i=\frac{P_{i1}-P_{i0}}{P_{i0}}$$

At the index level:

$$PR_I=\sum w_i\,PR_i$$
Dividends/interest are ignored.
    
4. **Total return = what investors actually earn**: Adds income to price change.

$$TR_I=\frac{V_{PRI1}-V_{PRI0}+Inc_I}{V_{PRI0}}$$

Over time, total return always exceeds price return when dividends exist.

5. **Price-weighted index (PWI)**: Each stock’s weight is proportional to its price. High-priced stocks dominate; stock splits mechanically reduce their weight unless the divisor is adjusted. Simple to compute but economically arbitrary. Equivalent replication: hold one share of each constituent. Examples: DJIA, Nikkei.
6. **Equal-weighted index (EWI)**: Each stock has the same weight. Implicitly rebalances back to equal weights; leads to higher turnover and a small-cap/Value tilt. Return ≈ arithmetic average of constituent returns. Matching requires frequent rebalancing to equal dollar amounts → higher transaction costs.
7. **Market-cap-weighted (value-weighted) index (MCWI)**: Weights are proportional to market capitalization. Buy-and-hold friendly; low turnover. Replicable by buy-and-hold of constituents at initial cap weights (aside from corporate actions). Momentum/large-cap tilt and tends to overweight overvalued names and underweight undervalued ones.
8. **Float-adjusted market-cap-weighted**: Same as MCWI but uses free-float shares (excludes closely held/government stakes) to better reflect investable, tradable supply.
9. **Fundamental-weighted index**: Weights based on fundamentals (book value, earnings, cash flow, dividends, sales). Intentionally value-tilted; higher turnover from periodic reconstitution.
10. **Rebalancing vs. reconstitution**: **Rebalancing restores target weights (e.g., equal weight each quarter). Reconstitution updates membership (adds/drops).** Both create transaction costs and potential index effects.

> [!abstract] MEMORISE
> - Core methods: **Price-weighted**, **Equal-weighted**, **(Float-adjusted) Market-cap-weighted**, **Fundamental-weighted**.
> - Biases: PWI → high-price bias; EWI → small-cap/value tilt + turnover; MCWI → large-cap/momentum tilt; Fundamental → value tilt.
> - Divisor: adjust D to maintain index continuity after splits/spin-offs/changes; no economic gain/loss from mechanical events.


> [!question] INDEX WEIGHTING NUMERICAL
> 
> Problem: Three stocks A, B, C. At t0: prices (A=50, B=20, C=10); shares (A=1, B=2, C=5). At t1: prices (A=55, B=18, C=12). No dividends. Compute t0→t1 returns for: Price-weighted, Equal-weighted, and Market-cap-weighted indices. Assume PWI divisor at t0 is D0=1 (base index), no corporate actions.
> 
> ---
> 
> Solution:
> - Individual returns: RA = 10%, RB = −10%, RC = 20%.
>
> Price-weighted (PWI) levels and return:
>
> $$I_0=\frac{50+20+10}{1}=80\qquad I_1=\frac{55+18+12}{1}=85$$
>
> $$R^{\mathrm{PWI}}=\frac{85-80}{80}=6.25\%$$
>
> Equal-weighted (EWI) return:
>
> $$R^{\mathrm{EWI}}=\frac{1}{3}\big(10\% - 10\% + 20\%\big)=6.67\%$$
>
> Market-cap-weighted (MCWI) weights and return:
>
> $$w_A=\frac{50}{140}=0.3571\quad w_B=\frac{40}{140}=0.2857\quad w_C=\frac{50}{140}=0.3571$$
>
> $$R^{\mathrm{MCWI}}=0.3571\cdot 10\%+0.2857\cdot(-10\%)+0.3571\cdot 20\%=8.93\%$$

> [!question] PRICE-WEIGHTED DIVISOR ADJUSTMENT (SPLIT)
> 
> Problem: Three stocks A, B, C. End of Day 1 prices: \$10, \$20, \$90. The price-weighted index uses divisor $D_1=3$, so index level is 40. On Day 2, C executes a 2-for-1 split (no other price changes). What divisor $D_2$ keeps the index level unchanged at the split instant?
> 
> ---
> 
> Solution:
> - Post-split C price = 90/2 = 45.
>
> $$\frac{10 + 20 + 45}{D_2} = 40\quad \Rightarrow\quad D_2 = \frac{75}{40} = 1.875$$
> 
> Explanation:
> - Adjust the divisor so mechanical events (splits) do not change the index. Economic value unchanged; only the share count/price split changes.
>

#### Uses and Types of Indexes

1. For commodities, 'quantity outstanding' is ambiguous (total reserves? annual production? stored inventory?). Because there is no universally accepted market cap equivalent for a physical good's futures contract, index providers must invent weighting rules. Common methods include equal weighting, global production values (e.g., S&P GSCI), or perceived importance determined by a committee. This leads to significant heterogeneity across different commodity indexes.
2. Large-cap, mid-cap, and small-cap definitions vary across different index providers because there is no universally agreed definition
3. In contrast to the capitalization weighting common in equity indexes, hedge fund indexes typically use: **Equal Weighting**
4. A commodity index will generate a positive roll yield when the futures market is in Backwardation.

> [!NOTE] ROLL YIELD
> 
You hold a futures contract. Time passes.
> - Futures must converge to spot at expiry.
> - If today’s futures price is above spot, it will drift down.
> - If today’s futures price is below spot, it will drift up.
**That drift, holding spot constant, is roll yield.**
5. The total return of a commodity index is calculated as the sum of the collateral yield, the spot price return, and the Roll Yield.
6. REIT valuations are driven by market-to-book ratios and earnings multiples, not a 'securitization premium.' REITs often trade below appraised values, not above.

7. **Rebalancing vs Reconstitution**: Rebalancing resets weights back to targets (usually quarterly). It matters most for equal-weighted indexes; price- and cap-weighted adjust via prices. Reconstitution adds/drops constituents when they no longer meet criteria (bankruptcy, delisting); committee judgment applies. Additions tend to push prices up; deletions down.
8. **Uses of indexes**:
   - Reflection of market sentiment: provide representative market returns (DJIA is popular but only 30 stocks, not broad).
   - Benchmark of manager performance: benchmark must match manager’s approach/style (e.g., value vs growth; small vs large).
   - Measure of market return and risk: asset-class expected return and standard deviation are estimated from index histories.
   - Measure of beta and risk-adjusted return: use an index as market proxy to estimate beta (CAPM) and expected return; compare to actuals.
   - Model portfolio for index funds: mutual funds, ETFs, and private portfolios replicate index returns.
3. **Equity index types**:
   - Broad market: captures >90% of market value; e.g., Wilshire 5000 (>6,000 stocks).
   - Multi-market: combines countries by region (e.g., Latin America), development (emerging), or global (e.g., MSCI World).
   - Multi-market with fundamental weighting: country sub-indexes cap-weighted; countries weighted by a fundamental (e.g., GDP) to avoid overweighting past winners.
   - Sector: industry groups (health care, financials, consumer goods); used for cyclical analysis, PM evaluation, and index products.
   - Style: by market cap and value/growth. Definitions vary (absolute thresholds or relative ranks). Classification often via P/E or dividend yield. Stocks migrate across styles → higher turnover than broad market.
4. **Fixed-income indexes**:
   - Many dimensions: issuer/collateral, coupon, maturity, credit risk (investment grade vs high yield), inflation protection; across sectors/regions/development levels.
   - Issues: very large universe; dealer markets and infrequent trading mean providers rely on dealer quotes; bonds mature → high turnover. Replication is difficult and expensive; constituent counts vary widely.
5. **Alternative investment indexes**:
   - Commodities: based on futures (not spot) for grains/livestock/metals/energy. Weighting differs (equal, production value, or fixed) → very different exposures and risk/return. Examples: Thomson Reuters/CoreCommodity CRB, S&P GSCI.
   - Real estate: appraisal-based indexes, repeat-sales indexes, and REIT indexes.
   - Hedge funds: managers report voluntarily → indexes vary substantially and have an upward bias.
6. **Global index characteristics**: Most widely used global security indexes are market capitalization-weighted with float adjustments; number of constituents varies.

> [!ABSTRACT] MEMORISE
> - Rebalancing: resets weights; key for equal-weighted. Reconstitution: changes membership; index effects on added/dropped names.
> - Uses: sentiment, benchmarking (match style), market return/risk, CAPM beta and expected return, model portfolios (index funds/ETFs).
> - Types: broad market, multi-market (incl. GDP-weighted by country), sector, style (higher turnover due to migration).
> - Fixed income: huge, illiquid, dealer-priced, high turnover → hard/expensive to replicate.
> - Alternatives: commodity indexes use futures and vary by weighting; real estate (appraisal/repeat-sales/REIT); hedge funds (voluntary reporting, upward bias).

> [!tip] Quick checks
> - Equal-weighted: Needs frequent rebalancing to match index returns; price/cap-weighted typically don’t.
> - Style indexes: Expect higher constituent turnover due to migration across size/value-growth buckets.
> - Commodities: Futures-based; weights differ widely → different risk/return; don’t equate with spot.
> - Fixed income: Dealer quotes + illiquidity → replication is non-trivial and costly.
> - Most global indexes: cap-weighted with float adjustment.
> 

> [!question] rebalance or reconstitute?
> 
> problem: an index committee removes 3 soon-to-mature bonds and 1 defaulted bond, and inserts 4 actively traded bonds. what happened?
> 
> ---
> 
> solution: reconstitution (membership change), not rebalancing (weight reset).

> [!warning] COMMODITY INDEXES ≠ SPOT PRICES
> - Commodity indexes are built from futures prices, not spot commodity prices.
> - Index providers use different weighting schemes (equal, production value, fixed), so exposures vary a lot across indexes.
> - Consequence: A commodity index’s return can differ materially from the change in spot commodity prices over the same period.
