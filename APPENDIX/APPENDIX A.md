# Appendix A — Variational Calculus, Noether's Theorems, and Conservation Laws

This appendix supplies the complete proofs behind the variational machinery that the main text states or sketches. It proves the Euler–Lagrange equations with their boundary terms, the Legendre transform to Hamilton's equations, the basic Poisson-bracket results, **Noether's first theorem** for particles and fields (including the total-derivative term that the short proof in Ch. 1 §1.7.2 omits), the canonical and Hilbert stress–energy tensors and how they are related, **Noether's second theorem** for local gauge invariance, the chain from the continuity equation through the integral charge balance to Kirchhoff's current law (with every lumping assumption stated), and the Rayleigh dissipation function that carries the Lagrangian formalism over to R/C/L networks. The chapters that rely on it are [Ch. 0](../CHAPTERS/CHAPTER%200.md) (the action and its symmetries), [Ch. 1](../CHAPTERS/CHAPTER%201.md) §§1.5–1.7 and §1.9 (the machinery itself), [Ch. 8](../CHAPTERS/CHAPTER%208.md) §8.1 (the metric definition of $T_{\mu\nu}$), [Ch. 9](../CHAPTERS/CHAPTER%209.md) §§9.5–9.6 (Lagrangian and Hamiltonian mechanics as tools), [Ch. 11](../CHAPTERS/CHAPTER%2011.md) §11.5 and §11.12 (charge conservation and the Kirchhoff laws), and [Ch. 17](../CHAPTERS/CHAPTER%2017.md) §§17.3–17.4 (the R/C/L template and the node laws).

Nothing here is new physics. What the appendix adds is the bookkeeping: which assumption each step needs, and the point at which each result stops holding.

---

## A.1 — Conventions

**Assumptions used throughout.**

1. **Signature.** The book's metric signature is $\eta_{\mu\nu} = \mathrm{diag}(-1,+1,+1,+1)$ (Ch. 0 §0.2.2, Ch. 8 §8.2.1, Ch. 11 §11.2.1), with $x^\mu = (ct,\mathbf{r})$, so $\partial_0 = c^{-1}\partial_t$. Indices are raised and lowered with $\eta$ (or $g$ in curved spacetime); repeated indices are summed.
2. **Units.** SI. Electromagnetism follows Ch. 11: $A^\mu = (\phi/c,\,\mathbf{A})$, so $A_0 = -\phi/c$; $j^\mu = (c\rho,\,\mathbf{J})$; $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu$. In Gaussian units (as in Ch. 1 §1.6.1 and Ch. 3) replace $q\mathbf{A} \to q\mathbf{A}/c$.
3. **Smoothness.** All fields and paths are taken $C^2$ on the region of interest, and variations $\eta(t)$ or $\delta\phi(x)$ are smooth. Distributional sources (point charges, surface currents) are handled by the usual limiting arguments and are not treated separately.
4. **Charge convention.** A matter field of charge $q$ (signed; $q = -e$ for the electron) transforms as $\psi \to e^{iq\alpha/\hbar}\psi$ with $A_\mu \to A_\mu + \partial_\mu\alpha$, and couples through $D_\mu = \partial_\mu - (iq/\hbar)A_\mu$. This matches the sign of the covariant derivative in Ch. 0 §0.5. With it, $-i\hbar D_k = p_k - qA_k$ and $i\hbar c\,D_0 = i\hbar\partial_t - q\phi$, so the nonrelativistic limit carries $(\mathbf{p}-q\mathbf{A})^2/2m + q\phi$.

A **functional** $F[\phi]$ assigns a number to a function. Its **functional derivative** $\delta F/\delta\phi(x)$ is defined by the first-order change under $\phi \to \phi + \delta\phi$ with $\delta\phi$ of compact support in the interior of the domain:

$$\delta F = \int dx\,\frac{\delta F}{\delta \phi(x)}\,\delta\phi(x) + \mathcal{O}(\delta\phi^2)$$

Boundary contributions are excluded from this definition on purpose. They are tracked separately in §A.2, because they are where boundary conditions come from.

---

## A.2 — The Euler–Lagrange Equations, with Boundary Terms

### A.2.1 — The fundamental lemma

**Lemma.** Let $f$ be continuous on $[t_1,t_2]$. If $\int_{t_1}^{t_2} f(t)\,\eta(t)\,dt = 0$ for every smooth $\eta$ that vanishes outside a closed subinterval of $(t_1,t_2)$, then $f \equiv 0$ on $[t_1,t_2]$.

*Proof.* Suppose $f(t_0) > 0$ at some interior $t_0$. By continuity, $f > f(t_0)/2$ on some interval $(t_0-\delta,\,t_0+\delta)$. Choose $\eta$ to be a smooth bump, positive on that interval and zero outside it. Then $\int f\eta\,dt > 0$, a contradiction. The case $f(t_0) < 0$ is the same with the sign reversed, and continuity extends $f = 0$ to the endpoints. $\square$

The same argument works in $d$ dimensions with bumps supported in a small ball, which is the version needed for fields.

### A.2.2 — One degree of freedom, endpoints free or fixed

**Assumptions.** $L(q,\dot q,t)$ is $C^2$, and $S[q] = \int_{t_1}^{t_2} L\,dt$. The variation is $q \to q + \epsilon\eta$ with $\eta$ smooth. At first we do **not** require $\eta(t_1) = \eta(t_2) = 0$.

Differentiate under the integral:

$$\left.\frac{d S[q+\epsilon\eta]}{d\epsilon}\right|_{\epsilon=0} = \int_{t_1}^{t_2}\left(\frac{\partial L}{\partial q}\,\eta + \frac{\partial L}{\partial \dot q}\,\dot\eta\right)dt$$

Integrate the second term by parts and define $p \equiv \partial L/\partial\dot q$:

$$\delta S = \int_{t_1}^{t_2}\underbrace{\left(\frac{\partial L}{\partial q} - \frac{d}{dt}\frac{\partial L}{\partial\dot q}\right)}_{\equiv\,\mathsf{E}(t)}\eta\,dt \;+\; \Big[\,p\,\eta\,\Big]_{t_1}^{t_2}$$

This is the complete first variation. Three things follow from it.

1. **Interior equation.** Restricting to $\eta$ of compact support in $(t_1,t_2)$ kills the bracket. The lemma then gives $\mathsf{E}(t) = 0$, which is the Euler–Lagrange equation. In the notation of §A.1, $\delta S/\delta q(t) = \mathsf{E}(t)$.
2. **Fixed endpoints (Hamilton's principle, Ch. 1 §1.4.2).** If $q(t_1)$ and $q(t_2)$ are prescribed, then $\eta(t_1) = \eta(t_2) = 0$ and the bracket vanishes identically. Stationarity is then equivalent to $\mathsf{E} = 0$.
3. **Free endpoint (natural boundary condition).** If $q(t_2)$ is left free, then stationarity for all $\eta$ requires $\mathsf{E} = 0$ *and* $p(t_2) = 0$. The boundary condition is not imposed. It is produced by the variational principle.

> **[DERIVATION]** Hamilton's principle with fixed endpoints is equivalent to $\frac{d}{dt}\frac{\partial L}{\partial\dot q_i} - \frac{\partial L}{\partial q_i} = 0$ for each $i$. This is Ch. 1 §1.5.1 with the boundary term kept explicit. The $n$-coordinate case follows by varying each $q_i$ independently.

**Total-derivative ambiguity.** If $L' = L + dG(q,t)/dt$, then $S' = S + G(q(t_2),t_2) - G(q(t_1),t_1)$. With fixed endpoints the extra term does not vary, so $L$ and $L'$ give identical equations of motion. The canonical momentum does change, $p' = p + \partial G/\partial q$. The gauge transformation of a charged particle (§A.3.2) is the standard example. This ambiguity is the reason Noether's theorem has to allow symmetries "up to a total derivative" (§A.4).

**Stationary, not minimal.** $\delta S = 0$ says nothing about the second variation. For $L = \tfrac12 m\dot q^2 - V(q)$ the action is a true local minimum only for time intervals shorter than the first conjugate point. For the harmonic oscillator that limit is half a period, $\pi/\omega$. See Gelfand & Fomin, *Calculus of Variations*, for the Jacobi condition. Physics only ever uses stationarity.

### A.2.3 — Higher derivatives: the Euler–Poisson equation

If $L = L(q,\dot q,\ddot q,t)$, two integrations by parts give

$$\delta S = \int_{t_1}^{t_2}\left(\frac{\partial L}{\partial q} - \frac{d}{dt}\frac{\partial L}{\partial \dot q} + \frac{d^2}{dt^2}\frac{\partial L}{\partial \ddot q}\right)\eta\,dt + \left[\left(\frac{\partial L}{\partial\dot q} - \frac{d}{dt}\frac{\partial L}{\partial\ddot q}\right)\eta + \frac{\partial L}{\partial\ddot q}\,\dot\eta\right]_{t_1}^{t_2}$$

The interior equation is fourth order. The boundary term now needs two conditions at each end, one on $\eta$ and one on $\dot\eta$. The static Euler–Bernoulli beam (Ch. 16) is this structure with $x$ in place of $t$. The energy is $\int[\tfrac12 EI\,(w'')^2 - q\,w]\,dx$, the interior equation is $EI\,w'''' = q$, and the boundary bracket yields the familiar pairs: clamped ($w = w' = 0$), simply supported ($w = 0$ with $EI\,w'' = 0$ produced naturally), and free ($EI\,w'' = 0$ and $(EI\,w'')' = 0$, both natural).

### A.2.4 — Fields

**Assumptions.** $S[\phi] = \int_\Omega d^4x\,\mathcal{L}(\phi_a,\partial_\mu\phi_a,x)$ over a spacetime region $\Omega$ with boundary $\partial\Omega$. In flat spacetime $d^4x = c\,dt\,d^3x$. The constant overall factor of $c$ does not affect anything below.

$$\delta S = \int_\Omega d^4x\left[\frac{\partial\mathcal{L}}{\partial\phi_a} - \partial_\mu\frac{\partial\mathcal{L}}{\partial(\partial_\mu\phi_a)}\right]\delta\phi_a + \oint_{\partial\Omega} d\Sigma_\mu\,\frac{\partial\mathcal{L}}{\partial(\partial_\mu\phi_a)}\,\delta\phi_a$$

The second term comes from Gauss's theorem in four dimensions. For variations of compact support the lemma gives the field Euler–Lagrange equation of Ch. 1 §1.9.2. The surface term supplies the boundary conditions of field problems in the same way as in §A.2.2: Dirichlet data where $\delta\phi = 0$ on the boundary, and natural (Neumann-type) conditions where $\phi$ is free.

**Where the naive statement fails: gravity.** The Einstein–Hilbert Lagrangian $\sqrt{-g}\,R$ contains second derivatives of $g_{\mu\nu}$. Its variation therefore leaves a boundary term in $\partial\delta g$ that does not vanish when only $\delta g_{\mu\nu}$ is fixed on $\partial\Omega$. A well-posed Dirichlet principle needs the Gibbons–Hawking–York boundary term $\frac{1}{8\pi G}\oint\sqrt{\lvert h\rvert}\,K$ added to $S_{EH}$. Here $h$ is the induced metric on the boundary and $K$ the trace of its extrinsic curvature (Wald, *General Relativity*, Appendix E). It does not change the field equations of Ch. 0 §0.3, which is why the chapters can omit it.

**What was proved.** Stationarity under variations of compact support is equivalent to the Euler–Lagrange equations. The boundary term decides which boundary conditions make the variational problem well posed. **Where it fails.** It fails for non-smooth extremals (corners need the Weierstrass–Erdmann conditions), for Lagrangians that are not differentiable in $\dot q$, and for systems whose equations of motion are not Euler–Lagrange equations of any Lagrangian. Dissipative systems are the important case of the last kind. They are handled in §A.10, and not by pretending they have an action.

---

## A.3 — The Legendre Transform and Hamilton's Equations

### A.3.1 — Regularity and the transform

**Assumption (regularity).** The Hessian $W_{ij} = \partial^2 L/\partial\dot q_i\partial\dot q_j$ is nonsingular. Then $p_i = \partial L/\partial\dot q_i(q,\dot q,t)$ can be solved locally for $\dot q_i(q,p,t)$ by the implicit function theorem. If $L$ is strictly convex in $\dot q$, which covers any $L = \tfrac12\dot q^{\mathsf T}M(q)\dot q + \dots$ with $M$ positive definite, the inversion is global.

Define $H(q,p,t) = \sum_i p_i\dot q_i - L$, with $\dot q = \dot q(q,p,t)$ substituted. Take the differential and use the definition of $p_i$ to cancel the $d\dot q_i$ terms:

$$dH = \sum_i\left(\dot q_i\,dp_i + p_i\,d\dot q_i - \frac{\partial L}{\partial q_i}dq_i - \frac{\partial L}{\partial\dot q_i}d\dot q_i\right) - \frac{\partial L}{\partial t}dt = \sum_i\left(\dot q_i\,dp_i - \frac{\partial L}{\partial q_i}dq_i\right) - \frac{\partial L}{\partial t}dt$$

Reading off the partial derivatives gives three identities that hold **off shell**:

$$\frac{\partial H}{\partial p_i} = \dot q_i, \qquad \frac{\partial H}{\partial q_i} = -\frac{\partial L}{\partial q_i}, \qquad \frac{\partial H}{\partial t} = -\frac{\partial L}{\partial t}$$

The Euler–Lagrange equation $\dot p_i = \partial L/\partial q_i$ turns the middle identity into $\dot p_i = -\partial H/\partial q_i$. That completes Hamilton's equations (Ch. 1 §1.6.3). Along a solution, $dH/dt = \partial H/\partial t = -\partial L/\partial t$, so $H$ is conserved when $L$ has no explicit time dependence. This is the content of Ch. 1 §1.7.3, here obtained without any symmetry language.

> **[DERIVATION]** For regular $L$, the $n$ second-order Euler–Lagrange equations are equivalent to the $2n$ first-order Hamilton equations. Equivalently, Hamilton's equations are the Euler–Lagrange equations of the **phase-space action** $S_H[q,p] = \int(\sum_i p_i\dot q_i - H)\,dt$, varied independently in $q$ (endpoints fixed) and $p$ (endpoints free). Varying $p_i$ gives $\dot q_i = \partial H/\partial p_i$, and varying $q_i$ gives $\dot p_i = -\partial H/\partial q_i$.

**$H$ is not always the energy.** $H$ equals $T+V$ only when $T$ is homogeneous quadratic in $\dot q$ and $V$ is velocity independent. In a rotating frame, or with time-dependent constraints, $H$ is conserved (when $\partial_t L = 0$) but is not $T+V$.

**Where it fails: singular Lagrangians.** If $\det W = 0$, some momenta are not independent and the equations $p_i = \partial L/\partial \dot q_i$ define **primary constraints**. Maxwell theory is the key example: $\mathcal{L}$ contains no $\partial_0 A_0$, so the momentum conjugate to $A_0$ vanishes identically. Preserving that constraint in time yields Gauss's law as a secondary constraint. This is the Hamiltonian face of the gauge redundancy treated in §A.8. The systematic method is Dirac's constraint analysis (Henneaux & Teitelboim, *Quantization of Gauge Systems*).

### A.3.2 — The charged particle

From Ch. 9 §9.5.2, $L = \tfrac12 m\dot{\mathbf{r}}^2 - q\phi + q\dot{\mathbf{r}}\cdot\mathbf{A}$. The Hessian is $m\,\mathbb{1}$, so $L$ is regular, and

$$\mathbf{p} = m\dot{\mathbf{r}} + q\mathbf{A}, \qquad H = \mathbf{p}\cdot\dot{\mathbf{r}} - L = \frac{(\mathbf{p}-q\mathbf{A})^2}{2m} + q\phi$$

Under $\phi \to \phi - \partial_t\chi$, $\mathbf{A} \to \mathbf{A} + \nabla\chi$, the Lagrangian changes by $q(\partial_t\chi + \dot{\mathbf{r}}\cdot\nabla\chi) = q\,d\chi/dt$. That is a total derivative, so by §A.2.2 the motion is unchanged. The canonical momentum shifts by $q\nabla\chi$, while the **kinetic** momentum $\boldsymbol{\pi} = \mathbf{p} - q\mathbf{A} = m\dot{\mathbf{r}}$ is gauge invariant. This is the classical origin of minimal coupling $\hat{\mathbf p} \to \hat{\mathbf p} - q\mathbf A$ (Ch. 3 §3.9.4, where Gaussian units give $e\mathbf A/c$).

---

## A.4 — Poisson Brackets and the Hamiltonian Form of Noether's Theorem

**Definition** (Ch. 1 §1.6.4):

$$\{f,g\} = \sum_i\left(\frac{\partial f}{\partial q_i}\frac{\partial g}{\partial p_i} - \frac{\partial f}{\partial p_i}\frac{\partial g}{\partial q_i}\right)$$

**Properties**, all verified by direct expansion: antisymmetry $\{f,g\} = -\{g,f\}$; bilinearity; the Leibniz rule $\{f,gh\} = \{f,g\}h + g\{f,h\}$; and the **Jacobi identity** $\{f,\{g,h\}\} + \{g,\{h,f\}\} + \{h,\{f,g\}\} = 0$. In the Jacobi identity every term contains a second derivative of exactly one of $f,g,h$, and these cancel in pairs because mixed partial derivatives commute. The canonical brackets are $\{q_i,p_j\} = \delta_{ij}$ and $\{q_i,q_j\} = \{p_i,p_j\} = 0$.

**Equation of motion.** By the chain rule and Hamilton's equations, for any $f(q,p,t)$ along a solution,

$$\frac{df}{dt} = \sum_i\left(\frac{\partial f}{\partial q_i}\dot q_i + \frac{\partial f}{\partial p_i}\dot p_i\right) + \frac{\partial f}{\partial t} = \{f,H\} + \frac{\partial f}{\partial t}$$

**Generators.** A phase-space function $G$ generates the infinitesimal canonical transformation $\delta q_i = \epsilon\,\partial G/\partial p_i = \epsilon\{q_i,G\}$, $\delta p_i = -\epsilon\,\partial G/\partial q_i = \epsilon\{p_i,G\}$. To first order this preserves the canonical brackets, and it changes any function by $\delta f = \epsilon\{f,G\}$. In particular, $\delta H = \epsilon\{H,G\} = -\epsilon\{G,H\}$.

**Theorem (Hamiltonian Noether, both directions).** Let $G$ have no explicit time dependence. Then
$$\frac{dG}{dt} = 0 \quad\Longleftrightarrow\quad \{G,H\} = 0 \quad\Longleftrightarrow\quad \delta_G H = 0$$
*Proof.* The first equivalence is the equation of motion above. The second follows from $\delta_G H = -\epsilon\{G,H\}$. $\square$

So in Hamiltonian form the correspondence between symmetries and conserved quantities runs **both ways**: every conserved $G$ generates a symmetry of $H$. The Lagrangian first theorem (§A.5) proves only the direction from symmetry to conservation.

**Examples.** $G = \mathbf{n}\cdot\mathbf{P}$ generates translations, $\delta\mathbf{r}_a = \epsilon\mathbf{n}$. $G = \mathbf{n}\cdot\mathbf{L}$ generates rotations, $\delta\mathbf{r}_a = \epsilon\,\mathbf{n}\times\mathbf{r}_a$. The angular momenta close into the rotation algebra $\{L_i,L_j\} = \epsilon_{ijk}L_k$. **Poisson's theorem** follows from the Jacobi identity: if $\{F,H\} = \{G,H\} = 0$, then $\{\{F,G\},H\} = 0$, so the bracket of two conserved quantities is conserved.

> **[STRUCTURAL CONNECTION]** The map $\{\,,\} \to (i\hbar)^{-1}[\,,]$ of Ch. 1 §1.6.4 preserves antisymmetry, bilinearity, Leibniz and Jacobi. It is **not** a derivation of quantum mechanics. The Groenewold–van Hove theorem shows that no linear map can send all polynomial phase-space functions to operators while turning every Poisson bracket into $(i\hbar)^{-1}$ times the commutator. The correspondence holds exactly only on a restricted class of observables, for example polynomials of degree two or less. Canonical quantization is a structural template, and it needs ordering choices beyond that.

---

## A.5 — Noether's First Theorem in Mechanics

**Assumptions.**
1. The system has a regular Lagrangian $L(q,\dot q,t)$ (regularity is needed only for the Hamiltonian reading of the result).
2. There is a one-parameter family of transformations $q_i \to q_i + \epsilon K_i(q,\dot q,t) + \mathcal{O}(\epsilon^2)$, with $\epsilon$ a constant.
3. **Symmetry condition, off shell.** For every path $q(t)$, not just solutions, $L$ changes by a total derivative:
$$\delta L \equiv \epsilon\sum_i\left(\frac{\partial L}{\partial q_i}K_i + \frac{\partial L}{\partial\dot q_i}\dot K_i\right) = \epsilon\,\frac{dF}{dt}$$
for some function $F(q,\dot q,t)$.

Allowing $F \neq 0$ is essential, not decorative. Without it, time translation and Galilean boosts would not count as symmetries. The proof in Ch. 1 §1.7.2 sets $F = 0$, and Ch. 1 §1.7.3 then handles time translation by a separate argument. The proof here covers both cases at once.

**Proof.** Rewrite the left side using the product rule $\frac{\partial L}{\partial\dot q_i}\dot K_i = \frac{d}{dt}\big(p_iK_i\big) - \dot p_iK_i$:

$$\sum_i\left(\frac{\partial L}{\partial q_i} - \frac{d}{dt}\frac{\partial L}{\partial \dot q_i}\right)K_i + \frac{d}{dt}\sum_i p_iK_i = \frac{dF}{dt}$$

This is an **identity**, valid on every path. Define the Noether charge and the Euler–Lagrange expressions,

$$J \equiv \sum_i p_iK_i - F, \qquad \mathsf{E}_i \equiv \frac{\partial L}{\partial q_i} - \frac{d}{dt}\frac{\partial L}{\partial\dot q_i}$$

The identity then reads

$$\boxed{\frac{dJ}{dt} = -\sum_i\mathsf{E}_i\,K_i}$$

On solutions $\mathsf{E}_i = 0$, so $J$ is constant. $\square$

> **[DERIVATION]** A continuous symmetry of $L$ up to a total derivative implies the off-shell identity $\dot J = -\sum_i\mathsf{E}_iK_i$, hence on-shell conservation of $J = \sum_ip_iK_i - F$. Boundary conditions play no role. The time-endpoint argument of Ch. 1 §1.7.2 is equivalent when $F = 0$.

**The standard cases.** Each row is checked against the symmetry condition with the assumption it needs.

| Symmetry | $K_i$ | $F$ | Conserved $J$ | Requires |
|---|---|---|---|---|
| Time translation $q(t)\to q(t+\epsilon)$ | $\dot q_i$ | $L$ (since $\delta L = \epsilon\,dL/dt$ when $\partial_tL = 0$) | $\sum p_i\dot q_i - L = H$ | $\partial L/\partial t = 0$ |
| Translation along $\mathbf{n}$ | $\mathbf{n}$ on every $\mathbf{r}_a$ | 0 | $\mathbf{n}\cdot\mathbf{P}$ | $V$ depends on differences $\mathbf{r}_a - \mathbf{r}_b$ |
| Rotation about $\mathbf{n}$ | $\mathbf{n}\times\mathbf{r}_a$ | 0 | $\mathbf{n}\cdot\sum_a \mathbf{r}_a\times\mathbf{p}_a$ | $V$ depends on $\lvert\mathbf{r}_a-\mathbf{r}_b\rvert$ only |
| Galilean boost along $\mathbf{n}$ | $t\,\mathbf{n}$ on every $\mathbf{r}_a$ | $\mathbf{n}\cdot M\mathbf{X}$ | $\mathbf{n}\cdot(\mathbf{P}t - M\mathbf{X})$ | translation invariance plus $T = \sum\tfrac12 m_a\dot{\mathbf{r}}_a^2$ |

Here $M = \sum m_a$ and $\mathbf{X}$ is the centre of mass. The boost row is the **centre-of-mass theorem**, $M\mathbf{X} = \mathbf{P}t + \text{const}$. It is a genuine Noether charge with explicit time dependence, and it exists only because $F \neq 0$ is allowed. The rotation row reproduces Ch. 1 §1.7.3 with $\mathbf{n} = \hat{\mathbf z}$: $K = (-y,x,0)$ gives $J = xp_y - yp_x = L_z$.

**What was proved.** Each continuous symmetry of the stated kind yields one conserved quantity. **Where it fails.** (i) Discrete symmetries such as parity and time reversal give selection rules, not conserved charges. (ii) A symmetry of the equations of motion that is not a symmetry of $L$ up to a total derivative gives no Noether charge. (iii) With external time-dependent forces, $\partial_tL \neq 0$ and energy is not conserved. (iv) Dissipative forces are not in $L$ at all (§A.10). (v) In quantum theory a classical Noether symmetry can fail to survive regularization. This is an **anomaly** (Ch. 0 §0.10), so classical conservation is a statement about the classical action.

---

## A.6 — Noether's First Theorem for Fields

### A.6.1 — The current and the charge

**Assumptions.** Take a flat spacetime Lagrangian density $\mathcal{L}(\phi_a,\partial_\mu\phi_a)$ and an infinitesimal transformation $\phi_a \to \phi_a + \epsilon\,\Delta\phi_a$ (a *form* variation at fixed $x$) such that, **off shell**,

$$\delta\mathcal{L} = \epsilon\,\partial_\mu K^\mu$$

for some $K^\mu(\phi,\partial\phi,x)$. Spacetime transformations are included by writing their effect as a form variation, for example $\Delta\phi = -a^\nu\partial_\nu\phi$ for a translation.

**Proof.** Expand $\delta\mathcal{L}$ and use the product rule on the derivative term:

$$\delta\mathcal{L} = \epsilon\left[\frac{\partial\mathcal{L}}{\partial\phi_a}\Delta\phi_a + \frac{\partial\mathcal{L}}{\partial(\partial_\mu\phi_a)}\partial_\mu\Delta\phi_a\right] = \epsilon\left[\mathsf{E}^a\,\Delta\phi_a + \partial_\mu\!\left(\frac{\partial\mathcal{L}}{\partial(\partial_\mu\phi_a)}\Delta\phi_a\right)\right]$$

Here $\mathsf{E}^a = \partial\mathcal{L}/\partial\phi_a - \partial_\mu\big(\partial\mathcal{L}/\partial(\partial_\mu\phi_a)\big)$. Equating to $\epsilon\,\partial_\mu K^\mu$ gives the off-shell identity

$$\boxed{\partial_\mu j^\mu = -\,\mathsf{E}^a\,\Delta\phi_a, \qquad j^\mu \equiv \frac{\partial\mathcal{L}}{\partial(\partial_\mu\phi_a)}\Delta\phi_a - K^\mu}$$

On shell, $\partial_\mu j^\mu = 0$. $\square$

Ch. 1 §1.9.3 gives the special case $K^\mu = 0$.

**From local to global.** Write $\partial_\mu j^\mu = c^{-1}\partial_t j^0 + \nabla\cdot\mathbf{j}$ and define $Q(t) = c^{-1}\int_{\mathbb{R}^3} j^0\,d^3x$. Integrating over a large ball $B_R$ and applying the divergence theorem gives

$$\frac{dQ_R}{dt} = -\oint_{\partial B_R}\mathbf{j}\cdot d\mathbf{A}$$

Here $Q_R$ is the charge inside the ball. So $Q$ is conserved **only if** the flux through the sphere at infinity vanishes, which needs $\lvert\mathbf{j}\rvert$ to fall faster than $R^{-2}$. Local conservation, $\partial_\mu j^\mu = 0$, is the stronger and more useful statement, because it holds region by region (§A.9).

**Ambiguities.** The current is not unique. (i) It can be rescaled by a constant. (ii) $K^\mu$ is defined only up to an identically conserved piece. (iii) For any antisymmetric $U^{\mu\nu} = -U^{\nu\mu}$, the current $j'^\mu = j^\mu + \partial_\nu U^{\mu\nu}$ is also conserved, because $\partial_\mu\partial_\nu U^{\mu\nu} \equiv 0$. Its charge differs by a surface integral at infinity. The Belinfante improvement (§A.7.3) and the gauge-theory "superpotential" (§A.8) are both instances of (iii).

### A.6.2 — Internal U(1): the charge current of a matter field

Let $\psi$ be a complex (or Dirac) field with $\mathcal{L}_m(\psi,\bar\psi,D_\mu\psi,\overline{D_\mu\psi})$ built only from the combinations $\psi$, $\bar\psi$ and the covariant derivative of §A.1. Under the **global** transformation $\psi \to e^{iq\epsilon/\hbar}\psi$, with $A_\mu$ held fixed, $\Delta\psi = (iq/\hbar)\psi$, $\Delta\bar\psi = -(iq/\hbar)\bar\psi$, and $\mathcal{L}_m$ is invariant with $K^\mu = 0$. The Noether current is

$$j_N^\mu = \frac{\partial\mathcal{L}_m}{\partial(\partial_\mu\psi)}\frac{iq}{\hbar}\psi - \frac{iq}{\hbar}\bar\psi\,\frac{\partial\mathcal{L}_m}{\partial(\partial_\mu\bar\psi)}$$

**Identity: the Noether current is the source current.** $A_\mu$ enters $\mathcal{L}_m$ only through $D_\mu\psi = \partial_\mu\psi - (iq/\hbar)A_\mu\psi$ and its conjugate. Hence $\partial\mathcal{L}_m/\partial A_\mu = -(iq/\hbar)\psi\,\partial\mathcal{L}_m/\partial(\partial_\mu\psi) + (iq/\hbar)\bar\psi\,\partial\mathcal{L}_m/\partial(\partial_\mu\bar\psi)$, so

$$J^\mu \equiv \frac{\partial\mathcal{L}_m}{\partial A_\mu} = -\,j_N^\mu$$

The overall sign is the convention ambiguity (i) above. What matters is that the current that sources Maxwell's equations (the $A_\mu j^\mu$ term of Ch. 11 §11.1) **is** the Noether current of the global phase symmetry. For the Dirac field, $\mathcal{L}_m = \bar\psi(i\hbar c\,\gamma^\mu D_\mu - mc^2)\psi$ with $\{\gamma^\mu,\gamma^\nu\} = -2\eta^{\mu\nu}$ in this signature, which keeps $\gamma^0 = \beta$ with $\beta^2 = 1$ (see Appendix B §B.1). It gives $J^\mu = qc\,\bar\psi\gamma^\mu\psi$, hence $\rho = J^0/c = q\,\psi^\dagger\psi$ and $\mathbf J = qc\,\psi^\dagger\boldsymbol\alpha\psi$.

> **[DERIVATION]** Global U(1) invariance of the matter Lagrangian implies, by Noether's first theorem, a current with $\partial_\mu J^\mu = 0$ whenever the **matter** equations of motion hold. For minimally coupled matter this current equals $\partial\mathcal{L}_m/\partial A_\mu$. Whether $A_\mu$ obeys its own equation is irrelevant to this statement (§A.8). Reading $\psi^\dagger\psi$ as a probability density is the Born postulate, not part of the theorem (Ch. 3 §3.9.2).

---

## A.7 — Energy–Momentum: Canonical and Hilbert Tensors

### A.7.1 — Translations and the canonical tensor

**Assumption.** $\mathcal{L}$ has no explicit $x$-dependence. Under $x^\mu \to x^\mu + a^\mu$ with constant $a^\mu$, a field transported along is $\phi'(x) = \phi(x-a)$, so $\Delta\phi_a = -a^\nu\partial_\nu\phi_a$. Then $\delta\mathcal{L} = -a^\nu\partial_\nu\mathcal{L} = \partial_\mu(-a^\mu\mathcal{L})$, so $K^\mu = -a^\mu\mathcal{L}$. The Noether current of §A.6.1 is

$$j^\mu = -\frac{\partial\mathcal{L}}{\partial(\partial_\mu\phi_a)}a^\nu\partial_\nu\phi_a + a^\mu\mathcal{L} = a_\nu\,T^{\mu\nu}_{\rm can}$$

with, in the book's signature,

$$\boxed{T^{\mu\nu}_{\rm can} = -\frac{\partial\mathcal{L}}{\partial(\partial_\mu\phi_a)}\,\partial^\nu\phi_a + \eta^{\mu\nu}\mathcal{L}, \qquad \partial_\mu T^{\mu\nu}_{\rm can} = 0 \text{ on shell}}$$

There is one current for each of the four independent $a^\nu$.

**Check of signs.** Let $\pi_a = \partial\mathcal{L}/\partial(\partial_t\phi_a)$, so that $\partial\mathcal{L}/\partial(\partial_0\phi_a) = c\,\pi_a$, and use $\partial^0 = -\partial_0$:

$$T^{00}_{\rm can} = \pi_a\dot\phi_a - \mathcal{L} = \mathcal{H}, \qquad \frac{T^{0i}_{\rm can}}{c} = -\pi_a\,\partial_i\phi_a$$

The first is the Hamiltonian density. The second is the momentum density, whose integral $-\int\pi_a\nabla\phi_a\,d^3x$ is the generator of spatial translations. The energy is $\int T^{00}d^3x$ and the momentum is $c^{-1}\int T^{0i}d^3x$.

> **Note on signature.** The form $T^{\mu\nu} = \frac{\partial\mathcal L}{\partial(\partial_\mu\phi)}\partial^\nu\phi - g^{\mu\nu}\mathcal{L}$ written in Ch. 1 §1.9.3 is the correct expression in the $(+,-,-,-)$ signature. In the book's $(-,+,+,+)$ signature both terms flip sign, as boxed above, so that $T^{00} = +\mathcal{H}$.

**Example (real scalar).** For $\mathcal{L} = -\tfrac12\partial_\mu\varphi\,\partial^\mu\varphi - V(\varphi)$, we have $\partial\mathcal L/\partial(\partial_\mu\varphi) = -\partial^\mu\varphi$ and

$$T^{\mu\nu}_{\rm can} = \partial^\mu\varphi\,\partial^\nu\varphi + \eta^{\mu\nu}\mathcal{L}, \qquad T^{00} = \tfrac12 c^{-2}\dot\varphi^2 + \tfrac12(\nabla\varphi)^2 + V \geq 0 \;\text{ for } V \ge 0$$

The $c^{-2}$ arises because $\partial^0\varphi = -c^{-1}\dot\varphi$. Here $\varphi$ is normalized so that $\mathcal L$ has dimensions of energy density. This tensor is symmetric.

### A.7.2 — Lorentz transformations and angular momentum

Under $x^\mu \to x^\mu + \omega^\mu{}_\nu x^\nu$ with $\omega_{\mu\nu} = -\omega_{\nu\mu}$, a scalar field has $\Delta\varphi = -\omega^\lambda{}_\nu x^\nu\partial_\lambda\varphi$. Because $\partial_\mu(\omega^\mu{}_\nu x^\nu) = \omega^\mu{}_\mu = 0$, $\delta\mathcal{L} = \partial_\mu(-\omega^\mu{}_\nu x^\nu\mathcal{L})$. The Noether current is $j^\mu = \omega_{\lambda\nu}x^\nu T^{\mu\lambda}_{\rm can} = -\tfrac12\omega_{\lambda\nu}M^{\mu\lambda\nu}$, with

$$M^{\mu\lambda\nu} = x^\lambda T^{\mu\nu} - x^\nu T^{\mu\lambda}, \qquad \partial_\mu M^{\mu\lambda\nu} = T^{\lambda\nu} - T^{\nu\lambda} \;\;\text{(on shell)}$$

So conservation of angular momentum requires a **symmetric** energy–momentum tensor. For the scalar it holds automatically. The conserved charges are $J^{ij} = c^{-1}\int M^{0ij}d^3x = \int(x^ig^j - x^jg^i)\,d^3x$, with $\mathbf g$ the momentum density, which is the field version of $\mathbf L = \mathbf r\times\mathbf p$. The boost charges $J^{0i}$ give the relativistic centre-of-energy theorem, the analogue of the Galilean row of §A.5.

For fields with spin, $\Delta\phi$ acquires an additional spin-matrix term. $T^{\mu\nu}_{\rm can}$ is then not symmetric, and only orbital plus spin angular momentum is conserved.

### A.7.3 — Belinfante improvement: the Maxwell example

For $\mathcal{L} = -\frac{1}{4\mu_0}F_{\alpha\beta}F^{\alpha\beta}$ in vacuum, $\partial\mathcal{L}/\partial(\partial_\mu A_\alpha) = -\mu_0^{-1}F^{\mu\alpha}$, so

$$T^{\mu\nu}_{\rm can} = \frac{1}{\mu_0}F^{\mu\alpha}\partial^\nu A_\alpha + \eta^{\mu\nu}\mathcal{L}$$

This is neither symmetric nor gauge invariant. Write $\partial^\nu A_\alpha = F^\nu{}_\alpha + \partial_\alpha A^\nu$, and use the vacuum field equation $\partial_\alpha F^{\mu\alpha} = 0$ to rewrite $F^{\mu\alpha}\partial_\alpha A^\nu = \partial_\alpha(F^{\mu\alpha}A^\nu)$. Then

$$T^{\mu\nu}_{\rm can} = \underbrace{\frac{1}{\mu_0}\left(F^{\mu\alpha}F^\nu{}_\alpha - \tfrac14\eta^{\mu\nu}F_{\alpha\beta}F^{\alpha\beta}\right)}_{T^{\mu\nu}_{\rm B}} + \partial_\lambda\!\left(\frac{1}{\mu_0}F^{\mu\lambda}A^\nu\right)$$

The added term has the form $\partial_\lambda B^{\lambda\mu\nu}$ with $B^{\lambda\mu\nu} = -\mu_0^{-1}F^{\mu\lambda}A^\nu$ antisymmetric in $\lambda\mu$. It is therefore identically divergence-free, it changes the four-momentum only by a surface term, and it can be dropped. The remainder $T_{\rm B}$ is symmetric, gauge invariant, and exactly the tensor of Ch. 11 §11.8.1. It gives $T^{00}_{\rm B} = \tfrac12(\epsilon_0E^2 + B^2/\mu_0)$ and $T^{0i}_{\rm B} = (\mathbf E\times\mathbf B)^i/(\mu_0 c)$. The general Belinfante–Rosenfeld construction, Belinfante (1940) and Rosenfeld (1940), builds $B^{\lambda\mu\nu}$ from the spin current for any field. See Weinberg, *The Quantum Theory of Fields*, Vol. I (the chapter on the canonical formalism).

### A.7.4 — The Hilbert tensor

**Definition and sign convention.** In curved spacetime with signature $(-,+,+,+)$:

$$\boxed{T_{\mu\nu} = -\frac{2}{\sqrt{-g}}\,\frac{\delta S_{\rm matter}}{\delta g^{\mu\nu}}} \qquad\Longleftrightarrow\qquad \delta S_{\rm matter} = -\tfrac12\int d^4x\,\sqrt{-g}\,T_{\mu\nu}\,\delta g^{\mu\nu} = +\tfrac12\int d^4x\,\sqrt{-g}\,T^{\mu\nu}\,\delta g_{\mu\nu}$$

The second form uses $\delta g^{\mu\nu} = -g^{\mu\alpha}g^{\nu\beta}\delta g_{\alpha\beta}$. This is the convention of Ch. 1 §1.9.3 and Ch. 8 §8.1. **The minus sign is tied to the signature.** In $(+,-,-,-)$ the same physical tensor is $+(2/\sqrt{-g})\,\delta S/\delta g^{\mu\nu}$. The check below fixes the sign by requiring positive energy density.

**Two facts used repeatedly:** $\delta\sqrt{-g} = -\tfrac12\sqrt{-g}\,g_{\mu\nu}\delta g^{\mu\nu}$ (Jacobi's formula for the determinant), and $g^{\mu\nu}$ appears explicitly in every contraction of lower-index derivatives.

**Scalar check.** $S = \int\sqrt{-g}\,[-\tfrac12 g^{\mu\nu}\partial_\mu\varphi\partial_\nu\varphi - V]$ gives $\delta S/\delta g^{\mu\nu} = \sqrt{-g}\,[-\tfrac12\partial_\mu\varphi\partial_\nu\varphi - \tfrac12 g_{\mu\nu}\mathcal{L}]$. Hence

$$T_{\mu\nu} = \partial_\mu\varphi\,\partial_\nu\varphi + g_{\mu\nu}\mathcal{L}$$

In flat space this is **identical** to the canonical tensor of §A.7.1 with its indices lowered, and $T_{00} > 0$. With $+2/\sqrt{-g}$ in this signature, the energy would come out negative.

**Maxwell check.** $\delta(\sqrt{-g}\,g^{\mu\alpha}g^{\nu\beta}F_{\mu\nu}F_{\alpha\beta})/\delta g^{\mu\nu} = \sqrt{-g}\,(2F_{\mu\alpha}F_\nu{}^\alpha - \tfrac12 g_{\mu\nu}F^2)$. With the prefactor $-1/(4\mu_0)$ this gives $T_{\mu\nu} = \mu_0^{-1}(F_{\mu\alpha}F_\nu{}^\alpha - \tfrac14 g_{\mu\nu}F^2)$, which is **exactly the Belinfante tensor** $T_{\rm B}$. No improvement term is needed: the metric variation produces the symmetric, gauge-invariant tensor directly.

**Einstein's equations.** Vary $S_{EH} + S_{\rm matter}$ with $S_{EH}$ as in Ch. 0 §0.3, using $\delta(\sqrt{-g}R) = \sqrt{-g}\,(R_{\mu\nu} - \tfrac12 Rg_{\mu\nu})\,\delta g^{\mu\nu}$ + (total derivative; §A.2.4) and $\delta(-2\Lambda\sqrt{-g}) = \Lambda\sqrt{-g}\,g_{\mu\nu}\delta g^{\mu\nu}$:

$$\frac{1}{16\pi G}\left(G_{\mu\nu} + \Lambda g_{\mu\nu}\right) - \frac12 T_{\mu\nu} = 0 \quad\Longrightarrow\quad G_{\mu\nu} + \Lambda g_{\mu\nu} = 8\pi G\,T_{\mu\nu}$$

This is the boxed equation of Ch. 0 §0.3 ($c = 1$). The factor $-2$ in the definition is chosen precisely so that this coefficient comes out as $8\pi G$ with positive energy. The unknown sector $S_{\rm unknown}$ contributes its own term of the same form wherever it depends on the metric. Nothing here assumes that contribution vanishes.

**Covariant conservation from diffeomorphism invariance.** **Assumptions:** $S_{\rm matter}$ is a scalar, and the matter fields obey their own equations of motion. Under an infinitesimal diffeomorphism generated by $\xi^\mu$ (compact support), $\delta g^{\mu\nu} = \mp(\nabla^\mu\xi^\nu + \nabla^\nu\xi^\mu)$, with the sign depending on active or passive convention. The matter-field variations multiply their Euler–Lagrange expressions and drop out on shell. Invariance then requires

$$0 = \delta S_{\rm matter} = \mp\tfrac12\int\sqrt{-g}\,(-T_{\mu\nu})(2\nabla^\mu\xi^\nu) = \mp\int\sqrt{-g}\,\xi^\nu\,\nabla^\mu T_{\mu\nu}$$

The last step integrates by parts, using $\nabla_\mu(\sqrt{-g}\,V^\mu) = \partial_\mu(\sqrt{-g}\,V^\mu)$. Since $\xi$ is arbitrary,

$$\nabla^\mu T_{\mu\nu} = 0$$

This is an instance of **Noether's second theorem** (§A.8), with an arbitrary function $\xi^\mu(x)$ playing the role of the gauge parameter. It reproduces the ordering stated in Ch. 8 §8.1.

> **[DERIVATION]** $\nabla_\mu T^{\mu\nu} = 0$ follows from diffeomorphism invariance of $S_{\rm matter}$ together with the matter equations of motion. It is **not** in general a conservation law with a conserved integral, because $\nabla_\mu$ contains connection terms. A conserved charge exists when the spacetime has a **Killing vector** $k^\nu$ ($\nabla_\mu k_\nu + \nabla_\nu k_\mu = 0$). Then $J^\mu = T^{\mu\nu}k_\nu$ satisfies $\nabla_\mu J^\mu = T^{\mu\nu}\nabla_\mu k_\nu = 0$, because a symmetric tensor contracted with an antisymmetric one vanishes. That is a genuine continuity equation. In flat space the ten Killing vectors of the Poincaré group return the energy, momentum, angular momentum and boost charges of §§A.7.1–A.7.2.

**How the two tensors relate.** In flat spacetime, for scalar, Maxwell, and (using a tetrad formalism) Dirac matter, the Hilbert tensor equals the Belinfante-improved canonical tensor, up to terms that vanish on shell. The scalar and Maxwell cases are proved above. The Dirac case needs a vierbein variation and is not done here (see a treatment of spinors in curved spacetime, e.g. Birrell & Davies, *Quantum Fields in Curved Space*, or the Belinfante–Rosenfeld papers). In general relativity only the Hilbert definition is available, as Ch. 8 §8.1 states.

---

## A.8 — Noether's Second Theorem and Gauge Redundancy

**Statement.** Suppose $S$ is invariant under a transformation that depends on arbitrary functions $\alpha(x)$ and their derivatives. Then the Euler–Lagrange expressions satisfy **identities**, one per arbitrary function, that hold whether or not the equations of motion do. Noether's 1918 paper (*Invariante Variationsprobleme*) contains both theorems. A modern account is Kosmann-Schwarzbach, *The Noether Theorems* (Springer, 2011).

### A.8.1 — The U(1) identity

**Assumptions.** $S[A,\psi,\bar\psi] = \int d^4x\,[-\frac{1}{4\mu_0}F_{\mu\nu}F^{\mu\nu} + \mathcal{L}_m(\psi,\bar\psi,D\psi,\overline{D\psi})]$. The action is invariant under the **local** transformation
$$\delta A_\mu = \partial_\mu\alpha, \qquad \delta\psi = \frac{iq}{\hbar}\alpha\,\psi, \qquad \delta\bar\psi = -\frac{iq}{\hbar}\alpha\,\bar\psi$$
for arbitrary $\alpha(x)$ of compact support. Invariance holds because $F_{\mu\nu}$ is invariant and $D_\mu\psi \to e^{iq\alpha/\hbar}D_\mu\psi$.

**Proof.** For variations of compact support, §A.1 gives

$$0 = \delta S = \int d^4x\left[\frac{\delta S}{\delta A_\mu}\partial_\mu\alpha + \frac{iq}{\hbar}\alpha\left(\frac{\delta S}{\delta\psi}\psi - \bar\psi\frac{\delta S}{\delta\bar\psi}\right)\right] = \int d^4x\;\alpha\left[-\partial_\mu\frac{\delta S}{\delta A_\mu} + \frac{iq}{\hbar}\left(\frac{\delta S}{\delta\psi}\psi - \bar\psi\frac{\delta S}{\delta\bar\psi}\right)\right]$$

Since $\alpha$ is arbitrary, the fundamental lemma gives the **Noether identity**:

$$\boxed{\partial_\mu\frac{\delta S}{\delta A_\mu} \equiv \frac{iq}{\hbar}\left(\frac{\delta S}{\delta\psi}\psi - \bar\psi\frac{\delta S}{\delta\bar\psi}\right)}$$

This holds **off shell**. $\square$

### A.8.2 — What the identity does and does not say

Compute the left side explicitly. From $\mathcal{L}_{\rm Maxwell}$, $\delta S/\delta A_\mu \supset -\partial_\nu\big(\partial\mathcal{L}/\partial(\partial_\nu A_\mu)\big) = \mu_0^{-1}\partial_\nu F^{\nu\mu}$. From $\mathcal{L}_m$, the contribution is $J^\mu$ of §A.6.2. So the Maxwell equation $\delta S/\delta A_\mu = 0$ reads

$$\partial_\nu F^{\mu\nu} = \mu_0 J^\mu \qquad\Longleftrightarrow\qquad \nabla\cdot\mathbf E = \rho/\epsilon_0, \;\; \nabla\times\mathbf B - c^{-2}\partial_t\mathbf E = \mu_0\mathbf J$$

The $\nu = 0$ component checks Gauss's law: $\partial_iF^{0i} = c^{-1}\nabla\cdot\mathbf E$ with $F^{0i} = E_i/c$ from Ch. 11 §11.2.1. **The index order matters.** $\partial_\nu F^{\nu\mu} = -\mu_0J^\mu$ is the same equation.

Substituting into the identity, the Maxwell piece drops out by antisymmetry ($\partial_\mu\partial_\nu F^{\nu\mu} \equiv 0$), leaving

$$\partial_\mu J^\mu \equiv \frac{iq}{\hbar}\left(\frac{\delta S}{\delta\psi}\psi - \bar\psi\frac{\delta S}{\delta\bar\psi}\right)$$

Four consequences follow, and the chapters need each one separately.

1. **Charge conservation needs the matter equations.** $\partial_\mu J^\mu = 0$ holds when $\psi$ is on shell, whatever $A_\mu$ is doing. This is the same conclusion as Noether's **first** theorem applied to the **global** subgroup ($\alpha$ = const; §A.6.2). Local invariance gives an identity. The global subgroup plus the matter equations gives the conservation law.
2. **Consistency of Maxwell's equations.** Taking $\partial_\mu$ of $\partial_\nu F^{\mu\nu} = \mu_0J^\mu$ shows that a solution can exist only if $\partial_\mu J^\mu = 0$. This is the argument of Ch. 11 §11.5. It proves that **external** sources must be conserved for Maxwell's equations to be solvable, and it shows that the field equation and matter conservation are compatible. It is a consistency condition, not a derivation of charge conservation from the gauge field alone.
3. **The charge is a surface integral.** On the full shell, $J^\mu = \mu_0^{-1}\partial_\nu F^{\mu\nu}$ has the improper form $\partial_\nu U^{\mu\nu}$ of §A.6.1(iii). Hence $Q = \int\rho\,d^3x = \epsilon_0\oint_{S^2_\infty}\mathbf E\cdot d\mathbf A$, which is Gauss's law. This is characteristic of second-theorem symmetries: the charges of the global subgroup of a gauge symmetry are measurable at infinity.
4. **Redundancy, not symmetry.** The identity means the field equations are not independent. One combination of them holds automatically, so the Cauchy data do not determine $A_\mu$ uniquely: $A_\mu$ and $A_\mu + \partial_\mu\alpha$ with $\alpha$ vanishing at $t = 0$ evolve from the same data. Physical predictions are therefore restricted to gauge-invariant quantities, and solving the equations requires gauge fixing (Ch. 11 §11.6). In Hamiltonian form the same fact appears as the primary constraint $\pi^0 = 0$ and the Gauss-law constraint (§A.3.1). A local gauge transformation maps a physical state to **the same** physical state. That is why it is called a redundancy, and why it carries no Noether charge of its own beyond the global one.

> **[DERIVATION]** Local U(1) invariance implies, by Noether's second theorem, the off-shell identity above. Together with the matter equations of motion, it implies $\partial_\mu J^\mu = 0$. Equivalently, the conservation law is the first theorem applied to the global constant-phase subgroup. The local invariance supplies an identity, the consistency of Maxwell's equations, and the surface-integral form of the charge, but on its own it does not supply a conserved charge. This is the distinction drawn in Ch. 17 §17.2.3 and required by MCP §8.

**Which U(1).** The symmetry relevant to circuits is $U(1)_{\rm em}$, generated by $Q = T_3 + Y$ after electroweak symmetry breaking (Ch. 0 §0.4.2, §0.7). It is not $U(1)_Y$. The argument above applies verbatim to $U(1)_{\rm em}$ with $A_\mu$ the photon field. The electromagnetic current is anomaly-free in the Standard Model, so the classical conservation law survives quantization.

**The gravitational analogue.** For $S_{EH}$ the same theorem with diffeomorphism parameter $\xi^\mu$ gives the off-shell contracted Bianchi identity $\nabla^\mu G_{\mu\nu} \equiv 0$ (Ch. 8 §8.1). For the matter action it gives the result of §A.7.4.

---

## A.9 — Continuity Equation → Integral Charge Balance → KCL

### A.9.1 — From local to integral

**Assumptions.** (C1) $\partial_t\rho + \nabla\cdot\mathbf J = 0$ holds pointwise (§A.8; Ch. 11 §11.5). (C2) $V$ is a fixed region with piecewise smooth boundary $\partial V$ and outward normal. (C3) $\rho$ and $\mathbf J$ are $C^1$ on a neighbourhood of $\bar V$. Surface charges and currents are included by the standard distributional limit.

Integrate over $V$, exchange $d/dt$ with $\int_V$ (allowed because $V$ is fixed and the integrand is $C^1$), and apply the divergence theorem:

$$\boxed{\frac{dQ_V}{dt} = -\oint_{\partial V}\mathbf{J}\cdot d\mathbf{A}, \qquad Q_V = \int_V\rho\,d^3x}$$

> **[DERIVATION]** The integral charge balance is mathematically equivalent to the local continuity equation for all fixed regions. The converse follows by shrinking $V$ to a point. For a moving region, the Reynolds transport theorem adds the flux $\oint\rho\,\mathbf u\cdot d\mathbf A$ of the boundary velocity $\mathbf u$. The balance contains no approximation.

**The exactly conserved current.** Taking the divergence of the Ampère–Maxwell law gives $\nabla\cdot(\mathbf J + \epsilon_0\partial_t\mathbf E) = 0$ **identically**, which is the integral balance with $Q_V = \epsilon_0\oint\mathbf E\cdot d\mathbf A$ by Gauss's law. So

$$\oint_{\partial V}\left(\mathbf J + \epsilon_0\frac{\partial\mathbf E}{\partial t}\right)\cdot d\mathbf A = 0 \quad\text{exactly, for every closed surface}$$

The **total** current, conduction plus displacement, always obeys a Kirchhoff-type law. All the approximation in KCL lies in neglecting part of the displacement current.

### A.9.2 — The lumping assumptions

A **node** is a region $V$ enclosing a junction of conductors. Its surface $\partial V$ cuts the conductors at terminal cross-sections $S_1,\dots,S_N$, and elsewhere passes through insulator or vacuum.

- **(L1) No leakage.** Conduction current crosses $\partial V$ only through the $S_k$, so $\sigma = 0$ on the rest of $\partial V$. Define the branch currents $I_k = \int_{S_k}\mathbf J\cdot d\mathbf A$ (counted outward).
- **(L2) Negligible stray displacement current.** $\big\lvert\epsilon_0\oint_{\partial V\setminus\cup S_k}\partial_t\mathbf E\cdot d\mathbf A\big\rvert \ll \max_k\lvert I_k\rvert$. Equivalently, $\lvert dQ_V/dt\rvert \ll \max\lvert I_k\rvert$.
- **(L3) Intended storage is assigned to elements.** Charge that is *supposed* to accumulate, on capacitor plates, is not counted at the node. The node surface is drawn so that it does not cut a capacitor's dielectric. If it does, the displacement current through the gap is the capacitor's branch current, and including it there is exact by §A.9.1.
- **(L4) Well-defined branch current.** The current along each wire is the same at every cross-section between nodes. By the continuity equation in one dimension, $\partial_zI = -\partial_t\lambda$ with $\lambda$ the charge per unit length, which requires the wire's own charging current to be negligible. This is again an electrical-smallness condition. Its breakdown is the transmission line (Ch. 17 §17.10).

**The small parameter.** Let the node have size $\ell$, angular frequency $\omega$, and node voltage $V_n$ relative to its surroundings. Its stray capacitance is $C_s \sim \epsilon_0\ell$, so $\lvert dQ_V/dt\rvert \sim \omega C_s\lvert V_n\rvert$. With $\lvert V_n\rvert \sim \lvert Z\rvert\,\lvert I\rvert$ for a characteristic impedance $Z$ at the node, and $\epsilon_0 = 1/(Z_0c)$ with $Z_0 = \sqrt{\mu_0/\epsilon_0} \approx 377\,\Omega$:

$$\varepsilon_{\rm KCL} \sim \omega C_s\lvert Z\rvert \sim \frac{\omega\ell}{c}\cdot\frac{\lvert Z\rvert}{Z_0}$$

> **[APPROXIMATION]** Under (L1)–(L4), $\sum_k I_k = -dQ_V/dt$ becomes $\sum_k I_k = 0$, with a relative error of order $\varepsilon_{\rm KCL} = (\omega\ell/c)(\lvert Z\rvert/Z_0)$. KCL therefore requires electrically small nodes ($\omega\ell/c \ll 1$, the criterion of Ch. 11 §11.12.1). It **also** requires node impedances that are not too large compared with $Z_0$. A high-impedance node in a picoampere circuit can violate KCL through stray capacitance even at low frequency, which is why guard rings exist. At DC with all fields static, $dQ_V/dt = 0$ exactly and KCL is exact under (L1).

**The dual criterion for KVL.** Faraday's law $\oint_{\mathcal C}\mathbf E\cdot d\mathbf l = -d\Phi_B/dt$ is exact. Lumping chooses the loop $\mathcal C$ to run, between element terminals, through a region where $\partial_t\mathbf B$ is negligible. There $\mathbf E \approx -\nabla\varphi$, the terminal voltages $v_k = \varphi(a_k) - \varphi(b_k)$ are path independent, and their sum around the loop vanishes identically. The time-varying flux is **not dropped**: it is confined inside the inductors. There Faraday's law, applied to the element's own winding, produces the branch relation $v_L = L\,dI/dt$ as part of the sum. The neglected piece is the stray flux through the loop outside the elements, $\omega L_s\lvert I\rvert$ with $L_s \sim \mu_0\ell$. The small parameter is

$$\varepsilon_{\rm KVL} \sim \frac{\omega L_s}{\lvert Z\rvert} \sim \frac{\omega\ell}{c}\cdot\frac{Z_0}{\lvert Z\rvert}$$

> **[APPROXIMATION]** KVL in the form $\sum_k v_k = 0$, with inductive branch voltages included, holds to relative order $(\omega\ell/c)(Z_0/\lvert Z\rvert)$. KCL fails first at high impedance and KVL fails first at low impedance. Both require $\omega\ell/c \ll 1$. Energy bookkeeping in the lumped circuit is Poynting's theorem (Ch. 11 §11.8.2) integrated over the element volumes, not KVL. The full step-by-step proof of lumped KVL from Faraday's law is in [Appendix E](APPENDIX%20E.md) §E.10. This paragraph supplies only the small parameter dual to the KCL one.

**What was proved.** KCL is an exact consequence of the charge balance plus four stated lumping assumptions, with a named small parameter. **Where it fails.** It fails for stray capacitance at high-impedance nodes, for electrically long interconnects and radiation ($\omega\ell/c \gtrsim 0.1$), and for leakage through imperfect insulation. The replacement is the telegrapher's equations or full-wave analysis (Ch. 17 §17.10). The same template gives the hydraulic junction law from mass conservation, with (L2) replaced by negligible junction compliance. The mechanical and thermal "node laws" of Ch. 17 §17.4.1 keep their storage terms ($m\ddot x$, $C_{th}\dot T$) and are balance laws, not $\sum f_k = 0$.

---

## A.10 — Dissipation: The Rayleigh Function and the Bridge to R/C/L

### A.10.1 — Why dissipation is not in the action

For a closed system with time-independent $L$, §A.5 makes $H$ conserved. Linear friction $m\ddot x + b\dot x + kx = 0$ dissipates the physical energy $\tfrac12m\dot x^2 + \tfrac12kx^2$, so it cannot come from a Lagrangian of the standard form $T - V$ with time-independent $T$ and $V$. Non-standard Lagrangians do exist: for one degree of freedom the inverse problem of the calculus of variations always has a solution (Darboux), and time-independent ones exist for this equation. But their conserved energy function is then not the physical energy, and they do not generalize usefully to networks. Time-dependent constructions also exist. The Caldirola–Kanai Lagrangian $L = e^{\gamma t}\big(\tfrac12 m\dot x^2 - \tfrac12 kx^2\big)$ gives $\frac{d}{dt}(e^{\gamma t}m\dot x) + e^{\gamma t}kx = 0$, that is $m\ddot x + \gamma m\dot x + kx = 0$. But its "Hamiltonian" is not the physical energy, and its canonical quantization does not describe a physically damped quantum oscillator. Physically, dissipation arises from coupling to unobserved degrees of freedom (Ch. 10, Ch. 13). The honest classical treatment adds it as a **generalized force**.

### A.10.2 — The Lagrange–d'Alembert principle with a Rayleigh function

**Assumptions.**
- (D1) Conservative dynamics come from $L(q,\dot q)$.
- (D2) Non-conservative forces are linear in velocities and derivable from a Rayleigh function
$$\mathcal{R}(q,\dot q) = \tfrac12\sum_{ij}b_{ij}(q)\,\dot q_i\dot q_j, \qquad Q_i^{\rm diss} = -\frac{\partial\mathcal R}{\partial\dot q_i}, \qquad b_{ij} = b_{ji}, \;\; b \succeq 0$$
- (D3) External drives are generalized forces $Q_i^{\rm ext}(t)$.

The Lagrange–d'Alembert principle $\delta\int L\,dt + \int\sum_i(Q_i^{\rm diss}+Q_i^{\rm ext})\,\delta q_i\,dt = 0$, with fixed endpoints, gives by §A.2.2

$$\boxed{\frac{d}{dt}\frac{\partial L}{\partial\dot q_i} - \frac{\partial L}{\partial q_i} + \frac{\partial\mathcal R}{\partial\dot q_i} = Q_i^{\rm ext}}$$

This is **not** a stationary-action principle. It is the variational form of Newton's law with the extra forces included.

**Energy theorem.** Let $h = \sum_i\dot q_i\,\partial L/\partial\dot q_i - L$ (equal to $H$ on the Legendre image). Differentiating along a solution and using the equation above:

$$\frac{dh}{dt} = \sum_i\dot q_i\left(\frac{d}{dt}\frac{\partial L}{\partial\dot q_i} - \frac{\partial L}{\partial q_i}\right) = \sum_i\dot q_iQ_i^{\rm ext} - \sum_i\dot q_i\frac{\partial\mathcal R}{\partial\dot q_i} = P_{\rm in} - 2\mathcal R$$

The last step is Euler's theorem for the degree-2 homogeneous function $\mathcal R$. Thus $2\mathcal R \ge 0$ is the dissipated power, and $b \succeq 0$ is **passivity**. An antisymmetric part of $b_{ij}$ would do no work. Such gyroscopic or magnetic forces belong in $L$, as the $q\dot{\mathbf r}\cdot\mathbf A$ term does, not in $\mathcal R$.

### A.10.3 — Circuits and the R/C/L template

**Series RLC, mesh-charge coordinate $q$, $I = \dot q$.**
$$L = \tfrac12\mathsf L\,\dot q^2 - \frac{q^2}{2C}, \qquad \mathcal R = \tfrac12 R\,\dot q^2, \qquad Q^{\rm ext} = V_s(t) \;\;\Longrightarrow\;\; \mathsf L\ddot q + R\dot q + \frac{q}{C} = V_s(t)$$
This is KVL for the loop, with $h = \tfrac12\mathsf L I^2 + q^2/2C$ and $dh/dt = V_sI - RI^2$.

**Parallel RLC, node-flux coordinate $\Phi$, $v = \dot\Phi$.**
$$L = \tfrac12 C\,\dot\Phi^2 - \frac{\Phi^2}{2\mathsf L}, \qquad \mathcal R = \frac{\dot\Phi^2}{2R}, \qquad Q^{\rm ext} = I_s(t) \;\;\Longrightarrow\;\; C\dot v + \frac{v}{R} + \frac{1}{\mathsf L}\int v\,dt = I_s(t)$$
This is KCL for the node.

Here $\mathsf L$ is inductance, to avoid a clash with the Lagrangian $L$. The two choices are dual. In the mesh formulation magnetic energy is "kinetic". In the node formulation electric energy is "kinetic", which matches the field Lagrangian $\tfrac{\epsilon_0}{2}(E^2 - c^2B^2)$ of Ch. 11 §11.2.2, in which $\mathbf E = -\dot{\mathbf A} - \nabla\phi$ is a velocity.

**Mechanical.** $L = \tfrac12 m\dot x^2 - \tfrac12 kx^2$ and $\mathcal R = \tfrac12 b\dot x^2$ give $m\ddot x + b\dot x + kx = F(t)$.

| Template slot (Ch. 17 §17.3) | Lagrangian role | Electrical (mesh) | Mechanical |
|---|---|---|---|
| Inductor / inertia | kinetic term $\tfrac12(\cdot)\dot q^2$ | $\mathsf L$ | $m$ |
| Capacitor / compliance | potential term $q^2/2(\cdot)$ | $C$ | $1/k$ |
| Resistor / damper | Rayleigh $\tfrac12(\cdot)\dot q^2$ | $R$ | $b$ |
| Source | generalized force | $V_s$ | $F$ |

> **[STRUCTURAL CONNECTION]** The electrical, mechanical and hydraulic second-order systems share the Lagrange–Rayleigh form $\mathsf M\ddot q + \mathsf B\dot q + \mathsf K q = Q$ because each has one quadratic kinetic store, one quadratic potential store and one linear dissipation. That is a shared mathematical structure, not a common derivation (Ch. 17 §17.7). The coefficients $\mathsf L$ and $C$ follow from integrating the field energies over the element under the lumping assumptions of §A.9 (`[APPROXIMATION]`, small parameter $\omega\ell/c$). The coefficient $R$, and every $b_{ij}$, is a **constitutive** input: Ohm's law or viscosity, understood within linear response (Ch. 13). It is not a consequence of the action or of any conservation law.

> **[PHENOMENOLOGICAL]** The quadratic form of $\mathcal R$ encodes the assumption of **linear** dissipation, which holds near equilibrium. Coulomb friction, diode conduction, turbulent pipe losses ($\Delta p \propto Q^2$) and hysteresis do not fit a quadratic Rayleigh function. They need a non-quadratic dissipation potential or no potential at all. Symmetry of $b_{ij}$ in multi-port linear dissipation is the Onsager reciprocity condition, which needs microscopic time-reversal arguments. It is assumed here, not proved.

**What was proved.** With dissipation added as a Rayleigh force, the Euler–Lagrange machinery reproduces the R/C/L network equations, and the energy theorem gives dissipated power $2\mathcal R$. **Where it fails.** It fails for nonlinear dissipation, for memory effects (frequency-dependent $R(\omega)$, dielectric relaxation), for distributed systems ($\omega\ell/c$ not small), and in quantum regimes where the bath must be modelled explicitly.

---

## A.11 — Summary

| Result | Statement | Assumptions | Used in |
|---|---|---|---|
| First variation | $\delta S = \int\mathsf E\,\eta\,dt + [p\,\eta]_{t_1}^{t_2}$; fields: plus $\oint d\Sigma_\mu\,\partial\mathcal L/\partial(\partial_\mu\phi)\,\delta\phi$ | $C^2$ Lagrangian; smooth variations | Ch. 1 §1.5.1, §1.9.2 |
| Euler–Lagrange | $\frac{d}{dt}\partial L/\partial\dot q - \partial L/\partial q = 0$ | fixed endpoints, or natural BCs $p = 0$ | Ch. 1 §1.5; Ch. 9 §9.5; Ch. 11 §11.3 |
| Euler–Poisson | fourth-order interior equation, two BCs per end | $L(q,\dot q,\ddot q)$ | Ch. 16 (beam) |
| Total-derivative freedom | $L \to L + dG/dt$ leaves EOM, shifts $p$ | fixed endpoints | Ch. 1 §1.6.1; Ch. 9 §9.5.2 |
| Hamilton's equations | $\dot q = \partial H/\partial p$, $\dot p = -\partial H/\partial q$; $dH/dt = -\partial_tL$ | regular Hessian | Ch. 1 §1.6; Ch. 9 §9.6 |
| Poisson dynamics | $\dot f = \{f,H\} + \partial_tf$; conserved $G$ iff $\{G,H\} = 0$ | canonical coordinates | Ch. 1 §1.6.4; Ch. 9 §9.6.2 |
| Noether I (mechanics) | $\dot J = -\sum\mathsf E_iK_i$, $J = \sum p_iK_i - F$ | $\delta L = \epsilon\,dF/dt$ off shell | Ch. 1 §1.7 |
| Noether I (fields) | $\partial_\mu j^\mu = -\mathsf E^a\Delta\phi_a$ | $\delta\mathcal L = \epsilon\,\partial_\mu K^\mu$ off shell; falloff for global $Q$ | Ch. 1 §1.9.3; Ch. 3 §3.9.2 |
| Source = Noether current | $J^\mu = \partial\mathcal L_m/\partial A_\mu = -j_N^\mu$ | minimal coupling | Ch. 11 §11.1, §11.5 |
| Canonical $T^{\mu\nu}$ | $-\frac{\partial\mathcal L}{\partial(\partial_\mu\phi)}\partial^\nu\phi + \eta^{\mu\nu}\mathcal L$, with $T^{00} = \mathcal H$ | translation invariance; $(-,+,+,+)$ | Ch. 1 §1.9.3 |
| Angular momentum | $\partial_\mu M^{\mu\lambda\nu} = T^{\lambda\nu} - T^{\nu\lambda}$ | Lorentz invariance; symmetric $T$ (or spin term) | Ch. 1 §1.7.3 |
| Belinfante = Maxwell $T$ | $T_{\rm can} = T_{\rm B} + \partial_\lambda B^{\lambda\mu\nu}$ | vacuum Maxwell, on shell | Ch. 11 §11.8.1 |
| Hilbert $T_{\mu\nu}$ | $-(2/\sqrt{-g})\,\delta S_m/\delta g^{\mu\nu}$; equals improved canonical in flat space (scalar, Maxwell) | $(-,+,+,+)$ signature | Ch. 0 §0.3; Ch. 1 §1.9.3; Ch. 8 §8.1 |
| Covariant conservation | $\nabla_\mu T^{\mu\nu} = 0$; conserved charge only with a Killing vector | diffeo invariance; matter on shell | Ch. 8 §8.1 |
| Noether II (U(1)) | $\partial_\mu\,\delta S/\delta A_\mu \equiv (iq/\hbar)(\dots)$ off shell; $\partial_\mu J^\mu = 0$ needs matter EOM | local U(1) invariance | Ch. 11 §11.5–11.6; Ch. 17 §17.2.3 |
| Gauss charge | $Q = \epsilon_0\oint\mathbf E\cdot d\mathbf A$ | full shell | Ch. 11 §11.4 |
| Integral charge balance | $dQ_V/dt = -\oint\mathbf J\cdot d\mathbf A$; total current exactly solenoidal | fixed $V$; $C^1$ fields | Ch. 11 §11.12.3; Ch. 17 §17.4.1 |
| KCL | $\sum I_k = 0$, error $\sim(\omega\ell/c)(\lvert Z\rvert/Z_0)$ | (L1)–(L4) | Ch. 11 §11.12.3; Ch. 17 §17.4; Ch. 18 |
| KVL (lumped) | $\sum v_k = 0$ incl. $\mathsf L\,dI/dt$, error $\sim(\omega\ell/c)(Z_0/\lvert Z\rvert)$ | flux confined to elements | Ch. 11 §11.12.2; Ch. 17 §17.4.2 |
| Rayleigh–Lagrange | $\frac{d}{dt}\partial_{\dot q}L - \partial_qL + \partial_{\dot q}\mathcal R = Q^{\rm ext}$; $\dot h = P_{\rm in} - 2\mathcal R$ | linear, symmetric, positive dissipation | Ch. 17 §17.3, §17.7, §17.9 |

---

**References** (standard texts; no claim here depends on a single page): Goldstein, Poole & Safko, *Classical Mechanics*, 3rd ed. (2002); Landau & Lifshitz, *Mechanics* and *The Classical Theory of Fields*; Gelfand & Fomin, *Calculus of Variations*; Arnold, *Mathematical Methods of Classical Mechanics*; Noether, "Invariante Variationsprobleme", *Nachr. Ges. Wiss. Göttingen* (1918); Kosmann-Schwarzbach, *The Noether Theorems* (2011); Weinberg, *The Quantum Theory of Fields*, Vol. I; Wald, *General Relativity*; Carroll, *Spacetime and Geometry*; Jackson, *Classical Electrodynamics*, 3rd ed.; Henneaux & Teitelboim, *Quantization of Gauge Systems* (1992).

End of Appendix A
