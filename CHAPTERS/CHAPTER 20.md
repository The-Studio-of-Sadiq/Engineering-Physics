# CHAPTER 20
# CE and ChE Systems: Structures, Hydraulics, and Process Engineering
### The Structural, Hydraulic, and Chemical Instantiations of Layer 3

---

> *Terzaghi's consolidation equation and the 1D heat equation are the same equation.*
> *The NTU method for an absorption column and the NTU method for a heat exchanger are the same design framework.*
> *Darcy's law and Fick's law are the same constitutive shape arrived at independently.*
> *The Arrhenius factor and the Boltzmann factor share a statistical origin, not an equation.*
>
> Four different claims, and the difference between them matters. This chapter
> labels which is which rather than calling all of them "identical".

---

## 20.0 — Overview

Chapters 18 and 19 instantiated the Layer-3 template (Ch. 17) in the electrical
and mechanical-thermal domains. This chapter completes the engineering coverage:

**Civil Engineering (CE):** Structural analysis, open-channel hydraulics,
groundwater flow, soil consolidation.

**Chemical Engineering (ChE):** Mass and energy balances, reaction kinetics
and reactor design, separation processes, mass transfer.

Every concept in this chapter traces to earlier physics. The last column states
**what kind of trace** — see §20.0.1 for why the distinction is not pedantry.

| Ch. 20 concept | Physics origin | Connection |
|---|---|---|
| Beam bending $EI\,d^4w/dx^4 = q$ | Euler-Bernoulli (Ch. 16 §16.7.2); Navier equation (Ch. 15) | `[DERIVATION]` |
| Stiffness method $\mathbf{K}\mathbf{u} = \mathbf{F}$ | FEM discretisation of the Navier equation (Ch. 16 §16.11) | `[DERIVATION]` |
| Terzaghi consolidation $\partial u_e/\partial t = c_v\,\partial^2 u_e/\partial z^2$ | 1D diffusion equation (Ch. 16 §16.8; Ch. 14 §14.8) | `[DERIVATION]` — same equation |
| Transient groundwater $S\,\partial h/\partial t = T\nabla^2 h$ | Advection–diffusion / storage formulation (Ch. 16) | `[DERIVATION]` under stated storage assumptions |
| Darcy's law $q = -K\nabla h$ | Linear transport law, same form as Fick (Ch. 13 §13.6) | `[STRUCTURAL CONNECTION]` |
| PFR design equation | 1D advection–reaction PDE (Ch. 16) | `[DERIVATION]` |
| CSTR design equation | Lumped mass balance (Bridge C, Ch. 17) | `[APPROXIMATION]` — well-mixed is an assumption |
| Arrhenius $k = A\,e^{-E_a/RT}$ | Boltzmann factor $e^{-E/k_BT}$ (Ch. 10 §10.3.3) | `[STRUCTURAL CONNECTION]` — shared statistical origin |
| NTU for absorption columns | NTU for heat exchangers (Ch. 19 §19.6.3) | `[STRUCTURAL CONNECTION]` — shared design framework |
| Two-resistance mass transfer | Thermal resistances in series (Ch. 17, 19) | `[STRUCTURAL CONNECTION]` |
| Manning's equation | Navier–Stokes, empirically integrated (Ch. 15) | `[PHENOMENOLOGICAL]` |
| Rational method unit hydrograph | Linear filter / transfer function (Ch. 21 §21.4) | `[ANALOGY]` |

### 20.0.1 — Four kinds of "same", and which one this chapter is allowed to claim

CE and ChE reuse the mathematics of physics constantly. But "the same
mathematics" is not one claim — it is four, with different strength and
different failure conditions. Collapsing them is how a physics text turns into
a false analogy, so the distinction is stated once here and then applied.

| Kind | What is actually shared | What is *not* shared | Can fail because… |
|---|---|---|---|
| **Mathematical identity** | The governing equation itself, term by term, once the assumptions are imposed | Nothing — the equations are the same object | The *assumptions* fail (1D, homogeneous, linear, incompressible) |
| **Constitutive correspondence** | The algebraic/functional form of a constitutive law, arrived at independently by different routes | The microscopic derivation, the closure, the coefficient values, the state variables | The closure model fails (turbulent, unsaturated, non-Newtonian, reactive) |
| **Shared statistical origin** | A statistical-mechanical structure (exponential activation, fluctuation–response) | The macroscopic law built on top of it | The statistical regime fails (non-equilibrium, non-ideal, many-body) |
| **Shared dimensionless framework** | The way dimensionless groups organise a design space | The driving forces, the equilibrium relations, the performance definition | The framework is applied outside its validated range |

Worked instantiations, in the order they appear:

- **Mathematical identity** — Terzaghi consolidation (§20.4.2). Once the soil
  skeleton is treated as linear-elastic and the flow as 1D, the equation *is*
  the diffusion equation. The erfc solution, the $T_v$ time factor, and the
  $T_v \approx (\pi/4)U^2$ parabola are not "analogues" of anything: they are
  the same solutions.
- **Constitutive correspondence** — Darcy's law (§20.4.1). Darcy's law is *not*
  a special case of Fick's law. It was measured, not derived, and the linear
  form emerges from pore-scale momentum balance plus an empirical closure. What
  it shares with Fick's law is the *shape* — linear in the gradient, flux
  proportional to a transport coefficient. The coefficient $K$ is not a
  diffusivity and does not have units that make it one.
- **Shared statistical origin** — Arrhenius kinetics (§20.7.1). The Arrhenius
  factor and the Boltzmann factor are the same exponential because both come
  from the Maxwell–Boltzmann energy distribution. But $k(T)$ is a rate
  constant for a specific reaction mechanism, whereas $e^{-E/k_BT}$ is a
  population ratio. Sharing an origin is not sharing an equation.
- **Shared dimensionless framework** — NTU/HTU (§20.9.2). The heat-exchanger and
  absorption-column methods are organised the same way, and the tabulated
  $\varepsilon$–NTU curves transfer usefully. But $NTU_{OG} = \int dy/(y^*-y)$
  and $NTU = UA/C_{min}$ have *different driving forces* (composition
  deficit against a VLE equilibrium vs temperature deficit against a fixed
  inlet), and the capacity-rate ratio is mimicked, not the same quantity.

**The rule used throughout this chapter:** the word "identical" appears only for
the first kind. Everything else is named for what it is.


---

## 20.1 — Structural Analysis: The Stiffness Method

### 20.1.1 — From PDE to Matrix: FEM for Structures

From Ch. 16 §16.11.2: the finite element method discretizes the domain into
elements and assembles a global matrix equation. For linear elastic structures
(Navier equation, Ch. 15 §15.9.2), the FEM gives:

$$\boxed{\mathbf{K}\mathbf{u} = \mathbf{F}}$$

where:
- $\mathbf{u}$: global displacement vector (degrees of freedom at nodes)
- $\mathbf{F}$: global force vector (applied loads and reactions)
- $\mathbf{K}$: global stiffness matrix (assembled from element stiffness matrices)

**The stiffness matrix is the discrete version of the elastic modulus tensor** from Ch. 15 §15.9.1 — the same physical law, now expressed as a matrix equation rather than a PDE.

**Model Ledger — continuum elastodynamics to the stiffness method**

| Field | Content |
|---|---|
| Parent theory | Linear elasticity (Ch. 15 §15.9): $\sigma_{ij} = \lambda\varepsilon_{kk}\delta_{ij} + 2\mu_L\varepsilon_{ij}$, $\varepsilon_{ij} = \tfrac12(\partial_i u_j + \partial_j u_i)$, $\varepsilon_{kk} = \nabla\cdot\mathbf{u}$ |
| Reduction | static equilibrium; small strain; linear elastic material; prismatic geometry; conforming interpolation |
| Model | $\mathbf{K}\mathbf{u} = \mathbf{F}$, with $\mathbf{K}$ assembled from element matrices |
| Assumptions | $\varepsilon \ll 1$; $\sigma = D\varepsilon$ with constant $D$; no body force in the element; full continuity of $u$ across elements |
| Physics retained | load path through stiffness; stress redistribution; equilibrium |
| Physics neglected | inertia (dynamics), geometric non-linearity, plasticity, fracture, contact, thermal strain |

> **Note on the constitutive form.** The isotropic law has two structurally
> distinct pieces, and both are load-bearing. The term
> $\lambda\varepsilon_{kk}\delta_{ij}$ is the *volumetric* response: it is
> multiplied by the trace $\varepsilon_{kk} = \nabla\cdot\mathbf{u}$, and it
> produces stress even in a pure hydrostatic strain where
> $\varepsilon_{ij} = 0$ for $i \ne j$. The factor of $2$ in
> $2\mu_L\varepsilon_{ij}$ is fixed by the requirement that $\mu_L$ be the
> shear modulus, i.e. that $\sigma_{ij}=2\mu_L\varepsilon_{ij}$ in pure shear
> where $\varepsilon_{kk}=0$. Writing $\lambda\varepsilon_{ij}\delta_{ij}$
> drops the trace dependence, and writing $\mu_L\varepsilon_{ij}$ without the 2
> makes $\mu_L$ the wrong modulus by a factor of two. An element stiffness
> matrix built on a corrupted form of this equation will pass equilibrium
> checks and still give the wrong displacements.
| Validity | deflections $\lesssim L/100$; stresses below yield; mesh refined so element stiffness converges |
| Fails when | large deflection (buckling, $P$-$\Delta$), yielding, or a singular/non-conforming element stiffness |
| Next model | nonlinear FEM; dynamic stiffness (modal analysis, Ch. 21); plastic $D(\varepsilon)$ |

### 20.1.2 — Bar Elements: Trusses

A truss member (bar) carries only axial force. For a bar of cross-sectional
area $A$, elastic modulus $E$, length $L$, along the $x$-axis:

**Element stiffness matrix** (in local coordinates, 2 nodes × 1 DOF = 2×2):

$$\mathbf{k}^{(e)} = \frac{EA}{L}\begin{pmatrix}1 & -1\\-1 & 1\end{pmatrix}$$

This is the spring stiffness from Ch. 17 §17.3.2 — a bar element is literally
a spring with $k = EA/L$ (Hooke's law, Ch. 13 §13.8.2, now applied to a bar).

**For a general truss member at angle $\theta$ to the global $x$-axis:**
transform the local stiffness matrix to global coordinates using the rotation matrix
$\mathbf{T}(\theta)$ — giving a 4×4 element stiffness matrix in the global frame.

**Assembly:** Add element stiffness contributions to the global positions
corresponding to their node DOFs. Apply displacement boundary conditions
(strike rows/columns for zero-displacement nodes). Solve the reduced system.

**Example: Three-bar truss**
Three members meeting at a central node (2 DOFs: $u_x$, $u_y$) with outer nodes
pinned to the ground. Each member contributes to the 2×2 global stiffness matrix:

$$\mathbf{K} = \sum_e \mathbf{k}^{(e)}, \qquad \begin{pmatrix}K_{xx}&K_{xy}\\K_{yx}&K_{yy}\end{pmatrix}\begin{pmatrix}u_x\\u_y\end{pmatrix} = \begin{pmatrix}F_x\\F_y\end{pmatrix}$$

Member forces: $N^{(e)} = \frac{EA}{L}(\Delta u_{axial})$ — axial stress $\sigma = N/A$.

### 20.1.3 — Beam Elements: Frames

A beam element carries transverse load, bending moment, and shear force.
For an Euler-Bernoulli beam element with 2 nodes × 2 DOFs (transverse displacement
$w$ + rotation $\theta = dw/dx$) = 4 DOFs per element:

**Element stiffness matrix** (4×4, Hermite shape functions):

$$\mathbf{k}^{(e)} = \frac{EI}{L^3}\begin{pmatrix}12&6L&-12&6L\\6L&4L^2&-6L&2L^2\\-12&-6L&12&-6L\\6L&2L^2&-6L&4L^2\end{pmatrix}$$

This matrix is the lumped version of the Euler-Bernoulli PDE
$EI\,d^4w/dx^4 = q(x)$ (Ch. 16 §16.7.2) — exactly Bridge C applied to beam bending.

**A frame element** combines axial bar behavior + bending beam behavior in
a 6-DOF element (3 per node: $u_x$, $u_y$, $\theta_z$). This is the basis
of commercial structural analysis software (SAP2000, ETABS, ANSYS, OpenSees).

---

## 20.2 — Beam Bending: Stress and Deflection

### 20.2.1 — The Euler-Bernoulli Beam Equation

For a slender beam with bending stiffness $EI$ (Young's modulus × second moment of area)
and distributed transverse load $q(x)$ [N/m]:

$$\boxed{EI\frac{d^4w}{dx^4} = q(x)}$$

This is a 4th-order ODE — a static limit of the flexural wave equation from Ch. 16 §16.7.2
(with $\partial_{tt}w = 0$). Integrating successively:

- $EI\,d^3w/dx^3 = V(x) + C_1$ — shear force
- $EI\,d^2w/dx^2 = M(x) + C_1 x + C_2$ — bending moment
- $EI\,dw/dx = \theta(x)$ — slope
- $EI\,w(x)$ — deflection

**Bending stress** at distance $y$ from the neutral axis:

$$\sigma_x = -\frac{My}{I}$$

Maximum bending stress at $y = c$ (outermost fiber): $\sigma_{max} = Mc/I = M/S$
where $S = I/c$ is the **section modulus** — the key geometric quantity in beam design.

### 20.2.2 — Standard Beam Cases

| Beam | Loading | Max deflection $w_{max}$ | Max moment $M_{max}$ |
|---|---|---|---|
| Cantilever, end load $P$ | $P$ at tip | $PL^3/3EI$ | $PL$ (at root) |
| Cantilever, UDL $q$ | $q$ uniform | $qL^4/8EI$ | $qL^2/2$ (at root) |
| Simply-supported, centre load $P$ | $P$ at midspan | $PL^3/48EI$ | $PL/4$ (at centre) |
| Simply-supported, UDL $q$ | $q$ uniform | $5qL^4/384EI$ | $qL^2/8$ (at centre) |
| Fixed-fixed, centre load $P$ | $P$ at midspan | $PL^3/192EI$ | $PL/8$ (at centre) |

**Design check:** $\sigma_{max} = M_{max}c/I \leq \sigma_{allowable}$ (strength)
and $w_{max} \leq L/360$ or $L/250$ (serviceability — deflection limit).

### 20.2.3 — Second Moment of Area

The second moment of area $I$ for common cross-sections about the centroidal axis:

| Section | $I$ |
|---|---|
| Rectangle $b\times h$ | $bh^3/12$ |
| Circle radius $r$ | $\pi r^4/4$ |
| Hollow rectangle (outer $B\times H$, inner $b\times h$) | $(BH^3 - bh^3)/12$ |
| I-beam (approx.) | $I_{flanges} + I_{web}$ (parallel axis theorem) |

**Parallel axis theorem:** $I = I_{centroid} + Ad^2$
(shift axis by $d$ from centroid, area $A$).

---

## 20.3 — Open-Channel Hydraulics

### 20.3.1 — Manning's Equation

For steady, uniform flow in an open channel (river, canal), the Navier-Stokes
equation integrated over the cross-section gives:

$$\boxed{V = \frac{1}{n}R_h^{2/3}S_0^{1/2}}$$

where $V$ is the average flow velocity, $n$ is Manning's roughness coefficient,
$R_h = A/P$ is the hydraulic radius (area/wetted perimeter), and $S_0$ is the
channel bed slope.

| Surface | Manning's $n$ |
|---|---|
| Smooth concrete | 0.011 |
| Brick/masonry | 0.015 |
| Gravel channel | 0.025–0.030 |
| Earth channel (clean) | 0.022 |
| Natural river (clean) | 0.025–0.035 |
| Floodplain (heavy brush) | 0.075–0.15 |

**Volume flow rate:** $Q = VA = \frac{1}{n}AR_h^{2/3}S_0^{1/2}$

**Connection to physics:** Manning's equation is an empirical fit to the
Navier-Stokes momentum equation with a turbulence model. The roughness
$n$ encodes the turbulent dissipation that Ch. 15 §15.8.2 showed cannot be
derived analytically for open-channel turbulent flow.

### 20.3.2 — The Froude Number and Flow Regimes

**Froude number** $Fr = V/\sqrt{gD}$ (analogous to Mach number in compressible flow):

- $Fr < 1$: **subcritical (tranquil) flow** — disturbances propagate both upstream and downstream; controls from downstream
- $Fr = 1$: **critical flow** — minimum specific energy for a given flow rate
- $Fr > 1$: **supercritical (rapid) flow** — disturbances only travel downstream; controls from upstream

**Specific energy:** $E = y + \frac{Q^2}{2gA^2}$ where $y$ is the flow depth.
For a given $Q$, minimum $E$ occurs at critical depth $y_c$ (where $Fr = 1$).

**Hydraulic jump:** An abrupt transition from supercritical to subcritical flow
(always increases depth, always dissipates energy). Sequent depths:

$$\frac{y_2}{y_1} = \frac{1}{2}\left(\sqrt{1+8Fr_1^2} - 1\right)$$

Energy loss: $\Delta E = (y_2-y_1)^3/4y_1y_2$. Used in spillway design to
dissipate kinetic energy before the downstream channel.

---

## 20.4 — Groundwater and Soil: The Diffusion Equation in CE

### 20.4.1 — Darcy's Law: Ohm's Law for Groundwater

For water flowing through a saturated porous medium (soil, rock):

$$q = -K\nabla h$$

where $q$ is the specific discharge (Darcy flux, [m/s]), $K$ is the hydraulic
conductivity [m/s], and $h$ is the hydraulic head $h = z + p/\gamma_w$.

`[STRUCTURAL CONNECTION]` — **same constitutive shape as Fick's law, different
derivation.** Fick's law (Ch. 13 §13.6) is a constitutive postulate. Darcy's law
was *measured*, not derived: Darcy's 1856 sand experiment produced a linear
relation between flux and head gradient, and the pore-scale justification —
drag balance on a grain, closed over an unresolved pore geometry — is a
different argument that arrives at the same algebraic form:

| | Fick's law | Darcy's law |
|---|---|---|
| Driving force | chemical potential gradient $\nabla\mu$ | hydraulic head gradient $\nabla h$ |
| Transport coefficient | diffusivity $D$ [m²/s] | hydraulic conductivity $K$ [m/s] |
| Driving variable | concentration | hydraulic head (length) |
| Status | constitutive postulate | empirical law, later rationalised |
| Fails when | activity coefficients matter | flow is turbulent, unsaturated, or reactive |

Note the dimensional asymmetry: $D$ carries the length that $K$ does not. That
single difference is why these are not the same equation and why
groundwater flow is *not* "Fick's law with different letters". What is shared
is the linear-gradient structure, which is why the same solvers, error-function
solutions, and network analogies reappear.

**Hydraulic conductivity values:**

| Material | $K$ (m/s) |
|---|---|
| Gravel | $10^{-2}$–$10^{-1}$ |
| Coarse sand | $10^{-4}$–$10^{-2}$ |
| Fine sand | $10^{-5}$–$10^{-4}$ |
| Silt | $10^{-7}$–$10^{-5}$ |
| Clay | $10^{-10}$–$10^{-7}$ |

**Groundwater flow equation** (confined, transient):
$$S\frac{\partial h}{\partial t} = T\nabla^2 h + W$$

where $S$ is the storage coefficient, $T = Kb$ is transmissivity, and $W$ is the
recharge rate. `[DERIVATION]` — given confined flow, constant $S$ and $T$, and
horizontal isotropic flow, this is the diffusion equation with $D = T/S$, so the
same error-function and well-function solutions apply. The identity is exact
*under those assumptions* and fails outside them: for unconfined flow
$h$ varies enough to matter in $T = Kb(h)$, and for unsaturated flow the
saturation-dependent Richards equation is nonlinear.

### 20.4.2 — Terzaghi's Consolidation: Settlement by Diffusion

When a saturated clay layer is loaded (by a building, embankment, or fill),
excess pore water pressure $u_e$ is generated. The clay consolidates (settles)
as water squeezes out under the excess pressure. Terzaghi's consolidation equation:

$$\boxed{\frac{\partial u_e}{\partial t} = c_v\frac{\partial^2 u_e}{\partial z^2}}$$

where $c_v = k(1+e_0)/\gamma_w m_v$ is the **coefficient of consolidation**
(hydraulic conductivity $k$, initial void ratio $e_0$, water unit weight $\gamma_w$,
volume compressibility $m_v$).

**This is the 1D diffusion equation from Ch. 16 §16.8 and Ch. 14 §14.8.**
The solution for a clay layer of thickness $H$ (drained top and bottom, so
drainage path $H_{dr} = H/2$), initially at uniform excess pressure $u_0$:

$$U(t) = 1 - \frac{8}{\pi^2}\sum_{n=0}^{\infty}\frac{1}{(2n+1)^2}\exp\!\left(-\frac{(2n+1)^2\pi^2 T_v}{4}\right)$$

where $U(t) = \Delta H/\Delta H_{final}$ is the **degree of consolidation** and
$T_v = c_v t/H_{dr}^2$ is the dimensionless time factor.

`[DERIVATION]` — **this is a mathematical identity, not an analogy.** The
Fourier-number series above, the step-load boundary condition, and the
$T_v \approx (\pi/4)U^2$ parabola are the *same* solutions as the slab
cooling problem of Ch. 14 §14.8, applied to a different field. Nothing is
being reinterpreted; only the name of the field changes.

| | Heat conduction (Ch. 14 §14.8) | Terzaghi consolidation |
|---|---|---|
| Field | temperature $T$ | excess pore pressure $u_e$ |
| Governing equation | $\partial T/\partial t = \alpha\,\partial^2 T/\partial z^2$ | $\partial u_e/\partial t = c_v\,\partial^2 u_e/\partial z^2$ |
| Transport coefficient | thermal diffusivity $\alpha$ | coefficient of consolidation $c_v$ |
| Step boundary condition | surface suddenly cooled | load suddenly applied |
| Solution | Fourier series in Fo | same series in $T_v$ |
| Early-time asymptote | $1 - \text{erf}(z/2\sqrt{\alpha t})$ | $U \approx (\pi/4)T_v$ |

**Model Ledger — load step to degree of consolidation**

| Field | Content |
|---|---|
| Parent theory | Poroelasticity: Terzaghi's one-dimensional consolidation theory |
| Reduction | Linear elastic soil skeleton + incompressible pore water + 1D flow + constant $c_v$ |
| Model | $\partial u_e/\partial t = c_v\,\partial^2 u_e/\partial z^2$ with step-load BCs |
| Assumptions | 1D; saturated; linear skeleton ($m_v$ constant); negligible self-weight; uniform $c_v$ |
| Physics retained | transient pore-pressure dissipation driving settlement |
| Physics neglected | lateral drainage, skeleton non-linearity, overconsolidation, secondary compression (creep), air entrapment |
| Validity | normally consolidated, single load increment, $U \lesssim 90\%$, drainage path well defined |
| Fails when | load is removed (swelling, not consolidation), $m_v$ varies with stress, or secondary compression dominates |
| Next model | nonlinear $m_v(\sigma')$; coupled 2D radial consolidation; creep superposition |

**Engineering application:** A 6 m clay layer ($c_v = 10^{-3}$ cm²/s, $H_{dr} = 3$ m)
achieves 90% consolidation at $T_v = 0.848$:
$$t_{90\%} = \frac{T_v H_{dr}^2}{c_v} = \frac{0.848\times(300\;\text{cm})^2}{10^{-3}\;\text{cm}^2/\text{s}} = 7.6\times 10^7\;\text{s} \approx 2.4\;\text{years}$$

Settlement continues for years — the engineer must design for long-term
deformation, not just immediate elastic deflection.

---

## 20.5 — Hydrology: Rainfall to Runoff

### 20.5.1 — The Rational Method

For small urban catchments, peak runoff:

$$Q_{peak} = CiA$$

where $C$ is the dimensionless runoff coefficient (0.1 for meadow, 0.95 for pavement),
$i$ is the rainfall intensity [m/s], and $A$ is the catchment area [m²].

**This is the lumped approximation** of the full hydrological balance — the
Bridge C operation applied to a catchment. The rational method assumes uniform
rainfall, uniform catchment response, and that the storm duration equals the
time of concentration $t_c$ (time for water from the farthest point to reach the outlet).

### 20.5.2 — Linear Systems Theory in Hydrology: Unit Hydrograph

The unit hydrograph $u(t)$ is the response of a catchment to a unit depth of
rainfall excess over unit time — exactly the **impulse response** (Green's function)
of the hydrological system.

For any rainfall excess pattern $r(t)$, the direct runoff hydrograph:

$$Q(t) = \int_0^t r(\tau)\,u(t-\tau)\,d\tau$$

This is a **convolution integral** — the same operation as a linear time-invariant
system in Ch. 18 §18.6.2. The hydrological system is treated as a linear filter
(provided watershed response is truly linear — an approximation that holds for
moderate rainfall events).

**Clark's method:** The unit hydrograph is modeled as a linear reservoir
(storage $S = KQ$) followed by a channel routing — exactly an RC system in the
hydraulic domain. The time-area method provides the input.

---

## 20.6 — Chemical Engineering: Mass and Energy Balances

### 20.6.1 — The Noether Foundation of Process Balances

Every process balance in ChE is a Noether conservation law (Ch. 1 §1.7) applied
to a control volume:

**Total mass balance** (Noether: particle number conservation):
$$\frac{dm_{sys}}{dt} = \sum\dot m_{in} - \sum\dot m_{out}$$

**Species mass balance** for component $A$ (with reaction):
$$\frac{dN_A}{dt} = \sum\dot N_{A,in} - \sum\dot N_{A,out} + r_A V$$

**Energy balance** (Noether: energy conservation, first law, Ch. 10):
$$\frac{dU_{sys}}{dt} = \dot Q - \dot W_s + \sum\dot m_{in}H_{in} - \sum\dot m_{out}H_{out}$$

where $H = U + pV/m = h$ is the specific enthalpy (the natural thermodynamic
potential for constant-pressure processes).

**The Kirchhoff analogy:** These balance equations at steady state are:
- Mass balance: $\sum\dot m_k = 0$ at every process node (KCL for mass)
- Energy balance: determines the enthalpy change (KVL for energy)

A process flow diagram is a bond graph in the chemical domain.

### 20.6.2 — Degrees of Freedom

For a process unit with $C$ components, $S$ streams, and $E$ equations:

$$DOF = S\times(C+1) - E - specifications$$

where the $+1$ accounts for the stream flow rate (in addition to $C-1$
mole fractions). A system with $DOF = 0$ is fully determined; $DOF > 0$
requires additional specifications (design variables).

This counting procedure is the chemical engineering analog of the Gibbs phase
rule (Ch. 10 §10.9.3) — both trace to the mathematical structure of simultaneous equations.

---

## 20.7 — Chemical Reaction Kinetics

### 20.7.1 — The Arrhenius Rate Constant: Boltzmann Factor at Work

The temperature dependence of a reaction rate constant:

$$k_{rxn}(T) = A\,e^{-E_a/RT}$$

**This is the Boltzmann factor from Ch. 10 §10.3.3.** The activation energy
$E_a$ is the energy barrier that reactant molecules must exceed to reach the
transition state. The fraction of molecules with enough energy is $e^{-E_a/k_BT}$
(from the Maxwell-Boltzmann distribution, Ch. 10 §10.8.2) — and this fraction
sets the reaction rate.

`[STRUCTURAL CONNECTION]` — **shared statistical origin, not a shared equation.**
Both exponentials come from the same place: the Boltzmann weight of a state at
energy $E$ relative to thermal energy $k_BT$. But they answer different
questions.

| | Boltzmann factor (Ch. 10) | Arrhenius factor (here) |
|---|---|---|
| Quantity | population ratio $n_E/n_0$ | rate constant $k(T)$ [1/s] |
| $E$ means | energy of a *state* | height of a *barrier* |
| Denominator | $k_BT$, per molecule | $RT$, per mole (hence the factor 1000) |
| What follows | equilibrium populations | a reaction rate, only after a mechanism is assumed |
| Needs a mechanism? | no | yes — the exponential is necessary, not sufficient |

The gap between the second and third rows is where mechanism lives. A rate
constant cannot be read off the Boltzmann factor; it is the Boltzmann factor
multiplied by a prefactor that encodes collision frequency, steric orientation,
entropy of activation, and — for a specific mechanism — the number of distinct
reaction routes. Two reactions with the same $E_a$ can differ in $k$ by orders
of magnitude.

Every thermally-activated process in engineering follows Arrhenius:
- Chemical reactions (this section)
- Solid-state diffusion (Ch. 14 §14.8.2: same formula!)
- Creep in metals (Ch. 19)
- Electrode reactions in batteries
- Crystal nucleation in processing

The pre-exponential $A$ encodes collision frequency and steric factors —
it comes from statistical mechanics (Ch. 10) and transition state theory.

**Model Ledger — Arrhenius fit to a reactor rate constant**

| Field | Content |
|---|---|
| Parent theory | Maxwell-Boltzmann energy distribution; transition state theory |
| Reduction | Single rate-limiting step, dilute collision-controlled regime, $E_a \gg k_BT$ |
| Model | $k(T) = A\exp(-E_a/RT)$, $A$ taken as $T$-independent |
| Assumptions | one mechanism dominates; $A$ constant over the fitted range; isothermal |
| Physics retained | thermal activation of a barrier |
| Physics neglected | entropy of activation, pressure dependence, non-Arrhenius curvature, falloff at high $T$, diffusion limitation |
| Validity | Arrhenius plot $ln\,k$ vs $1/T$ is linear over the fitted range |
| Fails when | plot curves (indicating a mechanism change or a diffusion-limited regime), or $A$ must vary with $T$ |
| Next model | modified Arrhenius / Eyring; explicit diffusion–reaction coupling |

### 20.7.2 — Rate Laws and Reaction Orders

For the reaction $A + B \to C$:

$$-r_A = k_{rxn}[A]^m[B]^n \quad\text{[mol/L·s]}$$

where $m$ and $n$ are the reaction orders (determined experimentally, not from
stoichiometry in general). The overall rate expression must be determined from
kinetic experiments — it is a Layer-2 constitutive relation, not derivable
from Layer-0 without a detailed molecular mechanism.

**Integrated rate laws** for simple cases:

| Order | $-r_A$ | $C_A(t)$ | Half-life $t_{1/2}$ |
|---|---|---|---|
| Zero | $k$ | $C_{A0} - kt$ | $C_{A0}/2k$ |
| First | $kC_A$ | $C_{A0}e^{-kt}$ | $\ln 2/k$ |
| Second | $kC_A^2$ | $1/(1/C_{A0}+kt)$ | $1/kC_{A0}$ |

First-order kinetics: same exponential decay as radioactive decay (Ch. 6 §6.10.3).
The nuclear decay rate constant $\lambda$ is the reaction rate constant for the
nuclear reaction — same Boltzmann physics, different energy scale.

---

## 20.8 — Reactor Design: CSTR and PFR

### 20.8.1 — The Three Ideal Reactor Types

**Batch reactor:** Closed, time-varying, perfectly mixed.
Design equation (species balance):

$$N_{A0}\frac{dX_A}{dt} = -r_A(X_A)\cdot V$$

where $X_A = (N_{A0}-N_A)/N_{A0}$ is the fractional conversion. At constant volume:

$$\frac{dC_A}{dt} = r_A(C_A) \quad\Longrightarrow\quad t = C_{A0}\int_0^{X_A}\frac{dX_A}{-r_A}$$

**CSTR (Continuous Stirred Tank Reactor):** Perfect mixing → uniform concentration
throughout the vessel = concentration at outlet.
Steady-state species balance (input − output + generation = 0):

$$\dot N_{A,in} - \dot N_{A,out} + r_A V = 0 \quad\Longrightarrow\quad F_{A0} - F_{A0}(1-X_A) + r_A V = 0$$

$$\boxed{V_{CSTR} = \frac{F_{A0}X_A}{-r_A(X_A)}}$$

The CSTR design equation is **algebraic** (not an ODE) because perfect mixing
eliminates spatial gradients. It is the lumped (Bridge C) version of the reactor
balance — one control volume, uniform conditions inside.

**PFR (Plug Flow Reactor):** No axial mixing; plug of fluid advances through the reactor.
Species balance over differential volume element $dV$:

$$\frac{dF_A}{dV} = r_A \quad\Longrightarrow\quad \boxed{V_{PFR} = F_{A0}\int_0^{X_A}\frac{dX_A}{-r_A(X_A)}}$$

The PFR design equation is an **integral** over conversion. The PFR is the
distributed-parameter version (Ch. 16: 1D convection-reaction PDE) of the CSTR lump.

### 20.8.2 — Comparing CSTR and PFR: The Levenspiel Plot

For a positive-order reaction ($-r_A$ decreasing with $X_A$), the Levenspiel plot
shows $1/(-r_A)$ vs. $X_A$:

- **PFR volume** = area under the curve from 0 to $X_A$
- **CSTR volume** = rectangle height $1/(-r_A)|_{X_{A,out}}$ × width $X_A$

Since $1/(-r_A)$ increases with $X_A$ (rate decreases as reactant depletes),
the rectangle is always larger than the area under the curve:

$$V_{CSTR} > V_{PFR} \quad\text{(for positive-order reactions at same conversion)}$$

**Engineering trade-off:**
- PFR: more efficient (less volume needed); harder to control; temperature
  gradients; sensitive to flow disturbances
- CSTR: easier control; well-suited for exothermic reactions (good heat removal);
  larger volume; cascades of CSTRs approach PFR performance

**Damköhler number:**
$$Da = \frac{\tau\cdot(-r_A)|_{X_A=0}}{C_{A0}} = \frac{\text{reaction rate}}{\text{convective rate}}$$

$Da \ll 1$: reaction is slow (conversion control by residence time)
$Da \gg 1$: reaction is fast (conversion control by equilibrium or transport)

---

## 20.9 — Separation Processes

### 20.9.1 — Distillation: Vapor-Liquid Equilibrium

Binary distillation separates two components with different volatilities.
The vapor-liquid equilibrium (VLE) relationship:

$$y_A = \frac{\alpha_{AB}x_A}{1+(\alpha_{AB}-1)x_A}$$

where $\alpha_{AB} = p_A^{sat}/p_B^{sat}$ is the **relative volatility** (ratio of
vapor pressures, both from the Clausius-Clapeyron equation, Ch. 10 §10.9.3).

**McCabe-Thiele method** (graphical design for a distillation column):

1. Plot VLE curve $y$ vs. $x$
2. Draw **rectifying operating line** (above feed):
   $y = (L/V)x + x_D(1 - L/V)$, slope = $L/V$ (internal reflux ratio)
3. Draw **stripping operating line** (below feed)
4. **Step off stages** between VLE curve and operating lines from the
   distillate composition $x_D$ to the bottoms composition $x_B$
5. Number of steps = number of theoretical stages

**Minimum reflux ratio** $R_{min}$: when the operating line passes through
a pinch point with the VLE curve — infinite stages needed.
**Actual reflux:** $R = 1.2$–$1.5\,R_{min}$ (practical trade-off: more reflux
= fewer stages = shorter column, but more energy).

### 20.9.2 — NTU-HTU Method: The Transfer Unit Approach

For continuous-contact equipment (packed columns for absorption, stripping,
liquid-liquid extraction), the number of theoretical stages is replaced by
**Transfer Units (NTU)** — the NTU concept used for heat exchangers
(Ch. 19 §19.6.3), applied here to a mass-transfer driving force. The
organisation of the method is shared; the equations are not (§20.9.2 below).

**NTU (gas-phase basis):**
$$NTU_{OG} = \int_{y_1}^{y_2}\frac{dy}{y^* - y}$$

where $y^*$ is the equilibrium gas-phase composition at the current liquid
composition, and $y$ is the actual gas composition.

**Height of a Transfer Unit (HTU):**
$$HTU_{OG} = \frac{G}{K_{ya}}$$

where $G$ is the gas molar flux, $K_y$ is the overall mass transfer coefficient,
and $a$ is the interfacial area per unit volume of packing.

**Packed column height:**
$$Z = NTU_{OG}\times HTU_{OG}$$

**The correspondence with heat exchangers:**
- Heat exchanger: $NTU = UA/C_{min}$, $\varepsilon = f(NTU, C_r)$
- Absorption column: $NTU_{OG} = K_{ya}Z/G$, efficiency $= f(NTU, mG/L)$
  where $mG/L$ plays the role of $C_r$

`[STRUCTURAL CONNECTION]` — **shared dimensionless design framework, not the
same equation.** What genuinely transfers is the *organising idea*: divide the
required driving-force change by the local driving force, count the number of
increments, multiply by the size of one increment. That is why the tabulated
$\varepsilon$–NTU curves and the "how many transfer units, how tall per unit"
workflow carry over intact.

What does **not** transfer, and is where a careless reading goes wrong:

| | Heat exchanger | Absorption column |
|---|---|---|
| Driving force | $\Delta T$ against a fixed $T_{h,\text{in}}$ | $y^* - y$ against a *moving* VLE equilibrium |
| Equilibrium | constant $T_h$ (single phase) | $y^* = f(x, T, P)$ — composition-dependent |
| Capacity rate | $C_{min}$ of one stream | $mG/L$ — a transformed, not identical, capacity |
| Transport coefficient | $U$ [W/m²K] | $K_{ya}$ [mol/m²s] — area *and* driving-force dependent |
| Failure mode | one side phase-changes | flooding, channeling, mass-transfer limitation |

Both are ultimately diffusive transport (Ch. 13 §13.10), but they are driven by
*different currents* with *different coefficients* against *different
equilibria*. The framework is shared; the equations are not interchangeable, and
the column's $K_{ya}$ cannot be measured with an NTU chart borrowed from a
heat-exchanger correlation.

**Model Ledger — packed column to NTU design**

| Field | Content |
|---|---|
| Parent theory | Two-film mass transfer (Ch. 13 §13.6, §20.10.1); countercurrent diffusion |
| Reduction | steady state; constant molar flow rates; linearised driving force; uniform packing |
| Model | $Z = NTU_{OG}\times HTU_{OG}$, $HTU_{OG} = G/K_{ya}$ |
| Assumptions | dilute solute; negligible pressure drop; constant $T,P$; no radial gradients; dilute-phase operation |
| Physics retained | composition-driven diffusion and the countercurrent gradient |
| Physics neglected | pressure drop, heat effects, non-dilute VLE curvature, channeling, flooding |
| Validity | $\varepsilon$ within the tabulated range; column below flooding limit |
| Fails when | flooding onset, $K_{ya}$ varies with composition, or heat effects shift $y^*$ |
| Next model | rigorous stagewise solve; non-isothermal VLE; packed-bed pressure-drop coupling |

---

## 20.10 — Mass Transfer: From Molecular to Engineering Scale

### 20.10.1 — Film Theory and Resistances

At a gas-liquid interface, the two-film theory assumes:
- Thin stagnant film on the gas side (thickness $\delta_G$)
- Thin stagnant film on the liquid side (thickness $\delta_L$)
- Equilibrium at the interface: $y_{Ai} = m\,x_{Ai}$ (Henry's law)

Fluxes through each film (Fick's law, Ch. 13):
$$N_A = k_G(y_A - y_{Ai}) = k_L(x_{Ai} - x_A)$$

where $k_G = D_{AG}/\delta_G$ and $k_L = D_{AL}/\delta_L$ are the individual
film coefficients.

**Overall resistance** (same logic as thermal resistances in series, Ch. 14 §14.7.2):

$$\frac{1}{K_G} = \frac{1}{k_G} + \frac{m}{k_L}$$

where $m$ is the Henry's law constant (equilibrium slope). This is the two-resistance
model in series. The **algebra** is identical to the overall heat transfer
coefficient of Ch. 19 §19.6.1 — $1/U = 1/h_1 + R_{wall} + 1/h_2$ — because series
addition of resistances is one piece of algebra. The **resistances** are not the
same physical quantities: $k_G$ and $k_L$ are mass-transfer coefficients set by
molecular diffusivity, whereas $h$ is set by convection, and $m$ is an
equilibrium slope that has no thermal counterpart. `[STRUCTURAL CONNECTION]`.

**The chemical potential** $\mu$ is the effort variable for mass transfer —
diffusion runs from high $\mu$ to low $\mu$, in the same sense as heat flows from
high $T$ to low $T$. `[ANALOGY]`: the two effort variables are not
interchangeable, and the driving force is $-\nabla\mu$ rather than $-k\nabla T$.
In the ideal case, $\Delta\mu = RT\ln(y/y^*)$
is the driving force for absorption.

### 20.10.2 — Dimensionless Groups for Mass Transfer

| Dimensionless group | Formula | Analog in heat transfer |
|---|---|---|
| Schmidt number $Sc$ | $\nu/D_{AB}$ (momentum/mass diffusivity) | Prandtl number $Pr = \nu/\alpha$ |
| Sherwood number $Sh$ | $k_m L/D_{AB}$ (convective/diffusive mass transfer) | Nusselt number $Nu = hL/\kappa$ |
| Mass transfer coefficient | $k_m = Sh\cdot D_{AB}/L$ | $h = Nu\cdot\kappa/L$ |

**Chilton-Colburn analogy:** For turbulent flow over a flat plate:

$$j_D = j_H = f/2$$

where $j_D = Sh/Re\cdot Sc^{1/3}$, $j_H = Nu/Re\cdot Pr^{1/3}$, and $f$ is
the friction factor. Heat and mass transfer have equal efficiency when
$Pr \approx Sc$ — which occurs for gases ($Pr \approx Sc \approx 0.7$).
Liquids differ ($Pr \gg Sc$ for most organic solvents).

---

## 20.11 — Coupled CE-ChE Systems: Multi-Physics at Layer 3

### 20.11.1 — Wastewater Treatment as a Multi-Domain Network

A wastewater treatment plant couples:
- **Hydraulic domain** (flow between unit processes): pipe network (§20.3)
- **Chemical domain** (biological oxygen demand, nutrient removal): CSTR kinetics (§20.8)
- **Mass transfer** (oxygen transfer to activated sludge): film theory (§20.10)
- **Thermal domain** (temperature affects microbial activity via Arrhenius, §20.7)

The entire plant is a **bond graph** (Ch. 17 §17.5) in the hydraulic + chemical
domains, with energy flows connecting to the thermal domain. The Arrhenius
coupling means this is a nonlinear system — temperature changes affect kinetics,
which affects oxygen demand, which affects aeration energy, which affects temperature.

### 20.11.2 — The Reactor-Separator Network

Many chemical processes alternate between reaction (CSTR or PFR) and separation
(distillation column). The recycle of unconverted reactant creates a **closed loop**:

```
Feed → [Reactor] → [Separator] → Product
         ↑               ↓
         └── Recycle ────┘
```

The recycle creates positive feedback (higher conversion per pass → more product
in separator → more recycle → higher reactor inlet concentration → ...).
This is analyzed using the same closed-loop transfer function as Ch. 21 control theory:

$$X_{overall} = \frac{X_{pass}}{1 - R(1-X_{pass})}$$

where $R$ is the recycle ratio and $X_{pass}$ is the single-pass conversion.
The same feedback algebra (Ch. 21 preview) governs both feedback control systems
and chemical recycle loops.

---

## 20.12 — Where CE/ChE Layer 3 Fails

| Failure mode | Physical cause | Required model | Return to |
|---|---|---|---|
| Soil liquefaction | Dynamic loading, loss of pore pressure | Nonlinear soil dynamics, wave propagation | Ch. 15, 16 |
| Turbulent open channels | $Re \gg 1$, no laminar model | CFD (RANS, LES) | Ch. 15 §15.8 |
| Non-ideal CSTR (RTD) | Bypassing, dead zones | Residence time distribution analysis | Ch. 16 (dispersion PDE) |
| Reactive distillation | Reaction + separation coupled | Rate-based simulation | Ch. 10, 13, 14 |
| Membrane transport | Non-Fickian at high pressure | Solution-diffusion model | Ch. 13 §13.6 |
| Non-equilibrium separation | Stage efficiency $<$ 1 | Mass transfer rate model | Ch. 20 §20.10 |
| Large deflection structures | Geometric nonlinearity | Nonlinear FEM | Ch. 15 |
| Seismic structural response | Dynamic wave propagation | Time-history analysis (FEM + Ch. 16) | Ch. 16 |

---

## 20.13 — Summary

| Domain | Effort | Flow | R | C | L | Conservation law |
|---|---|---|---|---|---|---|
| CE Structural | Force $F$ | Velocity $v$ | Damping $b$ | Compliance $1/k$ | Mass $m$ | Newton's 2nd law |
| CE Hydraulic (pipe) | Pressure $P$ | Flow $Q$ | $8\mu L/\pi r^4$ | Compressibility | Inertance $\rho L/A$ | Mass conservation |
| CE Open channel | Head $H$ | Flow $Q$ | Manning resistance | — | — | Continuity |
| CE Groundwater | Head $h$ | Flux $q$ | $1/K$ | Storativity $S/T$ | — | Darcy + continuity |
| ChE Chemical | Chem. potential $\mu$ | Molar flow $\dot n$ | Diffusion resistance | Tank capacity | — | Mole balance |

**Key PDEs that appear literally in CE/ChE Layer 3:**

| PDE | CE/ChE appearance | Chapter origin | Kind |
|---|---|---|---|
| Diffusion $\partial_t u = c_v\,\partial_{xx}u$ | Terzaghi consolidation (clay settlement) | Ch. 13, 16 | mathematical identity |
| Diffusion $\partial_t h = (T/S)\nabla^2 h$ | Groundwater (confined, transient) | Ch. 13, 16 | mathematical identity, under stated storage assumptions |
| Beam equation $EI\,\partial_{xxxx}w = q$ | Euler-Bernoulli beam deflection | Ch. 16 §16.7.2 | mathematical identity |
| Advection–reaction $\partial_V F_A = r_A$ | PFR design equation | Ch. 16 | mathematical identity |
| Linear gradient law $q = -K\nabla h$ | Darcy's law | Ch. 13 §13.6 | constitutive correspondence |
| $k = A\,e^{-E_a/RT}$ | Arrhenius kinetics | Ch. 10 §10.3.3 | shared statistical origin |
| $Z = NTU\times HTU$ | Packed-column design | Ch. 19 §19.6.3 | shared dimensionless framework |

Only the first four rows earn the word "identical" — and each one earns it
conditionally, on the assumptions named in its own section. The last three rows
are the ones that get over-claimed in textbooks, and they are the ones this
chapter now labels explicitly (§20.0.1).

---

## 20.14 — Engineering Thread

| Physics | Engineering application |
|---|---|
| Stiffness method $\mathbf{K}\mathbf{u}=\mathbf{F}$ | Structural analysis of buildings, bridges, towers (SAP2000, ETABS) |
| Beam bending $\sigma = My/I$ | Member sizing; serviceability deflection checks; composite slab design |
| Manning's equation | River flood routing; culvert design; storm drain sizing |
| Hydraulic jump | Spillway energy dissipator design; canal protection |
| Darcy's law | Groundwater contamination; dewatering systems; dam seepage |
| Terzaghi consolidation | Foundation settlement prediction; construction scheduling for embankments |
| Rational method + unit hydrograph | Stormwater management; culvert design; detention basin sizing |
| Arrhenius rate constant | Reaction temperature control; catalyst selection; reactor sizing |
| CSTR/PFR design equation | Reactor volume sizing; conversion optimization; operating conditions |
| NTU-HTU for columns | Packed absorption tower height; distillation column design |
| Two-resistance model $1/K_G$ | Gas scrubber design; oxygen transfer in bioreactors |
| Chilton-Colburn analogy | Mass transfer prediction from heat transfer data |

---

## 20.15 — Looking Ahead

Chapter 20 completes the Layer-3 engineering coverage across all four branches.
The inventory of what Layer-3 models are available:

- **EEE (Ch. 18):** Circuits, semiconductor devices, signals, power electronics
- **ME (Ch. 19):** Machines, vibrations, thermodynamic cycles, heat exchangers, fluid systems
- **CE (Ch. 20):** Structural analysis, open-channel hydraulics, groundwater, soil settlement
- **ChE (Ch. 20):** Process balances, reaction kinetics, reactor design, separations, mass transfer

**Chapter 21** closes the book with the capstone: **feedback and control**.
For any system that admits an appropriate linear time-invariant
representation, control theory operates at the level of the transfer function
$H(s)$ — above all physical domains simultaneously. A PID controller does not
know whether it is controlling temperature, position, flow rate, or pH; it sees
the error signal and the process transfer function, and nothing about the
underlying physics. That claim is bounded, and Chapter 21 §21.0.2 is explicit
about the bound: nonlinear, time-varying, hybrid, distributed, stochastic, and
delayed systems are not described by one $H(s)$, and each needs a different
representation before the same design machinery applies. Chapter 21 brings
everything from the layer map into a unified closing argument for the book's
central claim: physics, in the right limits, becomes engineering.

---

*End of Chapter 20.*

---
*Next: Chapter 21 — Feedback, Control, and the Cross-Branch Capstone*
