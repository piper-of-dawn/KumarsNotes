TL;DR (first-principles):
A bond’s price is just the present value of many future cashflows. The farther away a cashflow is, the more aggressively its value gets crushed when you divide by $(1+r)^t$. So if rates move even a little, the discounting shock grows exponentially with (t). Long-term bonds have many cashflows sitting far in the future → their prices react violently to rate changes. Shorter bonds don’t. Same mechanism also flips into reinvestment risk: the longer you stay in the game, the more coupon reinvestments depend on future interest rates.

---

## First Principles

### 1. What is Present Value?

Every cashflow $CF_t$ is worth:
$$
PV_t = \frac{CF_t}{(1+r)^t}
$$

Two knobs:

* **r** = discount rate
* **t** = how many times you divide by (1+r)

The impact of **t** is exponential. Small change in (r) is magnified by (t).

---

### 2. What happens if rates rise slightly?

Take derivative with respect to (r):
$$
\frac{\partial PV_t}{\partial r} = -t \frac{CF_t}{(1+r)^{t+1}}
$$

Key insight:
**The slope scales linearly with (t)** → farther payments fall *faster* when rates rise.

This single equation already tells you:

* Price sensitivity ∝ maturity
* Longer maturity → steeper negative slope → bigger price drop for same rate increase.

---

### 3. Compare 5-year vs 20-year

Identical coupon and face value. Only (t) changes.

Long bond: cashflows at $(t=1,2,\dots,20)$
Short bond: cashflows at $(t=1,2,\dots,5)$

The 20-year includes many cashflows with large (t).
So when (r) goes from, say, 4% → 5%, the discount factor jump ((1.04)^{-t} \to (1.05)^{-t}) produces:

* tiny change for (t=1)
* moderate change for (t=5)
* massive change for (t=20)

In numbers:

$$
\frac{1}{1.04^{20}} = 0.456 \quad\text{vs}\quad \frac{1}{1.05^{20}} = 0.377
$$
This is a **17.4% drop** for that distant cashflow.

For a 5-year cashflow:

$$
\frac{1}{1.04^{5}} = 0.822 \quad\text{vs}\quad \frac{1}{1.05^{5}} = 0.784
$$

Only a **4.6% drop**.

Same 1% rate change → 4× the impact on the long bond.

That is the mathematical core.

---
### 4. How this ties to duration?

Macaulay Duration:
$$
D = \frac{\sum t \cdot PV(CF_t)}{P}
$$

This is literally a **weighted average t**.
Longer bonds have:

* bigger t’s
* heavier weights on larger t
  → so duration is higher → price sensitivity is higher.

Modified duration:
$$
\frac{\Delta P}{P} \approx -D_{\text{mod}} \Delta r
$$

Higher $D_{\text{mod}}$ ⇒ steeper price drop when (r) rises.

20-year has much higher (D) than 5-year.

---

### 5. Now add reinvestment risk

Coupons get reinvested at *future* rates.
Long bonds → many coupons → long exposure to unknown reinvestment rates.

So:

* **Price risk grows with t** due to discounting convexity.
* **Reinvestment risk grows with horizon** because coupons must be rolled again and again.

These two risks are tightly linked: duration captures both.

---

## Final summary

Long-term bonds are more rate-sensitive because discounting is exponential:
((1+r)^t) blows up with (t), so small ∆r hits far-future PVs brutally.
Duration is just a clean way of aggregating this fact into one number.
More years → larger duration → bigger price fall when rates rise → larger reinvestment uncertainty.











