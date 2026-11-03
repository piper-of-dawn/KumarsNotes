## Variant: Read a One-Period Binomial Tree and Find Terminal Payoffs

**Abstract:** *A binomial tree is just two possible prices one step from now; build those prices first, then apply the option payoff rule.*

> A stock is \$80 today. Over one period it can rise by a factor of $1.25$ or fall by a factor of $0.75$. A European call and put both have an exercise price of \$85. Find the two future stock prices and every terminal option payoff.

All prices and payoffs below are USD per share. $S$ is today’s stock price; $u$ and $d$ are the up/down multipliers; $X$ is the exercise price. A terminal payoff is cash at expiry, before subtracting any premium paid today.

**1. Turn the factors into prices**

The up factor is not a 1.25% return. It means the stock becomes **1.25 times** its current price.

$$
S^+=Su=80(1.25)=\boxed{100}
$$

$$
S^-=Sd=80(0.75)=\boxed{60}
$$

**2. Apply the call payoff rule**

A call lets us buy for USD 85. We use it only when the stock is worth more than USD 85.

$$
c^+=\max(0,S^+-X)=\max(0,100-85)=\boxed{15}
$$

$$
c^-=\max(0,S^--X)=\max(0,60-85)=\boxed{0}
$$

**3. Apply the put payoff rule**

A put lets us sell for USD 85. We use it only when the stock is worth less than USD 85.

$$
p^+=\max(0,X-S^+)=\max(0,85-100)=\boxed{0}
$$

$$
p^-=\max(0,X-S^-)=\max(0,85-60)=\boxed{25}
$$

> [!NOTE]
> First build the stock tree. Only then put $\max(0,S-X)$ on a call and $\max(0,X-S)$ on a put.

![[images/one-period-option-payoffs.svg]]

---

## Variant: Calculate Risk-Neutral Probability and Catch an Impossible Tree

**Abstract:** *Risk-neutral probability is a pricing weight forced by no-arbitrage, not our forecast of whether the stock will actually rise.*

> A one-period tree has $u=1.25$, $d=0.80$, and a 5% per-period risk-free rate. Find the risk-neutral up probability. Then test a second tree with the same $u$ and $d$ but a 30% risk-free rate.

**1. Put risk-free growth between the branches**

The pricing weights must make the stock grow at the risk-free rate on average:

$$
\pi u+(1-\pi)d=1+r
$$

Subtract $d$ from both sides, then divide by the difference between the up and down factors:

$$
\pi u+d-\pi d=1+r
\quad\Rightarrow\quad
\pi(u-d)=1+r-d
$$

Therefore:

$$
\pi=\frac{(1+r)-d}{u-d}
$$

For the first tree:

$$
\pi=\frac{1.05-0.80}{1.25-0.80}
=\frac{0.25}{0.45}
=\boxed{0.5556}
$$

So the risk-neutral down weight is:

$$
1-\pi=\boxed{0.4444}
$$

**2. Check the no-arbitrage condition**

A valid tree needs:

$$
d<1+r<u
$$

The first tree passes because $0.80<1.05<1.25$.

For the second tree:

$$
\pi=\frac{1.30-0.80}{1.25-0.80}=1.1111
$$

A probability above 1 is the calculator screaming that the tree is broken. Risk-free growth of $1.30$ beats even the stock's up branch of $1.25$.

For example, short one share for $S$ and invest the proceeds at 30%. At expiry the investment is $1.30S$, while buying back the share costs at most $1.25S$. The trade starts with zero net cash and leaves at least $0.05S$.

$$
\boxed{\text{The second tree violates no-arbitrage.}}
$$

> [!NOTE]
> Before valuing anything, check $d<1+r<u$. If $\pi$ falls outside $[0,1]$, do not keep calculating.

---

## Variant: Value a One-Period Call Two Ways

**Abstract:** *The expected-payoff route and the replication route must land on the same call value because they manufacture the same future cash flows.*

> A stock is USD 100. In one period, $u=1.35$, $d=0.74$, the exercise price is USD 100, and the per-period risk-free rate is 5.15%. Value the European call using both risk-neutral expectation and replication.

**1. Build the end values**

$$
S^+=100(1.35)=135,\qquad S^-=100(0.74)=74
$$

$$
c^+=\max(0,135-100)=35,\qquad c^-=0
$$

**2. Find the pricing weight**

$$
\pi=\frac{1.0515-0.74}{1.35-0.74}=\boxed{0.510656}
$$

**3. Weight the payoffs and discount once**

$$
c=\frac{\pi c^++(1-\pi)c^-}{1+r}
$$

$$
c=\frac{0.510656(35)+0.489344(0)}{1.0515}
=\boxed{16.998}
$$

**4. Build the same payoff with stock and borrowing**

The hedge ratio asks how many shares reproduce the call's change across the two states:

$$
h_c=\frac{c^+-c^-}{S^+-S^-}
=\frac{35-0}{135-74}
=\boxed{0.573770}
$$

Let $L$ be the loan repayment at expiry. Stock minus that repayment must match the call in **both** states:

$$
L=h_cS^+-c^+=\frac{35}{61}(135)-35=42.459016
$$

$$
L=h_cS^--c^-=\frac{35}{61}(74)-0=42.459016
$$

The same repayment works in either state. Discount it to find how much we can borrow today.

$$
\text{Borrow today}=\frac{42.459016}{1.0515}=40.379474
$$

$$
\text{Replication cost}=\frac{35}{61}(100)-40.379474=\boxed{16.998}
$$

> [!NOTE]
> Risk-neutral expectation is not a second theory. It is the same no-arbitrage replication written as weighted cash flows.

---

## Variant: Value a One-Period Put and Check Put-Call Parity

**Abstract:** *A put is replicated with a short stock position plus lending because its value rises when the stock falls.*

> Use the same tree as the previous problem: $S=100$, $X=100$, $u=1.35$, $d=0.74$, $r=5.15\%$, and $\pi=0.510656$. Find the European put value, hedge ratio, and parity check.

**1. Find terminal put payoffs**

$$
p^+=\max(0,100-135)=0
$$

$$
p^-=\max(0,100-74)=26
$$

**2. Price the payoff**

$$
p=\frac{0.510656(0)+0.489344(26)}{1.0515}
=\boxed{12.100}
$$

**3. Find the put hedge ratio**

$$
h_p=\frac{0-26}{135-74}=\boxed{-0.426230}
$$

The negative sign means short stock. The lending leg supplies the rest of the payoff.

Let $B_T$ be the cash available from lending at expiry. The stock-plus-cash payoff must equal the put:

$$
B_T=p^+-h_pS^+=0-\left(-\frac{26}{61}\right)(135)=57.540984
$$

In the down state, the same cash leaves $57.540984-(26/61)(74)=26$, exactly the put payoff. Discount the maturity cash to find the amount lent today:

$$
\frac{57.541}{1.0515}=54.723
$$

So the replicated put costs:

$$
-0.426230(100)+54.723=\boxed{12.100}
$$

**4. Check put-call parity**

For a one-period European option with no carry benefit:

$$
c-p=S-\frac{X}{1+r}
$$

Left side:

$$
16.998-12.100=4.898
$$

Right side:

$$
100-\frac{100}{1.0515}=4.898
$$

$$
\boxed{\text{Parity holds.}}
$$

> [!NOTE]
> A long call has a non-negative hedge ratio; a long put has a non-positive hedge ratio. The sign is a fast error check.

---

## Variant: Arbitrage an Overpriced or Underpriced Call

**Abstract:** *If the market option and its replicating portfolio have different prices, buy the cheap copy and sell the expensive copy.*

> The fair one-period call value is USD 16.998. First suppose the market call trades at USD 20. Then suppose it trades at USD 15. State the arbitrage and today’s locked-in profit in each case.

**1. Market call at USD 20: the option is expensive**

Sell the call for USD 20 and buy its exact replication for USD 16.998.

$$
\text{Cash today}=20-16.998=\boxed{3.002}
$$

At expiration, the replication pays whatever the short call owes. Future net payoff is zero in both states, so the USD 3.002 is genuinely locked in today.

**2. Market call at USD 15: the option is cheap**

Buy the call for USD 15 and short the replicating portfolio worth USD 16.998.

$$
\text{Cash today}=16.998-15=\boxed{1.998}
$$

Again, the long call and short replication cancel in every future state.

**3. Spell out the replicating trades**

From the earlier tree, one call is replicated by **buying $35/61=0.573770$ shares and borrowing USD 40.379474**. For the USD 20 call, sell the call, buy those shares, and borrow that amount. For the USD 15 call, reverse every trade: buy the call, short those shares, and lend USD 40.379474.

At expiry the stock-and-loan replica pays $(35,0)$ in the up/down states. Thus expensive-call arbitrage has net payoffs $(-35,-0)+(35,0)=(0,0)$; cheap-call arbitrage reverses both signs.

> [!NOTE]
> Arbitrage needs no forecast: opposite future cash flows cancel, while the price gap is collected immediately.

---

## Variant: Roll Back a Two-Period European Call

**Abstract:** *A two-period tree is just three one-period problems: value the two Time-1 nodes, then value today.*

> A stock is $7.35$, with $u=1.445$, $d=0.715$, $X=8$, and a 4.35% risk-free rate per period. Value a two-period European call.

**1. Find the risk-neutral weight**

$$
\pi=\frac{1.0435-0.715}{1.445-0.715}=\boxed{0.45}
$$

At Time 1, $S^+=7.35(1.445)=10.62075$ and $S^-=7.35(0.715)=5.25525$. Two moves give $S^{++}=Su^2$, $S^{+-}=Sud$, and $S^{--}=Sd^2$. Up-then-down and down-then-up meet because $ud=du$.

**2. Build terminal stock prices and call payoffs**

$$
S^{++}=7.35(1.445)^2=15.347,\quad c^{++}=7.347
$$

$$
S^{+-}=7.35(1.445)(0.715)=7.594,\quad c^{+-}=0
$$

$$
S^{--}=7.35(0.715)^2=3.758,\quad c^{--}=0
$$

Each terminal call pays $\max(S_2-8,0)$. Only the top stock price exceeds 8, so only that branch pays. **Continuation value** means the value of keeping the option alive: take its two next-step values, weight by $\pi$ and $1-\pi$, then discount one period. Rounded tree values are displayed; carry full precision through the calculation.

**3. Roll back to Time 1**

$$
c^+=\frac{0.45(7.347)+0.55(0)}{1.0435}=\boxed{3.168}
$$

$$
c^-=\frac{0.45(0)+0.55(0)}{1.0435}=\boxed{0}
$$

**4. Roll back once more**

$$
c_0=\frac{0.45(3.168)+0.55(0)}{1.0435}
=\boxed{1.366}
$$

> [!NOTE]
> Discount one step at a time. Do not discount a Time-1 option value by two periods again.

![[images/two-period-european-call.svg]]

---

## Variant: Value a Two-Period European Put and Cross-Check with Parity

**Abstract:** *Work backward exactly as for the call, then use put-call parity as an independent checksum.*

> Keep $S=7.35$, $u=1.445$, $d=0.715$, $X=8$, $r=4.35\%$, and $\pi=0.45$. Value the matching two-period European put.

Rebuild the stock endpoints from the question: $S^{++}=7.35(1.445)^2=15.346984$, $S^{+-}=7.35(1.445)(0.715)=7.593836$, and $S^{--}=7.35(0.715)^2=3.757504$. Apply $\max(8-S_2,0)$ at each endpoint; a negative payoff is replaced by zero.

**1. Find terminal put payoffs**

$$
p^{++}=0,\qquad p^{+-}=8-7.594=0.406
$$

$$
p^{--}=8-3.758=4.242
$$

**2. Roll back to Time 1**

$$
p^+=\frac{0.45(0)+0.55(0.406)}{1.0435}=\boxed{0.214}
$$

$$
p^-=\frac{0.45(0.406)+0.55(4.242)}{1.0435}=\boxed{2.411}
$$

**3. Roll back to today**

$$
p_0=\frac{0.45(0.214)+0.55(2.411)}{1.0435}
=\boxed{1.363}
$$

**4. Use two-period parity**

$$
p=c-S+\frac{X}{(1+r)^2}
$$

$$
p=1.366-7.35+\frac{8}{1.0435^2}=\boxed{1.363}
$$

> [!NOTE]
> If backward induction and parity disagree beyond rounding, a payoff, probability, or discounting step is wrong.

![[images/two-period-european-put.svg]]

---

## Variant: Calculate Node-by-Node Hedge Ratios

**Abstract:** *The hedge ratio changes as the tree moves, so a multiperiod replication must be rebalanced at every node.*

> Use the preceding two-period tree. Find the call and put hedge ratios at each Time-1 node and at Time 0.

A hedge ratio is **shares per option**. At any node, holding $h$ shares changes the stock position’s value by $h(S_{next}^{up}-S_{next}^{down})$. Match this to the option-value difference and solve:

$$
h=\frac{V_{next}^{up}-V_{next}^{down}}{S_{next}^{up}-S_{next}^{down}}
$$

Today’s denominator uses **Time-1** stock prices: $7.35(1.445)=10.62075$ and $7.35(0.715)=5.25525$. At a Time-1 node, use its two **Time-2** children instead. This keeps numerator and denominator at the same date.

**1. Call hedge ratios at Time 1**

After an up move:

$$
h_c^+=\frac{7.347-0}{15.347-7.594}=\boxed{0.9476}
$$

After a down move:

$$
h_c^-=\frac{0-0}{7.594-3.758}=\boxed{0}
$$

**2. Call hedge ratio today**

$$
h_{c,0}=\frac{3.168-0}{10.621-5.255}=\boxed{0.5905}
$$

**3. Put hedge ratios at Time 1**

$$
h_p^+=\frac{0-0.406}{15.347-7.594}=\boxed{-0.0524}
$$

$$
h_p^-=\frac{0.406-4.242}{7.594-3.758}=\boxed{-1.0000}
$$

**4. Put hedge ratio today**

$$
h_{p,0}=\frac{0.214-2.411}{10.621-5.255}=\boxed{-0.4095}
$$

The hedge is not “set it and forget it.” The option’s exposure changes after the stock moves.

> [!NOTE]
> A multiperiod option is dynamically replicated: calculate a fresh hedge ratio from the two next-node values at every node.

---

## Variant: Compare European and American Put Values

**Abstract:** *At every American-option node, compare the value of waiting with the cash from exercising right now and keep the larger number.*

> A stock is $26$, with $X=25$, $u=1.466$, $d=0.656$, $r=2.05\%$ per period, and two periods remaining. Value the European and American puts.

**1. The pricing weight and terminal payoffs**

$$
\pi=\frac{1.0205-0.656}{1.466-0.656}=0.45
$$

Build the endpoints, then apply $\max(25-S_2,0)$:

$$
\begin{aligned}
S^{++}&=26(1.466)^2=55.878056,&p^{++}&=0\\
S^{+-}&=26(1.466)(0.656)=25.004096,&p^{+-}&=0\\
S^{--}&=26(0.656)^2=11.189056,&p^{--}&=13.810944
\end{aligned}
$$

These are expiry payoffs, so there is no continuation decision at Time 2.

**2. European continuation values at Time 1**

$$
p^+=\frac{0.45(0)+0.55(0)}{1.0205}=0
$$

$$
p^-=\frac{0.45(0)+0.55(13.811)}{1.0205}=\boxed{7.4436}
$$

Therefore:

$$
p_{E,0}=\frac{0.45(0)+0.55(7.4436)}{1.0205}
=\boxed{4.0117}
$$

At the Time-1 up node, $S^+=26(1.466)=38.116$, so immediate exercise pays $\max(25-38.116,0)=0$. Waiting also gives zero; the American up-node value stays zero.

**3. Check immediate exercise at the down node**

The stock there is $26(0.656)=17.056$.

$$
\text{Exercise value}=25-17.056=\boxed{7.9440}
$$

Exercise value $7.9440$ beats continuation value $7.4436$, so replace the node value with $7.9440$.

$$
p_{A,0}=\frac{0.45(0)+0.55(7.9440)}{1.0205}
=\boxed{4.2814}
$$

The root is an exercise node too: $\max(25-26,0)=0$, below the rolled-back value $4.2814$. Therefore keeping the option is optimal today.

$$
\text{Early-exercise premium}=4.2814-4.0117=\boxed{0.2697}
$$

> [!NOTE]
> For an American option, every non-terminal node is $\max(\text{continuation value},\text{exercise value})$.

![[images/two-period-american-put.svg]]

---

## Variant: Reject Early Exercise for a Non-Dividend-Paying American Call

**Abstract:** *An American call’s extra exercise freedom is worthless when the stock pays no dividend because exercising early throws away time value and pays the strike too soon.*

> In the earlier $S=7.35$, $X=8$, two-period tree, the Time-1 stock values are $10.621$ after an up move and $5.255$ after a down move. Use $u=1.445$, $d=0.715$, $r=4.35\%$ per period, and $\pi=0.45$ to calculate the continuation values. Should an American call be exercised at either node, and what is its value today?

The terminal stock prices are $7.35(1.445)^2=15.346984$, $7.35(1.445)(0.715)=7.593836$, and $7.35(0.715)^2=3.757504$. Applying $\max(S_2-8,0)$ gives call payoffs $7.346984$, $0$, and $0$. Weight the two children of each node and discount one period to calculate continuation.

**1. Test the up node**

$$
\text{Exercise value}=\max(0,10.621-8)=\boxed{2.621}
$$

$$
C_1^+=\frac{0.45(7.346984)+0.55(0)}{1.0435}=\boxed{3.168}
$$

Waiting wins because $3.168>2.621$.

**2. Test the down node**

$$
\text{Exercise value}=\max(0,5.255-8)=\boxed{0}
$$

$$
C_1^-=\frac{0.45(0)+0.55(0)}{1.0435}=\boxed{0}
$$

There is nothing to gain from exercising there either.

**3. Keep the European node values**

Because no node is replaced, the American call and European call have the same value:

$$
c_A=c_E=\frac{0.45(3.168)+0.55(0)}{1.0435}=\boxed{1.366}
$$

Today’s exercise value is $\max(7.35-8,0)=0$, also below continuation. At the down node, a zero/zero tie means exercise provides no benefit.

> [!NOTE]
> “American” does not automatically mean “more valuable.” The right to do something useless has zero value.

---

## Variant: Exercise an American Call Before a Known Dividend

**Abstract:** *Separate the known dividend from the stock’s risky value, build the ex-dividend tree, and calculate waiting value before comparing it with exercise just before the dividend.*

> A stock is USD 100, a two-period American call has $X=95$, the per-period risk-free rate is 1%, and $u=1.224$, $d=0.796$. A USD 3 dividend is paid at Time 1. Calculate the continuation value at the Time-1 up node, decide whether to exercise, and find the European and American values today. Use the escrowed-dividend tree below.

**1. Separate the dividend from the growing stock component**

The USD 3 payment is known, so discount it one period and remove it from today’s stock price. The remaining component, $S_0^*$, follows the up/down factors:

$$
PV(D)=\frac{3}{1.01}=2.970297,\qquad S_0^*=100-2.970297=97.029703
$$

$$
S_1^{*,+}=97.029703(1.224)=118.764356,\qquad
S_1^{*,-}=97.029703(0.796)=77.235644
$$

These are **after-dividend** prices. Just before payment, the share still includes the USD 3: $S_1^+=121.764356$ and $S_1^-=80.235644$.

**2. Build the terminal prices and option payoffs**

No dividends remain after Time 1. Grow the ex-dividend prices for one more period, then apply $\max(S_2-95,0)$:

$$
\begin{aligned}
S_2^{++}&=118.764356(1.224)=145.367572,&c_2^{++}&=50.367572\\
S_2^{+-}&=118.764356(0.796)=94.536356,&c_2^{+-}&=0\\
S_2^{--}&=77.235644(0.796)=61.479572,&c_2^{--}&=0
\end{aligned}
$$

**3. Calculate continuation: what is waiting worth at Time 1?**

The pricing weight is $\pi=(1.01-0.796)/(1.224-0.796)=0.5$. A call holder who waits receives no dividend, so use the **after-dividend** tree’s future option payoffs:

$$
C_1^+=\frac{0.5(50.367572)+0.5(0)}{1.01}=\boxed{24.9344}
$$

$$
C_1^-=\frac{0.5(0)+0.5(0)}{1.01}=\boxed{0}
$$

**4. Compare with exercise immediately before payment**

At the up node, exercise buys the share while it still includes the dividend:

$$
E_1^+=\max(121.764356-95,0)=\boxed{26.764356}>24.934442
$$

Thus $c_{A,1}^+=26.764356$. At the down node, $E_1^-=\max(80.235644-95,0)=0=C_1^-$, so $c_{A,1}^-=0$.

**5. Roll back the chosen values and check today’s exercise**

$$
c_{E,0}=\frac{0.5(24.934442)+0.5(0)}{1.01}=\boxed{12.3438}
$$

$$
c_{A,0}=\max\left(100-95,\frac{0.5(26.764356)+0.5(0)}{1.01}\right)=\boxed{13.2497}
$$

The American right adds $13.2497-12.3438=\boxed{0.9059}$ USD per share today.

> [!NOTE]
> Continuation uses future option payoffs; pre-dividend exercise uses the share price including the dividend. Do not add USD 3 again to either option value.

---

## Variant: Exercise an American Call on a Coupon Bond

**Abstract:** *A bond coupon is carry just like a stock dividend, so an American call on a coupon bond can rationally be exercised early.*

> A two-year call on a 7% annual-coupon bond has exercise price USD 100 and can be exercised after Year 1. At the Year-1 up node, the bond is USD 100.57 and the European continuation value is USD 0.29. At the Year-1 down node, the bond is USD 103.80 and continuation value is USD 1.35. The one-year rate is 3%, and the risk-neutral branch weights are 50/50. Find the American call value today.

Here the Year-1 bond prices and continuation values are **supplied inputs**. The question does not supply the Year-2 bond prices or Year-1 node rates needed to rebuild them. For a full tree, continuation would be $C_1^j=[0.5c_2^{j,u}+0.5c_2^{j,d}]/(1+r_1^j)$, with $c_2=\max(B_2-100,0)$. Do not use today’s 3% rate as a substitute for missing future node rates.

Compare the supplied waiting values with exercise at the same Year-1 valuation instant. The quoted bond prices are the exercise deliverable prices; do not add the 7% coupon again.

**1. Compare at the up node**

$$
\text{Exercise value}=100.57-100=\boxed{0.57}
$$

Because USD 0.57 > USD 0.29, exercise replaces continuation.

**2. Compare at the down node**

$$
\text{Exercise value}=103.80-100=\boxed{3.80}
$$

Because USD 3.80 > USD 1.35, exercise replaces continuation here too.

**3. Roll the chosen values back**

$$
c_A=\frac{0.5(0.57)+0.5(3.80)}{1.03}
=\boxed{2.12}
$$

Using the supplied continuation values, the comparable European call is:

$$
c_{E,0}=\frac{0.5(0.29)+0.5(1.35)}{1.03}=0.796117\approx\boxed{0.80}
$$

The early-exercise feature adds $2.121359-0.796117=\boxed{1.33}$ USD per bond price unit, using unrounded values. The supplied data specify the Year-1 decision; today’s bond price is not given, so a separate Time-0 exercise test cannot be calculated.

> [!NOTE]
> For any carry-paying underlying—dividend stock or coupon bond—test exercise before the carry leaves the asset.

---

## Variant: Value an Interest Rate Option with a Two-Period Rate Tree

**Abstract:** *The rollback logic is unchanged, but each rate-tree node has its own discount factor because the interest rate itself is moving.*

> A two-year European call and put are written on the one-year spot rate, with a USD 1,000,000 notional and 3.25% exercise rate. The risk-neutral up probability is 50%. Terminal rates are 3.9706%, 3.2542%, and 2.2593%. Time-1 discount factors are 0.962386 and 0.974627, and today’s factor is 0.970446. Value both options.

Let $K=0.0325$. This simplified contract pays $N_0\max(R_2-K,0)$ for the call or $N_0\max(K-R_2,0)$ for the put **at Time 2**, with a one-year accrual factor of 1. The supplied discount factors move cash back one step; multiply by them rather than dividing again.

**1. Terminal payoffs per USD 1 of notional**

$$
c^{++}=0.039706-0.0325=0.007206
$$

$$
c^{+-}=0.032542-0.0325=0.000042,\qquad c^{--}=0
$$

$$
p^{++}=0,\qquad p^{+-}=0,\qquad p^{--}=0.0325-0.022593=0.009907
$$

At each Time-1 node, average its two child payoffs, then multiply by **that node’s** factor: 0.962386 after up, 0.974627 after down. Only the final rollback uses today’s 0.970446. Retain the unrounded node values until after notional scaling.

**2. Roll back using the discount factor at each node**

$$
c^+=0.962386[0.5(0.007206)+0.5(0.000042)]=0.003487686864
$$

$$
c^-=0.974627[0.5(0.000042)+0.5(0)]=0.000020467167
$$

$$
p^+=0
$$

$$
p^-=0.974627[0.5(0)+0.5(0.009907)]=0.0048278148445
$$

**3. Roll back to today and scale the notional**

$$
c_0=0.970446[0.5(0.003487686864)+0.5(0.000020467167)]=0.001702237023
$$

$$
p_0=0.970446[0.5(0)+0.5(0.0048278148445)]=0.002342566802
$$

$$
\text{Call value}=1{,}000{,}000(0.001702237023)=\boxed{\$1{,}702.24}
$$

$$
\text{Put value}=1{,}000{,}000(0.002342566802)=\boxed{\$2{,}342.57}
$$

> [!NOTE]
> This simplified tree cash-settles at Time 2. The later Black-model problem handles the real-world deferred-settlement adjustment.

![[images/two-period-rate-option.svg]]

---

## Variant: Calculate BSM Call and Put Values and Replicating Positions

**Abstract:** *BSM is still stock minus financing for a call, and financing minus stock for a put; the normal-distribution terms tell us the quantities.*

> A European stock option has $S=100$, $X=100$, continuously compounded $r=5\%$, $T=1$, and $\sigma=30\%$. Calculate $d_1$, $d_2$, the call, the put, and both initial replicating positions.

$S$ is the share price, $X$ the strike, $T$ years to expiry, $r$ the continuous annual risk-free rate, and $\sigma$ annual volatility. $d_1$ and $d_2$ are standardized model inputs; $N(z)$ is the standard normal cumulative probability up to $z$, obtained from a normal table or CDF function. It is a **lookup**, not multiplication by $N$.

**1. Calculate the two standardized inputs**

$$
d_1=\frac{\ln(S/X)+(r+\sigma^2/2)T}{\sigma\sqrt{T}}
=\frac{0+(0.05+0.30^2/2)}{0.30}
=\boxed{0.3167}
$$

$$
d_2=d_1-\sigma\sqrt{T}=0.3167-0.30=\boxed{0.0167}
$$

Using unrounded $d_1,d_2$, the table/CDF gives the values below. Normal symmetry gives $N(-d_1)=1-0.624252=0.375748$ and $N(-d_2)=1-0.506649=0.493351$:

$$
N(d_1)=0.624252,\qquad N(d_2)=0.506649
$$

**2. Value the call**

$$
c=SN(d_1)-Xe^{-rT}N(d_2)
$$

$$
c=100(0.624252)-100e^{-0.05}(0.506649)=\boxed{14.23}
$$

**3. Value the put**

$$
p=Xe^{-rT}N(-d_2)-SN(-d_1)
$$

$$
p=100e^{-0.05}(0.493351)-100(0.375748)=\boxed{9.35}
$$

**4. Read the replication directly from BSM**

Call: buy $N(d_1)=0.624252$ shares and short $N(d_2)=0.506649$ zero-coupon bonds whose price is $Xe^{-rT}=95.123$.

Put: short $N(-d_1)=0.375748$ shares and buy $N(-d_2)=0.493351$ of those bonds.

The call’s initial share cost is $100(0.624252)=62.4252$; the borrowing leg is $100e^{-0.05}(0.506649)\approx48.1939$. Their difference is USD 14.23. The put’s lending leg is $100e^{-0.05}(0.493351)\approx46.9291$ and its short-share proceeds are $100(0.375748)=37.5748$, leaving a net cost of USD 9.35.

Each zero-coupon bond here pays **USD 100 at expiry**. These positions describe the initial replication; share and financing quantities must be rebalanced as inputs change.

> [!NOTE]
> BSM uses continuous compounding. If given a discrete annual rate $r_d$, convert with $r=\ln(1+r_d)$.

---

## Variant: Apply BSM to a Dividend-Paying Stock

**Abstract:** *A dividend yield is a carry benefit: it lowers the stock piece of a call and raises the relative value of a put.*

> A European option has $S=60$, $X=60$, $r=2\%$, $T=0.5$, continuous dividend yield $\delta=2\%$, and $\sigma=45\%$. Value the call and put.

Here $\delta=0.02$ is a continuous annual dividend yield, and $T=0.5$ years. The call holder misses dividends earned by a shareholder, so the stock component is adjusted to $Se^{-\delta T}$. Both $r$ and $\delta$ use continuous compounding.

**1. Put the dividend yield inside $d_1$**

$$
\begin{aligned}
d_1&=\frac{\ln(S/X)+(r-\delta+\sigma^2/2)T}{\sigma\sqrt{T}}\\
&=\frac{\ln(60/60)+(0.02-0.02+0.45^2/2)(0.5)}{0.45\sqrt{0.5}}\\
&=\boxed{0.15910}
\end{aligned}
$$

$$
d_2=0.159099-0.45\sqrt{0.5}=\boxed{-0.15910}
$$

$$
N(d_1)=0.563204572,\qquad N(d_2)=0.436795428
$$

**2. Value the call**

$$
c=Se^{-\delta T}N(d_1)-Xe^{-rT}N(d_2)
$$

$$
c=60e^{-0.02(0.5)}(0.563204572)-60e^{-0.02(0.5)}(0.436795428)
=\boxed{7.5091}
$$

**3. Value the put**

$$
p=Xe^{-rT}N(-d_2)-Se^{-\delta T}N(-d_1)
$$

Since $N(-z)=1-N(z)$, $N(-d_2)=0.563204572$ and $N(-d_1)=0.436795428$:

$$
p=60e^{-0.02(0.5)}(0.563204572)-60e^{-0.02(0.5)}(0.436795428)=\boxed{7.5091}
$$

They are equal here because $S=X$ and $r=\delta$, so carry-adjusted parity has a zero right-hand side:

$$
c-p=Se^{-\delta T}-Xe^{-rT}=0
$$

> [!NOTE]
> Do not subtract a continuous dividend yield from $S$. Use $Se^{-\delta T}$ and replace $r$ with $r-\delta$ inside $d_1$.

---

## Variant: Apply BSM to a Currency Option

**Abstract:** *Treat the foreign risk-free rate as the currency’s dividend yield because holding foreign currency earns the foreign rate.*

> The spot rate is JPY135 per EUR. A six-month European option on EUR has $X=135$, Japanese risk-free rate $r_d=0.25\%$, euro risk-free rate $r_f=1.00\%$, and volatility $\sigma=12\%$. Find the call and put values in yen per euro.

**1. Map the rates before touching the formula**

The domestic rate discounts yen. The foreign rate acts like carry on the underlying euro.

$$
\begin{aligned}
d_1&=\frac{\ln(S/X)+(r_d-r_f+\sigma^2/2)T}{\sigma\sqrt{T}}\\
&=\frac{\ln(135/135)+(0.0025-0.0100+0.12^2/2)(0.5)}{0.12\sqrt{0.5}}\\
&=\boxed{-0.001768}
\end{aligned}
$$

$$
d_2=-0.001768-0.12\sqrt{0.5}=\boxed{-0.086621}
$$

$$
N(d_1)=0.499294763,\qquad N(d_2)=0.465486553
$$

**2. Value the EUR call**

$$
\begin{aligned}
c&=Se^{-r_fT}N(d_1)-Xe^{-r_dT}N(d_2)\\
&=135e^{-0.0100(0.5)}(0.499294763)\\
&\quad-135e^{-0.0025(0.5)}(0.465486553)\\
&=\boxed{\text{JPY }4.3064\text{ per EUR}}
\end{aligned}
$$

For the put, normal symmetry gives $N(-d_2)=1-0.465486553=0.534513447$ and $N(-d_1)=1-0.499294763=0.500705237$. Values below use unrounded normal probabilities.

**3. Value the EUR put**

$$
\begin{aligned}
p&=Xe^{-r_dT}N(-d_2)-Se^{-r_fT}N(-d_1)\\
&=135e^{-0.0025(0.5)}(0.534513447)\\
&\quad-135e^{-0.0100(0.5)}(0.500705237)\\
&=\boxed{\text{JPY }4.8111\text{ per EUR}}
\end{aligned}
$$

> [!NOTE]
> First identify the quote. For JPY per EUR, EUR is the underlying and its rate is the carry yield; JPY is domestic and supplies the discount rate.

---

## Variant: Check BSM Lower and Upper Bounds at Zero Volatility

**Abstract:** *When volatility collapses toward zero, an option collapses toward its no-arbitrage lower bound rather than automatically becoming worthless.*

> A one-year European option has $S=100$, $X=95$, $r=4\%$, no dividends, and volatility approaching zero. Find the call and put lower bounds and the upper bounds.

**1. Present-value the strike**

$$
PV(X)=95e^{-0.04}=\boxed{91.2750}
$$

A European call can wait until expiry to pay USD 95, so compare the stock with **today’s cost of funding that future strike**, $PV(X)$, rather than with 95 today. The put reverses the comparison. The maximum with zero reflects the right to let an option expire.

**2. Find the lower bounds**

$$
c\geq\max[0,S-PV(X)]
=\max(0,100-91.2750)
=\boxed{8.7250}
$$

$$
p\geq\max[0,PV(X)-S]
=\max(0,91.2750-100)
=\boxed{0}
$$

With zero volatility, the future is effectively deterministic under the model, so these are also the limiting model values.

**3. Check the upper bounds**

A call payoff never exceeds the stock itself, so its price cannot exceed the cost of buying the stock. A put payoff never exceeds the strike paid at expiry, so its price cannot exceed the cost of funding that strike today.

$$
c\leq S=\boxed{100}
$$

$$
p\leq PV(X)=\boxed{91.2750}
$$

> [!NOTE]
> “Volatility goes to zero” does not mean “option goes to zero.” Discounted intrinsic value can remain positive.

---

## Variant: Value Calls and Puts on Futures with Black’s Model

**Abstract:** *For a futures option, Black’s model uses the futures price—not the spot price—and discounts the whole expected payoff.*

> An index spot is 1,860, but its 0.25-year futures price is 1,851.65. A European futures option has $X=1{,}860$, $r=0.2\%$, $T=0.25$, and $\sigma=15\%$. The contract multiplier is 250. Find the call and put values.

**1. Use the futures price in $d_1$**

$$
\begin{aligned}
d_1&=\frac{\ln[F_0(T)/X]+(\sigma^2/2)T}{\sigma\sqrt{T}}\\
&=\frac{\ln(1851.65/1860)+(0.15^2/2)(0.25)}{0.15\sqrt{0.25}}\\
&=\boxed{-0.02249}
\end{aligned}
$$

$$
d_2=-0.0224914-0.15\sqrt{0.25}=\boxed{-0.09749}
$$

$$
N(d_1)=0.491027990,\qquad N(d_2)=0.461168086
$$

The discount factor is $e^{-0.002(0.25)}=0.9995001$. Normal symmetry gives $N(-d_2)=0.538831914$ and $N(-d_1)=0.508972010$. Use unrounded CDF values and premiums before multiplying by 250 USD per index point.

**2. Price each option in index points**

$$
\begin{aligned}
c&=e^{-rT}[F_0(T)N(d_1)-XN(d_2)]\\
&=e^{-0.002(0.25)}[1851.65(0.491027990)-1860(0.461168086)]\\
&\approx\boxed{51.413625}
\end{aligned}
$$

$$
\begin{aligned}
p&=e^{-rT}[XN(-d_2)-F_0(T)N(-d_1)]\\
&=e^{-0.002(0.25)}[1860(0.538831914)-1851.65(0.508972010)]\\
&\approx\boxed{59.759451}
\end{aligned}
$$

**3. Apply the multiplier last**

$$
\text{Call contract}=51.4136(250)=\boxed{\$12{,}853.41}
$$

$$
\text{Put contract}=59.7595(250)=\boxed{\$14{,}939.86}
$$

> [!NOTE]
> Spot 1,860 and dividend yield are distractions once the futures price is supplied. Scale by the contract multiplier only after finding points.

---

## Variant: Value a Deferred-Settlement Interest Rate Call and Put

**Abstract:** *An interest rate option uses the FRA rate as its underlying, multiplies by the accrual period, and discounts to payment—not merely to option expiry.*

> On 15 May, a three-month loan beginning 15 June has FRA rate 0.68%. A call and put expire on 15 June with exercise rate 0.60%, notional SGD10,000,000, accrual period 0.25, volatility 25%, and continuously compounded discount rate 0.55%. Use $T=31/365$ and pay on 15 September, $T+0.25$ years from valuation.

The **FRA** is today’s forward rate for the future loan, $F=0.0068$; $K=R_X=0.0060$ is the strike. The rate is observed at expiry $T=31/365$, but the cash is paid at $T+AP$, where $AP=0.25$ is the loan accrual fraction. The call payoff at payment is $N_0AP\max(L_T-K,0)$; the put reverses the rate difference. Multiplying an annual rate difference by $AP$ converts it into a quarterly interest amount.

**1. Use decimal rates inside the logarithm**

$$
d_1=\frac{\ln(0.0068/0.0060)+(0.25^2/2)(31/365)}{0.25\sqrt{31/365}}
=\boxed{1.75435}
$$

$$
d_2=d_1-0.25\sqrt{31/365}=\boxed{1.68149}
$$

$$
N(d_1)=0.960314313,\qquad N(d_2)=0.953665886
$$

**2. Discount to the payment date**

$$
DF=e^{-0.0055[(31/365)+0.25]}=\boxed{0.998160}
$$

**3. Value the call**

$$
c=N_0(AP)(DF)[FRA\,N(d_1)-R_XN(d_2)]
$$

$$
\begin{aligned}
c&=10{,}000{,}000(0.25)(0.998159572)\\
&\quad\times\bigl[0.0068(0.960314313)\\
&\qquad-0.0060(0.953665886)\bigr]\\
&\approx\boxed{\text{SGD }2{,}016.64}
\end{aligned}
$$

**4. Value the put**

$$
p=N_0(AP)(DF)[R_XN(-d_2)-FRA\,N(-d_1)]
$$

Use normal symmetry to get the put’s probability inputs:

$$
\begin{aligned}
N(-d_2)&=1-0.953665886=\boxed{0.046334114}\\
N(-d_1)&=1-0.960314313=\boxed{0.039685687}
\end{aligned}
$$

$$
\begin{aligned}
p&=10{,}000{,}000(0.25)(0.998159572)\\
&\quad\times\bigl[0.0060(0.046334114)\\
&\qquad-0.0068(0.039685687)\bigr]\\
&\approx\boxed{\text{SGD }20.32}
\end{aligned}
$$

Normal probabilities are displayed rounded; carry their full precision and $DF=0.998159572$ to obtain the cent amounts. This matters especially for the small put, which subtracts two similar numbers.

The parity difference is a useful checksum:

$$
c-p=10{,}000{,}000(0.25)(0.998159572)(0.0068-0.0060)=\boxed{\text{SGD }1{,}996.32}
$$

> [!NOTE]
> Three classic traps: use the FRA, enter 0.0068 rather than 0.68, and discount through the underlying deposit’s maturity.

---

## Variant: Show Caplet-Floorlet Parity at an At-Market Strike

**Abstract:** *When strike equals the current FRA rate, a matching caplet and floorlet have the same value.*

> Keep the previous problem’s inputs, but set the exercise rate equal to the FRA rate of 0.68%. Find the caplet and floorlet values.

**1. The log-moneyness term disappears**

Because $FRA=R_X$:

$$
\ln(FRA/R_X)=\ln(1)=0
$$

$$
d_1=\frac{(0.25^2/2)(31/365)}{0.25\sqrt{31/365}}
=0.036429
$$

$$
d_2=-0.036429
$$

Here $F=K=0.0068$. The normal lookups are $N(d_1)=0.514529760$ and $N(d_2)=0.485470240$. Because $d_2=-d_1$, the put’s complementary probabilities are $N(-d_2)=0.514529760$ and $N(-d_1)=0.485470240$.

**2. Calculate both values**

Using notional SGD10,000,000, $AP=0.25$, and $DF=0.998160$:

$$
\begin{aligned}
\text{Caplet}&=N_0AP\,DF[F N(d_1)-K N(d_2)]\\
&=10{,}000{,}000(0.25)(0.998159572)\\
&\quad\times0.0068[0.514529760-0.485470240]\\
&=\boxed{\text{SGD }493.10}
\end{aligned}
$$

$$
\begin{aligned}
\text{Floorlet}&=N_0AP\,DF[K N(-d_2)-F N(-d_1)]\\
&=10{,}000{,}000(0.25)(0.998159572)\\
&\quad\times0.0068[0.514529760-0.485470240]\\
&=\boxed{\text{SGD }493.10}
\end{aligned}
$$

Parity explains the equality:

$$
c-p=N_0(AP)(DF)(FRA-R_X)=0
$$

> [!NOTE]
> A cap is a strip of rate calls; a floor is a strip of rate puts. At the at-market swap strike, equal-value cap and floor positions create swap equivalences.

---

## Variant: Value Payer and Receiver Swaptions

**Abstract:** *A payer swaption is call-like on the forward fixed swap rate; a receiver swaption is put-like, and the annuity factor carries the discounting.*

> A three-month option enters a five-year swap. The forward five-year swap rate is 2.65%, exercise rate is 2.50%, volatility is 20%, accrual period is 0.5, sum of today’s discount factors to the ten semiannual swap payment dates is $PVA=8.9$ (before multiplying by accrual), and notional is USD 10,000,000. Value payer and receiver swaptions.

A **payer** chooses to pay fixed at $K=2.50\%$ and receive floating; this is valuable when the market swap rate is higher. A **receiver** chooses the opposite direction. Use the forward swap rate $F=2.65\%$ for the swap beginning at option expiry. The uncertain waiting period is $T=0.25$ years; the five-year swap length affects its payment annuity.

Here $PVA=\sum_i DF(0,t_i)$, so $A=AP\times PVA=0.5(8.9)=4.45$. Multiplying $N_0A$ by an annual rate difference converts it into the present value of all fixed-leg payment differences.

**1. Use option expiry, not swap tenor, in $d_1$**

$$
d_1=\frac{\ln(0.0265/0.0250)+(0.20^2/2)(0.25)}{0.20\sqrt{0.25}}
=\boxed{0.632689}
$$

$$
d_2=0.632689-0.20\sqrt{0.25}=\boxed{0.532689}
$$

$$
N(d_1)=0.736531649,\qquad N(d_2)=0.702875587
$$

**2. Value the payer swaption**

$$
PAYSWN=N_0(AP)(PVA)[R_{FIX}N(d_1)-R_XN(d_2)]
$$

$$
\begin{aligned}
PAYSWN&=10{,}000{,}000(0.5)(8.9)\\
&\quad\times\bigl[0.0265(0.736531649)\\
&\qquad-0.0250(0.702875587)\bigr]\\
&\approx\boxed{\$86{,}605.86}
\end{aligned}
$$

Normal symmetry gives $N(-d_2)=1-0.702875587=0.297124413$ and $N(-d_1)=1-0.736531649=0.263468351$. Both premiums use full-precision CDF values before rounding to cents.

**3. Value the receiver swaption**

$$
\begin{aligned}
RECSWN&=N_0(AP)(PVA)[R_XN(-d_2)-R_{FIX}N(-d_1)]\\
&=10{,}000{,}000(0.5)(8.9)\\
&\quad\times\bigl[0.0250(0.297124413)\\
&\qquad-0.0265(0.263468351)\bigr]\\
&\approx\boxed{\$19{,}855.86}
\end{aligned}
$$

**4. Check swaption parity**

$$
PAYSWN-RECSWN=N_0(AP)(PVA)(R_{FIX}-R_X)
$$

$$
=10{,}000{,}000(0.5)(8.9)(0.0015)=\boxed{\$66{,}750}
$$

> [!NOTE]
> Do not add another discount factor: $PVA$ already contains the payment-date discounting. Use the forward swap rate, not today’s spot swap rate.

---

## Variant: Approximate an Option Price Change with Delta

**Abstract:** *Delta is the option’s local speed: multiply it by a small underlying move to estimate the option’s value change.*

> A call is worth $7.80$ and has delta $0.42$. The matching European call and put are on a stock with no dividends. Estimate both new option values if the stock falls by $1.50$ and the put is currently worth $5.20$.

Delta is the change in option value for a USD 1 stock-price rise, holding other inputs fixed. Here $\Delta S=-1.50$ USD. The symbol $\Delta_c$ means call delta; $\Delta c$ means the call’s **price change**.

**1. Call change**

$$
\Delta c\approx\Delta_c\Delta S=0.42(-1.50)=\boxed{-0.63}
$$

$$
\widehat{c}=7.80-0.63=\boxed{7.17}
$$

**2. Get put delta from call delta**

For matching European options with no dividends, parity is $c-p=S-PV(X)$. A USD 1 stock rise changes the right side by USD 1, while the strike funding is unchanged. Therefore call delta minus put delta equals 1:

$$
\Delta_p=\Delta_c-1=0.42-1=\boxed{-0.58}
$$

**3. Put change**

$$
\Delta p\approx(-0.58)(-1.50)=\boxed{+0.87}
$$

$$
\widehat{p}=5.20+0.87=\boxed{6.07}
$$

> [!NOTE]
> Delta is reliable for small moves. A large move bends away from the straight-line estimate, which is exactly what gamma measures.

---

## Variant: Make an Option Position Delta Neutral

**Abstract:** *Add a hedge whose delta exactly cancels the portfolio delta; the sign tells you whether to buy or sell the hedge.*

> You are short puts on 10,000 shares. Each put has delta $-0.419$. Find a stock hedge. Then find a hedge using calls with delta $0.532$.

**1. Find the short-put position delta**

A long put has negative delta, so a short put has positive delta:

$$
\Delta_{portfolio}=10{,}000(+0.419)=\boxed{+4{,}190}
$$

**2. Hedge with stock**

Stock delta is $+1$ per share.

$$
N_H=-\frac{\Delta_{portfolio}}{\Delta_H}
=-\frac{4{,}190}{1}
=\boxed{-4{,}190\text{ shares}}
$$

The minus sign means short 4,190 shares.

**3. Hedge with calls**

$$
N_H=-\frac{4{,}190}{0.532}
=-7{,}875.94
$$

Round to the nearest whole option:

$$
\boxed{\text{Sell }7{,}876\text{ calls}}
$$

Check the exposure after hedging: stock hedge gives $4{,}190-4{,}190=0$. Selling 7,876 one-share calls gives $4{,}190-7{,}876(0.532)=-0.032$ share-equivalent delta, a tiny rounding residual. These are **alternative** hedges; do not apply both.

> [!NOTE]
> Position sign comes first. Shorting a negative-delta put creates positive delta; the hedge must carry negative delta.
> If one listed contract covers several underlying units, multiply option delta by that contract multiplier before sizing the hedge.

---

## Variant: Improve a Price Estimate with Delta Plus Gamma

**Abstract:** *Delta draws a straight tangent line; the gamma term adds the missing bend in the option-price curve.*

> A call is worth $8.00$, delta is $0.55$, gamma is $0.018$, and the stock rises by $6$. Estimate the new call value using delta only and then delta plus gamma.

Gamma is how much delta changes per USD 1 stock move. The second-order Taylor approximation adds $\tfrac12\Gamma(\Delta S)^2$ to the first-order delta estimate, holding time, volatility, and rates fixed. Both answers are estimates of today’s USD 8 call after the stock move.

**1. Delta-only estimate**

$$
\widehat{c}=c+\Delta_c(\Delta S)
$$

$$
\widehat{c}=8.00+0.55(6)=\boxed{11.30}
$$

**2. Add curvature**

$$
\widehat{c}=c+\Delta_c(\Delta S)+\frac{1}{2}\Gamma_c(\Delta S)^2
$$

$$
\widehat{c}=8.00+0.55(6)+\frac{1}{2}(0.018)(6^2)
$$

$$
=8.00+3.30+0.324=\boxed{11.624}
$$

The gamma correction is positive because a long option has positive gamma and the stock move is squared.

> [!NOTE]
> Do not forget the $\tfrac12$, and square only the stock-price change—not delta or gamma.

---

## Variant: Neutralize Gamma First and Delta Second

**Abstract:** *Stock can repair delta but has zero gamma, so use an option to repair gamma first and stock to clean up the remaining delta.*

> A portfolio has delta $+2,400$ and gamma $-600$. A traded call has delta $0.40$ and gamma $0.15$ per option. Make the portfolio gamma neutral and then delta neutral.

Let $N_C$ be calls bought (negative means sold) and $N_S$ shares bought. The two neutrality conditions are:

$$
-600+0.15N_C=0,\qquad 2{,}400+0.40N_C+N_S=0
$$

Stock gamma is zero, so solve the first equation for the option trade, then use that answer in the delta equation.

**1. Fix gamma with the call**

$$
N_C=-\frac{\Gamma_{portfolio}}{\Gamma_C}
=-\frac{-600}{0.15}
=\boxed{+4{,}000\text{ calls}}
$$

Buying calls adds positive gamma $4{,}000(0.15)=600$, exactly cancelling $-600$.

**2. Recalculate delta after the option hedge**

$$
\Delta_{new}=2{,}400+4{,}000(0.40)=\boxed{4{,}000}
$$

**3. Fix delta with stock**

$$
N_S=-\frac{4{,}000}{1}=\boxed{-4{,}000\text{ shares}}
$$

Shorting stock removes delta but adds no gamma, so both targets remain satisfied.

Check both targets: $\Gamma_{final}=-600+4{,}000(0.15)=0$ and $\Delta_{final}=2{,}400+4{,}000(0.40)-4{,}000=0$. Positions are in single-option units; divide by a listed contract’s multiplier if sizing contracts.

> [!NOTE]
> Order matters: option first for gamma, stock second for delta. Stock cannot alter gamma because its delta is always 1.

---

## Variant: Translate Theta, Vega, and Rho into Profit and Loss

**Abstract:** *Each Greek is a rate of change; multiply by the correctly measured input move and keep the position sign straight.*

> One long option has daily theta $-0.0327$, vega $0.4231$ per one percentage-point volatility change, and rho $0.3705$ per one percentage-point rate change. Estimate the separate effects of five calendar days, volatility rising from 24% to 27%, and the risk-free rate rising from 4.0% to 4.5%.

Each requested effect holds the other inputs fixed and is quoted per one long option unit. Theta measures the change as calendar time passes, vega the change per volatility percentage point, and rho the change per interest-rate percentage point. A short position reverses every sign; multiply by units and any contract multiplier for a total position.

**1. Theta: five days pass**

$$
\Delta V_{theta}\approx5(-0.0327)=\boxed{-0.1635}
$$

**2. Vega: volatility rises by $27-24=3$ percentage points**

$$
\Delta V_{vega}\approx3(0.4231)=\boxed{+1.2693}
$$

**3. Rho: the rate rises by $4.5-4.0=0.5$ percentage point**

$$
\Delta V_{rho}\approx0.5(0.3705)=\boxed{+0.1853}
$$

If all three changes are treated as independent first-order effects:

$$
\Delta V\approx-0.1635+1.2693+0.1853=\boxed{+1.2911}
$$

> [!NOTE]
> Confirm the vendor’s units: a move from 24% to 27% is 3 units when vega is quoted per percentage point.
> Theta is usually negative, but a deep-in-the-money European put near expiry can have positive theta.

---

## Variant: Infer Implied Volatility and Trade Relative Value

**Abstract:** *Implied volatility is the volatility input that makes the model equal the market price; a higher option price means a higher implied volatility, all else equal.*

> With every BSM input except volatility fixed, a put is worth USD 6.40 at 20% volatility and USD 7.49 at 24%. The market put price is USD 7.20. Bracket its implied volatility with a linear interpolation. Then decide what to do if your own fair-volatility forecast is 19% for an option quoted at 24% implied volatility.

The model price increases with volatility when the other inputs stay fixed. We therefore locate the market price between two known model prices, then use its fraction of that **price interval** as an approximate fraction of the volatility interval.

**1. Bracket the answer**

USD 7.20 lies between USD 6.40 and USD 7.49, so implied volatility lies between 20% and 24%.

**2. Interpolate**

The market price has covered this fraction of the model-price gap:

$$
\frac{7.20-6.40}{7.49-6.40}
=\frac{0.80}{1.09}
=0.7339
$$

The volatility interval is $24\%-20\%=4$ percentage points. Apply the same fraction to that interval:

$$
\sigma_{imp}\approx20\%+0.7339(4\%)
=\boxed{22.94\%}
$$

This is an approximation; an exact answer comes from numerically inverting the pricing model.

**3. Make the relative-value decision**

The market asks 24% implied volatility, but your fair estimate is 19%. You think the option is priced with too much volatility and is therefore expensive.

$$
\boxed{\text{Sell the option, subject to hedge and risk limits.}}
$$

The opposite rule also holds: if your fair volatility is above quoted implied volatility, you see the option as cheap and would buy it.

> [!NOTE]
> Historical volatility looks backward. Implied volatility is backed out from today’s option price and is the market’s common comparison unit across strikes and maturities.

<!-- Revision audit (2026-11-03): All 27 variants reviewed for missing inputs, substitutions, rollback steps, signs, units, timing, and rounding. Dividend-tree reconstruction checked against official Exhibit 10, printed p. 101; coupon-bond waiting values remain explicitly supplied inputs. BSM CDF and rate-tree precision corrected. Source audit: Primary source is CFA Level II Derivatives, Learning Module 2, printed pages 81-155, including Examples 1-21 and end-of-module practice and solutions. Schweser Reading 29, Modules 29.1-29.7, was used only as a secondary exam-shape and edge-case cross-check. All published answers used here were independently recomputed; newly parameterized problems instantiate the official equations without adding new doctrine. -->
