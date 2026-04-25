### MODULE 8: Yield and Yield Spread Measures for Floating-Rate Instruments

> Source module: `/home/karma/CFAPractice/mcq/quiz/AI/PDF/FixedIncome/module_08_yield_and_yield_spread_measures_for_floating_rate_instruments.txt`

#### Extracted Notes 1

> [!tip] HAMMER THIS INTO YOUR HEAD
> When we do valuation of a floater we create cashflow coupons using quoted margin and discount them using discount margin or the required margin.

Remember this shortcut, whenever coupon rate exceeds discount rate, the bond trades at premium otherwise it trades at discount. 

If your quoted margin is less than discount margin the bond trades at discount and vice versa

1. The **quoted margin is the specified spread**, that is mentioned on the TnC of the bond, whereas the **required margin (discount margin) is market-determined** and can change with factors such as credit risk.
2. Floaters with longer reset periods may be more exposed to interest rate and price volatility. The longer the reset period, the more a floater will behave similarly to a short-dated fixed-rate security.
3.  The quoted margin is the spread required by investors for the instrument to be priced at par on a reset date, and it is required margin.

> [!tip] HAMMER THIS INTO YOUR HEAD
> - When a floater is quoted, investors ALWAYS quote the QUOTED MARGIN over the reference rate.
> - The REQUIRED MARGIN (or DISCOUNT MARGIN) is the margin that investors actually require to hold the bond in the market. This is what market dictates.
> - At inception, the REQUIRED MARGIN = QUOTED MARGIN, so the bond is priced at par.
> - If credit quality worsens, investors demand a HIGHER REQUIRED MARGIN OR DISCOUNT MARGIN, so the bond price falls below par.
> - **Quoted margin pins the coupon.**
> - **Required margin pins the price.**
> 



> [!question] Question
> A floating-rate note (FRN) has a face value of $10 million, total maturity 6 years, and pays coupons = reference rate + 2.5% margin. After 2.5 years, the issuer’s credit quality worsens and the market now demands a 3.5% margin (100 bps wider). The current flat spot curve is 4.1%, with semiannual payments. Compute the fair value of the FRN today.
> 
> ---
> 
> After 2.5 years, 7 coupons remain, hence N = 7
> PV, if nothing changed = 100
> Margin widened by 1% (0.5 per 100 per coupon period)
> PV of 7 payments of 0.5 @ 2.05% = 3.23
> So bond value should decline by 3.23 per 100 and bond should be priced at 96.77 per 100
> For $10 million notional, price = $9,677,000 (rounding may give $9,697,600) 
> 

4. Discount rate means **interest is added on top of principal**, not discounted. **Price = Face Value − Interest for the period**.
5. Add-on rate means **interest is calculated on the principal and added to it**. **Price = Face Value / (1 + Effective Yield)**.

   
> [!danger] DO NOT MAKE THIS MISTAKE
> 
> ==Look very very carefully if question gives you add-on rate or discount rate==
> 
> PV when Add-on rate is given:
> 
> $$ \text{Price} = \frac{\text{Face Value}}{1 + \text{Effective Yield}} $$
> 
> PV when Discount rate is given:
> 
> $$ \text{Price} = \text{Face Value} - \text{Interest} $$


> [!question] ADD ON YIELD
> Calculate the price of a 180-day money market instrument with a face value of 10,000,000 quoted at an add-on rate of 3.65% based on a 365-day year.
> 
> ---
> 
> Holding Period = 180/365 = N
> Effective Yield = 3.65% × 180/365 = 1.825%
> Price = 10 / (1.01825) = USD 9,823,183


> [!question] DISCOUNT YIELD
> A 90-day T-bill is quoted at a discount rate of 3.20% based on a 360-day year. The face value is 1,000,000. What is the purchase price of the T-bill?
> 
> ---
> 
> Holding Period = 90/360 = 0.25
> Effective Rate = 0.25 × 3.20% = 0.80%
> Interest = 1,000,000 × 0.008 = 8,000
> Price = FV - Interest = 1,000,000 - 8,000 = 992,000t



> [!question] ADD ON RATE VS DISCOUNT YIELD
> A 90-day Bankers' Acceptance is quoted at a discount rate of 5.00% (360-day year). A 90-day CD is quoted at an add-on rate of 5.10% (365-day year). Which instrument offers the higher yield to the investor?
> 
> ---
> 
> PV of Bankers Acceptance:
> HP = 90/360 = 0.25
> HPY = 0.25 × 5.00% = 1.25%
> PV  = 100(1-0.0125) = 98.75
> 
> PV of CD:
> HP = 90/365 = 0.2466
> HPY = 0.2466 × 5.10% = 1.258%
> PV = 100 / (1 + 0.01258) = 98.76

#### Extracted Notes 2

1. Coupon is reset periodically as per prevailing market reference rate + spread. 
2. On the reset date, the coupon resets to **reference rate + quoted margin (50 bps)**, but investors require **reference rate + required margin (75 bps)**, so the coupon is too low for the market.
3. Therefore, **the price will be below par**, because the bond must trade at a discount so that coupon plus price pull-to-par together deliver the higher required margin.
4. Between resets the bond still trades in the market and its price can move above or below par.
5. It trades **below par** when the quoted margin is too low for current market conditions or issuer risk; example: an FRN pays SOFR + 150 bps, but new FRNs from similar issuers are coming at SOFR + 200 bps, so investors mark the old bond down to 98 so its yield matches the higher required spread.
6. **Quoted margin** is the fixed spread added to the reference rate that defines the coupon on a floating-rate note; example: a FRN pays 3-month LIBOR + 150 bps, so if LIBOR is 5%, the coupon rate is 6.5%, and the 150 bps is the quoted margin written into the bond contract.    
7. **Discount margin** is the spread over the reference rate that makes the present value of all future cash flows equal to the bond’s current market price; example: if the same FRN (LIBOR + 150 bps) trades below par at 98, investors effectively earn LIBOR + 180 bps, and the extra 30 bps over the quoted margin is captured by the discount margin.
8. During issuance, QM = DM. If issuer credit quality deteriorates DM > QM, vice versa.


> [!question] NUMERICAL
> A $100,000 FRN with a semiannual coupon pays a 180-day MRR plus a quoted margin of 120 basis points. On a reset date with five years remaining to maturity, the 180-day MRR is quoted as 3.0% (annualized), and the discount margin (based on the issuer’s current credit rating) is 1.5% (annualized). Estimate the value of the FRN.
> 
> ---
> 
> Coupon Rate = (3.0% + 1.2%) / 2 = 2.1%
> PMT = 0.021 $\times$ 100 = 2.1
> I/Y = (3.0% + 1.5%) / 2 = 2.25%
> N = 10
> FV = 100
> PV = 98.67

9. **Discount yield** quotes return as a percentage of **face value**, not money invested, and ignores compounding; example: a 1-year T-bill with face value 100 bought at 95 has discount yield = (100 − 95)/100 = **5%**, even though you invested only 95.
10. **Add-on yield** quotes return as a percentage of **amount invested**, which reflects actual cash put in but still ignores compounding; example: the same bill bought at 95 has add-on yield = (100 − 95)/95 ≈ **5.26%**, higher than discount yield because it uses invested cash as the base.


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
