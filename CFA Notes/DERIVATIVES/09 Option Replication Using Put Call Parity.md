### MODULE 9: OPTION REPLICATION USING PUT-CALL PARITY
###### LOS 9.a: Explain put-call parity for European options.
###### LOS 9.b: Explain put-call forward parity for European options.

> [!tip] LOOK AT THESE BEFORE EXAM
> - Put-call parity links a European call, a European put, the underlying asset, and a risk-free bond under no-arbitrage.
> - **Protective put = fiduciary call.** That identity is the spine of the whole reading.
> - **Put-call parity:** 
> $$
> S_0 + p_0 = c_0 + X(1+r)^{-T}
> $$
> - **Put price from parity:** 
> $$
> p_0 = c_0 + X(1+r)^{-T} - S_0
> $$
> - **Call price from parity:** 
> $$
> c_0 = S_0 + p_0 - X(1+r)^{-T}
> $$
> - **Put-call forward parity:** 
> $$
> F_0(T)(1+r)^{-T} + p_0 = c_0 + X(1+r)^{-T}
> $$
> - **Forward version rearranged:** 
> $$
> p_0 - c_0 = [X - F_0(T)](1+r)^{-T}
> $$
> - **A share priced at INR 295, a call at INR 59, strike INR 265, risk-free rate 4%, and maturity 0.5 years. Find the put.** Quick algorithm: discount the strike to INR 259.85, then do $59 + 259.85 - 295 = 23.85$.
> - **Same setup, but the put trades at INR 30 instead of INR 23.85. Find arbitrage profit.** Quick algorithm: compare the two equal portfolios and pocket $295 + 30 - 59 - 259.85 = 6.15$ today.
> - **A share is INR 295, strike is INR 325, put is INR 56, risk-free rate is 4%, maturity is 0.5 years. Find the call.** Quick algorithm: do $295 - c_0 = 325(1.04)^{-0.5} - 56$, so $c_0 = 32.31$.
> - Big gotcha: same strike and same expiration date are not decoration; parity needs those matching details.
> - Big gotcha: this reading assumes European options on an underlying with no income or benefit.

> [!abstract] MEMORISE
> $$
> S_0 + p_0 = c_0 + X(1+r)^{-T}
> $$
>
> $$
> p_0 = c_0 + X(1+r)^{-T} - S_0
> $$
>
> $$
> S_0 = c_0 - p_0 + X(1+r)^{-T}
> $$
>
> $$
> F_0(T)(1+r)^{-T} + p_0 = c_0 + X(1+r)^{-T}
> $$
>
> $$
> p_0 - c_0 = [X - F_0(T)](1+r)^{-T}
> $$
>
> Notation in simple language:
> - $S_0$: underlying price today
> - $p_0$: put premium today
> - $c_0$: call premium today
> - $X$: exercise price
> - $r$: risk-free rate
> - $T$: time to expiration
> - $F_0(T)$: forward price agreed today for expiration at time $T$

1. This reading is about a very specific no-arbitrage relationship. What is no-arbitrage: a condition where two portfolios with identical future cash flows must have the same price today.
2. The source focuses on European options on an underlying with no income or benefit. That assumption matters because early exercise and income would disturb the clean parity relation.
3. Put-call parity says you can build one payoff using different instruments. What is parity: a pricing equality forced by identical expiration cash flows.
4. The key idea starts with two portfolios. One is a fiduciary call. The other is a protective put. If their ending cash flows match in every state, their prices today must match too.

##### PUT-CALL PARITY

5. A fiduciary call means buying a call option and buying a risk-free bond that will pay the exercise price at expiration. Why is it used: it gives upside above the strike while preserving the strike amount.
6. A protective put means buying the underlying asset and buying a put option on that same asset. Why is it used: it keeps upside in the asset while putting a floor under losses.
7. Slow down and see the symmetry. Both portfolios let you benefit if the underlying rises, but neither lets you fall below the exercise price at expiration.
8. If the expiration price is below the exercise price, the protective put ends at the exercise price because the put fills the hole. The fiduciary call also ends at the exercise price because the bond pays that amount.
9. If the expiration price is above the exercise price, the protective put is just the underlying price. The fiduciary call is also the underlying price because call payoff plus bond payoff becomes the asset price.
10. Since the two portfolios end the same way in every state, the source says their time-zero prices must match. That equality is put-call parity.

$$
S_0 + p_0 = c_0 + X(1+r)^{-T}
$$

11. What is $X(1+r)^{-T}$: the present value today of the exercise price paid at expiration. Why is it used: the bond must be sized so it grows to the strike exactly at maturity.
12. Read the formula like a sentence: long underlying plus long put equals long call plus the present value of the strike. That is much easier to remember than staring at symbols.
13. This is a no-arbitrage statement, not just a cute identity. If the left side and right side diverge in market prices, one side is overpriced and can be sold against the cheaper side.
14. The relation only works cleanly when the call and put share the same underlying, the same exercise price, and the same expiration date. Miss any one of those, and you are matching the wrong cash flows.

> [!info] WHY THIS WORKS
> Think like a very stubborn trader at expiration. You only care about the money that lands in your hand, not the story of how the portfolio was built.
>
> If the asset crashes below the strike, both portfolios still leave you with the strike.
>
> If the asset flies above the strike, both portfolios leave you with the asset price.
>
> Same ending movie in every scene means same ticket price today.

15. The source's first rearrangement solves for the put premium. That gives a replicating recipe for a put using a call, a bond, and a short underlying position.

$$
p_0 = c_0 + X(1+r)^{-T} - S_0
$$

16. What is a replicating portfolio: a portfolio of other instruments that produces the same payoff as the target instrument. Why is replication used: once payoff is matched, price is forced by no-arbitrage.
17. So a long put is equivalent to a long call, a long risk-free bond, and a short underlying. The short underlying hurts when prices rise, but the long call rescues that upside.
18. The next rearrangement solves for the underlying itself. That is the reading's clean proof that the asymmetric call and put payoffs can combine into the straight-line payoff of the asset.

$$
S_0 = c_0 - p_0 + X(1+r)^{-T}
$$

19. Read that one casually: long call minus long put plus a bond gives you the underlying. If you forget the algebra, remember that call and put asymmetry can be stitched into a linear asset payoff.
20. Exhibit 6 in the source is worth memorizing as building blocks. Any one of the four positions can be rebuilt from the other three by flipping signs correctly.

> [!warning] HAMMER THIS INTO YOUR HEAD
> Long underlying = long call, short put, and long risk-free bond.
> Long put = long call, long risk-free bond, and short underlying.
> These sign flips are where exam mistakes are born.

> [!question] BIOMIAN PUT PRICE
> Problem: Biomian shares are INR 295. A six-month call with strike INR 265 is INR 59. The risk-free rate is 4%. Find the six-month put with the same strike and maturity.
>
> Solution:
> $$
> \text{PV}(X) = 265(1.04)^{-0.5} = 259.85
> $$
> $$
> p_0 = 59 + 259.85 - 295 = 23.85
> $$
>
> Explanation: The no-arbitrage put premium is **INR 23.85**.

21. That example matters because it trains the simplest parity reflex. Discount the strike first, then move the terms across the equation with the correct signs.
22. Arbitrage appears when one parity side is priced above the other. What is arbitrage here: locking an initial positive cash flow while the later net cash flow is zero in every state.
23. If $S_0 + p_0$ is greater than $c_0 + X(1+r)^{-T}$, then the protective put side is overpriced. Sell the overpriced side and buy the cheap fiduciary call side.
24. The source's Biomian arbitrage does exactly that. It sells the shares and the put, and buys the call and the risk-free asset.
25. Why those trades: because they create equal and opposite expiration cash flows, leaving only the initial mispricing cash pocketed today.

> [!question] BIOMIAN ARBITRAGE
> Problem: Biomian shares are INR 295. The correct put is INR 23.85, but the market put is INR 30. The call is INR 59, strike is INR 265, and the risk-free rate is 4%. Find the arbitrage profit.
>
> Solution:
> $$
> \text{PV}(X) = 265(1.04)^{-0.5} = 259.85
> $$
> $$
> \text{Profit at } t=0 = 295 + 30 - 59 - 259.85 = 6.15
> $$
>
> Explanation: The later combined payoff is zero in every state, so **INR 6.15** is a riskless arbitrage gain today.

26. Do not over-romanticize arbitrage. It is just "sell the expensive copy, buy the cheap copy." The heavy lifting is done by proving those copies really end with the same payoff.

##### OPTION STRATEGIES BASED ON PUT-CALL PARITY

27. Put-call parity is not only for pricing options. It also lets you rebuild strategy payoffs from other pieces.
28. A covered call is long the underlying and short the call. Why is it used: the investor wants some income from the call premium while capping upside above the strike.
29. The source rearranges parity to express the covered call. Start from $S_0 + p_0 = c_0 + X(1+r)^{-T}$ and solve for $S_0 - c_0$.

$$
S_0 - c_0 = X(1+r)^{-T} - p_0
$$

30. Read that verbally: a covered call equals a long risk-free bond and a short put. This is a beautiful exam identity because it converts an asset-plus-option strategy into a bond-plus-option strategy.
31. What is a short put: an obligation to buy the asset at the strike if the holder exercises. Why does it fit: the covered call also gives limited upside and downside exposure below the strike.

> [!example] VISWAN FAMILY OFFICE COVERED CALL
> The Viswan Family Office liked Biomian for the long run but expected six sleepy months. So instead of just sitting on the shares, the office considered selling a call at a higher strike to squeeze income out of stillness.
>
> That is the emotional logic of a covered call: "I still want the asset, but if nothing dramatic happens soon, at least pay me for waiting."

> [!question] COVERED CALL REPLICATION
> Problem: Biomian shares are INR 295. A six-month put with strike INR 325 costs INR 56. The risk-free rate is 4%. Find the no-arbitrage call premium for the covered call setup.
>
> Solution:
> $$
> 295 - c_0 = 325(1.04)^{-0.5} - 56
> $$
> $$
> c_0 = 32.31
> $$
>
> Explanation: The covered call is equivalent to a long bond and a short put, so the implied call premium is **INR 32.31**.

32. This section teaches a deeper habit: whenever you see an option strategy, ask whether parity can rewrite it into something simpler. Often the exam is really testing the rewrite, not the story.

##### PUT-CALL FORWARD PARITY

33. Put-call forward parity starts from one earlier fact: a long underlying position can be replicated by a long forward contract plus a risk-free bond.
34. What is a synthetic underlying position: a combination of a forward purchase and a risk-free bond that replicates a cash purchase of the underlying. Why is it used: to replace the cash asset with forward-based building blocks.
35. Once you substitute that synthetic asset into ordinary put-call parity, you get put-call forward parity.

$$
F_0(T)(1+r)^{-T} + p_0 = c_0 + X(1+r)^{-T}
$$

36. This formula says a synthetic protective put has the same cost as a fiduciary call. The cash underlying has disappeared, but the expiration payoff logic is unchanged.
37. A synthetic protective put is a long forward, a risk-free bond with face value equal to the forward price, and a long put. Why is it used: together they mimic a protective put.
38. At expiration, the forward contributes $S_T - F_0(T)$, the bond contributes $F_0(T)$, and the put contributes either $X - S_T$ or zero. Add them and you again get either $X$ or $S_T$.
39. That is the same expiration profile as the fiduciary call, so the no-arbitrage prices today must match.
40. The cleanest rearrangement in this section is:

$$
p_0 - c_0 = [X - F_0(T)](1+r)^{-T}
$$

41. Read it slowly: long put and short call together are equivalent to a long risk-free bond and a short forward position. This is the forward-world cousin of the earlier parity identities.
42. The source's forward example with Biomian produces almost the same put premium as the cash-underlying version. That is exactly what you should expect if the replication logic is sound.

> [!question] PUT-CALL FORWARD PARITY
> Problem: Biomian shares are INR 295. The strike is INR 265. The six-month call is INR 59. The risk-free rate is 4%. Use put-call forward parity to find the put.
>
> Solution:
> $$
> F_0(T) = 295(1.04)^{0.5} = 300.84
> $$
> $$
> p_0 - 59 = (265 - 300.84)(1.04)^{-0.5}
> $$
> $$
> p_0 = 23.86
> $$
>
> Explanation: The no-arbitrage put premium is **INR 23.86**, essentially the same as the cash-underlying approach.

43. If you get a tiny rounding difference between 23.85 and 23.86, do not panic. The source itself is showing the same economics through two equivalent routes.

##### FIRM VALUE APPLICATIONS

44. The reading then stretches parity beyond trading desks and into capital structure. This is where the topic gets unexpectedly beautiful.
45. Suppose firm value today is $V_0$ and the firm has zero-coupon debt with face value $D$. Then firm value equals equity value plus the present value of debt.
46. At debt maturity, two worlds exist. The firm is solvent if firm value at maturity exceeds debt face value. The firm is insolvent if firm value falls short of debt face value.
47. If the firm is solvent, debtholders receive $D$ and shareholders receive the residual $V_T - D$. If the firm is insolvent, debtholders take the firm value and shareholders get zero.
48. The shareholder payoff is therefore:

$$
\max(0, V_T - D)
$$

49. What is a residual claim: the amount left after higher-priority claims are paid. Why is equity called residual: shareholders get paid only after debt has been satisfied.
50. That shareholder payoff is exactly the payoff of a call option on firm value with exercise price equal to debt face value. Unlimited upside, zero below the strike: same picture.
51. The debtholder payoff is:

$$
\min(V_T, D)
$$

52. That can also be written as debt face value minus a put option on firm value. So debtholders are like holders of risk-free debt who have sold a put to shareholders.
53. Why is that sold put intuition useful: as insolvency risk rises, the put becomes more valuable, which means the debtholder's position becomes worse.
54. The source interprets that put value as the credit spread intuition. More insolvency risk means a more valuable put written by debtholders, so debt should demand more compensation.
55. Put-call parity then becomes a firm-value identity:

$$
V_0 = c_0 + PV(D) - p_0
$$

56. Read that in plain English: firm value equals the shareholders' call-like claim plus the debtholders' risky debt claim, where risky debt is risk-free debt minus a short put.
57. This is one of those rare derivatives readings that explains corporate finance without leaving derivatives logic. Equity is not "sort of like" a call. In this setup, it really is a call-like payoff.

> [!warning] EXAM TRAP
> Shareholders are the long call side.
> Debtholders are the short put side layered onto risk-free debt.
> If leverage rises and insolvency risk rises, the put on firm value becomes more valuable, which hurts debtholders.

58. The source's practice problem says exactly that: when leverage rises, the debtholder position deteriorates because debtholders are effectively short a put on firm value that has appreciated.

> [!tip] QUICK CHECKS
> - Same underlying, same strike, same expiration date.
> - European options only in this reading.
> - Discount the strike before moving terms around.
> - Overpriced side gets sold; underpriced side gets bought.
> - Equity payoff maps to a call on firm value. Debt payoff maps to risk-free debt minus a put.
