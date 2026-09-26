# EXAMPLES — Six Worked Descents

Each file in this folder is a complete, self-contained worked example following
one shape:

```
1. THEORY            what the starting equation is, and why it is exact
2. APPROXIMATION     every reduction named, typed, and costed
3. REDUCTION         the algebra, step by step, with no physics hidden
4. REDUCED MODEL     the engineering object that results
5. ENGINEERING EQN   a worked numerical problem and the design finding
6. VALIDITY LIMITS   a table of assumptions, failure conditions, and alternatives
```

Step 6 is not a formality. The book's central claim is that physics becomes
engineering in the right limits, and an example that does not state its limits
is not demonstrating the claim — it is asserting it.

| # | File | Descent | Chapters |
|---|---|---|---|
| 1 | [Dirac → Pauli](01%20Dirac-to-Pauli.md) | Relativistic spin-½ field theory → 2×2 magnetic Hamiltonian | Ch. 0, 3 |
| 2 | [Quantum → Thermodynamics](02%20Quantum-to-Thermodynamics.md) | Single-particle QM + quantisation → Gibbs distribution, equipartition, $U,pV=Nk_BT$ | Ch. 3, 6, 10 |
| 3 | [Maxwell → Circuit](03%20Maxwell-to-Circuit.md) | Maxwell's equations → transmission line → $R$, $C$, KCL/KVL | Ch. 11, 16, 17, 18 |
| 4 | [Heat Equation → Thermal RC](04%20Heat-Equation-to-Thermal-RC.md) | Energy conservation + Fourier's law → thermal network — and why it has no inductors | Ch. 15, 16, 17, 19 |
| 5 | [Navier–Stokes → Fluid Network](05%20Navier-Stokes-to-Fluid-Network.md) | Cauchy–Navier flow → pipe network, and why it is *not* a linear circuit | Ch. 13, 15, 16, 19, 20 |
| 6 | [Motor → Control System](06%20Motor-to-Control-System.md) | Two coupled ODEs → second-order $G(s)$ → PI loop → saturation limit | Ch. 17, 18, 19, 21 |

---

## What the set is designed to show

**A descent is a chain of typed reductions, not a single leap.** Every step
carries one of the five connection tags — `[DERIVATION]`, `[APPROXIMATION]`,
`[STRUCTURAL CONNECTION]`, `[ANALOGY]`, `[PHENOMENOLOGICAL]` — and the
distinction is load-bearing, not decorative:

- Example 1 shows a `[DERIVATION]` (Euler–Lagrange) immediately followed by two
  `[APPROXIMATION]`s that produce a *more useful* model. Usefulness went up;
  truth did not.
- Example 3 shows that three of four steps are exact and the entire descent
  rests on one inequality, $L/\lambda \ll 1$.
- Example 4 shows a model that is a genuine circuit and genuinely not an
  electrical circuit: first order, no inertia, one empirical coefficient.
- Example 5 shows that "Ohm's law for pipes" is the same algebra but a
  *nonlinear* network, because inertia survives as a quadratic term.
- Example 6 shows the chain working end to end, and the final design finding
  coming from the physics that the transfer function discarded.

**The tag `[PHENOMENOLOGICAL]` earns its place.** Examples 4, 5, and 6 all end
up depending on at least one coefficient that was fitted rather than derived
($h$, $f$, the friction curve). A book that claims everything reduces to
first principles would have to hide this. Naming it is the honest move, and it
is the boundary between physics and engineering practice.

---

## Model Ledgers

Every descent is recorded in the **Model Ledger** format defined in
[`../METADATA/00 Map.md`](../METADATA/00%20Map.md) — nine rows covering parent
theory, reduction, model, assumptions, retained physics, neglected physics,
validity, failure, and the next model. Ledgers appear in Chapters 3, 7, 13, 16,
17, 19, 20, and 21, and each example above points to the ledger for its own
descent.

The placement rule is deliberate: a Ledger is a record of a *reduction*, so
only chapters that actually reduce something carry one. Making the count
uniform across all twenty-two chapters would dilute the convention into
decoration.

---

## Sources

Numerical constants and empirical correlations used in these examples are
sourced in [`../REFERENCES.md`](../REFERENCES.md), tiered as [MEASURED],
[DERIVED / TEXTBOOK], or [SYNTHESIS].
