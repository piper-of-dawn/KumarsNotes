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

**5. Check with a single terminal expectation**

A European option can also be valued directly from its expiry payoffs. The terminal weights are $\pi^2$, $2\pi(1-\pi)$, and $(1-\pi)^2$; the factor of 2 counts the two paths reaching the middle node.

$$
\begin{aligned}
c_0&=\frac{\pi^2c^{++}+2\pi(1-\pi)c^{+-}+(1-\pi)^2c^{--}}{(1+r)^2}\\
&=\frac{0.45^2(7.34698375)+2(0.45)(0.55)(0)+0.55^2(0)}{1.0435^2}\\
&=\boxed{1.3663}
\end{aligned}
$$

This reproduces rollback. For an American option with possible early exercise, use node-by-node exercise decisions instead.

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

## Variant: Finance a Binomial Replication and Rebalance Without Adding Cash

**Abstract:** *Match the next-node option values with shares plus a loan. After a move, let the old loan accrue and finance the change in shares through the new loan.*

> Use official CFA Example 7: $S_0=7.35$, $X=8$, $u=1.445$, $d=0.715$, per-period $r=4.35\%$, two periods, and risk-neutral up weight $\pi=0.45$. The European call values are $c_1^+=3.168320736$, $c_1^-=0$, and $c_0=1.366309852$. Find today’s shares and borrowing, then the trades after an up move. Show that no extra cash is needed.

<span class="jargon-unlock">**Self-financing. What does it mean?** Rebalancing uses the portfolio’s own cash and borrowing, with no new money injected. **Hedge ratio. What is it?** Shares per option, $h=(V_u-V_d)/(S_u-S_d)$, where $V$ denotes next-node option value and $S$ next-node stock price. A positive loan amount $L$ is a liability, so portfolio value is $hS-L$.</span>

**1. Build today’s share and loan positions**

The Time-1 stock prices are $S_1^+=7.35(1.445)=10.62075$ and $S_1^-=7.35(0.715)=5.25525$.

$$
\begin{aligned}
h_0&=\frac{3.168320736-0}{10.62075-5.25525}\\
&=\boxed{0.590498693\text{ shares}}\\
L_0&=h_0S_0-c_0\\
&=0.590498693(7.35)-1.366309852\\
&=\boxed{2.973855539}
\end{aligned}
$$

Borrowing reduces the net purchase cost to $\boxed{1.366309852}$, matching the call value.

**2. Recalculate after the up move**

The two next stock prices are $10.62075(1.445)=15.34698375$ and $10.62075(0.715)=7.59383625$. Their call payoffs are $7.34698375$ and zero.

$$
\begin{aligned}
h_1^+&=\frac{7.34698375-0}{15.34698375-7.59383625}\\
&=\boxed{0.947613050\text{ shares}}\\
L_1^+&=h_1^+(10.62075)-3.168320736\\
&=\boxed{6.896040566}
\end{aligned}
$$

**3. Pay for the added shares using additional borrowing**

The old loan has grown to $L_0(1.0435)=3.103218255$. Buy the difference between the new and old share counts:

$$
\begin{aligned}
\text{Extra share cost}&=(h_1^+-h_0)(10.62075)\\
&=\boxed{3.792822311}\\
\text{Additional borrowing}&=L_1^+-L_0(1.0435)\\
&=6.896040566-3.103218255\\
&=\boxed{3.792822311}
\end{aligned}
$$

The cash required and cash raised match. At the middle expiry node, $0.947613050(7.59383625)-6.896040566(1.0435)\approx\boxed{0}$, matching the call’s zero payoff there.

> [!NOTE]
> Rebalancing changes both the shares and the financing. Comparing the new loan with the old principal ignores accrued interest and breaks the self-financing check.

<!-- Official source: LM2 printed pp.93–95, self-financing discussion, and Example 7 pp.103–105, stock-plus-financing interpretation. -->

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

## Variant: Recalculate the Hedge Ratio After American Early Exercise

**Abstract:** *An American exercise decision changes the next-node option values. Use those chosen values to calculate today’s hedge ratio; the European hedge is no longer the right input.*

> In official CFA Example 7, $S_0=7.35$, $X=8$, $u=1.445$, $d=0.715$, per-period $r=4.35\%$, and $\pi=0.45$. At Time 1, $S^+=10.62075$ and $S^-=5.25525$. European put continuation values are $p^+=0.214077683$ and $p^-=2.411256948$. Find the American put value and today’s American and European hedge ratios.

<span class="jargon-unlock">**Continuation value. What is it?** The value of waiting rather than exercising now. **American option. What is it?** An option permitting exercise before expiry, so each node uses the larger of continuation and exercise. **Hedge ratio. What is it?** Shares per option: the difference between the next-node option values divided by the difference between their stock prices.</span>

**1. Choose the Time-1 American values**

At the up node, immediate exercise pays $\max(8-10.62075,0)=0$, so retain continuation $0.214077683$. At the down node:

$$
\begin{aligned}
E^-&=\max(8-5.25525,0)=2.74475\\
p_A^-&=\max(2.411256948,2.74475)\\
&=\boxed{2.74475}
\end{aligned}
$$

**2. Recalculate today’s hedge from the chosen values**

The stock-price denominator stays the same; the put-value numerator changes:

$$
\begin{aligned}
h_{E,0}&=\frac{0.214077683-2.411256948}{10.62075-5.25525}\\
&=\boxed{-0.409501307}\\
h_{A,0}&=\frac{0.214077683-2.74475}{10.62075-5.25525}\\
&=\boxed{-0.471656382}
\end{aligned}
$$

The American put requires a larger short-stock position: about 0.471656 shares per option rather than 0.409501.

**3. Roll back and test exercise today**

$$
\begin{aligned}
C_{A,0}&=\frac{0.45(0.214077683)+0.55(2.74475)}{1.0435}\\
&=1.539000918\\
p_{A,0}&=\max(8-7.35,C_{A,0})\\
&=\boxed{1.5390}
\end{aligned}
$$

Today’s exercise value is only $0.65$, so holding is optimal. The European value is $[0.45(0.214077683)+0.55(2.411256948)]/1.0435=1.363225950$, giving an early-exercise premium of $\boxed{0.175775}$ per option.

> [!NOTE]
> Decide exercise first, then calculate earlier hedge ratios. At a node where exercise is chosen, the option terminates; a hedge for continued holding is no longer needed there.

<!-- Official source: LM2 Example 7(3), printed pp.105–106. Full precision resolves the source's rounded 1.54 and -0.4717. -->

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

The call’s initial share cost is $100(0.624252)=62.4252$; the borrowing leg is $100e^{-0.05}(0.506649)\approx48.1939$. Their difference is USD 14.23. The put’s lending leg is $100e^{-0.05}(0.493351)\approx46.9290$ and its short-share proceeds are $100(0.375748)=37.5748$, leaving a net cost of USD 9.35.

Each zero-coupon bond here pays **USD 100 at expiry**. These positions describe the initial replication; share and financing quantities must be rebalanced as inputs change.

> [!NOTE]
> BSM uses continuous compounding. If given a discrete annual rate $r_d$, convert with $r=\ln(1+r_d)$.

---

## Variant: Count the Shares and Bonds That Replicate a BSM Call

**Abstract:** *Read BSM as quantity times price: $N(d_1)$ shares minus $N(d_2)$ strike-paying bonds. Distinguish the number of bonds from the dollars borrowed.*

> Use the official CFA Example 10 inputs: a non-dividend-paying stock has $S=100$, strike $X=100$, continuous annual risk-free rate $r=5\%$, expiry $T=1$ year, and volatility $\sigma=30\%$. The full-precision model gives $N(d_1)=0.624251728$ and $N(d_2)=0.506648730$. Find the initial shares and bonds for one long call and for 20 contracts covering 100 shares each. Each bond pays USD 100 at option expiry. What if each bond instead pays USD 1,000?

<span class="jargon-unlock">**Replicating portfolio. What is it?** A stock-and-financing strategy that reproduces an option when continually rebalanced. **Zero-coupon bond. What is it?** A risk-free security paying one stated face amount at expiry, with no interim interest payments. Its price is $B=Xe^{-rT}$ when its face equals strike $X$; $S$ is the price per share and $n_S,n_B$ are signed share and bond counts.</span>

**1. Make the quantities visible in Black–Scholes**

Compare the general portfolio cost with the call formula:

$$
\begin{aligned}
c&=n_SS+n_BB\\
c&=N(d_1)S-N(d_2)B\\
n_S&=\boxed{+0.624251728\text{ shares}}\\
n_B&=\boxed{-0.506648730\text{ bonds}}
\end{aligned}
$$

Positive means buy; negative means short. Buying stock provides the upward exposure. Shorting bonds raises cash now and creates a future repayment, so it is borrowing.

**2. Price the financing and check the net cost**

One bond costs $B=100e^{-0.05}=95.122942$. Therefore:

$$
\begin{aligned}
\text{Share cost}&=0.624251728(100)=62.425173\\
\text{Cash borrowed}&=0.506648730(95.122942)\\
&=\boxed{48.193918}\\
c&=62.425173-48.193918\\
&\approx\boxed{\text{USD }14.23}
\end{aligned}
$$

**3. Scale quantities before rounding**

There are $20(100)=2{,}000$ one-share option units:

$$
\begin{aligned}
n_S^{total}&=2{,}000(0.624251728)\\
&=\boxed{+1{,}248.503456\text{ shares}}\\
n_B^{total}&=-2{,}000(0.506648730)\\
&=\boxed{-1{,}013.297460\text{ bonds}}
\end{aligned}
$$

Borrow USD $96{,}387.84$ against the stock purchase; the net portfolio costs USD $28{,}462.51$, using unrounded inputs. With USD 1,000-face bonds, each bond is ten times larger, so short $1{,}013.297460/10=\boxed{101.329746}$ bonds. The financing dollars stay the same.

> [!NOTE]
> $N(d_1)$ gives share quantity; $N(d_2)$ gives bond quantity only when each bond pays $X$. These are initial holdings, not a portfolio to leave untouched until expiry.

<!-- Official source: LM2 printed pp.114–116, Exhibit 14 and Example 10(1); contract scaling and alternate face instantiate the same portfolio identity. -->

---

## Variant: Count the Shares and Bonds That Replicate a BSM Put

**Abstract:** *A long put is short stock plus lending. Take the complementary normal probabilities, apply the signs, and verify that the bond purchase exceeds the short-sale proceeds.*

> A non-dividend-paying stock has $S=100$, $X=100$, continuous annual $r=5\%$, $T=1$ year, and $\sigma=30\%$. As in official CFA Example 10, use $N(d_1)=0.624251728$ and $N(d_2)=0.506648730$. Each zero-coupon bond pays USD 100 at expiry. Find the initial replication for one long put and for 15 contracts covering 100 shares each. State the portfolio replicating a short put.

<span class="jargon-unlock">**Short stock. What does that mean?** Sell borrowed shares now and later buy shares to return them. **Lending. What is it here?** Buy a risk-free zero-coupon bond that pays a fixed face amount at expiry. $B=Xe^{-rT}$ is its price today; $n_S,n_B$ are signed share and bond counts, and $N(z)$ is a standard normal cumulative probability with $N(-z)=1-N(z)$.</span>

**1. Find the two complementary probabilities**

The put uses the opposite side of the normal distribution:

$$
\begin{aligned}
N(-d_1)&=1-0.624251728=0.375748272\\
N(-d_2)&=1-0.506648730=0.493351270
\end{aligned}
$$

**2. Read the share and bond counts from BSM**

Reorder the put formula into the same stock-plus-bond form:

$$
\begin{aligned}
p&=N(-d_2)B-N(-d_1)S\\
&=n_SS+n_BB\\
n_S&=\boxed{-0.375748272\text{ shares}}\\
n_B&=\boxed{+0.493351270\text{ bonds}}
\end{aligned}
$$

The short share position gains when stock falls; the bonds fund the cash needed to reproduce the put.

**3. Reconcile the money, not just the counts**

With $B=100e^{-0.05}=95.122942$:

$$
\begin{aligned}
\text{Short-sale proceeds}&=0.375748272(100)\\
&=37.574827\\
\text{Bond purchase}&=0.493351270(95.122942)\\
&=46.929024\\
p&=46.929024-37.574827\\
&\approx\boxed{\text{USD }9.35}
\end{aligned}
$$

**4. Scale and reverse positions**

For $15(100)=1{,}500$ option units, short $\boxed{563.622408}$ shares and buy $\boxed{740.026905}$ bonds. The net initial cost is $\boxed{\text{USD }14{,}031.30}$ using full precision. To replicate a **short** put, reverse both positions: buy those shares and short those bonds, receiving the same net amount initially.

> [!NOTE]
> Long put: $n_S=-N(-d_1)$ and $n_B=+N(-d_2)$. The official solution on p.155 has a bond-sign typo; p.114 and its actual numerical substitution use the positive complementary probability.

<!-- Official source: LM2 printed pp.114–116, Example 10(2); practice 11, solution p.155. The solution's n_B=-N(d_2)>0 is a typo, not a usable identity. -->

---

## Variant: Separate BSM Exercise Probability from Expected Payoff

**Abstract:** *$N(d_2)$ answers whether a call finishes in the money under risk-neutral pricing; expected payoff also needs the size of the gain. Discount that expected payoff to obtain today’s price.*

> For official CFA Example 10, take $S=X=100$, continuous annual $r=5\%$, $T=1$, $\sigma=30\%$, $N(d_1)=0.624251728$, and $N(d_2)=0.506648730$. Find the risk-neutral probabilities that the call and put finish in the money, their expected expiry payoffs, and their values today.

<span class="jargon-unlock">**In the money. What does that mean?** The call has a positive expiry payoff when $S_T>X$; the put does when $S_T<X$. **Risk-neutral expectation. What is it?** A pricing average, written $E^Q$, using the no-arbitrage probability measure $Q$ rather than a real-world forecast. $S_T$ is the stock price at expiry; $e^{-rT}$ discounts expiry cash to today.</span>

**1. Read the exercise probabilities**

The official BSM interpretation is:

$$
\begin{aligned}
Q(S_T>X)&=N(d_2)=\boxed{50.664873\%}\\
Q(S_T<X)&=1-N(d_2)=\boxed{49.335127\%}
\end{aligned}
$$

These sum to 100%. With positive volatility the continuous price distribution gives zero probability to exactly $S_T=X$.

**2. Calculate expected payoff, including payoff size**

BSM can be written as discounted expected payoff. Moving the discount factor outside gives the following expiry cash averages:

$$
\begin{aligned}
E^Q[c_T]&=Se^{rT}N(d_1)-XN(d_2)\\
&=100e^{0.05}(0.624251728)\\
&\quad-100(0.506648730)\\
&=\boxed{\text{USD }14.960907}
\end{aligned}
$$

For the put, use both complementary probabilities:

$$
\begin{aligned}
E^Q[p_T]&=XN(-d_2)-Se^{rT}N(-d_1)\\
&=100(0.493351270)\\
&\quad-100e^{0.05}(0.375748272)\\
&=\boxed{\text{USD }9.833797}
\end{aligned}
$$

**3. Discount once to today**

$$
\begin{aligned}
c&=e^{-0.05}(14.960907)\approx\boxed{14.23}\\
p&=e^{-0.05}(9.833797)\approx\boxed{9.35}
\end{aligned}
$$

Both are USD per one-share option. The probability is dimensionless; payoff and price are dollars at different dates.

> [!NOTE]
> $N(d_1)$ is the base-model share coefficient; $N(d_2)$ is the risk-neutral call exercise probability. Neither is a forecast of the actual stock return or the option payoff amount.

<!-- Official source: LM2 printed pp.113–116, expected-payoff interpretation, Example 10 and risk-neutral exercise-probability discussion. -->

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

## Variant: Replicate Dividend-Paying Options with Shares and Bonds

**Abstract:** *A dividend yield changes the share coefficient to $e^{-\delta T}N(d_1)$ for calls and $-e^{-\delta T}N(-d_1)$ for puts. The bond coefficients keep their usual form.*

> Use official CFA Example 11: $S=X=60$, continuous annual $r=\delta=2\%$, $T=0.5$ year, and $\sigma=45\%$. The model gives $N(d_1)=0.563204572$ and $N(d_2)=0.436795428$. Find the initial stock and bond positions for one long call and one long put, then scale each to 1,000 one-share option units. Each bond pays USD 60 at expiry.

<span class="jargon-unlock">**Dividend yield. What is it?** The annual dividend income relative to stock value, modeled continuously as $\delta$. **Share coefficient. What is it?** The number of actual shares initially held per option, $n_S$. **Bond coefficient. What is it?** The signed count $n_B$ of bonds priced at $B=Xe^{-rT}$; negative means borrowing by shorting bonds.</span>

**1. Include the dividend factor in the stock quantity**

The common yield adjustment is $e^{-\delta T}=e^{-0.02(0.5)}=0.990049834$. A shareholder receives dividends; a call holder does not. The replicating share holding must reflect that difference.

$$
\begin{aligned}
n_{S,c}&=e^{-\delta T}N(d_1)\\
&=0.990049834(0.563204572)\\
&=\boxed{+0.557600593}\\
n_{B,c}&=-N(d_2)=\boxed{-0.436795428}
\end{aligned}
$$

For the put, use the complementary probabilities and reverse the stock sign:

$$
\begin{aligned}
n_{S,p}&=-e^{-\delta T}[1-N(d_1)]\\
&=-0.990049834(0.436795428)\\
&=\boxed{-0.432449241}\\
n_{B,p}&=1-N(d_2)=\boxed{+0.563204572}
\end{aligned}
$$

**2. Check both portfolio costs**

Each bond costs $B=60e^{-0.02(0.5)}=59.402990$. Use unrounded holdings:

$$
\begin{aligned}
c&=0.557600593(60)\\
&\quad-0.436795428(59.402990)\\
&=33.456036-25.946954=\boxed{7.5091}\\
p&=-0.432449241(60)\\
&\quad+0.563204572(59.402990)\\
&=-25.946954+33.456036=\boxed{7.5091}
\end{aligned}
$$

For 1,000 calls, buy $\boxed{557.600593}$ shares and short $\boxed{436.795428}$ bonds. For 1,000 puts, short $\boxed{432.449241}$ shares and buy $\boxed{563.204572}$ bonds. Each portfolio initially costs USD $\boxed{7{,}509.08}$.

> [!NOTE]
> $N(d_1)$ alone is not the share count when dividends are present. Include $e^{-\delta T}$ and account for dividend receipts or payments as the strategy is rebalanced.

<!-- Official source: LM2 printed pp.116–118, eqs.12–14, replication discussion p.117 and Example 11. -->

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

The discounted futures parity check is $c-p=e^{-rT}(F_0-X)$. At contract scale:

$$
\begin{aligned}
250(c-p)&=250e^{-0.002(0.25)}(1851.65-1860)\\
&=\boxed{-\text{USD }2{,}086.46}
\end{aligned}
$$

The put exceeds the call by this amount, matching the two unrounded contract premiums.

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

## Variant: Add Caplets into a Cap and Reconcile the Matching Floor with a Swap

**Abstract:** *A cap is the sum of its caplets; a floor is the sum of its floorlets. Apply call-minus-put parity to each payment, then sum to get the equivalent swap value.*

> A two-payment rate contract has notional USD 10 million, accrual fraction $AP=0.25$ per payment, and common strike $K=3.5\%$. Forward rates are $F_1=3\%$ and $F_2=4\%$; today’s discount factors to their payment dates are $DF_1=0.98$ and $DF_2=0.96$. The matching caplets cost USD 5,000 and USD 17,000. Find both floorlet prices, total cap and floor prices, long-cap/short-floor value, and the common strike that would make cap and floor values equal.

<span class="jargon-unlock">**Caplet and floorlet. What are they?** A call and put on one future interest payment. A cap or floor is a strip covering several payments. **Parity. What is it?** Matching call-minus-put payoffs equal the underlying rate difference: $c_i-p_i=N_0AP\,DF_i(F_i-K)$, where $N_0$ is notional and $i$ identifies the payment.</span>

**1. Find each floorlet from its caplet**

At payment, $\max(L_i-K,0)-\max(K-L_i,0)=L_i-K$ for the observed rate $L_i$. Discounted forward-rate differences therefore give:

$$
\begin{aligned}
c_1-p_1&=10{,}000{,}000(0.25)(0.98)(0.03-0.035)\\
&=\boxed{-12{,}250}\\
p_1&=5{,}000-(-12{,}250)=\boxed{17{,}250}\\
c_2-p_2&=10{,}000{,}000(0.25)(0.96)(0.04-0.035)\\
&=\boxed{12{,}000}\\
p_2&=17{,}000-12{,}000=\boxed{5{,}000}
\end{aligned}
$$

**2. Sum the strips and interpret the sign**

$$
\begin{aligned}
\text{Cap}&=5{,}000+17{,}000=\boxed{22{,}000}\\
\text{Floor}&=17{,}250+5{,}000=\boxed{22{,}250}\\
\text{Cap}-\text{Floor}&=\boxed{-250}
\end{aligned}
$$

All amounts are USD today. Long cap plus short floor receives floating and pays fixed at 3.5% on these two payments; that swap exposure is worth negative USD 250.

**3. Solve for the strike giving zero swap value**

Set the sum of discounted rate differences to zero. With equal notional and accrual fractions, they cancel:

$$
\begin{aligned}
0&=DF_1(F_1-K^*)+DF_2(F_2-K^*)\\
K^*&=\frac{0.98(0.03)+0.96(0.04)}{0.98+0.96}\\
&=\boxed{3.494845\%}
\end{aligned}
$$

At this at-market swap strike, the **repriced** cap and floor have equal values. Their individual premiums must be recalculated; the original 22,000 and 22,250 do not carry over to a new strike.

> [!NOTE]
> Equal cap and floor strikes alone do not guarantee equal prices. Equality requires the common strike to equal the matching swap rate, with identical payment dates and other terms.

<!-- Official source: LM2 printed pp.124–125, cap/floor strips and FRA/swap equivalences; original inputs instantiate the official relationship. -->

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

## Variant: Value a Callable Bond Using the Receiver-Swaption Equivalence

**Abstract:** *A callable bond investor owns the straight bond and has sold the issuer an exercise right. Subtract the matched receiver-swaption value; reversing the calculation adds it back.*

> A straight fixed-rate bond position is worth USD 10,200,000. A matched receiver swaption representing its issuer’s call right is worth USD 19,855.86. Under the callable-bond decomposition in the official CFA reading, value the callable bond position. How much must the investor pay to buy the matched receiver swaption and recover straight-bond exposure?

<span class="jargon-unlock">**Callable bond. What is it?** A bond its issuer can redeem early under the contract’s terms. **Straight bond. What is it?** The same promised debt cash flows without the call right. **Receiver swaption. What is it?** The right to enter a swap receiving fixed and paying floating; it benefits from lower rates, like the issuer’s call right. Here the exercise dates, cash flows, and other terms are assumed matched for the stated decomposition.</span>

**1. Identify who owns the valuable right**

The issuer can call when falling rates make refinancing attractive. The investor has given away that right, so its value reduces the price the investor receives for the bond.

$$
\begin{aligned}
V_{callable}&=V_{straight}-V_{receiver}\\
&=10{,}200{,}000-19{,}855.86\\
&=\boxed{\text{USD }10{,}180{,}144.14}
\end{aligned}
$$

**2. Buy back the exercise exposure**

Buying the matched receiver swaption offsets the embedded short option:

$$
\begin{aligned}
V_{callable}+V_{receiver}&=V_{straight}\\
10{,}180{,}144.14+19{,}855.86&=\boxed{10{,}200{,}000}
\end{aligned}
$$

The investor pays $\boxed{\text{USD }19{,}855.86}$ for that offsetting option. The callable bond is cheaper than the straight bond by exactly the value of the call right in this matched setup.

> [!NOTE]
> Use the receiver direction for this decomposition. A generic swaption with different exercise rights or cash flows is not automatically an exact hedge for a callable bond.

<!-- Official source: LM2 printed p.127, callable fixed-rate bond/receiver-swaption equivalence; original price inputs illustrate the stated decomposition. -->

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

## Variant: Hedge an Existing Stock Holding with Calls or Puts and Compare Gamma

**Abstract:** *A long stock holding has positive delta. Short calls or long puts can cancel it, but the first adds negative gamma and the second positive gamma.*

> Use the official practice vignette’s 10,000-share ETF holding. Each share has delta 1 and gamma 0. Matching options have call delta $+0.6232$, put delta $-0.3689$, and gamma $+0.0139$ per one-share option unit. Find alternative delta-neutral hedges using calls and puts, then calculate the gamma of each combined portfolio. Assume fractional option units for exact sizing; report whole-unit trades too.

<span class="jargon-unlock">**Delta. What is it?** The local value change for a USD 1 underlying-price move. **Gamma. What is it?** How much delta changes for that move. **ETF. What is it?** An exchange-traded fund; here its shares are the underlying. A negative option count means sell, and reverses both that option’s delta and gamma.</span>

**1. Cancel the original stock delta**

The holding has $\Delta_P=10{,}000(1)=+10{,}000$. If $n_H$ is the number of hedge options, neutrality requires $\Delta_P+n_H\Delta_H=0$:

$$
\begin{aligned}
n_C&=-\frac{10{,}000}{0.6232}\\
&=\boxed{-16{,}046.213094\text{ calls}}\\
n_P&=-\frac{10{,}000}{-0.3689}\\
&=\boxed{+27{,}107.617240\text{ puts}}
\end{aligned}
$$

Thus sell approximately $\boxed{16{,}046}$ calls **or** buy approximately $\boxed{27{,}108}$ puts. These are alternative hedges, and whole-unit rounding leaves a small residual delta.

**2. Compare the resulting gamma**

Stock contributes no gamma. Using the exact fractional option counts:

$$
\begin{aligned}
\Gamma_{stock+short\ calls}&=0-16{,}046.213094(0.0139)\\
&=\boxed{-223.042362}\\
\Gamma_{stock+long\ puts}&=0+27{,}107.617240(0.0139)\\
&=\boxed{+376.795880}
\end{aligned}
$$

Both portfolios have zero current delta. For a small stock move, their second-order value changes are approximately $\tfrac12\Gamma(\Delta S)^2$: the call hedge has negative curvature; the put hedge has positive curvature. Option premiums and subsequent hedge changes still matter.

> [!NOTE]
> Delta-neutral does not mean gamma-neutral. These counts are one-share option units; for contracts covering 100 shares, divide the counts by 100 before contract rounding.

<!-- Official source: LM2 practice Exhibit 2 and problems 16–17, printed pp.149–151; solutions p.155. Quantifies the source's gamma comparison without adding a new hedge rule. -->

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

---

## Variant: Estimate Implied Volatility from a Price Gap and Vega

**Abstract:** *Vega translates a small price gap into a volatility change: divide price difference by vega, then add that change to the volatility used by the model.*

> In the official CFA practice vignette, a put’s model price is 7.4890 using 24% volatility, its market price is 7.20, and vega is 0.4231 per one volatility percentage point. Estimate implied volatility with one local vega step. Explain whether the exact implied volatility must be above or below 24%.

<span class="jargon-unlock">**Implied volatility. What is it?** The volatility input that makes the model price equal the observed market price. **Vega. What is it?** The local option-price change per volatility change; here one vega unit means a full percentage point, such as 24% to 25%. Other model inputs stay fixed.</span>

**1. Find the price correction needed**

The model needs to fall to the market price:

$$
\Delta V=V_{market}-V_{model}=7.20-7.4890=\boxed{-0.2890}
$$

**2. Invert the local vega relationship**

The approximation is $\Delta V\approx Vega\times\Delta\sigma_{pp}$, where $\Delta\sigma_{pp}$ is measured in percentage points:

$$
\begin{aligned}
\Delta\sigma_{pp}&\approx\frac{-0.2890}{0.4231}\\
&=\boxed{-0.683054\text{ percentage points}}\\
\sigma_{imp}&\approx24\%-0.683054\%\\
&=\boxed{23.316946\%}
\end{aligned}
$$

The option’s exact implied volatility is below 24% because a lower model price requires lower volatility. Its precise value requires solving the pricing equation; one vega step estimates it because vega changes as volatility changes.

> [!NOTE]
> Divide by vega quoted in matching units. The result is a percentage-point change, not a decimal change to add directly to 0.24.

<!-- Official source: LM2 vega pp.136–137 and implied volatility pp.138–144; practice Exhibit 2 p.149 and problem 14, solution p.155. The numerical inversion is explicitly a local approximation to the source's sensitivity relation. -->

<!-- Official-source extension audit (2026-11-04): 10 focused variants added. Scope inventoried: 14 LOS, equations 1–23, Examples 1–21, and practice problems 1–17 in LM2 printed pp.81–155. New coverage: explicit BSM call/put counts, contract/face scaling, dividend replication, RN probabilities/expected payoff, binomial self-financing, American hedge adjustment, stock-holding option hedges and gamma, cap/floor strips and swap-strike inversion, callable-bond decomposition, and local vega inversion. Existing coupon-bond comparison is a supplied-input supplementary question, not an official-source coverage item. Official p.155 put bond-sign typo resolved using p.114. Revision audit (2026-11-03): All 27 variants reviewed for missing inputs, substitutions, rollback steps, signs, units, timing, and rounding. Dividend-tree reconstruction checked against official Exhibit 10, printed p. 101; coupon-bond waiting values remain explicitly supplied inputs. BSM CDF and rate-tree precision corrected. Source audit: Primary source is CFA Level II Derivatives, Learning Module 2, printed pages 81-155, including Examples 1-21 and end-of-module practice and solutions. Schweser Reading 29, Modules 29.1-29.7, was used only as a secondary exam-shape and edge-case cross-check. All published answers used here were independently recomputed; newly parameterized problems instantiate the official equations without adding new doctrine. -->

<!--
Official-source coverage audit — 2026-11-04

Authority: CFA L2 B7 DERIVATIVES.pdf, LM2, printed pp. 81–155 (PDF pp. 87–161). All 14 learning outcomes, numbered equations (1)–(23), 21 worked examples, and 17 practice problems inventoried. Existing secondary-source coupon-bond question is retained as a supplied-node comparison, not counted as official-source coverage. New inputs instantiate official formulas; none imply additional syllabus rules. Full coverage here means distinct numerical methods, not every possible parameter rearrangement.

| Source | Numerical skill / direct or inverse form | Coverage and action | Trap |
|---|---|---|---|
| LOS 1–4; pp. 83–106; eqs. 1–9 | Payoffs, hedge ratios, financing, risk-neutral weights, arbitrage, European/American rollback | Existing variants 1–12; add self-financing rebalance and American hedge ratio; add terminal-expectation cross-check to European tree | Next-date values, borrowing signs, two paths to middle node, American exercise before hedge calculation |
| LOS 5; pp. 107–109; Example 8 | Node-specific discounting and notional scaling for rate options | Existing rate-tree variant | Rate percentage vs decimal; factor multiplication; stated cash-settlement timing |
| LOS 6; pp. 109–112; Example 9 | BSM assumptions | Conceptual; no separate numerical question needed | Continuous rebalancing, no dividends for base model, constant rates/volatility |
| LOS 7; pp. 112–116; eqs. 10–11; Exhibit 14; Example 10 | BSM prices, explicit share/bond counts, expected payoff and risk-neutral exercise probability | Existing combined valuation; add separate call and put counts plus probability/expected payoff variant | d versus N(d); counts versus USD financing; bond face; dynamic replication |
| LOS 8; pp. 116–120; eqs. 12–14; Examples 11–13 | Carry-adjusted equity/FX prices, parity, replication | Existing carry and FX pricing; add dividend-adjusted counts and position scaling | exp(-yield*T) in share count; foreign rate is carry; quote units |
| LOS 9; pp. 120–122; eqs. 15–17; Example 14 | Black futures valuation and parity | Existing futures pricing; add explicit discounted parity check | Futures price versus spot; discount whole payoff; multiplier |
| LOS 10; pp. 122–128; eqs. 18–21; Examples 15–16 | Deferred rate options, cap/floor strips and swaps, swaptions, callable-bond equivalence | Existing rate, caplet parity and swaption variants; add cap/floor strip and callable bond numerical | Expiry vs payment; accrual once; full payment-date annuity; equal cap/floor only at swap strike |
| LOS 11–13; pp. 129–138; eqs. 22–23; Examples 17–19 | Greeks, delta/gamma approximations, hedge sizing and rebalancing | Existing six Greeks variants; add stock holding hedged by calls or puts with gamma comparison | Short signs; one-share units vs contracts; stock gamma zero; delta neutrality local |
| LOS 14; pp. 138–144; Examples 20–21 | Implied-volatility comparisons and inference | Existing interpolation/relative value; add local vega inversion using practice Exhibit 2 | IV inferred, not historical; percentage-point units; inversion approximate |

| Worked examples | Distinct method | Coverage |
|---|---|---|
| 1–2, pp. 88–89 | Long-call and long-put replication in binomial model | Existing one-period call and put |
| 3–4, pp. 91–92 | Hedge ratio, price, one-period parity | Existing one-period call/put and parity |
| 5, p. 96 | Two-period risk-neutral valuation | Existing European call and put; terminal-expectation check added |
| 6, p. 99 | American put | Existing exercise comparison |
| 7, pp. 101–106 | European/American tree, hedge ratios, node financing | Existing tree/node hedges; new rebalance and American hedge variants |
| 8, pp. 107–109 | Rate-option tree | Existing rate tree |
| 9, p. 112 | Model assumptions | Conceptual exclusion |
| 10, pp. 115–116 | BSM long-call and long-put share/bond counts | New separate count questions plus existing valuation |
| 11–12, pp. 117–119 | Dividend equity valuation | Existing dividend value; new dividend replication |
| 13, pp. 119–120 | Currency mapping | Existing currency variant |
| 14, pp. 121–122 | Black futures | Existing futures variant and added parity |
| 15, p. 125 | FRA underlying and timing | Existing deferred rate option |
| 16, p. 128 | Payer swaption mapping | Existing swaption variant |
| 17–18, pp. 130–132 | Delta hedge | Existing short-put hedge; new stock-holding hedge |
| 19, p. 134 | Gamma sign in delta-hedged portfolio | Existing gamma hedge; new stock hedge with gamma comparison |
| 20–21, p. 141 | Relative value via IV | Existing implied-volatility variant |

| Practice problems | Coverage |
|---|---|
| 1–4, pp. 147–148 | Existing one-period hedge, probability, price, and arbitrage |
| 5–6, p. 148 | Existing European/American rollback |
| 7, p. 148 | New explicit terminal expectation check (European only) |
| 8–9, p. 148 | Existing rate tree; unchanged risk-neutral weights when strike changes |
| 10–11, p. 150; solutions pp. 154–155 | New explicit BSM share/bond counts; put sign typo checked against p.114 |
| 12, p. 150 | Existing Black futures input mapping |
| 13, p. 150 | Existing theta calculation |
| 14, p. 151 | Existing model/market-IV comparison; new vega inversion |
| 15, p. 151 | Existing FRA vs current spot rate and expiry/payment timing |
| 16–17, p. 151 | New existing-stock delta hedges and gamma comparison |

Source discrepancy: solution 11, printed p.155, writes n_B=-N(d2)>0 for a long put. This is a sign/complement typo: p.114 gives n_B=N(-d2)>0, and solution 11 itself uses +0.4404. Use the p.114 formula. No separate errata file was supplied; do not claim publisher errata verification.
-->
