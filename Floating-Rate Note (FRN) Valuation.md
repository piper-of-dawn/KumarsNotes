# Margin Widening Example


> [!QUESTION] Question
> A floating-rate note (FRN) has a face value of **$10 million**, total maturity **6 years**, and pays coupons based on a reference rate **+ 2.5% margin**. After **2.5 years**, the issuer’s credit quality worsens, and the market now demands a **margin of 3.5%** for similar risk — a **100 bps margin widening**. The **current flat spot curve is 4.1%**, and you may assume **semiannual payments**. Compute the **fair value of the FRN today**.

# **First-Principles Breakdown**

> [!TIP] TL;DR
**“FRN Price = (Par − PV of the spread shortfall) * Notional.”**
This is the only rule you need:
If the bond pays less margin than the market requires, discount the missing margin and subtract it from par.
## **1. What makes a floating-rate bond normally worth par?**

A floating-rate bond resets its coupon every period to:

$$
\text{Reference rate} + \text{Bond’s margin}
$$

If the bond’s margin equals the **market-required margin**, the coupon always matches current market pricing.
This makes the PV of future cash flows equal to the face value:

$$
\text{FRN at reset} \rightarrow \text{Value} = 100
$$

In other words, a “fair” FRN is a par instrument.

---

## **2. What breaks this par relationship?**

If **credit quality worsens**, the **required margin rises**:

* Old margin = 2.5%
* New required margin = 3.5%
* **Shortfall = 1.0% per year**

The bond’s coupons no longer reflect fair market compensation.
Every period, it now **underpays** by the amount of the shortfall.

So the FRN must trade **below par**.

## **3. Translate the shortfall into cash flows**

Since coupons are **semiannual**:

* Annual shortfall = **1%**
* Semiannual shortfall = **0.5%**
* Shortfall per $100 = **0.5**
* Remaining time = **3.5 years**
* With semiannual payments → **7 periods**

Thus, you are missing:

$$
0.5, ;0.5, ;0.5, \ldots,; 0.5 \quad (7 \text{ times})
$$

---

## **4. Discount the missing payments using the current curve**

Flat spot = 4.1% →
Semiannual discount rate = **2.05%**

PV of missing spread:

$$
PV = 0.5 \times (DF_1 + DF_2 + \dots + DF_7)
$$

This computes to approximately:

$$
PV \approx 3.23 \text{ (per \$100 of par)}
$$

This 3.23 is the **economic loss** from holding an under-margin FRN.

## **5. Subtract this loss from par**

An FRN trades at par **minus** the PV of its margin deficiency:

$$
\text{Price} = 100 - 3.23 = 96.77
$$

For **$10 million face**:

$$
0.9677 \times 10,000,000 = \boxed{9{,}677{,}000}
$$

Rounding differences lead to the standard solution **≈ $9,697,600 (96.98%).**




