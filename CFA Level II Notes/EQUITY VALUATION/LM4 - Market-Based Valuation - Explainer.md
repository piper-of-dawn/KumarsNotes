# Module 4: Market-Based Valuation — Price and Enterprise Value Multiples

**The whole chapter:** Pick a sensible business number, divide the right price by it, and ask whether the result makes sense given growth, risk, and profitability. The division takes three seconds. Establishing that you have divided two compatible things can consume the rest of your fucking afternoon.

This explainer moves through three depths: **what each measure means, how to calculate it, and where the apparently obvious interpretation falls apart.** Examples are original teaching examples. Dollar amounts are hypothetical.

## 1. What a multiple actually tells you

A **multiple** says how much investors pay for one unit of something: earnings, book equity, sales, or cash flow.

If a share costs $60 and annual earnings per share are $3:

$$
P/E=\frac{60}{3}=\boxed{20\text{ times}}
$$

You pay $20 for each $1 of annual earnings. You have **not** established that your investment pays itself back in 20 years. Earnings can change, companies retain earnings, and your landlord has yet to accept “my proportional share of undistributed corporate profits” as rent.

An **observed multiple** uses the market price. A **justified multiple** uses an estimated fair value or a defensible benchmark. Keep those separate: what people pay and what they should pay are different questions.

> [!NOTE]
> **A low multiple is a question, not a verdict.** It can mean a bargain, weak growth, high risk, poor accounting quality, or a business quietly decomposing.

### Two ways to establish a reasonable multiple

| Method | What you do | Economic foundation | Main trap |
|---|---|---|---|
| **Comparables** | Compare with similar companies, a sector, the market, or the company's history | Similar assets should have similar prices: the law of one price | Similar industry labels can hide very different businesses |
| **Forecasted fundamentals** | Derive a multiple from expected cash flows, growth, profitability, and required return | Discounted cash flow valuation | Your assumptions can be beautifully organized nonsense |

Comparables ask, “What do similar businesses sell for?” Fundamentals ask, “What should this business be worth given what it can distribute?”

A stock can be cheap relative to peers while the entire peer group is overpriced. Being the least drunk person driving the bus does not solve the bus problem.

## 2. The rule that prevents half the disasters: match the owners

**Equity value** belongs to common shareholders. **Enterprise value** measures operating business value attributable to the relevant capital providers, after the cash adjustment described below.

The denominator must belong to the same claimholders as the numerator.

| Numerator | Compatible denominator | Why |
|---|---|---|
| Share price | EPS, book value per share, sales per share, cash flow per share | Both are per-share figures |
| Common equity market value | Common earnings, common book equity, equity cash flow | Both concern common shareholders |
| Enterprise value | EBITDA, EBIT, FCFF, sales | These concern the operating business before allocating everything to common shareholders |

**Sales are a special case:** P/S is widely used, but sales support both lenders and shareholders. EV/sales is conceptually cleaner when debt levels differ.

> [!NOTE]
> **Equity with equity. Enterprise with enterprise. Per share with per share.** Never divide a $3 billion market capitalization by $2 EPS and admire the answer.

## 3. P/E: an easy fraction with an unusually active criminal record

### Trailing versus forward

**Trailing P/E** uses the most recent four quarters of available earnings. **Forward P/E** uses forecast earnings, but you must identify the forecast period.

$$
\text{Trailing P/E}=\frac{P_0}{E_{\text{last four quarters}}}
$$

$$
\text{Forward P/E}=\frac{P_0}{E_{\text{specified future period}}}
$$

At $60, trailing EPS of $3 gives **20×**. Forecast EPS of $4 gives **15×**. The stock has not become cheaper between those two sentences. You changed the denominator.

“Forward” can mean the current fiscal-year estimate, the next fiscal-year estimate, the next four forecast quarters, or an estimated next twelve months. These can differ sharply for seasonal or cyclical businesses.

When annual forecasts are blended to approximate next-twelve-month EPS:

$$
E_{NTM}\approx\frac{m}{12}E_{FY1}+\frac{12-m}{12}E_{FY2}
$$

Here $m$ is the months left in the current fiscal year. With three months left, FY1 EPS of $4 and FY2 EPS of $6:

$$
E_{NTM}\approx\frac{3}{12}(4)+\frac{9}{12}(6)=\boxed{5.50}
$$

This is a time-weighted approximation. Actual quarterly forecasts are preferable when seasonality makes that approximation poor.

> [!NOTE]
> Compare trailing with trailing and matching forward periods with each other. “Both say P/E” is insufficient evidence that the numbers speak the same language.

### Which earnings?

EPS means **earnings per share attributable to common shareholders**. Check basic versus diluted EPS, continuing operations, exceptional items, accounting policies, and share splits.

**Diluted EPS** accounts for potentially dilutive securities under the applicable rules. It is often the more cautious denominator, but comparability matters: do not quietly mix basic EPS for one company and diluted EPS for another.

**Underlying earnings** attempt to capture recurring earning power by removing genuinely unusual items. Start with reported earnings and investigate what made them unusual.

Suppose reported net income is $100 million. It includes a $30 million pretax asset-sale gain and a $10 million pretax unusual expense. At a 25% tax rate:

$$
NI_{underlying}=100-30(1-0.25)+10(1-0.25)=\boxed{85\text{ million}}
$$

With 10 million diluted shares, underlying EPS is **$8.50**.

We subtract the gain and add back the expense **after tax** because net income is already after tax. If the question gives after-tax amounts, do not tax them again.

Also: an expense described as “one-time” every year is developing an impressive attendance record. Restructuring, stock compensation, and acquisition costs do not become economically irrelevant because management has strong feelings about them.

### Underlying versus normalized earnings

These solve different problems:

- **Underlying:** remove genuinely unusual items.
- **Normalized:** estimate earnings under ordinary, middle-of-the-cycle conditions.

A steel producer can report perfectly legitimate, recurring operating earnings at a commodity-price peak. Those earnings may still be a terrible estimate of sustainable earning power.

**Method 1: average EPS over a representative full cycle.**

For cycle EPS of $1, $2, $5, $4, and $3:

$$
E_{normalized}=\frac{1+2+5+4+3}{5}=\boxed{3}
$$

This is simple, but historical EPS may reflect a much smaller company. Adjust for splits and consider whether changes in size make the average misleading.

**Method 2: average ROE times current book value per share.**

ROE is **return on common equity**: earnings relative to common shareholders' book investment.

$$
E_{normalized}=\overline{ROE}\times B_{current}
$$

At average cycle ROE of 12% and current book value per share of $40:

$$
E_{normalized}=0.12(40)=\boxed{4.80}
$$

This reflects the current equity base. It still assumes historical profitability is relevant and the book value is meaningful.

> [!NOTE]
> Cyclical stocks can have their **lowest P/E at peak earnings** and their **highest P/E near the bottom**. The denominator can dress a danger signal as a discount coupon.

### Negative earnings: use earnings yield carefully

If price is $20 and EPS is −$2, mathematical P/E is −10×. That does not make the stock cheaper than a profitable company at 5×. Negative P/E breaks the usual ranking interpretation.

**Earnings yield** turns the ratio over:

$$
E/P=\frac{EPS}{P}
$$

The loss-making company's earnings yield is −10%. A profitable company with $2 EPS at $20 has a +10% earnings yield. Zero and negative earnings can therefore remain in an economically interpretable ranking.

It is an **earnings yield**, not a promised cash distribution or expected total return.

## 4. Justified P/E: where growth, risk, and payout enter

The **Gordon growth model** values dividends growing at a constant rate forever:

$$
V_0=\frac{D_1}{r-g}
$$

- $V_0$: estimated value today.
- $D_1$: next period's dividend per share.
- $r$: required equity return, reflecting risk.
- $g$: sustainable long-run dividend growth.
- $b$: fraction of earnings retained, so $1-b$ is the payout ratio.

With a stable payout ratio, dividends and earnings grow together. Since $D_1=E_1(1-b)$:

$$
\boxed{\text{Justified forward P/E}=\frac{V_0}{E_1}=\frac{1-b}{r-g}}
$$

Since $E_1=E_0(1+g)$:

$$
\boxed{\text{Justified trailing P/E}=\frac{V_0}{E_0}=\frac{(1-b)(1+g)}{r-g}}
$$

With payout 40%, required return 10%, and growth 4%:

$$
\text{Forward P/E}=\frac{0.40}{0.10-0.04}=\boxed{6.67\times}
$$

$$
\text{Trailing P/E}=6.6667(1.04)=\boxed{6.93\times}
$$

If next year's EPS is $6, estimated value is $6 × 6.6667 = **$40 per share**.

**Holding other inputs fixed:** more growth raises justified P/E; more risk raises required return and lowers P/E; more payout raises P/E.

But the inputs are related. Under sustainable growth:

$$
g=b\times ROE
$$

Retaining more earnings reduces today's payout while potentially increasing growth. Retention creates value when reinvestment earns more than shareholders' required return. Reinvesting at a lousy return is how a company turns your money into a larger collection of disappointments.

> [!NOTE]
> Gordon growth requires **$r>g$** and a credible steady state. If $g\ge r$, the model is unsuitable; the company has not discovered infinite money.

Small changes in $r-g$ can cause enormous changes in value. A spreadsheet displaying six decimal places is still allowed to be catastrophically wrong.

## 5. Using P/E comparisons without outsourcing your brain

### Choosing a benchmark

| Benchmark | Useful because | What can go wrong |
|---|---|---|
| Close peers | Similar business economics | Different margins, leverage, growth, risk, or accounting |
| Industry or sector | Convenient broader reference | Broad groups contain very different businesses |
| Overall market | Gives market context | Sector mix and growth prospects differ |
| Company's own history | Holds business identity partly constant | The company, interest rates, or competitive position changed |
| Foreign peers | Expands the comparison set | Accounting, country risk, inflation, and growth differ |

A defensible comparison follows a sequence: choose peers, align inputs, calculate multiples, inspect fundamentals, select a benchmark, then estimate value.

At a peer benchmark of 18× forward earnings and target forecast EPS of $5:

$$
V_0=18(5)=\boxed{90\text{ per share}}
$$

If the market price is $75, the target has **20% potential upside to that estimate**:

$$
90/75-1=20\%
$$

That is different from saying price is 16.67% below estimated value, which uses $90 as the denominator. Both percentages can describe the same gap. Denominators remain annoying even outside the valuation ratios.

### Relative P/E

$$
\text{Relative P/E}=\frac{\text{Company P/E}}{\text{Benchmark P/E}}
$$

A company at 15× versus a market at 20× has relative P/E **0.75**: a 25% multiple discount. It is not automatically 25% undervalued. Perhaps its prospects deserve the discount.

### PEG: growth adjustment with several missing organs

$$
PEG=\frac{P/E}{\text{Expected EPS growth in percentage points}}
$$

For 24× P/E and expected growth of 12%:

$$
PEG=\frac{24}{12}=\boxed{2.0}
$$

Use **12**, not **0.12**, under the standard quoting convention.

A lower PEG can suggest cheaper growth, **other things equal**. But PEG ignores risk and payout differences, depends on the growth horizon, and assumes a simplistic relationship between P/E and growth. Zero growth makes it undefined; negative growth defeats the usual interpretation.

**PEG below 1 is not a law of valuation.** The universe has not appointed the number one as chief investment officer.

### Predicted P/E from regression

A **cross-sectional regression** uses differences across companies at a point in time to estimate how multiples relate to fundamentals.

Suppose a fitted equation is:

$$
\widehat{P/E}=8+0.8G-3\beta+4Q
$$

Here $G$ is expected growth measured in percentage points, $\beta$ is a risk measure, and $Q$ is payout expressed as a decimal. These units belong to this hypothetical equation; use whatever units the supplied regression specifies.

For $G=10$, $\beta=1.2$, and $Q=0.4$:

$$
\widehat{P/E}=8+0.8(10)-3(1.2)+4(0.4)=\boxed{14.0\times}
$$

An observed P/E of 11× lies below the model prediction. That is a reason to investigate possible undervaluation, not proof of it.

Regression can suffer from omitted variables, noisy inputs, unstable relationships, correlated explanatory variables, and poor fit outside its sample. It estimates how the sampled market prices companies. If the whole sample is overpriced, it can reproduce the collective hallucination with excellent statistical manners.

## 6. Terminal value: the future needs a date label

**Terminal value** is the estimated value at the end of the explicit forecast period.

For an equity valuation at time $n$:

$$
V_n=(\text{Trailing P/E at }n)E_n
$$

or:

$$
V_n=(\text{Forward P/E at }n)E_{n+1}
$$

Suppose year-five EPS is $4, year-six EPS is $4.40, and the exit **forward** P/E is 15×:

$$
V_5=15(4.40)=\boxed{66}
$$

Discount that value **five years** to today. The terminal value exists at year five even though its forward earnings input comes from year six.

For a dividend model:

$$
V_0=\sum_{t=1}^{n}\frac{D_t}{(1+r)^t}+\frac{V_n}{(1+r)^n}
$$

Use the mature company's likely growth and risk to choose the exit multiple. Today's glamorous high-growth multiple does not deserve a lifetime employment contract.

> [!NOTE]
> Forward exit multiple → next year's earnings. Trailing exit multiple → current year's earnings. Discount from the **valuation date**, not the earnings date.

An EV/EBITDA exit multiple instead produces terminal **enterprise value**. Keep the full DCF framework and subsequent equity bridge consistent with that choice.

## 7. P/B: buying the accounting equity base

$$
P/B=\frac{P}{BPS}=\frac{\text{Common equity market value}}{\text{Common book equity}}
$$

$$
BPS=\frac{\text{Common shareholders' book equity}}{\text{Common shares outstanding}}
$$

Exclude preferred equity when calculating common book equity. Use shares outstanding at the balance-sheet date, rather than blindly borrowing the weighted-average share count used for EPS.

At $45 per share and $30 book value per share, P/B is **1.5×**.

### Why use it?

Book equity is often more stable than earnings and can remain positive when earnings are negative. P/B can be useful for financial businesses whose asset and liability values are economically informative, and for some distressed businesses.

### Why can it mislead?

Book value reflects accounting history, recognition rules, buybacks, write-offs, and asset measurement. Internally created brands or software may barely appear on the balance sheet. An acquired version may produce recognized intangible assets and goodwill.

Two businesses can own similar economic resources while their balance sheets look as though they were assembled by rival religious sects.

Adjustments may address goodwill and other intangibles, asset fair values, off-balance-sheet exposures, or accounting differences. **Tangible common book equity** removes relevant intangible assets from common equity. It is a different denominator, not a universally superior answer.

Negative or tiny book equity can make P/B meaningless or extreme. A write-off also lowers book equity and can mechanically raise later ROE without improving operations. Congratulations on improving profitability by deleting the denominator.

### Justified P/B

Under stable growth, consistent accounting, and sustainable $g=b\times ROE$:

$$
\boxed{\frac{V_0}{B_0}=\frac{ROE-g}{r-g}}
$$

Here the model's forward ROE is $E_1/B_0$.

At ROE 12%, required return 10%, and growth 4%:

$$
P/B=\frac{0.12-0.04}{0.10-0.04}=\boxed{1.33\times}
$$

An especially useful rearrangement is:

$$
\frac{V_0}{B_0}=1+\frac{ROE-r}{r-g}
$$

- **ROE above required return:** justified P/B exceeds 1.
- **ROE equal to required return:** justified P/B equals 1.
- **ROE below required return:** justified P/B falls below 1, within the model's feasible assumptions.

The broader residual-income interpretation is:

$$
\frac{V_0}{B_0}=1+\frac{PV(\text{future residual income})}{B_0}
$$

**Residual income** means profit after charging shareholders' required return on their book equity investment.

> [!NOTE]
> **Below book value does not automatically mean cheap.** If a business reliably earns less than investors require, a discount to book may be perfectly reasonable.

Growth magnifies the effect of the profitability spread. Growth adds value when ROE exceeds required return and can destroy value when ROE falls short. Scaling a bad investment does not rehabilitate it.

## 8. P/S: revenue is not profit wearing a different hat

$$
P/S=\frac{P}{\text{Sales per share}}=\frac{\text{Common equity market value}}{\text{Annual sales}}
$$

A $500 million equity value divided by $1 billion sales gives **0.5×**.

Sales are usually more stable than earnings and can remain positive during losses. That makes P/S useful when earnings-based multiples fail.

But revenue says little about what remains after expenses. A business can sell enormous quantities of stuff while losing money on the entire magnificent operation.

**Net profit margin** is net income divided by sales. With consistent periods and definitions:

$$
P/S=(P/E)\times\text{Net profit margin}
$$

At 20× P/E, a 10% margin implies 2× P/S; a 2% margin implies 0.4× P/S. The lower sales multiple may simply reflect less profit per dollar sold.

### Justified P/S

Let $m_1=E_1/S_1$ be next-period net margin. Then:

$$
\boxed{\frac{V_0}{S_0}=\frac{m_1(1-b)(1+g)}{r-g}}
$$

For a forward sales denominator:

$$
\frac{V_0}{S_1}=\frac{m_1(1-b)}{r-g}
$$

At forward net margin 8%, payout 50%, growth 4%, and required return 10%:

$$
\frac{V_0}{S_0}=\frac{0.08(0.50)(1.04)}{0.10-0.04}=\boxed{0.693\times}
$$

Higher sustainable margins and growth support higher multiples, holding other inputs fixed. Higher risk lowers them.

### Sales still require inspection

Check gross versus net revenue reporting, early revenue recognition, acquisition-driven versus organic growth, and principal-versus-agent treatment. A marketplace reporting the customer's entire payment is not directly comparable with one reporting only its commission.

> [!NOTE]
> Sales are often less manipulable than earnings. **Less manipulable does not mean protected by a supernatural anti-bullshit force field.**

P/S also ignores capital structure. When borrowing differs materially, EV/sales usually provides the cleaner starting point.

## 9. Price/cash flow: first ask which cash flow

“Cash flow” can describe several different numbers. Treating them as interchangeable is like treating “doctor” as sufficient information before allowing someone to operate on your spine. The doctorate might be in medieval poetry.

| Measure | Meaning | Main limitation |
|---|---|---|
| **CF approximation** | Net income plus selected noncash charges | May ignore working capital and noncash revenues |
| **CFO** | Cash flow from operating activities | Excludes capital expenditure and can be temporarily boosted |
| **FCFE** | Cash available to common equity after reinvestment and net borrowing | Volatile; financing choices affect it |
| **EBITDA** | Earnings before interest, taxes, depreciation, amortization | An earnings measure, not actual free cash flow |

For a simple cash-flow approximation:

$$
CF\approx NI+\text{Noncash charges}
$$

For FCFE, assuming CFO includes interest paid consistently:

$$
FCFE=CFO-\text{Capital expenditure}+\text{Net borrowing}
$$

Net borrowing means new borrowing minus principal repaid. For example:

$$
FCFE=120-80+10=\boxed{50\text{ million}}
$$

At $600 million equity market value, P/CFO is **5×**, while P/FCFE is **12×**. Both calculations can be correct. They answer different questions.

FCFE has the clearest equity-valuation link because it measures cash potentially available to shareholders. Negative FCFE can still occur during worthwhile investment, making the multiple unhelpful for simple ranking.

### Cash flow can be managed too

Delaying suppliers boosts current CFO. Selling receivables can accelerate receipts. Cutting necessary investment improves current free cash flow while potentially wrecking future operations.

Deferring maintenance can make the cash-flow statement look excellent right up to the moment a machine starts producing smoke instead of inventory.

**Accounting classification matters:** interest paid and other items can appear in different cash-flow categories across reporting frameworks. Adjust definitions before comparing CFO.

For a stable FCFE stream:

$$
\frac{V_0}{FCFE_1}=\frac{1}{r-g}
$$

Use per-share FCFE with share value, or total FCFE with total equity value. Other P/CF measures also depend on growth and required return, but do not automatically inherit this exact formula: their relationship to distributable equity cash flow matters.

## 10. Dividend yield: actual payments, incomplete picture

$$
\text{Dividend yield}=\frac{\text{Annual dividend per share}}{P_0}
$$

A $2 annual dividend at a $40 price gives **5%**.

Check the convention. A vendor may use the last twelve months of dividends, an annualized latest regular payment, or a forecast. Four times the latest quarterly dividend estimates an annual run rate; it need not equal actual payments over the previous year.

At a stable quarterly dividend of $0.50 and price $40:

$$
\frac{4(0.50)}{40}=\boxed{5\%}
$$

Exclude special dividends when estimating a sustainable regular yield unless the question tells you otherwise.

### Gordon model connection

$$
\frac{D_1}{V_0}=r-g
$$

At fair value, required return is forward dividend yield plus constant dividend growth:

$$
r=\frac{D_1}{V_0}+g
$$

This is a model relationship, not a guarantee of next year's realized return.

A high yield can reflect a generous sustainable payout. It can also reflect a collapsing price before a dividend cut. The yield shoots up while the company approaches disaster, which is a remarkably polite way for a ratio to scream.

Buybacks also return capital but do not appear in dividend yield. Zero dividends therefore do not establish zero shareholder distributions or zero value.

> [!NOTE]
> A dividend is cash once paid. **Future dividends are still conditional.** High yield alone does not establish safety, value, or superior total return.

## 11. Enterprise value: buying the business, including its financing baggage

A common definition is:

$$
\boxed{EV=MV(\text{Common equity})+MV(\text{Preferred equity})+MV(\text{Debt})+NCI-\text{Cash and investments}}
$$

**MV** means market value. **NCI**, or non-controlling interest, represents outside investors' ownership of consolidated subsidiaries.

Cash and investments here mean the items appropriately excluded under the chosen EV convention. Restricted cash, operating cash needs, and non-operating investments can require judgment. Keep the EV adjustment consistent with the earnings measure.

For common equity $500 million, debt $200 million, preferred stock $20 million, NCI $10 million, and deductible cash $50 million:

$$
EV=500+200+20+10-50=\boxed{680\text{ million}}
$$

Why subtract cash? You acquire a cash asset along with the company. It offsets the amount attributed to the operating business.

Why add NCI? Consolidated EBITDA generally includes **100% of controlled subsidiaries' EBITDA**, even if the parent owns less than 100%. Include the outside claim so numerator and denominator cover the same business.

Use market debt value when available and materially different from carrying value. Book debt is often a practical approximation. Include relevant interest-bearing short-term debt too. “Debt” does not mean “whatever happens to be labeled long-term.”

Ordinary operating liabilities such as trade payables are not automatically added as financing debt. Lease liabilities, pensions, and other debt-like claims require consistent treatment with peer conventions and the denominator.

**Total invested capital**, in this chapter's market-value usage, is similar to EV before deducting cash and investments. Definitions vary elsewhere, so read the label rather than conducting a religious ceremony around the acronym.

### The bridge back to common shareholders

$$
\boxed{\text{Common equity value}=EV-\text{Debt}-\text{Preferred equity}-NCI+\text{Cash and investments}}
$$

Then divide by an appropriate common share count.

> [!NOTE]
> An EV-based estimate is **not yet the common shareholders' value**. Lenders do not disappear because your spreadsheet ran out of rows.

## 12. EV/EBITDA: useful, popular, and not cash flow

$$
EV/EBITDA=\frac{EV}{EBITDA}
$$

$$
EBITDA=EBIT+D\&A
$$

Here **EBIT** is earnings before interest and tax; **D&A** is depreciation and amortization. Starting from consistently defined total net income, add back interest, income tax, depreciation, and amortization. Check non-operating items and minority claims before assuming the result represents operating EBITDA.

At EV $680 million and EBITDA $85 million:

$$
EV/EBITDA=680/85=\boxed{8\times}
$$

### Why analysts use it

It helps compare businesses with different debt levels, tax situations, and depreciation policies. EBITDA may remain positive when net income is negative. It is widely used for capital-intensive companies and transaction comparisons.

**EV/EBITDA is more coherent than P/EBITDA** because EBITDA is before lenders' interest claim.

### Why it can mislead

EBITDA ignores cash taxes, working-capital investment, and capital expenditure. Depreciation is noncash today, but the equipment did not descend from heaven with a lifetime replacement warranty.

Two companies each report EBITDA of $100 million. One requires $15 million of annual maintenance investment; the other requires $80 million. Equal EBITDA does not mean equal cash available to investors.

Lease accounting and aggressive adjustments also affect comparability. “Adjusted EBITDA” is where management sometimes sends expenses it would prefer investors not to remember.

Higher expected FCFF growth and higher **ROIC**, return on invested capital, generally support a higher justified EV/EBITDA, holding other relevant inputs fixed. A higher **WACC**, weighted average cost of capital, lowers it.

ROIC measures operating profitability relative to invested capital. WACC is the required return for the business's mix of capital providers.

### Turning a peer multiple into a share price

Suppose benchmark EV/EBITDA is 9× and target EBITDA is $80 million:

$$
EV=9(80)=720\text{ million}
$$

With debt $200 million, cash $40 million, no preferred equity or NCI, and 20 million common shares:

$$
\text{Common equity}=720-200+40=560\text{ million}
$$

$$
V_{share}=560/20=\boxed{28}
$$

The multiple gives business value first. The equity bridge gives the shareholders' portion second.

## 13. Other enterprise multiples

| Multiple | What the denominator captures | Main judgment |
|---|---|---|
| **EV/EBIT** | Operating earnings after D&A | Useful when depreciation is economically relevant |
| **EV/EBITA** | EBIT plus amortization | Separates amortization while retaining depreciation |
| **EV/FCFF** | Cash available to capital providers after reinvestment | Strong cash-flow link, but investment can make FCFF volatile or negative |
| **EV/sales** | Revenue supporting the operating business | Compare operating margins and reinvestment needs |
| **EV/EBITDAR** | EBITDA before rent | Align lease and rent treatment carefully |
| **EV/subscriber, EV/reserves, etc.** | An industry-specific operating quantity | Units differ in quality and profitability |

A common FCFF calculation is:

$$
FCFF=EBIT(1-T)+D\&A-Capex-\Delta WC
$$

$T$ is the relevant tax rate; $\Delta WC$ is investment in **operating working capital**, excluding financing items such as cash and debt.

If CFO includes interest paid, an equivalent route under consistent assumptions is:

$$
FCFF=CFO+Interest(1-T)-Capex
$$

We add interest back **after tax** because FCFF is before financing payments while retaining the tax treatment consistently.

For a stable FCFF stream valued as an operating perpetuity:

$$
\frac{EV_0}{FCFF_1}=\frac{1}{WACC-g}
$$

**EV/sales** is particularly helpful when capital structures differ, but margins still matter. A subscriber who pays reliably and a subscriber who joined for a free trial are both “one subscriber.” Their economic resemblance may end there.

## 14. Cross-border comparisons: the ratio has a passport problem

Companies in different countries can differ in accounting, inflation, taxes, country risk, governance, business mix, and growth opportunities.

Accounting differences may involve development costs, inventory, asset revaluations, goodwill, pensions, or cash-flow classification. Even companies using the same accounting framework can make different choices and estimates.

A lower national-market P/E can reflect higher risk rather than a bargain. Different sector weights can explain part of the gap too.

**Cash-flow multiples are often less affected by accounting differences than earnings or book multiples**, but classification and underlying economics still need adjustment.

A consistently calculated P/E is dimensionless. Merely converting both price and EPS into another currency does not change it. Different inflation and discount-rate environments can still change the economics behind that P/E.

> [!NOTE]
> “Same industry, different country” is the start of the comparison. It is not permission to stop thinking.

## 15. Momentum: what is changing, rather than what is cheap

**Momentum indicators** examine price trends or changes in fundamentals relative to history or expectations. They can supplement valuation and stock selection. They do not independently establish intrinsic value.

### Earnings surprise

$$
UE_t=EPS_{actual,t}-EPS_{expected,t}
$$

Actual EPS of $1.20 versus expected $1.00 gives a **+$0.20 surprise**. Relative to a positive $1.00 expectation, the percentage surprise is **20%**. Percentage surprises become awkward when expected earnings are zero or negative.

### Scaled surprise: how much did today's analysts disagree?

$$
\text{Scaled surprise}=\frac{\text{Actual EPS}-\text{Consensus EPS}}{\text{Standard deviation of analysts' forecasts}}
$$

A $0.20 surprise divided by forecast dispersion of $0.10 gives **2.0**.

**Standard deviation** measures spread. A surprise is more striking when analysts were tightly clustered than when their estimates already ranged from prosperity to the extinction of commerce.

### SUE: how unusual is this compared with past misses?

$$
SUE_t=\frac{EPS_{actual,t}-EPS_{expected,t}}{\text{Standard deviation of historical earnings surprises}}
$$

A $0.20 surprise divided by a historical surprise standard deviation of $0.40 gives **0.5**.

> [!NOTE]
> **Scaled analyst surprise:** disagreement across analysts. **SUE:** variability of past forecast errors. Same-looking fractions, different denominators.

Positive surprises may be used as signals of continuing positive earnings or return momentum. They do not guarantee either.

### Relative strength

One form compares the stock's price performance with a benchmark, rebased to 1 at the start:

$$
RS_t=\frac{P_t/I_t}{P_0/I_0}=\frac{P_t/P_0}{I_t/I_0}
$$

Here $I$ is the benchmark index level. If the stock rises 10% and the benchmark rises 5%:

$$
RS=\frac{1.10}{1.05}=\boxed{1.0476}
$$

The stock outperformed by **4.76% on this relative-growth basis**. Its simple return exceeded the benchmark by **5 percentage points**. These are different calculations.

Relative strength is not the same indicator as RSI. A stock can also outperform while losing money: falling 10% is better than a benchmark falling 20%. Your account remains poorer, but it has won the misery contest.

## 16. Averaging multiples: even the average needs supervision

### Arithmetic mean

$$
\overline{M}=\frac{1}{n}\sum_{i=1}^{n}M_i
$$

For P/Es of 10× and 20×, the mean is **15×**. Simple, familiar, and sensitive to extreme values.

A company with almost zero positive earnings can produce an enormous P/E and drag the mean upward. The group has not necessarily become expensive; one denominator is having a medical emergency.

### Median

The median is the middle observation after sorting. For 10×, 12×, and 100×, it is **12×**, versus a mean of 40.67×. It resists extreme observations, but does not automatically measure a portfolio's aggregate multiple.

### Harmonic mean

For strictly positive multiples:

$$
H=\frac{n}{\sum_{i=1}^{n}(1/M_i)}
$$

For 10× and 20×:

$$
H=\frac{2}{1/10+1/20}=\boxed{13.33\times}
$$

It averages earnings yields and then takes the reciprocal. It reduces the influence of very high multiples but can be sensitive to tiny positive multiples.

### Weighted harmonic mean

For portfolio value weights $w_i$ summing to 1:

$$
H_w=\frac{1}{\sum_{i=1}^{n}(w_i/M_i)}
$$

Invest $100 in each of two stocks at 10× and 20× P/E. Your proportional annual earnings are $10 and $5:

$$
\text{Portfolio P/E}=\frac{100+100}{10+5}=\boxed{13.33\times}
$$

This equals the equally weighted harmonic mean, **not** the arithmetic mean of 15×.

At value weights of 60% and 40%:

$$
H_w=\frac{1}{0.60/10+0.40/20}=\boxed{12.50\times}
$$

> [!NOTE]
> For positive constituent P/Es, the **value-weighted harmonic mean** matches aggregate portfolio price divided by attributable earnings. Value weights are not share-count weights.

Do not mechanically apply the usual positive-multiple harmonic-mean interpretation to zero or negative P/Es. Aggregate earnings can include losses, but excluding loss-making firms changes the meaning of the reported portfolio statistic.

## 17. Using several indicators without holding a committee meeting of bad assumptions

Several multiples can expose different weaknesses:

- Low **P/E**: inspect whether earnings are temporary or risky.
- Low **P/B**: inspect profitability and asset quality.
- Low **P/S**: inspect margins and debt.
- Low **P/CFO**: inspect working capital and capital expenditure.
- Low **EV/EBITDA**: inspect reinvestment, leases, and adjustments.
- High **dividend yield**: inspect coverage and the probability of a cut.

Agreement across ratios helps, but the signals are not independent. Inflated earnings can simultaneously flatter P/E, ROE, and several related measures. Three ratios repeating the same mistake do not become peer review.

**Screening** means using rules to narrow a large investment universe. A low-multiple screen finds research candidates, including quite a few companies that are cheap because they are terrible. Add profitability, risk, balance-sheet, growth, and qualitative checks.

**Sector rotation** applies similar analysis across sectors to choose which to overweight. Sector composition, cycles, and accounting differences still matter.

### Look-ahead bias: accidentally giving your past self psychic powers

A backtest must use information actually available on the historical investment date.

If full-year earnings were released in February, a strategy supposedly executed in early January cannot use those published results. Use the latest four quarters available then, or forecasts genuinely available then.

Also avoid quietly substituting later restated accounts or revised forecasts for what investors actually knew.

> [!NOTE]
> **Reporting date and information-availability date are different.** A December accounting year-end does not mean the completed accounts were available at midnight on New Year's Eve.

## 18. The revision sheet

| Measure | Basic calculation | Main economic drivers | Trap to remember |
|---|---|---|---|
| P/E | Price / EPS | Growth, payout, required equity return | Temporary earnings and mismatched periods |
| E/P | EPS / price | Earnings relative to price | Not a cash payout or promised return |
| PEG | P/E / growth in percentage points | Growth adjustment only | Omits risk and payout; not a universal valuation rule |
| P/B | Price / common book value per share | ROE relative to required return | Below book can be justified |
| P/S | Equity market value / sales | Net margin, growth, payout, risk | Revenue is not profit; leverage matters |
| P/CF | Equity value / defined equity cash-flow measure | Sustainable cash generation, growth, risk | CF, CFO, and FCFE differ |
| Dividend yield | Annual dividend / price | Payout, growth, required return | High yield may precede a cut |
| EV/EBITDA | Enterprise value / EBITDA | Growth, ROIC, WACC, cash conversion | EBITDA ignores investment and taxes |
| EV/sales | Enterprise value / sales | Operating margins, growth, reinvestment, risk | Revenue quality and profitability differ |

**Before trusting any valuation, answer these questions:**

1. Does the numerator cover the same owners and operations as the denominator?
2. Are the periods, currencies, units, and accounting definitions consistent?
3. Is the denominator recurring, sustainable, and economically meaningful?
4. Do the peers actually match in growth, risk, profitability, and capital needs?
5. Does the chosen multiple estimate equity value or enterprise value?
6. If it estimates EV, have you completed the bridge to common equity?
7. Are you using only information available at the valuation date?
8. What change in assumptions would destroy the apparent bargain?

A multiple compresses a valuation into one number. The map is not the territory: the ratio represents a business, and the business still has customers, competitors, debt payments, and an alarming ability to disappoint you.

---

**Source and scope:** CFA Institute, *Equity Valuation*, Learning Module 4, “Market-Based Valuation: Price and Enterprise Value Multiples,” printed pp. 223–310 in the locally supplied PDF. Covers the module's learning outcomes and instructional sections. Teaching examples are original rather than reproductions of the textbook's examples or practice questions. Stable-growth formulas require their stated assumptions; figures are illustrative, not current market observations.
