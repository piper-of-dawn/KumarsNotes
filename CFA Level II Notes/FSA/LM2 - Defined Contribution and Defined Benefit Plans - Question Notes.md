## Variant: 1 — Defined contribution expense is earned before it is paid

**Abstract:** *A defined contribution plan promises a contribution, not a retirement payout. Expense follows employee service; cash flow follows the actual payment.*

> An employer contributes 5% of an employee's SGD 82,200 annual salary to a defined contribution plan every two weeks. There are 26 equal pay periods. The employee works the first period, ending 14 January, and the employer pays the plan on that date. Calculate the contribution, the expense and payable just before payment, and the cash-flow effect at payment. Round to whole SGD.

<span class="jargon-unlock">**Defined contribution (DC). What is it?** The employer owes an agreed contribution; the employee bears the risk that the resulting retirement savings are insufficient. **Accrued payable. What is it?** A contribution earned by the employee but not yet paid. **Operating cash flow. What is it?** Cash from ordinary business activity, including these employer contributions.</span>

**1. Price one period of service**

Annual promised contributions are SGD 82,200 × 5% = SGD 4,110. Split that across 26 equal periods.

$$
\text{Contribution per period}=\frac{82{,}200(0.05)}{26}=\boxed{\text{SGD }158.08\approx\text{SGD }158}
$$

**2. Put the same amount on the right statements at the right time**

Immediately before payment, operating expense and accrued payable each rise SGD 158. On 14 January, the payable falls SGD 158 and operating cash flow falls SGD 158. Payment creates no second expense.

> [!NOTE]
> **DC = Defined Contribution = Done after the contribution.** The employer does not book the employee's later investment gains, losses, or retirement payouts.

*Source pattern: 2025 CFA Level II FSA, LM2, Example 9, pp.90–91. Original inputs retained; whole-SGD rounding.*

---

## Variant: 2 — Recover a missing defined contribution payment

**Abstract:** *The accrued contribution is a simple unpaid bill. Opening payable plus this year's expense minus cash paid equals closing payable.*

> A company's defined contribution expense is EUR 480,000 for the year. Its unpaid contribution liability was EUR 35,000 at the start and EUR 47,000 at the end. No other adjustments exist. Calculate cash contributions and explain why they differ from expense.

<span class="jargon-unlock">**Defined contribution (DC) expense. What is it?** The employer contribution earned by staff during the period. **Payable. What is it?** The part earned but still unpaid. **Cash contribution. What is it?** Money actually transferred to the separate plan.</span>

**1. Build the unpaid-bill bridge**

The payable grew by EUR 12,000, so cash must be EUR 12,000 less than this year's expense.

$$
\text{Cash paid}=35{,}000+480{,}000-47{,}000=\boxed{\text{EUR }468{,}000}
$$

**2. Check the timing**

EUR 480,000 was earned as compensation; EUR 468,000 left the company's bank account. The remaining EUR 12,000 is still owed at year-end.

> [!NOTE]
> **Expense is earned; cash is paid.** For DC plans, their difference changes the short-term payable.

*Source pattern: 2025 CFA Level II FSA, LM2, Financial Reporting for DC Plans, pp.90–91. Inputs adapted.*

---

## Variant: 3 — Calculate the pension a defined benefit formula promises

**Abstract:** *A defined benefit formula specifies the employee's payout. Multiply the benefit rate, final salary, and credited years of service; then keep annual and monthly units straight.*

> A defined benefit pension promises an annual retirement payment equal to 1% of final annual salary for each year of service. An employee retires after 25 credited years with a final salary of EUR 80,000. Calculate the annual and monthly pension. Ignore tax and future increases.

<span class="jargon-unlock">**Defined benefit (DB). What is it?** The employer promises a retirement benefit calculated by a plan formula and bears investment and actuarial risk. **Credited service. What is it?** Years counted in that formula. **Final salary. What is it?** The salary amount to which this plan applies its benefit rate.</span>

**1. Convert years into a share of salary**

Each year earns 1% of final salary, so 25 years earn 25%. This is a promised annual payment, not a one-time account contribution.

$$
\text{Annual pension}=0.01(25)(\text{EUR }80{,}000)=\boxed{\text{EUR }20{,}000\text{ per year}}
$$

**2. Change the payment frequency, not the total benefit**

$$
\text{Monthly pension}=\frac{\text{EUR }20{,}000}{12}=\boxed{\text{EUR }1{,}666.67\text{ per month}}
$$

The employer must estimate and fund this promise; the employee's account balance is not the employer's obligation.

> [!NOTE]
> **DB = Defined Benefit = Benefit is defined.** The contribution needed to support it can change.

*Source pattern: 2025 CFA Level II FSA, LM2, DB formula discussion p.89 and Example 10 p.94. Inputs adapted.*

---

## Variant: 4 — A lower discount rate makes a fixed benefit promise heavier

**Abstract:** *The pension obligation is today's value of future benefits. A lower discount rate divides by a smaller growth factor, so today's obligation rises.*

> To isolate discount-rate direction, assume a pension plan owes one EUR 100,000 payment exactly ten years from now, with no other benefits or assumptions. Calculate its present value at annual discount rates of 5% and 4%, and the change.

<span class="jargon-unlock">**Pension obligation. What is it?** The present value of benefits earned for service already performed, before subtracting plan assets. **Present value. What is it?** Today's equivalent of future cash, $PV=F/(1+r)^n$, where $F$ is the future payment, $r$ the annual discount rate, and $n$ the years until payment. **Discount rate. What is it here?** The rate based on suitable high-quality bonds in the benefit currency.</span>

**1. Discount the same promise twice**

The EUR 100,000 future payment is unchanged. Only the rate used to translate it into today's money changes.

$$
\begin{aligned}
PV_{5\%}&=100{,}000/(1.05)^{10}=\boxed{\text{EUR }61{,}391.33}\\
PV_{4\%}&=100{,}000/(1.04)^{10}=\boxed{\text{EUR }67{,}556.42}
\end{aligned}
$$

**2. Read the sign**

The obligation rises by EUR 6,165.09. A pension plan holding bonds might simultaneously gain asset value, so the *net* funded-status change need not equal this obligation change.

> [!NOTE]
> **Rate down → obligation up. Rate up → obligation down.** Keep that direction in your head before touching a calculator.

*Source pattern: 2025 CFA Level II FSA, LM2, pension-obligation discounting pp.91–92 and practice Q7, Q21. Inputs adapted to one payment.*

---

## Variant: 5 — Funded status: subtract the promise from its dedicated assets

**Abstract:** *For each plan, funded status equals plan assets minus obligation. Negative means the employer owes the gap; separate plans stay separate.*

> At year-end, Plan A has fair-value assets of GBP 900m and a pension obligation of GBP 1,050m. Plan B has assets of GBP 300m and an obligation of GBP 260m. Calculate each funded status and the pension asset and liability presented by the sponsor. Ignore asset-ceiling limits.

<span class="jargon-unlock">**Funded status. What is it?** $F=A-O$, where $A$ is assets held solely to pay a particular plan's benefits and $O$ is the present value of benefits already earned. **Underfunded. What does it mean?** $F<0$: assets fall short. **Overfunded. What does it mean?** $F>0$: assets exceed the obligation. **Asset ceiling. What is it?** A possible limit on recognizing a surplus; this question excludes it.</span>

**1. Do the subtraction plan by plan**

$$
F_A=900-1{,}050=\boxed{-\text{GBP }150\text{m}},\qquad F_B=300-260=\boxed{+\text{GBP }40\text{m}}
$$

**2. Present the two claims separately**

The sponsor reports a GBP 150m pension liability and a GBP 40m pension asset, subject to the question's no-ceiling assumption. Their mathematical net is a GBP 110m deficit, but that is not permission to hide one plan inside another on the balance sheet.

> [!NOTE]
> **Assets minus obligation. Negative = liability. Positive = asset.** Repeat this sign check for *every* plan before adding anything.

*Source pattern: 2025 CFA Level II FSA, LM2, funded-status Equation 1 and separate-plan presentation pp.91–92.*

---

## Variant: 6 — Roll the gross pension obligation forward

**Abstract:** *The obligation grows with service and interest, changes with actuarial estimates, and shrinks when retirees receive benefits. Employer contributions do not enter this bridge.*

> A defined benefit plan opens with a pension obligation of GBP 28,416m. During the year, service cost is GBP 228m, interest cost GBP 1,557m, benefits paid GBP 1,322m, and actuarial change zero. Calculate the closing obligation. In a separate version, the closing obligation is GBP 28,779m; infer the actuarial gain or loss, keeping the other amounts fixed.

<span class="jargon-unlock">**Gross pension obligation. What is it?** Present value of earned retirement benefits before plan assets are deducted. **Service cost. What is it?** Additional benefits employees earn this year. **Interest cost. What is it?** Growth in present value as payment gets closer. **Actuarial gain/loss. What is it?** A change caused by updated assumptions; an obligation increase is a loss for the employer.</span>

**1. Add growth, subtract benefits paid**

$$
O_1=28{,}416+228+1{,}557-1{,}322=\boxed{\text{GBP }28{,}879\text{m}}
$$

**2. Solve the bridge backward**

The alternate obligation is GBP 100m below that baseline, so the missing adjustment is an actuarial *gain* of GBP 100m.

$$
\Delta O_{\text{actuarial}}=28{,}779-28{,}879=\boxed{-\text{GBP }100\text{m}}
$$

> [!NOTE]
> **Obligation bridge:** opening + service + interest + actuarial loss − benefits. Contributions fund the plan; they do not erase benefits already promised.

*Source pattern: 2025 CFA Level II FSA, LM2, Kensington practice Q1–7 and solution Q5, pp.102–103, 111. Direct inputs retained; inverse adapted.*

---

## Variant: 7 — Roll plan assets forward and solve for a missing contribution

**Abstract:** *Plan assets rise with investment return and employer contributions, then fall when the plan pays retirees. Solve the same bridge backward when cash paid is missing.*

> A defined benefit plan opens with GBP 23,432m of assets. Actual investment return is GBP 1,302m, employer contributions are GBP 693m, and benefits paid are GBP 1,322m. Find closing assets. If instead closing assets were GBP 24,005m, infer employer contributions with all other inputs unchanged.

<span class="jargon-unlock">**Plan assets. What are they?** Investments held by the pension plan exclusively for paying benefits, separate from the sponsor's own cash. **Actual return. What is it?** The investment gain or loss that really occurred. **Employer contribution. What is it?** Cash the sponsor transfers into the plan. **Benefit payment. What is it?** Cash the plan pays retirees.</span>

**1. Follow cash and investment value through the plan**

$$
A_1=23{,}432+1{,}302+693-1{,}322=\boxed{\text{GBP }24{,}105\text{m}}
$$

**2. Reverse the bridge**

If closing assets were GBP 100m lower, the contribution would have been GBP 100m lower.

$$
C=24{,}005-23{,}432-1{,}302+1{,}322=\boxed{\text{GBP }593\text{m}}
$$

> [!NOTE]
> **Asset bridge:** opening + actual return + employer cash − retiree payments. The contribution is cash flow, not pension expense.

*Source pattern: 2025 CFA Level II FSA, LM2, Kensington practice Q1–7, pp.102–103. Direct inputs retained; inverse adapted.*

---

## Variant: 8 — Reconcile the pension deficit, income statement, OCI, and cash

**Abstract:** *Four boxes, four different amounts: service in operating profit, net interest in financing profit, remeasurement in OCI, and contributions in operating cash flow.*

> A company's IFRS defined benefit plan opens with a GBP 28,416m obligation and GBP 23,432m assets. Service cost is GBP 228m; obligation interest is GBP 1,557m; actual asset return is GBP 1,302m; employer contributions are GBP 693m; benefits paid are GBP 1,322m. The opening discount rate is 5.48%, and there is no actuarial change. Calculate closing deficit, net interest expense, asset-return remeasurement, and operating cash outflow. Use the disclosed rounded interest amounts where applicable.

<span class="jargon-unlock">**IFRS. What is it?** International Financial Reporting Standards. **Net interest. What is it?** Discount rate times opening net pension liability or asset; a liability produces expense. **OCI. What is it?** Other comprehensive income, where IFRS reports pension remeasurements outside current profit. **Remeasurement. What is it?** Actual asset return beyond or below the discount-rate amount, plus actuarial changes in the obligation. **Deficit. What is it?** Obligation exceeding assets.</span>

**1. Rebuild the balance sheet from both gross bridges**

The obligation closes at GBP 28,879m and assets at GBP 24,105m.

$$
\text{Closing deficit}=28{,}879-24{,}105=\boxed{\text{GBP }4{,}774\text{m}}
$$

**2. Put each flow in its correct box**

The income statement has GBP 228m operating service expense and about GBP 273m financing net interest expense. The asset's discount-rate return is GBP 1,284.07m; actual return beats it by GBP 17.93m, an OCI gain of about GBP 18m. Cash outflow from operations is the GBP 693m employer contribution.

$$
\text{Net interest}=0.0548(28{,}416-23{,}432)=\boxed{\text{GBP }273.12\text{m}\approx273\text{m}}
$$

The deficit fell from GBP 4,984m to GBP 4,774m. Retiree payments reduce assets and obligation equally, so they cancel from this net movement.

> [!NOTE]
> **Service → operating profit; net interest → financing profit; remeasurement → OCI; contribution → cash flow.** The four-box rule is worth repeating until automatic.

*Source pattern: 2025 CFA Level II FSA, LM2, Kensington practice Q1–6 and solutions pp.102–103, 111. Original inputs retained.*

---

## Variant: 9 — First-year defined benefit plan: return belongs in two places

**Abstract:** *A contribution made at the start of the year earns a full year's interest assumption. IFRS puts that assumed amount in net interest and the difference from actual return in OCI.*

> At the beginning of the year, a company creates a defined benefit plan and contributes JPY 710m. Opening obligation is zero. During the year, employees earn JPY 5m of service cost, no benefits are paid, the discount rate is 2%, and assets actually return −3%. There are no other changes. Calculate closing funded status, net interest income, and remeasurement under IFRS.

<span class="jargon-unlock">**Funded status. What is it?** Plan assets minus the benefit obligation. **Net interest income. What is it?** Opening net pension asset times the discount rate, when the assets were funded at the start. **Remeasurement. What is it?** Actual return minus discount-rate return, recorded in other comprehensive income (OCI) under IFRS. **Service cost. What is it?** Benefits employees earned this year, recorded as operating expense.</span>

**1. Find the real end-of-year balances**

Actual investment loss is JPY 710m × 3% = JPY 21.3m. Plan assets end at JPY 688.7m and the obligation at JPY 5m.

$$
F_1=710-21.3-5=\boxed{\text{JPY }683.7\text{m asset}}
$$

**2. Split the return between profit and OCI**

The assumed discount-rate return is JPY 14.2m. Actual return was negative JPY 21.3m, so the difference is an OCI loss of JPY 35.5m.

$$
\text{Net interest income}=710(0.02)=\boxed{\text{JPY }14.2\text{m}},\qquad \text{OCI remeasurement}=-21.3-14.2=\boxed{-\text{JPY }35.5\text{m}}
$$

Check: opening asset 710 + financing income 14.2 − service cost 5 − OCI loss 35.5 = JPY 683.7m. The JPY 710m contribution is the sponsor's operating cash outflow.

> [!NOTE]
> **Opening funding earns opening-period interest.** The printed 2025 example omits it; the later official errata corrects the income/OCI split.

*Source pattern: 2025 CFA Level II FSA, LM2, Example 10 part 1, p.94–95; [2026 CFA Level II errata](https://www.cfainstitute.org/sites/default/files/docs/programs/cfa-program/candidate-resources/2026-cfa-level-ii-errata.pdf), Example 10 correction. Original inputs retained.*

---

## Variant: 10 — Defined benefit surplus: benefits paid cancel out

**Abstract:** *Roll assets and obligation separately, then subtract. A benefit payment lowers both by the same amount and cannot by itself change funded status.*

> A defined benefit plan opens with JPY 1,010m assets and a JPY 97m obligation. Service cost is JPY 9m, discount rate 2%, actual asset return 5%, benefits paid JPY 5m, and employer contributions zero. There are no actuarial changes. Calculate closing assets, obligation, funded status, IFRS net interest income, and OCI remeasurement.

<span class="jargon-unlock">**Defined benefit (DB) plan. What is it?** A retirement benefit promise borne by the employer. **Funded status. What is it?** Assets minus obligation. **Net interest income. What is it?** Opening surplus times discount rate. **OCI remeasurement. What is it?** Asset return beyond its discount-rate return, recorded outside profit under IFRS when no actuarial changes occur.</span>

**1. Roll both gross amounts**

The assets earn JPY 50.5m; the obligation accrues JPY 1.94m interest.

$$
\begin{aligned}
A_1&=1{,}010+50.5-5=\boxed{\text{JPY }1{,}055.50\text{m}}\\
O_1&=97+9+1.94-5=\boxed{\text{JPY }102.94\text{m}}\\
F_1&=1{,}055.50-102.94=\boxed{\text{JPY }952.56\text{m asset}}
\end{aligned}
$$

**2. Reconcile the accounting split**

Opening surplus is JPY 913m, yielding JPY 18.26m net interest income. Actual return exceeds the asset's JPY 20.2m discount-rate return by JPY 30.3m.

$$
F_1=913+\boxed{18.26}-9+\boxed{30.30}=\boxed{\text{JPY }952.56\text{m}}
$$

> [!NOTE]
> **Benefit payment −5 from assets and −5 from obligation = zero effect on surplus.** Official errata correct the printed OCI amount; a later erratum corrects the asset to JPY 952.56m.

*Source pattern: 2025 CFA Level II FSA, LM2, Example 10 part 2, p.95; [2025 errata](https://www.cfainstitute.org/sites/default/files/docs/programs/cfa-program/candidate-resources/2025-cfa-lii-curriculum-errata-notice.pdf) and [2026 errata](https://www.cfainstitute.org/sites/default/files/docs/programs/cfa-program/candidate-resources/2026-cfa-level-ii-errata.pdf). Original inputs retained.*

---

## Variant: 11 — US GAAP uses expected return, not actual return, in current profit

**Abstract:** *For the stipulated US GAAP treatment, add current service and gross obligation interest, then subtract expected asset return. Put the specified deferred changes in OCI.*

> A US GAAP defined benefit plan starts with an obligation of 42,000 currency units and assets of 39,000 units. Current service cost is 200 units. A 120-unit past-service plan amendment occurs at year-end. The discount rate is 7%, expected asset return is 8%, and actual asset return is 2,700 units. An actuarial loss raises the obligation 460 units. Assume no immediate recognition or amortization of past-service costs or remeasurements. Calculate pension cost in current profit, the return shortfall, and OCI losses from the specified changes.

<span class="jargon-unlock">**US GAAP. What is it?** United States Generally Accepted Accounting Principles. **Expected return. What is it?** Opening plan assets times management's assumed return; this reduces current pension cost under the stated US GAAP treatment. **Actual return. What is it?** What assets really earned. **Past-service cost. What is it?** Extra benefits for work employees performed before a plan amendment. **Actuarial loss. What is it?** An obligation increase from changed assumptions. **OCI. What is it?** Other comprehensive income, outside current profit.</span>

**1. Use opening balances for the two rate products**

The year-end amendment does not earn a full year's interest. Expected return, not the 2,700-unit actual return, offsets expense.

$$
\text{Pension cost in profit}=200+0.07(42{,}000)-0.08(39{,}000)=200+2{,}940-3{,}120=\boxed{20\text{ units}}
$$

**2. Park the stipulated differences outside current profit**

Actual return falls 420 units short of expected. Together with the 460-unit actuarial loss and 120-unit past-service cost, the deferred OCI loss is 1,000 units under the question's assumptions.

$$
\text{OCI loss}=120+(3{,}120-2{,}700)+460=\boxed{1{,}000\text{ units}}
$$

> [!NOTE]
> **US GAAP current cost uses expected asset return; IFRS net interest uses the discount rate.** Do not swap actual return into either current-profit formula.

*Source pattern: 2025 CFA Level II FSA, LM2, US GAAP comparison pp.96–97, practice Q8–9 and solution Q9 pp.104, 111; [2025 errata](https://www.cfainstitute.org/sites/default/files/docs/programs/cfa-program/candidate-resources/2025-cfa-lii-curriculum-errata-notice.pdf) corrects interest to 7% × 42,000. Original inputs retained.*

---

## Variant: 12 — The US GAAP corridor has a threshold, not a free pass

**Abstract:** *Compare cumulative unrecognized gain or loss with 10% of the larger opening obligation or assets. Amortize only the excess across remaining working lives.*

> A US GAAP defined benefit plan opens with an obligation of USD 600m and assets of USD 500m. Cumulative unrecognized actuarial loss is USD 90m. The average remaining working life is 10 years. Under the corridor approach, calculate the year's minimum loss amortization. What if the cumulative loss were USD 55m instead?

<span class="jargon-unlock">**Corridor approach. What is it?** A US GAAP smoothing method: only cumulative unrecognized gains or losses beyond 10% of the larger opening obligation or assets must enter profit over employees' remaining working lives. **Amortization. What is it?** Spreading that excess across years. **Unrecognized loss. What is it?** A previously deferred pension loss not yet charged to current profit.</span>

**1. Draw the threshold**

The larger opening amount is USD 600m, so the corridor is USD 60m.

$$
\text{Corridor}=0.10\max(600,500)=\boxed{\text{USD }60\text{m}}
$$

**2. Charge only the part outside it**

$$
\text{Annual amortization}=\frac{\max(90-60,0)}{10}=\boxed{\text{USD }3\text{m}}
$$

At USD 55m cumulative loss, the required corridor amortization is $\\boxed{\\text{USD }0}$. The loss still exists; the threshold delays its required recognition in profit.

> [!NOTE]
> **Corridor = 10% × larger opening balance. Expense only the excess.** Do not divide the whole cumulative loss by service life.

*Source pattern: 2025 CFA Level II FSA, LM2, US GAAP corridor rule, p.96. Inputs adapted.*

---

## Variant: 13 — Forecast next year's IFRS pension cost from the closing deficit

**Abstract:** *Next year's opening funded status is this year's closing status. Add forecast service cost and the discount-rate charge on that opening deficit.*

> At the end of FY2024, a company's defined benefit obligation is 41,720 currency units and plan assets are 38,700 units. Under IFRS, assume FY2025 current-plus-past service cost of 320 units, a 7% discount rate, and no additional timing adjustments. Forecast FY2025 net interest expense and total pension cost recognized in profit.

<span class="jargon-unlock">**IFRS pension cost in profit. What is it?** Service cost plus net interest expense, or minus net interest income. **Opening deficit. What is it?** Pension obligation minus plan assets at the start of the forecast year. **Discount rate. What is it?** The annual rate applied to that opening net balance for net interest.</span>

**1. Carry the closing balance into the new year**

The opening FY2025 deficit is 41,720 − 38,700 = 3,020 units.

$$
\text{Net interest expense}=0.07(3{,}020)=\boxed{211.4\text{ units}}
$$

**2. Add the service employees will earn**

$$
\text{Forecast profit expense}=320+211.4=\boxed{531.4\text{ units}\approx531\text{ units}}
$$

Contributions are a cash-flow forecast, not a substitute for this expense forecast. Remeasurements, if any, go to OCI under IFRS.

> [!NOTE]
> **Forecast rule:** closing deficit becomes next year's opening deficit. Service + net interest goes to profit; cash contributions go to cash flow.

*Source pattern: 2025 CFA Level II FSA, LM2, practice Q10 and solution p.112; [2025 errata](https://www.cfainstitute.org/sites/default/files/docs/programs/cfa-program/candidate-resources/2025-cfa-lii-curriculum-errata-notice.pdf) corrects 41,270 to 41,720. Original inputs retained.*

---

## Variant: 14 — Pension assumptions move different numbers

**Abstract:** *A higher expected asset return lowers US GAAP current expense but does not change the benefit promise. A higher discount rate lowers present value; higher expected salary raises it.*

> A US GAAP pension plan has opening assets of BRL 1,000m. Management changes its expected asset return assumption from 6.06% to 6.79%, holding actual returns and all else fixed. Calculate the change in current pension expense caused by that assumption. Separately, state the direction of the obligation if the discount rate rises, and if expected final salaries rise.

<span class="jargon-unlock">**Expected return assumption. What is it?** The return rate multiplied by opening assets to reduce US GAAP pension expense; it is not the plan's actual investment gain. **Pension obligation. What is it?** Present value of already-earned promised benefits. **Discount rate. What is it?** The rate translating those future benefits into today's value. **Salary growth assumption. What is it?** Estimated increase in salaries used by a final-pay benefit formula.</span>

**1. Isolate the assumption that has enough numbers**

A 0.73 percentage-point higher assumed return increases the expected return credit by BRL 7.3m, lowering reported current expense by that amount.

$$
\Delta\text{expense}=-1{,}000(0.0679-0.0606)=\boxed{-\text{BRL }7.3\text{m}}
$$

**2. Keep assumptions in their own lanes**

A higher discount rate makes the same future benefits worth less today; higher expected final salaries raise benefits and the obligation. The expected asset return assumption alone does not change the obligation or operating cash flow.

> [!NOTE]
> **Expected asset return → US GAAP expense. Discount rate → present value. Salary growth → promised amount.** Three knobs, three different mechanisms.

*Source pattern: 2025 CFA Level II FSA, LM2, assumptions discussion p.99 and practice Q20–23 pp.107–108. Return rates retained; asset amount adapted.*

---

## Variant: 15 — Reconcile a disclosed pension deficit and the asset ceiling

**Abstract:** *The gross deficit is obligation minus assets. An asset-ceiling adjustment can make recognized net assets smaller; disclosed asset and liability lines must still add to the reported net.*

> A company's pension note reports USD 107,336m obligations, USD 104,495m plan assets, and a USD 13m reduction from asset ceilings. Its balance sheet reports USD 8,471m pension assets, USD 6,458m pension liabilities, and USD 4,867m other post-employment-benefit liabilities. Reconcile the net amount both ways.

<span class="jargon-unlock">**Asset ceiling. What is it?** A limit on recognizing a pension surplus that cannot be used or recovered by the sponsor. **Funded status. What is it?** Plan assets minus obligations. **Other post-employment benefits (OPEB). What are they?** Benefits such as retiree health care, also treated as defined benefit obligations here. **Reconciliation. What is it?** Two independent routes to the same reported net amount.</span>

**1. Start with the gross plan economics**

Assets fall USD 2,841m short of obligations; the asset-ceiling adjustment worsens the reported net position by USD 13m.

$$
104{,}495-107{,}336-13=\boxed{-\text{USD }2{,}854\text{m}}
$$

**2. Check the reported line items**

$$
8{,}471-6{,}458-4{,}867=\boxed{-\text{USD }2{,}854\text{m}}
$$

Separate positive and negative plan balances appear in different lines; the net is a *check*, not an instruction to collapse every plan into one balance-sheet item.

> [!NOTE]
> **Two-route checksum:** assets − obligations − ceiling = recognized pension assets − pension liabilities − OPEB liabilities.

*Source pattern: 2025 CFA Level II FSA, LM2, Example 11, Shell disclosures p.99. Original disclosed figures retained.*

---

## Variant: 16 — Deduct a pension deficit once in a company valuation

**Abstract:** *Future service is a real future compensation cost in free cash flow. An existing underfunded obligation is debt-like in the enterprise-to-equity bridge; its net interest is already in that present value.*

> An analyst values operating assets at EUR 1,000m using a free-cash-flow forecast that includes EUR 12m annual future service cost but excludes pension net interest. Conventional net debt is EUR 180m. A defined benefit plan has a EUR 45m net pension liability at the valuation date. Compute equity value. A separate overfunded plan reports a EUR 10m accounting asset that cannot be withdrawn; show its effect under the reading's valuation approach.

<span class="jargon-unlock">**Enterprise value. What is it?** Present value of operations before subtracting financing claims. **Equity value. What is it?** Value left for shareholders after those claims. **Net pension liability. What is it?** The shortfall between plan assets and already-earned benefit obligations. **Future service cost. What is it?** Benefits employees will earn through future work. **Net interest. What is it?** Growth of the discounted existing pension claim as time passes.</span>

**1. Subtract each existing claim once**

The EUR 45m deficit is a current debt-like claim. Future service is already captured as a forecast cost.

$$
\text{Equity value}=1{,}000-180-45=\boxed{\text{EUR }775\text{m}}
$$

**2. Treat the separate surplus as restricted**

The plan's EUR 10m surplus is not cash shareholders can take out. Under the reading's approach, it adds EUR 0 to this enterprise-to-equity bridge; equity value remains EUR 775m.

> [!NOTE]
> **Future service stays in free cash flow; today's deficit comes off enterprise value; net interest is not charged again.** Keep the pension bill to one copy.

*Source pattern: 2025 CFA Level II FSA, LM2, valuation discussion pp.100–101 and practice Q6, Q26 with solutions pp.111, 113. Inputs adapted.*
