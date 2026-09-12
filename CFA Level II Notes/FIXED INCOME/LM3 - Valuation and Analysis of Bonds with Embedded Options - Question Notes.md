## Variant: Identify the Embedded Option and Exercise Style

**Abstract:** *First ask who owns the choice and when they may use it. The issuer owns a call; the investor owns a put or conversion option.*

> A bond may be called on two specified annual dates before maturity. Name the option owner and exercise style.

<span class="jargon-unlock">**Embedded option. What is it?** A right built inside a bond. **Callable bond. What is it?** A bond the issuer may repay early. **Bermudan style. What does that mean?** Exercise is allowed on several specified dates; European means one date, while American means any time during a stated window.</span>

**1. Match the right to its owner and calendar**

The issuer chooses whether to call, and two discrete dates make the option Bermudan.

$$
\boxed{\text{Issuer-owned Bermudan call option}}
$$

> [!NOTE]
> Call = issuer’s right. Put and conversion = investor’s rights. The dates determine the exercise style.

---

## Variant: Decompose Callable and Putable Bond Values

**Abstract:** *Start with the straight bond. An issuer call takes value away from the investor; an investor put adds value.*

> A straight bond is worth 104. Its embedded issuer call is worth 3, and its embedded investor put is worth 4. Find the otherwise identical callable and putable bond values.

<span class="jargon-unlock">**Straight bond. What is it?** An otherwise identical bond with no embedded option. **Callable value. What is the formula?** $V_{callable}=V_{straight}-V_{call}$. **Putable value. What is the formula?** $V_{putable}=V_{straight}+V_{put}$.</span>

**1. Give or take the option value**

$$
V_{callable}=104-3=\boxed{101}
$$

The put belongs to the investor, so it goes the other way.

$$
V_{putable}=104+4=\boxed{108}
$$

> [!NOTE]
> From the investor’s seat: short the issuer call, long the investor put.

---

## Variant: Infer the Issuer Call Value

**Abstract:** *The straight-minus-callable price gap is the value surrendered to the issuer.*

> An option-free bond is worth 102.80 and an otherwise identical callable bond is worth 100.25. Find the embedded call value.

<span class="jargon-unlock">**Issuer call value. What is it?** The price of the issuer’s right to retire the debt early. From $V_{callable}=V_{straight}-V_{call}$, rearrange to $V_{call}=V_{straight}-V_{callable}$.</span>

**1. Measure the missing investor value**

$$
V_{call}=102.80-100.25=\boxed{2.55}
$$

The investor accepts 2.55 less bond value because the issuer owns the refinancing right.

> [!NOTE]
> Callable must not exceed straight value when every other feature is identical.

---

## Variant: Infer the Investor Put Value

**Abstract:** *The putable-minus-straight price gap is what investors pay for their downside floor.*

> A putable bond is worth 103.40 and its otherwise identical straight bond is worth 99.10. Find the embedded put value.

<span class="jargon-unlock">**Investor put value. What is it?** The value of the holder’s right to sell the bond back at the put price. Rearranging $V_{putable}=V_{straight}+V_{put}$ gives $V_{put}=V_{putable}-V_{straight}$.</span>

**1. Strip out the straight bond**

$$
V_{put}=103.40-99.10=\boxed{4.30}
$$

> [!NOTE]
> Putable must be worth at least as much as straight because the investor may ignore an unattractive put.

---

## Variant: Apply Call Caps and Put Floors

**Abstract:** *At an exercise node, continuation fights the exercise price. The issuer chooses the cheaper call outcome; the investor chooses the richer put outcome.*

> At a node, a bond’s continuation value is 103. The call and put exercise prices are both 100. Find the node value if the bond is callable and if it is putable, before adding any coupon due now.

<span class="jargon-unlock">**Continuation value. What is it?** The discounted expected value of keeping the bond alive. **Call rule. What is it?** $V_{callable}=\min(Continuation,Call\ price)$. **Put rule. What is it?** $V_{putable}=\max(Continuation,Put\ price)$.</span>

**1. Let the option owner choose**

$$
V_{callable}=\min(103,100)=\boxed{100}
$$

The investor owns the put and rejects a worse 100 exit.

$$
V_{putable}=\max(103,100)=\boxed{103}
$$

> [!NOTE]
> Call uses **min** because the issuer chooses; put uses **max** because the investor chooses.

---

## Variant: Roll Back a Callable Bond without Volatility

**Abstract:** *Discount the final payment to the call date, cap it at the call price, add the current coupon, then roll back again.*

> A two-year 5% annual-pay bond has par 100. The one-year rate today is 4%, and the one-year rate one year from now is 2%. The issuer may call at 100 after the Year-1 coupon. Find the callable value today.

<span class="jargon-unlock">**Rollback. What is it?** Moving backward through a rate tree by discounting later cash. **Ex-coupon node value. What is it?** The bond value immediately after the current coupon is separated from the bond.</span>

**1. Test the Year-1 call**

$$
Continuation_1=\frac{105}{1.02}=102.941
$$

The issuer pays the cheaper 100 call price.

$$
V_0=\frac{5+\min(102.941,100)}{1.04}=\boxed{100.962}
$$

> [!NOTE]
> Compare continuation with the exercise price **before** adding the coupon paid at that node.

---

## Variant: Roll Back a Putable Bond without Volatility

**Abstract:** *At the put date, the investor takes the better of continuation and the put price, then the node coupon is added.*

> A two-year 5% annual-pay bond has par 100. The one-year rate today is 4%, and the one-year rate one year from now is 10%. The investor may put at 100 after the Year-1 coupon. Find today’s value.

<span class="jargon-unlock">**Put floor. What is it?** The investor can force the ex-coupon bond value up to at least the put price. The node rule is $\max(Continuation,Put\ price)$.</span>

**1. Test exercise at Year 1**

$$
Continuation_1=\frac{105}{1.10}=95.455
$$

The investor rejects 95.455 and puts at 100.

$$
V_0=\frac{5+100}{1.04}=\boxed{100.962}
$$

> [!NOTE]
> Rising rates make the put valuable because they push continuation below the guaranteed exit price.

---

## Variant: Roll Back a Callable Bond through a Volatile Tree

**Abstract:** *Apply the call separately in every state, average risk-neutrally, add the coupon, and discount one step.*

> A two-year 5% bond is callable at 100 in Year 1. The Year-1 one-year rate will be 2% or 10% with equal risk-neutral probabilities. Today’s one-year rate is 4%. Find the bond value.

<span class="jargon-unlock">**Risk-neutral probability. What is it?** A pricing weight used with risk-free discounting, not a real-world forecast. **Node call test. What is it?** Apply $\min(105/(1+r_1),100)$ in each Year-1 state.</span>

**1. Value both states**

$$
V_{1,low}=\min(105/1.02,100)=100
$$

The high-rate state stays alive because calling would cost more.

$$
V_{1,high}=\min(105/1.10,100)=95.455
$$

Now average, add the Year-1 coupon, and discount.

$$
V_0=\frac{5+0.5(100)+0.5(95.455)}{1.04}=\boxed{98.776}
$$

> [!NOTE]
> Never average continuation values first and apply the call once; exercise is decided node by node.

---

## Variant: Roll Back a Putable Bond through a Volatile Tree

**Abstract:** *The investor exercises only in the bad state. The put trims downside while leaving the good state alive.*

> Use the same two-year 5% bond and 2%/10% Year-1 rates, but give the investor a put at 100. Today’s one-year rate is 4%. Find value.

<span class="jargon-unlock">**Node put test. What is it?** Apply $\max(105/(1+r_1),100)$ in each state. **Downside floor. What does it mean?** The investor can refuse an ex-coupon value below 100.</span>

**1. Keep the upside and floor the downside**

$$
V_{1,low}=\max(105/1.02,100)=102.941
$$

The 10% state hits the put floor.

$$
V_{1,high}=\max(105/1.10,100)=100
$$

Average those two exercise-adjusted states and bring the result home.

$$
V_0=\frac{5+0.5(102.941)+0.5(100)}{1.04}=\boxed{102.375}
$$

> [!NOTE]
> A putable bond keeps favorable continuation value and replaces only unfavorable nodes with the put price.

---

## Variant: Measure Volatility’s Opposite Effects on Callable and Putable Bonds

**Abstract:** *More volatility makes either option richer. That hurts a callable investor but helps a putable investor.*

> At zero volatility, a callable bond is worth 100.962 and a putable bond 101.886. With a 2%/10% rate tree, they are worth 98.776 and 102.375. Calculate each price change.

<span class="jargon-unlock">**Interest-rate volatility. What is it?** Dispersion in possible future rates. **Option value effect. What is it?** More dispersion creates more states where an option pays off, so both call and put values rise.</span>

**1. Compare each bond before and after volatility**

$$
\Delta V_{callable}=98.776-100.962=\boxed{-2.186}
$$

The putable investor owns the option, so the sign flips.

$$
\Delta V_{putable}=102.375-101.886=\boxed{+0.489}
$$

> [!NOTE]
> Higher volatility: callable bond down, putable bond up, straight bond unchanged if the benchmark curve itself is unchanged.

---

## Variant: Apply a Yield-Curve Shape View to Embedded Options

**Abstract:** *A flatter or inverted curve lowers many forward rates, creating more call states and fewer put states.*

> Holding the current short rate and volatility fixed, a curve changes from upward sloping to inverted. Which embedded option gains value: an issuer call or an investor put?

<span class="jargon-unlock">**Yield-curve shape. What is it?** The pattern of rates across maturities. **Forward rates. What are they?** Future-period rates implied by today’s curve. **Inverted curve. What is it?** Longer rates lie below shorter rates.</span>

**1. Follow the forward-rate nodes**

Lower future rates raise continuation values and create more profitable refinancing opportunities for the issuer.

$$
\boxed{V_{issuer\ call}\uparrow,\qquad V_{investor\ put}\downarrow}
$$

> [!NOTE]
> Flatter or inverted curve generally helps the issuer call and hurts the investor put, all else equal.

---

## Variant: Price a Risky Callable Bond with an OAS

**Abstract:** *Add the same OAS to every benchmark node, then run the usual call-tree rollback with those higher discount rates.*

> A two-year 5% callable bond uses Year-1 benchmark rates of 2% and 10%, equal pricing weights, and a 2% OAS. The current benchmark rate is 4%, and the Year-1 call price is 100. Find value.

<span class="jargon-unlock">**OAS. What is OAS?** Option-adjusted spread is the constant spread added to every benchmark one-period rate that makes model value match market price. **Risky rollback. What is it?** Discount at $Benchmark\ rate+OAS$ before applying the option.</span>

**1. Revalue both Year-1 states**

$$
V_{1,low}=\min(105/1.04,100)=100,\quad V_{1,high}=\min(105/1.12,100)=93.75
$$

**2. Roll back at today’s 6% risky rate**

$$
V_0=\frac{5+0.5(100)+0.5(93.75)}{1.06}=\boxed{96.108}
$$

> [!NOTE]
> OAS changes discount rates, not call or put prices. Apply the option after calculating each spread-adjusted continuation value.

---

## Variant: Solve a One-Period OAS from Market Price

**Abstract:** *For one cash flow, the OAS is simply the bond’s required yield minus the benchmark rate.*

> A one-year risky bond pays 105 and trades at 100. The one-year benchmark rate is 3%. Find the constant OAS.

<span class="jargon-unlock">**Constant spread. What is it?** The same added yield at every node. For one period, $Price=Cash\ flow/(1+Benchmark+OAS)$.</span>

**1. Rearrange the pricing equation**

$$
100=\frac{105}{1+0.03+OAS}
$$

Now isolate the spread.

$$
OAS=\frac{105}{100}-1-0.03=\boxed{2.00\%=200\text{ bps}}
$$

> [!NOTE]
> One percentage point equals 100 basis points. Enter 200 bps as 0.02 in the pricing formula.

---

## Variant: Use OAS for Relative Value

**Abstract:** *Compare OAS only among genuinely similar bonds. The larger spread then signals the cheaper price.*

> Two callable bonds have the same maturity, coupon, credit quality, option terms, and model assumptions. Bond A has OAS 65 bps and Bond B has OAS 85 bps. Which is relatively cheaper?

<span class="jargon-unlock">**Relative value. What is it?** Comparing prices rather than declaring an absolute fair value. **Larger OAS. What does it mean?** The market price is lower relative to the same modeled cash-flow risk.</span>

**1. Compare like with like**

$$
85\text{ bps}>65\text{ bps}\quad\Rightarrow\quad\boxed{\text{Bond B is relatively cheaper}}
$$

> [!NOTE]
> Do not compare OAS across materially different credit quality or option features and call the larger number a bargain.

---

## Variant: Recalibrate OAS after Volatility Rises

**Abstract:** *First see what volatility does to model value at fixed OAS; then move OAS in the opposite direction to restore the unchanged market price.*

> Market prices do not change, but assumed interest-rate volatility rises. State the required OAS direction for an otherwise identical callable bond and putable bond.

<span class="jargon-unlock">**Recalibration. What is it?** Changing OAS until model value again equals the observed price. **Price–spread relation. What is it?** Higher OAS lowers model value; lower OAS raises it.</span>

**1. Offset the option-value effect**

At fixed OAS, higher volatility lowers callable value and raises putable value. Therefore:

$$
\boxed{OAS_{callable}\downarrow,\qquad OAS_{putable}\uparrow}
$$

> [!NOTE]
> Keep market price fixed in an OAS question. The spread moves to undo the model-price change caused by volatility.

---

## Variant: Calculate Effective Duration

**Abstract:** *Subtract the up-shift price from the down-shift price, then scale by twice the curve move and today’s full price.*

> A bond’s current full price is 101.000. Its values after a 30 bp parallel curve shift down and up are 101.599 and 100.407. Calculate effective duration.

<span class="jargon-unlock">**Effective duration. What is it?** Curve sensitivity that allows cash flows to change with embedded-option exercise: $EffDur=(PV_- -PV_+)/(2\Delta Curve\times PV_0)$. $PV_-$ uses lower rates, $PV_+$ higher rates, and $\Delta Curve$ is the decimal shift.</span>

**1. Convert 30 bps to 0.003 and substitute**

$$
EffDur=\frac{101.599-100.407}{2(0.003)(101.000)}=\boxed{1.97}
$$

This means a small 100 bp rise is estimated to reduce price by about 1.97%.

> [!NOTE]
> The minus subscript means rates moved down, so $PV_-$ is normally the higher price.

---

## Variant: Estimate a Price Change with Effective Duration

**Abstract:** *Duration turns a small curve move into an opposite-signed percentage price move.*

> A bond has full price 101 and effective duration 1.97. Estimate its price after a 50 bp parallel increase, ignoring convexity.

<span class="jargon-unlock">**Duration approximation. What is it?** $\Delta P/P\approx-EffDur\times\Delta Curve$. The negative sign captures the usual rates-up, prices-down relationship.</span>

**1. Estimate the percentage and money change**

$$
\frac{\Delta P}{P}\approx-1.97(0.005)=-0.00985=-0.985\%
$$

Apply that percentage loss to today’s price.

$$
P_{new}\approx101(1-0.00985)=\boxed{100.005}
$$

> [!NOTE]
> Convert 50 bps to 0.005. Using 50 in the formula would blow the answer up by 10,000 times.

---

## Variant: Recover a Missing Shifted Price from Effective Duration

**Abstract:** *Treat the duration formula as an equation and solve for the missing scenario price.*

> Effective duration is 2.00, current full price is 100, the curve shift is 20 bps, and the down-shift value is 100.60. Find the up-shift value.

<span class="jargon-unlock">**Up-shift value. What is it?** $PV_+$, the price after benchmark rates rise. Start from $EffDur=(PV_- -PV_+)/(2\Delta Curve\,PV_0)$.</span>

**1. Rebuild the required price gap**

$$
PV_- -PV_+=2.00(2)(0.002)(100)=0.80
$$

Subtract that required gap from the down-shift price.

$$
PV_+=100.60-0.80=\boxed{99.80}
$$

> [!NOTE]
> Sanity check: the up-shift price should normally sit below today’s price.

---

## Variant: Calculate Effective Duration When Current Price Must Be Found First

**Abstract:** *If $PV_0$ is missing, price the unshifted tree first; duration cannot be computed from only the two shocked prices.*

> A callable bond’s unshifted tree gives current full price 100.873. Its 20 bp down- and up-shift values are 101.238 and 100.478. Calculate effective duration.

<span class="jargon-unlock">**Full price. What is it?** The bond price including accrued interest. **Unshifted value. What is it?** $PV_0$, computed with the original benchmark curve and the same OAS used in both shocked trees.</span>

**1. Use all three prices**

$$
EffDur=\frac{101.238-100.478}{2(0.002)(100.873)}=\boxed{1.88}
$$

> [!NOTE]
> Never replace $PV_0$ with par just because the bond is quoted near 100.

---

## Variant: Rank Effective Duration across Common Bond Types

**Abstract:** *Options shorten the bond when exercise becomes likely; a floater keeps resetting toward market rates.*

> Rank the approximate duration behavior of cash, a five-year zero, a five-year fixed-rate coupon bond, a callable bond, a putable bond, and a floater resetting in three months.

<span class="jargon-unlock">**Effective-duration benchmark. What is it?** Cash has 0; a zero’s duration is about maturity; a coupon bond is below maturity; callable and putable durations do not exceed the matching straight bond; a floater is about time to next reset.</span>

**1. Write the anchor values and inequalities**

$$
\boxed{D_{cash}=0,\quad D_{zero}\approx5,\quad D_{coupon}<5,\quad D_{call},D_{put}\le D_{straight},\quad D_{floater}\approx0.25}
$$

> [!NOTE]
> Duration is an interest-rate sensitivity measure, not simply the contractual maturity printed on the bond.

---

## Variant: Explain Why Callable Duration Changes with Rates

**Abstract:** *Low rates wake up the call and pull expected life toward the first call date; high rates put the call to sleep.*

> A 10-year bond is callable in two years. What happens to its effective duration when benchmark rates fall far below its coupon, and when rates rise far above it?

<span class="jargon-unlock">**In the money. What does it mean for an issuer call?** Refinancing at the call price is attractive. **Expected life. What is it?** The economically likely time until repayment, which may be much shorter than legal maturity.</span>

**1. Follow exercise probability**

$$
\boxed{Rates\downarrow\Rightarrow D_{callable}\downarrow\text{ toward the call date}}
$$

When rates rise, exercise becomes unlikely and duration lengthens toward the straight bond’s duration.

> [!NOTE]
> A callable bond can **lose duration when yields fall**, exactly when an option-free bond owner hoped for more upside.

---

## Variant: Explain Why Putable Duration Changes with Rates

**Abstract:** *High rates wake up the investor put and shorten expected life; low rates leave the bond behaving more like straight debt.*

> A 10-year bond is putable in two years. What happens to effective duration when benchmark rates rise far above its coupon?

<span class="jargon-unlock">**In the money. What does it mean for an investor put?** Selling the bond back at the put price beats keeping its lower continuation value. **Put date. What is it?** The date on which the investor may force repayment.</span>

**1. Follow the downside floor**

$$
\boxed{Rates\uparrow\Rightarrow D_{putable}\downarrow\text{ toward the put date}}
$$

The put blocks much of the price decline, so the bond becomes less rate-sensitive.

> [!NOTE]
> Callable duration shortens in falling-rate states; putable duration shortens in rising-rate states.

---

## Variant: Calculate One-Sided Durations for a Callable Bond

**Abstract:** *Split the two-sided average into its rates-up and rates-down halves to expose the call cap.*

> A callable bond has $PV_0=99.75$, $PV_+=99.17$, and $PV_-=100.00$ for 30 bp shifts. Calculate one-sided up- and down-duration.

<span class="jargon-unlock">**Up-duration. What is it?** $D_{up}=(PV_0-PV_+)/(\Delta Curve\,PV_0)$. **Down-duration. What is it?** $D_{down}=(PV_- -PV_0)/(\Delta Curve\,PV_0)$.</span>

**1. Measure each side separately**

$$
D_{up}=\frac{99.75-99.17}{0.003(99.75)}=\boxed{1.94}
$$

The call caps the rates-down price gain.

$$
D_{down}=\frac{100.00-99.75}{0.003(99.75)}=\boxed{0.84}
$$

> [!NOTE]
> For a near-the-money callable bond, up-duration usually exceeds down-duration.

---

## Variant: Calculate One-Sided Durations for a Putable Bond

**Abstract:** *The investor put floors the rates-up loss, so the rates-down side carries more sensitivity.*

> A putable bond has $PV_0=100.45$, $PV_+=100.00$, and $PV_-=101.81$ for 30 bp shifts. Calculate both one-sided durations.

<span class="jargon-unlock">**Put asymmetry. What is it?** The put limits depreciation when rates rise but does not cap appreciation when rates fall.</span>

**1. Calculate the floored and unfloored sides**

$$
D_{up}=\frac{100.45-100.00}{0.003(100.45)}=\boxed{1.49}
$$

Now measure the much larger response when rates fall.

$$
D_{down}=\frac{101.81-100.45}{0.003(100.45)}=\boxed{4.51}
$$

> [!NOTE]
> For a near-the-money putable bond, down-duration usually exceeds up-duration.

---

## Variant: Recover Two-Sided Duration from One-Sided Durations

**Abstract:** *With equal up and down shifts, effective duration is the simple average of the two one-sided measures.*

> A callable bond has up-duration 1.94 and down-duration 0.84. Find its ordinary effective duration.

<span class="jargon-unlock">**Two-sided effective duration. What is it?** The centered sensitivity using equal curve shifts in both directions: $EffDur=(D_{up}+D_{down})/2$.</span>

**1. Average the two slopes**

$$
EffDur=\frac{1.94+0.84}{2}=\boxed{1.39}
$$

The average is convenient, but the two components retain the asymmetry information.

> [!NOTE]
> Two bonds can share the same effective duration while having very different one-sided risks.

---

## Variant: Calculate a Key-Rate Duration from Shocked Prices

**Abstract:** *Use the effective-duration formula, but move only one maturity point while holding every other key rate fixed.*

> A bond is worth 100. When only the five-year par rate falls or rises by 10 bps, value becomes 100.20 or 99.80. Find five-year key-rate duration.

<span class="jargon-unlock">**Key-rate duration, or KRD. What is it?** Price sensitivity to one selected maturity on the benchmark curve: $KRD_k=(PV_{k,-}-PV_{k,+})/(2\Delta z_kPV_0)$.</span>

**1. Isolate the five-year point**

$$
KRD_5=\frac{100.20-99.80}{2(0.001)(100)}=\boxed{2.00}
$$

> [!NOTE]
> Effective duration shifts the whole curve; key-rate duration shifts one key point at a time.

---

## Variant: Estimate Price Change from Several Key-Rate Moves

**Abstract:** *Multiply each key-rate duration by its own rate move, add the effects, and reverse the sign.*

> A bond has $KRD_2=0.5$, $KRD_5=2.0$, and $KRD_{10}=4.0$. The respective rates move +10, −5, and +20 bps. Estimate the percentage price change.

<span class="jargon-unlock">**Shaping-risk approximation. What is it?** $\Delta P/P\approx-\sum KRD_k\Delta z_k$, where each $\Delta z_k$ is that key rate’s decimal change.</span>

**1. Keep each maturity in its own lane**

$$
\frac{\Delta P}{P}\approx-[0.5(0.001)+2(-0.0005)+4(0.002)]=\boxed{-0.75\%}
$$

> [!NOTE]
> Do not add the rate changes first. Each curve point has a different sensitivity weight.

---

## Variant: Reconcile Key-Rate and Effective Duration

**Abstract:** *If every key rate moves equally, the key-rate pieces recombine into the parallel-shift duration.*

> A portfolio has key-rate durations of 0.5, 2.0, and 4.0 at 2, 5, and 10 years. Find effective duration for a parallel shift and estimate the effect of a 50 bp parallel decline.

<span class="jargon-unlock">**Parallel shift. What is it?** Every selected curve rate moves by the same amount. **Duration reconciliation. What is it?** $EffDur\approx\sum KRD_k$ when the key rates span the curve exposure.</span>

**1. Add the sensitivity pieces**

$$
EffDur=0.5+2.0+4.0=\boxed{6.5}
$$

Rates decline, so price rises.

$$
\frac{\Delta P}{P}\approx-6.5(-0.005)=\boxed{+3.25\%}
$$

> [!NOTE]
> The KRD sum is an independent checksum for the parallel effective duration.

---

## Variant: Interpret a Negative Key-Rate Duration

**Abstract:** *A negative KRD is not a typo: shifting one par rate can reshape implied spot rates and raise a distant cash flow’s value.*

> A low-coupon 10-year bond has five-year key-rate duration of −0.50. Estimate its price response if only the five-year par rate rises 10 bps.

<span class="jargon-unlock">**Negative KRD. What does it mean?** Price moves in the same direction as that isolated key rate because keeping other par points fixed reshapes the bootstrapped spot curve.</span>

**1. Apply the signed sensitivity**

$$
\frac{\Delta P}{P}\approx-(-0.50)(0.001)=\boxed{+0.05\%}
$$

> [!NOTE]
> Negative KRD can occur at shorter key points for zero- or low-coupon bonds; total duration can still be positive.

---

## Variant: Locate Key-Rate Exposure around an Exercise Date

**Abstract:** *When exercise is nearly certain, contractual maturity stops driving the bond; the first exercise date becomes the economic maturity.*

> A 30-year high-coupon bond is callable in 10 years. Its 10-year KRD is 6.06 and 30-year KRD is 0.19. Which curve point dominates and why?

<span class="jargon-unlock">**Economic maturity. What is it?** The date on which repayment is most likely, even if legal maturity is later. **Exercise-date exposure. What is it?** Sensitivity concentrated near the call or put date.</span>

**1. Compare the two measured exposures**

$$
6.06\gg0.19\quad\Rightarrow\quad\boxed{\text{The 10-year key rate dominates}}
$$

> [!NOTE]
> Out-of-the-money options leave exposure near final maturity; deep-in-the-money options pull exposure toward exercise.

---

## Variant: Identify the Largest KRD for a Par Option-Free Bond

**Abstract:** *A par bond’s maturity-matched par rate is its direct price-setting rate; other par points have zero KRD in the curriculum’s setup.*

> A 10-year 4% option-free bond trades at par on a 4% par curve. Which key-rate duration is largest?

<span class="jargon-unlock">**Maturity-matched par rate. What is it?** The par-curve point with the same maturity as the bond. **Par bond. What is it?** Coupon rate equals the maturity-matched par rate, so price is 100.</span>

**1. Use the defining par relationship**

$$
\boxed{KRD_{10}=EffDur\text{ and the shorter-point KRDs are }0}
$$

> [!NOTE]
> This zero-shorter-KRD result is for an option-free bond trading exactly at par on the same par curve.

---

## Variant: Calculate Effective Convexity

**Abstract:** *Add the two shocked prices, subtract twice today’s price, then divide by the squared curve move and today’s price.*

> A callable bond has $PV_0=100.785$, $PV_-=101.381$, and $PV_+=100.146$ for 30 bp parallel shifts. Calculate effective convexity.

<span class="jargon-unlock">**Effective convexity. What is it?** Curvature in the price–rate relationship when cash flows may change: $EffCon=(PV_-+PV_+-2PV_0)/[(\Delta Curve)^2PV_0]$.</span>

**1. Measure the bend around today’s price**

$$
EffCon=\frac{101.381+100.146-2(100.785)}{(0.003)^2(100.785)}=\boxed{-47.41}
$$

> [!NOTE]
> Duration uses the first price difference; convexity uses the sum of shocked prices around twice the center price.

---

## Variant: Improve a Price Estimate with Duration and Convexity

**Abstract:** *Duration draws the tangent line; convexity adds the bend that the straight-line estimate misses.*

> A bond has effective duration 5 and effective convexity 40. Estimate its percentage price change for a 100 bp rate increase.

<span class="jargon-unlock">**Duration-plus-convexity approximation. What is it?** $\Delta P/P\approx-D\Delta y+\tfrac12 C(\Delta y)^2$, where $D$ is duration, $C$ is raw convexity, and $\Delta y$ is the decimal yield move.</span>

**1. Add the linear and curved pieces**

$$
\frac{\Delta P}{P}\approx-5(0.01)+\frac12(40)(0.01)^2=-5.00\%+0.20\%=\boxed{-4.80\%}
$$

> [!NOTE]
> Positive convexity softens a price loss and boosts a price gain relative to duration alone.

---

## Variant: Interpret Negative Convexity for a Callable Bond

**Abstract:** *A near-the-money call caps the good side more than the bad side, bending the price curve the wrong way for investors.*

> A callable bond’s duration-only estimate for a 50 bp move is ±1.0%, but its actual price rises only 0.7% when rates fall and drops 1.1% when rates rise. What convexity sign does this reveal?

<span class="jargon-unlock">**Negative convexity. What is it?** Downside from rising rates exceeds upside from an equal rate decline. It commonly appears when an issuer call is near the money.</span>

**1. Compare equal-sized moves**

$$
0.7\%\text{ upside}<1.1\%\text{ downside}\quad\Rightarrow\quad\boxed{EffCon<0}
$$

> [!NOTE]
> Callable convexity can turn negative near the call price; putable and straight bonds retain positive convexity in this curriculum treatment.

---

## Variant: Convert between Raw and Scaled Convexity

**Abstract:** *Some systems divide raw convexity by 100. Identify the convention before inserting the number into a price-change formula.*

> A system reports raw effective convexity of 40. Another vendor scales convexity by dividing by 100. What will the second vendor display?

<span class="jargon-unlock">**Raw convexity. What is it?** The direct output of the curriculum formula. **Scaled convexity. What is it?** A reporting convention equal to $Raw/100$.</span>

**1. Apply the display convention**

$$
Convexity_{scaled}=\frac{40}{100}=\boxed{0.40}
$$

> [!NOTE]
> Do not mix a scaled convexity quote with a formula expecting raw convexity; confirm the vendor convention first.

---

## Variant: Compare Convexity across Straight, Callable, and Putable Bonds

**Abstract:** *The call clips upside; the put clips downside. That makes callable convexity the weakest and putable convexity the strongest near exercise.*

> Otherwise identical bonds have effective convexities of −35, +18, and +42. Assign them to a near-the-money callable, straight, and near-the-money putable bond.

<span class="jargon-unlock">**Convexity ranking. What is it?** Near the money, the callable can be negative, the straight bond has ordinary positive convexity, and the putable has extra positive curvature from its floor.</span>

**1. Match each shape to its option**

$$
\boxed{Callable=-35,\quad Straight=+18,\quad Putable=+42}
$$

> [!NOTE]
> Option moneyness matters. Far out of the money, callable and putable bonds behave more like the straight bond.

---

## Variant: Determine the Coupon on a Capped Floater

**Abstract:** *A cap is a ceiling: calculate the reference coupon, then take the smaller of that rate and the cap.*

> A floater pays the one-year reference rate and has a 4.50% cap. At the fixing node, the reference rate is 5.53%. What coupon rate and payment per 100 par apply?

<span class="jargon-unlock">**Capped floater. What is it?** A floating-rate bond whose coupon cannot exceed a maximum. Its coupon is $\min(Reference+Quoted\ margin,Cap)$.</span>

**1. Hit the ceiling**

$$
Coupon\ rate=\min(5.53\%,4.50\%)=\boxed{4.50\%}
$$

Turn the capped rate into cash on 100 of par.

$$
Coupon\ cash=100(0.045)=\boxed{4.50}
$$

> [!NOTE]
> The cap protects the issuer from high coupons and therefore reduces the floater’s value to the investor.

---

## Variant: Determine the Coupon on a Floored Floater

**Abstract:** *A floor is a minimum: calculate the reference coupon, then take the larger of that rate and the floor.*

> A floater pays the one-year reference rate and has a 3.50% floor. At the fixing node, the reference rate is 2.50%. What coupon rate and payment per 100 par apply?

<span class="jargon-unlock">**Floored floater. What is it?** A floating-rate bond whose coupon cannot fall below a minimum. Its coupon is $\max(Reference+Quoted\ margin,Floor)$.</span>

**1. Apply the investor’s floor**

$$
Coupon\ rate=\max(2.50\%,3.50\%)=\boxed{3.50\%}
$$

Turn the floored rate into cash on 100 of par.

$$
Coupon\ cash=100(0.035)=\boxed{3.50}
$$

> [!NOTE]
> The floor protects the investor from low coupons and therefore adds value to the floater.

---

## Variant: Value the Embedded Cap from Bond Prices

**Abstract:** *The capped floater is the straight floater minus the issuer-owned cap; the price gap is the cap value.*

> An uncapped floater is worth 100 and an otherwise identical capped floater is worth 99.761. Find the embedded cap value.

<span class="jargon-unlock">**Embedded cap. What is it?** The issuer’s option to stop the coupon above a ceiling. The identity is $V_{capped}=V_{straight}-V_{cap}$.</span>

**1. Recover the option taken from the investor**

$$
V_{cap}=100-99.761=\boxed{0.239}
$$

> [!NOTE]
> A capped floater cannot exceed its otherwise identical uncapped floater.

---

## Variant: Value the Embedded Floor from Bond Prices

**Abstract:** *The floored floater is the straight floater plus the investor-owned floor; the price gap is the floor value.*

> An unfloored floater is worth 100 and an otherwise identical floored floater is worth 101.133. Find the embedded floor value.

<span class="jargon-unlock">**Embedded floor. What is it?** The investor’s option to receive at least a minimum coupon. The identity is $V_{floored}=V_{straight}+V_{floor}$.</span>

**1. Strip out the straight floater**

$$
V_{floor}=101.133-100=\boxed{1.133}
$$

> [!NOTE]
> A floored floater must be worth at least as much as its otherwise identical straight floater.

---

## Variant: Value a Collared Floater by Components

**Abstract:** *A collar contains both options: subtract the issuer cap and add the investor floor.*

> A straight floater is worth 100. Its embedded cap is worth 0.40 and its embedded floor is worth 0.70. Find the collared floater’s value.

<span class="jargon-unlock">**Collared floater. What is it?** A floater with both a coupon ceiling and floor. Its value is $V_{collared}=V_{straight}-V_{cap}+V_{floor}$.</span>

**1. Combine the investor’s short cap and long floor**

$$
V_{collared}=100-0.40+0.70=\boxed{100.30}
$$

> [!NOTE]
> Cap subtracts; floor adds. Keep the signs tied to who owns each option.

---

## Variant: Handle a Coupon Set in Arrears

**Abstract:** *Set in arrears means the rate is observed at the end of the coupon period and paid immediately, so there is no extra waiting-period discount.*

> A one-year reference-rate floater sets its coupon in arrears. At year-end the observed rate is 4.2% on 100 par. What coupon is fixed and paid that day?

<span class="jargon-unlock">**Set in arrears. What does it mean?** The coupon’s setting date and payment date are the same at period-end. This differs from the usual set-in-advance convention.</span>

**1. Apply the observed rate directly**

$$
Coupon=100(0.042)=\boxed{4.20}
$$

> [!NOTE]
> Do not discount the just-set coupon for another year when setting and payment occur on the same date.

---

## Variant: Estimate a Floater’s Effective Duration

**Abstract:** *A floater resets toward market value, so its rate exposure is roughly the time remaining until the next reset.*

> A floating-rate bond resets quarterly, and the next reset occurs in two months. Estimate effective duration if the reference curve is flat.

<span class="jargon-unlock">**Reset date. What is it?** The date the coupon is updated to the current reference rate. **Floater duration rule. What is it?** $EffDur\approx Time\ to\ next\ reset$ in years.</span>

**1. Convert months to years**

$$
EffDur\approx\frac{2}{12}=\boxed{0.167}
$$

> [!NOTE]
> Use time to the **next reset**, not time to final maturity, for a plain floater on a flat reference curve.

---

## Variant: Calculate a Convertible Bond’s Conversion Price

**Abstract:** *Conversion price tells you the stock price at which par value equals the shares received.*

> A $1,000 par convertible bond can be exchanged for 25 common shares. Calculate its conversion price.

<span class="jargon-unlock">**Conversion ratio. What is it?** Shares received per bond. **Conversion price. What is it?** Par value per share obtained: $Conversion\ price=Par/Conversion\ ratio$.</span>

**1. Spread par across the promised shares**

$$
Conversion\ price=\frac{1{,}000}{25}=\boxed{\$40\text{ per share}}
$$

> [!NOTE]
> Conversion ratio is shares per bond; conversion price is currency per share. The units debug the division.

---

## Variant: Solve for the Conversion Ratio

**Abstract:** *Run the conversion-price formula backward: divide par by the stated conversion price.*

> A $1,000 par convertible has a conversion price of $32. Find the conversion ratio.

<span class="jargon-unlock">**Conversion ratio. What is it?** $CR=Par/Conversion\ price$, the number of shares delivered for one converted bond.</span>

**1. Count how many $32 share claims fit inside par**

$$
CR=\frac{1{,}000}{32}=\boxed{31.25\text{ shares}}
$$

> [!NOTE]
> Do not round the conversion ratio unless the contract requires whole shares; use the stated contractual convention.

---

## Variant: Calculate Conversion Value and the Convertible Floor

**Abstract:** *Conversion value is shares times stock price. The convertible cannot rationally trade below the better of conversion value and straight-bond value.*

> A convertible delivers 25 shares, the stock trades at $42, and the otherwise identical straight bond is worth $980. Find conversion value and minimum convertible value.

<span class="jargon-unlock">**Conversion value. What is it?** $CV=Conversion\ ratio\times Share\ price$. **Minimum value. What is it?** $\max(CV,Straight\ bond\ value)$ before considering extra option time value.</span>

**1. Compare the stock exit with the bond floor**

$$
CV=25(42)=\boxed{\$1{,}050}
$$

Compare that conversion route with staying in the bond.

$$
Minimum\ value=\max(1{,}050,980)=\boxed{\$1{,}050}
$$

> [!NOTE]
> The holder can choose conversion or keep the bond; the weaker route cannot set the minimum.

---

## Variant: Calculate Market Conversion Price and Premium

**Abstract:** *Translate the bond’s market price into cost per conversion share, then compare that cost with buying the stock directly.*

> A convertible trades at $1,120, converts into 25 shares, and the stock trades at $42. Find market conversion price, dollar premium per share, and percentage premium.

<span class="jargon-unlock">**Market conversion price. What is it?** $Bond\ price/Conversion\ ratio$. **Conversion premium. What is it?** The extra cost per share through the bond versus buying stock.</span>

$$
Market\ conversion\ price=\frac{1{,}120}{25}=\boxed{\$44.80}
$$

Subtract the actual share price to get the extra dollars paid per share.

$$
Premium=44.80-42=\boxed{\$2.80}
$$

Scale that extra cost by the actual share price.

$$
Premium\%=\frac{2.80}{42}=\boxed{6.67\%}
$$

> [!NOTE]
> Use the bond’s **market** price for market conversion price, but par for contractual conversion price.

---

## Variant: Adjust Conversion Terms for a Stock Split

**Abstract:** *Anti-dilution keeps the investor’s economic claim unchanged: a two-for-one split doubles shares and halves conversion price.*

> A convertible has a 25-share conversion ratio and $40 conversion price. The issuer completes a two-for-one stock split. Find adjusted terms.

<span class="jargon-unlock">**Anti-dilution adjustment. What is it?** A contractual reset preventing stock splits or specified distributions from watering down the conversion right.</span>

**1. Preserve the same total stock claim**

$$
CR_{new}=25(2)=\boxed{50\text{ shares}}
$$

Halve the price at which each of those now-more-numerous shares is received.

$$
Conversion\ price_{new}=40/2=\boxed{\$20}
$$

The claim remains $50\times20=\$1{,}000$.

> [!NOTE]
> Ratio and conversion price move inversely under a stock split.

---

## Variant: Interpret a Dividend Anti-Dilution Trigger

**Abstract:** *A dividend above the contract’s threshold can trigger a downward conversion-price adjustment, protecting convertible holders.*

> A convertible’s threshold dividend is €0.50 per share, but the issuer declares €0.70. State the conversion-price direction.

<span class="jargon-unlock">**Threshold dividend. What is it?** The dividend level above which the indenture adjusts conversion terms. **Downward conversion-price adjustment. What does it do?** It increases the shares obtainable for the same par claim.</span>

**1. Compare declared and threshold dividends**

$$
€0.70>€0.50\quad\Rightarrow\quad\boxed{Conversion\ price\downarrow}
$$

> [!NOTE]
> Use the contract’s adjustment rule; an ordinary dividend below the threshold need not change conversion terms.

---

## Variant: Decompose a Callable Putable Convertible

**Abstract:** *Start with straight debt, add investor-owned options, and subtract the issuer-owned call.*

> Straight-bond value is €978, the stock conversion option is €147, the issuer call is €43, and the investor put is €26. Find the convertible value.

<span class="jargon-unlock">**Convertible decomposition. What is it?** $V=V_{straight}+V_{stock\ call}-V_{issuer\ call}+V_{investor\ put}$.</span>

**1. Keep ownership signs visible**

$$
V=978+147-43+26=\boxed{€1{,}108}
$$

> [!NOTE]
> Investor options add; issuer options subtract. This sign rule works beyond convertibles too.

---

## Variant: Value a One-Period Convertible by State Payoffs

**Abstract:** *At maturity, take the better of bond redemption and conversion in each state, average with pricing probabilities, then discount.*

> In one year, a convertible pays 1,050 if kept as debt. It converts into 25 shares. The stock will be $50 or $30 with equal risk-neutral probabilities. The one-year risk-free rate is 5%. Find value.

<span class="jargon-unlock">**State payoff. What is it?** The cash received in one possible future outcome. **Convertible maturity payoff. What is it?** $\max(Bond\ redemption,Conversion\ ratio\times Stock\ price)$.</span>

$$
Payoff_{up}=\max(1{,}050,25\times50)=1{,}250
$$

Repeat the holder’s better-of-two choice in the down state.

$$
Payoff_{down}=\max(1{,}050,25\times30)=1{,}050
$$

Average the two pricing payoffs and discount once.

$$
V_0=\frac{0.5(1{,}250)+0.5(1{,}050)}{1.05}=\boxed{1{,}095.24}
$$

> [!NOTE]
> Conversion is a choice, not an obligation. Never use the lower conversion payoff when bond redemption is available.

---

## Variant: Classify Convertible Risk–Return Behavior

**Abstract:** *Compare stock price with conversion price: far below is bond-like, far above is stock-like, and nearby is hybrid.*

> A convertible’s conversion price is $40. Classify its behavior when the stock trades at $20, $38, and $60.

<span class="jargon-unlock">**Bond-like. What does it mean?** Straight-bond value dominates. **Stock-like. What does it mean?** Conversion value dominates. **Hybrid. What does it mean?** Both components materially influence price.</span>

$$
\boxed{\$20:\ Bond\!\!-like;\quad \$38:\ Hybrid;\quad \$60:\ Stock\!\!-like}
$$

> [!NOTE]
> The conversion price is the pivot: distance below or above it tells you which risk engine dominates.

---

## Variant: Compare Price Responses of Straight, Callable, and Putable Bonds

**Abstract:** *The option-free bond sits in the middle: the call removes value and upside; the put adds value and downside protection.*

> Otherwise identical bonds have a straight value of 100, issuer call value 3, and investor put value 4. Rank current prices and describe their rate protection.

<span class="jargon-unlock">**Price ranking. What is it?** $V_{callable}=V_{straight}-V_{call}$ and $V_{putable}=V_{straight}+V_{put}$.</span>

$$
V_{callable}=97<\boxed{V_{straight}=100}<V_{putable}=104
$$

The callable has capped falling-rate upside; the putable has floored rising-rate downside.

> [!NOTE]
> Same issuer, coupon, and maturity: callable ≤ straight ≤ putable.

---

## Variant: Rebuild the Official Callable-Bond Tree Result

**Abstract:** *Work from the last year backward and let the issuer replace any value above the call price with 100.*

> A three-year 4.40% annual-pay bond is callable at par at the end of Years 1 and 2. Its rate tree is 2.2500% now; 3.5930% and 2.9417% in Year 1; and 4.6470%, 3.8046%, and 3.1150% in Year 2. Find its value per 100 of par.

<span class="jargon-unlock">**Backward induction. What is it?** Start at maturity and repeatedly use $PV=(Coupon+Expected\ next\ value)/(1+Node\ rate)$. **Call cap. What is it?** At a call date, use $\min(Continuation\ value,100)$ because the issuer will not hand investors more than the par call price.</span>

At Year 2, the uncapped values are 99.764, 100.574, and 101.246. Apply the par call:

$$
V_2=\min(Uncapped\ value,100)=(99.764,100,100)
$$

Both Year 1 continuation values exceed 100, so both are capped at 100. Roll those values to today:

$$
V_0=\frac{4.40+0.5(100)+0.5(100)}{1.0225}=\boxed{102.103}
$$

> [!NOTE]
> The current value can exceed 100 because the bond cannot be called today. The next coupon is still yours before the first call decision.

---

## Variant: Rebuild the Official Putable-Bond Tree Result

**Abstract:** *Work backward and let the investor replace any exercise-date value below the put price with 100.*

> Use the same three-year 4.40% bond and rate tree as the prior problem, but make the bond putable at par at the end of Years 1 and 2. Find its value per 100 of par.

<span class="jargon-unlock">**Put floor. What is it?** At a put date, use $\max(Continuation\ value,100)$ because the investor can demand the par put price instead of keeping a cheaper bond.</span>

At Year 2, the put changes only the 99.764 state:

$$
V_2=\max(Uncapped\ value,100)=(100,100.574,101.246)
$$

Now roll back one step at each Year 1 node:

$$
V_{1,u}=\frac{4.40+0.5(100)+0.5(100.574)}{1.035930}=101.056
$$

Do the same at the lower Year 1 node.

$$
V_{1,d}=\frac{4.40+0.5(100.574)+0.5(101.246)}{1.029417}=102.301
$$

Both already beat the 100 put price, so the investor keeps them. Finally:

$$
V_0=\frac{4.40+0.5(101.056)+0.5(102.301)}{1.0225}=\boxed{103.744}
$$

> [!NOTE]
> Call means issuer chooses the lower value. Put means investor chooses the higher value.

---

## Variant: Roll Back the Official Capped Floater

**Abstract:** *Cap every coupon first, then discount the resulting cash flows through the tree.*

> A three-year floater pays the one-year reference rate annually, set in arrears, capped at 5.00%. Rates are 3.0000% now; 4.5027% and 3.5419% in Year 1; and 6.3679%, 5.0092%, and 3.9404% in Year 2. Find value per 100 of par.

<span class="jargon-unlock">**Capped floater. What is it?** A floating-rate bond whose coupon is $Coupon=\min(Reference\ rate,Cap)$. **Set in arrears. What does it mean?** The rate observed at the end of a coupon period sets the coupon paid on that same date.</span>

At Year 2, the top two rates hit the 5% cap. The three node values are 98.714, 99.991, and 100.000. Roll back:

$$
V_{1,u}=\frac{4.5027+0.5(98.714)+0.5(99.991)}{1.045027}=99.381
$$

Now roll back from the middle and bottom Year 2 nodes.

$$
V_{1,d}=\frac{3.5419+0.5(99.991)+0.5(100)}{1.035419}=99.996
$$

Average the Year 1 values, add the current coupon, and discount to today.

$$
V_0=\frac{3.0000+0.5(99.381)+0.5(99.996)}{1.03}=\boxed{99.697}
$$

> [!NOTE]
> An uncapped matching-index floater is worth about 100. The issuer-owned cap removes upside, so 99.697 passes the smell test.

---

## Variant: Roll Back the Official Floored Floater

**Abstract:** *Raise any coupon below the floor, then work backward exactly as for an ordinary floater.*

> Using the same three-year tree, a floater pays the one-year reference rate annually, set in arrears, but has a 3.50% floor. Find value per 100 of par.

<span class="jargon-unlock">**Floored floater. What is it?** A floating-rate bond whose coupon is $Coupon=\max(Reference\ rate,Floor)$, so the investor never receives less than the stated floor.</span>

Every Year 2 rate exceeds 3.50%, so all three Year 2 bond values are 100. Both Year 1 rates also exceed the floor, so both Year 1 values remain 100. The current 3.00% rate is below the floor, so today’s next coupon is raised to 3.50:

$$
V_0=\frac{3.50+0.5(100)+0.5(100)}{1.03}=\boxed{100.485}
$$

> [!NOTE]
> The investor-owned floor adds value. A result below 100 would tell you the sign or the max rule was flipped.

---

## Variant: Reproduce Effective Duration from Shifted Callable-Bond Trees

**Abstract:** *Use the recalculated prices from the down-shifted and up-shifted trees, not a yield-to-maturity shortcut.*

> A callable bond is worth 100.200 today. Rebuilding its tree after a 30 bp curve decrease gives 100.780; rebuilding after a 30 bp increase gives 99.487. Find effective duration.

<span class="jargon-unlock">**Effective duration. What is it?** Price sensitivity after the option is allowed to change behavior: $EffDur=(PV_{-}-PV_{+})/(2\times\Delta Curve\times PV_0)$.</span>

Thirty basis points is 0.0030. Put the down-rate price first because lower rates normally mean a higher price:

$$
EffDur=\frac{100.780-99.487}{2(0.0030)(100.200)}=\boxed{2.15}
$$

> [!NOTE]
> The 2.15 means roughly a 2.15% opposite-direction price move for a small 1 percentage-point parallel curve move, with the option revalued.

---

## Variant: Calculate the Official Market Conversion Premium

**Abstract:** *Turn the bond price into an effective share price, then compare that price with the actual stock.*

> A €1,000 convertible initially converts at €10 per share. It now trades at €1,123 while the stock trades at €9.10. Find the market conversion premium per share.

<span class="jargon-unlock">**Market conversion price. What is it?** The effective price per share paid through the bond: $Market\ conversion\ price=Convertible\ bond\ price/Conversion\ ratio$. **Market conversion premium per share. What is it?** $Market\ conversion\ price-Current\ share\ price$.</span>

First find how many shares one bond can become:

$$
Conversion\ ratio=\frac{1{,}000}{10}=100\ shares
$$

Then find the effective share price and the extra amount paid:

$$
Market\ conversion\ price=\frac{1{,}123}{100}=€11.23
$$

Now compare that effective price with buying the stock directly.

$$
Premium=11.23-9.10=\boxed{€2.13\ per\ share}
$$

> [!NOTE]
> Do not subtract the stock price from the whole bond price. Get both numbers onto a per-share basis first.

---

## Variant: Spot a Worthless Cap or Floor before Rolling the Tree

**Abstract:** *If no possible reset rate crosses the trigger, the option never changes a coupon and is worth zero.*

> A floater’s possible reset rates are 2.50%, 3.17%, 3.70%, 3.87%, 4.52%, and 5.53%. Find the values of a 5.60% cap and a 2.50% floor if the otherwise identical uncapped and unfloored floater is worth 100.

<span class="jargon-unlock">**Worthless embedded option. What is it?** A cap or floor that changes no possible cash flow. Its value is zero. A cap binds only when $Reference\ rate>Cap$; a floor binds only when $Reference\ rate<Floor$.</span>

The highest possible rate, 5.53%, never reaches the 5.60% cap. The lowest possible rate equals, but never falls below, the 2.50% floor. Neither option changes cash:

$$
V_{cap}=0,\qquad V_{floor}=0
$$

Therefore both bonds keep the straight floater’s value:

$$
V_{capped}=V_{floored}=\boxed{100}
$$

> [!NOTE]
> Equality does not create extra cash. At the trigger, the contractual coupon and the unmodified coupon are the same.

---

## Variant: Arbitrage a Convertible Trading below Its Conversion Value

**Abstract:** *If the bond costs less than the shares it can instantly become, buy the bond, convert, and sell the shares.*

> A convertible trades for $1,050 and can immediately be converted into 23.26 shares. The stock trades at $52. Ignore transaction costs. Build the arbitrage and find the locked-in profit.

<span class="jargon-unlock">**Arbitrage. What is it?** A set of simultaneous trades with no net market risk and a positive locked-in payoff. **Conversion value. What is it?** $CV=Conversion\ ratio\times Share\ price$; here the ratio is shares received per bond.</span>

Convert the bond and sell the received shares immediately:

$$
CV=23.26(52)=\boxed{\$1{,}209.52}
$$

The curriculum rounds that share package to $1,209. Using the displayed inputs without early rounding gives:

$$
Profit=1{,}209.52-1{,}050=\boxed{\$159.52}
$$

> [!NOTE]
> The official narrative reports about $159 because its displayed conversion ratio is rounded. Direction is the key: buy the underpriced convertible, then convert and sell stock.

---

## Variant: Calculate a Sinking-Fund Triple-Up

**Abstract:** *A triple-up lets the issuer retire three times the mandatory principal amount at par on that sinking-fund date.*

> A sinking-fund bond has original principal of $100 million and requires 5% of original principal to be retired this year. Its acceleration provision is a triple-up. How much may the issuer retire at par, and how much of the original issue remains if it uses the full amount?

<span class="jargon-unlock">**Sinking fund. What is it?** A schedule forcing the issuer to retire pieces of a bond issue over time. **Triple-up. What is it?** Permission to retire $3\times$ the mandatory amount on a scheduled sinking-fund date.</span>

First find the normal required retirement, then triple it:

$$
Mandatory=0.05(100\text{ million})=\$5\text{ million}
$$

Now use the provision’s three-times multiplier.

$$
Triple\!\!-up=3(5)=\boxed{\$15\text{ million at par}}
$$

After using the full provision, the remaining original principal is:

$$
Remaining=100-15=\boxed{\$85\text{ million}}
$$

> [!NOTE]
> The 5% is applied to original principal, not whatever happens to remain outstanding later.

---

## Variant: Appendix — The Invariants behind the Formulas

**Abstract:** *An invariant is a rule that stays true while the numbers change. These six invariants are the load-bearing walls behind nearly every formula in this module.*

> Build a compact map of the invariants used to derive and debug the embedded-option formulas.

<span class="jargon-unlock">**Invariant. What is an invariant?** A relationship that must remain true even when rates, prices, or tree nodes change. It is your formula debugger: if an answer breaks an invariant, the setup is wrong.</span>

**Invariant 1 — Ownership fixes the sign.** An option owned by the investor adds value; an option owned by the issuer removes value from the investor.

**Invariant 2 — The chooser takes the better deal.** At an exercise node, the investor chooses the larger value and the issuer forces the smaller value.

$$
Investor:\ \max(Keep,Exercise),\qquad Issuer:\ \min(Keep,Exercise)
$$

**Invariant 3 — Every tree node is just one-period present value.** Expected next value plus the next coupon is divided by one plus the node discount rate.

**Invariant 4 — Price and discount rate move in opposite directions.** A larger denominator means a smaller present value.

**Invariant 5 — A matching-index floater resets toward par.** If coupon rate and discount rate match at reset, numerator and denominator cancel back to 100.

**Invariant 6 — A convertible keeps the better exit.** The holder can stay in the bond or convert into stock, so neither route can push the minimum below the better one.

$$
Minimum\ convertible\ value=\boxed{\max(Straight\ value,Conversion\ value)}
$$

> [!NOTE]
> When a derivation feels slippery, return here: ownership gives the sign, control gives min or max, and discounting brings future money home.

---

## Variant: Appendix — Derive the Embedded-Option Value Identities

**Abstract:** *Start with the same straight bond, then add investor-owned rights and subtract issuer-owned rights. The signs come from ownership, not memorization.*

> Derive the value identities for callable, putable, and callable–putable convertible bonds.

<span class="jargon-unlock">**Value identity. What is a value identity?** Two economically identical packages must have the same price. Here $V$ means value, $V_S$ is straight-bond value, $C_I$ is an issuer-owned call, $P_H$ is a holder-owned put, and $C_E$ is the holder’s call on the issuer’s equity.</span>

A callable investor owns the straight bond but has handed the call right to the issuer. By Appendix Invariant 1:

$$
\boxed{V_{callable}=V_S-C_I}
$$

Move terms across the equals sign when the question asks for the option itself:

$$
\boxed{C_I=V_S-V_{callable}}
$$

A put belongs to the holder, so it adds:

$$
\boxed{V_{putable}=V_S+P_H},\qquad \boxed{P_H=V_{putable}-V_S}
$$

A convertible may stack several rights. Keep the ownership signs visible:

$$
\boxed{V_{convertible}=V_S+C_E-C_I+P_H}
$$

> [!NOTE]
> Investor owns it: plus. Issuer owns it: minus. That one invariant derives every sign on this page.

---

## Variant: Appendix — Derive Tree Rollback and Exercise Rules

**Abstract:** *A tree is repeated one-period discounting. First price continuation, then let whoever controls the option choose at that node.*

> Derive the generic rollback formula and the callable and putable node rules.

<span class="jargon-unlock">**Node. What is a node?** One possible rate and bond value at one date. **Continuation value. What is it?** The value of keeping the bond alive. In $CV_t=[Coupon_{t+1}+qV_{t+1,u}+(1-q)V_{t+1,d}]/(1+r_t+s)$, $q$ is the pricing weight, $u$ and $d$ mean next-period up and down states, $r_t$ is the node benchmark rate, and $s$ is OAS.</span>

Future value has two possible branches. Weight them, add the coupon received over the step, and discount once:

$$
\boxed{CV_t=\frac{Coupon_{t+1}+qV_{t+1,u}+(1-q)V_{t+1,d}}{1+r_t+s}}
$$

For the curriculum’s equal-weight trees, set $q=0.5$. Now apply Appendix Invariant 2. The issuer controls a call and pays the cheaper route:

$$
\boxed{V_{t,callable}=\min(CV_t,Call\ price_t)}
$$

The investor controls a put and takes the richer route:

$$
\boxed{V_{t,putable}=\max(CV_t,Put\ price_t)}
$$

Roll those exercise-adjusted node values into the previous step. Never exercise once on an average value; the decision happens separately at every eligible node.

> [!NOTE]
> Tree speedrun: value the future, roll back one step, apply min or max at that node, then repeat until today.

---

## Variant: Appendix — Derive OAS and Its Direction Rules

**Abstract:** *OAS is the extra discount spread that forces model value onto market price. Higher spread means heavier discounting and therefore lower value.*

> Derive one-period OAS and explain how to solve it in a multi-period option tree.

<span class="jargon-unlock">**OAS. What is OAS?** Option-adjusted spread is one constant spread $s$ added to every benchmark node so $V_{model}(s)=P_{market}$. $V_{model}$ is tree value and $P_{market}$ is the observed full price.</span>

For one cash flow $CF_1$ discounted at benchmark rate $r_0$ plus spread $s$:

$$
P_0=\frac{CF_1}{1+r_0+s}
$$

Multiply through, divide by price, and isolate the spread:

$$
\boxed{s=\frac{CF_1}{P_0}-1-r_0}
$$

For several periods, there is no honest one-line isolation because $s$ enters every rollback denominator and may change exercise. Guess $s$, rebuild the entire tree, and adjust until:

$$
\boxed{V_{model}(s)-P_{market}=0}
$$

Appendix Invariant 4 supplies the search direction: if model value is too high, raise OAS; if model value is too low, cut OAS.

At an unchanged market price, more volatility makes a callable bond’s model value fall and a putable bond’s model value rise. OAS must undo those moves:

$$
\boxed{Volatility\uparrow:\quad OAS_{callable}\downarrow,\qquad OAS_{putable}\uparrow}
$$

> [!NOTE]
> OAS moves discount rates, not coupons or exercise prices. Re-run every node after changing it.

---

## Variant: Appendix — Derive Effective and One-Sided Duration

**Abstract:** *Duration measures slope: shock rates both ways, observe the price gap, and divide by the total rate distance and today’s price.*

> Derive effective duration from one-sided price changes and show the small-shock price approximation.

<span class="jargon-unlock">**Effective duration. What is it?** Revalued price sensitivity: $D_{eff}=(PV_- -PV_+)/(2\Delta c\,PV_0)$. $PV_0$ is today’s price, $PV_-$ is price after rates fall, $PV_+$ is price after rates rise, and $\Delta c$ is the positive decimal curve-shift size.</span>

Measure each side separately. Up-duration measures the loss when rates rise; down-duration measures the gain when rates fall:

$$
D_{up}=\frac{PV_0-PV_+}{\Delta c\,PV_0},\qquad D_{down}=\frac{PV_- -PV_0}{\Delta c\,PV_0}
$$

Average them. The two $PV_0$ terms cancel in the numerator:

$$
\frac{D_{up}+D_{down}}{2}
=\frac{PV_0-PV_++PV_--PV_0}{2\Delta c\,PV_0}
$$

So:

$$
\boxed{D_{eff}=\frac{PV_- -PV_+}{2\Delta c\,PV_0}=\frac{D_{up}+D_{down}}{2}}
$$

Appendix Invariant 4 gives the minus sign in the price approximation:

$$
\boxed{\frac{\Delta P}{P}\approx-D_{eff}\Delta c}
$$

The embedded option can shorten effective duration but cannot make it longer than the matching straight bond:

$$
\boxed{D_{callable}\le D_{straight},\qquad D_{putable}\le D_{straight}}
$$

Exercise likelihood explains the direction changes:

$$
Rates\downarrow\Rightarrow D_{callable}\downarrow,\qquad Rates\uparrow\Rightarrow D_{putable}\downarrow
$$

> [!NOTE]
> For an asymmetric callable or putable bond, keep both one-sided durations; their average hides which direction carries the real pain.

---

## Variant: Appendix — Derive Key-Rate Duration

**Abstract:** *Effective duration moves the whole curve; key-rate duration moves one maturity point and exposes where the bond is actually sensitive.*

> Derive key-rate duration and show why key-rate durations approximately add to effective duration for a parallel shift.

<span class="jargon-unlock">**Key-rate duration, or KRD. What is it?** Sensitivity to one selected curve maturity $k$: $KRD_k=(PV_{k,-}-PV_{k,+})/(2\Delta z_kPV_0)$. $PV_{k,-}$ and $PV_{k,+}$ are prices after moving only key rate $k$ down and up, and $\Delta z_k$ is that decimal shock.</span>

The formula is the same centered slope as effective duration; only the shock changes:

$$
\boxed{KRD_k=\frac{PV_{k,-}-PV_{k,+}}{2\Delta z_kPV_0}}
$$

For small curve reshaping, add the contribution from each key point:

$$
\boxed{\frac{\Delta P}{P}\approx-\sum_k KRD_k\Delta z_k}
$$

If every key rate moves by the same parallel amount $\Delta c$, factor it out:

$$
\frac{\Delta P}{P}\approx-\left(\sum_k KRD_k\right)\Delta c
$$

Compare that with $\Delta P/P\approx-D_{eff}\Delta c$ and the coefficients must approximately match:

$$
\boxed{D_{eff}\approx\sum_k KRD_k}
$$

> [!NOTE]
> The sum is an approximation because interpolation, option exercise, and larger curve moves can make the price response nonlinear.

---

## Variant: Appendix — Derive Effective Convexity

**Abstract:** *Duration captures slope; convexity captures bend. Adding both shocked prices cancels the slope and leaves the curvature behind.*

> Derive effective convexity and combine it with duration for a price-change estimate.

<span class="jargon-unlock">**Effective convexity. What is it?** Revalued curvature: $C_{eff}=(PV_-+PV_+-2PV_0)/[(\Delta c)^2PV_0]$. The three $PV$ terms are down-shift, up-shift, and current prices; $\Delta c$ is the decimal curve shock.</span>

For equal shocks, the first-order gain on one side and loss on the other cancel when prices are added. What remains is the bend around today’s price:

$$
\boxed{C_{eff}=\frac{PV_-+PV_+-2PV_0}{(\Delta c)^2PV_0}}
$$

The squared shock appears because curvature is a second-order effect. Put slope and bend together:

$$
\boxed{\frac{\Delta P}{P}\approx-D_{eff}\Delta c+\frac12C_{eff}(\Delta c)^2}
$$

Positive convexity makes both directions kinder than the straight-line estimate. Negative convexity—common when a call is near the money—means the falling-rate upside is capped harder than rising-rate downside.

That gives the module’s usual local ranking when the options are near the money:

$$
\boxed{C_{callable}\text{ may be negative};\quad C_{straight}>0;\quad C_{putable}>0}
$$

Some systems report scaled convexity:

$$
\boxed{C_{scaled}=\frac{C_{raw}}{100}}
$$

> [!NOTE]
> Never mix raw and scaled convexity in the price formula. Check the reporting convention before plugging in.

---

## Variant: Appendix — Derive Capped, Floored, and Collared Floater Formulas

**Abstract:** *A cap clips coupons for the issuer; a floor lifts coupons for the investor. Value signs follow ownership, while coupon formulas follow min and max.*

> Derive the coupon and value formulas for capped, floored, and collared floating-rate bonds.

<span class="jargon-unlock">**Floater. What is a floater?** A bond whose coupon resets from a reference rate $R$ plus quoted margin $m$. A cap is maximum coupon $K_c$; a floor is minimum coupon $K_f$.</span>

The contractual coupon rates are simply ceiling and floor operations:

$$
Coupon_{capped}=\min(R+m,K_c),\qquad Coupon_{floored}=\max(R+m,K_f)
$$

The issuer owns the cap, so Appendix Invariant 1 makes it subtract from the straight floater $V_F$:

$$
\boxed{V_{capped}=V_F-V_{cap}}
$$

The investor owns the floor, so it adds:

$$
\boxed{V_{floored}=V_F+V_{floor}}
$$

A collar contains both:

$$
\boxed{V_{collared}=V_F-V_{cap}+V_{floor}}
$$

By Appendix Invariant 5, a matching-index floater is about par at reset and its duration is about the time to the next reset:

$$
\boxed{V_F\approx100,\qquad D_{floater}\approx Time\ to\ next\ reset\ in\ years}
$$

> [!NOTE]
> Coupon rule and value sign are different questions: min/max sets cash; issuer/investor ownership sets subtraction/addition.

---

## Variant: Appendix — Derive Convertible-Bond Metrics

**Abstract:** *Translate one bond into shares, compare the stock exit with the bond exit, and keep every measure on the same per-bond or per-share basis.*

> Derive conversion price, conversion value, minimum value, market conversion price, and conversion premium.

<span class="jargon-unlock">**Conversion ratio, or $CR$. What is it?** Shares received per bond. **Par, or $F$. What is it?** Contractual face value. **Share price, or $S$. What is it?** Current stock price. **Convertible price, or $P_{CB}$. What is it?** Current market price of the bond.</span>

If face value $F$ is exchanged for $CR$ shares, the contractual price paid per share is:

$$
\boxed{Conversion\ price=\frac{F}{CR}},\qquad \boxed{CR=\frac{F}{Conversion\ price}}
$$

Selling the received shares at market price $S$ gives conversion value:

$$
\boxed{Conversion\ value=CR\times S}
$$

Appendix Invariant 6 says the holder keeps the better exit:

$$
\boxed{Minimum\ value=\max(V_{straight},CR\times S)}
$$

Buying the bond and converting effectively pays this much per share:

$$
Market\ conversion\ price=\frac{P_{CB}}{CR}
$$

Compare that effective price tag with direct stock purchase:

$$
\boxed{Premium_{share}=\frac{P_{CB}}{CR}-S},\qquad \boxed{Premium\%=\frac{Premium_{share}}{S}}
$$

> [!NOTE]
> Units are the debugger: divide bond dollars by shares before comparing with a dollars-per-share stock price.

---

## Variant: Appendix — Derive Anti-Dilution and Sinking-Fund Mechanics

**Abstract:** *Anti-dilution preserves the same conversion claim through a stock split; sinking-fund acceleration multiplies the scheduled retirement amount.*

> Derive the stock-split conversion adjustment and the sinking-fund triple-up calculation.

<span class="jargon-unlock">**Anti-dilution. What is it?** A reset that preserves the convertible holder’s economic claim after specified corporate actions. **Split factor, or $n$. What is it?** New shares received for each old share. **Sinking-fund acceleration. What is it?** Permission to retire more than the mandatory scheduled principal.</span>

The conversion claim before a split is $CR_{old}\times CP_{old}=F$. To preserve that face-value claim after an $n$-for-one split, multiply shares and divide price by the same factor:

$$
\boxed{CR_{new}=nCR_{old},\qquad CP_{new}=\frac{CP_{old}}{n}}
$$

The invariant check proves nothing changed:

$$
CR_{new}CP_{new}=(nCR_{old})\left(\frac{CP_{old}}{n}\right)=\boxed{CR_{old}CP_{old}=F}
$$

For original issue principal $F_0$, mandatory retirement fraction $a$, and acceleration multiple $m$:

$$
Mandatory=aF_0
$$

Apply the allowed multiple. If this is the first retirement, the amount left from the original issue is:

$$
\boxed{Accelerated\ retirement=maF_0},\qquad \boxed{First\!\!-date\ remaining=F_0-maF_0}
$$

> [!NOTE]
> Stock-split ratio and conversion price move inversely; the sinking-fund percentage normally applies to original principal.

---

## Variant: Appendix — Derive the Directional Relationships

**Abstract:** *Rates move the straight bond first; the embedded option then either fights or amplifies that move. Volatility enriches both options, regardless of who owns them.*

> Derive the main direction rules for rates, curve shape, volatility, and callable or putable bond value.

<span class="jargon-unlock">**Directional relationship. What is it?** A reliable up-or-down link rather than an exact amount. **Moneyness. What is it?** Whether exercising beats continuation: an in-the-money option is worth using now.</span>

Appendix Invariant 4 starts the chain. When rates fall, straight-bond value rises. Refinancing becomes attractive, so the issuer call also rises and steals some of that gain:

$$
Rates\downarrow:\quad V_S\uparrow,\ C_I\uparrow,\ V_{callable}=V_S-C_I\uparrow\text{ less}
$$

The investor put becomes less useful, while the putable bond keeps the straight bond’s uncapped upside:

$$
Rates\downarrow:\quad P_H\downarrow,\ V_{putable}=V_S+P_H\uparrow
$$

Reverse the logic when rates rise: the call fades, while the put becomes valuable and cushions the putable bond’s loss.

More rate volatility creates more extreme states where either option pays. Therefore both option values rise, then Appendix Invariant 1 fixes the bond effects:

$$
\boxed{Volatility\uparrow:\quad C_I\uparrow,\ P_H\uparrow,\ V_{callable}\downarrow,\ V_{putable}\uparrow}
$$

A flatter or inverted curve generally places lower forward rates in more future nodes. That creates more issuer-call opportunities and fewer investor-put opportunities:

$$
\boxed{Curve\ flattens/inverts:\quad C_I\uparrow,\qquad P_H\downarrow}
$$

> [!NOTE]
> Separate option value from bond value. More volatility helps the option owner; whether the bond investor wins depends on who owns that option.

<!--
SOURCE COVERAGE AUDIT — Official CFA Level II Fixed Income, Learning Module 3, printed pp. 119–198.
LOS a–c: Variants 1–9, 53–55, and 62. LOS d–f: Variants 10–11 and 53–55. LOS g–h: Variants 12–15. LOS i–l: Variants 16–36 and 58. LOS m: Variants 37–43, 56–57, and 60. LOS n–q: Variants 44–52, 59, and 61.
Numbered equations: Eq. 1 in Variants 2–3; Eq. 2 in Variants 2 and 4; Eq. 3 in Variants 16–19, 25, and 58; Eq. 4 in Variants 32–36; Eq. 5 in Variants 37 and 39; Eq. 6 in Variants 38 and 40.
Official Examples 1–9: covered by Variants 1 and 62; 2 and 5; 8 and 10; 9 and 10; 12–15; 32–36; 16, 23–24, and 34; 37–43 and 60; 44–52, 59, and 61.
Official Practice Questions 1–36: Q1–10 in Variants 1, 9–11, 44–48, and 53–55; Q11–18 in Variants 2, 8, and 10–15; Q19–27 in Variants 14, 19–22, 37–43, 46, and 56–57; Q28–36 in Variants 23–36, 39–40, 49–52, and 58–59.
Secondary cross-check only: Schweser Fixed Income Reading 25. No Schweser-only rule or formula was introduced.
Formula appendix: Variants 63–73. The appendix derives the module’s value identities, rollback and exercise rules, OAS, duration, KRD, convexity, floater, convertible, anti-dilution, sinking-fund, and directional relationships from six named invariants.
-->
