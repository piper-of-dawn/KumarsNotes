## Variant: Spot Rates and Yield for a Coupon Bond

> [!abstract]
> Discount each cash flow at its own spot rate to get the price. Then solve for the single rate (YTM) that reproduces that same price — it is a weighted average of the spot rates, pulled toward the largest cash flow's spot rate.

> Compute the **price** and **yield to maturity** of a **three-year, 4% annual-pay, \$1,000 face** value bond given the spot rate curve: $S_1 = 5\%$, $S_2 = 6\%$, $S_3 = 7\%$.

**What is the question really asking?**

Two things: (1) the bond's price using the spot curve, and (2) the single YTM that reproduces that price. The key question is: **why are price and YTM different from each other and from any single spot rate?**

> [!NOTE]
> Each cash flow is discounted at the spot rate for its own maturity. YTM is the one rate that replaces all of them.

**1. Price the bond using the spot curve**

Each coupon and the face value get discounted at the spot rate matching their year:

$$
P = \frac{40}{1.05} + \frac{40}{1.06^2} + \frac{1040}{1.07^3}
$$

$$
P = 38.10 + 35.60 + 848.95 = \boxed{\$922.64}
$$

*Intuition:* The Year 3 cash flow (\$1,040) dominates, so $S_3$ has the biggest pull on the price.

**2. Solve for YTM**

Now find the single rate $y_3$ that makes the PV of all cash flows equal to \$922.64:

$$
\text{TI BA II Plus: } N=3,\; PV=-922.64,\; PMT=40,\; FV=1000,\; \text{CPT I/Y}
$$

$$
y_3 = \boxed{6.94\%}
$$

> [!NOTE]
> YTM sits between the spot rates: $S_1 < y_3 < S_3$, pulled closest to $S_3$ because the par payment dominates.

---

## Variant: Forward Pricing

> [!abstract]
> The forward price of a bond is today's price of the long bond divided by today's price of the shorter bond. $F(j,k) = P(j+k) / P(j)$. It is the price you lock in today to pay at time $j$ for a bond maturing at $j+k$.

> Calculate the **forward price two years from now** for a **\$1 par, zero-coupon, three-year bond** given $S_2 = 4\%$ and $S_5 = 6\%$.

**What is the question really asking?**

We need $F(2,3)$ — the price agreed today, paid in two years, for a bond that pays \$1 in five years. The key question is: **what two investments must have the same cost today?**

**1. Compute the two discount factors**

$$
P(2) = \frac{1}{(1.04)^2} = 0.9246
$$

$$
P(5) = \frac{1}{(1.06)^5} = 0.7473
$$

*Intuition:* $P(2)$ is today's price of \$1 received in 2 years. $P(5)$ is today's price of \$1 received in 5 years.

**2. Apply the forward pricing model**

Buying a 5-year zero today costs $P(5)$. Entering a forward contract to buy a 3-year bond in 2 years costs $P(2) \times F(2,3)$ today (the forward price discounted back 2 years). Arbitrage forces them equal:

$$
F(2,3) = \frac{P(5)}{P(2)} = \frac{0.7473}{0.9246} = \boxed{\$0.8082}
$$

> [!NOTE]
> Forward pricing model: $F(j,k) = P(j+k) / P(j)$. The forward price is a ratio of two discount factors.

---

## Variant: Forward Rates

> [!abstract]
> The forward rate is the rate that makes you indifferent between one long bond and a short bond plus reinvestment. $[1+f(j,k)]^k = (1+S_{j+k})^{j+k} / (1+S_j)^j$. Upward-sloping curve means forward rate is above the long spot rate.

> Given $S_2 = 4\%$ and $S_5 = 6\%$, calculate the implied **three-year forward rate** for a loan starting two years from now, $f(2,3)$.

**What is the question really asking?**

We need the rate on a 3-year loan that starts in 2 years. The key question is: **what rate makes a 5-year zero equal to a 2-year zero rolled into a 3-year forward?**

**1. Set up the forward rate model**

$$
[1 + f(2,3)]^3 = \frac{(1+S_5)^5}{(1+S_2)^2}
$$

**2. Substitute and solve**

$$
[1 + f(2,3)]^3 = \frac{(1.06)^5}{(1.04)^2} = \frac{1.33823}{1.08160} = 1.23727
$$

$$
1 + f(2,3) = (1.23727)^{1/3} = 1.0735
$$

$$
f(2,3) = \boxed{7.35\%}
$$

> [!NOTE]
> Upward-sloping curve $\Rightarrow$ forward rate is above the long spot rate: $f(2,3) = 7.35\% > S_5 = 6\%$.

---

## Variant: Bootstrapping Spot Rates from the Par Curve

> [!abstract]
> The 1-year spot rate equals the 1-year par rate. For each longer maturity, set the bond price to par (100), discount the known coupons at the spot rates you already found, and solve for the unknown spot rate on the final cash flow. Each step feeds the next.

> Given the **annual-pay par curve** — 1-year: **1.00%**, 2-year: **1.25%**, 3-year: **1.50%** — compute the corresponding **spot rate curve**.

**1. Spot rate for Year 1**

The 1-year par bond has no reinvestment risk, so:

$$
S_1 = \boxed{1.00\%}
$$

**2. Spot rate for Year 2**

A 2-year par bond pays a 1.25% coupon and trades at 100. Discount the first coupon at $S_1$, solve for $S_2$:

$$
100 = \frac{1.25}{1.01} + \frac{101.25}{(1+S_2)^2}
$$

$$
100 = 1.2376 + \frac{101.25}{(1+S_2)^2}
$$

$$
\frac{101.25}{(1+S_2)^2} = 98.7624
$$

$$
(1+S_2)^2 = \frac{101.25}{98.7624} = 1.02518
$$

$$
S_2 = \boxed{1.252\%}
$$

**3. Spot rate for Year 3**

A 3-year par bond pays 1.50% and trades at 100. Discount the first two coupons at $S_1$ and $S_2$, solve for $S_3$:

$$
100 = \frac{1.50}{1.01} + \frac{1.50}{(1.01252)^2} + \frac{101.50}{(1+S_3)^3}
$$

$$
100 = 1.4851 + 1.4632 + \frac{101.50}{(1+S_3)^3}
$$

$$
\frac{101.50}{(1+S_3)^3} = 97.0517
$$

$$
(1+S_3)^3 = \frac{101.50}{97.0517} = 1.04581
$$

$$
S_3 = \boxed{1.505\%}
$$

> [!NOTE]
> Bootstrapping is recursive: each new spot rate uses all previously found spot rates. Par bonds trade at 100, so the price is always 100.

---

## Variant: Spot Rate Evolution and Holding Period Returns

> [!abstract]
> If future spot rates evolve exactly as today's forward curve predicts, every bond — regardless of maturity — earns the 1-year spot rate over a 1-year horizon. Buy today, sell in one year at the forward-implied price; the return is always $S_1$.

> **Jane Dash, CFA** collects benchmark spot rates: $S_1 = 3\%$, $S_2 = 4\%$, $S_3 = 5\%$. Expected spot rates at end of Year 1: Year 1 = **5.01%**, Year 2 = **6.01%**. Calculate the **one-year holding period return** of a 1-year, 2-year, and 3-year zero-coupon bond.

**1. Verify the expected rates are the forward rates**

$$
f(1,1) = \frac{(1.04)^2}{1.03} - 1 = 5.01\%
$$

$$
f(1,2) = \left(\frac{(1.05)^3}{1.03}\right)^{1/2} - 1 = 6.01\%
$$

The expected rates match the forward rates, so all bonds will earn $S_1 = 3\%$.

**2. One-year bond**

$$
P_0 = \frac{1}{1.03} = 0.9709
$$

After one year, the bond matures and pays \$1:

$$
\text{HPR} = \frac{1}{0.9709} - 1 = \boxed{3.00\%}
$$

**3. Two-year bond**

$$
P_0 = \frac{1}{(1.04)^2} = 0.9246
$$

After one year, the bond has 1 year left. The 1-year expected spot rate is 5.01%:

$$
P_1 = \frac{1}{1.0501} = 0.9523
$$

$$
\text{HPR} = \frac{0.9523}{0.9246} - 1 = \boxed{3.00\%}
$$

**4. Three-year bond**

$$
P_0 = \frac{1}{(1.05)^3} = 0.8638
$$

After one year, the bond has 2 years left. The 2-year expected spot rate is 6.01%:

$$
P_1 = \frac{1}{(1.0601)^2} = 0.8898
$$

$$
\text{HPR} = \frac{0.8898}{0.8638} - 1 = \boxed{3.00\%}
$$

> [!NOTE]
> When spot rates evolve as the forward curve predicts, every zero-coupon bond earns $S_1$ over a 1-year horizon — maturity does not matter.

---

## Variant: Computing the Swap Rate Curve

> [!abstract]
> The swap fixed rate for tenor $T$ is the coupon rate that makes a \$1 par bond priced at par using the spot curve. $SFR_T = (1 - P_T) / \sum P_i$, where $P_i$ is the discount factor for year $i$.

> Given the **MRR spot rate curve** — $S_1 = 3\%$, $S_2 = 4\%$, $S_3 = 5\%$ — compute the **swap fixed rate** for tenors of 1, 2, and 3 years.

**1. Compute discount factors**

$$
P_1 = \frac{1}{1.03} = 0.9709, \quad P_2 = \frac{1}{(1.04)^2} = 0.9246, \quad P_3 = \frac{1}{(1.05)^3} = 0.8638
$$

**2. SFR for 1-year tenor**

$$
\frac{SFR_1}{1.03} + \frac{1}{1.03} = 1 \quad \Rightarrow \quad SFR_1 = \boxed{3.00\%}
$$

*Why?* A 1-year swap is just a 1-year par bond, so $SFR_1 = S_1$.

**3. SFR for 2-year tenor**

$$
\frac{SFR_2}{1.03} + \frac{SFR_2}{(1.04)^2} + \frac{1}{(1.04)^2} = 1
$$

$$
SFR_2 \times (0.9709 + 0.9246) = 1 - 0.9246 = 0.0754
$$

$$
SFR_2 = \frac{0.0754}{1.8955} = \boxed{3.98\%}
$$

**4. SFR for 3-year tenor**

$$
SFR_3 \times (0.9709 + 0.9246 + 0.8638) = 1 - 0.8638 = 0.1362
$$

$$
SFR_3 = \frac{0.1362}{2.7593} = \boxed{4.93\%}
$$

> [!NOTE]
> Swap fixed rate formula: $SFR_T = \frac{1 - P_T}{\sum_{i=1}^{T} P_i}$. It is the coupon that prices a \$1 par bond at par.

---

## Variant: Swap Spread

> [!abstract]
> Swap spread = swap rate minus Treasury yield for the same maturity. It measures the credit gap between banks (swap rate) and the government (risk-free).

> The **2-year swap rate** is **2.02%** and the **2-year U.S. Treasury** is yielding **1.61%**. What is the **swap spread**?

$$
\text{Swap spread} = 2.02\% - 1.61\% = \boxed{0.41\% \text{ or } 41 \text{ bps}}
$$

> [!NOTE]
> Swap spreads are almost always positive — banks are riskier than governments.

---

## Variant: I-Spread (Interpolated Spread)

> [!abstract]
> I-spread = bond yield minus the swap rate for the same maturity. If the swap rate for your exact maturity is missing, linear-interpolate from the swap curve first. The I-spread isolates credit and liquidity risk (time value is already in the swap rate).

> **6% Zinni, Inc. bonds** yield **2.35%** and mature in **1.6 years**. Given the swap curve: 0.5yr = 1.00%, 1yr = 1.25%, 1.5yr = 1.35%, 2yr = 1.50%. Compute the **I-spread**.

**1. Interpolate the 1.6-year swap rate**

1.6 years falls between the 1.5-year (1.35%) and 2-year (1.50%) swap rates:

$$
\text{Swap}_{1.6} = 1.35\% + \frac{1.6 - 1.5}{2.0 - 1.5} \times (1.50\% - 1.35\%)
$$

$$
= 1.35\% + \frac{0.1}{0.5} \times 0.15\% = 1.35\% + 0.03\% = \boxed{1.38\%}
$$

**2. Subtract from the bond yield**

$$
\text{I-spread} = 2.35\% - 1.38\% = \boxed{0.97\% \text{ or } 97 \text{ bps}}
$$

> [!NOTE]
> I-spread removes time value (already in the swap rate) and isolates credit + liquidity risk. Higher I-spread = riskier bond.

---

## Variant: Pricing a Risky Bond Using the Z-Spread

> [!abstract]
> Add the Z-spread to every spot rate, then discount each cash flow at that adjusted rate. If forward rates are given instead of spot rates, chain them to build spot rates first: $(1+S_n)^n = \prod (1 + f_i)$.

> A **3-year, 5% annual-pay ABC, Inc. bond** trades at a **Z-spread of 100 bps** over the benchmark spot curve. The benchmark 1-year spot rate is **3%**, the 1-year forward rate in Year 1 is **5.051%**, and the 1-year forward rate in Year 2 is **7.198%**. Compute the **bond's price**.

**1. Derive the spot rates from the forward rates**

$$
(1+S_1) = 1.03 \quad \Rightarrow \quad S_1 = 3.00\%
$$

$$
(1+S_2)^2 = (1.03)(1.05051) = 1.08203 \quad \Rightarrow \quad S_2 = 4.02\%
$$

$$
(1+S_3)^3 = (1.03)(1.05051)(1.07198) = 1.15995 \quad \Rightarrow \quad S_3 = 5.07\%
$$

*Intuition:* Spot rates chain forward rates — each forward rate extends the compounding by one more year.

**2. Add the Z-spread and discount each cash flow**

$$
P = \frac{5}{1.03 + 0.01} + \frac{5}{(1.0402 + 0.01)^2} + \frac{105}{(1.0507 + 0.01)^3}
$$

$$
P = \frac{5}{1.04} + \frac{5}{(1.0502)^2} + \frac{105}{(1.0607)^3}
$$

$$
P = 4.81 + 4.53 + 87.99 = \boxed{\$97.33}
$$

> [!NOTE]
> Z-spread is added to **every** spot rate uniformly. It assumes zero interest rate volatility — do not use it for bonds with embedded options.
