
> [!WARNING] Exam Critical
> ## **10 One-Liner Exam Traps**
> 1. **Commodity indexes return ≠ commodity price change** due to roll yield from futures contract rolling.   
> 2. **Hedge fund indexes overstate performance** from survivorship bias (poor funds stop reporting).   
> 3. **Bond index turnover is high** because bonds mature and exit, not because they trade.​    
> 4. **Style indexes have highest turnover** as stocks migrate between value/growth categories.  
> 5. **Most bond prices in indexes are estimated** via matrix pricing, not actual trades.​    
> 6. **Commodity weighting is arbitrary**—no market cap equivalent exists.   
> 7. **Wilshire 5000 ≠ 5,000 stocks**—it's all investable US equities (~3k-7k).  
> 8. **GDP-weighting fixes market cap bubbles** (e.g., cut Japan from 60% to 30% in MSCI EAFE).  
> 9. **Bond indexes can't be fully replicated**—too many illiquid securities forces sampling.​    
> 10. **Sector indexes measure manager skill**—separate stock picking from sector allocation luck.
    


### **TL;DR (First Principles)**

**What is an index?** An index is a standardized basket of securities designed to represent a specific market or segment of that market. It exists because investors need a yardstick to measure performance and gain exposure to markets without owning every security.[1][2][3]

**Why?** Markets are enormous. The US has thousands of stocks. Globally, there are tens of thousands. You can't own them all, and tracking performance against the entire market is impossible without a reference point.

**Memory hook:** "Indexes are market snapshots in a bottle—concentrated, weighted, and designed to move like the market they represent."[3]

***

## **PART 1: THE FUNDAMENTAL PROBLEM INDEXES SOLVE**

Before we can understand indexes, we need to understand why they matter.

Imagine you're an investor. You want to know:
1. How is the stock market performing today?
2. Am I outperforming the market?
3. How much equity risk should I take?

Without an index, these questions are unanswerable. You'd have to track every stock individually—impossible and impractical.

**The core insight:** Indexes provide a single number that represents the behavior of thousands or millions of securities. This single number is a *weighted* combination of many securities, designed to represent a larger market reality.[3]

***

## **PART 2: EQUITY INDEXES—THE FOUNDATION**

### **1. Broad Market Indexes: Capturing the Entire Market**

A broad market index represents an entire equity market and typically includes securities representing more than 90% of that market.[3]

**Examples:** 
- **US Wilshire 5000**: Includes all US equities with readily available prices. Despite its name, it's not limited to 5,000 stocks (it had ~5,000 at inception but can expand). It's designed to represent the *entire US equity market*.[3]
- **Russell 3000**: The largest 3,000 US stocks by market capitalization, representing approximately 98% of the US market.[3]
- **Shanghai Stock Exchange Composite (SSE)**: Market-cap-weighted index of all shares trading on the Shanghai exchange.[3]

**Why these differences exist?** Different index providers make different trade-offs between *completeness* and *practicality*. The Russell 3000 is easier to manage than the Wilshire 5000 because it only includes 3,000 stocks instead of potentially 7,000+. Yet both capture ~95%+ of market value.

**Memory hook:** "Broad market indexes = 'market in a mirror.' They're designed to move exactly like the market because they contain most of it."[3]

***

### **2. Multi-Market Indexes: Going Global**

Real investors don't just care about one country. Multi-market indexes represent multiple countries and regions. They address the question: "How is the *global* equity market performing?"[3]

MSCI is the dominant index provider here. They classify markets along **two dimensions:**[3]

**Dimension 1: Economic Development**
- **Developed Markets**: Mature economies (US, UK, Germany, Japan, Australia, Canada)
- **Emerging Markets**: Growing economies with higher growth potential but more volatility (Brazil, India, South Korea, Mexico, Russia)
- **Frontier Markets**: Early-stage markets with limited liquidity and infrastructure (Vietnam, Kazakhstan, Nigeria, Argentina)

**Dimension 2: Geography**
- Americas
- Europe, Middle East, and Africa
- Asia Pacific

**Exhibit from the PDF:**[3]

| Development | Geographic Split | Examples |
|---|---|---|
| **Developed Markets** | Americas | Canada, US |
| | Europe/Middle East | UK, Germany, France, Switzerland |
| | Pacific | Japan, Australia, Singapore |
| **Emerging Markets** | Asia | India, South Korea, Indonesia, Philippines, Thailand |
| | Europe/Middle East/Africa | Russia, Turkey, South Africa |
| | Americas | Brazil, Mexico, Chile |
| **Frontier Markets** | Various | Vietnam, Bangladesh, Kenya, Nigeria |

**Why classification matters:** Investors want exposure to different stages of economic development. An emerging market index provides *different risk/return characteristics* than a developed market index. A frontier market is riskier but potentially offers higher returns.[3]

**Example of why this matters:** In 1987, the MSCI EAFE (Europe, Australasia, Far East) was 60% weighted to Japanese equities because Japan was so economically dominant. This created massive concentration risk. MSCI responded by creating GDP-weighted indexes, where each country's weight is tied to its GDP, not just market cap. This reduced Japanese exposure to ~30%, creating more balanced global exposure.[3]

**Memory hook:** "Multi-market indexes = global diversity. They solve the problem: 'How do I track the world without tracking 50 countries separately?'"[3]

***

### **3. Sector Indexes: Slicing the Market by Industry**

Different sectors of the economy behave differently over the business cycle. Consumer goods, energy, finance, healthcare, and technology don't all move together.[3]

**Why sectors matter:**[3]
- A portfolio manager might overweight technology during a boom but underweight it during a recession.
- Sector indexes help you measure *whether a manager's success came from good stock picking or good sector allocation decisions*.

**Example:** Imagine a manager beats the market by 2%. Did they pick great stocks within each sector? Or did they simply overweight technology (which was hot that year)? Sector indexes help decompose this.

**Memory hook:** "Sector indexes = 'business cycle dial.' They show which parts of the economy are leading."[3]

***

### **4. Style Indexes: Categorizing Stocks by Characteristics**

Style indexes represent groups of securities based on **market capitalization** and **value vs. growth** characteristics.[3]

**Market Capitalization:**
- **Large cap**: Bigger, more stable companies
- **Mid cap**: Medium-sized companies
- **Small cap**: Smaller, faster-growing companies

Different definitions exist—some use absolute market cap (e.g., below €100 million = small cap), others use relative ranks (e.g., smallest 2,500 stocks = small cap).[3]

**Value vs. Growth:**
- **Value stocks**: Cheap stocks with low price-to-book, low P/E, high dividend yield
- **Growth stocks**: Expensive stocks with high growth potential

Different index providers use different ratios to distinguish them.[3]

**Combining them:** You get six basic categories:[3]
- Large-cap value
- Large-cap growth
- Mid-cap value
- Mid-cap growth
- Small-cap value
- Small-cap growth

**Key insight:** Stock valuations and market caps change constantly, so stocks *migrate between style categories* over time. This means **style indexes have much higher turnover than broad market indexes**. A stock might be "large-cap value" one year and "mid-cap growth" the next.[3]

**Memory hook:** "Style indexes = 'investor archetype mirrors.' They let investors who like small-cap value stocks see how 'their style' performed without owning 1,000 stocks."[3]

***

## **PART 3: FIXED-INCOME INDEXES—A DIFFERENT BEAST ENTIRELY**

Fixed-income indexes look similar to equity indexes on the surface, but they face *fundamentally different construction challenges*.[1]

### **1. The Core Construction Problem**

Why is fixed-income indexing harder than equity indexing?[1]

**Challenge 1: Universe Size**
- Equity universe: A few thousand stocks per country
- Fixed-income universe: *Tens of thousands of bonds* per country

The Bloomberg Barclays US Aggregate Bond Index alone contains ~8,000 securities.[1]

**Challenge 2: Pricing and Liquidity**
- Equity markets are continuous auction markets. Every stock trades constantly; prices are transparent.
- Bond markets are **dealer markets**. Dealers hold inventory and create liquidity by buying and selling. Many bonds rarely trade.[1]

When an index provider wants to update a bond price, they can't just look it up. They either:
- Contact dealers (expensive, time-consuming)
- *Estimate* the price using similar bonds that did trade (introduces error)[1]

**Challenge 3: Turnover**
- Stocks are perpetual (companies keep existing).
- Bonds *mature*. When a bond matures, it disappears from the index.[1]

This creates constant turnover as new bonds replace maturing ones. A bond issued in 2015 with a 10-year maturity disappears in 2025. The index must replace it.

**Result:** Fixed-income indexes are harder and more costly to replicate than equity indexes.[1]

**Memory hook:** "Fixed-income indexing = 'herding cats.' There are too many bonds, they don't trade enough, and they keep disappearing."[1]

***

### **2. Fixed-Income Index Dimensions**

Fixed-income indexes are sliced along *multiple* dimensions simultaneously:[1]

**By Issuer Type:**
- Government (US Treasuries)
- Government agencies (Fannie Mae, Freddie Mac)
- Corporations
- Collateralized/securitized (mortgage-backed, asset-backed)

**By Credit Quality:**
- **Investment grade**: BBB- or better (Standard & Poor's rating)
- **High yield**: Below BBB- (riskier, higher-yielding "junk bonds")

**By Maturity:**
- Short-term (1-3 years)
- Intermediate (3-5, 5-7, 7-10 years)
- Long-term (10+ years)

**By Currency, Inflation Protection, and Geography**

**Example: Bloomberg Barclays Global Aggregate Bond Index**[1]

This index includes approximately 8,000 bonds from multiple countries, multiple issuers, and multiple credit qualities. Its composition looks like:
- X% government
- Y% corporate
- Z% mortgage-backed
- etc.

And simultaneously:
- A% investment grade
- B% high yield

An investor wanting just US investment-grade corporate bonds would use a more specific index. An investor wanting *all* global bonds would use the aggregate index.[1]

**Memory hook:** "Fixed-income indexes = 'kaleidoscope of slices.' One index can be broken down across issuer type, credit quality, maturity, geography, and currency simultaneously."[1]

***

## **PART 4: ALTERNATIVE INVESTMENT INDEXES—ENTIRELY DIFFERENT RULES**

Alternative assets (commodities, real estate, hedge funds) don't fit into the equity/bond framework. Their indexes are fundamentally different.[2]

### **1. Commodity Indexes: Futures, Not Actual Commodities**

Commodity indexes consist of *futures contracts* on commodities (agricultural products, metals, energy), not the commodities themselves.[2]

**The problem:** Commodities don't have an obvious weighting mechanism like market capitalization. So index providers invent their own.[2]

**Different indexes, different weightings:**

| Index | Weighting Method |
|---|---|
| Thomson Reuters/CRB | Equal-weighted fixed commodities |
| S&P GSCI | Liquidity + world production value; heavier weight to rising prices |
| Other indexes | Fixed weights determined by committee |

**Real-world impact:**[2]

In 2018, the S&P GSCI weighted energy 50% *higher* and agriculture 40% *lower* than the CRB Index. This creates vastly different risk/return profiles. Unlike equity/bond indexes targeting the same market (which are very similar), commodity indexes targeting "the commodity market" can look completely different.

**The roll yield problem:**

Futures contracts expire, so indexes must continuously "roll" from expiring contracts into new ones. This means commodity index returns reflect:[2]
1. Changes in actual commodity prices
2. The risk-free interest rate
3. Roll yield (profit/loss from rolling contracts)

A commodity index return can differ dramatically from the actual price change of the underlying commodity.

**Example:** Crude oil price up 5%, but the commodity index down 2%? The roll from expiring contracts into new contracts (at different prices) likely caused losses that offset the spot price gain.

**Memory hook:** "Commodity indexes = 'complexity sandwich.' Weighting is arbitrary, and roll yield distorts returns from the underlying commodity."[2]

***

### **2. Real Estate Investment Trust (REIT) Indexes: Listed Securities Representing Illiquid Assets**

Real estate itself is illiquid—you can't sell a building as easily as you sell a stock. But Real Estate Investment Trusts (REITs) are publicly traded corporations that own real estate.[2]

**Why REITs for an index:**
- Publicly traded = continuous pricing
- Liquid = easy to buy/sell
- Real estate exposure = you get the real estate market returns

REIT indexes include share prices of public REITs, calculated continuously like stock indexes.[2]

**Example: FTSE EPRA/NAREIT Global REIT Index Family**

This represents real estate stocks worldwide, combining data from the European Public Real Estate Association and the National Association of REITs.[2]

**Memory hook:** "REIT indexes = 'real estate translated into stocks.' You get real estate exposure through liquid securities."[2]

***

### **3. Hedge Fund Indexes: Voluntary Reporting Creates Massive Bias**

Hedge fund indexes are fundamentally different because hedge funds are *unregulated* and report performance *voluntarily*.[2]

**The survivorship bias problem:**[2]

Unlike stocks and bonds, where all transactions are recorded, hedge funds choose which databases to report to (or whether to report at all). This creates systematic bias:

- Funds doing well tend to report (good marketing).
- Funds doing poorly may stop reporting or never report in the first place.
- Therefore, hedge fund indexes *overstate* actual hedge fund performance.

**Result:** Different hedge fund databases have *very different performance statistics* for "the hedge fund industry" in the same year, because they have little overlap in which funds they track.[2]

**Example:** Database A includes 500 funds; Database B includes 500 different funds (minimal overlap). If 100 funds went bankrupt this year but were in neither database, both databases' indexes look better than the actual hedge fund universe performed.

**Memory hook:** "Hedge fund indexes = 'survivor's bias trap.' They measure the returns of funds *that survived and reported*, not all hedge fund activity."[2]

***

## **ULTRA-CONDENSED REVISION NOTES**

- **Indexes exist to represent markets without owning every security.** They're weighted baskets designed to move like the market they represent.[3]

- **Equity indexes come in layers:** broad market (entire market), multi-market (global/emerging), sector (industries), and style (cap/value-growth combinations).[3]

- **Fixed-income indexes face three construction challenges:** universe size (thousands of bonds), pricing difficulty (illiquid dealer markets), and turnover (bonds mature).[1]

- **Fixed-income indexes slice by issuer type, credit quality, maturity, currency, and geography—often simultaneously.** Aggregate indexes include everything; specialized indexes narrow down.[1]

- **Commodity indexes are arbitrary.** Different weighting schemes lead to different risk profiles, and roll yield means futures-based returns differ from commodity price changes.[2]

- **REIT indexes provide real estate exposure through liquid securities**, bypassing the illiquidity of actual property markets.[2]

- **Hedge fund indexes suffer from survivorship bias.** Voluntary reporting means they measure the returns of funds that survived and reported, not the actual hedge fund universe.[2]

- **Style indexes have high turnover** because stocks migrate between categories as valuations change; sector and broad market indexes have lower turnover.[3]

- **Economic development classification (developed/emerging/frontier) matters for global investing.** Each has different risk/return characteristics.[3]

- **Replicating fixed-income indexes is harder than equity indexes** because of size, illiquidity, and pricing challenges.[1]

