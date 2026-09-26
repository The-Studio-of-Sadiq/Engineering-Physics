# CHAPTER 10
# Bridge B.b — Statistical Mechanics and Thermodynamics
### The $N \to \infty$ Descent: How the Four Laws Emerge from Counting

---

> *The second law of thermodynamics is, without a doubt, one of the most perfect laws in physics.*
> *Any reproducible violation of it, however small, would bring the discoverer great fame and*
> *probably a Nobel Prize. Yet all we have is a deep sense that the law is correct.*
> — Josef Loschmidt (paraphrased), 1876
>
> *The reason is simply that there are far more ways for a system to be disordered*
> *than ordered. Entropy increases because the universe is doing statistics.*
> — modern response

---

## 10.0 — Bridge B.b in Context

Chapter 9 performed Bridge B.a: taking $\hbar \to 0$ on quantum mechanics to
recover classical mechanics. This chapter performs Bridge B.b: a completely
different operation on the same quantum mechanics — taking $N \to \infty$
and averaging over microscopic degrees of freedom.

**The two operations are independent and produce different physics:**

| Bridge | Operation | Produces | Chapter |
|---|---|---|---|
| B.a | $\hbar\to 0$ | Classical mechanics | 9 |
| **B.b** | $N\to\infty$, ensemble average | **Statistical mechanics + thermodynamics** | **10 (this)** |
| B.c | Classical U(1) field limit | Maxwell's equations | 11 |
| B.d | Weak-field metric | Newtonian gravity | 8 |
| B.e | Kubo + quantum scattering | Generalized transport law | 13 |

The deep point: **you can take these limits in any order.** Classical statistical
mechanics applies Bridge B.a first (to get classical trajectories), then Bridge B.b
(to average over them). Quantum statistical mechanics applies Bridge B.b directly
to the quantum system, without Bridge B.a. This chapter does the latter — the
more fundamental approach — and recovers classical thermodynamics as a further
limiting case.

**The organizing question:** When you have $N \sim 10^{23}$ quantum particles
and you cannot possibly track every quantum number, what can you say?
Answer: exactly as much as an engineer needs.

---

## 10.1 — The Density Matrix: Describing What We Don't Know

### 10.1.1 — Pure States and Mixed States

A **pure state** $|\psi\rangle$ is a complete quantum mechanical description —
every property of the system is determined (up to measurement). The density
matrix of a pure state:

$$\hat\rho = |\psi\rangle\langle\psi|$$

has the property $\hat\rho^2 = \hat\rho$ (it is a projector).

A **mixed state** describes a statistical mixture of pure states — it is what
you use when you know the system is in one of several states $|n\rangle$,
with probabilities $p_n$, but you don't know which one:

$$\boxed{\hat\rho = \sum_n p_n|n\rangle\langle n|, \qquad p_n \geq 0, \qquad \sum_n p_n = 1}$$

A mixed state has $\hat\rho^2 \neq \hat\rho$; equivalently $\text{Tr}(\hat\rho^2) < 1$.

**Why we need mixed states for thermodynamics:** A hot gas in a box is not
in a pure state. It is in a statistical ensemble of energy eigenstates with
Boltzmann probabilities. You don't know (and couldn't measure) which exact
configuration the $10^{23}$ atoms are in. The density matrix encodes that ignorance.

### 10.1.2 — The Von Neumann Equation

The equation of motion for the density matrix (the quantum Liouville equation):

$$\boxed{\frac{\partial\hat\rho}{\partial t} = -\frac{i}{\hbar}[\hat H, \hat\rho]}$$

This is the quantum analog of the classical Liouville equation
$\partial\rho/\partial t + \{H,\rho\}_{Poisson} = 0$ from Ch. 9 §9.6.2.
The Poisson bracket has been replaced by $(-i/\hbar)\times$commutator —
the canonical quantization rule (Ch. 1 §1.6.4) applied consistently.

**Expectation values** of any observable $\hat A$:
$$\langle\hat A\rangle = \text{Tr}(\hat\rho\hat A)$$

This works for both pure and mixed states. Thermodynamics is the study of
expectation values of macroscopic observables (energy, pressure, magnetization,
etc.) in the $N\to\infty$ limit.

### 10.1.3 — The Reduced Density Matrix and Decoherence

Consider a system $S$ coupled to an environment $E$ (thermal reservoir). The
total density matrix $\hat\rho_{SE}$ evolves under the combined Hamiltonian
$\hat H = \hat H_S + \hat H_E + \hat H_{int}$.

The **reduced density matrix** of $S$ alone:
$$\hat\rho_S = \text{Tr}_E(\hat\rho_{SE})$$

is obtained by tracing out the environment's degrees of freedom. This operation:
- Destroys the off-diagonal elements of $\hat\rho_S$ in the energy eigenbasis
  → decoherence (Ch. 9 §9.4.2)
- Produces a mixed state even if $\hat\rho_{SE}$ was initially pure
- Converts the quantum Liouville equation into the **Lindblad master equation**
  (introduced in Ch. 0 §0.2 context) with dissipation terms from the environment

**This is the mathematical operation of Bridge B.b:** tracing out environmental
degrees of freedom converts the pure, reversible quantum dynamics into the
irreversible statistical mechanics of the reduced system. Irreversibility is
not put in by hand — it emerges from the $N\to\infty$ environmental degrees
of freedom.

---

## 10.2 — Von Neumann Entropy: Quantifying Ignorance

### 10.2.1 — Definition

The **von Neumann entropy** of a density matrix $\hat\rho$:

$$\boxed{S = -k_B\text{Tr}(\hat\rho\ln\hat\rho) = -k_B\sum_n p_n\ln p_n}$$

where the last form uses the eigenvalues $p_n$ of $\hat\rho$.

**Properties:**
- $S \geq 0$, with $S = 0$ iff $\hat\rho$ is a pure state ($p_n = 1$ for one $n$, zero otherwise)
- $S$ is maximized for the uniform distribution: $p_n = 1/\mathcal{N}$ for all $\mathcal{N}$ states, giving $S_{max} = k_B\ln\mathcal{N}$
- $S$ is invariant under unitary evolution: $d S/dt = 0$ under the von Neumann equation
- This last property means entropy **cannot increase** under closed quantum dynamics —
  irreversibility requires the coupling to an environment (§10.1.3)

### 10.2.2 — Connection to Boltzmann

For a classical system of $N$ particles with $\Omega$ accessible microstates:

$$S = k_B\ln\Omega$$

This is **Boltzmann's formula** (carved on his tombstone). It is the classical
limit of the von Neumann entropy for a uniform distribution over $\Omega$ states.

**What is a microstate?** In quantum mechanics: a specific eigenstate of the
full Hamiltonian. In classical statistical mechanics: a point in phase space.
The number of accessible microstates $\Omega$ grows astronomically with energy
and particle number — the central fact underlying the second law.

---

## 10.3 — The Maximum Entropy Principle: Temperature Emerges

### 10.3.1 — The Constrained Optimization

**Problem:** An isolated system has fixed total energy $\langle\hat H\rangle = U$.
What is the equilibrium density matrix $\hat\rho_{eq}$?

**Answer:** The one that maximizes $S = -k_B\text{Tr}(\hat\rho\ln\hat\rho)$
subject to:
- $\text{Tr}(\hat\rho) = 1$ (normalization)
- $\text{Tr}(\hat\rho\hat H) = U$ (fixed average energy)

Use Lagrange multipliers $\lambda_0$ (for normalization) and $\beta$ (for energy):

$$\frac{\partial}{\partial\hat\rho}\left[-k_B\text{Tr}(\hat\rho\ln\hat\rho) - \lambda_0\text{Tr}(\hat\rho) - \beta\text{Tr}(\hat\rho\hat H)\right] = 0$$

Result: $-k_B(\ln\hat\rho + \mathbf{1}) - \lambda_0\mathbf{1} - \beta\hat H = 0$

$$\boxed{\hat\rho_{eq} = \frac{1}{Z}\,e^{-\beta\hat H}, \qquad Z = \text{Tr}(e^{-\beta\hat H})}$$

This is the **canonical ensemble density matrix**. The normalization factor
$Z$ is the **partition function** — one of the most powerful objects in physics.

### 10.3.2 — Temperature as a Lagrange Multiplier

The Lagrange multiplier $\beta$ enforces the energy constraint. Comparing with
thermodynamics (to be derived in §10.4), $\beta$ equals:

$$\beta = \frac{1}{k_BT}$$

**Temperature is the Lagrange multiplier for energy in the maximum-entropy
optimization.** It is not a fundamental concept — it is the parameter that
controls the average energy of a system in contact with a reservoir. Two systems
in thermal equilibrium share the same $\beta$ — which is the thermodynamic
zeroth law, derived rather than postulated.

### 10.3.3 — The Boltzmann Distribution

In the energy eigenbasis $\hat H|n\rangle = E_n|n\rangle$:

$$p_n = \frac{e^{-\beta E_n}}{Z}, \qquad Z = \sum_n e^{-\beta E_n}$$

The probability of finding the system in state $n$ decreases exponentially
with energy — the **Boltzmann distribution**. This is not a postulate; it is
the maximum-entropy distribution subject to fixed average energy.

**The Boltzmann factor $e^{-E/k_BT}$** is the most important factor in
statistical mechanics. It appears in:
- Chemical reaction rates (Arrhenius: $k \propto e^{-E_a/k_BT}$)
- Carrier concentrations in semiconductors ($n \propto e^{-E_g/2k_BT}$, Ch. 6)
- Vacancy concentrations in crystals ($c_v \propto e^{-E_f/k_BT}$)
- Rate of radioactive decay products (nuclear systematics)
- Every thermally activated process in materials science

All of these are the same Boltzmann factor, applied to different activation
energies. A student who understands §10.3 understands all of them at once.

---

## 10.4 — Thermodynamic Quantities from the Partition Function

All thermodynamic quantities follow from $Z = \text{Tr}(e^{-\beta\hat H})$:

**Helmholtz free energy:**
$$\boxed{F = -k_BT\ln Z}$$

This is the fundamental relation — everything else is a derivative of $F$.

**Internal energy:**
$$U = \langle\hat H\rangle = -\frac{\partial\ln Z}{\partial\beta} = F + TS$$

**Entropy:**
$$S = -\frac{\partial F}{\partial T}\bigg|_V = k_B\left(\ln Z + \beta U\right) = -k_B\text{Tr}(\hat\rho\ln\hat\rho)$$

(Consistent with the von Neumann entropy — as it must be.)

**Pressure** (from the volume-dependence of energy levels $E_n(V)$):
$$P = -\frac{\partial F}{\partial V}\bigg|_T = k_BT\frac{\partial\ln Z}{\partial V}\bigg|_T$$

**Chemical potential** (for a system where particle number $N$ can vary):
$$\mu = \frac{\partial F}{\partial N}\bigg|_{T,V}$$

**Heat capacity:**
$$C_V = \frac{\partial U}{\partial T}\bigg|_V = k_B\beta^2\frac{\partial^2\ln Z}{\partial\beta^2} = \frac{\langle\hat H^2\rangle - \langle\hat H\rangle^2}{k_BT^2}$$

The last form shows $C_V$ is proportional to the energy **variance** — how much
the energy fluctuates around its mean. Larger fluctuations → larger heat capacity.

---

## 10.5 — The Four Laws of Thermodynamics: Derived

### Law 0 — Thermal Equilibrium (The Zeroth Law)

**Statement:** If two systems are each in thermal equilibrium with a third,
they are in equilibrium with each other.

**Derivation:** At equilibrium, each system maximizes its own entropy subject
to its energy. The Lagrange multiplier $\beta = 1/k_BT$ is the same for all
systems in equilibrium with each other (since energy flows until $\beta$ equalizes).
The zeroth law is the statement that $\beta$ is a transitive equality — a
mathematical fact about Lagrange multipliers.

### Law 1 — Conservation of Energy (The First Law)

**Statement:** $dU = \delta Q - \delta W$ (energy is conserved; work and heat
are both forms of energy transfer).

**Derivation:** From $U = \text{Tr}(\hat\rho\hat H)$:

$$dU = \underbrace{\text{Tr}(d\hat\rho\cdot\hat H)}_{\delta Q} + \underbrace{\text{Tr}(\hat\rho\cdot d\hat H)}_{\delta W}$$

- $\delta W = \text{Tr}(\hat\rho\,d\hat H) = -P\,dV$: work done by the system changes
  the energy levels $E_n(V)$ by changing the volume — the Hamiltonian itself changes
- $\delta Q = \text{Tr}(d\hat\rho\cdot\hat H)$: heat changes the occupation probabilities
  $p_n$ — the density matrix changes while energy levels stay fixed

**The first law is the statement that total energy is conserved (Noether's theorem
for time-translation symmetry, Ch. 1 §1.7) applied to a system where energy can
be transferred via two different mechanisms: rearranging the Hamiltonian (work)
or rearranging the probability distribution (heat).**

### Law 2 — Entropy Never Decreases (The Second Law)

**Statement:** The entropy of an isolated system is non-decreasing; it is
constant for reversible processes and increases for irreversible ones.

**Derivation sketch:** Consider all microstates of a gas in a $V/2$-box, then
remove the partition. The number of accessible microstates goes from $\Omega_{1/2}$
to $\Omega_{full} \sim 2^N\Omega_{1/2}$. The entropy change:

$$\Delta S = k_B\ln\frac{\Omega_{full}}{\Omega_{1/2}} = Nk_B\ln 2 > 0$$

For $N = 10^{23}$: $\Delta S = 10^{23}k_B\ln 2 > 0$ — overwhelmingly positive.

**Why does entropy increase?** The volume of phase space accessible to
high-entropy macrostates is astronomically larger than that for low-entropy
macrostates. A system that starts in a low-entropy state will move toward
higher-entropy states simply because there are so many more of them — not because
of any arrow-of-time in the microscopic laws.

The **Clausius inequality** for any cycle:
$$\oint \frac{\delta Q}{T} \leq 0$$
with equality for reversible cycles. This follows from the second law and is
the quantitative form used in engineering analysis.

### Law 3 — Zero Entropy at Zero Temperature (The Third Law)

**Statement:** The entropy of a system approaches a constant (usually zero) as
$T\to 0$.

**Derivation:** As $T\to 0$ ($\beta\to\infty$), the Boltzmann distribution
concentrates entirely on the ground state:

$$p_0 \to 1, \quad p_{n\neq 0} \to e^{-\beta(E_n - E_0)} \to 0$$

If the ground state is non-degenerate: $\hat\rho\to|0\rangle\langle 0|$, a pure state,
and $S = -k_B\text{Tr}(\hat\rho\ln\hat\rho) \to 0$.

If the ground state is $g$-fold degenerate: $S\to k_B\ln g$. For macroscopic
systems, $g \ll e^N$ so $S/N\to 0$ as $N\to\infty$ — the extensive entropy
per particle still vanishes.

**Engineering consequence:** As $T\to 0$, all specific heats $C\to 0$
(consistent with $S\to 0$ since $\int_0^T C\,dT'/T' = S(T)$ must converge).
This means you cannot remove a finite amount of heat to reach $T = 0$ in a
finite number of steps — it is asymptotically approachable but never reached.

---

## 10.6 — The Carnot Efficiency

From the first and second laws, the maximum efficiency of any heat engine
operating between a hot reservoir at $T_h$ and a cold reservoir at $T_c$:

$$\boxed{\eta_{Carnot} = 1 - \frac{T_c}{T_h}}$$

**Derivation:** In a reversible (Carnot) cycle:
- Heat absorbed from hot reservoir: $Q_h$
- Heat rejected to cold reservoir: $Q_c$
- Work output: $W = Q_h - Q_c$ (first law)
- Entropy balance for reversible cycle: $Q_h/T_h = Q_c/T_c$ (second law, equality)
- Efficiency: $\eta = W/Q_h = 1 - Q_c/Q_h = 1 - T_c/T_h$

No engine can exceed Carnot efficiency — if it did, entropy would decrease, violating
the second law. This is the fundamental limit on all heat engines: steam turbines,
internal combustion, Stirling, thermoelectric generators.

**Engineering reality:** Real engines achieve 40–60% of Carnot efficiency.
A coal power plant at $T_h = 600°C$ and $T_c = 30°C$: $\eta_{Carnot} = 1 - 303/873 = 65.3\%$.
Actual efficiency: ~42%. The gap is irreversibility (friction, heat leakage, finite-time
operation) and is the subject of finite-time thermodynamics.

---

## 10.7 — Ideal Gas and the Equipartition Theorem

### 10.7.1 — The Ideal Gas Partition Function

For a monatomic ideal gas of $N$ identical particles in volume $V$, each with
only translational kinetic energy $\hat H_i = \hat p_i^2/2m$:

$$Z_1 = \text{Tr}(e^{-\beta\hat p^2/2m}) = \frac{V}{\lambda_{th}^3}$$

where the **thermal de Broglie wavelength**:

$$\lambda_{th} = h/\sqrt{2\pi mk_BT}$$

sets the length scale at which quantum effects become important ($\lambda_{th}$
comparable to interparticle spacing $n^{-1/3}$ → quantum statistics matter).

For $N$ distinguishable particles: $Z = Z_1^N$. For identical particles (indistinguishable):

$$Z = \frac{Z_1^N}{N!} = \frac{V^N}{N!\lambda_{th}^{3N}}$$

The $N!$ is the **Gibbs correction factor** — without it, entropy is non-extensive
(Gibbs paradox). Quantum mechanics resolves this: identical particles are truly
indistinguishable.

From $F = -k_BT\ln Z$:
$$PV = Nk_BT, \qquad U = \frac{3}{2}Nk_BT, \qquad C_V = \frac{3}{2}Nk_B$$

The ideal gas law and monatomic heat capacity, derived from the partition function.

### 10.7.2 — The Equipartition Theorem

For any quadratic term in the Hamiltonian $H = \ldots + \frac{1}{2}\alpha q^2 + \ldots$:

$$\left\langle\frac{1}{2}\alpha q^2\right\rangle = \frac{1}{2}k_BT$$

Every quadratic degree of freedom contributes $\frac{1}{2}k_BT$ to the average energy.

| System | Quadratic DOF | $C_V$ | Prediction |
|---|---|---|---|
| Monatomic gas | 3 translational | $\frac{3}{2}Nk_B$ | Exact (He, Ar, Ne) |
| Diatomic gas (rigid) | 3 trans + 2 rot | $\frac{5}{2}Nk_B$ | Good at room T (N₂, O₂) |
| Diatomic gas (vibrating) | + 2 vib | $\frac{7}{2}Nk_B$ | Fails! |
| Monatomic solid (classical) | 3 pos + 3 mom | $3Nk_B$ | Dulong-Petit law |

### 10.7.3 — Failure of Equipartition and the Quantum Correction

**The problem:** Equipartition predicts $C_V = \frac{7}{2}Nk_B$ for vibrating diatomic
molecules and $C_V = 3Nk_B$ for all solids at all temperatures. Experiment shows
$C_V\to 0$ as $T\to 0$.

**The fix:** A quantum harmonic oscillator with frequency $\omega$ only contributes
to the heat capacity if $k_BT \gtrsim \hbar\omega$. For $k_BT \ll \hbar\omega$,
the mode is **frozen out** — it remains in its ground state $E_0 = \hbar\omega/2$
regardless of temperature.

**Einstein model** for a solid (all modes at same frequency $\omega_E$):

$$C_V = 3Nk_B\left(\frac{\hbar\omega_E}{k_BT}\right)^2\frac{e^{\hbar\omega_E/k_BT}}{(e^{\hbar\omega_E/k_BT}-1)^2}$$

- At high T ($k_BT \gg \hbar\omega_E$): $C_V \to 3Nk_B$ (Dulong-Petit) ✓
- At low T ($k_BT \ll \hbar\omega_E$): $C_V \to 0$ exponentially ✓

**Debye model** (realistic phonon spectrum, $\omega$ up to Debye cutoff $\omega_D$):

$$C_V = 9Nk_B\left(\frac{T}{T_D}\right)^3\int_0^{T_D/T}\frac{x^4 e^x}{(e^x-1)^2}dx$$

At low T: $C_V = \frac{12\pi^4}{5}Nk_B\left(\frac{T}{T_D}\right)^3$ — the **Debye $T^3$ law** ✓

The Debye temperature $T_D = \hbar\omega_D/k_B$ characterizes when quantum
effects matter: for diamond $T_D = 2230$ K; for lead $T_D = 105$ K. This is
why diamond remains quantum (low $C_V$) at room temperature while lead is classical.

---

## 10.8 — Quantum Statistics: Bose-Einstein and Fermi-Dirac

### 10.8.1 — The Grand Canonical Ensemble

When particle number $N$ can fluctuate (the system is coupled to a particle
reservoir), maximize entropy subject to both fixed $\langle\hat H\rangle = U$
and fixed $\langle\hat N\rangle = N$:

$$\hat\rho = \frac{1}{\Xi}e^{-\beta(\hat H - \mu\hat N)}, \qquad \Xi = \text{Tr}(e^{-\beta(\hat H-\mu\hat N)})$$

where $\mu$ is the **chemical potential** — the Lagrange multiplier for particle
number. The grand potential: $\Omega = -k_BT\ln\Xi = F - \mu N$.

### 10.8.2 — Mean Occupation Numbers

For a system of non-interacting particles, each single-particle state $\epsilon$
can be occupied by $n$ particles. The mean occupation:

**Bose-Einstein** (bosons, integer spin, $n = 0, 1, 2, \ldots$):
$$\boxed{\bar n_{BE}(\epsilon) = \frac{1}{e^{(\epsilon-\mu)/k_BT} - 1}}$$

**Fermi-Dirac** (fermions, half-integer spin, $n = 0$ or $1$ by Pauli exclusion):
$$\boxed{\bar n_{FD}(\epsilon) = \frac{1}{e^{(\epsilon-\mu)/k_BT} + 1}}$$

**Maxwell-Boltzmann** (classical limit, $e^{(\epsilon-\mu)/k_BT} \gg 1$):
$$\bar n_{MB}(\epsilon) = e^{-(\epsilon-\mu)/k_BT}$$

At high T (or low density), all three converge to Maxwell-Boltzmann. The quantum
corrections matter when $\lambda_{th}^3 n \gtrsim 1$ — when the thermal de Broglie
wavelength becomes comparable to the interparticle spacing.

### 10.8.3 — The Fermi-Dirac Distribution and Free Electrons

For electrons (fermions, $\mu \to E_F$ at $T=0$):

At $T = 0$: step function — all states below $E_F$ filled, all above empty.

The Fermi energy for a free electron gas of density $n$:

$$E_F = \frac{\hbar^2}{2m_e}(3\pi^2 n)^{2/3}$$

For copper ($n = 8.5\times 10^{28}$ m$^{-3}$): $E_F = 7.0$ eV, $T_F = E_F/k_B = 81{,}000$ K.
At room temperature ($T = 300$ K $\ll T_F$): the Fermi-Dirac distribution is
nearly a step function. Electrons are **degenerate** — their quantum statistics
dominate over thermal effects.

**Electronic specific heat:** Only electrons within $k_BT$ of $E_F$ can be
thermally excited. The fraction $\sim k_BT/E_F \ll 1$:

$$C_V^{electron} = \frac{\pi^2}{2}Nk_B\frac{T}{T_F} = \gamma T$$

where $\gamma = \pi^2 Nk_B/2T_F$ is the **Sommerfeld coefficient**. At low T,
$C_V^{electron} = \gamma T$ (linear in T) while $C_V^{phonon} = AT^3$ (Debye).
Total low-T specific heat: $C_V = \gamma T + AT^3$ — observed in all metals,
confirming the Fermi-Dirac picture.

**Connection to Ch. 6:** The Fermi-Dirac distribution with $\mu$ adjusted by
doping is exactly the occupation function used in semiconductor device physics
(Ch. 6 §6.6). The connection is direct: the grand canonical ensemble here
produces the Fermi-Dirac function used there.

### 10.8.4 — Blackbody Radiation: Photons Are Bosons with $\mu = 0$

Photons have integer spin (spin-1) → bosons. They are not conserved (can be
created and destroyed freely) → $\mu = 0$.

The mean number of photons in a mode of frequency $\nu$:

$$\bar n = \frac{1}{e^{h\nu/k_BT} - 1}$$

Energy per mode: $\bar E = h\nu\,\bar n = \frac{h\nu}{e^{h\nu/k_BT} - 1}$

Spectral energy density (summing over all modes in volume $V$ in frequency interval $d\nu$):

$$\boxed{u(\nu, T) = \frac{8\pi h\nu^3}{c^3}\frac{1}{e^{h\nu/k_BT}-1}}$$

This is **Planck's law** for blackbody radiation — derived from Bose-Einstein
statistics for photons.

**Limits:**
- Low frequency ($h\nu \ll k_BT$): $u\to 8\pi\nu^2 k_BT/c^3$ — the classical
  Rayleigh-Jeans law. This diverges as $\nu\to\infty$ (the ultraviolet catastrophe),
  the failure that motivated Planck to quantize energy in 1900.
- High frequency ($h\nu \gg k_BT$): $u\to 8\pi h\nu^3/c^3 \cdot e^{-h\nu/k_BT}$
  — Wien's displacement law; exponential suppression of high-frequency modes.

**Wien's displacement law:** Peak of $u(\nu, T)$ at $h\nu_{max} = 2.82\,k_BT$:
$$\lambda_{max} T = b = 2.898\times 10^{-3}\;\text{m·K}$$

**Stefan-Boltzmann law:** Total power radiated per unit area:
$$j = \sigma T^4, \qquad \sigma = \frac{2\pi^5k_B^4}{15c^2h^3} = 5.67\times 10^{-8}\;\text{W/m}^2\text{K}^4$$

---

## 10.9 — Phase Transitions and Landau Theory

### 10.9.1 — Order Parameters and Broken Symmetry

A **phase transition** is a discontinuous (or singular) change in the equilibrium
state as a control parameter (temperature, pressure, field) passes through a
critical value. The key concept is the **order parameter** $\phi$: a quantity
that is zero in the high-symmetry (disordered) phase and nonzero in the
low-symmetry (ordered) phase.

### 10.9.2 — The Landau Free Energy

Near a continuous (second-order) phase transition, the free energy as a functional
of the order parameter $\phi$:

$$\boxed{F = F_0 + a(T)\phi^2 + b\phi^4 + c|\nabla\phi|^2 + \cdots, \qquad b > 0}$$

with $a(T) = a_0(T - T_c)$ changing sign at the transition.

**This is the Mexican hat, appearing for the fourth time:**

| System | $\phi$ | Symmetry broken | $T_c$ | Chapter |
|---|---|---|---|---|
| Higgs field | Complex scalar $H$ | SU(2)×U(1) → U(1) | 246 GeV | 0, §0.7 |
| BCS superconductor | Gap $\Delta = |\Delta|e^{i\theta}$ | U(1) | $\sim$ meV | 7, §7.6 |
| BEC | Condensate $\Psi = |\Psi|e^{i\theta}$ | U(1) | $\sim$ μeV | 7, 10 |
| Ferromagnet | Magnetization **M** | SO(3) | Curie T | 10 |
| Ferroelectric | Polarization **P** | Inversion | Curie T | 10 |
| Liquid-gas | Density ρ-ρ_c | Z₂ | Critical T | 10 |
| Antiferromagnet | Staggered mag. | Translation + SO(3) | Néel T | 10 |

**The universal result:** For $T > T_c$ ($a > 0$): minimum at $\phi = 0$
(disordered phase). For $T < T_c$ ($a < 0$): minimum at
$|\phi|^2 = -a/2b = a_0(T_c-T)/2b \neq 0$ (ordered phase, spontaneous symmetry breaking).

Order parameter near $T_c$: $|\phi| \propto (T_c-T)^\beta$ with $\beta = \frac{1}{2}$
(mean-field value; corrected by fluctuations to $\beta \approx 0.326$ in 3D
Ising universality class).

### 10.9.3 — First-Order vs. Second-Order Transitions

**Second-order (continuous):** $\phi$ grows continuously from zero below $T_c$.
No latent heat. Diverging correlation length $\xi\propto|T-T_c|^{-\nu}$.
Examples: ferromagnetic transition, λ-transition in helium, superconducting
transition in zero field.

**First-order (discontinuous):** $\phi$ jumps discontinuously. Latent heat
$L = T_c\Delta S$. Phase coexistence. Requires a cubic term $c\phi^3$ in Landau
free energy (making the energy landscape asymmetric) or a $b < 0$ term.
Examples: melting/freezing, liquid-gas transition away from critical point,
first-order ferromagnetic transitions.

**Clausius-Clapeyron equation** for first-order phase boundaries:

$$\frac{dP}{dT} = \frac{L}{T\Delta V}$$

where $L$ is latent heat and $\Delta V$ is volume change. Applications:
- Ice: negative $dP/dT$ (water has larger $\Delta V$ than ice — anomalous)
- Most solids: positive $dP/dT$
- Boiling water at altitude: lower $T_{boil}$ due to lower pressure (same equation)

### 10.9.4 — Gibbs Phase Rule

For a system of $C$ chemical components in $P$ phases:

$$\boxed{F = C - P + 2}$$

where $F$ is the number of **degrees of freedom** (intensive variables that can
be independently varied without changing the number of phases).

| Example | $C$ | $P$ | $F$ |
|---|---|---|---|
| Water, one phase | 1 | 1 | 2 (choose $T$ and $p$) |
| Water+ice | 1 | 2 | 1 (only one $T$ for each $p$) |
| Water+ice+vapor (triple point) | 1 | 3 | 0 (unique $T$, $P$) |
| Salt water, one phase | 2 | 1 | 3 ($T$, $P$, concentration) |

The Gibbs phase rule tells ChE engineers how many independent variables can
be specified in a separation process.

---

## 10.10 — Entropy, Information, and the Arrow of Time

### 10.10.1 — Boltzmann's H-Theorem and the Approach to Equilibrium

Boltzmann proved (for a dilute gas obeying his kinetic equation) that the quantity:

$$H = \int f(\mathbf{v})\ln f(\mathbf{v})\,d^3v$$

(where $f$ is the single-particle distribution function) satisfies $dH/dt \leq 0$.
Since $S \propto -H$, entropy increases: $dS/dt \geq 0$.

The proof assumes **molecular chaos** (Stosszahlansatz): the velocities of two
particles about to collide are uncorrelated. This assumption breaks time-reversal
symmetry (the future-pointing assumption) — and is what injects the arrow of time.

### 10.10.2 — Maxwell's Demon and Landauer's Principle

Maxwell's demon can, in principle, sort molecules and decrease entropy —
seemingly violating the second law. The resolution (Szilard 1929, Landauer 1961):

**Erasing one bit of information costs at least $k_BT\ln 2$ of free energy.**

The demon must remember each measurement result in order to operate the door.
When the demon's memory is eventually erased (as it must be, since it has
finite memory), the entropy increase from erasure exactly compensates the
entropy decrease from sorting. Information is physical — it has thermodynamic cost.

**Landauer's principle:** $W_{erasure} \geq k_BT\ln 2$ per bit.

At 300 K: $k_BT\ln 2 \approx 2.87\times 10^{-21}$ J $\approx 0.018$ meV per bit.
Modern CMOS logic dissipates $\sim 10^{-16}$ J per bit — still $10^5$ times above
the Landauer limit, leaving enormous room for efficiency improvement.

**Engineering consequence:** The Landauer limit is the ultimate lower bound on
computing energy dissipation. It is currently unreachable in practice but
provides a target for reversible computing research.

### 10.10.3 — Shannon Entropy and the Unified Picture

The Shannon information entropy:

$$H = -\sum_i p_i\log_2 p_i \;\text{bits}$$

is identical in form to the von Neumann entropy (with $k_B\log_e$ replaced
by $\log_2$). This is not a coincidence. Statistical mechanics is the physics
of information: entropy measures how much we *don't know* about the microscopic
state. Temperature is the currency of that ignorance.

**The arrow of time is the arrow of decreasing information:** The universe started
in an extremely low-entropy (high information, low probability) state (the Big Bang).
It has been evolving toward higher entropy (lower information, higher probability)
ever since — not because the microscopic laws prefer the future, but because
high-entropy states are so overwhelmingly more numerous.

---

## 10.11 — Summary

Bridge B.b is complete. The descent from quantum mechanics to thermodynamics:

| Step | Operation | Result |
|---|---|---|
| Density matrix | $\hat\rho = \Sigma p_n|n\rangle\langle n|$ | Encodes statistical ignorance |
| Trace environment | $\hat\rho_S = \text{Tr}_E(\hat\rho_{SE})$ | Irreversibility from many DOF |
| Von Neumann entropy | $S = -k_B\text{Tr}(\hat\rho\ln\hat\rho)$ | Quantifies ignorance |
| Max entropy, fixed $\langle\hat H\rangle$ | Lagrange multiplier $\beta$ | Boltzmann distribution; temperature |
| Partition function | $Z = \text{Tr}(e^{-\beta\hat H})$ | All thermodynamics from one function |
| Zeroth law | $\beta$ equalizes at equilibrium | Temperature is transitive |
| First law | $dU = \delta Q - \delta W$ | Energy conservation (Noether, time symmetry) |
| Second law | $S = k_B\ln\Omega$ increases | High-entropy states vastly outnumber low |
| Third law | $S\to 0$ as $T\to 0$ | Ground state is pure |
| Carnot efficiency | $\eta = 1 - T_c/T_h$ | Maximum from first + second law |
| Equipartition | $\frac{1}{2}k_BT$ per quadratic DOF | Fails when $\hbar\omega \gg k_BT$ |
| Fermi-Dirac | $n_{FD} = 1/(e^{(\epsilon-\mu)/kT}+1)$ | Electrons in metals and semiconductors |
| Bose-Einstein | $n_{BE} = 1/(e^{(\epsilon-\mu)/kT}-1)$ | Phonons, photons, BEC |
| Planck radiation | $u(\nu,T) = (8\pi h\nu^3/c^3)/(e^{h\nu/kT}-1)$ | Blackbody spectrum |
| Landau theory | $F = a(T)\phi^2 + b\phi^4$ | Phase transitions (Mexican hat, 4th appearance) |
| Clausius-Clapeyron | $dP/dT = L/T\Delta V$ | Phase boundaries |
| Gibbs phase rule | $F = C - P + 2$ | ChE separation processes |
| Landauer limit | $W_{min} = k_BT\ln 2$ per bit | Ultimate computing energy limit |

---

## 10.12 — Engineering Thread

| Physics | Application |
|---|---|
| Boltzmann factor $e^{-E/kT}$ | Arrhenius reaction kinetics (ChE); semiconductor carrier density (EEE); diffusion activation (ME/CE) |
| Carnot efficiency $\eta = 1-T_c/T_h$ | Design limit for steam turbines, engines, refrigerators, heat pumps |
| Clausius-Clapeyron $dP/dT = L/T\Delta V$ | Boiling points vs. altitude; steam tables; vapor pressure calculations |
| Gibbs phase rule $F = C-P+2$ | Distillation design; alloy phase diagram reading; ChE process control |
| Equipartition + quantum freezeout | Specific heat of materials; thermal mass in HVAC; heat storage |
| Fermi-Dirac distribution | Electronic specific heat in metals; semiconductor device physics; Fermi level engineering (Ch. 6) |
| Bose-Einstein statistics (photons) | Blackbody furnace design; solar cell efficiency limits; thermal imaging |
| Planck/Stefan-Boltzmann | Furnace radiation heat transfer; spacecraft thermal control; IR sensor design |
| Debye $T^3$ law | Low-T cryogenic specific heat; thermal mass at millikelvin for quantum computers |
| Landau theory / phase diagrams | Materials processing (heat treatment, solidification); alloy design |
| Landauer limit | Energy-efficient computing; reversible logic design; fundamental sensor noise |
| Von Neumann entropy + decoherence | Quantum computing error budgets; qubit coherence time engineering |

---

## 10.13 — Looking Ahead

Chapters 9 and 10 have recovered classical mechanics and thermodynamics from
quantum mechanics via the $\hbar\to 0$ and $N\to\infty$ limits respectively.

**Chapter 11 performs Bridge B.c:** the classical field limit of the U(1) gauge
sector of $\mathcal{L}_{SM}$ (Ch. 0 §0.4.2). This gives Maxwell's equations
directly from the Lagrangian — showing that every field equation in classical
electromagnetism is a consequence of the Euler-Lagrange equations applied to
one term in $\mathcal{L}_{SM}$.

The entire Layer 2 landscape is now taking shape: Newtonian gravity (Ch. 8),
classical mechanics (Ch. 9), thermodynamics (Ch. 10), and next — Maxwell's
equations (Ch. 11) and the transport laws (Ch. 13). These five, together,
constitute the complete classical engineering science that Chapters 15–21
will lump into the engineering systems of Layer 3.

---

*End of Chapter 10.*

---
*Next: Chapter 11 — Bridge B.c: Maxwell's Equations from the U(1) Gauge Sector*
