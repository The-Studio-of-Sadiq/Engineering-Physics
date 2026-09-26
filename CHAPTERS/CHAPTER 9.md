# Bridge B.a — From Quantum Mechanics to Classical Mechanics

### The $\hbar \to 0$ Descent: How Newton Emerges from Schrödinger

---

> _Classical mechanics is not wrong. It is quantum mechanics seen from far away,_ _in the limit where the action is much larger than $\hbar$._ _Every classical trajectory is the stationary phase of a quantum path integral._ — Richard Feynman, _QED: The Strange Theory of Light and Matter_

---

## 9.0 — Bridge B.a in Context

Chapter 8 performed Bridge B.d: the weak-field, slow-motion limit of general relativity giving Newton's gravitational law. This chapter performs Bridge B.a: the $\hbar \to 0$ limit of quantum mechanics giving classical mechanics.

These are **separate, independent limits** — both are part of Bridge B, running simultaneously. The complete Layer-2 picture requires all five Bridge B operations (B.a through B.e) to run in parallel. Chapter 9 handles B.a alone; the others follow in Chapters 10, 11, and 13.

**The descent in this chapter:**

```
Layer 1: Quantum mechanics
         ψ satisfies iħ ∂ψ/∂t = Ĥψ
              │
              │  ħ → 0
              │  (action S ≫ ħ)
              │
              ▼
Bridge zone: WKB approximation (§9.3)
         ψ ≈ A(r,t) exp(iS(r,t)/ħ)
         leading order → Hamilton-Jacobi equation
              │
              │  wavepacket width Δx → 0
              │  (V varies slowly over Δx)
              │
              ▼
Layer 2: Classical mechanics
         Euler-Lagrange, Hamilton's equations, Newton's 2nd law
```

A critical point: the classical mechanics recovered here is not a separate subject patched onto quantum mechanics. It is **the same physical law**, expressed in the language appropriate to the regime $S \gg \hbar$.

---

## 9.1 — Ehrenfest's Theorem: The First Sign of Newton

### 9.1.1 — The General Theorem

For any quantum observable $\hat A$ (not explicitly time-dependent):

$$\frac{d\langle\hat A\rangle}{dt} = \frac{d}{dt}\int\psi^*\hat A\psi,d^3r$$

Using the Schrödinger equation $i\hbar,\partial_t\psi = \hat H\psi$ and its conjugate:

$$\boxed{\frac{d\langle\hat A\rangle}{dt} = \frac{i}{\hbar}\langle[\hat H, \hat A]\rangle + \left\langle\frac{\partial\hat A}{\partial t}\right\rangle}$$

This is **Ehrenfest's theorem** — the quantum analog of Hamilton's equation of motion $\dot f = {f, H}_{Poisson} + \partial f/\partial t$. Replacing the Poisson bracket with $(i/\hbar)\times$commutator is canonical quantization (Ch. 1 §1.6.4) operating in reverse: here we see the quantum equation reducing to the classical one.

### 9.1.2 — Recovering Newton's Second Law

Apply Ehrenfest's theorem to position and momentum, with $\hat H = \hat p^2/2m + V(\mathbf{r})$:

**For position $\hat x$:** $$[\hat H, \hat x] = [\hat p^2/2m, \hat x] = \frac{1}{2m}[\hat p^2, \hat x] = \frac{1}{2m}(\hat p[\hat p, \hat x] + [\hat p, \hat x]\hat p) = \frac{-i\hbar\hat p}{m}$$

Therefore: $$\frac{d\langle\hat x\rangle}{dt} = \frac{i}{\hbar}\left\langle\frac{-i\hbar\hat p}{m}\right\rangle = \frac{\langle\hat p\rangle}{m}$$

This is exactly Newton's kinematic relation $v = p/m$, now holding for expectation values. **A quantum wavepacket moves like a classical particle, at least in this sense.**

**For momentum $\hat p$:** $$[\hat H, \hat p] = [V(\mathbf{r}), \hat p] = V(\mathbf{r})(-i\hbar\nabla) - (-i\hbar\nabla)V(\mathbf{r}) = i\hbar\nabla V$$

Therefore: $$\boxed{\frac{d\langle\hat p\rangle}{dt} = -\left\langle\nabla V(\hat{\mathbf{r}})\right\rangle}$$

This is almost Newton's second law $\dot p = -\nabla V = F$, but not quite: the right side is $-\langle\nabla V\rangle$, not $-\nabla V(\langle\mathbf{r}\rangle)$.

### 9.1.3 — The Classical Limit Condition

When do these become identical?

Taylor expand $\nabla V(\mathbf{r})$ around $\langle\mathbf{r}\rangle$:

$$\langle\nabla V\rangle = \nabla V!\big|_{\langle\mathbf{r}\rangle}

- \frac{1}{2}\langle(\Delta\mathbf{r})^2\rangle\nabla^3 V!\big|_{\langle\mathbf{r}\rangle} + \cdots$$

The correction term involves $(\Delta x)^2 V''' \sim (\Delta x)^2/L_V^3$ where $L_V$ is the scale over which $V$ varies. This is negligible when:

$$\boxed{\Delta x \ll L_V}$$

**The wavepacket must be narrow compared to the scale over which the potential varies.** When this holds: $$\frac{d\langle\mathbf{p}\rangle}{dt} \approx -\nabla V(\langle\mathbf{r}\rangle) = \mathbf{F}(\langle\mathbf{r}\rangle)$$

This is Newton's second law — the expectation values of position and momentum of a narrow quantum wavepacket obey classical equations of motion.

**What controls the wavepacket width?** The uncertainty principle (Ch. 3 §3.11) requires $\Delta x,\Delta p \geq \hbar/2$. As $\hbar\to 0$, the minimum wavepacket width goes to zero — a perfectly sharp classical trajectory. For macroscopic objects, $\hbar/S_{action} \sim 10^{-34}$ J·s / (1 kg × 1 m/s × 1 m) $= 10^{-34}$ — the wavepacket is effectively a point.

---

## 9.2 — The Path Integral and Stationary Phase

### 9.2.1 — The Feynman Path Integral

From quantum mechanics (the rigorous formulation), the amplitude for a particle to travel from $(\mathbf{r}_a, t_a)$ to $(\mathbf{r}_b, t_b)$ is:

$$K(\mathbf{r}_b, t_b;,\mathbf{r}_a, t_a) = \int_{\text{all paths}} \mathcal{D}\mathbf{r}(t),\exp!\left(\frac{i}{\hbar}S[\mathbf{r}(t)]\right)$$

where $S[\mathbf{r}(t)] = \int_{t_a}^{t_b} L(\mathbf{r},\dot{\mathbf{r}},t),dt$ is the classical action (Ch. 1 §1.4) evaluated along each possible path, and the integral runs over **all continuous paths** connecting the endpoints — not just the classical one.

Every path contributes equally in magnitude but with a phase $e^{iS/\hbar}$. Paths of very different action have rapidly oscillating phases that cancel.

### 9.2.2 — Stationary Phase: $\hbar \to 0$

As $\hbar \to 0$, the phase $S/\hbar$ oscillates infinitely rapidly for any variation of the path. Neighboring paths cancel by destructive interference — **except near the path where $S$ is stationary**, where neighboring paths have nearly the same phase and interfere constructively.

The condition $\delta S = 0$ — stationary action — is exactly the **Euler-Lagrange equation** (Ch. 1 §1.5). The dominant contribution to $K$ comes from the classical trajectory $\mathbf{r}_{cl}(t)$:

$$K \xrightarrow{\hbar\to 0} A(\mathbf{r}_b,\mathbf{r}_a,t),\exp!\left(\frac{i}{\hbar}S_{cl}[\mathbf{r}_{cl}(t)]\right)$$

where $A$ is a slowly-varying prefactor from the Gaussian integral over fluctuations around the classical path.

**The physical statement:** In the classical limit, a particle takes the single path of stationary action. In the quantum world, it takes all paths. Classical mechanics is the stationary-phase approximation of quantum mechanics.

This is the answer to the question raised in Ch. 1 §1.4.2: _Why should $\delta S = 0$?_ Because nature is quantum. The classical trajectory is the path that survives when all other paths cancel by interference as $\hbar/S \to 0$.

---

## 9.3 — The WKB Approximation: The Bridge Zone

### 9.3.1 — The WKB Ansatz

Write the wavefunction as:

$$\psi(\mathbf{r}, t) = A(\mathbf{r},t),\exp!\left(\frac{i}{\hbar}S(\mathbf{r},t)\right)$$

where $A(\mathbf{r},t)$ is a real amplitude and $S(\mathbf{r},t)$ is a real phase. Substituting into the Schrödinger equation and separating real and imaginary parts, collecting terms by power of $\hbar$:

**Order $\hbar^0$ (leading order):**

$$\frac{\partial S}{\partial t} + \frac{|\nabla S|^2}{2m} + V = 0$$

This is the **Hamilton-Jacobi equation** (Ch. 1 §1.8.1). The quantum phase $S$ satisfies the classical equation for Hamilton's principal function. The HJ equation is exactly what the Schrödinger equation reduces to in the limit $\hbar \to 0$ — confirming that classical mechanics is the ħ→0 limit.

**Order $\hbar^1$ (next order):**

$$\frac{\partial A^2}{\partial t} + \nabla\cdot!\left(A^2\frac{\nabla S}{m}\right) = 0$$

This is the **continuity equation** for the probability density $\rho = A^2 = |\psi|^2$, with current density $\mathbf{J} = A^2\nabla S/m = |\psi|^2\mathbf{v}_{cl}$. Probability is conserved — as it must be by Noether's theorem (Ch. 1 §1.7).

**Order $\hbar^2$ (purely quantum correction):**

$$\text{Quantum potential: }Q = -\frac{\hbar^2}{2m}\frac{\nabla^2 A}{A}$$

This term — sometimes called the **Bohm potential** — vanishes as $\hbar\to 0$. It is responsible for tunneling (the wavefunction penetrates barriers where $E < V$, giving imaginary $p$ and an evanescent wave), interference, and zero-point energy. Setting $Q = 0$ is the WKB approximation.

### 9.3.2 — The WKB Wavefunction

In one dimension, the HJ equation gives $p(x) = \partial S/\partial x = \sqrt{2m(E-V(x))}$. The WKB wavefunction in a classically allowed region ($E > V$):

$$\psi_{WKB}(x) = \frac{C}{\sqrt{p(x)}}\exp!\left(\pm\frac{i}{\hbar}\int^x p(x'),dx'\right)$$

In a classically forbidden region ($E < V$), $p \to i\kappa$ where $\kappa = \sqrt{2m(V-E)}/\hbar$:

$$\psi_{WKB}(x) = \frac{C}{\sqrt{\kappa(x)}}\exp!\left(\mp\int^x\kappa(x'),dx'\right)$$

### 9.3.3 — Validity Criterion

WKB is valid when the de Broglie wavelength $\lambda = h/p$ changes slowly over one wavelength — i.e., when the potential is nearly constant locally:

$$\left|\frac{d\lambda}{dx}\right| \ll 1 \qquad\Longleftrightarrow\qquad \frac{\hbar}{p^2}\left|\frac{dp}{dx}\right| \ll 1$$

This fails at **classical turning points** ($p = 0$) where $\lambda \to \infty$. Connection formulas (derived by matching to exact Airy function solutions near the turning point) bridge the oscillatory and evanescent WKB solutions.

### 9.3.4 — WKB Applications

**Bohr-Sommerfeld quantization** (the semiclassical bridge): For a particle in a potential well, matching the WKB solutions at both turning points:

$$\oint p,dq = \left(n + \frac{1}{2}\right)h, \qquad n = 0, 1, 2, \ldots$$

The $\frac{1}{2}$ is the **Maslov correction** from the phase shift at turning points — it gives the zero-point energy automatically. For the harmonic oscillator: $\oint p,dq = 2\pi m\omega E/\omega^2 = 2\pi E/\omega = (n+\frac{1}{2})h$, recovering $E_n = \hbar\omega(n+\frac{1}{2})$ exactly.

**Geometric optics as WKB:** In the limit of short wavelength, electromagnetic waves (governed by Maxwell's equations in Layer 2) satisfy a WKB-like equation. The eikonal equation $|\nabla S|^2 = n^2(\mathbf{r})$ is the HJ equation for photons with $p = n(\mathbf{r})\hbar\omega/c$. Fermat's principle of least time is the stationary phase of the wave equation. **Optics is the $\lambda \to 0$ limit of electromagnetism, just as classical mechanics is the $\hbar \to 0$ limit of quantum mechanics — the mathematical structure is identical.**

---

## 9.4 — Coherent States: Quantum States That Look Classical

### 9.4.1 — The Most Classical Quantum State

A **coherent state** $|\alpha\rangle$ of the harmonic oscillator is the eigenstate of the lowering operator $\hat a_- |\alpha\rangle = \alpha|\alpha\rangle$ for complex $\alpha = |\alpha|e^{i\phi}$.

Properties:

- $\langle\hat x\rangle(t) = x_0\cos(\omega t + \phi)$ — classical oscillatory motion
- $\langle\hat p\rangle(t) = -m\omega x_0\sin(\omega t + \phi)$ — classical momentum
- $\Delta x = \sqrt{\hbar/2m\omega}$ and $\Delta p = \sqrt{m\omega\hbar/2}$ — constant, minimum uncertainty
- $\Delta x,\Delta p = \hbar/2$ — saturates the uncertainty principle at all times

A coherent state is a **minimum-uncertainty Gaussian wavepacket** that follows the classical trajectory without spreading. It is the quantum state that most closely resembles a classical particle in a harmonic potential.

### 9.4.2 — Decoherence: Why Macroscopic Objects Are Classical

A quantum superposition of macroscopically distinct states (the "Schrödinger's cat" state) rapidly loses its quantum coherence due to entanglement with environmental degrees of freedom.

For a system interacting with an environment at temperature $T$: $$\tau_{decoherence} \sim \frac{\hbar}{k_BT}\left(\frac{\lambda_{dB}}{\Delta x}\right)^2$$

where $\Delta x$ is the spatial separation between the superposed states and $\lambda_{dB} = h/\sqrt{2mkT}$ is the thermal de Broglie wavelength.

For a 1 g dust particle with $\Delta x = 1$ μm in air at 300 K: $$\tau_{decoherence} \sim 10^{-31};\text{s}$$

The coherence is destroyed in a time far shorter than any observable timescale. This is why macroscopic objects always appear classical — their quantum superpositions decohere before they can be measured. **Classical mechanics is not just $\hbar\to 0$; it is also the open quantum system limit**, where the environment continuously measures and collapses the quantum state.

This decoherence picture will be developed fully in Ch. 10 (Bridge B.b), where tracing out environmental degrees of freedom is the operation that produces statistical mechanics from quantum mechanics.

---

## 9.5 — Lagrangian Mechanics as a Classical Tool

The Lagrangian was derived in Ch. 1 and used to demonstrate Newton's law in Ch. 1 §1.5.2. In this chapter it becomes a working tool for engineering dynamics problems.

### 9.5.1 — The Method

For any mechanical system:

1. Choose $n$ generalized coordinates $q_1, \ldots, q_n$ (fewest independent parameters that specify the configuration)
2. Write $T$ and $V$ in these coordinates
3. Form $L = T - V$
4. Apply Euler-Lagrange: $\frac{d}{dt}\frac{\partial L}{\partial\dot q_i} - \frac{\partial L}{\partial q_i} = 0$

Constraint forces never appear. The approach is coordinate-free: it produces the same equations of motion regardless of which valid $q_i$ you choose.

### 9.5.2 — The Charged Particle in an EM Field

The Lagrangian for a particle of charge $q$ and mass $m$ in fields $(\phi, \mathbf{A})$ (from Ch. 3 §5.3 — minimal coupling in the Schrödinger equation, now in the classical limit):

$$L = \frac{1}{2}m|\dot{\mathbf{r}}|^2 - q\phi(\mathbf{r},t) + q\dot{\mathbf{r}}\cdot\mathbf{A}(\mathbf{r},t)$$

Applying Euler-Lagrange to coordinate $x$:

$$\frac{d}{dt}(m\dot x + qA_x) = q\dot{\mathbf{r}}\cdot\frac{\partial\mathbf{A}}{\partial x} - q\frac{\partial\phi}{\partial x}$$

Expanding using $\mathbf{E} = -\nabla\phi - \partial_t\mathbf{A}$ and $\mathbf{B} = \nabla\times\mathbf{A}$:

$$m\ddot x = q(E_x + \dot y B_z - \dot z B_y) = q(\mathbf{E} + \dot{\mathbf{r}}\times\mathbf{B})_x$$

This is the **Lorentz force law** — recovered from the Lagrangian with no additional input. The same Lagrangian term $q\dot{\mathbf{r}}\cdot\mathbf{A}$ that appeared as minimal coupling in quantum mechanics (Ch. 3) gives the Lorentz force in the classical limit. The physics is continuous across Bridge B.a.

### 9.5.3 — The Double Pendulum

Two masses $m_1$, $m_2$ on strings of length $\ell_1$, $\ell_2$, angles $\theta_1$, $\theta_2$:

$$T = \frac{1}{2}(m_1+m_2)\ell_1^2\dot\theta_1^2 + m_2\ell_2^2\dot\theta_2^2 + m_2\ell_1\ell_2\dot\theta_1\dot\theta_2\cos(\theta_1-\theta_2)$$

$$V = -(m_1+m_2)g\ell_1\cos\theta_1 - m_2 g\ell_2\cos\theta_2$$

Applying Euler-Lagrange gives two coupled nonlinear ODEs — the equations of motion for the double pendulum. These cannot be derived from Newton's law without first computing the tension in both strings (constraint forces). The Lagrangian approach is not just elegant; it is simpler.

For small oscillations (§9.7 below), the double pendulum has two normal modes. For large oscillations, it is **chaotic** — sensitive to initial conditions, with adjacent trajectories diverging exponentially. This is the first appearance of chaos in the book. We will return to it briefly in §9.9.

---

## 9.6 — Hamiltonian Mechanics and Phase Space

### 9.6.1 — Phase Space

The state of a mechanical system with $n$ degrees of freedom is a point in **phase space** $\Gamma = {(q_1,\ldots,q_n,,p_1,\ldots,p_n)}$ — a $2n$-dimensional space. Hamilton's equations (Ch. 1 §1.6.3):

$$\dot q_i = \frac{\partial H}{\partial p_i}, \qquad \dot p_i = -\frac{\partial H}{\partial q_i}$$

define a **flow** on phase space. Every initial condition maps to a unique trajectory. Trajectories never cross (uniqueness of solutions to ODEs with smooth $H$).

**Phase space portraits** for the harmonic oscillator ($H = p^2/2m + \frac{1}{2}m\omega^2 q^2$):

- Trajectories are ellipses $E = \text{const}$ in the $(q, p)$ plane
- All motion is periodic; no chaos possible for one degree of freedom
- Trajectory frequency: $\omega$ (independent of amplitude — special to harmonic oscillator)

For the pendulum ($H = p^2/2m\ell^2 - mg\ell\cos\theta$):

- Small energy: ellipses (harmonic approximation)
- Energy $= 2mg\ell$: **separatrix** — the figure-eight curve separating libration (bounded oscillation) from rotation (complete loops)
- Large energy: rotation trajectories (pendulum spins over the top)
- The separatrix itself is a **homoclinic orbit** — asymptotically approaches the unstable equilibrium as $t\to\pm\infty$; infinite period

### 9.6.2 — Liouville's Theorem

The phase space flow is **incompressible**: the volume occupied by any ensemble of initial conditions is conserved under Hamilton's equations.

$$\frac{d}{dt}\int_\Omega d^{2n}(q,p) = 0 \qquad\Longleftrightarrow\qquad \frac{\partial\rho}{\partial t} + {H, \rho} = 0$$

where $\rho(q,p,t)$ is the phase space density and ${\cdot,\cdot}$ is the Poisson bracket. This is the **classical Liouville equation**.

**Why this matters for Ch. 10:** The quantum analog of the Liouville equation is the **von Neumann equation** for the density matrix:

$$\frac{\partial\hat\rho}{\partial t} = -\frac{i}{\hbar}[\hat H, \hat\rho]$$

This is the quantum Liouville equation — the Poisson bracket replaced by the commutator (same canonical quantization rule as always). Bridge B.b (Ch. 10) takes the quantum Liouville equation, applies $N\to\infty$ and traces over unobserved degrees of freedom, to get thermodynamics.

**Engineering application:** Liouville's theorem governs the performance of optical and particle beam systems. A beam of particles (or photons) occupies a volume of phase space $(x,p_x,y,p_y)$. This volume — called **emittance** or **étendue** — is conserved by any lossless optical element (lens, mirror, waveguide). You cannot focus a beam to have smaller emittance than it started with; you can only redistribute phase space volume, not reduce it.

### 9.6.3 — Action-Angle Variables

For an integrable system (one with as many conserved quantities as degrees of freedom), a canonical transformation $(q_i, p_i) \to (J_i, \theta_i)$ exists where:

- $J_i = \frac{1}{2\pi}\oint p_i,dq_i$ are the **action variables** — adiabatic invariants
- $H = H(J_1, \ldots, J_n)$ — the Hamiltonian depends only on $J_i$
- $\dot\theta_i = \partial H/\partial J_i = \omega_i(J) = \text{const}$ — all angles evolve uniformly
- $\dot J_i = -\partial H/\partial\theta_i = 0$ — all action variables are constants of motion

The motion is **quasi-periodic** (superposition of oscillations at the fundamental frequencies $\omega_i$). For the harmonic oscillator: $J = E/\omega$ (the adiabatic invariant) and $\theta = \omega t$.

**Adiabatic invariance:** If parameters of the Hamiltonian change slowly (over many oscillation periods), the action $J$ is conserved even though $E$ changes. This governs:

- Plasma confinement (charged particle mirrors in magnetic bottles)
- Adiabatic demagnetization (reaching millikelvin temperatures)
- Quantum connection: $J = (n+\frac{1}{2})\hbar$ — the Bohr-Sommerfeld condition from §9.3.4 is adiabatic invariance at the quantum level

---

## 9.7 — Rigid Body Dynamics

### 9.7.1 — The Inertia Tensor

A rigid body with density $\rho(\mathbf{r})$ rotating with angular velocity $\boldsymbol{\omega}$ has angular momentum:

$$L_i = \sum_j I_{ij}\omega_j, \qquad I_{ij} = \int\rho(\mathbf{r})\left(|\mathbf{r}|^2\delta_{ij} - r_i r_j\right)d^3r$$

The **inertia tensor** $I_{ij}$ is a $3\times3$ symmetric matrix — a generalized version of the scalar moment of inertia $I = mr^2$ for rotation about a fixed axis.

In the **principal axis frame** (the frame in which $I_{ij}$ is diagonal):

$$I_{ij} = \text{diag}(I_1, I_2, I_3)$$

The principal moments $I_1, I_2, I_3$ are the eigenvalues of $I_{ij}$; the eigenvectors are the principal axes. Every rigid body has a unique set of principal axes through its center of mass.

**Computing principal moments:**

|Body|Symmetry|$I_1 = I_2$|$I_3$|
|---|---|---|---|
|Uniform sphere (radius $R$)|$I_1=I_2=I_3$|$\frac{2}{5}mR^2$|$\frac{2}{5}mR^2$|
|Thin rod (length $\ell$, axis = 3)|$I_1=I_2 \gg I_3$|$\frac{1}{12}m\ell^2$|$\approx 0$|
|Disk (radius $R$, axis = 3)|$I_1=I_2=\frac{1}{2}I_3$|$\frac{1}{4}mR^2$|$\frac{1}{2}mR^2$|
|Cylinder (radius $R$, length $\ell$)|$I_1 = I_2$|$\frac{m}{12}(3R^2+\ell^2)$|$\frac{1}{2}mR^2$|

**Parallel axis theorem:** If $I_{cm}$ is the moment about the center of mass, the moment about a parallel axis at distance $d$ is: $$I = I_{cm} + md^2$$

### 9.7.2 — Euler's Equations

In the **body frame** (rotating with the body), Newton's law for rotational motion:

$$\boxed{I_1\dot\omega_1 - (I_2-I_3)\omega_2\omega_3 = \tau_1}$$ $$\boxed{I_2\dot\omega_2 - (I_3-I_1)\omega_3\omega_1 = \tau_2}$$ $$\boxed{I_3\dot\omega_3 - (I_1-I_2)\omega_1\omega_2 = \tau_3}$$

These are **Euler's equations** — the equations of motion for rotational dynamics in the principal axis (body) frame. They are three coupled, nonlinear ODEs in general.

**Torque-free symmetric body** ($\tau = 0$, $I_1 = I_2 \neq I_3$, e.g., a football):

From Euler's equations: $\omega_3 = \text{const}$ (spin about symmetry axis is constant). The transverse components satisfy:

$$\dot\omega_1 = -\Omega_b\omega_2, \qquad \dot\omega_2 = +\Omega_b\omega_1$$

where $\Omega_b = \omega_3(I_3 - I_1)/I_1$ is the **body precession frequency**.

Solution: $\omega_1 = A\sin(\Omega_b t)$, $\omega_2 = A\cos(\Omega_b t)$ — the angular velocity vector traces a **body cone** at rate $\Omega_b$ around the symmetry axis.

In the **space frame**, the symmetry axis simultaneously precesses around the fixed angular momentum vector $\mathbf{L}$ at the **space precession frequency** $\Omega_s = L/I_1$. This is **torque-free precession** — the wobble of Earth's rotation axis relative to its geographic pole (the Chandler wobble, period ~14 months).

### 9.7.3 — The Gyroscope

A spinning gyroscope with large angular momentum $\mathbf{L} = I\boldsymbol{\omega}$ ($I\omega \gg$ other angular momenta) subject to a torque $\boldsymbol{\tau}$:

$$\boldsymbol{\tau} = \frac{d\mathbf{L}}{dt}$$

For a gyroscope with spin axis making angle $\theta$ with the vertical, weight $mg$ acting at distance $r$ from the pivot:

$$|\boldsymbol{\tau}| = mgr\sin\theta$$

The angular momentum is large and nearly fixed in direction, so $d\mathbf{L}/dt$ is perpendicular to $\mathbf{L}$. The spin axis **precesses** around the vertical:

$$\boxed{\Omega_{prec} = \frac{mgr}{I\omega}}$$

**Engineering applications:**

- Gyroscopic stabilization: the faster the spin, the slower the precession, the more stable the platform
- Gyrocompasses: precess to align with Earth's rotation axis (geographic North)
- MEMS gyroscopes (ADXRS, ITG-3200): vibrating ring or fork structures measuring Coriolis force on oscillating mass — in every smartphone
- Attitude control on spacecraft: control moment gyroscopes (CMGs) exert torques to orient the spacecraft

---

## 9.8 — Small Oscillations and Normal Modes

### 9.8.1 — The General Setup

Any stable mechanical equilibrium can be treated as a collection of coupled harmonic oscillators for small displacements. Near equilibrium ${q_i^{(0)}}$, expand $T$ and $V$ to second order in displacements $\eta_i = q_i - q_i^{(0)}$:

$$T = \frac{1}{2}\sum_{i,j}T_{ij}\dot\eta_i\dot\eta_j, \qquad V = V_0 + \frac{1}{2}\sum_{i,j}V_{ij}\eta_i\eta_j$$

where $T_{ij}$ and $V_{ij}$ are the kinetic and potential energy matrices (symmetric, positive-definite for a stable equilibrium).

The Euler-Lagrange equations:

$$\sum_j(T_{ij}\ddot\eta_j + V_{ij}\eta_j) = 0$$

### 9.8.2 — Normal Mode Eigenvalue Problem

Try $\boldsymbol{\eta}(t) = \mathbf{A}\cos(\omega t + \phi)$:

$$\left(\mathbf{V} - \omega^2\mathbf{T}\right)\mathbf{A} = \mathbf{0}$$

Non-trivial solution requires:

$$\boxed{\det!\left(\mathbf{V} - \omega^2\mathbf{T}\right) = 0}$$

This gives $n$ normal frequencies $\omega_k^2$ (eigenvalues) and $n$ normal mode vectors $\mathbf{A}^{(k)}$ (eigenvectors). Each normal mode is an independent oscillation in which all coordinates move at the same frequency $\omega_k$.

**Properties of normal modes:**

- Modes are orthogonal with respect to $T$: $\mathbf{A}^{(j)T}\mathbf{T}\mathbf{A}^{(k)} = \delta_{jk}$
- A zero frequency $\omega = 0$ corresponds to a **zero mode** — a rigid body translation or rotation
- In normal coordinates $Q_k$, the system decouples into $n$ independent harmonic oscillators

### 9.8.3 — Example: Coupled Pendulums

Two identical pendulums of length $\ell$, mass $m$, connected by a spring of constant $k$ at their midpoints. Generalized coordinates: $\theta_1$, $\theta_2$.

$$T_{ij} = m\ell^2\delta_{ij}, \qquad V_{ij} = \begin{pmatrix}mg\ell + k\ell^2/4 & -k\ell^2/4\-k\ell^2/4 & mg\ell + k\ell^2/4\end{pmatrix}$$

Normal frequencies:

$$\omega_1^2 = \frac{g}{\ell} \quad\text{(in-phase: spring doesn't stretch)}$$ $$\omega_2^2 = \frac{g}{\ell} + \frac{k}{2m} \quad\text{(out-of-phase: spring fully engaged)}$$

Normal modes:

- Mode 1: $(\theta_1, \theta_2) \propto (1, 1)$ — pendulums swing together
- Mode 2: $(\theta_1, \theta_2) \propto (1, -1)$ — pendulums swing opposite

This is the classical analog of bonding/antibonding molecular orbitals (Ch. 5 §5.8.1):

- In-phase combination = lower frequency = bonding orbital
- Out-of-phase combination = higher frequency = antibonding orbital

The mathematical structure is identical.

### 9.8.4 — Connection to Phonons (Ch. 6)

For $N$ atoms in a crystal, each atom is displaced from equilibrium and interacts with its neighbors through a potential expanded to second order in displacements. The result is exactly the normal mode eigenvalue problem with $3N$ coordinates.

The $3N$ normal mode frequencies give the **phonon dispersion relation** $\omega_k(\mathbf{q})$ (Ch. 6 §6.7): the $3N$ normal modes of the classical crystal become $3N$ quantum harmonic oscillators upon quantization, each with energy $\hbar\omega_k(n_k + \frac{1}{2})$. **Phonons are the quantum particles of the normal mode vibration field.**

The chain from Ch. 0 → Ch. 6 → Ch. 9 is explicit: the SM Lagrangian's matter fields give atomic bonding (Ch. 5); atomic bonding gives the crystal potential; the crystal potential quantized gives phonons (Ch. 6); the classical normal mode analysis of the crystal gives the phonon dispersion (this chapter).

---

## 9.9 — Non-Inertial Reference Frames

### 9.9.1 — The Rotating Frame

In a frame rotating with angular velocity $\boldsymbol{\Omega}$ relative to an inertial frame, the time derivative of any vector $\mathbf{A}$ transforms as:

$$\left(\frac{d\mathbf{A}}{dt}\right)_{inertial} = \left(\frac{d\mathbf{A}}{dt}\right)_{rot} + \boldsymbol{\Omega}\times\mathbf{A}$$

Applying this to the position and velocity, Newton's second law in the rotating frame:

$$\boxed{m\mathbf{a}_{rot} = \mathbf{F} \underbrace{- 2m\boldsymbol{\Omega}\times\mathbf{v}_{rot}}_{\text{Coriolis}} \underbrace{- m\boldsymbol{\Omega}\times(\boldsymbol{\Omega}\times\mathbf{r})}_{\text{centrifugal}} \underbrace{- m\dot{\boldsymbol{\Omega}}\times\mathbf{r}}_{\text{Euler force}}}$$

**Coriolis force** $-2m\boldsymbol{\Omega}\times\mathbf{v}_{rot}$:

- Acts perpendicular to velocity in the rotating frame
- Deflects moving objects to the right (Northern hemisphere) or left (Southern)
- Responsible for the rotation direction of cyclones and anticyclones
- Zero for stationary objects

**Centrifugal force** $-m\boldsymbol{\Omega}\times(\boldsymbol{\Omega}\times\mathbf{r}) = m\Omega^2\mathbf{r}_\perp$:

- Acts outward, perpendicular to rotation axis
- Modifies effective gravity: $\mathbf{g}_{eff} = \mathbf{g} - \boldsymbol{\Omega}\times(\boldsymbol{\Omega}\times\mathbf{r})$
- Makes Earth oblate at the equator: equatorial radius 21 km larger than polar

### 9.9.2 — Connection to Chapter 8

These fictitious forces are not mysterious — they are Christoffel symbol terms in the geodesic equation (Ch. 8 §8.1) evaluated in a non-inertial coordinate system. Specifically, in a uniformly rotating coordinate system:

$$\Gamma^i_{0j} \sim \epsilon_{ijk}\Omega^k \quad\Longrightarrow\quad -c^2\Gamma^i_{0j}\frac{dx^j}{dt} = -2\boldsymbol{\Omega}\times\mathbf{v}_{rot}$$

The Coriolis force is the gravitomagnetic term in the metric. For slow rotation ($\Omega \ll c/R$), it is purely a coordinate artifact — exactly what "fictitious force" means. In GR, fictitious forces and gravity are unified as curvature.

### 9.9.3 — The Foucault Pendulum

A pendulum free to swing in any direction, at latitude $\lambda$:

The effective angular velocity vector in the local vertical frame: $\boldsymbol{\Omega}_{vert} = \Omega_{Earth}\sin\lambda,\hat z$

The Coriolis force on the pendulum causes the plane of oscillation to precess:

$$\Omega_{prec} = -\Omega_{Earth}\sin\lambda$$

- At the North Pole ($\lambda = 90°$): full rotation in 24 hours (sidereal day)
- At the equator ($\lambda = 0°$): no precession
- At latitude 45°N (Paris, where Foucault demonstrated in 1851): rotation period $= 24/\sin(45°) = 33.9$ hours
- At latitude 53°N (Hamburg): period $= 24/\sin(53°) = 30.1$ hours

**Engineering applications of Coriolis:**

- Flow meters (Coriolis mass flowmeters): fluid forced to rotate deflects due to Coriolis; deflection ∝ mass flow rate. Precision: 0.1% of reading.
- MEMS gyroscopes: vibrating proof mass deflected by Coriolis when device rotates; capacitive sensing of deflection gives angular rate. Used in phones, cars, aircraft, missiles.
- Ballistic trajectory correction: long-range projectiles deflected $\sim$ meters by Coriolis over km-scale trajectories.

---

## 9.10 — Chaos: The Boundary of Classical Predictability

### 9.10.1 — Integrable vs. Non-Integrable Systems

An $n$-degree-of-freedom system is **integrable** if it has $n$ independent conserved quantities in involution (${F_i, F_j} = 0$). By the Liouville-Arnold theorem, such systems can be transformed to action-angle variables (§9.6.3), and all motion is quasi-periodic on $n$-dimensional tori in phase space.

A system with fewer than $n$ independent conserved quantities is **non-integrable**. For these systems, the KAM (Kolmogorov-Arnold-Moser) theorem says:

- Most phase space tori survive small perturbations (KAM tori)
- Some tori (those with rational frequency ratios $\omega_1/\omega_2 = p/q$) are destroyed and replaced by chains of islands and chaotic regions
- As perturbation grows, more tori are destroyed; eventually large regions become chaotic

### 9.10.2 — Sensitive Dependence and Lyapunov Exponents

In a chaotic region, nearby trajectories diverge exponentially:

$$|\delta\mathbf{x}(t)| \approx |\delta\mathbf{x}(0)|,e^{\lambda t}$$

where $\lambda > 0$ is the **largest Lyapunov exponent**. For the double pendulum: $\lambda^{-1} \sim 1/\omega$ for large-angle motion — predictability horizon is only a few oscillation periods.

**The weather:** Earth's atmosphere is a non-integrable fluid system. Lyapunov exponent corresponds to predictability limit of $\sim 2$ weeks. No amount of computing power overcomes this; it is a fundamental feature of nonlinear dynamics.

### 9.10.3 — Engineering Relevance

- **Mechanical systems:** Fatigue failure can be triggered by chaotic vibration in structures near homoclinic bifurcations
- **Power electronics:** DC-DC converters with fast switching can exhibit chaotic oscillations — undesirable in precision applications, studied in circuit design
- **Chemical reactors:** Belousov-Zhabotinsky oscillating reactions; chaotic mixing enhances reaction rates
- **Quantum chaos:** Statistical properties of quantum energy spectra in classically chaotic systems follow random matrix theory — relevant to quantum transport in mesoscopic devices

---

## 9.11 — Summary

Bridge B.a is complete. The descent from quantum mechanics to classical mechanics:

|Step|Mathematical operation|Result|
|---|---|---|
|Ehrenfest theorem|Commutator → Poisson bracket|$d\langle p\rangle/dt = -\langle\nabla V\rangle$|
|Classical limit condition|$\Delta x \ll L_V$|$d\langle p\rangle/dt = -\nabla V(\langle x\rangle) = F$|
|Path integral, $\hbar\to 0$|Stationary phase|Classical trajectory = $\delta S = 0$ path|
|WKB, order $\hbar^0$|Substitute $\psi = Ae^{iS/\hbar}$|Hamilton-Jacobi equation|
|WKB, order $\hbar^1$|Next order|Continuity equation for $|
|Normal modes|$T$, $V$ matrices → eigenvalue problem|Classical phonon dispersion|
|Rigid body|Euler-Lagrange for rotation|Euler's equations, gyroscope precession|
|Rotating frame|Coordinate transformation|Coriolis + centrifugal forces|

**What was discarded and when it matters:**

|Discarded|Physical content|Reinstated when|
|---|---|---|
|$Q = -\hbar^2\nabla^2 A/2mA$|Tunneling, zero-point energy, interference|$\Delta x \sim \lambda_{dB}$: quantum devices, atoms|
|Wavepacket spread|Uncertainty principle, quantum diffraction|Sub-nm scales, cold atoms|
|Quantum decoherence dynamics|Quantum-to-classical transition|Quantum computing, mesoscopic physics|
|Non-classical correlations|Entanglement, Bell inequality violations|Quantum information, precision sensing|

---

## 9.12 — Engineering Thread

|Physics from this chapter|Engineering application|
|---|---|
|Euler-Lagrange mechanics|Robotics dynamics, cable systems, spacecraft attitude|
|Hamilton's equations + phase space|Nonlinear dynamics, control system design|
|Liouville's theorem|Étendue conservation in optical systems; particle beam emittance|
|Action-angle + adiabatic invariance|Plasma magnetic mirror; adiabatic demagnetization refrigeration|
|Rigid body inertia tensor|Rotating machinery balancing; spacecraft moment of inertia|
|Euler's equations|Attitude control; gyroscope design|
|Gyroscope precession $\Omega_{prec} = mgr/I\omega$|Gyrocompasses; MEMS rate gyroscopes; CMGs|
|Normal modes|Vibration analysis; structural resonance; noise suppression|
|Coupled normal modes → phonons|Connects to thermal conductivity, specific heat (Ch. 10)|
|Coriolis force|Coriolis flow meters; MEMS gyroscopes; ballistics|
|Chaos / Lyapunov exponent|Predictability limits; robust control design; fatigue|

---

## 9.13 — Looking Ahead

Chapter 9 has descended from quantum mechanics to classical mechanics via $\hbar\to 0$. The resulting tools — Lagrangian, Hamiltonian, rigid body, normal modes — are the core of classical mechanical engineering science.

**Chapter 10 performs Bridge B.b:** the same quantum mechanics but with $N\to\infty$ and ensemble averaging, producing statistical mechanics and thermodynamics. The quantum Liouville equation from this chapter becomes the von Neumann equation; tracing over unobserved degrees of freedom produces the Boltzmann distribution and the four laws of thermodynamics.

The connection between Chapters 9 and 10 is important: classical mechanics (Ch. 9) gives individual deterministic trajectories; statistical mechanics (Ch. 10) gives ensemble-averaged behavior. The two descriptions are complementary — neither replaces the other.

---

_End of Chapter 9._

---

_Next: Chapter 10 — Bridge B.b: Statistical Mechanics and Thermodynamics ($N \to \infty$)_