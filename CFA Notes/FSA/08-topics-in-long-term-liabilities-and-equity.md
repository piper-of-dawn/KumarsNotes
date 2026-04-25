### MODULE 8: TOPICS IN LONG-TERM LIABILITIES AND EQUITY

> [!info] HOW TO READ THIS MODULE
> This module is about promises that do not always look like normal debt.
> The learning outcomes are: explain leases from lessee and lessor perspectives, explain defined contribution plans, defined benefit plans, and stock-based compensation, and read long-term liability disclosures.
> The trick is simple: liabilities are promises, not just bank loans.

#### Leases

#### Lessee accounting summary (IFRS 16 vs U.S. GAAP ASC 842)

- Balance sheet (both): recognize Right‑of‑Use (ROU) asset and Lease liability for substantially all leases (short‑term/low‑value exceptions under IFRS policy).
- Lease liability (both): effective interest rate method (EIRM): interest = opening liability × rate; principal = cash payment − interest; closing liability = opening + interest − payment.

IFRS 16 (single model):
- P&L shows separate depreciation of ROU asset (typically straight‑line) and interest expense on the liability → front‑loaded total expense.
- ROU asset falls linearly; liability falls non‑linearly (slow early, faster later) → often a net lease liability position over time.

U.S. GAAP ASC 842:
- Finance lease: same economics/presentation as IFRS (separate interest + amortization).
- Operating lease: still recognize ROU + liability and EIRM for liability, but present a single straight‑line lease expense; compute period amortization as a plug so that interest + amortization equals straight‑line lease cost.

Memory hooks:
- “If you lease it, you show it.” (ROU + liability on balance sheet.)
- “GAAP: one balance sheet; two income‑statement shapes.”

> [!tip] REAL-WORLD HOOK
> Airlines and retailers love leases because they can control expensive assets without buying them upfront. Before modern lease rules, many operating leases sat off the balance sheet, so companies looked less leveraged than they really were. The new rule says: if you control the asset and owe payments, show the asset and the liability.
	
1. An alternative way to look at a lease is: **taking a loan and buying the asset.**
2. To be called a lease, a lessee needs to have following characteristics:
	- Asset must be **Identified** a.k.a it should exist.
	- Lessee should have exclusive control of asset and must derive all the economic benefits from the asset. 
3. Under IFRS and U.S. GAAP, in a **financing lease** ownership and risks should be transferred to lessee. You break it and you pay for it. If either the benefits or the risks of ownership are not substantially transferred, it is an operating lease.

> [!warning] Remember
> Financing Lease:
> 	- **Present Value of payments >= Asset Fair Value**
> 	- You have an option to buy the asset and get rid of the lease.
4. Accounting treatment would be:
	- On liabilities side, you would create a lease liability that would be amortized with time.
	- On asset side, you would create ROU asset that would depreciate with time.


> [!question] QUESTION
> The Affordable Company (Affordable) leases a machine for its own use for four years with annual payments of $10,000. At the end of the lease, which is also the end of the machine's useful life, Affordable will return the machine to the lessor. The interest rate implicit in the lease is 5%. Assuming that the ROU asset is amortized on a straight-line basis over the term of the lease, calculate the impact of the lease on Affordable's financial statements for each of the four years.
> 
> Fair value of Asset: PMT = -10000, I/Y = 5, FV = 0, CPT ⟶ PV = 35549
> 
> Asset Amortisation per year = 35549 / 4 = 8887.25
> 

6. From Lessor's POV: **“What asset do I carry?”**
	- **Finance lease:** you stop carrying the physical asset and carry a **financial asset (lease receivable)** instead.  
	- **Operating lease:** you keep carrying the **physical asset (PP&E at cost − accumulated depreciation)**.

7. Lease receivable is measured as the **present value of future lease payments**, discounted using the **rate implicit in the lease**.
8. All lease payments represent operating revenues regardless of lease classification. **The entire lease payment (BOTH principal and interest) goes to CFO**

> [!question] QUESTION
> Financing Lease: $4,000 at each year-end for 3 years for PP&E worth $11,000. Rate implicit in the lease: 6%. Show the treatment in the accounts of the lessor.
> 
> PV = $10,692. This will be recorded as **Lease Receivable on Assets side of Balance Sheet** and **PP&E worth $11000 would be derecognized**. ==The asset swap created a spread of $308. The Equity (liability) must decline by $308 to show this loss. This "Loss at Lease inception" is also shown on P/L.==
> 
> AMORTISATION SCHEDULE
> 
| OB    | PMT  | P    | I   |
| ----- | ---- | ---- | --- |
| 10692 | 4000 | 3358 | 642 |
| 7332  | 4000 | 3560 | 440 |
| 3772  | 4000 | 3772 | 226 |
> 
> INCOME STATEMENT:
> 
> Y1:	Income from Lease =  $642. Loss on lease inception = $308
> 
> CASHFLOW STATEMENT
> 
> $4000 goes in CFO
> Under **both US GAAP and IFRS (for the lessor)**, the **interest received in a lease is not split out**—the **entire lease cash receipt** (which includes the interest component) is reported in **CFO (operating activities)**.
> 
> BALANCE SHEET
> 
> Y1: 
> - Assets: Lease Receivable is recorded as $10,692. PP&E is derecognized by $11,000. Liability: Equity is decreased by $308.
> - Lease Receivable drops by 3358 (Asset). Cash Balance increases by 4000 (Asset). Equity increases by 642 (Liability) 



> [!QUESTION] QUESTION
> A lessor buys equipment for **$50,000** on Jan 1, Year 1. It is leased out under an **operating lease** for **3 years** with **annual rent of $12,000 paid at each year-end**. The equipment is depreciated **straight-line over 5 years** with **$0 residual**. Ignore taxes. Required: how the lessor’s **balance sheet impact** at the end of **Year 1, Year 2, Year 3** (PP&E net, accumulated depreciation, cash change). Also state whether a **lease receivable** is recognized.


10. IFRS vs US GAAP: lessor balance sheet is basically the same (don’t overthink).

#### Deferred Compensation and Disclosures

> [!abstract] MEMORISE THIS FOR EFFICIENCY
> 


1. A pension is delayed salary. **Defined Contribution (DC)** ⟶ firm promises _how much it puts in_, employee bears **investment risk**. For example NPS and EPF in India and PPK in Poland. My employer puts in money, it gets invested into the market. If market collapses, everything turns to ashes. 
2. **Defined Benefit (DB)** ⟶ firm promises _how much you'll get_, employer bears investment + longevity risk. I am promised a pension of PLN 10k per month, no matter if market collapses or booms. For example, ZUS contributions or Military pensions. **Employer bears market risk and employee bears longevity risk.** If I die, the pension vanishes. 
3. Defined benefit is complicated. ==It is recorded as a **long term liability** on the balance sheet and on part of employers, it involves forecasting market cycles, interest rates, expected lifespan etc.==
4. Defined Benefit (DB) plans create a **net position** on the balance sheet = what the firm owes − what it has set aside.  **Assets > obligation ⟶ asset. Assets < obligation ⟶ liability**.  Annual changes flow partly through P&L, partly through OCI.
5. Funded status = **Fair value of plan assets − Pension obligation** **Overfunded** means I have saved more money (Plan Assets) that what my obligation demands (Pension to be paid), which creates a net asset position. **Underfunded** creates a net liability position.
6. IFRS = Pay for work + interest in P&L, dump all shocks into OCI GAAP = smooth P&L via amortization.


> [!question] QUESTION
> **Start**: Obligation = 1,000, Assets = 900, Net liability = 100, Discount rate = 10%. 
> **Year events**, Service cost = 50, Past service cost = 20, Actual asset return = 40, Expected return = 90, Actuarial Loss = 60. Identify what goes into OCI and what goes into P&L. 
> 
> #### IFRS
> **Any admin,  service cost (past or present) goes into P&L.** For example: Service + Past Service = 70
> **Any interest goes into P&L:** 10% of 1000 = 100
> **Any return or market shock goes to OCI:** Asset return surprise - Actuarial Loss = (40-90) - 60 = -110
> 
> #### US GAAP
> **PnL:** 
> 	- Current Service Cost + Interest = - 50 - 100 = -150
> 	- Expected Return on Assets = 90
> **OCI:**
> 	- Past Service Cost = -20
> 	- Actuarial Loss = -60

7. One of the differences from IFRS pension accounting is that past service costs are recognized in other comprehensive income, rather than in the income statement as part of employee service costs. These costs are amortized over the employees' service period. **Actuarial gains and losses are typically treated the same way, but U.S. GAAP allows firms to recognize them in the period incurred.**

> [!tip] HAMMER THIS INTO YOUR HEAD
> 
> Past service cost for Defined Contribution plans goes into OCI under US GAAP and PnL under IFRS.
8. ==Pension cost is **not shown as a separate line item** for manufacturing firms. It is **embedded** in expenses based on employee role.== Factory workers ⟶ pension cost goes into **inventory ⟶ COGS**. Office/admin staff ⟶ pension cost goes into **SG&A / salaries**. Income statement hides pension cost inside operating costs. Therefore, analysts **must read the notes** to see total pension expense and assumptions.
9. Stock options, on the other hand, may cause managers to take on too much risk, because options have asymmetrical payoffs. An option has value if the stock price is above the exercise price, but its value cannot fall below zero if the stock price is below the exercise price.
10. **Grant-date fair value rule (IFRS = GAAP)**: stock-based compensation is measured at **fair value on grant date** and expensed **over the vesting (service) period**; immediate vesting ⟶ full expense on grant date, delayed vesting ⟶ straight-line over service period.
11. These are shares awarded outright, with restrictions (Restricted Stock Units (RSU)) , or contingent on performance (Performance Shares).    
12. **Stock grants vs performance shares**:    
    - **Stock grants / RSUs** ⟶ FV = **share price at grant**, expense based only on service/vesting.        
    - **Performance shares** ⟶ vesting tied to **non-market metrics** (ROE, EPS, margins); fair value still set at grant but **managerial incentives can distort accounting choices**.        
13. Compensation expense exists **before shares are received**; if vesting conditions aren't met, expense is reversed.
14. **Stock grants (RSUs)**: the share price on the grant date is taken as the cost; this cost is charged to the income statement over the vesting period (or all at once if vesting is immediate); the same amount is added to equity; example: grant value 100 with 2-year vesting ⟶ expense 50 each year, equity increases by 50 each year, and at vesting it is moved into share capital and APIC.    
15. **Stock grants – why equity doesn't change**: the expense reduces retained earnings, but equity is increased by the same amount through APIC, so total equity stays the same; example: expense 50 ⟶ retained earnings −50, APIC +50.
16. **Stock options**: the option's value is calculated using an option pricing model at grant and expensed evenly over the vesting period; **until exercise, only APIC increases and no shares are issued;** example: option value 80 over 4 years ⟶ expense 20 per year, APIC +20 per year.    
17. **Stock options – exercise stage**: when employees exercise, the company receives cash equal to the strike price and issues shares; equity increases by the cash received, split between share capital (par) and APIC, and any accumulated reserve is moved into APIC; example: strike 50 ⟶ cash +50, share capital +1, APIC +49 plus the reserve.

> [!tip] HAMMER THIS INTO YOUR HEAD
> - Suppose UBS gave me a stock as salary. The price is 100 CHF. In this case retained earnings will go down by 100 (stock got charged on PnL) and APIC will increase by 100. **No new shares are issued**. If I don't complete 3 years, they will reverse the charge on PnL and APIC will go down.
> - Suppose UBS gave me a deferred stock (100 CHF) as salary that I can vest at the end of 3 years of service. Each year UBS will show a compensation expense of 33.33 CHF **always calculated on the price @ grant date** and APIC rises by 33.33 CHF every year.
> - Suppose UBS gave me a call option to exercise at the end of 3 years of service at strike price of 100 CFH. The Black Scholes value is 10 CHF, which is shown in income statement. If I exercise it, then UBS gets the strike price which moves into APIC and issues me shares. **UBS does not issue new shares**
18. Phantom stock a.k.a fake stock is a **cash bonus plan** that mimics share price performance, where employees receive **cash linked to the company's stock value without receiving actual shares or ownership**.

