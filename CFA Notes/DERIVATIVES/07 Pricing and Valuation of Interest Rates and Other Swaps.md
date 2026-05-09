
> [!tip] LOOK AT THESE BEFORE EXAM
> - A swap is just a **series of FRA-like settlements**. One FRA gives you one settlement. One swap gives you many.
> - If the exam says **pay fixed, receive floating**, think like this: **market reference rate minus fixed rate**. If that number is positive, the fixed-rate payer receives. If it is negative, the fixed-rate payer pays.
> - Periodic settlement for the fixed-rate payer:
> $$
> (\text{MRR} - s_N)\times \text{Notional}\times \text{Period}
> $$
> - **Par swap rate** means the fixed rate that makes the swap worth zero at the start. In words: **present value of fixed side = present value of floating side**.
> - Swap **price** is the fixed swap rate written into the contract. Swap **value** is what that old contract is worth now after time passes and rates move.
> - On any settlement date:
> $$
> \text{Swap value} = \text{current settlement value} + \text{present value of remaining future settlements}
> $$
> - If expected forward rates rise after inception, the fixed-rate payer likes that because the floating receipts are expected to get fatter while the fixed payments stay locked.
> - If expected forward rates fall after inception, the fixed-rate receiver likes that because fixed receipts stay locked while floating payments are expected to shrink.
> - **Fixed-rate payer swap settlement:** Fixed payer receives floating; use **floating minus fixed, times notional, times period**. Example: floating 5%, fixed 4%, notional 100 million, semiannual → 1% × 100 million × 0.5 = **receive 500,000**.
>   
> - **Fixed-rate receiver swap settlement:** Fixed receiver pays floating; use **fixed minus floating, times notional, times period**. Example: fixed 4%, floating 5%, notional 100 million, semiannual → negative 1% × 100 million × 0.5 = **pay 500,000**.
>     
> - **Implied forward or FRA rate:** Two-year investment must equal one-year investment followed by future one-year rate. Example: 100 grows at 5% for two years to 110.25; first year at 4% gives 104; 110.25 divided by 104 minus 1 = **6.01% forward rate**.
>     
> - **Par swap rate:** Fixed rate is the present-value-weighted average of floating rates. Example: discounted floating payments total 10.88; sum of discount factors is 2.76; fixed swap rate = 10.88 divided by 2.76 = **3.94%**.
>     
> - **Swap value after rates move:** Fixed payer gains when future floating rates rise above fixed rate. Example: receive floating 5%, pay fixed 4%, notional 100 million, one year → expected receipt 1 million; discount at 5% → value **952,381**.
>     
> - **Bond-equivalent valuation:** Receive fixed, pay floating equals long fixed bond minus floating note. Example: fixed bond value 102 million, floating note 100 million → swap value = **positive 2 million**.
>     
> - **Multi-period settlement table:** Calculate each period separately, then add. Example: pay fixed 4%, floating rates 5%, 3%, 6%, semiannual, notional 100 million → receive 500k, pay 500k, receive 1m → net **receive 1 million**.
>     
> - **Swap versus FRA strip:** FRA uses different fixed rates; swap uses one fixed rate. Example: FRAs at 3%, 4%, 5% versus swap at 4%; actual floating 4%, 5%, 6% → both total **receive 3 million**, but timing differs.
> 

### LEARNING OUTCOMES

- Describe how swap contracts are similar to but different from a series of forward contracts.
- Contrast the value and price of swaps.

### SWAPS VS. FORWARDS

> [!abstract] MEMORISE
> - Swap = many future exchanges. Forward = one future exchange.
> - Interest rate swap = one constant fixed rate against a series of floating market reference rates.
> - Series of forward rate agreements = many separate fixed rates, one for each future period.
> - Both swaps and forward rate agreements are firm commitments, have symmetric payoff profiles, and start with zero value ignoring costs.

1. Imagine the exam gives you a swap. Do not panic. First ask: is this one future exchange or many future exchanges? A forward gives you one. A swap gives you a series.
2. What is a swap: an agreement to exchange a series of future cash flows. Why is it used: because real loans, bonds, and liabilities usually create many payment dates, not just one.
3. What is a forward contract in this setting: one future exchange of value at a later date. That is why a swap feels like a chain of forward-style deals stitched together.
4. In interest rate land, the one-period forward-style building block is the **forward rate agreement**, or **FRA**. After this line, **FRA** is safe to read quickly.
5. What is a forward rate agreement: a contract for one interest-period settlement based on the difference between a fixed rate and a future market reference rate. Why is it used: it lets you lock one future borrowing or lending period.
6. So hammer this into your head: **one FRA equals one settlement; one swap equals many FRA-like settlements**.
7. Swaps and FRAs are similar in the ways the exam likes to test. Both are **firm commitments**, so both sides are stuck with the deal once they enter.
8. What is a firm commitment here: a derivative where both sides must perform if the contract is alive. This is not an option where one side can casually walk away.
9. Both swaps and FRAs also have a **symmetric payoff profile**. If one side wins, the other side loses by the same amount.
10. What is a symmetric payoff profile: gains for one counterparty are losses for the other. Why does it matter: it reminds you this is a zero-sum contract before costs.
11. Both contracts also start with **zero value at inception**, ignoring transaction costs and counterparty credit costs. That is because the fixed terms are chosen so nobody is gifted money on day one.
12. Another similarity is **counterparty credit exposure**. These are promises between counterparties, so each side cares whether the other side can still pay later.
13. Now come to the big difference. A series of FRAs usually has a **different fixed rate for each future period** because the term structure gives different forward rates at different maturities.
14. A standard interest rate swap does **not** do that. It uses **one constant fixed swap rate** across the life of the contract.
15. That is why you should think of a swap as “many FRA-like settlements, but one fixed rate held constant the whole way.”
16. The floating side is tied to the **market reference rate**, or **MRR**. After this line, **MRR** is safe to read quickly.
17. What is market reference rate: the floating benchmark that resets for each period and determines the floating leg cash flow. Why is it used: it lets the swap move with the market while the fixed side stays frozen.
18. If the exam says **pay fixed, receive floating**, your settlement logic is simple: **MRR minus fixed rate**. Positive means you receive. Negative means you pay.
19. If the exam says **receive fixed, pay floating**, just flip the sign. Same economics, opposite direction.
20. Now solve mechanically. First take the floating rate minus fixed rate. Second multiply by the notional. Third adjust for the period length.

$$
\text{Periodic settlement for fixed-rate payer} = (\text{MRR} - s_N)\times \text{Notional}\times \text{Period}
$$

21. Read that formula in plain English: “market rate minus locked fixed rate, times contract size, times fraction of the year.” That is it.
22. If the exam gives you a fixed-rate payer at **1.12%**, an MRR of **0.25%**, a notional of **EUR100 million**, and a semiannual period, do it step by step. The rate difference is **0.25% - 1.12% = -0.87%**.
23. One percent of **EUR100 million** is **EUR1 million**, so **0.87%** is **EUR870,000**. Then take half because the period is semiannual. You get **-EUR435,000**.
24. The negative sign means the fixed-rate payer pays **EUR435,000** to the fixed-rate receiver. Do not overcomplicate it. The sign already tells the story.

> [!question] SWAP SETTLEMENT
> Problem: You are the fixed-rate payer on a swap. Fixed rate is **4%**, floating market reference rate is **5%**, notional is **USD10 million**, and the payment period is **0.5 year**. What is the settlement from your perspective?
>
> ---
>
> First do floating minus fixed:
>
> $$
> 5\% - 4\% = 1\%
> $$
>
> Then multiply by notional:
>
> $$
> 1\% \times 10{,}000{,}000 = 100{,}000
> $$
>
> Then adjust for the period:
>
> $$
> 100{,}000 \times 0.5 = 50{,}000
> $$
>
> Settlement is **+USD50,000**. Positive means the fixed-rate payer receives.

25. Another exam favorite is: why use one swap instead of many FRAs? The short answer is efficiency. One swap handles a full stream of payments without forcing you to manage many separate contracts.
26. That matters a lot for issuers. A company with a floating-rate term loan usually has many future interest payments, so a swap matches the liability better than one lonely FRA.
27. Imagine a company has a floating-rate loan at **MRR + 1.50%** and hates uncertainty. It can enter a **pay-fixed, receive-MRR** swap.
28. When the company combines the loan and the swap, the floating MRR part largely cancels. What remains is roughly **fixed swap rate + loan spread**.
29. That is the real-life magic of the swap. The company did not refinance the loan. It changed the rate exposure sitting on top of the loan.
30. Swaps are also useful for investors. A portfolio manager can change interest rate exposure without buying or selling a pile of bonds.
31. If a portfolio manager wants to benefit from **falling interest rates**, the manager usually wants **receive fixed, pay floating** exposure because fixed cash flows become more valuable when rates drop.
32. If the manager wants to reduce duration or behave more like a short bond position, the manager usually wants **pay fixed, receive floating**.
33. So the intuition is clean: **receive fixed feels bond-like; pay fixed feels short-bond-like**. Keep that instinct ready for the exam.

> [!example] FLOATING LOAN TO FIXED COST
> Imagine a company borrowing at a floating rate and losing sleep because each reset can raise interest expense. The company enters a pay-fixed, receive-floating swap. Now the floating rate it pays on the loan is largely offset by the floating rate it receives on the swap, so the mess gets turned into something much closer to a steady fixed borrowing cost.

### SWAP VALUES AND PRICES

> [!abstract] MEMORISE
> - Swap **price** = the fixed swap rate written into the contract.
> - Swap **value at inception** = zero, ignoring costs.
> - On a settlement date, swap value = current settlement value + present value of remaining future settlements.
> - Higher expected future floating rates help the fixed-rate payer.
> - Lower expected future floating rates help the fixed-rate receiver.

34. Now slow down because this is where people mix up **price** and **value**. The exam absolutely loves that confusion.
35. What is swap price: the fixed swap rate written into the contract at inception. Why is it called a price: because it is the fixed term you solve for when the deal is first struck.
36. What is swap value: what the existing contract is worth now after time passes and rates move. Price is the locked rate. Value is the mark-to-market.
37. The **par swap rate** is the fixed rate that makes the swap worth zero at the start. In words: the present value of fixed payments equals the present value of expected floating payments.
38. What is par swap rate: the break-even fixed rate for the whole swap. Why is it used: because it prevents either side from receiving a free lunch at inception.
39. So if the exam asks for **swap price**, it is usually asking for that fixed par swap rate, not for some later mark-to-market value.
40. And if the exam asks for **swap value** on a later date, you are no longer solving for the fixed rate. You are judging how good or bad the old locked rate looks now.
41. For the fixed-rate payer, the current settlement on a settlement date is still:

$$
(\text{MRR} - s_N)\times \text{Notional}\times \text{Period}
$$

42. But the swap’s total value on that settlement date is bigger than just this one payment. You also add the present value of all remaining future settlements.
43. So the full logic is: **current settlement value plus present value of remaining future swap settlements**. That is the valuation backbone.
44. As time passes, the swap value can change even if the original fixed rate never changes. The contract rate is frozen, but the expected future floating side keeps getting rejudged by the market.
45. If expected forward rates rise after inception, the fixed-rate payer likes that. Why: the floating receipts are now expected to be larger while the fixed payments stay stuck at the old rate.
46. So a rise in expected forward rates creates a **mark-to-market gain for the fixed-rate payer** and a **mark-to-market loss for the fixed-rate receiver**.
47. If expected forward rates fall after inception, flip the story. The fixed-rate receiver now looks better because locked fixed receipts are high relative to the weaker expected floating payments.
48. Another way to see the same idea is with bond language. A fixed-rate payer is like being **long a floating-rate note and short a fixed-rate bond**. A fixed-rate receiver is the opposite.
49. That bond analogy is why **receive fixed increases duration** and **pay fixed reduces duration**. So when the exam asks how to make a fixed-income portfolio more sensitive to falling rates, your reflex should be: **receive fixed**.

> [!question] PRICE VS VALUE
> Problem: A swap was entered at a fixed rate of **2.05%**. Later, expected forward rates rise above what the market originally expected. From the fixed-rate payer’s perspective, what happens to the swap value?
>
> ---
>
> Do not recalculate the old price. That **2.05%** is the locked swap price.
>
> Ask what changed: expected floating payments are now higher.
>
> Fixed payments are still based on the old locked rate.
>
> So the fixed-rate payer now expects a richer floating side against the same fixed side.
>
> The swap therefore has a **positive mark-to-market value** to the fixed-rate payer.

> [!tip] QUICK CHECKS
> - **Pay fixed, receive floating**: use **MRR minus fixed**.
> - **Receive fixed, pay floating**: same math, opposite sign.
> - **One FRA** means one settlement. **One swap** means many.
> - **Price** is the contract’s fixed rate. **Value** is what that old contract is worth now.
