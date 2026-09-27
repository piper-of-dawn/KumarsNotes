## Variant: 1 — Build risk-weighted assets before testing capital

**Abstract:** *Weight each exposure for risk before adding it. A bank’s accounting assets and its regulatory risk-weighted assets answer different questions.*

> A bank holds USD 100m cash, USD 600m performing corporate loans, and USD 40m overdue loans. Use risk weights of 0%, 100%, and 150%, respectively. An off-balance-sheet commitment contributes another USD 20m of risk-weighted exposure after all adjustments. Calculate total risk-weighted assets and required total capital at the stipulated 8% minimum.

<span class="jargon-unlock">**Risk-weighted assets (RWA). What are they?** Exposures adjusted for regulatory risk: $RWA=\sum A_iw_i$, where $A_i$ is exposure and $w_i$ its supplied weight. **Off-balance-sheet commitment. What is it?** A promise that can create future funding or credit exposure despite not appearing as a current loan. **Capital. What is it?** Eligible loss-absorbing funding; it is not a pile of cash.</span>

**1. Apply the risk weights**

The overdue loans receive extra weight because their risk is greater. The cash receives zero under the supplied convention. The commitment has already been adjusted, so do not weight it twice.

$$
RWA=100(0)+600(1)+40(1.5)+20=\boxed{\text{USD }680\text{m}}
$$

**2. Apply the capital requirement**

The 8% requirement attaches to the risk-weighted amount, not the USD 740m of accounting assets.

$$
\text{Required capital}=0.08(680)=\boxed{\text{USD }54.4\text{m}}
$$

Risk weights are the regulatory map, not the territory: zero weight under this exercise does not mean every possible risk has disappeared.

> [!NOTE]
> Use the weights and thresholds supplied. Real requirements can include buffers and jurisdiction-specific adjustments beyond this simplified minimum.

*Source pattern: 2025 CFA Level II FSA, LM4, pp.207–210; practice Q2. Inputs adapted for practice.*

---

## Variant: 2 — Convert accounting equity into common equity Tier 1

**Abstract:** *Regulatory capital starts with accounting equity, then applies eligibility adjustments. Read the signs: subtracting a negative deduction adds it back.*

> A bank reports common shareholders’ equity of USD 200m. Add qualifying minority interests of USD 2m. Deduct goodwill of USD 15m and disallowed deferred tax assets of USD 10m. A further regulatory line reads “Less: accumulated unrealized loss adjustment, (USD 3m).” There are no other adjustments. Find CET1 and its ratio to USD 1,500m RWA.

<span class="jargon-unlock">**Common equity Tier 1 (CET1). What is it?** The highest-quality eligible bank capital after regulatory adjustments. **Minority interests. What are they?** Outside investors’ ownership in consolidated subsidiaries; only the qualifying amount enters here. **Goodwill. What is it?** An acquisition premium recorded as an asset. **Deferred tax asset. What is it?** A potential future tax benefit. **RWA. What is it?** Risk-weighted assets; the ratio is $CET1/RWA$.</span>

**1. Follow the adjustment signs**

The USD 3m negative entry is inside a “less” line. Subtracting it reverses a deduction; do not invent another loss.

$$
CET1=200+2-15-10-(-3)=\boxed{\text{USD }180\text{m}}
$$

**2. Divide by risk-weighted assets**

$$
\text{CET1 ratio}=\frac{180}{1{,}500}=\boxed{12.00\%}
$$

The check is simple: accounting equity was USD 200m, while net regulatory adjustments reduce it by USD 20m. Accounting equity cannot simply stroll into the capital calculation wearing a different name badge.

> [!NOTE]
> Only apply the adjustments specified. The historical case illustrates the reconciliation; it is not a universal list of current deductions.

*Source pattern: 2025 CFA Level II FSA, LM4, pp.210, 231–232, Exhibit 11. Inputs adapted for practice.*

---

## Variant: 3 — Build the three capital ratios without double-counting tiers

**Abstract:** *CET1 sits inside Tier 1, and Tier 1 sits inside total capital. Compare all three; a healthy total can conceal weaker capital quality.*

> Year 1 has CET1 of USD 90m, additional Tier 1 of USD 10m, Tier 2 of USD 30m, and RWA of USD 1,000m. Year 2 has USD 96m, USD 16m, USD 16m, and USD 1,100m, respectively. Calculate the three ratios in both years and assess the direction of change.

<span class="jargon-unlock">**CET1. What is it?** Common equity Tier 1, the highest-quality eligible bank capital. **Additional Tier 1 (AT1). What is it?** Other qualifying instruments added to CET1. **Tier 2 (T2). What is it?** A lower tier of qualifying capital. **Capital ratios. What are they?** $CET1/RWA$, $(CET1+AT1)/RWA$, and $(CET1+AT1+T2)/RWA$, where RWA means risk-weighted assets.</span>

**1. Build the nested numerators**

Tier 1 totals USD 100m then USD 112m. Total capital is USD 130m then USD 128m. CET1 is already inside Tier 1; adding it again would manufacture capital out of punctuation.

$$
\begin{array}{c|cc}
&\text{Year 1}&\text{Year 2}\\
\text{CET1 ratio}&90/1{,}000=9.00\%&96/1{,}100=8.73\%\\
\text{Tier 1 ratio}&100/1{,}000=10.00\%&112/1{,}100=10.18\%\\
\text{Total ratio}&130/1{,}000=13.00\%&128/1{,}100=11.64\%
\end{array}
$$

**2. Interpret each layer**

The overall result is $\boxed{\text{mixed}}$: Tier 1 improves, while CET1 and total capital ratios fall. Even the USD 6m increase in CET1 fails to keep pace with the growth in RWA.

> [!NOTE]
> A rising capital amount does not guarantee a rising capital ratio. Inspect the quality of capital as well as its total.

*Source pattern: 2025 CFA Level II FSA, LM4, Example 1; Exhibits 11–13; practice Q7, Q9. Inputs adapted for practice.*

---

## Variant: 4 — A stronger capital ratio with less capital

**Abstract:** *A ratio can rise because its denominator shrinks faster than its numerator. Calculate both growth rates before praising the bank.*

> A bank’s eligible capital falls from USD 180m to USD 160m. RWA falls from USD 1,200m to USD 900m. Find both capital ratios, the percentage changes in capital and RWA, and the amount of capital needed to support the old RWA at the new ratio.

<span class="jargon-unlock">**Capital ratio. What is it?** Eligible capital divided by risk-weighted assets (RWA). **Percentage change. What is it?** $(\text{new}/\text{old})-1$. **Percentage point. What is it?** The difference between two percentages, distinct from their relative percentage change.</span>

**1. Calculate the ratio and its moving parts**

$$
\begin{aligned}
\text{Old ratio}&=180/1{,}200=15.00\%\\
\text{New ratio}&=160/900=\boxed{17.78\%}\\
\Delta\text{ capital}&=160/180-1=-11.11\%\\
\Delta RWA&=900/1{,}200-1=\boxed{-25.00\%}
\end{aligned}
$$

The ratio rises by 2.78 percentage points because risk-weighted exposures contract more sharply. The bank has improved the fraction, but it has not raised fresh capital.

**2. Reverse the calculation**

Maintaining the new ratio on the old risk-weighted asset base would require:

$$
\text{Capital}=\frac{160}{900}(1{,}200)=\boxed{\text{USD }213.33\text{m}}
$$

That is USD 53.33m more than current capital. Shrinking the business and strengthening its funding are different explanations for the same attractive ratio.

> [!NOTE]
> Use unrounded ratios in inverse calculations. Ratio improvement alone does not identify whether capital rose or exposures fell.

*Source pattern: 2025 CFA Level II FSA, LM4, Example 1, pp.210–212. Inputs adapted for practice.*

---

## Variant: 5 — Find the binding limit on asset growth

**Abstract:** *Each capital tier imposes its own maximum RWA. The smallest ceiling controls; the other ratios do not get a vote.*

> A bank has USD 60m CET1, USD 75m total Tier 1, and USD 90m total capital. For this exercise, minimum ratios are 4.5%, 6%, and 8%, with no extra buffers. Current RWA is USD 1,000m. Capital stays fixed. Find maximum RWA and additional 100%-risk-weighted loans that can be added using funding that does not change capital.

<span class="jargon-unlock">**CET1. What is it?** Common equity Tier 1. **Tier 1. What is it?** CET1 plus other qualifying Tier 1 instruments. **RWA. What is it?** Risk-weighted assets. **Binding constraint. What is it?** The tightest limit. For capital $C$ and minimum ratio $r$, $RWA_{\max}=C/r$.</span>

**1. Solve each ratio backward**

$$
\begin{aligned}
RWA_{\text{CET1}}&=60/0.045=1{,}333.33\\
RWA_{\text{Tier 1}}&=75/0.06=1{,}250\\
RWA_{\text{total}}&=90/0.08=\boxed{1{,}125}
\end{aligned}
$$

All amounts are USD millions. Total capital is the binding constraint.

**2. Calculate the remaining room**

$$
\text{Additional loans}=1{,}125-1{,}000=\boxed{\text{USD }125\text{m}}
$$

At that limit, CET1 is 5.33%, Tier 1 is 6.67%, and total capital is exactly 8%. All three pass. This is a capital-only ceiling; it does not establish that liquidity, funding, or credit demand can support the growth.

> [!NOTE]
> Divide each eligible capital amount by its own minimum, then take the minimum ceiling. Do not average the three limits.

*Source pattern: 2025 CFA Level II FSA, LM4, pp.209–210; algebraic inverse of capital ratios. Inputs adapted for practice.*

---

## Variant: 6 — Stress both capital and RWA

**Abstract:** *A stress can shrink capital and increase RWA at once. A one-variable sensitivity understates the damage when both move against the bank.*

> A bank starts with USD 150m CET1 and USD 1,000m RWA. Find the ratio after (a) a USD 5m after-tax loss reducing CET1, (b) a USD 50m RWA increase only, and (c) both together. Report changes from the initial ratio in basis points.

<span class="jargon-unlock">**CET1. What is it?** Common equity Tier 1 capital. **RWA. What is it?** Risk-weighted assets. **Basis point (bp). What is it?** 0.01 percentage point; a ratio change in decimal form multiplied by 10,000 gives basis points. **Sensitivity. What is it?** The effect of changing a specified input while holding others fixed.</span>

**1. Start from the same baseline**

The initial ratio is $150/1{,}000=15.00\%$. The question already gives an after-tax capital loss, so do not apply tax again.

$$
\begin{aligned}
\text{Loss only}&=145/1{,}000=14.50\%\quad(-50.00\text{ bp})\\
\text{RWA only}&=150/1{,}050=14.2857\%\quad(-71.43\text{ bp})
\end{aligned}
$$

**2. Recalculate the combined case**

$$
\text{Combined ratio}=145/1{,}050=\boxed{13.8095\%}
$$

The combined decline is $\boxed{119.05\text{ bp}}$. Adding the separate declines gives 121.43 bp, a nearby approximation rather than the exact answer. The loss affects a different denominator in the combined case.

> [!NOTE]
> A sensitivity table is conditional. For a simultaneous shock, rebuild the ratio; do not silently treat separate effects as exactly additive.

*Source pattern: 2025 CFA Level II FSA, LM4, pp.250–251, Exhibit 25. Inputs adapted for practice.*

---

## Variant: 7 — Asset composition: more cash, less liquidity by proportion

**Abstract:** *Classify the assets, then divide by total assets in the same year. Absolute growth and portfolio share can point in opposite directions.*

> Year 1 assets are USD 200m liquid assets, USD 250m investments, USD 400m customer loans, USD 50m reverse repos, and USD 100m other assets. Year 2 amounts are USD 220m, USD 350m, USD 470m, USD 60m, and USD 100m. Treat reverse repos as loans for this classification. Calculate liquid-asset, investment, and loan shares in both years.

<span class="jargon-unlock">**Common-size analysis. What is it?** Expressing each category as a share of the total: $\text{share}=\text{category}/\text{total assets}$. **Reverse repo. What is it?** A collateralized loan from the cash lender’s perspective. **Liquidity. What is it?** Ability to meet cash obligations; a liquid-asset share is one indicator, not a complete stress test.</span>

**1. Add mutually exclusive categories**

Total assets are USD 1,000m and USD 1,200m. Loans including reverse repos are USD 450m and USD 530m.

$$
\begin{array}{c|cc}
&\text{Year 1}&\text{Year 2}\\
\text{Liquid assets}&200/1{,}000=20.00\%&220/1{,}200=18.33\%\\
\text{Investments}&250/1{,}000=25.00\%&350/1{,}200=29.17\%\\
\text{Loans}&450/1{,}000=45.00\%&530/1{,}200=44.17\%
\end{array}
$$

**2. Separate amounts from proportions**

Liquid assets rise by 10%, but their share falls by $\boxed{1.67\text{ percentage points}}$. Loans also rise in dollars while falling as a share. The investment share increases; whether that means more risk depends on the investments.

> [!NOTE]
> For this table, each asset belongs in one category. Reverse repos can be grouped differently in other disclosures; follow the specified classification without double-counting.

*Source pattern: 2025 CFA Level II FSA, LM4, Example 2; Exhibit 14; practice Q10. Inputs adapted for practice.*

---

## Variant: 8 — Credit quality and allowances can move in different directions

**Abstract:** *Compare gross credit-quality shares and allowance coverage separately. A falling impaired balance does not settle what future losses require.*

> A loan portfolio has gross balances of USD 1,000m then USD 1,100m. Strong-quality loans rise from USD 700m to USD 825m; impaired loans fall from USD 40m to USD 30m; past-due but unimpaired loans rise from USD 20m to USD 30m. Allowances increase from USD 16m to USD 24m. Find strong-quality shares, impaired-loan coverage, and relevant growth rates.

<span class="jargon-unlock">**Impaired loan. What is it?** A loan identified as credit-deteriorated under the disclosure’s classification. **Past due. What is it?** A payment is late; that category need not equal impaired loans. **Allowance. What is it?** A reduction against gross loans for estimated credit losses. **Coverage. What is it?** Here, allowance divided by impaired loans.</span>

**1. Use gross loans for credit-quality shares**

$$
\begin{aligned}
\text{Strong share}&:700/1{,}000=70\%\ \longrightarrow\ 825/1{,}100=\boxed{75\%}\\
\text{Coverage}&:16/40=40\%\ \longrightarrow\ 24/30=\boxed{80\%}
\end{aligned}
$$

**2. Explain the apparently odd allowance increase**

Impaired loans fall by 25%. Past-due unimpaired loans and allowances both rise by 50%. The allowance increase is consistent with concern about the growing late-payment category, despite better headline credit-quality shares.

Net loans are USD 984m then USD 1,076m. Those amounts belong on the net balance-sheet line; using them for the gross credit-quality shares would change the question halfway through.

> [!NOTE]
> An allowance trend is evidence to investigate, not proof that provisioning is sufficient or manipulated. Future losses can differ from currently impaired balances.

*Source pattern: 2025 CFA Level II FSA, LM4, Example 3; practice Q11. Inputs adapted for practice.*

---

## Variant: 9 — Roll forward the loan-loss allowance and solve the provision

**Abstract:** *The provision builds the allowance; charge-offs use it; recoveries restore it. Cash losses and income-statement expense are different entries.*

> A bank begins with a USD 50m loan-loss allowance and ends with USD 58m. During the year it writes off USD 18m and recovers USD 3m. There are no acquisitions, currency effects, or other movements. Find the provision expense. Closing gross loans are USD 1,000m; find net loans. What would ending allowance be if provision were only USD 15m?

<span class="jargon-unlock">**Allowance. What is it?** The balance-sheet estimate deducted from gross loans. **Provision. What is it?** The income-statement expense added to that estimate. **Charge-off. What is it?** Removal of a loan judged uncollectible. **Recovery. What is it?** Collection of a previously written-off amount. **Rollforward. What is it?** $A_e=A_b+P-C+R$, with ending/beginning allowance $A_e,A_b$, provision $P$, charge-offs $C$, and recoveries $R$.</span>

**1. Reconcile the allowance account**

Net charge-offs are $18-3=15$ million. The bank must replace that USD 15m and add another USD 8m to reach its closing balance.

$$
P=58-50+18-3=\boxed{\text{USD }23\text{m}}
$$

**2. Check the balance sheet and alternative**

$$
\text{Net loans}=1{,}000-58=\boxed{\text{USD }942\text{m}}
$$

With a provision of USD 15m, ending allowance would be $50+15-18+3=\boxed{\text{USD }50\text{m}}$. Provision would exactly replace net charge-offs, leaving the reserve unchanged. A write-off against an existing allowance is not automatically a fresh expense.

> [!NOTE]
> The allowance is a stock; provision and charge-offs are period flows. Never substitute one for another just because all three contain “loss.”

*Source pattern: 2025 CFA Level II FSA, LM4, pp.238–240, Exhibit 17. Inputs adapted for practice.*

---

## Variant: 10 — Three loan-loss ratios, three different questions

**Abstract:** *Calculate coverage of troubled loans, coverage of annual realized losses, and replenishment. Bigger reserves can still provide a thinner cushion.*

> Year 1 allowance is USD 120m, non-accrual loans USD 60m, provision USD 45m, charge-offs USD 50m, and recoveries USD 10m. Year 2 figures are USD 150m, USD 100m, USD 80m, USD 100m, and USD 20m. Calculate the three ratios used in the reading and interpret the changes. Other allowance movements may exist; do not assume these snapshots form a complete rollforward.

<span class="jargon-unlock">**Non-accrual loans. What are they?** Loans on which interest recognition has been suspended because collection is doubtful. **Net charge-offs (NCO). What are they?** Charge-offs minus recoveries. **Allowance. What is it?** The estimated loss reserve. **Provision. What is it?** Current-period loss expense. The ratios are allowance/non-accrual loans, allowance/NCO, and provision/NCO.</span>

**1. Net the recoveries first**

Net charge-offs rise from USD 40m to USD 80m.

$$
\begin{array}{c|cc}
&\text{Year 1}&\text{Year 2}\\
\text{Allowance/non-accrual}&120/60=2.00&150/100=1.50\\
\text{Allowance/NCO}&120/40=3.00&150/80=1.875\\
\text{Provision/NCO}&45/40=1.125&80/80=1.00
\end{array}
$$

**2. Read the pattern**

Allowance rises 25%, but both coverage measures deteriorate. The provision now just matches net charge-offs. The answer is $\boxed{\text{a thinner measured cushion}}$, despite the larger allowance. More sandbags are not necessarily reassuring when the water rises faster.

> [!NOTE]
> Allowance/NCO compares a reserve stock with one year’s losses. It is not a guarantee of that many years of protection, and portfolio mix matters.

*Source pattern: 2025 CFA Level II FSA, LM4, Exhibit 17; practice Q12. Inputs adapted for practice.*

---

## Variant: 11 — When a loss ratio’s denominator vanishes

**Abstract:** *Zero or negative net charge-offs break the usual coverage interpretation. Do not award a bank a perfect score because division stopped working.*

> A bank has allowance USD 30m, provision USD 5m, and non-accrual loans USD 10m. In Case A, charge-offs and recoveries are both USD 4m. In Case B, charge-offs are USD 4m and recoveries USD 6m. Find allowance/non-accrual loans, allowance/net charge-offs, and provision/net charge-offs. Interpret the results.

<span class="jargon-unlock">**Net charge-offs (NCO). What are they?** Charge-offs less recoveries; negative NCO means net recoveries. **Allowance. What is it?** Estimated loan losses recorded against assets. **Provision. What is it?** Current-period loss expense. **Undefined ratio. What is it?** A fraction with a zero denominator, for which ordinary division provides no value.</span>

**1. Calculate the unaffected ratio**

$$
\text{Allowance/non-accrual}=30/10=\boxed{3.00\text{ times}}
$$

**2. Examine the denominator before interpreting coverage**

Case A has $NCO=4-4=0$. Both ratios using NCO are $\boxed{\text{undefined}}$, not proof of infinite financial strength.

Case B has $NCO=4-6=-2$ million:

$$
\text{Allowance/NCO}=30/(-2)=-15,\qquad
\text{Provision/NCO}=5/(-2)=-2.5
$$

Those negative results describe an unusual recovery year. They do not mean reserves are negative or that the bank is under-reserved. Inspect gross write-offs, recoveries, troubled loans, and several years of experience.

> [!NOTE]
> Always inspect the denominator. The standard “higher coverage is better” reading assumes a meaningful positive loss base.

*Source pattern: 2025 CFA Level II FSA, LM4, pp.238–240; boundary cases of Exhibit 17 ratios. Inputs adapted for practice.*

---

## Variant: 12 — Investment losses: gross, net, and old

**Abstract:** *Net losses can hide larger gross losses. Measure loss severity against cost and aged losses against the correct loss pool.*

> A bank’s disclosed securities portfolio has amortized cost USD 500m, gross unrealized gains USD 12m, and gross unrealized losses USD 22m. Of the losses, USD 15m have existed for at least 12 months, including USD 9m on municipal bonds. Municipal bonds have cost USD 100m and gross losses USD 11m. Find fair value and the relevant severity and aging percentages.

<span class="jargon-unlock">**Amortized cost. What is it?** The investment’s accounting cost adjusted over time. **Unrealized gain/loss. What is it?** A value change before sale. **Gross losses. What are they?** Losses on losing positions before offsetting gains elsewhere. **Aging. What is it?** How long positions have remained below cost.</span>

**1. Reconcile cost to fair value**

$$
FV=500+12-22=\boxed{\text{USD }490\text{m}}
$$

Net decline is 2% of cost, but gross losses are $22/500=4.40\%$. Municipal gross losses are $11/100=\boxed{11.00\%}$ of municipal cost, indicating a concentration worth investigating.

**2. Use the loss pool for aging**

$$
\text{Aged share}=15/22=\boxed{68.18\%},\qquad
\text{Municipal share of aged losses}=9/15=\boxed{60.00\%}
$$

The 60% is not the municipal share of the entire investment portfolio. Persistent losses warrant investigation into rates, credit, and recoverability; age alone does not establish an accounting impairment.

> [!NOTE]
> This is valuation and risk analysis using historical disclosure patterns. It does not import the source’s old securities-classification rules into every current reporting regime.

*Source pattern: 2025 CFA Level II FSA, LM4, pp.235–237, Exhibits 15–16. Inputs adapted for practice.*

---

## Variant: 13 — Revenue mix: a bigger share can hide a smaller business

**Abstract:** *Build the total with its negative items intact. Then separate growth in a revenue source from growth in its share of a shrinking total.*

> In Year 1 a bank earns USD 60m net interest income, USD 25m fees, and USD 15m trading income. Year 2 has USD 54m, USD 20m, and USD 18m, plus a USD 12m fair-value loss classified within operating income. Find both years’ total operating income and the net-interest and trading shares. Assess the trend.

<span class="jargon-unlock">**Net interest income. What is it?** Interest earned on assets minus interest paid on funding. **Trading income. What is it?** Gains earned from trading positions; it can be volatile. **Common-size share. What is it?** A component divided by total income, including negative components. **Fair value. What is it?** The relevant market-based measurement of an asset or liability.</span>

**1. Keep the loss in the total**

$$
\text{Year 1 total}=60+25+15=100,\qquad
\text{Year 2 total}=54+20+18-12=\boxed{80}
$$

All amounts are USD millions. Total operating income falls 20%.

**2. Calculate the shares**

Net-interest share rises from 60% to $54/80=\boxed{67.50\%}$ even though its dollar amount falls 10%. Trading share rises from 15% to $18/80=\boxed{22.50\%}$, while its amount rises 20%.

Year 2 shares reconcile: $67.5\%+25\%+22.5\%-15\%=100\%$. Ignoring the negative component would give the bank a sunnier business mix by quietly deleting the bad weather.

> [!NOTE]
> Trading dependence is one earnings-quality signal. A revenue mix alone cannot prove that all interest and fee income is sustainable.

*Source pattern: 2025 CFA Level II FSA, LM4, Example 4; Exhibit 19; practice Q16. Inputs adapted for practice.*

---

## Variant: 14 — How much profit growth came from lower provisions?

**Abstract:** *A lower loss provision raises reported profit even without better operating performance. Add provisions back to compare performance before that estimate.*

> A bank reports pretax profit of USD 80m in Year 1 and USD 110m in Year 2. Loan-loss provisions are USD 50m and USD 20m, respectively. Find the share of profit growth explained by the lower provision. Normalize Year 2 using the Year 1 provision and calculate the after-tax difference at 25%.

<span class="jargon-unlock">**Pretax profit. What is it?** Profit after expenses but before income tax. **Provision. What is it?** Expense for estimated loan losses. **Normalization. What is it?** Recalculating profit under a stated comparison assumption; it does not establish the economically correct estimate. **Pre-provision profit. What is it?** Pretax profit plus the provision expense.</span>

**1. Separate operating change from the estimate**

$$
\begin{aligned}
\text{Profit increase}&=110-80=30\\
\text{Provision reduction}&=50-20=30\\
\text{Contribution to increase}&=30/30=\boxed{100\%}
\end{aligned}
$$

Pre-provision profit is USD 130m in both years. The operating result stood still while the estimate did the travelling.

**2. Normalize under the stated assumption**

$$
\text{Normalized Year 2 pretax profit}=110-(50-20)=\boxed{\text{USD }80\text{m}}
$$

At 25% tax, reported after-tax profit exceeds the normalized amount by $30(1-0.25)=\boxed{\text{USD }22.5\text{m}}$. If credit conditions genuinely improved, a lower provision may be justified; this calculation identifies dependence, not dishonesty.

> [!NOTE]
> Add back the full provision to compare pre-provision profit. Subtract only the change when normalizing one year to another year’s provision.

*Source pattern: 2025 CFA Level II FSA, LM4, pp.241–242, Exhibit 18. Inputs adapted for practice.*

---

## Variant: 15 — Net interest margin is not the interest-rate spread

**Abstract:** *Calculate interest income and expense in money first. The asset and liability rates usually apply to different balances, so subtracting rates can mislead.*

> A bank’s average interest-earning assets are USD 1,000m earning 6% annually. Average interest-bearing liabilities are USD 800m costing 3%. Average total assets are USD 1,200m. Find net interest income, net interest margin, and the interest-rate spread. Explain why they differ.

<span class="jargon-unlock">**Net interest income (NII). What is it?** $NII=yA-cL$, where $A$ is average earning assets, $y$ their yield, $L$ average interest-bearing liabilities, and $c$ their funding rate. **Net interest margin (NIM). What is it?** $NII/A$. **Interest-rate spread. What is it?** $y-c$; it compares two rates rather than two cash amounts.</span>

**1. Convert rates into amounts**

$$
\text{Interest income}=1{,}000(0.06)=60,\qquad
\text{Expense}=800(0.03)=24
$$

The bank earns $\boxed{\text{USD }36\text{m}}$ of NII.

**2. Apply the correct denominator**

$$
NIM=36/1{,}000=\boxed{3.60\%},\qquad
\text{Spread}=6\%-3\%=\boxed{3.00\%}
$$

The margin exceeds the spread because not every dollar of earning assets is funded with these interest-bearing liabilities. Using total assets gives 3.00%, but that is NII/total assets, not NIM. Its accidental equality to the spread is a numerical coincidence, not a new formula.

> [!NOTE]
> For NIM, use average interest-earning assets. Interest-bearing liabilities belong in the expense calculation, not the margin denominator.

*Source pattern: 2025 CFA Level II FSA, LM4, pp.242–246, Exhibits 20–21. Inputs adapted for practice.*

---

## Variant: 16 — Weighted yield, volume effects, and a forecast

**Abstract:** *Weight yields by the balances that earn them. Separate a rate change from a volume change, then use explicit forward assumptions for forecasts.*

> A bank’s average loan portfolio rises from USD 600m earning 7% to USD 700m earning 6%. Its other average earning assets remain USD 300m at 2%. Find total interest income and weighted yield each year. Attribute the loan-income change using a volume-first bridge. At year end, loans are USD 750m at an expected 6.2% and other earning assets USD 250m at 2.4%; assume these remain constant next year and forecast interest income.

<span class="jargon-unlock">**Weighted yield. What is it?** Total interest income divided by total average earning assets. **Volume-first bridge. What is it?** Change balance at the old rate, then change rate on the new balance: $\Delta I=(A_1-A_0)y_0+A_1(y_1-y_0)$, where $A$ denotes balances and $y$ yields. **Forecast. What is it?** A conditional estimate using stated future balances and rates.</span>

**1. Calculate the historical totals**

$$
\begin{aligned}
I_0&=600(0.07)+300(0.02)=48,\quad y_0=48/900=5.33\%\\
I_1&=700(0.06)+300(0.02)=48,\quad y_1=48/1{,}000=\boxed{4.80\%}
\end{aligned}
$$

Income stays at USD 48m while the bank commits more assets. More work, same paycheck.

**2. Explain the change and forecast separately**

Loan volume adds $100(0.07)=7$ million; the lower loan yield removes $700(0.06-0.07)=-7$ million. They offset exactly.

$$
I_{\text{forecast}}=750(0.062)+250(0.024)=\boxed{\text{USD }52.5\text{m}}
$$

This forecast uses the stated closing portfolio and forward rates, not last year’s average mix.

> [!NOTE]
> Do not take a simple average of category yields unless balances are equal. Rate-volume attribution also depends on the chosen bridge convention.

*Source pattern: 2025 CFA Level II FSA, LM4, pp.243–246, Exhibits 20–21. Inputs adapted for practice.*

---

## Variant: 17 — Liquidity coverage: buffer, shortfall, and implied days

**Abstract:** *Divide usable liquid assets by 30-day stressed net outflows. Convert to days only when a constant daily outflow assumption is explicitly supplied.*

> A bank has USD 360m of eligible high-quality liquid assets and USD 300m of 30-day stressed net cash outflows. Calculate LCR and the excess liquid-asset buffer. For illustration only, assume net outflows occur evenly each day with no replenishment. Find implied coverage days. If stressed net outflows rise 25%, how much additional eligible liquidity is needed to restore 100%?

<span class="jargon-unlock">**High-quality liquid assets (HQLA). What are they?** Eligible assets readily convertible to cash under the stress assumptions. **Liquidity coverage ratio (LCR). What is it?** $HQLA/NCO$, where $NCO$ is expected stressed net cash outflows over 30 days. **Buffer. What is it?** Eligible liquidity above the amount required at the specified threshold.</span>

**1. Measure coverage and spare liquidity**

$$
LCR=360/300=\boxed{120\%},\qquad
\text{Buffer}=360-300=\boxed{\text{USD }60\text{m}}
$$

At a constant USD 10m daily outflow, liquidity lasts $360/10=\boxed{36\text{ days}}$. Actual outflows rarely respect tidy classroom calendars.

**2. Apply the stronger stress**

$$
NCO_{\text{new}}=300(1.25)=375,\qquad
\text{Shortfall}=375-360=\boxed{\text{USD }15\text{m}}
$$

The new LCR is 96%. The initial buffer could absorb a 20% increase in net outflows, not a 25% increase.

> [!NOTE]
> The days conversion is a constant-runoff illustration, not a regulatory survival guarantee. LCR uses net outflows and puts HQLA in the numerator.

*Source pattern: 2025 CFA Level II FSA, LM4, pp.220, 247, Exhibit 22. Inputs adapted for practice.*

---

## Variant: 18 — A maturing reverse repo affects the cash-flow calculation

**Abstract:** *Use the eligible inflow specified in the question. A short maturity alone does not make a reverse repo an automatic addition to HQLA.*

> A bank has USD 240m eligible HQLA. Stressed cash outflows are USD 300m, eligible inflows before a transaction are USD 40m, and a required maturity-mismatch add-on is USD 10m. An existing reverse repo maturing within 30 days adds USD 30m of eligible inflow. HQLA stays unchanged. All figures already satisfy applicable caps and eligibility adjustments, with no double-counting. Calculate LCR before and after.

<span class="jargon-unlock">**Reverse repo. What is it?** A collateralized loan from the lender’s viewpoint. **HQLA. What is it?** Eligible high-quality liquid assets. **LCR. What is it?** HQLA divided by stressed net cash outflows. **Eligible inflow. What is it?** The amount permitted in the stress calculation after applicable rules. **Add-on. What is it?** An extra cash requirement included in the denominator here.</span>

**1. Assemble the original net outflow**

$$
NCO_0=300-40+10=270,\qquad
LCR_0=240/270=\boxed{88.89\%}
$$

**2. Include the qualifying cash receipt**

$$
NCO_1=300-(40+30)+10=240,\qquad
LCR_1=240/240=\boxed{100\%}
$$

The USD 30m receipt improves coverage by reducing the denominator. It is not also added to HQLA. Counting the same benefit in both places would make liquidity grow through creative bookkeeping.

The reading’s Q20 points to LCR as the relevant short-term measure, but its closing description reverses the fraction. Use the main chapter’s formula above. Detailed eligibility follows the [Basel LCR framework](https://www.bis.org/committees/bcbs/basel-framework/standard/lcr?allChapters=true).

> [!NOTE]
> A 30-day reverse repo is not automatically HQLA. Distinguish eligible inflows, usable collateral, and the liquid-asset stock; follow the problem’s specified treatment.

*Source pattern: 2025 CFA Level II FSA, LM4, pp.247, 276–277, 283; practice Q20. Inputs adapted for practice.*

---

## Variant: 19 — Weight the available stable funding

**Abstract:** *Funding that exists today is not all equally likely to stay. Apply each stability weight before comparing it with required stable funding.*

> A bank has USD 100m qualifying capital and long-term funding at a 100% ASF factor; USD 400m stable retail deposits at 95%; USD 200m less-stable retail deposits at 90%; USD 100m eligible corporate funding at 50%; and USD 100m other short funding at 0%. Required stable funding is USD 760m. Find NSFR and the gap to a stipulated 100% minimum. How much 0%-weighted funding must be replaced with 100%-weighted funding to close it?

<span class="jargon-unlock">**Available stable funding (ASF). What is it?** Funding balances multiplied by their supplied stability factors, then summed. **Required stable funding (RSF). What is it?** The stable funding needed for the asset and exposure mix. **Net stable funding ratio (NSFR). What is it?** $ASF/RSF$, a funding-structure measure over a one-year horizon.</span>

**1. Apply the factors**

$$
ASF=100+400(0.95)+200(0.90)+100(0.50)+100(0)=\boxed{710}
$$

All amounts are USD millions. The unweighted USD 900m funding total exaggerates the stable amount.

**2. Find the deficit and repair it**

$$
NSFR=710/760=\boxed{93.42\%},\qquad
\text{Gap}=760-710=\boxed{\text{USD }50\text{m}}
$$

Replacing USD 50m of the 0%-weighted funding with 100%-weighted funding adds USD 50m ASF without changing total funding or RSF. NSFR reaches 100%. Replacing 50%-weighted funding would require USD 100m for the same improvement.

> [!NOTE]
> The exercise uses 100% as the minimum, consistent with the reading’s later case and [Basel NSF20.2](https://www.bis.org/committees/bcbs/basel-framework/standard/nsf?allChapters=true). The early “greater than 100%” wording should not turn equality into a failure here.

*Source pattern: 2025 CFA Level II FSA, LM4, pp.220–221, Exhibit 8; p.248. Inputs adapted for practice.*

---

## Variant: 20 — A historical funding proxy is not regulatory NSFR

**Abstract:** *The reading’s unweighted case-study ratio is an approximation. Calculate it if requested, but preserve the label when comparing it with weighted NSFR.*

> For a historical-style proxy, a bank counts USD 500m deposits, USD 150m long-term debt, and USD 100m common equity as available funding. It counts USD 200m investments, USD 350m net loans, and USD 50m other non-liquid assets as required funding. Separately, its properly weighted ASF and RSF are USD 570m and USD 600m. Calculate both ratios and assess them against 100%.

<span class="jargon-unlock">**Proxy. What is it?** A simplified stand-in for a fuller calculation. **ASF/RSF. What do they mean?** Available stable funding and required stable funding after the applicable weighting rules. **NSFR. What is it?** $ASF/RSF$; the historical proxy uses unweighted selected balances instead.</span>

**1. Calculate the requested proxy**

$$
\text{Proxy}=\frac{500+150+100}{200+350+50}=\boxed{125\%}
$$

The proxy appears comfortable because it treats every selected funding dollar as equally stable.

**2. Use the weighted amounts for the proper ratio**

$$
NSFR=570/600=\boxed{95\%}
$$

The weighted measure is below 100%, with a USD 30m stable-funding shortfall. The proxy and the full calculation differ by 30 percentage points. A convenient shortcut has no obligation to preserve the conclusion.

The source’s 2016 case explicitly calls its unweighted calculation approximate. Its statement that NSFR was not yet required describes that historical setting, not a current implementation claim.

> [!NOTE]
> Do not present the case-study proxy as a regulatory calculation. Also do not assume every liquid asset has zero required funding under every rule.

*Source pattern: 2025 CFA Level II FSA, LM4, p.248, Exhibit 23. Inputs adapted for practice.*

---

## Variant: 21 — Funding concentration and a maturity shortfall

**Abstract:** *Even a solvent bank can lack cash when one large funder leaves. Match cash availability to payment dates rather than to eventual loan repayment.*

> A bank has USD 800m customer deposits, including USD 240m from one corporate customer. The customer withdraws USD 100m tomorrow. Available cash is USD 40m, and another USD 20m of loan receipts arrive tomorrow. Remaining loans will pay after 90 days. Calculate funding concentration, tomorrow’s gap, and the minimum additional same-day liquidity needed. Assume no other cash movements.

<span class="jargon-unlock">**Funding concentration. What is it?** Reliance on one source, here the largest customer’s deposits divided by total deposits. **Maturity mismatch. What is it?** Cash must be paid before corresponding assets generate cash. **Liquidity gap. What is it?** Required payments less cash available by that deadline. **Solvency. What is it?** Having sufficient asset value relative to obligations; it does not guarantee cash today.</span>

**1. Measure dependence on the customer**

$$
\text{Concentration}=240/800=\boxed{30\%}
$$

This customer provides almost one-third of the deposit base. Many accounts do not imply diversified funding if one account is doing the heavy lifting.

**2. Respect tomorrow’s deadline**

$$
\text{Gap}=100-(40+20)=\boxed{\text{USD }40\text{m}}
$$

The bank needs at least USD 40m of additional usable liquidity tomorrow. Loans paying in 90 days do not meet tomorrow’s withdrawal unless they can be monetized in time, which this question does not assume. Raising capital helps only if it also delivers usable cash by the deadline.

> [!NOTE]
> Capital adequacy and liquidity are separate tests. Future receipts and today’s obligations must be matched by timing, not optimism.

*Source pattern: 2025 CFA Level II FSA, LM4, pp.221–222, Example 5; bank funding characteristics. Inputs adapted for practice.*

---

## Variant: 22 — High short-term liquidity, weak long-term funding

**Abstract:** *LCR and NSFR cover different problems. Rank each separately; a spectacular result on one does not cancel failure on the other.*

> Entity A has USD 250m eligible HQLA, USD 100m stressed 30-day net outflows, USD 490m available stable funding, and USD 1,000m required stable funding. Entity B has USD 160m, USD 100m, USD 810m, and USD 500m, respectively. Calculate both ratios, identify each leader, and find A’s stable-funding gap to 100% at unchanged RSF.

<span class="jargon-unlock">**LCR. What is it?** Liquidity coverage ratio: eligible high-quality liquid assets (HQLA) divided by 30-day stressed net outflows. **NSFR. What is it?** Net stable funding ratio: available stable funding (ASF) divided by required stable funding (RSF), addressing the funding structure over a one-year horizon.</span>

**1. Keep the two scoreboards separate**

$$
\begin{array}{c|cc}
&\text{Entity A}&\text{Entity B}\\
LCR&250/100=\boxed{250\%}&160/100=160\%\\
NSFR&490/1{,}000=49\%&810/500=\boxed{162\%}
\end{array}
$$

A leads on near-term stress liquidity; B leads on stable funding. Both pass the stipulated 100% LCR threshold, while A fails the NSFR threshold.

**2. Quantify the funding repair**

$$
\text{A's ASF gap}=1{,}000-490=\boxed{\text{USD }510\text{m}}
$$

That is the required increase in weighted ASF if RSF remains fixed. It is not necessarily USD 510m of any arbitrary new deposit: funding weights and use of proceeds matter.

> [!NOTE]
> A high LCR cannot prove a strong NSFR. Nor do consolidated ratios prove that liquidity can move freely between legal entities.

*Source pattern: 2025 CFA Level II FSA, LM4, Example 5, pp.222–224. Inputs adapted for practice.*

---

## Variant: 23 — Repricing exposure and asymmetric interest-rate scenarios

**Abstract:** *Near-term earnings depend on which balances reprice and when. Use a disclosed scenario as a complete scenario; do not multiply an annual impact by four.*

> For a simple one-year shock, USD 600m of assets and USD 450m of liabilities reprice immediately by +1 percentage point for the full year. All other balances and rates stay fixed. Find the NII change. Separately, a bank’s model reports annual NII changes of +USD 17m and −USD 24m for paths with +25 bp and −25 bp at the start of each of four quarters. Base annual NII is USD 300m. Find each scenario’s NII and the downside/upside magnitude ratio.

<span class="jargon-unlock">**Repricing. What is it?** Resetting the rate earned or paid. **NII. What is it?** Net interest income, interest received minus interest expense. **Basis point (bp). What is it?** 0.01 percentage point. **Repricing gap. What is it?** Assets minus liabilities exposed to the specified reset. **Scenario. What is it?** A complete assumed path, including timing.</span>

**1. Calculate the simple immediate-reset effect**

$$
\Delta NII=(600-450)(0.01)=\boxed{\text{USD }1.5\text{m}}
$$

More assets than liabilities receive the rate increase for the full year, so NII rises under these assumptions.

**2. Read the model output literally**

$$
NII_{\text{up}}=300+17=\boxed{317},\qquad
NII_{\text{down}}=300-24=\boxed{276}
$$

Amounts are USD millions. Downside magnitude is $24/17=\boxed{1.41\text{ times}}$ upside. The model already incorporates four quarterly shocks. Multiplying its annual result by four would count the scenario four times.

> [!NOTE]
> Do not assume rate sensitivities are symmetric or extrapolate a static table to a new balance-sheet strategy. A yield-curve inversion can squeeze banks funding long assets with short liabilities.

*Source pattern: 2025 CFA Level II FSA, LM4, Example 6; pp.224–225, 242–246; practice Q19. Inputs adapted for practice.*

---

## Variant: 24 — Value at risk: diversification without a worst-case promise

**Abstract:** *Apply the disclosed diversification adjustments at the correct aggregation level. VaR is a percentile loss threshold, not a cap on possible damage.*

> A bank reports one-day 99% VaR: interest-rate risk USD 40m, credit-spread risk USD 50m, and their covariance adjustment −USD 20m. Add FX USD 25m, equity USD 15m, commodity USD 10m, and a further cross-risk adjustment −USD 30m. An additional credit portfolio increases aggregate VaR by USD 12m. Annual net income is USD 10,000m and equity USD 100,000m. Calculate aggregate VaR and its size relative to both.

<span class="jargon-unlock">**Value at risk (VaR). What is it?** A modeled loss threshold exceeded with the stated tail probability over the stated horizon; here 1% over one day. **Covariance adjustment. What is it?** A supplied adjustment reflecting risks not moving perfectly together. **FX. What is it?** Foreign exchange. **Incremental credit-portfolio VaR. What is it?** The extra risk after adding that portfolio, not its stand-alone VaR.</span>

**1. Aggregate in the disclosed order**

$$
\begin{aligned}
\text{Rate and spread VaR}&=40+50-20=70\\
\text{Trading VaR}&=70+25+15+10-30=90\\
\text{Trading plus credit VaR}&=90+12=\boxed{\text{USD }102\text{m}}
\end{aligned}
$$

**2. Compare magnitudes without confusing horizons**

$$
102/10{,}000=\boxed{1.02\%},\qquad
102/100{,}000=\boxed{0.102\%}
$$

These compare a daily risk measure with annual income and a point-in-time equity stock. They do not turn VaR into an annual loss forecast. Losses beyond USD 102m remain possible.

> [!NOTE]
> The source’s “worst-case” wording is not a sound definition of VaR. Tail losses can exceed VaR, and different banks’ models may not be comparable.

*Source pattern: 2025 CFA Level II FSA, LM4, pp.249–250, Exhibit 24. Inputs adapted for practice.*

---

## Variant: 25 — Trading revenue per unit of reported risk

**Abstract:** *Recover trading revenue by multiplying the risk metric by the reported multiple. Compare changes within the same model before making cross-bank claims.*

> A bank’s annual trading revenue/average daily VaR rises from 120 times to 150 times. Average daily VaR falls from USD 10m to USD 9m. The bank uses an unchanged VaR methodology. Calculate trading revenue in both years and growth in revenue, VaR, and revenue per unit of VaR. Can these data prove that it is safer than another bank?

<span class="jargon-unlock">**Average daily VaR. What is it?** The period’s average of modeled daily loss thresholds under specified confidence assumptions. **Reward-to-risk multiple. What is it?** Here $R/V$, with annual trading revenue $R$ and average daily VaR $V$. It is a comparison metric, not a conventional annual return percentage.</span>

**1. Reverse the ratio**

$$
R_0=120(10)=\boxed{\text{USD }1{,}200\text{m}},\qquad
R_1=150(9)=\boxed{\text{USD }1{,}350\text{m}}
$$

**2. Separate the two contributors**

Revenue rises $1{,}350/1{,}200-1=12.50\%$. Average daily VaR falls 10%. The multiple improves $150/120-1=\boxed{25.00\%}$ because the numerator rises while the denominator falls.

This indicates improved revenue per unit of reported risk within this bank’s unchanged measurement system. Another bank may use different positions, models, horizons, or confidence levels. Comparing the headline multiples alone could reward the more flattering ruler.

> [!NOTE]
> Do not multiply daily VaR by trading days to invent an annual denominator. VaR is not an expected daily expense or maximum daily loss.

*Source pattern: 2025 CFA Level II FSA, LM4, practice Q17; pp.249–250. Inputs adapted for practice.*

---

## Variant: 26 — Derivative notional is not the loss in earnings

**Abstract:** *For a freestanding derivative, the period’s fair-value change affects earnings. The notional is a reference amount, not the amount lost.*

> A bank’s freestanding credit-derivative notional falls from USD 20bn to USD 5bn. Separately, a remaining derivative asset falls in fair value from USD 80m to USD 50m during the year, with no settlements or other changes. It does not qualify for hedge accounting. Tax is 25%. Find the notional reduction, pretax and after-tax earnings effects, and explain what cannot be inferred about risk.

<span class="jargon-unlock">**Notional. What is it?** A contract’s reference amount used to determine payments. **Fair value. What is it?** The contract’s measured value at the reporting date. **Freestanding derivative. What is it?** A derivative not designated for qualifying hedge accounting in this question. **Mark-to-market change. What is it?** The change in measured fair value during the period.</span>

**1. Measure the exposure-scale change**

$$
\text{Notional reduction}=1-5/20=\boxed{75\%}
$$

A smaller position may reduce exposure, but the percentage change in notional is not a percentage change in risk. Terms, maturities, counterparties, and offsets matter.

**2. Calculate the actual valuation loss**

$$
\Delta FV=50-80=\boxed{-\text{USD }30\text{m}}
$$

The loss reduces pretax income by USD 30m and after-tax income by $30(1-0.25)=\boxed{\text{USD }22.5\text{m}}$. The asset is still positive at USD 50m; a fall in an asset does not automatically turn it into a liability.

> [!NOTE]
> Notional, fair value, and earnings change are three different quantities. Do not treat a USD 15bn notional reduction as a USD 15bn accounting gain.

*Source pattern: 2025 CFA Level II FSA, LM4, pp.246–247; practice Q18. Inputs adapted for practice.*

---

## Variant: 27 — Weighted CAMELS: the denominator has a job too

**Abstract:** *Weight each component and divide by total weights. Lower scores are better, but a tidy composite cannot erase an unmeasured risk.*

> An analyst assigns CAMELS scores of 1 for capital, 3 for asset quality, 2 for management, 4 for earnings, 1 for liquidity, and 1 for sensitivity. Scores run from 1 best to 5 worst. Calculate an equal-weighted average and an average giving asset quality and earnings twice the weight of each other component. Should either score settle concerns about intense competition or government support?

<span class="jargon-unlock">**CAMELS. What is it?** A bank-analysis framework covering Capital adequacy, Asset quality, Management, Earnings, Liquidity, and Sensitivity to market risk. **Weighted mean. What is it?** $\sum w_is_i/\sum w_i$, where $s_i$ is each score and $w_i$ its assigned weight. These are analyst-specified weights, not a mandatory supervisory formula.</span>

**1. Establish the equal-weighted score**

$$
\text{Equal-weighted score}=\frac{1+3+2+4+1+1}{6}=\boxed{2.00}
$$

**2. Apply the analyst’s priorities**

$$
\text{Weighted score}=\frac{1+2(3)+2+2(4)+1+1}{1+2+1+2+1+1}=\boxed{2.375}
$$

The weaker asset-quality and earnings scores receive more emphasis, so the result worsens. Dividing the weighted sum of 19 by six would be wrong; there are eight units of weight.

Competition, government support, business mission, culture, and other relevant exposures still need separate analysis. The composite is a summary, not a certificate of invincibility.

> [!NOTE]
> The source’s Exhibit 26 uses a weighted denominator of eight despite a row label saying “divided by 6.” Follow the weighted calculation, not that misleading label.

*Source pattern: 2025 CFA Level II FSA, LM4, pp.209, 226–230, 251–252; practice Q3, Q13. Inputs adapted for practice.*

---

## Variant: 28 — Premiums written versus premiums earned

**Abstract:** *Writing the policy records business sold; earning the premium follows the coverage period. Collecting the cash does not fast-forward the calendar.*

> On 1 October, an insurer writes one-year policies with direct premiums of USD 120m and cedes USD 24m of premiums to a reinsurer. Coverage is earned evenly, and there is no other business or opening unearned premium balance. Calculate net premiums written, net premiums earned by 31 December, and closing net unearned premiums.

<span class="jargon-unlock">**Premium. What is it?** The price of insurance coverage. **Ceded premium. What is it?** Premium transferred to another insurer in exchange for reinsurance protection. **Net premiums written. What are they?** Here, direct premiums less ceded premiums. **Earned premium. What is it?** The portion relating to coverage already provided. **Unearned premium. What is it?** The portion relating to future coverage.</span>

**1. Remove the ceded business**

$$
\text{Net written}=120-24=\boxed{\text{USD }96\text{m}}
$$

The company retains 80% of the premium; use the retained amount consistently for both earned and unearned figures.

**2. Recognize only three months of coverage**

$$
\text{Net earned}=96(3/12)=\boxed{\text{USD }24\text{m}}
$$

Closing net unearned premiums are $96-24=\boxed{\text{USD }72\text{m}}$. The check is USD 24m earned plus USD 72m unearned equals USD 96m written. Premium cash may arrive on day one; the insurer’s obligation does not finish on day one.

> [!NOTE]
> Use the written or earned denominator specified by each ratio. This is the reading’s simple premium-earning illustration, not a full insurance revenue measurement model.

*Source pattern: 2025 CFA Level II FSA, LM4, pp.255–257. Inputs adapted for practice.*

---

## Variant: 29 — The combined ratio and its two denominators

**Abstract:** *Use earned premiums for losses and written premiums for underwriting expenses under the reading’s convention. Then add the percentages, not the denominators.*

> A property and casualty insurer has net premiums earned USD 500m, net premiums written USD 550m, loss expense USD 290m, loss-adjustment expense USD 30m, underwriting expenses USD 165m, and policyholder dividends USD 15m. Calculate loss, expense, combined, dividend, and combined-after-dividend ratios using the reading’s convention.

<span class="jargon-unlock">**Loss adjustment expense. What is it?** Costs of investigating and settling claims. **Underwriting expense. What is it?** Costs of obtaining and administering insurance business. **Earned/written premiums. What are they?** Coverage revenue recognized/business sold. **Combined ratio. What is it?** $(L+LAE)/E+U/W$, with loss $L$, adjustment expense $LAE$, earned premiums $E$, underwriting expense $U$, and written premiums $W$.</span>

**1. Calculate the components separately**

$$
\text{Loss ratio}=\frac{290+30}{500}=\boxed{64\%},\qquad
\text{Expense ratio}=165/550=\boxed{30\%}
$$

The combined ratio is $64\%+30\%=\boxed{94\%}$. The loss ratio reflects claims relative to coverage revenue; the expense ratio reflects spending relative to written business.

**2. Include the dividend convention**

$$
\text{Dividend ratio}=15/500=3\%,\qquad
\text{Combined after dividends}=94\%+3\%=\boxed{97\%}
$$

Both combined measures are below 100%. However, because the expense ratio uses written premiums, multiplying $1-94\%$ by earned premiums does not necessarily reconstruct dollar underwriting profit.

> [!NOTE]
> Companies may use an earned-premium expense denominator instead. State the convention. The source’s dividend-inclusive measure must not turn shareholder dividends into an income-statement underwriting expense.

*Source pattern: 2025 CFA Level II FSA, LM4, pp.255–258, Exhibit 29; practice Q4, Q6. Inputs adapted for practice.*

---

## Variant: 30 — An underwriting loss can coexist with an overall profit

**Abstract:** *When both components use earned premiums, the combined ratio translates directly into underwriting margin. Investment income is a separate source of profit.*

> An insurer explicitly uses earned premiums for both components of its combined ratio. Earned premiums are USD 500m, losses including adjustment expenses USD 340m, and underwriting expenses USD 180m. Net investment income is USD 35m. Ignore all other income, expenses, dividends, and tax. Find the combined ratio, underwriting result, and overall pretax profit.

<span class="jargon-unlock">**Underwriting result. What is it?** Premiums earned minus incurred claim costs and underwriting expenses. **Combined ratio. What is it?** Here $(L+U)/E$, with claims including adjustment expenses $L$, underwriting expenses $U$, and earned premiums $E$. **Float. What is it?** Funds held between collecting premiums and paying claims; investing them can generate income.</span>

**1. Evaluate the insurance operation**

$$
CR=(340+180)/500=\boxed{104\%}
$$

The insurer spends USD 1.04 on underwriting costs for each USD 1 of earned premium.

$$
\text{Underwriting result}=500-340-180=\boxed{-\text{USD }20\text{m}}
$$

**2. Add investment income separately**

Overall pretax profit is $-20+35=\boxed{\text{USD }15\text{m}}$. The investment portfolio pays the underwriting department’s bill this year. That does not make the underwriting result profitable or guarantee the arrangement will keep working.

> [!NOTE]
> Combined ratio above 100% signals an underwriting loss under this common-denominator setup. It does not imply an overall company loss after investment income.

*Source pattern: 2025 CFA Level II FSA, LM4, pp.253–255, 257–259. Inputs adapted for practice.*

---

## Variant: 31 — Read ratio trends and solve the premium needed

**Abstract:** *A lower combined ratio can hide a higher acquisition-cost ratio. For a target ratio, solve the stated equation backward instead of guessing a price increase.*

> An insurer’s loss ratio falls from 62% to 59%, while its underwriting expense ratio rises from 35% to 37%. Its dividend ratio rises from 2% to 3%. Calculate combined ratios before and after dividends. Separately, forecast claim costs including adjustment expenses of USD 330m and underwriting expenses USD 180m; assume written premiums equal earned premiums. What premium volume achieves a 95% combined ratio, and what increase is needed from USD 500m?

<span class="jargon-unlock">**Loss ratio. What is it?** Incurred claim costs divided by earned premiums. **Expense ratio. What is it?** Underwriting expenses divided by the specified premium base. **Dividend ratio. What is it?** Specified dividends divided by earned premiums. **Target premium. What is it?** With equal premium bases, $P=(L+U)/c$, where costs are $L,U$ and target combined ratio $c$ is a decimal.</span>

**1. Separate the operational signals**

Combined ratio falls from $62\%+35\%=97\%$ to $59\%+37\%=\boxed{96\%}$. Claims performance improves while expense efficiency worsens. After dividends, both years equal $\boxed{99\%}$.

**2. Solve the target equation**

$$
P=\frac{330+180}{0.95}=\boxed{\text{USD }536.84\text{m}}
$$

Required growth from USD 500m is $536.842105/500-1=\boxed{7.37\%}$. This holds claim costs and underwriting expenses fixed. If growth changes the cost base, the target must be recalculated; more policies do not arrive expense-free.

> [!NOTE]
> Lower combined ratio does not mean every component improved. The inverse premium shortcut requires the stated common denominator and fixed costs.

*Source pattern: 2025 CFA Level II FSA, LM4, pp.254–258; practice Q15. Inputs adapted for practice.*

---

## Variant: 32 — Roll forward insurance reserves from gross to net and back

**Abstract:** *Start net of reinsurance, add incurred claim costs, subtract payments, and include other movements. Add closing recoverables back only when returning to gross reserves.*

> Opening gross claim reserves are USD 1,000m and reinsurance recoverables USD 200m. Current-year incurred claims including adjustment costs are USD 350m. Prior-year estimates are revised downward by USD 30m. Cash claim payments total USD 300m. An acquisition adds USD 10m of net reserves, and currency translation reduces net reserves by USD 5m. Closing reinsurance recoverables are USD 180m. Find closing net and gross reserves.

<span class="jargon-unlock">**Reserve. What is it?** A liability estimate for unpaid insurance claims. **Reinsurance recoverable. What is it?** Amount expected from another insurer. **Net reserve. What is it?** Gross reserve minus recoverables for this analysis. **Incurred claims. What are they?** Claim costs recognized during the period, including estimate changes, whether paid or unpaid. **Reserve release. What is it?** A downward revision of earlier estimates.</span>

**1. Begin with the net obligation**

Opening net reserves are $1{,}000-200=800$ million. The downward revision reduces claim expense and the liability.

$$
\text{Closing net}=800+350-30-300+10-5=\boxed{\text{USD }825\text{m}}
$$

**2. Rebuild the gross liability**

$$
\text{Closing gross}=825+180=\boxed{\text{USD }1{,}005\text{m}}
$$

The net balance increases USD 25m, while the gross balance increases only USD 5m because recoverables fall USD 20m. The period’s claim expense is USD 320m, not USD 300m of cash payments or USD 25m of reserve growth.

> [!NOTE]
> Reserve change includes payments and possibly acquisitions or currency effects. Do not equate the change in reserves with claims expense.

*Source pattern: 2025 CFA Level II FSA, LM4, pp.255–257, Exhibit 28. Inputs adapted for practice.*

---

## Variant: 33 — Reserve releases and the quality of insurance earnings

**Abstract:** *A reserve release reduces expense and raises profit. Measure its contribution before deciding how much reported profitability came from this year’s business.*

> An insurer reports pretax profit USD 150m including a USD 30m release of prior-year claim reserves. Current-year incurred claim costs are USD 350m, of which USD 140m is paid this year. Total reported expenses are USD 500m, including net claim expense of USD 320m. Tax is 25%. Find release-adjusted profit, the release’s contribution to pretax profit, the current-year payment share, and claims’ share of total expenses.

<span class="jargon-unlock">**Reserve release. What is it?** Reducing an earlier estimate of unpaid claims, which lowers current expense. **Release-adjusted profit. What is it?** Reported profit less that benefit, a stated analytical comparison. **Incurred claims. What are they?** Recognized claim costs, not just payments. **Payment share. What is it?** Payments on current-year claims divided by costs incurred for those claims.</span>

**1. Remove the estimate benefit**

$$
\text{Adjusted pretax profit}=150-30=\boxed{\text{USD }120\text{m}},\qquad
\text{Release share}=30/150=\boxed{20\%}
$$

After tax, reported profit is USD 112.5m and adjusted profit USD 90m, a USD 22.5m difference.

**2. Read claims expense and timing separately**

Current-year payment share is $140/350=\boxed{40\%}$. Reported claim expense equals $350-30=320$ million and represents $320/500=\boxed{64\%}$ of total expenses.

The unpaid 60% of current-year incurred claims remains an obligation estimate. The release concerns prior years; mixing those two stories makes current claims look cheaper than they were.

> [!NOTE]
> A reserve release may reflect genuinely conservative past estimates or aggressive current revisions. The ratio identifies earnings dependence, not intent.

*Source pattern: 2025 CFA Level II FSA, LM4, pp.255–257, Exhibit 28. Inputs adapted for practice.*

---

## Variant: 34 — Reinsurance reduces retained exposure, not the policyholder’s claim

**Abstract:** *Measure the portion recoverable from reinsurers and the portion retained. If the reinsurer cannot pay, the original obligation may remain.*

> An insurer has USD 900m gross claim reserves and USD 225m recoverables from reinsurers. The insurer remains responsible to policyholders for gross claims. For an analytical stress, assume only 80% of recoverables will be collected, with no change in gross claims. Find the ceded share, normal net exposure, stressed net exposure, and increase in retained exposure. Ignore tax.

<span class="jargon-unlock">**Reinsurance. What is it?** Insurance purchased by an insurer to transfer part of its risk. **Ceded share. What is it?** Here, recoverables divided by gross claim reserves. **Counterparty risk. What is it?** Risk that the reinsurer fails to pay. **Retained exposure. What is it?** Gross obligations less amounts expected to be recovered.</span>

**1. Measure the normal split**

$$
\text{Ceded share}=225/900=\boxed{25\%},\qquad
\text{Net exposure}=900-225=\boxed{\text{USD }675\text{m}}
$$

**2. Stress the recovery, not the policyholder obligation**

$$
\text{Stressed net}=900-225(0.80)=\boxed{\text{USD }720\text{m}}
$$

Expected recovery falls by USD 45m, so net exposure rises by $45/675=\boxed{6.67\%}$. Gross claims remain USD 900m. The customer did not agree to receive less because the insurer chose an unreliable insurer of its own.

> [!NOTE]
> Reinsurance transfers risk but introduces dependence on the reinsurer. Keep gross obligations, recoverables, and net analytical exposure distinct.

*Source pattern: 2025 CFA Level II FSA, LM4, pp.253, 255–256; reinsurance exposure in Exhibit 28. Inputs adapted for practice.*

---

## Variant: 35 — Investment allocation and fair-value hierarchy

**Abstract:** *Use portfolio totals for allocation, and the disclosed measured subset for hierarchy shares. Model dependence is a warning to investigate, not a mechanical liquidity verdict.*

> An insurer invests USD 600m in bonds, USD 80m in equities, USD 20m in property, and USD 100m in short-term securities. A fair-value hierarchy disclosure covers only the bonds and equities: Level 1 USD 90m, Level 2 USD 570m, Level 3 USD 20m. Find allocation percentages and hierarchy percentages. Is Level 2 automatically illiquid?

<span class="jargon-unlock">**Fair-value hierarchy. What is it?** Classification by valuation inputs. **Level 1. What is it?** Quoted prices for identical instruments in active markets. **Level 2. What is it?** Other observable inputs. **Level 3. What is it?** Significant unobservable inputs requiring estimates. **Portfolio weight. What is it?** Asset-class amount divided by the relevant portfolio total.</span>

**1. Calculate the investment mix**

Total investments are USD 800m. Bonds, equities, property, and short-term securities represent $\boxed{75\%,\ 10\%,\ 2.5\%,\ 12.5\%}$, respectively. The shares sum to 100%.

**2. Change the denominator for the hierarchy subset**

The disclosed subset totals $600+80=680$ million.

$$
\begin{aligned}
L1&=90/680=\boxed{13.24\%}\\
L2&=570/680=\boxed{83.82\%}\\
L3&=20/680=\boxed{2.94\%}
\end{aligned}
$$

Level 2 dominates, but that does not establish illiquidity. Observable pricing inputs can support valuations of securities that do not trade every day. Actual liquidity requires evidence about markets, trading conditions, and saleability.

> [!NOTE]
> Do not divide hierarchy amounts by a broader asset total unless that is explicitly the requested measure. Valuation observability and cash liquidity are related but distinct.

*Source pattern: 2025 CFA Level II FSA, LM4, pp.217–218, 258–260, Exhibits 30–31; Example 8 allocation. Inputs adapted for practice.*

---

## Variant: 36 — Investment returns: match income to the assets that earned it

**Abstract:** *Use average invested balances and keep the asset class consistent. Separate recurring income from gains so a good market year does not impersonate a higher yield.*

> An insurer begins with USD 900m bonds and USD 100m loans/deposits, ending with USD 1,000m and USD 120m. Annual interest income is USD 48m; fixed-income realized gains USD 5m; fixed-income unrealized gains USD 3m. Separately it earns USD 6m dividends and USD 2m rent. Calculate fixed-income returns from income alone, with realized gains, and with all gains. For this question, fixed income includes bonds and loans/deposits.

<span class="jargon-unlock">**Average invested assets. What are they?** Here, beginning plus ending balances divided by two. **Realized gain. What is it?** Gain recognized on disposal. **Unrealized gain. What is it?** A value increase on holdings not sold. **Return measure. What is it?** The chosen income-and-gain numerator divided by the matching average invested assets; this is a simple accounting yield estimate.</span>

**1. Build the matching asset base**

$$
\text{Average fixed income}=\frac{(900+100)+(1{,}000+120)}{2}=\boxed{\text{USD }1{,}060\text{m}}
$$

Dividends and rent belong to other asset classes, so they do not enter this fixed-income numerator.

**2. Show how gains change the result**

$$
\begin{aligned}
\text{Income only}&=48/1{,}060=\boxed{4.53\%}\\
\text{Including realized gains}&=53/1{,}060=\boxed{5.00\%}\\
\text{Including all gains}&=56/1{,}060=\boxed{5.28\%}
\end{aligned}
$$

The difference between 4.53% and 5.28% comes from gains, not a higher interest payment on the same assets.

> [!NOTE]
> Use the question’s income definition and average matching assets. This simplified accounting return does not claim to be a cash-flow-adjusted time-weighted portfolio return.

*Source pattern: 2025 CFA Level II FSA, LM4, pp.259, 266–267, Example 8. Inputs adapted for practice.*

---

## Variant: 37 — Life-insurer revenue diversification: mix versus growth

**Abstract:** *A premium share can rise because other revenue collapses. Calculate both the common-size mix and year-on-year growth before calling it a stronger franchise.*

> Life insurer A earns USD 700m premiums, USD 200m investment income, and USD 100m fees in Year 1. Year 2 has USD 714m, USD 140m, and USD 96m. Insurer B’s Year 2 mix is USD 600m premiums, USD 200m investment income, and USD 200m fees. Compare premium shares, A’s revenue growth, and diversification. Does B’s more even mix automatically mean better-quality earnings?

<span class="jargon-unlock">**Premium income. What is it?** Recognized revenue from insurance coverage. **Common-size mix. What is it?** Each income source divided by total revenue. **Year-on-year growth. What is it?** $(\text{current}/\text{previous})-1$. **Diversification. What is it?** Spreading dependence across sources whose risks may differ.</span>

**1. Calculate the totals and premium shares**

A’s total revenue falls from USD 1,000m to USD 950m. Its premium share rises from 70% to $714/950=\boxed{75.16\%}$. B’s premium share is $600/1{,}000=\boxed{60\%}$.

**2. Explain A’s changing mix**

$$
\begin{aligned}
\text{Premium growth}&=714/700-1=2\%\\
\text{Investment-income growth}&=140/200-1=-30\%\\
\text{Fee growth}&=96/100-1=-4\%\\
\text{Total revenue growth}&=950/1{,}000-1=\boxed{-5\%}
\end{aligned}
$$

A’s greater premium concentration comes mainly from weaker other income. B is more evenly distributed across these sources, but investment income can be more variable than premiums. More categories do not automatically buy more stability.

> [!NOTE]
> Distinguish diversification from earnings quality. A percentage share can improve because the rest of the denominator is having a terrible year.

*Source pattern: 2025 CFA Level II FSA, LM4, Example 7, pp.262–264. Inputs adapted for practice.*

---

## Variant: 38 — Life-insurer benefits and expense ratios

**Abstract:** *Use premiums plus deposits when the specified operating ratio calls for both. Do not turn product deposits into accounting revenue merely because they enter an analytical denominator.*

> A life insurer has net premiums written USD 800m, policyholder deposits USD 200m, benefits paid USD 650m, and commissions plus operating expenses incurred USD 180m. Total accounting revenue is USD 900m, pretax operating profit USD 90m, and tax on operating profit is 25%. Find the benefits ratio, commission-and-expense ratio, and pre- and post-tax operating margins.

<span class="jargon-unlock">**Policyholder deposit. What is it?** A contribution to an investment-type insurance product; it is not necessarily premium revenue. **Benefits ratio. What is it?** Benefits paid divided by net premiums written plus deposits. **Commission-and-expense ratio. What is it?** Those incurred expenses divided by the same base. **Operating margin. What is it?** Operating profit divided by accounting revenue.</span>

**1. Use the operating-ratio base**

$$
\text{Base}=800+200=1{,}000,\quad
\text{Benefits ratio}=650/1{,}000=\boxed{65\%}
$$

The commission-and-expense ratio is $180/1{,}000=\boxed{18\%}$. Using premiums alone would produce 81.25% and 22.50%, answering a different question.

**2. Switch to revenue for profit margins**

$$
\text{Pretax margin}=90/900=\boxed{10\%},\qquad
\text{Post-tax margin}=90(0.75)/900=\boxed{7.50\%}
$$

The benefits and expense ratios sum to 83%, but the remaining 17% is not an accounting profit margin. Their base includes deposits and their numerators mix cash benefits with incurred expenses.

> [!NOTE]
> Each ratio brings its own denominator and accounting basis. Do not force these L&H measures into a P&C combined-ratio identity.

*Source pattern: 2025 CFA Level II FSA, LM4, p.265, L&H profitability measures. Inputs adapted for practice.*

---

## Variant: 39 — ROE, ROA, and book value without denominator drift

**Abstract:** *Use average capital for period returns and closing shares for closing book value. Distinguish operating profit from reported net income.*

> An insurer has beginning and ending common equity of USD 400m and USD 500m, assets of USD 4,000m and USD 4,400m, net income attributable to common shareholders USD 36m, and comparable pretax operating profit USD 54m. Closing common shares are 50m; opening common shares were also 50m. Find ROE, ROA, pretax operating ROE, closing book value per share, and equity growth. Use simple averages and no minority or preferred interests.

<span class="jargon-unlock">**ROE/ROA. What are they?** Return on equity/assets: the specified period income divided by average equity/assets. **Operating ROE. What is it?** Operating profit divided by average equity, using the stated tax basis. **Book value per share. What is it?** Common equity divided by common shares outstanding. **Average. What is it?** Here, the mean of beginning and ending balances.</span>

**1. Match period income with average balances**

Average equity is USD 450m; average assets are USD 4,200m.

$$
ROE=36/450=\boxed{8\%},\quad
ROA=36/4{,}200=\boxed{0.86\%},\quad
ROE_{\text{operating, pretax}}=54/450=\boxed{12\%}
$$

The 12% and 8% measures differ in both profit definition and tax basis; the gap is not automatically all tax.

**2. Measure the closing capital position**

$$
BVPS=500/50=\boxed{\text{USD }10},\qquad
\text{Equity growth}=500/400-1=\boxed{25\%}
$$

Opening book value per share was USD 8. The USD 100m equity increase exceeds USD 36m net income, so other equity movements must exist; do not describe the entire increase as retained profit.

> [!NOTE]
> Ending equity measures the closing position; average equity supports the stated return calculation. Comparing companies requires consistent income and denominator definitions.

*Source pattern: 2025 CFA Level II FSA, LM4, p.265, Exhibit 34 and general L&H profitability measures. Inputs adapted for practice.*

---

## Variant: 40 — Duration mismatch: what happens to the insurer’s surplus?

**Abstract:** *Compare the dollar sensitivity of assets and liabilities, not durations alone. Surplus changes by the asset-value change minus the liability-value change.*

> An insurer has assets worth USD 1,000m with modified duration 5 and liabilities worth USD 900m with modified duration 7. Approximate the effect of a parallel 1-percentage-point rise in yields on assets, liabilities, and economic surplus. Ignore convexity, cash flows, and changes in credit spreads. Repeat the surplus direction for an equally sized fall.

<span class="jargon-unlock">**Modified duration. What is it?** Approximate proportional price sensitivity: $\Delta V\approx-DV\Delta y$, where $D$ is modified duration, $V$ the value, and $\Delta y$ the yield change in decimals. **Economic surplus. What is it?** Market value of assets minus market value of liabilities. **Convexity. What is it?** Curvature that the first-order duration approximation ignores.</span>

**1. Translate duration into money sensitivity**

$$
\Delta A\approx-5(1{,}000)(0.01)=-50,\qquad
\Delta L\approx-7(900)(0.01)=-63
$$

Amounts are USD millions. Both values fall, but liabilities fall more.

**2. Calculate the surplus change**

$$
\Delta S=\Delta A-\Delta L=-50-(-63)=\boxed{+\text{USD }13\text{m}}
$$

Initial surplus is USD 100m; estimated new surplus is USD 113m. Under an equally sized fall, the first-order surplus change is −USD 13m, leaving USD 87m. Rising bond prices do not necessarily help when the liabilities rise faster.

> [!NOTE]
> This instantiates the reading’s asset–liability duration comparison with the stated linear approximation. Economic value changes need not equal reported accounting earnings.

*Source pattern: 2025 CFA Level II FSA, LM4, p.266, interest-rate risk of L&H investment portfolios. Inputs adapted for practice.*

---

## Variant: 41 — Life-insurer liquidity under surrender stress

**Abstract:** *Adjust asset sale values and withdrawal obligations for the same scenario. A normal-times surplus can disappear when sales get harder and withdrawals accelerate.*

> A life insurer has USD 50m cash, USD 200m marketable bonds, and USD 100m less-liquid investments. Normal liquidity weights are 100%, 95%, and 50%; stress weights are 100%, 80%, and 20%. Normal cash needs are USD 100m benefits plus USD 80m surrenders. Stress needs are USD 100m benefits plus USD 200m surrenders. Find adjusted liquidity coverage and surplus or shortfall in each case. Assume no other inflows.

<span class="jargon-unlock">**Surrender. What is it?** A policyholder’s early cancellation generating a contractual payout. **Liquidity weight. What is it?** The assumed fraction of an asset realizable in cash for this model. **Adjusted coverage. What is it?** Scenario-adjusted available assets divided by scenario cash needs. This is a specified insurer model, not a bank LCR.</span>

**1. Calculate normal coverage**

$$
A_N=50+200(0.95)+100(0.50)=290,\qquad
\text{Coverage}_N=290/180=\boxed{161.11\%}
$$

Normal liquidity surplus is USD 110m.

**2. Stress both sides**

$$
A_S=50+200(0.80)+100(0.20)=230,\qquad
\text{Coverage}_S=230/300=\boxed{76.67\%}
$$

The stress shortfall is $300-230=\boxed{\text{USD }70\text{m}}$. Liquidity falls as assets become harder to sell at favorable prices and policyholders demand more cash. A normal-times ratio was not a promise about the stressed world.

> [!NOTE]
> Do not import the ordinary current ratio when the insurer’s balance sheet lacks current/non-current classifications. Use a specified liquidity model and consistent scenario assumptions.

*Source pattern: 2025 CFA Level II FSA, LM4, pp.267–268, L&H liquidity. Inputs adapted for practice.*

---

## Variant: 42 — Insurer capital coverage and a simultaneous stress

**Abstract:** *Compare qualifying capital with risk-based required capital. A loss and a higher requirement squeeze the ratio from both sides.*

> An insurer has qualifying capital USD 240m and risk-based required capital USD 160m. For this exercise only, its jurisdiction requires coverage of at least 120%. A stress reduces qualifying capital by USD 30m and increases required capital by 15%. Find current and stressed coverage, current capital buffer above the threshold, and new qualifying capital needed after stress. Assume any new capital qualifies fully and does not change required capital.

<span class="jargon-unlock">**Qualifying capital. What is it?** Capital eligible under the stipulated insurance regime. **Risk-based required capital. What is it?** The requirement determined from the insurer’s size and risk profile. **Capital coverage. What is it?** $C/R$, with qualifying capital $C$ and required capital $R$. **Buffer. What is it?** $C-rR$, where $r$ is the stipulated minimum coverage ratio as a decimal.</span>

**1. Establish the starting position**

$$
\text{Coverage}=240/160=\boxed{150\%},\qquad
\text{Buffer}=240-1.20(160)=\boxed{\text{USD }48\text{m}}
$$

**2. Apply both changes before testing compliance**

Required capital becomes $160(1.15)=184$ million; qualifying capital falls to USD 210m.

$$
\text{Stressed coverage}=210/184=\boxed{114.13\%}
$$

Restoring the stipulated 120% needs $1.20(184)-210=\boxed{\text{USD }10.8\text{m}}$ of additional qualifying capital. Merely staying above 100% would not meet this question’s threshold.

> [!NOTE]
> Insurance capital rules depend on the jurisdiction and business. The 120% threshold is supplied for this problem; it is not asserted as a universal regulatory minimum.

*Source pattern: 2025 CFA Level II FSA, LM4, pp.261, 268, insurance capitalization. Inputs adapted for practice.*
