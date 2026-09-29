Frank is shooting free throws. He makes his first free throw and misses his second free throw. For n≥3, the probability of making the nth free throw is equal to the proportion of free throws he made during his first n−1 attempts. How many free throws can Frank expect to make in 100 attempts?

We know, $P(3) = 1/2$

Let $X = 0$ if miss and $X = 1$ if throw. 

$$ \begin{aligned}
P(n) &= \frac{S}{n-1} \\  S &= (n-1)P(n)
\end{aligned}$$
$$P(n) =  S + X_{n-1}$$

where $S = \sum X \text{ if } X=1$

$$
\begin{aligned}
\mathrm{E}(P_{n+1}) = \mathrm{E}(S/n) \\

\end{aligned}
$$
