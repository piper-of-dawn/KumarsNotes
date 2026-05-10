###### LOS 14.a: Describe credit risk and its components, probability of default and loss given default.
###### LOS 14.b: Describe the uses of ratings from credit rating agencies and their limitations.
###### LOS 14.c: Describe macroeconomic, market, and issuer-specific factors that influence the level and volatility of yield spreads.

> [!tip] SEE THIS BEFORE EXAM
> - Credit risk is the risk of economic loss because the borrower does not make full and timely interest or principal payments.
> - The two core building blocks are **probability of default (POD)** and **loss given default (LGD)**.
> - Expected loss is:
> $$
> \text{EL} = \text{POD} \times \text{LGD}
> $$
> - And loss given default is:
> $$
> \text{LGD} = \text{EE} \times (1-\text{RR})
> $$
> - **Expected exposure (EE)** or **exposure at default (EAD)** is the amount at risk when default happens. **Recovery rate (RR)** is the percentage recovered. If recovery is high, loss severity is low.
> - Quick memory line: **POD tells you how often default might happen; LGD tells you how painful default would be if it happens.**
> - Credit spread is the compensation investors want for taking credit risk. The rough exam approximation is:
> $$
> \text{Credit spread} \approx \text{POD} \times \text{LGD}
> $$
> - If spread is bigger than expected loss, investor may be adequately compensated. If spread is below expected loss, that is a bad deal.
> - **Baa3 (Moody's) = BBB- (S&P/Fitch)** is the last investment-grade notch. One step below that, **Ba1 / BB+**, and you are in high-yield territory.
> - Investment-grade bonds have lower default risk and are less damaged by bad macro conditions. High-yield bonds have more upside in recovery, but more spread volatility, more liquidity pain, and more default risk.
> - Ratings are useful, but they are **sticky**. Market spreads move daily. Ratings move slowly.
> - Ratings mainly try to capture **expected loss**. Distressed bond pricing often cares more about **default timing** and **recovery**.
> - Two spreads, do not confuse them:
>   - **Yield spread** = premium over default-risk-free benchmark
>   - **Bid-ask spread** = transaction-cost / liquidity-risk signal
> - In stress, investors run from risky assets to safer ones. That is **flight to quality**. High-yield spreads widen first and hardest, but lower-rated investment-grade bonds can get dragged wider too.
> - Price impact from a spread change works just like a yield-change approximation:
> $$
> \%\Delta PV_{\text{Full}} \approx -(\text{AnnModDur} \times \Delta \text{Spread})
> $$
> - For bigger spread moves, add convexity:
> $$
> \%\Delta PV_{\text{Full}} \approx -(\text{AnnModDur} \times \Delta \text{Spread}) + \frac{1}{2}\text{AnnConvexity} \times (\Delta \text{Spread})^2
> $$
> - If modified duration is **4.5**, rescaled convexity is **23**, and spread widens by **1%**, then:
> $$
> \%\Delta PV_{\text{Full}} = -(4.5 \times 0.01) + \frac{1}{2}(23)(0.01)^2 = -4.385\%
> $$
> - Duration trap: the longer-duration bond is much more sensitive to spread changes. Same downgrade, much bigger price hit.

> [!abstract] MEMORISE THIS
> $$
> \text{EL} = \text{POD} \times \text{LGD}
> $$
>
> $$
> \text{LGD} = \text{EE} \times (1-\text{RR})
> $$
>
> $$
> \text{Credit spread} \approx \text{POD} \times \text{LGD}
> $$
>
> $$
> \%\Delta PV_{\text{Full}} \approx -(\text{AnnModDur} \times \Delta \text{Spread})
> $$
>
> $$
> \%\Delta PV_{\text{Full}} \approx -(\text{AnnModDur} \times \Delta \text{Spread}) + \frac{1}{2}\text{AnnConvexity} \times (\Delta \text{Spread})^2
> $$
>
> Rating cutoff:
> - Investment grade: **Baa3 / BBB- and above**
> - High yield: **Ba1 / BB+ and below**

1. Credit risk is the risk of economic loss because a borrower fails to make full and timely payments of interest and principal. This is not just “default happened, now I care.” Expected loss exists before actual default ever shows up.

2. Fixed-income credit analysis is really about one practical question: how likely is it that I will not get paid in full and on time, and if that happens, how much money will I actually lose?

3. A borrower in default is one that fails to meet promised interest or principal payments under the contract.

4. Credit risk changes over the life of the bond. It is not a fixed label stuck on the issuer forever.

#### Credit risk and expected loss

5. The two core components of credit risk are the probability of default and the loss given default.

6. Probability of default, or POD, is the likelihood that the issuer fails to make full and timely payments of principal and interest.

7. Loss given default, or LGD, is the investor’s loss if default actually happens.

8. Recovery rate, or RR, is the percentage of the debt claim that is recovered after default.

9. Loss severity is the unrecovered part, so it equals $(1-\text{RR})$.

10. Expected exposure, or EE, also called exposure at default, is the size of the investor’s claim when default happens. In plain English, it is the amount standing in the line of fire.

11. The module ties them together like this:

$$
\text{LGD} = \text{EE} \times (1-\text{RR})
$$

12. Then expected loss is:

$$
\text{EL} = \text{POD} \times \text{LGD}
$$

13. You can think of expected loss as “how often default might happen” times “how much it hurts if it does happen.”

14. LGD can be expressed either in currency or as a percentage, but the percentage form is usually more useful for comparing different borrowers and bond sizes.

15. One of the cleanest exam uses of expected loss is to compare it with the credit spread. The rough approximation is:

$$
\text{Credit spread} \approx \text{POD} \times \text{LGD}
$$

16. So if expected loss is close to the spread, the investor is roughly being compensated for the credit risk. If expected loss is above the spread, the investor is probably under-compensated.

> [!question] EXPECTED LOSS
> Problem: A EUR500,000 loan has probability of default **5%**, collateral **EUR100,000**, recovery rate **90%**, and expected exposure **EUR400,000**. Find expected loss.
>
> ---
>
> Solution:
>
> First compute the loss exposure after collateral:
>
> $$
> 400{,}000 - 100{,}000 = 300{,}000
> $$
>
> Then apply recovery:
>
> $$
> \text{LGD} = 300{,}000 \times (1 - 0.90) = 30{,}000
> $$
>
> Then apply probability of default:
>
> $$
> \text{EL} = 0.05 \times 30{,}000 = 1{,}500
> $$
>
> Explanation: default is only a 5% event, and even then 90% recovery plus collateral sharply reduce the economic loss.

#### Sources of credit risk

17. Credit analysis traditionally uses the “Cs of credit analysis,” which mix bottom-up and top-down thinking.

18. The bottom-up Cs are **capacity, capital, collateral, covenants, and character**.

19. Capacity means the borrower’s ability to make debt payments on time.

20. Capital means the other company resources available so the firm is not relying only on debt.

21. Collateral means the quality and value of assets supporting the borrowing.

22. Covenants are the legal promises and restrictions written into the debt agreement.

23. Character means management quality and willingness to repay.

24. The top-down Cs are **conditions, country, and currency**.

25. Conditions means the economic, competitive, and business environment.

26. Country means the legal, political, and geopolitical environment of the borrower’s jurisdiction.

27. Currency matters when exchange-rate moves affect cash flows or when the borrower has debt in a currency that is not naturally supported by its cash generation.

28. Corporate borrowers mainly repay from operating cash flow, financing activities, investments, and sometimes asset sales or fresh capital raising.

29. Sovereigns mainly repay from tax revenues, fees, and other government revenues, with new debt issuance and asset sales as secondary tools.

30. An illiquid borrower is one that cannot raise the funds needed right now to make payment, even if total assets may still exceed total liabilities.

31. An insolvent borrower is worse: assets are worth less than liabilities.

32. That distinction matters because a borrower can default from liquidity stress even before balance-sheet insolvency becomes obvious.

33. Secured debt usually has a lower LGD than unsecured debt because specific pledged assets act as a secondary source of repayment.

34. So a high-yield secured issuer can have a higher probability of default but still potentially lower severity of loss than an unsecured structure would imply.

#### Credit ratings and rating-agency limits

35. Credit ratings are symbol-based measures of the potential default risk of a bond issue or issuer.

36. The three major global agencies are Moody’s, S&P, and Fitch.

37. Their symbols look different, but the broad ladder maps closely across agencies.

38. The clean cutoff to memorize is this: **Baa3 by Moody’s and BBB- by S&P/Fitch are the last investment-grade notches**.

39. One notch lower, **Ba1 or BB+**, and the bond is already high yield, also called speculative grade, non-investment grade, or junk.

40. In broad buckets, **AAA/Aaa** is the safest, **AA and A** are still strong, **BBB/Baa** is the last investment-grade zone, **BB/Ba and B** are speculative, and **CCC/Caa and below** are distress territory.

41. Investment-grade issuers generally borrow more easily and at lower rates than high-yield issuers.

42. In comparison with high-yield bonds, investment-grade bonds usually have lower default risk, lower spread volatility, and less damage from bad macro conditions.

43. Ratings are useful because they allow quick cross-issuer and cross-industry comparison.

44. But the curriculum is explicit that relying solely on ratings is dangerous.

45. First problem: ratings tend to be sticky and lag market pricing of credit risk.

46. Bond prices and credit spreads can move daily. Ratings move much more slowly.

47. Second problem: ratings mainly aim at expected loss, but distressed debt pricing often focuses much more heavily on **default timing** and **expected recovery**.

48. That is why two equally rated speculative bonds can trade at very different spreads.

49. Third problem: some risks are hard to capture in advance, such as litigation, environmental shocks, natural disasters, or leveraged events like debt-financed acquisitions and huge buybacks.

50. Complex risks can produce split ratings, where agencies disagree because they are seeing the same mess differently.

51. Fourth problem: ratings can simply be wrong, or too slow, or based on assumptions that later collapse.

52. The mortgage-backed-securities disaster in 2008–2009 is the curriculum’s big historical warning.

53. Wirecard is another example in the module: bonds traded badly before the rating fully caught up, and investors relying only on the rating took a large hit.

54. The adult takeaway is simple: ratings are useful inputs, but they are not substitutes for your own credit analysis.

> [!warning] RATINGS TRAP
> Ratings can lag spreads.
>
> Ratings focus on expected loss.
>
> Distressed bond prices often care more about **when** default may happen and **how much** might be recovered.

#### Yield spreads and spread drivers

55. Credit-risky bonds trade at a yield premium over bonds considered default-risk free, such as US Treasuries or German government bonds. That premium is the yield spread.

56. Yield spreads widen when investors think credit risk is rising and narrow when investors think credit risk is falling.

57. Spread risk is the risk that expected loss or perceived credit conditions worsen, causing spreads to widen and prices to fall.

58. The business cycle matters a lot. Spreads are narrowest near the top of the credit cycle, when investors think credit risk is low.

59. Spreads are widest near the bottom of the credit cycle, when investors think credit risk is peaking.

60. High-yield spreads are much more sensitive to changing macro conditions than investment-grade spreads.

61. In bad markets, investors often sell risky assets and buy safer assets. That is the classic **flight to quality**.

62. High-yield bonds can still be attractive because they may improve diversification, offer equity-like upside with lower volatility than equities, and experience strong capital appreciation in recovery.

63. But those benefits come with heavier spread volatility, higher default risk, and more liquidity risk, especially when markets get stressed.

64. In general, higher-rated bonds have lower yields for the same maturity because investors need less compensation for lower expected loss.

65. In general, longer maturity means higher yield because default risk usually grows with time and uncertainty.

66. The yield differences across investment-grade categories are usually narrower than the jump from investment grade into high yield.

#### Credit spread vs liquidity spread

67. Do not confuse **yield spread** with **bid-ask spread**.

68. Yield spread is the risk premium over the government benchmark. It contains compensation for credit risk and also, in practice, compensation for liquidity risk and other factors.

69. Bid-ask spread is a market-liquidity measure. It reflects the transaction cost of actually buying or selling the bond.

70. Market liquidity risk means the actual transaction price may differ from the nice mid-price you see on the screen.

71. Two important issuer-specific drivers of liquidity risk are the amount of debt outstanding and credit quality.

72. In general, the less debt an issuer has outstanding and the less frequently that debt trades, the higher the liquidity risk.

73. Lower credit quality usually also means worse liquidity and wider bid-ask spreads.

74. During financial stress, liquidity can disappear fast. That means bond prices fall, yield spreads widen, and bid-ask spreads widen too.

75. Liquidity fear can spill over from high-yield into lower-rated investment-grade bonds even if the latter have not yet suffered the same credit deterioration.

> [!question] LIQUIDITY SPREAD
> Problem: A 5-year French government zero-coupon bond is quoted **93.75 / 93.775**. The bid yield is **1.2937%** and the offer yield is **1.2991%**. Find the liquidity spread.
>
> ---
>
> Solution:
>
> $$
> 1.2991\% - 1.2937\% = 0.0054\%
> $$
>
> $$
> 0.0054\% = 54 \text{ bps}
> $$
>
> Explanation: the liquidity spread is the yield gap between the offer side and the bid side.

#### Credit spread decomposition and issuer comparisons

76. The module also shows that a bond’s total yield spread can be thought of as having both a credit component and a liquidity component.

77. Romania’s Eurobond example makes that visible by using bid, offer, and benchmark yields to back out the liquidity spread and then the remaining credit spread.

78. Investors often compare a specific issuer’s yield or spread with peers in the same sector, same rating bucket, or similar business model to separate macro forces from issuer-specific forces.

79. WeWork is the module’s vivid example of why issuer-specific risk can dominate category averages. A B-rated-type peer group average could not explain the violence of WeWork’s own yield swings once its IPO failed and its business model came under pressure.

80. So when one issuer’s spread blows out far more than the general rating bucket, that is your clue that issuer-specific deterioration is doing the heavy lifting.

#### Spread risk and holding-period return

81. A corporate bond’s yield-to-maturity has two broad parts: the benchmark government yield and the spread.

82. If the spread changes, price changes. And for option-free fixed-rate bonds, the same duration and convexity logic you learned for yield changes also works for spread changes.

83. For a small instantaneous spread move:

$$
\%\Delta PV_{\text{Full}} = -(\text{AnnModDur} \times \Delta \text{Spread})
$$

84. Lower spreads help price. Wider spreads hurt price.

85. For larger spread moves, add convexity:

$$
\%\Delta PV_{\text{Full}} = -(\text{AnnModDur} \times \Delta \text{Spread}) + \frac{1}{2}\text{AnnConvexity} \times (\Delta \text{Spread})^2
$$

86. The convexity scaling trap is important. If duration is around 5 and reported convexity is **0.235**, you must rescale convexity to **23.5** before using the formula with decimal spread changes.

87. Longer-duration bonds have much higher spread sensitivity. Same credit-spread shock, much bigger price move.

88. That is why long-dated investment-grade bonds can still be nasty even if default risk looks low: they are heavily exposed to spread risk.

> [!question] PRICE IMPACT OF SPREAD WIDENING
> Problem: A high-yield bond has annualized modified duration **4.5** and reported convexity **0.23**. Spreads widen by **100 bps**. Estimate the price change.
>
> ---
>
> Solution:
>
> First rescale convexity:
>
> $$
> 0.23 \rightarrow 23
> $$
>
> Then apply the formula:
>
> $$
> \%\Delta PV_{\text{Full}} = -(4.5 \times 0.01) + \frac{1}{2}(23)(0.01)^2
> $$
>
> $$
> = -0.045 + 0.00115 = -0.04385
> $$
>
> $$
> = -4.385\%
> $$
>
> Explanation: the duration term drives the loss, and convexity softens it slightly.

89. The module’s BRWA downgrade example makes the duration point very visual. A one-notch downgrade barely hurts the shorter 2030 bond relative to the much larger price damage on the longer 2035 bond.

90. So when the exam asks which bond gets hurt more by worsening credit quality or liquidity, the longer-duration bond is usually the one with the bigger price wound.

#### Analyst traps and comparisons

91. Credit migration risk, also called downgrade risk, is the risk that investors revise the issuer’s creditworthiness downward, causing spreads to widen and prices to fall.

92. High-yield bonds can outperform in recovery, but they are also much more vulnerable to spread widening and liquidity pain in stress.

93. If two bonds have similar maturity and liquidity, comparing **spread minus expected loss** is a quick way to see which one may offer the better reward for the credit risk taken.

94. A bond with a slightly higher POD can still be the better choice if its spread more than compensates for that extra expected loss.

95. Final picture: credit risk is not just “will default happen?” It is a three-part story about **how likely default is, how much you lose if it happens, and how the market reprices that risk every day through spreads and liquidity.**
