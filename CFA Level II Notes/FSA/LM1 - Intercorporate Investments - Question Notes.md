## Variant: 1 — Choose the method before calculating income

**Abstract:** *Ownership percentage is a clue, not the verdict. Establish influence or control first; then decide whether income follows dividends, fair value changes, or the investee’s profit.*

> An investor owns 15% of a company, has board representation and demonstrably exercises significant influence without control. It paid EUR 300,000 on 1 January. The investee earns EUR 200,000 and distributes EUR 80,000 that year. There are no acquisition differences or other adjustments. Calculate equity income and the closing investment. Would passive-investment dividend accounting give the same income?

<span class="jargon-unlock">**Significant influence. What is it?** Participation in financial and operating decisions without directing them. **Equity method. What is it?** Record the investment at cost, then add your share of profit and subtract dividends received. **Carrying amount. What is it?** The value recorded on the balance sheet.</span>

**1. Follow the evidence of influence**

The 15% holding is below the usual 20% presumption, but the facts establish influence. The percentage does not overrule the relationship.

$$
\text{Equity income}=0.15(200{,}000)=\boxed{\text{EUR }30{,}000}
$$

**2. Separate earnings from distributions**

The investor receives EUR 12,000 in cash. This converts part of the investment into cash; it is not a second round of earnings.

$$
I_{\text{end}}=300{,}000+30{,}000-0.15(80{,}000)=\boxed{\text{EUR }318{,}000}
$$

Dividend-only income would be EUR 12,000, EUR 18,000 below equity income, before any applicable fair-value gains or losses.

> [!NOTE]
> Influence determines the method. Owning less than 20% does not automatically mean a passive financial asset.

*Source pattern: 2025 CFA Level II FSA, LM1, pp.4–5, 10–14; practice Q25. Inputs adapted unless stated.*

---

## Variant: 2 — Three debt categories, three carrying amounts

**Abstract:** *Fair-value categories use the current market price. Amortized cost follows the effective-interest schedule, even when market prices wander away.*

> Three IFRS debt investments were bought at par. At year-end, A has cost EUR 100,000 and fair value EUR 108,000 and is FVPL; B has cost EUR 200,000 and fair value EUR 190,000 and is FVOCI; C has cost EUR 300,000 and fair value EUR 315,000 and is amortized cost. Assume no credit impairment, transaction costs, or unpaid interest. Find total carrying value and the difference if C had been FVPL from purchase.

<span class="jargon-unlock">**IFRS. What is it?** International Financial Reporting Standards. **FVPL and FVOCI. What are they?** Fair value through profit or loss and fair value through other comprehensive income. **OCI. What is it?** Specified gains and losses recorded outside current profit but within comprehensive income. **Amortized cost. What is it?** Cost adjusted for principal repayments and effective-interest amortization; for these par purchases it remains par.</span>

**1. Apply each category separately**

A and B use market values. C stays at EUR 300,000 under the stated par-purchase assumptions.

$$
\text{Portfolio carrying value}=108{,}000+190{,}000+300{,}000=\boxed{\text{EUR }598{,}000}
$$

**2. Change C’s measurement basis**

If C had been FVPL, it would be measured at EUR 315,000.

$$
\text{Alternative total}=108{,}000+190{,}000+315{,}000=\boxed{\text{EUR }613{,}000}
$$

The difference is EUR 15,000. Moving B between FVOCI and FVPL would change where its gain or loss appears, not its year-end asset value.

> [!NOTE]
> “Amortized cost equals purchase cost” works here because the bonds were bought at par. It is not the general rule for premium or discount bonds.

*Source pattern: 2025 CFA Level II FSA, LM1, pp.6–10; practice Q1–2. Inputs adapted unless stated.*

---

## Variant: 3 — This year’s gain versus the gain since purchase

**Abstract:** *Current-year profit uses the change since the last reporting date. Cumulative OCI compares current fair value with the relevant amortized-cost baseline.*

> A par bond cost EUR 100,000, pays an annual coupon of EUR 5,000, and had fair values EUR 108,000 at the end of Year 1 and EUR 103,000 at the end of Year 2. Ignore tax and impairment. Calculate Year 2 investment-related profit under FVPL and under debt FVOCI. For FVOCI, find Year 2 OCI and cumulative OCI.

<span class="jargon-unlock">**Coupon. What is it?** Cash interest paid by a bond. **FVPL. What is it?** Fair value measurement with valuation changes in profit. **Debt FVOCI. What is it?** Fair value measurement with the specified valuation changes outside profit; effective interest still enters profit. **Cumulative OCI. What is it?** The accumulated balance of those OCI movements.</span>

**1. Measure the Year 2 price movement**

The bond is above purchase cost but fell during Year 2. “Still ahead” and “made money this year” are different claims.

$$
\Delta FV_2=103{,}000-108{,}000=\boxed{-\text{EUR }5{,}000}
$$

**2. Put that movement in the correct place**

Because the bond was bought at par, interest income equals the coupon.

$$
\begin{aligned}
\text{FVPL profit}_2&=5{,}000-5{,}000=\boxed{0}\\
\text{FVOCI profit}_2&=\boxed{\text{EUR }5{,}000}\\
OCI_2&=\boxed{-\text{EUR }5{,}000}\\
\text{Cumulative OCI}_2&=103{,}000-100{,}000=\boxed{\text{EUR }3{,}000}
\end{aligned}
$$

Both treatments produce zero Year 2 comprehensive income from this bond: classification moves the price loss between columns.

> [!NOTE]
> Current-year gain is ending minus beginning fair value, not ending fair value minus original cost.

*Source pattern: 2025 CFA Level II FSA, LM1, pp.7–10; practice Q3–4. Inputs adapted unless stated.*

---

## Variant: 4 — Premium bond: cash interest exceeds interest income

**Abstract:** *Use beginning carrying value times the effective yield for income. The coupon uses par value; their difference amortizes the premium.*

> A bond with EUR 1,000,000 par and a 5% annual coupon is purchased for EUR 1,100,000. Its effective annual yield is 4%. It qualifies for amortized-cost measurement. Find Year 1 and Year 2 interest income and closing carrying values, assuming annual year-end coupons, no impairment, and no principal repayment.

<span class="jargon-unlock">**Par. What is it?** Principal repaid at maturity. **Premium. What is it?** Purchase price above par. **Effective interest. What is it?** $J_t=B_{t-1}y$, where $J_t$ is period interest income, $B_{t-1}$ opening carrying value, and $y$ the original effective yield. Closing carrying value is opening value plus interest income minus cash coupon.</span>

**1. Keep the two interest calculations separate**

Cash coupon is $1{,}000{,}000(5\%)=50{,}000$. Year 1 income is based on the price paid, not par.

$$
J_1=1{,}100{,}000(0.04)=\boxed{44{,}000},\qquad B_1=1{,}100{,}000+44{,}000-50{,}000=\boxed{1{,}094{,}000}
$$

**2. Use the new opening balance next year**

The effective yield stays 4%, but the amount earning that yield has fallen.

$$
J_2=1{,}094{,}000(0.04)=\boxed{43{,}760},\qquad B_2=1{,}094{,}000+43{,}760-50{,}000=\boxed{1{,}087{,}760}
$$

All amounts are EUR. The premium shrinks by EUR 6,000 and then EUR 6,240. Part of each coupon is recovery of the extra purchase price, not fresh income.

> [!NOTE]
> Premium bond: coupon exceeds effective-interest income and carrying value declines toward par. A market-price increase does not change this schedule.

*Source pattern: 2025 CFA Level II FSA, LM1, practice Q5, Q22 and solutions pp.58–59. Inputs adapted unless stated.*

---

## Variant: 5 — Discount bond and an implied effective yield

**Abstract:** *A discount bond earns more accounting interest than the cash coupon. Reverse the carrying-value bridge to recover a missing yield.*

> A bond has opening amortized cost EUR 950,000, par EUR 1,000,000, and annual coupon rate 3%. Its original effective yield is 4%. Find interest income and closing carrying amount. Independently, an analyst sees opening value EUR 950,000, closing value EUR 958,000 and coupon EUR 30,000; infer the yield. Ignore impairment and principal repayments.

<span class="jargon-unlock">**Discount bond. What is it?** A bond bought below par. **Effective yield. What is it?** The acquisition-date return used for amortized-cost interest. With opening balance $B_0$, closing balance $B_1$, coupon $C$ and yield $y$, $B_1=B_0+B_0y-C$.</span>

**1. Calculate income and cash separately**

Interest accrues on EUR 950,000, while the coupon is based on EUR 1,000,000 par.

$$
J=950{,}000(0.04)=\boxed{38{,}000},\qquad B_1=950{,}000+38{,}000-30{,}000=\boxed{958{,}000}
$$

**2. Solve backward from the balance change**

The EUR 8,000 increase plus the EUR 30,000 cash payment must equal income earned.

$$
y=\frac{B_1-B_0+C}{B_0}=\frac{958{,}000-950{,}000+30{,}000}{950{,}000}=\boxed{4\%}
$$

All amounts are EUR. The asset grows toward par because some of the investor’s return is earned through the discount closing, rather than through coupons.

> [!NOTE]
> Reconcile opening value + income − cash = closing value before guessing which interest rate belongs where.

*Source pattern: 2025 CFA Level II FSA, LM1, effective-interest relationship in practice Q5 and Q22; inverse and discount case. Inputs adapted unless stated.*

---

## Variant: 6 — Debt reclassification without rewriting history

**Abstract:** *When a qualifying business-model change permits reclassification, use the required measurement at that date. Do not restate previous periods.*

> Following a genuine IFRS business-model change, Bond A is reclassified from amortized cost EUR 96,000 to FVPL when fair value is EUR 101,000. Separately, Bond B moves from FVPL to amortized cost when its fair value is EUR 88,000; original purchase cost was EUR 100,000. Ignore impairment and tax. Calculate A’s reclassification gain and B’s new carrying basis.

<span class="jargon-unlock">**Reclassification. What is it?** Moving an investment between accounting measurement categories. **Business model. What is it?** How the entity manages assets to collect cash flows and/or sell them. **FVPL. What is it?** Fair value through profit or loss. **Carrying basis. What is it?** The amount from which subsequent accounting starts.</span>

**1. Bring A to fair value**

A was measured below its current market value. On this reclassification, the difference goes into profit.

$$
\text{Gain}_A=101{,}000-96{,}000=\boxed{\text{EUR }5{,}000}
$$

**2. Start B’s new schedule at its reclassification-date value**

Original cost does not return merely because the accounting label changes.

$$
B_{\text{new basis}}=\boxed{\text{EUR }88{,}000}
$$

Earlier FVPL losses remain in the periods where they were recognized. There is no EUR 12,000 restoration to original cost.

> [!NOTE]
> IFRS debt reclassification requires a qualifying business-model change. Equity FVPL/FVOCI elections are not a mechanism for moving losses out of profit later.

*Source pattern: 2025 CFA Level II FSA, LM1, p.9. Inputs adapted unless stated.*

---

## Variant: 7 — Passive equity: dividends and fair-value changes

**Abstract:** *For eligible IFRS equity designated FVOCI, ordinary dividends enter profit while fair-value changes enter OCI. A trading equity investment instead uses FVPL.*

> An IFRS investor buys a passive, non-trading equity investment for EUR 80,000 and validly elects FVOCI at acquisition. It receives EUR 3,000 of ordinary dividends representing a return on investment; year-end fair value is EUR 92,000. Calculate carrying value, profit, and OCI. Compare with FVPL. Assume no tax or transaction costs and no sale.

<span class="jargon-unlock">**Passive equity. What is it?** A shareholding without significant influence or control. **FVOCI. What is it?** Fair value through other comprehensive income, elected irrevocably for eligible non-trading equity. **FVPL. What is it?** Fair value through profit or loss. **Dividend. What is it?** Cash distributed by the investee to shareholders.</span>

**1. Measure the same asset at the same fair value**

Both methods record EUR 92,000. They differ in where the EUR 12,000 increase is reported.

$$
\begin{aligned}
\text{FVOCI profit}&=\boxed{\text{EUR }3{,}000}\\
\text{FVOCI OCI}&=92{,}000-80{,}000=\boxed{\text{EUR }12{,}000}\\
\text{FVPL profit}&=3{,}000+12{,}000=\boxed{\text{EUR }15{,}000}
\end{aligned}
$$

**2. Reconcile total comprehensive income**

FVOCI gives $3{,}000+12{,}000=15{,}000$; FVPL gives EUR 15,000 entirely in profit. The label changes the income presentation, not the investment’s market gain.

> [!NOTE]
> This is IFRS passive-equity accounting. Do not apply equity-method dividend reductions or assume the same FVOCI election exists for ordinary US GAAP equity investments.

*Source pattern: 2025 CFA Level II FSA, LM1, pp.6–9. Inputs adapted unless stated.*

---

## Variant: 8 — Equity method over several years

**Abstract:** *Accumulate your share of post-acquisition profits, then subtract your share of dividends. Dividends move value into cash rather than creating more profit.*

> On 1 January Year 1 an investor purchases 30% of an associate for EUR 300,000, equal to its share of book and fair net assets. Associate profits in Years 1–3 are EUR 100,000, EUR 150,000, and EUR 200,000; total dividends are EUR 20,000, EUR 50,000, and EUR 80,000. No other changes occur. Find annual equity income and the ending investment each year.

<span class="jargon-unlock">**Associate. What is it?** An investee over which the investor has significant influence without control. **Equity income. What is it?** The investor’s adjusted share of associate profit. **Rollforward. What is it?** A bridge from opening to closing balance: $I_1=I_0+pN-pD$, where $I$ is carrying amount, $p$ ownership, $N$ associate profit and $D$ its total dividends.</span>

**1. Recognize the profits as earned**

Multiply each year’s profit by 30%.

$$
\text{Annual equity income}=\boxed{30{,}000;\ 45{,}000;\ 60{,}000\text{ EUR}}
$$

**2. Subtract the distributions from the investment**

Cash receipts are EUR 6,000, EUR 15,000, and EUR 24,000.

$$
\begin{aligned}
I_1&=300{,}000+30{,}000-6{,}000=\boxed{324{,}000}\\
I_2&=324{,}000+45{,}000-15{,}000=\boxed{354{,}000}\\
I_3&=354{,}000+60{,}000-24{,}000=\boxed{390{,}000}
\end{aligned}
$$

All balances are EUR. The cumulative check is $300{,}000+0.30(450{,}000-150{,}000)=390{,}000$.

> [!NOTE]
> Equity income follows profit, not dividends. Adding dividends to both cash and income would count the same earnings twice.

*Source pattern: 2025 CFA Level II FSA, LM1, Example 1, p.12. Inputs adapted unless stated.*

---

## Variant: 9 — Solve backward for dividends or associate profit

**Abstract:** *The equity-method bridge works backward too. First isolate the investor’s cash receipt, then divide by ownership if the question asks for total associate dividends.*

> An investor owns 25% of an associate. Opening investment is EUR 500,000, closing investment EUR 520,000, and recognized equity income EUR 40,000. There are no other investment movements. Find dividends received and total dividends paid by the associate. Equity income includes a EUR 5,000 acquisition-basis amortization deduction; infer the associate’s reported profit.

<span class="jargon-unlock">**Acquisition-basis amortization. What is it?** Extra expense reflecting the investor’s purchase-date fair-value adjustments. **Equity-method bridge. What is it?** Closing investment equals opening investment plus recognized equity income minus dividends received. **Reported profit. What is it?** The associate’s own profit before the investor’s acquisition-basis adjustment.</span>

**1. Find the cash that left the investment balance**

Without dividends the balance would have risen to EUR 540,000. It ended EUR 20,000 lower.

$$
D_{\text{received}}=500{,}000+40{,}000-520{,}000=\boxed{\text{EUR }20{,}000}
$$

**2. Undo the ownership fraction and amortization**

The EUR 20,000 belongs to the 25% owner. The EUR 5,000 adjustment must be restored before inferring the investee’s full profit.

$$
D_{\text{total}}=\frac{20{,}000}{0.25}=\boxed{80{,}000},\qquad N=\frac{40{,}000+5{,}000}{0.25}=\boxed{180{,}000}
$$

All amounts are EUR. Check: 25% of EUR 180,000 minus EUR 5,000 gives the reported EUR 40,000 equity income.

> [!NOTE]
> Determine whether an adjustment is already the investor’s share. Do not multiply a supplied investor-level amortization amount by ownership again.

*Source pattern: 2025 CFA Level II FSA, LM1, Examples 1–3, pp.12–18; algebraic inverses. Inputs adapted unless stated.*

---

## Variant: 10 — Losses stop at zero, but the loss ledger continues

**Abstract:** *Without additional obligations, stop recognizing equity-method losses at zero. Later profits first absorb unrecognized losses before income recognition resumes.*

> An investor’s associate balance is EUR 30,000. Its share of associate losses in Year 1 is EUR 50,000; its share of profits in Years 2 and 3 is EUR 12,000 and EUR 15,000. It has no guarantees, funding obligations, other interests or dividends. Calculate recognized income or loss, closing carrying amount, and unrecognized losses each year.

<span class="jargon-unlock">**Unrecognized losses. What are they?** The investor’s share of losses that exceeds the amount it can recognize under the stated zero-balance limit. **Resumption. What does it mean?** Recognizing profits only after previously unrecognized losses have been recovered. The supplied profit and loss amounts are already the investor’s share.</span>

**1. Exhaust the investment, not an imaginary liability**

Year 1 can reduce the asset by only EUR 30,000.

$$
\text{Year 1 loss recognized}=\boxed{30{,}000},\qquad I_1=\boxed{0},\qquad U_1=50{,}000-30{,}000=\boxed{20{,}000}
$$

**2. Use recovery profits to clear the backlog**

Year 2’s EUR 12,000 reduces unrecognized losses to EUR 8,000; recognized income and the investment stay zero. Year 3 clears that EUR 8,000 first.

$$
\text{Year 3 income}=15{,}000-8{,}000=\boxed{\text{EUR }7{,}000},\qquad I_3=\boxed{\text{EUR }7{,}000}
$$

Cumulative recognized loss is EUR 23,000, equal to the original EUR 30,000 asset less its EUR 7,000 ending value. Suspension postpones recognition; it does not erase the losses from memory.

> [!NOTE]
> This zero-floor case assumes no additional loss obligations or relevant other interests. Do not restart income at the first positive year automatically.

*Source pattern: 2025 CFA Level II FSA, LM1, p.12. Inputs adapted unless stated.*

---

## Variant: 11 — Allocate excess purchase price before calling it goodwill

**Abstract:** *Compare price with your share of fair-value net assets, not just book equity. Identifiable asset uplifts explain part of the excess; goodwill is the remainder.*

> An investor pays EUR 150,000 for 30% of an associate. Its book net assets are EUR 300,000. Equipment is worth EUR 60,000 above book and land EUR 40,000 above book; all other values match. Equipment has 10 years remaining, straight-line depreciation, no residual value. Ignore tax. Find excess over book, embedded goodwill, and annual extra depreciation.

<span class="jargon-unlock">**Net assets. What are they?** Assets minus liabilities. **Fair-value uplift. What is it?** Acquisition-date fair value above the recorded amount. **Goodwill. What is it?** Acquisition cost remaining after allocating the investor’s share of identifiable fair net assets. Under the equity method it stays inside the single investment asset.</span>

**1. Split the excess into identifiable pieces**

The purchase is EUR 60,000 above the investor’s share of book equity, but not all of that is goodwill.

$$
\begin{aligned}
\text{Excess over book}&=150{,}000-0.30(300{,}000)=\boxed{60{,}000}\\
\text{Investor’s identifiable uplift}&=0.30(60{,}000+40{,}000)=\boxed{30{,}000}\\
\text{Goodwill}&=60{,}000-30{,}000=\boxed{30{,}000}
\end{aligned}
$$

**2. Depreciate only the equipment uplift**

Land and goodwill are not systematically amortized in this case.

$$
\text{Annual adjustment}=\frac{0.30(60{,}000)}{10}=\boxed{\text{EUR }1{,}800}
$$

All other amounts above are EUR. Calling the whole EUR 60,000 goodwill would skip a real annual expense and overstate future equity income.

> [!NOTE]
> First allocate excess to identifiable assets and liabilities. Only the residual is goodwill; goodwill is not a separate equity-method balance-sheet line.

*Source pattern: 2025 CFA Level II FSA, LM1, Example 2, pp.16–17. Inputs adapted unless stated.*

---

## Variant: 12 — Inventory uplift, equipment uplift, and a carrying-value checksum

**Abstract:** *Expense acquisition differences when the related assets are consumed. Inventory uplift is released when sold; equipment uplift is depreciated over its remaining life.*

> An investor pays EUR 240,000 for 40% of an associate with book net assets EUR 400,000. At acquisition, inventory is undervalued by EUR 20,000, equipment by EUR 80,000, and land by EUR 50,000. All inventory sells in Year 1; equipment has 8 years remaining. Associate Year 1 profit is EUR 100,000 and dividends EUR 30,000. Ignore tax and other changes. Find equity income and closing investment.

<span class="jargon-unlock">**Equity income. What is it?** Ownership share of reported associate earnings after purchase-basis adjustments. **Unamortized excess. What is it?** Original price above share of book net assets that has not yet been expensed. **Checksum. What does it mean?** A second calculation that should give the same result.</span>

**1. Work out the annual deductions**

Fair net assets are EUR 550,000, so embedded goodwill is $240{,}000-0.40(550{,}000)=20{,}000$. Inventory adjustment is EUR 8,000; equipment adjustment is EUR 4,000.

$$
\text{Equity income}=0.40(100{,}000)-8{,}000-4{,}000=\boxed{\text{EUR }28{,}000}
$$

**2. Roll forward the investment**

Dividends received are EUR 12,000.

$$
I_1=240{,}000+28{,}000-12{,}000=\boxed{\text{EUR }256{,}000}
$$

**3. Rebuild the same balance from underlying net assets**

Ending book net assets are EUR 470,000. Original excess over book was EUR 80,000; EUR 12,000 has been expensed.

$$
0.40(470{,}000)+(80{,}000-12{,}000)=\boxed{\text{EUR }256{,}000}
$$

> [!NOTE]
> The associate’s reported profit does not contain the investor’s purchase-price adjustments. Add the remaining excess once, not ownership times the excess again.

*Source pattern: 2025 CFA Level II FSA, LM1, Example 3, pp.17–18; asset-consumption rule pp.16–17. Inputs adapted unless stated.*

---

## Variant: 13 — The 15% associate: the corrected one-year case

**Abstract:** *A small stake can still use the equity method. Separate goodwill from the depreciable uplift and use only earnings after the acquisition date.*

> On 1 January 2016 an investor pays USD 300m for a 15% associate interest with significant influence. Investee book net assets are USD 1,340m; equipment fair value exceeds book by USD 260m and has 10 years remaining. Other values match. During 2016 the associate earns USD 360m and pays USD 220m dividends. Ignore tax and other changes. Find goodwill, equity income and the investment at 31 December 2016.

<span class="jargon-unlock">**Associate. What is it?** An investment with significant influence, even below a 20% ownership presumption. **Embedded goodwill. What is it?** Purchase price minus ownership share of fair identifiable net assets. **Extra depreciation. What is it?** The investor’s equipment uplift spread over the remaining useful life. Here m means million.</span>

**1. Allocate the purchase price**

Fair net assets are $1{,}340+260=1{,}600$ million.

$$
G=300-0.15(1{,}600)=\boxed{\text{USD }60\text{m}},\qquad a=\frac{0.15(260)}{10}=\boxed{\text{USD }3.9\text{m}}
$$

**2. Recognize one year’s adjusted profit and dividends**

The supplied figures concern 2016, not three years of operations.

$$
\begin{aligned}
\text{Equity income}&=0.15(360)-3.9=\boxed{\text{USD }50.1\text{m}}\\
I_{2016}&=300+50.1-0.15(220)=\boxed{\text{USD }317.1\text{m}}
\end{aligned}
$$

The investment increases by USD 17.1m because adjusted earnings exceed dividends received.

> [!NOTE]
> Official errata change practice Q26 and its solution from “end of 2018” to “end of 2016.” The supplied data support a one-year calculation.

*Source pattern: 2025 CFA Level II FSA, LM1, practice Q24–26, pp.53–54 and 60–61; official 2025 errata. Original numerical inputs retained. Inputs adapted unless stated.*

---

## Variant: 14 — Upstream associate sale: remove your share of unsold profit

**Abstract:** *When the associate sells to the investor, its profit already includes the sale. Remove the investor’s share of profit still trapped in unsold inventory.*

> An investor owns 25% of an associate. Opening investment is EUR 200,000. Associate profit is EUR 80,000, including EUR 12,000 profit on goods sold to the investor and still entirely unsold outside the group relationship. Investor-level extra depreciation is EUR 2,000; total associate dividends are EUR 16,000. Ignore taxes. Find equity income and closing investment.

<span class="jargon-unlock">**Upstream sale. What is it?** A sale from associate to investor. **Unrealized intercompany profit. What is it?** Profit on goods not yet sold onward to an outside customer. Under the equity method, defer only the investor’s ownership share of this profit. **Investor-level adjustment. What does it mean?** An amount already scaled for ownership.</span>

**1. Remove profit not yet confirmed externally**

The investor’s share of the associate’s stated earnings is EUR 20,000. The EUR 12,000 inventory profit is not yet fully earned from the investor’s accounting perspective.

$$
\text{Equity income}=0.25(80{,}000)-2{,}000-0.25(12{,}000)=\boxed{\text{EUR }15{,}000}
$$

**2. Update the investment balance**

Dividends received are 25% of EUR 16,000, or EUR 4,000.

$$
I_1=200{,}000+15{,}000-4{,}000=\boxed{\text{EUR }211{,}000}
$$

If the goods were already sold externally, the EUR 3,000 deferral would be unnecessary. Moving inventory across related desks is not the same as selling it to a customer.

> [!NOTE]
> Equity method: eliminate ownership share × unrealized profit. Do not eliminate the entire sale price or the full associate profit.

*Source pattern: 2025 CFA Level II FSA, LM1, Example 4, pp.20–21. Inputs adapted unless stated.*

---

## Variant: 15 — Downstream associate sale: defer now, release later

**Abstract:** *For investor-to-associate sales, defer the ownership share of unrealized profit. Add that exact deferred amount back when the associate sells the goods outside.*

> An investor owns 30% of an associate and sells inventory costing EUR 60,000 to it for EUR 100,000 in Year 1. At year-end 25% of those goods remain unsold, measured at transfer-price cost. They all sell externally in Year 2. Associate profits are EUR 200,000 and EUR 220,000; investor-level extra amortization is EUR 5,000 each year. No new intercompany sales occur. Ignore taxes. Find equity income each year.

<span class="jargon-unlock">**Downstream sale. What is it?** Investor sells to associate. **Deferred profit. What is it?** The ownership share of profit on goods still held by the associate. The module presents the deferral and later release as adjustments to equity income. **Amortization. What is it?** Allocation of a finite-lived purchase-basis difference over time.</span>

**1. Find the profit still inside the relationship**

Total sale profit is EUR 40,000. One quarter remains unrealized; only 30% of that is deferred by this investor.

$$
D=0.30(100{,}000-60{,}000)(0.25)=\boxed{\text{EUR }3{,}000}
$$

**2. Match recognition to external sale**

Subtract the deferral in Year 1 and release it in Year 2.

$$
\begin{aligned}
EI_1&=0.30(200{,}000)-5{,}000-3{,}000=\boxed{\text{EUR }52{,}000}\\
EI_2&=0.30(220{,}000)-5{,}000+3{,}000=\boxed{\text{EUR }64{,}000}
\end{aligned}
$$

The two-year total is EUR 116,000, also $0.30(420{,}000)-10{,}000$. Deferral changes timing, not the lifetime profit after external sale.

> [!NOTE]
> Release the amount previously deferred, not ownership times that amount again. “Goods resold” must specify quantity or transfer-price cost, not ambiguous customer revenue.

*Source pattern: 2025 CFA Level II FSA, LM1, Example 5, pp.21–22. Inputs adapted unless stated.*

---

## Variant: 16 — Inventory margin is not markup

**Abstract:** *When ending inventory is quoted at transfer price, multiply it by the seller’s profit margin on sales. Markup on cost has a different denominator.*

> An investor owns 40% of an associate. It sells goods with cost EUR 80,000 for EUR 100,000. At year-end the associate holds EUR 30,000 of those goods measured at the transfer price. Calculate the unrealized profit and equity-method deferral. An analyst instead applies a 25% markup to the EUR 30,000: quantify the resulting overstatement of deferral. Ignore tax.

<span class="jargon-unlock">**Profit margin. What is it?** Profit divided by sales price. **Markup. What is it?** Profit divided by original cost. **Transfer price. What is it?** The price charged between investor and associate. **Deferral. What is it?** Profit recognition postponed until external sale; under the equity method use the investor’s share.</span>

**1. Match the percentage to the inventory’s measurement basis**

Profit is EUR 20,000: a 20% sales margin but a 25% markup on cost. Ending inventory is stated at the sales price.

$$
U=30{,}000\left(\frac{20{,}000}{100{,}000}\right)=\boxed{\text{EUR }6{,}000},\qquad D=0.40(6{,}000)=\boxed{\text{EUR }2{,}400}
$$

**2. Diagnose the wrong denominator**

Using 25% would produce a EUR 3,000 deferral.

$$
\text{Overstatement}=0.40(30{,}000)(0.25-0.20)=\boxed{\text{EUR }600}
$$

A percentage without its denominator is an instruction with the address torn off.

> [!NOTE]
> Transfer-price inventory × profit/sales × ownership gives the equity-method deferral. Convert markup to margin before using it on a sales-price amount.

*Source pattern: 2025 CFA Level II FSA, LM1, Example 5 alternative calculation, p.22. Inputs adapted unless stated.*

---

## Variant: 17 — Fair-value option versus equity method

**Abstract:** *The fair-value option uses market changes and dividends in profit. The equity method uses adjusted investee earnings and treats dividends as a reduction of the investment.*

> An eligible investment entity buys 30% of an associate for EUR 500,000. Under the equity method, its share of profit would be EUR 60,000 and annual acquisition-basis amortization EUR 6,000. Dividends received are EUR 15,000; year-end fair value of the stake is EUR 560,000. Assume the entity can validly elect the fair-value option on initial recognition. Compare income and closing investment under the two methods.

<span class="jargon-unlock">**Fair-value option. What is it?** An eligible irrevocable election at initial recognition to measure the investment at fair value through profit or loss. **Equity method. What is it?** Cost adjusted for the investor’s share of earnings, acquisition-basis expenses, and distributions. **Eligibility. What does it mean here?** The election is permitted for this entity; the source restricts it to specified investment-type entities under IFRS.</span>

**1. Use earnings under the equity method**

The acquisition-basis adjustment reduces the investor’s EUR 60,000 share.

$$
EI=60{,}000-6{,}000=\boxed{54{,}000},\qquad I_1=500{,}000+54{,}000-15{,}000=\boxed{539{,}000}
$$

**2. Use fair value under the elected option**

There is no separate equity-income share or purchase-uplift amortization in this route.

$$
\text{Profit}=560{,}000-500{,}000+15{,}000=\boxed{75{,}000},\qquad I_1=\boxed{560{,}000}
$$

All amounts are EUR. The option produces EUR 21,000 more profit and EUR 21,000 more carrying value here; a market decline could reverse the comparison.

> [!NOTE]
> Do not combine fair-value gains with equity-method income. These are alternative measurement models, not ingredients to add together.

*Source pattern: 2025 CFA Level II FSA, LM1, pp.18–19. Inputs adapted unless stated.*

---

## Variant: 18 — Associate impairment and the reversal ceiling

**Abstract:** *Test the whole equity-method investment, including embedded goodwill. Under IFRS use recoverable amount; a later reversal cannot exceed the balance that would exist without impairment.*

> An associate investment has carrying value EUR 500,000 and objective impairment evidence. Value in use is EUR 420,000; fair value less selling costs is EUR 390,000; fair value itself is EUR 400,000. For US GAAP assume the decline meets the source’s impairment criterion. Find the loss under each framework. One year later IFRS recoverable amount is EUR 530,000, and the no-impairment carrying amount would be EUR 510,000; the actual pre-reversal balance is EUR 430,000. Find the IFRS reversal.

<span class="jargon-unlock">**Recoverable amount. What is it?** The higher of value in use and fair value less disposal costs. **Value in use. What is it?** Present value of expected cash flows. **Impairment. What is it?** A write-down when the relevant recoverable measure falls below carrying value. **Reversal ceiling. What is it?** The carrying amount that would have existed without the original write-down.</span>

**1. Apply the specified measurement rule**

IFRS uses the better recovery route; the source’s US equity-method case writes to fair value once impairment is required.

$$
\begin{aligned}
R&=\max(420{,}000,390{,}000)=420{,}000\\
L_{\text{IFRS}}&=500{,}000-420{,}000=\boxed{80{,}000}\\
L_{\text{US}}&=500{,}000-400{,}000=\boxed{100{,}000}
\end{aligned}
$$

**2. Cap the IFRS recovery**

The permitted endpoint is the lower of recoverable amount and the no-impairment balance.

$$
\text{Reversal}=\min(530{,}000,510{,}000)-430{,}000=\boxed{\text{EUR }80{,}000}
$$

The source prohibits US GAAP reversals for these equity-method write-downs. IFRS does not permit restoring the investment beyond its otherwise applicable carrying amount.

> [!NOTE]
> This tests an associate investment as one asset. Do not confuse it with separately recognized subsidiary goodwill, whose impairment is not reversed.

*Source pattern: 2025 CFA Level II FSA, LM1, pp.13 and 19. Inputs adapted unless stated.*

---

## Variant: 19 — Share-financed acquisition: build the consolidated balance sheet

**Abstract:** *Use the market value of shares issued as consideration. Combine the parent’s existing book amounts with the subsidiary’s identifiable fair values, then add goodwill.*

> Before acquisition, Parent has assets EUR 20m, liabilities EUR 8m, share capital EUR 2m, share premium EUR 3m, and retained earnings EUR 7m. It buys 100% of Target by issuing 1m shares with par EUR 1 and market price EUR 6 each. Target’s identifiable fair-value assets are EUR 9m and liabilities EUR 4m. Ignore tax and fees. Find goodwill and the consolidated balance sheet totals and equity components.

<span class="jargon-unlock">**Consideration. What is it?** Value paid for the acquisition, here market value of issued shares. **Share premium. What is it?** Share issue proceeds above nominal or par capital. **Goodwill. What is it?** Consideration minus fair identifiable net assets in a 100% purchase. **Consolidation. What is it?** Reporting controlled entities as one economic group. Here m means million.</span>

**1. Price the transaction at market, not par**

Consideration is EUR 6m. Target net assets are EUR 5m.

$$
G=6-(9-4)=\boxed{\text{EUR }1\text{m}}
$$

**2. Combine assets and liabilities**

No cash was paid. The parent’s investment account is replaced by Target’s assets, liabilities and goodwill in consolidation.

$$
A=20+9+1=\boxed{30\text{m}},\qquad L=8+4=\boxed{12\text{m}},\qquad E=\boxed{18\text{m}}
$$

**3. Reconcile equity**

Share capital becomes EUR 3m; share premium becomes EUR 8m; retained earnings stay EUR 7m. Their sum is EUR 18m, and $30=12+18$.

> [!NOTE]
> Do not add the target’s old share capital or retained earnings. Parent share issuance increases consolidated equity; buying shares for cash does not.

*Source pattern: 2025 CFA Level II FSA, LM1, Example 7, pp.28–30. Inputs adapted unless stated.*

---

## Variant: 20 — Cash acquisition: avoid subtracting the payment twice

**Abstract:** *Check whether the supplied parent balance sheet is before or after payment. Consolidation removes the investment account; it does not pay the seller again.*

> Parent starts with assets EUR 20m, including sufficient cash, liabilities EUR 8m, and equity EUR 12m. It pays EUR 6m cash for all of Target. Target’s identifiable fair assets are EUR 9m and liabilities EUR 4m. No tax or fees apply. Calculate consolidated assets from the pre-purchase balance sheet. Then show the equivalent calculation from Parent’s post-purchase separate balance sheet, which contains a EUR 6m investment.

<span class="jargon-unlock">**Separate balance sheet. What is it?** The parent entity’s own accounts, containing an investment asset. **Consolidated balance sheet. What is it?** Group accounts replacing that investment with the controlled business’s assets and liabilities. **Goodwill. What is it?** Purchase consideration above identifiable fair net assets.</span>

**1. Start before the cash payment**

Goodwill is $6-(9-4)=1$ million. Cash leaves the group and Target’s assets enter it.

$$
A_{\text{group}}=20-6+9+1=\boxed{\text{EUR }24\text{m}}
$$

**2. Start after the cash payment instead**

Parent’s separate total assets are still EUR 20m: it exchanged EUR 6m cash for a EUR 6m investment. Remove that investment, not another cash payment.

$$
A_{\text{group}}=20-\underbrace{6}_{\text{investment}}+9+1=\boxed{\text{EUR }24\text{m}}
$$

Group liabilities are EUR 12m and equity EUR 12m. The balance sheet checks: $24=12+12$. The cash payment does not create an expense at acquisition.

> [!NOTE]
> “Before payment” requires subtracting cash; “after payment, investment included” requires eliminating the investment. Do not do both.

*Source pattern: 2025 CFA Level II FSA, LM1, acquisition process pp.26–30; practice Q29–34 balance-sheet setup. Inputs adapted unless stated.*

---

## Variant: 21 — Consideration, fees, and later contingent payments

**Abstract:** *Include acquisition-date fair value of contingent consideration in the purchase price. Expense advisory costs; remeasure liability-classified contingent consideration through later profit.*

> A buyer acquires 100% of a business for EUR 8m cash plus liability-classified contingent consideration with acquisition-date fair value EUR 1m. Identifiable fair net assets are EUR 7m. Legal and valuation fees are EUR 0.3m. An uncommitted restructuring plan would cost EUR 0.5m. Later, after the measurement period, the contingent liability rises to EUR 1.4m due to new performance expectations. Ignore tax. Find goodwill and the separate profit effects.

<span class="jargon-unlock">**Contingent consideration. What is it?** An additional purchase payment depending on future events. **Acquisition-date fair value. What is it?** Its measured value when control is obtained. **Measurement period. What is it?** The limited period for completing acquisition-date estimates; the later change here is explicitly outside it and reflects new events.</span>

**1. Separate the purchase from the costs of arranging it**

The seller receives cash plus a claim to possible future payments. The advisers’ invoice is an expense, not another acquired asset.

$$
G=(8+1)-7=\boxed{\text{EUR }2\text{m}},\qquad \text{Fee expense}=\boxed{\text{EUR }0.3\text{m}}
$$

The uncommitted EUR 0.5m restructuring plan creates no acquisition-date liability or goodwill adjustment in this case.

**2. Remeasure the later liability**

The increased expected payment is a subsequent loss.

$$
\text{Later loss}=1.4-1.0=\boxed{\text{EUR }0.4\text{m}}
$$

If the contingent consideration were equity-classified, the source says it would not be remeasured this way.

> [!NOTE]
> Purchase consideration, deal expenses, and later operating plans are different accounting items. Do not place all acquisition-related spending inside goodwill.

*Source pattern: 2025 CFA Level II FSA, LM1, pp.26–28 and 43–44. Inputs adapted unless stated.*

---

## Variant: 22 — Bargain purchase: the residual is a gain, not negative goodwill

**Abstract:** *After checking the acquisition measurements, consideration below fair identifiable net assets creates a bargain-purchase gain.*

> A buyer pays EUR 4m cash plus EUR 0.2m acquisition-date fair value of contingent consideration for 100% of a business. Identifiable assets have fair value EUR 7m and liabilities EUR 2m. All measurements have been reassessed and confirmed. Ignore tax and fees. Calculate goodwill or bargain-purchase gain, and explain its immediate effect on group profit and equity.

<span class="jargon-unlock">**Bargain purchase. What is it?** A business acquired for less than the fair value of identifiable net assets after required measurement checks. **Net assets. What are they?** Assets minus liabilities. **Goodwill. What is it?** A positive residual purchase amount; a confirmed negative residual is recognized as a gain instead.</span>

**1. Compare total consideration with net assets**

Include the contingent payment even though it is not all paid in cash today.

$$
\text{Net assets}=7-2=\boxed{\text{EUR }5\text{m}},\qquad \text{Consideration}=4+0.2=\boxed{\text{EUR }4.2\text{m}}
$$

**2. Recognize the confirmed bargain**

The group acquires EUR 5m of identifiable net assets for EUR 4.2m of consideration.

$$
\text{Gain}=5-4.2=\boxed{\text{EUR }0.8\text{m}},\qquad G=\boxed{0}
$$

Ignoring tax, profit and retained earnings increase by EUR 0.8m. It is an acquisition gain, not evidence that the acquired business generated EUR 0.8m of recurring operating profit.

> [!NOTE]
> Do not leave “negative goodwill” as an asset deduction. Reassess measurements, then recognize the confirmed bargain in profit.

*Source pattern: 2025 CFA Level II FSA, LM1, p.27. Inputs adapted unless stated.*

---

## Variant: 23 — Full versus partial goodwill with a separately valued minority stake

**Abstract:** *Full goodwill uses the fair value of the non-controlling interest. Partial goodwill uses its share of identifiable net assets; neither method scales the subsidiary’s assets down.*

> A parent pays EUR 800,000 for 80% of a subsidiary. Fair identifiable net assets are EUR 900,000. The separately measured fair value of the 20% non-controlling stake is EUR 180,000. Calculate goodwill and NCI under full goodwill and partial goodwill. Explain why dividing the purchase price by 80% is not the right total-value input here.

<span class="jargon-unlock">**NCI. What is it?** Non-controlling interest: subsidiary equity belonging to outside owners. **Full goodwill. What is it?** $G=C+N-F$, where $C$ is consideration, $N$ NCI fair value and $F$ fair identifiable net assets. **Partial goodwill. What is it?** $G=C-pF$, where $p$ is parent ownership; NCI is $(1-p)F$.</span>

**1. Use the provided NCI fair value for full goodwill**

The minority stake need not have the same per-share value as the controlling block.

$$
G_{\text{full}}=800{,}000+180{,}000-900{,}000=\boxed{80{,}000},\qquad NCI_{\text{full}}=\boxed{180{,}000}
$$

**2. Use identifiable net assets for partial goodwill**

Only the parent’s acquired goodwill is recognized under this option.

$$
G_{\text{partial}}=800{,}000-0.80(900{,}000)=\boxed{80{,}000},\qquad NCI_{\text{partial}}=0.20(900{,}000)=\boxed{180{,}000}
$$

All amounts are EUR. The methods happen to coincide because NCI fair value equals its share of identifiable net assets. Dividing EUR 800,000 by 80% would incorrectly imply EUR 200,000 NCI despite the given EUR 180,000 valuation.

> [!NOTE]
> Use a supplied NCI fair value. IFRS permits full or partial goodwill per transaction; the source’s US GAAP acquisition model uses full goodwill.

*Source pattern: 2025 CFA Level II FSA, LM1, Examples 6 and 8, pp.27 and 31–33; separately priced NCI edge case. Inputs adapted unless stated.*

---

## Variant: 24 — Consolidate 100% of assets even when ownership is 80%

**Abstract:** *Control brings the whole subsidiary onto the group balance sheet. The outside ownership claim appears in NCI, not as a reduction of each asset.*

> Parent’s pre-acquisition assets are EUR 2m, including equipment EUR 700,000; liabilities are EUR 800,000. It issues EUR 800,000 of shares for 80% of a subsidiary with fair assets EUR 1.2m, including equipment EUR 500,000, and fair liabilities EUR 300,000. NCI fair value is EUR 200,000. Ignore tax and fees. Calculate consolidated equipment, assets, liabilities and total equity under full and partial goodwill.

<span class="jargon-unlock">**Consolidation. What is it?** Reporting a controlled group as one entity. **Full/partial goodwill. What are they?** Full goodwill includes the acquired business’s measured NCI goodwill; partial goodwill recognizes only the parent’s goodwill. **NCI. What is it?** Outside shareholders’ equity claim. Both methods include all identifiable subsidiary assets and liabilities.</span>

**1. Calculate the two goodwill amounts**

Fair net assets are EUR 900,000. Full goodwill is EUR 100,000; partial goodwill is EUR 80,000.

$$
\text{Group equipment}=700{,}000+500{,}000=\boxed{\text{EUR }1{,}200{,}000}
$$

**2. Build both group balance sheets**

Parent equity rises from EUR 1.2m to EUR 2m because shares were issued. Add NCI of EUR 200,000 under full goodwill or EUR 180,000 under partial goodwill.

| EUR millions | Full | Partial |
|---|---:|---:|
| Assets | 3.30 | 3.28 |
| Liabilities | 1.10 | 1.10 |
| Parent equity | 2.00 | 2.00 |
| NCI | 0.20 | 0.18 |
| Total equity | 2.20 | 2.18 |

Both columns balance. The EUR 20,000 difference appears in goodwill and NCI, not in equipment or debt.

> [!NOTE]
> Full versus partial describes goodwill recognition, not the percentage of identifiable assets consolidated.

*Source pattern: 2025 CFA Level II FSA, LM1, Example 8, pp.31–34; practice Q8, Q12 and Q28. Inputs adapted unless stated.*

---

## Variant: 25 — Allocate subsidiary profit after the fair-value expense adjustment

**Abstract:** *Adjust the subsidiary’s profit for acquisition-basis depreciation before splitting it between parent shareholders and NCI.*

> A parent owns 80% of a subsidiary for the entire year. Parent profit excluding all investment income is EUR 200,000. Subsidiary profit is EUR 100,000 after its own recorded expenses. Acquisition-date equipment uplift was EUR 60,000 with 10 years remaining; no tax effects, intercompany sales, or goodwill impairment apply. Find total group profit, NCI profit, and profit attributable to parent shareholders.

<span class="jargon-unlock">**Acquisition-basis depreciation. What is it?** Extra group expense on equipment uplift not recorded in the subsidiary’s standalone accounts. **NCI profit. What is it?** Outside owners’ share of the subsidiary’s adjusted profit. **Parent-attributable profit. What is it?** Group profit remaining after the NCI allocation.</span>

**1. Put the subsidiary’s profit on the group’s purchase basis**

The equipment uplift adds EUR 6,000 of annual expense.

$$
N_S^{\text{adjusted}}=100{,}000-\frac{60{,}000}{10}=\boxed{\text{EUR }94{,}000}
$$

**2. Combine first, allocate second**

Consolidation includes the whole adjusted subsidiary profit before showing who owns it.

$$
\begin{aligned}
N_{\text{group}}&=200{,}000+94{,}000=\boxed{294{,}000}\\
N_{\text{NCI}}&=0.20(94{,}000)=\boxed{18{,}800}\\
N_{\text{parent}}&=294{,}000-18{,}800=\boxed{275{,}200}
\end{aligned}
$$

All amounts are EUR. The cross-check is $200{,}000+0.80(94{,}000)=275{,}200$. Full and partial goodwill give the same income here because goodwill is not amortized.

> [!NOTE]
> “Net income is the same under equity method and consolidation” refers to parent-attributable income under consistent assumptions, not group profit before NCI.

*Source pattern: 2025 CFA Level II FSA, LM1, pp.33–34; practice Q13, Q16. Inputs adapted unless stated.*

---

## Variant: 26 — Roll the non-controlling interest forward

**Abstract:** *NCI is an equity balance that grows with its share of adjusted profit and OCI, and falls with dividends paid to outside shareholders.*

> A parent owns 75% of a subsidiary. Opening NCI is EUR 120,000. The subsidiary’s group-adjusted annual profit is EUR 80,000 and OCI gain EUR 12,000. It pays total dividends EUR 40,000. There are no ownership changes or other movements. Calculate closing NCI and the part of the dividend that remains a group cash outflow after consolidation.

<span class="jargon-unlock">**NCI. What is it?** Equity in a subsidiary held by outside owners. **OCI. What is it?** Other comprehensive income, recorded outside profit. **Group-adjusted profit. What is it?** Subsidiary profit after relevant consolidation adjustments. Parent ownership is 75%, so outside ownership is 25%.</span>

**1. Add the outside owners’ earned amounts**

Their share of profit is EUR 20,000 and OCI EUR 3,000. OCI changes equity even though it is outside profit.

$$
NCI_1=120{,}000+0.25(80{,}000)+0.25(12{,}000)-0.25(40{,}000)=\boxed{\text{EUR }133{,}000}
$$

**2. Distinguish internal transfers from cash leaving the group**

EUR 30,000 of dividends goes to the parent and cancels inside the group. Only the outside shareholders’ payment leaves the consolidated entity.

$$
\text{External dividend outflow}=0.25(40{,}000)=\boxed{\text{EUR }10{,}000}
$$

The NCI balance rises EUR 13,000: EUR 23,000 comprehensive income less EUR 10,000 cash distribution.

> [!NOTE]
> Do not leave NCI frozen at acquisition-date value. Profit, OCI and distributions can all change it.

*Source pattern: 2025 CFA Level II FSA, LM1, pp.33–34 and financial-statement presentation pp.36–39. Inputs adapted unless stated.*

---

## Variant: 27 — Subsidiary sales: eliminate the whole unrealized profit

**Abstract:** *Consolidation eliminates the full intercompany profit, unlike the equity method’s ownership-share deferral. Sale direction affects which shareholders bear the income adjustment.*

> Parent owns 80% of Subsidiary. Goods cost the seller EUR 60,000 and are sold internally for EUR 100,000; 25% remain unsold externally at year-end. Compare an upstream sale by Subsidiary with a downstream sale by Parent. Ignore taxes and all other adjustments. Calculate total group profit elimination and its allocation between parent shareholders and NCI.

<span class="jargon-unlock">**Upstream/downstream. What do they mean?** Subsidiary-to-parent and parent-to-subsidiary sales respectively. **Unrealized profit. What is it?** Internal sale profit embedded in inventory not sold outside. **NCI. What is it?** The 20% outside ownership claim in this subsidiary.</span>

**1. Remove the internal profit in full**

The consolidated group has not sold one quarter of the goods to anyone outside itself.

$$
U=(100{,}000-60{,}000)(0.25)=\boxed{\text{EUR }10{,}000}
$$

**2. Assign the adjustment to the entity that recorded the profit**

For an upstream sale, the subsidiary booked the profit, so both sets of subsidiary owners share the reduction. For a downstream sale, the parent booked it.

| Profit reduction, EUR | Parent shareholders | NCI | Group |
|---|---:|---:|---:|
| Upstream | 8,000 | 2,000 | 10,000 |
| Downstream | 10,000 | 0 | 10,000 |

Inventory is reduced by EUR 10,000 in either case. Moving the invoice in the other direction changes attribution, not the amount of inventory profit the group invented internally.

> [!NOTE]
> Associate: defer the investor’s share. Controlled subsidiary: eliminate 100% of unrealized profit, then attribute income appropriately.

*Source pattern: 2025 CFA Level II FSA, LM1, intercompany elimination and NCI principles pp.20, 30 and 33; derived comparison. Inputs adapted unless stated.*

---

## Variant: 28 — IFRS goodwill impairment: use the better recovery route

**Abstract:** *Compare the unit’s carrying amount with the higher of value in use and fair value less disposal costs. Apply any loss to goodwill first.*

> An IFRS cash-generating unit has carrying amount EUR 1.4m including EUR 0.3m goodwill. Value in use is EUR 1.3m. Fair value is EUR 1.28m and selling costs EUR 0.03m. Identifiable net assets have a separately estimated fair value EUR 1.2m. Calculate impairment and remaining goodwill. Ignore tax.

<span class="jargon-unlock">**Cash-generating unit. What is it?** A group of assets producing cash inflows largely independent of other assets. **Recoverable amount. What is it?** $R=\max(VIU,FV-C)$, where $VIU$ is value in use, $FV$ fair value and $C$ disposal costs. **Goodwill impairment. What is it?** A write-down of acquisition goodwill when the unit cannot support its recorded amount.</span>

**1. Choose the higher recovery measure**

Keeping the unit has estimated value EUR 1.3m; selling it net of costs gives EUR 1.25m.

$$
R=\max(1.30,1.28-0.03)=\boxed{\text{EUR }1.30\text{m}}
$$

**2. Write off the shortfall against goodwill**

The EUR 1.2m identifiable-net-assets fair value is not needed for this IFRS calculation.

$$
L=1.40-1.30=\boxed{\text{EUR }0.10\text{m}},\qquad G_1=0.30-0.10=\boxed{\text{EUR }0.20\text{m}}
$$

The unit ends at EUR 1.3m. A subsequent recovery does not permit reversing this goodwill impairment.

> [!NOTE]
> IFRS unit impairment uses recoverable amount, not “unit fair value minus identifiable net assets” to infer goodwill.

*Source pattern: 2025 CFA Level II FSA, LM1, Example 9, p.35; practice Q27. Inputs adapted unless stated.*

---

## Variant: 29 — IFRS impairment larger than goodwill

**Abstract:** *Goodwill absorbs the first loss. If the shortfall exceeds goodwill, allocate the rest to eligible assets, subject to their applicable minimum carrying amounts.*

> An IFRS cash-generating unit contains goodwill EUR 300,000, equipment EUR 600,000 and a patent EUR 300,000, with no other assets or liabilities. Recoverable amount is EUR 600,000. No individual asset floor restricts the required allocation. Calculate total impairment, write-down of each asset, and the ending balance sheet. Ignore tax.

<span class="jargon-unlock">**Impairment waterfall. What is it?** The order in which a loss is applied: goodwill first, then eligible assets. **Pro rata. What does it mean?** In proportion to the remaining assets’ carrying amounts. **Asset floor. What is it?** A limit below which a particular asset cannot be reduced under the applicable impairment rules; none binds here.</span>

**1. Measure the total shortfall**

Carrying amount is EUR 1.2m and recoverable amount EUR 0.6m.

$$
L=1{,}200{,}000-600{,}000=\boxed{\text{EUR }600{,}000}
$$

**2. Exhaust goodwill, then allocate the remainder**

Write off EUR 300,000 goodwill. The remaining EUR 300,000 loss is split between equipment and patent in the ratio 600,000:300,000, or 2:1.

$$
L_{\text{equipment}}=300{,}000\frac{600{,}000}{900{,}000}=\boxed{200{,}000},\qquad L_{\text{patent}}=\boxed{100{,}000}
$$

All amounts are EUR. Ending balances are goodwill zero, equipment EUR 400,000, and patent EUR 200,000. Their sum equals the EUR 600,000 recoverable amount.

> [!NOTE]
> Do not cap the entire IFRS unit impairment at goodwill. Other eligible assets absorb the remaining loss, subject to their own restrictions.

*Source pattern: 2025 CFA Level II FSA, LM1, Example 9 alternative case, p.35. Inputs adapted unless stated.*

---

## Variant: 30 — US goodwill impairment: identify which version the question specifies

**Abstract:** *The local reading’s legacy two-step test differs from the later FASB one-step rule. State the requested framework before calculating; the same inputs can produce different answers.*

> A reporting unit has carrying amount USD 1.4m, including goodwill USD 0.3m. Unit fair value is USD 1.3m and fair value of identifiable net assets is USD 1.2m. Calculate impairment under the legacy two-step method explicitly taught in this local reading. Separately compare the one-step rule introduced by FASB ASU 2017-04. Ignore tax effects. Also find the legacy loss if unit fair value is only USD 0.8m.

<span class="jargon-unlock">**Reporting unit. What is it?** The unit used to assess goodwill under US accounting. **Legacy implied goodwill. What is it?** Unit fair value minus fair value of identifiable net assets. **One-step quantitative loss. What is it?** Excess of carrying amount over unit fair value, limited to recorded goodwill. The second calculation is an explicitly labeled source-version comparison.</span>

**1. Apply the reading’s legacy test**

Because $1.4>1.3$, the first step flags possible impairment. The second step measures implied goodwill as $1.3-1.2=0.1$ million.

$$
L_{\text{legacy}}=0.3-0.1=\boxed{\text{USD }0.2\text{m}}
$$

**2. Keep the later rule separate**

The later FASB rule measures the unit-level shortfall, capped at goodwill.

$$
L_{\text{one-step}}=\min(0.3,1.4-1.3)=\boxed{\text{USD }0.1\text{m}}
$$

If legacy unit fair value is USD 0.8m, implied goodwill is negative; the legacy goodwill loss is capped at $\boxed{\text{USD }0.3\text{m}}$, not USD 0.7m.

> [!NOTE]
> The local PDF’s two-step description is legacy guidance. Do not present it as current US GAAP or silently substitute the newer answer into its worked example.

*Source pattern: 2025 CFA Level II FSA, LM1, Example 10, pp.35–36; [FASB ASU 2017-04](https://storage.fasb.org/ASU2017-04.pdf) for the explicitly labeled comparison. Inputs adapted unless stated.*

---

## Variant: 31 — Joint venture: one line versus proportionate presentation

**Abstract:** *The equity method shows a net investment and a share of profit. Proportionate presentation replaces that net amount with the investor’s share of individual assets, liabilities, revenues and expenses.*

> An investor has a 50% joint venture. The venture has assets EUR 1,000, liabilities EUR 400, revenue EUR 800, expenses EUR 700, and profit EUR 100. There is no goodwill or other adjustment. Compare the venture-related amounts under the equity method and under proportionate consolidation as a stipulated historical/analytical comparison. Use equity method as the ordinary joint-venture treatment.

<span class="jargon-unlock">**Joint venture. What is it?** A jointly controlled arrangement giving parties rights to net assets. **Equity method. What is it?** Single investment and equity-income lines. **Proportionate consolidation. What is it?** Including an ownership share of each financial-statement line; it is used here only because the comparison explicitly requests it.</span>

**1. Present the net interest under the equity method**

Half of the venture’s net assets is the investment. Half of its profit is equity income.

$$
I=0.50(1{,}000-400)=\boxed{\text{EUR }300},\qquad EI=0.50(100)=\boxed{\text{EUR }50}
$$

**2. Open up the same net amount into individual lines**

| Venture contribution, EUR | Equity method | Proportionate |
|---|---:|---:|
| Venture-related assets shown | 300 investment | 500 assets |
| Venture liabilities shown | 0 | 200 |
| Revenue shown | 0 | 400 |
| Operating expenses shown | 0 | 350 |
| Profit contribution | 50 | 50 |

Net assets remain EUR 300 and profit EUR 50. Presentation has become larger without creating another euro of ownership.

> [!NOTE]
> Replace the investment with the proportionate assets and liabilities; do not retain it as well. The ordinary IFRS/US GAAP joint-venture method in the reading is equity accounting.

*Source pattern: 2025 CFA Level II FSA, LM1, p.11; practice Q14 and Q17–20. Inputs adapted unless stated.*

---

## Variant: 32 — Current ratio: a larger group can have a lower ratio

**Abstract:** *Combine current assets and current liabilities, not the two ratios. The subsidiary’s ratio determines whether it raises or lowers the combined result.*

> Parent’s post-purchase balance sheet has current assets EUR 250m and current liabilities EUR 110m; its investment in the investee is non-current. Investee has current assets EUR 140m and current liabilities EUR 90m. There are no intercompany balances or current-asset fair-value adjustments. Compare the parent’s current ratio under equity accounting and consolidation, as alternative stated influence/control scenarios.

<span class="jargon-unlock">**Current ratio. What is it?** $CR=CA/CL$, where $CA$ is current assets and $CL$ current liabilities. **Non-current investment. What is it?** An investment outside the short-term asset category. **Consolidation. What is it?** Inclusion of all controlled subsidiary balances, subject to eliminations.</span>

**1. Equity method leaves the current lines unchanged**

The investment is non-current, so it is not added to the numerator.

$$
CR_{\text{equity}}=\frac{250}{110}=\boxed{2.273}
$$

**2. Consolidation includes all subsidiary current balances**

Control means 100% of each line, not the ownership percentage.

$$
CR_{\text{group}}=\frac{250+140}{110+90}=\frac{390}{200}=\boxed{1.950}
$$

The subsidiary ratio is $140/90=1.556$, below the parent’s. The group ratio lies between the two; adding a lower-ratio business dilutes the parent’s liquidity ratio.

> [!NOTE]
> A current ratio does not always fall on consolidation. Its direction depends on the acquired current-asset and current-liability mix.

*Source pattern: 2025 CFA Level II FSA, LM1, practice Q29, pp.55–61. Inputs adapted unless stated.*

---

## Variant: 33 — Full goodwill changes leverage through the equity denominator

**Abstract:** *Full goodwill can increase both goodwill and NCI while leaving debt and parent equity unchanged. Specify whether equity includes NCI before comparing leverage.*

> A consolidated group has debt EUR 500m and parent-attributable equity EUR 800m. Under full goodwill, NCI is EUR 200m; under partial goodwill, NCI is EUR 180m. There are no other differences. Calculate debt/total equity under both methods and debt/parent equity under both. Explain the difference.

<span class="jargon-unlock">**Debt-to-equity. What is it?** Debt divided by the specified equity measure. **Total equity. What is it?** Parent-attributable equity plus non-controlling interest. **NCI. What is it?** Subsidiary equity owned by outside shareholders. **Full/partial goodwill. What are they?** Alternative recognition bases that can change recorded NCI and goodwill.</span>

**1. Include NCI when the denominator is total equity**

Debt is the same, but total equity is EUR 1,000m versus EUR 980m.

$$
(D/E)_{\text{full}}=\frac{500}{800+200}=\boxed{0.5000},\qquad (D/E)_{\text{partial}}=\frac{500}{800+180}=\boxed{0.5102}
$$

**2. Use parent equity when the question explicitly requests it**

The parent shareholders’ equity does not change between these two cases.

$$
\frac{D}{E_{\text{parent}}}=\frac{500}{800}=\boxed{0.6250}\quad\text{under either method}
$$

The lower total-equity leverage ratio under full goodwill reflects accounting measurement, not repayment of debt.

> [!NOTE]
> Keep debt definitions and equity denominators consistent. “Full goodwill lowers debt/equity” assumes total equity includes a higher NCI amount.

*Source pattern: 2025 CFA Level II FSA, LM1, pp.33–34; practice Q10 and Q30. Inputs adapted unless stated.*

---

## Variant: 34 — Profit margin: distinguish group profit from parent profit

**Abstract:** *Equity accounting adds a share of profit without adding investee sales. Consolidation adds all subsidiary sales and profit, then allocates NCI.*

> Parent has sales EUR 1,000m, operating profit EUR 100m and net profit EUR 60m before investment income. Investee has sales EUR 600m, operating profit EUR 30m and net profit EUR 20m. Ownership is 50%. Compare equity accounting with a stipulated control scenario requiring consolidation. No tax adjustments, purchase-basis differences or intercompany transactions apply. Compute parent-attributable net margin, group net margin, and consolidated operating margin.

<span class="jargon-unlock">**Net margin. What is it?** The specified net profit numerator divided by sales. **Operating margin. What is it?** Operating profit divided by sales. **Parent-attributable profit. What is it?** Group profit after allocating outside shareholders’ NCI. Equity income is assumed presented outside operating profit here.</span>

**1. Under equity accounting, sales stay at EUR 1,000m**

Net profit becomes $60+0.50(20)=70$ million.

$$
\text{Equity-method net margin}=\frac{70}{1{,}000}=\boxed{7\%}
$$

**2. Under consolidation, state whose profit is being divided**

Group sales are EUR 1,600m; group net profit is EUR 80m. NCI profit is EUR 10m, leaving the same EUR 70m for parent shareholders.

$$
\begin{aligned}
\text{Parent-attributable margin}&=70/1{,}600=\boxed{4.375\%}\\
\text{Group net margin}&=80/1{,}600=\boxed{5\%}\\
\text{Group operating margin}&=(100+30)/1{,}600=\boxed{8.125\%}
\end{aligned}
$$

The subsidiary’s 5% operating margin lowers the parent’s 10% margin. An accounting presentation change is not evidence that the factories suddenly became worse.

> [!NOTE]
> Never label parent profit and total group profit interchangeably. Either margin can be computed, but its numerator must be explicit.

*Source pattern: 2025 CFA Level II FSA, LM1, p.23; practice Q9, Q11, Q16 and Q32. Inputs adapted unless stated.*

---

## Variant: 35 — Return ratios: match the numerator to its owners

**Abstract:** *Parent-attributable profit belongs with parent equity; total group profit belongs with total group equity. Source-style mixed ratios can be calculated, but must be labeled.*

> Annual parent-attributable profit is EUR 90m and NCI profit EUR 10m. Beginning parent equity is EUR 600m and beginning NCI EUR 100m; beginning group assets are EUR 1,200m. Calculate parent ROE, group ROE, and group ROA using beginning balances. Also compute the mixed ratio of parent profit to total equity, solely to show the effect of its denominator.

<span class="jargon-unlock">**ROE and ROA. What are they?** Return on equity and return on assets: the specified annual income divided by equity or assets. **Beginning balances. What are they?** Values at the start of the year, used here because the question specifies them. **NCI. What is it?** The equity and income attributable to outside subsidiary owners.</span>

**1. Pair each profit measure with the matching equity**

Parent return excludes both outside profit and outside equity. Group return includes both.

$$
ROE_{\text{parent}}=\frac{90}{600}=\boxed{15\%},\qquad ROE_{\text{group}}=\frac{90+10}{600+100}=\boxed{14.2857\%}
$$

**2. Calculate the requested asset return and mixed ratio**

Total group net income is EUR 100m.

$$
ROA_{\text{group}}=\frac{100}{1{,}200}=\boxed{8.3333\%},\qquad \frac{N_{\text{parent}}}{E_{\text{total}}}=\frac{90}{700}=\boxed{12.8571\%}
$$

The last number is mathematically valid but is not the parent shareholders’ ROE. Its denominator includes capital belonging to owners whose income was excluded.

> [!NOTE]
> The reading sometimes uses parent profit over total equity in comparisons. Reproduce a requested convention explicitly; do not confuse it with matched parent ROE.

*Source pattern: 2025 CFA Level II FSA, LM1, ratio discussion p.34; practice Q33. Inputs adapted unless stated.*

---

## Variant: 36 — Asset turnover: remove the investment before adding subsidiary assets

**Abstract:** *Consolidation replaces the investment asset with underlying assets, including acquisition adjustments. Compare both the sales increase and the asset increase before predicting turnover.*

> Parent’s post-acquisition beginning assets are GBP 2,140m, including a GBP 320m investment representing 50% of another company. Parent sales are GBP 950m. Investee assets are GBP 1,070m, liabilities GBP 490m, and sales GBP 510m. Assuming control for the consolidated comparison, all excess price relates to unrecorded licenses with six-year lives; the same per-share valuation applies to both ownership blocks and there is no goodwill. Find beginning-asset turnover under equity accounting and consolidation. Parent and investee annual depreciation and amortization before purchase adjustments are GBP 102m and GBP 92m; also find the next full year’s consolidated expense. Ignore tax.

<span class="jargon-unlock">**Asset turnover. What is it?** Sales divided by the specified asset balance. **Purchase-basis license. What is it?** An identifiable intangible asset not recorded by the investee but recognized by the acquirer. **Consolidation elimination. What is it?** Removal of the parent’s investment to avoid counting both shares and underlying assets.</span>

**1. Infer the whole-company license adjustment**

The stake implies total fair net assets of $320/0.50=640$ million. Recorded net assets are $1{,}070-490=580$ million, leaving GBP 60m licenses.

$$
A_{\text{group}}=2{,}140-320+1{,}070+60=\boxed{\text{GBP }2{,}950\text{m}}
$$

**2. Divide the correct sales by each asset base**

Consolidation includes all GBP 510m subsidiary sales.

$$
AT_{\text{equity}}=\frac{950}{2{,}140}=\boxed{0.4439},\qquad AT_{\text{group}}=\frac{950+510}{2{,}950}=\boxed{0.4949}
$$

Annual license amortization is $60/6=10$ million. Consolidated depreciation and amortization is $102+92+10=\boxed{\text{GBP }204\text{m}}$. Consolidation raises turnover here; an asset-heavy subsidiary could lower it.

> [!NOTE]
> Do not add subsidiary assets while retaining the investment. Use the balance date requested: beginning, ending, or average assets are different denominators.

*Source pattern: 2025 CFA Level II FSA, LM1, practice Q31 and Q34, pp.55–62; original numerical inputs retained. Inputs adapted unless stated.*

---

## Variant: 37 — Receivables securitization through a controlled entity

**Abstract:** *If the special-purpose entity is consolidated, the receivables stay inside the group and external borrowing remains group debt. The internal sale does not create group revenue.*

> A sponsor has cash EUR 20m, receivables EUR 50m and other assets EUR 30m; current liabilities are EUR 25m, long-term debt EUR 30m and equity EUR 45m. It invests EUR 10m cash in an SPE. The SPE borrows EUR 40m externally and buys the sponsor’s receivables for EUR 50m. Control and consolidation are established. Prepare consolidated totals and compare with borrowing EUR 40m directly. Ignore fees, tax and credit losses.

<span class="jargon-unlock">**SPE. What is it?** A special-purpose entity formed for a limited activity. **Securitization. What is it here?** Financing receivables through that entity. **Consolidation. What is it?** Treating sponsor and controlled SPE as one group, cancelling their internal investment and asset transfer.</span>

**1. Follow the external cash**

The sponsor pays EUR 10m to its SPE, then receives EUR 50m. The net cash increase is the EUR 40m supplied by outside lenders.

$$
\text{Cash}=20-10+50=\boxed{\text{EUR }60\text{m}}
$$

**2. Cancel the internal sale and investment**

Receivables remain EUR 50m in the group. The sponsor’s SPE investment cancels against SPE equity.

| Consolidated item | EUR m |
|---|---:|
| Cash / receivables / other assets | 60 / 50 / 30 |
| Total assets | 140 |
| Current liabilities / long-term debt | 25 / 70 |
| Equity | 45 |

The check is $140=25+70+45$. Direct borrowing produces the same group balance sheet, and neither route creates revenue from the internal transfer.

> [!NOTE]
> A new legal entity does not automatically move debt outside the reporting group. This case stipulates control; voting percentage alone is not the consolidation test.

*Source pattern: 2025 CFA Level II FSA, LM1, Example 11, pp.41–42; practice Q6, Q21 and Q23. Inputs adapted unless stated.*

---

## Variant: 38 — Equity-method profit is not cash in the bank

**Abstract:** *Separate the associate earnings recognized from dividends actually received. A growing investment balance can coexist with little cash available to the investor.*

> An investor owns 40% of an associate. The associate reports EUR 100m profit and distributes EUR 10m total dividends. Investor-level acquisition-basis amortization is EUR 4m. No other movements occur. Calculate equity income, cash received, the investment increase, and cash received as a percentage of recognized equity income.

<span class="jargon-unlock">**Equity income. What is it?** The investor’s share of associate profit after required adjustments. **Cash conversion in this question. What is it?** Dividends received divided by recognized equity income; it is a simple analytical comparison, not a universal accounting ratio. **Acquisition-basis amortization. What is it?** Investor-specific expense for finite-lived purchase-price differences.</span>

**1. Measure accounting income and actual distributions**

The investor earns its share for accounting purposes even if the associate retains most of the cash.

$$
EI=0.40(100)-4=\boxed{\text{EUR }36\text{m}},\qquad D=0.40(10)=\boxed{\text{EUR }4\text{m}}
$$

**2. Reconcile the retained amount**

The difference remains in the investment carrying amount.

$$
\Delta I=36-4=\boxed{\text{EUR }32\text{m}},\qquad \text{Cash/income}=\frac4{36}=\boxed{11.1111\%}
$$

Only EUR 4m has reached the investor. The remaining earnings may support the associate’s growth, repay its debt, or be restricted from distribution. Profit on paper cannot directly pay the investor’s own bills.

> [!NOTE]
> Investigate cash-flow access and dividend restrictions. Do not count equity-method earnings as cash received or recognize the dividends as a second income item.

*Source pattern: 2025 CFA Level II FSA, LM1, Issues for Analysts, p.23; disclosure discussion pp.36–39. Inputs adapted unless stated.*

---

## Variant: 39 — Joint operation rights versus a joint venture’s net interest

**Abstract:** *Joint control does not by itself determine the presentation. Rights to net assets support joint-venture equity accounting; direct rights to assets and obligations for liabilities support recognition of those items.*

> Two arrangements are jointly controlled. In A, the investor has a 50% right to net assets of a separate joint venture with assets EUR 800, liabilities EUR 300, revenue EUR 600 and expenses EUR 500. In B, a joint-operation contract gives it direct rights to 50% of each asset and revenue and obligations for 50% of each liability and expense, using the same totals. Ignore acquisition differences and tax. Compare recognized assets, liabilities and profit.

<span class="jargon-unlock">**Joint venture. What is it?** An arrangement whose jointly controlling parties have rights to net assets. **Joint operation. What is it?** An arrangement giving rights to specified assets and obligations for specified liabilities. **Equity method. What is it?** Recognition of a single net investment and the investor’s share of profit.</span>

**1. A gives a net investment**

The investment is half of EUR 500 net assets. Profit is half of EUR 100.

$$
I_A=0.50(800-300)=\boxed{250},\qquad EI_A=0.50(600-500)=\boxed{50}
$$

**2. B gives direct rights and obligations**

Apply the explicitly supplied contractual shares to the individual items.

$$
A_B=\boxed{400},\qquad L_B=\boxed{150},\qquad R_B=\boxed{300},\qquad X_B=\boxed{250}
$$

All amounts are EUR. B also gives net assets EUR 250 and profit EUR 50, but presents the actual rights and obligations separately.

> [!NOTE]
> Do not describe joint-operation accounting as an elective proportionate-consolidation alternative for every joint venture. The contractual rights determine the treatment.

*Source pattern: 2025 CFA Level II FSA, LM1, classification disclosure p.5 and joint-arrangement discussion p.11. Inputs adapted unless stated.*

---

## Variant: 40 — Midyear acquisition: only post-acquisition profit belongs in the calculation

**Abstract:** *Split earnings at the acquisition date. Apply ownership and purchase-basis expense only to the period when the investment is held.*

> An investor purchases a 30% associate interest for EUR 300,000 on 1 July. Associate profit is EUR 200,000 for the year, earned evenly. The investor’s annual full-year purchase-basis depreciation adjustment would be EUR 6,000. The associate pays total dividends EUR 40,000 in December, all to the post-acquisition shareholders. No other movements or taxes apply. Calculate current-year equity income and closing investment.

<span class="jargon-unlock">**Post-acquisition earnings. What are they?** Profit earned after the investment is acquired. **Proration. What does it mean?** Adjusting a full-year figure to the relevant fraction of the year. **Equity-method carrying amount. What is it?** Cost plus recognized equity income minus distributions received, with other movements added only if present.</span>

**1. Use six months of profit and depreciation adjustment**

Half the annual profit was earned before the investor arrived. It is part of what was purchased, not new income earned afterward.

$$
EI=0.30(200{,}000)\frac6{12}-6{,}000\frac6{12}=\boxed{\text{EUR }27{,}000}
$$

**2. Deduct the actual dividend entitlement**

The December dividend is paid to the current shareholders, so the investor receives 30% of the full EUR 40,000 distribution.

$$
I_1=300{,}000+27{,}000-0.30(40{,}000)=\boxed{\text{EUR }315{,}000}
$$

Do not halve the dividend simply because ownership began midyear. The question specifies who receives that distribution.

> [!NOTE]
> Prorate earnings based on when they were earned; calculate dividends from actual entitlement and timing. Acquisition-date profit is not a full year of investor income.

*Source pattern: 2025 CFA Level II FSA, LM1, post-acquisition recognition pp.11–12 and acquisition-date principles p.26. Inputs adapted unless stated.*

---

## Variant: 41 — An assumed liability and a matching indemnification asset

**Abstract:** *An acquired liability lowers identifiable net assets; a recognized seller indemnity can offset part of that reduction. Recognize both rather than silently netting away the exposure.*

> A buyer pays EUR 10m for 100% of a business. Identifiable net assets before one legal contingency are EUR 8m. The acquired present obligation qualifies for recognition at fair value EUR 1m. A contractual seller indemnity for part of the same obligation qualifies for recognition at fair value EUR 0.6m on the same basis. Ignore tax. Calculate adjusted identifiable net assets, goodwill, and the net acquired exposure.

<span class="jargon-unlock">**Indemnification asset. What is it?** A contractual claim against the seller for specified losses on an acquired item. **Contingent liability. What is it?** An obligation whose amount or outcome is uncertain; this question explicitly establishes recognition. **Goodwill. What is it?** Consideration above identifiable fair net assets.</span>

**1. Record the obligation and the reimbursement claim**

The buyer owes EUR 1m under the measured liability and has a EUR 0.6m asset against the seller. Those are separate claims.

$$
F_{\text{net assets}}=8-1+0.6=\boxed{\text{EUR }7.6\text{m}}
$$

**2. Recalculate the acquisition residual**

The net identified exposure is EUR 0.4m, reducing net assets and raising goodwill by the same amount relative to the no-contingency case.

$$
G=10-7.6=\boxed{\text{EUR }2.4\text{m}},\qquad \text{Net exposure}=1-0.6=\boxed{\text{EUR }0.4\text{m}}
$$

The indemnity does not justify ignoring the liability. It supplies a separately measured reimbursement asset.

> [!NOTE]
> Recognition and measurement conditions matter. Here they are supplied explicitly; do not assume every hoped-for seller reimbursement qualifies as an asset.

*Source pattern: 2025 CFA Level II FSA, LM1, acquisition-date liabilities and indemnification assets, p.26. Inputs adapted unless stated.*

---

## Variant: 42 — Acquired research and licenses: identifiable assets before goodwill

**Abstract:** *Recognize qualifying acquired intangibles separately at fair value. Finite-lived assets are amortized when ready for use; unsuccessful acquired research is tested for impairment.*

> A buyer pays EUR 12m for all of a business. Fair net assets excluding unrecorded intangibles are EUR 7m. Qualifying acquired in-process research has fair value EUR 2m; an immediately usable license has fair value EUR 1m and a five-year life with no residual value. Ignore tax. Find goodwill and Year 1 license amortization. In Year 2, before any research amortization, the research fails and its recoverable amount is zero; find that loss.

<span class="jargon-unlock">**In-process research and development. What is it?** An unfinished project acquired with the business. **Identifiable intangible. What is it?** A separately recognizable non-physical asset, such as a license or qualifying research project. **Amortization. What is it?** Allocation of a finite-lived intangible’s amount over useful life. **Impairment. What is it?** A write-down when its recoverable value falls below carrying amount.</span>

**1. Allocate the price to identifiable assets first**

The research and license are not swept into goodwill merely because neither is a machine.

$$
G=12-(7+2+1)=\boxed{\text{EUR }2\text{m}}
$$

**2. Follow each asset’s subsequent economics**

The ready-to-use license is amortized. The unfinished research is not treated as a completed finite-lived product before completion.

$$
\text{Year 1 license expense}=1/5=\boxed{\text{EUR }0.2\text{m}},\qquad \text{Research loss}=2-0=\boxed{\text{EUR }2\text{m}}
$$

The research failure writes down the research asset, not goodwill automatically. Goodwill and other assets have their own impairment assessments.

> [!NOTE]
> Acquisition accounting can recognize identifiable assets the target had not recorded. Do not confuse acquired research with the separate rules for internally incurred research costs.

*Source pattern: 2025 CFA Level II FSA, LM1, identifiable assets p.26; in-process R&D p.44. Inputs adapted unless stated.*
