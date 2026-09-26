# Band Theory, Molecular Bonding, and Nuclear Physics

### Assembling Matter: From Atoms to Solids to Nuclei

---

> _The electron does not belong to any particular atom._ _In a metal, every electron belongs to every atom simultaneously._ _This is why metals conduct electricity and why they are shiny._ — Richard Feynman, _The Feynman Lectures_, Vol. III

---

## 6.0 — Where We Are

Chapters 4 and 5 built the quantum mechanical description of isolated atoms. Chapter 6 asks: what happens when you take $10^{23}$ atoms and pack them together?

The answer to that question is **band theory** — the quantum mechanics of electrons in a periodic crystal lattice. It is the single most engineering-relevant result in all of quantum mechanics:

- It explains why copper conducts and glass insulates
- It explains why silicon can be a transistor
- It explains why GaAs emits light and silicon does not
- It is the quantum foundation of every semiconductor device ever built

This chapter also completes two other branches of Layer 1: the full taxonomy of molecular bonds that hold materials together, and the nuclear physics that governs radioactivity, fission, and fusion. By the end of this chapter, Layer 1 is complete — every material property that engineering depends on has a quantum mechanical origin that you can trace.

---

## 6.1 — From One Atom to $10^{23}$: Bloch's Theorem

### 6.1.1 — The Problem

In Chapter 4, the potential was $V(r) = -e^2/4\pi\epsilon_0 r$ — a single nucleus. In a crystal with lattice constant $a$, there is a nucleus at every lattice point $\mathbf{R} = n_1\mathbf{a}_1 + n_2\mathbf{a}_2 + n_3\mathbf{a}_3$, so the potential is:

$$V(\mathbf{r}) = \sum_{\mathbf{R}} V_{atom}(\mathbf{r} - \mathbf{R})$$

This is a **periodic potential**: $V(\mathbf{r} + \mathbf{a}) = V(\mathbf{r})$.

The Schrödinger equation is now:

$$\left(-\frac{\hbar^2}{2m_e}\nabla^2 + V(\mathbf{r})\right)\psi = E\psi$$

with $V(\mathbf{r})$ having the periodicity of the crystal lattice.

### 6.1.2 — Bloch's Theorem from Noether's Theorem

A discrete translation by lattice vector $\mathbf{a}$ is a symmetry of the Hamiltonian: $[\hat H, \hat T_\mathbf{a}] = 0$ where $\hat T_\mathbf{a}$ is the translation operator.

By the argument of Ch. 1 §1.7 (Noether's theorem applied to discrete translations): the eigenstates of $\hat H$ can be simultaneously chosen as eigenstates of $\hat T_\mathbf{a}$. The eigenvalue of $\hat T_\mathbf{a}$ must have unit modulus (since $|\hat T_\mathbf{a}\psi|^2 = |\psi|^2$ — translations don't change the normalization). So:

$$\hat T_\mathbf{a}\psi = e^{i\mathbf{k}\cdot\mathbf{a}}\psi$$

for some wavevector $\mathbf{k}$. This immediately gives:

$$\boxed{\psi_{n\mathbf{k}}(\mathbf{r}) = e^{i\mathbf{k}\cdot\mathbf{r}},u_{n\mathbf{k}}(\mathbf{r})}$$

where $u_{n\mathbf{k}}(\mathbf{r} + \mathbf{a}) = u_{n\mathbf{k}}(\mathbf{r})$ is a function with the same periodicity as the lattice. This is **Bloch's theorem**.

The quantum number $\mathbf{k}$ is the **crystal momentum** — the conserved quantity corresponding to discrete translational symmetry, by Noether's theorem. The band index $n$ labels which periodic function $u_{n\mathbf{k}}$ the electron lives in.

### 6.1.3 — The Brillouin Zone

The crystal momentum $\mathbf{k}$ is not unique: adding a **reciprocal lattice vector** $\mathbf{G}$ (defined by $e^{i\mathbf{G}\cdot\mathbf{a}} = 1$) gives the same Bloch state. This means $\mathbf{k}$ and $\mathbf{k} + \mathbf{G}$ describe the same physical state.

We therefore restrict $\mathbf{k}$ to the **first Brillouin zone** — the region of $\mathbf{k}$-space closest to the origin, bounded by the planes where $|\mathbf{k}| = |\mathbf{k} - \mathbf{G}|$ (the perpendicular bisectors of reciprocal lattice vectors).

For a 1D crystal with lattice constant $a$: the first Brillouin zone is $k \in [-\pi/a, +\pi/a]$. The zone boundaries at $k = \pm\pi/a$ are where the electron wavelength $\lambda = 2\pi/k = 2a$ equals twice the lattice constant — the condition for Bragg reflection.

---

## 6.2 — The Nearly Free Electron Model: Where Band Gaps Come From

### 6.2.1 — Free Electrons as the Starting Point

For $V = 0$, the solutions are plane waves $\psi_k = e^{ikx}/\sqrt{L}$ with energy $E = \hbar^2k^2/2m_e$. This is the free electron parabola.

Now add a weak periodic potential. Write $V(x) = \sum_G V_G e^{iGx}$ (Fourier series), where $G = 2\pi n/a$ are reciprocal lattice vectors.

### 6.2.2 — Bragg Reflection and the Band Gap

Most $\mathbf{k}$ values are barely affected by the weak perturbation. But at the Brillouin zone boundary $k = \pm\pi/a$, two degenerate states $|k\rangle$ and $|k - G\rangle = |-\pi/a\rangle$ have equal energy. Degenerate perturbation theory gives two new eigenstates:

$$\psi_\pm = \frac{1}{\sqrt{2}}\left(e^{i\pi x/a} \pm e^{-i\pi x/a}\right) = \begin{cases}\sqrt{2}\cos(\pi x/a)\\sqrt{2}\sin(\pi x/a)\end{cases}$$

These have different spatial distributions:

- $\psi_+$: $|\psi_+|^2 \propto \cos^2(\pi x/a)$ — maxima at atomic sites (high $V$, ions are there) → **higher energy**
- $\psi_-$: $|\psi_-|^2 \propto \sin^2(\pi x/a)$ — maxima between atoms (low $V$) → **lower energy**

The energy splitting is:

$$E_g = E_+ - E_- = 2|V_G| = 2\left|\int_0^a V(x)e^{-i2\pi x/a}\frac{dx}{a}\right|$$

This is the **band gap** — it is twice the first Fourier coefficient of the periodic potential. **Band gaps are Bragg diffraction of electron waves.**

The electron wavelength $\lambda = 2a$ at the zone boundary satisfies the Bragg condition for reflection from planes separated by $a$: $2a\sin(90°) = \lambda$. The electron standing waves are Bragg-reflected, and the two standing waves have different energies — the gap.

### 6.2.3 — The Band Structure Picture

The result: energy $E(k)$ is not a single parabola but a sequence of **bands** separated by **gaps**, with the parabolic shape modified near zone boundaries:

```
E
│        ↑ 3rd band
│       ╱╲
│      /  ╲          ╱╲
│     /    ╲        /  ╲      gap (E_g)
│    /      ╲──────/    ╲     ↑ 2nd band
│   /                    ╲    │
│  /              gap     ╲───╯
│ /                        ╲  ↑ 1st band
│╱                          ╲╱
└────────────────────────────── k
  -π/a         0          π/a
```

Each band holds exactly $2N$ electrons (factor of 2 for spin), where $N$ is the number of unit cells. The first band holds $2N$ states, the second holds $2N$ states, and so on.

---

## 6.3 — The Tight-Binding Model: Band Theory from the Bottom Up

The nearly-free-electron model works when the potential is weak and electrons are nearly free. The **tight-binding model** works from the opposite limit: electrons are nearly localized on atoms, with small overlap between neighbors.

### 6.3.1 — The 1D Tight-Binding Chain

Consider $N$ atoms in a line with spacing $a$, each contributing one atomic orbital $\phi(\mathbf{r} - \mathbf{R}_n)$. The Bloch wavefunction:

$$\psi_k(x) = \frac{1}{\sqrt{N}}\sum_{n=1}^{N} e^{ikna}\phi(x - na)$$

Computing the energy $\langle\psi_k|\hat H|\psi_k\rangle$:

$$E(k) = E_0 + \langle\phi_0|\hat H - \hat H_{atom}|\phi_0\rangle + 2t\cos(ka) + \cdots$$

where $t = -\langle\phi_0|\hat H|\phi_1\rangle > 0$ is the **hopping integral** — the matrix element for an electron to tunnel from one atom to its neighbor.

Dropping constants:

$$\boxed{E(k) = E_0 - 2t\cos(ka)}$$

This is the 1D tight-binding band. Its width is $4t$ (from $E_0 - 2t$ at $k = 0$ to $E_0 + 2t$ at $k = \pi/a$). The **bandwidth** is set by the overlap between neighboring orbitals:

- Large overlap (e.g., metallic conductors): large $t$ → wide band → electrons nearly free → good conductor
- Small overlap (e.g., molecular crystals): small $t$ → narrow band → electrons nearly localized → poor conductor or insulator

### 6.3.2 — Graphene: The 2D Tight-Binding Model

Graphene is a single atomic layer of carbon with a hexagonal lattice. Each carbon is $sp^2$ hybridized (Ch. 5 §5.8.3), contributing one unhybridized $p_z$ orbital per site to the $\pi$-band.

The honeycomb lattice has two atoms per unit cell (sublattice A and B), giving two tight-binding bands. Solving the $2\times 2$ Hamiltonian near the $K$-point (corner of the hexagonal Brillouin zone):

$$E(\mathbf{q}) \approx \pm\hbar v_F|\mathbf{q}|, \qquad v_F = \frac{3ta}{2\hbar} \approx 10^6;\text{m/s}$$

where $\mathbf{q} = \mathbf{k} - \mathbf{K}$ is measured from the $K$-point.

**This is a linear dispersion relation** — the same as for a massless relativistic particle ($E = \hbar c |\mathbf{k}|$ with $v_F$ replacing $c$). The electrons in graphene near the $K$-point behave as massless Dirac fermions. The Schrödinger equation is not sufficient — a 2D Dirac equation governs them.

**This is exactly why graphene appears as a Weyl semimetal case study in Ch. 7:** a Layer-0 concept (Dirac/Weyl fermions from $\mathcal{L}_{SM}$) reappears in a carbon atom arrangement — a remarkable example of the top-down thread.

---

## 6.4 — Effective Mass: How Band Electrons Behave Like Classical Particles

### 6.4.1 — Deriving the Effective Mass

An electron in a band with dispersion $E_n(\mathbf{k})$ responds to an external force $\mathbf{F}$ (from electric or magnetic fields). Its equation of motion:

$$\mathbf{F} = \hbar\frac{d\mathbf{k}}{dt}$$

The group velocity (velocity of the wavepacket):

$$\mathbf{v}_g = \frac{1}{\hbar}\frac{\partial E_n}{\partial\mathbf{k}}$$

Differentiating:

$$\frac{d\mathbf{v}_g}{dt} = \frac{1}{\hbar}\frac{\partial^2 E_n}{\partial\mathbf{k}^2}\frac{d\mathbf{k}}{dt} = \frac{1}{\hbar^2}\frac{\partial^2 E_n}{\partial\mathbf{k}^2}\cdot\mathbf{F}$$

Comparing with $\mathbf{F} = m^*\mathbf{a}$:

$$\boxed{m^* = \hbar^2\left(\frac{\partial^2 E}{\partial k^2}\right)^{-1}}$$

The **effective mass** $m^*$ is the reciprocal of the band curvature. It tells you how the band electron responds to forces — replacing the bare electron mass $m_e$ in all macroscopic equations.

**Key physical consequences:**

|Region of band|$\partial^2 E/\partial k^2$|$m^*$|Physical meaning|
|---|---|---|---|
|Bottom of band|$> 0$ (concave up)|$m^* > 0$, often $< m_e$|Light electrons, easy to accelerate|
|Top of band|$< 0$ (concave down)|$m^* < 0$|Electron accelerates opposite to force|
|Inflection point|$= 0$|$m^* \to \infty$|Electron doesn't respond to force|

**Holes:** Near the top of a filled band, it is convenient to describe the missing electrons (vacancies) as **holes** with:

- Positive charge $+e$
- Positive effective mass $m_h^* = -m_e^* > 0$
- Energy measured downward from the band top

A hole in the valence band acts exactly like a positively charged particle — it moves opposite to an electron under the same field. This is not a classical analog; it is a consequence of the antisymmetry of the many-electron Fermi sea.

---

## 6.5 — Metals, Semiconductors, and Insulators

### 6.5.1 — The Fermi Level and Band Filling

At $T = 0$, electrons fill all available states up to the **Fermi energy** $E_F$. The key question is: **where does $E_F$ fall relative to the band structure?**

The **Fermi-Dirac distribution** (derived rigorously in Ch. 10, Bridge B.b):

$$f(E) = \frac{1}{e^{(E-E_F)/k_BT} + 1}$$

gives the probability that a state at energy $E$ is occupied at temperature $T$. At $T = 0$: $f = 1$ for $E < E_F$, $f = 0$ for $E > E_F$. At finite $T$, the step broadens over a range $\sim k_BT$ around $E_F$.

### 6.5.2 — The Three Cases

**Metals:** $E_F$ lies inside a band — the band is partially filled. States immediately above $E_F$ are available for electrons to scatter into. Any infinitesimal applied field produces a current. $\sigma \sim 10^6$–$10^8$ S/m.

Example: copper. Configuration $[\text{Ar}]3d^{10}4s^1$ — the half-filled $4s$ band gives one conduction electron per atom. The $3d$ band is full and below $E_F$, contributing to high density of states but not to conduction.

**Semiconductors:** $E_F$ lies in a band gap $E_g \sim 0.1$–$3$ eV. At $T = 0$, the valence band is completely full and the conduction band is completely empty — the material is an insulator. At room temperature ($k_BT \approx 0.026$ eV), a small fraction of electrons is thermally excited across the gap, producing both conduction electrons and valence band holes. Conductivity is intermediate and strongly temperature-dependent. $\sigma \sim 10^{-4}$–$10^3$ S/m.

**Insulators:** Same physics as semiconductors but $E_g > 3$–$4$ eV. Thermal excitation across the gap is negligible at room temperature. $\sigma \lesssim 10^{-10}$ S/m.

**The quantitative boundary is not sharp** — "semiconductor" and "insulator" differ in degree, not kind. Diamond ($E_g = 5.5$ eV) is an insulator; GaN ($E_g = 3.4$ eV) is a semiconductor used in blue LEDs.

### 6.5.3 — Why Filled Bands Don't Conduct

If a band is completely filled, for every electron at $+k$ there is one at $-k$ with opposite velocity. The net current is exactly zero regardless of field, because applying a field cannot promote any electron — all states are occupied. A small field shifts the $k$-distribution slightly, but a completely filled band has no available states to shift into.

This is a topological statement: a completely filled band's contribution to current is identically zero by crystal symmetry. This will reappear in Ch. 7 when we discuss the quantum Hall effect.

---

## 6.6 — Semiconductor Physics

### 6.6.1 — The Carrier Concentrations

In an intrinsic (undoped) semiconductor with band gap $E_g$:

$$n = p = n_i = \sqrt{N_c N_v},\exp!\left(-\frac{E_g}{2k_BT}\right)$$

where $N_c = 2(m_e^*k_BT/2\pi\hbar^2)^{3/2}$ and $N_v = 2(m_h^*k_BT/2\pi\hbar^2)^{3/2}$ are the **effective densities of states** for the conduction and valence bands.

For silicon at 300 K: $n_i = 1.5\times 10^{10};\text{cm}^{-3}$ compared to the total atomic density $5\times 10^{22};\text{cm}^{-3}$. Only 1 in $3\times 10^{12}$ silicon atoms contributes a free electron at room temperature.

The exponential factor $e^{-E_g/2k_BT}$ is the Boltzmann weight for exciting an electron across the gap. The same factor appears in reaction kinetics (Arrhenius law, Ch. 2 catalogue) — both reflect thermal activation over an energy barrier.

### 6.6.2 — Doping: Engineering the Fermi Level

The power of semiconductors is that $n$ and $p$ can be controlled over many orders of magnitude by adding **impurity atoms** — atoms with one more or one fewer valence electron than the host.

**n-type doping:** Replace Si ($4$ valence electrons) with phosphorus ($5$ valence electrons). The extra electron has no available bond — it sits in a hydrogen-like orbital bound to the P⁺ ion with binding energy:

$$E_d = \frac{m_e^* e^4}{2(4\pi\epsilon_0\epsilon_r)^2\hbar^2} = E_H\frac{m_e^*}{m_e\epsilon_r^2}$$

For Si ($m_e^* \approx 0.33m_e$, $\epsilon_r \approx 11.7$): $E_d \approx 45$ meV. The donor level sits just 45 meV below the conduction band — easily ionized at room temperature, donating a free electron to the conduction band.

At room temperature, essentially all donors are ionized: $n \approx N_D$.

**p-type doping:** Replace Si with boron ($3$ valence electrons). One bond is incomplete — a hole is "bound" to the B⁻ ion with acceptor energy $E_a \approx 45$ meV above the valence band. At room temperature: $p \approx N_A$.

**The mass action law** (valid for non-degenerate semiconductors):

$$n\cdot p = n_i^2 \qquad\text{(always, regardless of doping)}$$

This follows from the chemical equilibrium condition for electron-hole pair generation: $e^- + h^+ \rightleftharpoons 0$ with equilibrium constant $n_i^2$.

### 6.6.3 — Common Semiconductors and Their Properties

|Material|$E_g$ (eV)|Gap type|$m_e^*/m_e$|Application|
|---|---|---|---|---|
|Ge|0.67|Indirect|0.22|Infrared detectors|
|Si|1.12|Indirect|0.36|MOSFETs, solar cells, ICs|
|GaAs|1.42|Direct|0.067|Lasers, LEDs, HEMTs, solar cells|
|InP|1.34|Direct|0.077|Telecom lasers (1550 nm)|
|GaN|3.40|Direct|0.20|Blue LEDs, power electronics|
|SiC|3.26|Indirect|0.42|High-power, high-temperature electronics|
|diamond|5.50|Indirect|0.36|Potential future ultra-wide-bandgap devices|

**Direct vs. indirect gap** (Ch. 2 catalogue entry made explicit):

- **Direct gap** ($E_g$ at same $\mathbf{k}$ for valence and conduction band extrema): An electron can recombine with a hole by emitting a photon directly — momentum is conserved with no phonon required. High radiative efficiency. $\Rightarrow$ LEDs and semiconductor lasers.
- **Indirect gap** (extrema at different $\mathbf{k}$): Recombination requires a phonon to conserve crystal momentum. Very low radiative efficiency. Silicon does not emit light efficiently. $\Rightarrow$ Transistors and solar cells (where carrier collection, not emission, matters).

**The laser condition** requires a direct-gap material and population inversion ($E_F^n - E_F^p > E_g$, where $E_F^n$, $E_F^p$ are the quasi-Fermi levels under forward bias). All practical semiconductor lasers use III-V direct-gap materials.

---

## 6.7 — Phonons: The Quantum Mechanics of Heat

### 6.7.1 — Quantizing the Lattice Vibrations

The atoms in a crystal are not fixed — they vibrate around their equilibrium positions. For small displacements, every vibration mode is a harmonic oscillator (Ch. 4 §4.3). Quantizing it gives a **phonon** with energy $\hbar\omega$.

A crystal with $N$ atoms and $p$ atoms per unit cell has $3pN$ vibrational modes. These divide into branches:

- **Acoustic branches** (3 branches): all atoms in a unit cell move in phase; $\omega \to 0$ as $k \to 0$ (long-wavelength sound waves)
- **Optical branches** ($3p - 3$ branches): atoms in the unit cell move out of phase; finite frequency even at $k = 0$ (can interact with light — hence "optical")

For a diatomic chain with masses $M_1$ and $M_2$ and spring constant $K$:

$$\omega^2 = K\left(\frac{1}{M_1} + \frac{1}{M_2}\right) \pm K\sqrt{\left(\frac{1}{M_1}+\frac{1}{M_2}\right)^2 - \frac{4\sin^2(ka/2)}{M_1M_2}}$$

$+$ sign: optical branch; $-$ sign: acoustic branch. The gap between them is $\sqrt{2K/M_1}$ to $\sqrt{2K/M_2}$ — no phonon modes exist in this gap.

### 6.7.2 — Phonons Carry Heat

Thermal conductivity in a crystal comes from phonon transport (in insulators and semiconductors) and electron transport (in metals). For phonons:

$$\kappa_{phonon} = \frac{1}{3}C_v v_s \ell$$

where $C_v$ is the heat capacity, $v_s$ is the phonon group velocity (speed of sound), and $\ell$ is the phonon mean free path (limited by phonon-phonon scattering, phonon-boundary scattering, and phonon-impurity scattering).

Diamond has an exceptionally high thermal conductivity ($\kappa \approx 2000$ W/m·K, five times copper) because: (1) light carbon atoms → high $v_s$, (2) strong covalent bonds → high $\omega$ → sparse phonon-phonon scattering (fewer phonons to scatter from at room temperature), (3) no heavy atoms to scatter phonons.

### 6.7.3 — Electron-Phonon Scattering: Why Metals Resist

In metals, electrons near $E_F$ scatter from phonons. Phonon occupation increases with temperature as $n_{ph} \propto k_BT/\hbar\omega$ (Bose-Einstein distribution in the classical regime). Scattering rate $\propto$ phonon occupation $\propto T$. Since $\sigma = ne^2\tau/m^*$ (Bridge B.e result), and $\tau \propto 1/T$:

$$\rho_{metal} = 1/\sigma \propto T \quad\text{(at room temperature, Bloch-Grüneisen)}$$

This is the measured linear resistivity of metals at room temperature — aluminum, copper, gold, all show $\rho \propto T$ above ~100 K.

At low $T$: phonon occupation $\propto T^5$ (few phonons; only small-angle scattering), giving $\rho \propto T^5$ (Bloch-Grüneisen). At very low $T$: residual resistance from impurities and defects (temperature-independent). The Mathiessen rule adds these: $\rho = \rho_0 + AT^5 + BT$.

**Engineering thread:** The temperature dependence of resistance is what makes RTDs (Resistance Temperature Detectors) work. Platinum has a precisely characterized $\rho(T)$ from this physics, enabling temperature measurement to $\pm 0.01°$C.

---

## 6.8 — Bonding in Solids: A Complete Taxonomy

Chapter 5 gave covalent bonding from LCAO. Here we complete the picture with every bond type and the crystal structures they produce.

### 6.8.1 — Ionic Bonding

**Origin:** Transfer of electrons from electropositive to electronegative atoms creates charged ions; Coulomb attraction holds them together.

**Example:** NaCl. Na gives its $3s^1$ electron to Cl (which wants one to fill $3p^6$). The lattice energy (per ion pair):

$$U_{Madelung} = -\frac{M e^2}{4\pi\epsilon_0 r_0}\left(1 - \frac{1}{n}\right)$$

where $M \approx 1.748$ is the **Madelung constant** for the NaCl structure (from summing the alternating +/- Coulomb interactions over the entire lattice), $r_0$ is the equilibrium spacing, and $n \approx 9$ is the Born repulsion exponent.

**Properties:** High melting point (strong Coulomb attraction), brittle (cleavage on ionic planes), dissolve in polar solvents, conduct electricity when molten or dissolved (free ions).

**Engineering:** Ceramic insulators (Al₂O₃, MgO), ionic conductors for fuel cells (ZrO₂), piezoelectrics (BaTiO₃).

### 6.8.2 — Covalent Bonding

**Origin:** Shared electrons in bonding molecular orbitals (LCAO, Ch. 5 §5.8). Bond strength from electron density accumulation between nuclei.

**Properties:** Directional (bond angles determined by orbital geometry), hard, brittle (breaking a bond requires disrupting the electron sharing), covalent crystals: diamond, Si, GaAs.

**Engineering:** Semiconductor devices (Si, GaAs, SiC), hard coatings (diamond, SiC), ceramics (SiC, Si₃N₄).

### 6.8.3 — Metallic Bonding

**Origin:** Valence electrons delocalize from their parent atoms and form a "sea" that bonds all ions together. Band theory is the quantum description of this: the electrons occupy wide, partially filled bands (low effective mass, high mobility).

**Properties:** Non-directional (no preferred bond angles → ductile, malleable), high electrical and thermal conductivity (delocalized electrons), opaque and lustrous (plasma frequency in UV → reflects all visible light, Ch. 2).

**Why metals are ductile but ionic crystals are brittle:** In a metal, shifting atomic planes relative to each other merely rearranges which electrons are between which ions — the bond doesn't break. In an ionic crystal, shifting planes brings like-charge ions adjacent, creating a repulsive plane — catastrophic fracture.

### 6.8.4 — Van der Waals (London Dispersion) Bonding

**Origin:** Quantum fluctuations in the electron distribution of neutral atoms create instantaneous dipoles; these instantaneous dipoles polarize neighboring atoms. The interaction energy between induced dipoles:

$$U_{vdW} = -\frac{C}{r^6}$$

where $C$ depends on the atomic polarizabilities and ionization energies. This is the **London dispersion force** — it has a purely quantum origin (zero for classical atoms with no fluctuations) and is always attractive.

**Magnitude:** Much weaker than ionic or covalent bonds ($\sim 1$–$10$ kJ/mol vs. $\sim 100$–$1000$ kJ/mol). But present between _all_ atoms.

**Engineering:** Holds graphite layers together (weak interlayer vdW → easy sliding → graphite is a lubricant); adhesion of geckos to surfaces (van der Waals contact area); 2D material exfoliation (Scotch tape method for graphene exploits weak vdW between layers); molecular recognition in drug design.

### 6.8.5 — Hydrogen Bonding

**Origin:** An H atom covalently bonded to an electronegative atom (F, O, N) has its electron pulled away, exposing the bare proton. This positive proton attracts the lone pairs of neighboring electronegative atoms. Energy: $\sim 10$–$40$ kJ/mol.

**Engineering consequence:** Water's anomalously high boiling point (100°C vs. $-60$°C for H₂S, the next heavier group-16 hydride), its high heat capacity and latent heat — all from hydrogen bonds. These make water a uniquely effective heat transfer fluid and give it its role in biology and industrial cooling. Concrete strength depends on H-bonding in C-S-H gel. Polymer properties (nylon, proteins) depend critically on H-bond geometry.

---

## 6.9 — Nuclear Physics: The Strong Force's Engineering Consequences

### 6.9.1 — The Nuclear Force

In Ch. 0, the strong force was SU(3) color — confined to quark interactions inside hadrons. The **residual strong force** between nucleons (protons and neutrons) is an effective force mediated by pion exchange — an analog of the van der Waals force between atoms (which is a residual electromagnetic interaction between neutral atoms).

The nucleon-nucleon potential is approximately:

$$V_{NN}(r) \approx -\frac{g^2}{4\pi}\frac{e^{-m_\pi c r/\hbar}}{r}$$

(Yukawa potential, where $m_\pi c^2 \approx 135$ MeV is the pion mass). The range of the strong force:

$$r_0 = \frac{\hbar}{m_\pi c} \approx 1.4;\text{fm} \approx 1.4\times 10^{-15};\text{m}$$

This sets the scale of nuclear physics. At $r < r_0$: strong attraction. At $r > 2$–$3,r_0$: negligible. At $r \lesssim 0.5$ fm: short-range repulsion (hard core). The strong force is short-range, much stronger than EM at close range, and saturates (each nucleon bonds only to its immediate neighbors).

### 6.9.2 — Nuclear Binding Energy

The binding energy $B(Z, A)$ is the energy required to completely separate a nucleus of $Z$ protons and $N = A - Z$ neutrons into free nucleons:

$$B(Z, A) = (Zm_p + Nm_n - m_{nucleus})c^2$$

The **semi-empirical mass formula** (Bethe-Weizsäcker):

$$\boxed{B(Z, A) = a_V A - a_S A^{2/3} - a_C\frac{Z(Z-1)}{A^{1/3}} - a_A\frac{(A-2Z)^2}{A} + \delta(A,Z)}$$

Each term has a transparent physical origin:

|Term|Value|Physical origin|Analogy|
|---|---|---|---|
|Volume: $a_V A$|$a_V = 15.8$ MeV|Each nucleon bonds to its neighbors; binding energy ∝ $A$|Bulk cohesion energy|
|Surface: $-a_S A^{2/3}$|$a_S = 18.3$ MeV|Surface nucleons have fewer bonds; correction ∝ surface area $\propto A^{2/3}$|Surface tension|
|Coulomb: $-a_C Z(Z-1)/A^{1/3}$|$a_C = 0.714$ MeV|Proton-proton repulsion; all pairs interact; $R \propto A^{1/3}$|Electrostatic energy|
|Asymmetry: $-a_A(A-2Z)^2/A$|$a_A = 23.2$ MeV|Pauli exclusion: symmetric filling of $n$ and $p$ levels minimizes energy|Fermi pressure|
|Pairing: $+\delta/\sqrt{A}$|$\delta = \pm 12$ MeV|Paired nucleons are extra stable (like Cooper pairs); $+$ for even-even, $-$ for odd-odd, $0$ for odd $A$|Pairing gap in BCS|

### 6.9.3 — The Binding Energy per Nucleon Curve

Dividing $B(Z, A)$ by $A$ gives binding energy per nucleon, which:

- Rises steeply from $^2$H ($B/A = 1.1$ MeV) to carbon ($B/A \approx 7.7$ MeV)
- Peaks near $^{56}$Fe ($B/A = 8.79$ MeV) — the most stable nucleus
- Decreases slowly from Fe to $^{238}$U ($B/A = 7.6$ MeV)

**This single curve determines all nuclear energy release:**

- **Fusion** ($A < 56$, building toward Fe): joining two light nuclei increases $B/A$ → releases energy. Sun: $4\text{H} \to {}^4\text{He}$, releases $26.7$ MeV per reaction.
- **Fission** ($A > 56$, moving toward Fe): splitting a heavy nucleus increases $B/A$ → releases energy. $^{235}\text{U} + n \to {}^{141}\text{Ba} + {}^{92}\text{Kr} + 3n$, releases $\approx 200$ MeV per fission.

Both processes maximize binding energy per nucleon, approaching Fe from their respective sides of the curve.

---

## 6.10 — Radioactive Decay

### 6.10.1 — Alpha Decay: Tunneling Through the Coulomb Barrier

An $\alpha$ particle ($^4$He nucleus, $Z = 2$, $A = 4$) pre-forms inside a heavy nucleus and tunnels through the Coulomb barrier between the nuclear surface ($r = R$) and the classical turning point ($r = r_c$).

The Gamow tunneling factor (Ch. 4 §4.4, now applied to the Coulomb potential):

$$T_\alpha \propto \exp!\left(-2\int_R^{r_c}\kappa(r),dr\right), \qquad \kappa(r) = \frac{\sqrt{2m_\alpha(V_C(r)-E)}}{\hbar}$$

where $V_C(r) = 2Ze^2/4\pi\epsilon_0 r$ is the daughter-nucleus Coulomb potential. The integral gives the **Gamow factor** $G$:

$$G = \frac{\pi Ze^2}{\hbar v_\alpha}\left(1 - \frac{2}{\pi}\sqrt{\frac{E}{V_C(R)}}\right) \approx \frac{\pi Ze^2}{\hbar v_\alpha}$$

Decay rate: $\lambda \propto f\cdot e^{-2G}$ where $f \approx 10^{21}$ s$^{-1}$ is the assault frequency.

**The Geiger-Nuttall law:** $\log\lambda = C_1 Z/\sqrt{E_\alpha} + C_2$. Alpha emitters spanning 24 orders of magnitude in decay rate obey this relation — from $^{212}$Po ($t_{1/2} = 0.3;\mu$s) to $^{232}$Th ($t_{1/2} = 14$ Gyr). The enormous range comes from the exponential sensitivity of tunneling probability to $E_\alpha$ — a change of $1$ MeV in $\alpha$ energy changes $t_{1/2}$ by $\sim 20$ orders of magnitude.

### 6.10.2 — Beta Decay: The Weak Force at Work

**$\beta^-$ decay:** $n \to p + e^- + \bar\nu_e$ A down quark converts to an up quark via $W^-$ boson emission (Ch. 0 §0.4.3): $d \to u + W^-$, then $W^- \to e^- + \bar\nu_e$.

**$\beta^+$ decay:** $p \to n + e^+ + \nu_e$ (requires $Q > 2m_ec^2$)

**Electron capture:** $p + e^- \to n + \nu_e$

The $Q$-value (energy released): $$Q = (m_{\text{parent}} - m_{\text{daughter}} - m_{\text{emitted}})c^2$$

The electron energy spectrum is continuous (not discrete as in $\alpha$ decay), because the $Q$ is shared between the electron and the neutrino. The maximum electron energy equals $Q$ (when $\nu$ carries no energy).

**Fermi's Golden Rule applied to $\beta$ decay:** The decay rate:

$$\lambda = \frac{G_F^2|M_{fi}|^2}{2\pi^3\hbar^7}(m_ec^2)^5 f(Z, Q)$$

where $G_F$ is the Fermi constant (weak coupling, from $g_2$ in Ch. 0), $|M_{fi}|$ is the nuclear matrix element, and $f(Z, Q)$ is the Fermi function accounting for Coulomb effects on the outgoing electron.

### 6.10.3 — Gamma Decay and the Decay Law

**Gamma decay:** A nucleus in an excited state transitions to a lower state, emitting a $\gamma$ photon. Energies: $0.1$–$10$ MeV. Selection rules from angular momentum conservation determine which transitions are allowed and their rates.

**The radioactive decay law** (any mode):

$$N(t) = N_0,e^{-\lambda t}, \qquad t_{1/2} = \frac{\ln 2}{\lambda}$$

Activity: $A = \lambda N$ (decays per second, unit: Becquerel, 1 Bq = 1 decay/s).

**Decay chains:** A parent decays to a daughter which may itself be unstable, forming a chain. The Bateman equations govern the chain:

$$\frac{dN_i}{dt} = \lambda_{i-1}N_{i-1} - \lambda_i N_i$$

**Engineering:** Geological dating uses isotope ratios (U-Pb, Rb-Sr, K-Ar) measured against the decay law to determine rock ages with precision of $\pm 1%$ over billions of years. Medical nuclear imaging uses short-lived isotopes ($^{99m}$Tc, $t_{1/2} = 6$ h; $^{18}$F, $t_{1/2} = 110$ min).

---

## 6.11 — Nuclear Fission and Fusion

### 6.11.1 — Fission: The Liquid Drop Model

The binding energy formula (§6.9.2) predicts the **fission barrier**. When a $^{235}$U nucleus deforms from a sphere to a prolate ellipsoid:

- Surface energy increases (larger area → less stable)
- Coulomb energy decreases (charges further apart → more stable)

At small deformation: surface term wins → nucleus is stable (barrier exists). At large deformation: Coulomb term wins → nucleus splits.

The **fission barrier height** $E_b$:

$$E_b \approx a_S A^{2/3} - \frac{3}{5}\frac{e^2 Z^2}{4\pi\epsilon_0 R}$$

The fissility parameter $x = E_C/2E_S = Z^2/50.9A$ determines whether spontaneous fission can occur. For $x > 1$ ($Z^2/A > 50.9$): no barrier, spontaneous fission. $^{235}$U has $x \approx 0.77$ — a barrier of $\approx 6$ MeV.

A slow neutron absorbed by $^{235}$U provides $\sim 6.5$ MeV of excitation (neutron binding energy in $^{236}$U) — just enough to cross the barrier. This is why $^{235}$U is fissile with thermal neutrons while $^{238}$U is not (its fission barrier is $\sim 1$ MeV higher than the excitation energy from neutron capture).

**Chain reaction criticality:** Each fission releases $\nu \approx 2.4$ neutrons. Define:

- $k_{eff}$: average number of neutrons from one fission that cause the next fission
- $k_{eff} < 1$: subcritical (dies out)
- $k_{eff} = 1$: critical (sustained chain reaction — nuclear reactor)
- $k_{eff} > 1$: supercritical (exponentially growing — weapon)

The four-factor formula for a large reactor: $k_{eff} = \eta f p \varepsilon$ where:

- $\eta$: neutrons produced per neutron absorbed in fuel
- $f$: fraction absorbed in fuel vs. moderator
- $p$: resonance escape probability
- $\varepsilon$: fast fission factor

### 6.11.2 — Fusion: The Gamow Peak

For two nuclei to fuse, they must overcome the Coulomb barrier: $V_C = Z_1 Z_2 e^2/4\pi\epsilon_0 r$ (at nuclear contact radius $r \approx 2$ fm for D-T: $V_C \approx 0.36$ MeV).

The thermal energy in a plasma at $T$: $\langle E\rangle = \frac{3}{2}k_BT$. Achieving $\langle E\rangle > V_C$ would require $T > 10^{10}$ K — far above stellar core temperatures ($\sim 10^7$ K for the Sun).

**The resolution is quantum tunneling (Ch. 4 §4.4):** Even at $kT \ll V_C$, particles in the high-energy tail of the Maxwell-Boltzmann distribution can tunnel. The reaction rate involves:

$$\sigma(E)v \propto e^{-2\pi\eta}\times e^{-E/k_BT}$$

where $e^{-2\pi\eta}$ is the Gamow tunneling factor and $e^{-E/k_BT}$ is the Maxwell-Boltzmann weight. The product peaks at the **Gamow peak energy**:

$$E_0 = \left(\frac{\pi\alpha Z_1 Z_2 m_r c^2}{2^{1/2}}\right)^{2/3}(k_BT)^{2/3}$$

For D-T fusion at $k_BT = 10$ keV ($T \approx 10^8$ K): $E_0 \approx 64$ keV — in the tail of the Maxwell-Boltzmann distribution but exponentially enhanced by tunneling.

The D-T reaction ($^2$H + $^3$H $\to$ $^4$He + $n$ + 17.6 MeV) is the most practical fusion reaction due to its low Gamow peak energy and high cross-section. ITER (International Thermonuclear Experimental Reactor) targets $Q \geq 10$ (energy out/energy in $\geq 10$).

---

## 6.12 — Summary

Layer 1 is now complete. The tools assembled:

|From Ch. 4|From Ch. 5|From Ch. 6|
|---|---|---|
|Wavefunctions $\psi_{n\ell m}$|Spin $m_s$|Bloch states $\psi_{n\mathbf{k}}$|
|Quantization by BCs|Pauli exclusion from Ch. 0|Band structure $E_n(\mathbf{k})$|
|Hydrogen atom solution|Periodic table|Metal/SC/insulator distinction|
|Tunneling coefficient $T \propto e^{-2\kappa d}$|Fine structure (FW)|Fission barrier; Gamow peak|
|Uncertainty principle|Zeeman effect|Phonons; $\rho \propto T$ in metals|

**Engineering threads from Ch. 6:**

|Physics|Application|
|---|---|
|Band structure + Fermi level|Every semiconductor device (transistors, LEDs, solar cells)|
|Effective mass $m^*$|Carrier mobility → device speed|
|Direct vs. indirect gap|LEDs and lasers vs. transistors; material selection|
|Doping (n-type, p-type)|p-n junction, MOSFET, BJT|
|Phonon thermal conductivity|Heat sink design; thermoelectrics; CPU cooling|
|$\rho \propto T$ (electron-phonon)|RTD temperature sensors; conductor loss|
|Ionic bonding|Ceramic insulators; fuel cell electrolytes|
|vdW bonding|Graphene exfoliation; 2D materials; MEMS stiction|
|Nuclear binding energy curve|Nuclear reactor fuel selection; fusion energy|
|Radioactive decay law|Nuclear waste management; medical imaging; geological dating|
|Gamow tunneling|$\alpha$-decay rates; fusion cross-sections; tunnel diode design|

---

## 6.13 — Looking Ahead: Chapter 7

Chapter 6 treated electrons as if their quantum numbers were $(n, \mathbf{k}, s)$ with well-defined energies $E_n(\mathbf{k})$ — a single-particle picture. Chapter 7 asks what happens when the bands themselves carry topological invariants, when electron-electron interactions are strong, or when quantum phase coherence extends over macroscopic distances.

The results: the quantum Hall effect, topological insulators, Weyl semimetals, and superconductivity. These are not exotic additions to band theory — they are what band theory becomes when you stop ignoring topology.

---

_End of Chapter 6._

---

_Next: Chapter 7 — Topology, Quantum Hall Effect, and Superconductivity_