### MODULE 8: EQUITY VALUATION: CONCEPTS AND BASIC TOOLS

```table-of-contents
```

#### Dividend Discount Models

1. What I’m actually valuing is cash to me. DDM = PV of all future dividends. If dividends are messy, I use FCFE as “what could be paid.”
2. For short holds, I discount dividends I’ll get and the sale price. For long holds, I push to a point where growth is steady and drop in a terminal value.
3. Gordon (constant) growth is the workhorse. ==V0 = D1/(r − g)==. Only if (Required Rate) r > g (Dividend Growth) and the business is in “stable mode.” **==Common exam trap: plugging D₀ directly.==** Growth rate is strictly less than the required rate of return. 
4. Gordon Growth Model is appropriate for valuing company that has stable growth. 

> [!question] MULTI STAGE GROWTH
> A stock's current dividend is $5.00. Dividends are expected to grow at 10% for three years, then 5% thereafter. With a required return of 15%, the intrinsic value?
> 
> D1 = 5.5, D2 = 6.05, D3 = 6.655 = 13.73
> 
> Perpetual value = 6.655(1.05) / 0.15 - 0.05 = 6.98 / 0.10 = 69.8
> 
> Intrinsic Value = 69.8 / (1.15)

> [!question] VALUATION OF PREFERRED STOCK 
> A preferred stock has a par value of $100, pays a 5% annual dividend, and matures in exactly 4 years. The required rate of return is 6%. What is its value?
> 
> ---
> 
> Preferred stock will pay 5% or $5 for 4 years. Value it like a bond: N = 4, I/Y = 6, PMT = 5, FV = 100 → PV = 96.53


5. Preferred Dividend is just a level perpetuity: V0 = D/r. 
6. Sustainable growth:  $g = (1-\text{payout})\times ROE$. Growth comes only from **retained earnings earning ROE** → **g = b × ROE**

7. Multistage logic: add PV of high-growth dividends + PV of the terminal value set one period before constant growth starts.
8. If there’s no dividend yet, I anchor the first dividend, compute terminal value at t = (first dividend − 1), and discount back.

> [!ABSTRACT] MEMORISE
> - Finite horizon (sell at N):
>   $$V_0 = \sum_{t=1}^{N} \frac{D_t}{(1+k_e)^t} + \frac{P_N}{(1+k_e)^N}$$
> - Constant growth (Gordon):
>   $$V_0 = \frac{D_1}{k_e - g},\; k_e>g$$
> - Preferred (g = 0):
>   $$V_0 = \frac{D}{k_p}$$
> - Sustainable growth:  $g = (1-\text{payout})\times ROE$
> Growth comes only from **retained earnings earning ROE** → **g = b × ROE**
> Notation I use
> - D0 = just paid; D1 = next dividend. P_t = price at end of Year t. V0 = value today.
> - ke = required return on common; kp = required return on preferred; g = dividend growth.
> - b = retention = 1 − payout; ROE = return on equity.
> 

[!tip] Quick Checks
- “just paid/recently paid” → D0. “will pay/expected to pay” → D1. Gordon always uses D1.
- Check ke > g. If they’re too close, ==tiny tweaks blow up the value==.
- Terminal value sits one period before the first constant-growth dividend.
- If dividends are unreliable, cross-check with FCFE or a justified multiple.

[!question] MULTI-PERIOD DDM
Problem:
— D0 = 1.50, g = 8%, ke = 12%, P3 = 51.00. Find V0.
Solution:
— D1 = 1.62, D2 = 1.75, D3 = 1.89. PV(divs) ≈ 4.19. PV(P3) = 36.30. V0 ≈ 40.49.
Explanation:
— Add PV of the near dividends and the sale price. Don’t overthink it.

[!question] GORDON GROWTH VALUE
Problem:
— D0 = 1.50, g = 8%, ke = 12%. Find V0 and how much comes from growth.
Solution:
— D1 = 1.62. V0 = 1.62/0.04 = 40.50.
— Zero-growth value = 1.50/0.12 = 12.50 → value from growth ≈ 28.00.
Explanation:
— The ke − g spread drives everything. ==Narrow spread → big value.==

[!question] NO CURRENT DIVIDEND → FIRST DIV AT t=4
Problem:
— First dividend at Year 4; E4 = 1.64; payout = 50%; g = 5%; ke = 10%. Find V0.
Solution:
— D4 = 0.82. V3 = 0.82/0.05 = 16.40. V0 = 16.40/1.10^3 = 12.33.
Explanation:
— Set terminal at t=3 (one period before first dividend), then discount.

[!question] TWO-STAGE (SUPER-NORMAL → STABLE)
Problem:
— D0 = 1.00; g* = 15% for two years, then gc = 5% forever; ke = 11%. Find V0.
Solution:
— D1 = 1.15; D2 = 1.3225; D3 = 1.3886.
— P2 = 1.3886/0.06 = 23.144.
— V0 ≈ 1.15/1.11 + 1.3225/1.11^2 + 23.144/1.11^2 ≈ 20.90.
Explanation:
— Cash flows in the crazy years get discounted directly; everything after that is the Gordon block at t=2.

> [!warning] Remember
> - Don’t force Gordon on negative or supernormal growth forever. Use a finite high-growth window, then stabilize g.
> - Preferred → use kp and level D. Common → ke and D1.

#### Relative Valuation Measures

1. The economic principle underlying the method of comparables (using price multiples) is: **Law of One Price**
2. Common valuation multiples include **P/E, P/CF, P/S, and P/B**. You can invent others (e.g., price per user), but the logic is unchanged.    
3. Book Value = Total Assets − Total Liabilities - **Preferred Stock**
4. Multiples are per-share comparisons. The **denominator must be per share**.
5. **Justified P/E** = what P/E _should be_ given fundamentals. **Market (non-justified) P/E** = what P/E _is_. Undervalued/overvalued comes from **comparing the two**.
6. Given reqd. discount $k$, dividend growth $g$, dividend $D$ and price $P$	$$ P_0 = \frac{D_1}{k-g} $$
7. Divide both sides by expected EPS $E_1$	$$ \frac{P_0}{E_1} = \frac{D_1/E_1}{k-g}$$
8. At LHS, it is Justified P/E which is always **leading**. The denominator is expected earnings $E_1$.
9. Raising the **dividend payout** increases current cash to shareholders but **reduces sustainable growth** by cutting reinvestment. Higher dividends push value up; lower growth pulls value down. The effects **offset**. This trade-off is called **dividend displacement of earnings**.
10. It is very important to understand the relationship of PE ratio to each of its parameters:
	- Payout Ratio ↑ PE multiple ↑
	- k ↑ PE Multiple ↓. High DE Ratio, or anything that signals higher risk would crank up required rate of return
	- g ↑ PE multiple ↑. Anything that signals higher future earnings would crank up g. For example, higher sales growth, bullish outlook etc.
11. The disadvantages of multiples based approach is:
	- **Comparable vs fundamental conflict**: Tesla can look _overvalued_ on peer P/E versus automakers, yet _fair_ or undervalued on a DCF assuming high growth.
	- **Accounting differences**: SAP (IFRS) vs Oracle (US GAAP) can show different P/E or P/B purely due to R&D and revenue-recognition rules.
	- **Cyclicality distortion**: Delta Air Lines may show a very low P/E at peak earnings (looks cheap) and a very high P/E in a downturn (looks expensive), driven by the cycle, not mispricing.
12. Enterprise value represents the total takeover cost: equity plus debt minus cash, because the acquirer assumes debt but also receives the cash.

> [!NOTE] WHAT IS EV?
> A company is financed by:
> 
> Equity: owners’ money (shareholders).
> 
> Debt: borrowed money (lenders).
> 
> Preferred stock: a hybrid claim (often like “equity with fixed-like payments”).
> 
> If someone buys the whole company, they effectively take over all these claims.
> 
> 2) Cash on the company’s balance sheet
> 
> Cash and short-term investments are money the buyer “gets” on day 1 after buying.
> 
> So cash reduces the net amount the buyer must effectively pay.
> 
> 3) EV (Enterprise Value)
> 
> **EV = equity value + preferred stock + debt − cash & short-term investments.**
> 

13. **EV is preferred when comparing firms with different capital structures; market cap alone can mislead.**
14. EV must be matched with earnings available to both debt and equity holders, which is why EV/EBITDA is used; when net income is negative, P/E breaks but EV/EBITDA still works. Firm A has EV = 1,000, EBITDA = 100 ⟶ EV/EBITDA = 10. Net income = −10, so P/E is meaningless, but valuation via EV still works.
15. **EBITDA can mislead because it ignores capital expenditures and can overstate cash flow. Eg: Vodafone Group often reports strong EBITDA, but heavy recurring capex on spectrum licenses and network upgrades absorbs most of the cash, so free cash flow remains weak despite attractive EV/EBITDA.**


> [!NOTE] ASSET BASED VALUATION MODELS
>  Asset-based valuation starts from the balance sheet and estimates equity as fair value of assets minus liabilities, adjusting book values using depreciated cost, inflation-adjusted cost, or replacement cost because book ≠ market.

16. Asset-based models struggle when intangibles dominate, so values are usually treated as a floor or liquidation value and work best only for tangible-asset-heavy or liquidation cases. Eg: Google has a brand, talent and data which makes tangible asset valuation meaningless.
17. P/B fails when book value is not reliable.
