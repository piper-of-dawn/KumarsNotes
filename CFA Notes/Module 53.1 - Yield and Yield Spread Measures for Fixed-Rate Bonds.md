# Module 53.1 — Yield and Yield Spread Measures for Fixed-Rate Bonds (Fixed Income)

These notes summarize Schweser L1 Book 3, Reading 53, Module 53.1.

## LOS 53.a — Calculate annual yield for varying compounding periods

- Yield to Maturity (YTM): Discount rate that sets PV of cash flows equal to price.
- Periodicity: Number of coupon payments per year. Quoted YTM uses that periodicity.
  - Semiannual bond basis: quoted YTM = 2 × (semiannual discount rate).
- Effective Annual Yield (EAY): Converts quoted YTM (with periodicity n) to an annual effective rate.
  - Formula: EAY = (1 + YTM/n)^n − 1
  - Higher periodicity → higher EAY for a given quoted YTM.
- Comparing bonds with different periodicity:
  - Convert to a common basis (typically EAY) or convert between periodicities.
- Street convention vs True yield:
  - Street: assumes stated coupon dates.
  - True: shifts coupons forward when dates fall on weekends/holidays → slightly lower than street.
- Current yield (income/running yield): annual coupon / flat price.
- Simple yield: (annual coupon ± straight-line amortization of discount/premium) / flat price.
- Callable bonds:
  - Yield to call (YTC): compute for each call date/price using time to call and call price.
  - Yield to worst (YTW): min(YTM, all YTCs).
- Option-adjusted price/yield (concept): Removes embedded option value to put callable/putable and straight bonds on a consistent basis. For callable bonds, option-adjusted yield < quoted yield (option depresses price, raises quoted yield).

## LOS 53.b — Compare, calculate, and interpret yield and yield spread measures

- Yield spread (benchmark spread): Bond’s yield − benchmark yield.
  - Use nearest-maturity on-the-run government bond; if needed, linearly interpolate benchmark yield.
- G-spread: Spread over government bond yield of same/interpolated maturity.
- I-spread: Spread over swap rate (interbank market reference rate) of same tenor; common in EUR markets.
- Interpreting spread changes:
  - Yield up with spread unchanged → macro factors (benchmark moved: real rate/inflation).
  - Spread widens/narrows → micro factors (credit, liquidity, taxation) changed.

### Zero-Volatility Spread (Z-spread)

- Constant spread added to every point on the benchmark spot curve so PV(cash flows discounted at spot + Z) = price.
- More precise than G-/I-spread because it respects the term structure (spot rates for each cash flow).

### Option-Adjusted Spread (OAS)

- For bonds with embedded options; Z-spread with the option value removed.
- Relationships:
  - Callable: OAS = Z-spread − option value → OAS < Z-spread.
  - Interprets compensation for credit/liquidity/taxation risks excluding optionality.

## Quick formulas and tips

- EAY from quoted YTM with periodicity n: (1 + YTM/n)^n − 1.
- Current yield = annual coupon / flat price.
- Simple yield ≈ (annual coupon ± annual straight-line amortization) / flat price.
- Holding EAY constant: higher periodicity → lower quoted YTM.
- G-spread = YTM_bond − YTM_gov (same/interpolated maturity).
- Z-spread: solve Z so Σ[CF_t / (1 + spot_t + Z)^t] = price.
- Callable bonds: YTW = min(YTM, YTC_1, YTC_2, …).

## Mini examples (from module)

- Semiannual to annual comparison: YTM 4% (semiannual) → periodic 2% → EAY = 1.02^2 − 1 = 4.04%. Quarterly-equivalent quoted ≈ 4 × (1.02^(1/2) − 1) ≈ 3.98%.
- Current yield: 6% coupon, price 802.07 → 60 / 802.07 = 7.48%.
- G-spread: Bond YTM 6.82%, interpolated gov 4.33% → 249 bp.
- Callable vs OAS: Z-spread 180 bp, option value 60 bp → OAS 120 bp.

