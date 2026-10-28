# CFA Level II — Cost of Capital: Advanced Topics
## The entire chapter in six levels

*Based on the 2025 CFA Level II Corporate Issuers curriculum, Learning Module 3. Numerical illustrations are deliberately simplified unless identified as chapter case-study figures. The discussion includes the chapter's two mini-cases and covers all six learning outcomes.*

**The one question beneath this entire chapter:** What return must a company promise the people financing it, given what can go wrong?

Investors do not hand companies money because they admire the CEO's haircut. Lenders want their contractual payments. Shareholders want a sufficiently large upside because, in a bankruptcy, they stand at the back of the queue holding a motivational poster. The **cost of capital** is the price the business pays for making those people part with their money.

Start with the weighted-average cost of capital:

\[
\boxed{WACC=w_d r_d(1-T)+w_p r_p+w_e r_e}
\]

- **\(w_d,w_p,w_e\)**: target weights of debt, preferred equity, and common equity; sum to 1.
- **\(r_d\)**: *current marginal* pretax cost of debt, not the historical coupon.
- **\(r_p\)**: cost of preferred equity.
- **\(r_e\)**: required return on common equity.
- **\(T\)**: marginal tax rate **only to the extent incremental interest produces a usable tax deduction**.

Suppose a company targets 40% debt and 60% equity. Debt investors require 6%, equity investors 11%, and the marginal tax rate is 25%:

\[
WACC=0.40(0.06)(1-0.25)+0.60(0.11)=\boxed{8.4\%}.
\]

For an average-risk investment financed as part of this business, 8.4% is the relevant hurdle rate. It is **not** automatically the correct rate for a much riskier new project. A company selling electricity cannot justify a speculative cryptocurrency business merely because its historical WACC looks cheerful.

**Exam spine:** Understand the risk factors → estimate debt cost → estimate the market equity premium → estimate company equity cost → handle private and foreign companies → assess the complete capital structure.

---

## Level 1 — Why the cost of capital changes

The cost of debt begins with a risk-free rate and adds a spread for the possibility that the borrower disappoints its lenders:

\[
\boxed{r_d=r_f+\text{credit spread}}.
\]

The familiar CAPM makes a parallel argument for equity:

\[
\boxed{r_e=r_f+\beta\,ERP}.
\]

The **risk-free rate** is the base price of time. The **credit spread** compensates creditors for credit and other relevant debt risks. **ERP**, the equity risk premium, compensates the holder of a broad equity market for equity risk. **Beta** measures how strongly one company's stock moves with that market's excess return. These ingredients respond to two families of causes.

### A. Top-down: the world changes its price tag

| External factor | Mechanism | Typical effect |
|---|---|---|
| Available capital | More lenders and investors compete to supply funds | Greater supply generally lowers financing cost |
| Interest rates and inflation | Higher benchmark nominal yields increase the base financing rate | Higher nominal capital costs, all else equal |
| Business cycle | Recessions commonly widen credit spreads and required equity premiums | Financing becomes more expensive |
| Legal institutions and country risk | Weak investor protection, political instability, or volatile currencies increase uncertainty | Higher required returns |
| Corporate tax rules | Usable interest deductions shield taxable income | Lower **after-tax** debt cost |

A recession does not have to destroy a company's factory. It can merely persuade financiers to demand more compensation. The same factory, workers, and coffee machine suddenly carry a higher discount rate. Markets have a remarkable ability to make everyone's problems more expensive without changing a single physical object.

**Tax trap:** Debt at 8% with a usable 25% tax deduction costs 6% after tax. But if interest is not deductible, or the firm has already exhausted its applicable deduction limit, that 6% is a fantasy. The correct incremental debt cost remains 8%.

### B. Bottom-up: the company contributes its own chaos

| Company characteristic | Why financing becomes cheaper or dearer |
|---|---|
| Stable subscriptions, predictable cash flow | Lower uncertainty about servicing debt; often lower cost |
| Cyclical sales, high fixed operating costs | Small revenue falls can cause large profit declines; often higher cost |
| Few customers or regions | One lost customer or local shock can devastate results; higher risk |
| Tangible, liquid collateral | Creditors may recover more on default; often lower debt cost |
| Greater debt, weak interest coverage, poor liquidity | Higher probability of financial distress; typically wider spreads and higher equity risk |
| ESG exposures with financial consequences | Potential litigation, regulatory costs, lost sales, or governance failures alter risk and cash flows |

Imagine two companies. One collects predictable subscriptions from thousands of customers. The other sells luxury speedboats to four billionaires, two of whom are currently being investigated. Identical revenue last year tells you almost nothing about which deserves the lower financing rate. **Predictability is valuable because creditors cannot pay next month's coupon with last year's impressive PowerPoint.**

**Operating leverage** means high fixed operating costs: when revenue falls, earnings generally fall proportionally more. **Financial leverage** means debt magnifies the volatility of returns to equity and creates fixed payment commitments. Don't confuse the two; they can reinforce each other.

### Embedded rights: whose option is it?

- **Callable bond:** the issuer may refinance when rates fall. Investors dislike being kicked out of a good coupon; **higher initial yield** than comparable straight debt.
- **Putable bond:** investors can demand early repayment. They value the escape hatch; **lower initial yield**.
- **Convertible bond:** investors may exchange debt for shares. That upside option typically buys the issuer a **lower initial coupon/yield**, at the potential cost of future dilution.
- **Cumulative preferred stock:** unpaid preferred dividends accumulate and must be satisfied before common distributions; **lower required yield** than otherwise identical non-cumulative preferred.
- **Inferior-vote/inferior-cash-flow common shares:** investors may require more return to accept weaker rights.

Lower coupon today does not mean a free lunch forever. A put can force expensive refinancing; conversion can dilute owners. The financing terms simply move the pain around the calendar.

**ESG modeling warning:** If an environmental lawsuit already reduces your forecast cash flows, do not mechanically penalize the discount rate for exactly the same expected loss again. Double-counting risk is a sophisticated way to be wrong twice.

---

## Level 2 — Cost of debt: what would borrowing cost **today**?

**Priority: very high.** The historical interest expense or coupon is what management agreed to years ago. The cost of debt used in WACC asks what investors demand **now** for comparable new borrowing.

### 1. A liquid publicly traded straight bond

Use the bond's current **yield to maturity (YTM)**, preferably from a reasonably long maturity that is relevant to the firm's financing horizon. A more liquid shorter bond may provide better evidence than a stale price on a long bond.

A 5% coupon bond can have a 7% YTM. Its cost of debt estimate is closer to **7%**, not 5%. Coupon and required return are not synonyms; one is a contractual payment, the other is the market's current price of risk.

### 2. Thinly traded or non-traded debt: matrix pricing

Find traded bonds with similar rating, seniority, currency, maturity, and other relevant terms. Interpolate between their observed yields.

For illustration, comparable four-year debt yields **5%**, and eight-year debt yields **7%**. For a six-year issue:

\[
YTM_6=5\%+\frac{6-4}{8-4}(7\%-5\%)=\boxed{6\%}.
\]

This is **linear interpolation**, not a law of physics. An illiquid issuer may require an additional liquidity premium. In the chapter's Gretna Engines case, the interpolated seven-year BBB yield is approximately **5.8%**; the issuer's extremely thinly traded bond may deserve slightly more.

### 3. Unrated debt: synthetic credit rating

When no meaningful market YTM or actual rating exists, infer credit quality from fundamentals and map the inferred rating onto a traded spread.

Two commonly used indicators are:

\[
\text{Interest coverage}\approx\frac{EBIT}{\text{interest expense}},\qquad
D/E=\frac{\text{debt}}{\text{equity}}.
\]

The precise interest coverage convention depends on the case or rating model; the curriculum's Precision case uses EBITDA divided by interest expense as its stated coverage measure.

Suppose the appropriate synthetic rating maps to a **2%** credit spread and the matching government yield is **4%**:

\[
\boxed{r_d=4\%+2\%=6\%}.
\]

Under a usable 25% marginal tax rate, after-tax cost = **4.5%**. **One strong ratio cannot magically cancel one dreadful ratio**: if coverage implies a B rating but D/E implies BBB, investigate historical trends, business model, collateral, and other ratios rather than averaging letters into a fictitious 'BB½'. Ratings on particular secured issues can differ from the issuer rating.

### 4. Bank loans

A recently contracted borrowing rate can estimate the marginal bank debt cost **if** both market conditions and company credit risk remain similar. Amortizing loans usually have less outstanding principal exposed over time than otherwise comparable bullet loans. For variable-rate debt, consider the prevailing reference rate plus the contractual spread, rather than blindly using an old interest expense.

### 5. Lease financing

The **rate implicit in a lease (RIIL)** solves:

\[
\boxed{\text{Asset fair value}+\text{Lessor direct initial costs}
=PV(\text{lease payments})+PV(\text{residual value})}.
\]

More simply, discount the lease payments and the asset's value remaining for the lessor so that they equal **fair value plus direct initial costs**. The curriculum works an aircraft lease with asset fair value 100, initial lessor costs 5, annual payments 9 over 15 years, and residual 10, resulting in an implicit rate around **4.08%**.

When residual value or lessor costs are unavailable, use the company's **incremental collateralized borrowing rate (IBR)** for a comparable term; alternatively use comparable debt analysis. If deductions apply, translate to an after-tax debt cost once—not twice.

### 6. Currency and country

Match the borrowing discount rate to the **currency of the cash flows**. For a riskier country, the curriculum permits an appropriate incremental country risk premium:

\[
r_d=r_{f,\,matching\ currency}+\text{issuer spread}+\text{additional country premium}.
\]

A sovereign spread already embedded in the selected benchmark should not be counted twice. Political risk and sovereign **default** risk are related but not identical.

**Debt-level checklist:** Tradeable YTM? If yes, inspect freshness/liquidity. Otherwise matrix price. No rating? Infer synthetic rating. Bank/lease? Use relevant current effective/implicit cost. Foreign? Match currency and account for country risk without duplication. Apply taxes only if deductibility actually exists.

---

## Level 3 — ERP: the price of enduring the stock market

**Priority: very high.**

\[
\boxed{ERP=E(R_m)-r_f}.
\]

ERP is the extra **expected** return on a representative equity market over a government risk-free benchmark. It is not an individual company's cost of equity. That comes later, when you apply its factor sensitivities.

### A. Historical, or *ex post*, ERP

\[
\boxed{ERP_{hist}\approx\text{average market return}-\text{average government benchmark return}}.
\]

There are **four decisions**: which equity index, how many historical years, what definition of average, and whether to compare against short- or long-term government yields.

**Arithmetic versus geometric matters.** Suppose the market rises **50%** in Year 1 and falls **20%** in Year 2:

\[
R_{arith}=\frac{50\%+(-20\%)}2=\boxed{15\%}.
\]

\[
R_{geom}=\sqrt{1.50(0.80)}-1=\boxed{9.54\%}.
\]

Start with 100 and you finish at 120. Your terminal wealth grows at 9.54% a year, not 15%. The arithmetic mean is conceptually aligned with **single-period** expected-return models such as CAPM. The geometric mean measures the **realized compound growth rate** and is useful when thinking about wealth accumulation. Higher variance tends to widen the gap.

A longer time series reduces statistical noise but might include an entirely different economic regime. A short sample can accidentally become a biography of one market crash. **Survivorship/backfill bias** can make history look better when failed firms vanish from the data or only eventual surviving index constituents are included.

A short-term government bill yield offers a closer approximation to an initially known holding-period return; a long-term government yield better matches the long horizon of equities but carries reinvestment and price risk. **Consistency between historical ERP and the risk-free rate used to build today's cost of equity is crucial.**

### B. Forward-looking, or *ex ante*, ERP

Instead of asking what the market earned, ask what its price implies investors require **going forward**.

**1. Surveys.** Ask professionals about expected returns or ERP. Quick, but subject to sampling, anchoring, recency and response bias. Asking an investor about expected returns immediately after a crash is rather like asking a passenger about airline safety while the oxygen masks are falling.

**2. Dividend discount model (DDM).** For a broadly diversified market index and stable perpetual growth:

\[
E(R_m)=\frac{D_1}{P_0}+g,
\qquad\boxed{ERP=\frac{D_1}{P_0}+g-r_f}.
\]

Index forward dividend yield 3%, forecast perpetual dividend growth 5%, matching risk-free yield 4%:

\[
ERP=3\%+5\%-4\%=\boxed{4\%}.
\]

This simple version implicitly assumes stable growth and, in the chapter's explanation, **constant P/E**. Expected P/E expansion or contraction needs additional modeling. If you add repurchase yield to cash payouts, do not also count the same buyback-driven per-share growth twice. A multistage DDM discounts rapid-growth, transition, and mature-growth dividends, then solves for the return that equates their present value to the current index price.

**3. Grinold–Kroner decomposition.** Build expected market return from income, valuation re-rating, inflation, real growth, and share count changes:

\[
\boxed{ERP=DY+\Delta(P/E)+i+g-\Delta S-r_f}.
\]

- \(DY\): dividend yield.
- \(\Delta(P/E)\): anticipated **percentage growth** in market P/E.
- \(i\): expected inflation.
- \(g\): real growth in earnings per share, often proxied by real economic growth before share-count adjustment.
- \(\Delta S\): change in shares outstanding; issuance dilutes (+), repurchases reduce share count (−).
- \(r_f\): compatible nominal risk-free yield.

Try DY 2%, P/E growth 1%, inflation 2%, real growth 3%, shares outstanding rising 1%, risk-free 3%:

\[
ERP=2+1+2+3-1-3=\boxed{4\%}.
\]

**Inflation trap:** If expected inflation raises both nominal earnings growth and nominal risk-free yield by one percentage point, the impact on estimated **ERP** may approximately cancel. The expected **nominal market return** need not stay constant.

**Implied inflation**, using matching nominal and inflation-linked bond yields, can be approximated as:

\[
i\approx y_{nominal}-y_{real},\qquad
 i=\frac{1+y_{nominal}}{1+y_{real}}-1\text{ exactly under aligned conventions}.
\]

The macroeconomic model can be particularly weak where the public equity market is a small and unrepresentative part of the economy. Every forecast method is sensitive to assumptions. When models disagree, investigate why; don't pretend their average is divinely revealed truth.

---

## Level 4 — Cost of equity: what shareholders require from **this** company

**Priority: very high.** Investors in common shares receive the leftovers after creditors and preferred holders. The return they demand is not directly observable, so analysts triangulate with models.

### A. Gordon growth DDM

\[
\boxed{r_e=\frac{D_1}{P_0}+g}.
\]

Next year's dividend = 3, today's price = 100, sustainable growth = 4%:

\[
r_e=3/100+4\%=\boxed{7\%}.
\]

Remember that **\(D_1\)** is next year's dividend, not last year's. A current dividend \(D_0=3\) growing 4% implies \(D_1=3.12\), and the answer changes accordingly. The method is less suitable for non-dividend payers and erratic dividends. A multistage forecast can instead solve an IRR using the current price, forecast dividends, and a future terminal sale price.

### B. Bond-yield-plus-risk-premium (BYPRP)

\[
\boxed{r_e=r_d+RP_{equity\ over\ company's\ bonds}}.
\]

If the firm's current long-term bond yield is 6%, and investors require 4% more for equity than for comparable corporate debt, **cost of equity = 10%**. That premium is **not** automatically the whole-market ERP. The method needs useful traded debt, and the choice of the extra premium is subjective.

### C. CAPM: market risk sensitivity

\[
\boxed{r_e=r_f+\beta\,ERP}.
\]

With risk-free 3%, beta 1.2, market ERP 5%:

\[
r_e=3\%+1.2(5\%)=\boxed{9\%}.
\]

Beta is estimated from the slope in a regression of the company's historical **excess stock returns** on the market's **excess returns**, or equivalently from covariance over market variance under the usual single-factor specification. It is a sensitivity, not a probability of going bankrupt. Beta 1.2 means approximately 1.2 percentage points of stock excess-return movement per 1-point market excess-return movement **in the estimated relationship**, not that the stock will always outperform by 20%.

Time horizon, appropriate index, return frequency, risk-free-rate choice, and changes in the business can make estimated beta unreliable.

### D. Fama–French three- and five-factor models

CAPM blames one factor. Fama–French gives more than one character a role in the financial crime scene:

\[
\boxed{r_e=r_f+\beta_M ERP+\beta_S SMB+\beta_H HML}
\]

\[
\boxed{r_e=r_f+\beta_M ERP+\beta_S SMB+\beta_H HML+\beta_R RMW+\beta_C CMA}.
\]

| Factor | Economic idea |
|---|---|
| ERP / market | Broad equity market excess return |
| SMB | Small-minus-big capitalization return premium |
| HML | High-minus-low book-to-market / value factor |
| RMW | Robust-minus-weak profitability |
| CMA | Conservative-minus-aggressive investment |

A five-factor illustration: risk-free 3%; exposures/premiums are market 1.2 × 5%, SMB 0.5 × 2%, HML −0.2 × 3%, RMW 0.3 × 2%, CMA −0.1 × 1%:

\[
r_e=3+6+1-0.6+0.6-0.1=\boxed{9.9\%}.
\]

**The beta on the market factor can differ between CAPM and a five-factor regression**, because adding explanatory variables changes how covariance is allocated. A negative factor sensitivity subtracts the corresponding expected factor premium; you cannot turn every term positive because that looks nicer on a calculator.

### E. Preferred equity

A perpetual preferred share paying a fixed dividend of 7 and trading at 100 has:

\[
\boxed{r_p=7/100=7\%}.
\]

If redeemable, non-perpetual, or otherwise complicated, assess the actual security terms rather than applying a perpetuity blindly. In a normal comparison, common equity should carry a higher required return than otherwise comparable senior preferred equity; a contradictory model estimate merits investigation.

---

## Level 5 — Private companies and foreign operations: no stock price, no excuses

**Priority: very high.** Public companies hand you prices, beta estimates, bond yields, and filing data. Private companies may hand you their founder's optimistic forecast and the news that the founder is also the only person who knows the customer passwords.

A private company usually has no observable equity beta or traded equity return. The chapter offers two approaches.

### A. Expanded CAPM

\[
\boxed{r_e=r_f+\beta_{peer} ERP+SP+SCRP}
\]

- **SP**: incremental size premium.
- **SCRP**: firm-specific risk premium, for material risks **not already captured** by beta and other premia.
- An **industry premium**, if appropriate and not already captured by comparable company beta, is sometimes considered separately in the chapter's case study.

Estimate a beta from traded comparable businesses, adjust that beta for leverage differences, then add size and company-specific premia where justified.

**Unlevering and relevering** under the familiar approximate tax-adjusted relation:

\[
\boxed{\beta_U=\frac{\beta_{L,peer}}{1+(1-T_{peer})(D/E)_{peer}}}
\]

\[
\boxed{\beta_{L,target}=\beta_U[1+(1-T_{target})(D/E)_{target}]}
\]

For a peer beta of 1.2, peer D/E 50%, tax 20%:

\[
\beta_U=1.2/[1+0.8(0.5)]=\boxed{0.857}.
\]

If the private target has D/E 25% and tax 20%:

\[
\beta_{L,target}=0.857[1+0.8(0.25)]\approx\boxed{1.03}.
\]

**The point:** The target's business risk may resemble the peer's, but a change in leverage changes the equity owner's exposure to that business risk. Using the peer's raw levered beta without adjustment compares two people carrying different debts as though their positions were identical.

### B. Build-up approach

When reliable peers or beta estimates do not exist:

\[
\boxed{r_e=r_f+ERP+SP+IP+SCRP}
\]

This approach generally treats market beta as **1.0** implicitly. **IP** is an industry risk premium. Add an appropriate country premium if needed and not already embedded.

Suppose \(r_f=4\%\), ERP 5%, size premium 3%, industry premium 1%, company-specific premium 2%, country premium 1%:

\[
r_e=4+5+3+1+2+1=\boxed{16\%}.
\]

Size, industry, and company-specific risk premia can overlap. Extra risk premia are not loyalty-card points; don't collect five versions of the same risk. The chapter explicitly distinguishes **illiquidity/marketability**, which is usually reflected in a **valuation discount for lack of marketability**, rather than automatically stacking a new illiquidity premium into required return.

Key-person risk, customer concentration, geographic concentration, pricing power, operating leverage, cash-flow predictability, governance and asset quality help set SCRP. For a small private company, a size premium may be justified, but historical small-cap premia can be contaminated by distressed former large-cap firms.

### C. International cost of equity

Foreign investment can introduce risks not explained by a domestic CAPM. The chapter covers **country-spread and country-risk-rating approaches**, **global CAPM**, and **international CAPM**.

A common country-spread specification is:

\[
\boxed{ERP_{local}=ERP_{developed}+\lambda CRP}.
\]

Here **\(\lambda\)** measures the company's exposure to the riskier country. A firm with 40% relevant exposure and a 2% incremental country risk premium adds **0.8%**, not automatically the entire 2%.

A sovereign-spread proxy estimates incremental country risk by comparing **similar-maturity sovereign bonds denominated in the same currency**. The Damodaran volatility modification is:

\[
\boxed{CRP=\text{sovereign yield spread}\times\frac{\sigma_{local\ equity}}{\sigma_{local\ bonds}}}.
\]

For a 1% incremental sovereign spread, with local equity volatility twice local bond volatility, the volatility-adjusted country premium is **2%**. If the company's exposure fraction is 40%, the corresponding adjustment is **0.8%**. A credit spread is an imperfect stand-in for equity country risk, so treat this as an estimate, not a natural constant.

**Global CAPM** uses a global equity market factor; in a poorly integrated local market its beta can look misleadingly small. **International CAPM** adds foreign-currency exposure:

\[
\boxed{E(r_e)=r_f+\beta_G(E(r_{gm})-r_f)+\beta_C(E(r_c)-r_f)}.
\]

The first beta is sensitivity to global market excess returns; the second is exposure to a foreign-currency factor. It helps distinguish a company primarily exposed to domestic demand from one whose imports, exports, and investments are highly sensitive to currency movements.

**Consistency rule:** Use rates, returns, and cash-flow forecasts in compatible currency and nominal/real terms. Don't add a country premium already present in your risk-free benchmark or credit spread. And never insert a 3% 'politics is messy' premium simply because the country is unfamiliar.

---

## Level 6 — Put the company together and compare it with peers

**Priority: high.** This is where CFA stops letting you hide behind individual formulas. A company has a business, creditors, several classes of shareholders, a tax regime, country exposures, and financing choices that interact.

### First: compute a defensible WACC

Use **target long-run capital weights**, generally based on market values when reliably available. Avoid plugging in the accounting balance sheet just because the values are conveniently sitting there. Use the *current marginal* costs of new capital, not historical coupons or book yields. Preferred equity, if present, gets its own weight.

Suppose the target mix is 30% debt, 10% preferred, and 60% common; pretax debt costs 6%, preferred costs 8%, common costs 12%, and the marginal tax rate is 25%:

\[
WACC=0.30(6\%)(0.75)+0.10(8\%)+0.60(12\%)
\]

\[
=1.35\%+0.80\%+7.20\%=\boxed{9.35\%}.
\]

That is your blended price of capital **for a business of comparable risk**.

**Why simply adding debt does not indefinitely lower WACC:** Debt is cheaper in isolation and can provide tax shields, but additional debt raises default risk, lender spreads, and the volatility of returns to equity. Eventually the consequences of leverage can outweigh the tax benefit. A company cannot finance itself with 99.99% debt at a friendly 4% rate merely by declaring itself a financial innovator.

### The curriculum's public-company mini-case: Gretna Engines

Gretna is a small, cyclical engine manufacturer with high fixed costs and an illiquid BBB bond. The case tests **matrix pricing, preferred equity, three equity models, and capital structure changes**.

| Key item | Curriculum case result |
|---|---:|
| Current debt / preferred / common equity weights | 20% / 15% / 65% |
| Seven-year straight-debt YTM from BBB matrix interpolation | ~5.8% |
| Preferred dividend / preferred price | 70 / 980 = **7.14%** |
| CAPM equity cost | **7.11%** |
| Fama–French five-factor equity cost | **9.20%** |
| Bond-yield-plus-risk-premium equity cost | **12.00%** |

**The catch:** CAPM gives 7.11%, *below* the 7.14% cost of preferred equity. In this business and financing context, that is a reason to question the CAPM inputs or methodology, not to worship a decimal place. Different models can produce different plausible required returns; judgment matters.

Management considers issuing new debt to redeem preferred stock. Debt would increase from 20% to about 35%, but **do not assume the old 5.8% borrowing rate survives the added leverage**. Secure debt with collateral or include bondholder-friendly put/conversion rights and today's borrowing yield may decline; later refinancing pressure or dilution may increase. Re-estimate both capital costs and weights after the transaction.

### The curriculum's private-company mini-case: Precision Irrigation

Precision is a smaller, privately held software company in an emerging market. It has recurring subscription revenue, but also concentrated customers, intangible assets, and key-person risk. Analysts compare it with listed software peers.

The provided ratios imply a synthetic **A** rating with **1.46%** credit spread. Adding the benchmark 10-year yield **5.41%** and the specified **2%** incremental country risk premium:

\[
r_d=5.41+1.46+2.00=\boxed{8.87\%},\quad
r_{d,aftertax}=8.87(0.80)=\boxed{7.096\%}.
\]

Using the peer equity beta 1.25, the peer tax rate 25% and D/E 30.25%, the chapter unleverages to roughly **1.019**. Relevering for the target's 20% tax rate and D/E 21.20% gives beta roughly **1.19**.

An expanded-CAPM-style estimate with the case's indicated premia is:

\[
r_e=5.41+1.19(6)+5+1+6+2\approx\boxed{26.55\%}.
\]

The build-up method includes **6% ERP, 5% size, 1% industry, 6% company-specific, 2% country, and 5.41% risk-free**:

\[
r_{e,build-up}=5.41+6+5+1+6+2=\boxed{25.41\%}.
\]

If the industry premium is **not** added, the result is **24.41%**. That choice must be explicit and justified rather than quietly changed mid-calculation.

With debt weight \(18.4/105.2=17.49\%\), equity weight 82.51%, and the **25.41%** fully specified build-up cost of equity:

\[
WACC=0.1749(8.87\%)(1-0.20)+0.8251(25.41\%)
\]

\[
\boxed{WACC\approx22.21\%}.
\]

The weights above use the chapter's assumed target structure and available balance-sheet numbers. In an external valuation, investigate whether market-value weights would differ.

### An important note about arithmetic inconsistencies in the 2025 chapter

The PDF's Precision Irrigation solution contains internally inconsistent numbers: it labels its build-up return **25.41%** while displaying a sum **without the 1% industry premium**, which equals **24.41%**. It also computes **21.13% WACC** by multiplying an already after-tax debt cost (**7.096%**) by \((1-20\%)\) **again**. That double-taxes the interest shield. Correctly applying the tax adjustment **once** gives **21.38%** if cost of equity is 24.41%, or **22.21%** if the stated 1% industry premium is included for a 25.41% cost of equity. The expanded CAPM solution also alternates between approximately 26.55% and 26.56% because of rounding. These are arithmetic/source inconsistencies, not additional financial principles.

The chapter's Grinold–Kroner Scenario 1 also contains a mismatched prose figure; the specified inputs calculate **5.0% ERP**. Use the equation and actual inputs.

### How to evaluate a capital structure against peers

Compare **business risk first**, not just debt percentages. Two companies with the same 40% debt weight can have radically different financing risk if one has predictable subscriptions and easily recoverable assets while the other depends on the discretionary spending of six customers. Then compare:

1. **Debt mix and serviceability:** debt/EBITDA, debt/equity, interest coverage, maturities, seniority, collateral, put/call/convertible rights.
2. **Cash-flow durability:** recurring revenue, customer concentration, industry cyclicality, fixed-cost leverage, margins and available liquidity.
3. **Market costs:** contemporaneous yields, credit spreads, cost of equity estimates, country and currency risks.
4. **Capital assumptions:** target weights, marginal taxes, existing versus proposed leverage, and financing changes.
5. **WACC implications:** whether a higher or lower WACC reflects genuine risk or a mismatch of methodology and inputs.

A lower WACC is not a trophy. If a company appears to have a fantastically low WACC because the analyst borrowed its peers' beta, ignored country risk, used its bond coupon from ten years ago, and deducted its debt tax shield twice, the company has not become safer. The spreadsheet has become more imaginative.

---

## Exam-ready formula sheet

| Purpose | Formula / calculation |
|---|---|
| Weighted average cost of capital | \(WACC=w_dr_d(1-T)+w_pr_p+w_er_e\) |
| Pretax debt cost | \(r_d\approx r_f+\text{credit spread}\) |
| Interpolated YTM | \(y_T=y_A+\frac{T-A}{B-A}(y_B-y_A)\) |
| Interest coverage | \(EBIT/\text{interest}\), or case-specific stated numerator |
| Historic ERP | Representative average equity return − matching government return |
| DDM market ERP | \(ERP=D_1/P_0+g-r_f\) |
| Grinold–Kroner ERP | \(DY+\Delta(P/E)+i+g-\Delta S-r_f\) |
| Company DDM equity cost | \(r_e=D_1/P_0+g\) |
| BYPRP equity cost | \(r_e=r_d+RP_{equity/debt}\) |
| CAPM equity cost | \(r_e=r_f+\beta ERP\) |
| FF3 equity cost | \(r_f+\beta_M ERP+\beta_S SMB+\beta_H HML\) |
| FF5 equity cost | FF3 + \(\beta_R RMW+\beta_C CMA\) |
| Unlever/relever beta | \(\beta_U=\beta_L/[1+(1-T)D/E]\); reverse for target |
| Private expanded CAPM | \(r_f+\beta_{peer}ERP+SP+SCRP\) plus justified non-overlapping adjustments |
| Private build-up | \(r_f+ERP+SP+IP+SCRP\) plus justified country adjustment |
| Country-adjusted ERP | \(ERP_{developed}+\lambda CRP\) |
| Volatility-adjusted CRP | Sovereign yield spread × \(\sigma_{equity}/\sigma_{bonds}\) |
| ICAPM | \(r_f+\beta_G(r_{gm}-r_f)+\beta_C(r_c-r_f)\) in expected return terms |
| Perpetual preferred | \(r_p=D_p/P_p\) |

**Six deadly exam errors:** confusing bond coupon with current YTM; using past dividends instead of \(D_1\); mixing ERP with company equity cost; mixing premia and currencies; applying a debt tax shield twice; assuming debt can increase forever without raising risk. The CFA exam needs you to calculate, but more importantly it needs you to notice when a clean-looking answer comes from a filthy assumption.
