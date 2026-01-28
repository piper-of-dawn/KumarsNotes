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
