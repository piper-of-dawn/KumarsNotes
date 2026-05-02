### MODULE 25.1: WEIGHTED-AVERAGE COST OF CAPITAL

###### Expected number of questions: 1
###### LOS 25.a: Calculate and interpret the weighted-average cost of capital for a company.
###### LOS 25.b: Explain factors affecting capital structure and the weighted-average cost of capital.

1. In general, the more **stable**, **non-cyclical**, **predictable**, and **recurring** are a company's revenues and cash flows, the higher proportion of debt it can have in its capital structure. Eg: Walmart (regular cashflows and non-cyclicity), Adani (Huge amount of tangible assets for collateral and non-cyclicity).
2. Companies with low fixed operating costs can support larger debt. 
3. For raising additional debt: Interest Coverage Ratio = EBIT / Interest Expense ⟶ Higher the better. Debt to Equity Ratio ⟶ Lower the better. Debt to EBIT  ⟶ Lower the better.  
4. Capital structure is also dependent on the growth stage, a company is in. During startup stage, debt is very expensive. Company usually raises money through equity or convertible debt. During growth phase the risk is relatively lower and collateralized debt can be raised as capital. During mature stage, company can afford higher debt financing including unsecured debt. ==Remember: Startup companies can raise **Convertible Debt**, Growth ones can raise **Secured Debt** and Mature Ones can afford **Unsecured Debt**==
5. **Top Down Factors** such as inflation, the real GDP growth rate, monetary policy, and exchange rates impact capital structure. High Inflation scenarios demand greater yeilds.

> [!ABSTRACT]- MEMORISE THESE FOR EFFICIENCY
> WACC (use market‑value weights):
>
> $$
> \mathrm{WACC} = w_d\, r_d\, (1 - T) + w_p\, r_p + w_e\, r_e
> $$
>
> Weights (market values):
>
> $$
> w_d = \frac{D}{D + P + E}, \quad w_p = \frac{P}{D + P + E}, \quad w_e = \frac{E}{D + P + E}
> $$
>
> Cost of equity (CAPM):
>
> $$
> r_e = R_f + \beta\,\big(\mathbb{E}[R_m] - R_f\big)
> $$
>
> Cost of equity (DDM):
>
> $$
> r_e = \frac{D_1}{P_0} + g
> $$
>
> Cost of preferred:
>
> $$
> r_p = \frac{D_p}{P_p}
> $$
>
> After‑tax cost of debt:
>
> $$
> r_d\,(1 - T)
> $$
>
> Unlevering and relevering beta:
>
> $$
> \beta_\text{unlevered} = \frac{\beta_\text{comparable}}{1 + (1 - T)\, \frac{D}{E}}
> $$
>
> $$
> \beta_\text{relevered} = \beta_\text{unlevered}\,\Big[1 + (1 - T)\, \frac{D}{E}\Big]
> $$
>
> Notation in simple language:
> - Debt: market value of debt (symbol D)
> - Preferred: market value of preferred stock (symbol P)
> - Equity: market value of common equity (symbol E)
> - Debt weight: share of debt in total funding (wd)
> - Preferred weight: share of preferred in total funding (wp)
> - Equity weight: share of equity in total funding (we)
> - Cost of debt: return lenders demand on new debt (rd)
> - Cost of preferred: return investors demand on preferred shares (rp)
> - Cost of equity: return shareholders demand on common equity (re)
> - Risk‑free rate: rate on default‑free securities in same currency (Rf)
> - Equity market risk premium: expected market return minus risk‑free (E[Rm] − Rf)
> - Beta: sensitivity of the stock/project to the overall market (β)
> - Next dividend: dividend expected next period (D1)
> - Current share price: today’s price per share (P0)
> - Growth rate: long‑run dividend growth (g)
> - Tax rate: company’s marginal tax rate (T)

6. Use market values for weights (`w_d, w_p, w_e`), ideally the firm’s stated target structure; otherwise estimate via current market weights, trend, or industry averages.
7. Use marginal costs: estimate the return required on new debt/equity issues, not historical averages.
8. Project and division adjustments: riskier-than-firm projects need a higher hurdle rate; consider project beta or a divisional WACC rather than the firm-wide WACC.
9. Flotation costs (exam tip): treat as an incremental cash outflow at t=0 for equity issuance; do not bake into WACC.
10. International notes: add a country risk premium to the market risk premium for CAPM when relevant; adjust for currency consistency (inputs and cash flows in same currency).

> [!Question] NUMERICAL — Quick WACC
> Problem: Market values — Debt = 200, Equity = 300; tax rate = 30%; cost of debt = 6%; cost of equity = 12%. Compute the WACC.  
> Solution:  
> - Compute market weights:
> $$
> w_d = \frac{200}{200+300} = 0.4, \quad w_e = 0.6
> $$
> - Apply the WACC formula (no preferred):
> $$
> \mathrm{WACC} = w_d\, r_d\, (1-T) + w_e\, r_e
> $$
> - Substitute and compute:
> $$
> 0.4\cdot 0.06\cdot (1-0.30) + 0.6\cdot 0.12 = 0.0168 + 0.072 = 0.0888 \;\approx\; 8.9\%
> $$
> Explanation: Debt is adjusted for taxes because interest is tax‑deductible; equity has no tax shield.

> [!Question] NUMERICAL — Add preferred
> Problem: Market values — Debt = 200, Equity = 250, Preferred = 50; tax rate = 25%; cost of debt = 8%; cost of preferred = 7%; cost of equity = 13%. Compute the WACC.  
> Solution:  
> - Weights:
> $$
> w_d = \frac{200}{200+250+50} = 0.40,\quad w_p = \frac{50}{500} = 0.10,\quad w_e = \frac{250}{500} = 0.50
> $$
> - Apply and compute:
> $$
> \mathrm{WACC} = 0.40\cdot 0.08\cdot (1-0.25) + 0.10\cdot 0.07 + 0.50\cdot 0.13
> $$
> $$
> = 0.024 + 0.007 + 0.065 = 0.096 \;=\; 9.6\%
> $$
> Explanation: Only debt gets an after‑tax adjustment; preferred and common equity do not.

> [!Question] NUMERICAL — Cost of equity (CAPM)
> Problem: Risk‑free rate = 3%, beta = 1.2, market risk premium = 5%. Find the cost of equity.  
> Solution: Use CAPM to add the scaled risk premium to the risk‑free rate.
> $$
> r_e = R_f + \beta\,(\mathbb{E}[R_m] - R_f) = 0.03 + 1.2\times 0.05 = 0.09 = 9\%
> $$
> Explanation: A beta above 1 amplifies the market premium; here 1.2 adds 6% on top of the 3% risk‑free.

> [!Question] NUMERICAL — Cost of equity (DDM)
> Problem: Current price = 50, next dividend = 2, long‑run growth rate = 4%. Find the cost of equity.  
> Solution: Gordon growth model (dividend yield plus growth).
> $$
> r_e = \frac{D_1}{P_0} + g = \frac{2}{50} + 0.04 = 0.04 + 0.04 = 0.08 = 8\%
> $$
> Explanation: Valid for stable, perpetual growth; ensure g reflects long‑run fundamentals.

> [!Question] NUMERICAL — After‑tax debt cost
> Problem: Pre‑tax borrowing rate = 10%, tax rate = 25%. Find the after‑tax cost of debt.  
> Solution: Apply the tax shield to interest.
> $$
> r_d\,(1 - T) = 0.10\times(1-0.25) = 0.075 = 7.5\%
> $$
> Explanation: Interest reduces taxable income; the effective cost to the firm is lower by the tax rate.

> [!warning] Remember
> - Always match currency: if discounting USD cash flows, use a USD WACC (USD inputs).  
> - WACC uses market weights; book weights can materially misstate the hurdle rate on exam numericals.
