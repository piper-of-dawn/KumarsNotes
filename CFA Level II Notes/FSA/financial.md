## Variant: Defined Benefit Pensions — IFRS vs US GAAP

**Abstract:** *Start with the pension obligation and plan assets, then separate pension expense in profit or loss from remeasurements in OCI. The main trap is using the expected asset return for IFRS or treating employer contributions as pension expense.*

> A company has a defined benefit pension plan. Compare the accounting under IFRS and US GAAP, calculate pension expense and other comprehensive income (OCI), and identify the main exam traps.

**The concept in 20 seconds**

A **defined benefit plan** promises employees future retirement payments. The **projected benefit obligation (PBO)** is the present value of those promised benefits; **plan assets** are investments set aside to help pay them.

$$
\boxed{\text{Funded status}=\text{Plan assets}-\text{PBO}}
$$

A negative amount is an underfunded position; a positive amount is an overfunded position, subject to applicable asset recognition limits.

> [!NOTE]
> **Expense is not contributions:** pension expense follows accrual accounting; employer contributions are cash flows.

**The comparison to memorize**

| Component | IFRS | US GAAP |
| --- | --- | --- |
| Current service cost | Operating profit or loss | Operating profit or loss |
| Past service cost | Profit or loss immediately, generally within operating expense | Initially OCI; subsequently amortized into non-operating profit or loss |
| Interest on obligation | Included in net interest in profit or loss | Non-operating profit or loss |
| Return on assets in profit or loss | Discount-rate-based interest income | Expected return |
| Actuarial gains and losses | OCI; never recycled to profit or loss | OCI with subsequent amortization, or immediate recognition in profit or loss under an accounting policy |
| Asset return surprises | OCI; never recycled to profit or loss | OCI with possible subsequent amortization, or immediate recognition in profit or loss under an accounting policy |

> [!NOTE]
> **Memory hook:** IFRS recognizes service costs promptly and keeps remeasurements out of earnings. US GAAP uses expected returns and may smooth gains and losses through amortization.

**The formulas**

For IFRS, assuming no settlement effects or asset-ceiling adjustments:

$$
\boxed{\text{Pension expense}=\text{Current service cost}+\text{Past service cost}+\text{Net interest}}
$$

$$
\text{Net interest}=(\text{Beginning PBO}-\text{Beginning plan assets})\times r
$$

Here $r$ is the discount rate. The simplified formula assumes no adjustments for contributions, benefit payments, or other changes during the period.

For US GAAP, assuming no additional settlement effects:

$$
\boxed{\text{Pension expense}=CS+IC-ER+APSC+AGL}
$$

- $CS$: current service cost.
- $IC$: interest cost = beginning PBO $\times$ discount rate.
- $ER$: expected return = beginning plan assets $\times$ expected return rate.
- $APSC$: amortization of past service cost.
- $AGL$: amortization of actuarial losses, net of gains; a net gain reduces expense.

**Numerical example: same pension, different profit**

| Input | Amount |
| --- | ---: |
| Beginning PBO | 42,000 |
| Beginning plan assets | 39,000 |
| Discount rate | 7% |
| Expected asset return | 8% |
| Actual asset return | 2,700 |
| Current service cost | 200 |
| New past service cost | 120 |
| Actuarial loss on obligation | 460 |

Assume no amortization of previously deferred amounts, no settlement effects, no asset-ceiling adjustment, and no timing adjustments for contributions or benefit payments. For US GAAP, assume the gains and losses are initially recognized in OCI.

**1. IFRS: expense and OCI**

Interest on the obligation is $42{,}000\times7\%=2{,}940$. Interest income on plan assets uses the **discount rate**: $39{,}000\times7\%=2{,}730$.

$$
\begin{aligned}
\text{P&L expense} &=200+120+2{,}940-2{,}730\\
&=\boxed{530}
\end{aligned}
$$

Actual asset return was 30 below the interest income recognized in profit or loss. Add the obligation's actuarial loss to obtain the OCI loss:

$$
(2{,}730-2{,}700)+460=\boxed{490\text{ OCI loss}}
$$

**2. US GAAP: expense and OCI**

Expected asset return is $39{,}000\times8\%=3{,}120$. With no amortization of earlier amounts, the new past service cost does not yet enter pension expense.

$$
\begin{aligned}
\text{P&L expense} &=200+2{,}940-3{,}120\\
&=\boxed{20}
\end{aligned}
$$

Actual asset return was 420 below the expected return recognized in profit or loss. Add the obligation loss and the new past service cost:

$$
(3{,}120-2{,}700)+460+120=\boxed{1{,}000\text{ OCI loss}}
$$

> [!NOTE]
> The $120 past service cost enters profit or loss immediately under IFRS, but initially enters OCI under the US GAAP treatment assumed here.

**Five CFA exam traps**

1. **Interest cost:** use beginning PBO $\times$ discount rate under both standards in this simplified setup; adjust for relevant changes during the period when required.
2. **Asset returns:** IFRS uses the discount rate for net interest; US GAAP uses the expected return in pension expense.
3. **Past service cost:** IFRS recognizes it in profit or loss immediately; US GAAP generally recognizes it initially in OCI and subsequently amortizes it.
4. **Actuarial gains and losses:** IFRS does not recycle remeasurements into profit or loss; US GAAP may amortize them, including under the 10% corridor.
5. **Operating versus total expense:** under US GAAP, current service cost is the operating component; the other recognized components are presented outside operating income but affect net income.

**Bonus: the US GAAP 10% corridor**

$$
\text{Corridor}=10\%\times\max(\text{Beginning PBO},\text{Beginning plan assets})
$$

> [!NOTE]
> Under the corridor approach, the cumulative unrecognized net actuarial gain or loss above the corridor is subject to minimum amortization, generally over average remaining service life; different periods can apply, including for plans with mostly inactive participants.

> [!NOTE]
> **Final memory hook:** IFRS = *service costs now, remeasurements in OCI without recycling*. US GAAP = *current service now, expected returns in profit, and deferred amounts potentially returning later*.

*Source supplied: CFA Level II Financial Statement Analysis, Learning Module 2, pp. 93–97, especially Exhibit 8.*
