### MODULE 8.2: TYPES OF HYPOTHESIS TESTS

1. A researcher has gathered data on the daily returns on a portfolio of call options over a recent 250-day period. The mean daily return has been 0.1%, and the sample standard deviation of daily portfolio returns is 0.25%. The researcher believes that the mean daily portfolio return is not equal to zero. Construct a hypothesis test of the researcher’s belief.
	$H_0$: $\mu = 0$, $H_A$: $\mu \neq 0$
	$s$ = $0.0025 / \sqrt{250} = 0.00016$ 
	$t$ = $0.001 / 0.00016 = 6.25$
	Assume $\alpha = 0.05$ 
	Since |6.25| > |1.96| then we can reject null. 
 
	 	 
## CASHFLOW FROM INVESTING
Suppose I have this information:

|                | Opening | Closing |
| -------------- | ------- | ------- |
| Land           | 100     | 90      |
| P&M Gross      | 500     | 600     |
| P&M Accum Depn | 300     | 350     |

**Information:**
- P&M costing 100 was sold during the year for the profit of 30.
- Depreciation charged to P/L was 130
- Gain on sale of land was 45

Compute Cashflow from Investing activities

> [!TIP] HAMMER THIS INTO YOUR HEAD
> **Closing Anything = Opening Anything + Inflow (Purchase) - Outflow (Write Off / Sale)**
> What remains in closing, is the net of what you added to opening plus what you removed from opening. This will help you solve a lot of questions. You can calculate in variable by re-arranging the equation above
###### SOLUTION
First, compute land and P&M purchases/sale:
Land Purchases = Closing - Opening = 90 - 100 = -10
P&M Purchases = Closing - Opening + Sale =  600 - 500 + 100 = 200

Second compute Acc Dep for P&M Sold
Acc Dep for P&M Sold = Opening + Charge - Closing = 300 + 130 - 350 = 80

Third carrying amount of each asset sold
CA for P&M sold = Purchase Cost - Acc Dep = 100 - 80 = 20
CA for Land sold = 10

Fourth, Cashflow from P&M Sale = CA + Gain = 20 + 30 = 50 
Cashflow from P&M Purchase = -200
**Net Cashflow from P&M = -150**
Cashflow from land Sale = CA + Gain = 10 + 45 = 55
Cashflow from land Purchase = 0
**Net Cashflow from Land = 55**
CFI = -150 + 55 = -95

### Algorithm for such type of questions
#### Step 1: Compute Purchases or Sales

**“Cash from Long-Term Assets = Cash from all sales − Cash spent on all purchases.”**  

Everything else is just reconstructing those numbers. For each, write: 

 ==**Opening balance + Purchases - Cost of assets sold = Closing balance**== 

> [!WARNING] Remember
> **Closing Anything = Opening Anything + Inflow - Write Off / Sale**
> What remains, is the net of what you added to opening plus what you removed from opening

This always gives you **purchases** if sales cost is known. Or gives you **sale cost** if purchases are known. Do it for all the fixed assets. This gives you cash flow from purchase
#### Step 2: Calculate Accumulated Depreciation 

==**Closing Acc Dep = Opening Acc Dep + Dep Charged - Acc Dep on Asset Sold**==
#### **Step 3: Compute Carrying Amount of Assets Sold**

Carrying amount is purchase cost of the asset minus the accumulated depreciation attributed to the asset: 

**==Carrying amount = Cost - Acc Dep of thhe sold
==**
#### **Step 4: Use Profit/Loss on Sale to Get Cash Proceeds**

==**Cashflow From Sale = Carrying Amount + Gain**==
#### Step 5: Combine Everything

==**Cashflow = Cashflow from Sale - Cash flow from Purchase**==


> [!WARNING] Remember
> * **Depreciation NEVER appears directly** in investing cash flow.
> * **Profit on sale ≠ cash**. It helps you compute cash.
> * **Closing balances always guide you**; always start from them.
> * If asset has no depreciation (e.g., land), use:
  Sale proceeds = Gain + (Opening - Closing)
  
### RELATIVE VALUATION

Williams Optical is a publicly traded firm. An analyst estimates that the market value of net fixed assets is 120% of book value. Liability and short-term asset market values are assumed to equal their book values. The firm has 2,000 shares outstanding. Using the selected financial results in the table, calculate the value of the firm’s net assets on a per-share basis.

|Item|Amount|
|---|--:|
|Cash|10,000|
|Accounts receivable|20,000|
|Inventories|50,000|
|Net fixed assets|120,000|
|**Total assets**|**200,000**|
|Accounts payable|5,000|
|Notes payable|30,000|
|Term loans|45,000|
|Common stockholder equity|120,000|
|**Total liabilities and equity**|**200,000**|

Market Value of Net Fixed Assets = 120 * 1.2 = 144
Market Value of Liabilities = 200 - 120 = 80
Market Value of all assets = 144 + 50 + 20 + 10 = 224
Net Asset Value = 224 - 80 = 144
Net Asset Value per share =  144 / 2 = 72

## MODULE 65.1
| Mortgage | Interest Rate | Beginning Balance (000 USD) | Current Balance (000 USD) | Original Term (Months) | Months to Maturity |
| -------- | ------------- | --------------------------- | ------------------------- | ---------------------- | ------------------ |
| A        | 2.6%          | 100                         | 90                        | 240                    | 210                |
| B        | 1.0%          | 200                         | 72                        | 300                    | 100                |
| C        | 5.4%          | 300                         | 247                       | 360                    | 280                |
Total Outstanding Principal = 90 + 72 + 247 = 409 
WAM = (90/409 ⨯ 210) + (72/409 ⨯ 100) + (247/409 ⨯ 280) = 35 + 33.33 + 140 = 233
WAC = (90/409 ⨯ 2.6) + (72/409 ⨯ 1.0) + (247/409 ⨯ 5.4) = 4.0%