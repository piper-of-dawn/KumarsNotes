```table-of-contents
title: 
style: nestedList # TOC style (nestedList|nestedOrderedList|inlineFirstLevel)
minLevel: 0 # Include headings from the specified level
maxLevel: 0 # Include headings up to the specified level
include: 
exclude: 
includeLinks: true # Make headings clickable
hideWhenEmpty: false # Hide TOC if no headings are found
debugInConsole: false # Print debug info in Obsidian console
```
## Read these again 
- MODULE 24.2: CAPITAL ALLOCATION PRINCIPLES AND REAL OPTIONS

## QUANTITATIVE METHODS
### MODULE 6.1: LOGNORMAL DISTRIBUTIONS AND SIMULATION TECHNIQUES

1. **Log-Normal Distribution**
	1. If $\log(x)$ is normal, the $x$ is log normal. If $x$ is normal, then $e^x$ is log-normal. 
	2. Imagine **many parallel universes** starting today with the same initial price $P_0$. In each universe, the asset earns **continuously compounded (log) returns** over time. By definition of continuous compounding:$$ P_T = P_0 e^{r_{0,T}} $$where $r_{0,T}$ is the total log-return from 0 to $T$.
	3. These log-returns $r_{0,T}$ are independent (or weakly dependent) and identically distributed. Because log-returns **add**:  $$  r_{0,T} = \sum_{i=1}^n r_i $$By the **Central Limit Theorem**, the sum $r_{0,T}$ is approximately **normally distributed**.
	4. Since $\log P_T = \log P_0 + r_{0,T}$ is normal, $P_T$ is log-normally distributed** (not normal).

2. **Monte Carlo Simulation**
	 - Monte Carlo lets you test **scenarios that never happened**.  Example: Simulate a −40% equity crash even if history only saw −20%. Inputs are **not limited by past data ranges**. Example: Assume 80% volatility even if historical max was 35%.
	 - Results are **only as good as the assumptions**. Example: Assume normal returns → underestimate crash risk.
	 - Wrong assumptions give **precise but wrong answers**. Example: Simulation outputs USD 12.40, but real market price is USD 20 due to fat tails.
	 * Monte Carlo is **statistical, not analytic**. You get a price but no formula. It gives outcomes, **not intuition**. Example: You know the option value but not why it reacts strongly to volatility.
3. **Resampling and Bootstrapping:**
	- Start with n observed data points. Example: 250 daily returns.
	- For one bootstrap sample, do this: Randomly pick one return at a time from the original 250. Put it back after picking (sampling _with replacement_). Repeat until you have **250 picks**
	- Result is: Some days appear multiple times. Some days don’t appear at all. Total observations = still 250. Repeat this process many times (e.g., 10,000 bootstrap samples).
	- From 250 returns, bootstrapping shows the mean return is 8%, but with a wide spread (spread comes from 10k generated samples) → you see how unreliable that estimate is.
	- Instead of assuming normal returns, you reuse actual ugly days (crashes, spikes) exactly as they occurred. Even with small data, you can still quantify risk around estimates.
    
### MODULE 7.1: SAMPLING TECHNIQUES AND THE CENTRAL LIMIT THEOREM
1. Probability sampling: “Everyone had a ticket in the lottery.” Randomly selecting 500 firms from 10,000 gives each firm a 5% selection chance, making the sample’s average profitability an unbiased estimate of the population mean. This is probability sampling.
2. Non-probability sampling: “I picked whoever was easiest to reach.” Studying only easy-to-access or familiar firms (glossy reporters, followed companies, local firms) skews results because the sample is biased and not representative of the population. One way to form an approximately random sample is **systematic sampling** selecting every nth member from a population.
3. **Stratified sampling (Probability Sampling Method)** divides a heterogeneous population into homogeneous groups based on key characteristics and randomly samples from each group in proportion to its size. Eg: Estimating national income by first grouping people into income brackets (low, middle, high) and then randomly sampling individuals from each bracket in proportion to their population share.
4. One of the most important examples is of a bond index is replicated by grouping bonds by maturity and coupon, then randomly selecting bonds from each group in proportion to the group’s weight in the index.
5. **Cluster sampling (Probability Sampling Method)** means randomly picking a few groups that are assumed to look like the whole population and then collecting data from those groups instead of everyone. Eg: To estimate average student height in a city, randomly pick a few schools and measure all (or some) students in those schools instead of sampling from every school.
6. One-stage cluster sampling means randomly selecting a few clusters and including **every observation inside those clusters** in the sample. Eg: To estimate city electricity usage, randomly pick a few apartment buildings and use the electricity data of all households in those buildings.
7. Two-stage cluster sampling means randomly selecting a few clusters first (stage 1) and then randomly sampling individuals within each selected cluster (stage 2). To estimate city income, randomly pick a few neighborhoods and then randomly survey a sample of households within each selected neighborhood.
8. Two-stage cluster sampling can be expected to have greater sampling error than one-stage cluster sampling because you have done stuff randomly twice. But it costs less.
9. The non probability methods are Convenience Sampling and Judgemental Sampling. Convenience sampling refers to selecting sample data based on ease of access, using data that are readily available. Judgemental sampling refers to samples for which each observation is selected from a larger dataset by the researcher, based on one’s experience and judgement.
10. Suppose a sample contains the past 30 monthly returns for McCreary, Inc. The mean return is 2%, and the sample standard deviation is 20%. Calculate and interpret the standard error of the sample mean. SE($\mu$) = $\sigma / \sqrt{n}$ = 0.2 / $\sqrt{30}$ = 0.036. **As n $\to$ $\infty$, SE($\mu$) $\to$ 0
11. **Jackknife Method for SE:** From 5 returns {2, 4, 6, 8, 10}, compute 5 means by dropping one observation at a time (7, 6.5, 6, 5.5, 5). The standard deviation of these leave-one-out means estimates the standard error of the mean. **Works when sample size is small**
12. **Bootstrap Method for SE:** From the same 5 returns {2, 4, 6, 8, 10}, repeatedly draw samples of size 5 **with replacement** (e.g., {2,2,6,8,10}, {4,6,6,8,10}, …) and compute the mean each time.  After 10,000 such resamples, the **standard deviation of these means** is the bootstrap estimate of the standard error (and their percentiles give confidence intervals).
## FSA
### MODULE 37.2 TURNOVER AND LIQUIDITY RATIOS

> [!WARNING] Remember
> To memorise all the ratios and **most importantly their implications**

1. Turnover means how quickly something is replaced or replenished, inventory turnover ratio (ITR) would be COGS / Avg. Inventory, AR turnover (ART) would be Sales / Avg. AR, AP turnover would be COGS / Avg. AP. So think intuitively, for one unit of inventory, I have ITR units of COGS, so my inventory gets replenished ITR times. 

> [!Danger] Warning
> ITR is COGS / Avg Inventory, APR is COGS / Avg. AP, ART is Sale / Avg AR. 

2. Divide any turnover ratio by 365 and you get Days of that thing. For example, Days of Inventory (DIO) = 365 / ITR, Days of AP (DPO) = 365 / APR, Days Sales Outstanding (DSO) = 365 / ART
3. Current Ratio =  Current Assets / Current Liabilities. In liquidity ratios, the denominator will usually be CL. 
4. Cash Ratio =  (Cash + Marketable Securities) / Current Liabilities. Marketable Securities are anything that you can quickly sell and generate cash. 
5. Quick Ratio =  (Cash + Marketable Securities + AR) / Current Liabilities. 
6. Cash Conversion Cycle (CCC) = DSO + DIO - DPO. Assets are plus (Inventory and AR), Liability (AP) is minus. It measures how quickly inventory turns into cash. You can crank this up by aggressively demanding payments, not paying your suppliers. If it is negative then you require short term financing to cover the period. If it is positive, then you are sitting on cash that can be used in other parts of business. You can afford (CA < CL).
### MODULE 37.3 SOLVENCY AND PROFITABILITY RATIOS
1. Debt to Equity ratio = Total Debt / Total Shareholder Equity. All interest bearing instruments **except leases** are part of total debt. If question is silent, treat Preference shares as Total Shareholder Equity.
2. Debt to Capital Ratio = Total Debt / (Total Debt + Total Shareholder Equity)
3. Debt to Asset Ratio = Total Debt / Total Assets
4. Debt to EBITDA Ratio = Total Debt / EBITDA
5. Financial Leverage = Avg Total Assets / Avg Total Equity. *How much of shareholder equity has been used to finance the assets*
6. Interest Coverage = EBIT / Interest Payments **(Always EBIT, not EBITDA,  not PBT, and not PAT)**. Suppose I earn (EBIT) 100 and I have to pay 10 as interest, I can cover interest 10 times. 

> [!WARNING] Remember
> Any kind of margin is always calculated on Revenue

### MODULE 23.2 EXPENSE RECOGNITION
1. **Match costs with revenues:** recognize COGS **and estimated warranty costs** in the **period of sale**, not when paid in reality.
2. Remember US GAAP loves 'CFO'. Interest Expense go into operating always. IFRS gives you a choice. You can put Interest in 'CFF' or in 'CFO'.
3. IFRS is cool with splitting R&D. Research (incl. early software work) **expensed**; development (incl. saleable & internal software) **capitalized if criteria met**.
4. GAAP is strict, BOTH research and development is expensed. No capitalization at all.
5. GAAP hates R&D—except software. Saleable software = **capitalize (like IFRS)**; internal software = **capitalize only after build starts**.

## EQUITY

### MODULE 43.2: REVENUE, PROFITABILITY,AND CAPITAL

1. To calculate margin always divide by Sales. For example:
$$\text{Contribution Margin} = \frac{\text{(P - Var. Cost)} \times \text{Qty}}{\text{Revenue}}$$
> [!WARNING] Remember
> Operating Profit is **EBIT** (not EBITDA, not PAT or PBT)

2. Degree of Operating Leverage:
*By what percentage my operating profit moves with 1% change in sales*	$$ \text{DOL} = \frac{\Delta \% \text{EBIT}}{\Delta\% \text{Revenue}} $$
3. Degree of Financial Leverage
*By what percentage my net profit moves with 1% change in EBIT or operating profit*	$$ \text{DFL} = \frac{\Delta \% \text{PAT}}{\Delta\% \text{EBIT}} $$
Think in limits, suppose a firm is 0% leveraged, then $\Delta \% \text{PAT} = \Delta \% \text{EBIT}$, which implies DFL = 1 (no financial leverage). High DFL means **each borrowed buck magnifies outcomes**: more upside when EBIT rises, more pain when it falls.
4. Total Leverage = $DOL \times DFL$
$$ \text{TL} = \frac{\Delta \% \text{PAT}} {\Delta\% \text{Revenue}} $$



### MODULE 44.1: INDUSTRY ANALYSIS

1. GICS: Sector → Group → Industry → Sub-industry **[SGISub]**  
	ICB: Industry → Supersector → Sector → Subsector) **[ISSS]**  
	TRBC: Economic sector → Business sector → Group → Industry → Activity **[EBGIA]**
	*G for Group, S always for Sector, B for business, I for Industry*

2. How to classify?
	- **Single business:** classify in that business    
	- **Multiple businesses:** use the one with **≥60% revenue**    
	- **If not:** use **≥50% of revenue, profit, or assets**    
	- **If still unclear:** use **judgment** or label **conglomerate**
3. Other ways to group companies could be on the basis of business cycle (Consumer staples are stable so Defensive, Software is cyclical), geography, Financial Measures (large cap, mid cap) etc, or ESG (How green a company is?)
4. Company A sells USD 100 billion total in which Smartphones: USD 40 billion and Other products (laptops, services, TVs): USD 60 billion. Industry size = sales of the product, not total sales of multi-business firms. (only 40 bn in case of Smartphone industry)
5. Growth industries have considerable growth potential. (Semiconductors). Mature industries have little or no growth potential (Tobacco).
6. Profitability: Use ROIC (after-tax, capital-structure neutral) to rank firms by deciles, 
7. Market share = firm revenue ÷ industry size; levels are estimates, trends matter most.
8. Herfindahl Index (Industry Concentration) = sum of squared market shares; <1500 = low, 1500–2500 = moderate, >2500 = high concentration.

### MODULE 44.2: INDUSTRY STRUCTURE AND COMPETITIVE POSITIONING
1. Of the five forces described next, if some or all of them are strong, then firms will likely earn zero or close to zero economic profits (return on invested capital minus cost).
2. **Porter's Five Forces (Internal Analysis of Industry)**
	> **“Firms Fight, Entry is Expensive, Substitutes Cap Prices, Buyers Beg, Suppliers Rule.”**

	1. **Rivalry:** Rivalry is highest when many similar firms face slow growth and high fixed costs, forcing price cuts to stay at full capacity. Delta, United, American cut fares aggressively because planes, fuel contracts, and crews are fixed costs and demand grows slowly.
	2. **Barriers to Entry:** Aramco and ExxonMobil face little new competition because oil production needs billions in drilling, refining, and scale.
	3. **Threat of substitutes**: Substitutes cap pricing by making demand more price-sensitive.Pfizer can charge high prices for patented drugs.
	4. **Bargaining power of Buyers:** Buyers of addictive goods such as Cigarettes have low bargaining power.
	5. **Bargaining power of Suppliers:** Microsoft is one of the few suppliers of operating system software and thus has pricing power.
3. **PESTLE (External Analysis):**
	1. political, Trump may impose tariffs on your raw materials and you are bankrupt. Eg: Post tariff children toy industry in US. 
	2. economic, Economic cycles affect your business, an upcoming interest rate hike might wreck your leveraged business.
	3. social, This is how society reacts to a business, for example, don't try starting a beef factory in India (although its legal, but don't).
	4. technological, 
	5. legal,
	6. environmental

### MODULE 46.3 - RELATIVE VALUATION MEASURES

1. Common valuation multiples include **P/E, P/CF, P/S, and P/B**. You can invent others (e.g., price per user), but the logic is unchanged.    
2. Multiples are per-share comparisons. The **denominator must be per share**.
3. **Justified P/E** = what P/E _should be_ given fundamentals. **Market (non-justified) P/E** = what P/E _is_. Undervalued/overvalued comes from **comparing the two**.
4. Given reqd. discount $k$, dividend growth $g$, dividend $D$ and price $P$	$$ P_0 = \frac{D_1}{k-g} $$
5. Divide both sides by expected EPS $E_1$	$$ \frac{P_0}{E_1} = \frac{D_1/E_1}{k-g}$$
6. At LHS, it is Justified P/E which is always **leading**. The denominator is expected earnings $E_1$.
7. Raising the **dividend payout** increases current cash to shareholders but **reduces sustainable growth** by cutting reinvestment. Higher dividends push value up; lower growth pulls value down. The effects **offset**. This trade-off is called **dividend displacement of earnings**.
8. It is very important to understand the relationship of PE ratio to each of its parameters:
	- Payout Ratio ↑ PE multiple ↑
	- k ↑ PE Multiple ↓. High DE Ratio, or anything that signals higher risk would crank up required rate of return
	- g ↑ PE multiple ↑. Anything that signals higher future earnings would crank up g. For example, higher sales growth, bullish outlook etc.
9. The disadvantages of multiples based approach is:
	- **Comparable vs fundamental conflict**: Tesla can look _overvalued_ on peer P/E versus automakers, yet _fair_ or undervalued on a DCF assuming high growth.
	- **Accounting differences**: SAP (IFRS) vs Oracle (US GAAP) can show different P/E or P/B purely due to R&D and revenue-recognition rules.
	- **Cyclicality distortion**: Delta Air Lines may show a very low P/E at peak earnings (looks cheap) and a very high P/E in a downturn (looks expensive), driven by the cycle, not mispricing.
10. Enterprise value represents the total takeover cost: equity plus debt minus cash, because the acquirer assumes debt but also receives the cash.
11. EV is preferred when comparing firms with different capital structures; market cap alone can mislead.
12. EV must be matched with earnings available to both debt and equity holders, which is why EV/EBITDA is used; when net income is negative, P/E breaks but EV/EBITDA still works. Firm A has EV = 1,000, EBITDA = 100 → EV/EBITDA = 10. Net income = −10, so P/E is meaningless, but valuation via EV still works.
13. EBITDA can mislead because it ignores capital expenditures and can overstate cash flow. Eg: Vodafone Group often reports strong EBITDA, but heavy recurring capex on spectrum licenses and network upgrades absorbs most of the cash, so free cash flow remains weak despite attractive EV/EBITDA.
14. Asset-based valuation starts from the balance sheet and estimates equity as fair value of assets minus liabilities, adjusting book values using depreciated cost, inflation-adjusted cost, or replacement cost because book ≠ market.
15. Asset-based models struggle when intangibles dominate, so values are usually treated as a floor or liquidation value and work best only for tangible-asset-heavy or liquidation cases. Eg: Google has a brand, talent and data which makes tangible asset valuation meaningless.

## FIXED INCOME

### MODULE 65.1: MORTGAGE-BACKED SECURITY (MBS) INSTRUMENT AND MARKET FEATURES

1. **Prepayment Risk:** You own a callable bond (and interest rate falls) → They prepay and buy back their now cheaper bond issued at a high interest rate. Interest Rate falls to 2% and you take a cheaper loan and payback your expensive loan. For the bond investor, high-coupon mortgage cash flows disappear right when they’re most valuable, that is why a **risk**.
2. **Extension Risk:** Interest Rate ↑, Duration ↓ and Price ↓. Bond sellers (borrowers) won't exercise their call option. Expected cash-flows get extended. The market rate is higher but the bond buyer (investor) keeps receiving scraps from mortgages issued at low rates.
3. **Contraction Risk:** Interest Rate ↓, Duration ↑ and Price ↑. Prepayments speed up.  Bond sellers (borrowers) will exercise their call option. Cash-flows would arrive sooner than expected.
4. Because the prices of MBS reflect expectations for prepayments in low-rate environments, they will not rise as much in response to decreasing interest rates as other fixed-income instruments that do not have an embedded prepayment option.
5. Convexity is acceleration of prices with falling rates. Prepayments are friction. When rates fall, you lose the deals you earlier did (bought high coupon mortgages), so price of your MBS doesn't rise proportionally. So traditional FI instruments have +ve convexity and MBS **have a -ve convexity**

> [!TIP] HAMMER THIS INTO YOUR HEAD
> Long tranches absorb contraction risk. Short tranches absorb extension risk. People at the front of the queue hate delays (so they have to absorb extension), people at the back don't care because they were anyway waiting. 

6. A mortgage pool pays principal into two tranches: **Tranche S (short)** first, **Tranche L (long)** later. 
7. When **payments speed up**, principal rushes in. Tranch S is unaffected (it was already on the front line to get paid off). The contraction risk gets pushed to back of the line Tranch L. 
8. When **payments slow down (rates rise)**, prepayments stagnates. Tranch L is unaffected (it was already on the back of the line to get paid off). The extension risk hurts the front of the line.
9. If I take a loan of $100 against and pledge my asset of $200, my Loan to Value (LTV) is 200/100 = 2. 
10. A mortgage of USD 300,000 has an annual interest rate of 6%, is to be repaid monthly over 25 years, and the borrower’s annual pretax gross income is $80,000. Calculate DTI. Here, PV=-300,000, FV = 0, N = 25×12 = 300, I/Y = 6/12 = 0.5. This gives PMT = 1932. DTI = (1932 * 12) / 80000 = 0.289 ~ 28.9 %
11. Prime loans are made to creditworthy people, subprime loans are made to broke people.
12. 

## ETHICS

### STANDARD I(A) - PROFESSIONALISM - KNOWLEDGE OF THE LAW

#### Core Concepts

> **Stricter rule. Active awareness. Mandatory dissociation.**

1. Know the law that governs your role. You need not know every law on earth. Stay updated when laws/regulations change. When law and CFA differ → follow the stricter rule. If no law exists → follow CFA Standards
2. You must not knowingly participate or assist in violations If violations persist → dissociate (silence + staying = violation)
3. Legal advice does not override ethics obligation

#### Exam Traps

1. **“It’s legal in this country.”** Wrong logic: Local law allows it; correct logic: CFA is stricter → must follow CFA; tested angle: emerging markets, weak regulation.
2. **“I didn’t create the report.”** Wrong logic: Someone else prepared it; correct logic: using or distributing it = assisting; key phrase: *knowingly participates or assists*.
3. **“I escalated the issue.”** Wrong logic: Reporting alone is enough; correct logic: if violation continues → must dissociate; key phrase: *silence plus continued association*.
4. **“My lawyer said it’s fine.”** Wrong logic: Legal advice overrides ethics; correct logic: legal advice does not remove CFA obligations; tested angle: reliance on counsel.
5. **“I’m not a lawyer.”** Wrong logic: Ignorance excuses noncompliance; correct logic: must know laws directly governing your role; tested angle: role-based knowledge.
6. **“The client instructed me.”** Wrong logic: Client direction overrides rules; correct logic: law and CFA override client requests; tested angle: misleading disclosures, marketing.
7. **“My home country allows it.”** Wrong logic: Residence determines legality; correct logic: law governing the activity applies; tested angle: cross-border services.
8. **“I stayed silent.”** Wrong logic: Inaction avoids liability; correct logic: knowing inaction may be participation; key phrase: *failure to dissociate*.
9. **“There’s no regulation on this.”** Wrong logic: Absence of law means permitted; correct logic: follow CFA Standards; tested angle: regulatory gaps, new products.
10. **“Compliance handles this.”** Wrong logic: Delegation transfers responsibility; correct logic: duty remains if you know or should know; tested angle: shared accountability.