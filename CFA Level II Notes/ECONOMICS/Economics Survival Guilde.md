## Variant: Economics — Exam Survival Guide

**Abstract:** *For currencies, identify the quote, model, and time horizon. For growth, separate total output from output per worker—and a higher income level from permanently faster growth.*

> What determines exchange rates, which growth formulas matter, and where do the exam traps hide?

*5–6 minute review · Exchange Rates ≈ 2½ minutes · Growth Models ≈ 3 minutes*

## Exchange Rates

> [!NOTE] First: lock the quote
> Throughout, $S=D/F$: **domestic currency per one foreign unit**. $S\uparrow$ means **foreign appreciation / domestic depreciation**.

**The parity conditions — what must match?**

$i$ = nominal interest rate; $\pi$ = inflation; $F$ = forward rate. Subscripts $D,F$ identify countries. Formulas below use **one matching period**.

| Condition | Formula | Meaning |
| :--- | :--- | :--- |
| **Absolute PPP** | $S=P_D/P_F$ | Identical baskets should cost the same after conversion. |
| **Relative PPP** | $S_1/S_0=(1+\pi_D)/(1+\pi_F)$ | Higher-inflation currency **depreciates**. Expected inflation gives ex-ante PPP. |
| **Covered interest parity** | $F/S_0=(1+i_D)/(1+i_F)$ | Forward hedging equalizes comparable investment returns. |
| **Uncovered interest parity** | $E[S_1]/S_0=(1+i_D)/(1+i_F)$ | Higher-yield currency is **expected to depreciate** enough to offset its yield. |
| **International Fisher effect** | $i_D-i_F\approx E[\pi_D]-E[\pi_F]$ | Equal real rates link nominal yields to expected inflation. |
| **Forward rate parity** | $F=E[S_1]$ | Covered + uncovered parity imply an unbiased forward forecast. |

> [!NOTE] Pricing versus forecasting
> **Covered parity is enforced by arbitrage** under ideal trading assumptions. The others can fail for years; a forward premium does **not** prove expected appreciation.

**The policy models — identify the transmission channel**

> [!NOTE] Mundell–Fleming: interest rates → capital flows
> With a **floating rate and high capital mobility**, monetary easing → lower rates → outflows → depreciation; fiscal expansion → higher rates → inflows → appreciation.

> [!NOTE] Regime and mobility change the answer
> With low capital mobility, fiscal expansion can weaken the currency through imports. With a credible **fixed rate + free capital flows**, independent monetary policy is constrained; fiscal policy is stronger.

> [!NOTE] Monetary model: money → prices → PPP
> With flexible prices, more domestic money relative to demand → higher domestic prices → depreciation. Higher real income raises money demand, supporting appreciation, other things equal.

> [!NOTE] Dornbusch overshooting: asset prices move before goods prices
> With sticky goods prices, unexpected permanent monetary expansion can cause **immediate depreciation beyond the new long-run level**, followed by appreciation toward it.

> [!NOTE] Portfolio balance: debt → required return
> Domestic and foreign bonds are imperfect substitutes. More government debt requires higher yields/risk premiums and/or **depreciation today**, allowing expected appreciation later.

> [!NOTE] Balance of payments: trade plus financing
> Persistent current-account deficits suggest long-run depreciation pressure, but capital inflows can sustain them. **A deficit alone does not time a currency fall.**

> [!NOTE] The interest-rate trap
> Higher rates from **monetary tightening** can strengthen a currency now; higher rates reflecting **expected inflation or risk** need not. Ask *why rates rose*.

*Parity and policy reference: [CFA Institute—Exchange Rates](https://www.cfainstitute.org/insights/professional-learning/refresher-readings/2026/currency-exchange-rates-understanding-equilibrium-value).*

---

## Growth Models

**1 · Start with the production function**

$$
\boxed{Y=AK^\alpha L^{1-\alpha}}
$$

$Y$ = real output; $K$ = capital; $L$ = labor input; $A$ = **total factor productivity (TFP)**; $\alpha$ = capital's income share. Write $\theta=g_A$, $y=Y/L$, $k=K/L$; $g$ means growth rate.

$$
\boxed{g_Y\approx\theta+\alpha g_K+(1-\alpha)g_L}
$$
$$
\boxed{g_y\approx g_Y-g_L=\theta+\alpha(g_K-g_L)}
$$

> [!NOTE] Read the weights
> **Capital deepening:** $g_k\approx g_K-g_L$; its **contribution** is $\alpha g_k$. TFP is the residual: $\theta\approx g_Y-\alpha g_K-(1-\alpha)g_L$.

> [!NOTE] Productivity is not automatically living standards
> Labor productivity is output per worker/hour; GDP per capita uses population. They coincide only with suitable employment/hours assumptions. TFP shifts the production curve; deepening moves along it.

**2 · Three models, three answers**

| Model | Engine and constraint | Lasting growth in output per person? |
| :--- | :--- | :--- |
| **Classical / Malthus** | Higher income → population growth → pressure on scarce resources | Gains eventually disappear toward subsistence. |
| **Neoclassical / Solow** | Diminishing returns to capital; technology is **exogenous** (determined outside the model) | Requires continuing technological progress. |
| **Endogenous / Romer** | R&D, education, and knowledge spillovers generate progress **inside** the model | Investment and policy can permanently raise growth. |

**3 · Solow: the formulas to recognize immediately**

Let $s$ = saving rate, $\delta$ = depreciation, $n=g_L$ = labor growth. These are the standard continuous-time/growth-rate formulas.

$$
\boxed{\dot K=sY-\delta K}
\qquad
\boxed{g_y^*=g_k^*=\frac{\theta}{1-\alpha}}
$$
$$
\boxed{g_Y^*=n+\frac{\theta}{1-\alpha}}
\qquad
\boxed{\frac{Y}{K}=\frac{\delta+n+\theta/(1-\alpha)}{s}}
$$

The dot means change per unit of time; $*$ denotes the balanced growth path. Investment must cover **depreciation + capital for new workers + capital deepening**.

> [!NOTE] Steady state does not mean zero growth
> $Y/K$ is constant; $y$ and $k$ can keep growing together. Higher $s$ raises the **income level** and transitional growth, but **not** Solow's long-run growth rate.

> [!NOTE] The technology-definition trap
> Here $\theta$ is TFP growth in $Y=AK^\alpha L^{1-\alpha}$, so divide by $1-\alpha$. If technology instead multiplies labor, $Y=K^\alpha(BL)^{1-\alpha}$, then $g_y^*=g_B$ directly.

**4 · Endogenous growth: the simple constant-return version**

$$
\boxed{y=ck\quad\Rightarrow\quad g_y=sc-\delta-n}
$$

$c$ = constant output per unit of broad capital. This simplified model lets saving raise growth permanently. Knowledge spillovers mean **social returns can exceed private returns**, supporting R&D/education incentives.

> [!NOTE] Final exam filters
> **Convergence:** Solow predicts *conditional* catch-up with similar structural parameters; absolute = common destination for all; club = catch-up within groups. Trade helps capital allocation and technology adoption; catch-up is not guaranteed.

> [!NOTE] Growth is not a stock return
> Potential GDP anchors sustainable aggregate earnings growth. Equity returns also include dividends, dilution, inflation, and valuation changes; GDP growth alone is not the answer.

*Formula detail: [[Economic Growth]]. Model comparison checked against [CFA Institute—Economic Growth](https://www.cfainstitute.org/insights/professional-learning/refresher-readings/2026/economic-growth).*
