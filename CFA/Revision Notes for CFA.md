```table-of-contents
title: 
style: nestedList # TOC style (nestedList|nestedOrderedList|inlineFirstLevel)
minLevel: 0 # Include headings from the specified level
maxLevel: 3 # Include headings up to the specified level
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

### RATES OF RETURN
1. Interest rate = price of waiting. The required rate of return (discount rate) is the minimum return investors demand to delay consumption.
2. Nominal = real growth + inflation protection. Money must grow in real terms and also keep up with inflation. Exact relation (Fisher equation):
$$(1 + r_{nominal}) = (1 + r_{real}) \times (1 + \pi_{expected})$$
Expected inflation, not current inflation, because interest rates price the future.
$$ r_{nominal} \approx r_{real} + \pi$$Expected inflation, always
3. Every premium exists because uncertainty exists
	- Maturity Risk Premia: More time ⟶ more volatility ⟶ maturity premium. In simple words, a lot more could go wrong if money is locked up for long.
	- Liquidity Risk Premia: Asset might be very hard to sell if I need money quickly.
	- Default risk premia: The borrower may refuse or declare inability to pay.
	- Inflation premia: Purchansing power of money is lower in future.


### MODULE 6.1: LOGNORMAL DISTRIBUTIONS AND SIMULATION TECHNIQUES

1. **Log-Normal Distribution**
	1. If $\log(x)$ is normal, the $x$ is log normal. If $x$ is normal, then $e^x$ is log-normal. 
	2. Imagine **many parallel universes** starting today with the same initial price $P_0$. In each universe, the asset earns **continuously compounded (log) returns** over time. By definition of continuous compounding:$$ P_T = P_0 e^{r_{0,T}} $$where $r_{0,T}$ is the total log-return from 0 to $T$.
	3. These log-returns $r_{0,T}$ are independent (or wedakly dependent) and identically distributed. Because log-returns **add**:  $$  r_{0,T} = \sum_{i=1}^n r_i $$By the **Central Limit Theorem**, the sum $r_{0,T}$ is approximately **normally distributed**.
	4. Since $\log P_T = \log P_0 + r_{0,T}$ is normal, $P_T$ is log-normally distributed** (not normal).

2. **Monte Carlo Simulation**
	 - Monte Carlo lets you test **scenarios that never happened**.  Example: Simulate a \u221240% equity crash even if history only saw \u221220%. Inputs are **not limited by past data ranges**. Example: Assume 80% volatility even if historical max was 35%.
	 - Results are **only as good as the assumptions**. Example: Assume normal returns ⟶ underestimate crash risk.
	 - Wrong assumptions give **precise but wrong answers**. Example: Simulation outputs USD 12.40, but real market price is USD 20 due to fat tails.
	 * Monte Carlo is **statistical, not analytic**. You get a price but no formula. It gives outcomes, **not intuition**. Example: You know the option value but not why it reacts strongly to volatility.
3. **Resampling and Bootstrapping:**
	- Start with n observed data points. Example: 250 daily returns.
	- For one bootstrap sample, do this: Randomly pick one return at a time from the original 250. Put it back after picking (sampling _with replacement_). Repeat until you have **250 picks**
	- Result is: Some days appear multiple times. Some days don\u2019t appear at all. Total observations = still 250. Repeat this process many times (e.g., 10,000 bootstrap samples).
	- From 250 returns, bootstrapping shows the mean return is 8%, but with a wide spread (spread comes from 10k generated samples) ⟶ you see how unreliable that estimate is.
	- Instead of assuming normal returns, you reuse actual ugly days (crashes, spikes) exactly as they occurred. Even with small data, you can still quantify risk around estimates.
    
### MODULE 7.1: SAMPLING TECHNIQUES AND THE CENTRAL LIMIT THEOREM
1. Probability sampling: \u201cEveryone had a ticket in the lottery.\u201d Randomly selecting 500 firms from 10,000 gives each firm a 5% selection chance, making the sample\u2019s average profitability an unbiased estimate of the population mean. This is probability sampling.
2. Non-probability sampling: \u201cI picked whoever was easiest to reach.\u201d Studying only easy-to-access or familiar firms (glossy reporters, followed companies, local firms) skews results because the sample is biased and not representative of the population. One way to form an approximately random sample is **systematic sampling** selecting every nth member from a population.
3. **Stratified sampling (Probability Sampling Method)** divides a heterogeneous population into homogeneous groups based on key characteristics and randomly samples from each group in proportion to its size. Eg: Estimating national income by first grouping people into income brackets (low, middle, high) and then randomly sampling individuals from each bracket in proportion to their population share.
4. One of the most important examples is of a bond index is replicated by grouping bonds by maturity and coupon, then randomly selecting bonds from each group in proportion to the group\u2019s weight in the index.
5. **Cluster sampling (Probability Sampling Method)** means randomly picking a few groups that are assumed to look like the whole population and then collecting data from those groups instead of everyone. Eg: To estimate average student height in a city, randomly pick a few schools and measure all (or some) students in those schools instead of sampling from every school.
6. One-stage cluster sampling means randomly selecting a few clusters and including **every observation inside those clusters** in the sample. Eg: To estimate city electricity usage, randomly pick a few apartment buildings and use the electricity data of all households in those buildings.
7. Two-stage cluster sampling means randomly selecting a few clusters first (stage 1) and then randomly sampling individuals within each selected cluster (stage 2). To estimate city income, randomly pick a few neighborhoods and then randomly survey a sample of households within each selected neighborhood.
8. Two-stage cluster sampling can be expected to have greater sampling error than one-stage cluster sampling because you have done stuff randomly twice. But it costs less.
9. The non probability methods are Convenience Sampling and Judgemental Sampling. Convenience sampling refers to selecting sample data based on ease of access, using data that are readily available. Judgemental sampling refers to samples for which each observation is selected from a larger dataset by the researcher, based on one\u2019s experience and judgement.
10. Suppose a sample contains the past 30 monthly returns for McCreary, Inc. The mean return is 2%, and the sample standard deviation is 20%. Calculate and interpret the standard error of the sample mean. SE($\mu$) = $\sigma / \sqrt{n}$ = 0.2 / $\sqrt{30}$ = 0.036. **As n $\to$ $\infty$, SE($\mu$) $\to$ 0
11. **Jackknife Method for SE:** From 5 returns {2, 4, 6, 8, 10}, compute 5 means by dropping one observation at a time (7, 6.5, 6, 5.5, 5). The standard deviation of these leave-one-out means estimates the standard error of the mean. **Works when sample size is small**
12. **Bootstrap Method for SE:** From the same 5 returns {2, 4, 6, 8, 10}, repeatedly draw samples of size 5 **with replacement** (e.g., {2,2,6,8,10}, {4,6,6,8,10}, \u2026) and compute the mean each time.  After 10,000 such resamples, the **standard deviation of these means** is the bootstrap estimate of the standard error (and their percentiles give confidence intervals).

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

### MODULE 17.1: INTERNATIONAL TRADE
1. **Tariff**: tax on imports; raises domestic price, cuts imports, raises domestic output; producers gain, consumers lose; government gets revenue; foreigners lose. Example: Donald Trump put tariffs on Chinese steel; US steel prices rose, US mills benefited, US buyers paid more, Treasury collected tariff cash, Chinese exporters absorbed losses.    
2. **Quota**: hard cap on import quantity; raises domestic price and output; producers gain, consumers lose; no automatic government revenue; scarcity creates rents. Example: Trump-era steel quotas would limit tons entering the US; price jumps not from tax but from artificial shortage.    
3. **Quota with auctioned licenses**: government sells import licenses; outcome \u2248 tariff; same higher price and lower imports, but now government captures quota rents instead of tariff revenue. Example: if Trump had auctioned steel import permits, US government not the firms would pocket the scarcity value.  
4. Quota makes the good scarce in the domestic market, the price there rises above the world price; foreign exporters who hold the free import licenses can sell the limited quantity at this higher domestic price, pay no tax or fee to the government, and keep the entire price gap as extra profit \u2014 that gap is the **quota rent**.
5. In the case of a quota, if the domestic government collects the full value of the import licenses, the result is the same as for a tariff.
6. Under VER, the importing country pressures exporters to limit supply (think drug dealing by Pablo Escobar); scarcity pushes prices up; consumers lose; domestic producers gain; foreign exporters keep the price markup as profit; government gains nothing.
7. Because a VER raises domestic prices like a quota **but gives all the quota rents to foreign exporters**, while the importing country gets **no tariff revenue**, no license revenue, and still suffers consumer losses and efficiency distortions.
8. **Marshall\u2013Lerner condition**: a currency depreciation improves a country\u2019s trade balance **iff** the sum of the absolute price elasticities of demand for exports and imports is **greater than 1**. Why: depreciation makes exports cheaper to foreigners and imports costlier to locals; trade balance improves only if quantities respond strongly enough to offset the price effect.
9. **Stolper\u2013Samuelson theorem**: in a two-good, two-factor trade model, an increase in the relative price of a good raises the real return of the factor used intensively in producing that good and lowers the real return of the other factor. Why: higher output price raises demand for its intensive factor; factor prices adjust economy-wide, not just in that sector
10. In a Free Trade Area (FTA), member countries remove trade barriers among themselves but maintain independent trade policies toward non-members.  
11. A Customs Union extends an FTA by adopting a common external trade policy against non-members.
12. Under the WTO's 'Most Favored Nation' (MFN) principle, a country must apply the same tariff rates to all WTO members.  
13. Regional Trading Agreements (RTAs) like the EU or USMCA are permitted exceptions to the MFN principle.
 
### MODULE 18.1: THE FOREIGN EXCHANGE MARKET
1. When you buy a forward contract, you agree to BUY an underlying at a agreed price at a future date. If I buy a Euro / Rupee forward from you at 1 EUR = 100 INR, I am obliged to buy 1 EUR @ 100 INR, no matter whatever is the price. I have **hedged** my risk. 
2. ==Real P/B Exchange Rate = Nominal P/B � (CPI Base / CPI Price)== You multiply nominal by how pricier base is with respect to price currency.
3. At a base period, the CPIs of the United States and United Kingdom are both 100, and the exchange rate is $1.70/�. Three years later, the exchange rate is $1.60/�, and the CPI has risen to 110 in the United States and 112 in the United Kingdom. What is the real exchange rate at the end of the three-year period. Here Nominal P/B = $1.6/�, CPI Base = 112, CPI Price = 110. Real P/B = 1.6 � (112/110) = 1.632
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

### MODULE 9.1: TESTS FOR INDEPENDENCE



## CORPORATE ISSUERS

### MODULE 23.1: LIQUIDITY MEASURES AND MANAGEMENT


> [!abstract] MEMORISE THIS FOR EFFICIENCY
>  - **CCC = DIO + DSO - DPO**
>  - Suppliers offer payment terms in the form **a/b net c, which means a percentage discount of a if the invoice is paid within b days, otherwise full payment is due within c days.**


1. The cash conversion cycle (CCC) measures the time it takes for a company to convert its investments in inventory and other resources into cash inflows from sales. 

> [!TIP] HAMMER THIS INTO YOUR HEAD
> CCC = DIO + DSO - DPO

2. Lower CCC is better and can be artificially created
   -  **Delay paying suppliers** right before quarter-end ⟶ payables look high ⟶ CCC \u2193  
   -  **Sell receivables to a bank (factoring)** just before reporting ⟶ receivables drop ⟶ CCC \u2193
   -  **Ship inventory early to distributors** with return rights ⟶ inventory disappears on paper ⟶ CCC \u2193
   -  **Avoid writing down old inventory** ⟶ inventory looks lower than reality ⟶ CCC \u2193
   -  **Stop buying inventory** just before reporting ⟶ inventory temporarily low ⟶ CCC \u2193
2. We can think of accounts payable as an implicit source of credit from suppliers (as opposed to explicit sources such as bank loans). **Suppliers offer payment terms in the form a/b net c, which means a percentage discount of a if the invoice is paid within b days, otherwise full payment is due within c days.** Forgoing the discount for prompt payment amounts to borrowing money from the supplier for (c \u2013 b) days.

### MODULE 23.2 EXPENSE RECOGNITION

1. **Match costs with revenues:** recognize COGS **and estimated warranty costs** in the **period of sale**, not when paid in reality.
2. Remember US GAAP loves 'CFO'. Interest Expense go into operating always. IFRS gives you a choice. You can put Interest in 'CFF' or in 'CFO'.
3. IFRS is cool with splitting R&D. Research (incl. early software work) **expensed**; development (incl. saleable & internal software) **capitalized if criteria met**.
4. GAAP is strict, BOTH research and development is expensed. No capitalization at all.
5. GAAP hates R&D\u2014except software. Saleable software = **capitalize (like IFRS)**; internal software = **capitalize only after build starts**.
### MODULE 24.1: CAPITAL INVESTMENTS AND PROJECT MEASURES
###### Expected number of questions: 3
###### LOS: Describe types of capital investments. Describe the capital allocation process, calculate net present value (NPV), internal rate of return (IRR), and return on invested capital (ROIC), and contrast their use in capital allocation.

#CRITICAL_MODULE


> [!ABSTRACT]- MEMORISE THESE FOR EFFICIENCY
> - Return on Invested Capital (ROIC) = PAT / Capital
> - Capital Turnover =  Revenue / Capital
> - After-Tax Margin = PAT / REVENUE
> - For NPV on TI Calc. Enter **CF**s (using **\u2193**) then **NPV**. Enter I then \u2193 then **CPT**. 
> - IRR > Reqd Rate of Return ⟶ Accept Project
> - For IRR,  Calculate NPV then press **IRR** then **CPT**


1. Imagine an airline that has to replace aircraft engines as they age. This is a **going-concern project** because it is essential for airline survival. **The airline uses match funding approach**, that is, long-term debt or leases aligned with the engine\u2019s life. ==Match funding because: An asset generates benefits over time. Financing has to be repaid over time. If these timelines don\u2019t align, cash-flow risk appears.== 

> [!warning] Remember
> Maintenance activity that **reduces costs** will be a going concern project

1. If DGCA forces airlines to replace the old engines then that is a **Regulatory/compliance project**. If Indigo invests to buy Airbus A320s for international routes, then that is a **Expansion Project.**
2. The capital allocation process is identifying and evaluating capital projects (i.e., projects where the cash flows to the firm will be received over a period longer than a year). 
3. Capital Allocation Process looks like: Ideation ⟶ Forecast CF / Analyze ⟶ Budgeting ⟶ Audit 
4. A project has a conventional cash flow pattern if the sign on the cash flows changes only once, else it is unconventional.
5. NPV is the discounted PV of all future cashflows, discounted by Reqd. Rate of Return. IRR is the rate that makes NPV = 0. Accept if NPV > 0 and accept if IRR > Reqd. rate of Return.
6. NPV and IRR are forward looking approaches because you are talking about cashflows that **will happen in future.**

> [!warning] Remember
> It is important to understand, how cashflows are **reinvested** in each approach. **Under IRR method, they are reinvested at IRR and under NPV they are reinvested at Reqd. rate of return.**  

7. IRR is the discount rate that makes NPV = 0. If cash flows **change sign more than once** (e.g., \u2212 + \u2212 or \u2212 + \u2212 +), the NPV equation becomes a higher-degree polynomial, which can have **multiple real roots**. Each root is an IRR. Cash flows: \u2212100 (today), +230 (year 1), \u2212132 (year 2)  NPV(r) = \u2212100 + 230/(1+r) \u2212 132/(1+r)� = 0  This quadratic has **two solutions** ⟶ **two IRRs**.

> [!TIP] HAMMER THIS INTO YOUR HEAD
> Practice this on TI Calculator. You should be very very comfortable with this
> Suppose your cashflow stream is -1000, 100 ... (10 times). Required rate of return is 10%. Calculate NPV and IRR. 
> **CF** \u21e2 **CLR WORK** \u21e2 C0=-1000 \u21e2 **ENTER** **\u2193** C01=100 \u21e2 **ENTER** \u21e2 F01=10 \u21e2 **ENTER** \u21e2 **NPV** \u21e2 I=10 \u21e2 **CPT**
> This gives NPV = -385.543
> Now do **IRR** \u21e2 **CPT**
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

1. In general, the more **stable**, **non-cyclical**, **predictable**, and **recurring** are a company\u2019s revenues and cash flows, the higher proportion of debt it can have in its capital structure. Eg: Walmart (regular cashflows and non-cyclicity), Adani (Huge amount of tangible assets for collateral and non-cyclicity).
2. Companies with low fixed operating costs can support larger debt. 
3. For raising additional debt: Interest Coverage Ratio = EBIT / Interest Expense ⟶ Higher the better. Debt to Equity Ratio ⟶ Lower the better. Debt to EBIT  ⟶ Lower the better.  
4. Capital structure is also dependent on the growth stage, a company is in. During startup stage, debt is very expensive. Company usually raises money through equity or convertible debt. During growth phase the risk is relatively lower and collateralized debt can be raised as capital. During mature stage, company can afford higher debt financing including unsecured debt. ==Remember: Startup companies can raise **Convertible Debt**, Growth ones can raise **Secured Debt** and Mature Ones can afford **Unsecured Debt**==
5. **Top Down Factors** such as inflation, the real GDP growth rate, monetary policy, and exchange rates impact capital structure. High Inflation scenarios demand greater yeilds.

### MODULE 25.2: CAPITAL STRUCTURE THEORIES
###### Expected number of questions: 2
###### LOS: Explain the Modigliani\u2013Miller propositions regarding capital structure.

1. Asymmetric information exists because managers have superior knowledge about future prospects vs shareholders/creditors.    
2. Higher when business is complex or financial reporting is opaque ⟶ investors face more uncertainty. Investors price this uncertainty as higher required returns on both debt and equity.    
3. Investors infer management\u2019s private information from financing choices (**signaling**). Issuing debt signals confidence: fixed interest obligations imply expected stable cash flows. Issuing equity signals pessimism: markets infer management thinks stock is overvalued. **Therefore, equity financing is penalized more heavily than debt under asymmetric information.**    
4. Agency costs of equity arise from conflicts between managers and shareholders. Managers without ownership stake don\u2019t fully bear costs of overpaying themselves or mismanaging risk (too safe or too reckless). Shareholders anticipate this conflict and impose controls (monitoring, incentives, governance). Even after controls, some conflict remains ⟶ net agency cost of equity.
5. Agency costs of equity are related to conflicts of interest between managers and owners. Managers who do not have a stake in the company do not bear the costs associated with excessive compensation or taking on too much (or too little) risk. **Because shareholders are aware of this conflict, they take steps to reduce these costs. The result is called the net agency cost of equity.**
6. **Free cash flow hypothesis: excess cash invites wasteful spending or self-serving projects by managers.**
7. **Use of Debt forces managers to be disciplined**, because commits cash to interest and principal payments, reducing free cash flow available for misuse.
8. Pecking order theory is built on asymmetric information between managers and investors. Financing choices act as signals about management\u2019s private view of firm value. - Internal funds are preferred: no external scrutiny, no signal.

## FSA
### MODULE 29.1: INTANGIBLE ASSETS

1. IFRS rule: Under IFRS (set by [International Accounting Standards Board](chatgpt://generic-entity?number=0)), a purchased identifiable intangible (patent, license, trademark) is first recorded at cost and then you can choose cost model or revaluation model, but revaluation is allowed only if there is an active market with observable prices.
2. Cost model (IFRS and US GAAP): Asset stays at historical cost minus accumulated amortization and impairment; example: a firm buys a patent for INR 100, amortized straight-line over 10 years ⟶ carrying value after 3 years = INR 100 \u2212 INR 30 = INR 70, regardless of what similar patents trade at today.
3. Revaluation model (IFRS only): Asset is periodically marked to fair value using market prices, with increases going to OCI (revaluation surplus) and decreases to P&L if they exceed any existing surplus; example: taxi medallion bought for INR 100, amortized to INR 80, active market price now INR 120 ⟶ balance sheet value reset to INR 120 and INR 40 goes to equity via OCI, not income.

> [!warning] REMEMBER
> Under US GAAP, the intangible asset is always recorded at cost value. Re-evaluation is not allowed whatsoeverm> R&D is always expensed under US GAAP.

4. Under IFRS firm must explicitly identify research stage and expense it.  Then capitalise the development stage. Under US GAAP, firm must always expense both research and development, no matter what.
5. The intangible assets with finite life such as patents must be amortised. The lifespan of such assets must be reviewed annually. 
6. Any admin overhead, training costs etc must be expensed under both IFRS and US GAAP.
7. Any internally generated goodwill must be expensed. Goodwill is only created on balance sheet during purchase acquisition.w

> [!WARNING] REMEMBER
> Accounting goodwill should not be confused with economic goodwill. Economic goodwill derives from the future earning potential of the firm whereas accounting video is the result of the past acquisitions.
8. To improve comparability analysts should eliminate goodwill from the balance sheet while calculating ratios. 
9. Financial instruments are contracts that give rise to both a financial asset of one entity and a  financial liability or equity instrument of another entity.
10. Sometimes firms manipulate net income upward by allocating a larger proportion of acquisition price to goodwill. Lower value of tangible assets result in lower depreciation and amortisation expense and hence higher income.
11. Under US GAAP, held to maturity securities such as debentures are measured at amortised cost. Amortized cost is equal to the original issue price minus any principal payments, plus any amortized discount or minus any amortized premium, minus any impairment losses. **Subsequent changes in market value are ignored.** for example if credit rating of the borrower declines or interest rate shoots up, you do not account net for these changes. 
12. Tradable securities such as equity and derivatives which are held with an intent to sell are measured at fair value. This is also known as mark to market accounting. All gains and losses go into OCI. Short position on stocks ids recorded on liability side at fair value. 


> [!question] QUESTION
> Triple D Corporation, a U.S. GAAP reporting  firm, purchased a 6% bond, at par, for $1 million at the beginning of the year. Interest rates have recently increased, and the market value of the bond declined $20,000. Determine the bond\u2019s effect on Triple D\u2019s financial statements under each classification of securities.
> **US GAAP**: It matters if this bond is held to maturity or is held with an intention to sell. 
>If it is held to maturity then the change in bond price due to interest rate changes are ignored and bond is recorded at its amortised cost of 1 million. The interest of $6k goes to OCI.
>If it is held as a tradable security then we record it at its fair mark-to-market price. 

13. A vertical common-size balance sheet expresses each item of the balance sheet as a **percentage of total assets**.


> [!tip] HAMMER THIS INTO YOUR HEAD
> - A common size balance sheet expresses each item as percentage of total assets, income statement as percentage of revenue.
### MODULE 28.4 BASIC EARNINGS PER SHARE
1. **What is Warrant:** A warrant is essentially an equity call option issued by the company; a warrant holder has the right but not the obligation to purchase newly issued shares at the exercise price. 
2. **What is Basic EPS:** (Actual earnings - Preferred Dividend) / actual weighted ordinary shares.

> [!DANGER] DO NOT MAKE THIS MISTAKE
> Preferred Dividend is subtracted while calculating EPS

1. **What are Actual weighted shares:** Weighted average number of shares outstanding during the period. Shares outstanding adjusted for how long they existed during the year. For example:

|                                                        |           |
| ------------------------------------------------------ | --------- |
| Shares outstanding on 1 January 2018                   | 1,000,000 |
| Shares issued on 1 April 2018                          | 200,000   |
| Shares repurchased (treasury shares) on 1 October 2018 | (100,000) |
| Shares outstanding on 31 December 2018                 | 1,100,000 |
The actual weighted shares are calculated as:

|                                                                                              |           |
| -------------------------------------------------------------------------------------------- | --------- |
| 1,000,000 � (3 months/12 months) =                                                           | 250,000   |
| 1,200,000 � (6 months/12 months) =                                                           | 600,000   |
| 1,100,000 � (3 months/12 months) =                                                           | 275,000   |
| Weighted average number of shares outstanding = (3/12) * 1 + (6/12) * 1.2 + (3/12) * 1.1<br> | 1,125,000 |

4. **What is Preferred Dividend?** This is the dividend paid to the preferred shareholders. Preferred stock doesn't come under common stock and hence EPS removes it.
5. **What is Diluted EPS:** \u201cWhat EPS would be\u201d if all dilutive instruments became common stock. This would be (Actual Earnings - Preferred Dividends) / (Ordinary Shares + New common stock that would have been issued at conversion))
6. **What is Dilution:** The instruments convertible into ordinary equity can become shares ⟶ share count rises ⟶ EPS goes down. That\u2019s dilution.
7. **What is stock split:** Suppose a company with a market capitalization of $100 has 100 shares (each share is priced $1). The company declares 2:1 stock split, which means each share would be split into 2 shares. This means the number of shares will be now: (100 * (2/1)) = 200. Now each share would be priced $0.5.
8. Complex Capital Structure: 
Under IFRS, the type of equity for which EPS is presented is referred to as ordinary. Ordinary shares are those equity shares that are subordinate to all other types of equity. 

When a company has issued any financial instruments that are potentially convertible into common stock, it is said to have a complex capital structure. 
### MODULE 28.5 RATIOS AND COMMON SIZE STATEMENTS
1. Common-size income statement = divide every line item by **Revenue** and express as %.

> [!tip] HAMMMER THIS INTO YOUR HEAD
> Margin is always calculated as **Revenue** as denominator. Turnover is always calculated as **Revenue** as numerator. **Revenue is usually the numerator**, **except inventory and A/C payable turnover**, which uses COGS for matching.

> [!danger] DO NOT MAKE THIS MISTAKE
> Inventory and A/C Payables Turnover use COGS as numerator

## MODULE 32.1: ANALYSIS OF INVENTORIES


### MODULE 34.1: LEASES
1. An alternative way to look at a lease is: **taking a loan and buying the asset.**
2. To be called a lease, a lessee needs to have following characteristics:
	- Asset must be **Identified** a.k.a it should exist.
	- Lessee should have exclusive control of asset and must derive all the economic benefits from the asset. 
3. Under IFRS and U.S. GAAP, in a **financing lease** ownership and risks should be transferred to lessee. You break it and you pay for it.   If either the benefits or the risks of ownership are not substantially transferred, it is an operating lease.

> [!warning] Remember
> Financing Lease:
> 	- **Present Value of payments >= Asset Fair Value**
> 	- You have an option to buy the asset and get rid of the lease.
4. Accounting treatment would be:
	- On liabilities side, you would create a lease liability that would be amortized with time.
	- On asset side, you would create ROU asset that would depreciate with time.


> [!question] QUESTION
> The Affordable Company (Affordable) leases a machine for its own use for four years with annual payments of $10,000. At the end of the lease, which is also the end of the machine\u2019s useful life, Affordable will return the machine to the lessor. The interest rate implicit in the lease is 5%. Assuming that the ROU asset is amortized on a straight-line basis over the term of the lease, calculate the impact of the lease on Affordable\u2019s financial statements for each of the four years.
> 
> Fair value of Asset: PMT = -10000, I/Y = 5, FV = 0, CPT ⟶ PV = 35549
> 
> Asset Amortisation per year = 35549 / 4 = 8887.25
> 


Balance Sheet 
| Year | Liability | Asset |
| ---- | --------- | ----- |
| 1    | 35560     | 35560 |
| 2    | 25560     |       |
|      |           |       |
| 
|           |       |




> 
> Liability Side:
> 	| Year | 


### MODULE 34.2: DEFERRED COMPENSATION AND DISCLOSURES


> [!abstract] MEMORISE THIS FOR EFFICIENCY
> 


1. A pension is delayed salary. **Defined Contribution (DC)** ⟶ firm promises _how much it puts in_, employee bears **investment risk**. For example NPS and EPF in India and PPK in Poland. My employer puts in money, it gets invested into the market. If market collapses, everything turns to ashes. 
2. **Defined Benefit (DB)** ⟶ firm promises _how much you\u2019ll get_, employer bears investment + longevity risk. I am promised a pension of PLN 10k per month, no matter if market collapses or booms. For example, ZUS contributions or Military pensions. **Employer bears market risk and employee bears longevity risk.** If I die, the pension vanishes. 
3. Defined benefit is complicated. ==It is recorded as a **long term liability** on the balance sheet and on part of employers, it involves forecasting market cycles, interest rates, expected lifespan etc.==
4. Defined Benefit (DB) plans create a **net position** on the balance sheet = what the firm owes \u2212 what it has set aside.  **Assets > obligation ⟶ asset. Assets < obligation ⟶ liability**.  Annual changes flow partly through P&L, partly through OCI.
5. Funded status = **Fair value of plan assets \u2212 Pension obligation** **Overfunded** means I have saved more money (Plan Assets) that what my obligation demands (Pension to be paid), which creates a net asset position. **Underfunded** creates a net liability position.
6. IFRS = Pay for work + interest in P&L, dump all shocks into OCI GAAP = smooth P&L via amortization.


> [!question] QUESTION
> **Start**: Obligation = 1,000, Assets = 900, Net liability = 100, Discount rate = 10%. 
> **Year events**, Service cost = 50, Past service cost = 20, Actual asset return = 40, Expected return = 90, Actuarial Loss = 60. Identify what goes into OCI and what goes into P&L. 
> 
> #### IFRS
> **Any admin,  service cost (past or present) goes into P&L.** For example: Service + Past Service = 70
> **Any interest goes into P&L:** 10% of 1000 = 100
> **Any return or market shock goes to OCI:** Asset return surprise - Actuarial Loss = (40-90) - 60 = -110
> 
> #### US GAAP
> **PnL:** 
> 	- Current Service Cost + Interest = - 50 - 100 = -150
> 	- Expected Return on Assets = 90
> **OCI:**
> 	- Past Service Cost = -20
> 	- Actuarial Loss = -60

7. One of the differences from IFRS pension accounting is that past service costs are recognized in other comprehensive income, rather than in the income statement as part of employee service costs. These costs are amortized over the employees\u2019 service period. **Actuarial gains and losses are typically treated the same way, but U.S. GAAP allows firms to recognize them in the period incurred.**

> [!tip] HAMMER THIS INTO YOUR HEAD
> 
> Past service cost for Defined Contribution plans goes into OCI under US GAAP and PnL under IFRS.
8. ==Pension cost is **not shown as a separate line item** for manufacturing firms. It is **embedded** in expenses based on employee role.== Factory workers ⟶ pension cost goes into **inventory ⟶ COGS**. Office/admin staff ⟶ pension cost goes into **SG&A / salaries**. Income statement hides pension cost inside operating costs. Therefore, analysts **must read the notes** to see total pension expense and assumptions.
9. Stock options, on the other hand, may cause managers to take on too much risk, because options have asymmetrical payoffs. An option has value if the stock price is above the exercise price, but its value cannot fall below zero if the stock price is below the exercise price.
10. **Grant-date fair value rule (IFRS = GAAP)**: stock-based compensation is measured at **fair value on grant date** and expensed **over the vesting (service) period**; immediate vesting ⟶ full expense on grant date, delayed vesting ⟶ straight-line over service period.
11. These are shares awarded outright, with restrictions (Restricted Stock Units (RSU)) , or contingent on performance (Performance Shares).    
12. **Stock grants vs performance shares**:    
    - **Stock grants / RSUs** ⟶ FV = **share price at grant**, expense based only on service/vesting.        
    - **Performance shares** ⟶ vesting tied to **non-market metrics** (ROE, EPS, margins); fair value still set at grant but **managerial incentives can distort accounting choices**.        
13. Compensation expense exists **before shares are received**; if vesting conditions aren\u2019t met, expense is reversed.
14. **Stock grants (RSUs)**: the share price on the grant date is taken as the cost; this cost is charged to the income statement over the vesting period (or all at once if vesting is immediate); the same amount is added to equity; example: grant value 100 with 2-year vesting ⟶ expense 50 each year, equity increases by 50 each year, and at vesting it is moved into share capital and APIC.    
15. **Stock grants \u2013 why equity doesn\u2019t change**: the expense reduces retained earnings, but equity is increased by the same amount through APIC, so total equity stays the same; example: expense 50 ⟶ retained earnings \u221250, APIC +50.
16. **Stock options**: the option\u2019s value is calculated using an option pricing model at grant and expensed evenly over the vesting period; **until exercise, only APIC increases and no shares are issued;** example: option value 80 over 4 years ⟶ expense 20 per year, APIC +20 per year.    
17. **Stock options \u2013 exercise stage**: when employees exercise, the company receives cash equal to the strike price and issues shares; equity increases by the cash received, split between share capital (par) and APIC, and any accumulated reserve is moved into APIC; example: strike 50 ⟶ cash +50, share capital +1, APIC +49 plus the reserve.

> [!tip] HAMMER THIS INTO YOUR HEAD
> - Suppose UBS gave me a stock as salary. The price is 100 CHF. In this case retained earnings will go down by 100 (stock got charged on PnL) and APIC will increase by 100. **No new shares are issued**. If I don't complete 3 years, they will reverse the charge on PnL and APIC will go down.
> - Suppose UBS gave me a deferred stock (100 CHF) as salary that I can vest at the end of 3 years of service. Each year UBS will show a compensation expense of 33.33 CHF **always calculated on the price @ grant date** and APIC rises by 33.33 CHF every year.
> - Suppose UBS gave me a call option to exercise at the end of 3 years of service at strike price of 100 CFH. The Black Scholes value is 10 CHF, which is shown in income statement. If I exercise it, then UBS gets the strike price which moves into APIC and issues me shares. **UBS does not issue new shares**
18. Phantom stock a.k.a fake stock is a **cash bonus plan** that mimics share price performance, where employees receive **cash linked to the company\u2019s stock value without receiving actual shares or ownership**.
### MODULE 35.1: DIFFERENCES BETWEEN ACCOUNTING PROFIT AND TAXABLE INCOME
1. Suppose you have Operating Profit (EBIT) of USD 100. And

### MODULE 36.1: FINANCIAL REPORTING QUALITY 


> [!abstract] MEMORISE THIS FOR EFFICIENCY
> - GAAP allows managerial discretion in Financial Reporting Quality
> - Relevance and faithful representation


1. Financial reporting quality is about how decision-useful the financial statements are, not just whether they comply with GAAP, because ==GAAP allows managerial discretion== in methods, estimates, and classifications that can legally distort economic reality.
2. **Decision-useful reporting rests on two pillars: relevance and faithful representation;** relevance means the information can actually change user decisions and must be material, while faithful representation requires completeness, neutrality, and freedom from error.
3. Compliance with accounting rules is necessary but not sufficient; high-quality reporting reflects underlying economics rather than exploiting accounting flexibility to manage appearances.
4. Sustainable earnings arise from core business improvements like efficiency gains or market share growth, whereas earnings driven by one-off factors such as asset sales or exchange-rate movements are low quality.
5. **Valuation implication: one dollar of high-quality, sustainable earnings is worth more than one dollar of low-quality earnings because it has a higher probability of persisting and therefore contributes more to the present value of future cash flows.** Temporary earnings shocks, even if reported accurately, have limited valuation impact because they do not materially alter expectations of long-term earnings.
6. Financial reporting quality and earnings quality together form a spectrum: at the top are GAAP-compliant, decision-useful reports with sustainable earnings reflecting true economic returns on capital; at the bottom are reports that are non-compliant and effectively fictitious, where earnings quality cannot even be meaningfully assessed.
7. Moving down the spectrum, deterioration happens in layers: 
	- First earnings become unsustainable despite compliant reporting, Example: In 1990, IBM reported record profits of $6 billion while strictly following GAAP, yet these earnings were unsustainable because they were driven by a dying mainframe business and aggressive cost-cutting that masked a total failure to adapt to the personal computing revolution.\u200b
	- then reporting choices and estimates become biased, then earnings are actively managed or smoothed, Example: General Electric (GE) used "cookie jar" reserves for decades, over-estimating future liabilities in good years to create a pool of funds that could be released during lean quarters to meet analyst profit targets with uncanny consistency.\u200b
	- then GAAP is violated while still reflecting real activity Example: Byju's aggressively recognized the full value of multi-year subscriptions immediately upon sale, a practice auditors later forced them to reverse by spreading revenue over the actual contract duration, which slashed their reported income by 40%.\u200b
	- Finally numbers become outright fraudulent. Example: Satyam Founder Ramalinga Raju fabricated over $1 billion in non-existent cash reserves to inflate the company's stock price, eventually admitting that 94% of the stated cash on the balance sheet was fictitious.\u200b
8. Conservative vs aggressive accounting describes bias within GAAP: conservative choices depress current earnings (General Electric) and balance-sheet strength but tend to shift earnings into the future, while aggressive choices inflate current earnings and financial position at the cost of lower future earnings (Byjus).
9. Earnings smoothing is an intertemporal reallocation problem: management uses estimates (e.g., accruals, reserves, depreciation lives) to pull earnings forward or push them back to reduce volatility, even though total lifetime earnings are unchanged.
10. Valuation implication: analysts must adjust not only for reported earnings levels but also for where the firm sits on the reporting-quality spectrum and whether earnings reflect sustainable economics or accounting timing games.
11. **Motivation** refers to the economic or personal incentives to misreport, such as meeting analyst forecasts, avoiding covenant violations, or boosting bonuses and stock-based compensation.
12. **Opportunity** refers to the ability to misreport without being detected, which arises from weak internal controls, poor oversight, complex transactions, or ineffective audits.
13. **Rationalization** refers to the mental justification managers use to legitimize misconduct, such as believing the misstatement is temporary, harmless, or done in the firm


### MODULE 36.2: ACCOUNTING CHOICES AND ESTIMATES

1. **REVENUE:**
	1. **Free-on-board (FOB) shipping point vs FOB destination** changes when control passes and revenue is booked (at shipment vs at delivery); example: an automaker using FOB shipping point can record quarter-end sales as soon as cars leave the factory, even if dealers receive them next period.
	2. **Channel stuffing** records sales by pushing excess goods to intermediaries before real end-customer demand exists; example: Bristol-Myers Squibb shipped unusually large drug volumes to wholesalers to hit revenue targets, later reversing sales when inventories did not clear.
	3. **Bill-and-hold arrangements** book revenue before goods/services are delivered or performance is complete; example: Byju\u2019s recognized the full value of multi-year course subscriptions upfront rather than over the teaching period, so when auditors forced deferral over the contract life, reported income dropped sharply, revealing timing-driven earnings.
2. **INVENTORY:**
	1. **FIFO vs weighted-average affects earnings mechanically through COGS timing**: in rising price environments FIFO reports lower COGS and higher profits because older, cheaper inventory flows to the income statement first, a tailwind seen in commodity retailers and refiners during inflationary cycles (e.g., post-2021 energy and metals price spikes).	
	2. **Balance sheet relevance vs income statement realism trade-off**: Under FIFO, ending inventory consists of the most recent purchases, so its book value reflects near-current replacement cost, making the balance sheet closer to what the firm would actually pay to restock today. FIFO produces inventory values closer to current replacement cost, making the balance sheet more relevant, while weighted-average produces COGS closer to current costs, making gross margin more economically meaningful and less inflated by price-level gains.	
	3. **Earnings quality implication**: ==FIFO profits embed hidden holding gains (or losses) from price changes rather than operating performance==, so analysts prefer weighted-average margins for performance analysis and FIFO inventory for asset valuation, especially during volatile input-cost regimes.

3. **OTHER WAYS TO GAME THE SYSTEM:**
	 1. **Stretching payables** inflates operating cash flow by delaying supplier payments across reporting periods, improving CFO today but reversing it later with no impact on earnings; example: retailers and manufacturers under liquidity stress have repeatedly been flagged in earnings calls for rising days payable outstanding used to \u201csupport cash flow.\u201d
	2. **Capitalizing interest expense** shifts cash outflows from CFO to CFI and smooths earnings by spreading costs via depreciation instead of expensing immediately; example: real estate developers and infrastructure firms capitalize borrowing costs during construction to boost reported operating cash flow.
	3. **Cash flow classification flexibility (IFRS)** allows interest and dividends to be classified across CFO, CFI, or CFF, letting firms cosmetically raise CFO without changing total cash; example: European firms often classify interest paid as financing cash flow to report stronger operating cash generation than US GAAP peers.
	4. **Show straight-line depreciation** to inflate income.
	5. **Delay impairment of goodwill** as it is subjective.
	6. **Do not create VA to reduce DTA**

> [!TIP] HAMMER THIS INTO YOUR HEAD
> 1. Under **IFRS**, interest paid can be classified as CFO or CFF, interest received as CFO or CFI, dividends paid as CFO or CFF, and dividends received as CFO or CFI, giving management flexibility to boost reported operating cash flow.
> 2. Under **US GAAP**, interest paid and interest received must be classified as CFO, dividends received as CFO, and dividends paid as CFF, leaving no discretion to reclassify these items to manage CFO.


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



## EQUITY

### MARKET ORGANISATION 

1. **Financial Assets vs. Real Assets**: Financial assets are paper or digital claims on cash flows (stocks, bonds, derivatives), while real assets are tangible physical things that produce value directly (factories, land, gold).
   *Example: A share of Apple stock is a financial asset (a claim on Apple\u2019s profits); the factory where Apple assembles iPhones is a real asset.*
2. **Debt Securities**: These are simply IOUs where the borrower promises to repay the principal plus interest. They are legally binding contracts.
   *Example: You buy a \$1,000 corporate bond that pays 5% interest. The company legally owes you \$50 a year plus your \$1,000 back at the end.*
3. **Equity Securities**: These represent ownership in a company. Common stock gives you a residual claim (you get what's left after debts are paid) and voting rights. Preferred stock is a hybrid: it pays fixed dividends like a bond but usually has no voting rights.
   *Example: If a company goes bankrupt, bondholders get paid first. Common stockholders get whatever scraps are left (usually zero). Preferred stockholders sit in the middle.*
4. **Pooled Investment Vehicles**: These structures pool money from many investors to buy a portfolio of assets. Mutual funds trade once a day at a set price; ETFs trade all day like stocks. Asset-backed securities (ABS) are pools of loans (like car loans) packaged into a tradeable bond.
   *Example: Instead of buying 50 separate stocks yourself, you buy one share of an S&P 500 ETF (like SPY), which instantly gives you exposure to all 500 companies.*
5. **Derivatives**: These are contracts whose value is "derived" from an underlying asset (like a stock or oil price). They include forwards, futures, options, and swaps.
   *Example: An airline buys an oil futures contract. The value of that contract goes up or down based entirely on the price of jet fuel, not because the contract itself produces anything.*
6. **Forward vs. Futures Contracts**: Both are agreements to buy/sell something later at a set price. Forwards are private, custom deals between two parties (risky if one side defaults). Futures are standardized contracts traded on an exchange (safer because the exchange guarantees the trade).
   *Example: A farmer agrees privately with a cereal company to sell wheat at \$5/bushel in June (Forward). Or, the farmer sells a standardized "5,000 bushels of wheat" contract on the Chicago Mercantile Exchange (Future).*
7. **Options**: A "call" option gives you the right to buy an asset at a set price; a "put" option gives you the right to sell it. You pay a premium for this right, but you aren't forced to use it.
   *Example: You pay \$5 for a call option to buy Apple at \$150. If Apple goes to \$200, you use the option and make a profit. If Apple stays at \$140, you let the option expire and only lose the \$5 premium.*
8. **Swaps**: Two parties agree to exchange cash flows. An interest rate swap typically involves trading a fixed interest payment for a floating (variable) one. *Example: Company A has a loan with a variable interest rate that scares them. They swap payments with Company B, who agrees to pay the variable rate in exchange for receiving a steady 4% fixed rate from Company A.*
9. **Brokers vs. Dealers**: Brokers are agents who find a buyer for your sell order (like a real estate agent) and charge a commission. Dealers trade from their own inventory (like a car dealership), buying low and selling high to make a profit.  *Example: A broker connects you to someone selling 100 shares of Tesla. A dealer actually owns the 100 shares and sells them directly to you from their own stash.*
10. **Markets**: "Primary" markets are where new securities are created and sold (IPOs). "Secondary" markets are where investors trade existing securities with each other (the stock market). "Money markets" are for short-term debt (under 1 year); "Capital markets" are for long-term equity and debt. *Example: When Facebook went public, it sold shares in the primary market to big banks. Now, when you buy Facebook stock on Robinhood, you are trading in the secondary market with another investor, not Facebook itself.*
11. **Best-efforts offering** means the investment bank only tries to sell the securities and does not guarantee the amount raised; unsold shares are returned to the issuer.
12. **Underwritten offering** means the investment bank guarantees the funds by buying the entire issue from the issuer and then reselling it to investors, taking on the risk of unsold shares.
13. Money markets exclusively trade debt instruments with maturities of one year or less.
14. Capital markets trade instruments where the investment duration is longer than one year, including both equities and fixed-income securities.
15. When an issuer sells additional units of a previously issued security to the public, this transaction is referred to as a: Seasoned Offering.

16. Bid price is the highest price a buyer is willing to pay, and ask price is the lowest price a seller is willing to accept. You sell at bid price and buy at ask price
17. In order-driven markets, no central dealer exists; instead, traders submit limit orders that rest in the order book, creating a decentralized liquidity pool. The reason explains the functional equivalence: a standing limit buy order is an offer to buy at a specified price, just like a dealer bid; a standing limit sell order is an offer to sell, just like a dealer ask. Both are consumed by marketable orders (market or aggressive limit orders). The key distinction is that in order-driven markets, liquidity provision is distributed across many participants\u2014some may be market-makers, but many are public traders with no special status.
18. Cumulative preferred shares require the issuer to pay any omitted dividends to preferred shareholders before paying dividends to common shareholders.
19. **Good-till-canceled (GTC) order** stays active until it is filled or the investor cancels it; example: you place a buy order at $90 for a stock trading at $100 and it remains open for weeks until the price hits $90 or you cancel it.
20. **Hidden or iceberg order** shows only a small part of a large order to the market to avoid moving prices; example: an institution wants to buy 100,000 shares but displays only 5,000 at a time, with new pieces appearing as each is filled.
21. Stop orders are conditional: a stop-sell becomes valid after the market trades at or below the stop price; a stop-buy becomes valid at or above the stop price.
22. This feedback loop creates momentum and often leads to execution away from the stop price, especially in fast-moving or illiquid markets. The key is causality: stop orders mechanically convert price moves into order flow in the same direction, reinforcing trends and degrading execution quality for the stop-order user.
23. **Execution instruction** specifies *how* an order should be executed in the market, controlling price\u2013speed trade-offs; examples include market orders (immediate execution at best available price) and limit orders (execution only at a specified price or better).
24. The process where the investment bank lines up subscribers who will buy the security and compiles a 'book' of orders is specifically called **book building**
25. Initial offering prices in the secondary market often rise immediately following an IPO, but this effect is less pronounced in a seasoned offering primarily because: the conflict of interest for underwriters is less important in a seasoned offering, as secondary market trading helps identify the proper price.
26. In a shelf registration, a corporation sells shares directly into the secondary market over time rather than in a single large transaction.
27. The underwriting fee paid by the issuer in an underwritten public offering is the **spread**, which is the difference between the price the underwriters pay the issuer for the shares and the price at which they sell those shares to the public.
28. ==The underwriting fee is classified as a **reduction of equity**, not an expense; it is netted against additional paid-in capital (or share premium) because it is a direct cost of issuing shares.==
29. The investment bank has dual roles. As **agents for the issuer**, they should seek a high price to raise the most money. However, as **underwriters**, they have strong incentives to choose a low price. A low price allows them to allocate valuable shares to benefit their clients. A high price exposes them to the direct cost of having to buy overvalued, undersubscribed shares and potentially providing price support in the secondary market. This conflict tends to lower initial offering prices.
30. **Validity instruction** specifies *how long* an order remains active before it expires if not executed; examples include day orders (expire at market close) and good-till-canceled orders (remain until filled or canceled).
31. **Clearing instruction** specifies *how and where* the trade will be settled after execution, including settlement method, account, or clearing system, ensuring proper delivery of securities and cash.
32. A **rights offering** lets existing shareholders buy new shares in proportion to what they already own, usually at a discount; these rights can be traded for cash, and once they separate, the share price falls to the theoretical ex-rights price (TERP) to reflect the new shares being issued.
33. Immediate-or-Cancel (IOC) allows for partial execution; the unfilled portion is cancelled immediately.
34. All-or-Nothing (AON) requires full execution but does not mandate immediacy; the order can wait on the book until the full size is available.
35. **Fill-or-Kill (FOK) combines two constraints: the order must be filled in its **Entirety** (Fill-or-Kill part) and **Immediately** (Implied by Kill).
36. If you use your rights, your ownership stays the same; if you don\u2019t, your stake gets diluted, but you can sell the rights for cash so you are not worse off in value terms. Market signal: rights offerings are often viewed as weaker than public offerings because they are commonly used when firms want cheap capital quickly or have limited access to external equity markets.
37. IPO includes - Newly issued shares sold by the company, and potentially shares sold by the company\u2019s founders and early investors.
38. **Initial margin** is the money you must put in at the start to open a leveraged position; example: if a stock costs $100 and initial margin is 40%, you pay $40 and borrow $60.
39. **Maintenance margin** is the minimum equity you must keep after the trade is open; example: if maintenance margin is 25%, your equity must always be at least $25 on a $100 stock, or you get a margin call.
40. **Variation margin** is the daily cash adjustment based on price changes, common in futures; example: if your futures position loses $5 today, you must pay $5 today to restore the margin balance.



### SECURITY MARKET INDEXES
1. **Price return vs total return**: A price return index reflects only changes in constituent prices, while a total return index assumes all dividends and interest are reinvested. The headline **S&P 500** is a price return index, while **Germany\u2019s DAX** is quoted as a total return index, which is why na�ve comparisons are misleading. ==At inception PRI = TRI.==

2. **Price return index level**
$$  V_{PRI}=\frac{\sum_{i=1}^{N} n_i P_i}{D}$$
  The **divisor (D)** is **defined at inception** to scale the index to a base value. Its **numerical value is later adjusted only to maintain continuity** when mechanical events occur (stock splits, spin-offs, constituent changes), so the index does not show artificial gains or losses. Real-world hook: in the **Dow Jones Industrial Average**, Apple\u2019s stock split changed its price but not its economic value; the adjusted divisor prevented the Dow from falsely jumping.
3. **Price return (security or index)**: Measures only price change.  $$PR_i=\frac{P_{i1}-P_{i0}}{P_{i0}}$$, and at the index level $PR_I=\sum w_i PR_i$. Dividends/interest are ignored.
    
4. **Total return = what investors actually earn**: Adds income to price change.    $$TR_I=\frac{V_{PRI1}-V_{PRI0}+Inc_I}{V_{PRI0}}$$Over time, total return always exceeds price return when dividends exist.

### MODULE 41.1: MARKET EFFICIENCY
1. In an efficient market, prices already reflect all available information, so they\u2019re fair estimates of value; the return you earn is just pay for risk, not for being clever \u2014 in short, you can\u2019t consistently beat the market.
2. When markets are efficient, passive investing makes sense because active trading gets eaten up by fees and costs; only when prices are genuinely wrong does active investing have a chance to add value.
3. Prices move only on surprises, not on expected news: earnings up 45% is good, bad, or irrelevant depending entirely on what the market had already priced in.
4. Market value is the asset\u2019s current price, while intrinsic (fundamental) value is what a fully informed, rational investor would be willing to pay; in highly efficient markets, the two usually line up, but in less efficient markets active investors try to buy below intrinsic value and sell above it.  
5. Intrinsic value is based on fundamentals \u2014 for a bond, this means coupon, maturity, default risk, liquidity, and other key characteristics. Intrinsic value is constantly changing as new (unexpected) information becomes available.
6. **Information + attention**: markets are more efficient when lots of participants track them and when information is public, timely, and equally available. Fewer analysts, poor disclosure, or selective leaks ⟶ slower price adjustment and mispricing.    
7. **Ability to trade and correct prices**: arbitrage and short selling pull prices back to fair value, but only if trading is easy. High transaction costs, low liquidity, funding limits, or short-sale constraints let wrong prices survive.   
8. **Costs decide real efficiency**: markets are efficient if, **after all information, trading, and funding costs**, no positive risk-adjusted returns are left. Beating the market before fees doesn\u2019t count if you lose after fees.
9. When we talk about market efficiency ⟶ We talk about return adjusted for risk. For this you need a model for expected returns such as CAPM. 
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
16. **Event studies test semi-strong efficiency**: they ask whether you can make abnormal profits after public news. In developed markets, prices adjust almost immediately, so the null holds. *Example*: Apple launches a new iPhone, the stock barely moves on launch day because it\u2019s already priced in. In less efficient markets, even well-known events (like Diwali sales numbers) can lead to slow, multi-day price reactions.
17. Market Anomalies break market efficiency. Momentum is an anomaly. Small cap outperforming Large cap is an anomaly (Size Effect). Low P/E ratio stocks outperform High P/E ones (Value Effect). Price action die to earning surprises persist for days, IPOs are typically underpriced, NAV of closed end MF is undervalued. 
18. **Information cascade**: less-informed investors copy early, better-informed traders; if the early movers truly have superior information, this herding can actually help prices move closer to intrinsic value rather than distort them.


### MODULE 42.2: FOREIGN EQUITIES AND EQUITY RISK
1. When capital flows freely across borders, markets are said to be integrated.
2. Listing on a foreign exchange increases firm transparency because of more disclosures and firm's publicity. 
3. Direct investing is buying foreign firm's stock on a foreign exchange. The investment and return are denominated in a foreign currency.
4. A **depository receipt** lets you own a foreign company while trading in your local market and currency; a depository bank holds the actual foreign shares and handles dividends and corporate actions. You buy **Toyota Motor Corporation ADR (TM)** on the NYSE in USD. The real Toyota shares trade in Japan, while **JPMorgan** holds those shares, converts Toyota\u2019s yen dividends into dollars, and pays them to ADR holders.
5. Sponsored DR: issued with company involvement; investors usually get voting rights and better disclosure. Unsponsored DR: issued without company involvement; voting rights stay with the bank and disclosures are lighter.
6. Global Depository Receipts are issued **outside both the firm\u2019s home country and the U.S.**, typically trade in **London or Luxembourg**, ==are often **USD-denominated**==, and avoid capital-flow restrictions\u2014making it easier for global investors to invest. Firms list them where investors already recognize the company. **Tata Motors** has GDRs traded in **London**, letting international investors buy exposure to Tata Motors in USD without dealing with Indian market restrictions.
7. **ADRs** trade in the U.S., in USD, and usually require SEC registration. ==Some are also privately placed (Rule 144A or Regulation S receipts)==. **ADS (American Depository Share)**: the **actual underlying share** of the foreign company that sits in its **home market**.
8. Level I ADR trade OTC, and cheap to list. Level II ADR trade on Exchanges and are expensive to list. Both these CANNOT raise capital in US.
9. Level III is listed on exchange and CAN raise capital in US.
10. If it\u2019s listed publicly, SEC is involved. In all Level I, II and III, SEC registration is required.
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

1. GICS: Sector ⟶ Group ⟶ Industry ⟶ Sub-industry **[SGISub]**  
	ICB: Industry ⟶ Supersector ⟶ Sector ⟶ Subsector) **[ISSS]**  
	TRBC: Economic sector ⟶ Business sector ⟶ Group ⟶ Industry ⟶ Activity **[EBGIA]**
	*G for Group, S always for Sector, B for business, I for Industry*

2. How to classify?
	- **Single business:** classify in that business    
	- **Multiple businesses:** use the one with **\u226560% revenue**    
	- **If not:** use **\u226550% of revenue, profit, or assets**    
	- **If still unclear:** use **judgment** or label **conglomerate**
3. Other ways to group companies could be on the basis of business cycle (Consumer staples are stable so Defensive, Software is cyclical), geography, Financial Measures (large cap, mid cap) etc, or ESG (How green a company is?)
4. Company A sells USD 100 billion total in which Smartphones: USD 40 billion and Other products (laptops, services, TVs): USD 60 billion. Industry size = sales of the product, not total sales of multi-business firms. (only 40 bn in case of Smartphone industry)
5. Growth industries have considerable growth potential. (Semiconductors). Mature industries have little or no growth potential (Tobacco).
6. Profitability: Use ROIC (after-tax, capital-structure neutral) to rank firms by deciles, 
7. Market share = firm revenue � industry size; levels are estimates, trends matter most.
8. Herfindahl Index (Industry Concentration) = sum of squared market shares; <1500 = low, 1500\u20132500 = moderate, >2500 = high concentration.

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
	- Payout Ratio \u2191 PE multiple \u2191
	- k \u2191 PE Multiple \u2193. High DE Ratio, or anything that signals higher risk would crank up required rate of return
	- g \u2191 PE multiple \u2191. Anything that signals higher future earnings would crank up g. For example, higher sales growth, bullish outlook etc.
9. The disadvantages of multiples based approach is:
	- **Comparable vs fundamental conflict**: Tesla can look _overvalued_ on peer P/E versus automakers, yet _fair_ or undervalued on a DCF assuming high growth.
	- **Accounting differences**: SAP (IFRS) vs Oracle (US GAAP) can show different P/E or P/B purely due to R&D and revenue-recognition rules.
	- **Cyclicality distortion**: Delta Air Lines may show a very low P/E at peak earnings (looks cheap) and a very high P/E in a downturn (looks expensive), driven by the cycle, not mispricing.
10. Enterprise value represents the total takeover cost: equity plus debt minus cash, because the acquirer assumes debt but also receives the cash.
11. EV is preferred when comparing firms with different capital structures; market cap alone can mislead.
12. EV must be matched with earnings available to both debt and equity holders, which is why EV/EBITDA is used; when net income is negative, P/E breaks but EV/EBITDA still works. Firm A has EV = 1,000, EBITDA = 100 ⟶ EV/EBITDA = 10. Net income = \u221210, so P/E is meaningless, but valuation via EV still works.
13. EBITDA can mislead because it ignores capital expenditures and can overstate cash flow. Eg: Vodafone Group often reports strong EBITDA, but heavy recurring capex on spectrum licenses and network upgrades absorbs most of the cash, so free cash flow remains weak despite attractive EV/EBITDA.
14. Asset-based valuation starts from the balance sheet and estimates equity as fair value of assets minus liabilities, adjusting book values using depreciated cost, inflation-adjusted cost, or replacement cost because book \u2260 market.
15. Asset-based models struggle when intangibles dominate, so values are usually treated as a floor or liquidation value and work best only for tangible-asset-heavy or liquidation cases. Eg: Google has a brand, talent and data which makes tangible asset valuation meaningless.

## FIXED INCOME

### MODULE 52.1: FIXED INCOME BOND VALUATION

1. If 2 year YTM is 4.3% and 5 year YTM is 5.2%, what is the 3 year forward rate. $(1.052^5 / 1.043^2)^{(1/3)} - 1 = 5.81\%$
2. Matrix pricing uses the yields of actively traded bonds with similar credit quality, coupon rates, and maturities to estimate the yield of an illiquid bond. The process relies on linear interpolation to estimate the yield-to-maturity for the target bond's specific maturity date.
3. **Matrix Pricing:** Recipe is to first calculate interpolated YTM using the given info and then compute PV
	
> [!question] QUESTION
> 
> ##### Price Interpolation
> 
> Rob Phelps, CFA, is estimating the value of a nontraded 4% annual-pay, A+ rated bond that has three years remaining until maturity. He has obtained the following yields to maturity on similar corporate bonds: 
> A+ rated, 2-year annual-pay, YTM = 4.3% 
> A+ rated, 5-year annual-pay, YTM = 5.1% 
> A+ rated, 5-year annual-pay, YTM = 5.3% 
> Estimate the value of the nontraded bond.
> ---
> If 2 year YTM is 4.3% and 5 year YTM is 5.2%, what is the 3 year interpolated YTM. $\Delta YTM (\text{3y}) = 5.2-4.3 = 0.9$. YTM increases by 0.9/3 = 0.30 per year. So 3-year straight line approximate YTM: 4.3+0.3 = 4.6% 
> 
> Now: I/Y = 4.6, N = 3, FV = 100, PMT = 4, **PV = -98.353**
> 
> ##### Using Spreads
> 
> Consider the following market yields:
> 4-year, U.S. Treasury bond, YTM 1.48%
> 5-year, A rated corporate bond, YTM 2.64%
> 6-year, U.S. Treasury bond, YTM 2.15%
> Estimate the required yield spread on a newly issued 6-year, A rated corporate bond
> 
> ---
> 5y YTM of US Treasury = 1.48 + (2.15-1.48)/2 = 1.480 + 0.335 = 1.815%
> A rated bond spread = 2.640 - 1.815 = 0.825 
> 6y YTM = 2.150 + 0.825 = 2.975
> 

4. The 'constant-yield price trajectory' illustrates how a bond's price moves toward par value as time passes, assuming the issuer does not default.
5. The YTM calculation assumes the investor holds the bond until maturity. It assumes the issuer makes all coupon and principal payments as scheduled without default. **==It assumes all coupon payments are reinvested at the calculated Yield-to-Maturity.==**
6. Generally, for the same change in market discount rates, a longer-term bond will experience a greater percentage price change than a shorter-term bond because the longer maturity bond has more cashflows that suffer the wrath of discounting.
7. ==A lower-coupon bond will typically have a higher percentage price change than a lower-coupon bond when market discount rates change by the same amount.== Lower coupon bond has *higher* interest rate risk (greater percentage price change) because a larger proportion of its value comes from the final principal payment, which is more sensitive to discounting. A higher coupon bond returns cash sooner, reducing duration.
8. **Convexity is optimistic.** The convexity effect implies that for the same absolute change in yield, the percentage price increase when yields fall is greater than the percentage price decrease when yields rise. 
9. he Actual/Actual method counts *actual* calendar days, which includes weekends, holidays, and leap days; it does not exclude them. Government bonds typically use Actual/Actual to be precise. #memorise
10. The 30/360 day count convention assumes each month has 30 days and the year has 360 days, and is often used for corporate bonds. #memorise
11. The flat price (or clean price) is the quoted price. It excludes accrued interest so that the price does not appear to drop significantly solely because a coupon payment was made.
12. The full price, also known as the invoice price, is equal to the flat price plus accrued interest.


> [!QUESTION] Title
> A 10-year, 8% annual coupon bond is purchased at a premium price of 115.00 (Yield = 6.00%). Assuming the yield remains constant at 6.00%, what is the expected price of the bond 1 year later (9 years to maturity)?

### FIXED INCOME MARKETS FOR CORPORATE ISSUERS
1. Firms with low credit ratings must pledge collateral. Strong credit firms issue commercial paper (CP) which are unsecured, typically < 3 months maturity, used for working capital or temporary/bridge funding.
2. **Factoring** Firm sells receivables to a lender at a discount. Lender takes over credit risk + collection. Example: USD 100 invoice sold for USD 95 today ⟶ instant liquidity.
3. Bridge Financing refers to short-term funding used until permanent financing (bonds, equity) is arranged. A company plans to issue a 10-year bond in 3 months but needs cash now to run operations ⟶ it issues 3-month commercial paper today ⟶ when the bond is issued, the proceeds are used to repay the CP.
4. **Rollover** = repaying old short-term debt by issuing new short-term debt instead of using cash. ==The risk that the company would not be able to sell a new commercial paper to repay the old one is known as rollover risk.==
5. Banks fund short-term mainly through deposits: checking, operational corporate deposits, savings, and certificates of deposit (CDs). For example, fixed deposits in India.
6.  Asset Backed Commercial Paper: A bank sets up a vehicle that buys car loans, then issues 30-day asset-backed commercial paper to investors, and keeps issuing new 30-day ABCP every month to repay the old ABCP, with the car loans as collateral. Cash to repay ABCP comes from loan EMIs first, new ABCP issuance next, money from sponsoring bank during bad days, and asset sales only as last resort.
7. Repo = collateralised borrowing where one party sells a security today and agrees to buy it back later at a higher price; that price difference is the repo rate, i.e. the interest on the loan embedded in prices, not quoted separately.
8. Example (India): An Indian bank needs overnight cash ⟶ it sells government bonds to the RBI for INR 100 today and agrees to repurchase them tomorrow for INR 99.8. The INR 0.02 difference is the repo interest, and the bonds are the collateral.
9. Collateral protection: lender demands collateral worth more than the cash lent to protect against price drops.
10. **Initial margin (haircut)** = gap between collateral market value and loan amount ⟶ loan amount is a discount to collateral value. Collateral worth INR 105 is posted, but the lender gives only INR 100 cash ⟶ the INR 5 gap is the initial margin (haircut) protecting the lender if collateral prices fall.
11. During the repo life, if collateral value falls, borrower must post extra collateral ⟶ this top-up demand is variation margin.
12. Overnight repo = one-day repo; term repo = repo longer than one day. Repo rates are usually lower than unsecured bank loans because the loan is backed by high-quality collateral (often government bonds).
13.  Repo rates are usually lower when the collateral liquidity is high and the collateral is physically delivered to the lender. Repo rates are usually higher when the term is high and when interest rates for alternative sources of funds are higher.
14.  Tri-party repo = repo where a third party (clearing bank/CCP) handles collateral custody, valuation, and margining; example: an Indian bank borrows overnight via repo using G-secs, while CCIL sits in the middle holding the bonds and settling cash.
15. Reverse repo = the lender\u2019s side of a repo; example: a bank parks excess cash with the RBI, receives G-secs as collateral, and earns the reverse repo rate as interest.
16.  Tri Party repos protect against the following kinds of risks:
	- Default risk = the borrower takes cash today and fails to repurchase the collateral later, forcing the lender to sell the collateral to recover money.
	- Collateral risk = the value of the collateral falls sharply before it can be sold, so even after liquidation it does not fully cover the cash lent.
	- Margining risk = collateral prices move faster than margin calls, so the lender is exposed during the time gap between a price fall and posting of additional collateral.
	- Legal risk = in stress or bankruptcy, the repo is not enforced as expected, and courts may freeze or delay access to collateral by treating the repo like a normal loan.
	- Netting risk = when a counterparty defaults, you cannot offset what you owe against what you are owed, so you must pay all obligations in full while recovering only partially on claims.
	- Settlement risk = cash and securities do not settle simultaneously, so one party delivers cash while the collateral delivery fails or is delayed.

> [!warning] REMEMBER
> Subsidiary assets liquidated first, and subsidiary creditors can be paid from holding company assets if guarantees do not exist. 
> Being higher in the organisational chart does not imply earlier access to asset value. Without guarantees, holding-company creditors are economically subordinated to the operating company’s direct creditors.
17. A higher Retained Cashflow /Net debt ratio means the firm could, in principle, pay down net debt more quickly, implying lower effective leverage and default risk, all else equal.2
### FIXED INCOME MARKET FOR GOVERNMENT ISSUERS

1. Sovereign debt = bonds issued by national governments to fund public goods; backed by taxing power, usually the largest issuers in domestic markets, typically highest credit quality locally.
2. Public-sector accounting focuses on cash flows; analysts should think in balance-sheet terms: implied assets (future taxes) versus liabilities (promised debt payments).
3. Core divide: developed-market issuers borrow in stable, reserve currencies with deep markets and transparent fiscal policy; emerging-market issuers face higher volatility, weaker institutions, and funding constraints.
4. Emerging-market debt is often split into domestic debt (local currency, local investors) and external debt (foreign currency, foreign creditors); external debt adds FX risk because repayment currency \u2260 tax currency.
5. If a government earns in INR but owes USD debt, currency depreciation mechanically raises debt burden even if real activity is unchanged.
6. Governments issue across maturities to balance cost and risk; too much short-term debt lowers rates today but raises rollover risk tomorrow.
7. Rollover risk = inability to refinance maturing debt; classic crisis trigger when markets suddenly refuse to roll short-term bills.
8. Debt management policy decides how much, what type, maturity, currency, and indexation (floating, inflation-linked) of debt is issued.
9. Inflation-linked debt shifts inflation risk to the issuer; nominal fixed-rate debt shifts inflation risk to investors.
10. Sovereign issuance is done via regular public auctions to signal transparency and price discovery. Competitive bids specify both price and quantity; noncompetitive bids accept the auction price and are guaranteed allocation.
11. Government auctions INR 1,000 crore of a 10-year bond; competitive bidders submit bids like \u201cINR 300 crore at 7.10%,\u201d \u201cINR 400 crore at 7.15%,\u201d \u201cINR 500 crore at 7.25%.\u201d Because the auction cleared (filled the quota) at the 7.25% tier, 7.25% is the cutoff yield.
12. In a \u201csingle-price\u201d auction (also known as a Dutch auction), everyone pays the same yield\u2014the highest yield accepted to sell the entire offering. If the government needs to sell bonds and the clearing rate is 4.0%, a bidder who aggressively bid 3.8% still gets the bonds at 4.0%, which encourages more aggressive bidding by removing the fear of overpaying. In a \u201cmultiple-price\u201d auction, winning bidders pay exactly what they bid; if you bid 3.8% and the clearing rate was 4.0%, you are stuck earning 3.8% while others earn more. This structure can reduce aggressive bidding because investors fear the \u201cwinner\u2019s curse\u201d\u2014winning the auction but paying a price worse than the market average.
13. Issuers wanting to minimize yield volatility often prefer single-price auctions; bidders shade less.
14. On-the-run bonds = most recently issued securities at a given maturity; most liquid, used as benchmarks for risk-free rates. ==Yield curves in practice are built off on-the-run sovereign bonds, not off older illiquid issues.==
15. Primary dealers are designated banks obligated to bid in auctions and make secondary markets; they act as transmission channels for monetary policy. Central banks interact with primary dealers as counterparties when conducting open-market operations.
### MODULE 54.1: YIELD AND YIELD SPREAD MEASURES FOR FLOATING-RATE INSTRUMENTS

1. Coupon is reset periodically as per prevailing market reference rate + spread. 
2. On the reset date, the coupon resets to **reference rate + quoted margin (50 bps)**, but investors require **reference rate + required margin (75 bps)**, so the coupon is too low for the market.
3. Therefore, **the price will be below par**, because the bond must trade at a discount so that coupon plus price pull-to-par together deliver the higher required margin.
4. Between resets the bond still trades in the market and its price can move above or below par.
5. It trades **below par** when the quoted margin is too low for current market conditions or issuer risk; example: an FRN pays SOFR + 150 bps, but new FRNs from similar issuers are coming at SOFR + 200 bps, so investors mark the old bond down to 98 so its yield matches the higher required spread.
6. **Quoted margin** is the fixed spread added to the reference rate that defines the coupon on a floating-rate note; example: a FRN pays 3-month LIBOR + 150 bps, so if LIBOR is 5%, the coupon rate is 6.5%, and the 150 bps is the quoted margin written into the bond contract.    
7. **Discount margin** is the spread over the reference rate that makes the present value of all future cash flows equal to the bond\u2019s current market price; example: if the same FRN (LIBOR + 150 bps) trades below par at 98, investors effectively earn LIBOR + 180 bps, and the extra 30 bps over the quoted margin is captured by the discount margin.
8. During issuance, QM = DM. If issuer credit quality deteriorates DM > QM, vice versa.


> [!question] NUMERICAL
> A $100,000 FRN with a semiannual coupon pays a 180-day MRR plus a quoted margin of 120 basis points. On a reset date with five years remaining to maturity, the 180-day MRR is quoted as 3.0% (annualized), and the discount margin (based on the issuer\u2019s current credit rating) is 1.5% (annualized). Estimate the value of the FRN.
> 
> ---
> 
> Coupon Rate = (3.0% + 1.2%) / 2 = 2.1%
> PMT = 0.021 $\times$ 100 = 2.1
> I/Y = (3.0% + 1.5%) / 2 = 2.25%
> N = 10
> FV = 100
> PV = 98.67

9. **Discount yield** quotes return as a percentage of **face value**, not money invested, and ignores compounding; example: a 1-year T-bill with face value 100 bought at 95 has discount yield = (100 \u2212 95)/100 = **5%**, even though you invested only 95.
10. **Add-on yield** quotes return as a percentage of **amount invested**, which reflects actual cash put in but still ignores compounding; example: the same bill bought at 95 has add-on yield = (100 \u2212 95)/95 \u2248 **5.26%**, higher than discount yield because it uses invested cash as the base.


> [!question] NUMERICAL
> 1. A $1,000 90-day T-bill is priced with an annualized discount of 1.2%. Calculate its market price and its annualized add-on yield based on a 365-day year.
>  ---
>  HPY = 90/360 $\times$ 1.2 = 0.3%
>  PV = 1000 / 1.003 = 997
>  
>  2. A $1 million negotiable CD with 120 days to maturity is quoted with an add-on yield of 1.4% based on a 365-day year. Calculate the payment at maturity for this CD and its bond equivalent yield.
>     
>    ---
>    
>    HPY = 120/365 $\times$ 1.4 = 0.46%
>    PV = 1 / 1.0046 = 956,000
>    Discounted yeild = (1 - 0.956) / 1 = 4.4%
>    
> 1. A bank deposit for 100 days is quoted with an add-on yield of 1.5% based on a 360-day year. Calculate the bond equivalent yield and the yield on a semiannual bond basis.
>    
>    HPY = 100/360 $\times$ 1.5 = 0.4166%
>    PV  = 100 / 1.004166 = 99.58
>    Discount Yield = (100-99)/100 = 4.2%
>    Discount Yield (SemiAnnual) = 2.1%
>   
>   
>  

### MODULE 65.1: MORTGAGE-BACKED SECURITY (MBS) INSTRUMENT AND MARKET FEATURES

1. **Prepayment Risk:** You own a callable bond (and interest rate falls) ⟶ They prepay and buy back their now cheaper bond issued at a high interest rate. Interest Rate falls to 2% and you take a cheaper loan and payback your expensive loan. For the bond investor, high-coupon mortgage cash flows disappear right when they\u2019re most valuable, that is why a **risk**.
2. **Extension Risk:** Interest Rate \u2191, Duration \u2193 and Price \u2193. Bond sellers (borrowers) won't exercise their call option. Expected cash-flows get extended. The market rate is higher but the bond buyer (investor) keeps receiving scraps from mortgages issued at low rates.
3. **Contraction Risk:** Interest Rate \u2193, Duration \u2191 and Price \u2191. Prepayments speed up.  Bond sellers (borrowers) will exercise their call option. Cash-flows would arrive sooner than expected.
4. Because the prices of MBS reflect expectations for prepayments in low-rate environments, they will not rise as much in response to decreasing interest rates as other fixed-income instruments that do not have an embedded prepayment option.
5. Convexity is acceleration of prices with falling rates. Prepayments are friction. When rates fall, you lose the deals you earlier did (bought high coupon mortgages), so price of your MBS doesn't rise proportionally. So traditional FI instruments have +ve convexity and MBS **have a -ve convexity**

> [!TIP] HAMMER THIS INTO YOUR HEAD
> Long tranches absorb contraction risk. Short tranches absorb extension risk. People at the front of the queue hate delays (so they have to absorb extension), people at the back don't care because they were anyway waiting. 

6. A mortgage pool pays principal into two tranches: **Tranche S (short)** first, **Tranche L (long)** later. 
7. When **payments speed up**, principal rushes in. Tranch S is unaffected (it was already on the front line to get paid off). The contraction risk gets pushed to back of the line Tranch L. 
8. When **payments slow down (rates rise)**, prepayments stagnates. Tranch L is unaffected (it was already on the back of the line to get paid off). The extension risk hurts the front of the line.
9. If I take a loan of $100 against and pledge my asset of $200, my Loan to Value (LTV) is 200/100 = 2. 
10. A mortgage of USD 300,000 has an annual interest rate of 6%, is to be repaid monthly over 25 years, and the borrower\u2019s annual pretax gross income is $80,000. Calculate DTI. Here, PV=-300,000, FV = 0, N = 25�12 = 300, I/Y = 6/12 = 0.5. This gives PMT = 1932. DTI = (1932 * 12) / 80000 = 0.289 ~ 28.9 %
11. Prime loans are made to creditworthy people, subprime loans are made to broke people.
12. Residential mortgages are different because you **can\u2019t freely prepay**. If you do, you **pay a penalty**,. They can be **recourse or non-recourse**: in recourse loans, the lender can **come after your other assets**; in non-recourse, they\u2019re **stuck with just the house**.
 13. A 30-year US home loan that meets standards gets pooled and guaranteed by **Fannie Mae** or **Freddie Mac**. These **Agency RMBS** are backed either **directly by the government** or by **government-sponsored agencies** (quasi-government companies). Credit risk is basically **off your plate**. Non-agency RMBS: private-issued, no government/GSE backstop ⟶ investors eat credit risk. **2008:** subprime RMBS (e.g., Lehman Brothers) blew up; defaults surged, protections failed, MBS holders lost money.
 14. Mortgage pass-through = claim on cash flows from a pool of mortgages, net of admin fees. Pool can have any number of mortgages; each is a securitized mortgage.
 15. Mortgage A has an outstanding principal of USD 80, a coupon rate of 6%, and a final maturity of 30 years. Mortgage B has an outstanding principal of USD 20, a coupon rate of 4%, and a final maturity of 15 years. Total outstanding principal in the pool is USD 100. Weighted average coupon (WAC) = (80/100 � 6%) + (20/100 � 4%) = 5.6%. Weighted average maturity (WAM) = (80/100 � 30) + (20/100 � 15) = 27 years.
 
> [!DANGER] DO NOT MAKE THIS MISTAKE
> Outstanding and NOT beginning principal, while calculating weights.

16. A **Collaterized Mortgage Obligation (CMO) is a tranched MBS**. The **underlying cash flows are the same** mortgages. What changes is **how those cash flows are split and ordered**. Senior tranche gets paid first and lowest tranche gets paid the last. Total prepayment risk stays the same; it is redistributed across tranches.
17. **Z-tranche** = a CMO tranche that gets no cash interest at first.   During this phase, interest is not paid out; it is **added to principal** instead. Suppose Start: principal = USD 100, coupon = 5%. End of year: no cash paid, principal becomes USD 105. You didn\u2019t get money; your claim just got bigger.
18. So the bond grows silently while other tranches take the cash. After the accrual period, Z-tranche starts receiving normal interest and principal payments. Z-tranche is usually last in line. It sacrifices early cash so other tranches get paid first.     
19. Principal-only (PO) securities and Interest-only (IO) securities are **interest-rate / prepayment bets**, not boring bonds. - If rates fall, people refinance ⟶ **prepayments speed up**.
20. You get **only interest payments**, no principal. You want loans to **stay alive as long as possible**. If rates rise or stay high ⟶ prepayments slow ⟶ **more coupon checks**. Used by investors who want to **bet on rising/stable rates and slow prepayments**.
    
- Principal comes back **faster**, IRR shoots up.

### HEDGE FUNDS
1. **Commingled funds** = multiple clients\u2019 money pooled together and invested as one portfolio; each client owns a proportional share, not specific securities. Eg: Mutual Fund
2. **SMA** = one client, one portfolio. Not pooled. You directly own the securities. Risk preferences can be tailored. Higher than commingled funds due to customization and admin.
3. Hedge Fund Strategies: A **convertible bond** = bond floor (interest + principal) + call option on stock. Buy INR 1000 convertible of XYZ paying coupons + right to convert into shares. Short **XYZ stock** in the right ratio (delta-hedge). _Example_: If bond acts like 0.4 shares, short 0.4 XYZ.
4. Fund-of-funds is a hedge fund invested in multiple hedge funds. **Fee layering** = you pay fees twice in a fund-of-funds: once to the FoF manager, again to the underlying hedge funds.
5. �Under a **'1 or 30' fee structure**, the manager receives the greater of a 1% management fee or a 30% incentive fee on the fund's alpha.
6. Kinds of Fees at Hedge Fund
	- **Management fee**: Fixed annual fee (e.g., 2% of AUM) paid **regardless of performance** ⟶ covers salaries, rent, survival.    
	- **Incentive (performance) fee**: Share of profits (e.g., 20%) paid **only if fund makes money**.	    
	- **Hurdle rate**: Minimum return (e.g., T-bill or 5%) the fund must beat **before** incentive fees apply ⟶ no reward for just market drift.	    
	- **High-Water Mark (HWM)**: Highest NAV ever reached; incentive fees are paid **only on gains above the previous peak** ⟶ manager must first recover losses before earning again.
7. **Convertible arbitrage fixed income strategy:** \u201cArbitrage\u201d here is: market price of convertible \u2260 price of (bond + call). You buy the convertible bond (which acts like a stock with a safety net). Suppose the bond is selling for 100 and convertible at 95 (safety net). And short the actual stock to cancel out market direction. When prices go up bond gains value faster (convexity) than your short stock loses it. When prices go down, your bond holds value (bond floor protection) while your short stock soar.
8. **Hedge Fund Index performance is overstated:** 
	- Because of **survivorship bias**: Most hedge fund don't survive and indexes are constructed only on functioning ones.
	- Because of **selection bias** because indexes have their own constraints for which fund to include and which one not to include.
	- **Backfill Bias**: A hedge fund operates privately at first so its early returns are invisible to databases; if those early returns turn out good, the manager chooses to join a data`b`ase and backfills only that strong past performance, while funds with weak early results never join at all\u2014so the recorded history ends up showing only winners and systematically overstates true hedge-fund returns.

## ALTERNATIVE INVESTMENTS

### MODULE 77.1: PERFORMANCE APPRAISAL AND RETURN CALCULATIONS


> [!ABSTRACT] MEMORISE THIS FOR EFFICIENCY
> - IRR is the most important measure of performance here, MWROR is appropriate when manager controls the timing of cashflows. 
> - A simpler measure of investment success **is the multiple of invested capital (or money multiple)** - the ratio of total capital returned plus the value of any remaining assets, to the total capital paid in over the life of the investment.
> - Management fee is paid no matter what: a fund with INR 100 crore AUM charging 2% earns INR 2 crore per year even if returns are zero or negative.    
> - **Hurdle rate** is the minimum return the fund must earn before performance fees apply;
> - **Performance fee** is a share of profits taken by the manager after crossing the hurdle; example: with a 20% performance fee, if a INR 100 investment earns INR 20 above the hurdle, the manager keeps INR 4 and investors keep INR 16. **It has a zero lower bound.**

1. **Cashflow Lifecycle for Alternative Investments: **
	- Capital Commitment Phase: Partners and Investors promise to **commit a amount** and startup makes **"capital calls (give us the money)"**.
	- Capital Deployment Phase: Startup is investing and conquering the market aggressively. **ROI is negative.** 
	- Capital Distribution Phase: **ROI turns positive.** Investors earn dividends.
2. The above life-cycle is characterised by J-curve. Start from 0, do gown and then steeply climb upwards.
3. Given the variability of cash flows over a fund\u2019s life and the importance of management decisions in the timing and magnitude of after-tax cash flows, **an IRR over the life of a fund is the most appropriate measure of after-tax investment performance.**
4. A simpler measure of investment success�**is the multiple of invested capital (or money multiple)**�- the ratio of total capital returned plus the value of any remaining assets, to the total capital paid in over the life of the investment.
5. Suppose I have $V_0$ and I borrow $V_B$ at rate $r_b$. I make $r$ on my total investment.
	- My net return: Money I made - Money I owe (b/c I borrowed) = $r \times (V_0 + V_B) - r_b \times V_B$
	- My leveraged return would be:		$$ r_L = \frac{rV_0 + (r-r_b)V_B}{V_0} $$
6. Alt Investments are usually illiquid. Asset Valuations occur using the fair value hierarchy:
	- Level I: Liquid and trades frequently
	- Level II: Illiquid but valuation can be estimated using tradeable derivatives and other observable inputs. For example: A corporate bond might not trade on exchange but you can value it using the spread on similar bonds (or some bond index).
	- Level III: Extremely Illiquid
7. Particularly for Level 3 investments, the absence of market activity can result in **==valuations that remain near their initial cost for long periods==**. ==**As a result, these values might not reflect the actual exit costs of the investments.**== 
8. Importantly, **this relative lack of change in fair values can make reported returns for alternative investments appear higher, less risky, and less correlated with traditional investments than they really are.** Even if a startup is losing money, the valuation sticks to the cost value of its assets.
9. **Survivorship bias** happens when performance data shows only funds that are still alive, making results look better than they really were; example: 100 hedge funds start in 2020, 30 fail after losing money, but the index tracks only the surviving 70, so investor losses in the failed funds disappear from the numbers.    
10. **Backfill bias** happens when funds enter databases only after doing well and then report their good past returns; example: a fund launches in 2021, makes +20% in its first year, joins a database in 2022, and adds that +20% to its history, while funds with bad starts never get included.  
11. **Vintage year** means comparing funds that started in the same year so they are at similar stages of life; example: comparing 2018 funds with other 2018 funds is fair, but comparing a new fund with one that started in 2005 mixes early growing pains with mature performance and misleads.
12. **Management fee** is a fixed annual fee charged on assets under management, paid regardless of performance; example: a fund with INR 100 crore AUM charging 2% earns INR 2 crore per year even if returns are zero or negative.    
13. **Hurdle rate** is the minimum return the fund must earn before performance fees apply; example: with an 8% hurdle, a fund earning 6% pays no performance fee, but earning 12% pays fees only on the excess above 8%.    
14. **Performance fee** is a share of profits taken by the manager after crossing the hurdle; example: with a 20% performance fee, if a INR 100 investment earns INR 20 above the hurdle, the manager keeps INR 4 and investors keep INR 16. It cannot be negative.

> [!QUESTION] NUMERICAL
> BJI Funds is a hedge fund with a value of $110 million at initiation. BJI Funds charges a 2% management fee based on assets under management at the beginning of the year and a 20% performance fee with a 5% soft hurdle rate, and uses a high-watermark. Performance fees are calculated on gains net of management fees. The year-end values before fees are as follows: 
>     **Year 1:** $100.2 million 
>     **Year 2:** $119.0 million 
> Calculate the total fees and the investor\u2019s after-fee return for both years.
> 
> ---
> 
> 




> [!Question] NUMERICAL
> An investor makes a total investment of $60 million in a fund-of-funds that has a \u201c1 and 10\u201d fee structure, with management and performance fees calculated independently based on year-end values. Of the $60 million investment, $40 million is allocated to the Alpha fund and $20 million is allocated to the Beta fund. One year later, the value of the Alpha fund investment is $45 million, and the value of the Beta fund investment is $28 million, both net of fund fees. Calculate the investor\u2019s return for the year net of fees.


> [!question] NUMERICAL
> A private equity fund invests $100 million in a venture company that is sold for $130 million. The fund also invests $100 million in an LBO that goes poorly and is liquidated for $80 million.
> If the carried interest performance fee for the GP is 20% and there is no clawback provision, calculate the investor\u2019s return after performance fees, assuming the investment outcomes are realized in the same year under the following:
a. An American-style (deal-by-deal) waterfall structure
b. A European-style (whole-of-fund) waterfall structure


### PRIVATE EQUITY
1. Each private equity fund has a vintage year, which is the year the fund made its first investment. The performance of a fund is greatly influenced by its vintage year and the phase of the business cycle in that year. Funds that begin investing during a business cycle expansion are likely to earn higher rates of return if they specialize in early-stage companies. Funds that begin investing during business cycle contractions are likely to earn higher rates of return if they specialize in distressed companies. Investors in private capital should diversify across vintage years.

## PORTFOLIO MANAGEMENT

### INTRODUCTION TO RISK MANAGEMENT

1. The following are financial risks (CMLI):
	- **Credit risk** \u2013 The other side may not pay. _Example:_ A company sells goods on credit; the buyer goes bankrupt and never pays.
	- **Market risk** \u2013 Prices move against you. _Example:_ Equity prices fall in a recession; bond prices fall when interest rates rise.
	- **Liquidity risk** \u2013 You can\u2019t sell fast without taking a big price hit. _Example:_ You hold a small-cap stock; in a panic market, you sell much lower than its fair value.   
	- **Interest rate risk**: Risk of prepayments or higher opportunity cost of capital.
2. The following are non-finacial risks (*SolRegPolLegModTailOper*):	 
	- **Solvency risk** \u2013 The firm runs out of cash and can\u2019t survive. _Example:_ A company can\u2019t pay salaries or debt interest and goes bankrupt.    
	- **Regulatory risk** \u2013 Rules change and hurt the business. _Example:_ A new capital requirement forces banks to raise equity or cut lending.    
	- **Political / tax risk** \u2013 Government actions outside normal regulation hurt profits. _Example:_ Sudden tax hike reduces after-tax earnings of companies.    
	- **Legal risk** \u2013 Future lawsuits or legal action cause losses.   _Example:_ A firm is sued for mis-selling products and pays heavy penalties.    
	- **Model risk** \u2013 Your math or valuation model is wrong. _Example:_ A risk model underestimates losses because it assumes normal distributions.    
	- **Tail risk** \u2013 Rare, extreme events happen more often than expected. _Example:_ A 2008-style crash wipes out strategies built for \u201cnormal\u201d markets.    
	- **Accounting risk** \u2013 Financial statements turn out to be wrong.  
	    - _Example:_ Aggressive revenue recognition leads to restated earnings later.
	- **Operational risk** \u2013 Loss due to people, process, or system failure. _Example:_ A trading desk loses money because of a fat-finger trade or a cyberattack shuts systems.
3. With a **risk transfer**, another party takes on the risk. Insurance is a type of risk transfer. The risk of fire destroying a warehouse complex is shifted to an insurance company by buying an insurance policy and paying the policy premiums. Insurance companies diversify across many risks so the premiums of some insured parties pay the losses of others.
4. **Risk shifting** is a way to change the distribution of possible outcomes and is accomplished primarily with derivative contracts. For example, financial firms that do not want to bear currency risk on some foreign currency denominated debt securities can use forward currency contracts, futures contracts, or swaps to reduce or eliminate that risk.
5. With a **surety bond**, an insurance company has agreed to make a payment if a third party fails to perform under the terms of a contract or agreement with the organization.
6. Insurers also issue fidelity bonds, which will pay for losses that result from employee theft or misconduct.

### MODULE 84.1: SYSTEMATIC RISK AND BETA

1. Portfolio return is a weighted average, so if $W_P$ is invested in a risky portfolio $P$ and $W_f = 1 - W_P$ is invested in a risk-free asset, expected return is  
   $E(R) = W_f R_f + W_P E(R_P)$.
2. The risk-free asset has zero variance and zero covariance with all assets, so portfolio risk comes entirely from the risky portfolio.
3. Portfolio variance therefore reduces mechanically to  
   $\sigma^2 = W_P^2 \sigma_P^2$,  
   and portfolio standard deviation is  
   $\sigma = W_P \sigma_P$.
4. Solving for $W_P = \sigma / \sigma_P$ and substituting into the return equation gives  
   $E(R) = R_f + \frac{E(R_P) - R_f}{\sigma_P}\,\sigma$. This is a linear risk\u2013return relationship: expected return increases proportionally with risk. **In risk\u2013return space, all such portfolios lie on a straight line starting at $(0, R_f)$ and passing through $(\sigma_P, E(R_P))$. This is known as capital allocation line**
5. Example: if $R_f = 4\%$, $E(R_P) = 10\%$, and $\sigma_P = 20\%$, then a portfolio with $\sigma = 10\%$ must have $E(R) = 7\%$.
6. Economic intuition: combining a risk-free asset with a risky portfolio does not create diversification curvature; it only scales risk and excess return along a straight line.
7. If all investors are clones of each other, meaning they have identical beliefs about returns, risk, and correlations, they will all rank risky portfolios in exactly the same way. Since the efficient frontier is constructed purely from these beliefs, every investor faces the same frontier and identifies the same tangency (optimal) risky portfolio.
8. Intuitively, if everyone agrees on the risk\u2013return trade-offs, there is no reason for anyone to pick a different risky portfolio; they differ only in how much of that portfolio they combine with the risk-free asset. An investor who chooses to take no risk will allocate 100% in the risk free asset.
9. Diversification works because portfolio variance contains covariance terms, so when assets are not perfectly correlated, idiosyncratic shocks cancel out in aggregation; this cancelable component is unsystematic (firm-specific) risk, which shrinks as the number of independent return sources increases.
10. The market portfolio already holds all risky assets, so all unsystematic risk is averaged away, leaving only systematic risk\u2014the part of return variance driven by common market factors that move many assets together and therefore cannot cancel.
11. You do not need to hold every stock to eliminate unsystematic risk: **as the number of reasonably uncorrelated stocks increases, portfolio variance converges toward systematic variance, meaning marginal risk reduction from adding more stocks rapidly approaches zero.**
12. The implications of this conclusion are very important to asset pricing (expected returns).
13. Since unsystematic risk can be eliminated by diversification, competitive markets price it at zero premium; in equilibrium, bearing firm-specific volatility does not increase expected return.
14. Only systematic risk survives aggregation across investors, so expected returns load on exposure to common risk factors, summarized in equilibrium by a risk premium proportional to systematic risk (e.g., market beta).
15. Resulting implication for portfolio choice: rational investors diversify away idiosyncratic risk and choose portfolios based on how much systematic risk they want to bear, not on standalone stock volatility.
