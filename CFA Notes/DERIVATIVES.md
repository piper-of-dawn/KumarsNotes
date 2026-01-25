## DERIVATIVES

### MODULE 70.1: PRICING AND VALUATION OF FORWARD CONTRACTS AND FOR AN UNDERLYING WITH VARYING MATURITIES


> [!question] Implied Forward Rate
  > Consider two zero-coupon bonds, one that matures in two years and one that matures in three years, when Z2 = 2% and Z3 = 3%. Calculate the implied 1-year forward rate two years from now, F(2,1).
  > 
  > $$ F(2,1) = ((1.03)^3 / (1.02)^2) - 1 = 0.052$$
 
 1. **Forward Rate Agreement:** It is a forward on interest rates. Think forward on bonds. Long FRA ⟶ I will buy a bond from you at fixed price **(fixed rate)** in the future, in essence, **I lock in a fixed rate**. Short FRA ⟶ You sell a bond, in essence, **you are exposed to floating rate** because you have committed a fixed rate to me.

> [!tip] HAMMER THIS INTO YOUR HEAD
 > For all numericals related to settlement amount, first calculate tau ($\tau$), that is the duration in years for FRA, eg: FRA(3m,4m) has $\tau=4/12=0.33$ 
 > Then, Settlement Amount (Short pays Long) is calculated as
 > $$ S = P \times \frac{(R-K)\tau}{1+R\tau} $$
 > where $R$ is the realised rate, $K$ is the implied forward rate and $P$ is notional
 


 
> [!question] FRA
> Consider a 3-month forward on a 6-month MRR $(F_{3m6m})$ with a notional principal of $1 million. Assume that the current 3-month MRR is 1.0% and 9-month MRR is 1.2%. Realised 6-month MRR is 1.5%. Calculate settlement amount.  
> 
>  


> [!question] FRA
> Consider a **1-month forward on a 3-month MRR** (F1m3m) with notional principal **$5,000,000**. Current **1-month MRR = 2.10%** and **4-month MRR = 2.40%**. Realised **3-month MRR = 2.85%** at the end of 1 month. Calculate the **cash settlement at expiry (in 1 month)**.
