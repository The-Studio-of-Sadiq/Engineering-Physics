# Bridge A — The Quantum Descent

### From the Standard Model Lagrangian to the Schrödinger Equation

---

> _The Dirac equation is the most beautiful equation in physics._ _It predicted spin, antimatter, and the fine structure of hydrogen_ _before anyone had asked it to._ — attributed to Paul Dirac (paraphrased)

---

## 3.0 — Where We Are and Where We Are Going

In Chapter 0 you saw the full action. Every term was labeled and every field was named. Now we begin the actual descent.

This chapter performs the first controlled approximation — the one that takes you from quantum field theory (the full action) to single-particle quantum mechanics (the Schrödinger equation). This transition is called **Bridge A** in the layer map of this book.

At the end of this chapter you will have the Schrödinger equation written on your page. But unlike every other physics course, you will know exactly where it came from, what was thrown away to get it, and precisely when you are allowed to use it. That knowledge — not the equation itself — is what this chapter delivers.

**The map of this chapter:**

```
L_SM (Chapter 0)
      │
      │  Step 1: Isolate the U(1)-coupled fermion sector (§3.1)
      │  [discard SU(3) and SU(2): not relevant for electrons in atoms]
      ▼
The Dirac Lagrangian: L = ψ̄(iγᵘDμ - m)ψ
      │
      │  Step 2: Euler-Lagrange equations (§3.2)
      ▼
The Dirac Equation: iγᵘDμψ = mψ        ← Bridge zone (§3.3–3.5)
      │
      │  Step 3: Foldy-Wouthuysen transformation, order (v/c)¹ (§3.6)
      ▼
The Pauli Equation: spin included, relativistic corrections at O(v/c)²
      │
      │  Step 4: Drop spin-field coupling for spinless or B=0 case (§3.7)
      ▼
The Schrödinger Equation: iħ ∂ψ/∂t = [-ħ²∇²/2m + V]ψ    ← Layer 1
```

---

## 3.1 — Isolating the Right Sector

### 3.1.1 — Which Part of $\mathcal{L}_{SM}$ We Are Using

The full Standard Model Lagrangian (Chapter 0) contains three gauge sectors: SU(3)$_C$, SU(2)$_L$, and U(1)$_Y$. For electrons in atoms at energies $E \ll m_W c^2 \approx 80$ GeV:

- **SU(3)$_C$:** Acts only on quarks. Electrons carry no color charge. This sector is completely invisible to electrons. Discard it.
    
- **SU(2)$_L$:** Acts on left-handed fermions and is mediated by $W^\pm$ and $Z^0$ bosons. The interaction strength at atomic energies is suppressed by $G_F E^2/(\hbar c)^3 \approx 10^{-11}$ relative to electromagnetism (where $G_F \approx 1.17\times10^{-5};\text{GeV}^{-2}$ is the Fermi constant and $E \sim 10;\text{eV}$ for an atomic electron). This ratio is $\sim 10^{-22}$ — experimentally undetectable. Discard it.
    
- **U(1)$_{EM}$:** Electromagnetism. After the Higgs mechanism (§0.7), the physical photon $A_\mu$ couples to electrons with charge $-e$. This is the only force relevant for atomic structure.
    

**What we keep:**

$$\mathcal{L}_{electron} = \bar\psi\left(i\gamma^\mu\partial_\mu - m_e - e\gamma^\mu A_\mu\right)\psi$$

where $A_\mu$ is the electromagnetic four-potential ($A_0 = V/c$ is the scalar potential, $\mathbf{A}$ is the vector potential).

Using the shorthand $\not!\partial \equiv \gamma^\mu\partial_\mu$ and $\not!!A \equiv \gamma^\mu A_\mu$:

$$\mathcal{L}_{electron} = \bar\psi\bigl(i\not!\partial - m_e - e\not!!A\bigr)\psi$$

This is the **QED Lagrangian for the electron** — quantum electrodynamics reduced to its matter content. The photon's own kinetic term $-\frac{1}{4}F_{\mu\nu}F^{\mu\nu}$ is still present (it governs the electromagnetic field), but for atomic physics we treat $A_\mu$ as an external, given field rather than a dynamical one.

### 3.1.2 — What We Are Discarding and Why

By treating $A_\mu$ as a classical, external field and working at low energies, we are discarding:

|Discarded|Physical content|Validity|
|---|---|---|
|Full QED vertex corrections|Lamb shift, $g-2$ correction to magnetic moment|Corrections of order $\alpha/\pi \approx 0.002$|
|Virtual pair creation loops|Vacuum polarization, Uehling potential|Order $\alpha^2$ — measurable in precision spectroscopy, negligible in engineering|
|Pair creation processes|$\gamma\gamma \to e^+e^-$, $e^-\to e^-\gamma$|Requires $E \geq 2m_ec^2 = 1.022$ MeV — far above atomic energies|
|Quantization of the EM field|Spontaneous emission, Casimir effect|Included approximately via Einstein A coefficient; full treatment needs QFT|

**The validity criterion for this entire chapter:** $$\boxed{E_{kinetic} \ll m_e c^2 = 0.511;\text{MeV}}$$

For ground-state hydrogen: $E_1 = 13.6;\text{eV} \ll 511{,}000;\text{eV}$. The ratio is $\sim 10^{-5}$. The approximation is excellent.

---

## 3.2 — Euler-Lagrange Descent: The Dirac Equation

### 3.2.1 — Applying the Euler-Lagrange Equations

The equation of motion for $\psi$ is found by varying $\mathcal{L}_{electron}$ with respect to $\bar\psi$ (the Dirac adjoint). The Euler-Lagrange equation for a field is:

$$\frac{\partial\mathcal{L}}{\partial\bar\psi} - \partial_\mu\frac{\partial\mathcal{L}}{\partial(\partial_\mu\bar\psi)} = 0$$

Since $\mathcal{L}_{electron}$ depends on $\bar\psi$ but not on $\partial_\mu\bar\psi$ (the kinetic term $i\bar\psi\gamma^\mu\partial_\mu\psi$ is first-order in $\psi$, not $\bar\psi$), the second term vanishes. The first term gives directly:

$$\boxed{i\gamma^\mu\partial_\mu\psi - m_e\psi - e\gamma^\mu A_\mu\psi = 0}$$

Rearranging, and writing $D_\mu = \partial_\mu + ieA_\mu$ for the covariant derivative:

$$\boxed{i\gamma^\mu D_\mu\psi = m_e\psi}$$

This is the **Dirac equation** — the equation of motion of a spin-1/2 particle in an electromagnetic field, derived directly from the Lagrangian by the Euler-Lagrange procedure. It was not guessed or postulated here; it fell out of the variational principle applied to the fermion sector of the Standard Model.

### 3.2.2 — Restoring $\hbar$ and $c$

In the derivation above, we used natural units ($\hbar = c = 1$). Restoring physical units:

$$\left(i\hbar\gamma^\mu\partial_\mu - \frac{e}{c}\gamma^\mu A_\mu - m_e c\right)\psi = 0$$

Or, separating time and space components ($\mu = 0$: time; $\mu = 1,2,3$: space):

$$\boxed{i\hbar\frac{\partial\psi}{\partial t} = \left[c\boldsymbol{\alpha}\cdot\left(\hat{\mathbf{p}} - \frac{e}{c}\mathbf{A}\right) + \beta m_e c^2 + eV\right]\psi}$$

This is the **Dirac equation in Hamiltonian form**, where:

- $\hat{\mathbf{p}} = -i\hbar\nabla$ is the momentum operator
- $V = A_0$ is the electric scalar potential (with $e > 0$, the electron has charge $-e$)
- $\boldsymbol{\alpha}$ and $\beta$ are $4\times 4$ matrices defined by the gamma matrices

---

## 3.3 — Anatomy of the Dirac Equation

### 3.3.1 — The Gamma Matrices and the Clifford Algebra

The four gamma matrices $\gamma^\mu$ ($\mu = 0,1,2,3$) are $4\times 4$ complex matrices satisfying the **Clifford algebra**:

$${\gamma^\mu, \gamma^\nu} = \gamma^\mu\gamma^\nu + \gamma^\nu\gamma^\mu = 2g^{\mu\nu}\mathbf{1}_{4\times 4}$$

In the **Dirac representation** (standard representation, most transparent for the non-relativistic limit):

$$\gamma^0 = \beta = \begin{pmatrix}\mathbf{1} & 0 \ 0 & -\mathbf{1}\end{pmatrix}, \qquad \gamma^i = \begin{pmatrix}0 & \sigma^i \ -\sigma^i & 0\end{pmatrix}$$

where $\mathbf{1}$ is the $2\times 2$ identity matrix and $\sigma^i$ are the **Pauli matrices**:

$$\sigma^1 = \begin{pmatrix}0&1\1&0\end{pmatrix}, \quad \sigma^2 = \begin{pmatrix}0&-i\i&0\end{pmatrix}, \quad \sigma^3 = \begin{pmatrix}1&0\0&-1\end{pmatrix}$$

The **alpha matrices** $\boldsymbol{\alpha}$ appearing in the Hamiltonian form are:

$$\boldsymbol{\alpha} = \gamma^0\boldsymbol{\gamma} = \begin{pmatrix}0 & \boldsymbol{\sigma}\\boldsymbol{\sigma} & 0\end{pmatrix}$$

### 3.3.2 — The Four-Component Spinor

The field $\psi$ is a **Dirac spinor** — a four-component complex column vector:

$$\psi = \begin{pmatrix}\phi \ \chi\end{pmatrix}$$

In the non-relativistic limit, it will be shown (§3.5) that:

- $\phi$: two-component **large component** — survives as the physical electron wavefunction
- $\chi$: two-component **small component** — magnitude suppressed by $(v/c)$ relative to $\phi$; encodes relativistic corrections and the positron (antimatter) degree of freedom

The four components are not four spatial dimensions. They encode spin (up/down — two components) and particle/antiparticle (electron/positron — two more). The Lorentz group requires four dimensions for a consistent relativistic description of spin-1/2.

### 3.3.3 — The Dirac Hamiltonian

Write the Dirac equation in the form $i\hbar,\partial_t\psi = \hat H_{Dirac}\psi$:

$$\hat H_{Dirac} = \begin{pmatrix} m_e c^2 + eV & c,\boldsymbol{\sigma}\cdot\hat{\mathbf{\pi}} \ c,\boldsymbol{\sigma}\cdot\hat{\mathbf{\pi}} & -m_e c^2 + eV \end{pmatrix}$$

where $\hat{\mathbf{\pi}} = \hat{\mathbf{p}} - \frac{e}{c}\mathbf{A}$ is the **kinetic momentum** (canonical momentum minus gauge contribution).

The diagonal blocks:

- Upper-left $m_ec^2 + eV$: rest mass energy plus potential — the electron block
- Lower-right $-m_ec^2 + eV$: negative rest mass energy — the positron block

The off-diagonal blocks $c,\boldsymbol{\sigma}\cdot\hat{\mathbf{\pi}}$ couple electrons and positrons. This coupling is what makes the Dirac equation an inherently relativistic, multi-particle object — and what must be systematically removed to reach the Schrödinger equation.

---

## 3.4 — What the Dirac Equation Predicts Without Additional Assumptions

Before we descend to the Schrödinger equation, it is worth pausing to appreciate what the Dirac equation gives us **automatically** — with no extra postulates:

### 3.4.1 — Spin-1/2

The Dirac spinor automatically has two spin degrees of freedom per particle (the two components of $\phi$). The spin operator:

$$\hat{\mathbf{S}} = \frac{\hbar}{2}\begin{pmatrix}\boldsymbol{\sigma}&0\0&\boldsymbol{\sigma}\end{pmatrix}$$

falls directly from the spinor structure. It satisfies $\hat S^2 = \frac{3}{4}\hbar^2$, confirming spin-$\frac{1}{2}$.

**Nobody put spin into the Dirac equation.** It is there because the Lorentz group, when acting on a four-component field, has spin-$\frac{1}{2}$ built into its representation theory. The Clifford algebra ${\gamma^\mu,\gamma^\nu} = 2g^{\mu\nu}$ is the minimal algebraic structure consistent with a first-order, Lorentz-covariant wave equation — and it forces spin-$\frac{1}{2}$ as a consequence.

### 3.4.2 — The Magnetic Moment: $g = 2$

For an electron in a magnetic field $\mathbf{B}$, the Dirac equation contains an interaction term: $$\hat H_{mag} = -\frac{e\hbar}{2m_ec}\boldsymbol{\sigma}\cdot\mathbf{B} = -g_e\frac{e}{2m_ec}\hat{\mathbf{S}}\cdot\mathbf{B}$$

This gives $g_e = 2$ exactly — the electron has twice the magnetic moment you would expect from classical orbital motion. This was a mysterious experimental result before 1928. The Dirac equation explains it with no fitting: $g = 2$ is a mathematical consequence of the Clifford algebra.

(The small departure from exactly 2, $g_e = 2.00231930...$, is the QED correction — the Lamb-shift-era legacy, discarded in §3.1.2 as $\alpha/\pi$.)

### 3.4.3 — Antimatter

The negative-energy solutions of the Dirac equation — the lower two components becoming large for solutions with energy $E \approx -m_ec^2$ — were initially puzzling. Dirac interpreted them in 1930 as **positrons**: the antiparticle of the electron with the same mass and opposite charge.

The positron was discovered by Anderson in 1932. It was the first antiparticle ever found — predicted by the formalism, not hypothesized by experiment.

### 3.4.4 — Fine Structure of Hydrogen

Without any modification, the Dirac equation applied to the hydrogen atom (Coulomb potential $V = -e^2/r$) gives energy levels:

$$E_{nj} = m_ec^2\left(1 + \left(\frac{\alpha}{n - j - \frac{1}{2} + \sqrt{(j+\frac{1}{2})^2 - \alpha^2}}\right)^2\right)^{-1/2}$$

Expanding in $\alpha^2$ (where $\alpha = e^2/\hbar c \approx 1/137$ is the fine structure constant):

$$E_{nj} \approx -\frac{m_ec^2\alpha^2}{2n^2}\left(1 + \frac{\alpha^2}{n}\left(\frac{1}{j+\frac{1}{2}} - \frac{3}{4n}\right)\right)$$

The first term is the Bohr energy $-13.6/n^2;\text{eV}$. The second term — the **fine structure correction** — splits energy levels with the same $n$ but different $j$ (total angular momentum). This splitting is observed in the hydrogen spectrum to exactly the precision the Dirac equation predicts.

No additional assumptions. No spin-orbit coupling inserted by hand. Just the Dirac equation and a Coulomb potential.

---

## 3.5 — The Foldy-Wouthuysen Transformation: The Systematic Descent

To reach the Schrödinger equation from the Dirac equation, we need to **decouple the large and small components** of $\psi$ order by order in $v/c$. The systematic procedure for this is the **Foldy-Wouthuysen (FW) transformation**.

### 3.5.1 — The Strategy

The Dirac Hamiltonian has **even** operators (block-diagonal: couple $\phi$ to $\phi$ and $\chi$ to $\chi$) and **odd** operators (block-off-diagonal: couple $\phi$ to $\chi$):

$$\hat H_{Dirac} = \underbrace{\beta m_ec^2 + eV}_{\text{even: }\mathcal{E}} + \underbrace{c\boldsymbol{\alpha}\cdot\hat{\mathbf{\pi}}}_{\text{odd: }\mathcal{O}}$$

In the non-relativistic limit, the odd part $\mathcal{O}$ is small compared to the rest mass energy $m_ec^2$. We perform a sequence of unitary transformations $\psi \to e^{iS}\psi$ to eliminate odd operators order by order.

### 3.5.2 — First Transformation: Eliminating $\mathcal{O}$ at Leading Order

Choose the generator: $$S = -\frac{i\beta\mathcal{O}}{2m_ec^2} = -\frac{i\beta,c\boldsymbol{\alpha}\cdot\hat{\mathbf{\pi}}}{2m_ec^2}$$

The transformed Hamiltonian (to order $1/m_ec^2$):

$$\hat H' = e^{iS}\hat H_{Dirac}e^{-iS} = \beta m_ec^2 + eV + \frac{\hat\pi^2}{2m_e} - \frac{e\hbar}{2m_ec}\beta\boldsymbol{\sigma}\cdot\mathbf{B} + \text{remaining odd terms of order }(v/c)^3$$

The remaining odd terms are of order $(v/c)^3 \times m_ec^2$ — two orders smaller than the original odd term. A second FW transformation eliminates these.

### 3.5.3 — The Result: The Foldy-Wouthuysen Hamiltonian

After completing the transformation to order $(v/c)^2$, the full FW Hamiltonian acting on the **large component $\phi$ only** is:

$$\boxed{\hat H_{FW} = m_ec^2 + \frac{\hat\pi^2}{2m_e} + eV \underbrace{- \frac{e\hbar}{2m_ec}\boldsymbol{\sigma}\cdot\mathbf{B}}_{\text{Zeeman term}} \underbrace{- \frac{\hat\pi^4}{8m_e^3c^2}}_{\text{rel. mass corr.}} \underbrace{- \frac{e\hbar}{4m_e^2c^2}\boldsymbol{\sigma}\cdot(\mathbf{E}\times\hat{\mathbf{p}})}_{\text{spin-orbit coupling}} \underbrace{+ \frac{e\hbar^2}{8m_e^2c^2}\nabla\cdot\mathbf{E}}_{\text{Darwin term}}}$$

Each term has a name and a physics:

|Term|Size|Physics|
|---|---|---|
|$m_ec^2$|Constant offset|Rest mass energy (set to zero in non-rel. limit)|
|$\hat\pi^2/2m_e + eV$|$\sim E_{atom}$|**Schrödinger Hamiltonian**|
|$-\frac{e\hbar}{2m_ec}\boldsymbol{\sigma}\cdot\mathbf{B}$|$\sim\alpha^2 E_{atom}$|**Zeeman effect** (spin in magnetic field)|
|$-\hat\pi^4/8m_e^3c^2$|$\sim\alpha^4 m_ec^2$|Relativistic kinetic energy correction|
|$-\frac{e\hbar}{4m_e^2c^2}\boldsymbol{\sigma}\cdot(\mathbf{E}\times\hat{\mathbf{p}})$|$\sim\alpha^4 m_ec^2$|**Spin-orbit coupling** (fine structure)|
|$\frac{e\hbar^2}{8m_e^2c^2}\nabla\cdot\mathbf{E}$|$\sim\alpha^4 m_ec^2$|**Darwin term** (contact interaction at $r=0$)|

The last three terms together account for the fine structure of hydrogen — matching the exact Dirac result to order $\alpha^4$.

---

## 3.6 — First Stop: The Pauli Equation

Keeping only the Schrödinger term and the Zeeman term, and dropping the rest-mass constant $m_ec^2$ (a trivial energy offset), we arrive at the **Pauli equation**:

$$\boxed{i\hbar\frac{\partial\phi}{\partial t} = \left[\frac{\left(\hat{\mathbf{p}} - \frac{e}{c}\mathbf{A}\right)^2}{2m_e} - \frac{e\hbar}{2m_ec}\boldsymbol{\sigma}\cdot\mathbf{B} + eV\right]\phi}$$

where $\phi$ is now a **two-component Pauli spinor**: $$\phi = \begin{pmatrix}\phi_\uparrow\\phi_\downarrow\end{pmatrix}$$

$\phi_\uparrow$ and $\phi_\downarrow$ are the spin-up and spin-down components.

### What the Pauli Equation Adds Over Schrödinger

The Pauli equation is the correct equation for a non-relativistic electron **including its spin**. The Zeeman term $-\frac{e\hbar}{2m_ec}\boldsymbol{\sigma}\cdot\mathbf{B}$ gives:

- Splitting of energy levels in magnetic fields (Zeeman effect)
- Spin precession in magnetic fields (the basis of NMR and MRI)
- Pauli paramagnetism in metals

The Pauli equation is what you should use whenever:

- Spin matters (magnetic fields, spin-orbit coupling)
- But energies are still much less than $m_ec^2$

### Expanding $({\hat p} - eA/c)^2$

$$\left(\hat{\mathbf{p}} - \frac{e}{c}\mathbf{A}\right)^2 = \hat{p}^2 - \frac{e}{c}(\hat{\mathbf{p}}\cdot\mathbf{A} + \mathbf{A}\cdot\hat{\mathbf{p}}) + \frac{e^2}{c^2}A^2$$

In the Coulomb gauge $\nabla\cdot\mathbf{A} = 0$, the operators commute ($\hat{\mathbf{p}}\cdot\mathbf{A} = \mathbf{A}\cdot\hat{\mathbf{p}}$):

$$= \hat{p}^2 - \frac{2e}{c}\mathbf{A}\cdot\hat{\mathbf{p}} + \frac{e^2}{c^2}A^2$$

For weak fields, drop the $A^2$ term. Using $\mathbf{B} = \nabla\times\mathbf{A}$:

$$\hat H_{Pauli} = \frac{\hat{p}^2}{2m_e} + eV - \frac{e}{2m_ec}(\hat{\mathbf{L}} + 2\hat{\mathbf{S}})\cdot\mathbf{B}$$

where $\hat{\mathbf{L}} = \hat{\mathbf{r}}\times\hat{\mathbf{p}}$ is the orbital angular momentum. The factor of 2 in front of $\hat{\mathbf{S}}$ is the $g_e = 2$ we already saw in §3.4.2 — it appears here automatically, as it must.

---

## 3.7 — Second Stop: The Schrödinger Equation

When the magnetic field is absent or spin is irrelevant (e.g., we are studying spatial wavefunctions for spinless situations), each component of $\phi$ satisfies the same equation independently. Setting $\mathbf{B} = 0$ and writing $\psi$ for a single spin component:

$$\boxed{i\hbar\frac{\partial\psi}{\partial t} = \hat H\psi = \left(-\frac{\hbar^2}{2m_e}\nabla^2 + V(\mathbf{r})\right)\psi}$$

This is the **Schrödinger equation** — the foundation of all of Layer 1.

### What This Derivation Reveals

Every introductory quantum mechanics course treats the Schrödinger equation as an axiom — a starting postulate handed down without justification. From the perspective of this book, it is not an axiom. It is:

1. The non-relativistic, single-particle, spin-ignored limit of the Dirac equation
2. Which is itself the Euler-Lagrange equation of the electron Lagrangian
3. Which is the U(1)-coupled fermion sector of $\mathcal{L}_{SM}$
4. Which follows from requiring the action to be invariant under U(1) gauge transformations

**Every symbol in the Schrödinger equation has a traceable origin:**

|Symbol|Origin|
|---|---|
|$i$|Required by unitarity of time evolution (unitary representation of the Poincaré group)|
|$\hbar$|Sets the scale between the action and quantum phenomena; appears in the path integral weight $e^{iS/\hbar}$|
|$\partial/\partial t$|Time translation; by Noether → energy; operator $\hat H = i\hbar\partial_t$|
|$-\hbar^2\nabla^2/2m$|Non-relativistic kinetic energy; from $\hat p^2/2m$ with $\hat p = -i\hbar\nabla$|
|$V(\mathbf{r})$|The electromagnetic potential $eA_0$; from the U(1) gauge coupling in $D_\mu$|
|$\psi$|The large component of the Dirac spinor; $|

### The Time-Independent Schrödinger Equation

For a stationary state $\psi(\mathbf{r},t) = \phi(\mathbf{r})e^{-iEt/\hbar}$:

$$\boxed{\hat H\phi = E\phi \qquad \text{i.e.,} \qquad \left(-\frac{\hbar^2}{2m}\nabla^2 + V\right)\phi = E\phi}$$

This is an eigenvalue equation: $\phi$ are the **energy eigenstates** and $E$ are the **energy eigenvalues**. Its solutions for various potentials $V(\mathbf{r})$ are the substance of Chapters 4 and 5.

---

## 3.8 — The Bridge Zone: When to Use Which Equation

The three equations of this chapter are not competitors — they are a nested hierarchy. The appropriate equation depends on the regime:

```
Regime                      Equation to use          Chapters
─────────────────────────────────────────────────────────────
E ~ mc², pair creation      Full QED / L_SM          Ch. 0
E ≲ mc², single particle    Dirac equation           §3.3–3.4
E ≪ mc², spin matters       Pauli equation           §3.6, Ch. 5
E ≪ mc², spin irrelevant    Schrödinger equation     §3.7, Ch. 4–6
Classical: S ≫ ħ            Newtonian mechanics      Ch. 9 (Bridge B.a)
```

**The bridge zone** is the Dirac equation — it lives between the full QFT of Chapter 0 and the non-relativistic quantum mechanics of Chapters 4–7. The Dirac equation is the correct equation to use for:

- Relativistic electrons in heavy atoms (large nuclear charge $Z$; inner electrons have $v/c \sim Z\alpha$, which becomes significant for $Z \gtrsim 50$)
- Electron transport in graphene (the electrons in graphene mimic massless Dirac fermions because the band structure near the Dirac point is linear, not parabolic — a Layer-1 accident with Layer-0 mathematical structure)
- Positron emission tomography (PET): pair annihilation, requires the antiparticle solutions
- Spintronic devices where spin-orbit coupling is designed in deliberately

---

## 3.9 — What Survived the Descent

After the descent from $\mathcal{L}_{SM}$ to the Schrödinger equation, the following structures survive intact. Each one is traceable to a Layer-0 origin:

### 3.9.1 — The Wavefunction $\psi(\mathbf{r}, t)$

A complex-valued function of position and time. It is not a classical field you can directly observe — it is a **probability amplitude**. Its origin is the large component of the Dirac spinor, which is itself the fermion field $\psi$ of $\mathcal{L}_{SM}$ in the single-particle, non-relativistic limit.

### 3.9.2 — The Probability Interpretation: Noether's Theorem in Action

From the Dirac Lagrangian, the U(1) symmetry $\psi \to e^{i\alpha}\psi$ gives, via Noether's theorem, a conserved current:

$$j^\mu = -e\bar\psi\gamma^\mu\psi = \left(-e|\psi|^2,; -e\bar\psi\gamma^i\psi\right)$$

The conservation law $\partial_\mu j^\mu = 0$ becomes, in 3+1 notation:

$$\frac{\partial(-e|\psi|^2)}{\partial t} + \nabla\cdot\mathbf{j} = 0$$

Dividing by $-e$:

$$\frac{\partial|\psi|^2}{\partial t} + \nabla\cdot\left(\frac{\mathbf{j}}{-e}\right) = 0$$

This is the **continuity equation for probability**: $|\psi|^2$ is a conserved density. The probability of finding the electron somewhere is conserved over time.

**The probabilistic interpretation of quantum mechanics is not a philosophical choice added on top of the mathematics. It is Noether's theorem applied to U(1) gauge symmetry.**

### 3.9.3 — Superposition

The Schrödinger equation is linear in $\psi$. If $\psi_1$ and $\psi_2$ are solutions, so is $c_1\psi_1 + c_2\psi_2$ for any complex constants. This linearity is inherited from the linearity of the Dirac equation, which is itself linear because the Lagrangian $\bar\psi(i\gamma^\mu D_\mu - m)\psi$ is quadratic in the fields (first power of $\psi$ and first power of $\bar\psi$).

Superposition is not an axiom of quantum mechanics. It is a consequence of the Lagrangian having no higher powers of the fermion field.

### 3.9.4 — Minimal Coupling: $\hat{\mathbf{p}} \to \hat{\mathbf{p}} - \frac{e}{c}\mathbf{A}$

The replacement of the canonical momentum $\hat{\mathbf{p}}$ by the kinetic momentum $\hat{\mathbf{p}} - \frac{e}{c}\mathbf{A}$ — the standard way of introducing electromagnetic fields into quantum mechanics — comes directly from the covariant derivative $D_\mu = \partial_\mu + ieA_\mu$ in the original Lagrangian. Minimal coupling is not a separate rule; it is what covariant derivative means, evaluated in the non-relativistic limit.

### 3.9.5 — Spin (in the Pauli equation)

The Pauli matrices $\boldsymbol{\sigma}$ in the Pauli equation are the $2\times 2$ blocks of the $4\times 4$ gamma matrices — a direct inheritance from the Dirac spinor structure. Spin is not added to the Schrödinger equation from outside; it lives in the Pauli equation, which is one order higher in $v/c$ from Schrödinger.

---

## 3.10 — What Was Discarded, and Why It Was Allowed

|Discarded|Physical content|Smallness parameter|When it matters|
|---|---|---|---|
|Antiparticle components ($\chi$)|Positron; pair creation|$\sim (v/c)^2$ relative to $\phi$|$E \sim m_ec^2$ — not in atoms|
|Relativistic kinetic correction $-p^4/8m^3c^2$|Relativistic mass increase|$\alpha^4 m_ec^2/E_{Bohr} \sim \alpha^2$|Fine structure (Ch. 5)|
|Spin-orbit coupling|Fine structure splitting|$\sim\alpha^2$|Fine structure (Ch. 5)|
|Darwin term|$s$-state contact interaction|$\sim\alpha^2$|Fine structure (Ch. 5)|
|QED loop corrections|Lamb shift, $g-2$|$\sim\alpha/\pi \approx 0.002$|Precision spectroscopy|
|Virtual pair loops|Vacuum polarization|$\sim\alpha^2$|Precision spectroscopy|

**The key point:** every discarded term has a named smallness parameter. None are thrown away without justification. When you need more precision (spectroscopy, metrology, exotic atoms), you add terms back in the appropriate order.

---

## 3.11 — The Uncertainty Principle: A Structural Consequence

Before moving on, one of the most famous results in quantum mechanics deserves to be placed in its proper context.

The **Heisenberg uncertainty principle** $\Delta x,\Delta p \geq \hbar/2$ is often presented as a mysterious feature of quantum mechanics — a limit on measurement or a consequence of disturbing the system. Its actual origin is simpler and more structural.

The momentum operator in the Schrödinger equation is $\hat p = -i\hbar\nabla$. The position operator is $\hat x = x$ (multiplication by $x$). Their commutator:

$$[\hat x, \hat p] = \hat x\hat p - \hat p\hat x = i\hbar$$

This commutation relation is a **mathematical consequence of $\hat p = -i\hbar\nabla$** — which is itself a consequence of the field $\psi$ having the Fourier decomposition $\psi(\mathbf{r}) = \int \tilde\psi(\mathbf{k})e^{i\mathbf{k}\cdot\mathbf{r}}d^3k$ with $\hat p\psi = \hbar\mathbf{k}\psi$ for a definite-$k$ component.

A standard result from Fourier analysis then gives: $$\Delta x,\Delta k \geq \frac{1}{2} \qquad\Longrightarrow\qquad \Delta x,\Delta p \geq \frac{\hbar}{2}$$

**The uncertainty principle is the Fourier bandwidth theorem, applied to the wavefunction.** It is structural — it would hold for any wave-like description, classical or quantum. What makes it quantum is that $p = \hbar k$ — that momentum is proportional to wavenumber, which is itself a consequence of $\hat p = -i\hbar\nabla$ in the Schrödinger equation, which traces back to the covariant derivative in $\mathcal{L}_{SM}$.

---

## 3.12 — Summary of Bridge A

**What we started with:** $$\mathcal{L}_{SM} = \text{full Standard Model + gravity}$$

**The three steps:**

|Step|Operation|Result|
|---|---|---|
|§3.1|Isolate U(1)-coupled electron sector; treat $A_\mu$ as classical|Electron QED Lagrangian|
|§3.2|Apply Euler-Lagrange|**Dirac equation** (bridge zone)|
|§3.5–3.6|Foldy-Wouthuysen to order $(v/c)^2$|**Pauli equation** (with spin)|
|§3.7|Drop spin terms, $B\to0$|**Schrödinger equation**|

**What was preserved:** wavefunction, probability conservation (Noether/U(1)), superposition, minimal coupling, spin (in Pauli), uncertainty principle (Fourier structure)

**What was discarded:** antiparticles, pair creation, QED loops, relativistic corrections (available on demand: add FW terms back for fine structure)

**The validity criterion:** $$E_{kinetic} \ll m_ec^2 = 511;\text{keV} \qquad \Leftrightarrow \qquad v \ll c$$

For hydrogen ground state: $v/c = \alpha \approx 1/137$; error is $\alpha^2 \approx 0.005%$

---

## 3.13 — Looking Ahead: Layer 1

With the Schrödinger equation in hand, Layer 1 opens up. The next four chapters use it to build the atomic world from scratch:

**Chapter 4** — The Schrödinger equation in free space and in simple potentials. The infinite well, the harmonic oscillator, the hydrogen atom. Quantum numbers, energy levels, wavefunctions. The periodic table begins.

**Chapter 5** — Spin, multi-electron systems, and the periodic table completed. Spin-orbit coupling (FW term) gives fine structure. The Pauli equation gives the Zeeman effect. Many-electron Schrödinger + Pauli exclusion (which, remember, came from the anticommutation of $\psi$ in $\mathcal{L}_{SM}$) gives the shell structure of atoms.

**Chapter 6** — The Schrödinger equation in a periodic lattice. Bloch's theorem. Band structure. Metals, semiconductors, insulators. Molecular bonding. Nuclear binding energy. These are the material properties every engineer works with.

**Chapter 7** — Where Layer-1 physics becomes topological. Quantum Hall effect, Berry phase, topological insulators. The echo of the $\theta$-term from Chapter 0, heard at the scale of centimeter-sized condensed matter devices.

---

_End of Chapter 3._

---

_Next: Chapter 4 — Layer 1 Begins: The Schrödinger Equation, Energy Quantization, and the Hydrogen Atom_