# Probability Trees and Conditional Expectations

> [!ABSTRACT] LOS
> 1. Calculate expected values, variances, and standard deviations and apply them to investment problems.
> 2. Formulate an investment problem as a probability tree and explain conditional expectations in investment use.
> 3. Calculate and interpret updated probabilities using Bayes' formula.

> [!tip] SEE THIS BEFORE EXAM
> - Expected value just means probability-weighted average. If returns are **-5%**, **10%**, and **25%** with probabilities **0.20**, **0.50**, and **0.30**, then expected return is:
> $$
> E(X) = (0.20)(-5) + (0.50)(10) + (0.30)(25) = -1 + 5 + 7.5 = 11.5\%
> $$
> - Variance is not "square everything and pray." First find expected value, then subtract it from each outcome, square those gaps, weight them, and add. Using the same returns and **\(E(X) = 11.5\%\)**:
> $$
> \sigma^2(X) = (0.20)(-16.5)^2 + (0.50)(-1.5)^2 + (0.30)(13.5)^2 = 54.45 + 1.125 + 54.675 = 110.25
> $$
> $$
> \sigma(X) = \sqrt{110.25} = 10.5\%
> $$
> - In a probability tree, multiply as you move down one path. If recession probability is **0.40** and default probability given recession is **0.08**, that branch probability is:
> $$
> (0.40)(0.08) = 0.032
> $$
> - Add only when you are combining different ending branches. If default in recession is **0.032** and default in expansion is **0.012**, total default probability is:
> $$
> 0.032 + 0.012 = 0.044
> $$
> - Conditional expectation means the scenario is already known, so old unconditional weights are dead. If profit is **2** with probability **0.70** and **6** with probability **0.30** in a weak economy, then:
> $$
> E(X|\text{weak}) = (0.70)(2) + (0.30)(6) = 1.4 + 1.8 = 3.2
> $$
> - Unconditional expected value from scenario averages is just another weighted average. If **\(E(X|\text{weak}) = 3.2\)** with probability **0.40** and **\(E(X|\text{strong}) = 8.5\)** with probability **0.60**, then:
> $$
> E(X) = (0.40)(3.2) + (0.60)(8.5) = 1.28 + 5.10 = 6.38
> $$
> - Bayes is prior times likelihood divided by total probability of the signal. If bankruptcy prior is **0.10**, weak-signal probability given bankruptcy is **0.60**, and weak-signal probability given survival is **0.20**, first get signal probability:
> $$
> P(\text{weak signal}) = (0.60)(0.10) + (0.20)(0.90) = 0.06 + 0.18 = 0.24
> $$
> Then update:
> $$
> P(\text{bankruptcy}|\text{weak signal}) = \frac{(0.60)(0.10)}{0.24} = 0.25
> $$
> - Expected value is **not** the most likely outcome. It is the weighted average outcome.
> - Variance requires expected value first.
> - Multiplying down a path and adding across ending branches are not interchangeable.
> - Once a scenario is known, unconditional probabilities are outdated for that conditional calculation.
> - In Bayes, the denominator is the **total probability of the information**, not the prior probability of the event.
> - If probabilities in a full mutually exclusive and exhaustive event set do not add to **1**, stop and fix the setup before moving on.
> - ==Expected value first. Multiply down a tree. Add across ending branches. In Bayes, never forget the denominator.==

#### Core Flow

1. Expected value is the starting point. What is expected value: the probability-weighted average outcome across all possible cases.
2. Why expected value is used: it gives you the rational center of an uncertain situation before one actual outcome shows up.
3. In investing, expected value is a forecast, not a promise. One realized outcome can be much better or much worse.
4. If a distressed bond can return **-10%**, **5%**, or **30%**, the right first move is not "which one feels likely." The right move is probability-weighting all three.
5. The formula is:

$$
E(X) = \sum P(X_i)X_i
$$

7. Here, $X_i$ means one possible outcome and $P(X_i)$ means the probability of that outcome.
8. The probabilities must add to **1**. If they do not, the setup is incomplete or wrong.
9. A quick market analogy helps. Think of a biotech stock before a drug decision. Approval, delay, and rejection are different branches. Expected value is the weighted average across those branches, not your favorite narrative.
10. Variance is the next step. What is variance: the probability-weighted measure of how spread out the outcomes are around the expected value.
11. Why variance is used: two investments can have the same expected value but very different uncertainty.
12. The formula is:

$$
\sigma^2(X) = \sum P(X_i)[X_i - E(X)]^2
$$

13. That square is doing important work. It makes negative and positive misses both count as risk and punishes bigger misses more heavily.
14. Standard deviation is the square root of variance:

$$
\sigma(X) = \sqrt{\sigma^2(X)}
$$

15. Why standard deviation is used: it puts the dispersion back into the original units, so if return is in percent, standard deviation is also in percent.
16. The exam order never changes: expected value first, variance second, standard deviation last.
17. If variance is zero, there is no uncertainty. That means all probability mass sits on one outcome.

> [!question] EXPECTED VALUE AND STANDARD DEVIATION
> Problem: A stock's one-year return can be **-8%** with probability **0.25**, **12%** with probability **0.50**, or **20%** with probability **0.25**. Find expected return and standard deviation.
>
> ---
>
> Solution:
>
> $$
> E(X) = (0.25 x -8) + (0.50 x 12) + (0.25 x 20) = -2 + 6 + 5 = 9\%
> $$
>
> $$
> \sigma^2(X) = 0.25(-8-9)^2 + 0.50(12-9)^2 + 0.25(20-9)^2
> $$
>
> $$
> = 0.25(289) + 0.50(9) + 0.25(121) = 72.25 + 4.5 + 30.25 = 107
> $$
>
> $$
> \sigma(X) = \sqrt{107} \approx 10.34\%
> $$
>
> Explanation: the expected return is **9%**, but the spread around it is large. That is exactly why expected value alone is not enough.

18. Probability trees enter when uncertainty happens in stages.
19. What is a probability tree: a branching map where early branches show scenarios and later branches show what can happen inside each scenario.
20. Why a tree is used: it forces you to separate scenario probabilities from conditional probabilities instead of mixing them by instinct.
21. The first layer usually shows broad states like recession versus expansion, approval versus rejection, or default versus survival.
22. Later layers show outcomes inside each state.
23. Terminal branch probability is always path multiplication.
24. If recession probability is **0.30** and sales-drop probability given recession is **0.60**, then the joint probability of both is **0.18**.
25. Do not add while going down a path. That is the classic tree mistake.
26. You add only when you combine different ending branches that produce the same final event.
27. If an event can happen through two different states, compute each path separately, then add them.

> [!example] RATING DOWNGRADE MORNING
> Imagine a bond desk tracking whether a company will be downgraded. One branch is "economy weak," another is "economy strong." Inside each branch, the downgrade odds change. The tree matters because "weak economy" and "downgrade given weak economy" are not the same probability, and traders get burned when they blur the two.

28. Conditional probability is the probability of one event after another event is already known.
29. The formula is:

$$
P(A|B) = \frac{P(A \cap B)}{P(B)}
$$

30. What is conditional probability: a resized probability after the sample space has shrunk.
31. Why conditional probability is used: once you know something happened, the old unconditional probability is no longer the right weight.
32. If you already know the economy is weak, you do not keep weighting outcomes by strong-economy probabilities. That world is gone for this question.
33. Conditional expected value does the same thing for forecasts.
34. The formula is:

$$
E(X|S) = \sum P(X_i|S)X_i
$$

35. What is conditional expected value: the expected value after locking yourself inside one scenario.
36. Why conditional expected value is used: because once the scenario is known, the relevant probabilities change.
37. In plain words, unconditional expected value is the all-weather forecast; conditional expected value is today's forecast after you already know which weather state you are in.

> [!question] CONDITIONAL EXPECTATION FROM A TREE
> Problem: A company faces a **0.35** probability of recession and a **0.65** probability of expansion. In recession, earnings are **2** with probability **0.60** and **5** with probability **0.40**. In expansion, earnings are **7** with probability **0.50** and **11** with probability **0.50**. Find expected earnings in recession and unconditional expected earnings.
>
> ---
>
> Solution:
>
> Conditional expected earnings in recession:
>
> $$
> E(X|recession) = (0.60 x 2) + (0.40 x 5) = 1.2 + 2.0 = 3.2
> $$
>
> Conditional expected earnings in expansion:
>
> $$
> E(X|expansion) = (0.50 x 7) + (0.50 x 11) = 3.5 + 5.5 = 9.0
> $$
>
> Unconditional expected earnings:
>
> $$
> E(X) = (0.35 x 3.2) + (0.65 x 9.0) = 1.12 + 5.85 = 6.97
> $$
>
> Explanation: first work inside each scenario, then step back out and weight those scenario averages by scenario probability.

38. The total probability rule is just the tree logic written as a formula.
39. If scenarios $S_1, S_2, ..., S_n$ are mutually exclusive and exhaustive, then:

$$
P(A) = \sum P(A|S_i)P(S_i)
$$

40. What is mutually exclusive: only one scenario can happen at a time.
41. What is exhaustive: together the scenarios cover the full set of possibilities.
42. Why the total probability rule is used: it rebuilds an unconditional probability from conditional pieces.
43. The same logic works for expected value:

$$
E(X) = \sum E(X|S_i)P(S_i)
$$

44. This is not a different idea. It is the same weighted-average idea wearing a different jacket.
45. If your tree is built correctly, the unconditional expected value from terminal branches and the unconditional expected value from scenario averages must match.
46. If they do not match, you mixed a conditional with an unconditional number, or your branch probabilities are broken.

> [!tip] TREE SANITY CHECK
> If you are moving down one branch, multiply.
>
> If you are combining separate ending branches, add.
>
> If the tree answer and the scenario-average answer do not match, something upstream is wrong.

47. Bayes' formula flips the conditioning direction.
48. What is Bayes' formula: a rule for updating the probability of an event after seeing new information.
49. Why Bayes is used: because markets, lenders, and analysts constantly receive noisy signals and need to revise prior beliefs.
50. The formula is:

$$
P(\text{Event}|\text{Info}) = \frac{P(\text{Info}|\text{Event})P(\text{Event})}{P(\text{Info})}
$$

51. Prior probability means your belief before the new information arrives.
52. Posterior probability means your belief after updating with the new information.
53. Likelihood means the probability of seeing the information if the event is actually true.
54. The denominator is the unconditional probability of the information itself.
55. That denominator usually comes from the total probability rule.
56. In plain English, Bayes says: start with your old belief, reward it if the signal is especially likely under that event, and scale by how common the signal is overall.
57. If the signal is common even when the event is false, the update should be weaker.
58. If the signal is rare unless the event is true, the update should be stronger.

> [!example] CREDIT SCREENING
> A lender sees a "weak cash flow" signal on a borrower. Bayes is the grown-up way to ask the question. Not "Does weak cash flow feel scary?" but "How often do bankrupt borrowers show this signal, and how often do healthy borrowers also show it?" That difference is the whole game.

59. The Bayes workflow is mechanical and should stay mechanical.
60. Step 1: write the mutually exclusive events.
61. Step 2: write the prior probabilities.
62. Step 3: write the likelihoods for the new information under each event.
63. Step 4: calculate the unconditional probability of the information.
64. Step 5: update using Bayes.
65. Step 6: if you updated a full set of events, make sure the posterior probabilities sum to **1**.
66. That last check catches a shocking number of silly mistakes.

> [!question] BAYES UPDATE
> Problem: A borrower has a **0.15** probability of default. A weak operating-cash-flow signal appears with probability **0.70** if the borrower will default and with probability **0.25** if the borrower will not default. Find the probability of default after observing the weak-cash-flow signal.
>
> ---
>
> Solution:
>
> First compute the unconditional probability of the weak signal:
>
> $$
> P(weak) = (0.70 x 0.15) + (0.25 x 0.85) = 0.105 + 0.2125 = 0.3175
> $$
>
> Now apply Bayes:
>
> $$
> P(default|weak) = \frac{0.70 x 0.15}{0.3175} = \frac{0.105}{0.3175} \approx 0.3307
> $$
>
> Explanation: default probability rises from **15%** to about **33.07%**. The signal matters, but it is not perfect because healthy borrowers can also trigger it.

67. Some source examples use diffuse priors, which just means equal prior probabilities across the candidate events.
68. If priors are equal, the signal does more of the ranking work because you did not start with a favorite.
69. That does not change the formula. It just makes the arithmetic cleaner.
70. Bayes shows up naturally in bankruptcy prediction, credit scoring, fraud flags, medical screening, and any situation where signals are noisy rather than perfect.
71. A good signal does not make survival certain. A bad signal does not make failure certain. Bayes lives in that gray zone.
72. That is why this topic matters in finance. Real decisions are almost never made with certainty; they are made with updated probabilities.

> [!tip] FINAL QUICK CHECKS
> Expected value question: did you multiply each outcome by its probability before adding?
>
> Variance question: did you subtract the expected value before squaring?
>
> Tree question: did you multiply along paths and add across ending branches only?
>
> Conditional expectation question: did you use probabilities inside the known scenario only?
>
> Bayes question: did you calculate the overall probability of the signal before updating?
