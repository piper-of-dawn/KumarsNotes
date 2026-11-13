# Earnings Normalisation and Cashflow Estimation

## Reviewed vs. compiled vs. audited financial statements

The difference is **how much checking the accountant actually does.**

- **Compiled:** You tell your accountant, "I made $100 profit." They prepare the statements using your numbers.
- **Reviewed:** You tell them you made $100. They ask questions and check whether that figure seems reasonable.
- **Audited:** They conduct substantially more detailed testing to obtain reasonable assurance.


## Normalised Earnings

Adjust for things like using parent company's real estate, or a cousin hired at an inflated salary as chief of staff.

|Adjustment                 |Simple example                                                                        |
|---------------------------|--------------------------------------------------------------------------------------|
|**Revenue**                |Owner sells products cheaply to his brother's company. Adjust sales to market prices. |
|**Cost of goods sold**     |Owner buys materials at inflated prices from a family business. Adjust costs downward.|
|**Depreciation & amortization**|Remove distortions from unusual asset valuations or write-downs.                      |
|**Taxes**                  |Recalculate taxes using normalized taxable income.                                    |
|**Dividends**              |Adjust distributions to reflect normal shareholder payout policies.                   |


## Cashflow Forecasting

The problem is that private companies often have unreliable historical earnings, uncertain futures, and management forecasts that may be biased. For early-stage companies, a single growth forecast may be meaningless. Instead:
- Identify possible outcomes.
- Calculate each outcome's probability.
- Value the company under each outcome.
- Calculate the probability-weighted value.
- Discount to today.

# Discount Rates and Required Rate of Return

Private companies typically face higher discount rates. **The four factors affecting discount rates are the size premium, debt availability, acquisition discount rate, and projection risk.**
- Private companies are generally smaller and riskier, so they warrant a size premium. 
- Small private companies are also often shut out of bond markets, limiting debt availability. 
- During an acquisition, the target company's discount rate should be used; applying the parent's lower rate would artificially inflate the valuation. Imagine Microsoft buying a small startup and valuing it at Microsoft's risk level. 
- Finally, private-company forecasts are often unreliable, which adds projection risk.

## Required rate of return model

| CFA Exam Clue                                                           | Model to Use                 | Variables / Formula                                        |
| ----------------------------------------------------------------------- | ---------------------------- | ---------------------------------------------------------- |
| Reliable beta available; no additional private-company risk adjustments | **CAPM**                     | \(R_f+\beta \times ERP\)                                 |
| Reliable beta, but small size or company-specific risks                 | **Expanded CAPM**            | \(R_f+\beta \times ERP+SP+CP\)                           |
| No reliable comparable public-company beta                              | **Build-Up**                 | \(R_f+ERP+SP+IP+CP\)                                     |
| Industry risk premium used instead of beta adjustment                   | **Build-Up**                 | \(R_f+ERP+SP+IP+CP\)                                     |
| Company-specific premium is subjective                                  | **Expanded CAPM / Build-Up** | Add \(CP\) to either model                               |
| Question explicitly provides beta and size premium                      | **Expanded CAPM**            | \(R_f+\beta \times ERP+SP\), plus \(CP\) if applicable |

### **Variable legend**

| Variable    | Meaning                           |
| ----------- | --------------------------------- |
| \(R_f\)   | Risk-free rate                    |
| \(\beta\) | Systematic market risk            |
| \(ERP\)   | Equity risk premium               |
| \(SP\)    | Small-cap stock premium           |
| \(IP\)    | Industry risk premium or discount |
| \(CP\)    | Company-specific stock premium    |

**Memorize:** CAPM = Beta; Expanded CAPM = Beta + Extras; Build-Up = No Beta, Industry Adjustment.


# Valuation Discount and Premiums

How much control can you exert, and how easily can you sell it?

## Discount for lack of control (DLOC)


## Discount for lack of marketeability (DLOM)

CFA is making three points: **volatility affects DLOM, put options are imperfect proxies for illiquidity, and discounts must be multiplied not added.**

### **Why use put options to estimate DLOM?**

A private-company stock is an ownership stake that is difficult to sell. The CFA curriculum uses a put option to estimate the cost of that difficulty ==because being unable to sell exposes you to the risk of prices falling while you're stuck holding the  stock.==

The price of insuring yourself against falling prices is illiquidity.

Imagine you own private shares worth €100 but cannot easily sell them. A put option protects you against falling prices.

- Higher volatility → More downside risk → More expensive put → Higher estimated DLOM.
- Lower volatility → Cheaper put → Lower estimated DLOM.

**Advantage:** Unlike restricted-stock or IPO comparisons, the option model explicitly incorporates volatility.

A put gives price protection, not liquidity. It also allows unlimited upside participation. ==Therefore, its premium is only an imperfect estimate of DLOM.==

### **2. Other valuation discounts**

| Discount          | Reason                                     |
| ----------------- | ------------------------------------------ |
| Key person        | Business depends heavily on one individual |
| Portfolio         | Assets are heterogeneous or poorly matched |
| Non-voting shares | Shareholders lack voting rights            |

### **3. Combining DLOC and DLOM**

\[ \boxed{D_{\text{total}}=1-(1-DLOC)(1-DLOM)} \]

Suppose DLOC = 20% and DLOM = 25%.
$$ D_{\text{total}}=1-(0.80)(0.75)=\boxed{40\%} $$
**Not 45%.** The second discount applies to the value remaining after the first.
