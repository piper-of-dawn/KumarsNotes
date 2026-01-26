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

### MODULE 71.1: FUTURES VALUATION

LOS 71.a: Compare the value and price of forward and futures contracts.  
LOS 71.b: Explain why forward and futures prices differ.

> [!ABSTRACT] MEMORISE
> - Price vs Value (Forwards): Forward price is fixed at initiation; contract value fluctuates with the underlying and can be non-zero before expiry.  
> - Price vs Value (Futures): Daily mark-to-market (MTM) sets contract value back to zero each day; futures price moves to the settlement price daily.  
> - Quoting IR Futures:  
>   $$\text{Futures price} = 100 - (100 \times \text{MRR}_{A,\,B-A})$$  
>   A 6-month rate of 3% implies a futures price of 97.  
> - Basis Point Value (BPV):  
>   $$\text{BPV} = \text{Notional} \times \tau \times 0.0001$$  
>   where $\tau$ is year fraction for the accrual period.  
> - Futures vs Forwards Prices: If interest rates are constant or uncorrelated with futures prices → same price. If positively correlated → futures more valuable (for a long). If negatively correlated → futures less valuable.  
> - Convexity Bias (IR): FRAs/forwards exhibit convexity; longer maturities can show material forward–futures price differences.

1. Unlike a forward that is settled at a future date in totality, the future price difference is settled every day by Exchange. The exchange marks the price of the contract against the current market price. This is known as Mark to market. For example, if I bought a bitcoin future for $100 and the price of bitcoin futures increase to $110. The next day the $10 would be credited to my variation margin account. Daily variation margin cashflows settle the MTM P&L, so the futures contract is reset to ~0 each day.

2. To understand all three kinds of margin, hammer the table below into your head:

|     |                              |                     |                         |                           |                                       |                       |                      |
| --- | ---------------------------- | ------------------- | ----------------------- | ------------------------- | ------------------------------------- | --------------------- | -------------------- |
| Day | Futures settlement price (F) | Initial margin (IM) | Maintenance margin (MM) | Variation margin (VM = F) | Margin balance (end of day, pre-call) | Margin call / Top-up  | Balance after top-up |
| 0   | 100                          | 15                  | 10                      | NA                        | 15                                    | 0                     | 15                   |
| 1   | 102                          | 15                  | 10                      | +2                        | 17                                    | 0                     | 17                   |
| 2   | 92                           | 15                  | 10                      | -10                       | 7                                     | +8 (to restore to IM) | 15                   |
| 3   | 91                           | 15                  | 10                      | -1                        | 14                                    | 0                     | 14                   |
| 4   | 96                           | 15                  | 10                      | +5                        | 19                                    | 0                     | 19                   |
| 5   | 94                           | 15                  | 10                      | -2                        | 17                                    | 0                     | 17                   |
3. 

Notation in simple language
- MRR: Market reference (annualized) interest rate for the period.  
- $\tau$: Accrual year fraction of the period (e.g., 6 months → 0.5).  
- BPV: Change in contract value for a 1 bp change in MRR.  
- MTM: Daily settlement of gains/losses on futures.

> [!warning] Common mistakes to avoid
> - Confusing futures price with the interest rate: 97 price is 3% MRR, not 97%.  
> - Forgetting that futures value resets to zero each day after MTM.  
> - Using 1 instead of the period fraction in BPV: always multiply by $\tau$.  
> - Assuming futures = forwards regardless of rate dynamics; correlation matters.  
> - For interest rate forwards (e.g., FRAs), settlement is PV’d at the realized rate for the period, not at the forward rate.

Key relationships (display)
$$\text{IR Futures Price} = 100 - 100\,\text{MRR}_{A,\,B-A}$$
$$\text{BPV} = N \times \tau \times 0.0001$$

When forwards equal futures (pricing equality)  
- If interest rates are constant or uncorrelated with futures prices, the pricing is effectively the same.  
- With positive correlation (long futures): MTM cash arrives when rates are high → earns more interest → futures more attractive than forwards. With negative correlation → less attractive.

> [!tip] Quick checks
> - After each futures MTM, contract value → 0; price moves to settlement price.  
> - For a 6-month contract on $1,000,000,\ BPV = 1{,}000{,}000 \times 0.5 \times 0.0001 = 50.$  
> - A 1 bp move → $\pm$BPV in futures value; for forwards, discount the payoff at the realized rate for the same $\tau$.

Numericals

> [!question] Price vs Value with Daily MTM (Gold futures)
> Problem: A futures on 100 oz gold is initiated at $1{,}870$/oz. Day 1 settlement price rises to $1{,}880$/oz. What happens to price and value?  
> Solution: Price increases by $10 to $1{,}880$. The long receives MTM: $10 \times 100 = $1{,}000, and the contract value resets to 0 after settlement.  
> Explanation: Futures price changes and daily cash is exchanged; post-MTM, position value is reset to zero each day.

> [!question] BPV and Futures Payoff (IR futures)
> Problem: A 6-month MRR future settles in 6 months, notional $\$1{,}000{,}000$. Quoted futures price is 97.50 (implied MRR 2.50%). Compute BPV and the value change for a 1 bp increase in the MRR at settlement.  
> Solution:  
> $$\text{BPV} = 1{,}000{,}000 \times 0.5 \times 0.0001 = 50$$  
> A 1 bp increase in MRR → futures value increases by $\$50 for the long (price falls by 0.01, but contract value change is +$50 by convention).  
> Explanation: IR futures are quoted on a price basis (100 – rate). The contract value change per 1 bp move is governed by BPV.

> [!question] Forward vs Futures (convexity/discounting effect)
> Problem: Consider an otherwise equivalent 6-month FRA with notional $\$1{,}000{,}000$ struck at 2.50%. If the realized 6-month MRR at settlement is (i) 2.51% and (ii) 2.49%, compute the PV of the settlement at the beginning of the period. Compare to the $\pm$BPV from the futures.  
> Solution: For the FRA, per 1 bp: $\text{Nominal}\ \Delta = 50$. Discount at the realized rate over $\tau=0.5$.  
> (i) If realized is 2.51%:  
> $$\text{PV} = \frac{50}{1 + 0.0251/2} = 49.3803$$  
> (ii) If realized is 2.49%:  
> $$\text{PV} = \frac{50}{1 + 0.0249/2} = 49.3852$$  
> Explanation: The present value depends on the realized discount rate. Increases in the rate reduce the PV of gains slightly more than equal decreases increase it → convexity bias. By contrast, the futures marks $\pm 50$ without discounting nuance, causing potential forward–futures pricing differences for longer maturities.

> [!warning] Exam gotchas
> - Don’t PV the futures BPV change; PV at the realized rate applies to forward/FRA settlement.  
> - Positive correlation (rates with futures price) favors futures for longs; negative correlation favors forwards.  
> - Always convert quoted futures price to a rate correctly: rate = $(100 - \text{price})/100$.
