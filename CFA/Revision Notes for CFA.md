```table-of-contents
title: 
style: nestedList # TOC style (nestedList|nestedOrderedList|inlineFirstLevel)
minLevel: 0 # Include headings from the specified level
maxLevel: 3 # Include headings up to the specified level
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

### MODULE 8.1: THE BASICS OF HYPOTHESIS TESTING

1. Null hypothesis is always: **Effect doesn't exist**. Trust this statement like God or Gravity.
2. Significance level is the maximum type I error you are willing to tolerate. If p value > significance level, your CANNOT or FAIL TO REJECT the null hypothesis. Also trust this double negative statement like God or Gravity.

 > [!TIP] HAMMER THIS INTO YOUR HEAD
> Suppose null hypothesis is: the person is NOT pregnant. **Null is always no effect exists.** Type I error is a doctor telling a man that he is pregnant (False Positive). A positive outcome that is false. Type II error is a doctor telling a truly pregnant lady that she is not (False Negative). A negative outcome that is false.
> ![[Pasted image 20251230214023.png]]



> [!TIP] HAMMER THIS INTO YOUR HEAD
> - p-value measures, **how extreme is my sample**, given the null hypothesis is true. 
> - p-value measures how strong the evidence **against** the null hypothesis is, assuming the null is true.
> - A p-value of 0.01 means strong evidence that the drug is effective (null is no effect), since such results would occur only 1% of the time if the ground truth was no effect.

3. Power of the test is (1 - Type II error), that is probability of correctly rejecting a false null i.e. claiming the effect where it truly exists that is telling a pregnant lady that she is indeed pregnant. Remember it like: a powerful pregnancy kit can ALWAYS correctly identity if someone is indeed pregnant (even though it can give positive results that are false).4

### MODULE 8.2: TYPES OF HYPOTHESIS TESTS


## ECONOMICS

### MODULE 18.1: THE FOREIGN EXCHANGE MARKET
1. When you buy a forward contract, you agree to BUY an underlying at a agreed price at a future date. If I buy a Euro / Rupee forward from you at 1 EUR = 100 INR, I am obliged to buy 1 EUR @ 100 INR, no matter whatever is the price. I have **hedged** my risk. 
2. ==Real P/B Exchange Rate = Nominal P/B × (CPI Base / CPI Price)== You multiply nominal by how pricier base is with respect to price currency.
3. At a base period, the CPIs of the United States and United Kingdom are both 100, and the exchange rate is $1.70/£. Three years later, the exchange rate is $1.60/£, and the CPI has risen to 110 in the United States and 112 in the United Kingdom. What is the real exchange rate at the end of the three-year period. Here Nominal P/B = $1.6/£, CPI Base = 112, CPI Price = 110. Real P/B = 1.6 × (112/110) = 1.632
4. Suppose in January 1 EUR =  100 INR. In December 1 EUR = 120 INR. INR depreciated by 20%. To calculate EUR appreciation: 1 INR = 0.01 EUR in Jan and 1 INR = 0.0083 EUR in Dec. So EUR appreciated by (0.01-0.0083) / 0.01 = 16.99%

### MODULE 19.1: FOREIGN EXCHANGE RATES

1. A cross rate is a rate which is quoted using a third currency as a base. This is useful when there is no direct market between currencies in question.

> [!QUESTION] NUMERICAL
> Suppose INR / USD = 90.01 and PKR / USD = 279.90. INR and PKR do not trade. So to calculate PKR / INR
> PKR / INR = PKR / USD $\times$ USD / INR = 279.90 $\times$ (1/90.01) = 3.109
> This PKR / INR cross rate.


> [!tip] HAMMER THIS INTO YOUR HEAD
> **Spot + Cost of Carry - Benefits = Forward**
> Memorising and deeply understanding this one line will take you far 

2. We have domestic rate as $r_d$, foreign rate as $r_f$. 
	- Suppose we borrow spot(d/f) and lend to foreign. 
	- Here, cost of carry of spot = spot(d/f) $\times$ $r_d$
	- Here, benefits from investing spot into foreign country = forward(d/f) $\times$ $r_f$ . Why forward(d/f)? Because I will take back my money after one time period and will lock in forward rate today itself.
	- Now using **Spot + Cost of Carry - Benefits = Forward**. This gives spot(d/f) $\times$ $(1+r_d)$ - forward(d/f) $\times$ $r_f$ = forward(d/f)
	- ==spot(d/f)$(1+r_d)$ = forward(d/f)$(1+r_f)$== is no-arbitrage relationship.

> [!question] NUMERICAL
> Consider two currencies, the USD and the INR. The spot INR/USD exchange rate is 90.01, the 1-year riskless INR rate is 6.65%, and the 1-year riskless USD rate is 4.2%. What is the 1-year no-arbitrage forward exchange rate?
> Cost of borrowing INR = 90.01(1+0.065) = 95.86
> Benefits from lending USD = Forward(INR/USD)(1.042)
> Therefore no-arbitrage Forward(INR/USD)= 95.86/1.042 = 91.99

3. **How to make free money (arbitrage)?** Suppose Forward(INR/USD) is 92.5 > 91.99. Let us now borrow INR 9.01 Million from HDFC Bank @ 6.65% and convert it to USD. I have 100,000 USD which I lend to JP Morgan at 4.2%. Also I do a Forward(INR/USD) and lock in the price at 92.5. After 1 year:
		- JP Morgan pays me 100,000 (1.042) = 104,200, and I close the forward by selling 104,200 @ 92.5 which gives me INR 9.638 million. 
		- I pay back HDFC: 9.01 (1.0665) = USD 9.609 Million
		- I make free money = 9.638 - 9.601 = INR 0.028 Million ~ INR 28k.

> [!danger] DO NOT MAKE THIS MISTAKE
> Rates are always quoted annual. 

> [!question] NUMERICAL
> The spot ABE/DUB exchange rate is 4.5671, the 90-day riskless ABE rate is 5%, and the 90-day riskless DUB rate is 3%. What is the 90-day forward exchange rate that will prevent arbitrage profits?
> 90-day-rates: ABE = 0.0125, DUB = 0.0075
> Cost of borrowing DUB = 4.5671 (1.0125) = 4.624
> Forward(ABE/DUB) = 4.624 / 1.0075 = 4.589

3. **Forward rates are quoted as points, not prices:** points are the difference from spot, measured in the last decimal of the spot quote (e.g., with 4 decimals, 1 point = 0.0001). INR/USD future is trading at 198 bips, which makes forward rate = 90.01 + 1.98 = 91.99.
4. For INR, Forward > Spot, hence INR is trading at forward premium
## CORPORATE ISSUERS

### MODULE 24.1: CAPITAL INVESTMENTS AND PROJECT MEASURES
###### Expected number of questions: 3
###### LOS: Describe types of capital investments. Describe the capital allocation process, calculate net present value (NPV), internal rate of return (IRR), and return on invested capital (ROIC), and contrast their use in capital allocation.

#CRITICAL_MODULE


> [!ABSTRACT]- MEMORISE THESE FOR EFFICIENCY
> - Return on Invested Capital (ROIC) = PAT / Capital
> - Capital Turnover =  Revenue / Capital
> - After-Tax Margin = PAT / REVENUE
> - For NPV on TI Calc. Enter **CF**s (using **↓**) then **NPV**. Enter I then ↓ then **CPT**. 
> - IRR > Reqd Rate of Return → Accept Project
> - For IRR,  Calculate NPV then press **IRR** then **CPT**


1. Imagine an airline that has to replace aircraft engines as they age. This is a **going-concern project** because it is essential for airline survival. **The airline uses match funding approach**, that is, long-term debt or leases aligned with the engine’s life. ==Match funding because: An asset generates benefits over time. Financing has to be repaid over time. If these timelines don’t align, cash-flow risk appears.== 

> [!warning] Remember
> Maintenance activity that **reduces costs** will be a going concern project

1. If DGCA forces airlines to replace the old engines then that is a **Regulatory/compliance project**. If Indigo invests to buy Airbus A320s for international routes, then that is a **Expansion Project.**
2. The capital allocation process is identifying and evaluating capital projects (i.e., projects where the cash flows to the firm will be received over a period longer than a year). 
3. Capital Allocation Process looks like: Ideation → Forecast CF / Analyze → Budgeting → Audit 
4. A project has a conventional cash flow pattern if the sign on the cash flows changes only once, else it is unconventional.
5. NPV is the discounted PV of all future cashflows, discounted by Reqd. Rate of Return. IRR is the rate that makes NPV = 0. Accept if NPV > 0 and accept if IRR > Reqd. rate of Return.
6. NPV and IRR are forward looking approaches because you are talking about cashflows that **will happen in future.**

> [!warning] Remember
> It is important to understand, how cashflows are **reinvested** in each approach. **Under IRR method, they are reinvested at IRR and under NPV they are reinvested at Reqd. rate of return.**  

7. IRR is the discount rate that makes NPV = 0. If cash flows **change sign more than once** (e.g., − + − or − + − +), the NPV equation becomes a higher-degree polynomial, which can have **multiple real roots**. Each root is an IRR. Cash flows: −100 (today), +230 (year 1), −132 (year 2)  NPV(r) = −100 + 230/(1+r) − 132/(1+r)² = 0  This quadratic has **two solutions** → **two IRRs**.

> [!TIP] HAMMER THIS INTO YOUR HEAD
> Practice this on TI Calculator. You should be very very comfortable with this
> Suppose your cashflow stream is -1000, 100 ... (10 times). Required rate of return is 10%. Calculate NPV and IRR. 
> **CF** ⇢ **CLR WORK** ⇢ C0=-1000 ⇢ **ENTER** **↓** C01=100 ⇢ **ENTER** ⇢ F01=10 ⇢ **ENTER** ⇢ **NPV** ⇢ I=10 ⇢ **CPT**
> This gives NPV = -385.543
> Now do **IRR** ⇢ **CPT**
> This gives IRR = 0.0

8. **Return on Invested Capital (ROIC) = PAT / Average Invested Capital**
9. Operating Margin After Tax / After Tax Margin (PAT per unit Revenue) = PAT / Sales 
10. Capital Turnover (Revenue per unit capital) = Sales / Average Invested Capital.
11. **ROIC = After Tax Margin $\times$ Capital Turnover**
12. ROIC is backward looking because you are talking about PAT and Capital Investment that has **already happened**
13. ROIC is aggregated over a firm (Total PAT / Total Capital). So **profitable projects can hide trashy projects**. ROIC is accounting method and tax jurisdiction dependent hence **not comparable** across firms. ROIC can be **volatile** because it backward looking.
### MODULE 24.2: CAPITAL ALLOCATION PRINCIPLES AND REAL OPTIONS
###### Expected number of questions: 1
###### Describe principles of capital allocation and common capital allocation pitfalls
1. The three important 

### MODULE 25.1: WEIGHTED-AVERAGE COST OF CAPITAL

###### Expected number of questions: 1
###### Explain factors affecting capital structure and the weighted-average cost of capital

1. In general, the more **stable**, **non-cyclical**, **predictable**, and **recurring** are a company’s revenues and cash flows, the higher proportion of debt it can have in its capital structure. Eg: Walmart (regular cashflows and non-cyclicity), Adani (Huge amount of tangible assets for collateral and non-cyclicity).
2. Companies with low fixed operating costs can support larger debt. 
3. For raising additional debt: Interest Coverage Ratio = EBIT / Interest Expense → Higher the better. Debt to Equity Ratio → Lower the better. Debt to EBIT  → Lower the better.  
4. Capital structure is also dependent on the growth stage, a company is in. During startup stage, debt is very expensive. Company usually raises money through equity or convertible debt. During growth phase the risk is relatively lower and collateralized debt can be raised as capital. During mature stage, company can afford higher debt financing including unsecured debt. ==Remember: Startup companies can raise **Convertible Debt**, Growth ones can raise **Secured Debt** and Mature Ones can afford **Unsecured Debt**==
5. **Top Down Factors** such as inflation, the real GDP growth rate, monetary policy, and exchange rates impact capital structure. High Inflation scenarios demand greater yeilds.

### MODULE 25.2: CAPITAL STRUCTURE THEORIES
###### Expected number of questions: 2
###### LOS: Explain the Modigliani–Miller propositions regarding capital structure.

1. Costs of asymmetric information arise from the fact that managers typically have more information about a company’s prospects and future performance than owners or creditors. Firms with complex products or little transparency in financial statements tend to have higher costs of asymmetric information, which result in higher required returns on both debt and equity capital. Because shareholders and creditors are aware that asymmetric information problems exist, these investors look for management behavior that signals what knowledge or opinions management may have about the firm’s prospects. For example, taking on the commitment to make fixed interest payments through debt financing sends a signal that management is confident in the firm’s ability to make these payments in the future. By contrast, issuing equity is typically viewed as a negative signal that managers believe a firm’s stock is overvalued. The cost of asymmetric information increases with the proportion of equity in the capital structure
2. Agency costs of equity are related to conflicts of interest between managers and owners. Managers who do not have a stake in the company do not bear the costs associated with excessive compensation or taking on too much (or too little) risk. Because shareholders are aware of this conflict, they take steps to reduce these costs. The result is called the net agency cost of equity.
3. According to the free cash flow hypothesis, the use of debt forces managers to be disciplined with regard to how they spend cash because they have less free cash flow to use for their own benefit. It follows that greater amounts of financial leverage tend to reduce agency costs.
4. Pecking order theory, based on asymmetric information, is related to the signals that management sends to investors through its financing choices. According to pecking order theory, managers prefer to make financing choices that are least likely to send negative signals to investors. Financing choices under pecking order theory follow a hierarchy based on visibility to investors. Internally generated capital is most preferred, debt is the next-best choice, and external equity is the least preferred financing option. Pecking order theory implies that the capital structure is a by product of individual financing decisions.


## FSA
### MODULE 35.1: DIFFERENCES BETWEEN ACCOUNTING PROFIT AND TAXABLE INCOME
1. Suppose you have Operating Profit (EBIT) of USD 100. And   
### MODULE 37.2 TURNOVER AND LIQUIDITY RATIOS

> [!WARNING] Remember
> To memorise all the ratios and **most importantly their implications**

1. Turnover means how quickly something is replaced or replenished, inventory turnover ratio (ITR) would be COGS / Avg. Inventory, AR turnover (ART) would be Sales / Avg. AR, AP turnover would be COGS / Avg. AP. So think intuitively, for one unit of inventory, I have ITR units of COGS, so my inventory gets replenished ITR times. 

> [!Danger] DO NOT MAKE THIS MISTAKE
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
### SECURITY MARKET INDEXES
1. **Price return vs total return**: A price return index reflects only changes in constituent prices, while a total return index assumes all dividends and interest are reinvested. The headline **S&P 500** is a price return index, while **Germany’s DAX** is quoted as a total return index, which is why naïve comparisons are misleading. ==At inception PRI = TRI.==

2. **Price return index level**
$$  V_{PRI}=\frac{\sum_{i=1}^{N} n_i P_i}{D}$$
  The **divisor (D)** is **defined at inception** to scale the index to a base value. Its **numerical value is later adjusted only to maintain continuity** when mechanical events occur (stock splits, spin-offs, constituent changes), so the index does not show artificial gains or losses. Real-world hook: in the **Dow Jones Industrial Average**, Apple’s stock split changed its price but not its economic value; the adjusted divisor prevented the Dow from falsely jumping.
3. **Price return (security or index)**: Measures only price change.  $$PR_i=\frac{P_{i1}-P_{i0}}{P_{i0}}$$, and at the index level $PR_I=\sum w_i PR_i$. Dividends/interest are ignored.
    
4. **Total return = what investors actually earn**: Adds income to price change.    $$TR_I=\frac{V_{PRI1}-V_{PRI0}+Inc_I}{V_{PRI0}}$$Over time, total return always exceeds price return when dividends exist.

### MODULE 41.1: MARKET EFFICIENCY
1. In an efficient market, prices already reflect all available information, so they’re fair estimates of value; the return you earn is just pay for risk, not for being clever — in short, you can’t consistently beat the market.
2. When markets are efficient, passive investing makes sense because active trading gets eaten up by fees and costs; only when prices are genuinely wrong does active investing have a chance to add value.
3. Prices move only on surprises, not on expected news: earnings up 45% is good, bad, or irrelevant depending entirely on what the market had already priced in.
4. Market value is the asset’s current price, while intrinsic (fundamental) value is what a fully informed, rational investor would be willing to pay; in highly efficient markets, the two usually line up, but in less efficient markets active investors try to buy below intrinsic value and sell above it.  
5. Intrinsic value is based on fundamentals — for a bond, this means coupon, maturity, default risk, liquidity, and other key characteristics. Intrinsic value is constantly changing as new (unexpected) information becomes available.
6. **Information + attention**: markets are more efficient when lots of participants track them and when information is public, timely, and equally available. Fewer analysts, poor disclosure, or selective leaks → slower price adjustment and mispricing.    
7. **Ability to trade and correct prices**: arbitrage and short selling pull prices back to fair value, but only if trading is easy. High transaction costs, low liquidity, funding limits, or short-sale constraints let wrong prices survive.   
8. **Costs decide real efficiency**: markets are efficient if, **after all information, trading, and funding costs**, no positive risk-adjusted returns are left. Beating the market before fees doesn’t count if you lose after fees.
9. When we talk about market efficiency → We talk about return adjusted for risk. For this you need a model for expected returns such as CAPM. 
10. **Weak Form Efficiency:**
	1. Market prices reflect all the information in the historical market data. An investor cannot achieve positive risk-adjusted returns on average by using technical analysis because past price and volume (market) information will have no predictive power. 
	2. Trading on fundamentals or Trading on private information can still give you an edge.
11. Semi-Strong-Form Efficiency:
	1. Current security prices fully reflect all **publicly** available market and non information.
	2. Trading on private information can still give you an edge. 
12. Strong-Form Efficiency:
	1. Security prices fully reflect all information from both public and private sources.
	2. You just can't beat the market.
13. Technical analysis seeks to earn positive risk-adjusted returns by using historical price and volume (trading) data. These guys just harvest risk premia. 
14. Tests indicate that mutual fund performance has been inferior to that of a passive index strategy.
15. The majority of evidence is that anomalies are not violations of market efficiency but are due to the research methodologies used. 
16. **Event studies test semi-strong efficiency**: they ask whether you can make abnormal profits after public news. In developed markets, prices adjust almost immediately, so the null holds. *Example*: Apple launches a new iPhone, the stock barely moves on launch day because it’s already priced in. In less efficient markets, even well-known events (like Diwali sales numbers) can lead to slow, multi-day price reactions.
17. Market Anomalies break market efficiency. Momentum is an anomaly. Small cap outperforming Large cap is an anomaly (Size Effect). Low P/E ratio stocks outperform High P/E ones (Value Effect). Price action die to earning surprises persist for days, IPOs are typically underpriced, NAV of closed end MF is undervalued. 
18. **Information cascade**: less-informed investors copy early, better-informed traders; if the early movers truly have superior information, this herding can actually help prices move closer to intrinsic value rather than distort them.


### MODULE 42.2: FOREIGN EQUITIES AND EQUITY RISK
1. When capital flows freely across borders, markets are said to be integrated.
2. Listing on a foreign exchange increases firm transparency because of more disclosures and firm's publicity. 
3. Direct investing is buying foreign firm's stock on a foreign exchange. The investment and return are denominated in a foreign currency.
4. A **depository receipt** lets you own a foreign company while trading in your local market and currency; a depository bank holds the actual foreign shares and handles dividends and corporate actions. You buy **Toyota Motor Corporation ADR (TM)** on the NYSE in USD. The real Toyota shares trade in Japan, while **JPMorgan** holds those shares, converts Toyota’s yen dividends into dollars, and pays them to ADR holders.
5. Sponsored DR: issued with company involvement; investors usually get voting rights and better disclosure. Unsponsored DR: issued without company involvement; voting rights stay with the bank and disclosures are lighter.
6. Global Depository Receipts are issued **outside both the firm’s home country and the U.S.**, typically trade in **London or Luxembourg**, ==are often **USD-denominated**==, and avoid capital-flow restrictions—making it easier for global investors to invest. Firms list them where investors already recognize the company. **Tata Motors** has GDRs traded in **London**, letting international investors buy exposure to Tata Motors in USD without dealing with Indian market restrictions.
7. **ADRs** trade in the U.S., in USD, and usually require SEC registration. ==Some are also privately placed (Rule 144A or Regulation S receipts)==. **ADS (American Depository Share)**: the **actual underlying share** of the foreign company that sits in its **home market**.
8. Level I ADR trade OTC, and cheap to list. Level II ADR trade on Exchanges and are expensive to list. Both these CANNOT raise capital in US.
9. Level III is listed on exchange and CAN raise capital in US.
10. If it’s listed publicly, SEC is involved. In all Level I, II and III, SEC registration is required.
11. Rule 144A allows private listing. It is cheap and SEC is not involved. It can raise capital in US. 
### **MODULE** 43.2: REVENUE, PROFITABILITY,AND CAPITAL

12. To calculate margin always divide by Sales. For example:
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
	> Rivalry, new entrants and substitutes increase the bargaining power of buyers and reduces it for suppliers.

	1. **Rivalry:** Rivalry is highest when many similar firms face slow growth and high fixed costs, forcing price cuts to stay at full capacity. Delta, United, American cut fares aggressively because planes, fuel contracts, and crews are fixed costs and demand grows slowly.
	2. **Barriers to Entry:** Aramco and ExxonMobil face little new competition because oil production needs billions in drilling, refining, and scale.
	3. **Threat of substitutes**: Substitutes cap pricing by making demand more price-sensitive.Pfizer can charge high prices for patented drugs.
	4. **Bargaining power of Buyers:** Buyers of addictive goods such as Cigarettes have low bargaining power.
	5. **Bargaining power of Suppliers:** Microsoft is one of the few suppliers of operating system software and thus has pricing power.
4. **PESTLE (External Analysis):**
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
12. Residential mortgages are different because you **can’t freely prepay**. If you do, you **pay a penalty**,. They can be **recourse or non-recourse**: in recourse loans, the lender can **come after your other assets**; in non-recourse, they’re **stuck with just the house**.
 13. A 30-year US home loan that meets standards gets pooled and guaranteed by **Fannie Mae** or **Freddie Mac**. These **Agency RMBS** are backed either **directly by the government** or by **government-sponsored agencies** (quasi-government companies). Credit risk is basically **off your plate**. Non-agency RMBS: private-issued, no government/GSE backstop → investors eat credit risk. **2008:** subprime RMBS (e.g., Lehman Brothers) blew up; defaults surged, protections failed, MBS holders lost money.
 14. Mortgage pass-through = claim on cash flows from a pool of mortgages, net of admin fees. Pool can have any number of mortgages; each is a securitized mortgage.
 15. Mortgage A has an outstanding principal of USD 80, a coupon rate of 6%, and a final maturity of 30 years. Mortgage B has an outstanding principal of USD 20, a coupon rate of 4%, and a final maturity of 15 years. Total outstanding principal in the pool is USD 100. Weighted average coupon (WAC) = (80/100 × 6%) + (20/100 × 4%) = 5.6%. Weighted average maturity (WAM) = (80/100 × 30) + (20/100 × 15) = 27 years.
 
> [!DANGER] DO NOT MAKE THIS MISTAKE
> Outstanding and NOT beginning principal, while calculating weights.

16. A **Collaterized Mortgage Obligation (CMO) is a tranched MBS**. The **underlying cash flows are the same** mortgages. What changes is **how those cash flows are split and ordered**. Senior tranche gets paid first and lowest tranche gets paid the last. Total prepayment risk stays the same; it is redistributed across tranches.
17. **Z-tranche** = a CMO tranche that gets no cash interest at first.   During this phase, interest is not paid out; it is **added to principal** instead. Suppose Start: principal = USD 100, coupon = 5%. End of year: no cash paid, principal becomes USD 105. You didn’t get money; your claim just got bigger.
18. So the bond grows silently while other tranches take the cash. After the accrual period, Z-tranche starts receiving normal interest and principal payments. Z-tranche is usually last in line. It sacrifices early cash so other tranches get paid first.     
19. Principal-only (PO) securities and Interest-only (IO) securities are **interest-rate / prepayment bets**, not boring bonds. - If rates fall, people refinance → **prepayments speed up**.
20. You get **only interest payments**, no principal. You want loans to **stay alive as long as possible**. If rates rise or stay high → prepayments slow → **more coupon checks**. Used by investors who want to **bet on rising/stable rates and slow prepayments**.
    
### MODULE 58.1: YIELD-BASED BOND CONVEXITY AND PORTFOLIO PROPERTIES

###### MODULE 58.1: MODULE 58.1: YIELD-BASED BOND CONVEXITY AND PORTFOLIO PROPERTIES


> [!info] MEMORISE THIS FOR EFFICIENCY
> Effective Duration = $$ \frac{P_h - P_l}{P_o \times \Delta y} $$
> Effective Convexity = $$ \frac{P_h + P_l - 2P_o}{P_o \times (\Delta y)^2} $$

1. Effective duration assumes a **straight-line** price–yield relationship, meaning the slope is treated as the same no matter where yield is. Effective duration = **% price sensitivity to yield**: how much price changes (in %) when yield moves.    
2. Use symmetric yield shocks around **Y₀**: Y₁ = Y₀ + ΔY → price **P₁** (down), and Y₂ = Y₀ − ΔY → price **P₂** (up), with base price **P₀**.    
3. Central-difference idea: average slope of price vs yield near Y₀ ≈ **(P₂ − P₁) / (2ΔY)**.    
4. Convert slope into **percentage** sensitivity by dividing by P₀:  
    **Effective Duration = (P₂ − P₁) / (2 × P₀ × ΔY)**
5. Toy check: P₀=100, ΔY=0.01, P₁=96, P₂=104 ⇒ ED = (104−96)/(2×100×0.01)=8/2=**4** ⇒ ~**4% price move per 1% yield**, opposite direction.    
6. Use effective duration especially when **cash flows depend on yield** (callable/putable, MBS), where Macaulay/modified duration can mislead.
7. In reality, the price–yield relationship is **curved (convex)**, so the slope actually changes with yield.
8. Effective convexity measures the **curvature** of the price–yield relationship, i.e., the second-order effect after duration.    
9. Start at yield **Y₀** with price **P₀**. Move yield up by **Δy** → price becomes **P₁**. Move yield down by **Δy** → price becomes **P₂**.    
10. If the price–yield line were straight, the average of **P₁** and **P₂** would equal **P₀**. Any difference comes only from curvature.    
11. That curvature is captured by **P₂ − 2P₀ + P₁** (up + down − twice the middle).    
12. Convert this into a percentage measure by dividing by **P₀**, and scale it per unit of yield squared by dividing by **(Δy)²**.    
13. Final formula to remember:  
    **Effective Convexity = (P₂ − 2P₀ + P₁) / (P₀ · (Δy)²)**
14. Because of this, duration **understates the price gain when yields fall**.
15. And it **overstates the price loss when yields rise**.

> [!TIP] HAMMER THIS INTO YOUR HEAD
>  **Duration is pessimistic** — it underestimates price rise from a yield fall and exaggerates price decline from yeild rise.
16. **Convexity adjustment** is added to correct this straight-line error and account for curvature.

### MODULE 60.1: CREDIT RISK

1. **Bottom-up credit analysis = borrower first (the 5 Cs):**
   Capacity (the borrower’s ability to make their debt payments on time), Capital (Other financing sources available to reduce reliance on debt), Collateral (what can lenders grab on default?), Covenants (legal handcuffs protecting lenders), Character (management integrity and willingness to pay).
2. Bottom-up logic: even in a bad economy, a borrower with **strong cash flows, low leverage, good assets, tight covenants, and credible management** can survive.
3. **Top-down credit analysis = environment first:**
   Conditions (business cycle, rates, inflation), Country (political risk, legal enforcement, geopolitics), Currency (FX risk affecting debt repayment capacity).
4. Top-down logic: even a good borrower can fail if **macro turns hostile, country risk explodes, or currency collapses**.
5. **Corporate debt repayment sources:** primary source is **operating cash flows**; secured debt also has **pledged collateral**, unsecured debt relies only on business cash flows plus backups like **asset sales, divestitures, or new debt/equity**.
6. **Corporate credit risk drivers:** weak economy or markets, stronger competition, low profitability, or **too much leverage**.
7. **Sovereign debt repayment sources:** **tax revenue, tariffs, fees**; secondary sources are **issuing more debt** or **selling public assets (privatization)**.
8. **Sovereign credit risk drivers:** poor growth, political instability, **fiscal deficits**, and **high debt relative to GDP**.
9. **Illiquidity vs insolvency:** illiquid = can’t raise cash right now; insolvent = **assets < liabilities**. An issuer can be illiquid but still solvent and still default.
10. **Cross-default clause:** If the issuer defaults on **one bond**, all other bonds with a cross-default clause are **immediately treated as defaulted**, even if they were being paid on time.
11. **Pari passu clause:**- **Pari passu means “equal footing.”** Bonds with a pari passu clause have **no priority among themselves** in default. If two bonds are pari passu, **neither gets paid before the other** just because of issue date, size, or holder.
12. Default on one unsecured bond → **all unsecured bonds default** → **all unsecured holders line up together** and claim the issuer’s **general assets** (no collateral).
13. They are paid **first from collateral**. Only if collateral value is **not enough to cover all secured claims** do they start taking losses. Loss happens **only when** collateral value < total pari passu secured debt.
14. **Probability of default (PD):** the chance that the borrower **fails to pay interest or principal when due**, usually stated on an **annual basis*.   
15. **Recovery, loss severity, and exposure:** recovery rate is the **fraction of the claim recovered after default**; **loss severity = 1 − recovery rate**; exposure at default is **what you are owed minus the value of collateral available**.    
16. **Loss given default (LGD):** the loss **if default happens**, stated in money or percent; in percentage terms  
    **LGD% = expected exposure × (1 − recovery rate)**.
17. Fair Spread  = PD $\times$ LGD

> [!QUESTION] NUMERICAL
> A bond issuer has a 3% probability of default, and one of its bond issues has a recovery rate of 75%. The bond has a 4% coupon and is currently trading at par. A government security of similar maturity yields 2.5%. Assess whether the credit spread of the bond issue is adequately compensating investors for credit risk.
> 
> Here: Spread  = 4 - 2.5 = 1.5% = 0.015
> Fair Spread = PD $\times$ LGD = 0.03 $\times$ 0.25 = 0.0075
> **Bond is trading over-valued at twice its fair spread**

18. An analyst would need to estimate PD and LGD for the counterparty. Solvency ratios like:
		- Interest Coverage Ratio = EBIT / Interest
		- Financial Leverage = Average Total Assets / Average Total Equity
		- Fixed Charge Coverage = (EBIT + Lease Payments) / Interest + Lease Payments. This could be useful for US GAAP based companies with operating leases (where lease expense is shown as operating expense).
19. AAA (Aaa) is the highest rating. Think **pre-2008 mortgage CDOs**—they wore AAA badges and still blew up. Rating ≠ safety. Investment grade is **Baa3 / BBB− and above**. When **Ford** fell to junk in 2005, many funds were forced sellers overnight. The line matters. Below that (Ba1 / BB+ and lower) is **high-yield / junk**. Example: **Tesla bonds (2014–2018)** paid junk yields despite hype because default risk was real. Defaulted bonds are **D (S&P/Fitch)** or **C (Moody’s)**. Example: **Lehman Brothers 2008**—investment grade to default in days.
20. Longer-duration bonds usually have longer maturities and carry more uncertainty of future creditworthiness.
21. Credit migration risk: Investors can lose value without default—price damage comes from worsening credit perception, not missed payments. This is the risk that a borrower’s credit quality changes over time, shown by a rating upgrade or downgrade, even without default. A downgrade increases required yield spreads, reducing bond prices and increasing funding costs for the issuer.
22. Spreads are a **price of fear**, not just default math. When conditions worsen, investors demand more yield immediately. Credit spread risk = spreads widen → bond prices fall. This is the real risk for **investment-grade**, not sudden default.
23. Macro driver #1: business cycle. In booms, profits rise, defaults feel far away → spreads compress. In recessions, fear spikes → spreads widen. Classic **2008–09 GFC** pattern. High-yield behaves more violently than IG across the cycle. Dispersion is larger. Some junk names blow out, others survive.
24. Crisis effect: **flight to quality**. Investors dump risky bonds and pile into safe ones. Liquidity matters: high-yield is less liquid, so bid-ask spreads explode in stress because nobody wants to buy trash.
25. The limitation for ratings are:
	- Ratings lag markets. In early 2007, **subprime spreads exploded** while ratings stayed high. Markets smelled smoke first.
	- Same rating, different yields. Example: two **distressed airline bonds** with equal ratings—one with planes as collateral traded tighter than one with nothing backing it.
	- Hard-to-model risks get missed. **BP (Deepwater Horizon, 2010)**—environmental disaster nuked credit quality overnight.
	- Split ratings are common. **Italy’s sovereign debt** often had different ratings across agencies, confusing investors and widening spreads.
	- Agencies make mistakes. Systemic ones. **2008 GFC** is the canonical failure—AAA paper behaving like lottery tickets.
	- Fraud kills suddenly. **Enron** was investment grade days before bankruptcy. Ratings couldn’t see cooked books.
	- Legal and regulatory shocks matter. **PG&E** bonds collapsed after California wildfire liabilities—ratings reacted late.

> [!question] NUMERICAL
> A 10-year bond has an annual coupon of 5% and a bid–offer spread of 99.5/100.5. The benchmark 10-year yield is 3%. Decompose the yield spread into liquidity spread and credit spread.
> First calculate midpoint price = (100.5+99.5)/100
> N =10, FV = 100, PV = -100, so bond is at-par and YTM = Coupon Rate = 5%
> Now at bid price of 99.5: N =10, PV = -99.5, PMT = 5, FV = 100, I/Y = 5.064 
> Now at bid price of 100.5: N =10, PV = -100.5, PMT = 5, FV = 100, I/Y = 4.935 
> Total Spread = 2**
> **Liquidity Spread = 5.064 - 4.935 = 0.129**
> **Credit Spread = 2 - 0.129 = 1.871**







## ETHICS

### STANDARD I(A) - PROFESSIONALISM - KNOWLEDGE OF THE LAW

#### Core Concepts

> **Stricter rule. Active awareness. Mandatory dissociation.**

1. Know the law that governs your role. **You need not know every law on earth.** Stay updated when laws/regulations change. When law and CFA differ → follow the stricter rule. If no law exists → follow CFA Standards
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
### STANDARD III(A) – DUTIES TO CLIENTS – LOYALTY, PRUDENCE, AND CARE


> [!tip] TALISMAN
> **Think like a trustee handling someone else’s money.**  You must put the **client’s interests first**, ahead of your firm and yourself.  Act with **care and prudence**, not bravado or hindsight.  Follow the **mandate and IPS**, manage conflicts in the client’s favor, and remember:  **losses don’t mean violation — bad process does.**

#### Core Concepts

1. Members and Candidates owe a **fiduciary duty** to clients and must act with loyalty, prudence, and care when managing client assets. A fiduciary is someone who manages another person’s money or decisions and must always act in that person’s best interest.
2. **Client interests come before** the interests of the firm and before personal interests in all investment actions and recommendations.
3. Acting with **prudence and care** means exercising sound judgment, reasonable diligence, and appropriate risk management—not guaranteeing returns.
4. The duty applies to **investment decisions, portfolio construction, execution, monitoring, and advice**, not just security selection.
5. ==Conflicts of interest must be **managed in favour of the client**==; disclosure alone does not justify disadvantaging the client.
6. When managing pooled or institutional assets, decisions must be made **for the benefit of the client as a whole**, consistent with the mandate.
7. This standard is about **process and priority**, ==not outcomes==; losses alone do not imply a violation.

#### Exam Traps (Violation)

1. **“The firm benefits too.”** Wrong logic: Firm gain is acceptable; correct logic: client interests must come first; tested angle: proprietary products, fee incentives.
2. **“I followed the mandate loosely.”** Wrong logic: Flexibility is fine; correct logic: straying from stated objectives violates prudence and care; tested angle: mandate drift.
3. **“I disclosed the conflict.”** Wrong logic: Disclosure cures harm; correct logic: client must not be disadvantaged even after disclosure; tested angle: conflicts vs loyalty.
4. **“This trade helps another client.”** Wrong logic: Helping one client justifies harm to another; correct logic: each client’s interests must be protected; tested angle: cross-client favoritism.
5. **“The risk paid off before.”** Wrong logic: Past success proves prudence; correct logic: risk must be suitable and justified at the time; tested angle: excessive risk-taking.
6. **“I was trying to recover losses.”** Wrong logic: Chasing losses helps clients; correct logic: reckless behaviour violates prudence; tested angle: loss recovery trades.
7. **“The client didn’t object.”** Wrong logic: Silence implies consent; correct logic: fiduciary duty is proactive; tested angle: passive client approval.
8. **“Everyone in the market does this.”** Wrong logic: Industry norms override duty; correct logic: fiduciary duty overrides market practice; tested angle: herding behaviour.
9. **“It increased firm revenue.”** Wrong logic: Revenue supports firm stability; correct logic: firm benefit is secondary to client interest; tested angle: fee-driven advice.
10. **“The loss was unavoidable.”** Wrong logic: Any loss excuses conduct; correct logic: poor process still violates the standard; tested angle: outcome vs process.

#### Exam Traps (Not a Violation)

1. **“The portfolio lost money.”** Losses alone occurred; correct logic: losses do not imply violation if decisions were prudent and aligned with objectives.
2. **“Another strategy performed better.”** Hindsight comparison is tempting; correct logic: fiduciary duty is judged ex ante, not ex post.
3. **“The client chose the risky option.”** Client-directed risk within mandate; correct logic: honoring informed client choice is allowed.
4. **“Fees were charged as disclosed.”** Fees were transparent and agreed; correct logic: disclosed, reasonable fees are permitted.
5. **“The market moved suddenly.”** Unforeseeable events caused loss; correct logic: no duty to predict all market shocks.
6. **“The decision favored the pooled fund.”** Action benefited the fund per mandate; correct logic: ==duty is to the client entity, not individuals==.
7. **“The client approved the policy.”** Client consent to strategy existed; correct logic: following agreed policy satisfies duty.
8. **“The manager followed the IPS.”** Actions aligned with written objectives and constraints; correct logic: compliance with IPS supports prudence.
9. **“Risk controls were in place.”** Loss occurred despite controls; correct logic: having and using controls meets the care requirement.
10. **“No conflict existed.”** No competing interests were present; correct logic: loyalty standard is satisfied.

---

### STANDARD III(B) – DUTIES TO CLIENTS – FAIR DEALING

> [!tip] TALISMAN
> **Everyone gets a fair shot.**  Don’t play favourites, don’t tip a few, and don’t allocate benefits to insiders first.  Treat clients **equitably**, not identically—use fair processes so no group is disadvantaged by timing, access, or allocation.

#### Core Concepts

1. Members and Candidates must deal **fairly and objectively** with all clients when providing investment analysis, recommendations, actions, and changes in recommendations.
2. **Fair dealing ≠ equal dealing**: clients may receive different outcomes due to size, mandate, or timing, but the **process** must be fair.
3. New or changed recommendations must be **disseminated broadly and promptly** so no subset of clients gains an unfair advantage.
4. **Allocation of trades and investment opportunities** must be fair and consistent with written policies.
5. Personal trades and proprietary accounts must **not be favored** over client accounts.
6. Differences across clients must be **justified by mandate, suitability, or operational constraints**, not favoritism.
7. The standard focuses on **process integrity**—how information and opportunities are shared—not on identical results.

#### Exam Traps (Violation)

1. **“I told my best clients first.”** Wrong logic: Loyalty to top clients is fine; correct logic: selective early disclosure violates fair dealing; tested angle: staggered dissemination.
2. **“Small clients don’t need this update.”** Wrong logic: Materiality varies by client size; correct logic: material changes must be shared fairly with all relevant clients; tested angle: information asymmetry.
3. **“The trade went to the house account.”** Wrong logic: Firm priority is acceptable; correct logic: client interests must not be subordinated; tested angle: proprietary trading.
4. **“I allocated fills to whoever asked first.”** Wrong logic: First-come is fair; correct logic: allocation must follow a pre-established, fair policy; tested angle: allocation bias.
5. **“I tweeted the recommendation.”** Wrong logic: Public posting ensures fairness; correct logic: uncontrolled release may advantage some clients over others; tested angle: social media timing.
6. **“VIP clients expect better access.”** Wrong logic: Paying more buys priority info; correct logic: unequal access to material recommendations is unfair; tested angle: tiered service misuse.
7. **“I waited to inform the rest.”** Wrong logic: Delay is harmless; correct logic: delaying dissemination creates unfair advantage; tested angle: timing gaps.
8. **“I filled the easiest accounts first.”** Wrong logic: Operational convenience is fine; correct logic: convenience cannot override fairness; tested angle: cherry-picking fills.
9. **“Personal trade executed earlier.”** Wrong logic: Small personal trades don’t matter; correct logic: personal trades must not precede client trades; tested angle: front-running.
10. **“Policy exists, but I didn’t follow it.”** Wrong logic: Having a policy is enough; correct logic: policies must be followed consistently; tested angle: policy noncompliance.

#### Exam Traps (Not a Violation)

1. **“Different clients got different prices.”** Market timing and liquidity differed; correct logic: unequal outcomes are allowed if the process is fair.
2. **“Institutional clients received bulk fills.”** Large clients got more shares **because the allocation policy says orders are filled pro-rata by order size**, not because they were favored; size-based outcomes are fine if the **policy is pre-set and applied to everyone**.
3. **“Model portfolios updated overnight.”** Some clients acted earlier **only because of operational timing**, not selective disclosure; the recommendation was released to **all clients as quickly as reasonably possible**, so fairness is preserved.
4. **“Some clients declined the trade.”** Client choice drove outcomes; correct logic: honoring preferences is fair.
5. **“IPS constraints limited participation.”** Suitability restricted access; correct logic: mandate-based differences are allowed.
6. **“Trade allocation followed written policy.”** Policy applied consistently; correct logic: fair process met.
7. **“Public announcement used official channels.”** Broad, controlled release occurred; correct logic: no selective disclosure.
8. **“Block trade prorated.”** A large trade was split **pro-rata across all eligible client accounts**, meaning everyone received the same percentage of what they requested; this is a **textbook fair-allocation method**.
9. **“Personal trades occurred after clients.”** The manager traded **only after all client orders were executed**, so clients had priority and there was **no front-running or preferential treatment**.
10. **“Operational errors documented and corrected.”** Isolated error addressed; correct logic: not favoritism, process corrected.
---

### STANDARD III(C) – DUTIES TO CLIENTS – SUITABILITY

> [!tip] TALISMAN  
> **Know the client before you know the product.**  
> Recommend only what **fits the client’s goals, risk tolerance, and constraints**.  
> Suitability is about **matching**, not maximizing returns.  
> A good product for the market can still be **wrong for this client**.

#### Core Concepts

1. Members and Candidates must **understand the client**—including objectives, risk tolerance, financial situation, and constraints—**before** making recommendations or taking action.    
2. Suitability applies to **recommendations, portfolio construction, and ongoing management**, not just one-time advice.    
3. Recommendations must be **consistent with the client’s IPS**; deviation requires client consent and IPS update.    
4. For **discretionary accounts**, the member is responsible for ensuring investments remain suitable over time.    
5. For **non-discretionary accounts**, the member must make suitable recommendations but is not responsible for client-directed unsuitable actions.    
6. Suitability is judged **at the time of the decision**, not using hindsight.    
7. This standard focuses on **client fit**, not product quality or market performance.  
#### Exam Traps (Violation)

1. **“This product has the highest return.”** Wrong logic: High return equals suitability; correct logic: suitability depends on client objectives and risk tolerance; tested angle: yield chasing.    
2. **“The client didn’t complain.”** Wrong logic: Silence implies suitability; correct logic: suitability is proactive, not reactive; tested angle: passive clients.    
3. **“It fits most clients.”** Wrong logic: General suitability is enough; correct logic: suitability is client-specific; tested angle: one-size-fits-all advice.    
4. **“The IPS is old.”** Wrong logic: Outdated IPS can be ignored; correct logic: must update IPS before deviating; tested angle: stale documentation.    
5. **“The client approved it verbally.”** Wrong logic: Informal consent suffices; correct logic: recommendations must align with documented objectives; tested angle: informal approvals.    
6. **“This improves diversification.”** Wrong logic: Diversification always means suitability; correct logic: diversification must still fit risk tolerance and constraints; tested angle: portfolio context.    
7. **“I only recommended, I didn’t execute.”** Wrong logic: Advice has no duty; correct logic: suitability applies to recommendations alone; tested angle: advisory roles.    
8. **“The market conditions changed.”** Wrong logic: Market change excuses mismatch; correct logic: suitability must be reassessed as conditions and client circumstances change; tested angle: ongoing duty.    
9. **“The client wanted aggressive growth.”** Wrong logic: Stated desire overrides capacity; correct logic: risk tolerance and capacity both matter; tested angle: willingness vs ability.    
10. **“Everyone uses this strategy.”** Wrong logic: Industry practice defines suitability; correct logic: client circumstances define suitability; tested angle: herding.
    
#### Exam Traps (Not a Violation)

1. **“The client rejected the recommendation.”** Suitable advice was given; correct logic: client choice does not create a violation.    
2. **“The client insisted on the trade.”** Client-directed action in a non-discretionary account; correct logic: document advice, execution allowed.    
3. **“The portfolio lost money.”** Loss occurred despite suitability; correct logic: losses do not imply unsuitability if fit existed at decision time.     
4. **“Risk tolerance changed later.”** Change happened after recommendation; correct logic: suitability judged ex ante. 
5. **“The client signed the IPS.”** Documented objectives exist; correct logic: acting within IPS supports suitability.    
6. **“The product underperformed peers.”** Relative performance lagged; correct logic: suitability is not relative performance.    
7. **“The account is discretionary.”** Manager adjusted holdings within mandate; correct logic: ongoing suitability maintained.    
8. **“The recommendation was conservative.”** Lower risk than client’s maximum; correct logic: being conservative is allowed if aligned with objectives.    
9. **“Client constraints limited options.”** Liquidity/tax constraints narrowed choices; correct logic: suitability respects constraints.    
10. **“Advice was updated after life changes.”** Client circumstances changed and recommendations were revised; correct logic: ongoing suitability duty met.
---

### STANDARD III(D) – DUTIES TO CLIENTS – PERFORMANCE PRESENTATION

> [!tip] TALISMAN  
> **Don’t sell dreams—show reality.**  
> Performance must be **fair, accurate, complete, and comparable**.  
> No cherry-picking, no smoothing, no hiding bad years.  
> If a reasonable investor can be misled, you’ve crossed the line.

#### Core Concepts

1. Members and Candidates must present **investment performance information fairly, accurately, and completely** to clients and prospective clients.    
2. Performance presentation includes **returns, benchmarks, time periods, composites, and marketing materials**, not just formal reports.    
3. You must **not misrepresent past performance** through cherry-picking, selective periods, or excluding poor results.    
4. Hypothetical, simulated, or back-tested performance must be **clearly labeled and explained** as such.    
5. Changes in strategy, benchmarks, or calculation methods must be **clearly disclosed**.    
6. Performance must be presented in a way that allows **reasonable comparison**, not designed to confuse or exaggerate.    
7. This standard is about **truthful presentation**, not whether returns were good or bad.
    
#### Exam Traps (Violation)

1. **“We only showed our best-performing accounts.”** Wrong logic: Best accounts represent skill; correct logic: excluding poor performers misleads; tested angle: cherry-picking.    
2. **“The time period makes us look better.”** Wrong logic: Short periods are fine; correct logic: selective time horizons distort reality; tested angle: period manipulation.    
3. **“The benchmark was changed quietly.”** Wrong logic: Benchmark choice is flexible; correct logic: undisclosed benchmark changes mislead; tested angle: benchmark switching.    
4. **“Back-tested returns look great.”** Wrong logic: Simulated performance equals real results; correct logic: hypothetical returns must be clearly labeled; tested angle: back-testing abuse.    
5. **“Everyone smooths returns.”** Wrong logic: Industry norm excuses conduct; correct logic: smoothing hides volatility and misleads; tested angle: return smoothing.    
6. **“We excluded accounts that left.”** Wrong logic: Former clients are irrelevant; correct logic: excluding terminated accounts inflates results; tested angle: survivorship bias.    
7. **“The footnote explains it.”** Wrong logic: Any disclosure is enough; correct logic: disclosures must be clear, prominent, and not misleading; tested angle: buried disclosures.    
8. **“The model did the calculation.”** Wrong logic: Automation removes responsibility; correct logic: members are responsible for what they present; tested angle: outsourced reporting.    
9. **“This is just marketing.”** Wrong logic: Ads are exempt; correct logic: marketing materials are covered by the standard; tested angle: promotional presentations.    
10. **“We never claimed it will repeat.”** Wrong logic: No future promise avoids violation; correct logic: misleading past presentation alone violates; tested angle: implication vs guarantee.
#### Exam Traps (Not a Violation)

1. **“Performance was poor.”** Returns were honestly shown; correct logic: bad performance alone is not a violation.   
2. **“Different benchmarks were used.”** Benchmarks matched strategies and were disclosed; correct logic: appropriate, disclosed benchmarks are allowed.    
3. **“Hypothetical returns were labeled.”** Simulated results clearly identified and explained; correct logic: transparency satisfies the standard.    
4. **“Fees were deducted consistently.”** Net-of-fee presentation applied uniformly; correct logic: consistent methodology supports fairness.    
5. **“Accounts entered and exited the composite.”** Changes followed written composite rules; correct logic: rule-based inclusion is acceptable.    
6. **“Marketing simplified the numbers.”** Simplification without distortion; correct logic: clarity without misrepresentation is allowed.    
7. **“Returns were recalculated after an error.”** Corrections disclosed; correct logic: fixing mistakes transparently is acceptable.    
8. **“Performance aligned with disclosures.”** What was shown matched what was described; correct logic: no misleading gap exists.    
9. **“Clients received full reports on request.”** Summary marketing plus full disclosure availability; correct logic: layered disclosure is acceptable.    
10. **“Standards like GIPS were followed.”** Recognized performance standards applied; correct logic: compliance supports fair presentation.
---

### STANDARD III(E) – DUTIES TO CLIENTS – PRESERVATION OF CONFIDENTIALITY

> [!tip] TALISMAN
> **Client information stays locked.**
> Don’t share, hint, gossip, or reuse client data—inside or outside work.
> Break confidentiality **only** if the client permits, the law requires it, or illegal activity is involved.

#### Core Concepts

1. Members and Candidates must **keep client information confidential**, including identity, holdings, transactions, and personal details.
2. Confidentiality applies **during and after** the professional relationship ends.
3. Information may be disclosed **only** with client consent, when required by law, or to prevent/identify illegal activity.
4. Using client information for **personal benefit** or for another client is prohibited.
5. Confidentiality covers **all forms**: verbal, written, electronic, social media, and casual conversations.
6. This standard protects **trust**, not convenience; silence and discretion are expected.
7. Firm policies may add restrictions, but **CFA obligations apply regardless** of firm culture.

#### Exam Traps (Violation)

1. **“I didn’t name the client.”** Wrong logic: Anonymity avoids breach; correct logic: identifiable details still disclose confidential info; tested angle: indirect identification.
2. **“It was after work.”** Wrong logic: Off-duty sharing is fine; correct logic: confidentiality applies at all times; tested angle: social conversations.
3. **“I shared it internally.”** Wrong logic: Colleagues can know; correct logic: access must be on a need-to-know basis; tested angle: internal leakage.
4. **“I used it for another client’s benefit.”** Wrong logic: Helping clients justifies sharing; correct logic: client info cannot be reused; tested angle: cross-client misuse.
5. **“The relationship ended.”** Wrong logic: Duty ends with engagement; correct logic: confidentiality survives termination; tested angle: former clients.
6. **“Everyone already knows.”** Wrong logic: Market awareness excuses sharing; correct logic: client-specific data remains confidential; tested angle: assumed public knowledge.
7. **“I hinted without details.”** Wrong logic: Vague hints are harmless; correct logic: hints and signals can still disclose; tested angle: tipping by implication.
8. **“It helped marketing.”** Wrong logic: Business benefit permits sharing; correct logic: client consent is required; tested angle: testimonials, case studies.
9. **“I stored it insecurely.”** Wrong logic: No sharing occurred; correct logic: failure to safeguard can breach confidentiality; tested angle: data security.
10. **“Compliance didn’t stop me.”** Wrong logic: Lack of enforcement excuses conduct; correct logic: personal duty remains; tested angle: policy gaps.

#### Exam Traps (Not a Violation)

1. **“The client approved disclosure.”** Explicit consent was given; correct logic: permitted sharing.
2. **“Law required reporting.”** Regulatory or court mandate existed; correct logic: legal compulsion allows disclosure.
3. **“Illegal activity was suspected.”** Reporting to authorities followed law; correct logic: preventing illegality is allowed.
4. **“Information was aggregated.”** No client could be identified; correct logic: truly non-identifiable data is acceptable.
5. **“Access was limited internally.”** Need-to-know controls applied; correct logic: proper internal handling.
6. **“Client used public platform.”** Client voluntarily made info public; correct logic: member didn’t disclose it.
7. **“Data was encrypted and secured.”** Safeguards in place; correct logic: duty to protect satisfied.
8. **“Client requested a reference.”** Client initiated and consented; correct logic: allowed.
9. **“Information was outdated and irrelevant.”** No identification possible; correct logic: not confidential.
10. **“Disclosure followed firm and law.”** Policies aligned with legal requirements; correct logic: compliant handling.