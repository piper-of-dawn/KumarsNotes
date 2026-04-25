### MODULE 9: The Term Structure of Interest Rates: Spot, Par, and Forward Curves

> Source module: `/home/karma/CFAPractice/mcq/quiz/AI/PDF/FixedIncome/module_09_the_term_structure_of_interest_rates_spot_par_and_forward_curves.txt`

#### Forward Rates - Intuition and No-Arbitrage

- Why “forward”: It is the implied rate for a future period, inferred today from longer-dated spot yields.
- No-arbitrage relation (annual compounding example):
  (1 + S2)^2 = (1 + S1) × (1 + 1y1yF)
  → 1y1y forward = (1 + S2)^2 / (1 + S1) − 1.
- Interpretation: Being indifferent between buying a 2-year zero today vs. rolling 1-year zero for two years implies this equality; otherwise, arbitrage exists.

Par rate:  The yield-to-maturity for a given maturity that makes the present value of the bond’s cash flows equal to par (100% of face value).
#### Maturity Effect - Volatility Across Horizons

- Short-term rates/yields are typically more volatile than long-term rates because they reflect immediate policy and liquidity conditions, while long-term rates embed an average of expected short rates plus a term premium.
- **Term premium** compensates for uncertainty over long horizons; as maturity increases, instantaneous shocks are averaged across many expected future short rates, dampening volatility relative to short maturities.

Note: Premium bonds often have effective durations below time-to-maturity, as larger near-term coupons bring cash flows forward, reducing sensitivity to rate changes.
