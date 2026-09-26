# Authoring *Engineering Physics: Top Down*

**This file is the standard for how this book is written.** It covers structure,
notation, epistemic stance, and the review checklist. It is not a contribution
workflow document

If anything here conflicts with `00 Map.md` or `README.md`, those two are
authoritative and the conflict here is a bug in this file.

---

## 1. The core principle: one chain, not a collection of essays

The spine is a single action, introduced in Chapter 0 and stated canonically in
Ch. 0 §0.10:

```
S_eff = S_EH + S_SM + S_unknown
      = ∫ d⁴x √(−g) [ R/16πG + ℒ_SM + ℱ[g, φ?, new fields, topology, …] ]
```

**Every major result must identify its physical or mathematical provenance.**
Where a genuine descent from this framework exists, show it and name the step.
Where one does not, say so and label the result `[PHENOMENOLOGICAL]`,
`[STRUCTURAL CONNECTION]`, `[ANALOGY]`, or a constitutive correspondence.

An earlier draft of this rule said *every* chapter must connect back to the
master action. That was too strong, and it was wrong in a way that mattered:
Ch. 13's engineering correlations, Ch. 19's thermofluid property fits, and
Ch. 20's open-channel formulas are `[PHENOMENOLOGICAL]` or empirical. Forcing
them into a descent would have manufactured derivations that do not exist. The
book's own epistemic taxonomy already recognises this; the rule now matches it.

Concretely:

- Before writing a section, identify **which term of the master action it
  descends from and which named bridge gets you there** (Bridge A, Bridge
  B.a–B.e, Bridge C — see §7) — *or* identify why no such descent exists and
  tag it accordingly.
- When you introduce a new equation, state in prose what was discarded to get it
  and why discarding it was legitimate. The recurring question every chapter must
  answer somewhere: **"What did we throw away to get here, and why were we
  allowed to?"**
- When two results *look* structurally similar but are not the same derivation
  (the Higgs mechanism, Landau theory, ferromagnetism, superconductivity, and
  hysteresis all sharing a Mexican-hat potential), say so as an explicit
  `[STRUCTURAL CONNECTION]` thread. Do not imply a literal genealogy. **This
  distinction has caused real errors in review and must not recur.**
- Cross-reference by chapter and section number, always (§7). A chapter that
  does not cite where its starting equation came from is incomplete.

The five cross-layer threads to maintain: **Noether's theorem, symmetry breaking
(Mexican-hat potential), the action principle, topology, and the wave/diffusion
dichotomy**.

### 1.1 Four kinds of "same"

The single most common failure mode in a book like this is using one word —
"identical", "the same", "is just" — for four different relationships. Chapter
20 §20.0.1 names them, and the distinction is used throughout:

| Kind | Shared | Not shared | Chapter 20 example |
|---|---|---|---|
| **Mathematical identity** | the equation, term by term, once assumptions hold | nothing | Terzaghi consolidation ≡ 1D heat equation |
| **Constitutive correspondence** | the algebraic form, reached independently | derivation, closure, coefficients | Darcy's law ≅ Fick's law in form |
| **Shared statistical origin** | a statistical-mechanical structure | the macroscopic law built on it | Arrhenius ≅ Boltzmann factor |
| **Shared dimensionless framework** | how dimensionless groups organise design | driving forces, equilibria, performance | NTU for columns ≅ NTU for exchangers |

"The word *identical* appears only for the first kind." The other three are named
for what they are.

---

## 2. Notation and the tagging system

Because "connect everything into one chain" invites overclaiming, every
non-trivial connection between two results carries one of five tags:

- `[DERIVATION]` — a literal mathematical step follows from the previous
  equation via a named, checkable limit or substitution.
- `[APPROXIMATION]` — a term is dropped or a limit taken. **State the small
  parameter and the regime of validity.** An unlabelled approximation is a
  defect.
- `[STRUCTURAL CONNECTION]` — two results share mathematical form but one is
  **not** derived from the other.
- `[ANALOGY]` — a pedagogical comparison with no claimed formal equivalence.
- `[PHENOMENOLOGICAL]` — an empirical relation used as-is, not derived from the
  master action.

Use these consistently. Do not invent new tag categories without revising this
section first.

### 2.1 Model Ledgers

Tags classify a **connection**. The **Model Ledger** classifies a **model**.

Wherever a chapter performs a major model transition — a PDE becoming an ODE, a
field equation becoming a lumped circuit, a full model becoming a
linearisation — it records the transition in a fixed nine-row table:

| Field | Content |
|---|---|
| Parent theory | the equation it descends from, with chapter/section |
| Reduction | the specific approximations applied |
| Model | the resulting reduced equation |
| Assumptions | enumerated, including those inherited silently |
| Physics retained | what survives |
| Physics neglected | what does not — this row is the honest one |
| Validity | the regime where the model is trustworthy |
| Fails when | the specific condition, not "outside its domain" |
| Next model | what to use when it fails |

**Placement rule.** One Ledger per major model transition — not one per
equation, and not one per chapter. Chapters carrying Ledgers: **3, 7, 13, 16,
17, 19, 20, 21**. A chapter that only establishes, catalogues, or surveys has not
reduced anything, and adding a Ledger to it would dilute the convention into
decoration.

---

## 3. Formatting rules

LaTeX must be portable. Display math uses `$$ ... $$`, inline math uses
`$ ... $`.

1. **Markdown is the source of truth.** Never treat a word-processor export as
   canonical — round-trips have corrupted LaTeX before, silently turning
   underscores into asterisks.
2. **No `\[ \]`, no `\( \)`, no `equation`/`align` environments, no
   package-dependent macros, no `\newcommand`.** These break on import into
   most Markdown/LaTeX pipelines and render as literal source.
3. **Never number equations.** No `\tag{}`, no `\label{}`/`\ref{}`, no `(1)`,
   `(2)` style numbering. Reference equations in prose by chapter and section —
   *"the action from Ch. 0 §0.3"*, not *"Eq. (3)"*. Numbering is the single
   most common cause of broken rendering.
4. **Escape LaTeX specials even in obvious places.** A literal `%` inside a math
   span is a *comment* in LaTeX and will silently swallow the rest of the
   expression. Write `\%`. This has bitten the manuscript more than once: a
   quantity like `$\alpha^2 \approx 0.005\%$` lost its backslash and became an
   equation that rendered as nothing after the decimal point.
5. **Thin spaces are `\,` and they are not optional.** `C(s),e(s)` and
   `C(s)\,e(s)` are different expressions; so are `12.9\mu V` and `12.9\,\mu V`.
   Before submitting, scan your own new equations for bare `,` and `;` where a
   thin space belongs.
6. **Matrix row separators are `\\`.** A single `\` renders as garbage, and the
   failure is invisible in plain text — check `pmatrix`, `bmatrix`, `vmatrix`,
   and `cases` environments specifically.
7. **Verify rendering before considering the section done.** Paste the equations
   into a blank Markdown preview and confirm each one renders as intended.

---

## 4. Chapter structure

Every chapter follows this skeleton:

- Chapter number and title
- Epigraph
- **§X.0 — Overview**: where we are, what this chapter does, what it assumes
- Numbered sections (`§X.1`, `§X.2`, …) with derivations, interpretation, tables
- **§X.N — Summary**: a table of results, each with its origin
- **§X.(N+1) — Engineering Thread**: physics results mapped to concrete
  engineering applications
- **§X.(N+2) — Looking Ahead**: what comes next and why it follows
- Closing: `End of Chapter X`, then `Next: Chapter Y — Title`

Do not skip the Engineering Thread or Looking Ahead sections. They are what
make the single-chain structure legible, not optional polish.

---

## 5. Prose style

- Full textbook prose. Paragraphs, not fragments. Not bullet skeletons.
- Tone: a professor who has thought carefully about why the standard bottom-up
  teaching order is pedagogically wrong, and is directly correcting it. Honest,
  direct, precise. Never breezy, never hand-wavy.
- **No bluffing.** If something is unknown or unresolved, say so. Never claim
  confirmation the physics does not support.
- Never write "it can be shown that" without either showing it or stating where
  it is shown.
- **Name every approximation**, with its small parameter and its regime.
- One consistent voice across all chapters. Register drift — one section at
  introductory level, the next in unexplained tensor notation — is a real defect.

---

## 6. Epistemic stance

The book does **not** claim that a Lagrangian Theory of Everything is proven or
established. The correct framing, to be preserved in spirit wherever this comes
up:

> "If a Theory of Everything exists, we have overwhelming reason to expect it will
> appear in this form."

Do not write language implying the master action has been confirmed. Do not
present the hierarchy of approximations as a proven derivation chain where a
structural connection is what is actually meant.

The same discipline applies to the book's own load-bearing claims. Three of them
are **synthesis** rather than sourced fact, and must be labelled that way
wherever they appear:

1. the convergence thesis (Ch. 13) — Ohm, Fourier, Fick, and viscosity within a
   common linear-response framework, with Hooke's law appearing as a static
   susceptibility (zero-frequency limit) rather than an ordinary transport
   coefficient
2. the Mexican-hat cross-thread (Ch. 10, Ch. 21) — Higgs, BCS, and Landau as
   instances of one template
3. the four-way correspondence classification (Ch. 20 §20.0.1)

These are the book's contribution. A synthesis claim wearing a textbook
citation is the failure mode this rule exists to prevent. See
[`REFERENCES.md`](REFERENCES.md) for the tiering scheme.

---

## 7. Cross-chapter referencing

- Always by chapter and section: `Ch. 3 Bridge A`, `Ch. 0 §0.7`, `Ch. 8 §8.4`.
- **"will be developed in Ch. X"** forward; **"from Ch. X §Y.Z"** backward.
- The named bridges are fixed: **Bridge A** (Dirac → Schrödinger),
  **Bridge B.a** ($\hbar \to 0$), **Bridge B.b** ($N \to \infty$), remaining
  Bridge B sub-paths as defined in `00 Map.md`, and **Bridge C** (continuum →
  engineering limits).
- The phenomena catalogue (Ch. 2) uses **final** chapter numbers. If chapter
  numbering changes, update it in the same pass.

---

## 8. Design decisions — do not reverse these silently

- **Ch. 0 before Ch. 1.** Ch. 0 gives the full equation; Ch. 1 teaches the
  machinery that explains why it works. Deliberate.
- **The unknown sector `ℱ[…]` is never dropped.** The action is always written
  with all three sectors — $S_{EH}$, $S_{SM}$, $S_{\text{unknown}}$ — or with
  an explicit statement about $\mathcal{F}$. Writing $S_{EH} + S_{SM}$ alone is
  a silent claim that the unknown sector is empty.
- **Never write the unknown sector as $f(\phi)R$.** That form asserts the missing
  physics is a scalar times the Ricci scalar, which nothing supports.
  $\mathcal{F}[\ldots]$ is a placeholder for an unknown *sector*, not a
  functional form. This supersedes earlier drafts that used `f(φ)`.
- **Pauli exclusion is a theorem, not a postulate**, derived from fermion-field
  anticommutation in Ch. 0 and carried into Ch. 5. Do not reintroduce it as an
  axiom.
- **The Born rule remains a foundational probabilistic postulate of standard
  quantum mechanics.** It is *not* derived in this book, and no design decision
  may be reversed to make it look as though it were. What U(1) symmetry and
  Noether's theorem *do* give (Ch. 3 §3.9.2) is a conserved current of
  $|\psi|^2$, so that probability conservation follows from charge conservation
  *once the Born postulate is adopted*. That arrow runs one way. Never write the
  reverse — "the Born rule is Noether's theorem" is false, and it is the single
  most common error in "everything is symmetry" treatments of QM.
- **The periodic table is derived** term by term from Aufbau, Hund's rule, and
  the four quantum numbers in Ch. 5.
- **Newton's law is presented as GR's weak-field limit.** Ch. 8 derives it; Ch.
  9 assumes the reader has seen that.
- **Ch. 13 is the convergence chapter.** Do not fork discipline-specific
  derivations elsewhere that duplicate it.
- **Bridge zones are chapters in their own right** and must be as rigorous as
  any other chapter.
- **The architecture is frozen at Chapters 0–21 plus the Epilogue.** This is
  settled, not provisional. There is no Chapter 22.

---

## 9. Files and naming

- Chapters: `CHAPTERS/CHAPTER N.md`, N = 0…21.
- Metadata: `METADATA/00 Map.md`, `METADATA/EPILOGUE.md`.
- Provenance: `REFERENCES.md` (root — the single source of truth for sources;
  `METADATA/Reference.md` is a pointer, not a second copy).
- Worked examples: `EXAMPLES/`, each following the six-step shape documented in
  `EXAMPLES/README.md`.
- Landing page: `README.md`.
- Any new top-level file requires updating `00 Map.md` and `README.md` in the
  same pass.

---

## 10. Review checklist

Before a section is considered done:

- [ ] Every connection to another result carries one of the five tags (§2)
- [ ] Every major model transition has a nine-row Model Ledger (§2.1)
- [ ] Every dropped term is named, with its small parameter and regime
- [ ] No unescaped `%`, no bare `,` or `;` where `\,` belongs, no single `\`
      in a matrix environment (§3, items 4–6)
- [ ] No equation numbering; all cross-references by chapter and section
- [ ] Synthesis claims labelled as synthesis (§6)
- [ ] Summary table gives each result its origin
- [ ] Engineering Thread and Looking Ahead present
- [ ] All equations render correctly in preview

---

## 11. Known open items

Not defects. Recorded so they are not rediscovered as bugs:

- Chapter-level §-number pinning in `REFERENCES.md` needs a re-verification pass
  after the Ch. 7, 13, and 20 rewrites.
- Several named engineering correlations in Ch. 16, 17, 19, 20 are
  domain-sourced to a textbook but not pinned to a page.
- Non-equilibrium statistical mechanics is out of scope; Ch. 10 ends at
  equilibrium.
- The taxonomy of *why* a `[STRUCTURAL CONNECTION]` exists is stated in
  Ch. 20 §20.0.1 but is not yet propagated as a standalone section.
