Agent Operating Guide for KumarsNotes (Codex CLI)

Purpose

- Capture the working conventions for this notes repo so future runs consistently follow the user’s preferences and Codex CLI behaviors.
- Prioritize precise, minimal edits that respect the author’s voice and typography.

Core Principles

- Be concise, direct, and friendly. Provide brief preambles before grouped tool calls.
- Preserve the user’s original content. When adding, append as separate bullets/sections; do not delete unless explicitly asked.
- Match existing style: callouts, headings, typography, and tone.
- Validate changes with quick scans. Avoid unrelated edits.

Workflow Checklist

1) Understand scope
- Skim file structure with `rg --files` and search with `rg -n`.
- If using external sources (e.g., PDFs outside workspace), request escalated permissions as needed.

2) Communicate before acting
- Send a 1–2 sentence preamble describing upcoming related actions.
- Use `update_plan` for multi-step tasks; keep it short and update statuses.

3) Make targeted changes
- Use `apply_patch` only for the files you must touch.
- Keep edits minimal; maintain headings and callouts.
- Don’t commit or branch unless explicitly asked.

4) Verify and hand off
- Re-scan for the specific patterns you changed (e.g., `\uXXXX` sequences) or headings you added.
- Summarize changes and offer logical next steps.

Sandbox & Approvals

- Filesystem: write only in the workspace. Reading/writing outside requires escalated permissions (ask with a one-sentence justification).
- Network: assume restricted. Don’t fetch packages or remote data without approval.
- Safety: avoid destructive actions unless user requested and understands impact.

Tooling Preferences

- Search: prefer `rg` (ripgrep). Example: `rg -n "^### MODULE" file.md`.
- File views: `sed -n 'a,bp' file`, `nl -ba file | sed -n 'a,bp'` for numbered context.
- PDF text: use `pdftotext -layout -nopgbrk` to a workspace file, then search with `rg`.
- Local PDFs: All Schweser PDFs are located at `/home/piperofthedawn/Insync/kumarshan25@gmail.com/Google Drive/CFA/Schweser`.
- Patching: use `apply_patch` with Add/Update semantics. Don’t re-open unchanged files repeatedly.

Notes Style Conventions (KumarsNotes)

- Callouts: preserve and use the existing markers (e.g., `[!tip]`, `[!ABSTRACT]`, `[!Question]`, `[!warning]`).
- Math:
  - Use LaTeX in display blocks (not inline) for formulas.
  - Provide a plain-language “Notation” list spelling out symbols (e.g., “Debt: …”).
- Numericals:
  - Always “Problem → Solution → Explanation”.
  - Show key steps with display math.
- Typography:
  - Keep bullets and emphasis consistent with surrounding text.
  - Use plain language labels in prose (e.g., “Debt = 200”), reserve symbols for equations.
- Edits policy:
  - Do not remove the user’s original points.
  - Add missing information as independent bullets under the same section.
  - Keep the same callout/typography “spirit”.
  - Pointers formatting: Use numbered lists (1., 2., 3.) for module pointers instead of dash bullets, unless the user explicitly requests otherwise.

Plain-Language Rule (STRICT)

- Never use acronyms, tickers, or abbreviations without spelling them out first time in the same line. "ADR" → "average daily rate (the price per room actually sold)." "RevPAR" → "Revenue per Available Room." "ARPU" → "average revenue per user." No exceptions, even in short hammer-bullets.
- No cryptic shorthand like "Taj (USD 400 ADR × 70% occ) vs OYO (USD 30 × 95%) — same category, opposite levers." Write it out: "The Taj in Mumbai might charge USD 400 per night and fill 70% of its rooms. A budget hotel like OYO might charge USD 30 and fill 95%."
- Use full sentences. Do not rely on "≈", "→", or compressed phrases to carry meaning. Arrows and symbols are fine *after* the idea has been stated in words.
- Examples must be self-explanatory — the reader should not have to know what "Big-4" or "sq ft" means without being told.
- One-liner hammers still exist, but "one-liner" refers to *one concept per bullet*, not *one physical line of text*. A 2–4 sentence plain-English bullet is fine; a single cryptic sentence full of jargon is not.

Core Definition Breakdown Rule (STRICT)

- When writing a sentence that contains the core definition of a concept, immediately follow that sentence by unpacking every jargon term used in it.
- Use the exact format: "What is X:" followed by a one-line primitive meaning.
- If the term describes a process, function, or role, use the exact format: "Why is X used:" followed by a one-line causal purpose.
- Do not create a separate component section for this breakdown. Put the breakdown directly after the core definition sentence.
- Do not recurse definitions beyond one level. Define the terms inside the definition once, then move on.
- Do not repeat terms that have already been unpacked in that breakdown.
- After the breakdown, explain the concept in very casual Feynman style, speaking directly to the reader.
- Use real-world examples, scandals, interesting events, and anecdotes where they make the idea stick. Prefer concrete stories over sterile textbook examples.
- Focus on each learning outcome. This is sacrosanct: every explanation must serve the learning outcome being covered, not drift into trivia.

How Kumar Wants Examples Written

Every example that is meant to make a concept stick should follow this pattern. This is not a style suggestion — it is how examples must be written in these notes.

1. **Use a real, famous company the reader already knows.** Not "Firm A" or "Company X." Use Apple, Walmart, Starbucks, Steam/Valve, Netflix, Spotify, Jio, the Taj, OYO, Reliance. If it is a bank, name an Indian bank (State Bank of India, HDFC) or give it a plain name like "Janata Bank." Abstract placeholders do not stick; recognisable brands do.

2. **Give two contrasting cases, not one.** A single number has no meaning. "Apple Store earns about USD 5,500 per square foot" is forgettable. "Apple earns USD 5,500 per square foot while Walmart earns about USD 400" is unforgettable, because the contrast shows what the ratio actually *reveals* about a business. Always pair a high case with a low case, a typical case with an extreme case, or one business model against another.

3. **Use concrete, specific numbers — not ranges or vague language.** "USD 5,500 per square foot," "350 employees," "100 million gamers," "USD 12 per month." Not "a lot," "very high," or "substantial." Round to memorable figures, but keep them specific enough that the reader can visualise the shop, the hotel, the user.

4. **State the example in full plain English sentences.** No parenthetical shorthand. Write it the way you would say it out loud to someone at a chai stall. "Valve, the company that runs the Steam gaming store, has only about 350 employees but serves more than 100 million gamers." Not "Valve/Steam ≈ USD 10M/emp, ~350 staff, 100M+ users."

5. **Always end with "so what."** After the two numbers, explain in one sentence *what the ratio told you that the raw revenue number did not*. "That is why analysts watch same-store sales — it tells you whether the business itself is getting stronger, or whether the company is only buying growth by opening new outlets." Without the "so what," the example is trivia; with it, the example teaches the ratio.

6. **Prefer ceiling-vs-floor pairings for productivity ratios.** For revenue-per-employee, pair a software/platform extreme (Steam, WhatsApp pre-acquisition) with a normal service firm (a consulting firm). For sales-per-square-foot, pair Apple with Walmart. The spectrum gives the reader an anchor range to place any new firm inside.

7. **Use real regional examples where they fit.** Jio for ARPU, Taj/OYO for hotels, State Bank of India or HDFC for banks. The reader is Indian and studies for the CFA — Indian examples land faster than generic American ones, but American giants (Apple, Walmart, Netflix) are fine when they are the iconic case.

8. **Never sacrifice clarity for brevity.** If the full explanation needs 3–4 sentences, give 3–4 sentences. A 1-line cryptic example that the reader has to decode is worse than a 4-line plain one that reads itself. The test is: can the reader re-read the bullet a month from now and immediately see the point, without having to look anything up?

Feynman-Style Intuition Blocks (when the concept is counterintuitive)

- When a formula or ratio is counterintuitive, abstract, or commonly mis-interpreted (e.g., CV, interest burden, tax burden, leverage amplification, DuPont terms), add a dedicated intuition block **before or alongside** the formula — not only after.
- Use a `[!info]` callout with an uppercase title like `WHY X WORKS (intuition first)` or `WHY HIGHER X = MORE Y (intuition first)`.
- Write it in Feynman style: casual, conversational, address the reader directly, like explaining to a friend at a chai stall. Drop jargon on first pass and reintroduce it only after the intuition lands.
- Always include a concrete numerical example with real-sounding names/setups (two shops, two companies, utility vs semiconductor, grocer vs luxury brand). Compare two cases side-by-side so the reader *sees* the contrast, not just reads it.
- Close the block with a one-line "why this is the right definition" — i.e., why the formula is built this way and not some alternative (e.g., "why divide by mean and not total"). This inoculates against the most common exam trap.
- Keep it append-only: do not replace the crisp MEMORISE/Notation/Formula blocks. The intuition block supplements them; it does not substitute.
- Length guidance: 6–12 short lines is plenty. If it runs longer than one screen, cut.
- Triggers to add a Feynman block: a ratio that scales by size (CV, per-employee, per-room), a fraction that is "kept" vs "cost" (tax burden, interest burden), a decomposition with many terms (DuPont), or any place the sign/direction is commonly flipped.

Kumar’s Style Refinements (observed from DERIVATIVES.md, Module 71.1)

- Numbered pointers first: Start module sections with a short, numbered list of key points in the user’s voice (direct, imperative, concise) before deeper callouts or examples.
- Callout casing: Match the file’s existing casing for callouts. If the file uses `[!QUESTION]` (uppercase) in that section, keep using uppercase there; otherwise use `[!question]`.
- Mixed math style: Reserve display LaTeX for core formulas/definitions. For simple identities (e.g., futures price = 100 − 100×MRR), prefer bold inline plain text in the numbered list. Keep LaTeX for BPV and any multi-step equations.
- One-line takeaways: After numericals, add a bold or plainly stated one-line conclusion (e.g., “Rate decline harms long more than equal rise helps”). Use the user’s terse phrasing.
- Tables for mechanics: When explaining margin mechanics (IM/MM/VM), include a compact Markdown table showing day-by-day flows and balances. Favor columns: Day, Settlement Price, IM, MM, VM, Balance, Margin Call, Balance After Top-up.
- Quick checks/tips: Keep a `[!tip] Quick checks` callout with 2–4 bullets of sanity checks tailored to the module’s numericals.
- Emphasis: Obsidian highlight `==…==` is allowed for high-salience lines within lists. Use sparingly to mirror the user’s pattern.
- Problem blocks: Use `[!question]`/`[!QUESTION]` with the simple structure the user favors:
  - Title line in caps when appropriate (e.g., “CONVEXITY ISSUE”).
  - “Problem:” line, a short `---` separator, then minimal steps/answer lines.
  - Keep currency/units simple and consistent with the surrounding file.
- Jargon and symbols: Prefer plain-language terms first (e.g., “market reference rate (MRR)”) and reuse short symbols only after defining them once in the section.
- Keep tone: Use the user’s assertive cues (e.g., “hammer this into your head”) where they already appear in that file; otherwise, keep the default concise tone.

Topic-Agnostic Pattern (Use Across All Sections)

- Corporate Issuers was the first topic completed; use it as the model for every other topic. Do not hardcode topic-specific content here.
- For any topic (e.g., Quant, Econ, Equity, Fixed Income, etc.), follow the same structure:
  - Add/maintain a top “[!tip] LOOK AT THESE BEFORE EXAM” section with:
    - Core formulas in display LaTeX and plain-language notation.
    - Big Gotchas, each with a one-line example.
    - Quick Checks (sanity checks before final answers).
  - For each module:
    - Keep the user’s original bullets intact; append missing info as separate bullets.
    - Include LOS lines under the module heading when available.
    - Add a “[!ABSTRACT] MEMORISE” callout with distilled points and key formulas.
    - Use display LaTeX for equations; add a “Notation in simple language” list when symbols appear.
    - Add numericals in “Problem → Solution → Explanation” format with display math for the main steps.
    - Add small exam tips/warnings as callouts where confusion is common.

Common Module Types (Guidance)

- Cost of Capital / Valuation modules:
  - Include WACC/weights, CAPM, DDM, preferred, after-tax debt; if relevant, unlever/relever beta.
  - Emphasize market-value target weights, marginal costs, currency/nominal-real consistency, flotation in cash flows.

- Capital Structure / Financing modules:
  - Cover MM I/II, taxes, distress costs, static trade-off, target structure, pecking order, signaling/agency.
  - Keep formulas in display LaTeX and prose simple; append-only.

- Real Options / Capital Allocation modules:
  - Provide accept-if-NPV≥0, NPV with option, expected NPV; list delay/expand/abandon/contract/switch/stage.
  - Include decision-tree numericals and brief explanations.

Top Exam Tip Section (at file start)

- Must include:
  - Core formulas (WACC, CAPM, DDM, preferred, after-tax debt, MM relations, trade-off, ROIC, trade credit discount cost).
  - Big Gotchas: each with a one-line example.
  - Quick Checks: weight sum, tax adjustment only on debt, next dividend in DDM, unit consistency, project risk vs hurdle.

Unicode and Encoding Fixes

- Detect literal `\uXXXX` sequences in Markdown with `rg -n -S "\\u[0-9a-fA-F]{4}"`.
- Replace them by decoding escapes to actual Unicode characters. Re-scan to confirm none remain.

Communication Style

- Preambles: 8–12 words, grouped by intent. Example: “Next, I’ll patch WACC formulas and add numericals.”
- Progress updates: short, momentum-building; use `update_plan` for multi-step work.
- Final messages: concise bullets; note files changed and offer next steps (e.g., run tests, add examples, commit?)
- Jargon rule: If you introduce jargon or an abbreviation, define it the first time in plain language, with a brief example when helpful.
- When referring to the instructional text or reading material in notes, call it the `curriculum`, not the `source`.

Do / Don’t Summary

- Do
  - Ask for escalation to read external PDFs.
  - Keep edits scoped and reversible.
  - Mirror the user’s callout/typography style.
  - Use display LaTeX and plain-language notation.
  - Add numericals with Problem/Solution/Explanation.

- Don’t
  - Delete or rewrite user’s original bullets unless explicitly requested.
  - Change unrelated sections.
  - Embed flotation costs in WACC or tax-adjust equity/preferred.
  - Mix currencies or real/nominal rates.

Quick Start Template

1) Scan for target section with `rg -n "^### MODULE X.Y" file.md`.
2) If needed, extract PDF text with:
   - `pdftotext -layout -nopgbrk "/path/to/file.pdf" out.txt`
   - `rg -n "keywords" out.txt`
3) Plan (`update_plan`), then patch (`apply_patch`).
4) Re-scan to verify, then summarize changes and ask for next steps.
