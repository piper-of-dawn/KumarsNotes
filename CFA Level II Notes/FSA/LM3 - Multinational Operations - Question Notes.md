## Variant: 1 — A foreign-currency payable crosses year-end

**Abstract:** *Book the purchase at its transaction-date rate; remeasure the unpaid foreign-currency bill at each reporting date, then settle it. A stronger payment currency hurts the importer.*

> A euro-functional importer buys inventory for MXN 100,000 on 1 November. The peso costs EUR 0.0684 then, EUR 0.0690 at 31 December, and EUR 0.0703 when the payable is settled on 15 January. Calculate inventory cost, each year's exchange gain or loss, and settlement cash. The importer closes its books on 31 December. Its 20X1 revenue is EUR 10,000 and operating profit before exchange effects is EUR 1,000; find operating margin if the 20X1 loss is classified as operating or non-operating.

<span class="jargon-unlock">**Functional currency. What is it?** The currency of the entity's primary economic environment; here, EUR. **Foreign-currency payable. What is it?** A bill fixed in another currency; MXN 100,000 stays fixed, but its euro value moves. **Spot rate. What is it?** Today's euro price of one peso, stated as EUR/MXN. **Transaction gain or loss. What is it?** The change in euro value of the unpaid bill, recognized in net income. **Operating margin. What is it?** Operating profit divided by revenue.</span>

**1. Freeze the inventory cost on purchase day**

The inventory was acquired when one peso cost EUR 0.0684. Later currency moves change the bill, not the inventory's historical cost.

$$
\text{Inventory and opening payable}=100{,}000(0.0684)=\boxed{\text{EUR }6{,}840}
$$

**2. Reprice the bill at each date**

At year-end, the bill costs EUR 6,900, so 20X1 records a EUR 60 loss even though no cash has moved. At settlement it costs EUR 7,030, adding a 20X2 loss of EUR 130.

$$
\text{20X1 loss}=100{,}000(0.0690-0.0684)=\boxed{\text{EUR }60};\quad
\text{20X2 loss}=100{,}000(0.0703-0.0690)=\boxed{\text{EUR }130}
$$

Settlement cash is $\boxed{\text{EUR }7{,}030}$; total loss is EUR 190. The EUR 60 is unrealized at year-end, whereas the cumulative EUR 190 becomes realized on payment.

If the EUR 60 year-end loss is operating, margin is $(1{,}000-60)/10{,}000=\boxed{9.4\%}$; if classified as non-operating, margin is $1{,}000/10{,}000=\boxed{10.0\%}$. Net income includes the loss either way.

> [!NOTE]
> A foreign-currency **payable** loses when that currency strengthens; a **receivable** gains. Never reprice the inventory merely because payment is later.

*Source pattern: CFA Level II FSA, LM3, Examples 1–3, pp.119–124; practice Q1–3 and solutions pp.193–194. Year-end rate and dates adapted.*

---

## Variant: 2 — Strip exchange-rate growth out of subsidiary sales

**Abstract:** *Translate each year's local sales at that year's rate, then hold the earlier rate fixed to separate operating growth from currency translation.*

> A subsidiary makes FC 1,000 million in sales in Year 1 and FC 1,100 million in Year 2. The parent reports in USD. Average rates are USD 0.80/FC in Year 1 and USD 0.72/FC in Year 2. Find reported USD sales growth, Year 2 sales at constant Year 1 currency, and the dollar currency effect. Assume no acquisitions or divestitures.

<span class="jargon-unlock">**FC. What is it?** A placeholder for the subsidiary's local currency. **Average rate. What is it?** An approximation of transaction-date rates across the year, stated here as USD per FC. **Constant currency. What does that mean?** Translate both years' sales at the same rate to isolate the change in local sales. **Currency effect. What is it?** The reported Year 2 USD amount less Year 2 sales translated at the old rate.</span>

**1. Translate the amounts actually reported**

$$
\text{Year 1 USD sales}=1{,}000(0.80)=800;\quad
\text{Year 2 USD sales}=1{,}100(0.72)=\boxed{792\text{ million}}
$$

Reported growth is $(792/800)-1=\boxed{-1\%}$: the parent shows a decline despite higher local sales.

**2. Hold the exchange rate fixed**

$$
\text{Year 2 constant-currency sales}=1{,}100(0.80)=\boxed{880\text{ million}};\quad
\text{currency effect}=792-880=\boxed{-88\text{ million}}
$$

Local sales grew 10%. The USD 80 million operating increase minus the USD 88 million currency drag equals the reported USD 8 million decline. The foreign currency weakened because each FC now buys fewer dollars.

> [!NOTE]
> Do not label the full reported sales change as business growth. A rate move can reverse its sign.

*Source pattern: CFA Level II FSA, LM3, translated-sales discussion pp.129–130; practice Q32–33 and solutions p.198. Inputs adapted.*

---

## Variant: 3 — Current-rate balance sheet and its balancing adjustment

**Abstract:** *When the local currency is functional, translate every asset and liability at the closing rate, share capital at its issue-date rate, and retained earnings by rollforward; the remaining balance goes to equity.*

> A locally autonomous FC-functional subsidiary has year-end assets of FC 600 million, liabilities of FC 200 million, share capital of FC 250 million, and retained earnings of FC 150 million. Its parent reports in USD. Closing rate: USD 0.80/FC; share-issue rate: USD 0.60/FC. Opening translated retained earnings were USD 100 million. Current-year FC profit is 70 million, translated at the USD 0.75/FC average rate; FC 20 million of dividends were declared at USD 0.625/FC. Calculate translated retained earnings, net assets, and the cumulative translation adjustment (CTA).

<span class="jargon-unlock">**Current-rate method. What is it?** The method for a foreign-currency-functional subsidiary: assets and liabilities use the closing rate. **Historical rate. What is it?** The rate when an equity contribution happened. **Retained earnings. What is it?** Prior profits kept in the business, rolled forward from the prior translated balance. **CTA. What is it?** The cumulative translation adjustment that balances the translated statement and sits in equity, outside net income.</span>

**1. Roll forward translated retained earnings**

The FC 150 ending balance checks locally: FC 100 opening + FC 70 profit − FC 20 dividends. For the USD statement, keep each component's own translated amount.

$$
\text{USD retained earnings}=100+70(0.75)-20(0.625)=\boxed{140\text{ million}}
$$

**2. Translate net assets, then solve for CTA**

Assets are USD 480 million; liabilities USD 160 million; share capital is $250(0.60)=150$ million.

$$
\text{CTA}=600(0.80)-200(0.80)-250(0.60)-140=\boxed{+30\text{ USD million}}
$$

Check: USD 480 assets = USD 160 liabilities + USD 150 capital + USD 140 retained earnings + USD 30 CTA. The positive CTA matches a net asset position in a stronger FC.

> [!NOTE]
> Do not translate ending retained earnings at the closing rate. It is a history of profits and dividends, not a new year-end transaction.

*Source pattern: CFA Level II FSA, LM3, current-rate rules pp.136–139, Example 4 pp.143–146; practice Q10–12, Q24, Q28 and solutions pp.195–198. Inputs adapted.*

---

## Variant: 4 — Temporal method: historical assets and monetary exposure

**Abstract:** *When the parent's currency is functional, current-value and monetary items use today's rate; historical-cost non-monetary assets keep their acquisition rates. A net foreign-currency debt loses when that currency strengthens.*

> A subsidiary keeps FC books but has USD as its functional currency. At year-end it holds FC 100 million cash, FC 200 million historical-cost inventory, and FC 300 million historical-cost equipment. It owes FC 80 million trade payables and FC 120 million debt. Rates in USD/FC are 0.80 at year-end, 0.65 when inventory was acquired, and 0.60 when equipment was acquired. Translate these assets and liabilities. Separately, if the FC 100 million net monetary liability had been constant while the rate rose from 0.60 to 0.80, calculate the exchange gain or loss from that exposure alone.

<span class="jargon-unlock">**Temporal method. What is it?** Remeasurement into the functional currency while preserving each item's measurement basis. **Monetary. What does that mean?** A fixed number of currency units to receive or pay, such as cash, receivables, and debt. **Non-monetary. What does that mean?** An item such as inventory or equipment rather than a fixed currency claim. **Historical cost. What is it?** The amount recorded when that asset was acquired. **Net monetary liability. What is it?** Monetary liabilities minus monetary assets.</span>

**1. Match each item to its rate**

$$
\text{USD assets}=100(0.80)+200(0.65)+300(0.60)=\boxed{390\text{ million}}
$$

Payables and debt are both monetary, so translated liabilities are $(80+120)(0.80)=\boxed{160\text{ USD million}}$. Inventory and equipment keep the older USD rates because they remain at historical cost.

**2. Check the exposure's direction**

Fixed monetary liabilities exceed cash by FC 100 million. A stronger FC makes that net bill more expensive in dollars.

$$
\text{Exchange gain/loss}=(100-80-120)(0.80-0.60)=\boxed{-20\text{ USD million}}
$$

This controlled exposure change is a loss in net income; it is not the balancing amount for a full translated statement with operating flows.

> [!NOTE]
> Historical-cost inventory and equipment are not monetary; debt remains monetary even if it was issued years ago.

*Source pattern: CFA Level II FSA, LM3, temporal-method rules pp.137–140, Examples 4–6 pp.143–156; practice Q23, Q36, Q39–40 and solutions pp.197–199. Inputs adapted.*

---

## Variant: 5 — The same gross profit under two translation methods

**Abstract:** *Both methods usually translate sales at an average rate. Current rate gives cost of sales that same rate; temporal method follows the historical rate of the inventory sold, so margins can differ.*

> A subsidiary reports FC 1,000 million sales and FC 600 million cost of sales. Its USD parent's average USD/FC rate for the year is 0.75, and the historical rate for the inventory sold is 0.65. Ignore all other expenses. Calculate translated gross profit and gross margin if FC is functional (current-rate method) and if USD is functional (temporal method).

<span class="jargon-unlock">**Cost of sales. What is it?** The recorded cost of inventory delivered to customers. **Gross profit. What is it?** Sales minus cost of sales. **Gross margin. What is it?** Gross profit divided by sales. **Functional currency. What is it?** The main operating currency; it determines the translation method. **Current-rate method. What is it?** Translate revenues and expenses at transaction-date rates, often approximated by an average. **Temporal method. What is it?** Preserve historical cost by translating inventory-related expense at the rate attached to that inventory.</span>

**1. Translate the shared sales amount**

Sales become $1{,}000(0.75)=\boxed{\text{USD }750\text{ million}}$ under either method.

**2. Choose the rate for the inventory consumed**

$$
\begin{aligned}
\text{Current rate: GP}&=750-600(0.75)=\boxed{300};&\text{margin}&=300/750=\boxed{40\%}\\
\text{Temporal: GP}&=750-600(0.65)=\boxed{360};&\text{margin}&=360/750=\boxed{48\%}
\end{aligned}
$$

Amounts are USD millions. The FC margin is $(1{,}000-600)/1{,}000=40\%$, matching current rate here because sales and cost use the same average rate. Temporal cost uses an older, cheaper dollar rate, raising reported margin by 8 percentage points.

> [!NOTE]
> Under temporal translation, cost of sales follows the acquisition rate of inventory sold; inventory costing (such as FIFO) can change that rate.

*Source pattern: CFA Level II FSA, LM3, illustration pp.143–147, Examples 5–6 pp.149–156; practice Q33–34, Q37 and solutions pp.198–199. Inputs adapted.*

---

## Variant: 6 — Find the translation adjustment in income or equity

**Abstract:** *Use the functional currency to locate the exchange difference: current-rate CTA accumulates in equity, while temporal remeasurement affects profit. A sale of the foreign operation releases its accumulated CTA.*

> A USD parent reports USD 900 million net income before any disposal gain. Its FC-functional subsidiary's CTA was a USD 12 million credit at the start of the year and a USD 20 million credit just before sale. Assume the current-year USD 8 million CTA change has no tax effect. What is comprehensive income before sale if this is the only other comprehensive income item? If the parent then sells the entire subsidiary for proceeds that equal its carrying amount before CTA recycling, what gain is recognized on disposal and what is final net income? Ignore tax and transaction costs.

<span class="jargon-unlock">**CTA. What is it?** Cumulative translation adjustment, the accumulated currency difference in equity for an FC-functional subsidiary. **Other comprehensive income (OCI). What is it?** Income-like changes recorded outside net income; a current-rate CTA change goes here. **Comprehensive income. What is it?** Net income plus OCI. **Recycling. What is it?** Moving a previously accumulated CTA into net income when the foreign operation is disposed of.</span>

**1. Measure the year's OCI before sale**

The CTA credit grew by USD 8 million. Thus comprehensive income before disposal is $900+(20-12)=\boxed{\text{USD }908\text{ million}}$.

**2. Release the accumulated CTA on sale**

The sale price equals carrying amount before CTA, so the only disposal gain is the USD 20 million CTA credit reclassified from equity.

$$
\text{Disposal gain}=\boxed{\text{USD }20\text{ million}};\quad
\text{final net income}=900+20=\boxed{\text{USD }920\text{ million}}
$$

Reclassification removes USD 20 million from CTA; it does not create a second USD 20 million of total lifetime performance. If the subsidiary had USD as functional currency, temporal remeasurement gains and losses would already have entered net income instead.

> [!NOTE]
> Current rate: exchange difference in equity until disposal. Temporal method: remeasurement difference in current net income.

*Source pattern: CFA Level II FSA, LM3, translation rules pp.136–140, Examples 8–9 and disclosures pp.162–169; practice Q8, Q21, Q31 and solutions pp.194–198. Inputs adapted.*

---

## Variant: 7 — Which ratio changes when the method changes?

**Abstract:** *Compare rates on the ratio's numerator and denominator. If both use the same rates under both methods, the ratio stays put; a historical-cost asset can make a turnover ratio move.*

> A subsidiary has FC 500 million sales, FC 100 million cash, FC 200 million current liabilities, and FC 250 million historical-cost fixed assets. USD/FC rates are 0.80 at year-end, 0.75 average for sales, and 0.60 when the fixed assets were acquired. Calculate cash ratio and sales-to-fixed-assets under current-rate and temporal methods. Ignore depreciation and intra-year asset changes.

<span class="jargon-unlock">**Cash ratio. What is it?** Cash divided by current liabilities, a measure of immediate liquidity. **Fixed-asset turnover. What is it?** Sales divided by fixed assets, showing sales per dollar of plant and equipment. **Current rate. What is it?** Closing USD price of one FC. **Historical rate. What is it?** USD price of one FC when an asset was acquired. **Current-rate/temporal method. What are they?** The two ways of translating a foreign subsidiary; their main difference here is the rate on historical-cost fixed assets.</span>

**1. Identify the unchanged ratio**

Cash and current liabilities are monetary, so both methods use the 0.80 closing rate.

$$
\text{Cash ratio}=\frac{100(0.80)}{200(0.80)}=\boxed{0.50}\quad\text{under both methods}
$$

**2. Reprice only the fixed-asset denominator**

Sales are USD $500(0.75)=375$ million under either method. Fixed assets are USD 200 million at current rate but USD 150 million at their historical rate.

$$
\text{Sales/fixed assets: current}=375/200=\boxed{1.875};\quad
\text{temporal}=375/150=\boxed{2.50}
$$

The higher temporal turnover here comes from a lower translated asset balance, not more units sold.

> [!NOTE]
> A ratio can change solely because translation gives its components different rates. Check the rate on each component before interpreting performance.

*Source pattern: CFA Level II FSA, LM3, translation analytical issues pp.147–157; practice Q26–28, Q35–38 and solutions pp.197–199. Inputs adapted.*

---

## Variant: 8 — Hyperinflation: restate first under IFRS

**Abstract:** *IFRS first restores historical-cost non-monetary assets to year-end purchasing power, then uses the closing rate. US GAAP uses temporal remeasurement without that inflation restatement.*

> A subsidiary in a highly inflationary economy bought land for FC 1,000 million when the general price index was 100 and USD 0.50 bought one FC. At year-end the index is 150 and the rate is USD 0.30/FC. The land remains at historical cost in local books. Calculate its translated USD carrying amount under IFRS and US GAAP. It also earned FC 100 million revenue when the index was 125; calculate its IFRS-restated USD revenue. Separately, a constant FC 200 million cash balance was held throughout the period; what is its purchasing-power loss in year-end FC units, ignoring interest and transactions?

<span class="jargon-unlock">**General price index (GPI). What is it?** A measure of the local price level; 150/100 means prices rose 50%. **Non-monetary land. What is it?** Land is an asset rather than a fixed cash claim. **Inflation restatement. What is it?** Multiply historical cost by ending GPI divided by acquisition GPI. **Temporal remeasurement. What is it?** Translate historical-cost assets at their acquisition-date rate. **Purchasing-power loss. What is it?** The goods a fixed cash holding can no longer buy after inflation.</span>

**1. Apply each accounting route**

$$
\begin{aligned}
\text{IFRS land}&=1{,}000(150/100)(0.30)=\boxed{\text{USD }450\text{ million}}\\
\text{US GAAP land}&=1{,}000(0.50)=\boxed{\text{USD }500\text{ million}}
\end{aligned}
$$

The difference arises because the 50% inflation rise and 40% fall in USD/FC do not exactly offset. Under IFRS, a monetary item such as cash is not restated on the balance sheet.

Revenue must also be stated in year-end purchasing power before translation: $100(150/125)(0.30)=\boxed{\text{USD }36\text{ million}}$.

**2. Measure the cost of holding fixed cash**

FC 200 million would need to become FC 300 million to retain its opening purchasing power: $200(150/100)-200=\boxed{\text{FC }100\text{ million loss}}$. The monetary loss enters income under the IFRS inflation-restatement process, subject to the full period's actual monetary flows.

> [!NOTE]
> Inflation restatement applies to historical-cost non-monetary items; monetary cash and debt stay at nominal FC amounts, but holding them creates a purchasing-power gain or loss.

*Source pattern: CFA Level II FSA, LM3, IAS 29 procedures and Example 7 pp.157–162; practice Q14, Q17, Q20–21 and solutions pp.196–197. Inputs adapted.*

---

## Variant: 9 — A foreign profit mix changes the effective tax rate

**Abstract:** *Weight each jurisdiction's tax rate by its share of pretax profit. Then compare the result with the home statutory rate to isolate the foreign-rate effect.*

> A multinational earns EUR 600 million pretax profit at home taxed at 30% and EUR 400 million pretax profit abroad taxed at 20%. Assume all amounts are taxable as earned and there are no other tax adjustments. Calculate total tax, effective tax rate (ETR), and the percentage-point effect of foreign tax rates relative to taxing all EUR 1,000 million at home. Next year the same EUR 1,000 million profit is split EUR 400 million home and EUR 600 million abroad; compute the new ETR.

<span class="jargon-unlock">**Pretax profit. What is it?** Profit before income tax. **Statutory tax rate. What is it?** The rate written in tax law for a jurisdiction. **Effective tax rate (ETR). What is it?** Actual income tax expense divided by total pretax profit. **Profit mix. What is it?** The fraction of total profit earned in each jurisdiction. **Percentage point. What is it?** The arithmetic difference between two percentage rates, such as 30% minus 26% = 4 points.</span>

**1. Weight the tax bills, not the rates by country count**

$$
\text{Tax}=600(0.30)+400(0.20)=\boxed{\text{EUR }260\text{ million}};\quad
ETR=260/1{,}000=\boxed{26\%}
$$

All-home tax would be EUR 300 million, so foreign operations reduce the rate by $26\%-30\%=\boxed{-4\text{ percentage points}}$.

**2. Move profit without changing any statutory rate**

$$
ETR_{\text{new}}=\frac{400(0.30)+600(0.20)}{1{,}000}=\boxed{24\%}
$$

The two-point fall comes entirely from more profit being earned where the tax rate is lower. An actual reconciliation can also include exemptions, losses, withholding tax, and other items.

> [!NOTE]
> An ETR change does not prove tax law changed; the geographic mix of profits can move it by itself.

*Source pattern: CFA Level II FSA, LM3, effective-tax discussion and Example 10 pp.169–171; practice Q7, Q15 and solutions pp.194–196. Inputs adapted.*

---

## Variant: 10 — Reconcile reported, constant-currency, and organic sales growth

**Abstract:** *Remove the stated currency and portfolio effects from reported growth to expose the underlying sales trend; then compare geographic drivers before calling growth sustainable.*

> A company reports Year 2 sales of USD 1,040 million versus USD 1,000 million last year, or 4% growth. Management's bridge says exchange-rate changes added 6 percentage points and acquisitions added 3 points; divestitures had no effect. Calculate constant-currency and organic growth using the disclosed additive bridge. Separately, Region A's reported growth is 7% with a −4-point currency effect and no portfolio effect; Region B's is 9% with a +7-point currency effect and no portfolio effect. Which region has stronger underlying growth?

<span class="jargon-unlock">**Reported growth. What is it?** This year's reported sales divided by last year's, minus one. **Currency effect. What is it?** The disclosed percentage-point contribution from exchange-rate changes. **Constant-currency growth. What is it?** Reported growth excluding that effect. **Portfolio effect. What is it?** Growth added or removed by acquisitions and divestitures. **Organic growth. What is it?** Growth excluding both currency and portfolio effects. **Additive bridge. What is it?** A disclosure whose percentage-point components are designed to sum to reported growth.</span>

**1. Remove each disclosed contribution**

$$
\text{Constant-currency}=4\%-6\%=\boxed{-2\%};\quad
\text{organic}=4\%-6\%-3\%=\boxed{-5\%}
$$

Thus reported sales rose USD 40 million, but the bridge says the comparable business shrank. This is a percentage-point bridge, so do not compound its disclosed components as if they were sequential growth factors.

**2. Compare regions on the same basis**

Region A's underlying growth is $7\%-(-4\%)=\boxed{11\%}$; Region B's is $9\%-7\%=\boxed{2\%}$. Region A has the stronger operating trend even though its headline growth is lower. Currency effects may reverse, so they are usually a weaker basis for projecting sales than underlying volume or price changes.

> [!NOTE]
> Check each company's definition of “organic”; use the specific reconciliation it discloses rather than assuming every issuer removes identical items.

*Source pattern: CFA Level II FSA, LM3, sales-growth disclosures and Example 11 pp.171–174; practice Q4, Q16 and solutions pp.194–196. Inputs adapted.*
