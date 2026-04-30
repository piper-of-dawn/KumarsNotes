

> [!ABSTRACT] LOS
> 1. Describe the performance appraisal of alternative investments.
> 2. Calculate and interpret alternative investment returns both before and after fees.

> [!tip] SEE THIS BEFORE EXAM
> This module is not “alternatives are illiquid” theory. It is a return-calculation trap module.
>
> Memorize these:
>
> $$
> \text{MOIC}=\frac{\text{Realized value}+\text{Unrealized value}}{\text{Total invested capital}}
> $$
>
> $$
> r_L=r+\frac{V_b}{V_c}(r-r_b)
> $$
>
> $$
> R_{GP}=(P_1 \times r_m)+\max[0,(P_1-P_0)\times p]
> $$
>
> $$
> r_i=\frac{P_1-P_0-R_{GP}}{P_0}
> $$
>
> One-line hammer: **IRR cares about timing. MOIC ignores timing. Leverage magnifies. Level 3 smooths. Fees decide what the investor actually keeps.**

#### Core Flow

1. Alternative investment performance appraisal is harder than public-stock or public-bond appraisal because the cash flows, valuations, leverage, fees, taxes, and investor terms are not standardized.
2. Public securities are easier to compare because they have quoted prices, similar claims, regular cash flows, and broad benchmarks. Alternative investments are customized, so two investors in the same hedge fund can earn different net returns if they entered at different times or negotiated different fee terms.
3. The four big appraisal complications are the investment life cycle, borrowed funds, valuation, and fee structure. Higher fees alone are not the main point; **complex fee arrangements** are the main point.
4. Alternative returns are often less normally distributed than traditional returns. Do not blindly trust average return and standard deviation when the strategy has illiquidity, leverage, and ugly left-tail events.
5. The alternative investment life cycle usually has three phases: capital commitment, capital deployment, and capital distribution. Capital commitment means investors promise money; capital deployment means the manager actually puts it to work; capital distribution means cash comes back from income, exits, sales, or liquidations.
6. Early returns are often negative because fees and expenses start before assets produce income. During deployment, cash outflows usually exceed inflows. During distribution, successful assets finally generate cash or are sold.
7. The J-curve means returns first dip negative, then accelerate, then level off as assets are distributed and the fund closes. Memorize it as: **fees first, work second, harvest last**.

> [!warning] REAL WORLD: THE J-CURVE IS WHY IMPATIENT MONEY PANICS
> A private equity fund buys a boring packaging company. Year 1 looks bad because legal fees, consultants, debt costs, and restructuring expenses hit immediately. Year 4 may look good only if operations improve. Year 7 may look excellent if the company is sold at a high price.
>
> A public stock investor sees a price every second. A private equity investor may stare at ugly early cash flows for years before the payoff appears. The pain arrives on schedule; the glory is optional.

8. Internal rate of return, or IRR, is the preferred measure for many long-lived alternatives because it considers both the amount and timing of cash flows.
9. What is internal rate of return: the discount rate that makes the present value of all cash inflows and outflows equal to zero.
10. Why IRR is used: the private equity or real estate manager controls when capital is called and when proceeds are distributed, so timing is part of performance.
11. IRR is useful but not innocent. It requires assumptions about the financing rate for outgoing cash flows and the reinvestment rate for incoming cash flows.
12. Multiple of invested capital, or MOIC, is a shortcut money multiple. It tells you how many times invested capital came back, but it ignores timing.
13. Total invested capital means paid-in capital less management fees and fund expenses.
14. MOIC formula:

$$
\text{MOIC}=\frac{\text{Realized value of investment}+\text{Unrealized value of investment}}{\text{Total invested capital}}
$$

15. Realized value means value already received from exits, sales, or distributions. Unrealized value means value still sitting inside the fund.
16. Source-style MOIC numerical:
    Problem: A fund has paid-in capital of **€750 million**, pays **2%** annual management fees for **5 years**, distributes **€1,000 million**, and still owns assets worth **€500 million**.
    Solution:
    Management fees are:

$$
750 \times 2\% \times 5=75
$$

17. Total invested capital is:

$$
750-75=675
$$

18. MOIC is:

$$
\frac{1{,}000+500}{675}=2.22\times
$$

19. Explanation: the fund turned **€675 million** of actual invested capital into **€1,500 million** of realized plus unrealized value. The timing of those cash flows is invisible inside MOIC.

> [!tip] IRR VS MOIC
> If two funds both show **2.0x MOIC**, ask: “How long did it take?”
>
> Fund A doubles money in **3 years**. Fund B doubles money in **10 years**. The money multiple is identical, but Fund A is better because the capital came back faster. That is why IRR exists.

20. Leverage means using borrowed money or derivatives to take a larger market position than the investor’s own capital would allow.
21. Leverage magnifies both gains and losses because the asset return is earned on the full position, while the investor’s own capital absorbs the residual result after borrowing cost.
22. Leveraged return formula:

$$
r_L=\frac{r(V_c+V_b)-(V_b \times r_b)}{V_c}
$$

23. Shortcut formula:

$$
r_L=r+\frac{V_b}{V_c}(r-r_b)
$$

24. Notation in simple language: $r_L$ is leveraged return, $r$ is underlying asset return, $V_c$ is investor cash capital, $V_b$ is borrowed capital, and $r_b$ is borrowing rate.
25. The whole formula lives inside $r-r_b$. If the asset return is above the borrowing rate, leverage helps. If the asset return is below the borrowing rate, leverage hurts.
26. Source-style leverage numerical:
    Problem: Lupulus has **USD 100 million** of capital and borrows **USD 50 million** at **4%**. If the underlying position earns **8%**, calculate leveraged return.
    Solution:

$$
8\%+\frac{50}{100}(8\%-4\%)=10\%
$$

27. If the underlying position loses **2%**, leveraged return is:

$$
-2\%+\frac{50}{100}(-2\%-4\%)=-5\%
$$

28. If the underlying position earns **6%**, the breakeven borrowing rate is **6%** because leverage adds nothing when $r_b=r$.

> [!danger] SCANDAL MEMORY HOOK: LEVERAGE LOOKS LIKE GENIUS UNTIL THE BILL ARRIVES
> A hedge fund earning **8%** on assets while borrowing at **4%** looks clever. Add enough borrowed money, and the investor return looks juiced.
>
> If the asset return flips to **-2%**, the same machine becomes brutal. The loan still charges interest, the margin account shrinks, and the broker can demand more collateral.

29. A margin account represents the hedge fund’s net equity in its financed positions. A margin call happens when the equity or collateral falls below the required level and the lender demands more collateral.
30. Margin calls can lock in losses because the fund may be forced to sell losing positions at bad prices, especially if the sale itself pushes the market price lower.
31. Valuation is difficult because many alternative assets are illiquid and do not have clean market prices.
32. Fair value is the market-based price that market participants would use to exchange an asset or liability in an orderly transaction at the measurement date. The seller’s version is often called the exit price.
33. Fair value Level 1 means quoted prices in active markets for identical assets, such as a listed public stock’s closing price.
34. Fair value Level 2 means observable inputs other than Level 1 quoted prices, such as an over-the-counter interest rate derivative priced using observable market data.
35. Fair value Level 3 means unobservable inputs, usually for assets with little or no market activity, such as private equity or real estate valued through cash-flow projection models.
36. Mark-to-model valuation means the value comes from a model rather than a live market price. Models should be independently tested, benchmarked, and calibrated because the manager may have a conflict of interest.
37. Exam trap: Level 3 values can smooth or overstate returns and understate volatility and risk. The asset is not necessarily safer; it may simply be marked less directly.

> [!warning] REAL WORLD: LEVEL 3 MARKS CAN MAKE A BURNING ROOM LOOK CALM
> A public real estate stock can fall **20%** in a week because the market price moves every second. A private office building might still sit near old carrying value because no sale has happened yet and the model changes slowly.
>
> That does not mean the building is stable. It may mean the thermometer is slow. Level 3 valuation can hide volatility until a financing round, impairment, sale, or forced liquidation reveals the real price.

38. Gross return is what the fund earns before fees. Net return is what the investor keeps after fees.
39. A management fee is a fixed fee, often based on assets under management or end-of-period value. A performance fee is based on investment gains, often above a hurdle or high-water mark.
40. Different investors in the same fund can face different net returns because of larger commitments, earlier entry, founder share classes, side terms, high-water marks, or longer lockups.
41. Founders shares are lower-fee shares offered to early investors in a new fund. Example: **1.5%** management fee and **10%** performance fee instead of **2%** and **20%**.
42. Either/or fees let the manager take either a management fee or an incentive fee, whichever is higher. A large institution may negotiate **1%** management fee or **30%** incentive fee above a hurdle, whichever is greater.
43. Redemption fee discourages withdrawals and helps offset transaction costs. Notice period is advance warning before redemption, often **30 to 90 days**. Lockup period is the minimum holding period before withdrawal. A gate limits redemptions for a period.

> [!danger] REAL WORLD: THE EXIT DOOR CAN BECOME A VIP ROPE LINE
> During stress, everyone wants liquidity at the same time. A fund holding private loans, real estate, or complex hedge fund positions cannot sell everything politely by Friday.
>
> Redemption fees, notice periods, lockups, and gates protect the strategy and remaining investors, but they also mean your “investment value” and your “cash in hand” are not the same thing.

44. Basic general partner fee formula when management and performance fees are calculated independently:

$$
R_{GP}=(P_1 \times r_m)+\max[0,(P_1-P_0)\times p]
$$

45. Investor return after fees:

$$
r_i=\frac{P_1-P_0-R_{GP}}{P_0}
$$

46. Notation in simple language: $R_{GP}$ is total manager fee, $P_0$ is beginning fund value, $P_1$ is ending fund value before fees, $r_m$ is management fee rate, $p$ is performance fee rate, and $r_i$ is investor net return.
47. Source-style Kettleside numerical:
    Problem: Beginning value is **USD 100 million**, ending value is **USD 130 million**, management fee is **1%** of year-end assets, and performance fee is **20%**. If fees are independent, calculate manager fees and investor net return.
    Solution:

$$
R_{GP}=130 \times 1\%+(130-100)\times 20\%=7.3
$$

$$
r_i=\frac{130-100-7.3}{100}=22.7\%
$$

48. If performance fee is calculated net of management fee, the formula becomes:

$$
R_{GP,\ net}=(P_1 \times r_m)+\max[0,\{P_1(1-r_m)-P_0\}\times p]
$$

49. Using the same facts:

$$
R_{GP,\ net}=130 \times 1\%+\{130(0.99)-100\}\times 20\%=7.04
$$

$$
r_i=\frac{130-100-7.04}{100}=22.96\%
$$

50. Explanation: net-of-management-fee performance fee is slightly better for the investor because the performance-fee base is smaller.
51. A hard hurdle means the performance fee applies only to gains above the hurdle. With a hard hurdle calculated net of management fee:

$$
R_{GP,\ hurdle}=(P_1 \times r_m)+\max[0,\{P_1(1-r_m)-P_0(1+r_h)\}\times p]
$$

52. Same Kettleside facts with a **6%** hard hurdle:

$$
R_{GP,\ hurdle}=130 \times 1\%+\{130(0.99)-100(1.06)\}\times 20\%=5.84
$$

$$
r_i=\frac{130-100-5.84}{100}=24.16\%
$$

53. A high-water mark is the previous peak value of the fund net of fees. It stops the manager from charging performance fees again until the fund exceeds the earlier peak.
54. High-water mark fee formula:

$$
R_{GP,\ HWM}=(P_t \times r_m)+\max[0,(P_t-P_{HWM})\times p]
$$

55. In Kettleside Year 2, fund value falls to **USD 110 million** after Year 1 investor capital had reached **USD 122.7 million** net of fees:

$$
R_{GP,\ HWM}=110 \times 1\%+\max[0,(110-122.7)\times 20\%]=1.1
$$

$$
r_i=\frac{110-122.7-1.1}{122.7}=-11.25\%
$$

56. In Kettleside Year 3, fund value rises to **USD 128 million**. The old investor’s high-water mark is **USD 122.7 million**:

$$
R_{GP,\ HWM}=128 \times 1\%+(128-122.7)\times 20\%=2.34
$$

$$
r_i=\frac{128-108.9-2.34}{108.9}=15.39\%
$$

57. A new investor entering after Year 2 has a personal high-water mark of **USD 108.9 million**, so the Year 3 fee is higher:

$$
R_{GP,\ HWM}=128 \times 1\%+(128-108.9)\times 20\%=5.10
$$

$$
r_i=\frac{128-108.9-5.10}{108.9}=12.86\%
$$

58. Exam trap: the same fund and same gross Year 3 performance produced **15.39%** for the old investor and **12.86%** for the new investor because their high-water marks differed.

> [!danger] SCANDAL MEMORY HOOK: THE NEW INVESTOR PAYS FOR THE COMEBACK PARTY
> Suppose a fund crashes from **USD 130 million** to **USD 110 million**. Old investors are still underwater, so the high-water mark protects them from paying performance fees on a mere recovery.
>
> A new investor who enters at **USD 110 million** does not have that old scar. If the fund rebounds to **USD 128 million**, the new investor may pay incentive fees while old investors pay less.

59. A clawback provision gives limited partners the right to reclaim part of the general partner’s performance fee if later losses reduce aggregate profits.
60. Source-style clawback numerical:
    Problem: One investment gains **USD 12 million**, another later loses **USD 10 million**, and carry is **20%**. Calculate the final carry after clawback.
    Solution:
    The manager may initially accrue **USD 2.4 million** carry:

$$
12 \times 20\%=2.4
$$

61. But aggregate profit after the later loss is only **USD 2 million**, so final carry should be **USD 0.4 million**:

$$
(12-10)\times 20\%=0.4
$$

62. Explanation: **USD 2.0 million** of previously accrued performance fee must be returned to limited partner capital accounts because final carry is only **USD 0.4 million**, not the initially accrued **USD 2.4 million**.
63. Soft hurdle means once the hurdle is met, carried interest can apply to a larger base through a catch-up arrangement. Hard hurdle means carry applies only to the amount above the hurdle.
64. Source hurdle numerical:
    A property is bought for **USD 100 million** and sold after **2 years** for **USD 160 million**, with **8%** annual preferred return and **80/20** split.
65. With a soft hurdle and catch-up, limited partners first receive **USD 100 million** capital back and **USD 16 million** preferred return. The general partner then receives **USD 4 million** catch-up, and the remaining **USD 40 million** is split **80/20**, giving **USD 32 million** to limited partners and **USD 8 million** to the general partner.
66. Total soft-hurdle payout: limited partners receive **USD 148 million** and the general partner receives **USD 12 million**.
67. With a hard hurdle and no catch-up, only the **USD 44 million** above capital plus preferred return is subject to **20%** carry:

$$
44 \times 20\%=8.8
$$

68. Total hard-hurdle payout: limited partners receive **USD 151.2 million** and the general partner receives **USD 8.8 million**. Soft hurdle with catch-up gives the general partner more.
69. Fund-of-funds investing adds another fee layer. Direct hedge fund investment with **20%** gross return and **2 and 20** fees gives:

$$
\text{Management fee}=100 \times 2\%=2
$$

$$
\text{Incentive fee}=20 \times 20\%=4
$$

$$
\text{Investor return}=\frac{20-2-4}{100}=14\%
$$

70. If the investor uses a fund of funds that earns **14%** after underlying hedge fund fees and then charges **1 and 10**, investor return becomes:

$$
\frac{14-1-(14 \times 10\%)}{100}=11.6\%
$$

71. Fund of funds may still make sense if it provides due diligence, diversification, manager access, or access to a closed hedge fund. But the double-fee drag is real.
72. Relative performance needs benchmarks, but alternative benchmarks are dangerous if the peer group is not comparable.
73. Private equity and real estate comparisons are better when investments are from the same vintage year. Vintage year means the year a fund starts its investment life, so funds are compared at similar life-cycle stages.
74. A mature private equity fund harvesting exits should not be lazily compared with a new fund still paying fees and deploying capital.
75. Hedge fund indexes have special bias problems because funds self-report, fail, close, or selectively join databases.
76. Survivorship bias happens when failed funds are excluded from the index, making average reported returns look too good.
77. Backfill bias happens when successful funds join an index later and add their good past returns to the database.
78. Both survivorship bias and backfill bias create upward bias in hedge fund indexes.

> [!warning] SCANDAL MEMORY HOOK: THE INDEX MAY BE A BEAUTY PAGEANT OF SURVIVORS
> Imagine a coaching center advertises only the students who cracked the exam and quietly removes everyone who failed. Then it adds the past mock scores of its toppers after discovering they were toppers.
>
> That is survivorship bias plus backfill bias. Hedge fund indexes can look cleaner than the actual set of funds investors had to choose from in real time.

> [!tip] FINAL QUICK CHECKS
> IRR cares about timing. MOIC ignores timing.
>
> Leverage helps only when $r>r_b$. It hurts when $r<r_b$.
>
> Level 3 values can smooth returns and understate volatility.
>
> Management fee can still be charged in a bad year. Performance fee usually needs gains above the relevant hurdle or high-water mark.
>
> Hard hurdle pays carry only above the hurdle. Soft hurdle with catch-up can pay carry on a larger amount.
>
> Old and new investors in the same fund can have different high-water marks and therefore different net returns.
>
> Survivorship bias plus backfill bias usually makes hedge fund indexes look too good.
