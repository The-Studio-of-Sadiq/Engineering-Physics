# Bridge B.d — From General Relativity to Newton's Law of Gravitation

### How Spacetime Curvature Becomes an Inverse-Square Force

---

> _Before Einstein, space was just the stage on which physics happened._ _After Einstein, space became a participant. It curves. It waves._ _And in the limit where nothing moves fast and everything is weak,_ _it pretends to be Newton's force._ — paraphrased from Misner, Thorne, Wheeler, _Gravitation_

---

## 8.0 — Bridge B.d in Context

Chapters 3–7 descended through Layer 1: quantum mechanics from the Standard Model Lagrangian. Bridge B now takes us from Layer 1 to Layer 2 — the classical continuum world.

Bridge B is not one transition but five simultaneous limiting operations (from the layer map, Ch. 1 §1.9):

|Bridge|Limit|Produces|Chapter|
|---|---|---|---|
|**B.d**|Weak field + slow motion + static|Newton's gravity|**8 (this chapter)**|
|B.a|$\hbar\to 0$|Classical mechanics|9|
|B.b|$N\to\infty$, ensemble average|Thermodynamics|10|
|B.c|Classical U(1) field limit|Maxwell's equations|11|
|B.e|Kubo + quantum scattering|Generalized transport law|13|

This chapter extracts the gravitational sector from Ch. 0's action:

$$S_{EH} = \frac{1}{16\pi G}\int d^4x,\sqrt{-g},R$$

The destination is Newton's law $F = -GMm/r^2$ — but we will pass through general relativity properly, collecting every correction that engineering currently cares about along the way.

---

## 8.1 — The Starting Point: Einstein Field Equations

From Ch. 0 §0.3: varying $S_{EH}$ with respect to the inverse metric $g^{\mu\nu}$ gives the **Einstein field equations** (in SI units):

$$\boxed{G_{\mu\nu} \equiv R_{\mu\nu} - \frac{1}{2}g_{\mu\nu}R = \frac{8\pi G}{c^4},T_{\mu\nu}}$$

Everything in this equation has appeared before, but let us restate it clearly:

**Left side — geometry:**

- $g_{\mu\nu}$: the metric tensor — the dynamical field of gravity, encoding distances and angles in curved spacetime
- $R_{\mu\nu}$: the Ricci tensor — a contraction of the Riemann curvature tensor, measuring how much parallel transport around a loop rotates a vector
- $R = g^{\mu\nu}R_{\mu\nu}$: the Ricci scalar — a single number at each point measuring the total local curvature
- $G_{\mu\nu}$: the Einstein tensor — the unique symmetric, divergence-free ($\nabla^\mu G_{\mu\nu} = 0$), second-order combination of the metric

**Right side — matter:**

- $T_{\mu\nu}$: the stress-energy tensor — the Noether current of spacetime translations (Ch. 1 §1.9.3), encoding:
    - $T^{00} = $ energy density (including rest mass energy $\rho c^2$)
    - $T^{0i} = $ momentum density (energy flux)
    - $T^{ij} = $ stress tensor (pressure and shear)

**The equation in words:**

> Spacetime curvature = $\dfrac{8\pi G}{c^4}\times$ energy-momentum content

The factor $8\pi G/c^4 \approx 2.07\times 10^{-43}$ m/J is extraordinarily small — this is why you need planetary masses to produce measurable curvature.

---

## 8.2 — The Weak-Field Expansion

### 8.2.1 — The Perturbation

For weak gravitational fields (everywhere in the solar system, in every engineering context except near black holes), the metric is nearly flat:

$$g_{\mu\nu} = \eta_{\mu\nu} + h_{\mu\nu}, \qquad |h_{\mu\nu}| \ll 1$$

where $\eta_{\mu\nu} = \text{diag}(-1,+1,+1,+1)$ is the flat Minkowski metric and $h_{\mu\nu}$ is a small perturbation. We work to **first order in $h_{\mu\nu}$**.

**Quantitative justification:**

| Environment | $|h_{00}| = 2|\Phi|/c^2$ | Where | |---|---|---| | Earth's surface | $1.4\times 10^{-9}$ | Engineering on Earth | | GPS satellite orbit | $3.3\times 10^{-10}$ | GPS receivers | | Solar surface | $4.2\times 10^{-6}$ | Solar physics | | Neutron star surface | $\sim 0.3$ | Not weak! GR required exactly | | Black hole horizon | $\sim 1$ | Full GR, no perturbation theory |

The perturbative treatment is valid for everything from a laboratory balance to the GPS network to gravitational wave emission from neutron star binaries in their inspiral phase.

### 8.2.2 — Linearized Ricci Tensor

Expanding the Christoffel symbols to first order in $h$:

$$\Gamma^\rho_{\mu\nu} = \frac{1}{2}\eta^{\rho\sigma}\left(\partial_\mu h_{\nu\sigma} + \partial_\nu h_{\mu\sigma} - \partial_\sigma h_{\mu\nu}\right) + \mathcal{O}(h^2)$$

The linearized Ricci tensor:

$$R_{\mu\nu}^{(1)} = \frac{1}{2}\left(-\Box h_{\mu\nu} - \partial_\mu\partial_\nu h + \partial^\rho\partial_\mu h_{\nu\rho} + \partial^\rho\partial_\nu h_{\mu\rho}\right)$$

where $\Box = -\partial_t^2/c^2 + \nabla^2$ is the d'Alembertian and $h = \eta^{\mu\nu}h_{\mu\nu}$ is the trace.

### 8.2.3 — Lorenz Gauge and the Trace-Reversed Perturbation

Define the **trace-reversed perturbation**:

$$\bar h_{\mu\nu} = h_{\mu\nu} - \frac{1}{2}\eta_{\mu\nu}h$$

In the **Lorenz gauge** (the gravitational analog of the electromagnetic Lorenz gauge $\partial^\mu A_\mu = 0$):

$$\partial^\mu\bar h_{\mu\nu} = 0$$

the linearized Einstein equations simplify dramatically to:

$$\boxed{\Box\bar h_{\mu\nu} = -\frac{16\pi G}{c^4},T_{\mu\nu}}$$

This is a set of ten wave equations — one for each independent component of $\bar h_{\mu\nu}$. The source is the stress-energy tensor; the retarded solution is a superposition of gravitational waves propagating at $c$.

---

## 8.3 — The Newtonian Limit: Three Conditions

To recover Newton's law, apply three simultaneous limits:

### Condition 1: Slow Motion ($v \ll c$)

The stress-energy tensor for a pressureless dust of density $\rho$ and velocity $\mathbf{v}$:

$$T^{\mu\nu} = \rho c^2 u^\mu u^\nu$$

where $u^\mu = \gamma(c, \mathbf{v})$ is the four-velocity. For $v \ll c$: $\gamma \approx 1$, and:

$$T^{00} \approx \rho c^2 \gg T^{0i} \approx \rho c v^i \gg T^{ij} \approx \rho v^i v^j$$

Only $T^{00} = \rho c^2$ is significant. All spatial components of $T_{\mu\nu}$ are negligible.

### Condition 2: Weak Field ($|h_{\mu\nu}| \ll 1$)

Already imposed in §8.2. The linearized equations are valid.

### Condition 3: Static Field ($\partial_t h_{\mu\nu} \approx 0$)

For a slowly-varying source ($v \ll c$, quasi-static), time derivatives of $\bar h_{\mu\nu}$ are negligible compared to spatial derivatives: $\Box \approx \nabla^2$.

### 8.3.1 — The Poisson Equation

With all three conditions, the $(\mu,\nu) = (0,0)$ component of $\Box\bar h_{\mu\nu} = -16\pi G T_{\mu\nu}/c^4$ becomes:

$$\nabla^2\bar h_{00} = -\frac{16\pi G}{c^4}\cdot\rho c^2 = -\frac{16\pi G\rho}{c^2}$$

From the gauge conditions and slow-motion limit: $\bar h_{00} = -4\Phi/c^2$ where $\Phi$ is to be determined, and all other $\bar h_{\mu\nu} \approx 0$.

Substituting:

$$\boxed{\nabla^2\Phi = 4\pi G\rho}$$

This is **Poisson's equation for the Newtonian gravitational potential** — the exact equation Newton would have written.

For a point mass $M$ at the origin ($\rho = M\delta^3(\mathbf{r})$):

$$\nabla^2\Phi = 4\pi G M\delta^3(\mathbf{r}) \quad\Longrightarrow\quad \Phi(r) = -\frac{GM}{r}$$

### 8.3.2 — Newton's Law from the Geodesic Equation

The geodesic equation (the equation of motion for a freely falling particle in curved spacetime):

$$\frac{d^2x^\mu}{d\tau^2} + \Gamma^\mu_{\nu\rho}\frac{dx^\nu}{d\tau}\frac{dx^\rho}{d\tau} = 0$$

For slow motion ($dx^i/d\tau \approx v^i \ll c$, $dx^0/d\tau \approx c$):

$$\frac{d^2x^i}{dt^2} \approx -c^2\Gamma^i_{00} = -c^2\cdot\frac{1}{2}\eta^{ij}\partial_j h_{00} = -\partial_i\Phi$$

Therefore:

$$\boxed{\mathbf{a} = -\nabla\Phi \quad\Longrightarrow\quad \mathbf{F} = m\mathbf{a} = -\frac{GMm}{r^2}\hat r}$$

**Newton's law of gravitation is the geodesic equation in the weak-field, slow-motion, static limit of general relativity.**

The key insight: there is no gravitational _force_ in GR. A freely falling particle follows a **geodesic** — the straightest possible path in curved spacetime. What appears as a gravitational force to an accelerating observer (standing on the ground) is the Christoffel symbol term — the correction from the curvature of spacetime.

---

## 8.4 — The Metric in the Newtonian Limit

The full spacetime metric in the Newtonian limit (with $\Phi/c^2 \ll 1$):

$$\boxed{ds^2 = -\left(1 + \frac{2\Phi}{c^2}\right)c^2,dt^2 + \left(1 - \frac{2\Phi}{c^2}\right)\left(dx^2 + dy^2 + dz^2\right)}$$

This is the **linearized Schwarzschild metric** — valid wherever $|\Phi|/c^2 \ll 1$.

**Physical consequences read directly from the metric:**

### 8.4.1 — Gravitational Time Dilation

For a clock at rest ($d\mathbf{x} = 0$), the proper time interval:

$$d\tau = \sqrt{-g_{00}/c^2},dt = \sqrt{1 + \frac{2\Phi}{c^2}},dt \approx \left(1 + \frac{\Phi}{c^2}\right)dt$$

A clock deeper in a gravitational well ($\Phi$ more negative) ticks more slowly relative to coordinate time. The fractional rate difference between clocks at potentials $\Phi_1$ and $\Phi_2$:

$$\frac{\Delta\tau_1 - \Delta\tau_2}{\Delta\tau_2} = \frac{\Phi_1 - \Phi_2}{c^2} = \frac{\Delta\Phi}{c^2}$$

### 8.4.2 — Gravitational Redshift

A photon emitted at potential $\Phi_e$ and received at $\Phi_r > \Phi_e$:

$$\frac{\nu_r}{\nu_e} = \sqrt{\frac{1 + 2\Phi_e/c^2}{1 + 2\Phi_r/c^2}} \approx 1 + \frac{\Phi_e - \Phi_r}{c^2} = 1 - \frac{|\Delta\Phi|}{c^2}$$

The photon climbing out of the gravitational well loses energy and redshifts. **Pound and Rebka (1959)** verified this at Harvard, measuring the redshift of $^{57}$Fe gamma rays falling 22.5 m: $\Delta\nu/\nu = -2.5\times 10^{-15}$, confirmed to 1%.

---

## 8.5 — The Schwarzschild Solution: Gravity of a Spherical Mass

For a static, spherically symmetric mass $M$ (the Sun, Earth, a star), the exact solution to the Einstein equations is the **Schwarzschild metric** (Schwarzschild, 1916):

$$\boxed{ds^2 = -\left(1 - \frac{r_s}{r}\right)c^2,dt^2 + \frac{dr^2}{1 - r_s/r} + r^2,d\Omega^2}$$

where $d\Omega^2 = d\theta^2 + \sin^2\theta,d\phi^2$ and the **Schwarzschild radius**:

$$r_s = \frac{2GM}{c^2}$$

|Object|Mass $M$|Schwarzschild radius $r_s$|Actual radius|
|---|---|---|---|
|Earth|$5.97\times 10^{24}$ kg|8.87 mm|6371 km|
|Sun|$1.99\times 10^{30}$ kg|2.95 km|696,000 km|
|MW central BH (Sgr A*)|$4\times 10^6 M_\odot$|$1.2\times 10^7$ km|$\approx r_s$|
|GW150914 final BH|$62 M_\odot$|183 km|$\approx r_s$|

For Earth and the Sun: the actual radius is enormously larger than $r_s$, so we are always in the $r \gg r_s$ regime — the Newtonian limit applies.

### 8.5.1 — Gravitational Time Dilation from Schwarzschild

$$\frac{d\tau}{dt} = \sqrt{1 - \frac{r_s}{r}} \approx 1 - \frac{GM}{rc^2}$$

A clock at radius $r$ runs slow compared to a clock at infinity by factor $\sqrt{1 - r_s/r}$. At Earth's surface ($r = R_\oplus = 6.371\times 10^6$ m):

$$\frac{d\tau_{surface}}{dt} = 1 - \frac{GM_\oplus}{R_\oplus c^2} = 1 - 6.95\times 10^{-10}$$

The surface clock loses $60.1;\mu$s per day relative to a clock at infinity.

### 8.5.2 — Circular Orbits and Orbital Velocity

The geodesic equation for a circular orbit at radius $r$ gives:

$$v_{orbit} = \sqrt{\frac{GM}{r}}$$

This is identical to the Newtonian result — circular orbits at $r \gg r_s$ are indistinguishable from Newtonian ones to leading order.

The orbital period: $T = 2\pi r/v_{orbit} = 2\pi\sqrt{r^3/GM}$ (Kepler's third law).

---

## 8.6 — Gravitational Waves

### 8.6.1 — Propagating Solutions

In vacuum ($T_{\mu\nu} = 0$), the linearized equations reduce to:

$$\Box\bar h_{\mu\nu} = 0$$

This has wave solutions propagating at $c$. In the **transverse-traceless (TT) gauge** (imposing both $\partial^\mu\bar h_{\mu\nu} = 0$ and $\bar h = 0$ and choosing the wave propagating in the $z$-direction), only two independent components survive:

$$h_{\mu\nu}^{TT} = \begin{pmatrix}0&0&0&0\0&h_+&h_\times&0\0&h_\times&-h_+&0\0&0&0&0\end{pmatrix}\cos(\omega t - kz)$$

**The plus polarization** ($h_+$): stretches space in $x$, compresses in $y$ simultaneously, then reverses. Ring of test particles: oscillates between $\bigcirc\to\Rightarrow\to\bigcirc\to\Uparrow\to\bigcirc$.

**The cross polarization** ($h_\times$): same as $h_+$ but rotated 45°.

Gravitational waves have exactly 2 independent polarizations — as predicted for a massless spin-2 field. (Compare: photons have 2 polarizations for a massless spin-1 field.)

### 8.6.2 — The Quadrupole Formula

A gravitational wave is generated by any mass distribution with a time-varying quadrupole moment:

$$I_{ij}(t) = \int\rho(\mathbf{r},t)\left(x_i x_j - \frac{1}{3}\delta_{ij}r^2\right)d^3r$$

The power radiated:

$$P = -\frac{G}{5c^5}\left\langle\dddot I_{ij}\dddot I^{ij}\right\rangle$$

**A spherically symmetric pulsation emits no gravitational waves** — $I_{ij} = 0$. A uniformly rotating perfect sphere emits no GWs. You need asymmetry: binary stars, merging black holes, rotating neutron stars with bumps.

### 8.6.3 — LIGO and the First Detection

GW150914 (14 September 2015): merger of two black holes of masses $36 M_\odot$ and $29 M_\odot$ at $d \approx 1.3$ billion light-years.

The measured strain: $$h = \frac{\Delta L}{L} \approx 10^{-21}$$

For LIGO's 4 km arm: $\Delta L \approx 4\times 10^{-18}$ m — one-thousandth the diameter of a proton.

**Why LIGO can measure this:** The Michelson interferometer measures the differential phase shift between two arms perpendicular to each other. A GW with + polarization stretches one arm and compresses the other — doubling the phase difference. With 300 kW of laser power recycled in the 4 km arms, shot noise and thermal noise can be controlled below the gravitational wave signal.

The engineering: LIGO is the most sensitive instrument ever built. Its suspension systems achieve seismic isolation of $10^{-12}$ at 100 Hz. Its mirror coatings have thermal noise levels of $10^{-20}$ m/$\sqrt{\text{Hz}}$. Layer-2 classical physics (interferometry, noise analysis) serves a Layer-0 measurement.

---

## 8.7 — Post-Newtonian Corrections: Where GR Matters in the Solar System

The expansion of GR beyond leading-order Newtonian gravity gives **post-Newtonian (PN) corrections** of order $(v/c)^2$ and $\Phi/c^2$. These are small but measurable.

### 8.7.1 — Perihelion Precession of Mercury

The Newtonian orbit of a planet around the Sun is a closed ellipse (Kepler). In GR, there is an additional term in the effective potential:

$$V_{eff}(r) = -\frac{GM}{r} - \frac{L^2}{2m^2r^2} + \underbrace{\frac{GML^2}{m^2c^2r^3}}_{\text{GR correction}}$$

This causes the ellipse to **precess** — the perihelion advances by:

$$\Delta\phi_{per;orbit} = \frac{6\pi GM}{a(1-e^2)c^2}$$

For Mercury: $a = 5.79\times 10^{10}$ m, $e = 0.206$: $$\Delta\phi = \frac{6\pi\times(6.67\times10^{-11})(1.99\times10^{30})}{(5.79\times10^{10})(1-0.206^2)(9\times10^{16})} = 5.02\times 10^{-7};\text{rad/orbit}$$

Mercury completes 415 orbits per century: $\Delta\phi_{century} = 2.08\times 10^{-4}$ rad/century $= 43.0''$/century.

This matches the observed anomalous precession of Mercury (after accounting for perturbations from other planets) to better than 0.1% — one of the first and most famous confirmations of GR.

### 8.7.2 — Gravitational Deflection of Light

A photon passing a massive body at impact parameter $b$ is deflected by:

$$\alpha = \frac{4GM}{bc^2}$$

This is **twice the Newtonian prediction** ($2GM/bc^2$) because in GR both the temporal and spatial components of the metric are perturbed — light is deflected by time curvature AND space curvature equally, whereas Newton's law only captures the time-curvature analog.

For light grazing the Sun ($b = R_\odot$): $$\alpha = \frac{4\times(6.67\times10^{-11})\times(1.99\times10^{30})}{(6.96\times10^8)\times(9\times10^{16})} = 8.48\times10^{-6};\text{rad} = 1.75''$$

Eddington's 1919 expedition to measure stellar positions during a solar eclipse confirmed $\alpha = 1.75'' \pm 0.09''$ — the first empirical test of GR and the observation that made Einstein world-famous.

Modern measurements (Very Long Baseline Interferometry, VLBI) confirm the prediction to $10^{-4}$ precision.

### 8.7.3 — Frame Dragging: The Lense-Thirring Effect

A rotating mass ($M$, angular momentum $J$) drags spacetime around it, adding an off-diagonal term to the metric:

$$g_{0i} = -\frac{2G}{c^3r^3}\epsilon_{ijk}J^j x^k$$

A gyroscope in orbit around Earth precesses at the Lense-Thirring rate:

$$\boldsymbol{\Omega}_{LT} = \frac{G}{c^2r^3}\left[3(\mathbf{J}\cdot\hat r)\hat r - \mathbf{J}\right]$$

For a circular polar orbit at $r = R_\oplus + h$: $\Omega_{LT} \approx 39$ mas/yr (milli-arcseconds per year).

**Gravity Probe B** (Stanford / NASA, 2004–2011): Four cryogenic gyroscopes in polar orbit at 642 km altitude. Measured:

- Geodetic precession (mass-only, from $g_{00}$ and $g_{ij}$ terms): 6606 mas/yr (predicted 6606.1 mas/yr) ✓
- Lense-Thirring (from $g_{0i}$ terms): 37.2 mas/yr (predicted 39.2 mas/yr) ✓ (to 15%)

---

## 8.8 — GPS: General Relativity in an Engineering System

GPS is the most commercially important application of general relativity. The calculation below is a worked example of the theory in this chapter applied to a real engineering system.

### 8.8.1 — GPS Orbital Parameters

- Orbital altitude: $h = 20{,}200$ km above Earth's surface
- Orbital radius: $r_{sat} = R_\oplus + h = 2.659\times 10^7$ m
- Orbital velocity: $v_{sat} = \sqrt{GM_\oplus/r_{sat}} = 3.87$ km/s

### 8.8.2 — Gravitational Time Dilation (GR Effect)

Clock rate relative to infinity (from §8.5.1): $$\frac{d\tau}{dt}\bigg|_{surface} = 1 - \frac{GM_\oplus}{R_\oplus c^2} = 1 - 6.95\times10^{-10}$$ $$\frac{d\tau}{dt}\bigg|_{satellite} = 1 - \frac{GM_\oplus}{r_{sat} c^2} = 1 - 1.66\times10^{-10}$$

Satellite clock runs faster than surface clock due to weaker gravity by: $$\Delta\frac{d\tau}{dt}\bigg|_{GR} = (6.95 - 1.66)\times10^{-10} = 5.29\times10^{-10}$$

Per day: $5.29\times10^{-10}\times 86{,}400;\text{s} = +45.7;\mu\text{s/day}$ (satellite runs fast)

### 8.8.3 — Velocity Time Dilation (Special Relativity Effect)

From SR (time dilation due to velocity): $$\frac{d\tau}{dt}\bigg|_{SR} = \sqrt{1 - \frac{v_{sat}^2}{c^2}} \approx 1 - \frac{v_{sat}^2}{2c^2} = 1 - 8.32\times10^{-11}$$

Per day: $-8.32\times10^{-11}\times 86{,}400;\text{s} = -7.2;\mu\text{s/day}$ (satellite runs slow)

### 8.8.4 — Net Correction

$$\Delta t_{net} = +45.7 - 7.2 = +38.5;\mu\text{s/day}$$

The satellite clock runs fast by 38.5 μs/day. Since GPS positioning requires timing accuracy $\delta t < 20$ ns for $\delta x < 6$ m accuracy, and the uncorrected error would be $38{,}500$ ns/day:

$$\delta x_{uncorrected} \approx c\times 38.5;\mu\text{s} \approx 11.5;\text{km/day}$$

**Without the GR and SR corrections, GPS would accumulate 11.5 km of positional error per day.** The correction is implemented by pre-adjusting the satellite clock frequency before launch:

$$f_{corrected} = f_0 \times \left(1 - \frac{38.5\times10^{-6}}{86{,}400}\right) = f_0\times\left(1 - 4.46\times10^{-10}\right)$$

The satellite clock is made to tick slightly slow before launch ($f$ reduced by $4.46\times10^{-10}$), so that after it reaches orbit and both relativistic effects apply, it ticks at the correct rate relative to ground clocks.

**This is GR in commercial engineering practice, used by every smartphone, aircraft, and ship navigation system on Earth.**

---

## 8.9 — The Validity Criterion: When to Use GR vs. Newton

The weak-field expansion is valid when $r_s/r \ll 1$ and $v \ll c$. More precisely:

$$\text{GR correction} \sim \frac{v^2}{c^2} \sim \frac{r_s}{r} = \frac{2GM}{rc^2}$$

|Context|$r_s/r$|GR correction needed?|
|---|---|---|
|Civil engineering on Earth|$\sim 10^{-9}$|Never (except GPS receivers)|
|GPS satellite orbit|$\sim 10^{-9}$|Yes — 38 μs/day matters|
|Mercury's orbit|$\sim 10^{-8}$|Yes — 43''/century|
|Solar corona|$\sim 10^{-6}$|Yes — light deflection|
|White dwarf surface|$\sim 10^{-4}$|Yes — spectral line shifts|
|Neutron star surface|$\sim 0.3$|Full GR|
|Black hole horizon|$= 1$|Full GR (beyond perturbation theory)|

The rule of thumb: **Newton's law is sufficient when $GM/rc^2 \ll 1$ and $v \ll c$**. For engineering on Earth or in near-Earth orbit, the only GR correction that matters in practice is the gravitational time dilation for precision timekeeping.

---

## 8.10 — Summary: The Descent from GR to Newton

Three conditions applied to the Einstein field equations:

$$G_{\mu\nu} = \frac{8\pi G}{c^4}T_{\mu\nu}$$

|Condition|Mathematical operation|What it removes|
|---|---|---|
|Weak field|$g_{\mu\nu} = \eta_{\mu\nu} + h_{\mu\nu}$, linearize|Nonlinear metric self-interaction|
|Slow motion|$v \ll c$ → $T_{00} \approx \rho c^2$ dominates|Momentum and stress as sources|
|Static|$\partial_t h_{\mu\nu} = 0$|Retardation, gravitational waves|

**Output:** $\nabla^2\Phi = 4\pi G\rho$ → $F = -GMm/r^2\hat r$

**What was discarded and when it matters:**

|Discarded|GR effect|Magnitude|Engineering relevance|
|---|---|---|---|
|Wave term $\Box$|Gravitational waves|$h \sim 10^{-21}$|LIGO, LISA|
|$T_{ij}$ terms|Gravitational waves from pressure|Small|Neutron stars|
|$h_{ij}$ spatial metric|Gravitational lensing factor of 2|$1.75''$|VLBI astrometry|
|Time-dep. metric|Frame dragging|39 mas/yr|Gravity Probe B|
|Higher-order $h^2$|Perihelion precession|43''/century|Mercury, binary pulsars|
|Velocity of source|Gravitomagnetic effects|$\sim v/c$ times GR|Active research|

---

## 8.11 — Looking Ahead: Bridge B Continues

With Newton's law in hand, Chapter 9 takes the next Bridge B limit: $\hbar\to 0$, deriving classical mechanics from quantum mechanics. Newton's law (this chapter) and Lagrangian mechanics (Ch. 9) combine to give the full toolkit of classical particle and rigid-body dynamics — the spine of mechanical engineering.

Gravity enters engineering practice overwhelmingly through Newtonian approximation. The systematic position is clear: Newton is GR's leading-order term, fully justified in any context where $GM/rc^2 \ll 1$ and $v \ll c$.

---

_End of Chapter 8._

---

_Next: Chapter 9 — Bridge B.a: From Quantum Mechanics to Classical Mechanics ($\hbar \to 0$)_