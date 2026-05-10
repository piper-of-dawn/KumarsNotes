###### LOS 7.a: Compare and contrast simple random, stratified random, cluster, convenience, and judgmental sampling and their implications for sampling error in an investment problem.
###### LOS 7.b: Explain the central limit theorem and its importance for the distribution and standard error of the sample mean.
###### LOS 7.c: Describe the use of resampling (bootstrap, jackknife) to estimate the sampling distribution of a statistic.

> [!tip] LOOK AT THESE BEFORE EXAM
> - Start with the big split: **probability sampling** gives selection based on probability rules, so it is usually more representative. **Non-probability sampling** depends on convenience or human judgment, so bias risk is much higher.
> - **Simple random sampling** means every element has equal chance. Best when the population is fairly homogeneous.
> - **Stratified random sampling** means divide into important groups first, then randomly sample inside each group. Exam trap: ==all strata are represented==, which is why precision is usually better than under simple random sampling.
> - **Cluster sampling** is different: you sample whole clusters, not all subgroups. Cheap and practical for huge populations, but usually less accurate than other probability methods at the same sample size.
> - What is the difference between cluster and stratified sampling: **stratified means sample from every group; cluster means sample only selected groups**.
> - Suppose you want to survey US investors. Instead of sampling from every state, you randomly choose a few states, then survey investors inside those states. Each state is a **cluster**. In **one-stage cluster sampling**, you survey everyone in selected clusters. In **two-stage cluster sampling**, you randomly sample people inside selected clusters.
> - **Convenience sampling** means "take what is easy to get." Fast and cheap, but dangerous for inference.
> - **Judgmental sampling** means the researcher handpicks the sample using expertise. Useful under time pressure or in specialist settings, but bias risk is real.
> - Sampling error is not a scandal. It is the natural gap between a sample statistic and the population parameter because you used only part of the population.
> - The **central limit theorem** does **not** say the population itself becomes normal. It says the **sample mean distribution** becomes approximately normal for large samples if the population has finite variance.
> - The central limit theorem also does **not** say portfolio risk goes to zero just because you own many investments. That is a misuse of the theorem.
> - The mean of the sample-mean distribution is **population mean $\mu$**. The variance of that distribution is **$\sigma^2/n$**.
> - If population standard deviation is **6%** and you want sample-mean standard error to be **1%**, solve:
> $$
> 1\% = \frac{6\%}{\sqrt{n}}
> $$
> $$
> \sqrt{n} = 6 \Rightarrow n = 36
> $$
> - If you want standard error to fall to **0.25%**, then:
> $$
> 0.25\% = \frac{6\%}{\sqrt{n}}
> $$
> $$
> \sqrt{n} = 24 \Rightarrow n = 576
> $$
> - That is the key intuition: cutting standard error a lot usually requires a **much larger** sample, not a slightly larger one.
> - Standard deviation tells you how spread out the raw data are. **Standard error** tells you how imprecise your estimate is because of sampling.
> - **Bootstrap** resamples with replacement, keeps the same sample size as the original sample, and is great when no easy analytical formula exists.
> - **Jackknife** leaves one observation out at a time, is often used for bias reduction, and is more deterministic than bootstrap.
> - If CFA asks for the standard error of something awkward like a **median**, that is your clue to think **bootstrap**, not the simple $s/\sqrt{n}$ formula for the sample mean.

> [!abstract] MEMORISE
> $$
> \sigma_{\bar{X}} = \frac{\sigma}{\sqrt{n}}
> $$
>
> $$
> s_{\bar{X}} = \frac{s}{\sqrt{n}}
> $$
>
> $$
> s^2 = \frac{\sum_{i=1}^{n}(X_i - \bar{X})^2}{n-1}
> $$
>
> Central Limit Theorem:
> Given a population with mean $\mu$ and finite variance $\sigma^2$, the sampling distribution of the sample mean from large random samples is approximately normal with mean $\mu$ and variance $\sigma^2/n$.
>
> Bootstrap standard error:
> $$
> s_{\bar{X}} = \sqrt{\frac{1}{B-1}\sum_{b=1}^{B}(\hat{\theta}_b - \bar{\theta})^2}
> $$
>
> Notation in simple language:
> - $\mu$: population mean
> - $\sigma$: population standard deviation
> - $n$: sample size
> - $s$: sample standard deviation
> - $B$: number of bootstrap resamples
> - $\hat{\theta}_b$: statistic from bootstrap resample $b$

1. Estimation and inference start with one simple problem: you care about a population, but you usually cannot afford to observe every single member of that population.

2. A population is the full group you care about. A sample is only part of that group. A parameter describes the population, and a statistic describes the sample.

3. In practice, analysts sample for two reasons: either checking every member is impossible, or it is possible but not worth the time and cost.

4. The trade-off is clean. Sampling saves time and money, but you pay for that convenience with sampling error.

#### Sampling methods

5. Sampling methods split into two big families: probability sampling and non-probability sampling.

6. Probability sampling uses a fixed probability-based selection process, so every element has a known selection logic. That is why it is usually more accurate and reliable for inference.

7. Non-probability sampling does not rely on a fixed probability rule. It leans on accessibility or human selection, which means bias risk is much higher.

8. A sampling plan is just the set of rules used to choose the sample. CFA can make this sound grand, but it really means "what exact method did you use to pick observations?"

9. Simple random sampling is the clean baseline. Every element in the population has an equal probability of being selected.

10. This method works best when the population is fairly homogeneous, meaning the observations are broadly similar in the characteristics that matter.

11. If the population is already pretty similar, simple random sampling is often enough. If the population has important subgroups, simple random sampling may miss or underweight them by bad luck.

12. **Systematic sampling is a practical cousin of random sampling. Instead of coding every member and drawing them individually, you select every $k$th member.**

13. The curriculum treats systematic sampling as approximately random when a fully coded random draw is hard to execute, but the core LOS emphasis stays on simple random, stratified random, cluster, convenience, and judgmental sampling.

14. Sampling error is the difference between the observed value of a statistic and the population quantity it is trying to estimate, simply because you looked at a subset instead of the whole population.

15. This is important: sampling error is not the same thing as fraud, bad modeling, or sloppy math. It is the normal cost of using a sample.

16. A statistic computed from a random sample is itself a random variable, because a different random sample would usually give a different answer.

17. That leads to the idea of a sampling distribution. A sampling distribution is the distribution of all the possible values that a statistic could take when you repeatedly draw same-size samples from the same population.

18. Stratified random sampling improves on simple random sampling when the population naturally falls into meaningful groups.

19. **Stratified means every group is represented**. In bond indexing, strata can be issuer type, maturity bucket, and coupon bucket. If there are 3 issuer types, 10 maturity buckets, and 2 coupon buckets, that creates 60 cells. Minimum one bond per cell means minimum 60 bonds.

20. In stratified random sampling, divide the population into strata based on one or more classification criteria, then draw random subsamples from every stratum in proportion to that stratum’s size.

21. The big exam distinction is this: in stratified random sampling, **all strata are included**. Only the elements inside each stratum are sampled.

22. **==That is why stratified random sampling usually gives greater precision than simple random sampling. It forces the important subgroups into the sample instead of hoping random luck covers them properly.==**

23. Bond indexing is the curriculum’s clean finance application. **A bond index can be huge, so full replication is costly. Stratified sampling lets you match important risk characteristics like duration, sector, credit quality, and call exposure more efficiently.**

24. Cluster sampling also divides the population into groups, but the logic is different. **==Here, each cluster is meant to act like a mini-version of the whole population.==**

25. In one-stage cluster sampling, you randomly choose clusters and then include all members inside the selected clusters. In two-stage cluster sampling, you first choose clusters and then randomly choose a subsample from within each selected cluster.

26. **The trap is mixing up cluster and stratified sampling. Stratified sampling includes all strata and samples within each.** **Cluster sampling includes only some clusters, but may include many or all elements inside those chosen clusters.**

27. **==Cluster sampling is often the most time-efficient and cost-efficient probability method for a huge scattered population, especially in broad geographic surveys.==**

28. The price you usually pay is lower accuracy than other probability methods at the same sample size, because a chosen cluster may be less representative of the full population.

29. Convenience sampling means selecting observations because they are easy to access.

> [!abstract] What is the difference between Cluster and Stratified?
> Imagine a school has **Class A, Class B, Class C, and Class D**.
> 
> In **stratified sampling**, you say: “I want every class represented.” So you take **5 students from A, 5 from B, 5 from C, and 5 from D**. The goal is accuracy. You are making sure no important group is missed.
> 
> In **cluster sampling**, you say: “I cannot sample from every class. I will randomly pick two classes.” Suppose you pick **Class A and Class C**. Then you either survey everyone in those classes, or randomly sample inside those classes. The goal is convenience and lower cost.
> 
> So the memory rule is simple: **stratified means sample from every group; cluster means sample only selected groups**.

5. Its advantage is obvious: it is quick and cheap. Its weakness is also obvious: the resulting sample may not represent the full population well at all.

6. This is why convenience sampling is often fine for a small pilot study, but dangerous if you try to make strong population inference from it.

7. Judgmental sampling means selecting observations based on the researcher’s knowledge and professional judgment.

8. This method can be useful under time pressure or when expert knowledge helps identify the most relevant observations, such as an experienced auditor selecting transactions for review.

9. But the same human judgment that makes it useful also creates bias risk. Judgmental sampling can be smart, but it is never bias-proof.

10. If you need the fast ranking from safest for inference to riskiest for bias, think roughly like this: **==stratified and simple random are usually safer, cluster is practical but often less precise, and convenience and judgmental carry much bigger representativeness risk.==**

> [!question] IDENTIFY THE SAMPLING METHOD
> Problem: An analyst wants data on pharmaceutical companies. She considers three methods: use only firms already in her team’s internal database, select every fifth company from a vendor list, or first divide firms by region and then randomly sample within each region in proportion to region size. What are these three methods?
>
> ---
>
> Solution:
> - Internal database because it is easy to access: **convenience sampling**
> - Every fifth company: **systematic sampling**
> - Divide by region, then randomly sample within each region: **stratified random sampling**
>
> Explanation: the fastest way to solve these questions is to ask what the selection rule is really doing, not what the analyst happens to call it.

#### Sampling from different distributions

36. Bigger samples are not automatically better if you quietly mixed observations from different underlying populations.

37. **==The curriculum’s Sharpe-ratio example makes that point hard. If one year comes from a low-risk strategy and the next year comes from a high-risk strategy, pooling them may create one big sample that represents no real underlying distribution.==**

38. So the real lesson is not "more data always wins." **==The real lesson is "more homogeneous data wins." A smaller clean sample can be better than a larger mixed one.==**

#### Sampling Error

39. Imagine you want the average return of **all 1,000 funds**, but you study only **100 funds**. The average of 100 funds is the **sample statistic**. The true average of all 1,000 funds is the **population parameter**. The gap between them is **sampling error**. Sampling error exists because you used a subset, not the full population.
40. Sampling error is **not automatically a mistake**. Even a perfectly random sample has sampling error, because different random samples give different answers.
41. **==Sampling error is not the same as bias. A random sample can be unbiased but still imperfect. Bias means your method systematically overstates or understates the truth.==**
42. Bigger sample, lower sampling error. But it falls slowly, because standard error falls with the square root of sample size. To cut standard error by half, you need four times the sample size.
43. Sampling error links directly to the **sampling distribution**. If you repeatedly take samples of the same size, each sample mean differs. The distribution of those sample means is the sampling distribution.
#### Central limit theorem

39. The central limit theorem is one of the most useful ideas in quantitative methods because it tells you what happens to the distribution of the sample mean when sample size gets large.

40. The theorem says this: if the population has mean $\mu$ and finite variance $\sigma^2$, then the sampling distribution of the sample mean is approximately normal for large sample sizes, with mean $\mu$ and variance $\sigma^2/n$.

41. Two exam traps hide inside that sentence. First, the theorem is about the **sample mean distribution**, not the raw population distribution. Second, it needs finite variance.

42. The practical magic is that the underlying population does not need to be normal. Even if the population is ugly or unknown, the sample mean becomes approximately normal when the sample is large enough.

43. The curriculum’s rule of thumb is that $n \ge 30$ is often enough, though very non-normal populations may need much larger samples.

44. The mean of the sample-mean distribution is still the population mean. So the center stays at $\mu$.

45. The variance of the sample-mean distribution is $\sigma^2/n$. So as sample size gets larger, the sample mean becomes more tightly clustered around the true population mean.

46. That is the whole intuition: larger samples do not just "feel better." They mathematically squeeze the sampling distribution.

47. **==This is why the central limit theorem supports confidence intervals and hypothesis testing. Once the sample-mean distribution is approximately normal, you can make probability statements about how far your estimate is likely to be from the true population mean.==**

48. **==The theorem does not say a large diversified portfolio must have standard deviation near zero. That is a misuse of the theorem, because the theorem is about the behavior of sample means, not that claim about portfolio risk.==**

#### Standard error of the sample mean

49. The standard error of the sample mean is the standard deviation of the sample-mean distribution.

50. If population standard deviation is known, use:

$$
\sigma_{\bar{X}} = \frac{\sigma}{\sqrt{n}}
$$

51. In practice, population standard deviation is usualSampling from different distributions is one of the most dangerous hidden traps in finance. If regime changes, strategy shifts, or structural breaks happened, pooling the data may create a fake population that means nothing.ly unknown, so analysts more often estimate standard error with:

$$
s_{\bar{X}} = \frac{s}{\sqrt{n}}
$$

52. The sample standard deviation comes from the sample variance:

$$
s^2 = \frac{\sum_{i=1}^{n}(X_i - \bar{X})^2}{n-1}
$$

53. Standard deviation and standard error are not interchangeable. Standard deviation describes spread in the data. Standard error describes imprecision in the estimate caused by sampling.

54. So if you want to talk about how volatile the raw observations are, think standard deviation. If you want to talk about how precise your estimated mean is, think standard error.

55. The formula also gives you a fast exam intuition: if sample size increases by a lot, standard error falls, but only with the square root of sample size. That is why going from 36 to 576 observations cuts standard error from 1 percent to 0.25 percent.

> [!question] STANDARD ERROR OF THE SAMPLE MEAN
> Problem: The cross-sectional population standard deviation of manager returns is 6%. How large a random sample is needed if the analyst wants the standard deviation of sample means to be 1%? What if the target is 0.25%?
>
> ---
>
> Solution:
>
> For a 1% standard error:
>
> $$
> 1\% = \frac{6\%}{\sqrt{n}}
> $$
>
> $$
> \sqrt{n} = 6 \Rightarrow n = 36
> $$
>
> For a 0.25% standard error:
>
> $$
> 0.25\% = \frac{6\%}{\sqrt{n}}
> $$
>
> $$
> \sqrt{n} = 24 \Rightarrow n = 576
> $$
>
> Explanation: to make standard error much smaller, you usually need a dramatically bigger sample.

#### Resampling: bootstrap

56. Bootstrap is a resampling method that repeatedly draws samples from the original sample, with replacement, and keeps each resample the same size as the original sample.

57. ==**"With replacement" matters. After an observation is drawn, it goes back into the pool, so it can appear more than once in the same resample.**==

58. ==**Some original observations may appear several times in a bootstrap resample, and some may not appear at all. That is normal.==**

59. After creating many resamples, compute the statistic you care about for each one, such as the sample mean or sample median.

60. Those repeated resample statistics form the bootstrap sampling distribution, which is used as an approximation to the true sampling distribution.

61. This is why bootstrap is powerful. It lets you estimate standard errors or confidence intervals even when no clean analytical formula exists.

62. The curriculum especially emphasizes that bootstrap is useful for complicated estimators, such as the standard error of a sample median, where the simple sample-mean formula does not apply.

63. Bootstrap is also attractive because it can be accurate and widely useful in finance, such as historical simulation in asset allocation or evaluating investment performance against a benchmark.

64. The bootstrap estimate of standard error is:

$$
s_{\bar{X}} = \sqrt{\frac{1}{B-1}\sum_{b=1}^{B}(\hat{\theta}_b - \bar{\theta})^2}
$$

65. Here $B$ is the number of bootstrap resamples, $\hat{\theta}_b$ is the statistic from resample $b$, and $\bar{\theta}$ is the average across all those resample statistics.

> [!question] BOOTSTRAP INTERPRETATION
> Problem: An analyst needs the standard error of a sample median. Should she use the simple $s/\sqrt{n}$ formula or bootstrap?
>
> ---
>
> Solution:
> Use **bootstrap**.
>
> Explanation: the $s/\sqrt{n}$ shortcut is for the sample mean. Bootstrap is useful when no easy analytical formula exists for the estimator you care about.

#### Resampling: jackknife

66. Jackknife is another resampling technique, but it works differently from bootstrap.

67. **Jackknife** is stricter. It says: “I will remove one observation at a time.” If you have 10 returns, jackknife creates 10 samples: first leave out return 1, then leave out return 2, and so on. No replacement. It is often used to reduce estimator bias, and can also estimate standard error and confidence intervals.

68. Another practical contrast is that jackknife tends to produce similar results across runs, whereas bootstrap usually changes somewhat from run to run because the resamples are randomly drawn.

69. The quickest exam distinction is this: bootstrap is the more flexible general-purpose resampling tool, while jackknife is the leaner leave-one-out tool often linked to bias reduction.

#### Analyst traps and interpretation

72. Probability sampling is generally better for inference, but that does not mean every practical finance problem uses it cleanly. Real datasets, time constraints, and market structure often push analysts toward imperfect sampling plans.

73. The quality of inference depends on both the sampling plan and the quality of the underlying data. A statistically elegant method cannot save garbage inputs.

74. **==Sampling from different distributions is one of the most dangerous hidden traps in finance. If regime changes, strategy shifts, or structural breaks happened, pooling the data may create a fake population that means nothing.==**

75. So the adult version of this module is not just "memorize terms." It is: ask how the sample was built, ask whether the sample actually represents one population, and ask whether the inference tool matches the statistic.
