## Variant: Tell a Forward, Future, FRA, and Swap Apart

**Abstract:** *All four contracts lock in future economics, but the thing exchanged and the settlement pattern tell you which name belongs on the box.*

> A contract locks in one stock purchase six months from now and settles only then. A second is exchange-traded and settles gains daily. A third locks a three-month borrowing rate beginning in one month. A fourth exchanges fixed interest for floating interest every quarter. Name each contract.

<span class="jargon-unlock">**Forward commitment. What is it?** A binding deal today about a later transaction. **Forward. What is it?** A private, usually one-settlement deal. **OTC. What is it?** Over the counter: privately negotiated rather than exchange-traded. **Future. What is it?** A standardized exchange-traded deal settled daily. **FRA. What is it?** A forward rate agreement: a cash settlement tied to a future market interest rate. **Swap. What is it?** A series of exchanges, like a bundle of forwards. **Counterparty. What is it?** The person or institution on the other side.</span>

**1. Match the cash-flow pattern**

The answers are:

$$
\boxed{\text{forward; future; FRA; interest-rate swap}}
$$

> [!NOTE]
> One later trade suggests a forward; daily marking suggests a future; a future borrowing rate suggests an FRA; repeated exchanges suggest a swap.

---

## Variant: Separate Price from Value

**Abstract:** *The forward price is the delivery price written into a new fair contract; value is what an existing contract is worth today.*

> A new six-month forward has a fair delivery price of $104. An old long forward requires payment of $100 at the same date. The discount factor to that date is 0.98. State the new forward price and the old contract's value.

<span class="jargon-unlock">**Forward price. What is it?** The delivery price that makes a brand-new forward worth zero. **Forward value. What is it?** Today's worth of an already-existing contract. **Delivery price. What is it?** The price the long agreed to pay at maturity.</span>

**1. Name the price; discount the advantage**

$$
F_t=\boxed{104}
$$

The old long gets the asset for 100 when the current fair deal requires 104.

$$
V_t=(104-100)(0.98)=\boxed{3.92}
$$

> [!NOTE]
> A new fair forward starts at zero value even though its forward price is not zero.

---

## Variant: Find Long and Short Payoffs at Expiration

**Abstract:** *At expiration there is no discounting left: compare the asset price with the agreed delivery price.*

> A forward's delivery price is $72. At expiration the asset is worth $79. Find the long and short payoffs.

<span class="jargon-unlock">**Long forward. What is it?** The side forced to buy the asset. Its payoff is $S_T-F_0$. **Short forward. What is it?** The side forced to sell. Its payoff is $F_0-S_T$.</span>

**1. Sit in each chair**

$$
V_T^{long}=79-72=\boxed{7}
$$

The short owns the mirror image.

$$
V_T^{short}=72-79=\boxed{-7}
$$

> [!NOTE]
> The two values must add to zero. If they do not, one viewpoint has been signed incorrectly.

---

## Variant: Price a No-Income Forward with Annual Compounding

**Abstract:** *Buying later must cost the same as buying now with borrowed money and carrying the asset to maturity.*

> Gold costs $1,900 now, generates no cash flow, and can be financed for nine months at 4% with annual compounding. Find the no-arbitrage forward price.

<span class="jargon-unlock">**No-arbitrage price. What is it?** The price that prevents a risk-free free lunch. **Annual compounding. What is its formula here?** $F_0=S_0(1+r)^T$.</span>

**1. Grow spot for the exact fraction of a year**

$$
F_0=1{,}900(1.04)^{9/12}=\boxed{1{,}956.72}
$$

> [!NOTE]
> The exponent is time in years. Nine months is $9/12$, not 9.

---

## Variant: Back Out the Spot Price

**Abstract:** *If a fair forward is simply spot carried forward, run the same equation backward to recover spot.*

> A one-year no-income forward price is $84.84 and the annual risk-free rate is 5%. Find the current spot price.

<span class="jargon-unlock">**Spot price. What is it?** The cash price for buying the asset right now. From $F_0=S_0(1+r)^T$, the reverse formula is $S_0=F_0/(1+r)^T$.</span>

**1. Discount instead of grow**

$$
S_0=\frac{84.84}{1.05}=\boxed{80.80}
$$

> [!NOTE]
> Forward means move money forward; spot means bring the forward amount back.

---

## Variant: Back Out the Financing Rate

**Abstract:** *The spot-to-forward gap is the financing growth embedded in the contract.*

> A no-income asset is $100 today and its six-month forward price is $102.47. Assume annual compounding. Find the annualized risk-free rate.

<span class="jargon-unlock">**Financing rate. What is it?** The borrowing or lending rate that carries today's asset price to the delivery date. The equation is $r=(F_0/S_0)^{1/T}-1$.</span>

**1. Undo the half-year power**

$$
r=\left(\frac{102.47}{100}\right)^{1/0.5}-1=\boxed{5.00\%}
$$

> [!NOTE]
> A six-month growth rate is not automatically the annual rate; annualize through the exponent.

---

## Variant: Value an Existing Long from the New Forward Price

**Abstract:** *The old long owns the discounted difference between today's fair delivery price and the old locked price.*

> A long forward locked $105. With three months left, a new matching forward is priced at $111.35. The annual discount rate is 5%. Find the old forward's value.

<span class="jargon-unlock">**Matching forward. What is it?** A new contract on the same asset with the same remaining maturity. **Long-value formula. What is it?** $V_t=(F_t-F_0)/(1+r)^{T-t}$.</span>

**1. Find and discount the delivery-price advantage**

$$
V_t=\frac{111.35-105}{1.05^{0.25}}=\boxed{6.27}
$$

> [!NOTE]
> Discount the difference because the saving is realized at delivery, not today.

---

## Variant: Value a Long Directly from Spot

**Abstract:** *For a no-income asset, owning the old long is equivalent to owning spot and owing the present value of the delivery price.*

> A no-income asset is $110. An old long forward requires $102 in three months. The annual rate is 5%. Find the contract value without first calculating a new forward price.

<span class="jargon-unlock">**Direct valuation. What is its formula?** $V_t=S_t-PV_t(F_0)$. **Present value. What is it?** Money at delivery translated into today's smaller amount.</span>

**1. Subtract today's value of the promised payment**

$$
V_t=110-\frac{102}{1.05^{0.25}}=\boxed{9.24}
$$

> [!NOTE]
> This route and $PV(F_t-F_0)$ are the same law written two ways.

---

## Variant: Flip a Long Value into a Short Value

**Abstract:** *A forward is a zero-sum promise, so changing seats changes only the sign.*

> A long forward is currently worth $3.60 per unit. The contract covers 25,000 units. Find the short position's total value.

<span class="jargon-unlock">**Zero-sum. What does it mean?** One side's gain is exactly the other side's loss. The invariant is $V_t^{short}=-V_t^{long}$.</span>

**1. Flip the sign, then scale**

$$
V_t^{short}=-3.60(25{,}000)=\boxed{-90{,}000}
$$

> [!NOTE]
> Do not recalculate the whole contract when only the viewpoint changes.

---

## Variant: Price a Forward with a Known Cash Dividend

**Abstract:** *A dividend belongs to the person holding the stock, not the forward, so remove its present value before carrying the stock price forward.*

> A stock is $70. It will pay a $2.20 dividend exactly when a one-month forward expires. The annual rate is 1%. Find the forward price.

<span class="jargon-unlock">**Carry benefit. What is it?** Cash or usefulness earned by owning the asset before delivery. **Known-income formula. What is it?** $F_0=FV(S_0)-FV(I)$, where $I$ is the ownership income.</span>

**1. Grow spot; remove the dividend at delivery**

$$
F_0=70(1.01)^{1/12}-2.20=\boxed{67.86}
$$

> [!NOTE]
> A benefit lowers the forward price because the forward buyer misses it.

---

## Variant: Handle a Dividend Paid Before Expiration

**Abstract:** *A dividend paid early must be carried from its payment date to the forward's delivery date, not for the contract's whole life.*

> A stock is $1,000. A $10 dividend arrives in one month. A three-month forward is priced at a 5% annual rate. Find the forward price.

<span class="jargon-unlock">**Future value of income. What is it?** The dividend grown only from the day it is received to delivery. The formula is $F_0=S_0(1+r)^T-D(1+r)^{T-t_D}$.</span>

**1. Use two different clocks**

$$
F_0=1{,}000(1.05)^{3/12}-10(1.05)^{2/12}=\boxed{1{,}002.19}
$$

> [!NOTE]
> Spot grows three months; the month-one dividend grows only the remaining two.

---

## Variant: Price an Index Future with Continuous Dividend Yield

**Abstract:** *A continuous dividend yield acts like a continuously flowing benefit that offsets financing cost.*

> An index is 3,500. Its continuously compounded dividend yield is 3%, the continuously compounded risk-free rate is 0.15%, and maturity is three months. Find the futures price.

<span class="jargon-unlock">**Continuous compounding. What is it?** Growth represented with $e^x$. **Dividend yield. What is it?** Dividends expressed as a rate of index value. The formula is $F_0=S_0e^{(r_c-q)T}$.</span>

**1. Net benefit against financing**

$$
F_0=3{,}500e^{(0.0015-0.03)(3/12)}=\boxed{3{,}475.15}
$$

> [!NOTE]
> Because $q>r_c$, the fair futures price sits below spot.

---

## Variant: Include Storage Cost and Convenience Benefit

**Abstract:** *Carry costs push the forward up; ownership benefits pull it down.*

> Copper is $8,000 per tonne. Continuous financing is 4%, storage cost is 1.5%, and the convenience yield is 0.5%. Find the six-month forward price.

<span class="jargon-unlock">**Storage cost. What is it?** The cost of physically holding the asset. **Convenience yield. What is it?** The non-cash usefulness of having the physical asset available. The formula is $F_0=S_0e^{(r_c+CC-CB)T}$.</span>

**1. Add costs and subtract benefits**

$$
F_0=8{,}000e^{(0.04+0.015-0.005)(0.5)}=\boxed{8{,}202.52}
$$

> [!NOTE]
> Cost gets a plus sign; benefit gets a minus sign.

---

## Variant: Execute Carry Arbitrage on an Overpriced Forward

**Abstract:** *If the market forward is too expensive, manufacture delivery cheaply and sell the expensive promise.*

> A no-income asset is $100, the one-year rate is 5%, and the market forward price is $110. Show the locked arbitrage profit at maturity.

<span class="jargon-unlock">**Carry arbitrage. What is it?** Borrow, buy the asset, and short an overpriced forward. **Short the forward. What does that mean?** Promise to deliver the asset and receive the delivery price.</span>

**1. Build the cheap synthetic delivery**

Borrow 100, buy the asset, and short at 110. At maturity deliver the asset for 110 and repay $100(1.05)=105$.

$$
\text{Profit}_T=110-105=\boxed{5}
$$

> [!NOTE]
> The trade uses borrowed cash and takes no price risk because the asset needed for delivery is already owned.

---

## Variant: Execute Reverse Carry on an Underpriced Forward

**Abstract:** *If the forward is too cheap, buy it and fund the later payment with proceeds from short-selling the asset now.*

> A shortable no-income asset is $100, the one-year rate is 5%, and the market forward is $101. Find the locked maturity profit.

<span class="jargon-unlock">**Reverse carry arbitrage. What is it?** Short the asset, invest the proceeds, and go long an underpriced forward. **Shortable. What does it mean?** The asset can be borrowed and sold now.</span>

**1. Lock both ends**

Short the asset for 100 and invest it. The investment becomes 105. Pay 101 under the long forward, receive the asset, and return it to the lender.

$$
\text{Profit}_T=105-101=\boxed{4}
$$

> [!NOTE]
> Underpriced forward: buy forward, short spot. Overpriced forward: sell forward, buy spot.

---

## Variant: Revalue after a New Dividend Is Announced

**Abstract:** *A newly announced dividend lowers the new fair forward price, which hurts an existing long if spot itself does not move.*

> A long forward locked $102. With three months left, spot is $110 and the rate is 5%. A $2 dividend is newly announced for delivery day. Find the long value.

<span class="jargon-unlock">**Revaluation. What is it?** Recalculating an old contract using today's inputs. **New forward price. What is it here?** $F_t=S_t(1+r)^{T-t}-D_T$.</span>

**1. Reprice, then discount the gap**

$$
F_t=110(1.05)^{0.25}-2=109.35
$$

Now compare that fair price with the old locked price.

$$
V_t=\frac{109.35-102}{1.05^{0.25}}=\boxed{7.26}
$$

> [!NOTE]
> Without the dividend the value would be 9.24; the new benefit belongs to the spot owner, not the forward long.

---

## Variant: Explain Why a Settled Future Has Zero Value

**Abstract:** *Daily settlement pays yesterday's gain or collects yesterday's loss, leaving a fresh contract at today's futures price.*

> A long futures position was entered at 102. Today's settlement price is 112.35. After today's variation margin is paid, what is the contract's value?

<span class="jargon-unlock">**Mark to market. What is it?** Settle the day's gain or loss in cash. **Variation margin. What is it?** That daily cash transfer. Immediately after settlement, futures value is reset to zero.</span>

**1. Separate cash already paid from value still inside**

The price move created cash, but that cash has already left the contract through margin.

$$
\boxed{V_{futures}=0\text{ immediately after settlement}}
$$

> [!NOTE]
> Do not confuse the cumulative trading profit with the post-settlement contract value.

---

## Variant: Decide When Forward and Futures Prices Can Differ

**Abstract:** *Daily futures cash flows can be reinvested, so their timing matters when price changes and interest rates move together.*

> Interest rates tend to rise on days when an asset's futures price rises. Relative to a forward, which contract is likely more valuable to the long and why?

<span class="jargon-unlock">**Positive correlation. What is it?** Two things tend to rise and fall together. **Daily settlement effect. What is it?** Futures gains arrive early and can be reinvested at then-current rates.</span>

**1. Follow the cash timing**

The futures long receives gains when rates are high and can reinvest them well. Losses tend to arrive when rates are low.

$$
\boxed{Futures\ price\ tends\ to\ exceed\ forward\ price}
$$

> [!NOTE]
> The module usually assumes equal prices unless this correlation effect is explicitly introduced.

---

## Variant: Revalue a Forward with Remaining Costs and Benefits

**Abstract:** *At the valuation date, rebuild today's fair delivery price using only costs and benefits that remain from today to expiration.*

> An old long forward locked $1,000. Seven months later, the asset is $1,050. Present value of remaining ownership costs is $4 and remaining benefits is $28. Five months remain and the annual rate is 2%. Find today's fair forward price and the old long's value.

<span class="jargon-unlock">**Remaining carry. What is it?** Only costs and benefits occurring after today's valuation date. **Productive asset. What is it?** An asset that gives a non-cash ownership benefit. The formulas are $F_t=FV_t(S_t+CC_t-CB_t)$ and $V_t=PV_t(F_t-F_0)$.</span>

**1. Reprice the remaining package**

$$
F_t=(1{,}050+4-28)(1.02)^{5/12}=\boxed{1{,}034.50}
$$

Now discount the advantage over the old price.

$$
V_t=\frac{1{,}034.50-1{,}000}{1.02^{5/12}}=\boxed{34.22}
$$

> [!NOTE]
> Do not reuse costs or benefits that already happened before the valuation date.

---

## Variant: Read FRA Tenor Notation

**Abstract:** *The two numbers tell you when the protected loan starts and ends; their difference gives the loan length.*

> Interpret a $2\times5$ FRA using 30-day months. State the FRA expiration, underlying loan end, and loan length.

<span class="jargon-unlock">**Tenor notation. What is it?** In $h\times T$, $h$ is months until the loan starts and $T$ is months until it ends. **Underlying loan. What is it?** The imagined deposit or borrowing whose rate drives the FRA cash settlement.</span>

**1. Read left, right, difference**

$$
h=60\text{ days},\qquad T=150\text{ days},\qquad m=T-h=90\text{ days}
$$

In words, that means:

$$
\boxed{\text{FRA expires in 2 months on a 3-month rate}}
$$

> [!NOTE]
> A $2\times5$ FRA is not a five-month loan.

---

## Variant: Calculate MRR Interest on Add-On Basis

**Abstract:** *Add-on interest is principal times annual rate times the fraction of a year.*

> A £10 million 90-day deposit earns a 2.55% market reference rate using a 360-day year. Find interest and terminal amount.

<span class="jargon-unlock">**MRR. What is it?** Market reference rate: the observable money-market rate used in the contract. **ACT/360. What is it?** Actual days in the period divided by a 360-day rate year. **Add-on basis. What is its formula?** $I=NA\times L_m\times t_m$ and $TA=NA(1+L_mt_m)$.</span>

**1. Shrink the annual rate to 90 days**

$$
I=10{,}000{,}000(0.0255)\left(\frac{90}{360}\right)=\boxed{63{,}750}
$$

Add interest back to principal for the amount returned.

$$
TA=10{,}000{,}000+63{,}750=\boxed{10{,}063{,}750}
$$

> [!NOTE]
> The FRA usually settles only the interest-rate difference; it does not exchange the £10 million principal.

---

## Variant: Derive a Fair FRA Rate from Two Spot Rates

**Abstract:** *Two ways of investing to the same final date must grow to the same amount, so the missing middle rate is forced.*

> The 90-day MRR is 0.90% and the 180-day MRR is 0.95%, both add-on with a 360-day year. Find the fair $3\times6$ FRA rate for the 90-day period beginning on day 90.

<span class="jargon-unlock">**Implied forward rate. What is it?** The future-period rate forced by today's two spot rates. Its formula is $FRA=[(1+L_Tt_T)/(1+L_ht_h)-1]/t_m$.</span>

**1. Divide long growth by short growth**

$$
FRA=\frac{\frac{1+0.0095(180/360)}{1+0.0090(90/360)}-1}{90/360}
=\boxed{0.9978\%}
$$

> [!NOTE]
> Do not subtract the two annual rates. Their compounding periods differ.

---

## Variant: Price a 1x4 FRA

**Abstract:** *Use the spot rate to month one, the spot rate to month four, and a three-month underlying period.*

> The 30-day MRR is 0.75% and the 120-day MRR is 0.92%. Using a 360-day year, find the fair $1\times4$ FRA rate.

<span class="jargon-unlock">**$1\times4$ FRA. What is it?** A rate fixed now for a three-month loan that begins one month from now. The formula is $FRA=[(1+L_{120}120/360)/(1+L_{30}30/360)-1]/(90/360)$.</span>

**1. Put every day count in its own slot**

$$
FRA=\frac{\frac{1+0.0092(120/360)}{1+0.0075(30/360)}-1}{90/360}
=\boxed{0.9761\%}
$$

> [!NOTE]
> The underlying accrual fraction is $90/360$, not $120/360$.

---

## Variant: Back Out a Missing Long Spot Rate from an FRA

**Abstract:** *A quoted FRA plus the short spot investment must reproduce the long spot investment.*

> The 90-day rate is 1.00% and the fair $3\times6$ FRA rate is 1.40%. All rates use add-on basis and a 360-day year. Find the 180-day spot rate.

<span class="jargon-unlock">**Long spot rate. What is it?** The rate running from today all the way to the later date. Rearrangement gives $1+L_Tt_T=(1+L_ht_h)(1+FRA\,t_m)$.</span>

**1. Chain the two shorter growth pieces**

$$
L_{180}=\frac{(1+0.01\times0.25)(1+0.014\times0.25)-1}{0.5}
=\boxed{1.202\%}
$$

> [!NOTE]
> Multiply growth factors first; do not average the rates.

---

## Variant: Count All Possible FRAs

**Abstract:** *Each FRA uses two distinct spot maturities: one start date and one later end date.*

> A curve contains 7 usable spot maturities. How many distinct FRAs can be implied?

<span class="jargon-unlock">**Distinct FRA. What is it?** One unique choice of an earlier start maturity and a later end maturity. The count is $\binom{n}{2}=n(n-1)/2$.</span>

**1. Choose two ordered-by-time endpoints**

$$
\binom{7}{2}=\frac{7(6)}{2}=\boxed{21}
$$

> [!NOTE]
> Time supplies the order automatically: the earlier maturity is the start.

---

## Variant: Value a Long FRA Before Expiration

**Abstract:** *A pay-fixed FRA gains when today's fair FRA rate rises above the old locked rate.*

> A $20 million pay-fixed/receive-floating FRA locked 0.70%. Today the matching FRA rate is 0.9978%, the underlying period is 90 days, and the discount rate to the loan end is 0.95% for 180 days. Find its value.

<span class="jargon-unlock">**Long FRA. What is it?** Pay fixed and receive floating; it benefits when rates rise. **Interim value formula. What is it?** $V_g=NA(FRA_g-FRA_0)t_m/[1+D_{T-g}t_{T-g}]$.</span>

**1. Price the rate advantage, then discount it**

$$
V_g=\frac{20{,}000{,}000(0.009978-0.007)(90/360)}{1+0.0095(180/360)}
=\boxed{14{,}820}
$$

> [!NOTE]
> Value is discounted to today from the underlying loan's end date in the module's interim-value convention.

---

## Variant: Value the Short Side of an FRA

**Abstract:** *The short FRA is the receive-fixed side, so its value is exactly the long side with the sign flipped.*

> The pay-fixed side of an FRA is worth +$14,820. Find the value to the receive-fixed/pay-floating side.

<span class="jargon-unlock">**Short FRA. What is it?** Receive fixed and pay floating; it benefits when rates fall. **Symmetry formula. What is it?** $V_g^{short}=-V_g^{long}$.</span>

**1. Change the chair, not the economics**

$$
V_g^{short}=-14{,}820=\boxed{-14{,}820}
$$

> [!NOTE]
> “Long” in an FRA means long rates, not long a bond price.

---

## Variant: Settle a Pay-Fixed FRA at Expiration

**Abstract:** *The loan interest difference belongs at the loan end, but an advanced-settled FRA pays its discounted value at the loan start.*

> A $20 million pay-fixed FRA locked 0.70%. At FRA expiration, the 90-day MRR is 1.10%. The settlement discount rate is 1.10%. Find the cash received.

<span class="jargon-unlock">**Advanced settled. What does it mean?** Cash changes hands when the underlying loan begins, before its interest would normally be paid. The formula is $NA(L_m-FRA_0)t_m/[1+D_mt_m]$.</span>

**1. Find end-date interest difference; bring it to the start**

$$
Settlement=\frac{20{,}000{,}000(0.011-0.007)(90/360)}{1+0.011(90/360)}
=\boxed{19{,}945.15}
$$

> [!NOTE]
> Higher floating than fixed pays the pay-fixed/receive-floating side.

---

## Variant: Settle the Receive-Fixed FRA

**Abstract:** *A receive-fixed FRA gains when the observed market rate finishes below the locked fixed rate.*

> A $10 million receive-fixed FRA locked 2.60% for 90 days. At expiration the 90-day MRR is 2.55%, and the settlement discount rate is 2.40%. Find the settlement cash flow to the receive-fixed side.

<span class="jargon-unlock">**Receive-fixed settlement formula. What is it?** $NA(FRA_0-L_m)t_m/[1+D_mt_m]$. **Settlement cash flow. What is it?** The one net amount paid between the two parties.</span>

**1. Fixed beats floating by five basis points**

$$
Settlement=\frac{10{,}000{,}000(0.026-0.0255)(90/360)}{1+0.024(90/360)}
=\boxed{1{,}242.54}
$$

> [!NOTE]
> A basis point is 0.01 percentage point, so five basis points is $0.0005$ as a decimal.

---

## Variant: Catch Zero and Negative FRA Settlements

**Abstract:** *Settlement direction comes entirely from the market-minus-contract rate spread.*

> A pay-fixed FRA locked 1.20%. State its settlement sign if the observed MRR is (a) 1.20% and (b) 0.90%.

<span class="jargon-unlock">**Settlement sign. What is it?** Positive means cash received by the named party; negative means cash paid. For pay-fixed, the numerator is $L_m-FRA_0$.</span>

**1. Compare, without unnecessary arithmetic**

$$
(a)\ 1.20\%-1.20\%=0\Rightarrow\boxed{0}
$$

Below the locked rate, the pay-fixed side loses.

$$
(b)\ 0.90\%-1.20\%<0\Rightarrow\boxed{\text{pay-fixed side pays}}
$$

> [!NOTE]
> Before touching a calculator, predict the sign from the rate direction.

---

## Variant: Choose the Correct FRA Hedge

**Abstract:** *A future borrower fears higher rates; a future lender fears lower rates.*

> A company will borrow for three months beginning six months from now. Which $6\times9$ FRA side hedges it?

<span class="jargon-unlock">**Hedge. What is it?** A position designed to offset an unwanted risk. **Future borrower. What is the danger?** Market rates may rise. **Pay-fixed FRA. What is it?** Pay the locked rate and receive floating, producing a gain when rates rise.</span>

**1. Choose the payoff that fights the pain**

$$
\boxed{\text{Long }6\times9\text{ FRA: pay fixed, receive floating}}
$$

> [!NOTE]
> Future lender: receive fixed. Future borrower: pay fixed.

---

## Variant: Calculate Accrued Interest

**Abstract:** *Accrued interest is the coupon earned since the last coupon date, even though it has not yet been paid.*

> A 1.5% semiannual Treasury note has $100 par. Sixty days have passed in a 180-day coupon period. Find accrued interest per $100 par.

<span class="jargon-unlock">**Accrued interest. What is it?** The seller's earned slice of the next coupon. Its formula is $AI=(NAD/NTD)(C/n)$, where $NAD$ is days accrued, $NTD$ is total days, $C$ is annual coupon per 100, and $n$ is payments per year.</span>

**1. Earn one-third of the half-year coupon**

$$
AI=\frac{60}{180}\left(\frac{1.5}{2}\right)=\boxed{0.25}
$$

> [!NOTE]
> Use days since the last coupon, not days until the next coupon.

---

## Variant: Convert Clean Price to Full Price

**Abstract:** *The invoice-like full price includes accrued interest; the quoted clean price does not.*

> A bond's clean price is 101.00 and accrued interest is 0.25. Find its full spot price.

<span class="jargon-unlock">**Clean price. What is it?** The quoted bond price excluding accrued interest. **Full price. What is it?** Clean price plus accrued interest; it is also called dirty price. The formula is $S_0=B_0+AI_0$.</span>

**1. Put the earned coupon slice back in**

$$
S_0=101.00+0.25=\boxed{101.25}
$$

> [!NOTE]
> Carry formulas use the full economic price, even when the market quote is clean.

---

## Variant: Price a Bond Forward with No Interim Coupon

**Abstract:** *Start with the bond's full price and finance it to delivery.*

> A bond's clean price is 104.00, current accrued interest is 0.17, no coupon arrives before a three-month forward expires, and the annual rate is 1.65%. Find the full forward price.

<span class="jargon-unlock">**Full forward price. What is it?** The all-in delivery value before converting it into a quoted futures price. With no interim coupon, $F_0=(B_0+AI_0)(1+r)^T$.</span>

**1. Carry today's full bond price**

$$
F_0=104.17(1.0165)^{3/12}=\boxed{104.60}
$$

> [!NOTE]
> “No interim coupon” means the carry-benefit term is zero, not that the bond has no coupon rate.

---

## Variant: Remove a Coupon Paid Before Bond-Forward Delivery

**Abstract:** *A coupon collected by the spot owner before delivery is a carry benefit and must be removed from the forward price.*

> A bond's full spot price is 102. A coupon of 2 is paid in six months, delivery is in one year, and the annual rate is 4%. Find the bond forward price.

<span class="jargon-unlock">**Coupon income. What is it?** Cash paid by the bond before delivery. The formula is $F_0=FV(B_0+AI_0)-FV(CI)$.</span>

**1. Grow the bond for a year; grow the coupon for only six months**

$$
F_0=102(1.04)-2(1.04)^{0.5}=\boxed{104.04}
$$

> [!NOTE]
> The forward buyer does not receive a coupon paid before delivery.

---

## Variant: Turn Full Forward Price into a Quoted Bond Futures Price

**Abstract:** *The exchange quote removes delivery-date accrued interest and divides by the bond's conversion factor.*

> A bond's full forward price is 104.60, accrued interest at futures delivery will be 0.67, and its conversion factor is 0.7025. Find the quoted futures price.

<span class="jargon-unlock">**Conversion factor. What is it?** An exchange adjustment that makes deliverable bonds with different coupons and maturities comparable. **Quoted futures price. What is its formula?** $Q_0=(F_0-AI_T)/CF$.</span>

**1. Strip delivery accrued interest; scale by the factor**

$$
Q_0=\frac{104.60-0.67}{0.7025}=\boxed{147.94}
$$

> [!NOTE]
> Subtract accrued interest before dividing by the conversion factor.

---

## Variant: Recover Full Delivery Price from a Futures Quote

**Abstract:** *Reverse the quoting convention: multiply by the conversion factor and then restore accrued interest.*

> A bond futures quote is 125.00, the conversion factor is 0.90, and delivery-date accrued interest is 0.20. Find the full delivery invoice per $100 par.

<span class="jargon-unlock">**Invoice price. What is it?** The actual amount the futures long pays for the delivered bond, before any contract multiplier. Its formula is $Invoice=Q\times CF+AI_T$.</span>

**1. Undo the quote adjustment**

$$
Invoice=125(0.90)+0.20=\boxed{112.70}
$$

> [!NOTE]
> A futures quote of 125 does not mean the delivered bond costs 125.

---

## Variant: Value a Bond Forward Position with Quoted Prices

**Abstract:** *Discount the price-point gain, convert points to a fraction of par, then multiply by contract notional and count.*

> Eight JGB forwards each cover JPY100 million par. The long locked 153; the matching six-month forward is now 155. The annual rate is 0.12%. Find total value.

<span class="jargon-unlock">**Price point. What is it?** One percent of par because bond prices are quoted per 100. **Contract notional. What is it?** The face amount used to scale the quoted-price result.</span>

**1. Discount the two-point advantage**

$$
\Delta_{PV}=\frac{155-153}{1.0012^{6/12}}=1.9988\text{ points}
$$

Now translate points into yen across all contracts.

$$
V=\frac{1.9988}{100}(100{,}000{,}000)(8)=\boxed{JPY15{,}990{,}409}
$$

> [!NOTE]
> The division by 100 is the step that turns quoted points into a fraction of notional.

---

## Variant: Find Bond-Futures Arbitrage Profit

**Abstract:** *Compare the full futures invoice with the carried full spot bond price in the same units, then discount the locked delivery-date gap.*

> A bond has clean price 112.00 and current accrued interest 0.08. No coupon is paid before three-month delivery. The rate is 0.30%. Futures quote is 125, conversion factor 0.90, and delivery accrued interest 0.20. Find arbitrage profit per $100 today.

<span class="jargon-unlock">**Mispricing. What is it?** The market invoice minus the no-arbitrage full forward price. **Present arbitrage profit. What is it?** That locked delivery gap discounted to today.</span>

**1. Put both choices on a full-price basis**

$$
F_0=112.08(1.003)^{0.25}=112.1640
$$

The market futures contract instead demands this full invoice:

$$
Invoice=125(0.90)+0.20=112.70
$$

Discount the excess market invoice to today.

$$
Profit_0=\frac{112.70-112.1640}{1.003^{0.25}}=\boxed{0.5356}
$$

> [!NOTE]
> Comparing the raw quote 125 with spot 112 mixes two different quote systems.

---

## Variant: Identify the Cheapest-to-Deliver Bond

**Abstract:** *The futures short chooses the eligible bond that is cheapest after the exchange's conversion adjustment.*

> Bond A has full forward price 112.0, delivery accrued interest 0.2, and conversion factor 0.90. Bond B has 118.0, 0.4, and 0.95. Which is cheapest to deliver based on implied quoted cost?

<span class="jargon-unlock">**Cheapest-to-deliver bond. What is it?** The eligible bond that costs the short least after conversion-factor adjustment. Compare $(F-AI_T)/CF$ across bonds.</span>

**1. Translate both bonds into comparable quotes**

$$
Q_A=\frac{112.0-0.2}{0.90}=124.22
$$

Apply the same quote translation to Bond B.

$$
Q_B=\frac{118.0-0.4}{0.95}=123.79
$$

The smaller adjusted cost wins.

$$
\boxed{\text{Bond B is cheapest to deliver}}
$$

> [!NOTE]
> Lowest cash bond price alone does not decide CTD; the conversion factor matters.

---

## Variant: Price a Discount Factor from a Spot Rate

**Abstract:** *A present value factor tells you today's value of one currency unit paid at a specific future date.*

> The 180-day add-on spot rate is 2.00% on a 360-day year. Find the present value factor for $1 paid on day 180.

<span class="jargon-unlock">**Present value factor. What is it?** The amount today that grows to 1 at the stated spot rate. The formula is $PV_i(1)=1/[1+R_i(NAD_i/NTD)]$.</span>

**1. Discount one future dollar**

$$
PV_{180}(1)=\frac{1}{1+0.02(180/360)}=\boxed{0.990099}
$$

> [!NOTE]
> Each swap payment date needs its own factor from the term structure.

---

## Variant: Price a Plain-Vanilla Interest-Rate Swap

**Abstract:** *Choose the fixed rate that makes the fixed-rate bond worth par, because the floating-rate bond is worth par on a reset date.*

> A three-year annual-pay swap has discount factors 0.990099, 0.977876, and 0.965136. Find the par fixed swap rate.

<span class="jargon-unlock">**Plain-vanilla interest-rate swap. What is it?** One party pays a fixed rate and the other pays a market floating rate in the same currency. **Par swap rate. What is it?** The fixed rate making the swap worth zero initially.</span>

**1. Make fixed coupons fill the gap to par**

$$
r_{FIX}=\frac{1-PV_3}{AP\sum PV_i}
=\frac{1-0.965136}{1(0.990099+0.977876+0.965136)}
=\boxed{1.1887\%}
$$

> [!NOTE]
> The final discount factor belongs in both the numerator's gap and the denominator's sum.

---

## Variant: Convert an Annual Swap Rate into a Payment

**Abstract:** *The fixed leg pays notional times annual rate times the accrual-period fraction.*

> A $50 million quarterly swap has a fixed rate of 2.20% and uses 90/360. Find each fixed payment.

<span class="jargon-unlock">**Accrual period. What is it?** The fraction of a rate year covered by one payment. **Fixed swap amount. What is its formula?** $FS=NA\times AP\times r_{FIX}$.</span>

**1. Pay one quarter of the annual rate**

$$
FS=50{,}000{,}000\left(\frac{90}{360}\right)(0.022)=\boxed{275{,}000}
$$

> [!NOTE]
> Do not apply a full annual rate to a quarterly payment.

---

## Variant: Value a Receive-Fixed Interest-Rate Swap

**Abstract:** *Receiving an old fixed rate above today's fair fixed rate is valuable; discount every remaining rate advantage.*

> A €100 million receive-fixed swap pays annually. Its old fixed rate is 2.00%, today's matching fixed rate is 1.30%, and remaining discount factors sum to 4.822107. Find value.

<span class="jargon-unlock">**Receive-fixed swap. What is it?** Receive the contractual fixed payments and pay floating. Its reset-date formula is $V=NA(FS_0-FS_t)\sum PV_i$.</span>

**1. Price seven-tenths of a percent across all remaining dates**

$$
V=100{,}000{,}000(0.020-0.013)(4.822107)
=\boxed{3{,}375{,}475}
$$

> [!NOTE]
> Old fixed above current fixed helps the receiver and hurts the payer.

---

## Variant: Value the Pay-Fixed Side

**Abstract:** *The pay-fixed party owns the exact opposite cash flows, so its value is the negative of receive-fixed value.*

> The receive-fixed side of a swap is worth €3,375,475. Find the pay-fixed side's value.

<span class="jargon-unlock">**Pay-fixed swap. What is it?** Pay the contractual fixed rate and receive floating. **Counterparty symmetry. What is it?** $V_{pay-fixed}=-V_{receive-fixed}$.</span>

**1. Flip the viewpoint**

$$
V_{pay-fixed}=\boxed{-€3{,}375{,}475}
$$

> [!NOTE]
> The swap does not create value in total; it moves value between counterparties.

---

## Variant: Predict Swap Value from a Rate Move

**Abstract:** *A fixed payment becomes attractive when new market fixed rates fall and unattractive when they rise.*

> Market swap rates fall from 3% to 1.5%. Without calculating, state the sign of a receive-fixed position and a pay-fixed position entered at 3%.

<span class="jargon-unlock">**Market swap rate. What is it?** The fixed rate on a new zero-value swap today. **Receive-fixed position. What is it?** Receive the old contractual rate and pay floating.</span>

**1. Compare old fixed with replacement fixed**

$$
\boxed{V_{receive-fixed}>0,\qquad V_{pay-fixed}<0}
$$

> [!NOTE]
> Predict the sign before multiplying notional and discount factors.

---

## Variant: Back Out the Current Swap Rate from Value

**Abstract:** *Divide the swap's value by notional and the discount-factor sum to recover the fixed-rate advantage.*

> A $40 million receive-fixed swap has value $600,000, an old annual fixed rate of 2.50%, and remaining discount factors summing to 3. Find today's matching fixed rate.

<span class="jargon-unlock">**Matching fixed rate. What is it?** The par rate on a new swap with the same remaining payment dates. Rearrangement gives $FS_t=FS_0-V/(NA\sum PV_i)$.</span>

**1. Peel value back into a rate spread**

$$
FS_t=0.025-\frac{600{,}000}{40{,}000{,}000(3)}=\boxed{2.00\%}
$$

> [!NOTE]
> This shortcut applies on a payment/reset date under the module's valuation setup.

---

## Variant: See an Interest-Rate Swap as Two Bonds

**Abstract:** *Receive fixed/pay floating has the same cash-flow value as long a fixed-rate bond and short a floating-rate bond.*

> A fixed-rate bond leg is worth 101.4 per 100 notional and the floating-rate bond leg is worth 100 on a reset date. Find the receive-fixed swap value per 100.

<span class="jargon-unlock">**Bond replication. What is it?** Replacing a derivative with ordinary positions that create identical cash flows. **Floating-rate bond at par. What does it mean?** Immediately after reset, its coupon matches the market, so value is 100.</span>

**1. Long incoming leg, short outgoing leg**

$$
V_{swap}=V_{FIX}-V_{FLT}=101.4-100=\boxed{1.4}
$$

> [!NOTE]
> Pay-fixed reverses the bond positions and the sign.

---

## Variant: Set Currency-Swap Notionals

**Abstract:** *The two principals must be equal in value at the opening spot exchange rate.*

> A currency swap exchanges A$100 million against US dollars at A$1.14 per US$1. Find the US-dollar notional.

<span class="jargon-unlock">**Currency-swap notional. What is it?** The principal amount used to calculate payments in each currency. **Spot quote A$/US$. What does it mean?** Australian dollars per one US dollar. The identity is $NA_A=S_0NA_B$.</span>

**1. Divide A$ by A$ per US$**

$$
NA_{US}=\frac{A\$100{,}000{,}000}{A\$1.14/US\$1}
=\boxed{US\$87{,}719{,}298}
$$

> [!NOTE]
> Write units beside the exchange rate; the unwanted currency should cancel.

---

## Variant: Price Both Fixed Rates in a Currency Swap

**Abstract:** *Each currency has its own yield curve, so each leg gets its own par swap rate.*

> Quarterly A$ discount factors sum to 3.933870 with final factor 0.972763. US$ factors sum to 3.995009 with final factor 0.997506. Find both annual fixed rates using $AP=0.25$.

<span class="jargon-unlock">**Fixed-for-fixed currency swap. What is it?** Exchange fixed-rate payments and principal in one currency for fixed-rate payments and principal in another. For currency $k$, $r_k=(1-PV_{n,k})/(AP\sum PV_{i,k})$.</span>

**1. Price each bond leg separately**

$$
r_A=\frac{1-0.972763}{0.25(3.933870)}=\boxed{2.7695\%}
$$

Repeat using only the US-dollar curve.

$$
r_{US}=\frac{1-0.997506}{0.25(3.995009)}=\boxed{0.2497\%}
$$

> [!NOTE]
> Never use one country's curve to discount the other country's cash flows.

---

## Variant: Find Currency-Swap Periodic Payments

**Abstract:** *Once each annual fixed rate and notional are known, each leg's payment is ordinary fixed interest in its own currency.*

> An A$ leg has A$100 million notional at 2.7695%; a US$ leg has US$87,719,298 at 0.2497%. Payments are quarterly. Find both payments.

<span class="jargon-unlock">**Swap leg. What is it?** One stream of payments inside a swap. **Periodic fixed payment. What is its formula?** $FS_k=NA_k\times AP\times r_k$.</span>

**1. Keep the currencies separate**

$$
FS_A=100{,}000{,}000(0.25)(0.027695)=\boxed{A\$692{,}375}
$$

The US-dollar leg uses its own notional and rate.

$$
FS_{US}=87{,}719{,}298(0.25)(0.002497)=\boxed{US\$54{,}759}
$$

> [!NOTE]
> Currency-swap cash flows are generally exchanged, not netted, because their units differ.

---

## Variant: Value a Fixed-for-Fixed Currency Swap

**Abstract:** *Value the bond you receive, subtract the spot-converted bond you pay, and keep everything in one currency.*

> A dealer receives A$ and pays US$ in a currency swap. The A$ notional is 100 million, its periodic fixed rate is 0.692375%, its discount-factor sum is 3.967683, and its final factor is 0.986031. The US$ notional is 87,719,298, its periodic rate is 0.062425%, its factor sum is 3.994841, and its final factor is 0.998336. Spot is A$1.13/US$1. Find value in A$.

<span class="jargon-unlock">**Receive-currency-a value. What is it?** The present value of currency-a inflows minus the spot-converted present value of currency-b outflows. The formula is $V_{CS}=NA_a[c_a\sum PV_{i,a}+PV_{n,a}]-S_tNA_b[c_b\sum PV_{i,b}+PV_{n,b}]$.</span>

**1. Price each bond; convert only the US$ bond**

$$
V_A=100{,}000{,}000[0.00692375(3.967683)+0.986031]=101{,}350{,}225
$$

Price the US-dollar bond on its own curve.

$$
V_{US}=87{,}719{,}298[0.00062425(3.994841)+0.998336]=87{,}792{,}086
$$

Convert that bond to A$ and subtract it.

$$
V_{CS}=101{,}350{,}225-1.13(87{,}792{,}086)=\boxed{A\$2{,}145{,}168}
$$

> [!NOTE]
> “Receive A$” fixes the sign: long the A$ bond, short the US$ bond.

---

## Variant: Convert Currency-Swap Value to the Other Party and Currency

**Abstract:** *First flip the counterparty sign; then divide by an A$-per-US$ quote to convert A$ into US$.*

> A receive-A$ dealer's currency swap is worth A$2,145,167. Spot is A$1.13 per US$1. Find the value to the opposite party in US dollars.

<span class="jargon-unlock">**Opposite party. What does it mean?** The counterparty paying A$ and receiving US$. **Currency conversion. What is it here?** Divide A$ by A$/US$ to obtain US$.</span>

**1. Flip, then convert**

$$
V_{opposite,A}=-A\$2{,}145{,}167
$$

Now cancel A$ through the quoted exchange-rate units.

$$
V_{opposite,US}=\frac{-2{,}145{,}167}{1.13}=\boxed{-US\$1{,}898{,}378}
$$

> [!NOTE]
> Reversing the exchange-rate quote without reversing the arithmetic is a common unit error.

---

## Variant: Predict Currency-Swap Value from FX Movement

**Abstract:** *If the currency you must pay becomes more expensive, your swap position gets worse, all else equal.*

> A US firm receives US$ and pays A$ under a swap. The quote falls from A$1.14/US$ to A$1.05/US$, with yield curves unchanged. What happens to the firm's value?

<span class="jargon-unlock">**A$ strengthens. What does it mean?** One US dollar buys fewer Australian dollars. **FX risk. What is it?** Swap value changes because the two future currency streams translate at a new spot rate.</span>

**1. Follow the payment burden**

The firm owes A$. Each US$ now buys fewer A$, so those A$ payments are more expensive in US$.

$$
\boxed{\text{The US firm's swap value falls}}
$$

> [!NOTE]
> A currency swap has two interest-rate risks plus one exchange-rate risk.

---

## Variant: See a Currency Swap as Two Bonds

**Abstract:** *A fixed-for-fixed currency swap is long one fixed-rate bond and short another after translating them into one reporting currency.*

> In A$ terms, the received A$ bond is worth A$102 million. The US$ bond owed is worth US$88 million, and spot is A$1.10/US$. Find the swap value to the A$ receiver.

<span class="jargon-unlock">**Reporting currency. What is it?** The single currency used to state the answer. **Bond-difference formula. What is it?** $V_{CS}=V_a-S_tV_b$ for the party receiving currency $a$.</span>

**1. Translate before subtracting**

$$
V_{CS}=102-1.10(88)=\boxed{A\$5.2m}
$$

> [!NOTE]
> You cannot subtract 102 A$ from 88 US$ until one side is converted.

---

## Variant: Calculate a Positive Equity-Swap Cash Flow

**Abstract:** *The receive-equity side gets the equity return and pays the fixed slice for the same period.*

> A €5 million quarterly receive-equity/pay-fixed swap has a 1.6% annual fixed rate. The equity index returns +4.0% during the quarter. Find the net cash flow to the receive-equity side.

<span class="jargon-unlock">**Equity swap. What is it?** A contract exchanging an equity return for fixed, floating, or another equity return. **Receive-equity cash flow. What is its formula?** $NA(RE-AP\,r_{FIX})$ when $RE$ is already the period return.</span>

**1. Compare two quarterly returns**

$$
CF=5{,}000{,}000[0.04-(90/360)(0.016)]
=\boxed{€180{,}000}
$$

> [!NOTE]
> The 4% equity return is already quarterly; do not multiply it by $90/360$ again.

---

## Variant: Calculate a Negative Equity-Swap Cash Flow

**Abstract:** *If the equity leg loses money, the receive-equity party may owe both the equity loss and the fixed payment.*

> Use the same €5 million quarterly swap and 1.6% annual fixed rate, but the quarterly equity return is -6%. Find the receive-equity side's cash flow.

<span class="jargon-unlock">**Negative equity return. What does it mean in a swap?** The receive-equity side pays the loss rather than receiving a gain. The formula remains $NA(RE-AP\,r_{FIX})$.</span>

**1. Keep the negative sign**

$$
CF=5{,}000{,}000[-0.06-0.25(0.016)]
=\boxed{-€320{,}000}
$$

> [!NOTE]
> A negative equity leg can create a large liquidity need even though no shares are owned.

---

## Variant: Price the Fixed Leg of an Equity Swap

**Abstract:** *With equity notional equal to bond par, the fixed rate is the same par rate used for an interest-rate swap.*

> A five-year annual equity swap has discount factors 0.990099, 0.977876, 0.965136, 0.951529, and 0.937467. Find its fair annual fixed rate.

<span class="jargon-unlock">**Fair equity-swap fixed rate. What is it?** The fixed rate making a new fixed-versus-equity swap worth zero. The formula is $r_{FIX}=(1-PV_n)/(AP\sum PV_i)$ when equity notional equals par.</span>

**1. Fill the discounted gap to par**

$$
\sum PV_i=4.822107
$$

Use the sum with the final factor.

$$
r_{FIX}=\frac{1-0.937467}{1(4.822107)}=\boxed{1.2968\%}
$$

> [!NOTE]
> The future equity returns are unknown, but no forecast is required to price the swap.

---

## Variant: Value a Receive-Fixed, Pay-Equity Swap

**Abstract:** *Compare the current value of the promised fixed bond with the equity notional grown by the index since the last reset.*

> A €10 million receive-fixed/pay-equity swap was entered when the index was 100. It is now 105. The old fixed leg is currently worth €10,216,019 and bond par equals equity notional. Find the swap value.

<span class="jargon-unlock">**Last reset price. What is it?** The equity level from which the current swap-period return is measured. **Valuation formula. What is it?** $V_{EQ,t}=V_{FIX}(C_0)-(S_t/S_{t-1})NA_E-PV(Par-NA_E)$.</span>

**1. Value the equity obligation**

$$
V_{equity}=\frac{105}{100}(10{,}000{,}000)=10{,}500{,}000
$$

Subtract that obligation from the fixed-leg value.

$$
V_{EQ}=10{,}216{,}019-10{,}500{,}000-0
=\boxed{-€283{,}981}
$$

> [!NOTE]
> Receive-fixed/pay-equity benefits from lower equity performance, not higher.

---

## Variant: Find the Break-Even Equity Index Level

**Abstract:** *Set swap value to zero and solve for the index level that makes the equity leg exactly equal the fixed-leg value.*

> A receive-fixed/pay-equity swap has fixed-leg value €10,216,019, notional €10 million, last-reset index 100, and $Par=NA_E$. Find the current index that makes value zero.

<span class="jargon-unlock">**Break-even index. What is it?** The current equity level that makes neither party's position valuable. With $Par=NA_E$, $S_t=S_{t-1}V_{FIX}/NA_E$.</span>

**1. Solve the zero-value equation**

$$
0=10{,}216{,}019-\frac{S_t}{100}(10{,}000{,}000)
$$

Rearrange for the unknown index level.

$$
S_t=100\left(\frac{10{,}216{,}019}{10{,}000{,}000}\right)=\boxed{102.1602}
$$

> [!NOTE]
> The break-even level is not automatically the original index level because the fixed leg has changed value.

---

## Variant: Include a Par-Notional Mismatch in Equity-Swap Value

**Abstract:** *If the fixed bond's par and equity notional differ, finance the terminal difference instead of silently dropping it.*

> A receive-fixed/pay-equity swap has $V_{FIX}=10.4$ million, current equity-leg value $10.2$ million, bond par $10.5$ million, equity notional $10.0$ million, and the discount factor to maturity is 0.96. Find swap value.

<span class="jargon-unlock">**Par-notional mismatch. What is it?** The fixed bond repays a different terminal principal from the equity position. The adjustment is $PV(Par-NA_E)$ in $V_{EQ}=V_{FIX}-V_{equity}-PV(Par-NA_E)$.</span>

**1. Price the terminal mismatch**

$$
PV(Par-NA_E)=0.96(10.5-10.0)=0.48m
$$

Subtract it along with the equity obligation.

$$
V_{EQ}=10.4-10.2-0.48=\boxed{-0.28m}
$$

> [!NOTE]
> The mismatch term is zero only when the problem explicitly makes par equal to equity notional.

---

## Variant: Net an Equity-for-Equity Swap Cash Flow

**Abstract:** *An equity-for-equity swap simply pays one equity return and receives another on the same notional.*

> A $12 million swap receives Index A, which returns 3%, and pays Index B, which returns 5% during the period. Find the net cash flow to the receive-A side.

<span class="jargon-unlock">**Equity-for-equity swap. What is it?** Exchange one equity return for another without a fixed-rate leg. Its cash flow is $NA(RE_A-RE_B)$.</span>

**1. Net the two period returns**

$$
CF=12{,}000{,}000(0.03-0.05)=\boxed{-240{,}000}
$$

> [!NOTE]
> The two matching fixed legs in a replication cancel, which is why no fixed rate must be priced.

---

## Variant: Decide Whether Dividends Belong in an Equity Leg

**Abstract:** *The contract definition decides whether the equity return is price-only or total return; never assume.*

> An index rises from 200 to 206 and distributes dividends worth 2 index points. Find the period return for (a) a price-return equity leg and (b) a total-return equity leg.

<span class="jargon-unlock">**Price return. What is it?** Return from the index-level change only. **Total return. What is it?** Price change plus dividends, assuming dividends are included or reinvested.</span>

**1. Read the contract's return definition**

$$
RE_{price}=\frac{206-200}{200}=\boxed{3\%}
$$

Now include the dividend points for total return.

$$
RE_{total}=\frac{206-200+2}{200}=\boxed{4\%}
$$

> [!NOTE]
> A one-point return-definition difference can materially change a large-notional settlement.

---

## Variant: Appendix — Derive the No-Income Forward Price

**Abstract:** *Two routes to owning the asset at delivery must have the same cost or a risk-free trade appears.*

> Derive the no-income forward-price formula under annual compounding.

<span class="jargon-unlock">**Law of one price. What is it?** Two strategies with identical future cash flows must have the same price. **Invariant. What is it here?** Delivery through spot-and-carry must cost the same as delivery through the forward.</span>

**1. Build the replicating route**

Borrow $S_0$, buy the asset, and hold it. At $T$, you own the asset and owe:

$$
S_0(1+r)^T
$$

A long forward also gives the asset at $T$ for $F_0$. Equal future assets force equal future costs:

$$
\boxed{F_0=S_0(1+r)^T}
$$

> [!NOTE]
> This is not a price forecast. It is the delivery price that blocks arbitrage today.

---

## Variant: Appendix — Derive Forward Value

**Abstract:** *Cancel an old forward with an opposite new forward; the only cash left is the delivery-price difference.*

> Derive the value of an existing long forward using today's matching forward price.

<span class="jargon-unlock">**Offsetting forward. What is it?** A new opposite contract with the same asset and maturity. **Value additivity. What is it?** The value of combined positions equals the sum of their values.</span>

**1. Lock the remaining cash flow**

Old long: receive asset and pay $F_0$. New short: deliver that asset and receive $F_t$. The asset cancels, leaving $F_t-F_0$ at $T$.

$$
\boxed{V_t^{long}=PV_t(F_t-F_0)}
$$

For annual compounding:

$$
\boxed{V_t^{long}=\frac{F_t-F_0}{(1+r)^{T-t}}}
$$

> [!NOTE]
> The invariant is long-short symmetry: $V_t^{short}=-V_t^{long}$.

---

## Variant: Appendix — Derive the General Carry Formula

**Abstract:** *Start with spot, add every ownership cost, subtract every ownership benefit, and carry the net amount to delivery.*

> Derive the forward formula for an asset with present-value carry costs $CC_0$ and benefits $CB_0$.

<span class="jargon-unlock">**Carry balance. What is it?** The net cost of owning the asset until delivery. **Carry cost. What is it?** Storage, insurance, or other ownership expense. **Carry benefit. What is it?** Income or convenience received only by the owner.</span>

**1. Price the complete spot-and-carry package**

Today's funded amount is:

$$
S_0+CC_0-CB_0
$$

Grow it to delivery:

$$
\boxed{F_0=FV(S_0+CC_0-CB_0)}
$$

With continuous rates:

$$
\boxed{F_0=S_0e^{(r_c+CC-CB)T}}
$$

> [!NOTE]
> The signs follow ownership: costs hurt the owner; benefits help the owner.

---

## Variant: Appendix — Derive the FRA Rate

**Abstract:** *Investing to the long date directly must equal investing to the short date and then rolling at the FRA rate.*

> Derive the no-arbitrage FRA rate between times $h$ and $T$, where $m=T-h$.

<span class="jargon-unlock">**Roll investment. What is it?** Invest to $h$, then reinvest from $h$ to $T$. **Growth-factor invariant. What is it?** Direct and rolled investments ending at $T$ must produce the same cash.</span>

**1. Equate the two routes**

$$
1+L_Tt_T=(1+L_ht_h)(1+FRA_0t_m)
$$

Divide by the short growth factor and solve:

$$
\boxed{FRA_0=\frac{\frac{1+L_Tt_T}{1+L_ht_h}-1}{t_m}}
$$

> [!NOTE]
> Every $t$ belongs to its own rate: long spot, short spot, or underlying loan.

---

## Variant: Appendix — Derive Advanced FRA Settlement

**Abstract:** *Compute the interest difference due at the loan end, then discount it one loan period because the FRA pays at the loan start.*

> Derive expiration settlement to the pay-fixed/receive-floating FRA side.

<span class="jargon-unlock">**Advanced set. What is it?** The floating rate is observed at the loan's start. **Advanced settled. What is it?** The FRA cash is paid then too. **Arrears interest. What is it?** Ordinary loan interest paid at the loan's end.</span>

**1. Form the arrears-date difference**

$$
Difference_T=NA(L_m-FRA_0)t_m
$$

Bring it back one loan period:

$$
\boxed{Settlement_h=\frac{NA(L_m-FRA_0)t_m}{1+D_mt_m}}
$$

> [!NOTE]
> Receive-fixed reverses the rate difference to $FRA_0-L_m$.

---

## Variant: Appendix — Derive the Bond-Futures Quote

**Abstract:** *Carry the full bond, remove coupons received before delivery, strip delivery accrued interest, then apply the conversion factor.*

> Derive the quoted bond-futures price from a clean spot bond price.

<span class="jargon-unlock">**Full spot bond. What is it?** $B_0+AI_0$. **Interim coupon income. What is it?** Coupons received before delivery. **Quoted futures price. What is it?** The standardized exchange quote after delivery adjustments.</span>

**1. Build the full forward value**

$$
F_0=FV(B_0+AI_0)-FVCI
$$

The delivery invoice identity is $F_0=Q_0CF+AI_T$. Solve for the quote:

$$
\boxed{Q_0=\frac{FV(B_0+AI_0)-FVCI-AI_T}{CF}}
$$

> [!NOTE]
> This derivation protects the unit invariant: full price is compared with full price.

---

## Variant: Appendix — Derive the Par Swap Rate

**Abstract:** *At inception, discounted fixed coupons plus discounted principal must equal par.*

> Derive the fixed rate on an at-market interest-rate swap with constant accrual period $AP$.

<span class="jargon-unlock">**At-market swap. What is it?** A new swap with zero value. **Par replication. What is it?** Treat the fixed leg as a bond priced at 1 and the floating leg as a par bond worth 1 on a reset date.</span>

**1. Set the fixed bond equal to one**

$$
1=r_{FIX}AP\sum_{i=1}^{n}PV_i(1)+PV_n(1)
$$

Move the final principal's present value and divide:

$$
\boxed{r_{FIX}=\frac{1-PV_n(1)}{AP\sum_{i=1}^{n}PV_i(1)}}
$$

> [!NOTE]
> The same par-bond invariant prices fixed legs in interest-rate, currency, and equity swaps.

---

## Variant: Appendix — Derive Interest-Rate Swap Value

**Abstract:** *Offset the old fixed coupons with today's fair fixed coupons; the floating pieces cancel on a reset date.*

> Derive the reset-date value of a receive-fixed swap.

<span class="jargon-unlock">**Offsetting swap. What is it?** A new opposite swap using today's fair fixed rate. **Coupon-difference invariant. What is it?** After floating legs cancel, only old fixed minus new fixed remains on every payment date.</span>

**1. Present-value every remaining fixed-rate difference**

Each per-unit difference is $FS_0-FS_t$, so:

$$
\boxed{V_{receive-fixed}=NA(FS_0-FS_t)\sum_{i=1}^{n}PV_i}
$$

The opposite position is:

$$
\boxed{V_{pay-fixed}=-V_{receive-fixed}}
$$

> [!NOTE]
> This simple rate-difference form is a payment-date result; between-payment valuation needs the module's extra timing adjustments.

---

## Variant: Appendix — Derive Currency-Swap Value

**Abstract:** *Every received currency stream is a long bond; every paid stream is a short bond; convert them to one unit before subtracting.*

> Derive the value in currency $a$ of receiving fixed currency $a$ and paying fixed currency $b$.

<span class="jargon-unlock">**Currency-unit invariant. What is it?** Quantities may be added or subtracted only after they are expressed in the same currency. **Currency-$a$ bond value. What is it?** Fixed coupons plus principal discounted on the currency-$a$ curve.</span>

**1. Price and translate the two bonds**

$$
V_a=NA_a\left[APr_a\sum PV_{i,a}+PV_{n,a}\right]
$$

Price the paid bond on currency $b$'s curve.

$$
V_b=NA_b\left[APr_b\sum PV_{i,b}+PV_{n,b}\right]
$$

Therefore:

$$
\boxed{V_{CS}=V_a-S_tV_b}
$$

> [!NOTE]
> The party receiving currency $b$ has the negative value after consistent conversion.

---

## Variant: Appendix — Derive Equity-Swap Value

**Abstract:** *Replicate receive-fixed/pay-equity with a long fixed bond and a short reset equity position, then correct any terminal principal mismatch.*

> Derive the value of a receive-fixed/pay-equity swap between reset dates.

<span class="jargon-unlock">**Reset equity position. What is it?** The notional grown by the equity price ratio since the last reset, $(S_t/S_{t-1})NA_E$. **Terminal mismatch. What is it?** Bond par minus equity notional, discounted from maturity.</span>

**1. Add the replicated pieces**

Long fixed bond contributes $V_{FIX}(C_0)$. The equity obligation subtracts $(S_t/S_{t-1})NA_E$. Financing the terminal mismatch subtracts $PV(Par-NA_E)$.

$$
\boxed{V_{EQ,t}=V_{FIX}(C_0)-\frac{S_t}{S_{t-1}}NA_E-PV(Par-NA_E)}
$$

> [!NOTE]
> When $Par=NA_E$, the last term disappears, but the equity price ratio does not.

---

## Variant: Appendix — Use the Seven Invariants as an Error Check

**Abstract:** *When a long formula sheet feels slippery, test the answer against rules that cannot change.*

> List the core invariants that should survive every pricing or valuation problem in this module.

<span class="jargon-unlock">**Invariant. What is it?** A relationship that must remain true even when the numbers or contract type change. **Error check. What is it?** A fast test that catches a wrong sign, unit, timing, or price basis.</span>

**1. Keep these seven locks on the answer**

$$
\boxed{\begin{aligned}
&1.\ \text{Same future cash flows}\Rightarrow\text{same price}\\
&2.\ \text{New fair forward or swap value}=0\\
&3.\ V_{long}=-V_{short}\\
&4.\ \text{Carry cost raises }F;\ \text{carry benefit lowers }F\\
&5.\ \text{Discount only future cash}\\
&6.\ \text{Compare clean with clean or full with full}\\
&7.\ \text{Add values only in the same currency}
\end{aligned}}
$$

> [!NOTE]
> Predict direction, sign, time, price basis, and unit before trusting the calculator.

<!--
Source coverage audit
Primary: CFA Program Level II, Derivatives, Learning Module 1, Pricing and Valuation of Forward Commitments.
LOS: a equity forwards/futures; b carry arbitrage; c interest-rate forwards/futures; d fixed-income forwards/futures; e interest-rate swaps; f currency swaps; g equity swaps.
Official equations covered: 1-18.
Official worked examples mapped: 1-7 forward/carry/equity; 8-10 MRR/FRA; 11-12 fixed income; 13-14 interest-rate swaps; 15-16 currency swaps; 17-19 equity swaps.
Official practice families mapped: 1-11 carry, fixed income, equity forwards/futures, swaps; 12-20 swaps, FRA pricing/value/settlement.
Secondary cross-check: Schweser Reading 28, Pricing and Valuation of Forward Commitments, used only to confirm terminology and edge-question families.
-->
