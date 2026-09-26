# Spin, Many-Electron Systems, and the Periodic Table

### From One Electron to All of Chemistry

---

> _Pauli's exclusion principle is what prevents your hand from going through a table._ _It is not the electromagnetic repulsion of electrons — it is the antisymmetry_ _of their wavefunction._ — common observation among condensed matter physicists

---

## 5.0 — Where We Are

Chapter 4 solved the hydrogen atom exactly and derived three quantum numbers $(n, \ell, m)$. The solution depended on one simplification: a single electron.

Two things were left aside in Chapter 4 that this chapter now restores:

**First:** The electron has spin. It was derived from the Dirac equation in Ch. 3 and placed in the Pauli equation, but then suppressed when we descended further to the Schrödinger equation. Spin generates a fourth quantum number $m_s$, is responsible for fine structure, the Zeeman effect, and magnetic resonance.

**Second:** Real atoms have more than one electron. Adding a second electron immediately makes the Schrödinger equation impossible to solve exactly — but a single additional principle (the Pauli exclusion principle, traceable to Ch. 0's anticommutation relations) is enough to determine the structure of every atom in the periodic table without solving anything exactly.

By the end of this chapter, the periodic table is not a memorization exercise. It is a theorem.

---

## 5.1 — Spin: The Fourth Quantum Number

### 5.1.1 — Where Spin Comes From

In Ch. 3 §3.4.1, spin fell out of the Dirac equation automatically. The four-component Dirac spinor contains two spin degrees of freedom per particle as a mathematical consequence of requiring a first-order, Lorentz-covariant wave equation consistent with the Clifford algebra ${\gamma^\mu, \gamma^\nu} = 2g^{\mu\nu}$.

Spin is not the electron physically rotating — an electron is a point particle with no size, so "spinning" is meaningless classically. Spin is an intrinsic angular momentum with no classical analog, forced into existence by relativistic quantum mechanics.

### 5.1.2 — Spin Operators

The spin operator $\hat{\mathbf{S}}$ satisfies the same algebra as orbital angular momentum $\hat{\mathbf{L}}$:

$$[\hat S_x, \hat S_y] = i\hbar\hat S_z, \quad [\hat S_y, \hat S_z] = i\hbar\hat S_x, \quad [\hat S_z, \hat S_x] = i\hbar\hat S_y$$

The eigenvalues of $\hat S^2$ and $\hat S_z$:

$$\hat S^2,\chi = s(s+1)\hbar^2,\chi, \qquad \hat S_z,\chi = m_s\hbar,\chi$$

For the electron: $s = \frac{1}{2}$ (a fixed intrinsic property), so:

$$\hat S^2,\chi = \frac{3}{4}\hbar^2,\chi, \qquad m_s = \pm\frac{1}{2}$$

There are exactly two spin states. In the Pauli equation (Ch. 3 §3.6), they are represented by two-component **spinors**:

$$\chi_+ = \begin{pmatrix}1\0\end{pmatrix} \equiv \uparrow \quad\text{(spin-up, }m_s = +\tfrac{1}{2}\text{)}$$ $$\chi_- = \begin{pmatrix}0\1\end{pmatrix} \equiv \downarrow \quad\text{(spin-down, }m_s = -\tfrac{1}{2}\text{)}$$

In terms of the Pauli matrices (which appeared in the FW transformation of Ch. 3):

$$\hat{\mathbf{S}} = \frac{\hbar}{2}\boldsymbol{\sigma} = \frac{\hbar}{2}\begin{pmatrix}\sigma_x\\sigma_y\\sigma_z\end{pmatrix}$$

### 5.1.3 — The Stern-Gerlach Experiment: Spin Made Visible

In 1922, Otto Stern and Walther Gerlach sent a beam of silver atoms through an inhomogeneous magnetic field. Classically, a magnetic dipole in a field gradient experiences a force $F_z = \mu_z,\partial B_z/\partial z$; if the orientation of the magnetic moment is continuous, the beam should spread into a continuous smear on the detector.

Instead: two discrete spots appeared.

Silver has the electronic configuration $[\text{Kr}],4d^{10},5s^1$ — one unpaired electron with zero orbital angular momentum ($\ell = 0$) and spin $s = 1/2$. The magnetic moment is purely from spin. The two spots correspond to $m_s = +1/2$ and $m_s = -1/2$, separated by:

$$\Delta z = \frac{\mu_B}{m_{\text{atom}}v^2}\frac{\partial B_z}{\partial z}L_{\text{field}}$$

This experiment directly measures spin quantization. The discreteness is not a resolution limit — it is forced by the eigenvalue equation $\hat S_z\chi = m_s\hbar\chi$.

**Engineering connection:** The Stern-Gerlach principle is the basis of atomic beam frequency standards. The cesium atomic clock — which defines the SI second — uses a magnetic state selector that works exactly like a Stern-Gerlach apparatus, selecting the $m_s = 0$ hyperfine transition to define $1,\text{s} \equiv 9{,}192{,}631{,}770$ periods.

### 5.1.4 — The Complete Hydrogen Quantum Numbers

Adding spin, the complete state of the electron in hydrogen is:

$$\psi_{n\ell m m_s}(\mathbf{r}) = \psi_{n\ell m}(\mathbf{r}),\chi_{m_s}$$

Four quantum numbers, four constraints:

|Quantum number|Symbol|Values|Constraint origin|
|---|---|---|---|
|Principal|$n$|$1, 2, 3, \ldots$|Normalizability of radial equation|
|Orbital|$\ell$|$0, 1, \ldots, n-1$|Finiteness at $r = 0$|
|Magnetic|$m$|$-\ell, \ldots, +\ell$|Single-valuedness in $\phi$|
|Spin|$m_s$|$+\frac{1}{2},,-\frac{1}{2}$|Dirac equation (Ch. 3 §3.4.1)|

The degeneracy of level $n$ including spin: $2n^2$.

---

## 5.2 — Many-Electron Atoms: The Antisymmetry Requirement

### 5.2.1 — Why the Two-Electron Problem Has No Exact Solution

For helium (two electrons at positions $\mathbf{r}_1$ and $\mathbf{r}_2$):

$$\hat H = \underbrace{-\frac{\hbar^2}{2m_e}\nabla_1^2 - \frac{Ze^2}{4\pi\epsilon_0 r_1}}_{\text{electron 1 alone}} + \underbrace{-\frac{\hbar^2}{2m_e}\nabla_2^2 - \frac{Ze^2}{4\pi\epsilon_0 r_2}}_{\text{electron 2 alone}} + \underbrace{\frac{e^2}{4\pi\epsilon_0|\mathbf{r}_1 - \mathbf{r}_2|}}_{\text{electron-electron repulsion}}$$

The first two terms would be exactly solvable — two independent hydrogen-like problems. The last term, the electron-electron repulsion, couples the two coordinates and makes the problem analytically intractable. This is the quantum mechanical three-body problem.

**There is no exact closed-form solution for helium or any atom with $Z > 1$.**

Yet we can determine the structure of every atom in the periodic table. The key is a principle, not a solution.

### 5.2.2 — The Pauli Exclusion Principle: Its True Origin

From Ch. 0 §0.5: the fermion field $\psi$ satisfies **anticommutation relations**:

$${\hat\psi(\mathbf{r}), \hat\psi^\dagger(\mathbf{r}')} = \delta^3(\mathbf{r} - \mathbf{r}')$$

This is not put in by hand. It is required by Lorentz invariance and causality for half-integer spin fields (the spin-statistics theorem, Ch. 0 §0.5).

The consequence for many-electron wavefunctions: swapping any two identical electrons must change the sign of the wavefunction:

$$\Psi(\ldots, \mathbf{x}_i, \ldots, \mathbf{x}_j, \ldots) = -\Psi(\ldots, \mathbf{x}_j, \ldots, \mathbf{x}_i, \ldots)$$

where $\mathbf{x} = (\mathbf{r}, m_s)$ denotes both spatial and spin coordinates. This is **antisymmetry** — the full meaning of the Pauli exclusion principle.

**Immediate corollary:** If two electrons have identical quantum numbers ($\mathbf{x}_i = \mathbf{x}_j$), then swapping them gives:

$$\Psi = -\Psi \qquad\Longrightarrow\qquad \Psi = 0$$

A wavefunction that is identically zero means the probability of that configuration is exactly zero. **Two electrons cannot occupy the same quantum state.** This is the Pauli exclusion principle — a theorem, not a postulate.

### 5.2.3 — The Slater Determinant

The correct antisymmetric wavefunction for $N$ electrons, each occupying a single-particle state $\phi_i$, is:

$$\Psi(\mathbf{x}_1, \ldots, \mathbf{x}_N) = \frac{1}{\sqrt{N!}} \begin{vmatrix} \phi_1(\mathbf{x}_1) & \phi_1(\mathbf{x}_2) & \cdots & \phi_1(\mathbf{x}_N) \ \phi_2(\mathbf{x}_1) & \phi_2(\mathbf{x}_2) & \cdots & \phi_2(\mathbf{x}_N) \ \vdots & \vdots & \ddots & \vdots \ \phi_N(\mathbf{x}_1) & \phi_N(\mathbf{x}_2) & \cdots & \phi_N(\mathbf{x}_N) \end{vmatrix}$$

This is the **Slater determinant**. Its key properties:

- Swapping two columns (= two electrons) changes the sign of the determinant ✓
- If two rows are identical (= two electrons in the same state), the determinant is zero ✓

The Slater determinant is not the exact wavefunction of a real atom — it neglects correlation between electron positions. But it is the correct starting point for the Hartree-Fock mean-field theory and for density functional theory (DFT), both of which are the workhorses of computational chemistry and materials simulation.

---

## 5.3 — Screening and the Lifting of Hydrogen's Degeneracy

In hydrogen, the energy depends only on $n$ — all states with the same $n$ are degenerate regardless of $\ell$. In multi-electron atoms, this degeneracy is lifted. The reason is **screening**.

### 5.3.1 — The Effective Nuclear Charge

Inner electrons partially shield the outer electrons from the full nuclear charge $Z$. An electron in orbital $n\ell$ sees an **effective nuclear charge**:

$$Z_{\text{eff}} = Z - \sigma_{n\ell}$$

where $\sigma_{n\ell}$ is the **screening constant** — the amount of nuclear charge shielded by inner electrons. Slater's rules give approximate values.

The energy of a state in a multi-electron atom is approximately:

$$E_{n\ell} \approx -\frac{Z_{\text{eff}}^2 \times 13.6;\text{eV}}{n^2}$$

### 5.3.2 — Why $2s$ Has Lower Energy Than $2p$

For $\ell = 0$ (s-states), the radial wavefunction has nonzero probability at the nucleus ($|\psi_{n00}(0)|^2 > 0$). An $s$-electron "penetrates" to the nucleus and is not fully shielded — it sees a larger $Z_{\text{eff}}$ and has lower (more negative) energy.

For $\ell > 0$ (p, d, f-states), the centrifugal barrier $\hbar^2\ell(\ell+1)/2m_er^2$ in the effective potential keeps the electron further from the nucleus. A $p$-electron is more effectively screened and has higher energy.

**The energy ordering in multi-electron atoms:** $$E_{ns} < E_{np} < E_{nd} < E_{nf} \quad\text{(for the same }n\text{)}$$

This splitting of energies within a shell is what makes the periodic table non-trivial. In hydrogen, $2s$ and $2p$ are degenerate. In lithium, $2s$ is significantly lower than $2p$ — which is why lithium's third electron goes into $2s$, not $2p$.

---

## 5.4 — Building the Periodic Table: Aufbau and Hund

### 5.4.1 — The Aufbau Principle

Fill orbitals from lowest to highest energy, subject to:

- Pauli exclusion: at most 2 electrons per orbital (one spin-up, one spin-down)
- Hund's first rule (below)

The energy ordering of orbitals in multi-electron atoms: $$1s \to 2s \to 2p \to 3s \to 3p \to 4s \to 3d \to 4p \to 5s \to 4d \to 5p \to \cdots$$

**Why does $4s$ fill before $3d$?** Although $n = 3$ is closer to the nucleus, the $3d$ wavefunction has high angular momentum ($\ell = 2$), is pushed outward by the centrifugal barrier, and is well-screened. The $4s$ wavefunction ($\ell = 0$) penetrates the core and sees a large $Z_{\text{eff}}$, making its energy lower than $3d$ for elements from K to Zn.

### 5.4.2 — Hund's Rules

For a partially filled subshell (multiple electrons in orbitals with the same $n$ and $\ell$):

**Rule 1 (most important):** Maximize total spin $S$. Electrons singly occupy orbitals before doubling up, with parallel spins.

**Rule 2:** For the same $S$, maximize total orbital angular momentum $L$.

**Rule 3:** For less-than-half-filled subshells, $J = |L-S|$; for more-than-half, $J = L+S$.

**Why Rule 1?** Two electrons with parallel spins must have different spatial wavefunctions (Pauli exclusion). This spatial antisymmetry keeps them further apart, reducing their Coulomb repulsion energy — so parallel spins are energetically preferred. This is the **exchange interaction** — a purely quantum effect with no classical analog.

**Example: Carbon** ($Z = 6$, configuration $1s^22s^22p^2$): The two $2p$ electrons have $\ell = 1$ with three $m$ values $(-1, 0, +1)$. By Hund's Rule 1, both occupy different $m$ values with parallel spins: $m = 0, m_s = +\frac{1}{2}$ and $m = +1, m_s = +\frac{1}{2}$. Ground state: $^3P_0$.

### 5.4.3 — Period-by-Period Construction

**Period 1** ($n = 1$ shell, capacity 2):

|$Z$|Element|Configuration|Notes|
|---|---|---|---|
|1|H|$1s^1$|One unpaired electron|
|2|He|$1s^2$|First noble gas; $1s$ shell complete|

---

**Period 2** ($n = 2$ shell, capacity 8):

|$Z$|Element|Configuration|Chemical character|
|---|---|---|---|
|3|Li|$[\text{He}]2s^1$|Alkali metal; easily loses $2s$ electron|
|4|Be|$[\text{He}]2s^2$|Alkaline earth|
|5|B|$[\text{He}]2s^22p^1$|First $p$-block element|
|6|C|$[\text{He}]2s^22p^2$|Four valence electrons; basis of organic chemistry|
|7|N|$[\text{He}]2s^22p^3$|Half-filled $2p$ (Hund maximum); very stable|
|8|O|$[\text{He}]2s^22p^4$|Two unpaired $p$ electrons; highly reactive|
|9|F|$[\text{He}]2s^22p^5$|One electron short of noble gas; most electronegative|
|10|Ne|$[\text{He}]2s^22p^6$|Noble gas; $2p$ complete|

---

**Period 3** ($n = 3$ shell, $3s$ and $3p$ only — $3d$ doesn't fill yet):

|$Z$|Element|Config|Notes|
|---|---|---|---|
|11|Na|$[\text{Ne}]3s^1$|Alkali; analogue of Li|
|14|Si|$[\text{Ne}]3s^23p^2$|Semiconductor; same valence structure as C|
|18|Ar|$[\text{Ne}]3s^23p^6$|Noble gas|

---

**Period 4** ($4s$ fills first, then $3d$ transition metals, then $4p$):

|Range|Elements|Notes|
|---|---|---|
|$Z = 19, 20$|K, Ca|$4s^1$, $4s^2$ — fill $4s$ before $3d$|
|$Z = 21$–$30$|Sc–Zn|$3d$ transition metals; magnetic properties from partially filled $3d$|
|$Z = 31$–$36$|Ga–Kr|Fill $4p$; Kr is next noble gas|

The 10 transition metals (Sc through Zn) arise from filling the 5 $3d$ orbitals. Their chemical and magnetic properties (ferromagnetism in Fe, Co, Ni; catalytic activity of transition metals) all trace back to unpaired $3d$ electrons and the Hund's Rule exchange interaction.

### 5.4.4 — Periodic Trends

Three key properties vary systematically across the table, all explained by screening and orbital filling:

**Atomic radius:** Decreases across a period (increasing $Z_{\text{eff}}$ pulls electrons inward), increases down a group (larger $n$ → larger orbitals). This determines bond lengths, ionic sizes, and crystal structure.

**Ionization energy:** Energy to remove the outermost electron. Increases across a period (larger $Z_{\text{eff}}$ → harder to remove). Noble gases have the highest ionization energies; alkali metals the lowest. This determines electrochemical series, corrosion behavior, and semiconductor doping character.

**Electronegativity:** Tendency to attract electrons in a bond. Increases across a period and up a group. F is the most electronegative; Cs the least. Electronegativity differences determine bond polarity, solubility, and surface chemistry.

**Engineering consequence:** Every materials selection decision in EEE, ME, CE, and ChE ultimately traces back to these three properties and the electronic configurations that produce them. Copper's high conductivity comes from its $3d^{10}4s^1$ configuration giving a half-filled $4s$ band. Silicon's semiconductor behavior comes from its four-valence-electron $3s^23p^2$ configuration. Steel's properties are those of iron ($3d^64s^2$) modified by carbon occupying interstitial sites.

---

## 5.5 — Fine Structure: Spin-Orbit Coupling

In Ch. 3 §3.5.3, the Foldy-Wouthuysen transformation at order $(v/c)^2$ gave — among other terms — the spin-orbit coupling:

$$\hat H_{SO} = -\frac{e\hbar}{4m_e^2c^2}\boldsymbol{\sigma}\cdot(\mathbf{E}\times\hat{\mathbf{p}})$$

For the Coulomb field of the nucleus, $\mathbf{E} = (e/4\pi\epsilon_0r^3)\mathbf{r}$, this becomes:

$$\boxed{\hat H_{SO} = \frac{1}{2m_e^2c^2}\frac{1}{r}\frac{dV}{dr}\hat{\mathbf{L}}\cdot\hat{\mathbf{S}} \equiv \xi(r)\hat{\mathbf{L}}\cdot\hat{\mathbf{S}}}$$

where the factor of $\frac{1}{2}$ is the **Thomas precession correction** (a relativistic kinematic effect).

### 5.5.1 — Physical Picture

An electron moving through the electric field $\mathbf{E}$ of the nucleus sees, in its own rest frame, a magnetic field:

$$\mathbf{B}_{\text{eff}} \approx -\frac{\mathbf{v}\times\mathbf{E}}{c^2}$$

The electron's spin magnetic moment $\boldsymbol{\mu}_S = -g_e\mu_B\mathbf{S}/\hbar$ (with $g_e = 2$ from the Dirac equation) interacts with this effective field. **The spin-orbit coupling is the magnetic moment of the electron interacting with the magnetic field it experiences due to its own orbital motion.** The coupling strength is $\propto (v/c)^2 \propto \alpha^2$, which is why it is a fine structure correction.

### 5.5.2 — Total Angular Momentum $J$

Because $\hat H_{SO} = \xi(r)\hat{\mathbf{L}}\cdot\hat{\mathbf{S}}$ couples $\mathbf{L}$ and $\mathbf{S}$, neither $L_z$ nor $S_z$ is individually conserved. What is conserved is the **total angular momentum**:

$$\hat{\mathbf{J}} = \hat{\mathbf{L}} + \hat{\mathbf{S}}$$

Using $\hat{\mathbf{L}}\cdot\hat{\mathbf{S}} = \frac{1}{2}(\hat J^2 - \hat L^2 - \hat S^2)$:

$$\hat H_{SO} = \frac{\xi(r)}{2}\left(\hat J^2 - \hat L^2 - \hat S^2\right)$$

The energy shift from spin-orbit coupling in hydrogen (first-order perturbation theory):

$$\boxed{E_{SO} = \frac{\xi_{n\ell}}{2}\hbar^2\left[j(j+1) - \ell(\ell+1) - s(s+1)\right]}$$

where $\xi_{n\ell} = \langle n\ell|\xi(r)|n\ell\rangle$ and $j = \ell \pm \frac{1}{2}$.

### 5.5.3 — The $j$ Quantum Number

For an electron with orbital quantum number $\ell$ and spin $s = \frac{1}{2}$:

$$j = \ell + \frac{1}{2} \quad\text{or}\quad j = \ell - \frac{1}{2} \quad(\text{for }\ell \geq 1)$$

For $\ell = 0$: only $j = \frac{1}{2}$ (spin and orbital don't couple when there's no orbital angular momentum).

Each $j$ value gives a different energy — the spin-orbit coupling **splits the $\ell > 0$ levels into doublets**:

$$\Delta E_{SO} = E_{j=\ell+1/2} - E_{j=\ell-1/2} = \frac{\xi_{n\ell}}{2}\hbar^2(2\ell + 1)$$

This is the **fine structure** of the spectral lines.

### 5.5.4 — Spectroscopic Term Symbols

The state of a single electron is specified by $(n, \ell, j)$ using the notation:

$$n,^{2s+1}L_j$$

where $L = s, p, d, f, \ldots$ for $\ell = 0, 1, 2, 3, \ldots$ and $2s+1$ is the spin multiplicity (2 for one electron, since $s = 1/2$).

|State|$n$|$\ell$|$j$|Term|Energy relative to ground|
|---|---|---|---|---|---|
|Hydrogen 2p|2|1|1/2|$2,^2P_{1/2}$|$E_2 + E_{SO}(j=1/2)$|
|Hydrogen 2p|2|1|3/2|$2,^2P_{3/2}$|$E_2 + E_{SO}(j=3/2)$|

The splitting between $2,^2P_{1/2}$ and $2,^2P_{3/2}$ in hydrogen is $\Delta E = 4.53 \times 10^{-5}$ eV — tiny but precisely measurable and exactly matching the FW prediction from Ch. 3.

---

## 5.6 — The Zeeman Effect: Spin Included

### 5.6.1 — Interaction with an External Field

Adding an external magnetic field $\mathbf{B}$ along $\hat z$, the perturbation Hamiltonian is:

$$\hat H_Z = -\hat{\boldsymbol{\mu}}\cdot\mathbf{B} = \frac{e}{2m_e}\left(\hat{\mathbf{L}} + 2\hat{\mathbf{S}}\right)\cdot\mathbf{B} = \frac{e B}{2m_e}\left(\hat L_z + 2\hat S_z\right)$$

The factor of 2 in front of $\hat S_z$ is $g_e = 2$ from the Dirac equation (Ch. 3 §3.4.2) — not put in by hand.

### 5.6.2 — Weak Field: The Anomalous Zeeman Effect

For $B$ weak enough that $\hat H_Z \ll \hat H_{SO}$, the spin-orbit coupling dominates and $\mathbf{J} = \mathbf{L} + \mathbf{S}$ is a good quantum number. The energy shift is:

$$\Delta E = g_J \mu_B B m_J$$

where $\mu_B = e\hbar/2m_e = 9.274 \times 10^{-24}$ J/T is the **Bohr magneton**, and $g_J$ is the **Landé g-factor**:

$$\boxed{g_J = 1 + \frac{j(j+1) + s(s+1) - \ell(\ell+1)}{2j(j+1)}}$$

This gives $g_J = 1$ for purely orbital states (S = 0) and $g_J = 2$ for purely spin states ($\ell = 0$), consistent with Ch. 3.

**Why it was called "anomalous":** Before spin was understood, the factor of 2 for spin was mysterious. It seemed as if the electron's magnetism was "anomalous." After the Dirac equation explained $g_e = 2$, it became simply the Landé formula. Nothing about it is anomalous — it is an exact consequence of quantum mechanics.

### 5.6.3 — Strong Field: The Paschen-Back Effect

For $B$ large enough that $\hat H_Z \gg \hat H_{SO}$, the external field decouples $\mathbf{L}$ and $\mathbf{S}$ from each other; both couple independently to $\mathbf{B}$:

$$\Delta E = \mu_B B(m_\ell + 2m_s)$$

The Paschen-Back regime shows that $\mathbf{J}$ is not fundamental — it is the good quantum number only when spin-orbit coupling dominates. In strong fields, $m_\ell$ and $m_s$ are separately conserved (separately good quantum numbers).

**Engineering connection — NMR and MRI:** The Zeeman effect is the foundation of NMR and MRI. A nucleus with spin $I$ (e.g., $^1$H has $I = 1/2$, $^{13}$C has $I = 1/2$) in a magnetic field $B_0$ has energy levels split by:

$$\Delta E = \gamma_N \hbar B_0$$

where $\gamma_N$ is the **nuclear gyromagnetic ratio**. An RF pulse at the Larmor frequency $\omega_L = \gamma_N B_0$ drives Rabi oscillations between the $m_I$ levels. The free induction decay after the pulse contains structural and chemical information. MRI at 3 T uses $\omega_L = 128$ MHz for protons.

---

## 5.7 — Many-Electron Term Symbols

For atoms with multiple valence electrons, the total $L$, $S$, and $J$ are formed by vector addition of individual angular momenta.

**LS coupling (Russell-Saunders):** Valid for light atoms ($Z \lesssim 30$). Individual spins couple to total $S$; individual orbital moments to total $L$; then $\mathbf{J} = \mathbf{L} + \mathbf{S}$.

**jj coupling:** Valid for heavy atoms ($Z \gtrsim 60$). Each electron's spin and orbital angular momentum couple first (giving individual $j_i$), then these couple to total $J$. Spin-orbit coupling is stronger than electron-electron repulsion.

The ground state term symbol for LS coupling:

$$^{2S+1}L_J$$

where $L = 0, 1, 2, 3, 4, \ldots$ is written as $S, P, D, F, G, \ldots$

**Examples of ground state terms:**

|Atom|Config|$S$|$L$|$J$|Term|Why|
|---|---|---|---|---|---|---|
|H|$1s^1$|1/2|0|1/2|$^2S_{1/2}$|Single $s$ electron|
|He|$1s^2$|0|0|0|$^1S_0$|Paired spins; closed shell|
|C|$2p^2$|1|1|0|$^3P_0$|Hund: max $S$, max $L$, $J = L-S$ (< half-filled)|
|N|$2p^3$|3/2|0|3/2|$^4S_{3/2}$|Half-filled $p$: max $S$; $L=0$ by symmetry|
|O|$2p^4$|1|1|2|$^3P_2$|More than half-filled: $J = L+S$|
|Fe|$3d^6$|2|2|4|$^5D_4$|More than half-filled $d$; $J = L+S$|

Iron ($Z = 26$, $^5D_4$) has 4 unpaired $3d$ electrons giving $S = 2$ — a large magnetic moment of $4\mu_B$. This is why iron is ferromagnetic: sufficiently strong exchange interactions align these large moments macroscopically.

---

## 5.8 — Molecular Bonding: Where Chemistry Begins

The periodic table tells you what each atom wants to do. Molecular bonding tells you what happens when atoms find each other. This section is a preview of Ch. 6, where bonding is treated fully.

### 5.8.1 — Linear Combination of Atomic Orbitals (LCAO)

When two hydrogen atoms approach, their $1s$ wavefunctions overlap. Form linear combinations (the molecular orbital approach):

$$\psi_{\pm} = \frac{1}{\sqrt{2(1\pm S_{AB})}}(\phi_{1s}^A \pm \phi_{1s}^B)$$

where $S_{AB} = \int\phi_{1s}^A\phi_{1s}^B,d^3r$ is the **overlap integral**.

- $\psi_+$ (symmetric, bonding): probability density **between** the nuclei is enhanced — reduces the electron-nuclear distance and lowers energy
- $\psi_-$ (antisymmetric, antibonding): node between the nuclei — electrons are excluded from the internuclear region, raising energy

Energy of the two molecular orbitals:

$$E_{\pm} = E_{1s} \pm \frac{H_{AB} - E_{1s}S_{AB}}{1 \pm S_{AB}}$$

where $H_{AB} = \int\phi_{1s}^A \hat H\phi_{1s}^B,d^3r < 0$ is the resonance integral (negative, so $E_+$ is below $E_{1s}$).

Two electrons (one from each H atom, with opposite spins by Pauli exclusion) both occupy $\psi_+$: total energy is $2E_+ < 2E_{1s}$. The molecule is stable.

This is the covalent bond in H₂ — derived from the same quantum mechanics that gave us the hydrogen atom, using only the Pauli exclusion principle and the variational principle.

### 5.8.2 — Bond Types from Electronic Configuration

The type of molecular orbital formed depends on the symmetry of the atomic orbitals that overlap:

|Overlap type|Orbital|Symmetry|Bond|Example|
|---|---|---|---|---|
|Head-on ($s$-$s$, $s$-$p$, $p_z$-$p_z$)|$\sigma$|Cylindrical around bond axis|Single bond|H-H, C-H|
|Side-on ($p_x$-$p_x$, $p_y$-$p_y$)|$\pi$|Two lobes above/below axis|Part of double/triple bond|C=C, C≡C|
|$d$-$d$|$\delta$|Four-lobed|Metal-metal bonds|Transition metal clusters|

**The double bond** (e.g., ethylene $\text{C}_2\text{H}_4$): one $\sigma$ bond (head-on $p_z$ overlap) + one $\pi$ bond (side-on $p_x$ overlap). The $\pi$ bond is weaker (less overlap) and more reactive.

**The triple bond** (e.g., nitrogen $\text{N}_2$): one $\sigma$ + two $\pi$ bonds. Exceptionally strong — N$_2$ is the most stable diatomic molecule at room temperature, dissociation energy 945 kJ/mol.

### 5.8.3 — Hybridization: Carbon's Flexibility

Carbon ($2s^22p^2$) forms four bonds. But why are all four equivalent in methane ($\text{CH}_4$) if carbon has one $2s$ and two $2p$ electrons? Answer: the $2s$ and three $2p$ orbitals mix to form four equivalent **hybrid orbitals**:

**$sp^3$ hybridization** (methane, diamond): $$\phi_i = \frac{1}{2}(\phi_{2s} \pm \phi_{2p_x} \pm \phi_{2p_y} \pm \phi_{2p_z})$$ Four equivalent orbitals pointing to the corners of a tetrahedron, $109.5°$ apart. This is why diamond (all $sp^3$ C-C bonds) is the hardest natural material.

**$sp^2$ hybridization** (graphene, graphite): Three $sp^2$ hybrids in a plane ($120°$ apart) + one remaining unhybridized $2p_z$. The $2p_z$ orbitals from all carbons overlap to form a delocalized $\pi$ network. This delocalized $\pi$ system gives graphene its extraordinary electrical conductivity (the electrons in the $\pi$ band are nearly free) — and makes it a Dirac semimetal with linear band dispersion (Ch. 7).

**$sp$ hybridization** (acetylene, carbon nanotubes): Two $sp$ hybrids in a line ($180°$ apart) + two unhybridized $p$ orbitals forming two $\pi$ bonds.

**Engineering consequence:** The hybridization of carbon determines everything:

- $sp^3$ → diamond (insulator), polymer chains, organic molecules
- $sp^2$ → graphene, graphite, carbon nanotubes, fullerenes
- Mixed → amorphous carbon, diamond-like carbon (DLC) for hard coatings

---

## 5.9 — Summary

Starting from three things established in earlier chapters:

1. The quantum numbers $(n, \ell, m)$ from Ch. 4
2. Spin ($m_s = \pm\frac{1}{2}$) from the Dirac equation (Ch. 3)
3. Pauli exclusion from anticommutation of fermion fields (Ch. 0)

This chapter derived:

|Result|Derived from|
|---|---|
|Spin quantization|Dirac equation; Stern-Gerlach confirms|
|Pauli exclusion principle|Antisymmetry of fermion wavefunction (Slater determinant)|
|Aufbau orbital filling|Pauli exclusion + energy ordering from screening|
|Hund's rules|Exchange interaction (Pauli + Coulomb repulsion)|
|The periodic table|Aufbau + Hund + 4 quantum numbers|
|Fine structure|FW spin-orbit term (Ch. 3 §3.5.3)|
|Zeeman effect|Minimal coupling to external B; $g_e = 2$ from Dirac|
|Landé g-factor|LS coupling + vector addition of J|
|Covalent bond|LCAO: bonding/antibonding MOs from overlapping wavefunctions|
|Hybridization|Linear combinations of atomic orbitals from same atom|

---

## 5.10 — Engineering Thread

|Physics from this chapter|Engineering application|
|---|---|
|Spin quantization|NMR spectroscopy; MRI imaging; atomic clocks|
|Zeeman effect|Magnetometers; electron spin resonance (ESR) sensors|
|Pauli exclusion|Why metals are stiff; why matter has volume|
|Electronic configurations|Conductors vs. insulators vs. semiconductors (Ch. 6)|
|Transition metal $3d$ electrons|Ferromagnetism in Fe, Co, Ni; hard drives; inductors|
|Electronegativity (from periodic trends)|Battery electrode selection; corrosion engineering; semiconductor doping polarity|
|$sp^3$ carbon bonding|Diamond coatings; polymer chemistry; organic semiconductor design|
|$sp^2$ carbon bonding|Graphene electronics; carbon nanotube interconnects; carbon fiber composites|
|Molecular orbitals|Computational chemistry (DFT) for materials design|

---

## 5.11 — Looking Ahead: Chapter 6

The periodic table gives us the identity of atoms. Chapter 6 asks: what happens when you assemble $\sim 10^{23}$ of them into a solid?

The answer — Bloch's theorem, band theory, and the metal-semiconductor-insulator distinction — is Layer 1's most direct contribution to engineering practice. Every transistor, every conductor, every solar cell depends on what happens when $10^{23}$ atomic wavefunctions from this chapter are made to overlap.

---

_End of Chapter 5._

---

_Next: Chapter 6 — Band Theory, Molecular Bonding, and Nuclear Physics_