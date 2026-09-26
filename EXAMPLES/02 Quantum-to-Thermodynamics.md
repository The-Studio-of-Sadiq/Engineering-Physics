# Example 2 — Quantum → Thermodynamics

**A complete worked descent in six steps.**

**Source chapters:** [Ch. 3](../CHAPTERS/CHAPTER%203.md) (single-particle QM) →
[Ch. 6](../CHAPTERS/CHAPTER%206.md) (many-body, quantisation) → [Ch. 10](../CHAPTERS/CHAPTER%2010.md) §§10.2–10.6 (ensemble, Gibbs, entropy)

**Question answered:** Why do thermal physics and statistical mechanics follow
from quantum mechanics at all, rather than being a separate layer?

---

## Step 1 — Theory

A single quantum system is described by a state $|\psi\rangle$ evolving under
$\hat H$. The Schrödinger equation is deterministic and time-reversible: run it
backward and you recover the initial state exactly. Nothing in it produces
thermodynamics.

Thermodynamics needs three things the Schrödinger equation does not have:
**many** systems, a **large** number of degrees of freedom, and a **statistical
statement** about typical rather than particular outcomes.

---

## Step 2 — Approximation

Three approximations, in order of how much they cost:

| # | Reduction | Kind | What it assumes away |
|---|---|---|---|
| A | $N$ independent identical systems | `[APPROXIMATION]` | interactions between subsystems |
| B | Replace the microstate by an energy distribution | `[APPROXIMATION]` | which microstate is occupied |
| C | Equipartition: every quadratic degree of freedom carries $\tfrac12 k_BT$ | `[APPROXIMATION]` | anharmonicity, non-quadratic potentials |

Reduction A is the load-bearing one. **It is an approximation and it is a bad
one** — which is precisely why its failure is thermodynamically interesting. It
is good enough to derive the equipartition theorem and the ideal gas law, and
bad enough that its corrections (van der Waals, phase transitions) are the whole
of real thermodynamics.

---

## Step 3 — Mathematical reduction

Quantise $N$ independent one-particle levels $\epsilon_1,\dots,\epsilon_N$. A
microstate is an occupation assignment. The multiplicity of a configuration with
$n_i$ particles in level $i$:

$$W = \frac{N!}{\prod_i n_i!}$$

That is **all** statistical mechanics is at this stage: a counting statement
about integers. Gibbs entropy is the logarithm:

$$S = k_B \ln W$$

Maximise $S$ subject to fixed $N = \sum_i n_i$ and fixed $E = \sum_i n_i\epsilon_i$.
The method of Lagrange multipliers gives the **Boltzmann distribution**:

$$\frac{n_i}{N} = \frac{e^{-\beta\epsilon_i}}{Z},\qquad Z = \sum_i e^{-\beta\epsilon_i},\qquad \beta = \frac{1}{k_BT}$$

Note what did *not* appear. There is no appeal to probability axioms, no
assumption of randomness, and no time dynamics. Entropy maximisation under two
constraints is enough. The second law is a statement about where the maximum is.

---

## Step 4 — Reduced model

Equip the classical phase space with quantised levels and the distribution
becomes the continuous Maxwell–Boltzmann form:

$$f(E) = \frac{2}{\sqrt{\pi}}\frac{1}{(k_BT)^{3/2}}\sqrt{E}\,e^{-E/k_BT}$$

From here, two results follow in a few lines each.

**Equipartition.** For each independent quadratic term $\tfrac12 ax^2$ in the
Hamiltonian, $\langle x^2\rangle = k_BT/a$, so $\langle E\rangle = \tfrac12 k_BT$ per
term. With $f$ quadratic terms per particle, $U = \tfrac{f}{2}Nk_BT$.

**Ideal gas.** Substituting the level spacing $\epsilon_n = p^2/2m$ into $Z$ and
taking the continuum limit gives $pV = Nk_BT$, with $U = \tfrac32 Nk_BT$ (monatomic,
$f=3$).

**The macro-thermodynamics** follows by elimination: $p = -(\partial F/\partial V)_T$,
$S = -(\partial F/\partial T)_V$, $F = U - TS$ — the Gibbs free energy. Every
classical thermodynamic relation is a derivative of one scalar function.

---

## Step 5 — Engineering equation

**Worked problem.** 1.00 mol of monatomic ideal argon, initial state 300 K and
1.00 atm, compressed adiabatically and reversibly to 5.00 atm. Find the final
temperature, the work done on the gas, and $\Delta S$.

Reversible adiabatic means $S$ is constant, and for an ideal gas
$S = nC_V\ln T + nR\ln V + \text{const}$, so $TV^{\gamma-1} = \text{const}$
with $\gamma = C_P/C_V = 5/3$.

$$T_2 = T_1\left(\frac{P_1}{P_2}\right)^{(\gamma-1)/\gamma} = 300\left(\frac{1}{5}\right)^{0.4} = 300 \times 0.525 = 158\ \text{K}$$

$$W_{on} = \Delta U = nC_V(T_2 - T_1) = 1.00 \times 12.47 \times (158-300) = -1.77\ \text{kJ}$$

$$\Delta S = nC_V\ln\frac{T_2}{T_1} + nR\ln\frac{V_2}{V_1} = 0 \quad\text{(both terms cancel)}$$

Three engineering numbers, all from step 4, and the last one is a *check*: it is
zero because "reversible adiabatic" means exactly that. If a compressor model
returns $\Delta S \neq 0$, either the compression is irreversible or the model
is wrong.

**Design consequence.** Compressing gas is how a compressor is specified, and
the $T_2 = 157$ K outlet temperature is what forces intercooling. The whole
engineering rationale for multi-stage compression with intercooling falls out
of $\gamma$, which falls out of the equipartition count.

---

## Step 6 — Validity limits

| Assumption | Fails when | Consequence |
|---|---|---|
| Ideal gas, no interactions | High $P$, low $T$ | van der Waals; condensation |
| Independent subsystems | $N$ small, or interactions strong | quantum correlations, Bose/Fermi statistics |
| Boltzmann statistics | Degenerate gas, $n\lambda^3 \gtrsim 1$ | Fermi–Dirac or Bose–Einstein; the same partition function, different counting |
| Equipartition | Anharmonic potentials, low $T$ | frozen degrees of freedom; heat capacity falls below $\tfrac{f}{2}k_B$ |
| Equilibrium | Isolated system, integrable dynamics | non-ergodicity; microcanonical preparation required |

**The Bose/Fermi caveat is the important one.** Steps 1–4 assumed
$W = N!/\prod n_i!$, which is *Maxwell–Boltzmann* counting. It is valid only when
$\lambda = h/\sqrt{2\pi m k_BT} \ll$ mean interparticle spacing. When it fails,
the counting changes — and so does the distribution, while the thermodynamics
of $F = -k_BT\ln Z$ is unchanged. Same framework, different statistics. This is
why [Ch. 6](../CHAPTERS/CHAPTER%206.md) sits between quantum mechanics and
statistical mechanics in the architecture rather than after it.

**What this example demonstrates.** Thermodynamics is not a separate foundation
layered on top of quantum mechanics. It is a counting argument about a
large-number limit, and the entire classical apparatus is recoverable from one
constrained maximisation. The one place the story is genuinely incomplete is the
non-equilibrium case, which is why Chapter 10 ends at equilibrium.

---

**Model Ledger:** thermodynamics is a *reduction* of microscopic counting, so
its assumptions belong in a Ledger. See
[Ch. 10](../CHAPTERS/CHAPTER%2010.md) for the ensemble and free-energy
derivation these steps track.
