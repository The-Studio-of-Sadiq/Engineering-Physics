# The Schrödinger Equation and the Hydrogen Atom

### Layer 1 Begins: Quantization, Wavefunctions, and the Architecture of Atoms

---

> _The more I think about the physical portion of Schrödinger's theory,_ _the more repulsive I find it._ _What does it mean for an electron to be a wave?_ — Werner Heisenberg, 1926
> 
> _He was wrong to be repulsed. Schrödinger was right._ — The rest of physics, 1927–present

---

## 4.0 — Where We Are

In Chapter 3, you watched the Schrödinger equation fall out of the Standard Model Lagrangian through a sequence of named, controlled approximations. The equation arrived at your door already carrying its justification.

Now we use it.

This chapter does two things. First, it builds physical intuition through three exactly-solvable quantum systems — the infinite well, the harmonic oscillator, and the finite barrier. Each one teaches something about quantization that the next system confirms. Second, it solves the hydrogen atom completely — the most important calculation in all of chemistry and materials science.

By the end of this chapter, you will understand not just the energy levels of hydrogen but _why_ they are discrete, _why_ three quantum numbers appear, and _why_ atomic structure is the way it is. The entire periodic table follows from what happens here.

---

## 4.1 — Operators and the Language of Quantum Mechanics

### 4.1.1 — Physical Quantities as Operators

In classical mechanics, physical quantities are just numbers: the position of a particle is a vector $\mathbf{r}(t)$, its momentum is $\mathbf{p}(t) = m\dot{\mathbf{r}}$, and its energy is $H = p^2/2m + V$.

In quantum mechanics, physical quantities are **operators** — mathematical objects that act on wavefunctions:

|Classical quantity|Quantum operator|Action on $\psi$|
|---|---|---|
|Position $x$|$\hat x$|Multiply by $x$|
|Momentum $p_x$|$\hat p_x = -i\hbar,\partial/\partial x$|Differentiate, multiply by $-i\hbar$|
|Kinetic energy $p^2/2m$|$\hat T = -(\hbar^2/2m)\nabla^2$|Apply Laplacian, multiply by $-\hbar^2/2m$|
|Potential energy $V(\mathbf{r})$|$\hat V = V(\mathbf{r})$|Multiply by $V(\mathbf{r})$|
|Total energy $H$|$\hat H = \hat T + \hat V$|Apply both above|

The momentum operator $\hat p_x = -i\hbar,\partial/\partial x$ is not an arbitrary choice — it follows directly from the plane wave $\psi = e^{ikx}$ being an eigenstate with $\hat p_x \psi = \hbar k,\psi$, and $p = \hbar k$ being the de Broglie relation from Ch. 3.

### 4.1.2 — The Eigenvalue Equation

The Schrödinger equation in its time-independent form (§3.7):

$$\hat H\psi = E\psi \qquad \Longrightarrow \qquad \left(-\frac{\hbar^2}{2m}\nabla^2 + V(\mathbf{r})\right)\psi = E\psi$$

is an **eigenvalue equation**: find the functions $\psi_n$ (eigenfunctions) and numbers $E_n$ (eigenvalues) such that $\hat H$ acting on $\psi_n$ returns $E_n$ times $\psi_n$.

**Why eigenvalues are what you measure:** When you perform an energy measurement on a quantum system, the result is always one of the eigenvalues $E_n$. You cannot get an intermediate value. This is not a postulate here — it follows from the requirement that measurement must yield a definite number consistent with probability conservation (Noether's theorem, Ch. 1 §1.7). The discreteness of measured values is a mathematical consequence of the operator structure.

### 4.1.3 — Expectation Values

You will not always find the system in an energy eigenstate. For a general wavefunction $\psi$, the **expectation value** of an observable $\hat A$ is:

$$\langle A\rangle = \int_{-\infty}^{\infty}\psi^*\hat A\psi,d^3r$$

This is the statistical average of many repeated measurements on identically prepared systems. For the position:

$$\langle x\rangle = \int x,|\psi|^2,dx$$

The probability of finding the particle between $x$ and $x + dx$ is $|\psi(x)|^2 dx$. This is why normalization is required:

$$\int_{-\infty}^{\infty}|\psi|^2,d^3r = 1$$

Total probability must be 1 — the particle is somewhere. This is the continuity equation from Ch. 3 §3.9.2, integrated over all space.

---

## 4.2 — The Infinite Square Well: Where Quantization Is Born

### 4.2.1 — The Setup

The simplest quantum system that exhibits quantization: a particle of mass $m$ confined to a one-dimensional box of length $L$, with impenetrable walls:

$$V(x) = \begin{cases}0 & 0 \leq x \leq L \ \infty & \text{otherwise}\end{cases}$$

The infinite potential walls mean the particle cannot exist outside $[0,L]$:

$$\psi(x) = 0 \quad \text{for } x \leq 0 \text{ and } x \geq L$$

### 4.2.2 — The Solution

Inside the well ($V = 0$), the Schrödinger equation is:

$$-\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2} = E\psi \qquad\Longrightarrow\qquad \frac{d^2\psi}{dx^2} = -k^2\psi, \quad k = \frac{\sqrt{2mE}}{\hbar}$$

The general solution is $\psi(x) = A\sin(kx) + B\cos(kx)$.

**Applying boundary conditions:**

- $\psi(0) = 0$: gives $B = 0$, so $\psi = A\sin(kx)$
- $\psi(L) = 0$: requires $\sin(kL) = 0$, which means $kL = n\pi$ for integer $n$

$$\boxed{k_n = \frac{n\pi}{L}, \qquad n = 1, 2, 3, \ldots}$$

**The quantization condition** emerges from the boundary conditions — not from any additional axiom. The allowed wavefunctions and energies are:

$$\psi_n(x) = \sqrt{\frac{2}{L}}\sin!\left(\frac{n\pi x}{L}\right)$$

$$\boxed{E_n = \frac{n^2\pi^2\hbar^2}{2mL^2} = n^2 E_1, \qquad E_1 = \frac{\pi^2\hbar^2}{2mL^2}}$$

The $\sqrt{2/L}$ normalization constant comes from requiring $\int_0^L|\psi_n|^2 dx = 1$.

### 4.2.3 — What This Teaches

**Lesson 1: Quantization comes from boundary conditions.** The integer $n$ is not put in by hand — it is forced by requiring the wavefunction to vanish at both walls. This is exactly how a guitar string has discrete harmonics: $n$ nodes fit in the length $L$. Quantum mechanics is wave mechanics.

**Lesson 2: Zero-point energy is not zero.** The lowest allowed energy is $E_1 = \pi^2\hbar^2/2mL^2 > 0$, not zero. The particle cannot be at rest. From the uncertainty principle (Ch. 3 §3.11): confining a particle to length $\Delta x \approx L$ forces $\Delta p \geq \hbar/2L$, which requires nonzero kinetic energy. Zero-point energy is the uncertainty principle made concrete.

**Lesson 3: Quantum numbers label orthogonal states.** Different eigenfunctions are orthogonal: $\int_0^L\psi_m^*\psi_n,dx = \delta_{mn}$. States with different $n$ are completely distinguishable. The quantum number $n$ is an integer label for a standing-wave mode.

**Lesson 4: The correspondence principle.** For large $n$, the probability density $|\psi_n|^2$ becomes nearly uniform over the well — matching what classical mechanics predicts (equal probability of being anywhere in the well). Quantum mechanics recovers classical mechanics at large quantum numbers.

### 4.2.4 — Uncertainty Principle Check

For the ground state $\psi_1 = \sqrt{2/L}\sin(\pi x/L)$:

$$\langle x\rangle = \frac{L}{2}, \quad \Delta x = \frac{L}{\sqrt{12}}\sqrt{1 - \frac{6}{\pi^2}}$$

$$\langle p\rangle = 0, \quad \Delta p = \frac{\pi\hbar}{L}$$

$$\Delta x,\Delta p = \frac{\pi\hbar}{L}\cdot\frac{L}{\sqrt{12}}\sqrt{1 - \frac{6}{\pi^2}} \approx 0.568,\hbar \geq \frac{\hbar}{2};\checkmark$$

The inequality is satisfied — as it must be for any quantum state.

---

## 4.3 — The Quantum Harmonic Oscillator

The harmonic oscillator $V = \frac{1}{2}m\omega^2 x^2$ is the most important potential in all of physics. Every stable potential near equilibrium is approximately harmonic (Taylor expansion around the minimum). Atoms in a crystal, electrons in a magnetic field, electromagnetic modes in a cavity — all are harmonic oscillators in disguise.

### 4.3.1 — The Ladder Operator Method

Rather than grinding through the differential equation, introduce the **ladder operators**:

$$\hat a_\pm = \frac{1}{\sqrt{2\hbar m\omega}}\left(m\omega\hat x \mp i\hat p\right)$$

They satisfy $[\hat a_-, \hat a_+] = 1$. The Hamiltonian becomes:

$$\hat H = \hbar\omega\left(\hat a_+\hat a_- + \frac{1}{2}\right)$$

If $\psi$ is an eigenstate with energy $E$, then $\hat a_+\psi$ is an eigenstate with energy $E + \hbar\omega$, and $\hat a_-\psi$ is an eigenstate with energy $E - \hbar\omega$. They "climb" and "descend" the energy ladder.

Since energy must be bounded below, there exists a ground state $\psi_0$ with $\hat a_-\psi_0 = 0$. Solving this:

$$\psi_0(x) = \left(\frac{m\omega}{\pi\hbar}\right)^{1/4}\exp!\left(-\frac{m\omega x^2}{2\hbar}\right)$$

The ground state is a Gaussian. All higher states are generated by applying $\hat a_+$ repeatedly:

$$\psi_n = \frac{(\hat a_+)^n}{\sqrt{n!}}\psi_0$$

### 4.3.2 — Energy Levels

$$\boxed{E_n = \hbar\omega!\left(n + \frac{1}{2}\right), \qquad n = 0, 1, 2, \ldots}$$

Every energy level is separated by exactly $\hbar\omega$. The zero-point energy is $E_0 = \hbar\omega/2$.

**Why this matters beyond quantum mechanics:** The quantum field in Chapter 0 is a collection of quantum harmonic oscillators — one per mode per field. When you quantize a mode of the electromagnetic field (a photon of frequency $\omega$), you get $E = \hbar\omega(n+\frac{1}{2})$ where $n$ is the photon number. The $\hbar\omega/2$ zero-point energy summed over all modes gives the vacuum energy — and the Casimir effect (Ch. 2 entry) is the measurable consequence of this sum being different between two plates than in free space. The harmonic oscillator is the engine of quantum field theory.

### 4.3.3 — Wavefunctions

The $n$-th eigenfunction involves the $n$-th Hermite polynomial $H_n$:

$$\psi_n(x) = \left(\frac{m\omega}{\pi\hbar}\right)^{1/4}\frac{1}{\sqrt{2^n n!}}H_n!\left(\sqrt{\frac{m\omega}{\hbar}}x\right)\exp!\left(-\frac{m\omega x^2}{2\hbar}\right)$$

The first few:

- $\psi_0 \propto e^{-m\omega x^2/2\hbar}$ — Gaussian, no nodes
- $\psi_1 \propto x,e^{-m\omega x^2/2\hbar}$ — one node at $x = 0$
- $\psi_2 \propto (2m\omega x^2/\hbar - 1)e^{-m\omega x^2/2\hbar}$ — two nodes

The $n$-th state has exactly $n$ nodes — the same node-counting rule as the infinite square well. This is not a coincidence: for any confining potential, the $n$-th eigenstate has $n-1$ (or $n$) nodes, by the oscillation theorem.

---

## 4.4 — Quantum Tunneling: The Finite Barrier

### 4.4.1 — The Setup

For a rectangular potential barrier of height $V_0$ and width $d$, with particle energy $E < V_0$:

$$V(x) = \begin{cases}0 & x < 0 \text{ (region I)} \ V_0 & 0 \leq x \leq d \text{ (region II)} \ 0 & x > d \text{ (region III)}\end{cases}$$

### 4.4.2 — The Solution Inside the Barrier

Inside the barrier, the Schrödinger equation becomes:

$$\frac{d^2\psi}{dx^2} = \kappa^2\psi, \qquad \kappa = \frac{\sqrt{2m(V_0 - E)}}{\hbar}$$

Since $E < V_0$, $\kappa$ is real and positive. The solution inside is: $$\psi_{II}(x) = Ce^{\kappa x} + De^{-\kappa x}$$

This is not oscillatory — it decays (and grows) exponentially. Classically, the particle simply reflects at $x = 0$. Quantum mechanically, the wavefunction extends into the classically forbidden region.

### 4.4.3 — Transmission Coefficient

Matching the wavefunction and its derivative at both boundaries ($x = 0$ and $x = d$) gives the transmission coefficient — the probability that the particle passes through:

$$\boxed{T \approx 16\frac{E}{V_0}!\left(1 - \frac{E}{V_0}\right)e^{-2\kappa d}}$$

(valid for $\kappa d \gg 1$, the thick barrier limit)

**Key physics:**

- $T$ depends **exponentially** on the barrier width $d$ and on $\kappa \propto \sqrt{V_0 - E}$
- Doubling the barrier width squares the transmission: $T \to T^2$
- This extreme sensitivity to $d$ and $V_0 - E$ makes tunneling both measurable and controllable

### 4.4.4 — Engineering Applications

|Application|What tunnels|Barrier|Engineering use|
|---|---|---|---|
|Tunnel diode|Electrons|Semiconductor junction|Oscillators, fast switches|
|STM (Scanning Tunneling Microscope)|Electrons|Vacuum gap 1–10 Å|Atomic-resolution imaging|
|Flash memory|Electrons|Thin oxide|Non-volatile data storage|
|α-decay (Ch. 6)|α particle|Coulomb barrier|Nuclear dating|
|MOSFET gate leakage|Electrons|Gate oxide|Limits transistor scaling|

The STM tunnel current $I \propto e^{-2\kappa z}$ where $z$ is tip-sample distance; at $\kappa \approx 10,\text{nm}^{-1}$, a 1 Å change in $z$ changes the current by a factor of $e^2 \approx 7.4$. This extraordinary sensitivity is what gives STM atomic resolution.

---

## 4.5 — The Hydrogen Atom

This is the most important calculation in atomic physics. Everything that follows in Chapters 5, 6, and 7 is either an extension or an approximation of what we derive here.

### 4.5.1 — The Setup

One electron of mass $m_e$ and charge $-e$ orbiting a proton of charge $+e$. The potential energy is the Coulomb attraction:

$$V(r) = -\frac{e^2}{4\pi\epsilon_0 r}$$

This depends only on $r$ — the distance between electron and proton. The Schrödinger equation is:

$$-\frac{\hbar^2}{2m_e}\nabla^2\psi + V(r)\psi = E\psi$$

### 4.5.2 — Why Spherical Coordinates

The Coulomb potential has **spherical symmetry**: $V$ depends only on $r$, not on the angles $\theta$ and $\phi$. Working in spherical coordinates $(r, \theta, \phi)$ lets us exploit this symmetry directly.

The Laplacian in spherical coordinates:

$$\nabla^2 = \frac{1}{r^2}\frac{\partial}{\partial r}!\left(r^2\frac{\partial}{\partial r}\right) + \frac{1}{r^2\sin\theta}\frac{\partial}{\partial\theta}!\left(\sin\theta\frac{\partial}{\partial\theta}\right) + \frac{1}{r^2\sin^2\theta}\frac{\partial^2}{\partial\phi^2}$$

This looks terrifying. The key observation: **the angular part is a known operator**. The expression in angular brackets is proportional to $\hat L^2$ — the squared angular momentum operator — which has known eigenfunctions (spherical harmonics).

### 4.5.3 — Separation of Variables: The Core Strategy

Try a solution of the form: $$\psi(r,\theta,\phi) = R(r),Y(\theta,\phi)$$

Substituting into the Schrödinger equation and dividing through by $R(r)Y(\theta,\phi)$:

$$\underbrace{\frac{1}{R}\frac{d}{dr}!\left(r^2\frac{dR}{dr}\right) - \frac{2m_er^2}{\hbar^2}(V(r) - E)}_{\text{function of }r\text{ only}} = -\underbrace{\frac{1}{Y}\hat\Lambda^2 Y}_{\text{function of }\theta,\phi\text{ only}}$$

where $\hat\Lambda^2$ is the angular part of $\nabla^2$. Since the left side depends only on $r$ and the right only on $\theta, \phi$, **both sides must equal the same constant** — call it $\ell(\ell + 1)$. This gives two separate equations:

**Angular equation:** $$\hat\Lambda^2 Y = -\ell(\ell+1)Y$$

**Radial equation:** $$\frac{1}{r^2}\frac{d}{dr}!\left(r^2\frac{dR}{dr}\right) + \left[\frac{2m_e}{\hbar^2}(E - V(r)) - \frac{\ell(\ell+1)}{r^2}\right]R = 0$$

The constant $\ell(\ell+1)$ is called the **separation constant**. It will turn out to be related to the orbital angular momentum.

---

## 4.6 — The Angular Equations: Quantum Numbers $\ell$ and $m$

### 4.6.1 — The $\phi$ Equation

Further separate $Y(\theta,\phi) = \Theta(\theta)\Phi(\phi)$. The $\phi$ equation is:

$$\frac{d^2\Phi}{d\phi^2} = -m^2\Phi$$

Solution: $\Phi(\phi) = e^{im\phi}$

**Quantization of $m$:** The wavefunction must be single-valued — physically, rotating by $2\pi$ must return you to the same state:

$$\Phi(\phi + 2\pi) = \Phi(\phi) \qquad\Longrightarrow\qquad e^{im\cdot 2\pi} = 1$$

This forces $m$ to be an integer: $m = 0, \pm 1, \pm 2, \ldots$

**The origin of quantized angular momentum:** $m$ is the magnetic quantum number — it is forced to be an integer by the simple requirement that the wavefunction is single-valued around the $z$-axis. This is the same topological argument that gives flux quantization in a superconducting ring (Ch. 7).

### 4.6.2 — The $\theta$ Equation: Associated Legendre Polynomials

The $\theta$ equation becomes:

$$\frac{1}{\sin\theta}\frac{d}{d\theta}!\left(\sin\theta\frac{d\Theta}{d\theta}\right) + \left[\ell(\ell+1) - \frac{m^2}{\sin^2\theta}\right]\Theta = 0$$

The solutions are the **associated Legendre polynomials** $P_\ell^m(\cos\theta)$.

**Quantization of $\ell$:** For $\Theta(\theta)$ to be finite at $\theta = 0$ and $\theta = \pi$ (the poles), the separation constant must satisfy:

$$\ell = 0, 1, 2, 3, \ldots \quad\text{and}\quad |m| \leq \ell$$

The constraint $|m| \leq \ell$ has a clear physical meaning: the z-component of angular momentum cannot exceed the total angular momentum.

### 4.6.3 — Spherical Harmonics

Combining the $\Theta$ and $\Phi$ solutions gives the **spherical harmonics** $Y_\ell^m(\theta, \phi)$:

$$Y_\ell^m(\theta,\phi) = \sqrt{\frac{(2\ell+1)}{4\pi}\frac{(\ell-|m|)!}{(\ell+|m|)!}}P_\ell^m(\cos\theta),e^{im\phi}$$

These are the angular eigenfunctions of the hydrogen atom — and of every spherically symmetric potential. The first few:

|$\ell$|$m$|Label|$Y_\ell^m$|
|---|---|---|---|
|0|0|$s$|$1/\sqrt{4\pi}$|
|1|0|$p_z$|$\sqrt{3/4\pi}\cos\theta$|
|1|±1|$p_{x,y}$|$\mp\sqrt{3/8\pi}\sin\theta,e^{\pm i\phi}$|
|2|0|$d_{z^2}$|$\sqrt{5/16\pi}(3\cos^2\theta - 1)$|

The shapes of these functions — spherical, dumbbell, cloverleaf — are the shapes of the atomic orbitals that govern all of chemistry.

**Key properties:**

- Orthonormal: $\int Y_\ell^{m*}Y_{\ell'}^{m'},d\Omega = \delta_{\ell\ell'}\delta_{mm'}$
- Angular momentum: $\hat L^2 Y_\ell^m = \ell(\ell+1)\hbar^2 Y_\ell^m$ and $\hat L_z Y_\ell^m = m\hbar Y_\ell^m$

---

## 4.7 — The Radial Equation: Quantum Number $n$ and Energy

### 4.7.1 — Substitution and Simplification

With $u(r) \equiv rR(r)$, the radial equation becomes:

$$-\frac{\hbar^2}{2m_e}\frac{d^2u}{dr^2} + \left[V(r) + \frac{\hbar^2\ell(\ell+1)}{2m_e r^2}\right]u = Eu$$

This looks like the one-dimensional Schrödinger equation with an **effective potential**:

$$V_{eff}(r) = -\frac{e^2}{4\pi\epsilon_0 r} + \underbrace{\frac{\hbar^2\ell(\ell+1)}{2m_e r^2}}_{\text{centrifugal barrier}}$$

The centrifugal term $\ell(\ell+1)\hbar^2/2m_e r^2$ pushes the electron away from the nucleus for $\ell > 0$ — the quantum analog of the classical centrifugal effect.

### 4.7.2 — Boundary Conditions and the Quantization of Energy

**At $r \to \infty$:** For bound states ($E < 0$), the wavefunction must vanish: $u(r) \to 0$.

**At $r \to 0$:** $u(0) = 0$ (since $R(r) = u/r$ must be finite at the origin).

Solving the radial equation with the Coulomb potential $V = -e^2/4\pi\epsilon_0 r$, the mathematical requirement that $R(r)$ remains finite at both boundaries forces the energy to take discrete values. The solutions are the **associated Laguerre polynomials** $L_{n-\ell-1}^{2\ell+1}$, and they only exist when:

$$n = 1, 2, 3, \ldots \qquad\text{and}\qquad \ell \leq n-1$$

where $n$ is called the **principal quantum number**.

### 4.7.3 — The Energy Levels of Hydrogen

$$\boxed{E_n = -\frac{m_e e^4}{2(4\pi\epsilon_0)^2\hbar^2}\cdot\frac{1}{n^2} = -\frac{13.6;\text{eV}}{n^2}, \qquad n = 1, 2, 3, \ldots}$$

This is the **Bohr formula** — but now derived rigorously from the Schrödinger equation, not guessed from Bohr's circular orbit model. Bohr guessed correctly; Schrödinger explained why.

The **Bohr radius** $a_0$ sets the natural length scale:

$$a_0 = \frac{4\pi\epsilon_0\hbar^2}{m_e e^2} = 0.529;\text{\AA} = 0.0529;\text{nm}$$

In terms of $a_0$, the energy becomes $E_n = -e^2/8\pi\epsilon_0 a_0 n^2$.

---

## 4.8 — The Complete Solution: Three Quantum Numbers

Assembling the pieces:

$$\boxed{\psi_{n\ell m}(r,\theta,\phi) = R_{n\ell}(r),Y_\ell^m(\theta,\phi)}$$

The three quantum numbers and their origin:

|Quantum number|Name|Values|Origin|Physical meaning|
|---|---|---|---|---|
|$n$|Principal|$1, 2, 3, \ldots$|Normalizability of $R_{n\ell}$ at $r\to\infty$|Sets the energy: $E_n = -13.6/n^2$ eV|
|$\ell$|Orbital/azimuthal|$0, 1, \ldots, n-1$|Finiteness of $R_{n\ell}$ at $r = 0$|Total orbital angular momentum: $L = \sqrt{\ell(\ell+1)}\hbar$|
|$m$|Magnetic|$-\ell, \ldots, 0, \ldots, +\ell$|Single-valuedness of $\Phi(\phi)$|$z$-component: $L_z = m\hbar$|

**The constraint chain:** Solving one equation forces the next quantum number. Solving the $\phi$ equation gives integer $m$. The $\theta$ equation then requires $\ell \geq |m|$. The radial equation requires $n \geq \ell + 1$. The three quantum numbers are not three independent choices — they are three consecutive constraints on one wavefunction.

### 4.8.1 — Explicit Wavefunctions

**Ground state** ($n=1$, $\ell=0$, $m=0$): the 1s state

$$\psi_{100} = \frac{1}{\sqrt{\pi}}\left(\frac{1}{a_0}\right)^{3/2}e^{-r/a_0}$$

Spherically symmetric (no angular dependence). Electron most likely found at $r = a_0$ (the Bohr radius). Energy: $E_1 = -13.6$ eV.

**First excited states** ($n=2$): four degenerate states

$$\psi_{200} = \frac{1}{4\sqrt{2\pi}}\left(\frac{1}{a_0}\right)^{3/2}\left(2 - \frac{r}{a_0}\right)e^{-r/2a_0}$$

$$\psi_{210} = \frac{1}{4\sqrt{2\pi}}\left(\frac{1}{a_0}\right)^{3/2}\frac{r}{a_0}e^{-r/2a_0}\cos\theta$$

$$\psi_{21\pm1} = \mp\frac{1}{8\sqrt{\pi}}\left(\frac{1}{a_0}\right)^{3/2}\frac{r}{a_0}e^{-r/2a_0}\sin\theta,e^{\pm i\phi}$$

All have energy $E_2 = -13.6/4 = -3.4$ eV.

---

## 4.9 — Degeneracy: Why Multiple States Have the Same Energy

For hydrogen, the energy $E_n = -13.6/n^2$ eV depends **only on $n$**, not on $\ell$ or $m$. For a given $n$:

- $\ell$ can take values $0, 1, \ldots, n-1$ ($n$ values)
- For each $\ell$, $m$ takes $2\ell + 1$ values

Total number of degenerate states at energy $E_n$:

$$\sum_{\ell=0}^{n-1}(2\ell+1) = n^2$$

So the ground state is non-degenerate (1 state), the first excited level has 4 degenerate states, the second has 9, and so on.

**Why does this degeneracy exist?** The Coulomb potential $V \propto 1/r$ has an extra, accidental symmetry beyond rotational symmetry — the **Laplace-Runge-Lenz vector** is conserved, giving an additional conserved quantity. By Noether's theorem (Ch. 1 §1.7), this additional symmetry produces the extra degeneracy. This is special to the $1/r$ potential; a perturbed Coulomb potential (e.g., relativistic corrections, spin-orbit coupling) breaks this degeneracy and splits the levels.

---

## 4.10 — Spectroscopy: The Rydberg Formula

When an electron transitions from a higher energy state $n_i$ to a lower state $n_f$, a photon is emitted with energy:

$$h\nu = E_{n_i} - E_{n_f} = 13.6;\text{eV}\left(\frac{1}{n_f^2} - \frac{1}{n_i^2}\right)$$

The corresponding wavelength:

$$\boxed{\frac{1}{\lambda} = R_\infty\left(\frac{1}{n_f^2} - \frac{1}{n_i^2}\right), \qquad R_\infty = \frac{m_e e^4}{8\epsilon_0^2 h^3 c} = 1.097 \times 10^7;\text{m}^{-1}}$$

This is the **Rydberg formula**, empirically discovered in 1888, theoretically derived here. The **Rydberg constant** $R_\infty$ is one of the most precisely measured constants in physics ($R_\infty = 1.0973731568539 \times 10^7,\text{m}^{-1}$) and is used to define the hydrogen energy scale in the SI system.

**Spectral series:**

|Series|$n_f$|Spectral region|Engineering relevance|
|---|---|---|---|
|Lyman|1|Ultraviolet|UV lithography, astrophysics|
|Balmer|2|Visible|The red H-α line at 656 nm; plasma diagnostics|
|Paschen|3|Near infrared|IR spectroscopy|
|Brackett|4|Infrared|Fiber-optic window|

---

## 4.11 — Orbital Notation and Chemists' Language

The quantum numbers $(\ell = 0, 1, 2, 3)$ have spectroscopic labels $(s, p, d, f)$ — a historical accident from "sharp, principal, diffuse, fundamental" series of spectral lines, before quantum mechanics existed.

A state with $n = 2$, $\ell = 1$ is called "2p". The labels you see in chemistry:

|$\ell$|Label|Number of $m$ values|States|
|---|---|---|---|
|0|$s$|1|$m = 0$|
|1|$p$|3|$m = -1, 0, +1$|
|2|$d$|5|$m = -2,-1,0,+1,+2$|
|3|$f$|7|$m = -3,...,+3$|

At $n = 1$: only $1s$ (1 state). At $n = 2$: $2s$ and $2p$ (4 states). At $n = 3$: $3s$, $3p$, $3d$ (9 states).

**Including spin** (from Ch. 3 Bridge A, the Pauli equation): each orbital state splits into spin-up ($m_s = +\frac{1}{2}$) and spin-down ($m_s = -\frac{1}{2}$), doubling the count:

$$\text{Capacity of shell } n = 2n^2$$

Shell $n = 1$ holds 2 electrons, $n = 2$ holds 8, $n = 3$ holds 18. This is **why** the rows of the periodic table have lengths 2, 8, 18, 32...

---

## 4.12 — The Correspondence Principle Revisited

At large $n$, the classical orbit of hydrogen has radius $r_n = n^2 a_0$ and frequency $\nu_n = e^2/(4\pi\epsilon_0 2\hbar n^3)$. The photon frequency emitted in a transition from $n$ to $n-1$:

$$\nu = R_\infty c\left(\frac{1}{(n-1)^2} - \frac{1}{n^2}\right) \xrightarrow{n\to\infty} \frac{2R_\infty c}{n^3} = \nu_n^{classical}$$

At large $n$, the quantum orbital frequency matches the classical orbit frequency exactly. **Quantum mechanics reduces to classical mechanics at large quantum numbers** — the correspondence principle of Ch. 1 §1.8, seen in the hydrogen spectrum.

---

## 4.13 — What This Chapter Has Built

The hydrogen atom solution rests on three pillars, each of which you now have:

**Pillar 1:** The Schrödinger equation — derived in Ch. 3 from $\mathcal{L}_{SM}$

**Pillar 2:** Separation of variables — a mathematical technique for PDEs with symmetric potentials; valid here because $V = V(r)$ only

**Pillar 3:** Boundary conditions imposing quantization — the same principle as the infinite square well, now in 3D with three separate conditions giving three separate quantum numbers

Together they give a complete, exact description of the hydrogen atom that agrees with spectroscopic data to better than one part in $10^8$.

---

## 4.14 — Summary

|Result|Equation|Origin|
|---|---|---|
|Schrödinger equation|$\hat H\psi = E\psi$|Ch. 3 Bridge A|
|Particle in box: energies|$E_n = n^2\pi^2\hbar^2/2mL^2$|Boundary conditions|
|Harmonic oscillator: energies|$E_n = \hbar\omega(n+\frac{1}{2})$|Ladder operators|
|Tunneling transmission|$T \approx e^{-2\kappa d}$|Exponential decay in barrier|
|Hydrogen energies|$E_n = -13.6,\text{eV}/n^2$|Radial equation + normalizability|
|Quantum numbers|$n \geq 1$; $\ell \leq n-1$; $|m|
|Rydberg formula|$1/\lambda = R_\infty(1/n_f^2 - 1/n_i^2)$|Energy conservation for photon emission|
|Shell capacity (with spin)|$2n^2$ electrons per shell|Degeneracy × 2 for spin|

---

## 4.15 — Looking Ahead: Chapter 5

The hydrogen atom has one electron — the problem is exactly solvable. Real atoms have many electrons. Adding them one by one using three facts:

1. The quantum numbers $(n, \ell, m, m_s)$ from this chapter
2. The Pauli exclusion principle from Ch. 0 (anticommutation of fermion fields)
3. The spin from Ch. 3 (Foldy-Wouthuysen, Pauli equation)

...the periodic table falls out completely, without any additional assumptions.

The Zeeman effect, fine structure, and the spectroscopy of real atoms come from the FW correction terms (spin-orbit, Darwin, relativistic mass) that were systematically set aside in §3.5 of Bridge A. Chapter 5 puts them back in.

---

_End of Chapter 4._

---

_Next: Chapter 5 — Spin, Many-Electron Systems, and the Periodic Table_