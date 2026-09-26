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
| Assumptions | linear response; equilibrium; ergodicity (so $\tau$ is a state variable, not history-dependent); elastic scattering only; **single relaxation time** (the Drude closure — the only modelling input); Boltzmann equation valid in the local, diffusive regime (fails for $L \lesssim \ell$, §13.4.4). Note: the result is derived via the linearized Boltzmann equation and the Fermi-surface $\delta$-function, so it holds for degenerate electrons ($k_BT \ll E_F$) without a classical-equipartition assumption — see §13.4.2 |
| Physics retained | dissipation, the arrow of time, the relation between charge/heat/momentum diffusion coefficients; Fermi-surface restriction of the current-carrying states |
| Physics neglected | inelastic and memory-dependent scattering, phonon drag, interactions (in the elastic limit), non-equilibrium distributions, band-structure anisotropy. The **free** Fermi gas is exact and gives $\sigma\to\infty$; all finite resistivity comes from the closure |
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

> [!warning] This is the *classical* limit, not the general quantum relation
> `[APPROXIMATION]` The boxed formula is valid when $\hbar\omega \ll k_BT$ — the
> **classical (high-temperature) regime**, where the quantum energy scale is
> negligible compared with thermal energy and the Bose/detailed-balance factor
> reduces to $1/k_BT$.
>
> The general quantum fluctuation-dissipation relation carries a spectral
> factor that depends on $\hbar\omega/k_BT$. One standard convention is
>
> $$\text{Im}[\tilde\chi_{AA}(\omega)] = \frac{\omega}{1-e^{-\hbar\omega/k_BT}}\big[S_A(\omega)-S_A(-\omega)\big]$$
>
> For $k \gg 1$ (classical) the prefactor $\to \omega/2k_BT$ and detailed balance
> $S_A(\omega) = e^{-\hbar\omega/k_BT}S_A(-\omega)$ makes the bracket $\propto k_BT$,
> recovering the boxed result. For $\hbar\omega \gtrsim k_BT$ — zero-point
> fluctuations, cryogenic electronics, any genuinely quantum regime — it does
> not, and the classical form must not be used. Since this chapter presents
> itself as *quantum* linear-response theory, the distinction is flagged rather
> than glossed.

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

### 13.4.2 — The Drude Result

The honest structure of this result is a chain, and it is worth writing the chain
down before filling in any of its links:

```text
Kubo                        exact linear-response relation
  ↓
current–current correlator exact many-body object (not elementary)
  ↓
Boltzmann / memory function microscopic transport equation
  ↓
relaxation-time closure     ← the one modelling assumption
  ↓
Drude form                  σ = nₑe²τ/mₑ
```

Each arrow is a different kind of step. Only the first is "the framework".

#### Why the correlator cannot be skipped, and why it cannot be guessed

An earlier version of this section tried to evaluate $\langle \hat J^\alpha\hat J^\beta\rangle$
directly and reached the right answer through a wrong correlator. The failure is
instructive, so it is worth recording what actually blocks the direct route.

Start from the one occupation relation that *is* elementary. Since a fermionic
mode satisfies $n_k^2 = n_k$,

$$\langle \hat n_k \hat n_{k'}\rangle_0 = \delta_{kk'}\,\langle n_k^2\rangle_0 = \delta_{kk'} f_k, \qquad f_k = \frac{1}{e^{\beta(\epsilon_k-\mu)}+1}$$

(Note what this is *not*: the variance $\mathrm{Var}(n_k) = f_k(1-f_k)$ governs
number and charge fluctuations and shot noise. It is not the dc conductivity.)

But the correct number correlator does not deliver the current correlator. Two
obstructions:

1. **A non-interacting gas has no resistivity at all.** For quadratic
   dispersion, $[\hat{\mathbf{P}},\hat{H}_0]=0$, so
   $\hat{\mathbf{J}} = -e\hat{\mathbf{P}}/m_e$ is conserved and
   $\langle \hat{\mathbf{J}}(0)\!\cdot\!\hat{\mathbf{J}}(t)\rangle_0$ is
   time-independent. The Green–Kubo integral of a constant **diverges**:
   $\sigma_{DC}\to\infty$, the perfect conductor. *That is the correct exact
   answer for a collision-free gas.* All finite resistivity is a statement
   about collisions, so the decay cannot be derived from the free gas.
2. **The classical shortcut is invalid here.** Conduction electrons in a metal
   are degenerate, $k_BT \ll E_F$, with typical speed $v_F$ — *not*
   $\sqrt{k_BT/m_e}$. The familiar classical velocity autocorrelation
   $C_{vv}(t) = \frac{k_BT}{m_e}e^{-t/\tau}$ is built on equipartition and is
   simply **not a valid microscopic description of these electrons**.

> [!warning] A retraction worth stating explicitly
> It is tempting to write the classical correlator, notice that its $k_BT$
> cancels against the $1/k_BT$ in the Green–Kubo prefactor, and conclude the
> classical form must be fine. **That inference is invalid.** A factor that
> happens to cancel in the final answer does not repair an incorrect
> intermediate object. The correlator is a physical quantity in its own right —
> it governs shot noise, current fluctuations, and the full optical response —
> and it is wrong for degenerate electrons regardless of what survives
> division. Where the cancellation *is* genuinely useful is in justifying the
> classical *Boltzmann* treatment of transport (§13.6), not in licensing a
> classical correlator for a quantum gas.

So the correlator is a genuine many-body object: Fermi-surface geometry,
occupation factors, band structure, and scattering matrix elements all enter.
The efficient way to handle it is not to write it down, but to compute the
transport coefficient from the kinetic equation that governs the distribution
function.

#### The legitimate route: linearized Boltzmann transport

> [!note] Kubo does not imply Boltzmann — they are two branches
> This is a **change of framework**, not a step inside Kubo. Kubo is a
> many-body response theory; the Boltzmann equation is a *kinetic* description
> of a distribution function, valid under additional assumptions (well-defined
> quasiparticles, weak correlations, separation of microscopic collision scales
> from macroscopic transport scales). The relationship is:
>
> ```text
> Quantum many-body theory
>        │
>        ├── Kubo linear response          (exact, given linear response)
>        │
>        └── kinetic / semiclassical limit (requires the assumptions above)
>                 ↓
>         Boltzmann equation
>                 ↓
>         relaxation-time closure
>                 ↓
>            Drude conductivity
> ```
>
> So `[DERIVATION]` below is scoped: it is a derivation *within the Boltzmann
> framework*, and that framework's own validity conditions are part of the claim.

`[DERIVATION]` **Charge convention for the rest of this subsection:** the electron
charge is $-e$ with $e>0$, so the semiclassical equation of motion is

$$\hbar\dot{\mathbf{k}} = -e\mathbf{E} \qquad\Longleftrightarrow\qquad \dot{\mathbf{k}} = -\frac{e\mathbf{E}}{\hbar}$$

Note this is a $1/\hbar$ times a **$\mathbf{k}$-gradient**. (The familiar $1/m_e$
form, $\dot{\mathbf{v}} = -e\mathbf{E}/m_e$, is equivalent but must be paired
with a **$\mathbf{v}$-gradient**; mixing the $1/m_e$ coefficient with a
$\nabla_{\mathbf{k}}$ is a units error.) Since $\mathbf{v}_{\mathbf{k}} = \frac{1}{\hbar}\nabla_{\mathbf{k}}\epsilon_{\mathbf{k}}$, the Boltzmann equation is

$$\frac{\partial f}{\partial t} - \frac{e\mathbf{E}}{\hbar}\cdot\nabla_{\mathbf{k}}f(\mathbf{k}) = \left(\frac{\partial f}{\partial t}\right)_{\text{coll}}$$

`[PHENOMENOLOGICAL]` The collision term is the **relaxation-time closure**: all
scattering — electron–phonon, electron–impurity, electron–electron — is replaced
by relaxation toward the *unperturbed* equilibrium $f_0$ with a single time
constant $\tau$ (Ch. 6 §6.7.3),

$$\left(\frac{\partial f}{\partial t}\right)_{\text{coll}} = -\frac{f - f_0}{\tau} = -\frac{\delta f}{\tau}$$

(More refined collision models relax toward a *displaced* local equilibrium
$\delta f_{eq}$ — the displaced-Dirac-distribution or shift model of hot-electron
transport. That sophistication is not needed here and is deliberately omitted
rather than half-introduced.)

Linearizing, $f = f_0 + \delta f$ with $|\delta f| \ll f_0$, and taking the
steady state $\partial_t \delta f = 0$:

$$-\frac{e\mathbf{E}}{\hbar}\cdot\nabla_{\mathbf{k}}f_0 = -\frac{\delta f}{\tau}$$

Using $\nabla_{\mathbf{k}}f_0 = \frac{\partial f_0}{\partial\epsilon_{\mathbf{k}}}\nabla_{\mathbf{k}}\epsilon_{\mathbf{k}} = \hbar\,\mathbf{v}_{\mathbf{k}}\,\frac{\partial f_0}{\partial\epsilon_{\mathbf{k}}}$:

$$\delta f(\mathbf{k}) = e\tau\,(\mathbf{E}\cdot\mathbf{v}_{\mathbf{k}})\,\frac{\partial f_0}{\partial\epsilon_{\mathbf{k}}}$$

Since $\partial f_0/\partial\epsilon_{\mathbf{k}} < 0$, this correctly *depletes*
states moving along $\mathbf{E}$ — which is the right sign for electrons, whose
drift is opposite to $\mathbf{E}$.

The current density carries the electron charge $-e$:

$$\mathbf{J} = -e\int \mathbf{v}_{\mathbf{k}}\,\delta f(\mathbf{k})\,\frac{d^3k}{(2\pi)^3} = e^2\tau\int \frac{d^3k}{(2\pi)^3}\,(\mathbf{E}\cdot\mathbf{v}_{\mathbf{k}})\left(-\frac{\partial f_0}{\partial\epsilon_{\mathbf{k}}}\right)\mathbf{v}_{\mathbf{k}}$$

Both signs are now correct and they work together: $-\partial f_0/\partial\epsilon_{\mathbf{k}} > 0$ and the angular average of $(\mathbf{E}\cdot\mathbf{v})\mathbf{v}$ is along $+\mathbf{E}$, so $\mathbf{J} \parallel +\mathbf{E}$, as Ohm's law requires.

**This is where degeneracy is handled correctly.** The Fermi–Dirac derivative
becomes a surface delta function as $T\to0$:

$$-\frac{\partial f_0}{\partial\epsilon_{\mathbf{k}}} = \frac{1}{4k_BT}\operatorname{sech}^2\!\left(\frac{\epsilon_{\mathbf{k}}-\mu}{2k_BT}\right) \;\xrightarrow[T\to0]{}\; \delta(\epsilon_{\mathbf{k}}-\mu)$$

So the current is carried by states *on the Fermi surface* — which is the actual
physical content of conduction in a degenerate metal, and something the
classical correlator cannot express at all. Performing the angular average,

$$\int \frac{d^3k}{(2\pi)^3}\,\delta(\epsilon_{\mathbf{k}}-\mu)\,v^\alpha v^\beta = \frac{n_e}{m_e}\,\delta_{\alpha\beta}$$

(Angular average gives $\int(\mathbf{E}\cdot\mathbf{v})\mathbf{v}(-\partial f_0/\partial\epsilon)\frac{d^3k}{(2\pi)^3} = \frac{\mathbf{E}}{3}\int v^2\delta(\epsilon_{\mathbf{k}}-\mu)\frac{d^3k}{(2\pi)^3}$, and the radial integral is $\int \frac{d^3k}{(2\pi)^3}\delta(\epsilon_{\mathbf{k}}-\mu)\,v^2 = \frac{3n_e}{m_e}$ using $v_F^2 = \hbar^2k_F^2/m_e^2$ and $n_e = k_F^3/3\pi^2$ — so the angular $1/3$ and the radial factor of $3$ cancel exactly.) Therefore

$$\mathbf{J} = \frac{n_e e^2\tau}{m_e}\,\mathbf{E} \quad\Longrightarrow\quad \boxed{\sigma_{DC} = \frac{n_e e^2\tau}{m_e}}$$

The $e^2$ because the current is *charge* current; $n_e$ because only states in
a shell at the Fermi surface respond; $\tau$ because it is the closure
parameter. The mean free path is $\ell = v_F\tau$, so

$$\rho = \frac{1}{\sigma} = \frac{m_e}{n_e e^2\tau} = \frac{m_e v_F}{n_e e^2\ell}$$

**Frequency dependence.** Retaining $\partial_t \delta f$ gives the Drude form

$$\sigma(\omega) = \frac{n_e e^2\tau}{m_e}\cdot\frac{1}{1 - i\omega\tau}, \qquad \sigma_0 = \frac{n_e e^2\tau}{m_e}$$

At $\omega\tau \ll 1$: purely real, Ohmic. At $\omega\tau \gg 1$: purely imaginary, reactive. The crossover at $\omega = 1/\tau \sim 10^{13}$–$10^{14}$ Hz (infrared) marks where metals transition from good reflectors to transparent.

#### The classical Drude model, and why it agrees

The 1900-era Drude model treats electrons as classical billiard balls between
collisions. It gets the same answer — and it is *not* the same argument. In that
picture one writes $\mathbf{v}(t) = \mathbf{v}(0)e^{-t/\tau}$ for a tagged
particle and uses equipartition for $\langle v^2\rangle$, which is legitimate
*for that model*. The two routes converge because at $T\to0$ the only thing
$\tau$ needs to encode is momentum relaxation, and both the classical and the
quantum descriptions deliver it.

The agreement is the reassuring part: the Drude formula is robust to the choice
of description, because the Fermi-surface $\delta$-function of the quantum
treatment and the momentum-relaxation assumption of the classical treatment
encode the same physics. What is *not* legitimate is borrowing the classical
model's equipartition correlator and presenting it as the quantum result.

> [!warning] Epistemic summary
> | Step | Status |
> |---|---|
> | Kubo relates correlator to response | `[DERIVATION]` — exact given linear response |
> | Free Fermi gas gives $\sigma\to\infty$ | `[DERIVATION]` — exact, and the reason a closure is needed |
> | Current correlator from Fermi-surface integrals | `[DERIVATION]` via linearized Boltzmann |
> | Single relaxation time $\tau$ | `[PHENOMENOLOGICAL]` — **the closure**; the only modelling input |
> | Classical $C_{vv} = \frac{k_BT}{m}e^{-t/\tau}$ | **not used** — invalid for degenerate electrons |
> | $\sigma = n_e e^2\tau/m_e$ | `[DERIVATION]` within the closure |
>
> The framework is exact, the closure is a model, and the result does not depend
> on a classical approximation that fails for the electrons in question.

### 13.4.3 — Ohm's Law as an Emergent, Not Fundamental, Law

**Why Ohm's law has an arrow of time:** The current-current correlator decays because electrons relax momentum into phonons, defects, and other environmental degrees of freedom. Careful about what this claim is: the underlying electron–phonon or electron–impurity interaction is *reversible quantum dynamics* — closed-system unitary evolution cannot produce genuine irreversibility. What produces the decaying correlator is a **coarse-graining**: tracing over the phonons and defects, averaging over ensembles, and adopting a kinetic approximation that discards the full dynamics of the environment. Within that coarse-grained description the correlator decays, and that decay is what makes $\sigma$ finite and real. Irreversibility is a feature of the effective description, not of the microscopic laws. (The mechanism is the same partial trace that produces decoherence in Ch. 10 §10.1.3 — with the important difference that here we trace over *bath* degrees of freedom, not a measuring apparatus.)

**In an ideal translationally invariant system at $T = 0$:** With no momentum-relaxing mechanism, the current correlation function has a non-decaying component, so $\tau\to\infty$ and $\sigma_{DC}\to\infty$. Note precisely what this does and does not say: it means the DC conductivity contains a **persistent (Drude) contribution** — the system sustains a current against arbitrarily small dissipation. It does *not* mean a current spontaneously appears in the absence of an applied field. There is still no current unless something drives one; what is unbounded is the *response* to a drive, and the absence of resistivity. A finite resistivity requires momentum relaxation, whether from scattering, from boundaries, or from an explicit momentum sink.

This should also not be identified with superconductivity. A clean normal metal with exactly conserved momentum has infinite Drude weight while remaining an ordinary metal: $\omega_p \neq 0$, no gap, no phase-coherent supercurrent. Superconductivity is a distinct phenomenon — it adds a many-body state (Cooper pairing, energy gap, phase rigidity) on top of the electrons. Infinite Drude weight and superconductivity are related but not equivalent.

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

The *number* is universal; the *law* is not unconditional. $L_0$ is a **low-temperature Fermi-liquid** result, valid in the degenerate limit where electronic quasiparticle transport dominates.

`[APPROXIMATION]` **The universality of $L_0$ is a statement about a scattering model, not about metals.** The ratio is constant precisely because the *same* $\tau$ cancels between $\sigma$ and $\kappa$ — which requires elastic scattering off a static bath, Galilean-invariant parabolic dispersion, and heat carried by electrons alone. Whenever heat and charge relax by *different* mechanisms, the ratio drifts:

| Regime | What happens to $\kappa/\sigma T$ |
|---|---|
| Elastic scattering, low $T$ | approaches $L_0$ |
| Electron–phonon scattering, high $T$ | $\tau_Q \neq \tau_N$ — ratio below $L_0$ |
| Momentum-conserving electron–electron scattering | relaxes heat but not charge — ratio below $L_0$; a key diagnostic of strange metals |
| Transition metals, strong spin–orbit | $s$-wave scattering suppressed — ratio above $L_0$ |
| Strongly correlated (heavy fermions, cuprates) | quasiparticle picture fails — no constant ratio |
| High $T$ (classical regime) | degenerate-gas assumption breaks; equipartition applies instead |

So "a constant depending only on fundamental constants, independent of material" accurately describes the *low-temperature Fermi-liquid limit* and is false in general — including in exactly the materials where the interesting physics lives. Reading the deviations diagnostically is more useful than treating $L_0$ as a law: the size and sign of the departure identifies which additional relaxation channel is active.

This is a good illustration of the book's method. The *universal number* is `[DERIVATION]`; the *scope of validity* is `[APPROXIMATION]`; and the failure cases are where the new physics becomes visible.

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

> [!note] When the classical correlator *is* legitimate — and when it is not
> The velocity autocorrelation $C_{vv}(t) = \frac{k_BT}{m}e^{-t/\tau}$ used above
> is **legitimate here**, because a Brownian tracer in a classical thermal medium
> is non-degenerate: $v_{th} = \sqrt{k_BT/m}$ really is the relevant speed, and
> equipartition really does apply.
>
> The same expression is **not** legitimate for conduction electrons in a metal,
> which are degenerate with $v \sim v_F$. That is why §13.4.2 does not use it —
> it derives the Drude result from the Fermi-surface $\delta$-function instead.
> The contrast is worth keeping straight: the two cases share a formula but not
> its justification, and transferring the classical result to degenerate electrons
> without re-examining the correlator is a common and consequential error.

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

### 13.11.1 — Ballistic Transport and the Limits of the Bulk Formulation

Kubo linear response is **not** restricted to diffusive transport — it is the
general framework. What is restricted is the *bulk conductivity* formulation
used in §13.4, in which a local constitutive law $\mathbf{J} = \sigma\mathbf{E}$
with a single material constant is assumed to be meaningful. That assumption
requires the sample to be large compared with the mean free path, so that
scattering is frequent and a local $\sigma$ exists:

```text
Linear response
      │
      ├── bulk / diffusive  (L ≫ ℓ)  → Kubo conductivity, local σ
      │
      └── open ballistic mesoscopic (L ≲ ℓ) → Landauer / scattering, mode-resolved
```

For $L \lesssim \ell_{mfp}$, an electron crosses the device without scattering,
so no local bulk conductivity is defined. The Drude estimate then *overestimates*
the resistance, because it assumes a scattering probability that the geometry
never gives the electron the chance to take. The right object is then the
transmission of individual modes, not a material constant.

For a **ballistic conductor** (negligible scattering inside the channel), each
transverse mode contributes a conductance:

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

In the integer quantum Hall effect (Ch. 7 §7.3), the fundamental statement is
about a **conductivity**, not a conductance:

$$\boxed{\sigma_{xy} = \nu\frac{e^2}{h}}$$

the quantized **Hall conductivity**, with $\nu$ the number of filled Landau levels
and the longitudinal conductivity vanishing ($\sigma_{xx} = 0$) on the plateau.

The microscopic content, from Kubo applied to the full 2D system, is the
Chern-number integral over the Brillouin zone:

$$\sigma_{xy} = \frac{e^2}{h}\sum_{n\in\text{filled}}\frac{1}{2\pi}\iint_{\text{BZ}}\Omega_n(\mathbf{k})\,d^2k = \nu\frac{e^2}{h}$$

where $\Omega_n$ is the Berry curvature of band $n$. This is the TKNN result
(Ch. 7 §7.2.1) seen from the transport-theory side: the Kubo integral *counts
Chern number*, which is why the value is topologically protected and
independent of disorder, carrier density, and sample geometry.

> [!note] Conductivity vs. conductance — a distinction worth keeping
> $\sigma_{xy}$ and $G$ are different quantities, and identifying them is a
> common shortcut. $\sigma_{xy}$ is an intrinsic **material/response** property
> (conductivity, S), whereas $G$ is a **device** property (conductance, S) that
> depends on geometry and contacts.
>
> In a suitable ideal Hall-bar geometry with well-separated edge channels and
> equilibrating contacts, the two-terminal conductance of the same sample also
> takes the quantized value $G = \nu e^2/h$, because the contact resistance is
> negligible and $\sigma_{xx}=0$ forces the current to be carried entirely by the
> edges. That is a *consequence* of the conductivity quantization plus the
> geometry, not the primary statement — and in a two-terminal device without
> equilibrating contacts the Hall voltage and the two-terminal conductance are
> in general *not* quantized, because of contact and fringe effects.
>
> For this book's purposes the clean formulation is: the Hall **conductivity**
> is quantized; suitable geometries then exhibit the corresponding quantized
> conductance.

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
|Topology|$T_n = 1$ protected|$\sigma_{xy} = \nu e^2/h$ (QHE); $G$ quantized in ideal Hall-bar geometry|

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
|QHE $\sigma_{xy} = \nu e^2/h$|Primary resistance standard; metrological applications (Hall-bar geometry)|

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