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

> [!NOTE]
> This workbook has 24 study cases. The 11 appendices are optional formula derivations, not additional question types.

---

## Variant: Value Bonds and Recover Their Embedded Options

**Abstract:** *Ownership determines the sign: subtract the issuer’s right and add the investor’s. Solving for the option is the same identity rearranged.*

> A straight bond is worth 104. An otherwise identical callable bond is worth 101 and a putable bond 108. Recover each option value, reconstruct the bond prices, and rank them.

<span class="jargon-unlock">**Straight bond. What is it?** The matching bond without options. **Embedded option value. What is it?** The price difference attributable to the contractual right; $V_S$ is straight value, $C$ the issuer call, and $P$ the holder put.</span>

The callable investor gives the issuer a right, so receives a less valuable package. The putable investor receives an extra right.

$$
C=V_S-V_{callable}=104-101=\boxed{3},\qquad P=V_{putable}-V_S=108-104=\boxed{4}
$$

Reconstructing the packages checks the signs:

$$
V_{callable}=104-3=\boxed{101},\qquad V_{putable}=104+4=\boxed{108}
$$

> [!NOTE]
> For otherwise identical bonds, callable ≤ straight ≤ putable. A call limits falling-rate upside; a put cushions rising-rate downside.

---

## Variant: Apply Call and Put Decisions without Rate Volatility

**Abstract:** *Discount to the exercise date, compare continuation with the exercise price, and then add the coupon when rolling back. One known future rate is a one-branch tree.*

> A two-year annual-pay bond has par 100 and coupon 5. Today’s one-year rate is 4%. At Year 1, immediately after the coupon, it is either callable or putable at 100. Value each contract if the known Year-1 rate is (a) 2% or (b) 10%.

<span class="jargon-unlock">**Continuation value. What is it?** The value of keeping the remaining payments. **Ex-coupon. What does it mean?** The coupon due at the exercise date has already been separated. The issuer chooses the smaller value; the investor chooses the larger.</span>

At Year 1, only the final 105 remains. Discount it one year:

$$
CV_{low}=105/1.02=102.941176,\qquad CV_{high}=105/1.10=95.454545
$$

Apply each right separately. These are two alternative contracts, not a bond with both rights.

| Known Year-1 rate | Callable node: $\min(CV,100)$ | Putable node: $\max(CV,100)$ |
|---|---:|---:|
| 2% | 100: call | 102.941176: keep |
| 10% | 95.454545: keep | 100: put |

Bring each coupon-plus-node package back to today:

$$
V_0=\frac{5+V_1}{1.04}
$$

Thus the callable values are $\boxed{100.962}$ and $\boxed{96.591}$; the putable values are $\boxed{103.790}$ and $\boxed{100.962}$, respectively.

> [!NOTE]
> Apply min/max only on eligible exercise dates. Comparing ex-coupon continuation with the exercise price avoids counting the current coupon twice.

---

## Variant: Rebuild the Official Callable-Bond Tree Result

**Abstract:** *Work from the last year backward and let the issuer replace any value above the call price with 100.*

> A three-year 4.40% annual-pay bond is callable at par at the end of Years 1 and 2. Its rate tree is 2.2500% now; 3.5930% and 2.9417% in Year 1; and 4.6470%, 3.8046%, and 3.1150% in Year 2. Use equal risk-neutral branch probabilities and exercise after each coupon. Find its value per 100 of par.

<span class="jargon-unlock">**Backward induction. What is it?** Start at maturity and repeatedly use $PV=(Coupon+Expected\ next\ value)/(1+Node\ rate)$. **Call cap. What is it?** At a call date, use $\min(Continuation\ value,100)$ because the issuer will not hand investors more than the par call price.</span>

At Year 2, discount the final 104.4 using $104.4/(1+r_2)$: the uncapped values are 99.764, 100.574, and 101.246. Apply the par call:

$$
V_2=\min(Uncapped\ value,100)=(99.764,100,100)
$$

Year 1 continuation values are $(4.4+0.5(99.763968)+0.5(100))/1.035930=100.665088$ and $104.4/1.029417=101.416627$. Both exceed 100, so both are capped at 100. The source diagram prints 100.655 at the upper node; the displayed inputs give 100.665088. This does not change the call decision. Roll those values to today:

$$
V_0=\frac{4.40+0.5(100)+0.5(100)}{1.0225}=\boxed{102.103}
$$

> [!NOTE]
> The current value can exceed 100 because the bond cannot be called today. If it were callable now at 100, the current ex-coupon value would be capped at 100.

> [!NOTE]
> If no eligible node ever reaches the call price, the call is worthless and the bond equals its straight counterpart. With zero volatility, each branch collapses to the same known rate.

---

## Variant: Rebuild the Official Putable-Bond Tree Result

**Abstract:** *Work backward and let the investor replace any exercise-date value below the put price with 100.*

> A three-year annual-pay bond has par 100, coupon 4.40, and puts at par after the Years 1 and 2 coupons. One-year rates are 2.2500% today; 3.5930%/2.9417% in Year 1; and 4.6470%/3.8046%/3.1150% in Year 2, from high to low. Branch probabilities are 0.5. Find today’s value.

<span class="jargon-unlock">**Put floor. What is it?** At a put date, use $\max(Continuation\ value,100)$ because the investor can demand the par put price instead of keeping a cheaper bond.</span>

At Year 2, calculate $104.4/(1+r)$ in each state: 99.763968, 100.573578, and 101.246181. The put changes only the first:

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

> [!NOTE]
> If no eligible node falls below the put price, the put adds zero value. A putable bond also matches a shorter bond with a holder extension right when every possible cash flow matches.

---

## Variant: Separate Rate-Level, Curve-Shape, and Volatility Effects

**Abstract:** *Compare volatility at the same benchmark curve. Both options gain from more volatility; ownership determines which bond investor benefits.*

> For the same three-year 4.25% bond and unchanged benchmark curve, official callable values at 0% and 10% volatility are 101.707 and 101.540; putable values are 102.397 and 102.522. Calculate the changes. Explain the usual effects of falling rates and a flatter or inverted curve.

<span class="jargon-unlock">**Volatility. What is it?** Dispersion in possible future rates. **Calibration. What is it?** Adjusting the tree to reproduce the same benchmark prices. **Forward rates. What are they?** Future-period rates implied by today’s curve.</span>

Use the matched-curve values from curriculum Exhibits 2–3 and 12–13:

$$
\Delta V_{callable}=101.540-101.707=\boxed{-0.167},\qquad
\Delta V_{putable}=102.522-102.397=\boxed{+0.125}
$$

More volatility raises both option values. The callable investor is short the call; the putable investor owns the put.

| Change, other relevant assumptions fixed | Issuer call | Investor put |
|---|---|---|
| Rates fall | More valuable: refinancing improves | Less valuable: keeping the bond improves |
| Rates rise | Less valuable | More valuable |
| Curve flattens/inverts in the curriculum comparison | More valuable as forward rates fall | Less valuable |

> [!NOTE]
> Changing branch rates without recalibrating can change both volatility and the benchmark curve. That does not isolate the volatility effect.

> [!NOTE]
> Lower rates generally raise both bond prices, but the call restrains appreciation. Higher rates reduce prices, but the put cushions depreciation.

---

## Variant: Price with OAS and Solve Backward for the Spread

**Abstract:** *Add one constant spread to every discount rate, then repeat all exercise decisions. To infer the spread, find the value that reproduces market price.*

> A two-year bond pays annual coupon 5 on par 100 and is callable at 100 after the Year-1 coupon. Benchmark rates are 4% now and 2%/10% in Year 1 with equal pricing weights. Price it with 200 bps OAS, and explain how to recover OAS from that market price.

<span class="jargon-unlock">**OAS. What is it?** Option-adjusted spread $s$, added to each benchmark node rate $r$. One basis point is 0.0001 in decimal rate units, so 200 bps is 0.02.</span>

The spread changes discounting before the issuer makes its choice:

$$
V_{1,low}=\min(105/1.04,100)=100,\qquad V_{1,high}=\min(105/1.12,100)=93.75
$$

Roll back using today’s benchmark rate plus the same spread:

$$
V_0=\frac{5+0.5(100)+0.5(93.75)}{1.06}=\boxed{96.108491}
$$

If that is the market price, solve $V_{model}(s)=96.108491$ by trial and error or numerical root finding. Raise $s$ when model value is too high; lower it when value is too low. Here the recovered spread is approximately $\boxed{200\text{ bps}}$.

For a single payment with no remaining exercise decision, algebra suffices. A payment of 105 priced at 100 against a 3% benchmark implies:

$$
s=\frac{CF}{P}-1-r=\frac{105}{100}-1-0.03=\boxed{2\%}
$$

> [!NOTE]
> In a multiperiod tree, every trial spread requires fresh continuation values and exercise tests. OAS changes neither the coupon nor the exercise price.

---

## Variant: Compare OAS and Recalibrate after a Volatility Change

**Abstract:** *Compare spreads under consistent credit and model assumptions. At fixed market price, OAS must offset a volatility-driven model-price change.*

> Otherwise comparable callable bonds A and B have OAS of 65 and 85 bps. Which is cheaper? If assumed rate volatility increases while market prices stay fixed, how must callable and putable OAS change?

<span class="jargon-unlock">**Relative value. What is it?** Comparing market prices against a consistent valuation model. **Recalibration. What is it?** Changing the spread until model value again equals observed price.</span>

Bond B offers 20 bps more spread for comparable risk and is $\boxed{\text{relatively cheaper}}$.

At unchanged OAS, higher volatility reduces callable model value and increases putable model value. Since increasing the discount spread reduces price:

$$
\boxed{OAS_{callable}\downarrow,\qquad OAS_{putable}\uparrow}
$$

> [!NOTE]
> A larger spread can compensate for worse credit or different terms. Compare similar bonds using the same benchmark, volatility, and valuation conventions.

> [!NOTE]
> Hold market price fixed when recalibrating OAS. Hold OAS fixed when measuring effective duration.

---

## Variant: Calculate Effective Duration after Finding the Current Tree Price

**Abstract:** *Find the unshifted price if it is missing, then divide the shocked-price gap by the total curve move and current full price.*

> A three-year 4% annual-pay bond has par 100 and calls at par after the Years 1 and 2 coupons. Rates are 2.5000% now; 4.6343%/3.4331% in Year 1; and 5.3340%/3.9515%/2.9274% in Year 2. Branch weights are 0.5. Prices for −20/+20 bp curve shifts are 101.238/100.478. Calculate effective duration.

<span class="jargon-unlock">**Full price $PV_0$. What is it?** Today’s value including accrued interest; this example is at a coupon date. **Effective duration $D$. What is it?** $D=(PV_- -PV_+)/(2hPV_0)$, with decimal curve shock $h$, down-rate price $PV_-$, and up-rate price $PV_+$.</span>

**1. Obtain the missing denominator.** At Year 2, cap each discounted final payment:

$$
V_2=\min\left(\frac{104}{1+r_2},100\right)=(98.733552,100,100)
$$

Roll back, applying the Year-1 calls:

$$
V_{1,u}=\min\left(\frac{4+0.5(98.733552+100)}{1.046343},100\right)=98.788615,\qquad V_{1,d}=100
$$

Therefore:

$$
PV_0=\frac{4+0.5(98.788615+100)}{1.025}=\boxed{100.872495}
$$

The official solution displays 100.873; using the displayed tree rates at full precision gives the value above. The duration answer is unaffected at two decimals.

**2. Convert 20 bps to 0.002 and substitute.**

$$
D=\frac{101.238-100.478}{2(0.002)(100.872495)}=\boxed{1.88}
$$

> [!NOTE]
> Do not substitute par for current price. Revalue the option under both shocks while holding the original OAS fixed.

> [!NOTE]
> A missing shocked price is the same equation rearranged: $PV_+=PV_- -2hPV_0D$. It does not require a separate method.

---

## Variant: Rebuild Shocked Trees before Calculating Effective Duration

**Abstract:** *Revalue every node under each recalibrated curve, keeping OAS fixed. Then use those two prices in the usual duration formula.*

> A three-year 5.25% annual-pay bond, par 100, is callable at par after Years 1 and 2 coupons and trades at 100.200. For a −30 bp shift, adjusted tree rates are 3.8395%; 5.3363%/4.3943%; 7.1432%/5.8737%/4.8342%. For +30 bps, they are 4.4395%; 6.0000%/4.9377%; 7.8827%/6.4791%/5.3299%. Branch weights are 0.5. Calculate effective duration.

<span class="jargon-unlock">**Adjusted tree. What is it?** These official Q28 rates already include the fixed 13.95 bp OAS. **Rollback. What is it?** At each eligible node, $V_t=\min([5.25+0.5(V_u+V_d)]/(1+r_t),100)$.</span>

Begin with redemption of 100 at maturity. Apply each Year-2 rate to 105.25, then roll back and cap again in Year 1:

| Curve shock | Year-2 values, high to low | Year-1 values, high to low | Today |
|---|---|---|---:|
| −30 bps | 98.233019; 99.410902; 100 | 98.799711; 100 | 100.780393 |
| +30 bps | 97.559664; 98.845689; 99.924143 | 97.596865; 99.711463 | 99.487420 |

For example, the down-shock high Year-1 node is $(5.25+0.5(98.233019+99.410902))/1.053363=98.799711$. Today is not an exercise date, so discount without a call cap:

$$
PV_- =\frac{5.25+0.5(98.799711+100)}{1.038395}=100.780393
$$

Using full-precision prices:

$$
D=\frac{100.780393-99.487420}{2(0.003)(100.200)}=\boxed{2.15}
$$

> [!NOTE]
> Do not add OAS twice. Do not mechanically shift each original short-rate node by 30 bps: the benchmark curve is shifted and the tree recalibrated.

---

## Variant: Measure One-Sided Duration and Recover the Average

**Abstract:** *Calculate each direction separately to reveal the option’s asymmetry. Their average equals effective duration for equal-sized shocks.*

> For 30 bp shocks, a callable bond has current/down-rate/up-rate prices 99.75/100.00/99.17. A putable bond has 100.45/101.81/100.00. Find each up-duration, down-duration, and two-sided duration.

<span class="jargon-unlock">**Up-duration. What is it?** $D_{up}=(P_0-P_+)/(hP_0)$, sensitivity when rates rise. **Down-duration. What is it?** $D_{down}=(P_- -P_0)/(hP_0)$, sensitivity when rates fall; $h=0.003$.</span>

For the callable bond, measure the price loss and gain relative to today:

$$
D_{up}=\frac{0.58}{0.003(99.75)}=\boxed{1.94},\qquad
D_{down}=\frac{0.25}{0.003(99.75)}=\boxed{0.84}
$$

For the putable bond, use its own current price:

$$
D_{up}=\frac{0.45}{0.003(100.45)}=\boxed{1.49},\qquad
D_{down}=\frac{1.36}{0.003(100.45)}=\boxed{4.51}
$$

Averaging the unrounded values gives $\boxed{D_{callable}=1.39}$ and $\boxed{D_{putable}=3.00}$ because:

$$
\frac{D_{up}+D_{down}}2=\frac{P_- -P_+}{2hP_0}
$$

> [!NOTE]
> Near exercise, a call limits rates-down upside ($D_{up}>D_{down}$); a put limits rates-up downside ($D_{down}>D_{up}$). Straight-bond one-sided durations are approximately equal for small shocks.

---

## Variant: Interpret Duration across Bond Types and Exercise States

**Abstract:** *Duration follows the likely repayment date and coupon resetting. Exercise can shorten exposure well before legal maturity.*

> Compare cash, a five-year zero, a five-year coupon bond, and a plain floater resetting in two months. Explain how the duration of a 10-year callable or putable bond with a Year-2 exercise date changes as rates move.

<span class="jargon-unlock">**Duration. What is it?** Price sensitivity to a small interest-rate change. **Reset. What is it?** Updating a floater’s coupon to its reference rate. **Exercise likelihood. What is it?** Whether early repayment is economically attractive.</span>

Cash has approximately zero rate duration. A zero-coupon bond’s duration is approximately its maturity; with annual yield compounding its local yield duration is $T/(1+y)$, rather than exactly $T$. A positive-coupon bond has shorter duration than a matching zero under the usual positive-rate setup.

For a plain floater with stable credit spread and a flat reference curve:

$$
D_{floater}\approx\frac{2}{12}=\boxed{0.167\text{ years}}
$$

| Bond | Rates fall | Rates rise |
|---|---|---|
| Callable | Call becomes more likely; duration tends toward exposure to the call date | Call fades; duration approaches straight-bond duration |
| Putable | Put fades; duration approaches straight-bond duration | Put becomes more likely; duration tends toward exposure to the put date |

> [!NOTE]
> In the curriculum’s conventional comparisons, callable and putable durations do not exceed the matching straight bond. There is no universal ordering between the callable and putable durations.

> [!NOTE]
> Time to next reset approximates a plain floater’s benchmark-rate duration, not its credit-spread sensitivity or the duration of a floater with a binding cap/floor.

---

## Variant: Calculate Key-Rate Risk for Parallel and Uneven Curve Moves

**Abstract:** *Shock one maturity to measure its sensitivity. For a curve scenario, multiply each sensitivity by its own signed rate move before adding.*

> A bond is worth 100. Moving only its five-year par rate down/up 10 bps gives 100.20/99.80. Its two- and ten-year KRDs are 0.5 and 4.0. Find five-year KRD, estimate the price effect of +10/−5/+20 bp moves at 2/5/10 years, and reconcile a parallel −50 bp move.

<span class="jargon-unlock">**Key-rate duration $KRD_k$. What is it?** Sensitivity to curve point $k$: $(P_{k,-}-P_{k,+})/(2hP_0)$, holding other key rates fixed. **Parallel shift. What is it?** Every key rate moves equally.</span>

First isolate five-year sensitivity:

$$
KRD_5=\frac{100.20-99.80}{2(0.001)(100)}=\boxed{2.00}
$$

For different moves, weight each one separately:

$$
\frac{\Delta P}{P}\approx-\sum_k KRD_k\Delta z_k
=-[0.5(0.001)+2(-0.0005)+4(0.002)]=\boxed{-0.75\%}
$$

If the key-rate shocks span the parallel shift consistently, their sum approximates effective duration:

$$
D\approx0.5+2+4=\boxed{6.5},\qquad
\frac{\Delta P}{P}\approx-6.5(-0.005)=\boxed{+3.25\%}
$$

> [!NOTE]
> A negative KRD uses the same formula: $KRD=-0.5$ and a +10 bp move imply $-(-0.5)(0.001)=+0.05\%$. Do not discard the sign.

---

## Variant: Locate Key-Rate Exposure and Explain Negative Components

**Abstract:** *Principal usually concentrates risk near maturity; likely exercise moves it toward the exercise date. Par-curve shocks can give shorter points negative sensitivities.*

> A 10-year 4% option-free bond trades at par on a 4% par curve at zero OAS. Where is its KRD? A 30-year high-coupon callable bond, callable in Year 10, has ten-/thirty-year KRDs of 6.06/0.19. Explain the difference and why a low-coupon bond can have negative shorter-point KRD.

<span class="jargon-unlock">**Par curve. What is it?** Coupon rates that price matching bonds at par. **Economic maturity. What is it?** The likely repayment date. **Bootstrapping. What is it?** Inferring discount rates from quoted bond/par rates.</span>

The par bond stays at par while its own maturity-matched par rate stays at 4%. Thus, in the curriculum’s matching-curve setup:

$$
\boxed{KRD_{10}=D,\qquad KRD_{shorter}=0}
$$

For the callable bond, $6.06>0.19$: the likely Year-10 call concentrates risk near that exercise date. If the option becomes unlikely to be exercised, exposure shifts back toward final maturity. A likely put has the same shortening effect.

For a low-coupon or zero-coupon bond, raising a shorter par rate while holding longer par rates fixed can lower implied long-maturity discount rates. That raises the distant redemption value, producing a negative shorter-point KRD.

> [!NOTE]
> The zero-shorter-KRD rule requires a matching par bond at zero OAS. Away from par, shorter points can matter; maturity usually remains the dominant point for an option-free bond.

---

## Variant: Calculate Convexity and Use It with Duration

**Abstract:** *Adding shocked prices removes the first-order slope and reveals curvature. Keep the convexity scale consistent when estimating a price change.*

> A callable bond has current/down-rate/up-rate prices 100.785/101.381/100.146 for 30 bp shocks. Calculate convexity and interpret its sign. Separately, for a bond with duration 5 and raw convexity 40, estimate the price change after a 100 bp curve rise.

<span class="jargon-unlock">**Effective convexity $C$. What is it?** Curvature allowing option exercise to change: $C=(P_-+P_+-2P_0)/(h^2P_0)$. **Duration $D$. What is it?** The first-order price sensitivity. Rate moves enter as decimals.</span>

For the callable bond:

$$
C=\frac{101.381+100.146-2(100.785)}{0.003^2(100.785)}=\boxed{-47.41}
$$

Its rates-down gain is 0.596, less than the 0.639 rates-up loss. That is negative curvature. In the reading’s conventional comparison, straight and putable bonds have positive convexity; a callable bond can become negatively convex near exercise.

For the separate price estimate, duration alone gives $-5(0.01)=-5\%$. Add curvature:

$$
\frac{\Delta P}{P}\approx-D\Delta c+\tfrac12C(\Delta c)^2
=-5(0.01)+\tfrac12(40)(0.01)^2=\boxed{-4.80\%}
$$

A current price of 100 would therefore become approximately $\boxed{95.20}$.

> [!NOTE]
> A vendor dividing convexity by 100 would display raw 40 as 0.40. Restore raw convexity before using the formula above.

> [!NOTE]
> These are local approximations. Large moves or changed exercise decisions can make them inaccurate; reprice the tree when an exact model value is required.

---

## Variant: Apply Floater Coupon Limits and Identify Payment Timing

**Abstract:** *Compute the reference coupon, then clip it with min/max. The fixing date tells you which rate applies; the payment date tells you when cash arrives.*

> On par 100 with annual coupons and zero margin, find the payment for a 4.50% cap when the reference rate is 5.53%, and for a 3.50% floor when it is 2.50%. Also find cash paid if a coupon is explicitly fixed and paid at year-end using 4.20%.

<span class="jargon-unlock">**Floater. What is it?** A bond with coupon rate $R+m$, reference rate plus contractual margin. **Cap/floor. What are they?** A maximum/minimum coupon rate. **Set in arrears. What is it?** Fixing at the period’s end; payment timing must also be specified.</span>

Apply the limit to the rate, then multiply by par and the one-year accrual fraction:

$$
Coupon_{cap}=100\min(0.0553,0.045)=\boxed{4.50},\qquad
Coupon_{floor}=100\max(0.025,0.035)=\boxed{3.50}
$$

The explicitly same-day fixing/payment gives $100(0.042)=\boxed{4.20}$ paid that day. To value that payment at an earlier date, discount back to that date.

> [!NOTE]
> The official reading calls its tree floaters “set in arrears,” but its worked diagrams use the rate shown at Year $t$ for the coupon paid at Year $t+1$. The tree cases here explicitly follow those diagrams.

> [!NOTE]
> Distinguish payment in arrears from fixing in arrears. Do not combine a same-day-fixing assumption with a next-period-coupon rollback without stating the model convention.

---

## Variant: Roll Back the Official Capped Floater

**Abstract:** *Cap every coupon first, then discount the resulting cash flows through the tree.*

> A three-year floater pays annual reference-rate coupons capped at 5.00%, with no credit spread. Follow the official worked-tree convention: each node’s rate sets the coupon paid one year later; branch weights are 0.5. Rates are 3.0000% now; 4.5027% and 3.5419% in Year 1; and 6.3679%, 5.0092%, and 3.9404% in Year 2. Find value per 100 of par.

<span class="jargon-unlock">**Capped floater. What is it?** A floating-rate bond whose coupon is $Coupon=\min(Reference\ rate,Cap)$. **Coupon timing here. What is it?** The rate at node $t$ sets the cash coupon at $t+1$, as in the official solution diagram.</span>

At Year 2, the top two rates hit the 5% cap. Compute $[100+100\min(r,0.05)]/(1+r)$: the three node values are 98.714, 99.991, and 100.000. Retain unrounded values in the calculation. Roll back:

$$
V_{1,u}=\frac{4.5027+0.5(98.714)+0.5(99.991)}{1.045027}=99.381
$$

Now roll back from the middle and bottom Year 2 nodes.

$$
V_{1,d}=\frac{3.5419+0.5(99.991)+0.5(100)}{1.035419}=99.996
$$

Average the Year 1 values, add the Year-1 coupon, and discount to today.

$$
V_0=\frac{3.0000+0.5(99.381)+0.5(99.996)}{1.03}=\boxed{99.697}
$$

> [!NOTE]
> An uncapped matching-index floater is worth about 100. The issuer-owned cap removes upside, so 99.697 passes the smell test.

Recover the option value from the price gap:

$$
V_{cap}=100-99.697=\boxed{0.303}
$$

> [!NOTE]
> If the cap exceeds every possible reset rate, it changes no coupon and is worth zero. Equality at a node also makes no cash-flow difference.


---

## Variant: Roll Back the Official Floored Floater

**Abstract:** *Raise any coupon below the floor, then work backward exactly as for an ordinary floater.*

> A three-year floater has par 100, annual reference coupons, a 3.50% floor, no credit spread, and equal pricing weights. Rates are 3.0000% now; 4.5027%/3.5419% in Year 1; and 6.3679%/5.0092%/3.9404% in Year 2. Follow the official diagram: each node’s rate sets the next year’s coupon. Find bond and floor values.

<span class="jargon-unlock">**Floored floater. What is it?** A floating-rate bond whose coupon is $Coupon=\max(Reference\ rate,Floor)$, so the investor never receives less than the stated floor.</span>

Every Year 2 rate exceeds 3.50%, so all three Year 2 bond values are 100. Both Year 1 rates also exceed the floor, so both Year 1 values remain 100. The current 3.00% rate is below the floor, so today’s next coupon is raised to 3.50:

$$
V_0=\frac{3.50+0.5(100)+0.5(100)}{1.03}=\boxed{100.485}
$$

> [!NOTE]
> The investor-owned floor adds value. A result below 100 would tell you the sign or the max rule was flipped.

The embedded floor is the excess over the matching plain floater:

$$
V_{floor}=100.485437-100=\boxed{0.485437}
$$

For a consistent valuation of a floater containing both limits:

$$
V_{collared}=V_{plain}-V_{cap}+V_{floor}
$$

For example, a plain value of 100, cap of 0.40, and floor of 0.70 give $\boxed{100.30}$.

> [!NOTE]
> If the floor is at or below every possible reset rate, its value is zero. The floor changes coupons; it does not force the bond’s node value to an exercise price.


---

## Variant: Calculate Conversion Terms and the Market Premium

**Abstract:** *Convert par into shares to find the contract terms; convert market price into cost per share to find the premium. Keep both comparisons on the same unit basis.*

> A EUR 1,000 convertible has contractual conversion price EUR 10 and trades at EUR 1,123. Stock price is EUR 9.10. Find conversion ratio, conversion value, market conversion price, and premium per share and as a percentage.

<span class="jargon-unlock">**Conversion ratio $CR$. What is it?** Shares received per bond. **Contractual conversion price $CP$. What is it?** $F/CR$, with face value $F$. **Market conversion price. What is it?** Current bond price $P$ divided by $CR$, not par divided by $CR$.</span>

The contract delivers this number of shares:

$$
CR=\frac{1{,}000}{10}=\boxed{100\text{ shares}},\qquad CP=\frac{1{,}000}{100}=\boxed{\text{EUR }10}
$$

Selling those shares gives conversion value $CR\times S=100(9.10)=\boxed{\text{EUR }910}$.

The market price paid through the bond per share is:

$$
\frac{P}{CR}=\frac{1{,}123}{100}=\boxed{\text{EUR }11.23}
$$

Compare with buying stock directly:

$$
Premium_{share}=11.23-9.10=\boxed{\text{EUR }2.13},\qquad
Premium\%=\frac{2.13}{9.10}=\boxed{23.41\%}
$$

> [!NOTE]
> Conversion price and conversion ratio are inverse forms of one identity. A premium measures the extra price paid for the convertible’s bond protection and remaining option value.

---

## Variant: Use the Convertible Floor and Trade a Violated Conversion Bound

**Abstract:** *Compare the bond route with the share route. Immediate conversion provides an arbitrage only if the shares can actually be obtained and sold at the assumed prices.*

> A noncallable convertible delivers 23.26 shares worth USD 52 each; matching straight-bond value is USD 980. Find its minimum value. If the convertible costs USD 1,050 and conversion and share sale can be executed immediately without costs, describe the trade and profit.

<span class="jargon-unlock">**Conversion value. What is it?** $CR\times S$, shares per bond times price per share. **Straight value. What is it?** Present value of debt payments without conversion. **Arbitrage. What is it?** Locking in a positive price difference with offsetting trades under the stated assumptions.</span>

First price the conversion route:

$$
CV=23.26(52)=\boxed{\text{USD }1{,}209.52}
$$

For this conventional convertible with no issuer call interfering with the debt route:

$$
V_{min}=\max(980,1{,}209.52)=\boxed{\text{USD }1{,}209.52}
$$

Buy the bond for USD 1,050, immediately convert, and sell the 23.26 shares:

$$
Profit=1{,}209.52-1{,}050=\boxed{\text{USD }159.52\text{ per bond}}
$$

The curriculum Example 9 reports about USD 1,209 and USD 159. The displayed inputs produce 1,209.52 and 159.52; no assumption about an undisclosed precise conversion ratio is needed.

> [!NOTE]
> Conversion restrictions, settlement, costs, and issuer calls must be considered before applying the bound to a real contract. Straight value itself changes with rates and credit spreads.

> [!NOTE]
> Premium over straight value is $P_{CB}/V_{straight}-1$. It is not a guaranteed loss limit because the straight value can fall too.

---

## Variant: Adjust Conversion Terms for Corporate Actions

**Abstract:** *A stock split changes share count and conversion price inversely. Dividend protection follows the contract’s threshold and adjustment formula.*

> A convertible has a 25-share ratio and USD 40 conversion price before a two-for-one stock split. Find the new terms. Separately, a contract protects dividends above EUR 0.50 per share; a EUR 0.70 dividend is declared. State the conversion-price direction.

<span class="jargon-unlock">**Anti-dilution. What is it?** Contractual protection against specified corporate actions reducing the conversion claim. **Split factor. What is it?** New shares received for each old share; here it is 2.</span>

Double the number of shares and halve the price per share:

$$
CR_{new}=2(25)=\boxed{50},\qquad CP_{new}=40/2=\boxed{\text{USD }20}
$$

Both before and after, $CR\times CP=\boxed{\text{USD }1{,}000}$. Economically, if the share price halves in a pure split, twice as many conversion shares retain the same total market value.

The dividend exceeds its threshold, so under the stated protection $\boxed{CP\downarrow}$ and the conversion ratio increases.

> [!NOTE]
> The amount of a dividend adjustment requires the contract formula. The excess dividend alone is not automatically the amount subtracted from conversion price.

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

> [!NOTE]
> These are embedded component values under consistent contract assumptions. Independently priced standalone options need not capture interactions between call, put, and conversion rights.

To obtain those values from a model, evaluate continuation and permitted exercise choices at every node, then roll backward. At maturity a plain convertible pays the better of redemption and conversion, with coupon treatment specified by the contract. Earlier exercise also depends on future conversion opportunities, interest rates, equity risk, and credit risk.


---

## Variant: Classify Convertible Risk–Return Behavior

**Abstract:** *Compare stock price with conversion price: far below is bond-like, far above is stock-like, and nearby is hybrid.*

> A convertible’s conversion price is USD 40. Classify its behavior when the stock trades at USD 20, USD 38, and USD 60.

<span class="jargon-unlock">**Bond-like. What does it mean?** Straight-bond value dominates. **Stock-like. What does it mean?** Conversion value dominates. **Hybrid. What does it mean?** Both components materially influence price.</span>

$$
\boxed{\$20:\ Bond\!\!-like;\quad \$38:\ Hybrid;\quad \$60:\ Stock\!\!-like}
$$

> [!NOTE]
> The conversion price is the pivot: distance below or above it tells you which risk engine dominates.

Below the conversion price, rates and credit spreads usually dominate. Far above it, stock-price movements dominate. Near it, both matter: if the stock rises toward the conversion price from below, the convertible generally gains less in percentage terms than the stock, as in official Q36.

> [!NOTE]
> These are curriculum classifications, not exact thresholds. Remaining maturity, volatility, credit risk, and contractual terms also affect the mix of bond and equity exposure.


---

## Variant: Calculate a Sinking-Fund Triple-Up

**Abstract:** *A triple-up lets the issuer retire three times the mandatory principal amount at par on that sinking-fund date.*

> A sinking-fund bond has original principal of USD 100 million and requires its first 5% retirement of original principal this year. No principal has previously been retired. Its acceleration provision is a triple-up. How much may the issuer retire at par, and how much of the original issue remains if it uses the full amount?

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

> [!NOTE]
> A delivery option is a separate issuer benefit: if bonds trade at 90, buying 5 million face to satisfy a 5 million sinking-fund obligation costs only 4.5 million, assuming sufficient liquidity.


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

**Invariant 6 — A conventional noncallable convertible keeps the better exit.** The holder can stay in the bond or convert into stock, so neither route can push the minimum below the better one.

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

In the curriculum’s conventional bond comparisons, the embedded option shortens duration relative to the matching straight bond:

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

For a conventional noncallable convertible with conversion permitted, Appendix Invariant 6 compares the debt and stock routes:

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

The conversion claim before a split is $CR_{old}\times CP_{old}=F$. After an $n$-for-one split, multiply shares and divide conversion price by the same factor. If the stock price falls by that factor, conversion market value is also preserved:

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
CONSOLIDATION AUDIT — 2026-09-29
Source: official 2025 CFA Level II Fixed Income, Volume 6, LM3, printed pp. 119–198.
Errata consulted: https://www.cfainstitute.org/sites/default/files/docs/programs/cfa-program/candidate-resources/2025-cfa-level-ii-curriculum-errata.pdf (p.13 corrects Example 8 Q3 tree rates; it does not resolve the timing or Q4 intermediate discrepancies noted here).
Decision criterion: a standalone case earns its place by changing the cash-flow model, exercise decision, timing, valuation workflow, or risk interpretation. A rearrangement, changed inputs, or repeated official example does not alone qualify.
62 original study entries -> 24 study cases. Original 63–73 remain 11 optional derivation appendices.
All 62 original entries were reviewed. Mapping below refers to their pre-consolidation order:
New 1 (Identify the Embedded Option and Exercise Style): old 1.
New 2 (Value Bonds and Recover Their Embedded Options): old 2, 3, 4, 53.
New 3 (Apply Call and Put Decisions without Rate Volatility): old 5, 6, 7.
New 4 (Rebuild the Official Callable-Bond Tree Result): old 8, 54.
New 5 (Rebuild the Official Putable-Bond Tree Result): old 9, 55.
New 6 (Separate Rate-Level, Curve-Shape, and Volatility Effects): old 10, 11.
New 7 (Price with OAS and Solve Backward for the Spread): old 12, 13.
New 8 (Compare OAS and Recalibrate after a Volatility Change): old 14, 15.
New 9 (Calculate Effective Duration after Finding the Current Tree Price): old 16, 18, 19.
New 10 (Rebuild Shocked Trees before Calculating Effective Duration): old 58.
New 11 (Measure One-Sided Duration and Recover the Average): old 23, 24, 25.
New 12 (Interpret Duration across Bond Types and Exercise States): old 20, 21, 22, 43.
New 13 (Calculate Key-Rate Risk for Parallel and Uneven Curve Moves): old 26, 27, 28, 29.
New 14 (Locate Key-Rate Exposure and Explain Negative Components): old 30, 31.
New 15 (Calculate Convexity and Use It with Duration): old 17, 32, 33, 34, 35, 36.
New 16 (Apply Floater Coupon Limits and Identify Payment Timing): old 37, 38, 42.
New 17 (Roll Back the Official Capped Floater): old 39, 56.
New 18 (Roll Back the Official Floored Floater): old 40, 41, 57, 60.
New 19 (Calculate Conversion Terms and the Market Premium): old 44, 45, 47, 59.
New 20 (Use the Convertible Floor and Trade a Violated Conversion Bound): old 46, 61.
New 21 (Adjust Conversion Terms for Corporate Actions): old 48, 49.
New 22 (Decompose a Callable Putable Convertible): old 50, 51.
New 23 (Classify Convertible Risk–Return Behavior): old 52.
New 24 (Calculate a Sinking-Fund Triple-Up): old 62.

Specific dispositions:
Official Q4 source diagram prints upper Year-1 continuation as 100.655; recomputation gives 100.665088. Both trigger the call, so final price is unchanged. The source page was visually checked.
Old 10: removed unmatched/unexplained zero-volatility numerical inputs; substituted the official matched-curve 0%/10% comparison (Exhibits 2–3, 12–13).
Old 19: supplied a current price despite claiming it must be found. New 9 actually calculates the missing price from Q22 tree rates.
Old 58: supplied shocked prices despite claiming a tree rebuild. New 10 now performs both Q28 rollbacks; quoted node rates already include OAS.
Old 51: not retained as a separate required one-period equity-tree numerical. It was an added illustration, not a separate official worked question; its 1,095.24 result is arithmetically valid under default-free debt and an explicit coupon-forfeiture convention. The original omitted those assumptions. Its legitimate node-choice principle is retained in new 22.
Old 56–57: replaced inconsistent in-arrears narrative with explicit node-to-next-payment timing shown by official diagrams. Source prose on p.161 defines same-day fixing/payment; Exhibit 26 and solutions p.196 instead use node rate t for payment t+1. This is flagged in new 16 rather than silently treated as consistent.
Old 61: 23.26*52=1209.52 and profit=159.52. Removed unsupported attribution of the source 1209/159 figures to an unshown precise conversion ratio.
Old 62: 85 million remaining requires no earlier retirements; added that assumption.
Old 9: full-precision two-year putable value is 102.3755656, rounding to 102.376, not 102.375. Its replacement is the official three-year putable case.
Fixed bare currency dollar signs in retained question prose; made formerly dependent tree questions self-contained.
Original source ledger was inaccurate: official Example 5 is volatile-tree valuation, Example 6 is OAS, Example 7 is sensitivity. Replaced that ledger below.

Source-to-method coverage (coverage of methods, not reproduction of every question):
LOS a: 1,16,19,21,24; b: 2; c: 3–5,7; d–e: 6; f: 3–5; g–h: 7–8; i: 9–10; j: 12; k: 11,13–14; l: 15; m: 16–18; n: 19,21; o: 19–22; p: 22 plus backward-induction method in 4–5; q: 23.
Equations 1–2: 2; Equation 3: 9–11; Equation 4: 15; Equations 5–6: 17–18.
Examples 1–2: 1–3,6; Examples 3–4: 4–6 (including zero option value and put/extension equivalence); Example 5: 4–6; Example 6: 7–8; Example 7: 9–12,15; Example 8: 16–18; Example 9: 19–20,23.
Practice Q1: 1; Q2–3: 2,6,12,15; Q4: 4; Q5: 5; Q6–8: 6; Q9: 19; Q10: 20,23; Q11–13: 2,4,6,23; Q14: 2–4 (straight PV and exercise-now bound); Q15–16: 6; Q17: 3–4; Q18–19: 8; Q20–21: 12; Q22: 9; Q23: 17; Q24: 18; Q25: 22; Q26: 20; Q27: 23; Q28: 10; Q29: 12; Q30: 11; Q31: 14; Q32: 15; Q33: 21; Q34: 19; Q35: 22; Q36: 23.
Additional source points: sinking-fund acceleration/delivery p.123 -> 24; premium over straight value pp.170–171 -> 20; KRD Exhibits 23–25 -> 13–14. No new separate questions generated from these details.
Verification: 35 sections passed the local structural validator; math expressions parsed with KaTeX; 35 independent numerical assertions checked the retained calculations. Live Obsidian rendering was not checked.
No claim that all original entries were invalid or plagiarized. Question mining here means redundant splitting of one learning objective into multiple nominal variants; provenance beyond the local source comparison was not investigated.
-->
