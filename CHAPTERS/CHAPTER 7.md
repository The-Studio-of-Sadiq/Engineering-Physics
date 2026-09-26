# Topology, Quantum Hall Effect, and Superconductivity

### When Band Theory Becomes Topological

---

> _It is remarkable that the Hall conductance is quantized even in the presence_ _of impurities and disorder. The reason is topology._ — David Thouless, Nobel Lecture, 2016

---

## 7.0 — The Question This Chapter Answers

Chapter 6 built band theory — the quantum mechanics of electrons in periodic potentials. It explained conductors, semiconductors, and insulators. It gave you the tools to design transistors and solar cells.

But band theory as presented in Ch. 6 misses something profound. Two insulators can have identical band gaps, identical carrier concentrations, and completely identical local physics — and yet be fundamentally different. They cannot be continuously deformed into each other without closing the gap, passing through a metallic state.

The difference is **topology** — a global property of the band structure that cannot be detected by looking at any single $\mathbf{k}$-point, only by integrating a geometric quantity over the entire Brillouin zone.

This chapter develops the topological perspective on bands and shows that:

1. The integer quantum Hall conductance is quantized because it equals a topological integer (the Chern number) — immune to any disorder or imperfection
2. Topological insulators have surface states protected by symmetry — they cannot be removed without breaking that symmetry or closing the bulk gap
3. Weyl semimetals host quasiparticles that behave exactly as the Weyl fermions in the Standard Model Lagrangian (Ch. 0) — topology has brought particle physics into a material you can hold in your hand
4. Superconductivity is broken U(1) symmetry — the same mathematical template as the Higgs mechanism (Ch. 0 §0.7), now at millielectronvolt energies

The topology thread promised in Ch. 0 §0.9 is collected here.

---

## 7.1 — Berry Phase: Geometry Hidden in Quantum Mechanics

### 7.1.1 — The Adiabatic Theorem

Consider a quantum system with a Hamiltonian $\hat H(\mathbf{R})$ that depends on a set of slowly-varying external parameters $\mathbf{R}(t)$ — which could be a slowly-rotating magnetic field, or the crystal momentum $\mathbf{k}$ varying as an electron moves through the Brillouin zone.

**Adiabatic theorem (Born-Fock, 1928):** If the system starts in eigenstate $|n(\mathbf{R}(0))\rangle$ and the parameters change slowly (adiabatically), the system remains in the instantaneous eigenstate $|n(\mathbf{R}(t))\rangle$ — it tracks the eigenstate as $\mathbf{R}$ evolves.

The state acquires two phases:

$$|\psi(t)\rangle = e^{i\gamma_n(t)},e^{-\frac{i}{\hbar}\int_0^t E_n(t')dt'},|n(\mathbf{R}(t))\rangle$$

- The second exponential: the familiar **dynamical phase** $-\int E_n,dt/\hbar$
- The first exponential: a **geometric phase** $\gamma_n(t)$ discovered by Berry in 1984 — it depends only on the geometry of the path in parameter space, not on how fast you traverse it

### 7.1.2 — The Berry Connection and Berry Phase

Substituting into the Schrödinger equation and solving for $\gamma_n$:

$$\gamma_n = i\int_{\mathbf{R}(0)}^{\mathbf{R}(t)}\langle n(\mathbf{R})|\nabla_\mathbf{R}|n(\mathbf{R})\rangle\cdot d\mathbf{R}$$

Define the **Berry connection** (vector potential in parameter space):

$$\mathbf{A}_n(\mathbf{R}) = i\langle n(\mathbf{R})|\nabla_\mathbf{R}|n(\mathbf{R})\rangle$$

For a **closed loop** $\mathcal{C}$ in parameter space (returning to the starting point), the Berry phase is:

$$\boxed{\gamma_n = \oint_\mathcal{C}\mathbf{A}_n(\mathbf{R})\cdot d\mathbf{R}}$$

This is gauge-dependent (like any vector potential) — but for a closed loop, the gauge-invariant **Berry curvature** gives a gauge-independent result. By Stokes' theorem:

$$\gamma_n = \iint_\mathcal{S}\boldsymbol{\Omega}_n(\mathbf{R})\cdot d\mathbf{S}$$

where the **Berry curvature** is:

$$\boldsymbol{\Omega}_n(\mathbf{R}) = \nabla_\mathbf{R}\times\mathbf{A}_n = i\langle\nabla_\mathbf{R} n|\times|\nabla_\mathbf{R} n\rangle$$

**The Berry curvature is the "magnetic field" in parameter space** — just as $\mathbf{B} = \nabla\times\mathbf{A}$ in real space. The Berry phase accumulated around a loop is the "flux" of $\boldsymbol{\Omega}$ through the surface bounded by that loop.

### 7.1.3 — The Chern Number: Topology from Integration

For electrons in a crystal, the natural parameter space is the Brillouin zone (BZ) — a torus (periodic in all directions of $\mathbf{k}$-space). The Berry curvature for the $n$-th band is:

$$\Omega_n(\mathbf{k}) = i\sum_{m\neq n}\frac{\langle u_{n\mathbf{k}}|\partial_{k_x}\hat H|u_{m\mathbf{k}}\rangle\langle u_{m\mathbf{k}}|\partial_{k_y}\hat H|u_{n\mathbf{k}}\rangle - (x\leftrightarrow y)}{(E_n - E_m)^2}$$

The **Chern number** (first Chern number) of the $n$-th band:

$$\boxed{C_n = \frac{1}{2\pi}\iint_{\text{BZ}}\Omega_n(\mathbf{k}),d^2k \in \mathbb{Z}}$$

**This is always an integer.** It cannot take fractional values. It cannot change continuously. It can only change by jumping to another integer — which requires closing the band gap (making $E_n = E_m$ somewhere, making $\Omega_n$ singular).

The reason it is an integer is the Chern-Gauss-Bonnet theorem from differential geometry: the integral of a curvature over a closed surface is $4\pi$ times the Euler characteristic, which for a torus equals zero — but for a band over the BZ torus, the Chern number counts how many times the eigenvector $|u_{n\mathbf{k}}\rangle$ "wraps" around the BZ, and wrapping numbers are always integers.

**This is the same mathematics that makes flux quantization an integer:** the winding number of the superconducting phase around a loop (§7.8) is an integer for the same reason.

---

## 7.2 — Anomalous Velocity: How Topology Produces a Hall Effect

### 7.2.1 — The Semiclassical Equations of Motion, Corrected

The standard semiclassical equations of motion for a Bloch electron:

$$\dot{\mathbf{r}} = \frac{1}{\hbar}\frac{\partial E_n}{\partial\mathbf{k}}, \qquad \hbar\dot{\mathbf{k}} = -e\mathbf{E} - e\dot{\mathbf{r}}\times\mathbf{B}$$

are incomplete. Including the Berry curvature correction (derivable from the Schrödinger equation itself):

$$\dot{\mathbf{r}} = \frac{1}{\hbar}\frac{\partial E_n}{\partial\mathbf{k}} - \frac{e}{\hbar}\mathbf{E}\times\boldsymbol{\Omega}_n(\mathbf{k})$$

The second term is the **anomalous velocity** — it is **transverse** to the applied electric field $\mathbf{E}$. It produces a current perpendicular to the field without any magnetic field:

$$\mathbf{J}_{anomalous} = \frac{e^2}{\hbar}\sum_{n,\in,\text{filled}}\int\frac{d^2k}{(2\pi)^2}\boldsymbol{\Omega}_n(\mathbf{k})\times\mathbf{E}$$

The Hall conductivity:

$$\sigma_{xy} = \frac{e^2}{\hbar}\sum_{n,\in,\text{filled}}\frac{1}{2\pi}\iint_{\text{BZ}}\Omega_n,d^2k = \frac{e^2}{h}\sum_n C_n$$

**The Hall conductivity equals the sum of Chern numbers of all filled bands, in units of $e^2/h$.** This is the TKNN formula (Thouless, Kohmoto, Nightingale, den Nijs, 1982) — one of the deepest results in condensed matter physics.

---

## 7.3 — The Integer Quantum Hall Effect

### 7.3.1 — The Setup

A 2D electron gas (2DEG) — electrons confined to a plane (a GaAs/AlGaAs heterostructure, for example) — in a strong perpendicular magnetic field $B \sim 1$–$30$ T at temperatures $T \sim 1$–$4$ K.

**Landau levels** (from Ch. 6): the 2D kinetic energy in a magnetic field is quantized into discrete levels:

$$E_n = \hbar\omega_c\left(n + \frac{1}{2}\right), \quad \omega_c = \frac{eB}{m^*}$$

Each Landau level has a macroscopic degeneracy: $$N_{LL} = \frac{eB}{h}\times(\text{area}) = \frac{\Phi}{\Phi_0}$$

where $\Phi$ is the total magnetic flux and $\Phi_0 = h/e$ is the (single-particle) flux quantum. The degeneracy equals the number of flux quanta threading the sample.

### 7.3.2 — Integer Hall Conductance

When exactly $\nu$ Landau levels are filled (filling factor $\nu = nh/eB$ where $n$ is the electron density):

$$\sigma_{xy} = \nu\frac{e^2}{h}, \quad \sigma_{xx} = 0$$

**The measurements** (von Klitzing, 1980):

- $\sigma_{xy}$ is quantized to 1 part in $10^9$ — regardless of sample imperfections, impurities, or edge geometry
- $\sigma_{xx} = 0$ simultaneously — no energy dissipation at plateaus

The resistance standard: $R_K = h/e^2 \approx 25812.807,\Omega$ is now exact by SI definition (2019).

### 7.3.3 — Why Topology Protects It

The TKNN result §7.2 says $\sigma_{xy} = (e^2/h)\sum_n C_n$. The Chern number is:

1. **Quantized by mathematics** (always an integer)
2. **Robust against perturbations** — adding disorder, impurities, or changing sample shape does not change $C_n$ as long as the gap remains open
3. **Changed only by a phase transition** — closing and reopening the gap

This is why a "fractional" Hall conductance never arises in integer QHE: integers cannot be fractional. Disorder smears the Landau levels into bands but does not change the Chern numbers.

### 7.3.4 — Edge States: The Bulk-Edge Correspondence

A topologically non-trivial insulator (filled Landau levels) in contact with vacuum (topologically trivial, Chern number 0) must have conducting states at the boundary. The gap must close at some point as you go from bulk to vacuum — and it closes by having electronic states that cross the Fermi level.

**Bulk-edge correspondence:** Number of chiral edge channels = $|C_{total}|$.

For $\nu$ filled Landau levels: $\nu$ chiral edge channels, each carrying current $e^2/h \times V$ in the same direction. These channels are:

- **Chiral**: electrons move in one direction only (set by $\mathbf{B}$)
- **Backscattering-free**: an electron moving right cannot scatter to move left without crossing the bulk (there is no left-mover at the same edge)

**The quantization is protected by chirality.** No amount of disorder can cause backscattering in a chiral edge channel — there are no backward states to scatter into. This is the physical reason for the extraordinary precision of the QH plateau.

---

## 7.4 — Topological Insulators

### 7.4.1 — Time-Reversal Symmetry and the Z₂ Invariant

The QHE requires a magnetic field — time-reversal symmetry ($\mathcal{T}$) is broken. A different class of topological phases exists in systems with **preserved** time-reversal symmetry, characterized by a $\mathbb{Z}_2$ topological invariant $\nu_0 \in {0, 1}$ (not a Chern number).

Time-reversal for spin-1/2 systems: $\hat{\mathcal{T}}^2 = -1$.

The Kramers theorem: for $\hat{\mathcal{T}}^2 = -1$, every eigenstate is at least doubly degenerate. At high-symmetry $\mathbf{k}$-points in the BZ (where $\mathbf{k} \equiv -\mathbf{k}$, called time-reversal invariant momenta TRIM), these Kramers pairs are pinned at the same energy.

**The Z₂ invariant** counts the parity of the number of times the surface band crosses the Fermi energy between two TRIM points. Informally:

$$(-1)^{\nu_0} = \prod_{\text{TRIM}},\xi_{2m}(\Gamma_i)$$

where $\xi_{2m}$ are parity eigenvalues of occupied bands at TRIM points.

- $\nu_0 = 0$: topologically trivial (ordinary insulator)
- $\nu_0 = 1$: topological insulator (non-trivial)

### 7.4.2 — 2D Topological Insulator: Quantum Spin Hall Effect

**HgTe/CdTe quantum wells** (König et al., 2007): HgTe has inverted band order (the $\Gamma_8$ light-hole band is above the $\Gamma_6$ conduction band) while CdTe is normal. At a critical well thickness, band inversion occurs — the $Z_2$ invariant changes from 0 to 1.

Result: **helical edge states** with **spin-momentum locking**:

- Spin-up electrons move right
- Spin-down electrons move left
- These are time-reversal partners (Kramers pair)

**Why they cannot backscatter:** Backscattering would require spin-up (moving right) to become spin-down (moving left). Time reversal takes $\uparrow$right to $\downarrow$left. Since $\hat{\mathcal{T}}^2 = -1$, the backscattering matrix element $\langle\downarrow\text{left}|\hat V|\uparrow\text{right}\rangle$ satisfies:

$$\langle\downarrow\text{left}|\hat V|\uparrow\text{right}\rangle = -\langle\downarrow\text{left}|\hat V|\uparrow\text{right}\rangle = 0$$

**Any time-reversal invariant impurity produces exactly zero backscattering.** A magnetic impurity (which breaks $\mathcal{T}$) can gap the edge states — a feature used in quantum anomalous Hall devices.

### 7.4.3 — 3D Topological Insulators

**Materials:** Bi₂Se₃, Bi₂Te₃, Bi₂Sb₃Te₃ (and alloys).

These have strong spin-orbit coupling (from heavy Bi, Se, Te atoms) that inverts the band structure at the $\Gamma$-point. The result: $\nu_0 = 1$.

**Surface states:** A topological insulator with $\nu_0 = 1$ has a Dirac cone on every surface — a single cone (odd number — this is what $\nu_0 = 1$ means). The Hamiltonian near the cone:

$$H_{surface}(\mathbf{k}) = \hbar v_F(\hat z\times\boldsymbol{\sigma})\cdot\mathbf{k}$$

The spin is locked perpendicular to $\mathbf{k}$ (helical spin texture). ARPES (angle-resolved photoemission spectroscopy) directly images this cone and spin texture — it is one of the clearest demonstrations that a quantum-mechanical prediction is correct.

**Key properties:**

- Bulk is insulating: $E_g \approx 0.3$ eV for Bi₂Se₃
- Surface is metallic: single Dirac cone with $v_F \approx 5\times 10^5$ m/s
- Surface conductance is topologically protected: cannot be gapped by any non-magnetic surface perturbation (contamination, reconstruction, gentle disorder)

### 7.4.4 — The Axion Connection to Chapter 0

The effective electromagnetic action of a 3D TI contains a topological term:

$$S_\theta = \frac{\theta e^2}{2\pi h}\int d^3r,dt;\mathbf{E}\cdot\mathbf{B}$$

For a trivial insulator: $\theta = 0$. For a strong TI: $\theta = \pi$.

This is **exactly the form of the QCD θ-term** from Ch. 0 §0.9: $\theta\frac{g^2}{32\pi^2}G_{\mu\nu}\tilde G^{\mu\nu}$, with EM fields replacing gluon fields. The parameter $\theta$ that was a mystery in QCD (why is $|\theta_{QCD}| < 10^{-10}$?) appears in condensed matter with $\theta = \pi$ — a different value, but the same physics.

The Peccei-Quinn mechanism (Ch. 0) promotes $\theta$ to a dynamical field — the **axion**. Proposed axion dark matter could be detected by its coupling $\mathbf{E}\cdot\mathbf{B}$ — using topological insulator heterostructures as detectors. **This is a direct link from the f(φ) placeholder of Ch. 0 to a table-top condensed matter experiment.**

---

## 7.5 — Weyl Semimetals

### 7.5.1 — Weyl Nodes in the Brillouin Zone

A Weyl semimetal has pairs of band-touching points (Weyl nodes) in the Brillouin zone where the Hamiltonian near each node takes the form:

$$H_{Weyl}(\mathbf{q}) = \pm\hbar v_F\boldsymbol{\sigma}\cdot\mathbf{q}$$

where $\mathbf{q} = \mathbf{k} - \mathbf{k}_{Weyl}$ is measured from the node. This is the **Weyl equation** — the equation for a massless relativistic fermion of definite chirality from Ch. 0. The $+/-$ sign is the chirality.

**The condensed matter Weyl fermion is not an analogy** — the mathematical structure $H = \hbar v_F\boldsymbol{\sigma}\cdot\mathbf{k}$ is identical to the Weyl spinor in $\mathcal{L}_{SM}$, with $v_F$ replacing $c$. A Weyl semimetal is a material in which Standard Model Lagrangian physics emerges at low energies.

### 7.5.2 — Topological Protection and Berry Monopoles

The Berry curvature of a Weyl node:

$$\boldsymbol{\Omega}_+(\mathbf{q}) = \frac{\mathbf{q}}{2|\mathbf{q}|^3} \quad\text{(for chirality +1)}$$

This is the field of a magnetic monopole at $\mathbf{q} = 0$ in $\mathbf{k}$-space, with strength (Chern number) $C = +1$. The opposite-chirality node has $C = -1$.

**Why Weyl nodes are robust:** A single Weyl node cannot be removed by any perturbation — it is a monopole in Berry curvature, and monopoles cannot be continuously annihilated. Two nodes of opposite chirality can annihilate (same as a magnetic monopole and antimonopole meeting). This is why Weyl nodes come in pairs and can only disappear by merging in $\mathbf{k}$-space.

**Nielsen-Ninomiya theorem:** Any lattice regularization of a theory with Weyl fermions must have equal numbers of left- and right-handed Weyl nodes. This is a lattice version of the anomaly cancellation condition in Ch. 0 §0.10.

### 7.5.3 — Fermi Arcs: Open Surface Fermi Surfaces

Between Weyl nodes of opposite chirality projected onto the surface BZ, there are **Fermi arc surface states** — open arcs of Fermi surface connecting the projected positions of the two nodes.

This is forbidden in ordinary band theory (Fermi surfaces must be closed) but allowed here because the surface states are terminated by the bulk Weyl nodes — a purely topological consequence.

**Measurement:** ARPES directly measures the Fermi surface; Fermi arcs have been observed in TaAs, NbP, and WTe₂ exactly as predicted.

### 7.5.4 — Chiral Anomaly: A Quantum Field Theory Effect in a Material

In the presence of parallel electric and magnetic fields ($\mathbf{E}\parallel\mathbf{B}$), charge is pumped between Weyl nodes of opposite chirality at rate:

$$\frac{d(n_R - n_L)}{dt} = \frac{e^2}{2\pi^2\hbar^2}\mathbf{E}\cdot\mathbf{B}$$

This is the **ABJ chiral anomaly** from quantum field theory — the breaking of classical chiral symmetry by quantum effects, discovered in particle physics in 1969. It appears directly in the transport properties of Weyl semimetals as:

**Negative longitudinal magnetoresistance:** When $\mathbf{B}\parallel\mathbf{J}$, the chiral charge pumping increases conductivity (more carriers contribute to current). $\sigma$ increases with $B$ — **negative** magnetoresistance. This is the experimental signature of the chiral anomaly, measured in TaAs in 2015.

---

## 7.6 — Superconductivity: Broken U(1) Symmetry

### 7.6.1 — The Cooper Instability

In a normal metal at $T = 0$, the Fermi sea is filled. Adding two electrons above $E_F$ — even with a vanishingly small attractive interaction — leads to a bound state. This is the **Cooper instability** (1956), proven by showing that the two-electron Schrödinger equation above a Fermi sea has a bound-state solution for any $V < 0$ (attractive interaction), no matter how weak.

The binding energy of a Cooper pair:

$$E_{binding} \approx -2\hbar\omega_D,\exp!\left(-\frac{2}{N(0)V}\right)$$

where $\omega_D$ is the Debye frequency (maximum phonon frequency), $N(0)$ is the density of states at the Fermi level, and $V > 0$ is the dimensionless pairing strength.

**Why phonon-mediated attraction:** An electron moving through the lattice slightly polarizes the surrounding ions (they are attracted toward the electron's path). This positive ion polarization lingers for a time $\sim 1/\omega_D$ after the electron has passed. A second electron arriving later is attracted to this positive polarization — experiencing an effective attractive electron-electron interaction mediated by the lattice. The net effect: the retarded phonon interaction can overcome the instantaneous Coulomb repulsion.

### 7.6.2 — The BCS Ground State and Energy Gap

The full BCS theory (Bardeen-Cooper-Schrieffer, 1957) treats all pairs simultaneously. The BCS ground state is a coherent superposition:

$$|BCS\rangle = \prod_{\mathbf{k}}(u_\mathbf{k} + v_\mathbf{k}\hat c_{\mathbf{k}\uparrow}^\dagger\hat c_{-\mathbf{k}\downarrow}^\dagger)|0\rangle$$

where $|v_\mathbf{k}|^2 = \frac{1}{2}\left(1 - \frac{\xi_\mathbf{k}}{\sqrt{\xi_\mathbf{k}^2 + |\Delta|^2}}\right)$ is the probability that the pair $(\mathbf{k}\uparrow, -\mathbf{k}\downarrow)$ is occupied, and $\xi_\mathbf{k} = E_\mathbf{k} - E_F$ is the energy measured from the Fermi level.

The **BCS gap equation** determines $\Delta$ self-consistently:

$$\boxed{\Delta = V\sum_\mathbf{k}\frac{\Delta}{2\sqrt{\xi_\mathbf{k}^2 + |\Delta|^2}}}$$

At $T = 0$, the solution:

$$\Delta(0) = 2\hbar\omega_D,\exp!\left(-\frac{1}{N(0)V}\right)$$

At temperature $T$:

$$\Delta(T) \approx \Delta(0)\sqrt{1 - \frac{T}{T_c}}, \qquad k_BT_c = 1.764,\Delta(0)$$

The ratio $2\Delta(0)/k_BT_c = 3.528$ is a universal BCS prediction — one of the first great successes of the theory, confirmed in many conventional superconductors.

### 7.6.3 — The Mexican Hat: Superconductivity as Symmetry Breaking

The BCS ground state has a definite macroscopic phase $\phi$. The order parameter:

$$\Delta = |\Delta|,e^{i\phi}$$

The free energy (Ginzburg-Landau):

$$F = a(T)|\Delta|^2 + b|\Delta|^4 + \frac{\hbar^2}{2m^*}|\nabla\Delta|^2 + \cdots$$

with $a(T) = a_0(T - T_c)$. Below $T_c$: $a < 0$, the minimum is at $|\Delta| = \sqrt{-a/2b} \neq 0$.

**This is the Mexican hat potential from Ch. 0 §0.7** — identical mathematics, ten orders of magnitude different in energy scale:

|System|Order parameter|Symmetry broken|Energy scale|
|---|---|---|---|
|Higgs field (Ch. 0)|$H =|H|e^{i\phi}$|
|BEC (Ch. 10)|$\Psi =|\Psi|e^{i\phi}$|
|Superconductor|$\Delta =|\Delta|e^{i\phi}$|
|Ferromagnet|$M =|M|e^{i\phi}$|

**Same equation, same physics, same topology.** The broken U(1) gives:

- A Goldstone boson (the phason, or in SC: the phase $\phi$ becomes a dynamical field — but it is "eaten" by the photon, giving the photon a mass inside the SC — exactly the Higgs mechanism)
- The photon mass inside the SC is what causes the Meissner effect

---

## 7.7 — London Equations and the Meissner Effect

### 7.7.1 — The London Equations

The BCS condensate has a current density (from minimal coupling, Ch. 3):

$$\mathbf{J}_s = -\frac{n_s e^2}{m_e}\mathbf{A} - \frac{n_s e\hbar}{m_e}\nabla\phi$$

where $n_s$ is the superfluid density, $\phi$ is the condensate phase, and $\mathbf{A}$ is the vector potential (in the London gauge $\nabla\phi = 0$):

$$\mathbf{J}_s = -\frac{n_s e^2}{m_e}\mathbf{A}$$

This is **London's second equation**. Taking the curl and using $\mathbf{B} = \nabla\times\mathbf{A}$:

$$\nabla\times\mathbf{J}_s = -\frac{n_s e^2}{m_e}\mathbf{B}$$

Combined with Ampere's law $\nabla\times\mathbf{B} = \mu_0\mathbf{J}_s$:

$$\nabla^2\mathbf{B} = \frac{\mathbf{B}}{\lambda_L^2}, \qquad \lambda_L = \sqrt{\frac{m_e}{\mu_0 n_s e^2}}$$

The solution inside a superconductor occupying $x > 0$:

$$B(x) = B_0,e^{-x/\lambda_L}$$

The magnetic field **decays exponentially** from the surface with the **London penetration depth** $\lambda_L$. For most conventional SCs: $\lambda_L \sim 10$–$100$ nm. For $x \gg \lambda_L$: $\mathbf{B} = 0$ — the Meissner effect.

**The Higgs mechanism made explicit:** The photon inside the superconductor acquires effective mass $m_\gamma = \hbar/c\lambda_L$ — exactly the Higgs mechanism where the $W$ and $Z$ bosons acquire mass from the Higgs VEV. In the SC, the Higgs VEV is replaced by $|\Delta|$.

### 7.7.2 — Type I and Type II Superconductors

Compare the London penetration depth $\lambda_L$ (field expulsion) with the **Ginzburg-Landau coherence length** $\xi$ (spatial variation of $|\Delta|$, the distance over which the order parameter recovers its bulk value):

$$\kappa_{GL} = \frac{\lambda_L}{\xi}$$

- **Type I** ($\kappa_{GL} < 1/\sqrt{2}$): perfect Meissner up to $H_c$; then normal. Rare in practice.
    
- **Type II** ($\kappa_{GL} > 1/\sqrt{2}$): Meissner up to $H_{c1}$; then **mixed (Abrikosov vortex) state** from $H_{c1}$ to $H_{c2}$; then normal.
    

**Abrikosov vortices** (Nobel Prize 2003): In the mixed state, quantized tubes of magnetic flux penetrate the superconductor. Each vortex carries exactly one flux quantum $\Phi_0 = h/2e$ and has:

- A **normal core** of radius $\xi$ (where $|\Delta| \to 0$)
- Circulating supercurrents in a ring of radius $\lambda_L$

High-$T_c$ superconductors (YBCO, BSCCO) are Type II with $H_{c2} > 100$ T — the reason they can be used for high-field magnets.

---

## 7.8 — Flux Quantization and the Josephson Effect

### 7.8.1 — Flux Quantization

The single-valuedness of the superconducting order parameter $\Delta = |\Delta|e^{i\phi}$ around a closed loop requires:

$$\oint\nabla\phi\cdot d\mathbf{l} = 2\pi n, \quad n \in \mathbb{Z}$$

Using the expression for the supercurrent (London equation), the total magnetic flux threading the loop:

$$\boxed{\Phi = n\Phi_0, \qquad \Phi_0 = \frac{h}{2e} = 2.067\times 10^{-15};\text{Wb}}$$

**The $2e$ denominator** confirms that the supercurrent is carried by Cooper pairs (charge $2e$), not individual electrons ($e$). This was experimentally confirmed in 1961 — two years before BCS theory was fully accepted.

### 7.8.2 — The Josephson Effect

Two superconductors with order parameters $\Delta_1 = |\Delta|e^{i\phi_1}$ and $\Delta_2 = |\Delta|e^{i\phi_2}$ separated by a thin insulating barrier (a Josephson junction):

**DC Josephson effect:** A supercurrent flows with no applied voltage:

$$\boxed{I = I_c\sin(\phi_1 - \phi_2)}$$

where $I_c$ is the critical current (maximum Cooper pair tunneling rate) and $\phi_1 - \phi_2$ is the phase difference across the junction.

**AC Josephson effect:** Apply a DC voltage $V$ across the junction. The phase evolves as $d(\phi_1-\phi_2)/dt = 2eV/\hbar$, giving an AC supercurrent:

$$I(t) = I_c\sin!\left(\phi_0 + \frac{2eV}{\hbar}t\right) \quad\Longrightarrow\quad f_{AC} = \frac{2eV}{h}$$

**The Josephson frequency-voltage relation** $f = 2eV/h = 483597.8...;\text{GHz/V}$:

- It depends only on fundamental constants ($e$ and $h$), not on the material
- Since 2019, it defines the volt in the SI system: $1;\text{V} \equiv f/483597.8;\text{GHz}$ (exact by definition, traceable to quantum mechanics)

### 7.8.3 — The SQUID: Most Sensitive Magnetometer

A superconducting quantum interference device (SQUID) consists of a superconducting loop with two Josephson junctions. The critical current:

$$I_c(\Phi) = 2I_{c0}\left|\cos!\left(\frac{\pi\Phi}{\Phi_0}\right)\right|$$

oscillates with the magnetic flux $\Phi$ through the loop with period $\Phi_0 = h/2e$. Measuring $I_c$ to 1 part in $10^3$ resolves flux changes of:

$$\delta\Phi \sim 10^{-3}\Phi_0 = 2\times 10^{-18};\text{Wb}$$

For a loop area of $1;\text{mm}^2$: $\delta B \sim 2\times 10^{-12};\text{T}$ — sensitivity far below Earth's field ($\sim 50;\mu$T) and the magnetic field of the human brain ($\sim 10^{-13}$ T at the scalp).

**Engineering applications:** Magnetoencephalography (MEG) for brain imaging; non-destructive testing; geodetic surveys; detection of unexploded ordnance; qubit readout in superconducting quantum computers.

---

## 7.9 — Coulomb Blockade and Mesoscopic Physics

At the boundary between Layer 1 (quantum) and Layer 2 (classical continuum), sits a regime where systems are large enough to have continuous energy spectra but small enough that single-electron charging matters.

### 7.9.1 — The Quantum Dot

A **quantum dot** — a small conductor (semiconductor or metallic island) of capacitance $C$ — has a charging energy:

$$E_C = \frac{e^2}{2C}$$

For a dot with $C \sim 1$ aF: $E_C \sim 80$ meV $\gg k_BT$ at low temperature. Adding one electron to the dot costs energy $E_C$ — but if the gate voltage exactly compensates this, the electron tunnels freely.

The result: **Coulomb oscillations** — the conductance through the dot oscillates as a function of gate voltage, with period $\Delta V_g = e/C_g$. Each peak corresponds to adding exactly one electron. In a DC bias, single electrons tunnel one at a time: a **single-electron transistor**.

**The quantum dot level spectrum:** For very small dots, the discrete energy levels from quantum confinement (Ch. 4 particle-in-box) become relevant. The dot becomes an artificial atom — with shell structure, spin states, and exchange interactions controlled by gate voltages.

**Engineering:** Quantum dots are the leading platform for semiconductor spin qubits; the Coulomb blockade is used for charge sensing with $\sim 10^{-4} e/\sqrt{\text{Hz}}$ sensitivity; single-photon emitters for quantum communication.

---

## 7.10 — The Topology Thread: From Ch. 0 to Engineering

Five connections between the topology of Ch. 0 and the physics of this chapter:

|Ch. 0 structure|Condensed matter analog|Ch. 7 section|
|---|---|---|
|θ-term in QCD|Axion electrodynamics in TI; $\theta = \pi$|§7.4.4|
|Weyl fermion field $\psi_L$ in $\mathcal{L}_{SM}$|Weyl quasiparticle in TaAs, NbAs|§7.5.1|
|ABJ chiral anomaly|Negative magnetoresistance in Weyl metals|§7.5.4|
|Higgs mechanism: U(1) → photon mass|Meissner: U(1) breaking → photon mass inside SC|§7.7.1|
|Anomaly cancellation in SM requires specific particle content|Nielsen-Ninomiya: Weyl nodes come in equal and opposite pairs|§7.5.2|

**The summary statement:** The topological terms in the Standard Model Lagrangian (the θ-term, the chiral anomaly, the Higgs mechanism) are not curiosities of high-energy physics. They are the mathematical structure that also governs the behavior of electrons in specific crystal arrangements. The book's claim from Ch. 0 — that every later chapter is a limit or projection of the action — is literalized here: a Weyl semimetal is a condensed matter quantum field theory with the same action as part of $\mathcal{L}_{SM}$.

---

## 7.11 — Summary

Layer 1 closes with the topological perspective:

|Result|Key formula|Protection|
|---|---|---|
|Berry phase|$\gamma = \oint\mathbf{A}_n\cdot d\mathbf{k}$|Geometric (path-dependent)|
|Chern number|$C = (1/2\pi)\iint\Omega,d^2k \in\mathbb{Z}$|Topological (always integer)|
|Hall conductivity|$\sigma_{xy} = (e^2/h)\sum_n C_n$|Topological (quantized)|
|TI surface states|$H = \hbar v_F(\hat z\times\boldsymbol{\sigma})\cdot\mathbf{k}$|Symmetry ($\mathcal{T}$)|
|Weyl node|$H = \pm\hbar v_F\boldsymbol{\sigma}\cdot\mathbf{k}$; $C = \pm 1$|Topological (Berry monopole)|
|BCS gap|$\Delta = 2\hbar\omega_D e^{-1/N(0)V}$|Symmetry breaking|
|Meissner|$B = B_0 e^{-x/\lambda_L}$; $B_{bulk} = 0$|Broken U(1) + Higgs|
|Flux quant.|$\Phi = n h/2e$|Phase winding (integer)|
|Josephson|$I = I_c\sin\Delta\phi$; $f = 2eV/h$|Phase coherence|

---

## 7.12 — Engineering Thread

|Physics|Application|
|---|---|
|Quantum Hall effect|Primary resistance standard $R_K = h/e^2$ (exact); calibration|
|Topological surface states|Spin-polarized current sources; future low-dissipation transistors|
|Weyl semimetal chiral anomaly|Ultra-high mobility; negative MR sensors|
|Meissner effect|MRI magnets (YBCO, NbTi); magnetic shielding; Maglev|
|Flux quantization + SQUID|Magnetoencephalography; brain imaging; geophysical surveys|
|Josephson voltage standard|SI volt definition; precision metrology|
|BCS superconductors|Particle accelerator magnets (LHC uses 8.3 T NbTi); power cables|
|High-T_c superconductors|Future power grids; FCL (fault current limiters)|
|Superconducting qubits|IBM, Google, IQM quantum computers all use Josephson junctions|
|Coulomb blockade / quantum dots|Spin qubits; single-electron transistors; single-photon emitters|

---

## 7.13 — Looking Ahead: Bridge B

Layer 1 is complete. Starting with the Standard Model Lagrangian (Ch. 0) and the action principle (Ch. 1), we derived:

- The Schrödinger equation (Ch. 3 Bridge A)
- Quantization and the hydrogen atom (Ch. 4)
- Spin, Pauli exclusion, the periodic table (Ch. 5)
- Band theory, bonding, nuclear physics (Ch. 6)
- Topology, quantum Hall effect, superconductivity (Ch. 7)

Everything above is quantum mechanical. Chapter 8 begins **Bridge B** — the descent to the classical world. Four simultaneous limits (§1.9 of the layer map):

- $\hbar\to 0$: quantum expectation values → Newton's laws (Ch. 9)
- $N\to\infty$, ensemble average: quantum states → thermodynamics (Ch. 10)
- Classical U(1) field limit: quantum EM → Maxwell's equations (Ch. 11)
- Weak metric field: GR → Newtonian gravity (Ch. 8)
- Kubo averaging: quantum scattering → Ohm, Fourier, Fick, viscosity, Hooke (Ch. 13)

The entire landscape of classical engineering science emerges from these five limiting operations applied to the quantum world of Layer 1.

---

_End of Chapter 7. End of Layer 1._

---

_Next: Chapter 8 — Bridge B.d: From General Relativity to Newton's Law of Gravitation_