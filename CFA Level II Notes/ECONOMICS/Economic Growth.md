# Economic Growth

See this just before exam:

\[ \boxed{g_Y=\underbrace{\theta+\alpha(g_K-g_L)}_{\text{Labor productivity growth}}+g_L} \]

In **developed countries**, **TFP growth has a larger effect on per capita output growth**, while **capital deepening matters most in developing countries**. ==Population growth appears to have no effect on per capita output growth.==

> What is Dutch Disease
> Strong natural resource exports (oil, gas, minerals) -> Foreign buyers demand the country's currency -> Currency appreciates -> Manufactured goods become expensive for foreign buyers -> Manufacturing exports decline → Economic growth suffers

## Growth Acconting

\[ g_Y=\theta+\alpha g_K+(1-\alpha)g_L \]


Economic growth comes from three sources: technological progress (growth in total factor productivity), capital deepening (growth in capital available per worker), and growth in total labor hours worked.

Importantly, capital deepening's contribution to GDP growth is weighted by capital's income share (\(\alpha\)).

Capital deepening contribution plus growth in total factor productivity equals growth in labor productivity.

Rearrange:

\[ \boxed{g_Y=\underbrace{\theta+\alpha(g_K-g_L)}_{\text{Labor productivity growth}}+g_L} \]

Therefore:

\[ \boxed{\underbrace{g_{LP}-\theta}_{\text{Capital deepening contribution}}=\alpha(g_K-g_L)} \]

Important distinction:

- \(g_K-g_L\) = Growth in capital per worker.
- \(\alpha(g_K-g_L)\) = Contribution of capital deepening to labor productivity growth.
- $g_L$ = Growth in Labour Hours


## Potential GDP Growth

The book identifies two mechanisms:
1. Higher potential GDP growth → Higher equilibrium real interest rates, because more savings are needed to finance investment.
2. Actual GDP growth above potential → Inflationary pressure → Higher nominal interest rates.

## Steady State — Solow Growth Model

Definition: Steady state is a long-run equilibrium in which ==capital per worker and output per worker grow at the same constant rate==, keeping the output-to-capital ratio \(Y/K\) unchanged.

### Important formulas for CFA numericals

1. Growth rate of output per capita

\[ \boxed{g_y=\frac{\theta}{1-\alpha}} \]

$\theta$ is TFP growth, that is the growth in the 'A' part of Cobb-Douglas Model. $1-\alpha$ is the share of income paid to labors. $\theta$ increases productivity and and $1-\alpha$ pulls in back.

Why? Technological progress increases output → more savings and investment → more capital per worker → even higher output per worker.

Imagine a factory with 100 workers and 10 machines.

Technology improves by 2%. Everyone becomes more productive.

Now, two things happen:

1. Direct effect: Better technology → workers produce more.
2. Indirect effect: More production → more savings → more machines → workers become even more productive.

Here's where \(\alpha\) matters.

- High \(\alpha\): Extra machines make a big difference. The indirect effect is powerful.
- Low \(\alpha\): Extra machines make less difference. The indirect effect is weak.

Mathematically:

\[ g_y=\underbrace{\theta}_{\text{Direct effect}}+\underbrace{\alpha g_y}_{\text{Capital amplification}} \]

Suppose technology grows 2% annually.

- \(\alpha=0.2\): \(g_y=2.5\\%\)
- \(\alpha=0.5\): \(g_y=4\\%\)

The punchline: Higher \(1-\alpha\) means lower \(\alpha\). Machines contribute less to production, so technological progress gets less amplification.

It isn't that labor is dragging growth down. It's that capital is providing less of a boost.

2. Sustainable growth rate of total GDP

\[ \boxed{g_Y=\frac{\theta}{1-\alpha}+n} \]

Two engines drive GDP growth:
- Productivity growth \(\frac{\theta}{1-\alpha}\): Each worker produces more.
- Labor force growth \(n\): More workers produce more goods.

3. Steady-state output-to-capital ratio

\[ \boxed{\Psi=\frac{Y}{K}=\frac{\delta+n+\frac{\theta}{1-\alpha}}{s}} \]

4. Capital accumulation

\[ \boxed{\Delta K=sY-\delta K} \]

5. Growth accounting equation

\[ \boxed{g_y=\theta+\alpha g_k} \]


## Intuition: Machines must grow fast enough to keep the economy balanced.

\[ \boxed{\Psi=\frac{Y}{K}=\frac{\delta+n+\frac{\theta}{1-\alpha}}{s}} \]

Imagine an economy that produces 100 units of GDP and saves 20%.

That gives it 20 units to invest in machines.

But those machines face three demands:

1. \(\delta\) — Depreciation: Old machines wear out. Replace them.
2. \(n\) — Population growth: More workers arrive. Give them machines.
3. \(\frac{\theta}{1-\alpha}\) — Productivity growth: Output per worker rises. Capital must grow alongside it.

At steady state (Injection == Leakage):

\[ \underbrace{sY}_{\text{Investment}} = K \left(\underbrace{\delta}_\text{Depriciation}+\underbrace{n}_\text{Population Growth}+\underbrace{\frac{\theta}{1-\alpha}}_\text{Y/K growth}\right)\]

Divide both sides by \(sK\), and you get the formula.

### Memorize it

\[ \boxed{\frac{Y}{K}=\frac{\text{Wear}+\text{Workers}+\text{Productivity}}{\text{Savings}}} \]

Why savings in the denominator?

Higher savings → more investment → more capital relative to output → lower \(Y/K\).

Why the other three in the numerator?

More depreciation, workers, or productivity growth → more investment needed per unit of capital → higher required \(Y/K\).

Memory hook: Three demands on machines, funded by one savings pool.

## Extension of Neoclassical Growth Model

### Why economists criticized Solow

Solow's model had three problems:

1. Technology is a mystery: TFP explained 70–80% of historical US growth, yet Solow treated it as exogenous—basically, technology improves because... well, it just does.

2. Savings don't affect long-run growth: Higher savings → more investment → temporarily faster growth. Eventually diminishing returns kick in, and growth returns to its original rate.

3. Returns on capital should decline: As capital accumulates, its marginal productivity should fall. Yet advanced economies haven't experienced the persistent decline predicted by the model.

### Augmented Solow Model — The Fix

Jorgenson's approach: Perhaps we're measuring capital too narrowly. Include human capital, R&D, infrastructure, and capital quality alongside physical capital. More explained inputs → Smaller unexplained TFP residual.

CFA takeaway: Augmented Solow improves growth accounting but retains diminishing returns and exogenous technological progress. It doesn't fundamentally solve Solow's central problem.



## Endogenous Growth Model - Romer (1986)

Solow's problem: Technology drives growth, but Solow never explains where technology comes from. It apparently just falls from the sky. Romer's answer: Companies invest in R&D, education, and knowledge. Innovation is produced inside the economy hence endogenous.

1. Why growth can continue indefinitely
    - A machine benefits its owner.
    - An invention can benefit thousands of companies.
    - Knowledge creates positive externalities (spillovers).
    - These spillovers offset diminishing marginal returns to capital at the economy-wide level.
    -
Key distinction: ==Private returns to R&D can be smaller than social returns.==

2. Important formulas
Production function
\[
\boxed{y_e=ck_e}
\]

- \(c\) = constant marginal product of capital. This is how much output one additional unit of capital produces. 
- \(k_e\) = capital per worker
- \(y_e\) = output per worker


Growth rate of GDP per capita

\[
\boxed{g_y=sc-\delta-n}
\]

Three forces determine how fast output per worker grows.

1. Savings × Capital Productivity (\(sc\)): People save money → businesses buy machines → machines produce more goods. Higher savings or more productive capital means faster growth.

2. Wear (\(\delta\)): Machines break down. Some investment merely replaces old machines instead of expanding production.

3. Workers (\(n\)): More workers enter the economy. Existing capital must be spread across more people, reducing capital per worker unless investment keeps up.

|Metric            |Solow                       |Romer                       |
|------------------|----------------------------|----------------------------|
|Returns on Capital|Diminishing                 |Constant                    |
|Technology        |Exogenous                   |Endogenous                  |
|Convergence       |Predicted                   |Not guaranteed              |
|Savings Impact    |Temporary increase in growth|Permanent Increase in growth|

## Convergence Hypothesis

Core idea: Poor countries have less capital per worker. Because of diminishing marginal returns, adding capital should generate bigger productivity gains than in rich countries.

Therefore, poor countries should grow faster and eventually catch up. Unfortunately, economics has three versions of this story.

### 1. Three Types of Convergence

|Type       |Meaning                                                                                                                                                                                           |Memory trick                     |
|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------|
|Absolute   |All poor countries eventually catch up to rich countries, regardless of their characteristics                                                                                                     |Everyone catches up              |
|Conditional|Countries with identical savings, population growth, and production functions converge to the same income level                                                                                   |Same conditions, same destination|
|Club       |Only countries belonging to certain groups converge; the poorest may remain trapped. Members have institutions, infrastructure, and technology adoption capabilities that support catch-up growth.|Members only                     |

### Why Convergence Happens

Poor country → Little capital → High marginal productivity of capital → Faster capital accumulation → Faster GDP per capita growth → Catch-up.

But bad institutions, weak property rights, or inadequate investment can derail the process.

==Solow predicts conditional convergence, not necessarily absolute convergence.==

Two mechanisms explain why developing economies can grow faster.

### Capital Deepening — More Machines

- Poor country: Few machines → High marginal productivity of capital → Huge gains from new investment.
- Rich country: Already has plenty of machines → Diminishing returns → Smaller gains.

Intuition: Giving a tractor to a farmer using a shovel changes everything. Giving a tenth tractor to someone with nine barely changes anything.

### Technology Transfer — Copy, Don't Reinvent

Poor countries can adopt technologies already developed by rich countries.

But there is a catch: Technology adoption requires investment in education, skills, and infrastructure.

Without those investments, countries risk remaining outside the convergence club.

### Solow vs. Romer

| Solow                                  | Endogenous growth                                        |
| -------------------------------------- | -------------------------------------------------------- |
| Diminishing returns encourage catch-up | Knowledge spillovers can sustain rich-country advantages |
| Predicts conditional convergence       | Convergence not guaranteed                               |


## Growth in an Open Economy — CFA L2

Core idea: Opening an economy allows capital, technology, and goods to move across borders. Resources can flow toward where they're most productive.

### Five Benefits of Open Economies

1. Global capital: Investment no longer restricted by domestic savings.
2. Comparative advantage: Countries specialize in what they produce relatively efficiently.
3. Economies of scale: Larger markets → Lower average costs.
4. Technology transfer: Poor countries can adopt rich countries' innovations.
5. Competition: Inefficient firms improve or disappear.

### Solow: Capital Flows from Rich to Poor

Poor countries have fewer machines → Higher marginal productivity of capital → Higher expected returns → Foreign capital flows in.

This creates:

- Poor countries: Capital inflows → Investment rises → Faster growth → Trade deficits tend to emerge.
- Rich countries: Capital outflows → Slower domestic capital accumulation → Trade surpluses tend to emerge.

Eventually, diminishing returns reduce the advantage.

Solow's conclusion: Trade and capital mobility accelerate convergence, but do not permanently increase steady-state growth.

### 3. Endogenous Growth: Trade Can Permanently Boost Growth

Three mechanisms:

| Effect       | Intuition                               |
| ------------ | --------------------------------------- |
| Selection    | Competition kills inefficient firms     |
| Scale        | Bigger markets reduce unit costs        |
| Backwardness | Poor countries copy existing technology |

Innovation and knowledge spillovers can sustain higher growth indefinitely.

### China and India — The Solow Surprise

Solow would predict capital-poor China and India attracting capital and running trade deficits.

But China attracted substantial FDI while running trade surpluses, supported by high domestic savings.

Turns out, poor countries don't automatically need to borrow from rich countries.


## Stock Market Growth

### Grinold–Kroner Model

\[ \boxed{E(R_e)=dy+\Delta(P/E)+i+g-\Delta S} \]

| Component         | Meaning                      |
| ----------------- | ---------------------------- |
| \(dy\)          | Dividend yield               |
| \(\Delta(P/E)\) | Change in valuation multiple |
| \(i\)           | Inflation                    |
| \(g\)           | Real GDP growth              |
| \(\Delta S\)    | Dilution effect              |

### Short Run vs. Long Run

Short run: All five factors influence stock returns. P/E changes can be particularly significant.

Very long run:

- Earnings/GDP cannot rise indefinitely.
- P/E cannot expand indefinitely.
- Therefore, their annualized growth rates tend toward zero.
- Sustainable real GDP growth becomes the principal driver of aggregate earnings growth.

**Over the long run, the corporate-profits-to-GDP ratio is mean-reverting, since corporate profits are part of GDP.**

Thus:

\[ \boxed{E(R_e)\approx dy+i+g_{\text{potential}}-\Delta S} \]

### Dilution Effect

\[ \boxed{\Delta S=nbb+rd} \]

- \(nbb\): Net buybacks versus new share issuance.
- \(rd\): Relative dynamism—economic growth captured by unlisted businesses.


