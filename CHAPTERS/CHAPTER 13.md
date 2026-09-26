# Bridge B.e — The Kubo Formula and the Generalized Transport Law

### Five Transport Laws from One Quantum Mechanical Calculation

---

> _The Green-Kubo relations are among the most profound results in statistical mechanics._ _They say that the dissipation of a system driven out of equilibrium_ _is completely determined by the spontaneous fluctuations of the same system at equilibrium._ — David Chandler, _Introduction to Modern Statistical Mechanics_

---

## 13.0 — Bridge B.e and the Convergence Chapter

This is the final Bridge B path — and the most important chapter in the book for making it discipline-agnostic.

**The claim of Chapter 1** was that every engineering branch shares one mathematical template at Layer 2:

$$\text{flux} = -L \cdot \nabla\phi$$

The claim was that Ohm's law, Fourier's law, Fick's law, Newton's law of viscosity, and Hooke's law are the same formula with different labels.

**This chapter delivers the proof.** All five transport coefficients ($\sigma$, $\kappa$, $D$, $\eta$, $C$) are derived from one formula — the **Green-Kubo relation** — applied to five different current operators. The only thing that changes is which physical current you put in.

**Bridge B.e is also the bridge that injects irreversibility.** Chapters 9 and 11 (classical mechanics and Maxwell's equations) are time-reversible: run them backward and you get equally valid physics. Ohm's law is not time-reversible — current flows from high to low potential, not randomly. The irreversibility comes from this chapter: quantum scattering and decoherence, averaged over an equilibrium ensemble, produce a finite relaxation time and a finite, dissipative conductivity.

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

$$\hat H(t) = \hat H_0 - \hat A,F(t)$$

where $\hat A$ is a quantum observable (the operator that couples to the perturbation) and $F(t)$ is the classical driving force (an electric field, temperature gradient, pressure difference, etc.).

**Examples of coupling:**

- Electric field: $\hat A = -e\hat{\mathbf{r}}$ (dipole coupling), $F = \mathbf{E}(t)$
- Temperature gradient: $\hat A = \hat H_0$ (energy), $F = \nabla T / T^2$
- Chemical potential gradient: $\hat A = \hat N$ (particle number), $F = -\nabla\mu/T$

### 13.1.2 — The Linear Response

To first order in $F$, the expectation value of a second observable $\hat B$:

$$\langle\hat B(t)\rangle = \langle\hat B\rangle_0 + \int_{-\infty}^t \chi_{BA}(t-t'),F(t'),dt'$$

where $\chi_{BA}$ is the **retarded Green's function** (generalized susceptibility):

$$\boxed{\chi_{BA}(t-t') = \frac{i}{\hbar}\Theta(t-t')\langle[\hat B(t), \hat A(t')]\rangle_0}$$

$\Theta$ is the Heaviside step function (enforcing **causality**: response cannot precede the perturbation). The commutator $[\hat B, \hat A]$ is computed in the Heisenberg picture with respect to $\hat H_0$, and $\langle\cdot\rangle_0$ is the equilibrium average.

In frequency space (Fourier transform):

$$\langle\hat B(\omega)\rangle = \tilde\chi_{BA}(\omega),F(\omega)$$

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

**3. The formula is exact.** No approximations have been made beyond the linear response assumption (weak perturbation). It is valid for any quantum system, any temperature, any material.

---

## 13.3 — The Fluctuation-Dissipation Theorem

### 13.3.1 — Statement

The imaginary part of the susceptibility (which governs energy absorption from a periodic perturbation) is directly related to the spectral density of equilibrium fluctuations:

$$\boxed{\text{Im}[\tilde\chi_{AA}(\omega)] = \frac{\omega}{2k_BT}S_A(\omega)}$$

where the **spectral density** (power spectrum of fluctuations):

$$S_A(\omega) = \int_{-\infty}^{\infty}\langle\hat A(0)\hat A(t)\rangle_0,e^{i\omega t},dt$$

**Physical interpretation:** The rate at which the system absorbs energy from an external drive at frequency $\omega$ is exactly determined by how strongly the system spontaneously fluctuates at the same frequency at equilibrium. Noise and dissipation are the same phenomenon.

### 13.3.2 — Johnson-Nyquist Noise

Applied to a resistor $R$ at temperature $T$:

$$S_V(\omega) = 4k_BT,\text{Re}[Z(\omega)] \xrightarrow{\omega\to 0} 4k_BTR$$

The **open-circuit voltage noise** of a resistor: $\langle V^2\rangle = 4k_BTR\Delta f$ in bandwidth $\Delta f$.

For $R = 1,\text{M}\Omega$ at $T = 300$ K in $B = 10$ kHz: $V_{rms} = \sqrt{4k_BTR\Delta f} = \sqrt{4\times 1.38\times 10^{-23}\times 300\times 10^6\times 10^4} = 12.9;\mu$V

This is the **floor on voltage measurement** — regardless of amplifier quality, the resistor itself generates this noise. It sets the sensitivity limit of every resistive sensor, every voltmeter, every impedance measurement.

### 13.3.3 — Shot Noise

When current is carried by discrete particles (electrons tunneling one at a time), the current fluctuations follow Poisson statistics:

$$S_I = 2eI \qquad\text{(full shot noise)}$$

The **Fano factor** $F = S_I/2eI$ measures the deviation from Poissonian statistics. $F = 1$: independent tunnel events. $F < 1$: sub-Poissonian (fermion antibunching; Pauli exclusion supresses fluctuations). $F > 1$: super-Poissonian (bunching; correlated transport).

**Engineering:** Shot noise limits the SNR of photodetectors and PIN diodes. The Fano factor is used to characterize quantum transport regimes — a direct measurement of whether transport is diffusive ($F = 1/3$ for 1D diffusive wire), ballistic ($F = 0$), or correlated.

---

## 13.4 — Deriving Ohm's Law

### 13.4.1 — The Kubo Conductivity

The electrical conductivity tensor:

$$\sigma_{\alpha\beta}(\omega) = \frac{1}{V}\int_0^\infty dt,e^{i\omega t}\int_0^\beta d\lambda,\langle\hat J_\alpha(-i\hbar\lambda)\hat J_\beta(t)\rangle_0$$

where $\hat{\mathbf{J}}$ is the charge current density operator:

$$\hat{\mathbf{J}} = \frac{e\hbar}{m}\sum_k\mathbf{k},\hat c_k^\dagger\hat c_k$$

summing over all occupied single-particle states.

For an isotropic system in the DC limit ($\omega\to 0$):

$$\sigma_{DC} = \frac{1}{3Vk_BT}\int_0^\infty\langle\hat{\mathbf{J}}(0)\cdot\hat{\mathbf{J}}(t)\rangle_0,dt$$

### 13.4.2 — The Drude Result from Kubo

In a metal with an effective relaxation time $\tau$ (from electron-phonon or electron-impurity scattering, Ch. 6 §6.7.3), the current-current correlator decays exponentially:

$$\langle\hat J_\alpha(0)\hat J_\beta(t)\rangle_0 = \frac{n_e^2k_BT}{m}\delta_{\alpha\beta},e^{-t/\tau}$$

(The prefactor follows from the equipartition theorem for the current in a free electron gas, Ch. 10 §10.7.2.)

Substituting into the Kubo formula:

$$\sigma_{DC} = \frac{1}{3Vk_BT}\cdot\frac{Vn_e^2k_BT}{m}\int_0^\infty e^{-t/\tau}dt = \frac{n_e^2\tau}{m}\cdot\frac{1}{3}\times 3 = \frac{n_e^2\tau}{m_e}$$

$$\boxed{\sigma_{DC} = \frac{n_e e^2\tau}{m_e}}$$

This is the **Drude formula** — derived from quantum mechanics via the Kubo formula, not from a classical billiard-ball model. The mean free path is $\ell = v_F\tau$, and the resistivity:

$$\rho = \frac{1}{\sigma} = \frac{m_e}{n_e e^2\tau} = \frac{m_e v_F}{n_e e^2\ell}$$

**Frequency-dependent conductivity** (from the full Kubo formula):

$$\sigma(\omega) = \frac{\sigma_0}{1 - i\omega\tau}, \qquad \sigma_0 = \frac{n_ee^2\tau}{m_e}$$

At $\omega\tau \ll 1$: purely real, Ohmic. At $\omega\tau \gg 1$: purely imaginary, reactive. The crossover at $\omega = 1/\tau \sim 10^{13}$–$10^{14}$ Hz (infrared) marks where metals transition from good reflectors to transparent.

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

$$\kappa_{\alpha\beta} = \frac{1}{Vk_BT^2}\int_0^\infty\langle\hat J_Q^\alpha(0)\hat J_Q^\beta(t)\rangle_0,dt$$

### 13.5.2 — The Result and the Wiedemann-Franz Law

For metals (electronic heat conduction dominates), the same relaxation time $\tau$ governs both charge and heat transport. Taking the ratio:

$$\frac{\kappa}{\sigma T} = \frac{\pi^2}{3}\left(\frac{k_B}{e}\right)^2 = L_0 = 2.44\times 10^{-8};\text{W}\cdot\Omega\cdot\text{K}^{-2}$$

This is the **Wiedemann-Franz law** with the **Lorenz number** $L_0$ — a universal constant depending only on fundamental constants, independent of the material. It holds for all metals in the diffusive regime and is confirmed to $\sim 10%$ across metals from $-200°$C to $+600°$C.

**Physical origin:** Both charge and heat are carried by electrons near the Fermi level. The energy $E_F$ per electron is the same whether you are measuring electrical or thermal transport. The factor $k_B^2/e^2$ converts energy² (thermal) to energy/charge (electrical) squared.

**Engineering consequence:** Wiedemann-Franz allows you to estimate thermal conductivity of a metal from its electrical resistivity (easier to measure): $\kappa = L_0\sigma T$. For copper at 300 K: $\sigma = 6\times 10^7$ S/m → $\kappa = 2.44\times 10^{-8}\times 6\times 10^7\times 300 = 439$ W/m·K (measured: 401 W/m·K — 10% error from non-Drude effects).

### 13.5.3 — Phonon Thermal Conductivity

For insulators and semiconductors (no free electrons), heat is carried by phonons. The Green-Kubo formula:

$$\kappa = \frac{1}{Vk_BT^2}\int_0^\infty\langle\hat{\mathbf{J}}_Q^{ph}(0)\cdot\hat{\mathbf{J}}_Q^{ph}(t)\rangle_0,dt$$

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

$$D = \frac{1}{3}\int_0^\infty\langle\mathbf{v}(0)\cdot\mathbf{v}(t)\rangle_0,dt$$

For a particle undergoing Brownian-like motion with momentum relaxation time $\tau$: $\langle v_\alpha(0)v_\alpha(t)\rangle = \frac{k_BT}{m}e^{-t/\tau}$

$$D = \frac{1}{3}\cdot 3\cdot\frac{k_BT}{m}\tau = \frac{k_BT\tau}{m} = \frac{k_BT}{m}\cdot\frac{\ell}{v_{th}}$$

where $\ell$ is the mean free path and $v_{th} = \sqrt{k_BT/m}$ is the thermal velocity.

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

$$\eta = \frac{V}{k_BT}\int_0^\infty\langle\hat\sigma_{xy}(0)\hat\sigma_{xy}(t)\rangle_0,dt$$

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

$$C_{ijkl} = \frac{V}{k_BT}\int_0^\infty\langle\hat\sigma_{ij}(0)\hat\sigma_{kl}(t)\rangle_0,dt\bigg|_{t\to 0}$$

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

$$\tilde C(\omega) = \frac{V}{k_BT}\int_0^\infty\langle\hat\sigma_{xy}(0)\hat\sigma_{xy}(t)\rangle_0,e^{i\omega t},dt$$

At $\omega\to 0$: recovers the static elastic modulus (material responds slowly and fully). At $\omega\to\infty$: recovers the unrelaxed (glassy) modulus (material doesn't have time to rearrange). At intermediate $\omega$: complex modulus $C' + iC''$ — energy storage and loss.

---

## 13.9 — The Onsager Matrix: All Transport Unified

### 13.9.1 — Coupled Transport

When multiple driving forces act simultaneously, the currents become coupled. Define thermodynamic forces:

$$\mathbf{X}_E = \mathbf{E} - \frac{\nabla\mu}{e}, \quad \mathbf{X}_Q = -\frac{\nabla T}{T}$$

The Onsager transport equations:

$$\begin{pmatrix}\mathbf{J}^e \ \mathbf{J}^Q\end{pmatrix} = \begin{pmatrix}L_{EE} & L_{EQ} \ L_{QE} & L_{QQ}\end{pmatrix}\begin{pmatrix}\mathbf{X}_E \ \mathbf{X}_Q\end{pmatrix}$$

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

For a free electron gas: $S = -\frac{\pi^2k_B^2T}{3eE_F}$ (Mott formula) At 300 K for copper ($E_F = 7$ eV): $S \approx -1.8;\mu$V/K (measured: $-1.8;\mu$V/K) ✓

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

All five transport laws, now with their Kubo derivations:

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

**The quantum of conductance** $G_0 = 2e^2/h \approx 7.75\times 10^{-5}$ S $= 1/(12.9;\text{k}\Omega)$: the conductance of a single perfectly transmitting channel. First measured directly in quantum point contacts (1988).

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

$$\sigma_{xy} = \frac{e^2}{h}\sum_{n\in\text{filled}}\frac{1}{2\pi}\iint_{\text{BZ}}\Omega_n(\mathbf{k}),d^2k = \nu\frac{e^2}{h}$$

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