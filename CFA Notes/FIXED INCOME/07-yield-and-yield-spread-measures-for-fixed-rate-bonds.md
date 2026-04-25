### MODULE 7: Yield and Yield Spread Measures for Fixed-Rate Bonds

> Source module: `/home/karma/CFAPractice/mcq/quiz/AI/PDF/FixedIncome/module_07_yield_and_yield_spread_measures_for_fixed_rate_bonds.txt`

1. Yield to maturity (YTM): the single rate that makes the present value of all coupon and principal payments equal to today’s price. For semiannual coupons, the quoted YTM is 2 × (half‑year rate).
2. Periodicity and effective annual yield (EAY): more coupon periods per year means more compounding. Always compare bonds on EAY if payment frequency differs.
3. Street vs true yield: street uses stated coupon dates; true shifts payments that land on weekends/holidays to the next business day, making true yield slightly lower.
4. Income measures: current yield = annual coupon ÷ flat price. Simple yield adjusts current yield for straight‑line amortization of discount/premium.
5. Calls and “worst” yield: compute a yield to call (YTC) for each call date/price. Yield to worst (YTW) is the lowest of YTM and all YTCs.
6. Spreads to benchmarks: G‑spread = bond yield minus government yield (same or interpolated maturity). I‑spread = bond yield minus swap rate (same tenor).
7. Reading spread moves: if the bond yield changes but its spread does not, the benchmark moved (economy‑wide). If the spread changes, the issuer/issue changed (credit, liquidity, tax).
8. Curve‑aware spreads: Z‑spread is the constant number of basis points added to every point on the benchmark spot curve so discounted cash flows equal price. For embedded options, option‑adjusted spread (OAS) removes the option’s effect. For callables: OAS < Z‑spread.

> [!ABSTRACT] MEMORISE
> Effective annual yield (periodicity n):
>
> $$\mathrm{EAY} = \left(1 + \frac{y}{n}\right)^{n} - 1$$
>
> Current and simple yield:
>
> $$\text{Current} = \frac{\text{Annual coupon}}{\text{Flat price}},\quad \text{Simple} \approx \frac{\text{Annual coupon} \pm \text{Annual amortization}}{\text{Flat price}}$$
>
> Government spread (G‑spread):
>
 > G SPREAD =  Bond Yield − Government Yield (same maturity)
 > 
 > 
 > Zero Volatility Spread (Z-Spread) 
> 
> Z‑spread over spot curve (solve for Z so price matches):
>
> $$\sum_{t=1}^{T} \frac{CF_t}{\big(1 + s_t + Z\big)^{t}} = \text{Price}$$
>
> Callable bonds - option‑adjusted spread:
>
> OAS = Z‑spread − Option cost
>
> Yield to worst:
>
> $$\text{YTW} = \min\big(\,\text{YTM},\ \{\text{YTC}_i\}\,\big)$$
>
> Notation in simple language: y = quoted YTM; n = coupons/year; s_t = benchmark spot rate at time t; Z = Z‑spread (in decimal); bp = basis points (1 bp = 0.01%).

> [!tip] Quick checks
> - Hold EAY fixed: higher periodicity → lower quoted YTM.
> - “Yield moved, spread didn’t” → benchmark moved (economy‑wide).
> - “Spread moved” → issuer/issue changed (credit/liquidity/tax).
> - Callable: YTW is the smallest among YTM and all YTCs.
> - Interpolate the benchmark yield when exact maturity is missing.

> [!question] ZERO‑COUPON: QUOTED YTM (SEMIANNUAL BASIS)
> 
> Problem A 15‑year zero with $1,000 par trades at $331.40. Find the quoted YTM on a semiannual bond basis.
> 
> ---
> 
> Solution:
> $$N=30,\ PMT=0,\ FV=1000,\ PV=-331.40 \Rightarrow I/Y_{\tfrac{1}{2}\,yr}=3.750\%$$
> Quoted YTM = 2 × 3.750% = \textbf{7.500%}.
> Explanation: The calculator’s I/Y is per half‑year; bond‑basis quotes double it.

> [!question] G‑SPREAD WITH INTERPOLATED BENCHMARK
> Problem: A 3‑year, 8% semiannual‑pay bond is priced at 103.165. Treasury 1y = 3.0%, 4y = 5.0%. Compute the G‑spread.
>
---

> Solution:
> Bond YTM: $N=6,\ PMT=4,\ FV=100,\ PV=-103.165 \Rightarrow$ I/Y (per half‑year) = 3.408% → quoted = \textbf{6.82%}.
> Interpolated 3y Treasury: $3.0 + \tfrac{(3-1)}{(4-1)} (5.0-3.0) = \textbf{4.33\%}.$
> G‑spread = 6.82 − 4.33 = \textbf{2.49% (249 bp)}.
> Explanation: Use nearest on‑the‑run government yields and linear interpolation for the missing maturity.
