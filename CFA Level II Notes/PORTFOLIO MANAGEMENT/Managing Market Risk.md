

# Interpretation of VaR
VaR is the minimum loss in the worst 1% or any x% of outcomes, not a guaranteed maximum loss. The phrase “VaR will limit losses” is a red flag. VaR measures risk; it doesn't prevent losses.

# Advantages and Disadvantages of VaR

VaR can evaluate risk-adjusted performance, we can compare returns relative to VaR, provided the return and VaR measures use consistent units and horizons.

## Disadvantages 
1. Subjectivity: Results depend on confidence level, horizon, methodology, data and assumptions.
2. Fat tails: Normal distributions underestimate extreme losses and their frequency.
3. Liquidity ignored: Assumes positions can be exited without substantial price impact.
4. ==**Correlation breakdown==: Assets that normally diversify each other may crash together.**
5. **Volatility regimes: ==C====alm markets produce artificially low VaR==; risk explodes when volatility rises.**
6. **VaR can be gamed by ==slow bleeding==. A portfolio stays under its daily VaR every day and still piles up a catastrophic loss. Stop-loss fixes that.**
7. Not worst-case loss: A $10m VaR doesn't mean losses cannot reach $100m.
8. Oversimplification and upside ignored: One number hides complex risks and focuses on losses rather than potential gains.



# Value at Risk Approaches


Value at risk estimates the minimum loss expected to occur x percent of the time.

If a question indicates that tail-risk probabilities have risen or the market has become unevenly volatile, do not use parametric VaR. Fall back on Monte Carlo simulations with fat-tailed distributions.


## Incremental VaR (IVaR)

How much does my portfolio's VaR change when I add or remove a position?

\[ \boxed{IVaR=VaR_{\text{new}}-VaR_{\text{old}}} \]

### Example

You own Asset A and are considering adding Asset B.

- Asset A standalone VaR = $3 million
- Asset B standalone VaR = $4 million
- Correlation = 0

Step 1: Calculate new portfolio VaR.

\[ VaR_{\text{new}}=\sqrt{3^2+4^2}=\\$5M \]

Step 2: Subtract original VaR.

\[ IVaR=5-3=\boxed{\\$2M} \]

Although Asset B has $4M standalone VaR, it adds only $2M of risk because of diversification.

Remember: Positive IVaR increases portfolio risk; negative IVaR reduces it.



Relative VaR measures the risk of underperforming a benchmark, rather than the risk of losing money outright.

### Example

Suppose your portfolio and the S&P 500 have these returns:

|            | Portfolio | Benchmark |
| ---------- | --------- | --------- |
| Scenario 1 | −20%      | −22%      |
| Scenario 2 | +10%      | +12%      |

In both scenarios, your portfolio underperforms or outperforms the benchmark by +2% and −2%, respectively. Relative VaR focuses on the distribution of these return differences, not the portfolio's absolute returns.

### Formula

\[ R_{\text{active}}=R_P-R_B \]

\[ VaR_{\text{relative}}=z\sigma_{\text{active}}-\mu_{\text{active}} \]

At 95% confidence, \(z=1.645\), assuming normally distributed active returns.

CFA distinction:

- Absolute VaR: How much money could I lose?
- Relative VaR: How badly could I underperform my benchmark?

==The CFA curriculum also refers to relative VaR as ex ante tracking error, typically expressed as annualized active-return volatility (one standard deviation).==


# Scenario Analysis

It also covers qualitative risk events. For example, what happens if equities drop 30%, bond spreads blow out, liquidity vanishes, and a bank fails?

Stress testing sits within scenario analysis.

- A historical scenario replays a past crisis against your portfolio, such as the COVID-19 selloff or the 2008 crash. 
- A hypothetical scenario asks you to build one from scratch: what happens if bond spreads widen, buyers disappear, and liquidity haircuts suddenly shoot up?
- Reverse stress testing means finding what could destroy your portfolio, then imagining a disaster that would make it happen. Suppose you hold a long-duration bond. The obvious disaster is the yield curve steepening by an obnoxious amount.

# Constraints in Risk Management

| Risk constraint       | Meaning                                                                     | Example                                                        |
| --------------------- | --------------------------------------------------------------------------- | -------------------------------------------------------------- |
| 1. Risk budget        | Maximum risk you're permitted to take                                       | Daily VaR cannot exceed $2m                                    |
| 2. Position limit     | Maximum exposure to a particular investment                                 | NVIDIA cannot exceed 10% of NAV                                |
| 3. Scenario limit     | Maximum estimated loss under a hypothetical or historical shock             | A market crash scenario must not produce losses exceeding $15m |
| 4. Stop-loss limit    | Reduce or liquidate positions after actual losses hit a threshold           | Liquidate if monthly losses reach $8m                          |
| 5. Capital allocation | Allocate scarce capital to activities according to risk and expected reward | Reserve $20m of economic capital to support a strategy         |

## Critical CFA distinctions

Scenario limit vs. Stop-loss limit

- Scenario limit: What if things go horribly wrong tomorrow? (Potential loss)
- Stop-loss limit: Things have already gone horribly wrong. (Realized or accumulated loss)

Risk budgeting vs. Capital allocation

- Risk budgeting typically uses VaR or ex ante tracking error.
- Capital allocation typically uses economic capital, emphasizing severe tail losses and survival.

Related term — Drawdown control / Portfolio insurance: Instead of liquidating immediately, increase hedging as losses accumulate.

# Who uses which risk measure 

1. Three things shape which risk measures a market participant uses: ==how leveraged it is, what mix of risks it holds, and the accounting or regulatory rules it must follow.==
2. Levered players obsess over the ugly tail—high confidence, short horizon, “will we still be alive after the next two-week nightmare?” Unlevered long-only managers care more about looking stupid next to their benchmark. They use lower confidence levels and longer windows.
3. Mark-to-market books get VaR, economic capital, duration, beta. Book-value books get gap models.

# Pension Funds

Long-only asset managers most commonly express risk measures in percentage terms and relative to a benchmark, whereas the entities in answers A and B measure risk more commonly in currency units and in absolute terms (not relative to a benchmark).

Ex ante tracking error uses current portfolio holdings exposed to the variability of historical markets, whereas ex post tracking error measures the variability of historical portfolio holdings in historical markets.


Interest rate and curve risk. First job is figuring out the expected future payments to the pensioners and grouping those cash flows by maturity. If it’s an international plan paying in multiple currencies, group by currency too. In places that force you to use a specific fixed-income instrument or curve for the discount rate (corporate bonds in the U.S., inflation-linked gilts in the U.K., government bonds in the Netherlands), you treat those liability cash flows like a short position at the relevant points on the curve.

Liability-hedging exposures versus return-generating exposures. Matching the liabilities is important, but it’s not the only game. Plans usually split the portfolio: one pile is supposed to track the liabilities as closely as possible, the other is supposed to generate excess returns. You often can’t buy the exact instruments the liability model wants, so you need that second pile. It also helps cover the stuff the models miss—people living longer than expected, wages growing faster than forecasted, the usual ways the universe finds to make your carefully calculated number look stupid.That’s the job. Keep the funding ratio from going full crisis or full embarrassment, and try not to let the return-seeking side blow up the matching side while you’re at it.