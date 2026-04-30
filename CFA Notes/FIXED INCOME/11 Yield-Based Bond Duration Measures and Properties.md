
> [!abstract] SEE THIS BEFORE EXAM
> - Duration is the bond’s interest-rate sensitivity meter.
> - Macaulay duration = weighted-average time to cash flows.
> - Modified duration = percentage price sensitivity to a change in the bond’s own yield.
> - Money duration and PVBP translate that sensitivity into actual currency moves.

1. Duration exists because bond prices and yields move in opposite directions, but not all bonds move by the same amount. A tiny 1-year zero barely flinches. A long 30-year bond can get slapped around.
2. So duration is just a cleaner answer to one question: **if yield moves, how hard does this bond’s price get hit?**

##### THE DURATION FAMILY

> [!abstract] MEMORISE
> - Macaulay = time.
> - Modified = percentage price move.
> - Money duration = currency move.
> - PVBP = price move for 1 basis point.

3. Macaulay duration is the **present-value-weighted average time** to receive the bond’s cash flows. It is still a time concept, not directly a price-change concept.
4. Modified duration is what traders care about more day to day. It converts Macaulay duration into **price sensitivity**:
$$
\text{ModDur} = \frac{\text{MacDur}}{1+r}
$$
5. Read that in plain English: modified duration tells you the approximate **percentage change in full price** for a change in the bond’s own yield-to-maturity.
6. The key approximation is:
$$
\% \Delta PV_{\text{Full}} \approx - \text{AnnModDur} \times \Delta \text{AnnYield}
$$
7. The minus sign is the whole bond market in one symbol: yields up, prices down; yields down, prices up.

> [!info] FOR THE MATH GUYS
> - Modified duration is the **first derivative** of bond price with respect to yield.
> - It is the slope of the price-yield curve at today’s yield.
> - Bigger slope in absolute value = more interest-rate risk.
> - This is still a linear approximation, not the full curved story.

8. If a bond has modified duration of 5, then a 100 basis point rise in yield means roughly a **5% price drop**. That is the quick-and-dirty mental math.
9. This is why higher modified duration means higher interest-rate risk. The price-yield line is steeper.

##### APPROXIMATE MODIFIED DURATION

> [!abstract] MEMORISE
> - Shock yield up a bit, shock yield down a bit, and measure the slope.
> - This approximation is extremely close for plain bonds.
> - It also becomes useful later when closed-form duration is messy.

10. You do not always need to compute modified duration through Macaulay duration first. You can estimate it directly from prices:
$$
\text{AnnModDur} \approx \frac{PV_- - PV_+}{2 \times \Delta \text{Yield} \times PV_0}
$$
11. Meaning:
   - $PV_0$ = current full price
   - $PV_+$ = price after a small yield increase
   - $PV_-$ = price after a small yield decrease
12. This is just the slope estimate from a tiny bump up and tiny bump down in yield.

> [!question] BRWA MODIFIED DURATION
> Problem: A 5-year BRWA bond has annualized modified duration of 4.58676. What is the estimated percentage price change if its yield rises by 80 basis points?
> 
> $\% \Delta PV_{\text{Full}} \approx -4.58676 \times 0.008 = -0.0367$
> Estimated price change: about **-3.67%**
> If yield falls by 80 basis points, the estimate flips to **+3.67%**
> **Takeaway:** duration gives equal-and-opposite estimates because it is a straight-line approximation.

##### MONEY DURATION AND PVBP

> [!abstract] MEMORISE
> - Modified duration gives percentage move.
> - Money duration gives cash move.
> - PVBP gives the price move for a 1 basis point shift.
> - Big portfolio + modest duration can still mean ugly money losses.

13. Money duration is just modified duration translated into position size:
$$
\text{MoneyDur} = \text{AnnModDur} \times PV_{\text{Full}}
$$
14. So instead of saying “the bond may move 4.3%,” you say, “this position may gain or lose EUR 4.3 million per 100 bp move,” depending on the position size.
15. The price change in currency terms is:
$$
\Delta PV_{\text{Full}} \approx - \text{MoneyDur} \times \Delta \text{Yield}
$$
16. PVBP, the price value of a basis point, is the estimated price change for a **1 bp** change in yield. It is just a tiny money-duration slice:
$$
\text{PVBP} \approx \text{MoneyDur} \times 0.0001
$$

> [!info] Example
> A bond can look “safe” because it is high quality, but if the position is huge, money duration can still be savage. That is how apparently boring rate moves turn into tens of millions of portfolio pain.

> [!question] MONEY DURATION
> Problem: A bond has annualized modified duration of 4, price 95, and yield rises by 50 basis points. Estimate the change in price per 100 of par.
> 
> Money duration = $4 \times 95 = 380$
> Price change $\approx -380 \times 0.005 = -1.90$
> **Takeaway:** percentage sensitivity becomes real money very quickly.

##### WHAT CHANGES DURATION

> [!abstract] HAMMER THIS
> - Longer maturity = more duration.
> - Lower coupon = more duration.
> - Lower yield = more duration.
> - Duration falls as the bond rolls toward maturity.

17. All else equal, a bond’s interest-rate risk rises when:
   - time to maturity is longer
   - coupon rate is lower
   - yield-to-maturity is lower
18. The intuition for **longer maturity** is simple: more of the bond’s value sits far in the future, and distant cash flows get hit harder when discount rates change.
19. The intuition for **lower coupon** is that less cash comes back early, so more of the value gets pushed into the final principal payment. That makes the bond behave more like a zero-coupon bond, which is more rate-sensitive.
20. The intuition for **lower yield** is that the discounting is gentler, so future cash flows keep more weight in today’s price. When those future-heavy cash flows dominate, duration rises.

> [!info] Example
> It was 1994. Bond investors had gotten comfortable. Rates had been calm, carry felt easy, and long bonds looked like safe, sleepy money. Then the Federal Reserve started tightening faster than the market expected. Yields jumped. And suddenly the trap snapped shut. The longest-duration bonds got hit the hardest because their cash flows were sitting far out in the future, where discount-rate changes do the most damage. That is the duration lesson in blood: you do not need default to get wrecked. If duration is huge and yields rise fast, price losses can turn savage very quickly.
> <img src="https://cdn.substack.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fa3730565-4d29-4966-bf59-2236a16478cc_604x772.png" alt="Chart from Adam Tooze article on the 1994 bond market massacre" width="220" style="display:block; margin-top:8px; border-radius:8px;" />

21. Duration is not static. As a bond moves closer to maturity, duration falls. Time itself slowly bleeds interest-rate risk out of the bond.
22. One subtle exam point: if yield is negative, modified duration can actually be **greater** than Macaulay duration because you are dividing by a number less than 1.
23. Another exam point: for a zero-coupon bond, Macaulay duration equals maturity, but modified duration is still **less** than maturity when yield is positive.

> [!tip] QUICK CHECKS
> - Macaulay = time; modified = percentage sensitivity.
> - Use full price, not flat price, in duration work.
> - Convert basis points to decimals before multiplying.
> - Bigger duration means steeper price response.
> - Long maturity, low coupon, low yield = higher duration.

> [!warning] DO NOT DO THIS
> - Don’t confuse Macaulay duration with modified duration.
> - Don’t forget the minus sign in the price-change approximation.
> - Don’t use flat price when the formula is about full price.
> - Don’t assume duration stays constant as the bond ages.
