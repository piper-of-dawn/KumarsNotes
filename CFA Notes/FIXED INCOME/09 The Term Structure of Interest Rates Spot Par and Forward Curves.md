### MODULE 9: The Term Structure of Interest Rates: Spot, Par, and Forward Curves

> Source module: `/home/karma/CFAPractice/mcq/quiz/AI/PDF/FixedIncome/module_09_the_term_structure_of_interest_rates_spot_par_and_forward_curves.txt`

> [!ABSTRACT] LOS
> 1. Define spot rates and the spot curve, and calculate the price of a bond using spot rates.
> 2. Define par and forward rates, and calculate par rates, forward rates from spot rates, spot rates from forward rates, and the price of a bond using forward rates.
> 3. Compare the spot curve, par curve, and forward curve.

> [!tip] SEE THIS BEFORE EXAM
> - Spot-rate bond pricing:
> $$
> PV = \frac{PMT}{(1 + Z_1)^1} + \frac{PMT}{(1 + Z_2)^2} + \cdots + \frac{PMT + FV}{(1 + Z_N)^N}
> $$
> - Par-rate equation:
> $$
> 100 = \frac{PMT}{(1 + Z_1)^1} + \frac{PMT}{(1 + Z_2)^2} + \cdots + \frac{PMT + 100}{(1 + Z_N)^N}
> $$
> - Forward-rate equation:
> $$
> (1 + Z_A)^A \times (1 + IFR_{A,B-A})^{B-A} = (1 + Z_B)^B
> $$
> - Spot from one-year forwards:
> $$
> (1 + Z_N)^N = (1 + 0y1y)(1 + 1y1y)\cdots(1 + (N-1)y1y)
> $$
> - **Price a 3-year 5% bond with 2%, 3%, 4% spot rates.** Match each cash flow to its own date: $5/1.02 + 5/1.03^2 + 105/1.04^3 = 102.960$.
> - **If price is 102.960 and coupon is 5%, what must be true about yield-to-maturity?** Above par means yield-to-maturity is below coupon.
> - **Spot rates 5.263% and 5.616%: 2-year par rate?** Set price to 100, solve for $PMT = 5.606$, so par rate is **5.606%**.
> - **3-year spot 3.65%, 4-year spot 4.18%: 3y1y?** Use the 3-year and 4-year spot rates. Answer: **5.79%**.
> - **If the label is 2y3y, what maturities do you use?** Start in year 2, end in year 5, so use the **2-year and 5-year spot rates**.
> - **Forward rates 0y1y 1.88%, 1y1y 2.77%, 2y1y 3.54%, 3y1y 4.12%: 4-year spot rate?** Multiply the path, then take the fourth root. Answer: **3.0741%**.
> - **Price a 4-year 3.75% bond from those forward rates. What is the trap?** Discount by the whole path to each date, not only the last forward rate. Answer: **102.637**.
> - Big gotcha: each cash flow gets its own spot rate.
> - Big gotcha: par pricing uses **price = 100**. Between coupon dates, use **flat price = 100**.
> - Big gotcha: short-term discount-rate quotes must be converted to bond-equivalent yields before you mix them into the curve.
> - Big gotcha: positive upward spot curve means **par below spot, forward above spot**.
> - Big gotcha: negative and upward sloping can coexist, and forward rates can still be positive.

> [!ABSTRACT] MEMORISE
> - Spot rates are the no-arbitrage discounting truth by date.
> - Par rates and forward rates are derived from spot rates.
> - Spot pricing and forward pricing must agree.
> - If you decode the cash-flow story first, the formulas become mechanical.

1. Earlier bond math often used one discount rate, like yield-to-maturity, but this module says that is only a shortcut.
2. The term structure of interest rates is the relationship between interest rates and time-to-maturity.
3. The cleanest version of the term structure comes from default-risk-free zero-coupon government bonds.
4. What is a spot rate: the discount rate for one cash flow on one maturity date. Why is it used: one cash flow gives the cleanest no-arbitrage discount rate for that date.
5. The spot curve is the collection of spot rates across maturities, and it is also called the zero curve or strip curve.
6. Spot rates matter because they let you price each cash flow with the rate appropriate to its own date instead of forcing one summary rate on every cash flow.
7. Not every yield difference comes from maturity alone; credit, currency, liquidity, tax treatment, periodicity, and maturity can all move yields.
8. In theory, the ideal curve uses default-risk-free zero-coupon government bonds.
9. In practice, analysts usually use recently issued, liquid government coupon bonds, avoid stale seasoned bonds where possible, and fill missing maturities with interpolation.
10. Short-term government instruments may be quoted on a discount-rate basis, so they must be converted to bond-equivalent yields before being compared with coupon bonds.
11. All yields on the curve must use a consistent periodicity or compounding convention before you compare them.
12. Spot-rate pricing is no-arbitrage pricing because each cash flow is discounted at the market rate for its own date.
13. For an annual-pay bond, write each cash flow by year, match it to the spot rate for that year, discount separately, and add the present values.
14. If a bond is riskier than the government curve, a spread must be added to the spot rates.
15. Yield-to-maturity is still useful, but it is only one internal-rate-of-return summary number that reproduces the total bond price.
16. Spot-rate pricing is more precise because the first coupon, second coupon, and principal repayment usually deserve different discount rates.
17. Two very different curve shapes can still give the same bond price if the spot rates attached to the largest cash flows, especially the final one, are similar enough.
18. A par rate is the yield-to-maturity and coupon rate that would make a hypothetical bond trade exactly at par value.
19. What is par used for: it strips away the noise from actual premium and discount bonds and creates a cleaner benchmark curve.
20. To solve a par-rate question, set price equal to 100, treat the coupon payment as the unknown, discount all coupon dates with the spot rates up to maturity, solve for the coupon payment, and divide by 100.
21. Between coupon dates, the curriculum uses flat price equal to 100, not full price, for the par-rate setup.
22. For a bond priced at par, coupon rate equals yield-to-maturity equals par rate; for a premium or discount bond, that identity does not hold.
23. An implied forward rate is a future-period rate backed out from today’s spot rates.
24. What is the economic meaning of a forward rate: it is the breakeven reinvestment rate that makes two maturity strategies equally attractive under no arbitrage.
25. The label format is mechanical: in 2y3y, the forward starts after 2 years and lasts 3 years, so the end date is year 5.
26. To solve a forward-rate label, decode start year, add tenor to get end year, pull the start-maturity and end-maturity spot rates, and then use the forward-rate equation.
27. Forward rates from spot rates come from the no-arbitrage relation between shorter and longer zero-coupon investment paths.
28. A spot rate can also be recovered from one-year forward rates by multiplying the whole forward path and then taking the geometric-average root.
29. Do not memorize "geometric average" like dead jargon; think "one constant annual rate that matches the whole chained path."
30. You can price a bond directly from forward rates because the forward path compounds into the same spot discount factor path.
31. To price with forward rates, discount each cash flow by the full chain from today to that cash-flow date, not just by the last forward rate in the chain.
32. Spot pricing and forward pricing must give the same bond value if your arithmetic and label decoding are correct.
33. The curriculum compares spot, par, and forward curves because their shapes are mechanically connected.
34. If the spot curve is positive and upward sloping, the par curve will usually sit below the spot curve and the forward curve will sit above it.
35. Why par is below spot in that case: earlier coupons are discounted at lower short-term rates, so the bond does not need as high a coupon as the final long spot rate to trade at par.
36. Why forward is above spot in that case: if the average rate rises with maturity, the marginal future rates must be higher than the current average.
37. If the spot curve is flat, spot, par, and forward all collapse into the same line.
38. If the spot curve is downward sloping or inverted, the par curve will usually sit above the spot curve and the forward curve below it.
39. Forward curves below spot in an inverted structure simply mean the market-implied future short rates are lower than today’s shorter rates.
40. Negative spot rates do not break the math; the same formulas still work.
41. A curve can be negative and still upward sloping if rates move from very negative to less negative as maturity extends.
42. In that case, forward rates can even become positive, and the par curve can sit above the spot curve, so you cannot blindly reuse the positive-rate rule.
43. The practical exam map is: spot rates discount one dated cash flow, par rates make a whole bond trade at 100, and forward rates price a future period hidden between two spot rates.
44. The first solving reflex should be "what cash flow story am I being asked to price?" not "which formula do I panic-memorize?"
45. If the question is spot-rate pricing, match each cash flow to its own date.
46. If the question is par-rate calculation, force price to 100 and solve for the coupon.
47. If the question is forward-rate calculation, decode the forward label before touching the algebra.
48. If the question is spot from forward rates, multiply the path and compress it into one annual rate.
49. The final exam reflex is simple: start with the cash-flow story, then the date structure, then the formula, because in this module the formulas are only shorthand for the cash-flow logic.
