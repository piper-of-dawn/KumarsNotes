## Module 1: Alternative Investment Features, Methods, and Structures

1. **Numerical: Hard hurdle performance fee**  
   Stem: A fund earns **18%**, has a **10% hard hurdle**, and charges a **20% performance fee** on returns above the hurdle. Calculate the general partner's performance fee as a percentage of fund value.  
   Solution: First ask what the manager is allowed to charge on. A **hard hurdle** means the manager charges only on the return above the hurdle. The fund earned 18%, but the first 10% belongs to the limited partners before carry starts. Excess return is 8%. The manager takes 20% of that 8%, so the fee is 1.6% of fund value.  
   Formula: `Performance fee = max[0, p x (fund return - hard hurdle)]`.  
   Memory: Hard hurdle = bonus only on the extra part.  
   Trap: CFA is testing whether you charge carry on **18%** or only on **8%**.

2. **Numerical: Catch-up clause**  
   Stem: A fund earns **18%**, has an **8% preferred return**, a **20% performance fee**, and a **2% catch-up return** to the general partner. Calculate the general partner's total return.  
   Solution: Give the first 8% to limited partners. Then the general partner receives the 2% catch-up. After that, the remaining return is 18% - 8% - 2% = 8%. The manager gets 20% of that remaining 8%, which is 1.6%. Total general partner return is 2.0% + 1.6% = 3.6%.  
   Formula: `GP return = max[0, catch-up + p x (return - hurdle - catch-up)]`.  
   Memory: Catch-up lets the manager run after crossing the hurdle.  
   Trap: Do not treat catch-up like a hard hurdle. It accelerates the manager's share.

3. **Management fee base trap**  
   Mistake: Charging private equity management fees on only invested capital.  
   Correct logic: Private equity commonly charges management fees on **committed capital**, because capital is drawn down over years and the manager should not be pushed to invest too fast just to grow fees. Hedge funds and real estate investment trusts usually charge on **assets under management**.  
   Memory: Private equity fee base = promise first, investment later.  
   Trap: CFA gives committed capital and invested capital together; use the committed amount for private equity unless the stem says otherwise.

4. **Waterfall trap**  
   Mistake: Saying deal-by-deal and whole-of-fund waterfalls protect limited partners equally.  
   Correct logic: **Deal-by-deal**, or American waterfall, pays the general partner as each profitable deal exits, so it favors the general partner. **Whole-of-fund**, or European waterfall, waits until limited partners recover initial investment plus the hurdle at the aggregate fund level, so it favors limited partners.  
   Memory: American = manager gets paid deal by deal. European = investors get whole-fund protection first.  
   Trap: A later losing deal is exactly why clawback matters.

5. **Clawback vs high-water mark**  
   Mistake: Treating clawback and high-water mark as the same protection.  
   Correct logic: A **high-water mark** stops the manager from earning performance fees again until prior losses are recovered. A **clawback** lets limited partners reclaim performance fees already paid when later losses erase earlier gains.  
   Memory: High-water mark blocks future fees; clawback pulls back old fees.  
   Trap: Hedge funds often use high-water marks; private equity and real estate are more likely to need clawbacks over a long fund life.

## Module 2: Alternative Investment Performance and Returns

1. **Numerical: MOIC**  
   Stem: A private equity fund invests **JPY 3.8 billion** in Year 0, adds **JPY 1.2 billion** in Year 2, adds **JPY 0.2 billion** in Year 3, and exits for **JPY 8.5 billion** in Year 8. Calculate multiple of invested capital.  
   Solution: Multiple of invested capital ignores timing. First add every amount actually invested: 3.8 + 1.2 + 0.2 = 5.2 billion. Then divide the exit value by that total invested capital. MOIC = 8.5 / 5.2 = 1.63 times.  
   Formula: `MOIC = (realized value + unrealized value) / total invested capital`.  
   Memory: MOIC asks, "How many times did the money come back?"  
   Trap: MOIC does **not** care that the money arrived in different years.

2. **Numerical: Leveraged return when the trade works**  
   Stem: A hedge fund has **USD 100 million** of capital, borrows **USD 50 million** at **4%**, and the underlying position earns **8%** for the period. Calculate the leveraged return on investor capital.  
   Solution: Start with the unleveraged asset return of 8%. The fund borrowed half as much as its own capital, because 50 / 100 = 0.5. The borrowed money earns 8% but costs 4%, so the spread is 4%. Leverage adds 0.5 x 4% = 2%. Investor return is 8% + 2% = 10%.  
   Formula: `Leveraged return = r + (borrowed capital / cash capital) x (r - borrowing rate)`.  
   Memory: Leverage helps only when asset return beats borrowing cost.  
   Trap: Do not calculate return on total assets; the question asks return on investor capital.

3. **Numerical: Leveraged return when the trade loses**  
   Stem: Same fund: **USD 100 million** capital, **USD 50 million** borrowed at **4%**. The underlying position loses **2%**. Calculate the leveraged return.  
   Solution: Start with the asset return of -2%. The borrowed slice is still 0.5 of investor capital. The spread is now -2% - 4% = -6%, because the asset lost money and the loan still costs 4%. Extra damage is 0.5 x -6% = -3%. Leveraged return is -2% - 3% = -5%.  
   Formula: `Leveraged return = r + (Vb / Vc) x (r - rb)`.  
   Memory: Borrowing cost does not disappear just because the asset falls.  
   Trap: CFA is testing the sign inside `r - rb`.

4. **Numerical: Basic hedge fund fees**  
   Stem: A fund starts with **USD 100 million**, ends at **USD 130 million**, charges a **1% management fee** on year-end assets, and charges **20% performance fee** on total return. Fees are calculated independently. Calculate investor net return.  
   Solution: First calculate management fee: 1% of 130 = 1.3 million. Then calculate performance fee on the gain: 20% of (130 - 100) = 6.0 million. Total fees are 7.3 million. The investor made 30 million before fees, keeps 30 - 7.3 = 22.7 million, so net return is 22.7%.  
   Formula: `Fees = (P1 x management fee) + max[0, (P1 - P0) x performance fee]`.  
   Memory: Gross return is what the fund made; net return is what the investor kept.  
   Trap: Management fee is on **ending assets** if the stem says year-end assets.

5. **Numerical: High-water mark for old vs new investor**  
   Stem: A fund's old investor has a high-water mark of **USD 122.7 million**. Fund value falls to **USD 108.9 million**, then rises to **USD 128 million**. Fees are **1% management fee** on ending assets and **20% performance fee** above the high-water mark. Calculate the old investor's Year 3 return.  
   Solution: First charge management fee: 1% of 128 = 1.28 million. Then performance fee applies only above the old high-water mark: 128 - 122.7 = 5.3 million. Performance fee is 20% x 5.3 = 1.06 million. Total fee is 2.34 million. Investor wealth goes from 108.9 to 128 - 2.34 = 125.66 million. Return is (125.66 - 108.9) / 108.9 = 15.39%.  
   Formula: `Fee = management fee + max[0, (ending value - high-water mark) x performance fee]`.  
   Memory: Same fund, different entry point, different net return.  
   Trap: A new investor starting at 108.9 has a lower high-water mark and pays more performance fee.

6. **Index bias trap**  
   Mistake: Trusting hedge fund index returns as clean asset-class returns.  
   Correct logic: Survivorship bias removes failed funds. Backfill bias adds strong past returns only after successful funds join the database. Both overstate return and understate risk.  
   Memory: Dead funds disappear; winners show up with a resume.  
   Trap: CFA often asks why hedge fund returns look too smooth or too good.

## Module 3: Investments in Private Capital: Equity and Debt

1. **Venture stage trap**  
   Mistake: Calling every early private company investment "private equity buyout."  
   Correct logic: Pre-seed or angel capital funds the idea stage. Seed financing supports product development and market research. Early-stage financing funds operations before production and sales. Later-stage financing comes after production and sales begin. Mezzanine-stage financing prepares for an initial public offering.  
   Memory: Idea, seed, start-up, expansion, exit prep.  
   Trap: Mezzanine-stage venture capital is not the same phrase as mezzanine debt.

2. **Leveraged buyout trap**  
   Mistake: Thinking a leveraged buyout creates value just because debt is used.  
   Correct logic: Debt is the financing tool. The value story is improving or restructuring operations, then using stronger cash flows to service and pay down debt. If debt financing is unavailable or expensive, leveraged buyouts become less attractive.  
   Memory: Debt buys control; operations must pay the bill.  
   Trap: Management buyout means existing management participates; management buy-in means new management replaces current management.

3. **Exit strategy trap**  
   Mistake: Treating recapitalization as a clean exit.  
   Correct logic: Trade sale and public listing are main exits. Public listing can be an initial public offering, direct listing, or special purpose acquisition company transaction. Recapitalization can pay a dividend using new debt, but it is not a true exit because the private equity firm typically still controls the company.  
   Memory: Sale exits; recap takes cash but stays invested.  
   Trap: Write-off or liquidation is the bad exit, not a planned value-maximizing route.

4. **Vintage-year trap**  
   Mistake: Comparing private equity funds without matching vintage years.  
   Correct logic: Vintage year is when deployment begins. Funds seeded in expansion tend to earn excess returns when they fund early-stage companies. Funds seeded in contraction tend to do better with distressed companies. Diversify across vintage years because entry valuation and business-cycle phase matter.  
   Memory: Private capital performance is born in its vintage year.  
   Trap: Do not compare a boom-vintage venture fund with a contraction-vintage distressed fund as if timing did not matter.

5. **Private debt risk ladder**  
   Mistake: Treating all private debt as one risk bucket.  
   Correct logic: Senior direct lending is lower risk because it is usually senior, secured, and covenant protected. Mezzanine debt is subordinated and may include equity-like upside, so it has higher risk and return. Unitranche blends secured and unsecured debt into one loan with one blended rate. Distressed debt needs restructuring skill and recovery analysis.  
   Memory: Senior is safer; mezzanine wants extra return; distressed needs a rescue plan.  
   Trap: Venture debt often comes with warrants or convertibility because the borrower is young and not yet profitable.

6. **Diversification trap**  
   Mistake: Saying private capital diversifies only because it has many exit routes.  
   Correct logic: Diversification comes from exposure to different private company life-cycle stages, debt priorities, vintage years, and return drivers that are not identical to public markets. Venture capital has especially low correlations in the curriculum's comparison.  
   Memory: Different life cycles create different return patterns.  
   Trap: Low observed correlation may also reflect appraisal smoothing, so do not oversell it as perfect risk reduction.

## Module 4: Real Estate and Infrastructure

1. **Real estate quadrant trap**  
   Mistake: Mixing up public/private with debt/equity.  
   Correct logic: Direct property ownership is private equity real estate. A mortgage is private debt real estate. Real estate investment trust shares are public equity real estate. Mortgage-backed securities or mortgage real estate investment trusts are public debt real estate.  
   Memory: Ask two questions: traded or private, owner or lender.  
   Trap: Real estate investment trust does not automatically mean equity; mortgage and hybrid real estate investment trusts exist.

2. **REIT tax and valuation trap**  
   Mistake: Thinking the main real estate investment trust benefit is only liquidity.  
   Correct logic: The main appeal is avoiding entity-level taxation, so income is not taxed once at the trust and again at the shareholder level. Public real estate investment trusts also give transparency and easier trading, but they can have higher correlation with public equity markets.  
   Memory: REIT = pass-through tax appeal plus traded access.  
   Trap: Equity investors in public real estate discount future cash flows; private real estate appraisal can lag market reality.

3. **Strategy risk ladder**  
   Mistake: Ranking core-plus as riskier than opportunistic.  
   Correct logic: Core real estate targets stable, high-quality properties. Core-plus adds modest development or redevelopment. Value-add uses larger refurbishment, renovation, or repositioning. Opportunistic is highest risk because it can include large-scale redevelopment, distressed property, repurposing, or speculation on market recovery.  
   Memory: Core cash flow first; opportunistic story first.  
   Trap: Higher expected return usually comes from accepting development, leasing, or market-timing risk.

4. **Infrastructure cash-flow trap**  
   Mistake: Treating all infrastructure revenue as toll revenue.  
   Correct logic: Infrastructure can generate **availability payments** for making an asset available, **usage-based payments** such as tolls, and **take-or-pay arrangements** where the buyer pays for a minimum agreed volume even if it uses less.  
   Memory: Available, used, or promised.  
   Trap: Take-or-pay is not the same as usage-based revenue; payment can happen even below actual usage.

5. **Greenfield vs brownfield trap**  
   Mistake: Calling an already operating asset greenfield.  
   Correct logic: Greenfield means the asset still has to be built, so construction and demand uncertainty are high. Secondary-stage means fully operational and usually lowest risk. Brownfield means existing infrastructure with operating history, sometimes with expansion or redevelopment risk.  
   Memory: Green = build; secondary = running; brown = existing.  
   Trap: Fully constructed brownfield assets with contracted revenues are less risky than greenfield projects.

## Module 5: Natural Resources

1. **Return-driver trap**  
   Mistake: Giving raw land, farmland, and timberland the same return source.  
   Correct logic: Raw land return is mainly price appreciation. Farmland and timberland can earn lease income, income from crops or timber, and price changes in land and output. Timberland also has a biological growth cycle because trees keep growing.  
   Memory: Raw land waits; farms and forests produce.  
   Trap: Income pass-through belongs more naturally to farmland and timberland than raw land.

2. **Numerical: Commodity futures carry**  
   Stem: A commodity spot price is **100**, the risk-free financing effect is **3**, storage cost is **4**, and convenience yield is **2**. Estimate the futures price.  
   Solution: Start with spot price of 100. Add the financing cost and storage cost because holding the physical commodity costs money. Then subtract convenience yield because owning the physical commodity gives a benefit. Futures price is 100 + 3 + 4 - 2 = 105.  
   Formula: `Futures price approximately = spot price x (1 + risk-free rate) + storage costs - convenience yield`.  
   Memory: Costs lift futures; convenience yield pulls futures down.  
   Trap: Convenience yield is a benefit, so subtract it.

3. **Contango vs backwardation**  
   Mistake: Memorizing the words without checking spot versus futures.  
   Correct logic: **Contango** means futures price is above spot price because cost of ownership exceeds convenience yield. **Backwardation** means futures price is below spot price because the convenience yield is high enough to outweigh costs.  
   Memory: Contango hurts the long-only investor; backwardation helps.  
   Trap: Low inventories can create high convenience yield and push the market into backwardation.

4. **Inflation hedge trap**  
   Mistake: Saying commodities hedge inflation because inflation rises first.  
   Correct logic: Commodity prices are components of consumer inflation, especially energy and food. Commodity price changes can come before reported inflation changes. The curriculum's evidence shows commodities perform better in higher or rising inflation environments but poorly when inflation declines.  
   Memory: Commodities often move before the inflation report catches up.  
   Trap: Farmland and timberland may perform well, but their direct correlation with inflation is lower than commodities.

5. **Diversification trap**  
   Mistake: Using high return or high volatility as proof of diversification.  
   Correct logic: Diversification comes from low correlation with traditional stocks and bonds, not from return level alone. Commodities, farmland, and timberland have historically shown low correlations with traditional investments, while commodities also have high volatility.  
   Memory: Correlation diversifies; volatility just shakes the ride.  
   Trap: A good inflation hedge should have higher correlation with the inflation risk being hedged.

## Module 6: Hedge Funds

1. **Numerical: Hedge fund fee with hurdle after management fee**  
   Stem: A hedge fund starts with **USD 100 million**, ends with **USD 120 million**, charges **1.6% management fee** on end-of-year assets, and charges **18% performance fee** on the return left after subtracting the management fee and an **8% hurdle**. Calculate the investor return.  
   Solution: First calculate management fee: 1.6% of 120 = 1.92 million. Gross growth is 120 - 100 = 20 million. The hurdle is 8% of beginning capital, or 8 million. Because the hurdle is after fees, subtract both the hurdle and the management fee from the growth: 20 - 8 - 1.92 = 10.08 million. Performance fee is 18% x 10.08 = 1.81 million. Total fees are 1.92 + 1.81 = 3.73 million, so investors keep about 20 - 3.73 = 16.27 million, or about 16.3%.  
   Formula: `Investor return = (gross gain - management fee - performance fee) / beginning value`.  
   Memory: Management fee first, hurdle test second, incentive fee last.  
   Trap: The answer changes if the hurdle is before fees, after fees, or absent.

2. **Strategy classification trap**  
   Mistake: Calling hedge funds a separate asset class.  
   Correct logic: Hedge funds invest in traditional asset classes but use specific strategies, leverage, short selling, derivatives, concentrated positions, and flexible mandates. Equity hedge, event-driven, relative value, and opportunistic strategies are strategy buckets, not new asset classes.  
   Memory: Hedge fund = wrapper plus strategy, not a magic asset.  
   Trap: The word "hedge" does not mean the fund must reduce risk.

3. **Long/short vs market neutral vs short bias**  
   Mistake: Treating every long/short equity strategy as market neutral.  
   Correct logic: Fundamental long/short often has net long exposure. Market neutral tries to balance long undervalued and short overvalued positions to reduce market beta. Short bias keeps negative market exposure overall.  
   Memory: Long/short may lean long; market neutral tries to cancel market; short bias leans down.  
   Trap: A market-neutral label is about exposure, not simply owning both long and short positions.

4. **Merger arbitrage trap**  
   Mistake: Thinking merger arbitrage is risk-free arbitrage.  
   Correct logic: The common trade is long the target and short the acquirer, trying to capture the spread if the deal closes. The spread exists because the deal can fail, be delayed, face regulatory hurdles, or be repriced.  
   Memory: The spread is payment for deal risk.  
   Trap: Leverage is often used because the spread can be small, which means losses can also be amplified.

5. **Fund-of-funds fee drag**  
   Mistake: Comparing a fund of hedge funds to a direct hedge fund before fee layers.  
   Correct logic: A fund of funds adds manager selection and diversification but also adds another layer of management and incentive fees on top of underlying hedge fund fees. The curriculum emphasizes that this can reduce returns even when gross strategy exposure looks attractive.  
   Memory: More access, more selection, more fees.  
   Trap: Better diversification does not automatically mean better net return.

6. **Hedge fund index bias trap**  
   Mistake: Treating hedge fund databases like clean public-market indexes.  
   Correct logic: Reporting is voluntary, so self-reporting and selection bias matter. Survivorship bias removes failed funds. Backfill bias adds a successful fund's prior returns when it enters the index.  
   Memory: Bad funds vanish; good histories get imported.  
   Trap: Index returns may be overstated and risk understated.

## Module 7: Introduction to Digital Assets

1. **Proof of work vs proof of stake**  
   Mistake: Saying all validation is mining by computers solving puzzles.  
   Correct logic: **Proof of work** uses miners solving cryptographic problems. **Proof of stake** uses validators that pledge digital assets as collateral to support block validity. Both can reward successful validators or miners with digital assets.  
   Memory: Work burns computing power; stake pledges capital.  
   Trap: The curriculum says mining rewards can occur under validation, but the mechanism differs.

2. **Permissionless vs permissioned network trap**  
   Mistake: Treating all distributed ledgers as open blockchains.  
   Correct logic: Permissionless networks are open: participants can access the ledger and transact without a central authority. Permissioned networks restrict what members can do and are more likely to be cost effective for controlled business uses.  
   Memory: Permissionless = open crowd; permissioned = controlled access.  
   Trap: Permissionless decentralization can reduce central trust, but it does not remove fraud or market manipulation risk.

3. **Stablecoin trap**  
   Mistake: Assuming every stablecoin is safely backed by actual reserve assets.  
   Correct logic: Securitized stablecoins are backed by reserve assets such as fiat currency baskets. Algorithmic, or smart, stablecoins try to hold value through supply algorithms instead of physical backing. Asset-backed tokens maintain price parity with a target asset through tokenization.  
   Memory: Backed coin has collateral; algorithmic coin has a rule.  
   Trap: "Stable" describes the design goal, not a guaranteed outcome.

4. **Token type trap**  
   Mistake: Calling every token a cryptocurrency.  
   Correct logic: Cryptocurrencies use their own blockchains or related crypto networks as digital currencies. Non-fungible tokens represent distinct objects or authenticity claims. Security tokens digitize ownership rights in securities. Utility tokens pay for network services. Governance tokens provide voting rights on permissionless networks.  
   Memory: Currency spends; NFT identifies; security owns; utility uses; governance votes.  
   Trap: Most initial coin offerings do not typically attach voting rights.

5. **Centralized vs decentralized exchange trap**  
   Mistake: Saying decentralized exchanges are safer in every way.  
   Correct logic: Centralized exchanges run on private servers and can provide price and volume transparency, but server or key leaks create vulnerabilities. Decentralized exchanges run on distributed frameworks, making hacking one computer much less damaging, but they are harder to regulate. Both exchange types can face fraud and manipulation.  
   Memory: Centralized is easier to run and regulate; decentralized is harder to shut down.  
   Trap: Lower hack vulnerability does not mean lower fraud risk.

6. **Wallet-key trap**  
   Mistake: Thinking a lost crypto wallet passkey is like a forgotten brokerage password.  
   Correct logic: Direct cryptocurrency ownership requires a wallet with encryption keys. If the passkey is lost, the holding can become irretrievable. Buying through a centralized exchange may still give direct exposure, but the custody and server risks are different.  
   Memory: Lose the key, lose the asset.  
   Trap: Digital ownership removes some intermediaries but adds credential and custody risk.
