## PORTFOLIO MANAGEMENT

### INTRODUCTION TO RISK MANAGEMENT

1. The following are financial risks (CMLI):
	- **Credit risk** – The other side may not pay. _Example:_ A company sells goods on credit; the buyer goes bankrupt and never pays.
	- **Market risk** – Prices move against you. _Example:_ Equity prices fall in a recession; bond prices fall when interest rates rise.
	- **Liquidity risk** – You can't sell fast without taking a big price hit. _Example:_ You hold a small-cap stock; in a panic market, you sell much lower than its fair value.   
	- **Interest rate risk**: Risk of prepayments or higher opportunity cost of capital.
2. The following are non-finacial risks (*SolRegPolLegModTailOper*):	 
	- **Solvency risk** – The firm runs out of cash and can't survive. _Example:_ A company can't pay salaries or debt interest and goes bankrupt.    
	- **Regulatory risk** – Rules change and hurt the business. _Example:_ A new capital requirement forces banks to raise equity or cut lending.    
	- **Political / tax risk** – Government actions outside normal regulation hurt profits. _Example:_ Sudden tax hike reduces after-tax earnings of companies.    
	- **Legal risk** – Future lawsuits or legal action cause losses.   _Example:_ A firm is sued for mis-selling products and pays heavy penalties.    
	- **Model risk** – Your math or valuation model is wrong. _Example:_ A risk model underestimates losses because it assumes normal distributions.    
	- **Tail risk** – Rare, extreme events happen more often than expected. _Example:_ A 2008-style crash wipes out strategies built for “normal” markets.    
	- **Accounting risk** – Financial statements turn out to be wrong.  
	    - _Example:_ Aggressive revenue recognition leads to restated earnings later.
	- **Operational risk** – Loss due to people, process, or system failure. _Example:_ A trading desk loses money because of a fat-finger trade or a cyberattack shuts systems.
3. With a **risk transfer**, another party takes on the risk. Insurance is a type of risk transfer. The risk of fire destroying a warehouse complex is shifted to an insurance company by buying an insurance policy and paying the policy premiums. Insurance companies diversify across many risks so the premiums of some insured parties pay the losses of others.
4. **Risk shifting** is a way to change the distribution of possible outcomes and is accomplished primarily with derivative contracts. For example, financial firms that do not want to bear currency risk on some foreign currency denominated debt securities can use forward currency contracts, futures contracts, or swaps to reduce or eliminate that risk.
5. With a **surety bond**, an insurance company has agreed to make a payment if a third party fails to perform under the terms of a contract or agreement with the organization.
6. Insurers also issue fidelity bonds, which will pay for losses that result from employee theft or misconduct.

### MODULE 84.1: SYSTEMATIC RISK AND BETA

1. Portfolio return is a weighted average, so if $W_P$ is invested in a risky portfolio $P$ and $W_f = 1 - W_P$ is invested in a risk-free asset, expected return is  
   $E(R) = W_f R_f + W_P E(R_P)$.
2. The risk-free asset has zero variance and zero covariance with all assets, so portfolio risk comes entirely from the risky portfolio.
3. Portfolio variance therefore reduces mechanically to  
   $\sigma^2 = W_P^2 \sigma_P^2$,  
   and portfolio standard deviation is  
   $\sigma = W_P \sigma_P$.
4. Solving for $W_P = \sigma / \sigma_P$ and substituting into the return equation gives  
   $E(R) = R_f + \frac{E(R_P) - R_f}{\sigma_P}\,\sigma$. This is a linear risk–return relationship: expected return increases proportionally with risk. **In risk–return space, all such portfolios lie on a straight line starting at $(0, R_f)$ and passing through $(\sigma_P, E(R_P))$. This is known as capital allocation line**
5. Example: if $R_f = 4\%$, $E(R_P) = 10\%$, and $\sigma_P = 20\%$, then a portfolio with $\sigma = 10\%$ must have $E(R) = 7\%$.
6. Economic intuition: combining a risk-free asset with a risky portfolio does not create diversification curvature; it only scales risk and excess return along a straight line.
7. If all investors are clones of each other, meaning they have identical beliefs about returns, risk, and correlations, they will all rank risky portfolios in exactly the same way. Since the efficient frontier is constructed purely from these beliefs, every investor faces the same frontier and identifies the same tangency (optimal) risky portfolio.
8. Intuitively, if everyone agrees on the risk–return trade-offs, there is no reason for anyone to pick a different risky portfolio; they differ only in how much of that portfolio they combine with the risk-free asset. An investor who chooses to take no risk will allocate 100% in the risk free asset.
9. Diversification works because portfolio variance contains covariance terms, so when assets are not perfectly correlated, idiosyncratic shocks cancel out in aggregation; this cancelable component is unsystematic (firm-specific) risk, which shrinks as the number of independent return sources increases.
10. The market portfolio already holds all risky assets, so all unsystematic risk is averaged away, leaving only systematic risk—the part of return variance driven by common market factors that move many assets together and therefore cannot cancel.
11. You do not need to hold every stock to eliminate unsystematic risk: **as the number of reasonably uncorrelated stocks increases, portfolio variance converges toward systematic variance, meaning marginal risk reduction from adding more stocks rapidly approaches zero.**
12. The implications of this conclusion are very important to asset pricing (expected returns).
13. Since unsystematic risk can be eliminated by diversification, competitive markets price it at zero premium; in equilibrium, bearing firm-specific volatility does not increase expected return.
14. Only systematic risk survives aggregation across investors, so expected returns load on exposure to common risk factors, summarized in equilibrium by a risk premium proportional to systematic risk (e.g., market beta).
15. Resulting implication for portfolio choice: rational investors diversify away idiosyncratic risk and choose portfolios based on how much systematic risk they want to bear, not on standalone stock volatility.
