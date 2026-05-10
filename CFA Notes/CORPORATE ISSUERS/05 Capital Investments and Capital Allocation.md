###### LOS 24.a: Describe types of capital investments.
###### LOS 24.b: Describe the capital allocation process, calculate net present value (NPV), internal rate of return (IRR), and return on invested capital (ROIC), and contrast their use in capital allocation.

> [!tip] LOOK AT THESE BEFORE EXAM
> - Capital projects are long-term investments whose cash flows usually stretch beyond one year.
> - Four buckets: going concern, regulatory or compliance, expansion of existing business, and new lines of business or other.
> - Capital Allocation Process: **ideas first, analysis and numbers second, ranking and prioritization third, monitoring and review last. NPV and IRR live in investment analysis; discipline lives in monitoring.**
> - **Accept if NPV is at least 0. Accept if IRR is at least the required rate of return.**
> - If two projects are mutually exclusive, meaning I can choose only one, do not blindly choose the higher IRR. Project A adds 100 of value with a 15 percent IRR. Project B adds 20 of value with a 40 percent IRR. Choose Project A. **NPV tells wealth added; IRR tells percentage return; when they fight, NPV wins.**
> - NPV re-invests at required rate of return and IRR re-invests at IRR itself.
> - NPV uses after-tax cash flows discounted at the required rate of return. IRR is the discount rate that forces NPV to 0.
> - ROIC is the company-wide return on invested capital; numerator is after-tax operating profit, denominator is average long-term debt plus equity ==**(EXCLUDING WORKING CAPITAL)**==, and value is created only when ROIC beats the required return.
> - ROIC can be broken into two moving parts: **margin** and **turnover**.First term: **after-tax operating profit margin**. This means: from every 100 of sales, how much operating profit does the company keep after tax? If sales are 100 and after-tax operating profit is 15, margin is 15 percent.
> - Second term: **capital turnover**. This means: how much sales does the company generate from the capital invested in the business? If invested capital is 200 and sales are 400, capital turnover is 2 times.
> - Now combine them. Margin is 15 percent. Capital turnover is 2 times. ROIC becomes 30 percent.
> - The intuition is simple: a company can create high ROIC in two ways. One, it can keep a lot of profit from each sale. That is the **high-margin route**. Two, it can sell a lot using very little capital. That is the **high-turnover route**.
> - **ROIC is useful because analysts can calculate it, ==but it is backward-looking, accounting-based, aggregated, and adjustment-sensitive.==**
> - Remember, if the cash flow would anyway occur whether the project is accepted or not then that never enters the cash flow stream while NPV and IRR calculation. This could maybe be sunk cost on research about the project.
> - **A project costs EUR 50 million today and returns EUR 16 million for four years plus EUR 20 million in Year 5 at 10%. Find NPV.** Quick algorithm: discount each after-tax inflow, total them to EUR 63.136 million, subtract EUR 50 million, and get **EUR 13.136 million**.
> - **Using the same cash flows, find IRR.** Quick algorithm: set NPV to 0 and solve with the IRR function; the answer is **19.52%**, so it clears a 10% hurdle rate.
> - **After-tax operating profit is 24,395 and average invested capital is the average of long-term liabilities plus equity across two years. Find ROIC.** Quick algorithm: divide 24,395 by average invested capital and get **8.73%**.
> - Big gotcha: IRR quietly assumes interim cash flows are reinvested at the IRR itself; NPV assumes reinvestment at the required rate of return.
> - Big gotcha: if cash-flow signs change more than once, IRR can give multiple answers; in that case trust NPV.
> - Quick check: NPV is in currency, IRR is in percent, and ROIC is historical and accounting-based.

> [!abstract] MEMORISE
> $$
> \text{NPV} = \sum_{t=0}^{T} \frac{CF_t}{(1+r)^t}
> $$
>
> $$
> \sum_{t=0}^{T} \frac{CF_t}{(1+\text{IRR})^t} = 0
> $$
>
> $$
> \text{ROIC} = \frac{\text{After-tax operating profit}}{\text{Average invested capital}}
> $$
>
> $$
> \text{ROIC} = \text{After-tax operating profit margin} \times \text{Capital turnover}
> $$
>
> Notation in simple language:
> - $CF_t$: after-tax cash flow at time $t$
> - $r$: required rate of return on a similarly risky investment
> - Average invested capital: average of long-term liabilities and equity

70. Capital investments, also called capital projects, are investments with a life of one year or longer. What is a capital project: a long-lived business investment whose cash flows arrive over time, not just this year.
71. The first accounting thing to remember is that the spending usually lands on the balance sheet first as a long-term asset. Later, the cost is spread over time through depreciation or amortization.
72. Why is that spreading done: because the asset helps the business over several periods, so accounting tries to match cost with the years receiving the benefit.
73. On the cash flow statement, the cash spending is shown when it happens. On the balance sheet later, the asset sits at cost minus accumulated depreciation or amortization.
74. Do not think capital investment means only factories and machines. The source is explicit that digital capabilities and other intangible assets can also be capital investments.
75. Analysts care about capital investment because it reveals how management is trying to create value. You are basically watching where the company is placing its long-term bets.

##### TYPES OF CAPITAL INVESTMENTS

7. Capital investments are long-term investments. Think: the company spends money today, and the benefit comes over many years. The exam wants you to classify **why** the company is spending.

8. First bucket: **going concern or maintenance projects**. These keep the current business running. Replacing old machines, upgrading existing IT, maintaining facilities, improving efficiency. These are usually lower risk because the company already understands the business. **A common exam trap: maintenance capex is often estimated using depreciation and amortization, but this is only an estimate, not a required disclosure.**
9. These projects are usually easier to evaluate because management already understands the existing business. The company is not jumping into the dark; it is mostly repeating something it already runs.
10. Match funding matters here. What is match funding: financing a long-term asset with financing that lasts about as long as the asset's useful life Why is match funding used: it reduces financing risk because the firm is less likely to face a refinancing problem before the asset has finished generating benefits.
11. Think of it like this: if the asset pays you back slowly over 30 years but your debt comes due in 2 years, the project can still be good and yet your financing can blow up.
12. Second bucket: **regulatory or compliance projects**. These are done because a law, regulator, safety rule, or compliance standard forces the company to act. ==They may add cost without adding revenue. Exam trap: these projects may still be accepted even with negative NPV because not doing them could mean fines, shutdown, or loss of license==.
13. The tricky part is that even costly compliance projects can create strategic value. Tough rules can become barriers to entry that protect incumbents from weaker competitors. **==A good example is that if I want to start a bank tomorrow I can't do it because regulations around starting a banking firm is humongous.==**

> [!example] DANSKE BANK AND THE PRICE OF NEGLECT
> Danske Bank's anti-money-laundering failures were not some sleepy back-office issue. Weak controls, governance failures, resignations, branch closure, arrests, and the threat of billions in fines turned compliance into a story about survival.
>
> Compliance spending may feel painful up front, but the bill for ignoring it can be far uglier and far more public.
7. Firms with stronger financial flexibility may adopt new rules early. Why is early adoption used: it can reduce uncertainty, attract customers, and create an edge over slower rivals.
8. Once compliance costs rise, management must ask a brutal question: does this business still clear the minimum required return after those extra costs are included?
9. Third bucket: **expansion of existing business**. Here the company grows what it already knows: more stores, more capacity, new region, adjacent product, acquisition within the core business. Risk is higher than maintenance because execution can fail.
10. Younger firms often fund expansion mostly with equity because the risk is high and cash flows are less established. More proven firms may use debt once investors trust the expansion playbook.
11. Expanding scope can look smart because it reuses existing capabilities for a different customer base. The hidden danger is complexity: more business lines and more competitors can make execution messy.4

> [!example] SONY PUSHES PLAY HARDER
> Sony did not buy Bungie just to own another logo. It moved to deepen live game services and reach more players through a business it already understood.
>
> That is what expansion of existing business feels like in real life: not survival spending, but a deliberate push to widen the moat around the core engine.


7. Fourth bucket: **new lines of business and other projects**. This is the riskiest bucket. The company enters something unfamiliar, invests in a new technology, or buys a business outside its core.
8. These projects often look like startup bets inside a mature company. Management may be exploring a new technology, a new business model, or a sector it does not yet understand well.
9. The major risks are unfamiliar operations and overpaying. You can hear the warning in the source: new growth stories are exciting, but the business may be strange territory.

> [!example] KIRIN WALKS OUT OF ITS OLD LANE
> Kirin was already a giant beverage name in Japan, then it invested heavily in Fancl, a cosmetics and dietary supplement company. This was not just "more of the same"; it was a move into a different market with new habits, customers, and execution risk.
>
> That is why this bucket carries the highest danger. The dream can be huge, but the map is unfamiliar.

> [!warning] REMEMBER
> A maintenance project that cuts costs can still be a going concern project. The key idea is not glamour; the key idea is preserving and improving the current business.



10. Analysts should examine both the level and trend of expansion capital spending. Why is this done: it helps judge growth prospects, management priorities, and whether returns look sensible relative to alternatives.
11. A rough estimate of expansion capital spending can be made by taking total capital expenditures and subtracting estimated maintenance spending. The source says maintenance spending is often approximated by depreciation and amortization.

##### CAPITAL ALLOCATION PROCESS

32. Capital allocation is the process management and the board use to make capital investment and return decisions. What is capital allocation: deciding where the firm's scarce capital should go.
33. The core goal is not just "find a profitable project." The goal is to earn risk-adjusted returns greater than investors could earn elsewhere on similarly risky opportunities.
34. The source says this process resembles investment portfolio construction, but with more granular detail and more proprietary, non-public information.
35. Step one is idea generation. Good ideas can come from anywhere, but management needs a strong grip on the competitive environment, current operations, capabilities, and positioning.
36. Step two is investment analysis. How is investment analysis done: forecast the amount, timing, duration, and volatility of expected cash flows, then test whether the project is a wise use of capital. ==This is where **NPV and IRR are calculated**. If CFA asks, “In which step are NPV and IRR most likely used?” answer: investment analysis.==
37. Step three is planning and prioritization. Management now chooses the mix of projects that creates the most value on a risk-adjusted basis, not just the projects that look attractive one by one.
38. This is where many students make the beginner mistake. A project can look fine in isolation and still lose when compared with other projects, existing operations, or financing constraints.
39. When value-creating opportunities are exhausted, the CFA curriculum says remaining capital should be returned to shareholders. If management cannot beat the shareholders' outside opportunities, it should stop pretending.
40. Step four is monitoring and post-investment review. Why is this done: to test assumptions, expose systematic errors, enforce discipline, and generate better future ideas.
41. Post-investment review also helps management scale up strong areas and scale down weak areas. **That feedback loop is part of the capital allocation process, not an optional afterthought.**

##### NET PRESENT VALUE

42. Net present value, or NPV, is the present value of expected future cash inflows minus the investment's costs. What is present value: today's value of future cash after discounting for time and risk.
43. The required rate of return is the rate investors could earn on a similarly risky investment. Why is it used: it captures opportunity cost, so a project must beat real alternatives, not a fantasy hurdle.
44. NPV is measured in currency, not in percent. That matters because NPV tells you how much shareholder wealth the project adds or destroys in money terms.
45. If NPV is positive, the project increases wealth. If NPV is negative, it destroys wealth. If NPV is exactly zero, it barely clears the hurdle and leaves no room for forecast error.
46. The decision rule is straightforward: invest if NPV is at least 0. **==The curriculum still warns that this is usually necessary but not always sufficient because other strategic considerations can matter.==**
47. Unconventional cash-flow patterns matter. What is an unconventional cash-flow pattern: a pattern where the sign of cash flows changes more than once instead of only once.
48. A project can require more spending after inception, not just at time 0. In those cases, you still use NPV, but the timing of each cash flow has to be handled carefully.

> [!question] NPV NUMERICAL
> Problem: Gerhardt Corporation pays EUR 50 million today and expects after-tax cash inflows of EUR 16 million in Years 1 to 4 and EUR 20 million in Year 5. Required rate of return is 10%. Find NPV.
>
> Solution: Discount each inflow at 10%, add the present values to get EUR 63.136 million, then subtract the EUR 50 million outlay.
>
> $$
> \text{NPV} = -50 + \frac{16}{1.10} + \frac{16}{1.10^2} + \frac{16}{1.10^3} + \frac{16}{1.10^4} + \frac{20}{1.10^5} = 13.136
> $$
>
> Explanation: The project adds EUR 13.136 million of present value, so it should be accepted.

49. For unevenly spaced cash flows, the source points to tools like XNPV because ordinary NPV functions assume evenly spaced periods and treat the first listed cash flow as time 1.
##### INTERNAL RATE OF RETURN

51. Internal rate of return, or IRR, is the discount rate that makes NPV equal to zero. What is IRR: the break-even rate of return implied by the project's own cash flows.
52. The decision rule is to invest if IRR is at least the required rate of return. This is why the required rate of return is often called the hurdle rate.
53. Students love IRR because it feels intuitive as a percentage. The curriculum still says NPV is the more theoretically sound criterion.
54. **==The key hidden assumption is reinvestment. Why is IRR tricky: it assumes interim cash flows are reinvested at the IRR itself, which may be unrealistic.==**
55. NPV instead assumes reinvestment at the required rate of return. The source calls that assumption more economically realistic in many cases.

> [!warning] REINVESTMENT TRAP
> ==**Under IRR, interim cash flows are assumed to earn the IRR. Under NPV, interim cash flows are assumed to earn the required rate of return.**== That single difference is an exam favorite.

> [!question] IRR NUMERICAL
> Problem: Use the same Gerhardt cash flows of EUR 50 million today, EUR 16 million in Years 1 to 4, and EUR 20 million in Year 5. Find IRR.
>
> Solution: Solve for the discount rate that makes NPV equal to 0.
>
> $$
> 0 = -50 + \frac{16}{(1+\text{IRR})} + \frac{16}{(1+\text{IRR})^2} + \frac{16}{(1+\text{IRR})^3} + \frac{16}{(1+\text{IRR})^4} + \frac{20}{(1+\text{IRR})^5}
> $$
>
> Explanation: The answer is **19.52%**. Since 19.52% is above the 10% hurdle rate, the project should be accepted.

56. **If cash flows are not evenly spaced, the source points to XIRR rather than the ordinary IRR function. Again, the issue is timing accuracy.**
57. Multiple IRRs can exist when cash-flow signs change more than once. That is not a minor quirk; it is a direct reason to prefer NPV in such cases.
58. Imagine a project with a negative outlay, then a big positive inflow, then another negative outflow later. That pattern can produce more than one IRR solution.
59. The source gives a simple example with cash flows of -1,000, +5,000, and -6,000 that produces IRRs of 100% and 200%. Same project, two IRRs, so IRR loses credibility there.
60. In mutually exclusive projects, choose the project with the higher NPV, not automatically the higher IRR. IRR tells you rate; NPV tells you wealth added.
61. If two projects are mutually exclusive, meaning I can choose only one, do not blindly choose the higher IRR. Project A adds 100 of value with a 15 percent IRR. Project B adds 20 of value with a 40 percent IRR. Choose Project A. **NPV tells wealth added; IRR tells percentage return; when they fight, NPV wins.**

##### RETURN ON INVESTED CAPITAL

61. **ROIC is the company-wide return on invested capital; numerator is after-tax operating profit, denominator is average long-term debt plus equity (EXCLUDING WORKING CAPITAL), and value is created only when ROIC beats the required return.**
62. External analysts usually cannot audit management's project-level NPV or IRR calculations, because they do not see the granular internal project data.
63. That is why ROIC matters. What is ROIC: a company-wide profitability measure that compares after-tax operating profit with the capital invested in the business.
64. Numerator first. Use **after-tax operating profit**. Not net income. Not EPS. Not cash flow. The focus is operating profit after tax, because we are measuring return from the business operations.
65. Denominator next. Use **average invested capital**. In this module, that means average **long-term liabilities and equity**. Do not include short-term operating liabilities like accounts payable. Do not treat working capital as the main denominator here. **==The CFA curriculum explicitly excludes working capital from this denominator.==**
66. Why is working capital excluded: because the denominator is meant to capture the long-term capital invested in the business.
67. ROIC is valuable because analysts can calculate it from consolidated financial statements. That makes it practical in a way project-level NPV and IRR often are not.
68. ROIC can be broken into two moving parts: **margin** and **turnover**.
69. First term: **after-tax operating profit margin**. This means: from every 100 of sales, how much operating profit does the company keep after tax? If sales are 100 and after-tax operating profit is 15, margin is 15 percent.
70. Second term: **capital turnover**. This means: how much sales does the company generate from the capital invested in the business? If invested capital is 200 and sales are 400, capital turnover is 2 times.
71. Now combine them. Margin is 15 percent. Capital turnover is 2 times. ROIC becomes 30 percent.
72. The intuition is simple: a company can create high ROIC in two ways. One, it can keep a lot of profit from each sale. That is the **high-margin route**. Two, it can sell a lot using very little capital. That is the **high-turnover route**.

> [!question] ROIC NUMERICAL
> Problem: A company reports after-tax operating profit of 24,395 in Year 2. End-of-Year 1 long-term debt, share capital, and retained earnings are 112,257, 15,688, and 148,442. End-of-Year 2 values are 106,597, 15,688, and 159,995. Find ROIC.
>
> Solution: First average invested capital, then divide after-tax operating profit by that average.
>
> $$
> \text{Average invested capital} = \frac{(112,257 + 15,688 + 148,442) + (106,597 + 15,688 + 159,995)}{2}
> $$
>
> $$
> \text{ROIC} = \frac{24,395}{279,333.5} = 8.73\%
> $$
>
> Explanation: The firm earned 8.73% on the long-term capital invested in the business during the year.

73. ROIC can be compared with investors' required rate of return. If ROIC stays above that required return over time, the firm is creating value.
74. If ROIC stays below the required return, investors could have done better elsewhere. **The curriculum says management should then improve margins or turnover, dispose of weak assets, return capital, or find better opportunities.**
75. ROIC should be compared to a required return relevant for both debt and equity investors, not just equity. Equity alone would overstate the benchmark because debt is less risky.
76. **==ROIC is not perfect. It is accounting-based, not cash-based, so operating profit can differ materially from cash flow.==**
77. ROIC is also backward looking and can be volatile year to year. A strong project may take time to show up as an attractive aggregate return.
78. **==Because ROIC is highly aggregated, it can hide ugly business areas inside a decent overall number. Good segments can cover up bad segments, and bad segments can dilute great ones.==**
79. ==One final limitation is measurement disagreement. The curriculum warns that practitioners differ on whether to exclude excess cash, intangible assets, or some long-term liabilities from invested capital.==

#### CAPITAL ALLOCATION PRINCIPLES

80. Before you calculate NPV or IRR, make sure the cash flows are built correctly.”
81. First principle: use **after-tax cash flows**, not accounting profit. Taxes matter because the project creates taxable income, but it also creates tax shields. For example, depreciation is non-cash, but it reduces taxable income, so it increases after-tax cash flow. If CFA says a project has depreciation, do not treat it as cash paid out, but do remember its tax benefit.
82. Second principle: use **incremental cash flows only**. Incremental means: what changes because I accept this project? If the cash flow happens whether I take the project or not, ignore it. **Exclude sunk costs.**

> [!question] EXCLUDE SUNK COSTS
> Suppose a company spent **2 million last year** on a market research report.
> 
> Now the project needs:
> 
> Initial machine cost today: **10 million**
> Expected present value of future after-tax cash flows: **13 million**
> 
> Wrong CFA-student logic:
> “I should include the 2 million research cost, so total cost is 12 million. NPV is 1 million.”
> 
> Correct logic:
> The 2 million is already gone whether I accept or reject the project. So it is a **sunk cost** and must be ignored.
> 
> Correct NPV logic:
> Cost today is 10 million. Future cash flows are worth 13 million. NPV is **3 million**.
> 
> Memory line: **if the money is already spent and cannot be recovered, it does not enter the project decision.**

83. If the new project reduces costs elsewhere, include the cost savings.
84. If the new product steals sales from the company’s existing product, include the lost sales. This is **cannibalization**. It is bad, but it is still incremental.
85. If the new project increases sales of another product, include that benefit too. That is a positive side effect, often called synergy.
86. Third principle: get **timing** right. Cash flow timing, duration, volatility, and possible direction changes matter. Moving the same cash flow earlier or later can change both NPV and IRR.


#### REAL OPTIONS
87. Real options are simple: they are **future choices built into a project**.
88. A normal NPV problem assumes management decides everything today and then just follows the plan. Real options say: no, management may get new information later and then change the plan. That flexibility has value. A real option is a **right, not an obligation**, so the company should exercise it only if it increases value.
89. First, **timing option**. The company can delay the project. It gives up near-term cash flows, but gets better information. Exam clue: “wait,” “delay,” “postpone,” “sequence investment.”
90. Second, **abandonment option**. If the project performs badly, the company can shut it down or sell the asset. Exercise it when abandoning gives more value than continuing.
91. Third, **expansion or growth option**. If the project works well, the company can invest more later. Exam clue: “scale up,” “expand capacity,” “enter more markets.”
92. Fourth, **flexibility option**. The company can change operations after the project starts: raise prices, add shifts, use overtime, change production.
93. Fifth, **fundamental option**. The project’s value depends on an outside variable, like oil price, gold price, or R&D success.

> [!Question] NUMERICAL — Abandonment option adds value
> Problem: A two‑year project costs 100 today and yields a single cash flow in two years that is either 140 (good) with probability 60% or 80 (bad) with probability 40%. Discount rate = 10% per year. Without flexibility, should the firm invest? If the firm can abandon at the end of Year 1 for a guaranteed salvage of 60, how does that change the decision?  
> Solution:  
> - Without flexibility (single payoff at Year 2):
> $$
> \text{Expected payoff at Year 2} = 0.6\cdot 140 + 0.4\cdot 80 = 112 \;\text{(currency units)}
> $$
> $$
> \mathrm{NPV}_{\text{base}} = \frac{112}{(1.10)^2} - 100 = \frac{112}{1.21} - 100 \approx -7.4
> $$
> Explanation: Negative expected NPV, so reject without flexibility.
>
> - With abandonment after Year 1: If prospects look bad at Year 1, abandon and take 60 instead of continuing to the low outcome. Model with a simple decision tree; assume the “bad” branch is revealed at Year 1 and leads to the low outcome if continued.
> $$
> \text{Value if good branch} = \frac{140}{(1.10)^2} \approx 115.7
> $$
> $$
> \text{Value if bad branch with abandon} = \frac{60}{1.10} \approx 54.5
> $$
> $$
> \text{Expected present value} = 0.6\cdot 115.7 + 0.4\cdot 54.5 \approx 91.7
> $$
> $$
> \mathrm{NPV}_{\text{with option}} = 91.7 - 100 \approx -8.3
> $$
> Explanation: In this setup the salvage is too small to offset the weak bad state; the option does not rescue the project. If the salvage were higher (e.g., 80), the option value would be larger and could turn NPV positive. Key idea: abandonment limits downside and can add material value depending on salvage and timing.
