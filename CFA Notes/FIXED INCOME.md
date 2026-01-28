```table-of-contents
```
### MODULE 47.1: FIXED-INCOME INSTRUMENT FEATURES

#### Callable Bond
1. Issuer has the right to buy back (redeem) the bond at a specified call price.
2. Example timeline: sell a bond for $1,000 at t; issuer may call at $1,050 at t+1.
At t+1:
- If market price is 1,100, issuer calls (investor’s upside is capped at the call price).
- If market price is 1,000, issuer will not call.

- Negative convexity: as yields fall and prices rise, upside is capped by the call feature; price rises less than for an option‑free bond.
- Value vs option‑free: callable bond value is lower than an identical non‑callable bond because the investor is short the call option.

#### Puttable Bond
1. Investor (bondholder) has the right to sell the bond back to the issuer at a specified put price.
2. Puts provide downside protection when rates rise (prices fall), generally increasing the bond’s value relative to an option‑free bond and improving effective convexity on the downside.

### YIELD AND YIELD SPREAD MEASURES FOR FIXED-RATE BONDS
1. **Annual Yield:**
2. **Adjusting Yields for Periodicity:**
3. **Current Yields**

### MODULE 52.1: FIXED INCOME BOND VALUATION

1. If 2 year YTM is 4.3% and 5 year YTM is 5.2%, what is the 3 year forward rate. $(1.052^5 / 1.043^2)^{(1/3)} - 1 = 5.81\%$
2. Matrix pricing uses the yields of actively traded bonds with similar credit quality, coupon rates, and maturities to estimate the yield of an illiquid bond. The process relies on linear interpolation to estimate the yield-to-maturity for the target bond's specific maturity date.
3. **Matrix Pricing:** Recipe is to first calculate interpolated YTM using the given info and then compute PV
	
> [!question] QUESTION
> 
> ##### Price Interpolation
> 
> Rob Phelps, CFA, is estimating the value of a nontraded 4% annual-pay, A+ rated bond that has three years remaining until maturity. He has obtained the following yields to maturity on similar corporate bonds: 
> A+ rated, 2-year annual-pay, YTM = 4.3% 
> A+ rated, 5-year annual-pay, YTM = 5.1% 
> A+ rated, 5-year annual-pay, YTM = 5.3% 
> Estimate the value of the nontraded bond.
> ---
> If 2 year YTM is 4.3% and 5 year YTM is 5.2%, what is the 3 year interpolated YTM. $\Delta YTM (\text{3y}) = 5.2-4.3 = 0.9$. YTM increases by 0.9/3 = 0.30 per year. So 3-year straight line approximate YTM: 4.3+0.3 = 4.6% 
> 
> Now: I/Y = 4.6, N = 3, FV = 100, PMT = 4, **PV = -98.353**
> 
> ##### Using Spreads
> 
> Consider the following market yields:
> 4-year, U.S. Treasury bond, YTM 1.48%
> 5-year, A rated corporate bond, YTM 2.64%
> 6-year, U.S. Treasury bond, YTM 2.15%
> Estimate the required yield spread on a newly issued 6-year, A rated corporate bond
> 
> ---
> 5y YTM of US Treasury = 1.48 + (2.15-1.48)/2 = 1.480 + 0.335 = 1.815%
> A rated bond spread = 2.640 - 1.815 = 0.825 
> 6y YTM = 2.150 + 0.825 = 2.975
> 

4. The 'constant-yield price trajectory' illustrates how a bond's price moves toward par value as time passes, assuming the issuer does not default.
5. The YTM calculation assumes the investor holds the bond until maturity. It assumes the issuer makes all coupon and principal payments as scheduled without default. **==It assumes all coupon payments are reinvested at the calculated Yield-to-Maturity.==**
6. Generally, for the same change in market discount rates, a longer-term bond will experience a greater percentage price change than a shorter-term bond because the longer maturity bond has more cashflows that suffer the wrath of discounting.
7. ==A lower-coupon bond will typically have a higher percentage price change than a lower-coupon bond when market discount rates change by the same amount.== Lower coupon bond has *higher* interest rate risk (greater percentage price change) because a larger proportion of its value comes from the final principal payment, which is more sensitive to discounting. A higher coupon bond returns cash sooner, reducing duration.
8. **Convexity is optimistic.** The convexity effect implies that for the same absolute change in yield, the percentage price increase when yields fall is greater than the percentage price decrease when yields rise. 
9. he Actual/Actual method counts *actual* calendar days, which includes weekends, holidays, and leap days; it does not exclude them. Government bonds typically use Actual/Actual to be precise. #memorise
10. The 30/360 day count convention assumes each month has 30 days and the year has 360 days, and is often used for corporate bonds. #memorise
11. The flat price (or clean price) is the quoted price. It excludes accrued interest so that the price does not appear to drop significantly solely because a coupon payment was made.
12. The full price, also known as the invoice price, is equal to the flat price plus accrued interest. The full price includes accrued interest, which accumulates linearly between coupon dates and drops to zero immediately after a coupon payment.


> [!QUESTION] QUESTION
> A 4% annual coupon bond matures in 3 years. The market discount rate is 5%. The last coupon was paid 90 days ago. The coupon period is 360 days (30/360). What is the Full Price (Dirty Price)?
> 
> ---
> 
> Revalue the bond with 2.75 years remaining:
> N = 2.75, I/Y = 5, PMT = 4, FV = 100 -> **PV = 97.48**
> 
> Calculate lost coupon (accrued interest) = 90/360 $\times$ 4 = 1
> 
> Price = 98.48
>
 
 


> [!question] QUESTION
> A bond has a Full Price of 102.45. The semiannual coupon is 3.5% (annual rate). Settlement is 60 days into a 182-day coupon period. What is the Flat Price?
> 
> ---
> 
> Coupon = 3.5 
> Accrued Interest (linear) = 3.5 / 365 $\times$ 60 = 0.58
> Flat price = Full price - Accrued Interest = 101.87
 


13. The forward rate represents the marginal interest rate required to extend an investment for one additional period to break even with a longer-term spot investment.


> [!tip] HAMMER THIS INTO YOUR HEAD
> **What are Strips?** - Each **coupon payment** → becomes its **own zero-coupon bond**. The **principal repayment** → also becomes a **zero-coupon bond**.
> Bond: Face value **100**, maturity **3 years**, annual coupon **10%**. 
> - STRIP 1 (ZCB): pays **10** in Year 1 
> - STRIP 2 (ZCB): pays **10** in Year 2    
> - STRIP 3 (ZCB): pays **110** in Year 3
> Discount each Strip by YTM and you get the ZCB price.
> **Important things is to know is implication:**
> If the price of a bond calculated using the spot rate curve (theoretical price) is lower than the market price of the bond -> Bond is overvalued. Sell the bond, replicate its cash flows cheaper using strips → lock risk-free profit. 



> [!QUESTION] Title
> A 10-year, 8% annual coupon bond is purchased at a premium price of 115.00 (Yield = 6.00%). Assuming the yield remains constant at 6.00%, what is the expected price of the bond 1 year later (9 years to maturity)?

### MODULE 54.1: Yield and Yield Spread Measures for Floating-Rate Instruments

#### Floating-Rate Note (FRN) Valuation — Margin Widening

> [!question] Question
> A floating-rate note (FRN) has a face value of $10 million, total maturity 6 years, and pays coupons = reference rate + 2.5% margin. After 2.5 years, the issuer’s credit quality worsens and the market now demands a 3.5% margin (100 bps wider). The current flat spot curve is 4.1%, with semiannual payments. Compute the fair value of the FRN today.

> [!tip] TL;DR
> FRN price at reset ≈ par, but if its margin < market-required margin, Price = Par − PV(missing margin cash flows).

1. Shortfall per year = required margin − bond margin = 3.5% − 2.5% = 1.0% → per semiannual period = 0.5% (= 0.5 per 100 par).
2. Remaining time = 3.5 years = 7 semiannual periods → missing cash flows: 0.5 each period (per 100 par).
3. Discount at semiannual rate 2.05% (flat 4.1%/2). PV of shortfall ≈ 3.23 per 100.
4. Price per 100 = 100 − 3.23 = 96.77. For $10 million notional → ≈ $9,677,000 (rounding may give ≈ $9,697,600).

Key idea: FRNs trade near par at reset; deviations reflect margin differences relative to current market.

### MODULE 55.1: The Term Structure of Interest Rates — Spot, Par, and Forward Curves

#### Forward Rates — Intuition and No-Arbitrage

- Why “forward”: It is the implied rate for a future period, inferred today from longer-dated spot yields.
- No-arbitrage relation (annual compounding example):
  (1 + S2)^2 = (1 + S1) × (1 + 1y1yF)
  → 1y1y forward = (1 + S2)^2 / (1 + S1) − 1.
- Interpretation: Being indifferent between buying a 2-year zero today vs. rolling 1-year zero for two years implies this equality; otherwise, arbitrage exists.

#### Maturity Effect — Volatility Across Horizons

- Short-term rates/yields are typically more volatile than long-term rates because they reflect immediate policy and liquidity conditions, while long-term rates embed an average of expected short rates plus a term premium.
- **Term premium** compensates for uncertainty over long horizons; as maturity increases, instantaneous shocks are averaged across many expected future short rates, dampening volatility relative to short maturities.

Note: Premium bonds often have effective durations below time-to-maturity, as larger near-term coupons bring cash flows forward, reducing sensitivity to rate changes.

### MODULE 57.1: Yield-Based Bond Duration Measures and Properties

#### Maturity Risk — First Principles and Duration Link

- Present value mechanics: each cash flow $PV_t = CF_t / (1 + r)^t$. Sensitivity to r grows with t:
  $∂PV_t/∂r = − t · CF_t / (1 + r)^{t+1}$ → farther cash flows (larger t) lose more value for the same ∆r.
- Long-maturity bonds have more far-dated cash flows, so for a given yield change, percentage price moves are larger than for short bonds (higher interest rate risk).
- Macaulay duration $$D = Σ[t · PV(CF_t)] $$Price is a weighted-average time; longer maturities and lower coupons increase D and thus modified duration (price sensitivity):
  $$∆P / P ≈ − D_{mod} \times \delta Y$$ where 
$$D_{mod} = D / (1 + y).$$

Reinvestment dimension: longer horizons imply more coupon reinvestments at uncertain future rates, increasing reinvestment risk alongside price risk.

Convexity note: As a bond approaches maturity, both duration and convexity decline; the price–yield curve flattens toward par at maturity (convexity → 0).

### MODULE 58.1: Yield-Based Bond Convexity and Portfolio Properties

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

### FIXED INCOME MARKETS FOR CORPORATE ISSUERS
1. Weak credit → secured borrowing. Firms with low credit ratings must pledge collateral. Strong credit firms issue commercial paper (CP) → unsecured, typically < 3 months maturity, used for working capital or temporary/bridge funding.
2. **Factoring** Firm sells receivables to a lender at a discount. Lender takes over credit risk + collection. Example: ₹100 invoice sold for ₹95 today → instant liquidity.
3. Bridge Financing refers to short-term funding used until permanent financing (bonds, equity) is arranged. A company plans to issue a 10-year bond in 3 months but needs cash now to run operations → it issues 3-month commercial paper today → when the bond is issued, the proceeds are used to repay the CP.
4. **Rollover** = repaying old short-term debt by issuing new short-term debt instead of using cash. ==The risk that the company would not be able to sell a new commercial paper to repay the old one is known as rollover risk.==
5. Banks fund short-term mainly through deposits: checking, operational corporate deposits, savings, and certificates of deposit (CDs). For example, fixed deposits in India.
6.  Asset Backed Commercial Paper: A bank sets up a vehicle that buys car loans, then issues 30-day asset-backed commercial paper to investors, and keeps issuing new 30-day ABCP every month to repay the old ABCP, with the car loans as collateral. Cash to repay ABCP comes from loan EMIs first, new ABCP issuance next, money from sponsoring bank during bad days, and asset sales only as last resort.
7. Repo = collateralised borrowing where one party sells a security today and agrees to buy it back later at a higher price; that price difference is the repo rate, i.e. the interest on the loan embedded in prices, not quoted separately.
8. Example (India): An Indian bank needs overnight cash → it sells government bonds to the RBI for ₹100 today and agrees to repurchase them tomorrow for ₹100.02 → the ₹0.02 difference is the repo interest, and the bonds are the collateral.
9.   Collateral protection: lender demands collateral worth more than the cash lent to protect against price drops.
10. **Initial margin (haircut)** = gap between collateral market value and loan amount → loan amount is a discount to collateral value. Collateral worth ₹105 is posted, but the lender gives only ₹100 cash → the ₹5 gap is the initial margin (haircut) protecting the lender if collateral prices fall.
11. During the repo\u2019s life, if collateral value falls, borrower must post extra collateral → this top-up demand is variation margin.
12. Overnight repo = one-day repo; term repo = repo longer than one day. Repo rates are usually lower than unsecured bank loans because the loan is backed by high-quality collateral (often government bonds).
13.  Repo rates are usually lower when the collateral liquidity is high and the collateral is physically delivered to the lender. Repo rates are usually higher when the term is high and when interest rates for alternative sources of funds are higher.
14.  Tri-party repo = repo where a third party (clearing bank/CCP) handles collateral custody, valuation, and margining; example: an Indian bank borrows overnight via repo using G-secs, while CCIL sits in the middle holding the bonds and settling cash.
15. Reverse repo = the lender\u2019s side of a repo; example: a bank parks excess cash with the RBI, receives G-secs as collateral, and earns the reverse repo rate as interest.
16.  Tri Party repos protect against the following kinds of risks:
	- Default risk = the borrower takes cash today and fails to repurchase the collateral later, forcing the lender to sell the collateral to recover money.
	- Collateral risk = the value of the collateral falls sharply before it can be sold, so even after liquidation it does not fully cover the cash lent.
	- Margining risk = collateral prices move faster than margin calls, so the lender is exposed during the time gap between a price fall and posting of additional collateral.
	- Legal risk = in stress or bankruptcy, the repo is not enforced as expected, and courts may freeze or delay access to collateral by treating the repo like a normal loan.
	- Netting risk = when a counterparty defaults, you cannot offset what you owe against what you are owed, so you must pay all obligations in full while recovering only partially on claims.
	- Settlement risk = cash and securities do not settle simultaneously, so one party delivers cash while the collateral delivery fails or is delayed.

### FIXED INCOME MARKET FOR GOVERNMENT ISSUERS

1. Sovereign debt = bonds issued by national governments to fund public goods; backed by taxing power, usually the largest issuers in domestic markets, typically highest credit quality locally.
2. Public-sector accounting focuses on cash flows; analysts should think in balance-sheet terms: implied assets (future taxes) versus liabilities (promised debt payments).
3. Core divide: developed-market issuers borrow in stable, reserve currencies with deep markets and transparent fiscal policy; emerging-market issuers face higher volatility, weaker institutions, and funding constraints.
4. Emerging-market debt is often split into domestic debt (local currency, local investors) and external debt (foreign currency, foreign creditors); external debt adds FX risk because repayment currency \u2260 tax currency.
5. If a government earns in INR but owes USD debt, currency depreciation mechanically raises debt burden even if real activity is unchanged.
6. Governments issue across maturities to balance cost and risk; too much short-term debt lowers rates today but raises rollover risk tomorrow.
7. Rollover risk = inability to refinance maturing debt; classic crisis trigger when markets suddenly refuse to roll short-term bills.
8. Debt management policy decides how much, what type, maturity, currency, and indexation (floating, inflation-linked) of debt is issued.
9. Inflation-linked debt shifts inflation risk to the issuer; nominal fixed-rate debt shifts inflation risk to investors.
10. Sovereign issuance is done via regular public auctions to signal transparency and price discovery. Competitive bids specify both price and quantity; noncompetitive bids accept the auction price and are guaranteed allocation.
11. Government auctions ₹1,000 crore of a 10-year bond; competitive bidders submit bids like \u201c₹300 crore at 7.10%,\u201d \u201c₹400 crore at 7.15%,\u201d \u201c₹500 crore at 7.25%.\u201d Because the auction cleared (filled the quota) at the 7.25% tier, 7.25% is the cutoff yield.
12. In a \u201csingle-price\u201d auction (also known as a Dutch auction), everyone pays the same yield→the highest yield accepted to sell the entire offering. If the government needs to sell bonds and the clearing rate is 4.0%, a bidder who aggressively bid 3.8% still gets the bonds at 4.0%, which encourages more aggressive bidding by removing the fear of overpaying. In a \u201cmultiple-price\u201d auction, winning bidders pay exactly what they bid; if you bid 3.8% and the clearing rate was 4.0%, you are stuck earning 3.8% while others earn more. This structure can reduce aggressive bidding because investors fear the \u201cwinner\u2019s curse\u201d→winning the auction but paying a price worse than the market average.
13. Issuers wanting to minimize yield volatility often prefer single-price auctions; bidders shade less.
14. On-the-run bonds = most recently issued securities at a given maturity; most liquid, used as benchmarks for risk-free rates. ==Yield curves in practice are built off on-the-run sovereign bonds, not off older illiquid issues.==
15. Primary dealers are designated banks obligated to bid in auctions and make secondary markets; they act as transmission channels for monetary policy. Central banks interact with primary dealers as counterparties when conducting open-market operations.
### MODULE 54.1: YIELD AND YIELD SPREAD MEASURES FOR FLOATING-RATE INSTRUMENTS

1. Coupon is reset periodically as per prevailing market reference rate + spread. 
2. On the reset date, the coupon resets to **reference rate + quoted margin (50 bps)**, but investors require **reference rate + required margin (75 bps)**, so the coupon is too low for the market.
3. Therefore, **the price will be below par**, because the bond must trade at a discount so that coupon plus price pull-to-par together deliver the higher required margin.
4. Between resets the bond still trades in the market and its price can move above or below par.
5. It trades **below par** when the quoted margin is too low for current market conditions or issuer risk; example: an FRN pays SOFR + 150 bps, but new FRNs from similar issuers are coming at SOFR + 200 bps, so investors mark the old bond down to 98 so its yield matches the higher required spread.
6. **Quoted margin** is the fixed spread added to the reference rate that defines the coupon on a floating-rate note; example: a FRN pays 3-month LIBOR + 150 bps, so if LIBOR is 5%, the coupon rate is 6.5%, and the 150 bps is the quoted margin written into the bond contract.    
7. **Discount margin** is the spread over the reference rate that makes the present value of all future cash flows equal to the bond\u2019s current market price; example: if the same FRN (LIBOR + 150 bps) trades below par at 98, investors effectively earn LIBOR + 180 bps, and the extra 30 bps over the quoted margin is captured by the discount margin.
8. During issuance, QM = DM. If issuer credit quality deteriorates DM > QM, vice versa.


> [!question] NUMERICAL
> A $100,000 FRN with a semiannual coupon pays a 180-day MRR plus a quoted margin of 120 basis points. On a reset date with five years remaining to maturity, the 180-day MRR is quoted as 3.0% (annualized), and the discount margin (based on the issuer\u2019s current credit rating) is 1.5% (annualized). Estimate the value of the FRN.
> 
> ---
> 
> Coupon Rate = (3.0% + 1.2%) / 2 = 2.1%
> PMT = 0.021 $\times$ 100 = 2.1
> I/Y = (3.0% + 1.5%) / 2 = 2.25%
> N = 10
> FV = 100
> PV = 98.67

9. **Discount yield** quotes return as a percentage of **face value**, not money invested, and ignores compounding; example: a 1-year T-bill with face value 100 bought at 95 has discount yield = (100 \u2212 95)/100 = **5%**, even though you invested only 95.
10. **Add-on yield** quotes return as a percentage of **amount invested**, which reflects actual cash put in but still ignores compounding; example: the same bill bought at 95 has add-on yield = (100 \u2212 95)/95 \u2248 **5.26%**, higher than discount yield because it uses invested cash as the base.


> [!question] NUMERICAL
> 1. A $1,000 90-day T-bill is priced with an annualized discount of 1.2%. Calculate its market price and its annualized add-on yield based on a 365-day year.
>  ---
>  HPY = 90/360 $\times$ 1.2 = 0.3%
>  PV = 1000 / 1.003 = 997
>  
>  2. A $1 million negotiable CD with 120 days to maturity is quoted with an add-on yield of 1.4% based on a 365-day year. Calculate the payment at maturity for this CD and its bond equivalent yield.
>     
>    ---
>    
>    HPY = 120/365 $\times$ 1.4 = 0.46%
>    PV = 1 / 1.0046 = 956,000
>    Discounted yeild = (1 - 0.956) / 1 = 4.4%
>    
> 1. A bank deposit for 100 days is quoted with an add-on yield of 1.5% based on a 360-day year. Calculate the bond equivalent yield and the yield on a semiannual bond basis.
>    
>    HPY = 100/360 $\times$ 1.5 = 0.4166%
>    PV  = 100 / 1.004166 = 99.58
>    Discount Yield = (100-99)/100 = 4.2%
>    Discount Yield (SemiAnnual) = 2.1%
>   
>   
>  


### MODULE 59.1: CURVE-BASED AND EMPIRICAL FIXED-INCOME RISK MEASURES
1. The yield curve does not always move in a parallel way—short-term rates, medium-term rates, and long-term rates can change by different amounts or even in different directions. At the same time, many bonds do not have fixed cash flows: borrowers may prepay, issuers may call the bond early, or payments may change when interest rates move. 
2. Macaulay and modified duration assume a **parallel yield curve shift** and **fixed cash flows with no embedded options**.
3. **Effective Duration:** 
4. **Macaulay Duration:** Weighted Average of Time where weights are PV of cashflows.
$$\boxed{\text{Mac. D} = \sum_{i=o}^N \text{PV}_i \times i}$$
5. **Modified Duration:** Sensitivity of bond price to changes in yield. **It is an approximation (tangent slope) which means that it overestimates the Eprice decline (when yields rise) and underestimates the price increase (when yields fall).** Memory hook: ==Modified Duration is pessimistic.== $$ \text {Mod. D} = \frac{\text{Mac. D}}{{1+y}}$$
6. **Effective Duration:** Effective duration is basically brute-force. You don’t derive sensitivity from a formula. You reprice the bond twice (yields up, yields down). You observe what actually happens to price and cash flows. Then you compute the slope numerically.
      - **Numerator $(PV_+−PV_-)$:** This captures how much the bond’s price actually moves when yields are nudged down versus up, with cash flows allowed to change. It’s the observed price response to rate movements.
      - **Denominator $2\,\Delta y$:** This is the total yield change between those two scenarios (down by Δy, up by Δy). Dividing by it converts the price move into a price change per unit of yield (a slope).
	    - Divide by $PV_0$: Normalizes the slope by today’s price so the result is a percentage sensitivity.    $$\boxed{\text{Effective Duration}=\dfrac{PV_- - PV_+}{2\,\Delta y\,PV_0}}​​$$
7. Callable vs putable convexity (plain English):  
   - Callable: when yields fall a lot, the issuer will likely call. Your upside is capped. Price rises slow down → this is “negative convexity.”  
   - Putable: when yields rise a lot, you can sell back (put). Your downside is cushioned. Price falls slow down → convexity stays positive.
8. Option‑free bonds: Modified Duration (Mod. D) and Effective Duration (Eff. D) are usually close for small moves. They can differ when the curve isn’t flat. Keep it simple: for plain bonds use Mod. D; if options/prepayments can change cash flows, use Eff. D.
9. Effective Convexity (Eff. Conv.): Same idea as Eff. D. Reprice the bond with the curve shifted slightly down and up. Use those two prices to measure curvature. Use Eff. Conv. when the bond has options or path‑dependent cash flows.
10. Price change with effective measures (Δ in decimals):  
    $$\Delta P/P \approx -\text{Eff. D}\,\Delta\text{Curve} + \tfrac{1}{2}\,\text{Eff. Conv}\,(\Delta\text{Curve})^2$$  
    Read it as: duration gives the main move; convexity adds a small correction.

> [!QUESTION] PRICE CHANGE USING EFF. D AND EFF. CONV.
> Problem: Eff. D = 10.5, Eff. Conv. = 97.3. Curve falls by 200 bps. What is % price change?  
> ---  
> Step 1 (duration): −10.5 × (−0.02) = +0.2100 → +21.00%  
> Step 2 (convexity): 0.5 × 97.3 × (0.02)^2 = 0.0195 → +1.95%  
> Answer: ≈ +22.95%  
> Takeaway: Use decimals for bps (200 bps = 0.02). Add convexity for big moves.

11. Key Rate Duration (KRD): Sensitivity to a move at one maturity (e.g., “5‑year point”), holding other maturities fixed.  
    - KRDs across maturities add up to Eff. D.  
    - Use KRDs to handle non‑parallel curve moves (steeper, flatter, or curved shapes).  
    - Portfolio KRD = sum of position KRDs (weighted by market value).

> [!QUESTION] KRD WITH A NON‑PARALLEL MOVE
> Problem: 50% in a 5‑year zero at 5% and 50% in a 10‑year zero at 6% (annual).  
> 5‑year yield +50 bps; 10‑year yield −25 bps. Estimate portfolio % change.  
> ---  
> 5y: Mod. D = 5/1.05 = 4.762 → KRD5 = 4.762 × 0.5 = 2.381 → Impact = −2.381 × 0.0050 = −1.19%  
> 10y: Mod. D = 10/1.06 = 9.434 → KRD10 = 9.434 × 0.5 = 4.717 → Impact = −4.717 × (−0.0025) = +1.18%  
> Net: ≈ −0.01% (roughly flat).  
> Takeaway: KRDs let you see which maturity points drive P&L.

12. Analytical vs empirical duration (keep it practical):  
    - Analytical (Macaulay, Mod. D, Eff. D): model‑based; assumes spreads don’t change when you shift the benchmark curve.  
    - Empirical: uses history; captures how credit spreads and yields actually move together.  
    - Example: “Flight to quality” → gov’t yields drop but credit spreads widen; corporate bond prices may rise less or even fall → empirical duration is lower than analytical for credit‑heavy portfolios.

> [!TIP] QUICK CHECKS
> - Options or prepayments? Use Effective (not Modified).  
> - Convert bps to decimals (50 bps = 0.005).  
> - KRDs add up to Eff. D.  
> - Callable at low yields → negative convexity; putable stays positive.

> [!DANGER] DO NOT DO THIS
> - Don’t use Mod. D for callable/putable/MBS.  
> - Don’t assume all curve moves are parallel; use KRDs for shape changes.  
> - Don’t mix spread moves into “effective” shocks unless your model changes spreads too.

### MODULE 65.1: MORTGAGE-BACKED SECURITY (MBS) INSTRUMENT AND MARKET FEATURES

1. **Prepayment Risk:** You own a callable bond (and interest rate falls) → They prepay and buy back their now cheaper bond issued at a high interest rate. Interest Rate falls to 2% and you take a cheaper loan and payback your expensive loan. For the bond investor, high-coupon mortgage cash flows disappear right when they\u2019re most valuable, that is why a **risk**.
2. **Extension Risk:** Interest Rate \u2191, Duration \u2193 and Price \u2193. Bond sellers (borrowers) won't exercise their call option. Expected cash-flows get extended. The market rate is higher but the bond buyer (investor) keeps receiving scraps from mortgages issued at low rates.
3. **Contraction Risk:** Interest Rate \u2193, Duration \u2191 and Price \u2191. Prepayments speed up.  Bond sellers (borrowers) will exercise their call option. Cash-flows would arrive sooner than expected.
4. Because the prices of MBS reflect expectations for prepayments in low-rate environments, they will not rise as much in response to decreasing interest rates as other fixed-income instruments that do not have an embedded prepayment option.
5. Convexity is acceleration of prices with falling rates. Prepayments are friction. When rates fall, you lose the deals you earlier did (bought high coupon mortgages), so price of your MBS doesn't rise proportionally. So traditional FI instruments have +ve convexity and MBS **have a -ve convexity**

> [!TIP] HAMMER THIS INTO YOUR HEAD
> Long tranches absorb contraction risk. Short tranches absorb extension risk. People at the front of the queue hate delays (so they have to absorb extension), people at the back don't care because they were anyway waiting. 

6. A mortgage pool pays principal into two tranches: **Tranche S (short)** first, **Tranche L (long)** later. 
7. When **payments speed up**, principal rushes in. Tranch S is unaffected (it was already on the front line to get paid off). The contraction risk gets pushed to back of the line Tranch L. 
8. When **payments slow down (rates rise)**, prepayments stagnates. Tranch L is unaffected (it was already on the back of the line to get paid off). The extension risk hurts the front of the line.
9. If I take a loan of $100 against and pledge my asset of $200, my Loan to Value (LTV) is 200/100 = 2. 
10. A mortgage of USD 300,000 has an annual interest rate of 6%, is to be repaid monthly over 25 years, and the borrower\u2019s annual pretax gross income is $80,000. Calculate DTI. Here, PV=-300,000, FV = 0, N = 25�12 = 300, I/Y = 6/12 = 0.5. This gives PMT = 1932. DTI = (1932 * 12) / 80000 = 0.289 ~ 28.9 %
11. Prime loans are made to creditworthy people, subprime loans are made to broke people.
12. Residential mortgages are different because you **can\u2019t freely prepay**. If you do, you **pay a penalty**,. They can be **recourse or non-recourse**: in recourse loans, the lender can **come after your other assets**; in non-recourse, they\u2019re **stuck with just the house**.
 13. A 30-year US home loan that meets standards gets pooled and guaranteed by **Fannie Mae** or **Freddie Mac**. These **Agency RMBS** are backed either **directly by the government** or by **government-sponsored agencies** (quasi-government companies). Credit risk is basically **off your plate**. Non-agency RMBS: private-issued, no government/GSE backstop → investors eat credit risk. **2008:** subprime RMBS (e.g., Lehman Brothers) blew up; defaults surged, protections failed, MBS holders lost money.
 14. Mortgage pass-through = claim on cash flows from a pool of mortgages, net of admin fees. Pool can have any number of mortgages; each is a securitized mortgage.
 15. Mortgage A has an outstanding principal of USD 80, a coupon rate of 6%, and a final maturity of 30 years. Mortgage B has an outstanding principal of USD 20, a coupon rate of 4%, and a final maturity of 15 years. Total outstanding principal in the pool is USD 100. Weighted average coupon (WAC) = (80/100 � 6%) + (20/100 � 4%) = 5.6%. Weighted average maturity (WAM) = (80/100 � 30) + (20/100 � 15) = 27 years.
 
> [!DANGER] DO NOT MAKE THIS MISTAKE
> Outstanding and NOT beginning principal, while calculating weights.

16. A **Collaterized Mortgage Obligation (CMO) is a tranched MBS**. The **underlying cash flows are the same** mortgages. What changes is **how those cash flows are split and ordered**. Senior tranche gets paid first and lowest tranche gets paid the last. Total prepayment risk stays the same; it is redistributed across tranches.
17. **Z-tranche** = a CMO tranche that gets no cash interest at first.   During this phase, interest is not paid out; it is **added to principal** instead. Suppose Start: principal = USD 100, coupon = 5%. End of year: no cash paid, principal becomes USD 105. You didn\u2019t get money; your claim just got bigger.
18. So the bond grows silently while other tranches take the cash. After the accrual period, Z-tranche starts receiving normal interest and principal payments. Z-tranche is usually last in line. It sacrifices early cash so other tranches get paid first.     
19. Principal-only (PO) securities and Interest-only (IO) securities are **interest-rate / prepayment bets**, not boring bonds. - If rates fall, people refinance → **prepayments speed up**.
20. You get **only interest payments**, no principal. You want loans to **stay alive as long as possible**. If rates rise or stay high → prepayments slow → **more coupon checks**. Used by investors who want to **bet on rising/stable rates and slow prepayments**.
    
- Principal comes back **faster**, IRR shoots up.

### HEDGE FUNDS
1. **Commingled funds** = multiple clients\u2019 money pooled together and invested as one portfolio; each client owns a proportional share, not specific securities. Eg: Mutual Fund
2. **SMA** = one client, one portfolio. Not pooled. You directly own the securities. Risk preferences can be tailored. Higher than commingled funds due to customization and admin.
3. Hedge Fund Strategies: A **convertible bond** = bond floor (interest + principal) + call option on stock. Buy ₹1000 convertible of XYZ paying coupons + right to convert into shares. Short **XYZ stock** in the right ratio (delta-hedge). _Example_: If bond acts like 0.4 shares, short 0.4 XYZ.
4. Fund-of-funds is a hedge fund invested in multiple hedge funds. **Fee layering** = you pay fees twice in a fund-of-funds: once to the FoF manager, again to the underlying hedge funds.
5. �Under a **'1 or 30' fee structure**, the manager receives the greater of a 1% management fee or a 30% incentive fee on the fund's alpha.
6. Kinds of Fees at Hedge Fund
	- **Management fee**: Fixed annual fee (e.g., 2% of AUM) paid **regardless of performance** → covers salaries, rent, survival.    
	- **Incentive (performance) fee**: Share of profits (e.g., 20%) paid **only if fund makes money**.	    
	- **Hurdle rate**: Minimum return (e.g., T-bill or 5%) the fund must beat **before** incentive fees apply → no reward for just market drift.	    
	- **High-Water Mark (HWM)**: Highest NAV ever reached; incentive fees are paid **only on gains above the previous peak** → manager must first recover losses before earning again.
7. **Convertible arbitrage fixed income strategy:** \u201cArbitrage\u201d here is: market price of convertible \u2260 price of (bond + call). You buy the convertible bond (which acts like a stock with a safety net). Suppose the bond is selling for 100 and convertible at 95 (safety net). And short the actual stock to cancel out market direction. When prices go up bond gains value faster (convexity) than your short stock loses it. When prices go down, your bond holds value (bond floor protection) while your short stock soar.
8. **Hedge Fund Index performance is overstated:** 
	- Because of **survivorship bias**: Most hedge fund don't survive and indexes are constructed only on functioning ones.
	- Because of **selection bias** because indexes have their own constraints for which fund to include and which one not to include.
	- **Backfill Bias**: A hedge fund operates privately at first so its early returns are invisible to databases; if those early returns turn out good, the manager chooses to join a data`b`ase and backfills only that strong past performance, while funds with weak early results never join at all→so the recorded history ends up showing only winners and systematically overstates true hedge-fund returns.
