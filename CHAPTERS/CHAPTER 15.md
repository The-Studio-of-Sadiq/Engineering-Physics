# Continuum Mechanics: Fluids and Solids

### Newton's Second Law Applied to $10^{23}$ Particles Simultaneously

---

> _The equations of fluid motion are Newton's second law for a fluid parcel._ _Everything else is bookkeeping._ — commonly attributed to G. I. Taylor

---

## 15.0 — Overview

Chapters 8–14 completed the five Bridge B paths, bringing all of classical physics into Layer 2. But Layer 2 still has two important members unwritten:

- **Continuum mechanics** (this chapter): the mechanics of deformable media — fluids and solids — treated as continuous fields rather than discrete particles
- **The unified PDE structure** (Ch. 16): showing that the wave equation and diffusion equation appear identically across all physical domains

This chapter derives the governing equations of fluid mechanics (Euler and Navier-Stokes) and solid mechanics (Navier's equation of linear elasticity) from first principles. The derivation has a single organizing strategy: **apply Newton's second law to a fluid or solid parcel** and use the stress tensor to represent internal forces. Every subsequent complication — viscosity, elasticity, compressibility, non-linearity — is a refinement of this one idea.

**Connections to previous chapters:**

|Concept|Origin|
|---|---|
|Continuum hypothesis|$N\to\infty$ limit of Ch. 10 (Bridge B.b), spatial averaging|
|Strain tensor $\varepsilon_{ij}$|Generalization of Ch. 9 spring extension to 3D|
|Viscous stress|Newton's viscosity from Ch. 13 §13.7 (Kubo)|
|Elastic stress|Hooke's law from Ch. 13 §13.8|
|Conservation laws|Noether's theorem (Ch. 1 §1.7): mass, momentum, energy|
|Elastic waves|Classical limit of phonons (Ch. 6 §6.7)|
|Turbulence|Where the PDE refuses to lump — Layer 3 has no exact model|

---

## 15.1 — The Continuum Hypothesis

### 15.1.1 — From Particles to Fields

The N→∞ statistical limit of Ch. 10 gave thermodynamic quantities as ensemble averages. Applied to a spatially inhomogeneous system, it gives **field variables** — quantities that vary continuously in space:

- **Density field:** $\rho(\mathbf{r}, t) = \langle\hat\rho\rangle$ — mass per unit volume
- **Velocity field:** $\mathbf{v}(\mathbf{r}, t) = \langle\hat{\mathbf{v}}\rangle$ — momentum per unit mass
- **Pressure field:** $p(\mathbf{r}, t)$ — isotropic stress
- **Temperature field:** $T(\mathbf{r}, t)$ — local thermodynamic temperature
- **Displacement field:** $\mathbf{u}(\mathbf{r}, t)$ — displacement from equilibrium (solids)

The averaging volume must be:

- Large enough to contain many molecules (thermodynamic limit valid)
- Small enough to resolve the spatial variation of interest

**Validity criterion — Knudsen number:** $$Kn = \frac{\ell_{mfp}}{L} \ll 1$$

where $\ell_{mfp}$ is the mean free path and $L$ is the characteristic length of the problem. Continuum mechanics is valid for $Kn < 0.01$.

|Medium|$\ell_{mfp}$|Continuum breaks at|
|---|---|---|
|Air at 1 atm, 300 K|68 nm|Micro/nano-channels $L < 7;\mu$m|
|Water at 300 K|$\sim 0.3$ nm|Near-molecular systems|
|Liquid metals|$\sim 0.1$ nm|Essentially always valid|
|Air at 30 km altitude|$\sim 1$ mm|Small aircraft structures|
|Re-entry vehicle wake|several cm|Kinetic theory needed|

### 15.1.2 — Eulerian vs. Lagrangian Description

**Lagrangian** (tracking particles): follow each fluid parcel as it moves. Natural for solid mechanics (track each material point).

**Eulerian** (fixed spatial grid): observe what passes through a fixed point. Natural for fluid mechanics (the flow field at fixed locations).

The connection is the **material derivative** (substantial derivative) — the rate of change of a quantity as seen by a parcel moving with the fluid:

$$\boxed{\frac{D}{Dt} = \frac{\partial}{\partial t} + \mathbf{v}\cdot\nabla}$$

- $\partial/\partial t$: local rate of change at fixed position (Eulerian)
- $\mathbf{v}\cdot\nabla$: change due to moving to a new location (advection)

**Example:** The temperature of a fluid parcel changes because (a) the temperature at that location changes with time, and (b) the parcel moves to a region of different temperature. Both contribute to $DT/Dt$.

The advection term $(\mathbf{v}\cdot\nabla)\mathbf{v}$ in Newton's law for a fluid parcel is what makes Navier-Stokes **nonlinear** — and what makes turbulence so difficult.

---

## 15.2 — Kinematics: Describing Deformation

### 15.2.1 — The Strain Tensor

When a solid body deforms, each point $\mathbf{r}$ moves to $\mathbf{r}+\mathbf{u}(\mathbf{r})$. For small deformations, the infinitesimal **strain tensor**:

$$\boxed{\varepsilon_{ij} = \frac{1}{2}\left(\frac{\partial u_i}{\partial x_j} + \frac{\partial u_j}{\partial x_i}\right)}$$

Symmetric: $\varepsilon_{ij} = \varepsilon_{ji}$ (6 independent components in 3D).

Physical interpretation of components:

- **Diagonal** $\varepsilon_{11}$, $\varepsilon_{22}$, $\varepsilon_{33}$: normal strains (fractional extension along each axis). $\varepsilon_{kk} = \nabla\cdot\mathbf{u}$ = volumetric strain.
- **Off-diagonal** $\varepsilon_{12}$, $\varepsilon_{13}$, $\varepsilon_{23}$: shear strains (change in angle between originally perpendicular line elements). Factor of 2 compared to engineering shear strain $\gamma_{ij} = 2\varepsilon_{ij}$.

**Decomposition:** Any displacement gradient decomposes into: $$\frac{\partial u_i}{\partial x_j} = \underbrace{\varepsilon_{ij}}_{\text{strain}} + \underbrace{\omega_{ij}}_{\text{rotation}}$$

where the antisymmetric part $\omega_{ij} = \frac{1}{2}(\partial_i u_j - \partial_j u_i)$ is a rigid body rotation — it causes no stress and is not related to deformation.

### 15.2.2 — The Strain Rate Tensor (Fluids)

For a flowing fluid, it is not the displacement but the **velocity gradient** that causes viscous stress. The strain rate tensor:

$$\dot\varepsilon_{ij} = \frac{1}{2}\left(\frac{\partial v_i}{\partial x_j} + \frac{\partial v_j}{\partial x_i}\right)$$

Same structure as $\varepsilon_{ij}$ but with velocities instead of displacements. This is Newton's law of viscosity generalized to three dimensions.

**Vorticity:** The antisymmetric part of the velocity gradient: $$\omega_{ij} = \frac{1}{2}\left(\frac{\partial v_i}{\partial x_j} - \frac{\partial v_j}{\partial x_i}\right), \qquad \boldsymbol{\omega} = \nabla\times\mathbf{v}$$

Irrotational flow: $\boldsymbol{\omega} = 0$ → potential flow ($\mathbf{v} = \nabla\phi$).

---

## 15.3 — The Stress Tensor: Internal Forces

### 15.3.1 — Cauchy's Stress Tensor

Consider a material cut by an imaginary plane with unit normal $\hat n$. The force per unit area exerted by the material on the positive side on the negative side is the **traction vector** $\mathbf{t}^{(\hat n)}$.

**Cauchy's theorem:** The traction vector is linear in $\hat n$:

$$t_i^{(\hat n)} = \sigma_{ij} n_j$$

where $\sigma_{ij}$ is the **Cauchy stress tensor** — a $3\times3$ matrix (9 components, reduced to 6 by symmetry) that completely characterizes the internal force state at a point.

Physical interpretation:

- $\sigma_{11}$, $\sigma_{22}$, $\sigma_{33}$: **normal stresses** — tension (positive) or compression (negative)
- $\sigma_{12} = \sigma_{21}$, etc.: **shear stresses** — tangential forces on each face
- **Pressure:** $p = -\frac{1}{3}\sigma_{kk}$ (hydrostatic stress, sign convention: compression is positive pressure)

**Symmetry of $\sigma_{ij}$:** Angular momentum balance for a fluid parcel requires $\sigma_{ij} = \sigma_{ji}$ — the stress tensor is symmetric (6 independent components, not 9).

### 15.3.2 — Principal Stresses

The stress tensor can always be diagonalized by rotating to principal axes — the three orthogonal directions in which only normal stresses act (no shear). The eigenvalues $\sigma_1 \geq \sigma_2 \geq \sigma_3$ are the **principal stresses**.

The **von Mises equivalent stress** (used in failure criteria, §15.11): $$\sigma_{vM} = \sqrt{\frac{(\sigma_1-\sigma_2)^2 + (\sigma_2-\sigma_3)^2 + (\sigma_3-\sigma_1)^2}{2}}$$

---

## 15.4 — Conservation Laws: Noether's Theorem in Continuum Form

The conservation laws from Ch. 1 (Noether's theorem) apply to continua as **partial differential equations** — one for each conserved density.

### 15.4.1 — Mass Conservation (Continuity Equation)

$$\boxed{\frac{\partial\rho}{\partial t} + \nabla\cdot(\rho\mathbf{v}) = 0}$$

or equivalently: $\frac{D\rho}{Dt} + \rho\nabla\cdot\mathbf{v} = 0$

**For incompressible flow** ($D\rho/Dt = 0$, constant density following a parcel): $$\nabla\cdot\mathbf{v} = 0$$

Every divergence-free velocity field is volume-preserving. This is the continuum form of the conservation of particle number (Noether, U(1) of mass in the non-relativistic limit, Ch. 1 §1.7).

### 15.4.2 — Momentum Conservation (Cauchy's Equation of Motion)

Newton's second law for a material parcel of density $\rho$, acted on by body force $\mathbf{f}$ per unit volume and surface force from the stress tensor:

$$\boxed{\rho\frac{D\mathbf{v}}{Dt} = \rho\left(\frac{\partial\mathbf{v}}{\partial t} + (\mathbf{v}\cdot\nabla)\mathbf{v}\right) = \nabla\cdot\boldsymbol{\sigma} + \mathbf{f}}$$

This is **Cauchy's equation of motion** — the universal momentum equation for any continuum. It is Newton's second law in continuum form. The specific form of $\boldsymbol{\sigma}$ (the constitutive relation) determines whether this is fluid mechanics or solid mechanics.

- **Body force** $\mathbf{f}$: gravity $\rho\mathbf{g}$, electromagnetic (Lorentz force on a charged continuum), centrifugal and Coriolis (in a rotating frame, Ch. 9 §9.9)
- **Surface force** $\nabla\cdot\boldsymbol{\sigma}$: from the divergence of the stress tensor — a net stress gradient gives a net force

This is Noether's theorem (space translation → momentum conservation, Ch. 1 §1.7) in PDE form: $\partial_t(\rho v_i) + \partial_j(\rho v_i v_j - \sigma_{ij}) = f_i$.

### 15.4.3 — Energy Conservation

The energy equation (first law of thermodynamics per unit volume in motion):

$$\rho\frac{De}{Dt} = \sigma_{ij}\dot\varepsilon_{ij} - \nabla\cdot\mathbf{q} + \dot Q_{vol}$$

where $e$ is the specific internal energy, $\sigma_{ij}\dot\varepsilon_{ij}$ is the viscous dissipation rate (always positive, second law), $\mathbf{q}$ is the heat flux (from Fourier's law, Ch. 13 §13.5), and $\dot Q_{vol}$ is any volumetric heat source.

---

## 15.5 — The Ideal Fluid: Euler Equations

### 15.5.1 — The Constitutive Relation for an Ideal Fluid

An **ideal** (inviscid) fluid has no viscosity: no tangential stress between fluid layers. The only stress is isotropic pressure:

$$\sigma_{ij} = -p,\delta_{ij}$$

Substituting into Cauchy's equation:

$$\boxed{\rho\frac{D\mathbf{v}}{Dt} = -\nabla p + \rho\mathbf{g}}$$

These are the **Euler equations** for an inviscid fluid. Together with the continuity equation and an equation of state $p = p(\rho)$, they form a closed system.

### 15.5.2 — Bernoulli's Equation

For **steady** ($\partial/\partial t = 0$), **incompressible** ($\rho = \text{const}$), **irrotational** ($\boldsymbol{\omega} = \nabla\times\mathbf{v} = 0$) flow, the Euler equation integrates along a streamline to:

$$\boxed{p + \frac{1}{2}\rho v^2 + \rho g z = \text{const along a streamline}}$$

**Bernoulli's equation** — derived from Newton's law for an ideal fluid parcel.

**The three terms:**

- $p$: static pressure (energy density stored as pressure)
- $\frac{1}{2}\rho v^2$: dynamic pressure (kinetic energy density)
- $\rho g z$: hydrostatic pressure (potential energy density)

**Applications:**

- **Pitot tube:** measures dynamic pressure $\frac{1}{2}\rho v^2 = p_{stagnation} - p_{static}$ → airspeed
- **Venturi meter:** pressure drop at constriction $\Delta p = \frac{1}{2}\rho(v_2^2 - v_1^2)$ → flow rate
- **Lift on an airfoil:** faster flow over upper surface → lower pressure → net upward force (though Kutta-Joukowski is more precise)
- **Cavitation onset:** when local $p$ drops below vapor pressure $p_v$

### 15.5.3 — Hydrostatics

For a static fluid ($\mathbf{v} = 0$), Euler reduces to:

$$\nabla p = \rho\mathbf{g} \quad\Longrightarrow\quad \frac{dp}{dz} = -\rho g$$

For incompressible fluid: $p(z) = p_0 - \rho g z$ (linear pressure increase with depth).

**Archimedes' principle** follows directly: integrate pressure over the surface of a submerged body → net upward force $= \rho_f g V_{displaced}$.

---

## 15.6 — Viscous Flow: The Navier-Stokes Equation

### 15.6.1 — The Constitutive Relation for a Newtonian Fluid

A **Newtonian fluid** has a linear relationship between the stress tensor and the strain rate tensor. The most general isotropic, linear, symmetric relation:

$$\sigma_{ij} = -p,\delta_{ij} + 2\mu\dot\varepsilon_{ij} + \lambda\dot\varepsilon_{kk}\delta_{ij}$$

where:

- $-p\delta_{ij}$: isotropic pressure (as in ideal fluid)
- $2\mu\dot\varepsilon_{ij}$: deviatoric (shear) viscous stress ($\mu$ = dynamic viscosity)
- $\lambda\dot\varepsilon_{kk}\delta_{ij}$: bulk viscous stress from volume rate of change

**Stokes' hypothesis** ($\lambda = -\frac{2}{3}\mu$): the bulk viscosity is zero for monoatomic ideal gases (well-verified) and approximately zero for most Newtonian liquids. With Stokes' hypothesis and incompressibility ($\dot\varepsilon_{kk} = \nabla\cdot\mathbf{v} = 0$):

$$\sigma_{ij} = -p,\delta_{ij} + 2\mu\dot\varepsilon_{ij}$$

### 15.6.2 — The Navier-Stokes Equation

Substituting the Newtonian constitutive relation into Cauchy's equation (using $\nabla\cdot\boldsymbol{\sigma} = -\nabla p + \mu\nabla^2\mathbf{v}$ for incompressible flow):

$$\boxed{\rho\frac{D\mathbf{v}}{Dt} = \rho\underbrace{\left(\frac{\partial\mathbf{v}}{\partial t} + (\mathbf{v}\cdot\nabla)\mathbf{v}\right)}_{\text{inertia}} = \underbrace{-\nabla p}_{\text{pressure}} + \underbrace{\mu\nabla^2\mathbf{v}}_{\text{viscosity}} + \underbrace{\rho\mathbf{g}}_{\text{gravity}}}$$

together with the incompressibility constraint:

$$\nabla\cdot\mathbf{v} = 0$$

These are the **Navier-Stokes equations for incompressible Newtonian flow** — four scalar equations (3 momentum + 1 continuity) for four unknowns ($v_x, v_y, v_z, p$).

**The nonlinear term** $(\mathbf{v}\cdot\nabla)\mathbf{v}$: advection of momentum by the flow itself. This is the source of all complexity in fluid mechanics — instabilities, turbulence, chaotic behavior. Without this term, NS is linear and easily solvable.

**Origin of the viscous term:** The term $\mu\nabla^2\mathbf{v}$ is Newton's law of viscosity (Ch. 13 §13.7) applied at every point and every direction simultaneously. The viscosity $\mu$ is the Kubo Green function of §13.7.1.

### 15.6.3 — Vorticity Transport

Taking the curl of NS for incompressible flow:

$$\frac{D\boldsymbol{\omega}}{Dt} = (\boldsymbol{\omega}\cdot\nabla)\mathbf{v} + \nu\nabla^2\boldsymbol{\omega}$$

where $\nu = \mu/\rho$ is the **kinematic viscosity** and $\boldsymbol{\omega} = \nabla\times\mathbf{v}$.

- $(\boldsymbol{\omega}\cdot\nabla)\mathbf{v}$: vortex stretching — the term responsible for the cascade to smaller scales in turbulence (absent in 2D!)
- $\nu\nabla^2\boldsymbol{\omega}$: viscous diffusion of vorticity

---

## 15.7 — Exact Solutions of Navier-Stokes

### 15.7.1 — Hagen-Poiseuille Flow (Pipe Flow)

Steady, fully-developed, incompressible flow through a circular pipe of radius $R$. Assume: $\mathbf{v} = v_z(r)\hat z$, $\partial/\partial t = 0$, $\partial/\partial z = 0$.

NS simplifies to: $\mu\nabla^2 v_z = \frac{dp}{dz} = \text{const} \equiv -G$

In cylindrical coordinates: $\frac{\mu}{r}\frac{d}{dr}\left(r\frac{dv_z}{dr}\right) = -G$

Boundary conditions: $v_z(R) = 0$ (no-slip), $dv_z/dr|_{r=0} = 0$ (symmetry):

$$\boxed{v_z(r) = \frac{G}{4\mu}(R^2 - r^2)} \quad\text{(parabolic profile)}$$

**Hagen-Poiseuille law** (volume flow rate $Q$ and pressure drop $\Delta p$):

$$Q = \int_0^R v_z(r)\cdot 2\pi r,dr = \frac{\pi R^4}{8\mu}\frac{\Delta p}{L} \quad\Longrightarrow\quad \Delta p = \frac{8\mu LQ}{\pi R^4}$$

The $R^4$ dependence is dramatic: doubling the pipe radius increases flow by 16× at the same pressure drop. Halving the radius increases resistance by 16×.

**The hydraulic resistance:**

$$R_{hyd} = \frac{\Delta p}{Q} = \frac{8\mu L}{\pi R^4}$$

This is the fluid analog of electrical resistance ($R = \rho L/A$) — the same formula structure from the same Kubo-derived transport law. In Bridge C (Ch. 17), this becomes the "R" element in the hydraulic circuit.

**Validity:** Laminar flow only. Turbulence onset at $Re_c \approx 2300$.

### 15.7.2 — Couette Flow (Flow Between Plates)

Steady flow between two parallel plates, lower at rest, upper moving at velocity $U$. Only $v_x(y)$ nonzero, no pressure gradient:

$$\mu\frac{d^2v_x}{dy^2} = 0 \quad\Longrightarrow\quad v_x = U\frac{y}{h}$$

Linear velocity profile. Wall shear stress:

$$\tau_w = \mu\frac{dv_x}{dy} = \frac{\mu U}{h}$$

This is Newton's law of viscosity from Ch. 13 §13.7 — now derived as an exact solution of NS with the appropriate boundary conditions. Couette flow is the canonical laboratory setup for measuring viscosity (the cone-and-plate rheometer is a variant).

### 15.7.3 — Stokes Flow (Very Low Reynolds Number)

When $Re \ll 1$, the inertia term $\rho(\mathbf{v}\cdot\nabla)\mathbf{v}$ is negligible compared to viscous forces. NS becomes linear (Stokes equations):

$$\mu\nabla^2\mathbf{v} = \nabla p, \qquad \nabla\cdot\mathbf{v} = 0$$

**Stokes drag on a sphere** of radius $a$ moving at velocity $U$:

$$\mathbf{F}_{drag} = -6\pi\mu a\mathbf{U}$$

**Applications:** Sedimentation of small particles; blood cell motion; swimming of microorganisms; MEMS fluid channels; aerosol particle dynamics.

The Stokes drag formula is also the basis for the Einstein relation (Ch. 13 §13.6.2): combining $F_{drag} = 6\pi\mu a v$ with $F_{drift} = D\nabla c / c$: $D = k_BT/(6\pi\mu a)$ (Stokes-Einstein equation).

---

## 15.8 — Dimensional Analysis and the Reynolds Number

### 15.8.1 — Non-Dimensionalizing the Navier-Stokes Equation

Scale all variables by characteristic values: velocity $U_0$, length $L_0$, time $L_0/U_0$, pressure $\rho U_0^2$. The dimensionless NS equation:

$$\frac{D\mathbf{v}^_}{Dt^_} = -\nabla^* p^* + \frac{1}{Re}\nabla^{_2}\mathbf{v}^_ + \frac{1}{Fr^2}\hat g$$

where the **Reynolds number** $Re$ and **Froude number** $Fr$:

$$\boxed{Re = \frac{\rho U_0 L_0}{\mu} = \frac{U_0 L_0}{\nu}} \qquad Fr = \frac{U_0}{\sqrt{gL_0}}$$

**The Reynolds number is the single most important parameter in fluid mechanics.** It measures the ratio of inertial forces to viscous forces.

|$Re$|Flow regime|Example|
|---|---|---|
|$Re \ll 1$|Stokes (creeping) flow|Pollen in air, microfluidics|
|$Re \sim 1$|Transitional (still laminar)|Blood in capillaries|
|$Re \sim 10^2$|Laminar with separation|Flow past a cylinder, streamlined bodies|
|$Re \sim 10^3$|Wake instabilities, vortex shedding|Kármán vortex street|
|$Re \gtrsim 2300$|Transition in pipes|Pipe flow becomes turbulent|
|$Re \sim 10^6$|Fully turbulent|Aircraft at cruise, water in rivers|
|$Re \sim 10^9$|Atmospheric flows|Ocean circulation, hurricanes|

### 15.8.2 — Turbulence: Where Layer 3 Has No Exact Model

At high $Re$, the inertial term $(\mathbf{v}\cdot\nabla)\mathbf{v}$ dominates. The flow becomes unstable to perturbations. Small eddies cascade into ever smaller eddies (Kolmogorov energy cascade) until viscous dissipation absorbs the energy at the Kolmogorov length scale:

$$\eta_K = \left(\frac{\nu^3}{\varepsilon_{diss}}\right)^{1/4}$$

For air at $Re = 10^6$: $\eta_K \sim 0.1$ mm — nine orders of magnitude smaller than the flight vehicle. Direct numerical simulation (DNS) of the NS equations at these $Re$ is computationally intractable.

**The engineering consequence:** Turbulence is the single most important unsolved problem in classical physics for engineering practice. Engineers use:

- **RANS** (Reynolds-Averaged NS): solve for time-averaged flow, model turbulence stresses ($k$-$\varepsilon$, $k$-$\omega$ models)
- **LES** (Large-Eddy Simulation): resolve large eddies, model small ones
- **DNS** (Direct Numerical Simulation): resolve all scales; feasible only for moderate $Re$

None of these is a closed-form Layer 3 model. Turbulence is where the Navier-Stokes PDE refuses to be lumped — one of the most honest demonstrations of why this book maintains all four layers rather than jumping straight to engineering formulas.

---

## 15.9 — Linear Elasticity: The Navier Equation

### 15.9.1 — Constitutive Relation for a Linear Elastic Solid

From Ch. 13 §13.8.2 (Hooke's law, general form):

$$\sigma_{ij} = C_{ijkl}\varepsilon_{kl}$$

For an **isotropic** material (same properties in all directions), $C_{ijkl}$ has only two independent constants — the **Lamé constants** $\lambda$ and $\mu_L$:

$$\boxed{\sigma_{ij} = \lambda\varepsilon_{kk}\delta_{ij} + 2\mu_L\varepsilon_{ij}}$$

Equivalently, in terms of Young's modulus $E$ (stiffness) and Poisson's ratio $\nu_P$ (lateral contraction):

$$\lambda = \frac{\nu_P E}{(1+\nu_P)(1-2\nu_P)}, \qquad \mu_L = G = \frac{E}{2(1+\nu_P)}$$

|Quantity|Definition|Typical range|
|---|---|---|
|Young's modulus $E$|Uniaxial stress/strain|Steel: 200 GPa; Al: 70 GPa; rubber: 0.01–0.1 GPa|
|Shear modulus $G$|Shear stress/strain|Steel: 80 GPa; Al: 26 GPa|
|Poisson's ratio $\nu_P$|$-\varepsilon_{yy}/\varepsilon_{xx}$ for uniaxial $\sigma_{xx}$|Metals: 0.25–0.35; rubber: $\approx 0.5$; foam: $\approx 0$|
|Bulk modulus $K$|Pressure/volumetric strain|Steel: 160 GPa; water: 2.2 GPa|

**Relations:** $K = \lambda + \frac{2}{3}\mu_L = \frac{E}{3(1-2\nu_P)}$

### 15.9.2 — The Navier Equation of Motion

Substituting the isotropic Hooke's law into Cauchy's equation:

$$\rho\frac{\partial^2\mathbf{u}}{\partial t^2} = (\lambda+\mu_L)\nabla(\nabla\cdot\mathbf{u}) + \mu_L\nabla^2\mathbf{u} + \mathbf{f}$$

This is the **Navier equation** (or **Lamé-Navier equation**) of linear elasticity — the governing equation for displacement in a deformable elastic solid.

**Comparison with Navier-Stokes:**

- In NS: $\rho D\mathbf{v}/Dt = -\nabla p + \mu\nabla^2\mathbf{v} + \mathbf{f}$ (velocities)
- In Navier: $\rho\ddot{\mathbf{u}} = (\lambda+\mu_L)\nabla(\nabla\cdot\mathbf{u}) + \mu_L\nabla^2\mathbf{u} + \mathbf{f}$ (displacements)

Same mathematical structure, different physical variables. The elastic equation is linear; NS is nonlinear (the $(\mathbf{v}\cdot\nabla)\mathbf{v}$ term). This is why solid mechanics is mathematically much more tractable than turbulent fluid mechanics.

### 15.9.3 — Static Equilibrium

In statics ($\ddot{\mathbf{u}} = 0$):

$$(\lambda+\mu_L)\nabla(\nabla\cdot\mathbf{u}) + \mu_L\nabla^2\mathbf{u} + \mathbf{f} = 0$$

For incompressible material ($\nabla\cdot\mathbf{u} = 0$, $\nu_P\to\frac{1}{2}$):

$$\mu_L\nabla^2\mathbf{u} + \mathbf{f} = 0 \quad\Longrightarrow\quad \nabla^2\mathbf{u} = -\mathbf{f}/\mu_L$$

This is a vector Poisson equation — same structure as electrostatics (Ch. 11 §11.10). The Green's function for the elastic displacement field due to a point force is the **Kelvin fundamental solution** — the elastic analog of the Coulomb potential.

---

## 15.10 — Elastic Waves: P-waves and S-waves

### 15.10.1 — Wave Solutions to the Navier Equation

In a homogeneous elastic medium with no body forces ($\mathbf{f} = 0$), try plane wave solutions $\mathbf{u} = \mathbf{A}e^{i(\mathbf{k}\cdot\mathbf{r}-\omega t)}$.

**Helmholtz decomposition:** $\mathbf{u} = \nabla\phi + \nabla\times\boldsymbol{\psi}$ separates into a scalar potential (irrotational) and vector potential (solenoidal) part.

**P-waves** (Primary, Pressure, Longitudinal): $\nabla\times\mathbf{u} = 0$, $\mathbf{k}\parallel\mathbf{A}$

$$\rho\omega^2\mathbf{A} = (\lambda+2\mu_L)k^2\mathbf{A} \quad\Longrightarrow\quad \boxed{v_P = \sqrt{\frac{\lambda+2\mu_L}{\rho}} = \sqrt{\frac{K+\frac{4}{3}G}{\rho}}}$$

P-waves: particles oscillate parallel to propagation direction (compression and rarefaction); transmitted through solids, liquids, and gases.

**S-waves** (Secondary, Shear, Transverse): $\nabla\cdot\mathbf{u} = 0$, $\mathbf{k}\perp\mathbf{A}$

$$\rho\omega^2\mathbf{A} = \mu_L k^2\mathbf{A} \quad\Longrightarrow\quad \boxed{v_S = \sqrt{\frac{\mu_L}{\rho}} = \sqrt{\frac{G}{\rho}}}$$

S-waves: particles oscillate perpendicular to propagation; transmitted only through solids (liquids and gases have $G = 0$, so $v_S = 0$).

Since $\lambda + 2\mu_L > \mu_L$: **P-waves always travel faster than S-waves.**

|Material|$v_P$ (m/s)|$v_S$ (m/s)|$v_P/v_S$|
|---|---|---|---|
|Steel|5960|3235|1.84|
|Aluminum|6420|3040|2.11|
|Granite|5950|3640|1.63|
|Water|1480|0|∞|
|Air (1 atm)|343|0|∞|

**Connection to phonons (Ch. 6 §6.7.1):** The elastic wave equations derived here are the classical ($\hbar\to 0$) limit of quantum phonon dispersion. Acoustic phonons (Ch. 6) → acoustic elastic waves in the long-wavelength limit. The speed of sound in a solid is the group velocity of acoustic phonons at $k\to 0$.

### 15.10.2 — The Poisson's Ratio Constraint

The wave speed ratio:

$$\frac{v_P}{v_S} = \sqrt{\frac{\lambda+2\mu_L}{\mu_L}} = \sqrt{\frac{2(1-\nu_P)}{1-2\nu_P}}$$

For most metals ($\nu_P \approx 0.3$): $v_P/v_S \approx 1.87$. For incompressible materials ($\nu_P \to 0.5$): $v_P\to\infty$ (pressure waves travel instantaneously — bulk modulus $K\to\infty$). For materials with $\nu_P = 0$ (cork-like): $v_P/v_S = \sqrt{2}$.

**Seismology:** The time delay between P-wave and S-wave arrivals at a seismometer directly gives the distance to an earthquake epicenter. Three stations triangulate the location. The ratio $v_P/v_S$ also reveals subsurface geology — different for water-saturated rock vs. dry rock.

---

## 15.11 — Failure Criteria

### 15.11.1 — The von Mises Criterion (Ductile Materials)

Ductile materials (metals) yield when the **elastic strain energy of distortion** reaches a critical value. In terms of principal stresses:

$$\sigma_{vM} = \sqrt{\frac{(\sigma_1-\sigma_2)^2+(\sigma_2-\sigma_3)^2+(\sigma_3-\sigma_1)^2}{2}} \geq \sigma_y$$

where $\sigma_y$ is the uniaxial yield strength. The von Mises surface is a cylinder in principal stress space — yielding is insensitive to hydrostatic pressure.

For plane stress ($\sigma_3 = 0$): $$\sigma_{vM} = \sqrt{\sigma_1^2 - \sigma_1\sigma_2 + \sigma_2^2} \geq \sigma_y$$

### 15.11.2 — The Tresca Criterion (Maximum Shear Stress)

Simpler but slightly more conservative: yielding occurs when the maximum shear stress exceeds the shear yield strength $\tau_y = \sigma_y/2$:

$$\tau_{max} = \frac{\sigma_1 - \sigma_3}{2} \geq \frac{\sigma_y}{2}$$

Von Mises is more accurate for ductile metals; Tresca is simpler and safe (conservative). Both give the same result for uniaxial stress.

### 15.11.3 — Fracture Mechanics (Brittle Materials)

Brittle materials (ceramics, glass, rock) fail by crack propagation before yielding. Griffith's criterion: a crack of half-length $a$ propagates when the stress intensity factor exceeds the fracture toughness:

$$K_I = \sigma\sqrt{\pi a} \geq K_{Ic}$$

$K_{Ic}$ (MPa√m): steel $\sim 50$–$200$; aluminum $\sim 20$–$45$; glass $\sim 0.7$; concrete $\sim 0.2$–$1.4$; Si wafer $\sim 0.9$.

The fracture mechanics approach is not covered in full depth here — it is the subject of an entire CE/ME course. The key point: **the failure criterion is as important as the stress distribution.** Solving the Navier equation gives you stresses; the failure criterion tells you what those stresses mean.

---

## 15.12 — Beyond Newtonian: Viscoelasticity and Non-Newtonian Fluids

### 15.12.1 — Viscoelastic Materials

From Ch. 13 §13.8.1: at finite frequency, the elastic modulus becomes complex: $\tilde C(\omega) = C'(\omega) + iC''(\omega)$. Materials with significant $C''$ are **viscoelastic**:

- Elastic behavior at short times (behave like solids)
- Viscous behavior at long times (flow like liquids)
- Maxwell model: $\frac{d\sigma}{dt} + \frac{\sigma}{\tau_{rel}} = E\dot\varepsilon$ (series spring + dashpot)
- Kelvin-Voigt model: $\sigma = E\varepsilon + \eta\dot\varepsilon$ (parallel spring + dashpot)

**Engineering materials:** Polymers, biological tissues, asphalt, concrete (under creep), metals at elevated temperature. The loss tangent $\tan\delta = C''/C'$ characterizes energy dissipation per cycle — critical for vibration damping, acoustic absorption, and tire hysteresis.

### 15.12.2 — Non-Newtonian Fluids

The Newtonian constitutive relation $\tau = \mu\dot\varepsilon$ (constant $\mu$) is an approximation. For complex fluids:

**Power-law fluids:** $\mu_{eff} = K\dot\varepsilon^{n-1}$

- $n < 1$: **shear-thinning** (ketchup, blood, polymer melts) — viscosity decreases with shear rate
- $n > 1$: **shear-thickening** (cornstarch in water, some slurries)
- $n = 1$: Newtonian

**Bingham plastics:** require a yield stress $\tau_0$ before flowing: $\tau = \tau_0 + \mu_B\dot\varepsilon$ for $|\tau| > \tau_0$, $\dot\varepsilon = 0$ otherwise. Examples: toothpaste, certain drilling muds, fresh concrete.

**Thixotropy:** viscosity is history-dependent (decreased by recent shearing and recovers over time). Paints, gels, some clays.

**Engineering importance:** Non-Newtonian rheology governs polymer processing (injection molding, extrusion), food processing, pharmaceutical formulation, concrete placement, drilling mud design, and biological fluid dynamics (blood is shear-thinning; this matters in arterial flow).

---

## 15.13 — Summary

All major equations of continuum mechanics derived from Cauchy's equation + constitutive relations:

|Result|Constitutive input|Application|
|---|---|---|
|Euler equation|$\sigma_{ij} = -p\delta_{ij}$ (ideal fluid)|Aerodynamics, hydraulics|
|Bernoulli equation|Euler + steady + irrotational|Pitot, Venturi, airfoil|
|Navier-Stokes|Newtonian: $\sigma_{ij} = -p\delta_{ij} + 2\mu\dot\varepsilon_{ij}$|All viscous flow|
|Hagen-Poiseuille|NS + pipe geometry|Pipe flow, blood vessels|
|Couette flow|NS + shear geometry|Viscometry, lubrication|
|Stokes drag|NS + $Re\ll 1$|Particle settling, microfluidics|
|Reynolds number|Non-dimensionalized NS|Flow regime classification|
|Navier equation|Hooke: $\sigma_{ij} = \lambda\varepsilon_{kk}\delta_{ij} + 2\mu_L\varepsilon_{ij}$|Solid deformation|
|P-wave speed|$v_P = \sqrt{(\lambda+2\mu_L)/\rho}$|Seismology, NDT, geophysics|
|S-wave speed|$v_S = \sqrt{\mu_L/\rho}$|Seismology, shear wave imaging|
|Von Mises criterion|Yield when $\sigma_{vM} \geq \sigma_y$|Ductile metal design|
|Stokes-Einstein|$D = k_BT/6\pi\mu a$|Particle diffusion, Einstein relation|

---

## 15.14 — Engineering Thread

|Physics|Application|
|---|---|
|Continuity equation $\partial_t\rho + \nabla\cdot(\rho\mathbf{v}) = 0$|Mass balance in all pipe and duct systems; conservation checks in CFD|
|Bernoulli $p+\frac{1}{2}\rho v^2+\rho gz = \text{const}$|Pitot tubes; Venturi meters; nozzle design; pump head calculations|
|Hagen-Poiseuille $\Delta p = 8\mu LQ/\pi R^4$|Pipe sizing; hydraulic system design; microfluidic channel design|
|Reynolds number $Re = \rho vL/\mu$|Flow regime prediction; scale model testing (similarity); turbulence onset|
|Stokes drag $F = 6\pi\mu aU$|Particle settling in ChE; filtration; aerosol dynamics; electrophoresis (Ch. 13)|
|Navier equation + elastic waves|NDT (ultrasonic testing); geophysical exploration; medical ultrasound|
|Von Mises criterion $\sigma_{vM} \geq \sigma_y$|Structural design of pressure vessels, beams, frames|
|Fracture mechanics $K_I = \sigma\sqrt{\pi a}$|Crack growth prediction; fatigue life; brittle fracture of glass/ceramic components|
|Non-Newtonian rheology|Polymer processing; concrete mix design; food and pharmaceutical manufacturing|
|Viscoelastic $\tan\delta$|Vibration damper selection; acoustic panel design; polymer material selection|
|Stokes-Einstein $D = k_BT/6\pi\mu a$|Drug diffusion in tissue; membrane separation processes; colloid stability|

---

## 15.15 — Looking Ahead

Chapter 15 completes the governing equations of continuum mechanics. Layer 2 now contains its full set of PDEs:

- Newton's gravity: $\nabla^2\Phi = 4\pi G\rho$ (Ch. 8)
- Classical mechanics: Hamilton's equations (Ch. 9)
- Thermodynamics: 4 laws + equations of state (Ch. 10)
- Maxwell's equations (Ch. 11)
- EM wave equation: $\Box\mathbf{E} = 0$ (Ch. 12)
- Transport laws: Ohm, Fourier, Fick, viscosity, Hooke (Ch. 13)
- Navier-Stokes: fluid mechanics (Ch. 15, this chapter)
- Navier equation: solid mechanics (Ch. 15, this chapter)

**Chapter 16** now shows the unifying PDE structure: the wave equation $\partial^2\phi/\partial t^2 = v^2\nabla^2\phi$ and the diffusion equation $\partial\phi/\partial t = D\nabla^2\phi$ appear identically across acoustics, electromagnetism, elasticity, heat, and mass transport — with only $v$, $D$, and the identity of $\phi$ changing. This is the final Layer-2 unification before Bridge C begins the descent to Layer 3.

---

_End of Chapter 15._

---

_Next: Chapter 16 — The Unified PDE: Waves and Diffusion Across All Domains_