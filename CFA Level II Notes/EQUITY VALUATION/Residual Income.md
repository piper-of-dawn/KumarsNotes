# TL;DR

1. Just remember these formulas:

\[ \boxed{V_0=B_0+\sum_{t=1}^{\infty}\frac{(E_{t+1} - rB_t)}{(1+r)^t}} \]

\[ \boxed{V_0=B_0+\sum_{t=1}^{\infty}\frac{(ROE_t-r)B_{t-1}}{(1+r)^t}} \]

- $r$ is the required rate of return on equity
- $rB_t$ is the anticipated return for holding equity (cost of equity). B is Book Value per Share
- $E_{t+1}$ actual at EPS per share 
- $ROE_t$ is the return on equity at time t is net income divided by equity capital, or the book value of equity.
2. **The model uses beginning book value, not average book value**
\[
\boxed{ROE_t=\frac{EPS_t}{B_{t-1}}}
\]

3. Book Value does NOT include preferred shares.==Preferred equity must be excluded from total shareholders' equity when calculating common BVPS. ==
Suppose the company also reports a $10 loss through other comprehensive income (OCI). The actual relationship is:
\[
\boxed{B_t=B_{t-1}+EPS_t-D_t+OCI_t}
\]

4. The residual income model's main advantage is that terminal value does not dominate the valuation, and it relies on figures readily available in the books. Another benefit is that it can value companies with no dividends or cash flows too erratic to trust.
5. Management can manipulate accounting data, ==and the clean surplus relation must hold - a disadvantage in its own right. ==This assumes that, apart from transactions with owners, all changes in book value pass through earnings.

> If forecast OCI is material and not expected to offset over time, incorporate it into comprehensive income when estimating residual income.

But don't mechanically capitalize every historical OCI fluctuation. Temporary gains and losses may reverse. The book emphasizes that valuation bias matters when the present value of expected clean surplus violations does not net to zero.

6. When OCI has remained negative for years, potential return on equity is overstated. The book value, however, already includes the accumulated OCI.
7. Justified P/B:
\[
\boxed{\frac{V_0}{B_0}=\frac{ROE-g}{r-g}}
\]
Another version is

$$\boxed{\frac{V_0}{B_0} = 1 + \left( 1 + \frac{ROE -r}{r-g} \right)} $$
8. Memorise the persistence factor formula. ==The setup is identical, except the terminal value now has an additional denominator term: 1 + r - ω, where omega is the persistence factor.==
\[
\boxed{V_0=B_0+\sum_{t=1}^{T-1}\frac{RI_t}{(1+r)^t}+\frac{RI_T}{(1+r-\omega)(1+r)^{T-1}}}
\]

9. The chapter highlights **restructuring charges**, discontinued operations, accounting changes, unusual items, and nonoperating gains. Suppose EPS is $3, but includes a one-off restructuring charge of $1. A reasonable normalized forecast might begin with $4, if the charge is genuinely nonrecurring. ==The book explicitly states that a separate book-value adjustment for such charges is generally unnecessary because their effects are already reflected in assets and equity.== And if a company reports a major restructuring charge every single year, the expense may not actually be nonrecurring.
10. A zero terminal value does not mean the company is worthless. It means the company earns a return on equity equal to its required return on equity forever, which is less dramatic than it sounds.

# Residual Income Mechanics

We want to prove one simple idea:

**Stock value = Today's book value + Present value of future residual income.**

## **Step 1: Begin with the clean surplus relationship**

\[ B_{t+1}=B_t+E_{t+1}-D_{t+1} \]

Rearrange to isolate dividends:

\[ \boxed{D_{t+1}=E_{t+1}+B_t-B_{t+1}} \]

In plain English:

Dividend = Earnings + Beginning book value − Ending book value.

## **Step 2: Introduce residual income**

We know:

\[ RI_{t+1}=E_{t+1}-rB_t \]

Our objective is to create \(E_{t+1}-rB_t\) inside the dividend formula.

Here's the algebraic trick:

\[ B_t=(1+r)B_t-rB_t \]

Substitute into dividends:

\[ D_{t+1}=E_{t+1}+(1+r)B_t-rB_t-B_{t+1} \]

Rearrange:

\[ \boxed{D_{t+1}=\underbrace{(E_{t+1}-rB_t)}_{\text{Residual income}}+(1+r)B_t-B_{t+1}} \]

## **Step 3: Substitute into the dividend discount model**

\[ P_0=\frac{D_1}{1+r}+\frac{D_2}{(1+r)^2}+\cdots \]

For Year 1:

\[ D_1=(E_1-rB_0)+(1+r)B_0-B_1 \]

Therefore:

\[ \frac{D_1}{1+r} = \frac{RI_1}{1+r}+B_0-\frac{B_1}{1+r} \]

For Year 2:

\[ \frac{D_2}{(1+r)^2} = \frac{RI_2}{(1+r)^2}+\frac{B_1}{1+r}-\frac{B_2}{(1+r)^2} \]

## **Step 4: Add the years together**

\[ \begin{aligned} P_0={}&B_0+\frac{RI_1}{1+r}\\\ &\underbrace{-\frac{B_1}{1+r}+\frac{B_1}{1+r}}_{\text{Cancel}}\\\ &+\frac{RI_2}{(1+r)^2}\\\ &\underbrace{-\frac{B_2}{(1+r)^2}+\frac{B_2}{(1+r)^2}}_{\text{Cancel}}\\\ &+\frac{RI_3}{(1+r)^3}+\cdots \end{aligned} \]

*Every intermediate book value cancels!*

Assuming the discounted terminal book value approaches zero, we get:

\[ \boxed{P_0=B_0+\sum_{t=1}^{\infty}\frac{RI_t}{(1+r)^t}} \]

### **Step 5: Express residual income using ROE**

We know:

\[ ROE_t=\frac{E_t}{B_{t-1}} \]

Therefore:

\[ E_t=ROE_t\times B_{t-1} \]

Substitute into residual income:

\[ RI_t=E_t-rB_{t-1} \]

\[ \boxed{RI_t=(ROE_t-r)B_{t-1}} \]

### **Step 6: Substitute into the valuation formula**

\[ \boxed{V_0=B_0+\sum_{t=1}^{\infty}\frac{(ROE_t-r)B_{t-1}}{(1+r)^t}} \]

**Core intuition:** A company creates value above book value only when its ROE exceeds its required return \(r\).

- \(ROE>r\): Positive residual income.
- \(ROE=r\): Zero residual income.
- \(ROE<r\): Negative residual income.

# Justified P/B

The single-stage residual income model is:
\[
\boxed{V_0=B_0\left(1+\frac{ROE-r}{r-g}\right)}
\]

Divide by book value:
\[
\boxed{\frac{V_0}{B_0}=1+\frac{ROE-r}{r-g}}
\]

Equivalently:
\[
\boxed{\frac{V_0}{B_0}=\frac{ROE-g}{r-g}}
\]

The second formula looks different but is algebraically identical.

Suppose ROE = 10% and the required return = 10%.

Then:
\[
\frac{V_0}{B_0}=1
\]

It doesn't matter whether the company grows at 2% or 8%, provided the constant-growth model's assumptions hold. Why? Because its additional investments earn exactly what shareholders require. The company grows, but generates no additional economic value.

> Growth creates value only when the incremental returns on reinvested equity exceed the cost of equity.


**Don't confuse intrinsic P/B with market P/B**
A company can have:
- Market P/B = 3.
- Justified P/B = 2.
- ROE greater than the cost of equity.
It creates positive residual income, yet its shares can still be overvalued.

Positive residual income tells you intrinsic value exceeds book value. It does not guarantee intrinsic value exceeds market price.


## **Reverse-engineering the implied growth rate**


Starting with:
\[
\frac{P_0}{B_0}=1+\frac{ROE-r}{r-g}
\]

Rearrange:
\[
\boxed{g=r-\frac{ROE-r}{P_0/B_0-1}}
\]


# Persistence Factor

The chapter introduces \(\omega\), the residual income persistence factor.
\[
\boxed{V_0=B_0+\sum_{t=1}^{T-1}\frac{RI_t}{(1+r)^t}+\frac{RI_T}{(1+r-\omega)(1+r)^{T-1}}}
\]

The last term incorporates Year \(T\)'s residual income and its subsequent persistence. Therefore, Year \(T\)'s residual income is not added separately again.