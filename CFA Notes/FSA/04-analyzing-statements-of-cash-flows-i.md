### MODULE 4: ANALYZING STATEMENTS OF CASH FLOWS I

> [!info] HOW TO READ THIS MODULE
> Cash flow is where accrual accounting meets the bank account.
> The learning outcomes are: link cash flow with the income statement and balance sheet, prepare direct and indirect cash flow statements, convert indirect to direct, and compare International Financial Reporting Standards (IFRS) with United States Generally Accepted Accounting Principles (U.S. GAAP).
> Your mantra: profit can be estimate-heavy; cash movement is harder to hand-wave.

#### Cash Flow Introduction and Direct Method Cash Flow from Operating Activities

1. Balance sheet = snapshot (assets, how they're funded) at one date → income statement, cash flow statement, and equity statement are all "flow" bridges that explain _how_ you got from last snapshot to this one → so every line-item change on the balance sheet must trace through at least one flow statement, and if it doesn't, something's wrong.
2. Income statement runs on accrual accounting (recognize revenue when earned, not when cash lands) → cash flow statement corrects for this by tracking only actual cash movement → the gap between the two creates or destroys current assets/liabilities on the balance sheet: e.g., revenue recognized but cash not yet collected = accounts receivable goes up; cash received before you deliver = deferred revenue (a liability) goes up until you perform.
3. That gap gives you a built-in diagnostic: Beginning A/R + Revenue − Cash Collected = Ending A/R → if ending A/R is ballooning while cash collected flatlines, the company may be booking fake revenue (sales recognized on paper with no real expectation of collection) → same logic applies in reverse to payables and deferred revenue, so cross-checking flow statements against balance sheet movements is your primary fraud-detection tool.
4. Cash flow statement splits into operating (core business cash), investing (buying/selling long-term assets), and financing (debt/equity raises and repayments) → a transaction hits the income statement and the cash flow statement at _different times_ — depreciation hits income as an expense over years but the full cash outflow hit investing on purchase day; interest accrues on the income statement over the loan's life but cash leaves only on payment date → understanding which bucket and which timing applies is the whole game of reading these statements together.
5. Real example: ABC buys $100 inventory on credit Jan 1 
	- Balance sheet: inventory ↑$100, A/P ↑$100, no cash move yet. 
	- Pays supplier Jan 30 — cash ↓$100, A/P ↓$100, operating cash flow ↓$100. 
	- Sells for $150 on credit Feb 1 — A/R ↑$150, inventory ↓$100, income statement: revenue $150, COGS $100, profit $50, still no cash. 
	- Customer pays Feb 15 — cash ↑$150, A/R ↓$150, operating cash flow ↑$150. Net result: $50 profit on income statement, $50 net cash inflow on cash flow statement, but they arrived at completely different dates.


> [!info] MEMORISE THIS 
> How to use direct method? - Pick a P&L line (revenue, COGS, salary expense, whatever)
> - Find its B/S partner (A/R for revenue, A/P for purchases, wages payable for salary, etc.)
> - Check: did that B/S account go up or down?
> - Asset up = you got less cash than the P&L says. Liability up = you paid less cash than the P&L says. Reverse for decreases.
> - P&L number ± that B/S change = actual cash. Done.

> [!TIP] HAMMER THIS INTO YOUR HEAD
> Memorise these two lines:
> **BEGINNING + WHAT GOES IN − WHAT GOES OUT = ENDING**
> **CASH PAID = EXPENSE + INCREASE IN ASSET - INCREASE IN LIABILITY**

6. **Cash from customers — one step:**
	Beginning A/R + Revenue − Cash Collected = Ending A/R
You know beginning A/R, revenue, ending A/R → solve for cash collected. Done.

7. **Cash to suppliers — two steps, same rule twice:**
	- Step 1 — _how much did you buy?_ **Beginning Inventory + Purchases − COGS = Ending Inventory** You know everything except purchases → solve for purchases.
	- Step 2 — _how much did you actually pay?_ **Beginning A/P + Purchases − Cash Paid = Ending A/P** You now know purchases from step 1 → solve for cash paid.
8. Same logic extends to every operating line: 
	- **Opening Wages Payable + Salary Expense - Cash Wage Payments = Ending Wages Payable**. Solve for Cash Wage Payments.
	- **Opening Interest Payable + Interest Expense - Cash Interest Payments = Ending Interest Payable**. Solve for Cash Interest Payments.
#### Cash flow classifications (US GAAP vs IFRS)

- US GAAP: Interest paid = CFO; interest received = CFO; dividends received = CFO; dividends paid = CFF; taxes = CFO (with limited exceptions).
- IFRS: Interest paid = CFO or CFF; interest received = CFO or CFI; dividends received = CFO or CFI; dividends paid = CFO or CFF; taxes allocated by nature when specifically identifiable, otherwise CFO.
- Bank overdrafts: US GAAP = financing liability; IFRS = may be included in cash and cash equivalents if repayable on demand and integral to cash management.
- CFO examples: cash from customers; cash paid to suppliers/employees; trading securities cash flows (if operating by policy); taxes and interest (per standard).
- CFI examples: purchase/sale of PP&E and intangibles; business acquisitions/disposals; lending and collections (if not classified as operating under policy); long-term investment securities.
- CFF examples: issuing/repaying debt (principal); issuing/repurchasing equity; dividends paid (US GAAP) or per policy (IFRS).

#### Indirect Method Cash Flow from Operating Activities

**Learning outcomes covered here:** analyze and interpret both reported and common-size cash flow statements; calculate and interpret free cash flow to the firm, free cash flow to equity, and performance and coverage cash flow ratios.

> [!abstract] MEMORISE THIS FOR EFFICIENCY
> Your brain should hear: **Net Income → Remove non-operating → Undo Non Cash → Fix WC timing → CFO.**
> 				 **==CFO = NI or PAT + NCC - $\Delta$ WC==**
> Indirect method is NOT preferred by either US GAAP or IFRS 
> **US GAAP requires disclosure of cash paid for interest and income taxes**, while **IFRS encourages (but does not mandate) similar disclosure**. 
> 
> Do not stop at calculating cash flow from operating activities. The Chartered Financial Analyst (CFA) exam wants you to read the story: **where cash came from, where it went, whether operations paid for investment, and whether net income is backed by cash.**

1. Indirect CFO = “net income (accrual story)” converted into “cash reality” by 
		 - Removing stuff that isn’t operating, **Gain on sale of equipment / land** is removed from CFO because the cash from sale is shown in investing.
		 - Undoing expenses/gains/losses that didn’t move cash. Things like depreciation reduce Net Income but don't cost actual cash. We must **add them back**
		 - Adjust for timing in working capital: 
			 - Increase in current operating asset → subtract from NI; decrease → add. Current Asset could be A/R or Inventory.
			 - Increase in current operating liability → add to NI; decrease → subtract. Current liability could be A/P or Wages Payable.
		 - Fixing timing mismatches created by working capital accruals. Your brain should hear: **Net Income → Remove non-operating → Undo Non Cash (NCC) → Fix WC timing ($\Delta WC$) → CFO.**
	
	
> [!TIP] HAMMER THIS INTO YOUR HEAD
> **Closing Anything = Opening Anything + Inflow (Purchase) - Outflow (Write Off / Sale)**
> What remains in closing, is the net of what you added to opening plus what you removed from opening. This will help you solve a lot of questions. You can calculate any variable by re-arranging the equation above

2. Memorize what should be added and subtracted
	  ==**Subtract the gains and Add the losses**== (We are reversing).
	  ==**Subtract the Asset Increase and Add the Asset Decrease**== (We are reversing).
	  ==**Subtract the Liability Decrease and Add the Liability Increase**== (We are reversing).

| **Stuff to be added:**                   | **Stuff to be subtracted:**              |
| ---------------------------------------- | ---------------------------------------- |
| Depreciation, Amortization and Depletion | Anything that eats into a liability      |
| Loss on sale of land, PPE                | Gain on sale of land, PPE                |
| Asset Impairment, write-down             | Reversal of asset Impairment, write-down |
| Decrease in DTA<br>                      | Increase in DTA                          |
| Increase in DTL<br>                      | Decrease in DTL                          |
| **Losses** on Prepayment of Debt         | **Gains** on Prepayment of Debt          |
3. Fix timing of working capital (**==Subtract change in working capital==**):
	- Operating assets move opposite to cash; operating liabilities move with cash.
	- Working capital (for CFO–indirect) = **current operating assets − current operating liabilities**.
	- **Inventory up = cash trapped → CFO down,   Inventory down = cash released → CFO up**

4. Read the cash flow statement like a detective, not like a calculator:
	- For a mature company, the main source of cash should usually be **cash flow from operating activities (CFO)**. If operations are always negative, the company survives only by borrowing money or issuing shares. That cannot go on forever because lenders and shareholders eventually want cash back from the business.
	- For a young growth company, negative cash flow from operating activities can be okay for a while because cash may be tied up in inventory and receivables. Think of a fast-growing retailer opening new stores: shelves must be stocked before the cash register starts ringing. But this is a temporary excuse, not a permanent business model.
	- The cleanest pattern is: operations generate cash, the company uses some of it for capital expenditures, and the leftover cash can reduce debt, pay dividends, buy back shares, or fund new projects.
	- If investing cash flow is heavily negative, ask: is the company buying productive assets for the future, or just burning cash? Danone's 2017 cash flow statement showed a huge investing outflow because it acquired WhiteWave. That is not the same as a normal maintenance capital expenditure.
	- If financing cash flow is heavily positive, ask: why did outsiders have to provide cash? Was the company funding growth, plugging an operating hole, or preparing for a large acquisition?

> [!info] WHY OPERATING CASH FLOW QUALITY MATTERS (intuition first)
> Imagine Apple and Sears both report net income of 1,000 in a simplified classroom example.
> Apple collects cash quickly from customers, pays suppliers normally, and reports cash flow from operating activities of 1,300.
> Sears books more sales on credit, receivables balloon, inventory piles up, and cash flow from operating activities is only 200.
> On paper, both earned 1,000. In the real world, Apple has money in the bank and Sears has promises from customers plus products sitting in stores.
> This is why the Chartered Financial Analyst (CFA) Curriculum treats the relationship between net income and cash flow from operating activities as an earnings-quality check.
> Enron is the famous warning sign here: reported earnings can look impressive while the cash story is much weaker. Cash is harder to fake than accrual profit, so always ask whether profit turned into cash.

5. Compare cash flow from operating activities with net income:
	- For a mature company, cash flow from operating activities should usually be **higher than net income** because depreciation and amortization reduce accounting profit but do not use current-period cash.
	- If net income is high but cash flow from operating activities is weak, earnings quality may be poor. The company may be recognizing revenue too early, stretching assumptions, or letting receivables and inventory absorb cash.
	- If cash flow from operating activities is volatile, forecasting future cash flows becomes harder. That matters directly for valuation because debt and equity are ultimately valued from expected future cash.
	- A simple exam line: **Net income tells you the accounting story. Cash flow from operating activities tells you whether customers actually funded the business.**

6. Common-size cash flow statements under the indirect method:
	- Method 1: express each cash inflow as a percentage of total cash inflows, and each cash outflow as a percentage of total cash outflows.
	- Method 2: express each cash flow line item as a percentage of net revenue. This is useful for forecasting because once you forecast revenue, you can estimate items like depreciation, capital expenditures, debt repayment, and dividends as a percentage of sales.
	- Under the **direct method**, operating cash inflows and outflows are visible separately, such as cash received from customers and cash paid to suppliers.
	- Under the **indirect method**, operating cash inflows and outflows are not shown separately. You only see the net cash flow from operating activities. So in a common-size inflow/outflow statement, positive cash flow from operating activities appears as one inflow line, not as separate customer collections and supplier payments.

> [!warning] EXAM TRAP
> If cash flow from operating activities is positive under the indirect method, it is shown as a cash inflow in the total-inflows common-size format.
> If cash flow from operating activities is negative, it is shown as a cash outflow.
> Do not try to split it into customer cash received and supplier cash paid unless the statement uses the direct method.

7. Connect this module to free cash flow and ratios:
	- Free cash flow starts with the same idea: after operations generate cash, ask whether that cash covers capital expenditures. If yes, the company has room to repay lenders, pay shareholders, or reinvest.
	- Free cash flow to the firm (FCFF) is cash available to both debt and equity capital providers after operating expenses, taxes, working capital investment, and fixed capital investment.
	- Free cash flow to equity (FCFE) is cash available to common shareholders after operating expenses, taxes, working capital investment, fixed capital investment, and net borrowing effects.
	- Performance ratios use cash flow from operating activities to judge cash productivity, such as cash flow from operating activities divided by revenue.
	- Coverage ratios use cash flow from operating activities to judge solvency pressure, such as whether operations can cover debt, interest, dividends, or reinvestment needs.

> [!tip] Quick checks
> 1. Mature company: cash flow from operating activities should normally be positive and should ideally cover capital expenditures.
> 2. Cash flow from operating activities greater than net income is usually a good quality signal, but still check why.
> 3. Receivables up means sales were not fully collected in cash, so cash flow from operating activities goes down.
> 4. Payables up means suppliers financed part of the business, so cash flow from operating activities goes up.

> [!QUESTION] Question
> A company reports net income of 1,000 for the year. Depreciation expense recorded during the year is 200. Accounts receivable increased by 150 over the period. Calculate cash flow from operating activities using the indirect method.
> NI = 1000, NCC = 200, $\Delta$ WC = 150
> CFO = 1000 + 200 - 150 = 1050
> ---
> A firm shows net income of 2,000. During the year, inventory increased by 300 and accounts payable increased by 180. Using the indirect method, determine cash flow from operating activities.
> NI = 2000, $\Delta$ WC = 300 - 180 = 120
> CFO = 2000 - 120 = 1820
> ---
> A firm shows Net Income of 39000. Current Depreciation Expense is 7000. Gain on Sale of Land is 10000. Loss on disposal of PP&E is 2000. AR increased by 1000. Inventory decreased by 2000. CL increased by 11,000
> NI = 39000, NCC = 7000 - 10000 + 2000 = -1000, $\Delta$ WC = 1000 - 2000 - 11000 = -12000.
> CFO = 39000 - 1000 + 12000 = 50000
>

#### Investing and Financing Cash Flows and IFRS/U.S. GAAP

1. Investing cash flow tells you what the company did with long-term assets and investments: bought equipment, sold equipment, acquired businesses, or bought securities.
2. Financing cash flow tells you how capital providers moved money in or out: issued debt, repaid debt, issued shares, repurchased shares, or paid dividends.
3. A healthy mature company usually generates cash from operations, invests enough to stay competitive, and returns surplus cash to debt or equity holders.
4. A risky pattern is negative operating cash flow funded by repeated borrowing. That is like paying rent with a credit card every month.
5. International Financial Reporting Standards (IFRS) gives more classification flexibility for interest and dividends than United States Generally Accepted Accounting Principles (U.S. GAAP). For comparisons, rebuild classifications consistently.

> [!tip] REAL-WORLD HOOK
> Netflix spent heavily on content for years. The income statement could show improving scale, but the cash flow statement showed how much cash was being poured into content assets. That is why you read cash flow, not just net income.

