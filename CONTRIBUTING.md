# Contributing to *Engineering Physics: Top Down*

*Engineering Physics: Top Down* derives engineering science from fundamental physics — descending from the Standard Model Lagrangian combined with the Einstein–Hilbert action, through named, explicit approximations, down to the classical engineering results used by EEE, ME, CE, and ChE students. This document is the single source of truth for how to write, format, and submit content so that every chapter reads as one continuous, disciplined argument rather than a collection of independent notes.

If anything here conflicts with an instruction given elsewhere, this file wins. If it conflicts with the repo's `00 Map.md` or `README.md`, treat that as a bug and open an issue.

---

## 1. Core principle: this is one chain, not a collection of essays

The book's spine is a single equation, introduced in Chapter 0:

```
S = ∫ d⁴x √(−g) [ f(φ) R + ℒ_SM ]
```

Every chapter, bridge, and thread must connect back to this action through an explicit, named step — either a literal mathematical limit (a derivation) or an explicitly labeled structural analogy. There are no free-floating results.

Concretely, this means:

- Before writing a section, identify **which term in the master action it descends from**, and **which named bridge or limit gets you there** (Bridge A, Bridge B.a–B.e, Bridge C — see §7).
- When you introduce a new equation, state in prose what was thrown away to get it and why that throwing-away was legitimate. The recurring question every chapter must answer somewhere is: **"What did we throw away to get here, and why were we allowed to?"**
- When two results *look* structurally similar but are not literally the same derivation (e.g., the Higgs mechanism, Landau theory, ferromagnetism, superconductivity, and hysteresis all sharing a Mexican-hat potential), you must say so as an **explicit structural-connection thread**, not imply a literal genealogy. See the tagging system in §6 — this distinction has already caused real errors in review and must not recur.
- Cross-reference by chapter and section number, always (§7). A chapter that doesn't cite where its starting equation came from is incomplete.

The five cross-layer threads that must be maintained and pointed back to whenever they recur are: **Noether's theorem, symmetry breaking (Mexican-hat potential), the action principle, topology, and the wave/diffusion dichotomy**.

---

## 2. Formatting rules (non-negotiable)

These exist because the book is drafted and reviewed in Google Docs, and violations have broken real files in the past.

1. **All content is written and submitted as `.md` (Markdown) files.** No `.docx` drafts as the source of truth — `.docx` round-trips have previously corrupted LaTeX (underscores silently became asterisks).
2. **LaTeX must be Google-Docs-importable.** Use inline math with single dollar signs, `$ ... $`, and display math with double dollar signs, `$$ ... $$`. Do not use `\[ \]`, `\( \)`, `equation`/`align` environments, or any LaTeX package-dependent macros — Google Docs' equation editor does not support them and the import will silently break or drop the equation.
3. **Never use equation numbering.** No `\tag{}`, no `\label{}`/`\ref{}`, no `(1)`, `(2)` style numbering. This is a hard rule: numbered-equation syntax is exactly what breaks LaTeX rendering on import into Google Docs. If an equation needs to be referenced later, refer to it in prose by chapter and section: *"the action from Ch. 0 §0.3"*, not *"Eq. (3)"*.
4. Keep LaTeX expressions in standard, portable notation (`\hbar`, `\nabla`, `\partial`, Greek letters via `\alpha`, `\beta`, etc.) and avoid custom macro definitions (`\newcommand`) — they don't survive the Docs import either.
5. Before submitting, mentally (or literally) paste your equations into a blank Google Doc using the equation-import path the project uses, and confirm every equation renders. A chapter is not done until this check has been done.

---

## 3. Chapter structure template

Every chapter follows this skeleton:

- Chapter number and title
- Epigraph (one or two relevant quotes)
- **§X.0 — Overview**: where we are in the book, what this chapter does, what prerequisites it assumes
- Numbered sections (`§X.1`, `§X.2`, …) containing derivations, physical interpretation, and tables
- **§X.N — Summary**: a table of results, each with its origin (which equation/limit it came from)
- **§X.(N+1) — Engineering Thread**: a table mapping physics results to concrete engineering applications
- **§X.(N+2) — Looking Ahead**: what comes next and why it follows from this chapter
- Closing line: `"End of Chapter X"` followed by `"Next: Chapter Y — Title"`

Do not skip the Engineering Thread or Looking Ahead sections — they are what make the "single chain" structure legible to the reader, not optional polish.

---

## 4. Prose style

- Full textbook prose — not lecture notes, not bullet skeletons. Paragraphs, not fragments.
- Tone: a professor who has thought carefully about why the standard (bottom-up) teaching order is pedagogically wrong, and is directly correcting it. Honest, direct, precise — never breezy, never hand-wavy.
- **No bluffing.** If something is unknown or genuinely unresolved (e.g., whether a Lagrangian ToE exists at all), say so explicitly. Never claim confirmation the physics doesn't support.
- Never write "it can be shown that" without either showing it or explicitly stating why the derivation is being deferred (and where it will be shown, if it will).
- Name every approximation. "We take the limit ħ → 0" is not enough on its own — say what this discards and what regime that's valid in.
- Maintain one consistent voice across all chapters. Do not let register drift between chapters (this was a real defect found in prior source material — some sections read at introductory level while adjacent sections used full tensor notation with no bridge between them).

---

## 5. Epistemic stance — read this before writing anything about the master equation

The book does **not** claim the Lagrangian form of a Theory of Everything is proven or established. The correct framing, to be preserved verbatim in spirit wherever this comes up, is:

> "If a Theory of Everything exists, we have overwhelming reason to expect it will appear in this form."

Do not write language implying physicists have "confirmed" this. Do not present the book's own hierarchy of approximations as a literal, proven derivation chain where a structural analogy is what's actually meant — mark it as an analogy (§6). This distinction has been the single most common category of correction in review so far; treat it as the thing most likely to get your submission sent back.

---

## 6. Notation / tagging system

Because "connect everything into one chain" can tempt a writer into overclaiming a literal derivation where only a structural resemblance exists, every non-trivial connection between two results must be tagged with one of the following, as a blockquote:

- `[DERIVATION]` — a literal mathematical step follows from the previous equation via a named, checkable limit or substitution.
- `[APPROXIMATION]` — a term is dropped or a limit taken; state the small parameter and the regime of validity.
- `[STRUCTURAL CONNECTION]` — two results share mathematical form (e.g., a Mexican-hat potential appearing in the Higgs mechanism, Landau theory, ferromagnetism, and superconductivity) but one is **not** derived from the other. Use this instead of implying a literal genealogy.
- `[ANALOGY]` — a pedagogical comparison with no claimed formal equivalence.
- `[PHENOMENOLOGICAL]` — an empirical relation used as-is, not derived from the master action in this book.

Use these tags consistently; do not invent new tag categories without discussing it first.

---

## 7. Cross-chapter referencing

- Always reference by chapter and section number: `"Ch. 3 Bridge A"`, `"Ch. 0 §0.7"`, `"Ch. 8 §8.4"`.
- Use **"will be developed in Ch. X"** for forward references, and **"from Ch. X §Y.Z"** for backward references.
- The named bridges are fixed and must be referred to by name, not improvised: **Bridge A** (Dirac → Schrödinger, relativistic → non-relativistic QM), **Bridge B.a** (ħ → 0, QM → classical mechanics), **Bridge B.b** (N → ∞, statistical mechanics/thermodynamics), remaining Bridge B sub-paths as defined in `00 Map.md`, and **Bridge C** (continuum/engineering-systems limits — transmission line, Euler–Bernoulli beam, etc.).
- The phenomena catalogue (Ch. 2) cross-references use **final** chapter numbers — if chapter numbering changes, that catalogue must be updated in the same pass.

---

## 8. Key design decisions — do not reverse these without raising it first

- **Ch. 0 before Ch. 1**: Ch. 0 gives the full equation first (the blueprint). Ch. 1 then teaches the mathematical machinery (why the blueprint works). This ordering is deliberate.
- **`f(φ)` is never dropped.** The action is never written without the `f(φ)` placeholder — this is the book's honest acknowledgment of an open question, not a simplification to be cleaned up.
- **Pauli exclusion is a theorem, not a postulate** in this book — it must be shown to derive from fermion-field anticommutation in Ch. 0, and that thread must be carried into Ch. 5, not re-introduced as an axiom.
- **The Born rule is Noether's theorem**, not a separate postulate — established in Ch. 3 via U(1) charge conservation. Don't reintroduce it elsewhere as an independent axiom.
- **The periodic table is derived**, term by term, from Aufbau + Hund's rule + the four quantum numbers in Ch. 5 — not asserted or hand-waved as "explained by QM."
- **Newton's law is presented as GR's weak-field limit** (Ch. 8 derives it; Ch. 9 assumes the reader has already seen that derivation) — never re-introduced as an independent law.
- **The Generalized Transport Law (Kubo formula, Ch. 13) is the convergence chapter**: Ohm's law, Fourier's law, Fick's law, Newtonian viscosity, and Hooke's law all fall out of one calculation. This is what makes the book branch-agnostic; don't fork discipline-specific derivations elsewhere that duplicate this.
- **Bridge zones are not optional connective tissue** — they are chapters in their own right and must be as rigorously written as any other chapter.

If you think one of these should change, open an issue describing the physics or pedagogical reason before rewriting the relevant chapters.

---

## 9. File and naming conventions

- Filenames: `CHAPTER N.md` (matching the existing repo pattern), or when drafting outside the repo, `chapter-0X-descriptive-name.md`.
- The repo's canonical structure is: `00 Map.md` (the layer map: Layers 0–3, Bridges A/B/C, cross-layer threads), `CHAPTER 0.md` through `CHAPTER 21.md`, `EPILOGUE.md`, `README.md`.
- Do not introduce a new top-level file without updating `00 Map.md` and `README.md` in the same submission.

---

## 10. Workflow for contributing a chapter or edit

1. **Review before you write.** Read `00 Map.md`, the relevant chapter(s) adjacent to yours, and any open reviewer-feedback items in the repo issues. Confirm which master-action term and which named bridge your content descends from.
2. **Draft in Markdown**, following §§2–7 above.
3. **Self-check against §5 and §6** — look specifically for places where you've implied a literal derivation chain and mark them `[STRUCTURAL CONNECTION]` if that's what they actually are.
4. **Verify every equation imports cleanly into Google Docs** with no numbering and no unsupported macros (§2, item 5).
5. **Open a pull request** with a short note on: which chapter/section this touches, which master-action term and bridge it connects to, and any design decisions from §8 it interacts with.
6. **Review happens in two passes**, matching how this project has been reviewed so far:
   - **Round 1 — physics correctness**: is every derivation, limit, and claimed connection actually true?
   - **Round 2 — repo hygiene and rigor**: chapter-numbering consistency, missing disclaimers, unlabeled connection chains, notation-tag coverage, cross-reference correctness.
7. Fixes are prioritized P0–P3 by severity (P0 = factual/physics error, up through P3 = polish). Address P0/P1 items before P2/P3 in any given pass.

---

## 11. Known deferred items (not blockers, don't re-raise as bugs)

The following are intentionally deferred and are not omissions needing a fix:

- Full references/bibliography
- A per-major-equation "Model Ledger" beyond what's already demonstrated
- Worked-example sets and diagrams (planned, not yet in scope)
- README trim / GitHub metadata polish
- The chapter-count freeze at 21 + Epilogue is intentional, not provisional

If you want to pick one of these up, say so in an issue first so effort isn't duplicated.

---

## 12. Questions

If a formatting rule and a content rule seem to conflict (e.g., you genuinely need to number something), open an issue rather than improvising — equation numbering in particular has broken real files before and the fix is always to restructure the reference as prose (§7), not to add numbering back.
