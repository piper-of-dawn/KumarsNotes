# AGENTS.md — KumarsNotes vault

This is a personal **Obsidian vault** tracked with git, not a software project. There is no build, test, lint, or package manifest. "Done" means the Markdown renders correctly inside Obsidian and follows the relevant style guide below.

## Nested AGENTS.md override this file

Read the nearest `AGENTS.md` before editing notes; deeper files win.

- `CFA Level II Notes/Corporate Issuers/AGENTS.md` — required style for any study note or worked numerical under `CFA Level II Notes/`. Enforces a single `## Variant:` heading, an abstract, a blockquote question, no further headers, `[!NOTE]` callouts, and a one-A4-page target.
- `Dark Arts/AGENTS.md` — style for research-paper summaries. It is gitignored (local-only, not pushed).
- Style benchmark for CFA numerical notes: `CFA Level II Notes/FIXED INCOME/Credit Default Swaps.md`. Match its structure when in doubt.

## Git is on auto-sync

- `.git-scripts/sync.sh` runs `git pull --rebase`, then `git add -A && git commit -m "auto-sync <ts>" && git push` whenever the tree is dirty.
- The `obsidian-git` plugin also auto-commits as `vault backup: <ts>`.
- Repo-wide `pull.rebase` is `true`; remote is `git@github.com:piper-of-dawn/KumarsNotes.git` (SSH).
- Commit your own work with a descriptive message before the sweeper hits it. Expect rebases, and don't be surprised by `vault backup:` / `auto-sync` commits in the log.

## Do not git-add these (gitignored)

`.obsidian/`, `*.pdf`, `WIP/`, `Diary/`, `Personal/`, `Archives/`, `ARCHIVES/`, `Cinematography/`, `Interviews/`, `*HSBC*/`, `PD LGD*`, `Dark Arts/AGENTS.md`.

- `.obsidian/workspace.json` is already tracked despite the ignore and changes on every edit — leave it alone; do not revert or "clean" it.

## Pushing rebuilds a public blog

A push to `master` fires `.github/workflows/rebuild-blog.yml`, which dispatches the `pages.yaml` workflow on `piper-of-dawn/blog`. A push therefore publishes. Do not push unless asked, and never push private or half-broken content.

## Obsidian math and formatting (vault-wide)

- Inline math `$...$`, display math `$$...$$`. Never use `\[ \]` or `\( \)`.
- The `transfer-latex-from-gpt-fix` plugin exists to convert pasted GPT LaTeX into MathJax — emit Obsidian-native math directly so no manual fix is needed.
- Use `\boxed{}` for key intermediate and final numeric answers (per the CFA guide).

## Paths

The repo lives under a Google Drive / Insync mount; the absolute path contains spaces and an `@`. Always quote paths.
