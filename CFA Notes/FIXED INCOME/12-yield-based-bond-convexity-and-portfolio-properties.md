### MODULE 12: Yield-Based Bond Convexity and Portfolio Properties

> Source module: `/home/karma/CFAPractice/mcq/quiz/AI/PDF/FixedIncome/module_12_yield_based_bond_convexity_and_portfolio_properties.txt`

#### Extracted Notes 1

#### Convexity of the Yield Curve

##### What is a convex function?
If $f(x)$ is twice differentiable then $f''(x) > 0$.

##### What does it mean?
In terms of rate of change, convexity means the rate of change itself is increasing; that is, acceleration is positive.

##### Convexity of the Yield Curve
Suppose we have a 1-period zero coupon bond.
$$ P  = FV (1+r)^{-t} $$
$$ \frac{dP}{dr} = -t(1+r)^{-t-1}\cdot FV < 0 $$
$$ \frac{d^2P}{dr^2} = t(t+1)(1+r)^{-t-2}\cdot FV > 0 $$
We see that the first derivative is negative and the second derivative is positive. Therefore, the function decreases at a decreasing rate. The positive second derivative implies that the slope is approaching zero, so the function is decelerating.

##### What does this mean intuitively?
At higher levels of yield, a small decline in yield causes a larger increase in bond price; at lower yields, the same decline will cause a smaller increase.

##### What is its implication?
In a high-yield environment, long-duration bonds (e.g., TLT) will gain sharply as yields fall.

##### Question
A non-callable, fixed-coupon bond has a price of 106.0625 and a YTM of 2.8%. If the YTM were to increase instantaneously by 80 bps, the price of the bond would decrease by 11%. If the YTM were to decrease instantaneously by 80 bps, the price of the bond would increase by:

#### Extracted Notes 2

> [!abstract] MEMORISE
> - Duration is the slope. Convexity is the bend.
> - For an option-free fixed-rate bond, convexity is positive and valuable.
> - Price accelerates as yields fall.
> - Longer maturity, lower coupon, and lower yield all increase convexity.
> - Portfolio convexity from weighted averages is practical, but it quietly assumes a parallel curve shift.

1. Duration alone is only half the story. It tells you the **first-order** effect of yield changes on price, which is just the slope of the price-yield relationship.
2. Convexity is the **second-order** effect. It tells you how that slope itself changes as yield moves. In plain English: duration gives the straight-line estimate, convexity fixes the miss because the real price-yield relationship is curved.

> [!info] Example
> Think of a long government bond when yields fall sharply. Duration says the price should rise by some amount. But the actual bond usually rises **even more** because the price-yield curve bows outward. That extra pop is convexity doing its job.
> 
> ![[module58_convexity_curve.svg]]

3. This is why convexity matters more for **larger** yield changes. For tiny moves, the straight-line duration approximation is fine. For bigger moves, ignoring curvature starts making you look silly.
4. For an option-free fixed-rate bond, convexity is always positive. That is good news for you as an investor:
   - when yields fall, price rises **more** than duration alone predicts
   - when yields rise, price falls **less** than duration alone predicts
5. That is why convexity is valuable. It makes the bond less nasty on the downside and more generous on the upside. But markets know this, so you usually pay for more convexity through a higher price and lower yield.

##### THE FORMULA LOGIC

> [!abstract] MEMORISE
> - Duration term = main move.
> - Convexity term = always additive for an option-free bond.
> - Convert basis points to decimals before touching the formula.
> - Bigger yield move = convexity matters more.

6. The standard approximation is:
$$
\% \Delta PV_{\text{Full}} \approx (-\text{AnnModDur} \times \Delta \text{Yield}) + \left(\tfrac{1}{2} \times \text{AnnConvexity} \times (\Delta \text{Yield})^2\right)
$$
7. Read it like this:
   - first term = duration effect
   - second term = convexity adjustment
8. The convexity adjustment gets added to the duration estimate. Because convexity is positive for an option-free fixed-rate bond, this term helps you on both sides.

> [!info] FOR THE MATH GUYS
> - Duration is the **first derivative** of price with respect to yield.
> - Convexity is the **second derivative**.
> - This price-change formula is just a **second-order Taylor expansion** around the current yield.
> - Linear term first, curvature correction second.

> [!question] PRICE CHANGE WITH CONVEXITY
> Problem: A GBP 50,000,000 position in a 10-year 3.50% bond has annualized modified duration of 8.376 and annualized convexity of 81.701. Yields fall by 100 basis points. Estimate the percentage price change.
> 
> Duration effect: $-8.376 \times (-0.01) = +0.08376 = +8.376\%$
> Convexity adjustment: $\tfrac{1}{2} \times 81.701 \times (0.01)^2 = 0.004085 = +0.4085\%$
> Estimated total price change: about **+8.78%**
> **Takeaway:** when the move is large, convexity is not decoration. It adds real money.

9. Money convexity is just convexity translated into currency terms. Instead of saying “the bond has convexity 81.701,” you ask “how many pounds or euros is that worth for this position size?”
10. The idea is simple:
$$
\text{Money Convexity} = \text{Annual Convexity} \times PV_{\text{Full}}
$$
11. Then the money convexity adjustment is:
$$
\text{Money Convexity Adjustment} \approx \tfrac{1}{2} \times \text{Money Convexity} \times (\Delta \text{Yield})^2
$$

> [!question] MONEY CONVEXITY
> Problem: Use the same GBP 50,000,000 bond position with annualized convexity 81.701 and a 100 basis point rate decline. What is the money convexity adjustment?
> 
> Money convexity: $81.701 \times 50{,}000{,}000 \approx GBP\ 4.085$ billion
> Money convexity adjustment: $\tfrac{1}{2} \times 4.085$ billion $\times (0.01)^2 \approx GBP\ 204{,}252$
> **Takeaway:** that “small” convexity term can still mean more than GBP 200k on a big position.

##### WHAT MAKES CONVEXITY BIGGER

> [!abstract] MEMORISE
> - Longer maturity = more convexity.
> - Lower coupon = more convexity.
> - Lower yield-to-maturity = more convexity.
> - Same story as duration, just even more curved.

12. Bond features that increase convexity are the same ones that increase duration:
   - longer time to maturity
   - lower coupon rate
   - lower yield-to-maturity
   - **Longer time to maturity:** more of the bond’s value sits far out in the future, and distant cash flows react more dramatically when discount rates move. Long bonds live on the bendier part of the curve.
   - **Lower coupon rate:** less cash comes back early, so more of the bond’s value is pushed into the final principal payment. That makes the bond behave more like a zero-coupon bond, which is highly curved.
   - **Lower yield-to-maturity:** when discount rates are already low, the price-yield curve becomes steeper and more curved. A small change in yield now moves present values more violently.
12. There is one extra intuition point: if two bonds have the same duration, the one whose cash flows are spread out more over time has higher convexity.
13. The numbers make the point very clearly:
   - Romanian 30-year bond: approximate modified duration about **15.91**, approximate convexity about **369.64**
   - BRWA 5-year bond: approximate modified duration about **4.59**, approximate convexity about **24.24**
15. That gap is huge. Same basic asset class, but the long bond is living in a much more curved world.

##### PORTFOLIO PROPERTIES

> [!abstract] MEMORISE
> - Portfolio duration and convexity are usually taken as market-value-weighted averages.
> - That is practical, not perfectly “theoretical.”
> - The hidden assumption is a parallel shift in the yield curve.
> - Real curves rarely move that politely.

16. In practice, portfolio managers usually calculate portfolio duration and convexity by taking the weighted averages of the durations and convexities of the individual bonds. This is easy and useful, which is exactly why everyone does it.
17. But the curriculum makes an important distinction: the **theoretically correct** method is to calculate duration and convexity from the weighted average time to receipt of the **aggregate cash flows** of the whole portfolio.
18. The weighted-average-of-bonds method is common because it is practical, but it quietly assumes a **parallel yield curve shift**.

> [!info] Example
> Silicon Valley Bank is the brutal real-world reminder. It stuffed itself with long-duration Treasury and mortgage-backed securities when yields were low. Then rates ripped higher in 2022–2023, the value of those bonds sank, and the unrealized losses became terrifying once depositors started pulling cash. The main villain here was **duration** because it drove the big price hit. Convexity matters too, but as the second-order amplifier: long bonds live on a more curved part of the price-yield relationship, so big rate moves become even less forgiving.
> <img src="https://commons.wikimedia.org/wiki/Special:Redirect/file/SVB%20stock%20price.webp" alt="SVB stock price collapse" width="480" style="display:block; margin-top:8px; border-radius:8px;" />

> [!question] PORTFOLIO CONVEXITY
> Problem: A EUR 100 million portfolio holds Bond A at 40% weight with modified duration 2.858 and convexity 9.752, and Bond B at 60% weight with modified duration 8.376 and convexity 81.701. Yields rise by 50 basis points. Estimate the portfolio percentage price change.
> 
> Portfolio modified duration: $(0.4 \times 2.858) + (0.6 \times 8.376) = 6.169$
> Portfolio convexity: $(0.4 \times 9.752) + (0.6 \times 81.701) = 52.921$
> Estimated price change: $(-6.169 \times 0.005) + \left(\tfrac{1}{2} \times 52.921 \times 0.005^2\right) \approx -3.018\%$
> **Takeaway:** weighted averages make portfolio risk estimation fast, but they still rest on the parallel-shift assumption.

> [!tip] QUICK CHECKS
> - Convexity is the curvature correction to duration.
> - For an option-free fixed-rate bond, convexity is positive.
> - More convexity helps you in both yield directions.
> - Longer maturity, lower coupon, lower yield = more convexity.
> - Portfolio weighted averages are practical but assume parallel shifts.
