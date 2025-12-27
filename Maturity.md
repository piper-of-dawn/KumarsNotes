
Long term bonds have a larger maturity risk because even minor interest rate changes snowball to a bigger impact on bond price because of compounding. This is closely related to reinvestment risk.

Compare 5 year with a 20 year bond. 

A rise in interest rate will cause a larger decline in  price of the 20 year bond that a 5 year bond. 

Mathematically understand this:

**Portfolio A**
Take a bond of FV = $1 with a 5% coupon and 3 year maturity. It will generate cashflows: 0.5, 0.5, 1.05 in succeeding 3 years. 

**Portfolio B**
But a 1 year zero coupon bond (ZCB) of FV = 0.5, a 2 year ZCB of FV = 0.5 and 3 year ZCB of FV = 1.05.

Both portfolios generate the same cashflows and hence should have same price otherwise there will be free money.

This is also known as **stripping a zero coupon bond.** This is called Strips. 

The PV of Portfolio A would be

$$ P_A = \frac{0.5}{(1+y)^1} + \frac{0.5}{(1+y)^2} + \frac{1.05}{(1+y)^3} $$

The PV of Portfolio B would be
$$ P_B = \frac{0.5}{(1+s_1)^1} + \frac{0.5}{(1+s_2)^2} + \frac{1.05}{(1+s_3)^3} $$

**Spot Rate** 
It is the [[Yeild to Maturity]] of a Zero Coupon Bond. Spot rate is also called **Discount Factor**

| ZCB Maturity | Purchase Price | Spot Rate |
|--------------|----------------| - |
| 1 year       | 980 | 
| 2 year       | 945 |
| 3 year       | 901 |
| 4 year       | 845 |



> [!TIP] Somewhat Useless Fact
> Zero coupon bond is also called deep discount or a pure discount bond.







## Maturity Effect
The maturity effect states that short-term interest rates (and thus short-maturity bond yields) are more volatile than long-term rates.
**Why?** This is because the short term interest rates are sensitive to immediate market conditions and monetary policy changes that might fluctuate frequently. On the other hand, long term rates represent an average of expected of the short rates.

$$ e_\text{long} = E(r_\text{short}) + \text{term premium} $$

> [!INFO] Why would maturity effect ALWAYS hold for bonds that trade at premium?
> If a bond is trading at a premium, which means its effective duration is lesser than its maturity. In simple words, it will generate large share of cashflows sooner. This effectively reduces the long term uncertainty for these bonds and hence these are less volatile and exceptions to maturity won't happen.


> [!INFO] What happens to convexity as bond approaches maturity?
>As a bond approaches maturity, **its convexity decreases**.
>**Reason:**
>- Fewer remaining cash flows → less sensitivity to interest rate changes.
>- Duration shortens, and the **price–yield curve flattens** toward a straight line.
> 
> **In the limit:**  
At maturity, the bond’s value = face value → **no curvature, convexity = 0.



