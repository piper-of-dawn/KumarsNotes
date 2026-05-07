```table-of-contents
```
## QUANTITATIVE METHODS

> [!NOTE] LOS
> 1. Explain an interest rate as the sum of a real risk-free rate and premiums that compensate investors for distinct types of risk.
> 2. Calculate and interpret different approaches to return measurement over time and describe their appropriate uses.
> 3. Compare the money-weighted and time-weighted rates of return and evaluate portfolio performance using these measures.
> 4. Calculate and interpret annualized return measures and continuously compounded returns, and describe their appropriate uses.
> 5. Calculate and interpret major return measures and describe their appropriate uses.

> [!tip] SEE THIS BEFORE EXAM
> - Interest rate can be read three ways: required return, discount rate, or the opportunity cost of consuming now instead of later.
> - Exact Fisher relation:
>
> $$
> (1+r_{\text{nominal}})=(1+r_{\text{real}})(1+\pi_e)
> $$
>
> - Quick approximation:
>
> $$
> r_{\text{nominal}} \approx r_{\text{real}}+\pi_e
> $$
>
> - Full rate build-up:
>
> $$
> r \approx r_{\text{real risk-free}}+\pi_e+\text{default premium}+\text{liquidity premium}+\text{maturity premium}
> $$
>
> - Holding period return (HPR):
>
> $$
> \mathrm{HPR}=\frac{V_1-V_0+\text{income}}{V_0}
> $$
>
> - Multi-period return:
>
> $$
> (1+R_T)=\prod_{t=1}^{n}(1+R_t)
> $$
>
> - Annualized return over `d` days:
>
> $$
> r_{\text{annual}}=(1+\mathrm{HPR})^{365/d}-1
> $$
>
> - Continuously compounded return:
>
> $$
> r_{cc}=\ln(1+\mathrm{HPR})=\ln\left(\frac{V_1}{V_0}\right)
> $$
>
> - Money-weighted rate of return = internal rate of return (IRR) on account cash flows.
> - Time-weighted rate of return = break at each external cash flow, compute each subperiod HPR, multiply them, and annualize if needed.
> - Real return:
>
> $$
> r_{\text{real}}=\frac{1+r_{\text{nominal}}}{1+\pi}-1
> $$
>
> - Leveraged return:
>
> $$
> r_L=r+\frac{V_B}{V_C}(r-r_B)
> $$
>
> ==If money is added just before bad performance, money-weighted return falls below time-weighted return.==
> ==Arithmetic mean answers "average period." Geometric mean answers "compound growth." Harmonic mean answers "average cost with equal money invested each time."==

#### Module 1.1: Interest Rates and Return Measurement

1. Interest rate is just the price of waiting. If you give up spending today, the market demands compensation for that delay. That same number can be read as the required return, the discount rate, or the opportunity cost of present consumption.

2. The cleanest starting point is the real risk-free rate. What is real risk-free rate: the theoretical one-period rate with no inflation and no default. Why is real risk-free rate used: it isolates pure time preference, meaning how much extra return people demand just to wait.

3. Once inflation enters the picture, the market stops quoting a pure real rate and starts quoting a nominal rate. The exact Fisher relation is:

$$
(1+r_{\text{nominal}})=(1+r_{\text{real}})(1+\pi_e)
$$

Symbol intuition: $r_{\text{nominal}}$ is the quoted market rate, $r_{\text{real}}$ is growth in purchasing power, and $\pi_e$ is expected inflation. Expected inflation matters because rates price the future, not last year's grocery bill.

4. In exam questions, you will often use the approximation:

$$
r_{\text{nominal}} \approx r_{\text{real}}+\pi_e
$$

This approximation is usually good enough when rates are not huge. If the question says "exact," go back to the multiplied version.

5. A quoted interest rate can also include extra premiums because real life is messy. If the borrower may default, if the security may be hard to sell, or if you are locking money up for longer, investors demand more.

$$
r \approx r_{\text{real risk-free}}+\pi_e+\text{default premium}+\text{liquidity premium}+\text{maturity premium}
$$

Default premium pays you for the chance the borrower does not pay on time. Liquidity premium pays you for the risk that you may need cash fast and be forced to sell cheap. Maturity premium pays you because long-dated prices move around more.

6. The first return formula you should hammer into your head is holding period return (HPR):

$$
\mathrm{HPR}=\frac{V_1-V_0+\text{income}}{V_0}
$$

Symbol intuition: $V_0$ is beginning value, $V_1$ is ending value, and income is any cash received during the period such as dividends, coupons, or rent.

> [!question] HOLDING PERIOD RETURN
> Problem: A stock starts at **EUR 20**, pays a **EUR 1** dividend, and ends at **EUR 22**. Find the holding period return.
>
> ---
>
> Solution:
>
> $$
> \mathrm{HPR}=\frac{22-20+1}{20}=\frac{3}{20}=15\%
> $$
>
> Explanation: You made **EUR 2** from price change and **EUR 1** from income, all on an initial **EUR 20** investment.

7. For multiple periods, returns compound. Do not add returns across time unless the question is explicitly asking for an arithmetic average.

$$
(1+R_T)=(1+R_1)(1+R_2)\cdots(1+R_n)
$$

If Year 1 return is **10%** and Year 2 return is **-10%**, your two-year return is not zero. It is:

$$
(1.10)(0.90)-1=-1\%
$$

That is the whole reason geometric thinking matters in finance.

8. Arithmetic mean return is the simple average of periodic returns:

$$
\bar R_{\text{arith}}=\frac{1}{n}\sum_{t=1}^{n}R_t
$$

Use it when you want the average single-period observation. It is an unbiased estimator of the underlying mean return, but it does not tell you what money actually compounded to.

9. Geometric mean return is the compound growth rate:

$$
\bar R_{\text{geo}}=\left[\prod_{t=1}^{n}(1+R_t)\right]^{1/n}-1
$$

Use it when the question is asking, "What constant periodic return would produce the same final wealth?"

> [!question] GEOMETRIC MEAN RETURN
> Problem: Annual returns over three years are **-9.34%**, **23.45%**, and **8.92%**. Find the compound annual rate of return.
>
> ---
>
> Solution:
>
> $$
> (1-0.0934)(1+0.2345)(1+0.0892)=1.21903
> $$
>
> $$
> \bar R_{\text{geo}}=(1.21903)^{1/3}-1=6.82\%
> $$
>
> Explanation: Your money grew by a total factor of **1.21903** over three years, so you now back out the one constant annual growth rate that would do the same job.

10. A very common trap is mixing up geometric mean with annualized return when the periods are not years. If the returns are semiannual, the geometric mean gives the average six-month return, not the annual return.

> [!question] GEOMETRIC MEAN VS ANNUALIZED RETURN
> Problem: Four semiannual returns are **2.0%**, **0.5%**, **-1.0%**, and **1.5%**. Find both the geometric mean per semiannual period and the annualized return.
>
> ---
>
> Solution:
>
> $$
> (1.02)(1.005)(0.99)(1.015)=1.0298715
> $$
>
> Semiannual geometric mean:
>
> $$
> (1.0298715)^{1/4}-1=0.743\%
> $$
>
> Annualized return over two years:
>
> $$
> (1.0298715)^{1/2}-1=1.49\%
> $$
>
> Explanation: Four semiannual periods equal two years. So the root for the geometric mean is **4**, but the root for annualization is **2**.

11. Harmonic mean is the one students keep forgetting because it looks less glamorous. It matters when equal amounts of money are invested at different prices and you need the average cost per share.

$$
\bar X_H=\frac{n}{\sum_{t=1}^{n}(1/X_t)}
$$

Why is harmonic mean used: because equal-money purchases mean you buy more shares when price is low and fewer when price is high, so the true average cost must weight the cheaper periods more heavily.

> [!question] HARMONIC MEAN FOR AVERAGE COST
> Problem: An investor buys **USD 1,000** of mutual fund shares at prices of **USD 8**, **USD 9**, and **USD 10** over three months. Find the average cost per share.
>
> ---
>
> Solution:
>
> $$
> \bar X_H=\frac{3}{\frac{1}{8}+\frac{1}{9}+\frac{1}{10}}=8.93
> $$
>
> Explanation: Equal dollars are being invested each time, so the harmonic mean captures the fact that the investor bought more shares when the fund was cheaper.

12. The clean ranking for positive values is:

$$
\text{harmonic mean} < \text{geometric mean} < \text{arithmetic mean}
$$

The only time they are equal is when every observation is the same. More volatility pushes them farther apart.

13. If a return dataset has ugly outliers, the curriculum also mentions trimmed means and winsorized means. You do not use them for compounding. You use them to reduce the influence of extreme observations.

#### Module 1.2: Time-Weighted and Money-Weighted Returns

14. Money-weighted return is internal rate of return (IRR) applied to a portfolio. It answers: "What single discount rate makes the present value of money going into the account equal the present value of money coming out?"

15. Time-weighted return is designed to remove the distortion created by external cash flows. It answers a different question: "How fast did the portfolio itself grow, independent of when the investor added or withdrew money?"

16. For money-weighted return, put the beginning value and all deposits on one side, and the ending value and withdrawals on the opposite side. Then solve for the internal rate of return.

> [!question] MONEY-WEIGHTED RETURN
> Problem: An investor buys one share for **USD 100** at `t = 0`. At `t = 1`, she adds **USD 118** net and buys one more share. At `t = 2`, she receives **USD 264** from selling both shares and collecting dividends. Find the money-weighted rate of return.
>
> ---
>
> Solution:
>
> Cash flows from the investor's point of view are:
>
> $$
> -100,\ -118,\ 264
> $$
>
> Solve:
>
> $$
> \mathrm{IRR}(-100,-118,264)=13.86\%
> $$
>
> Explanation: Money-weighted return gives more weight to periods where more capital was sitting in the account.

17. Time-weighted return has a three-step exam flow: break the timeline at each significant external cash flow, compute holding period return for each subperiod, then multiply the subperiod growth rates and annualize if the full horizon is longer than one year.

18. The most common mistake here is using the wrong beginning value for the second subperiod. The beginning value must be the portfolio value immediately after the external flow resets the subperiod.

> [!question] TIME-WEIGHTED RETURN
> Problem: Use the same facts as the previous example. One share is bought for **USD 100** at `t = 0`, another share is bought for **USD 120** at `t = 1`, each share pays a **USD 2** dividend each year, and both shares are sold at `t = 2` for **USD 130** each. Find the annual time-weighted rate of return.
>
> ---
>
> Solution:
>
> First subperiod:
>
> $$
> \mathrm{HPR}_1=\frac{122-100}{100}=22\%
> $$
>
> The first share is worth **USD 120** at `t = 1`, and the dividend is **USD 2**. So the first subperiod ends at **USD 122**.
>
> Second subperiod:
>
> Immediately after the investor adds the second share, beginning portfolio value is:
>
> $$
> 120+120=240
> $$
>
> Ending value plus dividends at `t = 2` is:
>
> $$
> 130+130+2+2=264
> $$
>
> $$
> \mathrm{HPR}_2=\frac{264-240}{240}=10\%
> $$
>
> Two-year total return:
>
> $$
> (1.22)(1.10)=1.342
> $$
>
> Annual time-weighted return:
>
> $$
> (1.342)^{1/2}-1=15.84\%
> $$
>
> Explanation: Time-weighting strips out the effect of the investor choosing to add money after Year 1.

19. If cash is added just before poor performance, money-weighted return will usually be lower than time-weighted return because more money got hit during the bad period. If cash is added just before strong performance, money-weighted return will usually be higher.

20. For manager evaluation, time-weighted return is usually the right choice because managers usually do not control when clients add or withdraw money. If the manager actually controls the timing of capital flows, money-weighted return becomes more relevant.

> [!question] QUICK COMPARISON NUMERICAL
> Problem: An investor buys a share for **USD 40** at `t = 0`, buys another share for **USD 50** at `t = 1`, and sells both for **USD 60** each at `t = 2`. The stock pays **USD 1** dividend at `t = 1` and `t = 2`. Find the periodic money-weighted return and the annual time-weighted return.
>
> ---
>
> Solution:
>
> Money-weighted return:
>
> $$
> \mathrm{IRR}(-40,-49,122)=23.82\%
> $$
>
> Time-weighted return subperiods:
>
> $$
> \mathrm{HPR}_1=\frac{50-40+1}{40}=27.5\%
> $$
>
> $$
> \mathrm{HPR}_2=\frac{122-100}{100}=22\%
> $$
>
> Two-period compounded return:
>
> $$
> (1.275)(1.22)-1=55.55\%
> $$
>
> Annual time-weighted return:
>
> $$
> (1.5555)^{1/2}-1=24.72\%
> $$
>
> Explanation: **23.82%** is the periodic internal rate of return. The portfolio's total two-period time-weighted growth is **55.55%**, which converts to an annual time-weighted return of **24.72%**.

#### Module 1.3: Common Measures of Return

21. Interest rates and market returns are usually quoted on an annual basis even when the actual investment lasted a different number of days. That is why annualization exists.

$$
r_{\text{annual}}=(1+\mathrm{HPR})^{365/d}-1
$$

Symbol intuition: `d` is the number of days in the holding period. The curriculum uses a **365-day** year here.

> [!question] ANNUALIZED RETURN: LESS THAN ONE YEAR
> Problem: A saver deposits **USD 100** and has **USD 100.75** after **90 days**. Find the annualized return.
>
> ---
>
> Solution:
>
> $$
> \mathrm{HPR}=\frac{100.75-100}{100}=0.75\%
> $$
>
> $$
> r_{\text{annual}}=(1.0075)^{365/90}-1=3.08\%
> $$
>
> Explanation: The actual 90-day return is tiny, but annualization asks what one full year would look like if that growth rate repeated on the same compounding basis.

> [!question] ANNUALIZED RETURN: MORE THAN ONE YEAR
> Problem: An investor buys a **500-day** government bill for **USD 970** and redeems it for **USD 1,000**. Find the annualized return.
>
> ---
>
> Solution:
>
> $$
> \mathrm{HPR}=\frac{1000-970}{970}=3.0928\%
> $$
>
> $$
> r_{\text{annual}}=(1.030928)^{365/500}-1=2.25\%
> $$
>
> Explanation: The raw 500-day return is about **3.09%**, but the annualized rate is lower because that gain was earned over more than one year.

22. Continuously compounded return looks scary only because of the logarithm. In plain English, it is the return quoted on the limiting basis where compounding happens continuously instead of monthly or daily.

$$
r_{cc}=\ln(1+\mathrm{HPR})=\ln\left(\frac{V_1}{V_0}\right)
$$

23. The big reason this measure matters is additivity. Continuously compounded returns across adjacent periods can be added directly.

> [!question] CONTINUOUSLY COMPOUNDED RETURN
> Problem: A stock is bought for **USD 100** and sold one year later for **USD 120**. Find the continuously compounded annual return.
>
> ---
>
> Solution:
>
> $$
> r_{cc}=\ln\left(\frac{120}{100}\right)=\ln(1.20)=18.23\%
> $$
>
> Explanation: The ordinary holding period return is **20%**, but the continuously compounded equivalent is **18.23%**.

24. Gross return is what the portfolio earns before management and administration fees. Net return is what remains after those fees are deducted. Trading commissions and other direct trading costs are already baked into both because those costs are necessary to generate the return in the first place.

25. Pretax nominal return is the percentage return before taxes. After-tax nominal return is what remains after the tax bill. Real return asks the only question that actually matters to your lifestyle: "How much did my purchasing power grow?"

> [!question] REAL RETURN
> Problem: An investor earns a **7%** nominal return while inflation is **2%**. Find the exact real return.
>
> ---
>
> Solution:
>
> $$
> r_{\text{real}}=\frac{1.07}{1.02}-1=4.90\%
> $$
>
> Explanation: The shortcut says about **5%**, but the exact purchasing-power gain is slightly lower because inflation also compounds.

26. Leveraged return means you are earning the asset return on a position that is partly funded with borrowed money. That is why leverage can make you look brilliant in good times and stupid in bad times.

$$
r_L=r+\frac{V_B}{V_C}(r-r_B)
$$

Symbol intuition: $r$ is the asset return, $V_B$ is borrowed capital, $V_C$ is your own cash capital, and $r_B$ is the borrowing rate.

> [!question] LEVERAGED RETURN
> Problem: A fund invests **USD 100 million** of its own capital, borrows **USD 50 million** at **4%**, and earns **8%** on the full asset position. Find the leveraged return on the fund's own capital.
>
> ---
>
> Solution:
>
> $$
> r_L=8\%+\frac{50}{100}(8\%-4\%)=10\%
> $$
>
> Explanation: The fund earns an extra **4% spread** on borrowed money equal to half of its own capital, so leverage adds **2%** on top of the unleveraged **8%** return.

27. The exam logic here is simple: leverage helps only when asset return is above borrowing cost. If asset return falls below borrowing cost, leverage makes the loss worse. ==Leverage is not a new return source. It is just a return amplifier.==

> [!tip] QUICK CHECKS
> - If periods are not annual, separate "geometric mean per period" from "annualized return."
> - If the question is about manager skill, your default answer is usually time-weighted return.
> - If the question is about investor experience with actual deposits and withdrawals, look hard at money-weighted return.
> - If you see inflation, ask whether the examiner wants nominal return or real return.
> - If leverage is present, compare asset return with borrowing cost before doing anything else.

### MODULE 6.1: LOGNORMAL DISTRIBUTIONS AND SIMULATION TECHNIQUES

1. **Log-Normal Distribution**
	1. If $\log(x)$ is normal, the $x$ is log normal. If $x$ is normal, then $e^x$ is log-normal. 
	2. Imagine **many parallel universes** starting today with the same initial price $P_0$. In each universe, the asset earns **continuously compounded (log) returns** over time. By definition of continuous compounding:$$ P_T = P_0 e^{r_{0,T}} $$where $r_{0,T}$ is the total log-return from 0 to $T$.
	3. These log-returns $r_{0,T}$ are independent (or wedakly dependent) and identically distributed. Because log-returns **add**:  $$  r_{0,T} = \sum_{i=1}^n r_i $$By the **Central Limit Theorem**, the sum $r_{0,T}$ is approximately **normally distributed**.
	4. Since $\log P_T = \log P_0 + r_{0,T}$ is normal, $P_T$ is log-normally distributed** (not normal).

2. **Monte Carlo Simulation**
	 - Monte Carlo lets you test **scenarios that never happened**.  Example: Simulate a −40% equity crash even if history only saw −20%. Inputs are **not limited by past data ranges**. Example: Assume 80% volatility even if historical max was 35%.
	 - Results are **only as good as the assumptions**. Example: Assume normal returns ⟶ underestimate crash risk.
	 - Wrong assumptions give **precise but wrong answers**. Example: Simulation outputs USD 12.40, but real market price is USD 20 due to fat tails.
	 * Monte Carlo is **statistical, not analytic**. You get a price but no formula. It gives outcomes, **not intuition**. Example: You know the option value but not why it reacts strongly to volatility.
3. **Resampling and Bootstrapping:**
	- Start with n observed data points. Example: 250 daily returns.
	- For one bootstrap sample, do this: Randomly pick one return at a time from the original 250. Put it back after picking (sampling _with replacement_). Repeat until you have **250 picks**
	- Result is: Some days appear multiple times. Some days don't appear at all. Total observations = still 250. Repeat this process many times (e.g., 10,000 bootstrap samples).
	- From 250 returns, bootstrapping shows the mean return is 8%, but with a wide spread (spread comes from 10k generated samples) ⟶ you see how unreliable that estimate is.
	- Instead of assuming normal returns, you reuse actual ugly days (crashes, spikes) exactly as they occurred. Even with small data, you can still quantify risk around estimates.
    
### MODULE 7.1: SAMPLING TECHNIQUES AND THE CENTRAL LIMIT THEOREM
1. Probability sampling: “Everyone had a ticket in the lottery.” Randomly selecting 500 firms from 10,000 gives each firm a 5% selection chance, making the sample's average profitability an unbiased estimate of the population mean. This is probability sampling.
2. Non-probability sampling: “I picked whoever was easiest to reach.” Studying only easy-to-access or familiar firms (glossy reporters, followed companies, local firms) skews results because the sample is biased and not representative of the population. One way to form an approximately random sample is **systematic sampling** selecting every nth member from a population.
3. **Stratified sampling (Probability Sampling Method)** divides a heterogeneous population into homogeneous groups based on key characteristics and randomly samples from each group in proportion to its size. Eg: Estimating national income by first grouping people into income brackets (low, middle, high) and then randomly sampling individuals from each bracket in proportion to their population share.
4. One of the most important examples is of a bond index is replicated by grouping bonds by maturity and coupon, then randomly selecting bonds from each group in proportion to the group's weight in the index.
5. **Cluster sampling (Probability Sampling Method)** means randomly picking a few groups that are assumed to look like the whole population and then collecting data from those groups instead of everyone. Eg: To estimate average student height in a city, randomly pick a few schools and measure all (or some) students in those schools instead of sampling from every school.
6. One-stage cluster sampling means randomly selecting a few clusters and including **every observation inside those clusters** in the sample. Eg: To estimate city electricity usage, randomly pick a few apartment buildings and use the electricity data of all households in those buildings.
7. Two-stage cluster sampling means randomly selecting a few clusters first (stage 1) and then randomly sampling individuals within each selected cluster (stage 2). To estimate city income, randomly pick a few neighborhoods and then randomly survey a sample of households within each selected neighborhood.
8. Two-stage cluster sampling can be expected to have greater sampling error than one-stage cluster sampling because you have done stuff randomly twice. But it costs less.
9. The non probability methods are Convenience Sampling and Judgemental Sampling. Convenience sampling refers to selecting sample data based on ease of access, using data that are readily available. Judgemental sampling refers to samples for which each observation is selected from a larger dataset by the researcher, based on one's experience and judgement.
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


> [!question] Basics — One-Sample Mean Test  
> **Problem**  
> An analyst suspects that, in the most recent year, excess returns on stocks have fallen below **5%**. She wants to test whether excess returns are **less than 5%**. Let the population mean be denoted by $\mu$.
>
> **Hypotheses**  
> $$
> H_0:\ \mu \ge 0.05
> \qquad
> H_A:\ \mu < 0.05
>$$
>
> **Appropriate Test**  
> One-sample, **left-tailed t-test** (population variance unknown).
>
> **Significance and Confidence**  
> Significance level: $\alpha = 5\%$  
> Confidence level: $1-\alpha = 95\%$
>
> **Test Statistic**  
> $$
> t = \frac{\bar X - 0.05}{s / \sqrt{n}}, \quad \text{df} = n-1
>$$
>
> **Decision Rule**  
> Reject $H_0$ if  
> $$
> t < -t_{\alpha,\,n-1}
>$$
> (left-tail rejection region).


> [!Question] Basics - Difference between Means
> Sue Smith is investigating whether the abnormal returns for acquiring firms during merger announcement periods differ for horizontal and vertical mergers. She estimates the abnormal returns for a sample of acquiring firms associated with horizontal mergers and a sample of acquiring firms involved in vertical mergers. Smith finds that abnormal returns from horizontal mergers have a **mean of 1.0%** and a **standard deviation of 1.0%**, while abnormal returns from vertical mergers have a **mean of 2.5%** and a **standard deviation of 2.0%**. Smith assumes the samples are independent, the population means are normally distributed, and the population variances are equal. Smith calculates the **t-statistic as −5.474** and the **degrees of freedom as 120**. Using a 5% significance level, should Smith reject or fail to reject the null hypothesis that the abnormal returns to acquiring firms during the announcement period are the same for horizontal and vertical mergers?
> 
> **Hypotheses**
> > $$H_0: \mu_H - \mu_V = 0 \qquad H_A: \mu_H - \mu_V \neq 0$$
> 
> **Appropriate Test**
> t-test for independent population with known variance
> 
> **Test Statistic**
> -5.474
> 
> **Decision Rule**
> Reject if: $$ |t| > t_{0.975,\ 120}$$
> $t_{0.975,\ 120} = 1.979$
> 
> Hence $H_0$ is rejected


> [!QUESTION] Basics - Difference between Means
> Joe Andrews is examining changes in estimated betas for the common stock of companies in the telecommunications industry before and after deregulation. Andrews believes the betas may decline because of deregulation, because companies are no longer subject to the uncertainties of rate regulation—or that they may increase because there is more uncertainty regarding competition in the industry. Andrews calculates a t-statistic of 10.26 for this hypothesis test, based on a sample size of 39. Using a 5% significance level, determine whether there is a change in betas.




> [!question] One-tailed vs Two-tailed Test Selection  
> A manager tests whether a portfolio’s mean monthly return is **greater than 1%** using a **one-tailed test at the 5% significance level**. After observing that the sample mean is **below 1%**, she decides to **switch to a two-tailed test** at the same significance level and reassess the result.  
>  
> Is this procedure statistically valid? State the **correct decision rule** and identify **which hypothesis test must be used**.

> [!question] Pooled vs Unpooled Variance Decision  
> Two **independent samples** of returns have **unknown variances**. Sample A has $n_1 = 18$, Sample B has $n_2 = 22$. The analyst assumes **equal variances** and applies a **pooled t-test**, even though the sample standard deviations differ materially.  
>  
> At the **5% significance level**, test whether the population means differ. Identify **whether the test choice is appropriate** and **what error this assumption introduces**.

> [!question] Chi-square Test Tail Direction  
> An analyst tests whether a fund’s **variance is less than 4%** using **24 monthly return observations** at the **5% significance level**. The calculated **chi-square test statistic falls in the rejection region**, but the analyst compares it against the **upper-tail critical value** instead of the **lower-tail critical value**.  
>  
> Should the null hypothesis be rejected? Identify the **exact procedural mistake**.

> [!question] Significance Level vs Confidence Level  
> A researcher states that using a **1% significance level** means she is **99% confident that the null hypothesis is false** if it is rejected.  
>  
> Is this interpretation correct? Restate the **correct probabilistic meaning** of the significance level and confidence level.

> [!question] Type I vs Type II Error Interpretation  
> An analyst designs a hypothesis test with a **very low significance level** to avoid false positives. As a result, the test rarely rejects the null hypothesis.  
>  
> Identify how this choice affects the **probability of a Type II error** and the **power of the test**.
