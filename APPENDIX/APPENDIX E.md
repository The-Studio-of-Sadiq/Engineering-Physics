# Appendix E — Continuum Balance Laws and Their Reduction to Lumped Networks

This appendix supplies the proofs that the continuum and Bridge C chapters state, sketch, or use without derivation. It proves the Reynolds transport theorem; derives the local mass, momentum, and energy balances from their integral forms; proves the symmetry of the Cauchy stress from angular-momentum balance; derives Navier–Stokes from the Newtonian constitutive assumption; solves Hagen–Poiseuille flow exactly; derives the heat equation and the lumped-capacitance model, with an explicit error estimate in the Biot number; reduces Maxwell's equations to the telegrapher's equations and then to a lumped ladder; derives KVL from Faraday's law by lumping, with the inductive branch voltage kept; proves Poynting's theorem and the lumped port-power identity $P = v\,i$; derives the Euler–Bernoulli beam from three-dimensional elasticity and states what Timoshenko adds; and proves the Buckingham $\pi$ theorem. The chapters that rely on these results are [Ch. 11](../CHAPTERS/CHAPTER%2011.md) (§11.8, §11.12), [Ch. 15](../CHAPTERS/CHAPTER%2015.md) (§15.3–§15.8), [Ch. 16](../CHAPTERS/CHAPTER%2016.md) (§16.2, §16.3, §16.7.2, §16.10), [Ch. 17](../CHAPTERS/CHAPTER%2017.md) (§17.1, §17.4, §17.10), [Ch. 19](../CHAPTERS/CHAPTER%2019.md) (§19.6, §19.7), and [Ch. 20](../CHAPTERS/CHAPTER%2020.md) (§20.2), together with the worked examples [03](../EXAMPLES/03%20Maxwell-to-Circuit.md), [04](../EXAMPLES/04%20Heat-Equation-to-Thermal-RC.md), and [05](../EXAMPLES/05%20Navier-Stokes-to-Fluid-Network.md).

Two distinctions organise everything that follows, and they are the distinctions the book insists on throughout. First, **balance laws are not constitutive laws.** Mass, momentum, angular momentum, energy, and charge balances hold for any continuum; Newtonian viscosity, Fourier conduction, Hooke elasticity, and Ohm conduction are closures that describe a particular class of material and can fail without any conservation law failing. Second, **lumping is an approximation with a small parameter**, never a free identity. Each section below names which steps are exact and which step discards something.

**Notation.** It matches Ch. 15: velocity $\mathbf{v}$, density $\rho$, Cauchy stress $\sigma_{ij}$ with traction $t_i = \sigma_{ij}n_j$, strain-rate tensor $\dot\varepsilon_{ij} = \tfrac12(\partial_i v_j + \partial_j v_i)$, material derivative $D/Dt = \partial_t + \mathbf{v}\cdot\nabla$, specific internal energy $e$, heat flux $\mathbf{q}$, volumetric heat source $\dot Q_{vol}$. Thermal conductivity is $\kappa$ (as in Ch. 16 and Ch. 19; Example 04 writes $k$). Summation over repeated indices is implied.

---

## E.1 — The Reynolds Transport Theorem

### E.1.1 — Setting and assumptions

Label each material particle by its position $\mathbf{X}$ in a reference configuration at $t=0$. The motion is a map $\mathbf{x} = \boldsymbol{\chi}(\mathbf{X},t)$ with velocity $\mathbf{v}(\mathbf{x},t) = \partial_t\boldsymbol{\chi}(\mathbf{X},t)$ evaluated at $\mathbf{X} = \boldsymbol{\chi}^{-1}(\mathbf{x},t)$. Assume:

1. $\boldsymbol{\chi}$ is continuously differentiable in $\mathbf{X}$ and $t$ and invertible at each $t$ — no fracture, cavitation, or interpenetration;
2. the deformation gradient $F_{iK} = \partial\chi_i/\partial X_K$ has $J = \det F > 0$;
3. the field $f(\mathbf{x},t)$ being transported is continuously differentiable on a neighbourhood of the material volume $V_m(t) = \boldsymbol{\chi}(V_0,t)$.

The continuum hypothesis itself (Ch. 15 §15.1.1) is presupposed: the fields are coarse-grained averages over a volume much larger than the microscopic scale and much smaller than the scale on which the fields vary.

### E.1.2 — Euler's expansion formula

**Lemma.** $\partial J/\partial t\,|_{\mathbf{X}} = J\,\nabla\cdot\mathbf{v}$.

*Proof.* Jacobi's formula for the derivative of a determinant gives $dJ = J\,\mathrm{tr}(F^{-1}dF)$. Differentiating $F$ in time at fixed $\mathbf{X}$ and using the chain rule,

$$\frac{\partial F_{iK}}{\partial t} = \frac{\partial v_i}{\partial X_K} = \frac{\partial v_i}{\partial x_j}\frac{\partial x_j}{\partial X_K} = (\partial_j v_i)\,F_{jK}$$

so $\partial_t F = (\nabla\mathbf{v})F$ with $(\nabla\mathbf{v})_{ij} = \partial_j v_i$. Then $\mathrm{tr}(F^{-1}\partial_t F) = \mathrm{tr}(F^{-1}(\nabla\mathbf{v})F) = \mathrm{tr}(\nabla\mathbf{v}) = \nabla\cdot\mathbf{v}$, by cyclicity of the trace. $\square$

### E.1.3 — The theorem

**Theorem (Reynolds).** Under E.1.1,

$$\frac{d}{dt}\int_{V_m(t)} f\,dV = \int_{V_m(t)}\left(\frac{\partial f}{\partial t} + \nabla\cdot(f\mathbf{v})\right)dV = \int_{V_m(t)}\frac{\partial f}{\partial t}\,dV + \oint_{\partial V_m(t)} f\,\mathbf{v}\cdot\hat n\,dA$$

*Proof.* Change variables to the fixed reference volume, $dV = J\,dV_0$:

$$\frac{d}{dt}\int_{V_m(t)} f\,dV = \frac{d}{dt}\int_{V_0} f(\boldsymbol{\chi}(\mathbf{X},t),t)\,J(\mathbf{X},t)\,dV_0$$

The domain $V_0$ no longer depends on $t$, so by assumption 3 the derivative passes inside the integral. The time derivative of $f$ at fixed $\mathbf{X}$ is the material derivative $Df/Dt = \partial_t f + \mathbf{v}\cdot\nabla f$, and by the lemma $\partial_t J = J\nabla\cdot\mathbf{v}$. Therefore

$$\frac{d}{dt}\int_{V_m(t)} f\,dV = \int_{V_0}\left(\frac{Df}{Dt} + f\,\nabla\cdot\mathbf{v}\right)J\,dV_0 = \int_{V_m(t)}\left(\frac{\partial f}{\partial t} + \nabla\cdot(f\mathbf{v})\right)dV$$

using $\mathbf{v}\cdot\nabla f + f\nabla\cdot\mathbf{v} = \nabla\cdot(f\mathbf{v})$. The surface form follows from the divergence theorem. $\square$

> **[DERIVATION]** The Reynolds transport theorem is an identity of calculus given a smooth, invertible motion. No physics beyond the existence of a continuum velocity field enters.

### E.1.4 — Arbitrary control volumes

Engineering balances are written over control volumes that are not material: a pipe section, a heat-exchanger shell, a tank with a moving free surface. Let $V_c(t)$ have boundary points moving with velocity $\mathbf{w}$. Applying the same argument with the flow map of $\mathbf{w}$ in place of $\mathbf{v}$,

$$\frac{d}{dt}\int_{V_c(t)} f\,dV = \int_{V_c}\frac{\partial f}{\partial t}\,dV + \oint_{\partial V_c} f\,\mathbf{w}\cdot\hat n\,dA$$

If $f$ obeys a balance law $\partial_t f + \nabla\cdot(f\mathbf{v} + \mathbf{j}) = s$ (convective flux $f\mathbf{v}$, non-convective flux $\mathbf{j}$, production $s$), then eliminating $\partial_t f$ gives the **control-volume balance**

$$\frac{d}{dt}\int_{V_c(t)} f\,dV + \oint_{\partial V_c} \left[f(\mathbf{v}-\mathbf{w}) + \mathbf{j}\right]\cdot\hat n\,dA = \int_{V_c} s\,dV$$

This is the form behind Step 1 and Step 2 of the lumping procedure in Ch. 17 §17.1.1: it is exact, and it is the last exact statement before the lumping step.

### E.1.5 — Where it fails

The theorem fails where the motion is not smooth. Across a shock, a contact discontinuity, or a phase boundary, $f$ jumps, and the local differential form is replaced by jump conditions (Rankine–Hugoniot) derived from the same integral balance applied to a pillbox straddling the surface. The integral balance survives; only its localisation fails. It also fails, more fundamentally, when the continuum hypothesis does: at Knudsen numbers $Kn = \ell_{mfp}/L$ that are not small, there is no well-defined local velocity field to transport.

---

## E.2 — From Integral to Local Balances: Mass and Linear Momentum

### E.2.1 — The localisation lemma

**Lemma.** If $g$ is continuous on a region $\Omega$ and $\int_V g\,dV = 0$ for every subvolume $V\subset\Omega$, then $g\equiv0$ on $\Omega$.

*Proof.* Suppose $g(\mathbf{x}_0) > 0$. By continuity there is a ball $B_\delta(\mathbf{x}_0)$ on which $g > g(\mathbf{x}_0)/2$, so $\int_{B_\delta} g\,dV > 0$, a contradiction; likewise for $g(\mathbf{x}_0) < 0$. $\square$

The lemma is how every postulated integral balance becomes a PDE. It requires continuity of the integrand, which is exactly what fails at the discontinuities of E.1.5.

### E.2.2 — Mass

**Postulate.** The mass of a material volume is constant: $\frac{d}{dt}\int_{V_m}\rho\,dV = 0$.

Reynolds with $f = \rho$ and localisation give

$$\frac{\partial\rho}{\partial t} + \nabla\cdot(\rho\mathbf{v}) = 0 \qquad\Longleftrightarrow\qquad \frac{D\rho}{Dt} + \rho\nabla\cdot\mathbf{v} = 0$$

which is Ch. 15 §15.4.1. Its status is as Ch. 15 states it: for a single species of fixed particle mass $m$ it follows from particle-number conservation; it is not a consequence of a fundamental $U(1)$ in general.

**Corollary (transport of specific quantities).** For any specific (per-unit-mass) quantity $\phi$,

$$\frac{d}{dt}\int_{V_m}\rho\phi\,dV = \int_{V_m}\rho\frac{D\phi}{Dt}\,dV$$

*Proof.* Reynolds gives the integrand $\partial_t(\rho\phi) + \nabla\cdot(\rho\phi\mathbf{v}) = \phi[\partial_t\rho + \nabla\cdot(\rho\mathbf{v})] + \rho[\partial_t\phi + \mathbf{v}\cdot\nabla\phi]$, and the first bracket vanishes by mass balance. $\square$

### E.2.3 — Linear momentum and the Cauchy tetrahedron

**Postulate (Euler's first law).** For every material volume,

$$\frac{d}{dt}\int_{V_m}\rho\mathbf{v}\,dV = \oint_{\partial V_m}\mathbf{t}^{(\hat n)}\,dA + \int_{V_m}\mathbf{f}\,dV$$

where $\mathbf{t}^{(\hat n)}(\mathbf{x},t)$ is the surface force per unit area (traction) on a surface element with outward normal $\hat n$, and $\mathbf{f}$ is the body force per unit volume. This is Newton's second law applied to a continuum, and it is the place where the "short-range contact force" idealisation enters: the force exerted by the outside on the inside is assumed to be representable as a surface density depending only on position, time, and the local normal (Cauchy's postulate).

**Theorem (Cauchy).** The traction is linear in $\hat n$: $t_i^{(\hat n)} = \sigma_{ij}n_j$ for a tensor field $\sigma_{ij}$.

*Proof.* Take a tetrahedron with three faces in the coordinate planes, through a point $\mathbf{x}_0$, and an oblique face with outward normal $\hat n$ (all $n_j > 0$) at distance $h$ from $\mathbf{x}_0$. If the oblique face has area $A$, the coordinate face with outward normal $-\hat e_j$ has area $A n_j$, and the volume is $Ah/3$. Apply the momentum postulate, using the corollary of E.2.2 for the left side:

$$\int_{tet}\left(\rho\frac{D\mathbf{v}}{Dt} - \mathbf{f}\right)dV = \int_{A}\mathbf{t}^{(\hat n)}\,dA + \sum_j\int_{A n_j}\mathbf{t}^{(-\hat e_j)}\,dA$$

The left side is bounded by a constant times $Ah$ (bounded integrand times volume). Divide by $A$ and let $h\to0$; by continuity of the traction in $\mathbf{x}$,

$$\mathbf{t}^{(\hat n)} + \sum_j n_j\,\mathbf{t}^{(-\hat e_j)} = 0$$

Applying the same argument to a thin slab with faces $\pm\hat n$ gives Newton's third law in the form $\mathbf{t}^{(-\hat n)} = -\mathbf{t}^{(\hat n)}$. Hence $\mathbf{t}^{(\hat n)} = \sum_j n_j\mathbf{t}^{(\hat e_j)}$. Defining $\sigma_{ij} = t_i^{(\hat e_j)}$ gives $t_i^{(\hat n)} = \sigma_{ij}n_j$; normals with some $n_j<0$ follow by reorienting the tetrahedron. $\square$

> **[DERIVATION]** Cauchy's theorem follows from the momentum postulate plus continuity of the traction. The surface-to-volume scaling ($A$ versus $Ah$) is the whole argument: inertia and body forces are volume effects and cannot balance an imbalance in surface forces on a vanishing tetrahedron.

### E.2.4 — Cauchy's equation of motion

Substituting $t_i = \sigma_{ij}n_j$ into the postulate and using the divergence theorem, $\oint\sigma_{ij}n_j\,dA = \int\partial_j\sigma_{ij}\,dV$. Localisation gives

$$\rho\frac{Dv_i}{Dt} = \partial_j\sigma_{ij} + f_i$$

and, adding $v_i$ times the mass balance, the conservation form

$$\frac{\partial(\rho v_i)}{\partial t} + \partial_j\left(\rho v_i v_j - \sigma_{ij}\right) = f_i$$

This is Ch. 15 §15.4.2. No constitutive information has been used: Cauchy's equation holds equally for water, steel, and blood. Its connection to translational symmetry (Noether) is the one Ch. 15 states; the derivation here starts from the integral postulate rather than from an action, which is how continuum mechanics is usually built and has the advantage of admitting dissipative stresses that no simple action produces.

---

## E.3 — Symmetry of the Cauchy Stress from Angular Momentum

### E.3.1 — Assumptions

The continuum is **non-polar**: (a) there are no body couples (torque per unit volume not arising as $\mathbf{x}\times\mathbf{f}$), (b) there are no couple stresses (torque per unit area not arising as $\mathbf{x}\times\mathbf{t}$), and (c) there is no intrinsic angular momentum density (spin) of the material elements.

### E.3.2 — Proof

**Postulate (Euler's second law).** About a fixed origin,

$$\frac{d}{dt}\int_{V_m}\mathbf{x}\times\rho\mathbf{v}\,dV = \oint_{\partial V_m}\mathbf{x}\times\mathbf{t}\,dA + \int_{V_m}\mathbf{x}\times\mathbf{f}\,dV$$

In components, with the Levi-Civita symbol $\epsilon_{ijk}$: the left side, by the corollary of E.2.2 with $\phi = \epsilon_{ijk}x_jv_k$ and $Dx_j/Dt = v_j$, is

$$\int\rho\,\epsilon_{ijk}\left(v_jv_k + x_j\frac{Dv_k}{Dt}\right)dV = \int\rho\,\epsilon_{ijk}x_j\frac{Dv_k}{Dt}\,dV$$

since $\epsilon_{ijk}v_jv_k = 0$. The surface term, by the divergence theorem, is

$$\oint\epsilon_{ijk}x_j\sigma_{kl}n_l\,dA = \int\epsilon_{ijk}\partial_l(x_j\sigma_{kl})\,dV = \int\epsilon_{ijk}\left(\delta_{jl}\sigma_{kl} + x_j\partial_l\sigma_{kl}\right)dV = \int\left(\epsilon_{ijk}\sigma_{kj} + \epsilon_{ijk}x_j\partial_l\sigma_{kl}\right)dV$$

Collecting, the postulate becomes

$$\int_{V_m}\epsilon_{ijk}x_j\left(\rho\frac{Dv_k}{Dt} - \partial_l\sigma_{kl} - f_k\right)dV = \int_{V_m}\epsilon_{ijk}\sigma_{kj}\,dV$$

The bracket on the left vanishes by Cauchy's equation (E.2.4). So $\int\epsilon_{ijk}\sigma_{kj}\,dV = 0$ for every volume, and localisation gives $\epsilon_{ijk}\sigma_{kj} = 0$, i.e. $\sigma_{23} = \sigma_{32}$, $\sigma_{31} = \sigma_{13}$, $\sigma_{12} = \sigma_{21}$. $\square$

> **[DERIVATION]** Given linear-momentum balance, angular-momentum balance for a non-polar continuum is *equivalent* to $\sigma_{ij} = \sigma_{ji}$. It is not an independent equation of motion; its entire content is the symmetry of the stress. This is the result Ch. 15 §15.3.1 cites.

### E.3.3 — Where it fails

Each assumption of E.3.1 can fail. Ferrofluids in a magnetic field experience a body couple $\mathbf{M}\times\mathbf{B}$, and their stress is not symmetric; polarised dielectrics in a field likewise ($\mathbf{P}\times\mathbf{E}$). Granular media, foams, liquid crystals, and lattice materials at scales comparable to their microstructure are modelled as Cosserat (micropolar) continua with couple stresses and independent microrotation. In all of these the antisymmetric part of $\sigma_{ij}$ is balanced by the couple terms, and the six-component stress of Ch. 15 is incomplete.

---

## E.4 — The Energy Balance

### E.4.1 — Postulate

**Postulate (first law for a material volume).** With $e$ the specific internal energy, $\mathbf{q}$ the heat flux (outward-positive), and $\dot Q_{vol}$ the volumetric heat supply,

$$\frac{d}{dt}\int_{V_m}\rho\left(e + \tfrac12|\mathbf{v}|^2\right)dV = \oint_{\partial V_m}\left(\mathbf{t}\cdot\mathbf{v} - \mathbf{q}\cdot\hat n\right)dA + \int_{V_m}\left(\mathbf{f}\cdot\mathbf{v} + \dot Q_{vol}\right)dV$$

The right side is the rate of work by surface and body forces plus the rate of heat supply.

### E.4.2 — Local total-energy balance

Using the corollary of E.2.2, $\mathbf{t}\cdot\mathbf{v} = \sigma_{ij}n_jv_i$, the divergence theorem, and localisation:

$$\rho\frac{D}{Dt}\left(e + \tfrac12|\mathbf{v}|^2\right) = \partial_j(\sigma_{ij}v_i) - \nabla\cdot\mathbf{q} + f_iv_i + \dot Q_{vol}$$

### E.4.3 — Separating mechanical and thermal energy

Contract Cauchy's equation with $v_i$. This is not a new law; it is a consequence of momentum balance, the **mechanical energy theorem**:

$$\rho\frac{D}{Dt}\left(\tfrac12|\mathbf{v}|^2\right) = v_i\partial_j\sigma_{ij} + f_iv_i$$

Subtracting from E.4.2, and using $\partial_j(\sigma_{ij}v_i) - v_i\partial_j\sigma_{ij} = \sigma_{ij}\partial_jv_i = \sigma_{ij}\dot\varepsilon_{ij}$ (the antisymmetric part of $\partial_jv_i$ drops out because $\sigma$ is symmetric, E.3):

$$\rho\frac{De}{Dt} = \sigma_{ij}\dot\varepsilon_{ij} - \nabla\cdot\mathbf{q} + \dot Q_{vol}$$

This is the equation of Ch. 15 §15.4.3. Now split the stress into pressure and viscous (deviatoric-plus-bulk) parts, $\sigma_{ij} = -p\,\delta_{ij} + \tau_{ij}$:

$$\sigma_{ij}\dot\varepsilon_{ij} = -p\,\nabla\cdot\mathbf{v} + \Phi, \qquad \Phi \equiv \tau_{ij}\dot\varepsilon_{ij}$$

The term $-p\nabla\cdot\mathbf{v}$ is the **reversible** work of compression: it is positive when the fluid is compressed and negative when it expands, and it is exchanged back and forth between kinetic and internal energy. Only $\Phi$ — the viscous dissipation — is sign-definite, and its sign ($\Phi\geq0$) is a constraint that the second law places on the constitutive law (E.5.4), not a consequence of the energy balance. The full stress power $\sigma_{ij}\dot\varepsilon_{ij}$ is not "always positive"; that statement is true only of its viscous part.

> **[DERIVATION]** The internal-energy equation is the first law minus the mechanical energy theorem. The split into reversible compression work and dissipation is exact; the sign of the dissipation is a second-law constraint on the closure.

---

## E.5 — The Newtonian Constitutive Law and the Navier–Stokes Equations

### E.5.1 — What is being assumed

Cauchy's equation has more unknowns than equations: $\sigma_{ij}$ needs a closure. For a Newtonian fluid we assume:

1. **Fluidity.** At rest the stress is isotropic, $\sigma_{ij} = -p\,\delta_{ij}$, with $p$ the thermodynamic pressure.
2. **Linearity and locality.** The viscous stress $\tau_{ij}$ is a linear function of the velocity gradient $\partial_lv_k$ at the same point and time — no memory, no gradient-of-gradient terms.
3. **Frame indifference.** The viscous stress cannot depend on the antisymmetric part $W_{kl} = \tfrac12(\partial_lv_k - \partial_kv_l)$, which describes local rigid rotation; a fluid in rigid rotation has no viscous stress.
4. **Isotropy.** The linear map has no preferred direction.

> **[PHENOMENOLOGICAL]** The Newtonian law is a constitutive assumption, not a consequence of any balance law. Its microscopic foundation, where it exists, is the linear-response (Green–Kubo) framework of Ch. 13 §13.7, which supplies $\mu$ as a transport coefficient in the regime of small gradients; it does not supply the linear form for polymer solutions, suspensions, or blood at low shear rate (Ch. 15 §15.12.2).

### E.5.2 — The isotropic linear form

By assumptions 2–3, $\tau_{ij} = C_{ijkl}\dot\varepsilon_{kl}$. By isotropy, $C_{ijkl}$ is an isotropic fourth-order tensor, and every such tensor has the form $a\,\delta_{ij}\delta_{kl} + b\,\delta_{ik}\delta_{jl} + c\,\delta_{il}\delta_{jk}$ (a classical representation theorem; a proof is in R. Aris, *Vectors, Tensors, and the Basic Equations of Fluid Mechanics*, Prentice-Hall 1962, reprinted Dover). Contracting with the symmetric $\dot\varepsilon_{kl}$, the $b$ and $c$ terms combine:

$$\tau_{ij} = 2\mu\,\dot\varepsilon_{ij} + \lambda\,\dot\varepsilon_{kk}\,\delta_{ij}$$

with $2\mu = b + c$ and $\lambda = a$. Symmetry of $\tau_{ij}$ — required by E.3 — is automatic. This is the relation of Ch. 15 §15.6.1, and the bulk viscosity is $\zeta_b = \lambda + \tfrac23\mu$.

### E.5.3 — Substitution into Cauchy's equation

For constant $\mu$ and $\lambda$,

$$\partial_j\tau_{ij} = \mu\,\partial_j(\partial_iv_j + \partial_jv_i) + \lambda\,\partial_i(\nabla\cdot\mathbf{v}) = \mu\nabla^2v_i + (\mu+\lambda)\,\partial_i(\nabla\cdot\mathbf{v})$$

so Cauchy's equation becomes the **compressible Navier–Stokes equation**

$$\rho\frac{D\mathbf{v}}{Dt} = -\nabla p + \mu\nabla^2\mathbf{v} + (\mu+\lambda)\nabla(\nabla\cdot\mathbf{v}) + \mathbf{f}$$

> **[DERIVATION]** Navier–Stokes is Cauchy's equation with the Newtonian closure substituted, for spatially uniform $\mu$, $\lambda$. If $\mu$ varies (temperature-dependent viscosity), the extra term $2(\partial_j\mu)\dot\varepsilon_{ij}$ must be kept.

> **[APPROXIMATION]** Incompressibility. If $\nabla\cdot\mathbf{v} = 0$, the bulk term vanishes regardless of $\lambda$, giving $\rho\,D\mathbf{v}/Dt = -\nabla p + \mu\nabla^2\mathbf{v} + \rho\mathbf{g}$ (Ch. 15 §15.6.2). **Small parameter:** the relative density variation $\delta\rho/\rho$, which for steady isothermal flow scales as $Ma^2$ with $Ma = U/c_s$, and for unsteady flow also requires $L/(c_sT)\ll1$ (acoustic transit time small compared with the flow time $T$). Thermal expansion gives a separate contribution $\beta\Delta T$; keeping it only in the buoyancy term is the Boussinesq approximation. **Fails when:** $Ma\gtrsim0.3$, in acoustics, in water hammer (Ch. 19 §19.7), or with large heating.

In the incompressible case $p$ is no longer a thermodynamic variable but a Lagrange multiplier enforcing $\nabla\cdot\mathbf{v}=0$, determined by the Poisson equation obtained from the divergence of the momentum equation.

### E.5.4 — The second-law constraint

Decompose $\dot\varepsilon_{ij} = \dot\varepsilon'_{ij} + \tfrac13\dot\varepsilon_{kk}\delta_{ij}$ with $\dot\varepsilon'$ traceless. Then

$$\Phi = \tau_{ij}\dot\varepsilon_{ij} = 2\mu\,\dot\varepsilon_{ij}\dot\varepsilon_{ij} + \lambda(\dot\varepsilon_{kk})^2 = 2\mu\,\dot\varepsilon'_{ij}\dot\varepsilon'_{ij} + \left(\lambda + \tfrac23\mu\right)(\dot\varepsilon_{kk})^2$$

since $\dot\varepsilon_{ij}\dot\varepsilon_{ij} = \dot\varepsilon'_{ij}\dot\varepsilon'_{ij} + \tfrac13(\dot\varepsilon_{kk})^2$. The two terms are independent (one can choose pure shear or pure dilatation), so $\Phi\geq0$ for all motions iff $\mu\geq0$ and $\zeta_b = \lambda + \tfrac23\mu\geq0$. Stokes' hypothesis $\zeta_b = 0$ is the boundary case; its status is discussed in Ch. 15 §15.6.1.

---

## E.6 — Hagen–Poiseuille Flow and the Hydraulic Resistance

### E.6.1 — Assumptions

Incompressible Newtonian fluid with constant $\mu$; circular pipe of radius $R$ (diameter $D = 2R$), length $L$; rigid wall with no-slip; steady; **fully developed**, meaning $\mathbf{v} = v_z(r)\,\hat z$ with no radial or swirl component and no $z$-dependence; gravity absorbed into the modified pressure $P = p + \rho g\,h$ ($h$ the height), so that body forces drop out.

### E.6.2 — Exact reduction of Navier–Stokes

Continuity: $\nabla\cdot\mathbf{v} = \partial_zv_z = 0$ — satisfied identically. The convective term is $(\mathbf{v}\cdot\nabla)\mathbf{v} = v_z\,\partial_zv_z\,\hat z = 0$, so **the nonlinear term vanishes identically**, not approximately; this is why the solution is an exact solution of the full nonlinear equations. The radial and azimuthal momentum equations reduce to $\partial_rP = 0$ and $\partial_\theta P = 0$, so $P = P(z)$. The axial equation is

$$0 = -\frac{dP}{dz} + \mu\,\frac{1}{r}\frac{d}{dr}\left(r\frac{dv_z}{dr}\right)$$

The first term depends only on $z$, the second only on $r$; both must equal the same constant. Write $dP/dz = -G$ with $G = \Delta P/L > 0$ for flow in $+z$.

### E.6.3 — Solution

Integrate once: $r\,dv_z/dr = -Gr^2/(2\mu) + c_1$. Regularity at $r=0$ (finite shear) forces $c_1 = 0$. Integrate again and impose $v_z(R) = 0$:

$$v_z(r) = \frac{G}{4\mu}\left(R^2 - r^2\right)$$

The volume flow rate is

$$Q = \int_0^R v_z(r)\,2\pi r\,dr = \frac{2\pi G}{4\mu}\left[\frac{R^4}{2} - \frac{R^4}{4}\right] = \frac{\pi G R^4}{8\mu}$$

so

$$\Delta P = \frac{8\mu L}{\pi R^4}\,Q, \qquad R_{hyd} = \frac{\Delta P}{Q} = \frac{8\mu L}{\pi R^4} = \frac{128\,\mu L}{\pi D^4}$$

using $R^4 = D^4/16$. The units check: $[\mu L/D^4] = \text{Pa·s·m/m}^4 = \text{Pa·s/m}^3$, i.e. pressure per volume flow rate.

**Consistency checks.** The mean velocity is $U = Q/\pi R^2 = GR^2/(8\mu)$ and the centreline velocity is $2U$. The wall shear stress is $\tau_w = \mu|dv_z/dr|_{r=R} = GR/2$; a force balance on the fluid cylinder, $\Delta P\,\pi R^2 = \tau_w\,2\pi RL$, gives the same value independently. Writing $\Delta P = f_D(L/D)\tfrac12\rho U^2$ with $G = 32\mu U/D^2$ gives the Darcy friction factor $f_D = 64/Re_D$, $Re_D = \rho UD/\mu$.

> **[DERIVATION]** Under E.6.1, $R_{hyd} = 128\mu L/(\pi D^4)$ is an exact consequence of Navier–Stokes. The constitutive input is the Newtonian law; the "R" element of the hydraulic network (Ch. 17 §17.3.1, Ch. 19 §19.7.1) is this number.

> **[STRUCTURAL CONNECTION]** $R_{hyd}$ and the electrical $R = L/(\sigma A)$ share the structure "length over (transport coefficient × geometric factor)", because both are integrals of a linear flux–force law over a cross-section. The geometric factors differ ($D^4$ versus $D^2$) because the viscous flux is a momentum flux whose profile is set by a no-slip boundary condition, whereas the conduction current in a uniform wire is uniform. Same template, different physics.

### E.6.4 — Where it fails

| Assumption | Small parameter / condition | What happens when it fails |
|---|---|---|
| Laminar | $Re_D \lesssim 2300$ (empirical, `[PHENOMENOLOGICAL]`) | Transition to turbulence; $\Delta P$ becomes roughly $\propto Q^{1.75}$–$Q^2$ (Darcy–Weisbach, Ch. 19 §19.7.2). Hagen–Poiseuille flow is linearly stable at every $Re$ investigated (no proof for all $Re$ is known); transition is triggered by finite-amplitude disturbances, which is why $Re_c$ depends on inlet quality |
| Fully developed | $L \gg L_e$, with $L_e \approx 0.06\,Re_D\,D$ for laminar flow (widely used correlation, `[PHENOMENOLOGICAL]`) | Developing profile; extra entrance pressure drop |
| Steady | Womersley number $Wo = R\sqrt{\omega/\nu} \ll 1$ | Pulsatile flow; the profile lags the pressure; effective resistance and an inertance $\rho L/(\pi R^2)$ both matter |
| Incompressible, rigid wall | $L\omega/c\ll1$ | Pressure waves; the pipe becomes a hydraulic transmission line |
| No-slip | $Kn = \ell_{mfp}/D \ll 1$ | Slip flow in microchannels and rarefied gases |
| Newtonian | constant $\mu$ | Shear-thinning fluids give a blunter profile and a different $D$-scaling |

---

## E.7 — The Heat Equation

### E.7.1 — Assumptions

A solid at rest ($\mathbf{v} = 0$) or a fluid in which convection is ignored; constant density; caloric equation of state $de = c\,dT$ with constant specific heat $c$ (for solids and liquids $c_p\approx c_v$ to within a few percent, which is why the book writes $\rho c_p$); Fourier's law $\mathbf{q} = -\kappa\nabla T$.

### E.7.2 — Derivation

With $\mathbf{v} = 0$, $\dot\varepsilon_{ij} = 0$ and the internal-energy equation of E.4.3 becomes $\rho\,\partial_te = -\nabla\cdot\mathbf{q} + \dot Q_{vol}$. Substituting the caloric relation and Fourier's law,

$$\rho c\,\frac{\partial T}{\partial t} = \nabla\cdot(\kappa\nabla T) + \dot Q_{vol} \quad\xrightarrow{\ \kappa\ \text{uniform}\ }\quad \frac{\partial T}{\partial t} = \alpha\nabla^2T + \frac{\dot Q_{vol}}{\rho c}, \qquad \alpha = \frac{\kappa}{\rho c}$$

> **[DERIVATION]** Energy balance + caloric equation of state + Fourier closure → heat equation. Only the first is a conservation law.

> **[PHENOMENOLOGICAL]** Fourier's law is a constitutive, linear-response relation (Ch. 13 §13.5). It fails for ballistic phonon transport ($Kn_{phonon} = \ell_{ph}/L \not\ll 1$), at times shorter than the heat-flux relaxation time (where a hyperbolic Cattaneo-type closure is sometimes used), and in anisotropic media, where $\kappa$ becomes a tensor.

For a moving fluid the same steps give $\rho c_p\,DT/Dt = \nabla\cdot(\kappa\nabla T) + \Phi + \dot Q_{vol}$ (plus a pressure-work term $\beta T\,Dp/Dt$ for compressible flow), which is the starting point of convective heat transfer.

### E.7.3 — The convective boundary condition

At a solid surface exposed to a fluid at $T_\infty$, the heat flux leaving the solid is written

$$-\kappa\,\frac{\partial T}{\partial n}\bigg|_{surface} = h\left(T_s - T_\infty\right)$$

> **[PHENOMENOLOGICAL]** Newton's law of cooling with a heat-transfer coefficient $h$ is not derived here: $h$ comes from a solution of the fluid's own energy and momentum equations or, in practice, from correlations (Ch. 19 §19.6.2). The solid's heat equation and this Robin condition together are the problem whose lumped limit is E.8.

---

## E.8 — Lumped Capacitance and the Biot Criterion

### E.8.1 — The exact integral balance

Integrate the heat equation (no source) over the body volume $V$, with surface $A$, and use the Robin condition with uniform $h$:

$$\rho cV\,\frac{d\bar T}{dt} = -\oint_A\mathbf{q}\cdot\hat n\,dA = -hA\left(\bar T_s - T_\infty\right)$$

where $\bar T$ is the volume average and $\bar T_s$ the surface average of $T$. **This is exact.** The lumped-capacitance model makes one replacement:

> **[APPROXIMATION]** $\bar T_s \approx \bar T$. Then $\rho cV\,d\bar T/dt = -hA(\bar T - T_\infty)$, with solution $\bar T - T_\infty = (T_0 - T_\infty)\,e^{-t/\tau}$ and
> $$\tau = \frac{\rho cV}{hA} = R_{conv}\,C_{th}, \qquad R_{conv} = \frac{1}{hA}, \qquad C_{th} = \rho cV$$
> **Small parameter:** the Biot number $Bi = hL_c/\kappa$ with $L_c = V/A$. **Regime:** $Bi \ll 1$, conventionally $Bi < 0.1$.

The rest of this section shows that the error of this replacement is $O(Bi)$ and computes the coefficient.

### E.8.2 — Why $Bi$ is the right parameter: scaling

Inside the body heat flows by conduction across a distance $\sim L_c$, a resistance $\sim L_c/(\kappa A)$; at the surface it leaves by convection, a resistance $1/(hA)$. The ratio is $Bi = hL_c/\kappa$. The surface flux $hA(T_s - T_\infty)$ must be carried through the interior by a gradient $\sim(T_{centre} - T_s)/L_c$, so

$$\frac{T_{centre} - T_s}{T_s - T_\infty} \sim \frac{hL_c}{\kappa} = Bi$$

Small $Bi$ means the internal temperature differences are small compared with the temperature drop across the boundary layer, which is precisely the replacement $\bar T_s\approx\bar T$. The exact slab problem below confirms the scaling and fixes the coefficients.

### E.8.3 — Exact solution for a slab

Take a slab of half-thickness $L$ (so $L_c = V/A = L$), insulated by symmetry at its mid-plane and exposed to convection on both faces, initially at uniform $T_0$. Define $\theta = (T - T_\infty)/(T_0 - T_\infty)$, $\xi = x/L$, and the Fourier number $Fo = \alpha t/L^2$. The problem is

$$\frac{\partial\theta}{\partial Fo} = \frac{\partial^2\theta}{\partial\xi^2}, \qquad \frac{\partial\theta}{\partial\xi}\bigg|_{\xi=0} = 0, \qquad \frac{\partial\theta}{\partial\xi}\bigg|_{\xi=1} = -Bi\,\theta(1,Fo), \qquad \theta(\xi,0) = 1$$

Separation of variables (Ch. 16 §16.5) gives

$$\theta(\xi,Fo) = \sum_{n=1}^\infty C_n\cos(\lambda_n\xi)\,e^{-\lambda_n^2Fo}, \qquad \lambda_n\tan\lambda_n = Bi, \qquad C_n = \frac{4\sin\lambda_n}{2\lambda_n + \sin2\lambda_n}$$

where the eigenvalue condition is the Robin condition applied to $\cos\lambda\xi$, and $C_n$ follows from orthogonality of $\{\cos\lambda_n\xi\}$ on $[0,1]$ (a Sturm–Liouville system, Ch. 16 §16.5.2). This classical solution is in H. S. Carslaw and J. C. Jaeger, *Conduction of Heat in Solids*, 2nd ed., Oxford 1959, Ch. III.

### E.8.4 — Asymptotics as $Bi\to0$

**Fundamental mode.** For small $\lambda$, $\tan\lambda = \lambda + \lambda^3/3 + O(\lambda^5)$, so $\lambda^2 + \lambda^4/3 + O(\lambda^6) = Bi$. Inverting,

$$\lambda_1^2 = Bi - \frac{Bi^2}{3} + O(Bi^3)$$

The lumped model predicts the decay rate $t/\tau$ with $\tau = \rho cL/h$, i.e. in dimensionless form $t/\tau = hL\,t/(\rho cL^2) = Bi\cdot Fo$: a decay exponent $Bi$ in place of the exact $\lambda_1^2$. Therefore

$$\frac{\tau_{exact}}{\tau_{lump}} = \frac{Bi}{\lambda_1^2} = 1 + \frac{Bi}{3} + O(Bi^2)$$

**Amplitude.** With $\sin\lambda = \lambda - \lambda^3/6 + \ldots$ and $\sin2\lambda = 2\lambda - \tfrac43\lambda^3 + \ldots$,

$$C_1 = \frac{4\lambda_1(1 - \lambda_1^2/6)}{4\lambda_1(1 - \lambda_1^2/3)} + O(\lambda_1^4) = 1 + \frac{Bi}{6} + O(Bi^2)$$

**Internal non-uniformity.** In the fundamental mode $\theta(1)/\theta(0) = \cos\lambda_1 = 1 - Bi/2 + O(Bi^2)$: the surface–centre temperature difference is $Bi/2$ of the local excess temperature, in agreement with the scaling of E.8.2.

**Higher modes.** For $n\geq2$ write $m = n-1$; then $\lambda_n = m\pi + \delta_m$ with $\tan\lambda_n = \tan\delta_m\approx\delta_m$, so the eigenvalue condition gives $m\pi\,\delta_m\approx Bi$, i.e. $\delta_m\approx Bi/(m\pi)$ to leading order. Hence $\sin\lambda_n\approx(-1)^m\delta_m$, $\sin2\lambda_n\approx2\delta_m$, and

$$C_n \approx \frac{2(-1)^m\,Bi}{m^2\pi^2}, \qquad \sum_{n\geq2}|C_n| \approx \frac{2Bi}{\pi^2}\sum_{m\geq1}\frac{1}{m^2} = \frac{Bi}{3}$$

As a check, $\theta(0,0) = 1$ requires $C_1 + \sum_{n\geq2}C_n = 1$; the alternating sum is $\tfrac{2Bi}{\pi^2}\left(-\tfrac{\pi^2}{12}\right) = -\tfrac{Bi}{6}$, which exactly cancels the $+Bi/6$ in $C_1$. The higher modes decay at rates $\lambda_n^2\geq\pi^2$ in units of $\alpha/L^2$ — the diffusion time — and so are gone once $Fo\gtrsim0.5$.

### E.8.5 — The error bound

Combining, for all $\xi\in[0,1]$ and $Fo\geq0$, to leading order in $Bi$:

$$\theta(\xi,Fo) = e^{-Bi\,Fo}\left[1 + Bi\left(\frac16 - \frac{\xi^2}{2}\right) + \frac{Bi^2\,Fo}{3} + O(Bi^2)\right] + R(\xi,Fo), \qquad |R| \leq \frac{Bi}{3}\,e^{-\pi^2Fo}\,(1 + O(Bi))$$

Three statements follow.

1. **Uniform $O(Bi)$ accuracy on the relevant timescale.** For $t\lesssim$ a few $\tau$ (i.e. $Bi\,Fo = O(1)$), the term $Bi^2Fo/3 = (Bi/3)(Bi\,Fo)$ is $O(Bi)$, so the lumped solution is accurate to relative error $O(Bi)$ everywhere in the body.
2. **Time-constant error.** The lumped $\tau$ is too short by the factor $1/(1 + Bi/3)$: about 3.4\% at $Bi = 0.1$ (the exact root gives $\lambda_1^2 = 0.09675$, so $Bi/\lambda_1^2 = 1.034$).
3. **Long-time relative error grows.** For $t\gg\tau$ the relative error grows linearly as $(Bi/3)(t/\tau)$, although the absolute error is exponentially small. A lumped model used to predict *when* a body reaches $1\%$ of its initial excess ($t\approx4.6\,\tau$) carries a timing error of about $1.5\,Bi$ — small, but larger than $Bi/3$.

The numbers depend on shape. For a sphere of radius $R_s$ ($L_c = R_s/3$, $Bi_{R} = hR_s/\kappa = 3Bi$), the eigenvalue condition is $1 - \lambda\cot\lambda = Bi_R$, giving $\lambda_1^2 = 3Bi_R(1 - Bi_R/5 + \ldots)$; the decay-rate error is then $3Bi/5$ (6\% at $Bi = 0.1$) and the surface/centre ratio $\sin\lambda_1/\lambda_1\approx1 - \tfrac32Bi$ (about 14\% difference at $Bi = 0.1$). The criterion $Bi<0.1$ is therefore a convention guaranteeing errors of a few to roughly fifteen percent, not a sharp threshold.

> **[APPROXIMATION]** Proved: for $Bi\to0$ the exact conduction solution approaches the lumped exponential with $\tau = \rho cV/(hA)$, with relative error $O(Bi)$ for $t = O(\tau)$; the coefficient is $Bi/3$ in the time constant for a slab and $3Bi/5$ for a sphere.

### E.8.6 — Where it fails

The lumped model fails (a) when $Bi\gtrsim0.1$; (b) when $h$ is non-uniform over the surface, since then even the exact balance of E.8.1 involves a weighted surface average; (c) when the forcing ($T_\infty(t)$ or a surface flux) varies on timescales shorter than the diffusion time $L_c^2/\alpha$, because then the higher modes are continually re-excited — this is the time-window caveat of Ch. 16 §16.10.1, and it is independent of $Bi$; (d) with radiation, unless $h_{rad}\approx4\epsilon\sigma T_m^3$ is linearised about a mean temperature (Ch. 19 §19.6.1) and included in $Bi$; (e) with internal generation that is non-uniform.

**Model Ledger — conduction with a convective boundary to lumped thermal RC**

| Field | Content |
|---|---|
| Parent theory | Heat equation with Robin boundary condition (§E.7; Ch. 16 §16.2) |
| Reduction | Integrate over the body (exact); replace surface-average by volume-average temperature |
| Model | $\rho cV\,d\bar T/dt = -hA(\bar T - T_\infty)$, $\tau = \rho cV/(hA)$ |
| Assumptions | uniform $h$; constant $\kappa$, $\rho c$; no internal source; Fourier conduction; Newton cooling |
| Physics retained | total stored energy and the surface heat-loss rate |
| Physics neglected | internal gradients (fractional size $\approx Bi/2$ for a slab); higher spatial modes (total amplitude $\approx Bi/3$) |
| Validity | $Bi = hL_c/\kappa \ll 1$, and forcing slow compared with $L_c^2/\alpha$ |
| Fails when | $Bi\gtrsim0.1$; rapid surface forcing; non-uniform $h$; strong radiation without linearisation |
| Next model | one-term (Heisler) eigenfunction solution; full heat equation; finite-volume thermal network (Ch. 16 §16.11.3) |

---

## E.9 — Maxwell's Equations to the Telegrapher's Equations

### E.9.1 — Assumptions

A uniform two-conductor line along $z$ (coaxial cable, twin lead, stripline), cross-section independent of $z$, embedded in a linear, isotropic, homogeneous dielectric with permittivity $\epsilon$ and permeability $\mu$. Begin with perfect conductors and a lossless dielectric; losses are added in E.9.4. The mode of interest is **TEM**: $E_z = 0$, $B_z = 0$.

### E.9.2 — The transverse problem is electrostatic and magnetostatic

Write $\nabla = \nabla_t + \hat z\,\partial_z$. The $z$-component of Faraday's law reads $(\nabla_t\times\mathbf{E}_t)\cdot\hat z = -\partial_tB_z = 0$. So in each transverse plane $\mathbf{E}_t$ is curl-free and $\mathbf{E}_t = -\nabla_t\phi(x,y;z,t)$. Gauss's law in the charge-free dielectric, with $E_z = 0$, gives $\nabla_t\cdot\mathbf{E}_t = 0$, so $\nabla_t^2\phi = 0$: in every plane, $\phi$ solves the two-dimensional electrostatic problem, with each perfect conductor an equipotential (tangential $\mathbf{E}$ vanishes there). Define the line voltage

$$V(z,t) = \phi_1 - \phi_2 = \int_1^2\mathbf{E}_t\cdot d\mathbf{l}$$

along any path in the transverse plane from conductor 1 to conductor 2; path-independence follows from $\nabla_t\times\mathbf{E}_t = 0$. Similarly, the $z$-component of the Ampère–Maxwell law in the dielectric gives $\nabla_t\times\mathbf{H}_t = 0$ there, so the line current $I(z,t) = \oint\mathbf{H}_t\cdot d\mathbf{l}$ around conductor 1 is independent of the loop chosen. Because both transverse problems are linear and depend only on the cross-section geometry, the charge per unit length is $q' = C'V$ and the magnetic flux per unit length passing between the conductors is $\Phi' = L'I$, with $C'$ and $L'$ fixed by geometry and material.

### E.9.3 — The two line equations

**Faraday.** Take a rectangular contour in a plane containing the $z$ axis: from conductor 1 to conductor 2 at $z$, along conductor 2 to $z + \Delta z$, back to conductor 1, and along conductor 1 to $z$. The segments along perfect conductors contribute nothing ($E_{tan} = 0$). Faraday's law gives

$$V(z+\Delta z) - V(z) = -\frac{\partial}{\partial t}\left(\Phi'\Delta z\right) \quad\Longrightarrow\quad \frac{\partial V}{\partial z} = -L'\frac{\partial I}{\partial t}$$

(the sign of the flux being fixed by the contour orientation; with $V$ and $I$ defined as above and power flowing in $+z$ for $V,I>0$, this is the standard sign).

**Charge conservation.** The continuity equation integrated over the surface of conductor 1 between $z$ and $z+\Delta z$ gives $I(z) - I(z+\Delta z) = \partial_t(q'\Delta z)$, so

$$\frac{\partial I}{\partial z} = -C'\frac{\partial V}{\partial t}$$

For the exact TEM mode in a homogeneous medium, $L'C' = \mu\epsilon$, so the phase speed $1/\sqrt{L'C'}$ equals the plane-wave speed in the dielectric (D. M. Pozar, *Microwave Engineering*, 4th ed., Wiley 2012, Ch. 2–3).

### E.9.4 — Losses and the quasi-TEM approximation

With finite conductivity, current in the conductors requires a small axial field $E_z$ at their surfaces, and the mode is no longer exactly TEM. Treating $E_z$ perturbatively, the contour of E.9.3 picks up a series term $R'I\,\Delta z$, where $R'$ is the conductor resistance per unit length (frequency-dependent through the skin effect). A slightly conducting dielectric carries a transverse conduction current $G'V$ per unit length. The result is the **telegrapher's equations** of Ch. 16 §16.3.2 and Example 03:

$$\frac{\partial V}{\partial z} = -R'I - L'\frac{\partial I}{\partial t}, \qquad \frac{\partial I}{\partial z} = -G'V - C'\frac{\partial V}{\partial t}$$

> **[APPROXIMATION]** Quasi-TEM. **Small parameters:** $|E_z|/|E_t|$, which is of order $R'/(\omega L')$ for conductor loss; for an inhomogeneous dielectric (microstrip, with field partly in air) the dispersion correction scales with $(d/\lambda)^2$, $d$ the transverse dimension. **Fails when:** $d\gtrsim\lambda/2$ (higher-order waveguide modes propagate, Ch. 12), when losses are so large that $R'\sim\omega L'$ and the field is far from TEM, or near discontinuities, where evanescent higher-order modes are excited locally.

### E.9.5 — The lumped limit $\ell\ll\lambda$

For a section of length $\ell$, integrate the telegrapher's equations over $z\in[0,\ell]$. Exactly,

$$V(0) - V(\ell) = R'\ell\,\langle I\rangle + L'\ell\,\frac{d\langle I\rangle}{dt}, \qquad I(0) - I(\ell) = G'\ell\,\langle V\rangle + C'\ell\,\frac{d\langle V\rangle}{dt}$$

with $\langle\cdot\rangle$ the average over the section. The approximation is to replace $\langle I\rangle$ and $\langle V\rangle$ by terminal values. To quantify it, use the exact phasor solution. With $Z' = R' + j\omega L'$, $Y' = G' + j\omega C'$, $\gamma = \sqrt{Z'Y'}$, and $Z_0 = \sqrt{Z'/Y'}$, the section is the two-port

$$\begin{pmatrix}V(0)\\ I(0)\end{pmatrix} = \begin{pmatrix}\cosh\gamma\ell & Z_0\sinh\gamma\ell\\ Z_0^{-1}\sinh\gamma\ell & \cosh\gamma\ell\end{pmatrix}\begin{pmatrix}V(\ell)\\ I(\ell)\end{pmatrix}$$

Let $Z = Z'\ell$ and $Y = Y'\ell$, so that $(\gamma\ell)^2 = ZY$. Expanding for $|\gamma\ell|\ll1$:

$$\cosh\gamma\ell = 1 + \frac{ZY}{2} + O\big((\gamma\ell)^4\big), \qquad Z_0\sinh\gamma\ell = Z\left(1 + \frac{ZY}{6} + \ldots\right), \qquad \frac{\sinh\gamma\ell}{Z_0} = Y\left(1 + \frac{ZY}{6} + \ldots\right)$$

The symmetric $\pi$-section (shunt $Y/2$, series $Z$, shunt $Y/2$) has transmission matrix with diagonal entries $1 + ZY/2$, off-diagonal entries $Z$ and $Y(1 + ZY/4)$ — agreeing with the exact line to relative error $O(ZY) = O((\gamma\ell)^2)$. For a low-loss line $|\gamma\ell|\approx\omega\ell\sqrt{L'C'} = 2\pi\ell/\lambda$.

> **[APPROXIMATION]** Lumping a line section into $L = L'\ell$, $C = C'\ell$, $R = R'\ell$, $G = G'\ell$. **Small parameter:** $\ell/\lambda$; error $O((2\pi\ell/\lambda)^2)$ per section. **Fails when:** $\ell\gtrsim\lambda/10$, the conventional engineering threshold: there $(\gamma\ell)^2\approx0.39$ and the $\pi$-section's off-diagonal entries err by about 3–7\%; for a digital edge with rise time $t_r$, when the one-way delay $\ell/v$ is not small compared with $t_r$. A ladder of $N$ sections converges to the line as $N\to\infty$ at fixed total length; that convergence, read backwards, is the descent from line to lumped circuit in Ch. 16 §16.10.2.

---

## E.10 — Kirchhoff's Voltage Law from Faraday's Law by Lumping

### E.10.1 — The lumping hypotheses

This section proves KVL as a consequence of Faraday's law plus explicit assumptions, and shows where the $d\Phi_B/dt$ term goes. It does **not** go to zero; it is relocated into the inductor branch voltages. The hypotheses are:

1. **Element boxes.** The circuit is a set of elements, each enclosed in a closed surface (its "box"), joined by wires outside the boxes. Each element has two terminals on its box surface.
2. **Flux confinement.** Outside the boxes, $\partial\mathbf{B}/\partial t = 0$ in the region swept by the circuit and its spanning surfaces. All time-varying magnetic flux lives inside inductor (and transformer) boxes.
3. **Charge confinement.** Outside the boxes, $\partial\rho/\partial t = 0$; time-varying charge lives on capacitor plates inside capacitor boxes. (Needed for KCL, E.10.4.)
4. **Ideal wires.** The wires outside the boxes are perfect conductors, so $\mathbf{E}\cdot d\mathbf{l} = 0$ along them (or have resistance assigned to a resistor box).
5. **Quasi-statics.** Circuit dimension $\ell\ll\lambda$, so that retardation across the circuit is negligible and radiation is negligible (E.10.5).

### E.10.2 — Branch voltages are well defined

In the exterior region of hypothesis 2, $\nabla\times\mathbf{E} = 0$, so locally $\mathbf{E} = -\nabla\phi$. Define the branch voltage of element $k$ with terminals $a_k$, $b_k$ as

$$v_k = \int_{a_k}^{b_k}\mathbf{E}\cdot d\mathbf{l} = \phi(a_k) - \phi(b_k) \qquad\text{(path just outside the box)}$$

The integral is path-independent provided paths are deformable into one another within the exterior without crossing time-varying flux — which hypothesis 2 guarantees for paths that stay outside every box. This is exactly what a voltmeter with short leads routed away from the inductor measures; a voltmeter whose leads loop around a transformer core measures something else, and that is not a paradox but a violation of hypothesis 2.

### E.10.3 — The loop law and the inductor's voltage

**Loop law.** Take any loop of the circuit graph. Construct a closed contour $\mathcal{C}$ that runs along the wires and, at each element, crosses from terminal to terminal along the exterior path used to define $v_k$. Choose a spanning surface for $\mathcal{C}$ lying entirely in the exterior — possible because each box is crossed only on its outside. Faraday's law on $\mathcal{C}$:

$$\oint_\mathcal{C}\mathbf{E}\cdot d\mathbf{l} = -\frac{d}{dt}\int_S\mathbf{B}\cdot d\mathbf{S} = 0$$

by hypothesis 2. The wire segments contribute zero (hypothesis 4) and each element contributes $\pm v_k$ according to orientation. Hence

$$\sum_{k\in\text{loop}}\pm v_k = 0$$

**Inductor branch relation.** Now apply Faraday's law to a *different* contour: the one that runs from $a$ to $b$ **through the winding** of an inductor and returns from $b$ to $a$ through the exterior. Its spanning surface is pierced by the inductor's flux; the flux linkage through it is $\lambda = Li$ for a linear inductor, with $i$ the winding current from $a$ to $b$ and orientations related by the right-hand rule. Inside a winding of resistance $R_w$, $\mathbf{E} = \mathbf{J}/\sigma$, so $\int_{winding}\mathbf{E}\cdot d\mathbf{l} = R_wi$. Faraday's law gives

$$R_w\,i + \int_b^a\mathbf{E}\cdot d\mathbf{l}\bigg|_{ext} = -\frac{d\lambda}{dt} \quad\Longrightarrow\quad R_w\,i - v_{ab} = -L\frac{di}{dt} \quad\Longrightarrow\quad v_{ab} = R_w\,i + L\frac{di}{dt}$$

This is where the $-d\Phi_B/dt$ went: the flux of the circuit lives inside the inductor, and Faraday's law applied to the contour *through* the inductor produces its branch relation. For coupled coils, $\lambda_j = \sum_kM_{jk}i_k$ and $v_j = \sum_kM_{jk}\,di_k/dt$.

> **[DERIVATION]** Under hypotheses 1–4, KVL in the form $\sum\pm v_k = 0$, with inductor branch voltages $v = L\,di/dt$ (plus winding resistance), follows from Faraday's law. KVL is not "Faraday's law with $d\Phi/dt$ dropped": the flux term is kept and assigned to the elements that hold the flux. This supersedes the phrasing in Ch. 11 §11.12.2 and Ch. 17 §17.4.2 where the two might be read as equivalent.

> **[APPROXIMATION]** The lumping hypotheses. **Small parameters:** stray flux through the circuit loop compared with the inductors' flux, $\Phi_{stray}/(Li)$; and $\ell/\lambda$. **Fails when:** loop areas are large or fast edges couple stray flux (the "parasitic inductance" of a layout is precisely a violation of hypothesis 2 that is then repaired by adding an inductor box); when $\ell/\lambda$ is not small (E.9).

### E.10.4 — KCL by the same method

Enclose a node by a closed surface lying in the exterior. Charge conservation gives $\oint\mathbf{J}\cdot\hat n\,dA = -dQ_{enc}/dt = 0$ by hypothesis 3, and $\mathbf{J}$ crosses the surface only in the wires, so $\sum i_k = 0$. For a capacitor, enclosing one plate gives $i = dq/dt$ with $q = Cv$ from the electrostatics of the box. Note that the total current $\mathbf{J} + \partial_t\mathbf{D}$ is always solenoidal; KCL for conduction currents alone is the statement that displacement current outside capacitor boxes is negligible — the electric counterpart of hypothesis 2.

### E.10.5 — Radiation and retardation

Hypotheses 2 and 3 cannot hold exactly for a time-varying circuit, since a changing current always produces some changing field outside the boxes. The leading corrections are (i) retardation, of relative size $\omega\ell/c = 2\pi\ell/\lambda$, and (ii) radiation, which for an electrically small loop appears as a radiation resistance scaling as $(\ell/\lambda)^4$ (C. A. Balanis, *Antenna Theory*, 4th ed., Wiley 2016, Ch. 5). Both vanish as $\ell/\lambda\to0$, which is the content of the criterion of Ch. 11 §11.12.1.

---

## E.11 — Poynting's Theorem and Lumped Port Power

### E.11.1 — Assumptions

Macroscopic Maxwell equations $\nabla\times\mathbf{E} = -\partial_t\mathbf{B}$, $\nabla\times\mathbf{H} = \mathbf{J} + \partial_t\mathbf{D}$; media linear, non-dispersive, and time-invariant, $\mathbf{D} = \epsilon\mathbf{E}$, $\mathbf{B} = \mu\mathbf{H}$, with $\epsilon$, $\mu$ symmetric tensors constant in time.

### E.11.2 — Proof

The vector identity $\nabla\cdot(\mathbf{E}\times\mathbf{H}) = \mathbf{H}\cdot(\nabla\times\mathbf{E}) - \mathbf{E}\cdot(\nabla\times\mathbf{H})$ and the two curl equations give

$$\nabla\cdot(\mathbf{E}\times\mathbf{H}) = -\mathbf{H}\cdot\partial_t\mathbf{B} - \mathbf{E}\cdot\partial_t\mathbf{D} - \mathbf{J}\cdot\mathbf{E}$$

For symmetric, time-independent $\epsilon$: $\mathbf{E}\cdot\partial_t(\epsilon\mathbf{E}) = \partial_t(\tfrac12\mathbf{E}\cdot\epsilon\mathbf{E})$, and likewise for $\mu$. Hence

$$\frac{\partial u}{\partial t} + \nabla\cdot\mathbf{S} = -\mathbf{J}\cdot\mathbf{E}, \qquad u = \tfrac12\left(\mathbf{E}\cdot\mathbf{D} + \mathbf{B}\cdot\mathbf{H}\right), \qquad \mathbf{S} = \mathbf{E}\times\mathbf{H}$$

and in vacuum this is Ch. 11 §11.8.2. In integral form over a fixed volume $V$,

$$-\oint_{\partial V}\mathbf{S}\cdot\hat n\,dA = \frac{d}{dt}\int_Vu\,dV + \int_V\mathbf{J}\cdot\mathbf{E}\,dV$$

power flowing in equals the rate of increase of field energy plus the work done on charges (Joule heat $\sigma E^2$ for an ohmic conductor).

> **[DERIVATION]** Poynting's theorem is an identity following from the two curl equations; the identification of $u$ as an energy density uses the linear, non-dispersive constitutive relations. In dispersive or lossy-dielectric media the clean split fails and $u$ must be redefined (J. D. Jackson, *Classical Electrodynamics*, 3rd ed., Wiley 1999, Ch. 6).

### E.11.3 — Lumped port power $P = v\,i$

Enclose a two-terminal element in a surface $\Sigma$ lying in the exterior region of E.10, crossed only by its two leads. On $\Sigma$, $\mathbf{E} = -\nabla\phi$ (hypothesis 2), so

$$\mathbf{E}\times\mathbf{H} = -\nabla\phi\times\mathbf{H} = -\nabla\times(\phi\mathbf{H}) + \phi\,\nabla\times\mathbf{H}$$

The surface integral of a curl over a closed surface vanishes, so

$$-\oint_\Sigma\mathbf{S}\cdot\hat n\,dA = -\oint_\Sigma\phi\,(\mathbf{J} + \partial_t\mathbf{D})\cdot\hat n\,dA$$

Neglect the displacement current through $\Sigma$ (the hypothesis 3 counterpart). $\mathbf{J}$ crosses $\Sigma$ only within the two leads, at potentials $\phi_a$, $\phi_b$, carrying current $i$ inward at $a$ and outward at $b$. So

$$-\oint_\Sigma\mathbf{S}\cdot\hat n\,dA = \phi_a\,i - \phi_b\,i = v\,i$$

> **[DERIVATION]** Under the lumping hypotheses, the electromagnetic power delivered to an element through its box equals $v\,i$. This is the field-theoretic origin of the power-conjugate pairing of effort and flow (Ch. 17 §17.2) in the electrical domain. KVL itself is not an energy statement; Tellegen's theorem ($\sum v_ki_k = 0$ for any $v$ satisfying KVL and any $i$ satisfying KCL on the same graph) is the network form of energy balance, and it requires both laws.

---

## E.12 — The Euler–Bernoulli Beam from Three-Dimensional Elasticity

### E.12.1 — Assumptions

A straight prismatic beam along $x$, length $L$, cross-section $A$ with characteristic transverse size $h$, symmetric about the $x$–$y$ plane in which it bends. Linear isotropic elasticity with Young's modulus $E$ and shear modulus $G$ (Ch. 15 §15.9). The **slender-beam assumptions** are:

1. **Slenderness:** $h/L\ll1$ (equivalently $r_g/L\ll1$, $r_g = \sqrt{I/A}$ the radius of gyration);
2. **Small deflection:** $|w|/L\ll1$ and $|w'|\ll1$, so the problem is linear;
3. **Bernoulli–Kirchhoff kinematics:** plane cross-sections remain plane and normal to the deformed axis;
4. **Uniaxial stress:** $\sigma_{yy}$, $\sigma_{zz}\ll\sigma_{xx}$; lateral surfaces carry only the applied transverse load $q(x,t)$ per unit length.

### E.12.2 — Kinematics, stress, and moment

Assumption 3 gives the displacement field $u_x = -y\,w'(x)$, $u_y = w(x)$, so the only significant strain is

$$\varepsilon_{xx} = \partial_xu_x = -y\,w''$$

Assumption 4 with Hooke's law gives $\sigma_{xx} = E\varepsilon_{xx} = -Ey\,w''$ (uniaxial stress, hence $E$ and not the plane-strain modulus). Measuring $y$ from the centroid makes the axial force $\int_A\sigma_{xx}\,dA$ vanish. Define the bending moment and shear force

$$M(x) = -\int_Ay\,\sigma_{xx}\,dA = EI\,w'', \qquad V(x) = \int_A\sigma_{xy}\,dA, \qquad I = \int_Ay^2\,dA$$

and so $\sigma_{xx} = -My/I$, matching Ch. 20 §20.2.1.

### E.12.3 — Integrating Cauchy's equation over the cross-section

The beam equations are cross-sectional moments of Cauchy's equation (E.2.4). Statically and without body force, the $x$-component is $\partial_x\sigma_{xx} + \partial_y\sigma_{xy} + \partial_z\sigma_{xz} = 0$. Multiply by $y$ and integrate over $A$; the lateral surface is traction-free in $x$, so integrating by parts gives $\int_Ay(\partial_y\sigma_{xy} + \partial_z\sigma_{xz})\,dA = -\int_A\sigma_{xy}\,dA = -V$. Hence

$$-M' - V = 0 \quad\Longrightarrow\quad V = -M'$$

The $y$-component, $\partial_x\sigma_{yx} + \partial_y\sigma_{yy} + \partial_z\sigma_{yz} = 0$, integrated over $A$, gives $V' + q = 0$, since the boundary integral of $\sigma_{yy}n_y + \sigma_{yz}n_z$ around the cross-section's perimeter is the applied load per unit length. Combining, $M'' = q$ and

$$\left(EI\,w''\right)'' = q \quad\xrightarrow{\ EI\ \text{uniform}\ }\quad EI\,\frac{d^4w}{dx^4} = q$$

**Dynamics.** Restoring $\rho\,\partial_t^2u_y = \rho\ddot w$ in the $y$-equation adds $-\rho A\ddot w$ to the load, giving the bridge-zone equation of Ch. 16 §16.7.2 and Ch. 17 §17.10.1:

$$EI\,\frac{\partial^4w}{\partial x^4} + \rho A\,\frac{\partial^2w}{\partial t^2} = q(x,t)$$

The $x$-equation also acquires $\rho\,\partial_t^2u_x = -\rho y\,\ddot w'$, whose $y$-moment adds the **rotary inertia** term $-\rho I\,\ddot w''$ (the Rayleigh beam). Euler–Bernoulli drops it.

### E.12.4 — The internal inconsistency, and why it is harmless

Assumption 3 implies $\varepsilon_{xy} = 0$ and therefore $\sigma_{xy} = 0$ — yet the shear force $V$ is nonzero. The resolution is that Euler–Bernoulli is the leading order of an asymptotic expansion in $h/L$: the shear stress is $O(h/L)$ smaller than the bending stress, its *strain* contribution to the deflection is $O((h/L)^2)$ smaller, and its value is recovered *a posteriori* from equilibrium (the Jourawski/Zhuravskii formula $\sigma_{xy} = VQ_A/(Ib)$). The kinematic hypothesis is a statement about which strains are negligible, not a claim that the shear stress is zero.

> **[APPROXIMATION]** Three-dimensional elasticity → Euler–Bernoulli beam. **Small parameters:** $h/L$ (slenderness) and $|w|/L$ (linearity); in dynamics, $kr_g$ with $k$ the flexural wavenumber. Neglected: shear deformation (relative deflection error $O(E r_g^2/(\kappa_sGL^2))$), rotary inertia ($O((kr_g)^2)$), cross-section distortion (Poisson effects), and geometric nonlinearity. The status `[DERIVATION]` sometimes attached to the beam equation (Ch. 20 overview table) is accurate only for the reduction *given* these assumptions.

### E.12.5 — What Timoshenko adds

Timoshenko (S. P. Timoshenko, *Philosophical Magazine* 41, 744–746, 1921) relaxes assumption 3: cross-sections remain plane but rotate by an independent angle $\varphi(x,t)$, so the shear strain $\gamma = w' - \varphi$ is retained, and rotary inertia is kept. With a shear coefficient $\kappa_s$ correcting for the non-uniform shear distribution ($\kappa_s = 5/6$ is the usual value for a rectangle),

$$\rho A\,\ddot w = \kappa_sGA\,(w'' - \varphi') + q, \qquad \rho I\,\ddot\varphi = EI\,\varphi'' + \kappa_sGA\,(w' - \varphi)$$

Two consequences show the size of the correction. *Statics:* a cantilever with tip load $P$ deflects by $PL^3/(3EI) + PL/(\kappa_sGA)$; the ratio of shear to bending terms is $3EI/(\kappa_sGAL^2) = 3(E/\kappa_sG)(r_g/L)^2$, which is $O((h/L)^2)$ and becomes significant for $L/h\lesssim10$ or for sandwich and composite beams with small $G/E$. *Dynamics:* Euler–Bernoulli's dispersion relation $\omega^2 = (EI/\rho A)k^4$ (Ch. 16 §16.7.2) gives a phase velocity growing without bound as $\sqrt\omega$; Timoshenko's has two branches whose high-$k$ speeds approach the finite values $\sqrt{E/\rho}$ and $\sqrt{\kappa_sG/\rho}$, so it corrects the unphysical infinite signal speed. The Timoshenko model is in turn an approximation to three-dimensional elastodynamics, accurate up to wavelengths comparable to $h$ (K. F. Graff, *Wave Motion in Elastic Solids*, Ohio State University Press 1975, reprinted Dover).

---

## E.13 — The Buckingham $\pi$ Theorem

### E.13.1 — Statement

Let a physical relation $f(q_1,\ldots,q_n) = 0$ connect $n$ positive dimensional quantities. Let there be $k$ base dimensions (M, L, T, Θ, …), and let the **dimension matrix** $\mathsf{D}$ be the $k\times n$ matrix whose column $i$ lists the exponents of the base dimensions in $q_i$. Let $r = \mathrm{rank}\,\mathsf{D}$. Assume:

1. **Completeness:** the list $q_1,\ldots,q_n$ contains every quantity on which the relation depends (including dimensional constants);
2. **Unit covariance:** the relation holds in every system of units obtained from one another by rescaling the base units.

Then the relation is equivalent to $F(\pi_1,\ldots,\pi_{n-r}) = 0$ among $n - r$ independent dimensionless products $\pi_j = \prod_iq_i^{a_{ij}}$.

### E.13.2 — Proof sketch

*Counting.* A product $\prod_iq_i^{a_i}$ is dimensionless iff its exponent vector $\mathbf{a}\in\mathbb{R}^n$ satisfies $\mathsf{D}\mathbf{a} = 0$. By the rank–nullity theorem, $\dim\ker\mathsf{D} = n - r$, so there are exactly $n - r$ independent dimensionless products; any other is a product of powers of these. (Because $\mathsf{D}$ has integer, in practice rational, entries, a basis of $\ker\mathsf{D}$ can be chosen with rational exponents.)

*Reduction.* Reorder so that $q_1,\ldots,q_r$ have linearly independent dimension columns (the "repeating variables"). For each $j > r$, column $j$ of $\mathsf{D}$ is a combination of the first $r$ columns, so there are exponents with $\pi_{j-r} = q_j\prod_{i\leq r}q_i^{-b_{ij}}$ dimensionless. Now rescale the base units by positive factors $\Lambda_1,\ldots,\Lambda_k$; the numerical value of $q_i$ changes by $\prod_m\Lambda_m^{\mathsf{D}_{mi}}$. Taking logarithms, the change of $(\ln q_1,\ldots,\ln q_r)$ is $\mathsf{D}_{rep}^{T}(\ln\Lambda_1,\ldots,\ln\Lambda_k)$, where $\mathsf{D}_{rep}$ is the $k\times r$ submatrix of rank $r$; its transpose maps $\mathbb{R}^k$ onto $\mathbb{R}^r$. So a unit system exists in which $q_1 = \cdots = q_r = 1$. In that system the $\pi$'s equal $q_{r+1},\ldots,q_n$ numerically (dimensionless products are unit-invariant). By unit covariance the relation holds there:

$$f(1,\ldots,1,\pi_1,\ldots,\pi_{n-r}) = 0 \equiv F(\pi_1,\ldots,\pi_{n-r})$$

and since the $\pi$'s are the same in every unit system, this relation holds in all of them. $\square$

A careful treatment, including the role of the completeness assumption and of intermediate asymptotics, is G. I. Barenblatt, *Scaling, Self-Similarity, and Intermediate Asymptotics*, Cambridge University Press 1996, Ch. 1; the original is E. Buckingham, *Physical Review* 4, 345–376 (1914).

> **[DERIVATION]** The $\pi$ theorem is a theorem of linear algebra plus unit covariance. Its physical content is entirely in assumption 1: a missing variable, or an irrelevant one included, produces a correct theorem about the wrong relation.

### E.13.3 — Example: pipe flow, and what the theorem does not give

Take $\Delta P$, $L$, $D$, $U$, $\rho$, $\mu$: $n = 6$, base dimensions M, L, T with $r = 3$, so $n - r = 3$ groups, e.g. $\Delta P/(\rho U^2)$, $L/D$, $Re_D = \rho UD/\mu$. The theorem gives $\Delta P/(\rho U^2) = \Psi(L/D, Re_D)$ — nothing more. The further statement that $\Delta P\propto L$ for a long pipe is a *physical* input (fully developed flow, E.6), giving $\Delta P/(\rho U^2) = (L/D)\,\tfrac12f_D(Re_D)$; and the function $f_D = 64/Re_D$ comes only from solving Navier–Stokes (E.6.3) or, for turbulent flow, from experiment. The same reasoning applied to the dimensionless Navier–Stokes equation is how $Re$ and $Fr$ emerge in Ch. 15 §15.8.1.

---

## E.14 — Summary

| Result | Statement | Assumptions | Used in |
|---|---|---|---|
| Reynolds transport theorem | $\frac{d}{dt}\int_{V_m}f\,dV = \int\partial_tf\,dV + \oint f\,\mathbf{v}\cdot\hat n\,dA$ | smooth invertible motion; $C^1$ field | Ch. 15 §15.4; Ch. 17 §17.1.1 |
| Local mass balance | $\partial_t\rho + \nabla\cdot(\rho\mathbf{v}) = 0$ | material mass constant; continuity of fields | Ch. 15 §15.4.1; Ch. 19 §19.7 |
| Cauchy's theorem | $t_i = \sigma_{ij}n_j$ | momentum postulate; contact forces as surface densities | Ch. 15 §15.3.1 |
| Cauchy's equation | $\rho\,Dv_i/Dt = \partial_j\sigma_{ij} + f_i$ | as above; any material | Ch. 15 §15.4.2 |
| Stress symmetry | $\sigma_{ij} = \sigma_{ji}$ | non-polar continuum (no body or couple stresses, no spin) | Ch. 15 §15.3.1 |
| Internal-energy equation | $\rho\,De/Dt = -p\nabla\cdot\mathbf{v} + \Phi - \nabla\cdot\mathbf{q} + \dot Q_{vol}$ | first law; stress symmetric | Ch. 15 §15.4.3 |
| Navier–Stokes | $\rho\,D\mathbf{v}/Dt = -\nabla p + \mu\nabla^2\mathbf{v} + (\mu+\lambda)\nabla(\nabla\cdot\mathbf{v}) + \mathbf{f}$ | Newtonian closure (constitutive); uniform $\mu$, $\lambda$ | Ch. 15 §15.6 |
| Second-law constraint | $\mu\geq0$, $\lambda + \tfrac23\mu\geq0$ | $\Phi\geq0$ for all motions | Ch. 15 §15.6.1 |
| Hagen–Poiseuille | $R_{hyd} = 128\mu L/(\pi D^4)$, $f_D = 64/Re_D$ | laminar, fully developed, steady, Newtonian, no-slip | Ch. 15 §15.7.1; Ch. 17 §17.3.1; Ch. 19 §19.7.1 |
| Heat equation | $\rho c\,\partial_tT = \nabla\cdot(\kappa\nabla T) + \dot Q_{vol}$ | energy balance + Fourier (constitutive) + $de = c\,dT$ | Ch. 16 §16.2.2; Ch. 19 §19.6 |
| Lumped capacitance | $\tau = \rho cV/(hA)$; $\tau_{exact}/\tau_{lump} = 1 + Bi/3 + O(Bi^2)$ (slab) | $Bi\ll1$; uniform $h$; slow forcing | Ch. 16 §16.10.1; Ch. 17 §17.1; Ch. 19 §19.6.2 |
| Telegrapher's equations | $\partial_zV = -R'I - L'\partial_tI$, $\partial_zI = -G'V - C'\partial_tV$ | uniform line; quasi-TEM; $d\ll\lambda$ | Ch. 16 §16.3.2; Ch. 17 §17.10 |
| Line → lumped section | $\pi$-section matches exact two-port to $O((\gamma\ell)^2)$ | $\ell\ll\lambda$ | Ch. 16 §16.10.2; Ch. 17 §17.10.2 |
| KVL with inductor branches | $\sum\pm v_k = 0$, $v_L = L\,di/dt$ | flux confined to element boxes; ideal wires; $\ell\ll\lambda$ | Ch. 11 §11.12.2; Ch. 17 §17.4.2; Ch. 18 §18.1.1 |
| KCL | $\sum i_k = 0$, $i_C = C\,dv/dt$ | charge confined to capacitor boxes | Ch. 11 §11.12.3; Ch. 17 §17.4.1 |
| Poynting's theorem | $\partial_tu + \nabla\cdot\mathbf{S} = -\mathbf{J}\cdot\mathbf{E}$ | linear, non-dispersive, time-invariant media | Ch. 11 §11.8.2 |
| Lumped port power | $-\oint\mathbf{S}\cdot\hat n\,dA = v\,i$ | lumping hypotheses on the box surface | Ch. 17 §17.2, §17.9 |
| Euler–Bernoulli beam | $EI\,w'''' + \rho A\,\ddot w = q$ | $h/L\ll1$; small deflection; plane sections normal; uniaxial stress | Ch. 16 §16.7.2; Ch. 17 §17.10; Ch. 20 §20.1.3, §20.2 |
| Timoshenko correction | shear deflection ratio $3(E/\kappa_sG)(r_g/L)^2$; finite high-$k$ wave speeds | plane sections, not normal; rotary inertia kept | Ch. 16 §16.7.2; Ch. 19 §19.10 |
| Buckingham $\pi$ | $n - r$ independent dimensionless groups | complete variable list; unit covariance | Ch. 15 §15.8.1; Ch. 19 §19.6.2; Ch. 20 §20.10.2 |

---

*End of Appendix E*
