# Bridge B.e — The Kubo Formula and the Generalized Transport Law

### Five Constitutive Laws Through the Kubo / Linear-Response Framework

> [!note] Why not "one calculation"?
> An earlier title claimed *Five Transport Laws from One Quantum Mechanical Calculation*.
> That is false as stated, and it is false in a way the chapter itself
> demonstrates. The five laws share one **response-theory structure**, but
> producing each one requires a different generalized force, a different current
> operator, a different constitutive closure, and — for $C$ — a different
> limiting procedure entirely (§13.9.2). What this chapter delivers is a
> *framework* in which all five sit, not a single calculation that emits all five.

---

> _The Green-Kubo relations are among the most profound results in statistical mechanics._ _They say that the dissipation of a system driven out of equilibrium_ _is completely determined by the spontaneous fluctuations of the same system at equilibrium._ — David Chandler, _Introduction to Modern Statistical Mechanics_

---

## 13.0 — Bridge B.e and the Convergence Chapter

This is the final Bridge B path — and the most important chapter in the book for making it discipline-agnostic.

**The claim of Chapter 1** was that every engineering branch shares one mathematical template at Layer 2:

$$\text{flux} = -L \cdot \nabla\phi$$

The claim was that Ohm's law, Fourier's law, Fick's law, Newton's law of viscosity, and Hooke's law are the same formula with different labels.

**This chapter delivers the framework.** All five response coefficients ($\sigma$, $\kappa$, $D$, $\eta$, $C$) are *expressible* through the **Green–Kubo relation**, but each one requires its own generalized force, its own current operator, its own closure, and — for $C$ — a different limiting procedure. What is shared is the response structure, not the calculation:

| Law | Generalized force $\hat A$ | Current operator $\hat B$ | Extra step needed |
|---|---|---|---|
| Ohm | $\hat{\mathbf{E}}$ | $\hat{\mathbf{J}}$ (charge) | Drude/memory closure |
| Fourier | $\hat{\mathbf{T}}$ or $-\nabla T$ | $\hat{\mathbf{J}}_Q$ | same closure; Wiedemann–Franz adds an assumption |
| Fick | $\nabla\mu$ | $\hat{\mathbf{J}}^N$ | Einstein relation |
| Newton viscosity | $\partial_j u_i$ | $\hat\sigma_{ij}$ (transverse) | transverse projection |
| Hooke | $\varepsilon_{kl}$ | $\delta\hat\sigma_{ij}$ | **free-energy second derivative** — not a transport coefficient at all |

`[STRUCTURAL CONNECTION]` — the unification is real and it is the book's
organizing insight, but it is a shared *framework* claim, not a claim that one
substitution yields five laws. The honest formulation: **linear-response theory
gives a single template for dissipative response, and these five laws are
instances of that template applied to five different observables — with the
fifth, elasticity, only partially an instance.**

`[DERIVATION]` — *within* that framework, the Kubo relation itself is derived
rather than assumed, but it carries boundary conditions that must be stated,
because "delivers the proof" is doing more work than it should. Three assumptions
carry the whole chapter:

1. **Linear response.** The system is perturbed weakly, $\hat A = \hat A_0 + \delta\hat A$
   with $|\delta\hat A| \ll |\hat A_0|$, and the response is taken to first order
   in $\delta\hat A$. This is what produces the linear constitutive laws at all.
   Finite-amplitude transport is not covered (§13.12).
2. **Equilibrium initial condition.** The correlator $\langle\cdots\rangle_0$ is
   an *equilibrium* average. This is what produces the time integral, and hence
   the dissipative arrow of time described below.
3. **Time-translation invariance of the unperturbed state.** Without it, the
   $\langle J(t)J(0)\rangle_0$ in the Kubo formula is not a function of $t$ alone.

Note also that the five results are not equally "the same". **Four** of them
($\sigma$, $\kappa$, $D$, $\eta$) are dissipative transport coefficients,
obtained from the same dissipative part of the correlator — but $\eta$ is built
on a *transverse* current, the off-diagonal stress component $\hat\sigma_{xy}$,
rather than on a conserved total current, which is why its Kubo formula is
written with a factor of $1/V$ and a different relaxation time $\tau_v$. The
fifth, $C$ in Hooke's law, is not a transport coefficient at all: it is a
*zero-frequency, non-dissipative* static susceptibility, a second derivative of
the free energy rather than an integral over a dissipative correlator. The
unified template holds, but the members of the family differ in which part of
the Kubo expression they use — a distinction that matters when the relaxation
time goes to zero or the response becomes non-Markovian, and that is why
"Hooke's law falls out of Kubo alongside Ohm's law" is a `[STRUCTURAL
CONNECTION]` in the strict sense rather than a fifth instance of the same
calculation.

**Bridge B.e is also the bridge that injects irreversibility.** Chapters 9 and 11 (classical mechanics and Maxwell's equations) are time-reversible: run them backward and you get equally valid physics. Ohm's law is not time-reversible — current flows from high to low potential, not randomly. The irreversibility comes from this chapter: quantum scattering and decoherence, averaged over an equilibrium ensemble, produce a finite relaxation time and a finite, dissipative conductivity.

**Model Ledger — microscopic Hamiltonian to linear transport coefficient**

| Field | Content |
|---|---|
| Parent theory | Quantum many-body Hamiltonian $\hat H_0$ in thermal equilibrium (Ch. 5, Ch. 6) |
| Reduction | Weak perturbation; first order in the field; equilibrium initial state; replace the bath with a relaxation time $\tau$ (Drude closure) |
| Model | $L_{\alpha\beta} = \frac{1}{Vk_BT}\int_0^\infty \langle \hat J^\alpha(0)\hat J^\beta(t)\rangle_0\,e^{i\omega t}\,dt$; then $L = \frac{nq^2\tau}{m}$ |
| Assumptions | linear response; equilibrium; ergodicity (so $\tau$ is a state variable, not history-dependent); elastic scattering only; single-exponential relaxation closure; molecular chaos (first Stosszahlansatz, valid for $L \gg \ell$). Note: the derivation uses a *classical* equipartition prefactor, but it cancels against the $1/k_BT$ in the Green–Kubo prefactor, so the result remains valid in the degenerate regime $k_BT \ll E_F$ — see §13.4.2 Step 3 |
| Physics retained | dissipation, the arrow of time, the relation between charge/heat/momentum diffusion coefficients |
| Physics neglected | inelastic and memory-dependent scattering, phonon drag, interactions (in the elastic limit), non-equilibrium distributions. The **free** Fermi gas is exact and gives $\sigma\to\infty$; all finite resistivity comes from the closure |
| Validity | diffusive regime $\ell \ll L_{\text{device}}$; $\omega\tau \ll 1$; well-defined $\tau$ |
| Fails when | $\ell \gtrsim L$ (ballistic/Landauer, §13.11), $\omega\tau \gtrsim 1$, strong correlations, or non-equilibrium driving |
| Next model | memory kernel / non-Markovian response; Landauer (ballistic); hydrodynamic transport; BTE (Ch. 19 for phonons) |

|Bridge|Path|Result|
|---|---|---|
|B.a|$\hbar\to 0$|Classical mechanics (Ch. 9)|
|B.b|$N\to\infty$|Thermodynamics (Ch. 10)|
|B.c|Classical U(1)|Maxwell's equations (Ch. 11)|
|B.d|Weak-field GR|Newton's gravity (Ch. 8)|
|**B.e**|**Kubo averaging**|**Generalized Transport Law (Ch. 13)**|

---

## 13.1 — Linear Response Theory: The Setup

### 13.1.1 — The Perturbation

Consider a system in equilibrium, described by density matrix $\hat\rho_0 = e^{-\beta\hat H_0}/Z$ (Ch. 10 §10.3). At $t = 0$, a weak time-dependent perturbation is switched on:

$$\hat H(t) = \hat H_0 - \hat A\,F(t)$$

where $\hat A$ is a quantum observable (the operator that couples to the perturbation) and $F(t)$ is the classical driving force (an electric field, temperature gradient, pressure difference, etc.).

**Examples of coupling:**

- Electric field: $\hat A = -e\hat{\mathbf{r}}$ (dipole coupling), $F = \mathbf{E}(t)$
- Temperature gradient: $\hat A = \hat H_0$ (energy), $F = \nabla T / T^2$
- Chemical potential gradient: $\hat A = \hat N$ (particle number), $F = -\nabla\mu/T$

### 13.1.2 — The Linear Response

To first order in $F$, the expectation value of a second observable $\hat B$:

$$\langle\hat B(t)\rangle = \langle\hat B\rangle_0 + \int_{-\infty}^t \chi_{BA}(t-t')\,F(t')\,dt'$$

where $\chi_{BA}$ is the **retarded Green's function** (generalized susceptibility):

$$\boxed{\chi_{BA}(t-t') = \frac{i}{\hbar}\Theta(t-t')\langle[\hat B(t), \hat A(t')]\rangle_0}$$

$\Theta$ is the Heaviside step function (enforcing **causality**: response cannot precede the perturbation). The commutator $[\hat B, \hat A]$ is computed in the Heisenberg picture with respect to $\hat H_0$, and $\langle\cdot\rangle_0$ is the equilibrium average.

In frequency space (Fourier transform):

$$\langle\hat B(\omega)\rangle = \tilde\chi_{BA}(\omega)\,F(\omega)$$

The response at frequency $\omega$ is proportional to the driving at the same frequency — this is linear response.

---

## 13.2 — The Kubo Formula

### 13.2.1 — Derivation Sketch

Starting from the von Neumann equation (Ch. 10 §10.1.2) for the perturbed system:

$$i\hbar\frac{\partial\hat\rho}{\partial t} = [\hat H_0 + \hat H', \hat\rho]$$

Write $\hat\rho = \hat\rho_0 + \delta\hat\rho$ and linearize in $\hat H'$:

$$i\hbar\frac{\partial,\delta\hat\rho}{\partial t} = [\hat H_0, \delta\hat\rho] + [\hat H', \hat\rho_0]$$

Solving this first-order equation using the interaction picture and integrating:

$$\delta\hat\rho(t) = \frac{i}{\hbar}\int_{-\infty}^t e^{-i\hat H_0(t-t')/\hbar}[\hat H'(t'), \hat\rho_0]e^{i\hat H_0(t-t')/\hbar}dt'$$

Taking the trace with $\hat B$ and using the cyclic property of the trace and the equilibrium density matrix $[\hat\rho_0, e^{-\beta\hat H_0}] = 0$:

$$\chi_{BA}(\tau) = \frac{i}{\hbar}\Theta(\tau)\langle[\hat B(\tau), \hat A(0)]\rangle_0$$

This confirms §13.1.2. The transport coefficient $L_{BA}$ (the DC, $\omega\to 0$ limit):

$$\boxed{L_{BA} = \frac{1}{Vk_BT}\int_0^\infty\langle\hat J_B(0)\hat J_A(t)\rangle_0,dt}$$

where $\hat J_A$, $\hat J_B$ are the current operators associated with observables $\hat A$, $\hat B$ (related by continuity equations), and $V$ is the system volume. This is the **Green-Kubo formula** for transport coefficients.

### 13.2.2 — What the Formula Says

The transport coefficient $L_{BA}$ — which tells you how much of current $B$ flows in response to a force on $A$ — equals the **time-integrated autocorrelation** of the equilibrium current fluctuations.

**Three things to notice:**

**1. No perturbation appears in the formula.** The right side is an equilibrium average — no external force, no out-of-equilibrium state. The coefficient that describes the dissipative response to a perturbation is entirely determined by the system's behavior at equilibrium. Dissipation and equilibrium fluctuations are two faces of the same physics.

**2. The integral must converge for a finite transport coefficient to exist.** If the current-current correlator decays to zero at long times (as it does in any real material with scattering), $L_{BA}$ is finite. If the correlator never decays (perfect crystal at $T = 0$ with no defects), $L_{BA}\to\infty$ — the material is a perfect conductor. **Ohm's law requires scattering.**

**3. The framework is exact; a given formula for a given coefficient is not automatically so.** The derivation above made exactly one approximation — linear response. Within that, the Kubo relation is an identity. But "exact" attaches to the *relation*, not to any particular closed form for $\sigma$, $\kappa$, $D$, or $\eta$. Getting a usable expression for a specific coefficient additionally requires:

- choosing the correct observable–force pair $\hat A$, $\hat B$ and defining the current operator consistently (§13.4.1 shows this is where factors of $e$ and $V$ come from);
- an equilibrium state and a well-defined order of limits — $\omega\to 0$, $V\to\infty$, and $t\to\infty$ **do not always commute**, and dc conductivity is a case where the order matters;
- the thermodynamic limit, or an explicit finite-size treatment;
- boundary conditions, and for charged systems the treatment of **diamagnetic and contact terms**, which contribute a nondissipative ($\delta$-function in $\omega$) piece that must be separated from the dissipative part;
- handling **conservation laws** — a conserved current has a Drude weight, and a nondecaying correlator is a statement about a conserved quantity, not a divergence;
- deciding whether the coefficient wanted is dissipative or nondissipative, since only the dissipative part is positive and only that part is a "transport coefficient" in the Green–Kubo sense.

So the defensible statement is: **the Kubo linear-response formalism is exact within its domain of assumptions; specific transport-coefficient formulas require the appropriate equilibrium state, operator definitions, limiting procedure, and treatment of nondissipative/contact contributions.** "Valid for any quantum system, any temperature, any material" was an overclaim and has been removed.

---

## 13.3 — The Fluctuation-Dissipation Theorem

### 13.3.1 — Statement

The imaginary part of the susceptibility (which governs energy absorption from a periodic perturbation) is directly related to the spectral density of equilibrium fluctuations:

$$\boxed{\text{Im}[\tilde\chi_{AA}(\omega)] = \frac{\omega}{2k_BT}S_A(\omega)}$$

where the **spectral density** (power spectrum of fluctuations):

$$S_A(\omega) = \int_{-\infty}^{\infty}\langle\hat A(0)\hat A(t)\rangle_0\,e^{i\omega t}\,dt$$

**Physical interpretation:** The rate at which the system absorbs energy from an external drive at frequency $\omega$ is exactly determined by how strongly the system spontaneously fluctuates at the same frequency at equilibrium. Noise and dissipation are the same phenomenon.

### 13.3.2 — Johnson-Nyquist Noise

Applied to a resistor $R$ at temperature $T$:

$$S_V(\omega) = 4k_BT\,\text{Re}[Z(\omega)] \xrightarrow{\omega\to 0} 4k_BTR$$

The **open-circuit voltage noise** of a resistor: $\langle V^2\rangle = 4k_BTR\Delta f$ in bandwidth $\Delta f$.

For $R = 1\,\text{M}\Omega$ at $T = 300$ K in $B = 10$ kHz: $V_{rms} = \sqrt{4k_BTR\Delta f} = \sqrt{4\times 1.38\times 10^{-23}\times 300\times 10^6\times 10^4} = 12.9\,\mu$V

This is the **floor on voltage measurement** — regardless of amplifier quality, the resistor itself generates this noise. It sets the sensitivity limit of every resistive sensor, every voltmeter, every impedance measurement.

### 13.3.3 — Shot Noise

When current is carried by discrete particles (electrons tunneling one at a time), the current fluctuations follow Poisson statistics:

$$S_I = 2eI \qquad\text{(full shot noise)}$$

The **Fano factor** $F = S_I/2eI$ measures the deviation from Poissonian statistics. $F = 1$: independent tunnel events. $F < 1$: sub-Poissonian (fermion antibunching; Pauli exclusion supresses fluctuations). $F > 1$: super-Poissonian (bunching; correlated transport).

**Engineering:** Shot noise limits the SNR of photodetectors and PIN diodes. The Fano factor is used to characterize quantum transport regimes — a direct measurement of whether transport is diffusive ($F = 1/3$ for 1D diffusive wire), ballistic ($F = 0$), or correlated.

---

## 13.4 — Deriving Ohm's Law

### 13.4.1 — The Kubo Conductivity

**Operator convention first, because the factors of $e$ and $V$ depend on it.** Two
different objects are both called "current" in the literature, and conflating them
is the usual source of a Drude derivation that loses an $e^2$:

| Symbol | Object | Units | Definition |
|---|---|---|---|
| $\hat{\mathbf{J}}$ | **total** charge current | C·m/s | $\hat{\mathbf{J}} = \sum_k \mathbf{j}_k$ |
| $\hat{\mathbf{j}}$ | **current density** | A/m² | $\hat{\mathbf{j}} = \hat{\mathbf{J}}/V$ |

For a free electron in band state $k$, with velocity $\mathbf{v}_k = \hbar\mathbf{k}/m_e$ and
charge $-e$, the single-particle current is

$$\mathbf{j}_k = -e\,\mathbf{v}_k = -\frac{e\hbar}{m_e}\,\mathbf{k}$$

so the total current operator is

$$\hat{\mathbf{J}} = -\frac{e\hbar}{m_e}\sum_k \mathbf{k}\,\hat c_k^\dagger\hat c_k = -\frac{e}{m_e}\hat{\mathbf{P}}$$

with $\hat{\mathbf{P}} = \sum_k \hbar\mathbf{k}\,\hat c_k^\dagger\hat c_k$ the total
momentum operator. **Note the sign** — the electron charge is $-e$ with $e>0$, and it
survives into the correlator as a positive $e^2$.

The conductivity **tensor** follows from the full retarded response. Writing the
current–current correlator in spectral (imaginary-time) form, with
$\beta = 1/k_BT$:

$$\sigma_{\alpha\beta}(\omega) = \frac{1}{V}\int_0^\infty dt\,e^{i\omega t}\int_0^\beta d\lambda\,\langle\hat J_\alpha(-i\hbar\lambda)\hat J_\beta(t)\rangle_0$$

Note the $1/V$: the prefactor converts a **total** current into a current **density**.
That single factor is what keeps the conductivity's units at $(\text{S/m})$.

For an isotropic system in the DC limit ($\omega\to 0$), the standard
Green–Kubo reduction drops the $\lambda$ integral (the $\omega=0$ correlator is
$\lambda$-independent) and contracts the tensor with $\frac{1}{3}\delta_{\alpha\beta}$:

$$\sigma_{DC} = \frac{1}{3Vk_BT}\int_0^\infty \langle\hat{\mathbf{J}}(0)\cdot\hat{\mathbf{J}}(t)\rangle_0\,dt$$

The $\frac{1}{3}$ is the **isotropic average** $\langle k_\alpha k_\beta\rangle \to \frac{1}{3}k^2\delta_{\alpha\beta}$ — it is required because a conductor has no preferred direction. It is *not* a fudge factor, and the next step shows exactly what it does.

### 13.4.2 — The Drude Result from Kubo

This section has to separate two things that are often run together: the
**algebraic step**, which is exact, and the **modelling step**, which is a
closure. Kubo relates a correlation function to a response coefficient. It does
*not* tell you what the correlation function is. That second question is where
the physics — and the honest labelling — lives.

#### Step 1 (exact): the free electron gas has *no* resistivity

Start from the occupation correlator of a non-interacting Fermi gas. Since a
fermionic mode satisfies $n_k^2 = n_k$,

$$\langle \hat n_k \hat n_{k'}\rangle_0 = \delta_{kk'}\,\langle n_k^2\rangle_0 = \delta_{kk'} f_k, \qquad f_k = \frac{1}{e^{\beta(\epsilon_k-\mu)}+1}$$

Note what this is *not*. The variance $\mathrm{Var}(n_k) = f_k(1-f_k)$ governs
number and charge fluctuations (and shot noise); it is not what enters dc
conductivity. The correlator above is a bare Fermi–Dirac occupation average.

Now the decisive step. For a quadratic dispersion, total momentum is conserved:

$$\hat{\mathbf{J}} = -\frac{e}{m_e}\hat{\mathbf{P}}, \qquad [\hat{\mathbf{P}},\hat{H}_0] = 0$$

so $\hat{\mathbf{J}}$ commutes with the Hamiltonian and

$$\langle \hat{\mathbf{J}}(0)\cdot\hat{\mathbf{J}}(t)\rangle_0 = \langle \hat{\mathbf{J}}^2\rangle_0 \qquad \text{(independent of } t\text{)}$$

The Green–Kubo integral of a constant **diverges**, giving
$\sigma_{DC}\to\infty$: the perfect conductor. *This is the correct exact answer
for a collision-free gas.*

The consequence is worth stating plainly, because it is the honest structure of
the whole result: **the exponential decay cannot be derived from the free
electron gas.** Any finite resistivity is a statement about collisions. Kubo is
not incomplete here — it is accurately reporting that dissipation requires a
dissipation mechanism, and that mechanism has to be supplied.

#### Step 2 (closure): the relaxation-time model

`[PHENOMENOLOGICAL]` The one modelling input is a **single relaxation time**
$\tau$ (Ch. 6 §6.7.3), modelling electron–phonon and electron–impurity
scattering as a memory kernel with one time constant. In the uniform-field
limit this is the Drude/BGK kinetic equation,

$$\frac{\partial f}{\partial t} - \frac{e\mathbf{E}}{m_e}\cdot\nabla_{\mathbf{v}}f = -\frac{f - f_0}{\tau}$$

where $f_0$ is the (field-shifted) equilibrium distribution. Solving for a
tagged particle and taking the velocity autocorrelation gives

$$C^{\alpha\beta}_{vv}(t) \equiv \langle \hat v^\alpha(0)\hat v^\beta(t)\rangle_0 = \frac{k_BT}{m_e}\,\delta_{\alpha\beta}\,e^{-t/\tau}$$

Two ingredients, both named deliberately:

- the **exponential** $e^{-t/\tau}$ — this is the closure. A single time
  constant is an approximation; the true correlator has a long tail.
- the **prefactor** $k_BT/m_e$ — this is *classical* equipartition,
  $\tfrac{1}{2}m_e\langle v^2\rangle = \tfrac{3}{2}k_BT$ per degree of freedom.

#### Step 3: why that classical ingredient is legitimate anyway

This is the subtle point, and it is where a naive derivation goes wrong. A real
metal is a strongly degenerate Fermi gas with $k_BT \ll E_F$. In that regime
per-particle equipartition is **false**: the typical speed is $v_F$, not
$\sqrt{k_BT/m_e}$, and $\langle v^2\rangle \neq 3k_BT/m_e$. Using equipartition
here looks like a contradiction.

It is not, and the reason is structural. The $k_BT$ sitting in $C_{vv}$ is
**divided out** by the $1/(k_BT)$ in the Green–Kubo prefactor. It cancels
identically before any physical result is formed.

> **General Green–Kubo fact.** The $1/k_BT$ normalization is what converts a raw
> correlation function into a response coefficient. Because it cancels the
> classical thermal scale in the correlator, Green–Kubo formulas routinely *look*
> classical while remaining valid in strongly quantum systems. The Drude
> conductivity is a standard instance: it is correct for copper despite the
> equipartition argument being inapplicable to copper's electrons.

A fully quantum treatment of the degenerate gas gives a correlator with $O(T^2)$
corrections and a non-exponential tail; the memory-function formulation absorbs
these into $M(\omega)$, and the leading low-frequency result is unchanged.

#### Step 4: total current, and the result

Under the same closure, and using **molecular chaos** (Boltzmann's first
Stosszahlansatz: distinct particles have uncorrelated velocities,
$\langle \hat v_i^\alpha(0)\hat v_j^\beta(t)\rangle_0 = \delta_{ij}C^{\alpha\beta}_{vv}(t)$),

$$\hat{\mathbf{J}} = -e\sum_{i=1}^{N}\hat{\mathbf{v}}_i \quad\Longrightarrow\quad \langle \hat J^\alpha(0)\hat J^\beta(t)\rangle_0 = e^2 N C^{\alpha\beta}_{vv}(t) = \frac{n_e e^2 V k_BT}{m_e}\,\delta_{\alpha\beta}\,e^{-t/\tau}$$

with $n_e$ the number density and $N = n_eV$ the electron count. Dimension check:
$[e^2k_BT/m_e] = \text{C}^2\!\cdot\!\text{J}/\text{kg} = (\text{C}\!\cdot\!\text{m/s})^2$, current squared — correct for two *total* currents.

Substituting into the Green–Kubo formula, with the $\delta_{\alpha\beta}$
contraction $\mathbf{J}\cdot\mathbf{J} = \sum_\alpha\langle J_\alpha J_\alpha\rangle$
supplying the factor of 3 that cancels the isotropic $\frac{1}{3}$:

$$\sigma_{DC} = \frac{1}{3Vk_BT}\int_0^\infty \frac{n_e e^2 Vk_BT}{m_e}\,\underbrace{3}_{\delta_{\alpha\beta}\ \text{contraction}}\,\underbrace{e^{-t/\tau}dt}_{\tau} = \frac{1}{3Vk_BT}\cdot\frac{3n_e e^2 Vk_BT\tau}{m_e}$$

$$\boxed{\sigma_{DC} = \frac{n_e e^2\tau}{m_e}}$$

The $V$ and $k_BT$ cancel between correlator and prefactor; the $1/3$ and 3
cancel. What survives is $n_e e^2\tau/m_e$ — the **Drude formula**: $e^2$ because
the current is *charge* current, $n_e$ because it is a carrier density, and
$\tau$ because it is the integral of the decay. The mean free path is
$\ell = v_F\tau$, and the resistivity:

$$\rho = \frac{1}{\sigma} = \frac{m_e}{n_e e^2\tau} = \frac{m_e v_F}{n_e e^2\ell}$$

**Frequency-dependent conductivity** (same closure, with the $e^{i\omega t}$ weight
converting the time integral to a frequency response):

$$\sigma(\omega) = \frac{n_ee^2\tau}{m_e}\cdot\frac{1}{1 - i\omega\tau}, \qquad \sigma_0 = \frac{n_e e^2\tau}{m_e}$$

At $\omega\tau \ll 1$: purely real, Ohmic. At $\omega\tau \gg 1$: purely imaginary, reactive. The crossover at $\omega = 1/\tau \sim 10^{13}$–$10^{14}$ Hz (infrared) marks where metals transition from good reflectors to transparent.

> [!warning] Epistemic summary of this derivation
> | Step | Status |
> |---|---|
> | Kubo relates correlator to response | `[DERIVATION]` — exact given linear response |
> | Free Fermi gas gives $\sigma\to\infty$ | `[DERIVATION]` — exact, and the reason a closure is needed |
> | Exponential decay $e^{-t/\tau}$ | `[PHENOMENOLOGICAL]` — **closure**, not derived |
> | Equipartition prefactor $k_BT/m_e$ | `[APPROXIMATION]` — classical, but cancels out of $\sigma$ |
> | Molecular chaos | `[APPROXIMATION]` — valid for $L \gg \ell$; breaks in ballistic mesoscopic regimes |
> | $\sigma = n_e e^2\tau/m_e$ | `[DERIVATION]` within the closure |
>
> The framework is exact; the closure is a model; and the result is correct for
> degenerate metals because the one classical ingredient cancels.

### 13.4.3 — Ohm's Law as an Emergent, Not Fundamental, Law

**Why Ohm's law has an arrow of time:** The current-current correlator decays because electrons scatter off phonons and defects. Each scattering event is irreversible (the electron's phase is randomized). This decoherence — the same operation as tracing out environmental degrees of freedom in Ch. 10 §10.1.3 — is what makes $\sigma$ finite and real.

**In a perfect crystal at $T = 0$:** No phonons, no impurities, no scattering. The correlator never decays. $\tau\to\infty$, $\sigma\to\infty$ — perfect conductance without applied voltage. This is not Ohm's law; it is the non-dissipative current of a superconductor or a topological edge state.

**Ohm's law is not fundamental.** It is an emergent law valid in the regime of diffusive, decoherent transport. Its emergence from the Kubo formula tells you exactly when it fails: when mean free path exceeds the device size (ballistic transport), when topology protects the current from backscattering, or when strong correlations destroy the quasiparticle picture.

---

## 13.5 — Deriving Fourier's Law of Heat Conduction

### 13.5.1 — The Heat Current Operator

For electrons, the heat current is the energy current minus the chemical potential times the particle current:

$$\hat{\mathbf{J}}_Q = \hat{\mathbf{J}}_E - \mu\hat{\mathbf{J}}_N = \frac{\hbar}{V}\sum_k(E_k - \mu)\mathbf{v}_k\hat c_k^\dagger\hat c_k$$

The Kubo formula for thermal conductivity (at zero electric field):

$$\kappa_{\alpha\beta} = \frac{1}{Vk_BT^2}\int_0^\infty\langle\hat J_Q^\alpha(0)\hat J_Q^\beta(t)\rangle_0\,dt$$

### 13.5.2 — The Result and the Wiedemann-Franz Law

For metals (electronic heat conduction dominates), the same relaxation time $\tau$ governs both charge and heat transport. Taking the ratio:

$$\frac{\kappa}{\sigma T} = \frac{\pi^2}{3}\left(\frac{k_B}{e}\right)^2 = L_0 = 2.44\times 10^{-8}\,\text{W}\cdot\Omega\cdot\text{K}^{-2}$$

This is the **Wiedemann-Franz law** with the **Lorenz number** $L_0$ — a constant depending only on fundamental constants, independent of material. It holds for all metals in the diffusive regime and is confirmed to $\sim 10\%$ across metals from $-200°$C to $+600°$C.

`[APPROXIMATION]` — **the universality of $L_0$ is a statement about a scattering
model, not about metals.** The ratio is constant precisely because the *same*
$\tau$ cancels from both $\sigma$ and $\kappa$. That requires elastic scattering
only. When heat and charge relax by different mechanisms, the ratio drifts:

| Regime | What happens to $\kappa/\sigma T$ |
|---|---|
| Elastic scattering, low $T$ | approaches $L_0$ |
| Electron–phonon scattering, high $T$ | $\tau_Q \neq \tau_N$ — ratio below $L_0$ |
| Transition metals, strong spin–orbit | $s$-wave scattering suppressed — ratio far above $L_0$ |
| Strongly correlated (heavy fermions, cuprates) | quasiparticle picture fails — no constant ratio |

So "universal constant, independent of material" is true to $\sim 10\%$ across
ordinary metals and false in exactly the materials where the interesting physics
is. Reading the deviations diagnostically is more useful than treating $L_0$ as
a law.

**Physical origin:** Both charge and heat are carried by electrons near the Fermi level. The energy $E_F$ per electron is the same whether you are measuring electrical or thermal transport. The factor $k_B^2/e^2$ converts energy² (thermal) to energy/charge (electrical) squared.

**Engineering consequence:** Wiedemann-Franz allows you to estimate thermal conductivity of a metal from its electrical resistivity (easier to measure): $\kappa = L_0\sigma T$. For copper at 300 K: $\sigma = 6\times 10^7$ S/m → $\kappa = 2.44\times 10^{-8}\times 6\times 10^7\times 300 = 439$ W/m·K (measured: 401 W/m·K — 10% error from non-Drude effects).

### 13.5.3 — Phonon Thermal Conductivity

For insulators and semiconductors (no free electrons), heat is carried by phonons. The Green-Kubo formula:

$$\kappa = \frac{1}{Vk_BT^2}\int_0^\infty\langle\hat{\mathbf{J}}_Q^{ph}(0)\cdot\hat{\mathbf{J}}_Q^{ph}(t)\rangle_0\,dt$$

In kinetic theory language (the result of integrating the correlator):

$$\kappa_{phonon} = \frac{1}{3}C_v v_s^2\tau_{ph} = \frac{1}{3}C_v v_s\ell_{ph}$$

where $C_v$ is specific heat (per unit volume, Ch. 10 §10.7.3), $v_s$ is the phonon group velocity, and $\ell_{ph} = v_s\tau_{ph}$ is the phonon mean free path.

**High thermal conductivity requires:** large $C_v$ (many phonon modes active) × large $v_s$ (stiff material, strong bonds) × large $\ell_{ph}$ (few scattering events).

|Material|$\kappa$ (W/m·K)|Primary mechanism|Why|
|---|---|---|---|
|Diamond|2000|Phonon|Light C atoms, stiff bonds, few defects|
|Silver|429|Electron|High $\sigma$, Wiedemann-Franz|
|Copper|401|Electron|High $\sigma$, Wiedemann-Franz|
|Silicon|148|Phonon|Moderate $v_s$, moderate $\ell_{ph}$|
|Glass|1.0|Phonon|Amorphous → very short $\ell_{ph}$|
|Air|0.026|Gas kinetics|Very low $C_v$ per unit volume|

---

## 13.6 — Deriving Fick's Law of Diffusion

### 13.6.1 — The Velocity Autocorrelation Function

The diffusivity of a species in a medium is given by the **Green-Kubo formula for diffusion** — the integral of the velocity autocorrelation function (VACF):

$$D = \frac{1}{3}\int_0^\infty\langle\mathbf{v}(0)\cdot\mathbf{v}(t)\rangle_0\,dt$$

For a particle undergoing Brownian-like motion with momentum relaxation time $\tau$: $\langle v_\alpha(0)v_\alpha(t)\rangle = \frac{k_BT}{m}e^{-t/\tau}$

$$D = \frac{1}{3}\cdot 3\cdot\frac{k_BT}{m}\tau = \frac{k_BT\tau}{m} = \frac{k_BT}{m}\cdot\frac{\ell}{v_{th}}$$

where $\ell$ is the mean free path and $v_{th} = \sqrt{k_BT/m}$ is the thermal velocity.

> [!note] Same correlator, different justification than §13.4.2
> The velocity autocorrelation used here is formally identical to the one in
> §13.4.2, but the classical equipartition prefactor is *genuinely* appropriate
> here: a Brownian tracer in a classical thermal medium is non-degenerate, so
> $v_{th} = \sqrt{k_BT/m}$ really is the relevant speed. For conduction electrons
> in a metal it is not, which is why §13.4.2 Step 3 has to argue that the
> classical prefactor cancels out of $\sigma_{DC}$. Same building block, different
> regime — worth keeping straight, because applying the Einstein relation to
> degenerate electrons without noticing the cancellation is a common error.

### 13.6.2 — The Einstein-Smoluchowski Relation

For a charged particle (charge $q$, mobility $\mu_{mob} = e\tau/m$):

$$D = \frac{k_BT}{m}\tau = \frac{k_BT}{q}\cdot\frac{q\tau}{m} = \frac{k_BT}{q}\mu_{mob}$$

$$\boxed{D = \frac{k_BT}{q}\mu_{mob}}$$

This is the **Einstein-Smoluchowski (or Einstein) relation** — a direct consequence of the fluctuation-dissipation theorem. It connects:

- **Diffusion** $D$: random spreading driven by thermal fluctuations (Fick's law)
- **Drift** $\mu_{mob}$: directed motion under an applied force (Ohm's law)

Both are caused by the same scattering events. They cannot be independently specified — knowing one gives the other through $k_BT/q$.

**Engineering:** In semiconductors, $D_n = \mu_n k_BT/e$ and $D_p = \mu_p k_BT/e$ (thermal voltage $V_T = k_BT/e = 26$ mV at 300 K). The p-n junction equations (Shockley diode equation), minority carrier diffusion lengths, and transistor gain all trace back to this relation.

### 13.6.3 — Fick's First and Second Laws

With the Green-Kubo diffusivity, the constitutive relation (Fick's first law):

$$\mathbf{J}_N = -D\nabla c$$

Combined with the continuity equation (mass conservation, Noether for particle number, Ch. 1 §1.7):

$$\frac{\partial c}{\partial t} + \nabla\cdot\mathbf{J}_N = 0 \quad\Longrightarrow\quad \boxed{\frac{\partial c}{\partial t} = D\nabla^2 c}$$

**Fick's second law** — the diffusion equation. Same mathematical structure as the heat equation (Ch. 12 §12.1.1 with $\sigma = 0$), as the charge diffusion equation in semiconductors, and as the Schrödinger equation in imaginary time. One equation, four domains.

---

## 13.7 — Deriving Newton's Law of Viscosity

### 13.7.1 — The Stress Tensor Autocorrelation

The viscosity of a fluid is given by the Green-Kubo formula applied to the off-diagonal stress tensor component $\hat\sigma_{xy}$ (the momentum flux in the $y$-direction from flow in the $x$-direction):

$$\eta = \frac{V}{k_BT}\int_0^\infty\langle\hat\sigma_{xy}(0)\hat\sigma_{xy}(t)\rangle_0\,dt$$

For a simple fluid with a single structural relaxation time $\tau_v$:

$$\langle\hat\sigma_{xy}(0)\hat\sigma_{xy}(t)\rangle_0 = \frac{nk_BT}{V}e^{-t/\tau_v}$$

$$\eta = nk_BT\tau_v$$

The viscosity equals the thermal energy density times the structural relaxation time.

**Engineering interpretation:** Viscosity measures how long a fluid "remembers" a stress. A gas has $\tau_v \sim \ell/\bar v \sim$ ps (very short memory, low $\eta$); a polymer melt has $\tau_v \sim$ ms–s (long memory, very high $\eta$); glass at room temperature has $\tau_v > 10^{12}$ s — effectively infinite (solid-like).

### 13.7.2 — Temperature Dependence of Viscosity

**Gases** (kinetic theory): $\eta \propto \sqrt{T}$ (more collisions at higher $T$, but higher mean free velocity; they nearly cancel — viscosity of gases **increases** with temperature).

**Liquids** (thermally-activated flow, Arrhenius): $\eta = \eta_0 e^{E_a/k_BT}$ — viscosity **decreases** with temperature (activation energy $E_a$ for a molecule to squeeze past neighbors).

**Polymers** (WLF equation — empirical): log($\eta$) varies with $T - T_g$ where $T_g$ is the glass transition temperature.

This difference (gas vs. liquid viscosity-temperature behavior) is a key practical indicator for the ChE engineer selecting a working fluid.

---

## 13.8 — Deriving Hooke's Law: Elastic Moduli

### 13.8.1 — The Stress-Strain Correlation

The elastic modulus tensor $C_{ijkl}$ can be derived from two routes:

**Route 1: Green-Kubo** (isothermal modulus):

$$C_{ijkl} = \frac{V}{k_BT}\int_0^\infty\langle\hat\sigma_{ij}(0)\hat\sigma_{kl}(t)\rangle_0\,dt\bigg|_{t\to 0}$$

For an elastic solid (no viscous relaxation at short times), the correlator does not decay to zero at $t\to 0^+$ but retains its elastic value — giving a finite modulus.

**Route 2: Second derivative of free energy** (more practical for static moduli):

$$C_{ijkl} = \frac{1}{V}\frac{\partial^2 F}{\partial\varepsilon_{ij}\partial\varepsilon_{kl}}\bigg|_{\varepsilon=0}$$

where $\varepsilon_{ij}$ is the strain tensor. This can be computed from first-principles DFT (density functional theory, using the band structure machinery of Ch. 6) by calculating how the total energy changes with strain.

### 13.8.2 — Hooke's Law for Engineering

The constitutive relation for a linear elastic solid:

$$\sigma_{ij} = C_{ijkl}\varepsilon_{kl}$$

For an isotropic material, $C_{ijkl}$ has only two independent parameters (Lamé constants $\lambda$, $\mu_L$):

$$\sigma_{ij} = \lambda\varepsilon_{kk}\delta_{ij} + 2\mu_L\varepsilon_{ij}$$

Equivalently, in terms of Young's modulus $E$ and Poisson's ratio $\nu$:

$$E = \frac{\mu_L(3\lambda+2\mu_L)}{\lambda+\mu_L}, \qquad \nu = \frac{\lambda}{2(\lambda+\mu_L)}$$

**The same Kubo framework shows that Hooke's law has a frequency-dependent generalization.** For a **viscoelastic** material:

$$\tilde C(\omega) = \frac{V}{k_BT}\int_0^\infty\langle\hat\sigma_{xy}(0)\hat\sigma_{xy}(t)\rangle_0\,e^{i\omega t}\,dt$$

At $\omega\to 0$: recovers the static elastic modulus (material responds slowly and fully). At $\omega\to\infty$: recovers the unrelaxed (glassy) modulus (material doesn't have time to rearrange). At intermediate $\omega$: complex modulus $C' + iC''$ — energy storage and loss.

---

## 13.9 — The Onsager Matrix: All Transport Unified

### 13.9.1 — Coupled Transport

When multiple driving forces act simultaneously, the currents become coupled. Define thermodynamic forces:

$$\mathbf{X}_E = \mathbf{E} - \frac{\nabla\mu}{e}, \quad \mathbf{X}_Q = -\frac{\nabla T}{T}$$

The Onsager transport equations:

$$\begin{pmatrix}\mathbf{J}^e \\ \mathbf{J}^Q\end{pmatrix} = \begin{pmatrix}L_{EE} & L_{EQ} \\ L_{QE} & L_{QQ}\end{pmatrix}\begin{pmatrix}\mathbf{X}_E \\ \mathbf{X}_Q\end{pmatrix}$$

**Diagonal elements** (from Kubo):

- $L_{EE}$: charge current from electric force → conductivity $\sigma = L_{EE}/T$
- $L_{QQ}$: heat current from temperature gradient → thermal conductivity $\kappa = (L_{QQ} - L_{QE}^2/L_{EE})/T^2$

**Off-diagonal elements** (from Kubo — cross-correlators):

- $L_{EQ} = L_{QE}$: charge current from temperature gradient (Seebeck), or heat current from electric field (Peltier)

### 13.9.2 — Onsager Reciprocal Relations

$$\boxed{L_{AB} = L_{BA}}$$

**Proof:** Time-reversal symmetry of the equilibrium correlation functions. Under time reversal, $\langle J_A(0)J_B(t)\rangle_0 = \langle J_B(0)J_A(t)\rangle_0$ for currents with the same sign under time reversal (both odd or both even). Therefore the Kubo integrals are equal: $L_{AB} = L_{BA}$.

**Physical consequence:** If a temperature gradient drives a charge current (Seebeck effect), then an electric field drives an equal heat current (Peltier effect). These must be related — you cannot have one without the other.

### 13.9.3 — Thermoelectric Coefficients

**Seebeck coefficient** (thermopower) $S$ — open-circuit voltage per degree:

$$S = \frac{L_{EQ}}{TL_{EE}} = \frac{\Delta V}{\Delta T}\bigg|_{J^e=0}$$

For a free electron gas: $S = -\frac{\pi^2k_B^2T}{3eE_F}$ (Mott formula) At 300 K for copper ($E_F = 7$ eV): $S \approx -1.8\,\mu$V/K (measured: $-1.8\,\mu$V/K) ✓

**Peltier coefficient** $\Pi$ — heat current per unit charge current:

$$\Pi = \frac{L_{QE}}{L_{EE}}$$

**Kelvin's relation** (from Onsager reciprocity):

$$\Pi = ST$$

This is not an independent empirical law — it is the Onsager reciprocal relation $L_{QE} = L_{EQ}$ written in terms of $S$ and $\Pi$.

**Thermoelectric figure of merit:**

$$ZT = \frac{S^2\sigma T}{\kappa} = \frac{S^2 L_{EE}}{L_{QQ} - L_{QE}^2/L_{EE}}$$

$ZT > 1$ is the threshold for useful thermoelectric devices. Best materials (Bi₂Te₃ alloys, SnSe single crystals): $ZT \approx 2$–$3$. The Onsager matrix shows exactly what needs to be optimized — maximize $S^2\sigma$ (power factor) while minimizing $\kappa$ (thermal conductivity). These are coupled through the underlying band structure and phonon spectrum.

---

## 13.10 — The Generalized Transport Law: The Complete Table

The five constitutive laws, each in its Green–Kubo form. Read the table as *five instances of one template*, not five outputs of one calculation — and note that $C$ is a static susceptibility, not a transport coefficient (§13.9.2):

$$\boxed{\mathbf{J}_X = -L_{XX}\nabla\phi_X}$$

|Current $\mathbf{J}_X$|Coefficient $L_{XX}$|Potential $\phi_X$|Named Law|Branch|Kubo integrand|
|---|---|---|---|---|---|
|Charge density $\mathbf{J}^e$|$\sigma$ (conductivity)|Electric potential $V$|**Ohm's law**|EEE|$\langle\hat J^e(0)\hat J^e(t)\rangle$|
|Heat flux $\mathbf{J}^Q$|$\kappa$ (thermal cond.)|Temperature $T$|**Fourier's law**|ME, ChE|$\langle\hat J^Q(0)\hat J^Q(t)\rangle$|
|Particle flux $\mathbf{J}^N$|$D$ (diffusivity)|Concentration $c$|**Fick's law**|ChE, CE|$\langle\mathbf{v}(0)\mathbf{v}(t)\rangle$|
|Momentum flux $\tau_{xy}$|$\eta$ (viscosity)|Velocity $u$|**Newton's viscosity**|ME, CE|$\langle\hat\sigma_{xy}(0)\hat\sigma_{xy}(t)\rangle$|
|Stress $\sigma_{ij}$|$C_{ijkl}$ (elastic moduli)|Strain $\varepsilon_{kl}$|**Hooke's law**|CE, ME|$\partial^2 F/\partial\varepsilon^2$|

**Off-diagonal (Onsager) transport** also from Kubo cross-correlators:

|Effect|From|Coefficient|Branch|
|---|---|---|---|
|Seebeck|$\langle\hat J^e(0)\hat J^Q(t)\rangle$|$S = L_{EQ}/TL_{EE}$|EEE, ME|
|Peltier|(Onsager: $L_{QE} = L_{EQ}$)|$\Pi = ST$|EEE, ME|
|Soret (thermodiffusion)|$\langle\hat J^N(0)\hat J^Q(t)\rangle$|$S_T$|ChE|
|Dufour (diffusion-thermo)|(Onsager)|$D^Q$|ChE|

**This table is the architectural backbone of Layer 2 engineering science.** Every constitutive relation used in electrical engineering, mechanical engineering, civil engineering, and chemical engineering is one row in this table. Every coefficient in the table is a Green-Kubo integral of an equilibrium quantum mechanical correlation function.

---

## 13.11 — Beyond Kubo: Landauer and Topology

### 13.11.1 — When Kubo Fails: The Ballistic Regime

Kubo assumes **diffusive transport**: the electron scatters many times in traversing the device ($L \gg \ell_{mfp}$). As devices shrink below the mean free path, the Kubo formula overestimates the resistance.

For a **ballistic conductor** (no scattering inside the channel), each transverse mode contributes a conductance:

$$G_n = \frac{2e^2}{h}T_n$$

where $T_n \in [0,1]$ is the **transmission probability** of mode $n$. Total conductance:

$$\boxed{G = \frac{2e^2}{h}\sum_n T_n}$$

This is the **Landauer formula** (1957). For a perfect conductor ($T_n = 1$) with $N$ modes: $G = 2Ne^2/h$.

**The quantum of conductance** $G_0 = 2e^2/h \approx 7.75\times 10^{-5}$ S $= 1/(12.9\,\text{k}\Omega)$: the conductance of a single perfectly transmitting channel. First measured directly in quantum point contacts (1988).

**The hierarchy of transport theories:**

```
Quantum field theory (Ch. 0)
        ↓ Kubo formula (this chapter)
Diffusive: G = σA/L     (Ohm's law, L ≫ ℓ_mfp)
        ↓ Landauer
Ballistic: G = (2e²/h)ΣTₙ  (L < ℓ_mfp)
        ↓ Topology (Ch. 7)
Topological: G = νe²/h  (Tₙ = 1, protected by topology)
```

### 13.11.2 — The Quantum Hall Conductance from Topology

In the integer quantum Hall effect (Ch. 7 §7.3), each edge channel has $T_n = 1$ (backscattering forbidden by chirality) and there are $\nu$ channels:

$$G_{Hall} = \frac{\nu e^2}{h}$$

This is the Landauer formula with perfect transmission — but the reason for $T_n = 1$ is topological (Chern number), not accidental. The Kubo formula gives the same result when applied to the full 2D system:

$$\sigma_{xy} = \frac{e^2}{h}\sum_{n\in\text{filled}}\frac{1}{2\pi}\iint_{\text{BZ}}\Omega_n(\mathbf{k})\,d^2k = \nu\frac{e^2}{h}$$

**The Kubo formula and topology connect at the integer QHE** — the Kubo integral over the Brillouin zone counts the Chern number. This is the TKNN result (Ch. 7 §7.2.1), now seen from the transport theory perspective.

---

## 13.12 — When Transport Laws Break Down (and What to Do)

|Failure|Regime|Alternative|Return to|
|---|---|---|---|
|Ohm's law (high E)|$eE\ell \gtrsim E_F$: hot carriers|Nonlinear Boltzmann equation; impact ionization|L1 (band structure, Ch. 6)|
|Ohm's law (small L)|$L \lesssim \ell_{mfp}$: ballistic|Landauer formula|L1 (quantum transport, Ch. 7)|
|Fourier's law (nanoscale)|$L \lesssim \ell_{phonon}$: ballistic phonons|Boltzmann transport equation for phonons|L1 (phonon dispersion, Ch. 6)|
|Fick's law (crowded medium)|High concentration: interactions matter|Generalized diffusion equation; activity coefficients|L2 (thermodynamics, Ch. 10)|
|Newton's viscosity (non-Newtonian)|Polymers, colloids: $\tau_{flow}$ spans many decades|Generalized Maxwell/Oldroyd equations|L2 (viscoelasticity)|
|Hooke's law (large strain)|$\varepsilon > 0.01$: nonlinear elasticity|Hyperelastic models (Mooney-Rivlin, Ogden)|L2 (continuum mechanics, Ch. 15)|
|All laws (strongly correlated)|Mott insulators, strange metals|DMFT, slave-boson, RVB theories|L0/L1 (beyond quasiparticles)|

The engineer who knows this table knows exactly when to trust their formula and exactly where to go when it fails.

---

## 13.13 — Summary

Bridge B.e is complete. The five transport laws, unified:

|Step|Operation|Result|
|---|---|---|
|Linear response theory|Perturbation on $\hat\rho_0$|Response $\propto$ equilibrium correlator|
|Kubo formula|Time-integrate current correlator|Transport coefficient $L_{AB}$|
|FDT|Imaginary $\chi$ ↔ noise spectrum|$S_V = 4k_BTR$ (Johnson-Nyquist)|
|Ohm's law|Charge current-current Kubo|$\sigma = ne^2\tau/m$; $\rho\propto T$|
|Fourier's law|Heat current-current Kubo|$\kappa = L_0\sigma T$ (Wiedemann-Franz)|
|Fick's law|Velocity autocorrelation|$D = k_BT\mu/q$ (Einstein relation)|
|Newton viscosity|Stress autocorrelation|$\eta = nk_BT\tau_v$|
|Hooke's law|Free energy second derivative|$C_{ijkl}$ from DFT or Kubo|
|Onsager matrix|Cross-correlators + reciprocity|Seebeck-Peltier-Thomson relations|
|Landauer|Ballistic transport|$G = (2e^2/h)\sum T_n$|
|Topology|$T_n = 1$ protected|$G = \nu e^2/h$ (QHE)|

---

## 13.14 — Engineering Thread

|Physics|Application|
|---|---|
|$\sigma = ne^2\tau/m$|Conductor sizing; resistor design; contact resistance minimization|
|$\sigma(\omega) = \sigma_0/(1-i\omega\tau)$|Skin effect; RF conductor loss; plasma frequency|
|Wiedemann-Franz $\kappa = L_0\sigma T$|Thermal management: copper heat spreaders; Peltier coolers|
|Phonon $\kappa = C_v v_s\ell/3$|Thermal interface materials; diamond heat sinks; thermoelectric leg design|
|Einstein relation $D = \mu k_BT/e$|Semiconductor diffusion length $L_D = \sqrt{D\tau}$; p-n junction analysis|
|Fick's equation $\partial_t c = D\nabla^2 c$|Semiconductor doping profiles; ChE mass transfer; concrete carbonation|
|Newton viscosity $\eta = nk_BT\tau_v$|Pipe flow ($\Delta P = 8\eta LQ/\pi r^4$); lubrication; rheology|
|Viscoelastic $\tilde C(\omega)$|Polymer processing; damping materials; tire hysteresis|
|Seebeck $S$, Peltier $\Pi = ST$|Thermocouples; Peltier coolers; thermoelectric generators|
|$ZT = S^2\sigma T/\kappa$|Thermoelectric device efficiency optimization|
|Johnson-Nyquist $S_V = 4k_BTR$|Amplifier noise floor; sensor sensitivity limit; low-noise design|
|Landauer $G = (2e^2/h)\sum T_n$|Nanoscale transistor resistance; quantum point contact sensors|
|QHE $G = \nu e^2/h$|Primary resistance standard; metrological applications|

---

## 13.15 — Looking Ahead: Bridge B Complete, Layer 2 Assembled

With Chapter 13, all five Bridge B paths are complete:

```
Layer 1 (Quantum)
  │
  ├─ B.a (ħ→0) ──────────────► Classical mechanics (Ch. 9)
  ├─ B.b (N→∞) ──────────────► Thermodynamics (Ch. 10)
  ├─ B.c (U(1) classical) ───► Maxwell's equations (Ch. 11)
  │                              └─ EM waves, optics (Ch. 12)
  ├─ B.d (weak-field GR) ────► Newton's gravity (Ch. 8)
  └─ B.e (Kubo) ─────────────► Generalized transport law (Ch. 13)
                                  └─ Ohm, Fourier, Fick, viscosity, Hooke
```

**Layer 2 is now complete.** Every classical engineering science equation you will use in Chapters 15–21 is assembled. The inventory:

- Equations of motion: Newton (Ch. 8, 9), Euler-Lagrange (Ch. 9)
- Thermodynamics: four laws, partition function, phase diagrams (Ch. 10)
- Electromagnetism: Maxwell's equations, wave equation, KVL/KCL (Ch. 11, 12)
- Transport: Ohm, Fourier, Fick, viscosity, Hooke (Ch. 13)
- Continuum mechanics: stress-strain, Navier-Stokes (Ch. 15)

**Chapter 15** covers continuum mechanics (fluid and solid) — deriving Navier-Stokes from Newton + statistical mechanics and the stress-strain equation from Hooke's law in the continuum limit.

**Chapter 16** then shows that the wave equation and diffusion equation appear identically in every domain — the final unification of Layer 2 before the descent to engineering systems begins in Chapter 17 (Bridge C).

---

_End of Chapter 13. End of Bridge B._

---

_Next: Chapter 14 — Transport Phenomena and Thermoelectrics (Layer 2 Applied)_