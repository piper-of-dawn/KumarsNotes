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

1. Unlike a forward that is settled at a future date in totality, the future price difference is settled every day by Exchange. The exchange marks the price of the contract against the current market price. This is known as Mark to market. For example, if I bought a bitcoin future for $100 and the price of bitcoin futures increase to $110. The next day the $10 would be credited to my variation margin account. **Daily variation margin cashflows settle the MTM P&L, so the futures contract is reset to ~0 each day.**

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
3. Interest rate futures are quoted as a “price,” not a rate. They convert a market reference rate (MRR) into a price via:
				**Futures price=100−(100×MRR)**
	So higher rates ⇒ lower futures prices. 

> [!QUESTION] FUTURES PRICE
> Suppose an interest rate futures contract is for a **6-month rate starting 6 months from now**, and the quoted futures price is **97**.
> 
> ---
> 
> 100−(100×MRR) = 97, implies, MRR = 0.03

4. How much does my futures value change if my MRR moves by 1bp. That is BPV which is notional times time in years times 0.0001. $$\text{BPV} = \text{Notional} \times \tau \times 0.0001$$  
5. **==If interest rates are constant or uncorrelated with futures prices, the pricing is effectively the same.==**  
6. When interest rates are high, futures are more attractive than forwards because I receive cash daily, and hence futures are expensive than forwards. This makes interest rate and futures price positively correlated.
7. With negative correlation → futures are less attractive.

> [!tip] Quick checks
> - After each futures MTM, contract value → 0; price moves to settlement price.  
> - For a 6-month contract on $1,000,000,\ BPV = 1{,}000{,}000 \times 0.5 \times 0.0001 = 50.$  
> - A 1 bp move → $\pm$BPV in futures value; for forwards, discount the payoff at the realized rate for the same $\tau$.


> [!question] CONVEXITY ISSUE
> Consider a $1 million interest rate future on a 6-month MRR priced at 97.50 (an MRR of 2.5%) that settles six months from now. If the realised 6-month MRR at settlement is (i) 2.51% and (ii) 2.49%, compute the PV of the settlement at the beginning of the period. 
> 
> ---
> 
> BPV = 1 Million $\times$ 0.0001 $\times$ 0.5 = $50
> - If the MRR at settlement is 2.51%, the long receives 50/(1 + 0.0251/2) = $49.3803.
> - If the MRR at settlement is 2.49%, the long must pay 50/(1 + 0.0249/2) = $49.3852.
>   
>Rate decline harms long more than Rate rise of same amount benefits him.


> [!question] Price vs Value with Daily MTM (Gold futures)
> 
> Problem: A futures on 100 oz gold is initiated at $1870$/oz. Day 1 settlement price rises to $1880$/oz. What happens to price and value?  
> 
> ---
> 
> MTM Value = 10 $\times$ 100 = 1000. 
> Deposit $1000 in VM and reset Future contract price to 0 



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

### MODULE 75.1: BINOMIAL MODEL FOR OPTION VALUES

1. The “risk-neutral probability” is simply the weight that makes the stock’s **average outcome** equal to what you’d earn risk-free.

2. In a 1-step binomial world, **no-arbitrage** means “a stock can’t have a free lunch relative to the risk-free asset.” So we choose a fake probability $\pi_U$ (the **risk-neutral** one) such that the **expected gross return of the stock equals the risk-free gross return**:  
$$  
\pi_U R^u + (1-\pi_U)R^d = 1+R_f  
$$  
Solve for $\pi_U$ and you get:  
$$  
\pi_U=\frac{1+R_f-R^d}{R^u-R^d},\qquad \pi_D=1-\pi_U  
$$
3. Consider a call option with strike $K$:
	- $S_u > K > S_d$ 
	- Upside $S_u$ with probability $\pi_u$. Call Payoff $(C_u)$ = $S_u - K$
	- Downside $S_d$ with probability $\pi_d$. Call Payoff $(C_d)$ = 0
	
	Price of call option at t0:
	$$ \boxed{C_0 = \frac{\pi_u C_u + \pi_d C_d}{1+R_f}} $$


> [!QUESTION]
> Given up-move factor = 1.15, down-move factor 0.87, K = 30, S = 30, Rf = 7%. Calculate the price of call option


> [!QUESTION]
> Given up-move factor = 1.15, down-move factor 0.87, K = 30, S = 30, Rf = 7%. Calculate the price of call option

> [!QUESTION]
> A stock’s price is currently ¥8,000. At the end of one month when its options expire, the stock price is either up by 5% or down by 15%. If the risk-free rate is –0.20% for the period, what is the value of a put option with a strike price of ¥7,950?


> [!QUESTION]
> Kleinert’s analyst estimates a 50-50 chance that the price of SparCoin will either increase by 12% or decline by 10% at the put option’s expiration date. Which of the following statements best describes the no-arbitrage option price implied by this assumption? 
> Exercise price is €100. SparCoin’s spot price (S0) is €105.25, and it pays no dividends. The risk-free rate is 0.37%.


> [!QUESTION]
> If Kleinert’s clients observe that the one-year put option with a €100 exercise price is trading at €2.50, which of the following statements best describes how Kleinert’s clients could take advantage of this to earn a risk-free return greater than 0.37% over the year.


###### HEDGE RATIO

4. Hedge ratio (h) is the **shares that cancels the option’s up/down risk** in a 1-step world. You pick (h) so the portfolio “long (h) shares, short 1 call” has **the same payoff in both states**. That forces:  
$$  
h=\frac{C_u-C_d}{S_u-S_d}  
$$
 - **Stock states:** $S_u, S_d$
 - **Call payoffs:** $C_u=\max(S_u-K,0)$, $C_d=\max(S_d-K,0)$
 - **Hedged portfolio:** long $h$ shares, short 1 call
 - Value in up: $V_u=hS_u-C_u$ and Value in down: $V_d=hS_d-C_d$    
 - **Riskless condition:** set $V_u=V_d$
 - Solve $V_u = V_d$ for $h$

