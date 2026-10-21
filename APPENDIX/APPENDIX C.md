# Appendix C — From Quantum to Classical: Stationary Phase, WKB, and Ehrenfest

This appendix supplies the derivations behind two of the Bridge B limits. The first is Bridge B.a, the descent $\hbar \to 0$ from quantum to classical mechanics, which [Ch. 1](../CHAPTERS/CHAPTER%201.md) §1.4.3 and §1.8.3–§1.8.4 introduce and [Ch. 9](../CHAPTERS/CHAPTER%209.md) §9.1–§9.3 develops: why the classical path is the one with $\delta S = 0$, in what sense expectation values obey Newton's law, how the WKB wavefunction and its connection formulas are derived, and where the Bohr–Sommerfeld rule and the tunnelling exponent used in [Ch. 4](../CHAPTERS/CHAPTER%204.md) §4.4 and [Ch. 6](../CHAPTERS/CHAPTER%206.md) §6.10.1 come from. The second is Bridge B.d, the weak-field, slow-motion, quasi-static limit of general relativity that [Ch. 8](../CHAPTERS/CHAPTER%208.md) §8.2–§8.4 and §8.8 use to recover Newtonian gravity and the GPS clock correction.

The two limits are grouped together because they have the same logical shape. In each, one dimensionless number is small ($\hbar/S$ in the first case, $|\Phi|/c^2 \sim v^2/c^2$ in the second). The reduced theory is the leading term in an expansion in that number, and the reduction fails exactly where that number stops being small. Neither limit is a theorem about all states or all spacetimes. Each is an asymptotic statement with stated hypotheses, and those hypotheses are written out below.

Conventions follow the chapters. The metric signature is $(-,+,+,+)$ with $x^0 = ct$. Wavefunctions satisfy $i\hbar\,\partial_t\psi = \hat H\psi$. The local wavenumber in a classically forbidden region is $\kappa(x) = \sqrt{2m(V-E)}/\hbar$, as in Ch. 4 §4.4.2 and Ch. 9 §9.3.2. Euler–Lagrange equations are derived in Ch. 1 §1.5 and in [Appendix A](APPENDIX%20A.md); they are used here, not re-derived.

---

## C.1 — Stationary Phase and the Classical Path

### C.1.1 — What is being claimed

Ch. 1 §1.4.3 and Ch. 9 §9.2.2 state that as $\hbar \to 0$ the Feynman propagator is dominated by paths near the one with stationary action. This section separates that claim into a part that is a theorem and a part that is a heuristic.

**The theorem** is the finite-dimensional method of stationary phase.

**The heuristic** is applying that method to an integral over infinitely many variables (all paths), for which no Lebesgue measure exists.

The heuristic can be made rigorous in specific settings. Those settings are stated in §C.1.5.

### C.1.2 — The one-dimensional stationary-phase lemma

**Assumptions.**

1. $\phi(x)$ is real and smooth.
2. $g(x)$ is smooth and has compact support (or decays fast enough that the boundary terms below vanish).
3. On the support of $g$, $\phi$ has exactly one stationary point $x_0$, with $\phi'(x_0) = 0$ and $\phi''(x_0) \neq 0$. A stationary point with $\phi''(x_0) \neq 0$ is called *nondegenerate*.

Consider

$$I(\hbar) = \int_{-\infty}^{\infty} g(x)\,e^{i\phi(x)/\hbar}\,dx .$$

**Step 1: regions without a stationary point contribute only $O(\hbar^\infty)$.** Where $\phi' \neq 0$ we can write $e^{i\phi/\hbar} = \frac{\hbar}{i\phi'}\frac{d}{dx}e^{i\phi/\hbar}$ and integrate by parts:

$$\int g\,e^{i\phi/\hbar}\,dx = -\frac{\hbar}{i}\int \frac{d}{dx}\!\left(\frac{g}{\phi'}\right)e^{i\phi/\hbar}\,dx .$$

The boundary terms vanish by assumption 2. Each further integration by parts gains another factor of $\hbar$, so the contribution from any region bounded away from $x_0$ is smaller than every power of $\hbar$. This is the precise form of "rapidly oscillating phases cancel".

**Step 2: the neighbourhood of $x_0$.** Near $x_0$ we have $\phi(x) = \phi(x_0) + \tfrac12\phi''(x_0)(x-x_0)^2 + O((x-x_0)^3)$. The phase stays within order one of its stationary value over a window of width $|x-x_0| \sim \sqrt{\hbar/|\phi''(x_0)|}$, and that window shrinks to zero as $\hbar \to 0$. Over it, $g$ can be replaced by $g(x_0)$, and the cubic term changes the phase by only $O(\hbar^{1/2})$. What remains is the Fresnel integral

$$\int_{-\infty}^{\infty} e^{i a u^2/2\hbar}\,du = \sqrt{\frac{2\pi\hbar}{|a|}}\;e^{\,i\pi\,\mathrm{sgn}(a)/4}, \qquad a \neq 0 .$$

**Result.**

$$I(\hbar) = g(x_0)\sqrt{\frac{2\pi\hbar}{|\phi''(x_0)|}}\;\exp\!\left(\frac{i\phi(x_0)}{\hbar} + \frac{i\pi}{4}\,\mathrm{sgn}\,\phi''(x_0)\right)\big[1 + O(\hbar)\big].$$

A full proof, which uses the Morse lemma to make Step 2 exact and controls the error to all orders, is given in Hörmander, *The Analysis of Linear Partial Differential Operators I*, §7.7.

In $n$ dimensions with a nondegenerate stationary point $\mathbf{x}_0$ (Hessian $\phi_{ij} = \partial_i\partial_j\phi$ invertible), the same steps give

$$I(\hbar) \simeq g(\mathbf{x}_0)\,\frac{(2\pi\hbar)^{n/2}}{\sqrt{|\det\phi_{ij}|}}\;e^{i\phi(\mathbf{x}_0)/\hbar}\,e^{i\pi\,\mathrm{sgn}(\phi_{ij})/4},$$

where $\mathrm{sgn}(\phi_{ij})$ is the number of positive eigenvalues of the Hessian minus the number of negative ones.

> `[DERIVATION]` For finitely many integration variables, the dominance of the stationary point is a theorem, with corrections controlled by the small parameter $\hbar/|\phi''|\,\delta x^2$, where $\delta x$ is the scale over which $g$ and $\phi''$ vary.

### C.1.3 — The time-sliced path integral

The propagator for $\hat H = \hat p^2/2m + V(\hat x)$ in one dimension is defined as the limit of a finite-dimensional integral. Divide $[t_a, t_b]$ into $N$ steps of length $\varepsilon = (t_b - t_a)/N$ and fix $x_0 = x_a$, $x_N = x_b$. Then

$$K(x_b,t_b;x_a,t_a) = \lim_{N\to\infty}\left(\frac{m}{2\pi i\hbar\varepsilon}\right)^{N/2}\int\prod_{k=1}^{N-1}dx_k\;\exp\!\left(\frac{i}{\hbar}S_N[x_0,\dots,x_N]\right),$$

$$S_N = \sum_{k=0}^{N-1}\varepsilon\left[\frac{m}{2}\left(\frac{x_{k+1}-x_k}{\varepsilon}\right)^2 - V(x_k)\right].$$

For fixed $N$ this is an ordinary $(N-1)$-dimensional oscillatory integral, and §C.1.2 applies to it. Its stationarity condition $\partial S_N/\partial x_k = 0$ is

$$m\,\frac{x_{k+1}-2x_k+x_{k-1}}{\varepsilon^2} = -V'(x_k), \qquad k = 1,\dots,N-1 .$$

This is the finite-difference form of $m\ddot x = -V'(x)$. As $\varepsilon \to 0$ it becomes the Euler–Lagrange equation of Ch. 1 §1.5.2 with the fixed endpoints $x(t_a) = x_a$ and $x(t_b) = x_b$.

> `[DERIVATION]` For each finite $N$, the stationary point of the discretised action is the discretised classical trajectory.

Expanding the action to second order around the classical path $x_{cl}(t)$ gives a Gaussian integral over the fluctuations. Its value is the **Van Vleck–Pauli–Morette prefactor**:

$$K \simeq \left(\frac{1}{2\pi i\hbar}\left|-\frac{\partial^2 S_{cl}}{\partial x_b\,\partial x_a}\right|\right)^{1/2} e^{iS_{cl}(x_b,t_b;x_a,t_a)/\hbar - i\pi\nu/2},$$

where $\nu$ counts the conjugate (focal) points crossed by the classical path. This $\nu$ is the Maslov index; the same index reappears at turning points in §C.4. The prefactor is the quantity written $A$ in Ch. 9 §9.2.2.

**Check on the free particle.** For $V = 0$, $S_{cl} = m(x_b-x_a)^2/2T$ with $T = t_b - t_a$, so $-\partial^2 S_{cl}/\partial x_b\partial x_a = m/T$ and the formula gives

$$K_{free} = \sqrt{\frac{m}{2\pi i\hbar T}}\;\exp\!\left(\frac{im(x_b-x_a)^2}{2\hbar T}\right).$$

This is the *exact* free propagator. The semiclassical formula is exact for every action that is at most quadratic in the path, which includes the free particle, a uniform force, and the harmonic oscillator, because then the expansion to second order around $x_{cl}$ leaves nothing out. This is the same structural reason that Ehrenfest's theorem is exact for these potentials (§C.2.3).

### C.1.4 — Where the heuristic step lies

To go from §C.1.3 to "$\hbar \to 0$ selects the classical path", two limits must be exchanged: $N \to \infty$ (which defines the path integral) and $\hbar \to 0$ (which selects the stationary point). Three facts make this exchange more delicate than it looks.

1. **There is no measure on paths.** The factor $(m/2\pi i\hbar\varepsilon)^{N/2}$ diverges as $N\to\infty$. The object "$\mathcal{D}x(t)$" in Ch. 9 §9.2.1 is shorthand for the limiting procedure above, not a measure. (In imaginary time, the Wiener measure does exist; in real time it does not.)
2. **The typical paths are not smooth.** The paths that dominate the time-sliced integral at fixed $\hbar$ are continuous but nowhere differentiable: their increments scale as $|x_{k+1}-x_k| \sim \sqrt{\hbar\varepsilon/m}$. The classical path is an exceptional, smooth path. It dominates only after the oscillatory cancellation has been carried out.
3. **Uniqueness can fail.** There may be several classical paths between the same endpoints, for example in a harmonic oscillator over more than half a period. There may also be degenerate stationary points (caustics, where $\partial^2 S_{cl}/\partial x_b\partial x_a \to \infty$), or no real stationary path at all (tunnelling, §C.6).

What survives in general is therefore not "the particle takes the classical path". It is

$$K \simeq \sum_{\text{classical paths } j} A_j\,e^{iS_j/\hbar - i\pi\nu_j/2},$$

an interfering sum over classical paths, valid away from caustics. Classical mechanics proper, with a single trajectory, also requires the interference between different $j$ to be washed out, either by averaging over initial conditions or by decoherence (Ch. 9 §9.4.2). Stationary phase alone does not provide that step.

### C.1.5 — What makes it rigorous

For potentials $V$ that are smooth with bounded derivatives of order two and higher, the time-sliced propagator converges for short times, and the semiclassical expansion around the classical path can be proved with controlled errors. Real-time Feynman integrals can also be defined as infinite-dimensional oscillatory integrals with a stationary-phase theorem of their own. See Albeverio, Høegh-Krohn and Mazzucchi, *Mathematical Theory of Feynman Path Integrals* (Lecture Notes in Mathematics 523, 2nd ed., Springer 2008), and Schulman, *Techniques and Applications of Path Integration* (Wiley 1981) for the physics-level treatment. A separate route to the same physical conclusion, which avoids path integrals altogether, is the coherent-state limit of Hepp, *Commun. Math. Phys.* **35**, 265 (1974): quantum correlation functions in suitably scaled coherent states converge to classical ones as $\hbar \to 0$.

> `[APPROXIMATION]` The small parameter is $\hbar/S_{cl}$, the ratio of $\hbar$ to the action of the relevant classical motion. The selection of the stationary path holds asymptotically in that parameter and fails at caustics, for classically forbidden processes, and at times long enough for the semiclassical sum to break down (§C.2.4).

**What was proved.** For every finite discretisation, the stationary point of the action is the discretised classical path, and its neighbourhood dominates by a theorem. In the continuum limit, the same conclusion holds asymptotically under the regularity conditions above, in the form of a sum over classical paths with Van Vleck amplitudes and Maslov phases. The conclusion fails where stationary points merge (caustics), where no real stationary point exists (tunnelling), and where interference between several classical paths is not suppressed.

---

## C.2 — Ehrenfest's Theorem

### C.2.1 — Proof

**Assumptions.**

1. $\hat H$ is self-adjoint.
2. $\psi(t)$ stays in a domain on which $\hat H\hat A$ and $\hat A\hat H$ are defined, so that the expectation values below are finite.
3. The state evolves by $i\hbar\,\partial_t|\psi\rangle = \hat H|\psi\rangle$.

Then $\partial_t\langle\psi| = (i/\hbar)\langle\psi|\hat H$, because $\hat H^\dagger = \hat H$. Differentiating $\langle\hat A\rangle = \langle\psi|\hat A|\psi\rangle$ gives

$$\frac{d\langle\hat A\rangle}{dt} = \frac{i}{\hbar}\langle\psi|\hat H\hat A|\psi\rangle - \frac{i}{\hbar}\langle\psi|\hat A\hat H|\psi\rangle + \left\langle\frac{\partial\hat A}{\partial t}\right\rangle = \frac{i}{\hbar}\langle[\hat H,\hat A]\rangle + \left\langle\frac{\partial\hat A}{\partial t}\right\rangle .$$

This is the boxed result of Ch. 9 §9.1.1. Assumption 2 is not decorative. For an unbounded operator, the domain can fail to be preserved, and then the formal identity can fail. Standard examples involve wavefunctions with slowly decaying tails.

For $\hat H = \hat p^2/2m + V(\hat x)$, apply the canonical commutator $[\hat x,\hat p] = i\hbar$ and the identity $[f(\hat x),\hat p] = i\hbar f'(\hat x)$. This gives $[\hat H,\hat x] = -i\hbar\hat p/m$ and $[\hat H,\hat p] = i\hbar V'(\hat x)$, so

$$\frac{d\langle\hat x\rangle}{dt} = \frac{\langle\hat p\rangle}{m}, \qquad \frac{d\langle\hat p\rangle}{dt} = -\langle V'(\hat x)\rangle, \qquad m\frac{d^2\langle\hat x\rangle}{dt^2} = \langle F(\hat x)\rangle,$$

with $F = -V'$. These equations hold for *every* state and *every* potential.

> `[DERIVATION]` Ehrenfest's theorem is exact, given the Schrödinger equation and the domain conditions. It is not itself the classical limit.

### C.2.2 — The gap between $\langle F(\hat x)\rangle$ and $F(\langle\hat x\rangle)$

Write $\bar x = \langle\hat x\rangle$, $\delta\hat x = \hat x - \bar x$, and $\sigma_x^2 = \langle\delta\hat x^2\rangle$. For $F$ analytic over the region where $|\psi|^2$ is appreciable, expand $F$ about $\bar x$. The linear term averages to zero, so

$$\langle F(\hat x)\rangle = F(\bar x) + \tfrac12F''(\bar x)\,\sigma_x^2 + \tfrac16F'''(\bar x)\,\langle\delta\hat x^3\rangle + \cdots$$

With $F = -V'$, the leading correction to Newton's law is

$$m\ddot{\bar x} = -V'(\bar x) - \tfrac12 V'''(\bar x)\,\sigma_x^2 + \cdots,\qquad\text{equivalently}\qquad \langle V'\rangle = V'(\bar x) + \tfrac12\sigma_x^2V'''(\bar x) + \cdots$$

Note the sign: the correction to $\langle\nabla V\rangle$ is $+\tfrac12\sigma_x^2\,\nabla^3V$. The centroid obeys Newton's law with the force evaluated at the centroid provided

$$\sigma_x^2\,|V'''(\bar x)| \ll |V'(\bar x)| \qquad\Longleftrightarrow\qquad \sigma_x \ll L_V \equiv \sqrt{|V'/V'''|}.$$

This is the precise version of $\Delta x \ll L_V$ in Ch. 9 §9.1.3.

> `[APPROXIMATION]` The small parameter is $\sigma_x/L_V$, the width of the wavepacket divided by the length over which the force changes.

### C.2.3 — When the gap is exactly zero, and when it is large

**Exact cases.** The equality $\langle F(\hat x)\rangle = F(\langle\hat x\rangle)$ holds for every state if and only if $F$ is affine, $F(x) = a + bx$, which means $V$ is at most quadratic. The free particle, the uniform field, and the harmonic oscillator are the three examples. For them, the centroid of *any* wavefunction (including a cat state or a highly excited eigenstate) follows the classical trajectory exactly.

Following the classical trajectory does not make a state classical. A harmonic-oscillator energy eigenstate has $\langle\hat x\rangle = 0$ at all times, which is a correct classical trajectory (rest at the minimum), but the state is nothing like a classical particle at rest.

**A failure case.** In a symmetric double well, a packet that splits at the barrier into transmitted and reflected parts can have $\bar x$ near the barrier top, where no classical particle with that energy could be. There $\sigma_x$ is comparable to the well separation, the expansion of §C.2.2 does not converge usefully, and $F(\bar x)$ has nothing to do with $\langle F\rangle$.

**Ehrenfest is necessary but not sufficient.** A classical description requires the whole distribution to evolve classically, not only its first moment. The Wigner function $W(x,p,t)$ obeys the Moyal equation

$$\frac{\partial W}{\partial t} = -\frac{p}{m}\frac{\partial W}{\partial x} + V'(x)\frac{\partial W}{\partial p} - \frac{\hbar^2}{24}V'''(x)\frac{\partial^3 W}{\partial p^3} + O(\hbar^4).$$

Its first two terms are the classical Liouville equation (Ch. 9 §9.6.2).

> `[STRUCTURAL CONNECTION]` Quantum and classical phase-space dynamics differ by terms of order $\hbar^2V'''$. These vanish identically for potentials that are at most quadratic, which is the same condition as the exact cases of Ehrenfest's theorem above.

### C.2.4 — How long the classical description lasts

Even when $\sigma_x \ll L_V$ initially, wavepackets spread. For a free Gaussian of initial minimum-uncertainty width $\sigma_0$,

$$\sigma_x^2(t) = \sigma_0^2 + \left(\frac{\hbar t}{2m\sigma_0}\right)^2 .$$

The Ehrenfest condition therefore holds only up to a time at which $\sigma_x(t)$ reaches $L_V$.

- In a regular (integrable) system, spreading is typically algebraic in $t$, and this time is long.
- In a chaotic system, the width grows like $e^{\lambda t}$ with Lyapunov exponent $\lambda$ (Ch. 9 §9.10.2). The standard semiclassical estimate is then $t_E \sim \lambda^{-1}\ln(S/\hbar)$, where $S$ is a typical action of the motion. This is only logarithmically long in $1/\hbar$; see Haake, *Quantum Signatures of Chaos* (Springer).

For macroscopic bodies the observed classicality on all practical time scales does not come from $t_E$ alone. It comes from decoherence by the environment (Ch. 9 §9.4.2), which suppresses the interference terms that would otherwise make the evolution non-classical.

**What was proved.** The Ehrenfest equations hold exactly. Newton's law for the centroid follows when the packet is narrow compared with $L_V$, with leading error $\tfrac12V'''\sigma_x^2$. The result is exact for potentials that are at most quadratic, and it fails when the packet splits or spreads to $L_V$, which happens on the Ehrenfest time $t_E$.

---

## C.3 — The WKB Approximation to First Order

### C.3.1 — The exact Riccati form

**Assumptions.**

1. The problem is one-dimensional and time-independent: $-\frac{\hbar^2}{2m}\psi'' + V(x)\psi = E\psi$.
2. $V$ is smooth.

No approximation is made in this subsection. Write $\psi = e^{i\sigma(x)/\hbar}$ with $\sigma$ complex. Then $\psi' = (i\sigma'/\hbar)\psi$ and $\psi'' = \left(i\sigma''/\hbar - \sigma'^2/\hbar^2\right)\psi$. The Schrödinger equation becomes, exactly,

$$\frac{\sigma'^2}{2m} - \frac{i\hbar}{2m}\sigma'' + V(x) - E = 0 .$$

### C.3.2 — Expansion in $\hbar$

Expand $\sigma = \sigma_0 + \hbar\sigma_1 + \hbar^2\sigma_2 + \cdots$ and collect powers of $\hbar$.

**Order $\hbar^0$.**

$$\sigma_0'^2 = 2m(E - V) \equiv p(x)^2 \quad\Longrightarrow\quad \sigma_0 = \pm\int^x p(x')\,dx' .$$

This is the time-independent Hamilton–Jacobi equation (Ch. 1 §1.8.2), with $\sigma_0$ playing the role of Hamilton's characteristic function.

**Order $\hbar^1$.**

$$2\sigma_0'\sigma_1' - i\sigma_0'' = 0 \quad\Longrightarrow\quad \sigma_1' = \frac{i}{2}\frac{\sigma_0''}{\sigma_0'} = \frac{i}{2}\frac{d}{dx}\ln p \quad\Longrightarrow\quad e^{i\sigma_1} = p^{-1/2} .$$

Keeping these two orders gives the WKB wavefunction of Ch. 1 §1.8.4 and Ch. 9 §9.3.2:

$$\psi_{WKB}(x) = \frac{C_+}{\sqrt{p(x)}}\,e^{\,\frac{i}{\hbar}\int^x p\,dx'} + \frac{C_-}{\sqrt{p(x)}}\,e^{-\frac{i}{\hbar}\int^x p\,dx'} \qquad (E > V),$$

$$\psi_{WKB}(x) = \frac{D_+}{\sqrt{\kappa(x)}}\,e^{\,\int^x\kappa\,dx'} + \frac{D_-}{\sqrt{\kappa(x)}}\,e^{-\int^x\kappa\,dx'} \qquad (E < V),\qquad \kappa = \frac{\sqrt{2m(V-E)}}{\hbar}.$$

In the forbidden region $p = i\hbar\kappa$, and the factor $|p|^{-1/2}$ is written $\kappa^{-1/2}$ up to a constant that is absorbed into $D_\pm$.

**Two consistency checks.**

1. The probability current of each travelling component is $j = |C_\pm|^2(\pm 1/m)$, independent of $x$. This is the time-independent form of the order-$\hbar$ continuity equation of Ch. 1 §1.8.3, $(A^2\sigma_0')' = 0$, which forces $A \propto p^{-1/2}$.
2. The density $|\psi|^2 \propto 1/p \propto 1/v$ is proportional to the time a classical particle spends in $dx$. This is the semiclassical correspondence for densities.

> `[DERIVATION]` Given the expansion, the WKB form follows at first order in $\hbar$. Whether the expansion is accurate is a separate question, answered in §C.3.3.

### C.3.3 — The validity criterion

Truncating after $\sigma_1$ is justified when each successive term in the expansion is small compared with the one before. The first such comparison is

$$\left|\frac{\hbar\sigma_1'}{\sigma_0'}\right| = \frac{\hbar}{2}\frac{|p'|}{p^2} \ll 1 .$$

The order-$\hbar^2$ equation, $2\sigma_0'\sigma_2' + \sigma_1'^2 - i\sigma_1'' = 0$, gives $\hbar^2\sigma_2' \sim \hbar^2(p'^2/p^3 + p''/p^2)$. This is small under the same condition together with $\hbar|p''| \ll |p'|\,p$.

In terms of the reduced de Broglie wavelength $\tilde\lambda \equiv \lambda/2\pi = \hbar/p$,

$$\left|\frac{d\tilde\lambda}{dx}\right| = \frac{\hbar|p'|}{p^2} \ll 1 \qquad\Longleftrightarrow\qquad \frac{m\hbar\,|V'(x)|}{p(x)^3} \ll 1,$$

using $p' = -mV'/p$. Ch. 9 §9.3.3 writes this as $|d\lambda/dx| \ll 1$ with the full wavelength $\lambda = h/p$. That form differs by a factor of $2\pi$, which does not change a "much less than" statement. The reduced-wavelength form is the one that appears directly in the expansion.

**Physical reading.** The second form says that the change in potential energy across one reduced wavelength, $|V'|\tilde\lambda$, must be small compared with the local kinetic energy $p^2/m$.

**Where it fails.** At a turning point $x = a$ where $V(a) = E$, we have $p^2 \approx 2m|V'(a)|\,|x-a|$, so

$$\frac{m\hbar|V'|}{p^3} \approx \frac{1}{2^{3/2}}\left(\frac{\ell}{|x-a|}\right)^{3/2}, \qquad \ell \equiv \left(\frac{\hbar^2}{2m|V'(a)|}\right)^{1/3}.$$

WKB therefore fails within a distance of order $\ell$ of every turning point. It is also unreliable wherever $V$ changes appreciably within a wavelength, for example at a step or a hard wall. This last case is why the rectangular barrier of Ch. 4 §4.4.3 has a prefactor that WKB does not reproduce (§C.6.3).

> `[APPROXIMATION]` The small parameter is $\hbar|p'|/p^2 = |d\tilde\lambda/dx|$. The approximation is valid where $V$ is smooth on the scale of $\tilde\lambda$, and it fails within $\sim\ell$ of turning points and at discontinuities of $V$.

---

## C.4 — Connection Formulas at a Linear Turning Point

### C.4.1 — The local problem

**Assumptions.**

1. There is an isolated turning point at $x = a$ with $V'(a) \equiv F > 0$, so the allowed region is $x < a$ and the forbidden region is $x > a$.
2. $V$ is linear over a region around $a$ that is much wider than $\ell$. If $L$ is the scale over which $V'$ changes, $L \sim |V'/V''|$, this requires $\ell \ll L$.

> `[APPROXIMATION]` Linearise $V(x) \approx E + F(x-a)$. The small parameter is $\ell/L$, and it goes to zero as $\hbar \to 0$ because $\ell \propto \hbar^{2/3}$.

In the linear region the Schrödinger equation reads $\psi'' = (2mF/\hbar^2)(x-a)\psi$. Set $z = (x-a)/\ell$ with $\ell = (\hbar^2/2mF)^{1/3}$. This gives the **Airy equation**

$$\frac{d^2\psi}{dz^2} = z\,\psi,$$

whose two independent solutions are $\mathrm{Ai}(z)$ and $\mathrm{Bi}(z)$.

### C.4.2 — Airy asymptotics

Let $\zeta = \tfrac23|z|^{3/2}$. The standard asymptotic forms are (Abramowitz and Stegun, *Handbook of Mathematical Functions*, §10.4; or the NIST *Digital Library of Mathematical Functions*, §9.7):

$$z \to +\infty:\qquad \mathrm{Ai}(z) \simeq \frac{e^{-\zeta}}{2\sqrt\pi\,z^{1/4}}, \qquad \mathrm{Bi}(z) \simeq \frac{e^{\zeta}}{\sqrt\pi\,z^{1/4}},$$

$$z \to -\infty:\qquad \mathrm{Ai}(z) \simeq \frac{\sin(\zeta + \pi/4)}{\sqrt\pi\,|z|^{1/4}}, \qquad \mathrm{Bi}(z) \simeq \frac{\cos(\zeta + \pi/4)}{\sqrt\pi\,|z|^{1/4}} .$$

### C.4.3 — Matching

In the linear region the WKB quantities are $\kappa(x) = z^{1/2}/\ell$ for $z > 0$ and $k(x) \equiv p/\hbar = |z|^{1/2}/\ell$ for $z < 0$. The phase integrals are

$$\int_a^x\kappa\,dx' = \int_0^z z'^{1/2}\,dz' = \tfrac23 z^{3/2} = \zeta, \qquad \int_x^a k\,dx' = \tfrac23|z|^{3/2} = \zeta,$$

and the amplitude factors $\kappa^{-1/2}$ and $k^{-1/2}$ are both proportional to $|z|^{-1/4}$.

The WKB solutions are valid for $|x-a| \gg \ell$, and the linearisation is valid for $|x-a| \ll L$. When $\ell \ll L$ the two regions overlap, and in the overlap the WKB solutions must coincide with the Airy asymptotics above. Reading off coefficients:

- $\mathrm{Ai}$ has coefficient $1/2\sqrt\pi$ on the decaying side and $1/\sqrt\pi$ on the oscillating side, a ratio of $2$.
- $\mathrm{Bi}$ has the same coefficient on both sides, a ratio of $1$.

Hence:

$$\frac{2}{\sqrt{k}}\cos\!\left(\int_x^a k\,dx' - \frac{\pi}{4}\right) \;\longleftarrow\; \frac{1}{\sqrt{\kappa}}\exp\!\left(-\int_a^x\kappa\,dx'\right),$$

$$\frac{1}{\sqrt{k}}\cos\!\left(\int_x^a k\,dx' + \frac{\pi}{4}\right) \;\longleftrightarrow\; \frac{1}{\sqrt{\kappa}}\exp\!\left(+\int_a^x\kappa\,dx'\right).$$

The first line uses $\sin(\zeta + \pi/4) = \cos(\zeta - \pi/4)$.

For a turning point $b$ with the allowed region on the *right* (so $V'(b) < 0$), the same argument with $z = -(x-b)/\ell$ gives the mirror-image formulas:

$$\frac{1}{\sqrt{\kappa}}e^{-\int_x^b\kappa\,dx'} \;\longrightarrow\; \frac{2}{\sqrt{k}}\cos\!\left(\int_b^x k\,dx' - \frac{\pi}{4}\right), \qquad \frac{1}{\sqrt{\kappa}}e^{+\int_x^b\kappa\,dx'} \;\longleftrightarrow\; \frac{1}{\sqrt{k}}\cos\!\left(\int_b^x k\,dx' + \frac{\pi}{4}\right).$$

> `[DERIVATION]` Given the linearisation and the overlap condition $\ell \ll L$, the connection formulas follow from the exact Airy solution.

### C.4.4 — Directionality and the meaning of $\pi/4$

The arrows matter. The decaying exponential connects reliably to the oscillatory solution: a pure $\mathrm{Ai}$ is fixed by the requirement of decay. The reverse inference is unsafe. A small error in the phase of the oscillating solution admixes some $\mathrm{Bi}$, which grows exponentially into the forbidden region and swamps the decaying piece. Conversely, a subdominant decaying term cannot be resolved underneath a growing one. Statements that rely on keeping both exponentials in the same forbidden region therefore carry errors of the same order as the subdominant term (see §C.6.2).

The phase $\pi/4$ is the turning-point instance of the Maslov phase met in §C.1.3: a phase loss of $\pi/2$ for each reflection at a smooth turning point, split as $\pi/4$ on the way in and $\pi/4$ on the way out. The same result can be obtained without Airy functions by continuing the WKB solution around the turning point in the complex $x$ plane at a distance $\gg\ell$. That is the Zwaan–Kemble method; see Berry and Mount, *Rep. Prog. Phys.* **35**, 315 (1972), for a review of both routes.

**What was proved.** For an isolated turning point at which $V$ is linear over a width much larger than $\ell$, the WKB solutions on the two sides are connected as above. The derivation fails when two turning points are closer than a few $\ell$ (near a barrier top or a well bottom), when $V'(a) = 0$ (a degenerate turning point), and at hard walls, where the phase loss is $\pi/2$ per wall instead of $\pi/4$ per side.

---

## C.5 — Bohr–Sommerfeld Quantisation

### C.5.1 — Derivation

**Assumptions.**

1. The bound state lives in a single well with two isolated linear turning points $x_1 < x_2$.
2. The state is classically forbidden outside $[x_1, x_2]$.
3. The connection formulas of §C.4 hold at both turning points.

Define $k = p/\hbar$, $\theta(x) = \int_{x_1}^x k\,dx'$, and $\Theta = \int_{x_1}^{x_2}k\,dx$.

**From $x_1$.** The allowed region is on the right of $x_1$, so the decaying solution in $x < x_1$ connects, by the mirror formula of §C.4.3, to

$$\psi \simeq \frac{2C_1}{\sqrt k}\cos\!\left(\theta(x) - \frac{\pi}{4}\right).$$

**From $x_2$.** The allowed region is on the left of $x_2$, so the decaying solution in $x > x_2$ connects to

$$\psi \simeq \frac{2C_2}{\sqrt k}\cos\!\left(\Theta - \theta(x) - \frac{\pi}{4}\right) = \frac{2C_2}{\sqrt k}\cos\!\left(\theta(x) - \Theta + \frac{\pi}{4}\right).$$

**Matching.** Both expressions describe the same function throughout the interior. Two cosines $\cos(\theta - \alpha)$ and $\cos(\theta - \beta)$ are proportional for all $\theta$ if and only if $\alpha - \beta = n\pi$. Here $\alpha = \pi/4$ and $\beta = \Theta - \pi/4$, so

$$\Theta - \frac{\pi}{2} = n\pi, \qquad C_2 = (-1)^nC_1 .$$

Since $\Theta > 0$, $n = 0,1,2,\dots$, and $n$ is the number of nodes of $\psi$ in the interior. Using $\oint p\,dq = 2\int_{x_1}^{x_2}p\,dx = 2\hbar\Theta$,

$$\boxed{\oint p\,dq = \left(n + \frac12\right)h, \qquad n = 0,1,2,\dots}$$

This is the result quoted in Ch. 1 §1.8.4 and Ch. 9 §9.3.4.

> `[DERIVATION]` The Bohr–Sommerfeld rule follows from first-order WKB plus the two linear-turning-point connections.

**Level spacing and the classical period.** Differentiating the rule with respect to $E$ gives

$$\frac{d}{dE}\oint p\,dq = \oint\frac{dq}{\dot q} = T_{cl}(E) .$$

So adjacent levels are separated by $\Delta E \simeq h/T_{cl} = \hbar\omega_{cl}$. Emission frequencies $\Delta E/\hbar$ between neighbouring levels therefore approach the classical orbital frequency, which is the correspondence principle of Ch. 4 §4.12 in quantitative form.

### C.5.2 — Check 1: the harmonic oscillator

For $V = \tfrac12m\omega^2x^2$, the orbit at energy $E$ is an ellipse in phase space with semi-axes $\sqrt{2mE}$ and $\sqrt{2E/m\omega^2}$. Its area is

$$\oint p\,dq = \pi\sqrt{2mE}\sqrt{\frac{2E}{m\omega^2}} = \frac{2\pi E}{\omega} .$$

Setting this equal to $(n+\tfrac12)h$ gives $E_n = (n+\tfrac12)\hbar\omega$, which is the exact spectrum of Ch. 4 §4.3.2. Exactness here is special. All higher-order WKB corrections to the quantisation condition vanish identically for the oscillator; see Dunham, *Phys. Rev.* **41**, 713 (1932). In general the first correction to the quantisation condition is of relative order $\hbar^2$, which for low-lying states means corrections of order $1/n^2$ or so.

### C.5.3 — Check 2: the $\tfrac12$ is not universal

The $\tfrac12$ counts two *smooth* turning points, each contributing a phase of $\pi/4$ on each side. Writing the rule as $\oint p\,dq = 2\pi\hbar\,(n + \mu/4)$, $\mu$ is the Maslov index, with $\mu = 1$ for each smooth turning point and $\mu = 2$ for each hard wall (where $\psi = 0$ forces a phase loss of $\pi/2$ on each side).

- **Two hard walls** (the infinite square well of Ch. 4 §4.2): $\mu = 4$. With $p = \sqrt{2mE}$ constant, $\oint p\,dq = 2L\sqrt{2mE} = (n+1)h$, so $E = (n+1)^2\pi^2\hbar^2/2mL^2$. This is exact, with $n+1$ the usual quantum number.
- **One wall and one smooth turning point** (the half-oscillator, $V = \tfrac12m\omega^2x^2$ for $x > 0$ with a wall at $x = 0$): $\mu = 3$. Half the ellipse gives $\pi E/\omega = 2\pi\hbar(n + \tfrac34)$, so $E = (2n + \tfrac32)\hbar\omega$. These are exactly the odd-parity oscillator levels, which are the true spectrum of this problem.

**What was proved.** For a well bounded by two isolated linear turning points, $\oint p\,dq = (n+\tfrac12)h$ up to corrections of relative order $\hbar^2$. The rule is exact for the oscillator. The $\tfrac12$ must be replaced according to the Maslov index when the boundary conditions change. The derivation fails for a well so shallow that the turning points lie within a few $\ell$ of each other, which typically means the lowest one or two levels of an anharmonic well. It also fails in more than one dimension when the motion is not separable or integrable: there the Einstein–Brillouin–Keller generalisation applies to integrable systems, and chaotic systems need trace formulas.

---

## C.6 — The WKB Tunnelling Exponent

### C.6.1 — Setup

**Assumptions.**

1. A smooth barrier has $V(x) > E$ for $x_1 < x < x_2$, with linear turning points at both ends.
2. The barrier is thick in the sense that $\Theta \equiv \int_{x_1}^{x_2}\kappa\,dx \gg 1$.
3. A wave is incident from the left, and there is only a transmitted wave for $x > x_2$.

### C.6.2 — Derivation

**Right region.** Take the transmitted wave to be $\psi_{III} = \frac{F}{\sqrt k}\exp\!\left[i\left(\int_{x_2}^x k\,dx' + \frac{\pi}{4}\right)\right]$. The phase $\pi/4$ is chosen for convenience. Expanding $e^{iu} = \cos u + i\sin u$ and using the mirror formulas at $x_2$ in their Airy form, in which $\mathrm{Bi}$ pairs $\cos(\cdot + \pi/4)$ with the growing exponential and $\mathrm{Ai}$ pairs $2\sin(\cdot + \pi/4)$ with the decaying one:

$$\psi_{II} = \frac{F}{\sqrt\kappa}\left[e^{+\int_x^{x_2}\kappa\,dx'} + \frac{i}{2}e^{-\int_x^{x_2}\kappa\,dx'}\right] = \frac{F}{\sqrt\kappa}\left[e^{\Theta}e^{-\int_{x_1}^x\kappa\,dx'} + \frac{i}{2}e^{-\Theta}e^{+\int_{x_1}^x\kappa\,dx'}\right].$$

**Left region.** Connecting at $x_1$ with the formulas of §C.4.3 (with $a = x_1$), and setting $\chi = \int_x^{x_1}k\,dx'$ and $u = \chi + \pi/4$:

$$\psi_I = \frac{F}{\sqrt k}\left[2e^{\Theta}\sin u + \frac{i}{2}e^{-\Theta}\cos u\right] = \frac{F}{\sqrt k}\left[e^{iu}\left(-ie^{\Theta} + \tfrac{i}{4}e^{-\Theta}\right) + e^{-iu}\left(ie^{\Theta} + \tfrac{i}{4}e^{-\Theta}\right)\right].$$

Since $\chi$ decreases as $x$ increases, $e^{-iu}$ is the right-moving (incident) wave.

**Transmission.** All waves carry the same $k^{-1/2}$ normalisation, so the transmission probability is the ratio of squared amplitudes:

$$T = \frac{1}{\left(e^{\Theta} + \tfrac14e^{-\Theta}\right)^2}, \qquad R = \frac{\left(e^{\Theta} - \tfrac14e^{-\Theta}\right)^2}{\left(e^{\Theta} + \tfrac14e^{-\Theta}\right)^2}, \qquad R + T = 1 .$$

The last identity follows from $(a+b)^2 - (a-b)^2 = 4ab = 1$ with $a = e^\Theta$, $b = \tfrac14 e^{-\Theta}$, and it is a useful check on the algebra. However, the $e^{-\Theta}$ terms are of the same order as the error committed by carrying a subdominant exponential through the connection formulas (§C.4.4). The only result that is reliable to leading order is therefore

$$\boxed{T \simeq \exp\!\left(-2\int_{x_1}^{x_2}\kappa(x)\,dx\right) = \exp\!\left(-\frac{2}{\hbar}\int_{x_1}^{x_2}\sqrt{2m\big(V(x)-E\big)}\,dx\right)}$$

> `[APPROXIMATION]` The small parameters are $e^{-2\Theta}$ (the thick-barrier condition) and $\ell/L$ at each turning point (smoothness). Near the top of the barrier the two turning points merge, and the parabolic-barrier result $T = [1 + e^{2\Theta}]^{-1}$ replaces the formula above (Landau and Lifshitz, *Quantum Mechanics: Non-Relativistic Theory*, Ch. VII).

### C.6.3 — Checks and uses

**Rectangular barrier (Ch. 4 §4.4.3).** Here $\Theta = \kappa d$, so the WKB exponent $e^{-2\kappa d}$ is the same as the exact thick-barrier result. The exact prefactor $16(E/V_0)(1 - E/V_0)$ is not reproduced, because the walls of a rectangular barrier violate the smoothness condition of §C.3.3. **The exponent is robust; the prefactor is not.**

**Alpha decay (Ch. 6 §6.10.1).** Take $V = B/r$ with $B = 2Ze^2/4\pi\varepsilon_0$, outer turning point $r_c = B/E$, inner boundary at the nuclear radius $R$, and $v = \sqrt{2E/m_\alpha}$. Then

$$G \equiv \int_R^{r_c}\kappa\,dr = \frac{\sqrt{2m_\alpha E}}{\hbar}\,r_c\left[\arccos\sqrt{\frac{R}{r_c}} - \sqrt{\frac{R}{r_c}\left(1 - \frac{R}{r_c}\right)}\right] \simeq \frac{\pi B}{\hbar v}\left(1 - \frac{4}{\pi}\sqrt{\frac{R}{r_c}}\right),$$

with $T_\alpha \simeq e^{-2G}$. In SI units the leading term is $\pi B/\hbar v = 2\pi Ze^2/(4\pi\varepsilon_0\hbar v)$, and $R/r_c = E/V_C(R)$. The radial problem with $\ell = 0$ reduces to this one-dimensional form, and the inner boundary at $R$ is not a smooth turning point, which affects only the prefactor.

**Field emission.** For a triangular barrier $V - E = W - e\mathcal{E}x$ (work function $W$, applied field $\mathcal{E}$, no image force), $\Theta = \frac{2\sqrt{2m}\,W^{3/2}}{3\hbar e\mathcal{E}}$. This gives the Fowler–Nordheim exponent $T \sim \exp\!\left(-\frac{4\sqrt{2m}\,W^{3/2}}{3\hbar e\mathcal{E}}\right)$, which is the high-field counterpart of the thermionic and Schottky emission treated in Ch. 14 §14.6.

**What was proved.** For a smooth barrier with $\Theta \gg 1$, the tunnelling probability is $e^{-2\Theta}$ to leading exponential accuracy. The result fails near the top of the barrier, where the turning points merge. For sharp barriers it gives the right exponent but the wrong prefactor. For a non-separable barrier in several dimensions it must be replaced by the instanton (complex-time stationary-phase) method, which is the many-dimensional generalisation of §C.1 to imaginary time.

---

## C.7 — General Relativity to Newton: the Weak-Field Limit

### C.7.1 — Assumptions and the bookkeeping parameter

Ch. 8 §8.3 names three conditions. Here they are stated as a single expansion. There exist coordinates $x^\mu = (ct, \mathbf{x})$ in which:

1. **(W) Weak field.** $g_{\mu\nu} = \eta_{\mu\nu} + h_{\mu\nu}$ with $|h_{\mu\nu}| \ll 1$. Work to first order in $h$.
2. **(S) Slow motion.** Sources and test bodies move with $v \ll c$, and stresses are small: $|T^{ij}| \ll T^{00}$. For a perfect fluid this means $p \ll \rho c^2$.
3. **(Q) Quasi-static.** Time derivatives of the field are small compared with space derivatives: $|\partial_0 h| \sim (v/c)|\partial_i h|$.

For bound systems the virial theorem links (W) and (S): $|\Phi|/c^2 \sim v^2/c^2 \equiv \epsilon$. Terms are therefore ordered as follows: $h_{00} \sim \epsilon$, $T^{0i}/T^{00} \sim \epsilon^{1/2}$, $T^{ij}/T^{00} \sim \epsilon$, and $\partial_0/\partial_i \sim \epsilon^{1/2}$.

> `[APPROXIMATION]` Newtonian gravity is the leading order in $\epsilon$. It requires all three assumptions at once.

### C.7.2 — Geodesic equation to Newton's second law

The geodesic equation is

$$\frac{d^2x^\mu}{d\tau^2} + \Gamma^\mu_{\alpha\beta}\frac{dx^\alpha}{d\tau}\frac{dx^\beta}{d\tau} = 0 .$$

Under (S), $dx^0/d\tau = c\,\gamma \simeq c$ and $dx^i/d\tau \simeq v^i$. In the spatial equation, the three groups of terms scale as

$$\Gamma^i_{00}\,c^2 \;:\; \Gamma^i_{0j}\,c\,v^j \;:\; \Gamma^i_{jk}\,v^jv^k \;\sim\; 1 : \epsilon^{1/2} : \epsilon ,$$

so only $\Gamma^i_{00}$ survives at leading order.

Converting from $\tau$ to $t$ adds a term $(d^2t/d\tau^2)\,dx^i/dt$, which involves $\Gamma^0_{00} = -\tfrac12\partial_0h_{00}$ and is suppressed by (Q). To first order in $h$,

$$\Gamma^i_{00} = \tfrac12\eta^{ij}\left(2\partial_0h_{0j} - \partial_jh_{00}\right) \;\xrightarrow{\;(Q)\;}\; -\tfrac12\partial_ih_{00},$$

and therefore

$$\frac{d^2x^i}{dt^2} = -c^2\,\Gamma^i_{00} = +\frac{c^2}{2}\,\partial_ih_{00} .$$

Newton's law $\ddot x^i = -\partial_i\Phi$ is recovered if and only if $h_{00} = -2\Phi/c^2 + \text{const}$. Requiring $h_{00} \to 0$ where $\Phi \to 0$ (far from all sources) sets the constant to zero:

$$\boxed{g_{00} \simeq -\left(1 + \frac{2\Phi}{c^2}\right)}$$

**Sign check.** Ch. 8 §8.3.2 writes the intermediate step as $-c^2\cdot\tfrac12\eta^{ij}\partial_jh_{00}$. The correct expression carries the opposite sign, because $\Gamma^i_{00} = -\tfrac12\partial_ih_{00}$. With $h_{00} = -2\Phi/c^2$, the result $\ddot x^i = -\partial_i\Phi$ follows as stated.

Slow test bodies probe only $g_{00}$ at this order. The spatial components $g_{ij}$ enter at relative order $\epsilon$, and they are what doubles the light-deflection angle (Ch. 8 §8.7.2), because light has $v = c$ and so violates (S).

> `[DERIVATION]` Under (W), (S) and (Q), the geodesic equation reduces to $\ddot{\mathbf{x}} = -\nabla\Phi$ with $\Phi \equiv -c^2h_{00}/2$.

### C.7.3 — Einstein equations to Poisson's equation

Taking the trace of $G_{\mu\nu} = (8\pi G/c^4)T_{\mu\nu}$ gives $R = -(8\pi G/c^4)T$, and so the trace-reversed form

$$R_{\mu\nu} = \frac{8\pi G}{c^4}\left(T_{\mu\nu} - \tfrac12g_{\mu\nu}T\right).$$

Only the $00$ component is needed.

**Matter side.** For a perfect fluid in its rest frame to leading order, $T_{00} = \rho c^2$, $T_{ij} = p\,\delta_{ij}$, and $T = g^{\mu\nu}T_{\mu\nu} = -\rho c^2 + 3p$. Therefore

$$T_{00} - \tfrac12g_{00}T = \rho c^2 + \tfrac12\left(-\rho c^2 + 3p\right) = \tfrac12\left(\rho c^2 + 3p\right) \;\xrightarrow{\;p\,\ll\,\rho c^2\;}\; \tfrac12\rho c^2 .$$

This is the factor that comes from $T_{00}$ dominance. The trace reversal halves the source. Pressure contributes to the "active" gravitational mass density as $\rho + 3p/c^2$, and Newtonian gravity requires that contribution to be negligible: $p \ll \rho c^2$ is part of assumption (S).

**Geometry side.** The linearised Ricci tensor of Ch. 8 §8.2.2, with every $\partial_0$ dropped under (Q), gives

$$R_{00}^{(1)} = \tfrac12\left(-\Box h_{00} - \partial_0\partial_0h + 2\partial^\rho\partial_0h_{0\rho}\right) \;\xrightarrow{\;(Q)\;}\; -\tfrac12\nabla^2h_{00} .$$

**Combining.**

$$-\tfrac12\nabla^2h_{00} = \frac{8\pi G}{c^4}\cdot\frac{\rho c^2}{2} \quad\Longrightarrow\quad \nabla^2\!\left(-\frac{c^2h_{00}}{2}\right) = 4\pi G\rho \quad\Longrightarrow\quad \boxed{\nabla^2\Phi = 4\pi G\rho}$$

where $\Phi = -c^2h_{00}/2$, exactly as identified in §C.7.2. This route needs no gauge choice, because the static $R_{00}$ involves only $h_{00}$.

**Cross-check with Ch. 8's gauge route.** In the Lorenz gauge, the derivation of Ch. 8 §8.3.1 gives $\bar h_{00} = -4\Phi/c^2$ with the other components of $\bar h_{\mu\nu}$ of higher order. The trace is $\bar h = \eta^{\mu\nu}\bar h_{\mu\nu} = +4\Phi/c^2$, so $h = -\bar h = -4\Phi/c^2$. Then $h_{\mu\nu} = \bar h_{\mu\nu} - \tfrac12\eta_{\mu\nu}\bar h$ gives

$$h_{00} = -\frac{4\Phi}{c^2} + \frac{2\Phi}{c^2} = -\frac{2\Phi}{c^2}, \qquad h_{ij} = -\frac{2\Phi}{c^2}\delta_{ij} .$$

This reproduces the metric of Ch. 8 §8.4, including the spatial factor $(1 - 2\Phi/c^2)$, and is consistent with the result above.

**Dimensional remark.** Ch. 8 §8.3 writes the dust tensor as $T^{\mu\nu} = \rho c^2u^\mu u^\nu$. With $u^\mu = \gamma(c, \mathbf{v})$ carrying units of velocity, the dimensionally consistent form is $T^{\mu\nu} = \rho\,u^\mu u^\nu$. That form gives $T^{00} = \rho c^2$, which is what both derivations use.

> `[DERIVATION]` Under (W), (S) and (Q), the $00$ Einstein equation reduces to Poisson's equation, with the factor $\tfrac12$ from trace reversal cancelling against the factor $2$ in $h_{00} = -2\Phi/c^2$.

**What was proved, and where it fails.** Newtonian gravity, meaning both the field equation and the equation of motion, is the leading term in $\epsilon \sim |\Phi|/c^2 \sim v^2/c^2$. It fails in four ways:

1. When $|\Phi|/c^2$ is not small (neutron stars and black holes; Ch. 8 §8.9).
2. When $v$ is comparable to $c$ for the test body (light deflection, where $g_{ij}$ matters).
3. When sources move fast enough that $g_{0i}$ (gravitomagnetism, frame dragging; Ch. 8 §8.7.3) or radiation (Ch. 8 §8.6) is needed.
4. When the pressure is relativistic.

The first corrections (perihelion advance and the Shapiro delay) are the post-Newtonian terms of order $\epsilon$ beyond this limit.

---

## C.8 — The Leading GPS Clock-Rate Correction

### C.8.1 — Rate of an orbiting clock

**Assumptions.**

1. The metric of §C.7.3, $ds^2 = -(1 + 2\Phi/c^2)c^2dt^2 + (1 - 2\Phi/c^2)|d\mathbf{x}|^2$, in an Earth-centred non-rotating frame.
2. The potential is the monopole $\Phi = -GM_\oplus/r$ (oblateness $J_2$ neglected).
3. The clock moves with coordinate speed $v$.

Proper time along the clock's worldline satisfies

$$\frac{d\tau}{dt} = \sqrt{1 + \frac{2\Phi}{c^2} - \left(1 - \frac{2\Phi}{c^2}\right)\frac{v^2}{c^2}} = 1 + \frac{\Phi}{c^2} - \frac{v^2}{2c^2} + O(\epsilon^2) .$$

> `[DERIVATION]` Both the "gravitational" and the "velocity" terms of Ch. 8 §8.8.2–§8.8.3 come from one expansion of one metric. They are the two order-$\epsilon$ terms of the same quantity, not two separate effects added by hand.

For a satellite on a circular orbit of radius $r$, $v^2 = GM_\oplus/r$, so

$$\frac{d\tau}{dt}\bigg|_{sat} = 1 - \frac{3GM_\oplus}{2rc^2} .$$

For a ground clock at radius $R_\oplus$ with speed $v_g$ due to Earth's rotation,

$$\frac{d\tau}{dt}\bigg|_{gnd} = 1 - \frac{GM_\oplus}{R_\oplus c^2} - \frac{v_g^2}{2c^2} .$$

### C.8.2 — Numbers

Take $GM_\oplus = 3.986\times10^{14}$ m³ s⁻², $c^2 = 8.988\times10^{16}$ m² s⁻², $R_\oplus = 6.371\times10^6$ m, and $r = 2.656\times10^7$ m (the GPS semi-major axis). Then:

| Term | Value | Per day |
|---|---|---|
| $GM_\oplus/R_\oplus c^2 - GM_\oplus/rc^2$ | $6.961\times10^{-10} - 1.670\times10^{-10} = 5.29\times10^{-10}$ | $+45.7\,\mu$s |
| $-v_{sat}^2/2c^2$, with $v_{sat} = 3.874$ km/s | $-8.35\times10^{-11}$ | $-7.2\,\mu$s |
| $+v_g^2/2c^2$ at the equator ($v_g = 465$ m/s) | $+1.2\times10^{-12}$ | $+0.10\,\mu$s |
| **Net fractional rate, satellite minus ground** | $\approx 4.47\times10^{-10}$ | $\approx +38.6\,\mu$s |

Omitting the ground-rotation term reproduces the $+38.5\,\mu$s/day and $4.46\times10^{-10}$ of Ch. 8 §8.8.4. The operational system sets the satellite clocks' nominal $10.23$ MHz to $10.22999999543$ MHz, a fractional offset of $4.467\times10^{-10}$. Treating the ground clock on the rotating geoid, and including $J_2$ in the potential, closes the remaining gap. See Ashby, "Relativity in the Global Positioning System", *Living Rev. Relativ.* **6**, 1 (2003).

### C.8.3 — The eccentricity term

For a Keplerian orbit with semi-major axis $a$, energy conservation gives $v^2/2 = GM_\oplus(1/r - 1/2a)$, so

$$\frac{d\tau}{dt} = 1 - \frac{3GM_\oplus}{2ac^2} - \frac{2GM_\oplus}{c^2}\left(\frac1r - \frac1a\right).$$

With $r = a(1 - e\cos E)$ and $dt = \sqrt{a^3/GM_\oplus}\,(1 - e\cos E)\,dE$, where $E$ here is the eccentric anomaly, the last term integrates to

$$\Delta\tau_{periodic} = -\frac{2\sqrt{GM_\oplus a}}{c^2}\,e\,\sin E .$$

Its amplitude is about $23$ ns for $e = 0.01$. Receivers apply this term in software; it is not absorbed by the factory frequency offset.

**What was proved.** The fractional rate offset of a GPS clock is the order-$\epsilon$ term in the proper-time expansion of the weak-field metric. That is $\approx 4.5\times10^{-10}$, of which the gravitational part dominates. Neglected here are signal-propagation effects (the Sagnac correction in the rotating frame and the Shapiro delay), $J_2$, and terms of order $\epsilon^2 \sim 10^{-19}$, all of which are treated in Ashby (2003).

---

## C.9 — Summary

| Result | Statement | Assumptions | Used in |
|---|---|---|---|
| Stationary-phase lemma | $\int g\,e^{i\phi/\hbar} \simeq g(x_0)\sqrt{2\pi\hbar/\lvert\phi''\rvert}\,e^{i\phi(x_0)/\hbar \pm i\pi/4}$ | finite dimension; nondegenerate stationary point; smooth $g$, $\phi$ | Ch. 1 §1.4.3; Ch. 9 §9.2.2 |
| Classical path from path integral | stationary point of $S_N$ is the discretised Euler–Lagrange path; $K \simeq \sum_j A_je^{iS_j/\hbar - i\pi\nu_j/2}$ | $\hbar/S_{cl} \ll 1$; no caustics; heuristic exchange of $N\to\infty$ and $\hbar\to0$ (rigorous under regularity conditions, §C.1.5) | Ch. 1 §1.4.3; Ch. 9 §9.2 |
| Ehrenfest theorem | $d\langle\hat A\rangle/dt = (i/\hbar)\langle[\hat H,\hat A]\rangle + \langle\partial_t\hat A\rangle$; $m\ddot{\bar x} = \langle F\rangle$ | self-adjoint $\hat H$; domain conditions | Ch. 9 §9.1 |
| Centroid follows Newton | $\langle V'\rangle = V'(\bar x) + \tfrac12\sigma_x^2V''' + \cdots$ | $\sigma_x \ll L_V$; $t \ll t_E$; exact for $V$ at most quadratic | Ch. 9 §9.1.3 |
| WKB wavefunction | $\psi \simeq Cp^{-1/2}e^{\pm i\int p\,dx/\hbar}$; $\kappa^{-1/2}e^{\pm\int\kappa\,dx}$ | $\hbar\lvert p'\rvert/p^2 \ll 1$ | Ch. 1 §1.8.4; Ch. 9 §9.3.2–§9.3.3 |
| Connection formulas | $\frac{2}{\sqrt k}\cos(\int_x^ak - \frac\pi4) \leftarrow \frac{1}{\sqrt\kappa}e^{-\int_a^x\kappa}$ | isolated linear turning point; $\ell \ll L$; direction matters | Ch. 9 §9.3.3 |
| Bohr–Sommerfeld | $\oint p\,dq = (n + \tfrac12)h$; generally $2\pi\hbar(n + \mu/4)$ | two smooth turning points; corrections $O(\hbar^2)$; exact for oscillator | Ch. 1 §1.8.4; Ch. 9 §9.3.4; Ch. 4 §4.3, §4.12 |
| Tunnelling exponent | $T \simeq \exp(-2\int\kappa\,dx)$ | $\Theta \gg 1$; smooth barrier; not near the top | Ch. 4 §4.4; Ch. 6 §6.10.1; Ch. 14 §14.6 |
| Newtonian metric | $g_{00} \simeq -(1 + 2\Phi/c^2)$, $g_{ij} \simeq (1 - 2\Phi/c^2)\delta_{ij}$ | weak field, slow motion, quasi-static | Ch. 8 §8.3.2, §8.4 |
| Poisson equation | $\nabla^2\Phi = 4\pi G\rho$ from the $00$ trace-reversed Einstein equation | as above plus $p \ll \rho c^2$; source $\tfrac12(\rho c^2 + 3p)$ | Ch. 8 §8.3.1 |
| GPS clock rate | $d\tau/dt \simeq 1 + \Phi/c^2 - v^2/2c^2$; net $\approx 4.5\times10^{-10}$, $\approx 38.5\,\mu$s/day | monopole potential; order $\epsilon$; periodic eccentricity term separate | Ch. 8 §8.8 |

---

## C.10 — References

Standard sources used in this appendix (see also [`REFERENCES.md`](../REFERENCES.md)):

- L. Hörmander, *The Analysis of Linear Partial Differential Operators I*, Springer, §7.7 (stationary phase).
- S. Albeverio, R. Høegh-Krohn, S. Mazzucchi, *Mathematical Theory of Feynman Path Integrals*, Lecture Notes in Mathematics 523, 2nd ed., Springer (2008).
- L. S. Schulman, *Techniques and Applications of Path Integration*, Wiley (1981).
- K. Hepp, *Commun. Math. Phys.* **35**, 265 (1974).
- M. V. Berry and K. E. Mount, *Rep. Prog. Phys.* **35**, 315 (1972).
- J. L. Dunham, *Phys. Rev.* **41**, 713 (1932).
- L. D. Landau and E. M. Lifshitz, *Quantum Mechanics: Non-Relativistic Theory*, Ch. VII.
- F. Haake, *Quantum Signatures of Chaos*, Springer.
- S. M. Carroll, *Spacetime and Geometry*, Addison-Wesley (2004), Ch. 4 and Ch. 7 (Newtonian limit, linearised gravity).
- N. Ashby, *Living Rev. Relativ.* **6**, 1 (2003).
