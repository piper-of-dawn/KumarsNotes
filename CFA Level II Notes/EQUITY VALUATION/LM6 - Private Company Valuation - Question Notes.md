## Variant: 1 — Normalized earnings: remove the owner's extras

**Abstract:** *Replace unusual owner-related costs with the costs of running the business normally. Adjust the right profit line, then recalculate tax; an expense disappearing does not make tax disappear too.*

> A private manufacturer reports revenue of €10m, cost of goods sold of €6m, selling and administrative expenses of €2m, and depreciation of €0.5m. Administrative expenses include owner pay of €0.8m versus a market salary of €0.3m, plus €0.1m of personal-property upkeep. Depreciation includes €0.05m on that personal property. Remove the personal assets from operations. At a 25% tax rate, calculate normalized EBITDA, EBIT, and after-tax operating income.

<span class="jargon-unlock">**Normalized earnings. What are they?** Profit adjusted to represent ordinary economic operations. **EBITDA and EBIT. What are they?** Earnings before interest, tax, depreciation and amortization; subtract depreciation and amortization to get EBIT, or operating profit. Depreciation spreads an asset's cost across accounting periods. **After-tax operating income. What is it?** $EBIT(1-T)$, where $T$ is the tax rate; financing costs are excluded. Here m means million.</span>

**1. Remove the excess, not the entire salary**

Someone still has to run the factory. The €0.3m replacement salary survives the owner's departure; the private-property upkeep does not.

$$
\text{Normalized administrative costs}=2-(0.8-0.3)-0.1=\boxed{\text{EUR }1.4\text{m}}
$$

**2. Rebuild profit from the top**

EBITDA excludes depreciation, so the €0.05m depreciation adjustment enters only when calculating EBIT.

$$
\begin{aligned}
EBITDA&=10-6-1.4=\boxed{\text{EUR }2.6\text{m}}\\
EBIT&=2.6-(0.5-0.05)=\boxed{\text{EUR }2.15\text{m}}\\
EBIT(1-T)&=2.15(0.75)=\boxed{\text{EUR }1.6125\text{m}}
\end{aligned}
$$

Reported EBIT was €1.5m. Removing €0.65m of expenses raises after-tax operating profit by €0.4875m. The tax authority also enjoys the owner's newfound restraint.

> [!NOTE]
> Normalize each expense once. Removing depreciation raises EBIT, but cannot raise EBITDA: EBITDA already excludes it.

*Source pattern: 2025 curriculum, LM6, Example 1, pp.418–419; practice Q3 and Q11. Inputs adapted.*

---

## Variant: 2 — An unpaid owner is not free management

**Abstract:** *If the owner works for less than market pay, normalized earnings fall. Dividends distribute profit; they do not replace the missing salary expense.*

> A private retailer reports EBITDA of €1m. Its owner works full-time as CEO, takes no salary, and receives a €0.4m dividend. A replacement CEO would cost €0.25m annually. There are no other adjustments. Calculate normalized EBITDA and the after-tax reduction in operating earnings at a 20% tax rate.

<span class="jargon-unlock">**CEO. What is a CEO?** The chief executive officer who manages the company. **EBITDA. What is it?** Earnings before interest, taxes, depreciation and amortization. **Dividend. What is it?** A payment to owners from the company's resources, not an operating expense. **Normalization. What does it mean?** Replacing reported costs with sustainable, market-based costs.</span>

**1. Price the job that must continue**

The business receives management services worth €0.25m without recording their cost. Free labour makes an excellent reported margin and a rather fragile business plan.

$$
\text{Normalized EBITDA}=1-0.25=\boxed{\text{EUR }0.75\text{m}}
$$

**2. Measure the after-tax effect**

The new salary reduces operating profit by €0.25m but also reduces tax, assuming the expense is deductible and the tax benefit is usable.

$$
\Delta\text{after-tax operating earnings}=-0.25(1-0.20)=\boxed{-\text{EUR }0.20\text{m}}
$$

The €0.4m dividend is irrelevant to this earnings adjustment. It was never deducted in EBITDA, so adding it back would invent profit.

> [!NOTE]
> Excess salary → raise normalized profit. Missing or inadequate salary → lower it. Dividend size does not decide the salary adjustment.

*Source pattern: pp.419, 423; practice Q11. Inputs adapted.*

---

## Variant: 3 — Free rent between related companies

**Abstract:** *Put a market rent into both companies' separate accounts: a cost for the occupier and income for the owner. The internal transfer cancels for the combined group.*

> ShopCo earns €0.9m before tax and pays no rent for space owned by sister company PropertyCo. Market rent is €0.3m per year. PropertyCo currently earns €0.2m before tax. All other costs are already recorded correctly. Normalize each company's pre-tax earnings and reconcile the combined total. Both companies are wholly owned by the same family.

<span class="jargon-unlock">**Related parties. What are they?** Parties linked by ownership or other shared interests. **Arm's-length rent. What is it?** Rent independent parties would agree in the market. **Combined earnings. What are they?** The two businesses' earnings after cancelling transactions between them; internal rent is not revenue from an outside customer.</span>

**1. Stop treating the shop floor as a family favour**

An independent buyer of ShopCo would need premises. Charge the rent it would actually face, and credit the same amount to the company supplying the space.

$$
\begin{aligned}
\text{ShopCo normalized profit}&=0.9-0.3=\boxed{\text{EUR }0.6\text{m}}\\
\text{PropertyCo normalized profit}&=0.2+0.3=\boxed{\text{EUR }0.5\text{m}}
\end{aligned}
$$

**2. Check the group total**

The family has moved income between pockets, not found a new customer.

$$
\text{Combined profit}=0.6+0.5=0.9+0.2=\boxed{\text{EUR }1.1\text{m}}
$$

ShopCo's standalone valuation should now reflect lower earnings; PropertyCo's should reflect higher rental income. Different valuation rates can mean the individual valuation changes are not equal.

> [!NOTE]
> Market rent changes each unit's economic picture. Do not count internal rent as extra group income or add PropertyCo's building to ShopCo's assets.

*Source pattern: Example 2, pp.420–421. Inputs adapted.*

---

## Variant: 4 — Separate the operating business from its building

**Abstract:** *If property is valued separately, first charge the business market rent. Otherwise the building earns a return inside the business valuation and gets sold to you again on the next line.*

> A debt-free firm owns its premises. Reported annual EBITDA is €1.2m and includes €0.1m of owner-property costs. Under the assumed rental arrangement, those costs would be borne by the landlord; market rent would be €0.25m. Comparable operating businesses trade at 6 times EBITDA. The building's separately appraised value is €2m. Calculate total equity value, assuming no other assets or adjustments.

<span class="jargon-unlock">**EBITDA multiple. What is it?** A price expressed as a number of times earnings before interest, taxes, depreciation and amortization. **Operating value. What is it?** Value of the trading business, excluding property appraised separately here. **Equity value. What is it?** Value belonging to owners after debt and other claims; this question has no debt.</span>

**1. Make the operating business comparable to a tenant**

Remove owner-property costs, then add the full rent under the stated rental terms.

$$
\text{Tenant-basis EBITDA}=1.2+0.1-0.25=\boxed{\text{EUR }1.05\text{m}}
$$

**2. Value the business and property separately**

The multiple applies to the rent-paying operation. Add the building because this company actually owns it.

$$
\text{Equity value}=6(1.05)+2=\boxed{\text{EUR }8.30\text{m}}
$$

Applying 6 times reported EBITDA and then adding the property gives €9.2m: an overstatement of €0.9m. The same building has acquired a suspicious talent for appearing twice.

> [!NOTE]
> Separate property valuation requires matching rental adjustments. If the property belongs to the owner personally, its value is not a company asset.

*Source pattern: p.420, owned-property normalization; market-multiple approach pp.442–446. Inputs adapted.*

---

## Variant: 5 — Profit becomes cash only after reinvestment

**Abstract:** *Start with after-tax operating profit, add back non-cash depreciation, and subtract actual investment. EBITDA is not cash available to investors: equipment suppliers still expect payment.*

> Normalized EBITDA is €4m, depreciation €0.8m, capital expenditure €1.1m, and the increase in operating working capital €0.3m. The tax rate is 25%. Calculate FCFF by starting from EBIT and independently check it using EBITDA. Interest expense is €0.2m; explain whether to deduct it.

<span class="jargon-unlock">**FCFF. What is it?** Free cash flow to the firm: cash available to debt and equity investors together. $FCFF=EBIT(1-T)+D-C-\Delta W$, where $T$ is tax rate, $D$ depreciation, $C$ capital expenditure, and $\Delta W$ the increase in operating working capital. **Working capital. What is it here?** Cash tied up in day-to-day operations, such as inventories and customer receivables less operating payables. **EBIT. What is it?** Operating profit after depreciation; EBITDA is profit before depreciation and amortization as well as interest and tax.</span>

**1. Calculate operating cash after reinvestment**

Depreciation reduced accounting profit without using cash this period. Add it back, then subtract the actual equipment bill and cash absorbed by operations.

$$
FCFF=(4-0.8)(1-0.25)+0.8-1.1-0.3=\boxed{\text{EUR }1.80\text{m}}
$$

**2. Check with the EBITDA route**

Starting before depreciation means adding only depreciation's tax saving, not all depreciation again.

$$
FCFF=4(1-0.25)+0.8(0.25)-1.1-0.3=\boxed{\text{EUR }1.80\text{m}}
$$

Do not deduct the €0.2m interest: FCFF belongs to lenders and shareholders together. Financing enters the discount rate and the later debt deduction.

> [!NOTE]
> EBIT route: add full depreciation. EBITDA route: add depreciation × tax rate. Both subtract gross capital expenditure, not a second deduction for depreciation.

*Source pattern: Example 12, pp.449–450. The source diagram's EBIT/EBITDA labels are inconsistent; the two equivalent routes above make the distinction explicit. Inputs adapted.*

---

## Variant: 6 — Approval probabilities belong to the whole path

**Abstract:** *Multiply conditional probabilities along each path, value each successful outcome, then discount the weighted future value. A 50% chance after approval is not a 50% chance today.*

> A drug developer has a 75% chance of preliminary approval in Year 1. Conditional on that approval, Year 2 outcomes are broad approval with probability 50%, narrow approval 30%, and failure 20%. Broad approval produces Year 3 FCFF of €12m growing forever at 4%; narrow approval produces €4m growing at 2%. Failure is worth zero. There are no interim cash flows. Use a 12% annual WACC to estimate value today.

<span class="jargon-unlock">**Conditional probability. What is it?** A probability applying only after an earlier event occurs. **FCFF and WACC. What are they?** Cash available to all capital providers and their weighted average required return. **Continuing value. What is it?** Value at the start of a growing cash-flow stream: $V_2=FCFF_3/(r-g)$, where $r$ is WACC and $g$ annual perpetual growth. Subscripts identify years.</span>

**1. Value the successful businesses at Year 2**

The first operating cash arrives in Year 3, so these perpetuity values sit one year earlier.

$$
V_{2,\text{broad}}=\frac{12}{0.12-0.04}=\boxed{\text{EUR }150\text{m}},\qquad V_{2,\text{narrow}}=\frac{4}{0.12-0.02}=\boxed{\text{EUR }40\text{m}}
$$

**2. Weight whole paths, then travel back two years**

Broad approval has probability $0.75(0.50)=0.375$; narrow approval has probability $0.75(0.30)=0.225$. Total failure probability is $0.25+0.75(0.20)=0.40$. The probabilities sum to one.

$$
V_0=\frac{0.375(150)+0.225(40)+0.40(0)}{1.12^2}=\boxed{\text{EUR }52.02\text{m}}
$$

The lab's promising future still has two approval gates. The valuation cannot walk through them without paying the probability toll.

> [!NOTE]
> Use real scenario probabilities as supplied; these are not risk-neutral trading weights. Discount the Year 2 value for two years, not three.

*Source pattern: Example 3, pp.421–423; approval tree visually checked. Inputs adapted.*

---

## Variant: 7 — Worse approval odds can still mean higher value

**Abstract:** *Value depends on which outcomes become more likely, not just the headline success probability. A smaller chance of a much better payoff can outweigh a larger chance of a modest one.*

> A developer has no interim cash flows and is worth €150m at Year 2 after broad approval, €40m after narrow approval, and zero after failure. Previously preliminary approval probability was 75%, followed by conditional probabilities of 50% broad and 30% narrow approval. New preliminary approval probability is 60%, followed by 70% broad and 10% narrow. Remaining outcomes are failure. At a 12% annual discount rate, calculate the change in today's value.

<span class="jargon-unlock">**Expected value. What is it?** The sum of each outcome's value times its probability, not a promised payoff. **Conditional probability. What does it mean?** The second-stage probability applies only if the first stage succeeds. **Present value. What is it?** A future amount divided by $(1+r)^n$, where $r$ is the annual required return and $n$ years until receipt.</span>

**1. Compare the weighted Year 2 payoffs**

The old broad and narrow probabilities were 37.5% and 22.5%. The new ones are 42% and 6%.

$$
\begin{aligned}
E(V_{2,\text{old}})&=0.375(150)+0.225(40)=\text{EUR }65.25\text{m}\\
E(V_{2,\text{new}})&=0.42(150)+0.06(40)=\text{EUR }65.40\text{m}
\end{aligned}
$$

**2. Discount the difference**

The new forecast loses many narrow successes but gains some broad successes, which are worth much more.

$$
\Delta V_0=\frac{65.40-65.25}{1.12^2}=\boxed{+\text{EUR }0.1196\text{m}}
$$

Overall final success probability falls from 60% to 48%, yet value rises by roughly €119,579. Counting successes without weighing their value is a scoreboard with half the numbers missing.

> [!NOTE]
> Compare probability × payoff across every outcome. A lower overall approval probability alone does not establish a lower valuation.

*Source pattern: knowledge check p.424, Q3. Inputs adapted.*

---

## Variant: 8 — CAPM, expanded CAPM, and the build-up approach

**Abstract:** *CAPM prices market risk through beta; expanded CAPM adds size and company premiums; build-up replaces the beta-scaled market premium with the unscaled premium and an industry adjustment.*

> Use a 3% risk-free rate, 6% equity risk premium, beta of 1.2, size premium of 2%, company-specific premium of 1%, and industry premium of 0.5%. Calculate cost of equity under CAPM, expanded CAPM, and build-up. Explain why the answer is not necessarily larger merely because the model lists more inputs.

<span class="jargon-unlock">**Cost of equity. What is it?** The return shareholders require for bearing risk. **CAPM. What is it?** Capital asset pricing model: $r_e=r_f+\beta ERP$, where $r_e$ is cost of equity, $r_f$ the risk-free rate, $ERP$ the market equity risk premium, and $\beta$ sensitivity to market movements. **Risk premium. What is it?** An extra required return. Size and company premiums address additional assessed risks; the build-up industry premium adjusts for the business sector.</span>

**1. Apply each model's actual ingredients**

All quoted premiums are additions in percentage points. Multiply only the market premium by beta in the two CAPM versions.

$$
\begin{aligned}
r_{e,\text{CAPM}}&=3\%+1.2(6\%)=\boxed{10.2\%}\\
r_{e,\text{expanded}}&=10.2\%+2\%+1\%=\boxed{13.2\%}\\
r_{e,\text{build-up}}&=3\%+6\%+2\%+0.5\%+1\%=\boxed{12.5\%}
\end{aligned}
$$

**2. Explain the difference**

Expanded CAPM adds 1.2 percentage points above the unscaled market premium; build-up adds a 0.5-point industry premium instead. Build-up therefore comes out 0.7 points lower. More lines in a spreadsheet do not necessarily mean more risk.

CAPM assumes diversified investors. An owner with most of their wealth in one firm may care about risks that diversification would otherwise spread away.

> [!NOTE]
> Beta measures market-related risk, not every company-specific risk. Do not add the build-up industry premium automatically to expanded CAPM.

*Source pattern: Example 4, pp.426–429; practice Q7. Inputs adapted.*

---

## Variant: 9 — Compare return models without knowing the risk-free rate

**Abstract:** *Subtract the two models. Shared inputs cancel, leaving the industry premium plus the difference between an unscaled and beta-scaled market premium.*

> A firm has beta 0.8, equity risk premium 6%, size premium 2%, company-specific premium 1.5%, and industry premium 1%. Both models use the same unspecified risk-free rate. By how much does build-up exceed expanded CAPM? What industry premium would make the two models equal, holding everything else fixed?

<span class="jargon-unlock">**Expanded CAPM. What is it?** $r_X=r_f+\beta ERP+s+c$. **Build-up. What is it?** $r_B=r_f+ERP+s+i+c$. Here $r_X,r_B$ are required equity returns, $r_f$ risk-free rate, $\beta$ market sensitivity, $ERP$ equity risk premium, $s$ size premium, $c$ company premium, and $i$ industry adjustment. An adjustment can be negative when the industry warrants a lower required return.</span>

**1. Cancel the common terms**

The risk-free rate is missing because we do not need it. Neither do we need to carry identical size and company premiums through two long sums.

$$
r_B-r_X=(1-\beta)ERP+i=(1-0.8)(6\%)+1\%=\boxed{2.2\text{ percentage points}}
$$

**2. Solve backward for equality**

Set the difference to zero. The industry adjustment must offset the extra 1.2 percentage points build-up gets from using an unscaled market premium.

$$
i=(\beta-1)ERP=(0.8-1)(6\%)=\boxed{-1.2\%}
$$

The positive 1% industry premium in the question cannot produce equality. Calling everything a “premium” should not prevent the algebra from noticing a discount.

> [!NOTE]
> Unknown common inputs cancel when comparing models. The 2.2-point difference is not either model's total cost of equity.

*Source pattern: practice Q12 and solution p.465; inverse is algebra from the same models.*

---

## Variant: 10 — Borrow the business risk, not the peer's debt structure

**Abstract:** *Remove the peer's leverage effect from beta, then add the target's leverage effect. Use each company's own tax rate and debt-to-equity ratio.*

> Public peers have an average levered beta of 1.21, debt/equity of 50%, and tax rate of 21.6%. The private target has debt/equity of 25% and a tax rate of 18%. Using the module's unlevering convention, calculate the target's beta. If its risk-free rate is 3% and equity risk premium 6%, calculate its CAPM cost of equity.

<span class="jargon-unlock">**Beta. What is it?** Sensitivity of returns to market movements. **Leverage. What does it mean?** Use of debt, which increases risk borne by shareholders. **Unlevered beta. What is it?** Business-risk beta after removing the modeled debt effect: $\beta_U=\beta_L/[1+(1-T)D/E]$, where $\beta_L$ is levered beta, $T$ tax rate, and $D/E$ debt divided by equity. **CAPM. What is it?** Cost of equity equals risk-free rate plus beta times the equity risk premium.</span>

**1. Remove peer leverage**

The denominator strips away the peer shareholders' extra debt-related sensitivity.

$$
\beta_U=\frac{1.21}{1+(1-0.216)(0.50)}=\boxed{0.869253}
$$

**2. Add the target's financing, then price its market risk**

Keep full precision from Step 1.

$$
\begin{aligned}
\beta_{L,\text{target}}&=\frac{1.21}{1.392}[1+(1-0.18)(0.25)]=\boxed{1.047450}\\
r_e&=3\%+1.0474497(6\%)=\boxed{9.2847\%}
\end{aligned}
$$

Target beta lies above the unlevered beta but below the peer beta, consistent with lower borrowing. Copying the peer beta unchanged would also copy a debt burden the target does not have.

> [!NOTE]
> $D/E$ is not debt divided by total capital. The official 2025 errata correct Example 10's final beta from 0.8693 to 1.0475.

*Source pattern: Example 10, pp.443–444; official 2025 errata, p.19. CAPM inputs added for practice.*

---

## Variant: 11 — Actual financing, feasible financing, and wishful financing

**Abstract:** *Weight equity cost and after-tax debt cost using the financing mix appropriate to the valuation. A public peer's debt capacity is not automatically available to a private target.*

> A private firm has cost of equity 13%, pre-tax debt cost 7.5%, and tax rate 17%. Current debt/total capital is 2%; a feasible target is 10%; public peers use 20%. Holding component costs fixed only for this comparison, calculate WACC at all three weights. Which mix fits a controlling buyer able to implement the feasible target? What happens at zero debt?

<span class="jargon-unlock">**WACC. What is it?** Weighted average cost of capital: $WACC=w_Dr_D(1-T)+(1-w_D)r_E$, where $w_D$ is debt's share of total capital, $r_D$ pre-tax debt cost, $T$ tax rate, and $r_E$ equity cost. **Capital structure. What is it?** The mix of debt and equity funding. Market-value weights are normally relevant; use the supplied valuation weights here.</span>

**1. Allow for the tax saving on interest**

After-tax debt cost is $7.5\%(1-0.17)=6.225\%$. Under the stated fixed-cost assumption, substituting some cheaper debt for equity lowers WACC.

$$
\begin{aligned}
WACC_{2\%}&=0.02(6.225\%)+0.98(13\%)=\boxed{12.8645\%}\\
WACC_{10\%}&=0.10(6.225\%)+0.90(13\%)=\boxed{12.3225\%}\\
WACC_{20\%}&=0.20(6.225\%)+0.80(13\%)=\boxed{11.6450\%}
\end{aligned}
$$

**2. Choose a feasible assumption**

The controlling buyer can use the 10% feasible target. The 20% case is arithmetic, not evidence that lenders will provide the money. With no debt, WACC equals the 13% equity cost.

> [!NOTE]
> More debt does not lower WACC forever: borrowing can change both component costs. The source later quotes 12.8% for current WACC; the stated inputs produce 12.8645%.

*Source pattern: Example 4 and knowledge check, pp.427–431; practice Q4.*

---

## Variant: 12 — Who gets paid for the buyer's improvements?

**Abstract:** *Value the target's own cash flows at a target-appropriate rate. Then identify improvement or synergy value separately before deciding how much to offer the seller.*

> A target generates next-year FCFF of €5m, growing perpetually at 2%. Its appropriate WACC is 12%. A buyer's own WACC is 8%. Calculate the target's standalone operating value and the result of incorrectly using the buyer's rate. Separately, the buyer expects achievable synergies with present value €15m, net of implementation costs. What is its total investment value at the target-appropriate standalone valuation?

<span class="jargon-unlock">**FCFF and WACC. What are they?** Cash available to all capital providers and the weighted return required for its risk. **Standalone value. What is it?** Value without this buyer's special benefits. **Synergies. What are they?** Additional benefits from combining businesses. **Investment value. What is it?** Value to a particular buyer. A growing cash stream has value $FCFF_1/(r-g)$, where $r$ is its appropriate discount rate and $g$ perpetual growth.</span>

**1. See what the discount-rate shortcut gives away**

The target's risk does not vanish because its buyer has a larger stationery budget.

$$
V_{\text{standalone}}=\frac{5}{0.12-0.02}=\boxed{\text{EUR }50\text{m}},\qquad V_{\text{buyer-rate shortcut}}=\frac{5}{0.08-0.02}=\boxed{\text{EUR }83.33\text{m}}
$$

**2. Add identified benefits separately**

The supplied €15m is already a present value, so do not discount it again.

$$
V_{\text{investment}}=50+15=\boxed{\text{EUR }65\text{m}}
$$

The €15m is the buyer's total incremental value under these assumptions, not a mandatory payment to the seller. Paying €65m gives the seller all of it. A strategic buyer may justify more than a financial buyer because it can realize additional combinations of benefits.

> [!NOTE]
> Use the risk and feasible financing of the target's cash flows. An offer can share improvement value, but a lower buyer-wide WACC does not establish that value.

*Source pattern: pp.425, 431–432; practice Q2, Q5–6. Inputs adapted.*

---

## Variant: 13 — A control premium is not the same-sized control discount

**Abstract:** *A premium starts from the smaller minority value; the reverse discount starts from the larger control value. Divide by one plus the premium to reverse it.*

> A company's controlling equity value is €125m. The applicable control premium over an otherwise identical marketable minority basis is 25%. Find the equivalent minority-basis value of all equity and the discount for lack of control. Then reverse the calculation to check your answer.

<span class="jargon-unlock">**Control premium. What is it?** Extra value for rights to direct the company, measured relative to a non-controlling value. **DLOC. What is it?** Discount for lack of control: $DLOC=1-1/(1+CP)$, where $CP$ is the control premium expressed as a decimal. **Minority-basis value of all equity. What does that mean?** A valuation basis applied to the whole equity amount before selecting a particular ownership percentage.</span>

**1. Reverse the original increase**

The €125m already includes the 25% premium. Removing it means division by 1.25, not a 25% subtraction.

$$
V_{\text{minority basis}}=\frac{125}{1.25}=\boxed{\text{EUR }100\text{m}},\qquad DLOC=1-\frac{1}{1.25}=\boxed{20\%}
$$

**2. Check both directions**

The premium and discount both represent €25m, but they divide that amount by different starting values.

$$
\frac{125-100}{100}=25\%,\qquad \frac{125-100}{125}=20\%,\qquad CP=\frac{1}{1-0.20}-1=\boxed{25\%}
$$

Percentages have a home address: their denominator. Moving house changes the percentage even when the euro amount stays put.

> [!NOTE]
> Convert the premium before applying a DLOC. A 25% premium reverses with a 20% discount, not 25%.

*Source pattern: Equation 4 and Example 5, p.433. Inputs adapted.*

---

## Variant: 14 — Two discounts, one minority stake

**Abstract:** *Apply control and marketability discounts to what remains, then take the ownership share. Discounts multiply; adding them removes some value twice.*

> A firm's controlling, marketable equity value is €20m. A 10% non-controlling stake requires a 20% DLOC and a 15% DLOM. Neither adjustment is already reflected in the starting value. Calculate the stake value and total discount. If instead the total discount were 36% with the same DLOC, infer the DLOM.

<span class="jargon-unlock">**DLOC and DLOM. What are they?** Discounts for lack of control and lack of marketability. The first reflects missing decision rights; the second limited ability to sell. **Combined discount. What is it?** $d=1-(1-a)(1-b)$, where $a$ is DLOC and $b$ DLOM. **Pro rata stake. What does that mean?** The ownership percentage times total equity value before stake-specific adjustments.</span>

**1. Apply discounts sequentially**

The investor starts with a €2m proportional claim. A 20% control discount leaves €1.6m; the marketability discount applies to that smaller amount.

$$
\begin{aligned}
V_{\text{stake}}&=20(0.10)(0.80)(0.85)=\boxed{\text{EUR }1.36\text{m}}\\
d&=1-(0.80)(0.85)=\boxed{32\%}
\end{aligned}
$$

**2. Solve the inverse case**

A total discount of 36% means 64% survives. Remove the known control factor to find the surviving marketability factor.

$$
DLOM=1-\frac{1-0.36}{1-0.20}=\boxed{20\%}
$$

Adding 20% and 15% would give 35%, understating the first stake by €60,000. The discounts do not each get a fresh copy of the original company to nibble on.

> [!NOTE]
> Combined discount is less than the sum when both discounts are positive. Establish the equity basis before applying either one.

*Source pattern: Equation 5, Example 7, pp.435–436; practice Q15. Inputs adapted.*

---

## Variant: 15 — The discount that has already been taken

**Abstract:** *Read the starting valuation's rights and liquidity assumptions before adjusting it. A private-company label is not permission to apply every discount again.*

> Case A: A controlling equity valuation is €8m and explicitly already includes a 20% marketability discount. Value a 25% non-controlling stake using a 10% DLOC. Case B: An otherwise separate company has marketable minority-basis equity value €10m from public trading comparables. Value a 25% stake using a 20% DLOM; no additional control adjustment is warranted by the facts.

<span class="jargon-unlock">**Valuation basis. What is it?** The ownership rights and marketability assumptions already included in a value. **DLOC. What is it?** Discount for lack of control. **DLOM. What is it?** Discount for lack of marketability. **Public trading comparables. What are they?** Similar listed companies whose share prices usually represent readily tradable, non-controlling holdings.</span>

**1. Case A needs only the missing control adjustment**

The €8m has already been reduced for difficulty selling. Applying that discount again would charge the investor twice for the same locked exit.

$$
V_A=8(0.25)(1-0.10)=\boxed{\text{EUR }1.80\text{m}}
$$

**2. Case B needs only the missing marketability adjustment**

The starting value already represents minority rights under the stated facts.

$$
V_B=10(0.25)(1-0.20)=\boxed{\text{EUR }2.00\text{m}}
$$

These are separate cases, not two competing valuations of one firm. Control rights depend on actual voting and contractual arrangements; percentage ownership alone is not a complete legal description.

> [!NOTE]
> Apply only adjustments absent from the starting basis. A cash-flow valuation is controlling only when its cash flows and financing assumptions support that interpretation.

*Source pattern: pp.433–436 and 446, including the Starbeam knowledge check. Inputs adapted.*

---

## Variant: 16 — Estimate a marketability discount with a put option

**Abstract:** *Under this module's option convention, select the put struck near the forward share price, then divide its premium by today's share price. The forward helps choose the option; it is not the discount's denominator.*

> A non-dividend-paying comparable trades at €29.70. The annual continuously compounded risk-free rate is 4%; the horizon is three months. Put premiums are €1.25, €3.75, and €6.95 for strikes €25, €30, and €35, respectively. Using the module's forward-at-the-money convention, estimate DLOM and apply it to a €2m marketable minority interest.

<span class="jargon-unlock">**Put option. What is it?** A right to sell at a specified strike price; its premium is its current price. **Forward-at-the-money. What does it mean?** The strike is near the share's forward price, $F=S_0e^{rT}$, where $S_0$ is today's price, $r$ annual continuously compounded rate, $T$ years, and $e$ the exponential constant. **DLOM. What is it?** Discount for lack of marketability, estimated here as put premium divided by today's share price.</span>

**1. Match the strike to the horizon**

Three months is 0.25 years. There are no dividends to adjust for.

$$
F=29.70e^{0.04(0.25)}\approx\boxed{\text{EUR }30.00}
$$

**2. Use the €30-strike put and today's share price**

The €3.75 premium measures the modeled protection cost relative to an asset costing €29.70 now.

$$
DLOM=\frac{3.75}{29.70}=\boxed{12.6263\%},\qquad V=2\left(1-\frac{3.75}{29.70}\right)=\boxed{\text{EUR }1.7475\text{m}}
$$

A put protects against price falls for a limited period. It does not summon a buyer for the private shares. The map is not the territory: this is an estimate of a marketability cost, not a liquid market delivered in an envelope.

> [!NOTE]
> Divide by spot, not strike or forward. Do not treat an annual 4% rate as a three-month return; this question explicitly specifies annual continuous compounding.

*Source pattern: Example 6, p.434; practice Q10 and solution p.465. Stake amount added.*

---

## Variant: 17 — Capitalize next year's cash, then subtract debt

**Abstract:** *Grow the latest FCFF once, divide by WACC minus perpetual growth, and subtract debt's market value. A business valuation and a shareholder valuation are different stopping points.*

> A stable firm produced FCFF of €2m in the year just ended. Cash flow is expected to grow 3% forever. WACC is 11%. Debt has market value €4m but book value €5m. There are no non-operating assets or other claims. Calculate enterprise value and equity value before ownership discounts.

<span class="jargon-unlock">**FCFF. What is it?** Cash available to lenders and shareholders together. **Capitalized cash flow method. What is it?** A stable-growth valuation: $EV_0=FCFF_1/(WACC-g)$, where $EV_0$ is today's enterprise value, $FCFF_1$ next-year cash flow, $WACC$ weighted required return, and $g$ perpetual growth. **Book value. What is it?** An accounting carrying amount, which can differ from today's market value.</span>

**1. Move the cash flow forward one year**

The €2m has already been earned. The buyer is purchasing future cash flows.

$$
FCFF_1=2(1.03)=\boxed{\text{EUR }2.06\text{m}},\qquad EV_0=\frac{2.06}{0.11-0.03}=\boxed{\text{EUR }25.75\text{m}}
$$

**2. Leave the lenders their share**

Debt is a claim on the business. Subtract its market value to find what remains for shareholders.

$$
E_0=25.75-4=\boxed{\text{EUR }21.75\text{m}}
$$

The required return exceeds growth, so the perpetuity is finite. Using book debt would give €20.75m and understate equity by €1m.

> [!NOTE]
> FCFF/WACC gives enterprise value. Subtract debt once. Book debt is only a proxy when justified; use a supplied market value.

*Source pattern: Equations 7 and 10, Example 8, pp.438–439. Inputs adapted.*

---

## Variant: 18 — FCFE already belongs to shareholders

**Abstract:** *Discount shareholder cash flow at the cost of equity. Do not subtract debt again after using a cash flow that already reflects debt financing.*

> A stable firm has expected next-year FCFE of €1.8m, perpetual growth 3%, and cost of equity 12%. A separate, internally consistent FCFF valuation gives enterprise value €25m and debt value €5m, with no other adjustments. Calculate equity directly from FCFE and reconcile the two approaches.

<span class="jargon-unlock">**FCFE. What is it?** Free cash flow to equity: cash for shareholders after operating investment and debt-related cash flows, including net borrowing. **Cost of equity. What is it?** Shareholders' required return. $E_0=FCFE_1/(r_e-g)$, where $E_0$ is equity value today, $FCFE_1$ next-year shareholder cash flow, $r_e$ equity cost, and $g$ growth. **Enterprise value. What is it?** Operating value before separating lenders' and owners' claims.</span>

**1. Use the shareholder discount rate**

The question already supplies next-year FCFE. Growing it again would quietly award the buyer a second Year 1.

$$
E_0=\frac{1.8}{0.12-0.03}=\boxed{\text{EUR }20\text{m}}
$$

**2. Reconcile from enterprise value**

The second route values the whole operation, then removes the lenders' claim.

$$
E_0=25-5=\boxed{\text{EUR }20\text{m}}
$$

Subtracting €5m from the FCFE answer would produce €15m, charging shareholders twice for financing. Agreement between methods requires consistent cash-flow and financing assumptions; it is not guaranteed for unrelated forecasts.

> [!NOTE]
> FCFE → cost of equity → equity directly. FCFF → WACC → enterprise value → subtract debt.

*Source pattern: p.421 and Equation 10, p.438. Inputs constructed to provide an independent valuation check.*

---

## Variant: 19 — Growth timing and the assumptions hidden in a price

**Abstract:** *Changing growth can change both next year's cash flow and the capitalization rate. State when the change begins before touching either input.*

> Latest annual FCFF is €10m and WACC is 12%. Case A: growth becomes 2% immediately and stays there. Case B: cash flow first grows 5% next year, then grows 2% forever. Value each case. Separately, what perpetual growth rate is implied by enterprise value €150m if growth begins immediately from the €10m base? Explain what fails if perpetual growth is 12% or more.

<span class="jargon-unlock">**Capitalization rate. What is it?** The discount rate minus perpetual growth, $r-g$. **Implied growth. What does it mean?** The growth assumption needed to make a model equal an observed valuation. For latest cash flow $C_0$, value is $V=C_0(1+g)/(r-g)$, where $r$ is WACC and $g$ starts immediately. All cash flows here belong to the whole firm.</span>

**1. Write the first future cash flow separately**

Both cases have 2% growth after Year 1, but they begin with different Year 1 cash amounts.

$$
V_A=\frac{10(1.02)}{0.12-0.02}=\boxed{\text{EUR }102\text{m}},\qquad V_B=\frac{10(1.05)}{0.12-0.02}=\boxed{\text{EUR }105\text{m}}
$$

**2. Solve backward for the price's growth assumption**

Rearranging $V(r-g)=C_0(1+g)$ gives:

$$
g=\frac{Vr-C_0}{V+C_0}=\frac{150(0.12)-10}{150+10}=\boxed{5\%}
$$

At $g=r=12\%$, the denominator is zero. Above it, the formula produces a negative figure even though all projected cash flows are positive: the discounted series does not converge. That is a broken assumption, not a bargain company.

> [!NOTE]
> With positive perpetual cash flows, require $r>g$. The 2025 errata change Example 8's next cash flow; the 2026 errata instead clarify delayed growth. Do not mix their timelines.

*Source pattern: Example 8 and Equation 7, pp.438–440; official errata for both editions. Inputs adapted.*

---

## Variant: 20 — Growth needs reinvestment: use the module's assumption carefully

**Abstract:** *In the module's simplified capitalization setup, reinvestment equals growth divided by WACC. Apply that convention when specified; it is not a universal identity for every company.*

> Use LM6's stated convention $RIR=g/WACC$. Expected next-year EBIT is €9m, tax is 25%, WACC 12%, and perpetual growth 4%. Calculate reinvestment rate, next-year FCFF, and enterprise value. What growth rate does the same convention imply if the reinvestment rate is 25% instead?

<span class="jargon-unlock">**EBIT. What is it?** Earnings before interest and tax. **Reinvestment rate, RIR. What is it?** The share of after-tax operating earnings put back into operations instead of paid to capital providers. Here $RIR=g/WACC$, with $g$ growth and $WACC$ weighted required return. **FCFF. What is it?** Cash available to all capital providers: $FCFF=EBIT(1-T)(1-RIR)$, where $T$ is tax rate.</span>

**1. Deduct the money required to support growth**

The question explicitly adopts the module's simplified relationship. Growth is not an extra feature installed for free.

$$
RIR=\frac{0.04}{0.12}=\boxed{33.3333\%},\qquad FCFF_1=9(0.75)\left(1-\frac13\right)=\boxed{\text{EUR }4.5\text{m}}
$$

**2. Capitalize the distributable cash**

The EBIT input is already next year's figure, so no additional growth multiplication is required.

$$
EV=\frac{4.5}{0.12-0.04}=\boxed{\text{EUR }56.25\text{m}},\qquad g_{\text{alternative}}=0.25(0.12)=\boxed{3\%}
$$

Under this simplified convention, with next-year after-tax EBIT held fixed, the expression reduces to after-tax EBIT divided by WACC. It does not establish that growth is economically irrelevant in other models.

> [!NOTE]
> Equations 8–9 use $RIR=g/WACC$. Treat this as the specified module convention; do not overwrite an explicitly supplied reinvestment forecast.

*Source pattern: Equations 8–9, p.438; knowledge check p.447, Q1. Inputs adapted.*

---

## Variant: 21 — Excess earnings: pay the tangible assets first

**Abstract:** *Charge working capital and fixed assets their required returns. Only the remaining earnings support intangible value; add tangible asset value back after capitalizing that remainder.*

> A small debt-free business has normalized current annual earnings of €120,000, working capital worth €200,000, and fixed assets worth €800,000. Required returns are 5% on working capital, 11% on fixed assets, and 12% on intangible earnings. Excess earnings grow 3% forever. Use the excess earnings method to estimate intangible value and total firm value.

<span class="jargon-unlock">**Excess earnings method. What is it?** A method assigning ordinary required earnings to tangible assets and valuing the remaining earnings separately. **Tangible and intangible assets. What are they?** Tangible assets include physical operating assets; intangibles include technology and customer relationships. Here $RI=NI-WC\,r_W-FA\,r_F$, where $RI$ is excess earnings, $NI$ normalized earnings, $WC$ working capital, $FA$ fixed assets, and $r_W,r_F$ their required returns. Intangible value is $RI(1+g)/(r_I-g)$, where $r_I$ is the intangible earnings discount rate and $g$ growth.</span>

**1. Give tangible capital its required earnings**

The €120,000 is not all evidence of a valuable brand. Some of it is the return needed just to justify the money tied up in operations.

$$
RI=120{,}000-200{,}000(0.05)-800{,}000(0.11)=\boxed{\text{EUR }22{,}000}
$$

**2. Value the remainder and add the assets**

Grow current excess earnings once to get next year's amount.

$$
\begin{aligned}
V_I&=\frac{22{,}000(1.03)}{0.12-0.03}=\boxed{\text{EUR }251{,}777.78}\\
V_{\text{firm}}&=200{,}000+800{,}000+251{,}777.78=\boxed{\text{EUR }1{,}251{,}777.78}
\end{aligned}
$$

Only €251,777.78 is attributed to intangibles. Capitalizing all earnings and then adding tangible assets would make those assets earn their value twice.

> [!NOTE]
> Asset charges are annual earnings deductions, not deductions of the entire asset balances. EEM is especially relevant to intangibles and small businesses, not a default for every firm.

*Source pattern: Equations 11–12 and Example 9, pp.440–441.*

---

## Variant: 22 — Small changes in asset charges can move value substantially

**Abstract:** *Changing an asset's required return changes excess earnings before the capitalization step. Changing the intangible discount rate changes the capitalization step itself.*

> A debt-free firm has current normalized earnings €120,000, working capital €200,000, and fixed assets €800,000. Correct required returns are 4%, 10%, and 11% for working capital, fixed assets, and intangible earnings respectively. Excess earnings grow 3% forever. Find its EEM value. Then find normalized earnings that would make intangible value exactly zero, keeping all other inputs fixed.

<span class="jargon-unlock">**EEM. What is it?** Excess earnings method, which separates tangible asset value from the value of earnings remaining after required tangible-asset returns. **Residual income. What is it here?** $RI=NI-WC\,r_W-FA\,r_F$, with normalized income $NI$, working capital $WC$, fixed assets $FA$, and their return rates $r_W,r_F$. Intangible value equals $RI(1+g)/(r_I-g)$, where $g$ is growth and $r_I$ its discount rate.</span>

**1. Recalculate both the numerator and denominator**

The lower tangible-asset charges leave more earnings attributed to intangibles. The lower intangible discount rate then makes that stream more valuable.

$$
RI=120{,}000-200{,}000(0.04)-800{,}000(0.10)=\boxed{\text{EUR }32{,}000}
$$

Now capitalize those earnings and add the tangible assets.

$$
V=200{,}000+800{,}000+\frac{32{,}000(1.03)}{0.11-0.03}=\boxed{\text{EUR }1{,}412{,}000}
$$

**2. Find the zero-intangible boundary**

Intangible value is zero when normalized earnings merely cover tangible capital's required returns.

$$
NI_{\text{boundary}}=200{,}000(0.04)+800{,}000(0.10)=\boxed{\text{EUR }88{,}000}
$$

Below that amount, the mechanical model gives negative residual value. That signals inadequate returns under these assumptions; it is not proof that every patent has a negative selling price.

> [!NOTE]
> The source solution on p.448 prints €32,000,000 residual income, but its inputs and subsequent €412,000 intangible value require €32,000.

*Source pattern: knowledge check pp.447–448, Q2; zero-residual case follows Equation 11.*

---

## Variant: 23 — A two-stage valuation with a properly dated terminal value

**Abstract:** *Discount explicit cash flows and terminal value separately. The terminal value sits at the end of the forecast and uses the following year's cash flow.*

> A firm expects FCFF of €2m at the end of Year 1 and €3m at the end of Year 2. From Year 3, FCFF grows 3% annually forever from the Year 2 base. WACC is 10%, debt's current market value is €5m, and no non-operating assets exist. Calculate terminal value at Year 2, enterprise value today, and equity value today.

<span class="jargon-unlock">**FCFF. What is it?** Cash available to lenders and owners after operating investment. **WACC. What is it?** Their weighted required return. **Terminal value. What is it?** Value at the forecast's end of all subsequent cash flows: $TV_n=FCFF_{n+1}/(r-g)$, where $n$ is the final explicit year, $r$ WACC, and $g$ growth after that year. Enterprise value is the present value of the operating cash flows.</span>

**1. Value Year 3 onward at the end of Year 2**

Year 2 cash flow is paid separately. Terminal value begins with Year 3 cash flow, avoiding a duplicate payment.

$$
FCFF_3=3(1.03)=\boxed{\text{EUR }3.09\text{m}},\qquad TV_2=\frac{3.09}{0.10-0.03}=\boxed{\text{EUR }44.142857\text{m}}
$$

**2. Bring all values to today**

Year 2 cash flow and terminal value share a date, so they share the same two-year discount factor.

$$
EV_0=\frac{2}{1.10}+\frac{3+44.142857}{1.10^2}=\boxed{\text{EUR }40.7792\text{m}}
$$

**3. Deduct today's debt claim**

The debt value is already current, so no extra discounting is needed.

$$
E_0=40.7792208-5=\boxed{\text{EUR }35.7792\text{m}}
$$

Terminal value contributes about 89.5% of enterprise value. Most of the price rests on the distant forecast; giving the early years extra decimal places will not strengthen that foundation.

> [!NOTE]
> Use terminal growth in $FCFF_{n+1}$ and in $r-g$. Example 12 and its 2025 erratum conflict on this timing; this original case states it explicitly.

*Source pattern: Equation 6, p.437; Example 12, pp.449–451. Inputs adapted.*

---

## Variant: 24 — A sale multiple can also supply terminal value

**Abstract:** *An exit multiple values the business on the future sale date. Convert the relevant future operating metric into terminal enterprise value, then discount it with the explicit cash flows.*

> A firm expects FCFF of €1m at the end of each of Years 1 and 2. At the end of Year 2, normalized annual EBITDA is expected to be €4m. A justified exit enterprise-value/EBITDA multiple is 6 times. Use a 10% WACC. The Year 2 cash distribution and sale proceeds are separate. Calculate enterprise value today and compare the exit value with a €3m first post-sale FCFF estimate.

<span class="jargon-unlock">**Exit multiple. What is it?** A valuation ratio applied when the investor expects to sell. **EBITDA. What is it?** Earnings before interest, taxes, depreciation and amortization. **FCFF. What is it?** Cash available to all capital providers. **WACC. What is it?** The weighted required return used to discount that cash. **Terminal enterprise value. What is it?** Value of operations at the sale date, before separating debt and equity.</span>

**1. Estimate sale-date operating value**

A multiple is a compact market assumption, not a guarantee of a buyer in two years.

$$
TV_2=6(4)=\boxed{\text{EUR }24\text{m}}
$$

**2. Discount the cash received on each date**

The Year 2 total is €1m operating cash plus €24m sale value.

$$
EV_0=\frac{1}{1.10}+\frac{1+24}{1.10^2}=\boxed{\text{EUR }21.5702\text{m}}
$$

The first post-sale cash estimate implies a capitalization rate of $3/24=12.5\%$. At a 10% required return, a constant-growth interpretation would imply $10\%-12.5\%=\boxed{-2.5\%}$ annual growth. That is a useful consistency question for the selected multiple.

> [!NOTE]
> An enterprise multiple produces enterprise value, not shareholder sale proceeds. Compare its implied assumptions with the cash-flow forecast before trusting the exit price.

*Source pattern: terminal-value alternatives, p.437, Exhibit 7; capitalization-rate interpretation p.438. Inputs adapted.*

---

## Variant: 25 — Why sales and profit multiples disagree

**Abstract:** *Apply each multiple to its matching metric. If the target's profit margin differs from peers, sales-based and profit-based values can disagree for an economically sensible reason.*

> A private business has annual sales €50m, EBIT €7m, and debt market value €10m. Comparable companies have EV/Sales of 2 times and EV/EBIT of 16 times. There are no excess assets or other adjustments. Estimate enterprise and equity value with each multiple, then compare the target's operating margin with the margin implied by the peer ratios.

<span class="jargon-unlock">**EV. What is it?** Enterprise value: value of business operations attributable to all capital providers. **EBIT. What is it?** Earnings before interest and taxes. **Operating margin. What is it?** EBIT divided by sales. **Multiple. What is it?** Value divided by a financial metric; multiplying the ratio by the matching target metric yields a value estimate.</span>

**1. Keep each multiple attached to its denominator**

Sales measures activity; EBIT measures what survives operating expenses. They are not interchangeable descriptions of the same euro.

$$
\begin{aligned}
EV_{\text{sales}}&=2(50)=\boxed{\text{EUR }100\text{m}},&E_{\text{sales}}&=100-10=\boxed{\text{EUR }90\text{m}}\\
EV_{\text{EBIT}}&=16(7)=\boxed{\text{EUR }112\text{m}},&E_{\text{EBIT}}&=112-10=\boxed{\text{EUR }102\text{m}}
\end{aligned}
$$

**2. Explain the gap through margins**

Dividing the two peer ratios cancels enterprise value and leaves EBIT/sales.

$$
\text{Target margin}=\frac7{50}=\boxed{14\%},\qquad \text{Implied peer margin}=\frac{2}{16}=\boxed{12.5\%}
$$

The target earns more EBIT per euro of sales. Its higher profit-based valuation therefore has a reason; the calculator has not taken sides. For averages drawn from different peer observations, the ratio is an implied benchmark, not necessarily the average actual margin.

> [!NOTE]
> Multiples require comparable risk, growth, and accounting. Two different estimates are a prompt to investigate assumptions, not automatically an arithmetic error.

*Source pattern: Example 10, p.444; practice Q14. Inputs adapted.*

---

## Variant: 26 — Build a composite sales multiple without weighting twice

**Abstract:** *Weight segment EV/Sales multiples by segment revenue shares, then multiply by total revenue. Check by valuing each segment separately and adding.*

> A private group's three divisions have sales of £70m, £25m, and £5m. Relevant single-business public comparables have EV/Sales multiples of 2.8, 1.1, and 8.0 respectively. Calculate the composite multiple and enterprise value. Which division contributes least value? If a set of whole-company peers already matches this business mix, should you apply these segment weights again to each peer's whole-company multiple?

<span class="jargon-unlock">**Composite multiple. What is it?** A weighted combination of valuation ratios representing a mixed business. **EV/Sales. What is it?** Enterprise value divided by revenue. For segment sales $S_i$ and matching multiple $m_i$, total value is $EV=\sum_i m_iS_i$. The equivalent composite multiple is $\sum_i(S_i/S)m_i$, where $S$ is total sales and $\sum$ means add across divisions.</span>

**1. Weight the ratios by revenue**

Total sales are £100m, so the weights are 70%, 25%, and 5%.

$$
M=0.70(2.8)+0.25(1.1)+0.05(8.0)=\boxed{2.635\text{ times}}
$$

**2. Value the group and check division by division**

Multiply the composite by total sales once.

$$
EV=2.635(100)=70(2.8)+25(1.1)+5(8)=\boxed{\text{GBP }263.5\text{m}}
$$

Division values are £196m, £27.5m, and £40m. The middle division contributes least, despite having more sales than the third. Revenue gets you into the calculation; the multiple decides its price tag.

Whole-company peers with an already matching mix need no second segment reconstruction. Their combined activities are already inside their ratios.

> [!NOTE]
> Weighted multiple × total sales equals sum of segment values. Do not multiply by segment revenue shares a second time.

*Source pattern: Examples 11 and 13, pp.444–457; knowledge check pp.457–458. Inputs scaled.*

---

## Variant: 27 — A negative EBITDA weight is a warning, not a verdict

**Abstract:** *EBITDA-weighted multiples can assign negative value to a loss-making division. Calculate the mechanical result, then test whether a different metric better fits that division's economics.*

> A group's divisions have EBITDA of £18.75m, £7.5m, and −£1.25m. Peer EV/EBITDA multiples are 8.2, 8.1, and 20. The third division is an early-stage operation with sales £5m and a suitable EV/Sales multiple of 8. Calculate the mechanical composite EBITDA multiple and enterprise value. Then use EBITDA multiples for the first two divisions and the sales multiple for the third.

<span class="jargon-unlock">**EBITDA. What is it?** Earnings before interest, taxes, depreciation and amortization. **EV/EBITDA. What is it?** Enterprise value divided by that earnings measure. **Negative weight. What does it mean here?** A division with a loss contributes negative EBITDA to the group total. **Hybrid segment valuation. What is it?** Valuing different divisions with different justified metrics and then adding the resulting values.</span>

**1. Calculate the mechanical answer honestly**

Total EBITDA is £25m. The corresponding weights are 75%, 30%, and −5%; they still sum to 100%.

$$
M=0.75(8.2)+0.30(8.1)-0.05(20)=\boxed{7.58\text{ times}},\qquad EV=7.58(25)=\boxed{\text{GBP }189.5\text{m}}
$$

**2. Inspect what the formula says about the loss-maker**

The last division contributes $-1.25(20)=-\text{GBP }25$m mechanically. Current losses alone do not prove a young business has negative economic value. That would turn an early investment phase into a permanent sentence.

$$
EV_{\text{hybrid}}=18.75(8.2)+7.5(8.1)+5(8)=\boxed{\text{GBP }254.5\text{m}}
$$

The hybrid replaces −£25m with +£40m, increasing the estimate by £65m. The higher answer is not automatically right: its sales multiple still needs comparable economics and credible prospects.

> [!NOTE]
> A negative denominator makes an earnings multiple difficult to interpret. If aggregate EBITDA is zero, the composite EBITDA multiple is undefined.

*Source pattern: Examples 11 and 13, pp.445–457. Inputs scaled; hybrid follows the alternative explicitly discussed in the source.*

---

## Variant: 28 — Apply discounts to a clearly identified market valuation basis

**Abstract:** *Normalize the ownership basis before combining valuation indications. Discount consistently and carry full precision; a rounded discount can quietly move a large valuation.*

> Two valuation methods give £100m and £80m for a debt-free company's whole equity, explicitly on a controlling, marketable basis after all necessary comparability adjustments. Apply DLOC of 13% and DLOM of 16.8%, then give the two resulting minority, non-marketable indications equal weight. Separately, find the combined discount if the control input had instead been a 15% control premium, not a 13% DLOC.

<span class="jargon-unlock">**DLOC and DLOM. What are they?** Discounts for lack of control and lack of marketability. **Equal weighting. What does it mean?** Taking the arithmetic average of equally credible indications. **Control premium, CP. What is it?** An increase from minority to controlling value; its reverse discount is $1-1/(1+CP)$. The retained value after two discounts is $(1-DLOC)(1-DLOM)$.</span>

**1. Keep the exact retention factor**

Using a 13% DLOC, the surviving fraction is $0.87(0.832)=0.72384$.

$$
V_1=100(0.72384)=\boxed{\text{GBP }72.384\text{m}},\qquad V_2=80(0.72384)=\boxed{\text{GBP }57.9072\text{m}}
$$

**2. Average comparable indications**

Both numbers now describe the same rights and liquidity.

$$
V_{\text{average}}=\frac{72.384+57.9072}{2}=\boxed{\text{GBP }65.1456\text{m}}
$$

The combined discount is 27.616%. With a 15% control premium instead, it is $1-0.832/1.15=\boxed{27.6522\%}$. The difference is small in percentage terms but real in money.

> [!NOTE]
> Public trading prices normally reflect minority holdings. Example 13 applies a DLOC to its stated public-derived indications; do not generalize that into an automatic extra discount.

*Source pattern: Examples 5, 7 and 13, pp.433–456. This case explicitly supplies a controlling basis to avoid ambiguous double counting.*

---

## Variant: 29 — Acquisition multiples may already contain control and synergies

**Abstract:** *A transaction price is evidence about the rights and benefits actually purchased. Separate buyer-specific synergies when appropriate before carrying the multiple to a standalone target.*

> A comparable acquisition has announced enterprise consideration with present value €60m: €54m upfront and €6m in expected contingent payments already valued today. The acquired firm's normalized EBITDA is €6m. The price includes €12m of identified buyer-specific synergy value unavailable to your target's buyer. Target EBITDA is €5m and debt is €10m. Estimate target equity using a synergy-adjusted transaction multiple; no further control premium is justified.

<span class="jargon-unlock">**Guideline transactions method. What is it?** Valuing a firm using multiples from acquisitions of comparable businesses. **Contingent consideration. What is it?** Extra payments depending on future milestones; the question supplies their present value. **Synergy. What is it?** An extra benefit from combining particular businesses. **EBITDA. What is it?** Earnings before interest, taxes, depreciation and amortization; an enterprise multiple values operations before deducting debt.</span>

**1. Identify the relevant acquisition price**

Total enterprise consideration is €60m, not just cash paid upfront. Remove the specifically identified synergy value to match the target's standalone economics.

$$
M_{\text{adjusted}}=\frac{54+6-12}{6}=\boxed{8\text{ times}}
$$

**2. Apply the adjusted multiple and subtract target debt**

The comparable acquisition already transfers control. Adding another control premium would charge a second admission fee for the same rights.

$$
EV_{\text{target}}=8(5)=\boxed{\text{EUR }40\text{m}},\qquad E_{\text{target}}=40-10=\boxed{\text{EUR }30\text{m}}
$$

Using the unadjusted 10-times multiple would yield €40m of equity, €10m higher. Removing synergies is possible here because their value is explicitly given; real transactions rarely arrive this neatly labelled.

> [!NOTE]
> Inspect control, synergies, contingent payments, payment form, and transaction date. A deal multiple is not automatically comparable simply because it is a real price.

*Source pattern: guideline transactions and control premiums, pp.446–447. Inputs adapted.*

---

## Variant: 30 — Use a prior transaction without inventing control value

**Abstract:** *A recent sale of the same company's shares can anchor the same class and ownership basis. Scaling its price does not transform minority rights into control rights.*

> Last month, an independent investor paid €0.9m for a 10% non-controlling stake in a private company. The transaction was orderly, and its price already reflects illiquidity. No new shares have been issued and no relevant conditions have changed. Estimate another 15% stake with identical rights and liquidity. Does the calculation establish the price of acquiring control?

<span class="jargon-unlock">**Prior transaction method. What is it?** Using actual previous trades in the target company's shares as valuation evidence. **Non-controlling stake. What is it?** An ownership interest without power to direct the company. **Illiquidity. What does it mean?** Difficulty selling quickly at a reasonable price. **Same-basis scaling. What is it?** Multiplying price in proportion to ownership only when relevant rights and conditions match.</span>

**1. Infer the whole-equity equivalent on that basis**

The investor paid €0.9m for one tenth of the equity. Divide by the ownership fraction, not the number 10.

$$
E_{\text{same basis}}=\frac{0.9}{0.10}=\boxed{\text{EUR }9\text{m}}
$$

**2. Price the matched stake**

All relevant rights and marketability conditions match by assumption.

$$
V_{15\%}=9(0.15)=\boxed{\text{EUR }1.35\text{m}}
$$

This does not establish a controlling acquisition price. Buying more shares can change what decisions you can make; the right to choose management is not simply another line of identical small parcels.

> [!NOTE]
> Check transaction date, independence, share class, dilution, rights, and liquidity. Do not apply another illiquidity discount when the price already reflects the same limitation.

*Source pattern: prior transaction method, p.442; comparability cautions pp.446–447. Inputs adapted.*

---

## Variant: 31 — Asset-based value: replace the accounting labels with current values

**Abstract:** *Value assets and liabilities on a consistent current basis, then subtract. The asset approach is only as complete as the asset list and the assumptions behind those values.*

> A private asset-holding company has cash €1m, property with book value €4m but appraised current value €7m, and equipment with book value €3m but current value €2m. Debt is worth €3m and other liabilities €1m; both equal their book amounts. The appraisal already includes all relevant realization costs and tax effects; there are no unrecorded assets. Calculate asset-based equity value and compare with book equity.

<span class="jargon-unlock">**Asset-based valuation. What is it?** Current value of assets less current value of related liabilities. **Book equity. What is it?** Accounting assets minus accounting liabilities. **Appraised value. What is it?** An estimated value on a stated valuation basis, rather than necessarily the amount recorded in the accounts.</span>

**1. Use current asset values consistently**

The property has gained €3m while the equipment has lost €1m relative to book. Neither change politely waits for the balance sheet to notice.

$$
E_{\text{asset basis}}=1+7+2-3-1=\boxed{\text{EUR }6\text{m}}
$$

**2. Reconcile the accounting difference**

The liability figures equal their book amounts, so only the asset revaluations explain the difference.

$$
E_{\text{book}}=1+4+3-3-1=\boxed{\text{EUR }4\text{m}},\qquad \Delta E=(7-4)+(2-3)=\boxed{\text{EUR }2\text{m}}
$$

The current asset approach gives €2m more equity. It does not prove that every operating company should be valued this way: a firm's customer relationships or operating organization may have value missing from a simple list of physical assets.

> [!NOTE]
> Use a consistent going-concern or realization basis. Asset-based value is not automatically forced-sale value, and book balances are not automatically market values.

*Source pattern: asset-based approach, p.437. Inputs adapted.*

---

## Variant: 32 — From earnings cleanup to the value of one shareholder's stake

**Abstract:** *Work in order: normalize operations, value the firm, subtract debt, then value the specified ownership interest. Do not let a correct formula answer the wrong ownership question.*

> A furniture firm reports EBITDA €4m, including CEO salary €0.3m; a market salary is €0.6m. After this and all other operating adjustments, the analyst independently forecasts base-year FCFF of €0.6m. WACC is 8%, perpetual growth 4%, and debt market value €6m. An independent market method uses sales €30m and EV/Sales 0.60. The owner holds 25%. For this exercise, both enterprise indications have been established on a controlling, marketable basis. Apply DLOC 20% and DLOM 15%. Compare the owner's stake values under the two methods.

<span class="jargon-unlock">**EBITDA. What is it?** Earnings before interest, taxes, depreciation and amortization. **FCFF and WACC. What are they?** Cash for lenders and owners together, and their weighted required return. **EV. What is it?** Enterprise value before subtracting debt to reach equity. **DLOC and DLOM. What are they?** Discounts for missing control rights and limited marketability. A growing cash stream is valued as $FCFF_1/(WACC-g)$, where $g$ is perpetual growth.</span>

**1. Normalize pay, but do not repeat the adjustment in FCFF**

Normalized EBITDA is $4-(0.6-0.3)=\boxed{\text{EUR }3.7\text{m}}$. The supplied FCFF already includes the salary adjustment. It is not another invitation to subtract €0.3m.

**2. Calculate firm value, then shareholder value**

The cash-flow method needs next year's cash; the market method uses the supplied sales multiple.

$$
\begin{aligned}
EV_{\text{income}}&=\frac{0.6(1.04)}{0.08-0.04}=\text{EUR }15.6\text{m},&E_{\text{income}}&=15.6-6=\text{EUR }9.6\text{m}\\
EV_{\text{market}}&=0.60(30)=\text{EUR }18\text{m},&E_{\text{market}}&=18-6=\text{EUR }12\text{m}
\end{aligned}
$$

**3. Price the actual interest**

Both discounts are required by the explicitly supplied basis. Their combined retained fraction is $0.80(0.85)=0.68$.

$$
\begin{aligned}
V_{\text{income stake}}&=9.6(0.25)(0.68)=\boxed{\text{EUR }1.632\text{m}}\\
V_{\text{market stake}}&=12(0.25)(0.68)=\boxed{\text{EUR }2.040\text{m}}
\end{aligned}
$$

The €0.408m difference comes from the valuation methods' operating assumptions, not the discounts. Averaging the answers would not, by itself, settle which assumptions deserve belief.

> [!NOTE]
> Normalize → value operations → subtract debt → apply ownership share and missing discounts. Check the starting rights basis before copying this sequence into another case.

*Source pattern: practice Q11–15 and solutions, pp.462–465. Valuation basis made explicit; final stake calculation added.*

<!-- Source scope: 2025 CFA Program Level II, Volume 5, Learning Module 6, Private Company Valuation, printed pp.407–465. Original teaching cases follow official equations, examples and practice-question patterns. Official 2025 errata: https://www.cfainstitute.org/sites/default/files/docs/programs/cfa-program/candidate-resources/2025-cfa-lii-curriculum-errata-notice.pdf . Growth-timing cross-check only: official 2026 errata, https://www.cfainstitute.org/sites/default/files/docs/programs/cfa-program/candidate-resources/2026-cfa-level-ii-errata.pdf . No prep-provider source used. -->
