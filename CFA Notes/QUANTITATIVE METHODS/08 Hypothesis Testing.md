###### LOS 8.a: Explain hypothesis testing and its components, including statistical significance, Type I and Type II errors, and the power of a test.
###### LOS 8.b: Construct hypothesis tests and determine their statistical significance, the associated Type I and Type II errors, and power of the test given a significance level.
###### LOS 8.c: Compare and contrast parametric and nonparametric tests, and describe situations where each is the more appropriate type of test.

> [!tip] LOOK AT THESE BEFORE EXAM
> - Hypothesis testing is just disciplined decision-making under uncertainty. You use sample data to judge whether a claim about a population parameter still looks believable.
> - The six-step flow is fixed: **state hypotheses -> pick test statistic -> choose significance level -> state decision rule -> calculate test statistic -> decide.**
> - The **null hypothesis** is the one you try to reject. The **alternative hypothesis** is the rival story you move to if the evidence is strong enough.
> - Null and alternative must be **mutually exclusive** and **collectively exhaustive**. In plain English: they cannot overlap, and together they must cover all possibilities.
> - The **null almost always carries the equality sign**. That is one of the easiest CFA traps.
> - A **test statistic** is the number you compute from the sample and compare with a **critical value**.
> - If the test statistic is more extreme than the critical value, you **reject** the null. Otherwise, you **fail to reject** the null. Never say “accept the null.”
> - **Statistically significant** just means the result is extreme enough to reject the null at the chosen significance level. It does **not** mean “economically important.”
> - **Type I error** = reject a true null. False positive. Its probability is **alpha**. False Alarm.
> - **Type II error** = fail to reject a false null. False negative. Its probability is **beta**. Missed Alarm.
> - Power of the test = 1 - Type II error. Probability of not missing the alarm.
> - “Probability of correctly rejecting the null?” Answer: **power of the test**. It can ask: “Power is probability of not making what error?” Answer: **Type II error**.
> - Lower **alpha** reduces Type I risk but usually raises Type II risk. The cleanest way to reduce both is usually a **bigger sample**.
> - **p-value** means the smallest significance level at which the null would be rejected.
> - If **p-value < alpha**, reject the null. If **p-value > alpha**, fail to reject.
> - One-tailed versus two-tailed trap: for the same alpha, the absolute critical value is **smaller** in a one-tailed test.
> - If the population is normal with **unknown variance**, the correct test for a single mean is usually **t**, not z.
> - Single variance test uses **chi-square**.
> - Equality of two variances uses **F**.
> - Independent two-mean test with unknown but equal variances uses **pooled t**.
> - Related or paired observations use a **paired-comparisons t-test**, not the independent-samples t-test.
> - If returns are non-normal, data are ranked, outliers are ugly, or the question is not really about a parameter, think **nonparametric**.

> [!abstract] MEMORISE
> Six steps of hypothesis testing:
> 1. State the hypotheses.
> 2. Identify the appropriate test statistic and its distribution.
> 3. Specify the significance level.
> 4. State the decision rule.
> 5. Collect data and calculate the test statistic.
> 6. Make a decision.
>
> Core error and power relations:
> - Type I error probability = $\alpha$
> - Confidence level = $1-\alpha$
> - Type II error probability = $\beta$
> - Power = $1-\beta$
>
> Test-statistic reminders:
> $$
> t = \frac{\bar{X} - \mu_0}{s / \sqrt{n}}
> $$
>
> $$
> \chi^2 = \frac{(n-1)s^2}{\sigma_0^2}
> $$
>
> $$
> F = \frac{s_1^2}{s_2^2}
> $$

1. Hypothesis testing is part of statistical inference, which means using sample data to make judgments about a larger population.

2. In estimation, you are trying to estimate a parameter. In hypothesis testing, you are asking whether the sample evidence is strong enough to challenge a claim about that parameter.

3. The point is not certainty. The point is disciplined probability-based judgment under uncertainty.

#### Hypothesis-testing framework

4. The process has six steps, and CFA loves asking which step you are in even when the numbers are simple.

5. Step 1 is stating the hypotheses. Step 2 is identifying the right test statistic and its distribution. Step 3 is choosing the significance level. Step 4 is stating the decision rule. Step 5 is calculating the test statistic from the data. Step 6 is making the decision.

6. If you skip the order and jump straight to a formula, you can still get trapped because the wrong tail, wrong test, or wrong null setup will poison the whole answer.

#### Null and alternative hypotheses

7. Every hypothesis test has two hypotheses: the null hypothesis, written as $H_0$, and the alternative hypothesis, written as $H_a$.

8. The null hypothesis is the statement treated as true unless the sample gives convincing evidence against it. This is the status quo or the default state.

9. The alternative hypothesis is the rival claim you move to if the evidence is strong enough to reject the null.

10. **==The exam rule that saves failed attempts is this: the null hypothesis almost always contains the equality sign. That equality may appear as $=$, $\le$, or $\ge$, depending on the setup, but the null is the one that owns the boundary.==**

11. The alternative hypothesis carries the direction of the real suspicion: greater than, less than, or not equal to.

12. The null and alternative must be mutually exclusive and collectively exhaustive. That means they cannot overlap, and together they must cover all possible parameter values.

13. If management claims mean earnings are greater than 24, the clean setup is usually $H_0: \mu \le 24$ versus $H_a: \mu > 24$.

14. This is why the null is not automatically the claim management wants. The null is the baseline you challenge.

#### Test statistics, significance, and decision rules

16. A test statistic is a number calculated from the sample that becomes the basis for the statistical decision.

17. You compare the calculated test statistic with one or more critical values that come from the chosen significance level and the test statistic’s probability distribution.

18. If the calculated value is more extreme than the critical value, reject the null. If it is not extreme enough, fail to reject the null.

19. Failing to reject the null does not prove the null is true. It only means the sample did not give strong enough evidence against it.

20. Statistical significance means the calculated result is extreme enough to reject the null at the chosen significance level.

21. Statistical significance does not automatically mean practical, economic, or investment significance. A tiny effect can be statistically significant in a huge sample.

22. The significance level, alpha, is the probability of making a Type I error. If alpha is 5 percent, you are accepting a 5 percent risk of rejecting a true null.

23. The complement of alpha is the confidence level. So a 5 percent significance level corresponds to a 95 percent confidence level.

24. The decision rule can be stated either with critical values or with p-values. Both are doing the same job in different language.

25. The p-value is the smallest significance level at which the null would be rejected.

26. So the quick exam rule is simple: if p-value is less than alpha, reject the null. If p-value is greater than alpha, fail to reject.

27. One-tailed and two-tailed tests matter because they change where the rejection region lives.

28. A one-tailed test puts all the rejection area into one tail because the alternative is directional, such as greater than or less than.

29. A two-tailed test splits the rejection area across both tails because the alternative is “not equal to.”

30. For the same alpha, the absolute critical value is smaller in a one-tailed test than in a two-tailed test. That is a standard CFA trap.

> [!question] DECISION RULE WITH p-VALUE
> Problem: A two-tailed test has alpha = 5%. If the calculated p-value is 4.6352%, what do you do?
>
> ---
>
> Solution:
> Reject the null hypothesis.
>
> Explanation: the p-value is below the significance level, so the result is statistically significant at the 5% level.

#### Type I error, Type II error, and power

31. There are four logical outcomes in hypothesis testing: two correct decisions and two mistakes.

32. If the null is true and you fail to reject it, that is a correct decision.

33. If the null is true and you reject it, that is a Type I error, also called a false positive.

34. If the null is false and you fail to reject it, that is a Type II error, also called a false negative.

35. If the null is false and you reject it, that is the correct rejection.

36. Alpha is the probability of a Type I error. Beta is the probability of a Type II error.

37. Power is the probability of correctly rejecting a false null, so power equals $1-\beta$.

38. The trade-off matters. If you make alpha smaller, you reduce the chance of a Type I error, but all else equal you usually increase the chance of a Type II error.

39. This is intuitive: if you demand stronger evidence before rejecting, you will reject less often, including in some cases where the null is actually false.

40. The main clean way to reduce both Type I and Type II risk at the same time is to increase the sample size.

41. Whether Type I or Type II error is “worse” depends on the context. In medicine, regulation, audit, and investing, the cost of the two mistakes can be very different.

> [!question] TYPE I, TYPE II, AND POWER
> Problem: What is the probability of correctly rejecting a false null hypothesis called?
>
> ---
>
> Solution:
> It is called the **power of the test**.
>
> Explanation: power is the complement of Type II error, so power = $1-\beta$.

#### Tests for means

42. In finance, tests about means are everywhere: mean return, mean forecast error, mean performance difference, mean spread, and so on.

43. For a single population mean from a normally distributed population with unknown variance, the theoretically correct test statistic is the t-statistic.

44. The formula is:

$$
t = \frac{\bar{X} - \mu_0}{s / \sqrt{n}}
$$

45. Here $\bar{X}$ is the sample mean, $\mu_0$ is the hypothesized population mean under the null, $s$ is the sample standard deviation, and $n$ is the sample size.

46. Degrees of freedom for this single-mean t-test are $n-1$.

47. A two-tailed single-mean test is used when you want to know whether the true mean is different from the hypothesized value in either direction.

48. A one-tailed test is used when the research question is directional, such as “greater than” or “less than.”

> [!question] TEST OF A SINGLE MEAN
> Problem: A mutual fund has mean monthly return 1.50%, sample standard deviation 3.60%, and sample size 24. A pricing model says the true mean should be 1.10%. At a 5% two-tailed significance level, is performance significantly different from 1.10%?
>
> ---
>
> Solution:
>
> Step 1:
>
> $$
> H_0:\mu = 1.10\% \qquad H_a:\mu \ne 1.10\%
> $$
>
> Step 2: use a t-test with $24-1=23$ degrees of freedom.
>
> Step 3: at 5% two-tailed, critical values are about $\pm 2.069$.
>
> Step 4: calculate the test statistic.
>
> $$
> t = \frac{1.50 - 1.10}{3.60/\sqrt{24}} = 0.54433
> $$
>
> Step 5: compare with the critical values.
>
> Since $0.54433$ lies between $-2.069$ and $+2.069$, fail to reject the null.
>
> Explanation: there is not enough evidence to say the true mean monthly return is different from 1.10%.

49. When you compare two population means using two independent samples from normal populations with unknown but equal variances, the right tool is a t-test using a pooled estimate of the common variance.

50. The key trap here is independence. If the samples are not independent, this is the wrong test.

51. For the pooled-variance two-sample t-test, degrees of freedom are $n_1 + n_2 - 2$.

52. This test is often used when comparing means across two different groups, such as two analysts, two industries, or two unrelated time buckets treated as independent samples.

53. When the samples are dependent, use a paired-comparisons test instead.

54. In a paired test, you first compute the difference within each pair and then test whether the mean of those differences is zero or some other hypothesized value.

55. This is more powerful than pretending the paired observations are independent, because the pairing strips out some irrelevant noise.

56. The paired-comparisons t-statistic uses the mean difference and the standard deviation of the differences, and the degrees of freedom are again $n-1$ where $n$ is the number of pairs.

> [!question] PAIRED OR INDEPENDENT?
> Problem: You compare daily returns on two bond indexes over the same 1,304 days. Should you use an independent-samples mean test or a paired-comparisons mean test?
>
> ---
>
> Solution:
> Use a **paired-comparisons t-test**.
>
> Explanation: the observations are naturally paired by date. You are comparing same-day returns, so the samples are dependent, not independent.

#### Tests for variances

57. A test of a single variance asks whether the population variance equals, exceeds, or falls below some hypothesized variance.

58. For a single normally distributed population, the test statistic is chi-square with $n-1$ degrees of freedom.

59. The formula is:

$$
\chi^2 = \frac{(n-1)s^2}{\sigma_0^2}
$$

60. Here $s^2$ is the sample variance and $\sigma_0^2$ is the hypothesized population variance.

61. The tail matters just as much here as in mean tests. If the alternative says variance is less than the benchmark, the rejection region is on the left. If the alternative says greater than, it is on the right. If the alternative says not equal, it is two-tailed.

62. When comparing the variances of two normally distributed populations using two random independent samples, the correct test is an F-test based on the ratio of sample variances.

63. The test statistic is:

$$
F = \frac{s_1^2}{s_2^2}
$$

64. The degrees of freedom are $n_1-1$ for the numerator variance and $n_2-1$ for the denominator variance.

65. A two-tailed variance comparison uses two critical values. A one-tailed variance comparison uses one.

66. The exam trap is that if you flip which variance is on top, the F-statistic changes, but the logic of the conclusion can still be the same if you match the correct critical region.

> [!question] TEST OF A SINGLE VARIANCE
> Problem: A portfolio’s sample standard deviation over 10 years is 15%. You want to test whether the true variance is less than 400 at the 5% significance level. A left-tail chi-square critical value is 3.325. What is the decision?
>
> ---
>
> Solution:
>
> Step 1:
>
> $$
> H_0:\sigma^2 \ge 400 \qquad H_a:\sigma^2 < 400
> $$
>
> Step 2: use a chi-square test with $10-1=9$ degrees of freedom.
>
> Step 3: compute the test statistic.
>
> $$
> \chi^2 = \frac{(10-1)15^2}{400} = \frac{2025}{400} = 5.0625
> $$
>
> Step 4: compare with the left-tail critical value 3.325.
>
> Since $5.0625$ is not less than $3.325$, fail to reject the null.
>
> Explanation: there is not enough evidence to conclude that the true variance is less than 400.

#### Parametric vs nonparametric tests

67. A parametric test is a hypothesis test about a population parameter or a test that depends on specific distributional assumptions.

68. The t-test, chi-square test, and F-test are parametric because they care about parameters and rely on distributional assumptions.

69. A nonparametric test either is not about a parameter or makes only minimal assumptions about the population distribution.

70. The curriculum’s examples of nonparametric alternatives include the Wilcoxon signed-rank test, Mann–Whitney U test, sign test, and runs test.

71. Nonparametric tests are mainly useful in four situations: when data do not meet distributional assumptions, when there are serious outliers, when data are ranked or ordinal, or when the question does not concern a parameter.

72. **==If the data are ugly, heavily non-normal, rank-based, or structurally unsuited for the parametric test, nonparametric methods extend the reach of inference.==**

73. The trade-off is that nonparametric tests often make fewer assumptions, but parametric tests can be more powerful when their assumptions are actually satisfied.

#### Analyst traps and interpretation

74. Hypothesis testing is supposed to discipline judgment, not replace it. A statistically significant result can still be economically trivial, and a non-significant result does not prove equality in any deep sense.

75. The most common failures are mechanical: wrong null, wrong tail, wrong test statistic, wrong degrees of freedom, or confusing p-value with alpha.

76. The most common conceptual failure is overclaiming. “Fail to reject” is not the same as “proved true,” and “reject” is not the same as “proved forever.”

77. The safest way to read a hypothesis-testing problem is this: what parameter is being tested, what direction is being suspected, what sample structure exists, what distributional assumptions matter, and what exact error risk are we willing to accept?
