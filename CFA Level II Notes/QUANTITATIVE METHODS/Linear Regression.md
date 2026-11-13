1. The intercept never counts as an independent variable.  If a question states that there are five independent variables, the regression contains six variables in total once the intercept is included.
2. With a lagged dependent variable, serial autocorrelation makes the regression coefficients inconsistent. Without a lagged dependent variable, they remain consistent, assuming strict exogeneity.
3. Multicollinearity is caused by inappropriate variable scaling.
4. The DOF of BG F-test is $n-p-k-1$

> Get this through your head: the lower the p-value, the stronger the evidence against the null hypothesis. A p-value is the probability, assuming the null hypothesis is true, of observing a sample at least as extreme as the one you got.

> A Type I error means rejecting a true null hypothesis. If "not pregnant" is the null, it is calling a man pregnant. 
> A Type II error means failing to reject a false null hypothesis: you called a pregnant woman not pregnant.

## Leverage, Outliers and Influential Datapoints

> Leverage is an unusual value of the independent variable X. An outlier is an unusual value of the dependent variable Y. An influential data point is any observation that changes the regression.

Leverage formula:

$$ \boxed {h > 3 \left(\frac{k}{n+1}\right)} $$


The chapter's central point is understanding the difference between leverage, outliers and influential data points. 

**Leverage** refers to any data point with an unusual independent-variable $X$ value. Suppose we are fitting a five-factor model and our stock universe is maybe South Korean stocks, and one company (Samsung) is so large by market capitalization that it overwhelms the rest.

**Outliers** are data points with unusually high or low for the dependent variable that $Y$.Suppose we are fitting a five-factor model, and one company has posted returns so extreme this year that they swamp everything else.

**Influential observations** are the points whose inclusion or exclusion changes the regression as a whole.




