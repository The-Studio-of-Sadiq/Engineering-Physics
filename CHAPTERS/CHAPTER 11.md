# CHAPTER 11
# Bridge B.c — Maxwell's Equations from the U(1) Gauge Sector
### Four Equations from One Lagrangian Term

---

> *From the long view of the history of mankind, seen from, say, ten thousand years from now,*
> *there can be little doubt that the most significant event of the 19th century will be judged*
> *as Maxwell's discovery of the laws of electrodynamics.*
> — Richard Feynman, *The Feynman Lectures on Physics*, Vol. II

---

## 11.0 — Bridge B.c in Context

Bridges B.a and B.b ($\hbar\to 0$ and $N\to\infty$) recovered classical
mechanics and thermodynamics from quantum mechanics. Bridge B.c is a different
operation entirely: it takes the **classical limit of the U(1) gauge sector**
of $\mathcal{L}_{SM}$.

**The operation:** The quantum U(1) gauge field $A_\mu$ is, at the quantum level,
the photon field — its excitations are photons. In the classical limit
(many photons in a coherent state, field amplitudes large compared to $\hbar\omega$),
the quantum field operator $\hat A_\mu$ becomes a classical field
$A_\mu(\mathbf{r},t)$. The Euler-Lagrange equations for this classical field
are **Maxwell's equations**.

**What this chapter shows:**

The four Maxwell equations — which every EEE student learns as four separate,
empirically-derived postulates — are in fact:
- **Two equations:** from a single covariant Euler-Lagrange equation
- **Two more:** from a mathematical identity on the field tensor

Neither set is postulated. Both follow from the U(1) gauge sector
of Ch. 0 by the field Euler-Lagrange procedure of Ch. 1 §1.9.

| Bridge B sub-path | Limit | Result | Chapter |
|---|---|---|---|
| B.a | $\hbar\to 0$ | Classical mechanics | 9 |
| B.b | $N\to\infty$ | Thermodynamics | 10 |
| **B.c** | Classical U(1) field | **Maxwell's equations** | **11** |
| B.d | Weak-field metric | Newton's gravity | 8 |
| B.e | Kubo averaging | Transport laws | 13 |

---

## 11.1 — The Starting Point: The Electromagnetic Lagrangian Density

From Ch. 0 §0.4.2, the U(1) gauge sector of $\mathcal{L}_{SM}$ in the classical
field limit:

$$\boxed{\mathcal{L}_{EM} = -\frac{1}{4\mu_0}F_{\mu\nu}F^{\mu\nu} + A_\mu j^\mu}$$

Every symbol:

**$A^\mu = (\phi/c,\, \mathbf{A})$** — the **electromagnetic four-potential**.
The scalar potential $\phi$ (volts) and the vector potential $\mathbf{A}$ (V·s/m)
are unified into a single four-vector. The physical fields $\mathbf{E}$ and
$\mathbf{B}$ are both encoded in $A^\mu$.

**$F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu$** — the **field strength tensor**
(or Faraday tensor). It is antisymmetric: $F_{\mu\nu} = -F_{\nu\mu}$. It is
the gauge-invariant content of the theory — every physical observable is expressed
through $F_{\mu\nu}$, not through $A_\mu$ directly.

**$j^\mu = (c\rho,\, \mathbf{J})$** — the **electromagnetic four-current**:
$j^0 = c\rho$ (charge density scaled to have units consistent with current
density), and $j^i = J^i$ (current density components). This is the Noether
current of U(1) symmetry (Ch. 1 §1.7.3) — charge conservation is built into
its very definition.

**$\mu_0 = 4\pi\times 10^{-7}$ H/m** — the permeability of free space
(in SI units). The factor $1/\mu_0$ gives the correct normalization for
SI electromagnetic fields.

**$A_\mu j^\mu = -\phi\rho + \mathbf{A}\cdot\mathbf{J}$** — the coupling
between the gauge field and the current: the source term that drives the fields.

---

## 11.2 — The Field Strength Tensor: $E$ and $B$ Unified

### 11.2.1 — Constructing $F_{\mu\nu}$

Using the spacetime metric $\eta_{\mu\nu} = \text{diag}(-1,+1,+1,+1)$ and
the four-potential $A^\mu = (\phi/c, A_x, A_y, A_z)$:

$$F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu$$

Computing each independent component using
$\mathbf{E} = -\nabla\phi - \partial_t\mathbf{A}$ and $\mathbf{B} = \nabla\times\mathbf{A}$:

$$F_{0i} = \partial_0 A_i - \partial_i A_0 = -\frac{E_i}{c}$$

$$F_{12} = \partial_1 A_2 - \partial_2 A_1 = B_z, \qquad F_{23} = B_x, \qquad F_{31} = B_y$$

The complete field tensor in matrix form:

$$F_{\mu\nu} = \begin{pmatrix}0 & -E_x/c & -E_y/c & -E_z/c \\ E_x/c & 0 & -B_z & B_y \\ E_y/c & B_z & 0 & -B_x \\ E_z/c & -B_y & B_x & 0\end{pmatrix}$$

The contravariant version $F^{\mu\nu} = \eta^{\mu\alpha}\eta^{\nu\beta}F_{\alpha\beta}$
differs only in the sign of the $E/c$ entries:

$$F^{\mu\nu} = \begin{pmatrix}0 & E_x/c & E_y/c & E_z/c \\ -E_x/c & 0 & -B_z & B_y \\ -E_y/c & B_z & 0 & -B_x \\ -E_z/c & -B_y & B_x & 0\end{pmatrix}$$

**Physical meaning:** A single antisymmetric tensor $F_{\mu\nu}$ encodes all six
components of the electromagnetic field: three electric ($E_x, E_y, E_z$) and
three magnetic ($B_x, B_y, B_z$). What one observer sees as purely electric,
another observer moving relative to the first sees as a mixture of electric and
magnetic. $F_{\mu\nu}$ is the observer-independent object; $\mathbf{E}$ and
$\mathbf{B}$ separately are observer-dependent projections.

### 11.2.2 — The Lagrangian in Terms of $E$ and $B$

$$-\frac{1}{4\mu_0}F_{\mu\nu}F^{\mu\nu} = \frac{1}{2}\left(\frac{\epsilon_0 E^2}{1} - \frac{B^2}{\mu_0}\right) = \frac{\epsilon_0}{2}\left(E^2 - c^2B^2\right)$$

using $\mu_0\epsilon_0 = 1/c^2$.

The electromagnetic Lagrangian density is proportional to $E^2 - c^2B^2$ —
the Lorentz-invariant combination of the field magnitudes. This is not
$E^2 + c^2B^2$ (the energy density); the Lagrangian is $T - V$, not $T + V$.

---

## 11.3 — Euler-Lagrange Descent: Covariant Maxwell Equations

### 11.3.1 — Applying the Field Euler-Lagrange Equation

From Ch. 1 §1.9.2, the field Euler-Lagrange equation for dynamical field $A_\nu$:

$$\frac{\partial\mathcal{L}_{EM}}{\partial A_\nu} - \partial_\mu\frac{\partial\mathcal{L}_{EM}}{\partial(\partial_\mu A_\nu)} = 0$$

**First term:** $\frac{\partial\mathcal{L}_{EM}}{\partial A_\nu} = j^\nu$
(from the source term $A_\mu j^\mu$)

**Second term:** Using $\frac{\partial F_{\alpha\beta}}{\partial(\partial_\mu A_\nu)} = \delta^\mu_\alpha\delta^\nu_\beta - \delta^\mu_\beta\delta^\nu_\alpha$:

$$\frac{\partial\mathcal{L}_{EM}}{\partial(\partial_\mu A_\nu)} = -\frac{1}{\mu_0}F^{\mu\nu}$$

Substituting:

$$j^\nu - \partial_\mu\left(-\frac{1}{\mu_0}F^{\mu\nu}\right) = 0$$

$$\boxed{\partial_\mu F^{\mu\nu} = \mu_0 j^\nu}$$

**This single covariant equation contains two of Maxwell's four equations.**

### 11.3.2 — The Bianchi Identity: Two More Equations for Free

Since $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu$, direct computation
shows:

$$\partial_\lambda F_{\mu\nu} + \partial_\mu F_{\nu\lambda} + \partial_\nu F_{\lambda\mu} = 0$$

This is the **Bianchi identity** — not an equation of motion, but a
**mathematical identity** that holds for any antisymmetric tensor derived
from a four-potential. It requires no variation, no Lagrangian — it is
automatic from the definition $F = \partial\wedge A$.

**The Bianchi identity contains the other two Maxwell equations.**

The structure: one covariant equation from dynamics, one identity from geometry.
Maxwell's four equations split exactly 2+2.

---

## 11.4 — The Four Maxwell Equations in 3D Form

### 11.4.1 — From $\partial_\mu F^{\mu\nu} = \mu_0 j^\nu$

**Component $\nu = 0$** (time component, using $j^0 = c\rho$):

$$\partial_i F^{i0} = \mu_0 j^0 = \mu_0 c\rho$$

$$\frac{1}{c}\partial_i E^i = \mu_0 c\rho \quad\Longrightarrow\quad \boxed{\nabla\cdot\mathbf{E} = \frac{\rho}{\epsilon_0}}$$

**Gauss's law for electricity.** The divergence of $\mathbf{E}$ is sourced by
free charge density.

**Component $\nu = i$** (spatial components, $j^i = J^i$):

Expanding $\partial_0 F^{0i} + \partial_j F^{ji} = \mu_0 J^i$:

$$\boxed{\nabla\times\mathbf{B} - \mu_0\epsilon_0\frac{\partial\mathbf{E}}{\partial t} = \mu_0\mathbf{J}}$$

**The Ampere-Maxwell law.** The curl of $\mathbf{B}$ is sourced by current
density plus Maxwell's displacement current $\epsilon_0\partial\mathbf{E}/\partial t$
— the term Maxwell added in 1865. This single addition made electromagnetism
predict electromagnetic waves at speed $c = 1/\sqrt{\mu_0\epsilon_0}$, confirmed
by Hertz in 1887.

### 11.4.2 — From the Bianchi Identity

**Components $(\lambda,\mu,\nu) = (1,2,3)$:**

$$\partial_1 F_{23} + \partial_2 F_{31} + \partial_3 F_{12} = 0 \quad\Longrightarrow\quad \boxed{\nabla\cdot\mathbf{B} = 0}$$

**Gauss's law for magnetism.** There are no magnetic monopoles in the Standard
Model — and this is why. The equation $\nabla\cdot\mathbf{B} = 0$ is a
mathematical consequence of writing $\mathbf{B} = \nabla\times\mathbf{A}$,
which is guaranteed by the field tensor structure. (Note: if magnetic monopoles
are discovered — possibly in the f(φ) sector — $\nabla\cdot\mathbf{B} = \mu_0\rho_m$
would need to be added.)

**Components $(\lambda,\mu,\nu) = (0,i,j)$:**

$$\partial_0 F_{ij} + \partial_i F_{j0} + \partial_j F_{0i} = 0$$

In 3D vector form:

$$\boxed{\nabla\times\mathbf{E} + \frac{\partial\mathbf{B}}{\partial t} = 0}$$

**Faraday's law.** A time-varying magnetic field induces a circulating electric
field. The source of electromotive force in every transformer, generator, and
inductive sensor.

### 11.4.3 — All Four Maxwell Equations, Assembled

$$\begin{aligned}
\nabla\cdot\mathbf{E} &= \frac{\rho}{\epsilon_0} &\quad &\text{(Gauss — electric)}\\
\nabla\times\mathbf{B} &= \mu_0\mathbf{J} + \mu_0\epsilon_0\frac{\partial\mathbf{E}}{\partial t} &\quad &\text{(Ampere-Maxwell)}\\
\nabla\cdot\mathbf{B} &= 0 &\quad &\text{(Gauss — magnetic)}\\
\nabla\times\mathbf{E} &= -\frac{\partial\mathbf{B}}{\partial t} &\quad &\text{(Faraday)}
\end{aligned}$$

**The counting:** Four vector equations in 3D — but in covariant form, just one
dynamical equation and one identity. The apparent complexity of Maxwell's
equations in 3D is a coordinate artifact. In four-dimensional spacetime notation:

$$\partial_\mu F^{\mu\nu} = \mu_0 j^\nu \qquad \partial_{[\lambda}F_{\mu\nu]} = 0$$

Two lines. All of classical electrodynamics.

---

## 11.5 — Charge Conservation: Noether's Theorem Completing the Circle

Taking the four-divergence of both sides of the dynamical equation:

$$\partial_\nu\partial_\mu F^{\mu\nu} = \mu_0\partial_\nu j^\nu$$

The left side vanishes identically because $\partial_\nu\partial_\mu$ is
symmetric in $(\mu,\nu)$ while $F^{\mu\nu}$ is antisymmetric:
$\partial_\nu\partial_\mu F^{\mu\nu} = 0$.

Therefore:

$$\partial_\mu j^\mu = 0 \qquad\Longrightarrow\qquad \frac{\partial\rho}{\partial t} + \nabla\cdot\mathbf{J} = 0$$

**Charge conservation is built into Maxwell's equations.** It is not an
additional postulate. It follows from the antisymmetry of $F^{\mu\nu}$, which
follows from $F = \partial\wedge A$, which follows from U(1) gauge invariance.

**The chain from Ch. 0 to KCL:**
1. Ch. 0: U(1) gauge symmetry in $\mathcal{L}_{SM}$
2. Ch. 1 Noether: U(1) symmetry → conserved charge, $\partial_\mu j^\mu = 0$
3. This chapter: $\partial_\mu j^\mu = 0$ → continuity equation $\partial_t\rho + \nabla\cdot\mathbf{J} = 0$
4. Quasi-static limit (§11.9): $\partial_t\rho \to 0$ → $\nabla\cdot\mathbf{J} = 0$ → $\sum I_{node} = 0$
5. Ch. 18 (Layer 3): Kirchhoff's Current Law

KCL is Noether's theorem for U(1) gauge symmetry, seen from the other end
of a five-step descent.

---

## 11.6 — Gauge Invariance and the Electromagnetic Potentials

### 11.6.1 — Gauge Freedom

The field tensor $F_{\mu\nu}$ is invariant under:

$$A_\mu \to A_\mu + \partial_\mu\chi(\mathbf{r},t)$$

for any smooth scalar function $\chi$. Since $\mathbf{E}$ and $\mathbf{B}$
are determined by $F_{\mu\nu}$, they are also gauge-invariant. Physical
observables cannot depend on the choice of $\chi$.

**This is the electromagnetic manifestation of U(1) gauge invariance from Ch. 0.**
The redundancy in $A_\mu$ (the gauge freedom) is the price of writing the
theory in a way that makes Lorentz invariance and locality manifest.

### 11.6.2 — Gauge Choices

**Lorenz gauge** $\partial_\mu A^\mu = 0$ (Lorentz-covariant):
$$\Box A^\mu = \mu_0 j^\mu, \qquad \Box = -\frac{1}{c^2}\frac{\partial^2}{\partial t^2} + \nabla^2$$

Each component of $A^\mu$ satisfies an independent wave equation driven by the
corresponding component of $j^\mu$. Manifest covariance; retarded potentials.

**Coulomb gauge** $\nabla\cdot\mathbf{A} = 0$ (non-covariant but practical):
$$\nabla^2\phi = -\frac{\rho}{\epsilon_0} \quad\text{(instantaneous Coulomb potential)}$$
$$\Box\mathbf{A} = \mu_0\mathbf{J} - \frac{1}{c^2}\nabla\frac{\partial\phi}{\partial t}$$

The scalar potential is determined instantaneously by the charge distribution
(no retardation); retardation enters only through $\mathbf{A}$. Useful for
static and low-frequency problems.

---

## 11.7 — Electromagnetic Waves

### 11.7.1 — The Wave Equation in Vacuum

In free space ($\mathbf{J} = 0$, $\rho = 0$), the Lorenz gauge gives:

$$\Box A^\mu = 0 \quad\Longrightarrow\quad \left(-\frac{1}{c^2}\frac{\partial^2}{\partial t^2} + \nabla^2\right)A^\mu = 0$$

Plane wave solutions: $A^\mu = \epsilon^\mu\,e^{i(k_\nu x^\nu)} = \epsilon^\mu\,e^{i(\mathbf{k}\cdot\mathbf{r} - \omega t)}$

Dispersion relation: $k_\mu k^\mu = 0 \Rightarrow \omega^2 = c^2|\mathbf{k}|^2$, so:

$$\boxed{c = \frac{\omega}{|\mathbf{k}|} = \frac{1}{\sqrt{\mu_0\epsilon_0}} = 2.998\times 10^8\;\text{m/s}}$$

The speed of light falls out automatically — it is not put in by hand.
Maxwell noticed this in 1865: the ratio $\sqrt{1/\mu_0\epsilon_0}$ equals the
measured speed of light, and concluded that light must be an electromagnetic wave.

### 11.7.2 — Polarization: Two Physical Degrees of Freedom

The Lorenz gauge condition $k_\mu\epsilon^\mu = 0$ constrains $\epsilon^\mu$ to
be orthogonal to the wavevector — eliminating the time-like component.
A residual gauge freedom $\epsilon^\mu \to \epsilon^\mu + k^\mu\Lambda$ removes
one more degree of freedom, leaving exactly **two independent transverse
polarization states**.

For a wave propagating in $\hat z$: $\epsilon_x$ (linear $x$-polarization)
and $\epsilon_y$ (linear $y$-polarization). Or equivalently, right and left
circular polarization. No longitudinal photon in vacuum — this is a consequence
of U(1) gauge invariance.

Parallel: gravitational waves (Ch. 8) also have exactly two transverse polarizations
($+$ and $\times$), now from the diffeomorphism invariance of the metric.
The number of physical polarizations is $(d^2 - d)/2 - (d-2) = (d-2)$ for a
massless spin-1 field in $d$ spacetime dimensions: 2 in 3+1D.

### 11.7.3 — The Electromagnetic Spectrum

The wave equation gives $\omega = ck$ for any frequency. The physical spectrum:

| Band | Frequency | Wavelength | Engineering use |
|---|---|---|---|
| Radio (LF–UHF) | 30 kHz–3 GHz | 10 km–10 cm | Broadcast, radar, GPS |
| Microwave | 3–300 GHz | 10 cm–1 mm | WiFi, 5G, satellite, radar |
| Infrared | 300 GHz–400 THz | 1 mm–750 nm | Thermal imaging, fiber comms |
| Visible | 400–750 THz | 750–400 nm | LEDs, lasers, solar cells |
| UV | 750 THz–30 PHz | 400–10 nm | Lithography, sterilization |
| X-ray | 30 PHz–30 EHz | 10 nm–10 pm | Medical imaging, crystallography |
| Gamma | $>$ 30 EHz | $< 10$ pm | Nuclear medicine, radiation |

All governed by the same wave equation $\Box A^\mu = 0$ from one Lagrangian term.

---

## 11.8 — Energy and Momentum: Poynting's Theorem

### 11.8.1 — The Electromagnetic Energy-Momentum Tensor

From the Noether procedure (Ch. 1 §1.9.3), the energy-momentum tensor of the
EM field:

$$T^{\mu\nu}_{EM} = \frac{1}{\mu_0}\left(F^{\mu\alpha}F^\nu{}_\alpha - \frac{1}{4}\eta^{\mu\nu}F_{\alpha\beta}F^{\alpha\beta}\right)$$

Components in 3D:

**Energy density:**
$$u = T^{00} = \frac{1}{2}\left(\epsilon_0 E^2 + \frac{B^2}{\mu_0}\right)$$

**Poynting vector** (energy flux density):
$$\mathbf{S} = \frac{1}{\mu_0}\mathbf{E}\times\mathbf{B} = c^2\epsilon_0\mathbf{E}\times\mathbf{B}$$

**Maxwell stress tensor** $T^{ij}$ (momentum flux):
$$T^{ij} = \epsilon_0\left(E^iE^j - \frac{\delta^{ij}}{2}E^2\right) + \frac{1}{\mu_0}\left(B^iB^j - \frac{\delta^{ij}}{2}B^2\right)$$

### 11.8.2 — Poynting's Theorem

Conservation of EM energy (from $\partial_\mu T^{\mu 0} = -j^\mu F_{\mu 0}$):

$$\boxed{\frac{\partial u}{\partial t} + \nabla\cdot\mathbf{S} = -\mathbf{J}\cdot\mathbf{E}}$$

- Left side: rate of change of EM energy density + outward energy flux
- Right side: $-\mathbf{J}\cdot\mathbf{E}$ = power delivered to charges per unit volume
  (negative = EM field does work on charges; positive if charges do work on field)

**For a conductor with $\mathbf{J} = \sigma\mathbf{E}$ (Ohm's law, from Ch. 13):**
$$-\mathbf{J}\cdot\mathbf{E} = -\sigma E^2 < 0$$

The EM field continuously loses energy to the conductor as Joule heat $\sigma E^2$ per unit volume.

**The Poynting vector $\mathbf{S}$** tells you where the energy flows:

For a DC-carrying wire: $\mathbf{E}$ is parallel to the wire (driving the current);
$\mathbf{B}$ circles around it. $\mathbf{S} = \mathbf{E}\times\mathbf{B}/\mu_0$ points
**radially inward** toward the wire — the electrical power flows through the
space *around* the wire, not through the wire itself. This counterintuitive but
correct picture follows directly from Maxwell's equations.

**Momentum density:**
$$\mathbf{g} = \frac{\mathbf{S}}{c^2} = \epsilon_0(\mathbf{E}\times\mathbf{B})$$

**Radiation pressure** on a perfectly absorbing surface:
$P_{rad} = u = (\epsilon_0 E^2 + B^2/\mu_0)/2$ — the energy density equals the
radiation pressure. For sunlight at Earth's surface ($\sim 1400$ W/m²):
$P_{rad} \approx 4.7\;\mu$Pa — small but measurable, and crucial for spacecraft
attitude control (solar sails, thermal radiation torque).

---

## 11.9 — Constitutive Relations: Connecting Layer 1 to Layer 2

Maxwell's equations are exact but describe vacuum. In matter, the response of
charge distributions to applied fields must be added. In the macroscopic limit,
this is done through **constitutive relations** — relationships between the
macroscopic fields.

$$\mathbf{D} = \epsilon_0\mathbf{E} + \mathbf{P} = \epsilon\mathbf{E} = \epsilon_0(1+\chi_e)\mathbf{E}$$

$$\mathbf{H} = \frac{\mathbf{B}}{\mu_0} - \mathbf{M} = \frac{\mathbf{B}}{\mu} = \frac{\mathbf{B}}{\mu_0(1+\chi_m)}$$

$$\mathbf{J}_f = \sigma\mathbf{E}$$

The permittivity $\epsilon$, permeability $\mu$, and conductivity $\sigma$ are
**not fundamental constants** — they are Layer-1 properties of the material
that emerge from the quantum mechanics of electrons in the crystal lattice.

| Quantity | Layer-1 origin | Engineering implication |
|---|---|---|
| $\epsilon(\omega)$ | Electronic polarizability (Ch. 4 atoms, Ch. 6 bands) | Determines refractive index, capacitance, optical dispersion |
| $\mu(\omega)$ | Spin magnetization (Ch. 5 Zeeman), orbital currents | Determines inductance, magnetic shielding |
| $\sigma(\omega)$ | Kubo formula (Ch. 13): $\sigma = (e^2\tau/m)n$ | Determines resistance, skin depth, loss |

**The Drude model** gives $\sigma(\omega)$ for metals:
$$\sigma(\omega) = \frac{\sigma_0}{1-i\omega\tau} = \frac{ne^2\tau/m}{1-i\omega\tau}$$

At $\omega = 0$: DC conductivity $\sigma_0 = ne^2\tau/m$.
At $\omega\tau \gg 1$ (high frequency): $\sigma \to -i ne^2/(m\omega)$ — purely imaginary,
giving reactive behavior. The plasma frequency $\omega_p = \sqrt{ne^2/m\epsilon_0}$
marks where $\text{Re}[\epsilon(\omega)] = 0$ and the metal becomes transparent.

**Frequency dispersion — Kramers-Kronig relations:**
The real and imaginary parts of any causal response function $\epsilon(\omega)$
are related by:

$$\text{Re}[\epsilon(\omega)] - 1 = \frac{2}{\pi}\mathcal{P}\int_0^\infty\frac{\omega'\,\text{Im}[\epsilon(\omega')]}{\omega'^2 - \omega^2}d\omega'$$

These follow from causality alone (the response cannot precede the stimulus) and
are universal — satisfied by any physical $\epsilon(\omega)$, $\mu(\omega)$, or
$\sigma(\omega)$. They are used to extract absorption spectra from reflectance
measurements and to verify self-consistency of optical models.

---

## 11.10 — Electrostatics: The Static Limit of Two of Maxwell's Equations

When $\partial/\partial t = 0$ and no magnetic fields are present:

$$\nabla\cdot\mathbf{E} = \frac{\rho}{\epsilon_0}, \qquad \nabla\times\mathbf{E} = 0$$

Since $\nabla\times\mathbf{E} = 0$, write $\mathbf{E} = -\nabla\phi$ (always possible
for a curl-free vector field). Substituting into Gauss's law:

$$\boxed{\nabla^2\phi = -\frac{\rho}{\epsilon_0}}$$

**Poisson's equation** for the electrostatic potential. For $\rho = 0$: Laplace's
equation $\nabla^2\phi = 0$.

**Solution via Green's function:**
$$\phi(\mathbf{r}) = \frac{1}{4\pi\epsilon_0}\int\frac{\rho(\mathbf{r}')}{|\mathbf{r}-\mathbf{r}'|}d^3r'$$

**Boundary value problems:** Unique solution to Poisson/Laplace with boundary
conditions (Dirichlet: $\phi$ specified; Neumann: $\partial_n\phi$ specified).
Standard methods: separation of variables (spherical harmonics from Ch. 4),
image charges, conformal mapping.

**Capacitance:**

For a conductor system at potential $V$ holding charge $Q$:
$$C = \frac{Q}{V}, \qquad U = \frac{Q^2}{2C} = \frac{1}{2}CV^2 = \frac{\epsilon_0}{2}\int E^2\,d^3r$$

The energy stored equals the volume integral of $\epsilon_0 E^2/2$ — consistent
with the Poynting energy density formula.

---

## 11.11 — Magnetostatics: The Static Limit of the Other Two

When $\partial/\partial t = 0$ and no electric fields:

$$\nabla\cdot\mathbf{B} = 0, \qquad \nabla\times\mathbf{B} = \mu_0\mathbf{J}$$

Since $\nabla\cdot\mathbf{B} = 0$, write $\mathbf{B} = \nabla\times\mathbf{A}$.
In Coulomb gauge ($\nabla\cdot\mathbf{A} = 0$):

$$\nabla\times(\nabla\times\mathbf{A}) = \mu_0\mathbf{J} \quad\Longrightarrow\quad -\nabla^2\mathbf{A} = \mu_0\mathbf{J}$$

**Solution via Green's function:**
$$\mathbf{A}(\mathbf{r}) = \frac{\mu_0}{4\pi}\int\frac{\mathbf{J}(\mathbf{r}')}{|\mathbf{r}-\mathbf{r}'|}d^3r' \quad\Longrightarrow\quad \mathbf{B} = \frac{\mu_0}{4\pi}\int\frac{\mathbf{J}(\mathbf{r}')\times(\mathbf{r}-\mathbf{r}')}{|\mathbf{r}-\mathbf{r}'|^3}d^3r'$$

This is the **Biot-Savart law** — derived, not postulated.

**Inductance:**

For a circuit carrying current $I$ with total flux linkage $\Lambda = N\Phi$:
$$L = \frac{\Lambda}{I} = \frac{N\Phi}{I}, \qquad U = \frac{1}{2}LI^2 = \frac{1}{2\mu_0}\int B^2\,d^3r$$

The energy stored equals the volume integral of $B^2/2\mu_0$.

---

## 11.12 — The Quasi-Static Limit: Bridge to Circuit Theory

### 11.12.1 — The Lumping Criterion for Electromagnetism

The full Maxwell equations are PDEs. To use lumped-element circuit theory (Ch. 18),
we need the **quasi-static approximation**: the system is small compared to the
electromagnetic wavelength.

For a circuit of characteristic size $L$ operating at frequency $f$:

$$\text{Quasi-static valid when: } \frac{L}{\lambda_{EM}} = \frac{Lf}{c} \ll 1$$

At 60 Hz (power systems), $\lambda = 5000$ km → valid for all practical circuits.
At 1 GHz (RF), $\lambda = 30$ cm → a 3 cm device satisfies $L/\lambda = 0.1$ — marginally valid.
At 10 GHz, $L = 1$ cm → $L/\lambda = 1/3$ — distributed effects essential.

### 11.12.2 — Kirchhoff's Voltage Law from Faraday

In the quasi-static limit, consider a closed loop $\mathcal{C}$. Integrate
Faraday's law over a surface $\mathcal{S}$ bounded by $\mathcal{C}$:

$$\oint_\mathcal{C}\mathbf{E}\cdot d\mathbf{l} = -\frac{d}{dt}\iint_\mathcal{S}\mathbf{B}\cdot d\mathbf{S} = -\frac{d\Phi_B}{dt}$$

For a circuit with lumped inductors (where flux is concentrated in the inductors):

$$\sum_{elements}\int\mathbf{E}\cdot d\mathbf{l} = -\frac{d\Phi_B}{dt}$$

At low frequency (negligible magnetic flux in the "empty" space between components):

$$\sum_{\text{branches}} V_k = 0$$

This is **Kirchhoff's Voltage Law** — the integral form of Faraday's law
in the quasi-static limit with lumped flux.

At DC ($d\Phi_B/dt = 0$): the right side vanishes exactly, giving the simple
form $\sum V_k = 0$ without qualification.

### 11.12.3 — Kirchhoff's Current Law from Charge Conservation

From the continuity equation $\partial_t\rho + \nabla\cdot\mathbf{J} = 0$,
integrate over the volume of a node:

$$\frac{dQ_{node}}{dt} = -\oint\mathbf{J}\cdot d\mathbf{S} = -\sum_k I_k$$

In the quasi-static limit, charge does not accumulate at a node on timescales
of interest ($dQ_{node}/dt \to 0$ in steady state or low-frequency AC):

$$\sum_k I_k = 0$$

This is **Kirchhoff's Current Law** — charge conservation (Noether U(1))
applied to a lumped node.

**The two Kirchhoff laws are exactly Maxwell's equations in the quasi-static,
lumped-element limit.** Every circuit calculation you will ever perform in
Chapter 18 traces back to the two lines of covariant EM theory in §11.3.

### 11.12.4 — Impedance from Maxwell

In phasor (frequency-domain) form, the relation between voltage and current
for each passive element follows from Maxwell:

**Resistor:** $\mathbf{J} = \sigma\mathbf{E}$ → $V = IR$ (Ohm's law from Ch. 13 Kubo formula)

**Capacitor:** Gauss's law → $Q = CV$, differentiated → $I = C\,dV/dt$ → $Z_C = 1/i\omega C$

**Inductor:** Faraday's law → $V = L\,dI/dt$ → $Z_L = i\omega L$

The impedance concept is the frequency-domain projection of Maxwell's equations
onto a lumped circuit. AC circuit analysis (impedance, transfer functions, filters,
resonance) is Layer-3 Maxwell, Noether, and Ohm packaged for daily engineering use.

---

## 11.13 — Electromagnetic Duality

Maxwell's equations in vacuum ($\rho = 0$, $\mathbf{J} = 0$) are symmetric
under the **duality transformation**:

$$\mathbf{E} \to c\mathbf{B}, \qquad c\mathbf{B} \to -\mathbf{E}$$

or equivalently $F_{\mu\nu} \to \tilde F_{\mu\nu} = \frac{1}{2}\epsilon_{\mu\nu\rho\sigma}F^{\rho\sigma}$.

This symmetry is broken by the presence of electric charges (source for
$\nabla\cdot\mathbf{E}$) but not magnetic charges (since $\nabla\cdot\mathbf{B} = 0$
— no magnetic monopoles). If magnetic monopoles exist (they appear in some GUT
extensions in $\mathcal{F}$), the symmetry would be restored:
$\nabla\cdot\mathbf{B} = \mu_0\rho_m$, $\nabla\times\mathbf{E} = -\partial_t\mathbf{B} - \mu_0\mathbf{J}_m$.

This is another instance where $\mathcal{F}$ of Ch. 0 would modify our equations —
and where the phenomenology of Layer 2 (the presence or absence of magnetic
monopoles) would directly reflect Layer-0 physics.

---

## 11.14 — Summary

Bridge B.c complete. Maxwell's equations descended from one Lagrangian term:

| Result | Origin |
|---|---|
| $\mathcal{L}_{EM} = -\frac{1}{4\mu_0}F_{\mu\nu}F^{\mu\nu} + A_\mu j^\mu$ | U(1) sector of $\mathcal{L}_{SM}$, classical field limit |
| $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu$ | Definition of field tensor |
| $\partial_\mu F^{\mu\nu} = \mu_0 j^\nu$ | Euler-Lagrange applied to $A_\nu$ |
| $\nabla\cdot\mathbf{E} = \rho/\epsilon_0$ | $\nu = 0$ component |
| $\nabla\times\mathbf{B} = \mu_0\mathbf{J} + \mu_0\epsilon_0\partial_t\mathbf{E}$ | $\nu = i$ components |
| $\partial_{[\lambda}F_{\mu\nu]} = 0$ | Bianchi identity (automatic from $F = \partial A$) |
| $\nabla\cdot\mathbf{B} = 0$ | Bianchi, all-spatial |
| $\nabla\times\mathbf{E} + \partial_t\mathbf{B} = 0$ | Bianchi, one time index |
| $\partial_\mu j^\mu = 0$ | Antisymmetry of $F^{\mu\nu}$ → automatic charge conservation |
| $\omega = ck$ (EM waves) | Wave equation in vacuum |
| $c = 1/\sqrt{\mu_0\epsilon_0}$ | Speed of light from Lagrangian parameters |
| KVL: $\sum V_k = 0$ | Faraday's law, quasi-static, lumped |
| KCL: $\sum I_k = 0$ | Charge conservation, quasi-static, lumped node |
| $Z_C = 1/i\omega C$ | Gauss's law → $Q = CV$ → differentiated |
| $Z_L = i\omega L$ | Faraday's law → $V = L\,dI/dt$ |

---

## 11.15 — Engineering Thread

| Physics | Application |
|---|---|
| Wave equation $\omega = ck$ | Antenna design; waveguides; optical fiber; radar |
| Faraday's law | Transformers; generators; electric motors; wireless charging |
| Ampere-Maxwell (displacement current) | Why capacitors "conduct" at AC; RF circuit behavior |
| Poynting vector $\mathbf{S} = \mathbf{E}\times\mathbf{B}/\mu_0$ | Power flow in transmission lines; electromagnetic power delivery |
| Poisson equation $\nabla^2\phi = -\rho/\epsilon_0$ | Capacitor design; electrostatic actuators; MEMS |
| Biot-Savart | Inductor and transformer design; MRI coil design |
| KVL (from Faraday, quasi-static) | All circuit analysis |
| KCL (from charge conservation) | All node analysis |
| $\epsilon(\omega), \mu(\omega)$ | Dielectric material selection; antenna substrate; optical coatings |
| $\sigma(\omega)$ Drude + Kubo | Conductor sizing; skin depth; RF shielding design |
| Kramers-Kronig | Optical material characterization; loss estimation |
| Radiation pressure | Laser-based positioning; solar sail mission design |

---

## 11.16 — Looking Ahead

Chapters 8–11 have now completed four of the five Bridge B paths:
- B.a (Ch. 9): $\hbar\to 0$ → classical mechanics
- B.b (Ch. 10): $N\to\infty$ → thermodynamics
- B.c (Ch. 11): classical U(1) → Maxwell's equations
- B.d (Ch. 8): weak-field GR → Newton's gravity

**Chapter 12** uses the Maxwell equations derived here to develop electromagnetic
wave propagation, optics, and photonics — applying the wave equation to the
full EM spectrum and building toward the optical phenomena catalogued in Ch. 2.

**Chapter 13** then performs Bridge B.e: applying the Kubo formula (quantum
scattering + statistical averaging) to derive the constitutive relations
$\mathbf{J} = \sigma\mathbf{E}$, $\mathbf{q} = -\kappa\nabla T$, and the
full table of transport laws. This completes Bridge B and assembles the
complete Layer-2 toolkit.

---

*End of Chapter 11.*

---
*Next: Chapter 12 — Electromagnetic Waves, Optics, and Photonics*
