# Bridge C — Lumping and the Effort-Flow Template

### The Descent from PDEs to Engineering Systems

---

> _An electrical engineer, a mechanical engineer, and a chemical engineer_ _are all solving the same equation. The only difference is what they call the variables._ — teaching tradition in engineering mathematics

---

## 17.0 — Bridge C in Context

Chapters 8–16 built Layer 2 completely. The full set of classical continuum physics — Newton, thermodynamics, Maxwell, transport laws, fluid mechanics, solid mechanics, and the unified PDE — is now assembled.

**Bridge C performs one operation:** integrate the Layer-2 PDEs over finite control volumes, invoke the lumping criterion ($L/\lambda \ll 1$ or $Bi \ll 1$), and the PDEs collapse into ordinary differential equations and algebraic balance equations.

The result is **Layer 3** — the engineering systems scale. Its defining feature: all physical domains share one mathematical template, with the only difference being the names of variables.

**This chapter is the book's most important structural claim, made explicit:** EEE, ME, CE, and ChE are not four different subjects. They are four different labelings of one mathematical system, valid when the lumping criterion holds.

**Bridge C in the layer map:**

```
Layer 2 (PDEs)
   ∂²φ/∂t² = v²∇²φ         (wave equation)
   ∂φ/∂t = D∇²φ            (diffusion equation)
   ρ Dv/Dt = -∇p + μ∇²v    (Navier-Stokes)
   ρü = (λ+μ)∇(∇·u) + μ∇²u (Navier elasticity)
              │
              │  Integrate over control volume
              │  Invoke L/λ ≪ 1 (or Bi ≪ 1)
              │
              ▼
Layer 3 (ODEs + algebraic balance equations)
   L ẍ + R ẋ + x/C = e_source    (universal second-order ODE)
   Σ flows at node = 0            (Kirchhoff-type laws)
   Σ efforts around loop = 0      (Kirchhoff-type laws)
```

---

## 17.1 — The Lumping Operation: PDE to ODE

### 17.1.1 — The Formal Procedure

Consider the diffusion equation on an element of size $L$:

$$\frac{\partial\phi}{\partial t} = D\nabla^2\phi + S$$

**Step 1: Integrate over the control volume $V = L^3$:**

$$\int_V\frac{\partial\phi}{\partial t},dV = D\int_V\nabla^2\phi,dV + \int_V S,dV$$

**Step 2: Apply the divergence theorem to the Laplacian:**

$$\frac{d}{dt}\int_V\phi,dV = D\oint_{\partial V}\nabla\phi\cdot\hat n,dA + \dot Q_{source}$$

**Step 3: Invoke the lumping assumption** — $\phi$ is spatially uniform inside $V$, so:

$$\frac{d\phi}{dt}\cdot V = D\cdot\frac{\phi_{out}-\phi_{in}}{L}\cdot A + \dot Q_{source}$$

**Step 4: Identify the lumped parameters:**

$$C_{lump}\frac{d\phi}{dt} = \frac{\phi_{out}-\phi_{in}}{R_{lump}} + S_{lump}$$

where $C_{lump} = V$ (capacitance = volume for mass storage, $\rho c_p V$ for heat) and $R_{lump} = L/DA$ (resistance).

**This is an ODE — the PDE has become a lumped circuit element.**

The same procedure applied to the wave equation gives an LC oscillator. Applied to Navier-Stokes (linearized) gives a mass-spring-damper. The lumping criterion is the only assumption — **the mathematical identity between domains is exact, not approximate.**

### 17.1.2 — The Lumping Criterion, Domain by Domain

From Ch. 16 §16.10.1, the lumping criterion for each domain:

|Domain|Criterion|Physical meaning|
|---|---|---|
|EM (circuits)|$L/\lambda = Lf/v_{em} \ll 1$|Component smaller than EM wavelength|
|Acoustic|$L/\lambda = Lf/c_s \ll 1$|Component smaller than sound wavelength|
|Elastic structural|$L/\lambda = Lf/v_P \ll 1$|Component smaller than stress wave wavelength|
|Thermal|$Bi = hL/\kappa \ll 1$|Temperature uniform within body|
|Hydraulic (pipe network)|$Lf/c_{water} \ll 1$|No water hammer effects|
|Chemical (CSTR)|Perfect mixing assumed|Concentration uniform in vessel|

**When the criterion fails:** do not use the lumped model. Use the distributed-parameter bridge zone model (transmission line, Euler-Bernoulli beam, heat equation) or the full PDE. The chapter map tells you exactly where to go.

---

## 17.2 — Effort and Flow: The Universal Variable Pair

### 17.2.1 — Definitions

From the lumped control volume, every physical domain has exactly two conjugate variable types:

**Effort variable $e$:** The "potential" — the quantity that drives the flow, does work per unit of flow passing through. Measured across an element.

**Flow variable $f$:** The "current" — the quantity that flows, the Noether current (Ch. 1 §1.7) of the conserved quantity. Measured through an element.

**Power:** $P = e \times f$ in every domain.

### 17.2.2 — The Complete Effort-Flow Table

|Domain|Effort $e$|Flow $f$|Power $e\times f$|Conserved quantity|
|---|---|---|---|---|
|Electrical|Voltage $V$ [V]|Current $I$ [A]|Watts [W]|Charge $Q$|
|Translational mech.|Force $F$ [N]|Velocity $v$ [m/s]|Watts [W]|Momentum $p$|
|Rotational mech.|Torque $\tau$ [N·m]|Angular velocity $\omega$ [rad/s]|Watts [W]|Angular momentum $L$|
|Thermal|Temperature $T$ [K]|Heat flow rate $\dot Q$ [W]|Watts (trivially)|Energy $U$|
|Hydraulic|Pressure $P$ [Pa]|Volume flow $Q$ [m³/s]|Watts [W]|Volume/mass|
|Pneumatic|Pressure $P$ [Pa]|Mass flow $\dot m$ [kg/s]|Watts [W]|Mass|
|Chemical|Chem. potential $\mu$ [J/mol]|Molar flow $\dot n$ [mol/s]|Watts [W]|Moles|
|Magnetic|Magnetomotive force $\mathcal{F}$ [A]|Magnetic flux rate $\dot\Phi$ [V]|Watts [W]|Flux $\Phi$|

**The generalized momentum** (integral of effort): $p_e = \int e,dt$ (charge in electrical, momentum in mechanical, flux linkage in magnetic)

**The generalized displacement** (integral of flow): $q_f = \int f,dt$ (charge $Q = \int I,dt$ in electrical, displacement $x = \int v,dt$ in mechanical)

### 17.2.3 — Why Exactly Two Variables?

From the Noether perspective (Ch. 1 §1.7): every conserved quantity generates a pair of conjugate variables in its domain. The conserved charge becomes the flow variable; its conjugate potential (from the Hamiltonian formulation, Ch. 1 §1.6) becomes the effort variable.

The electrical case is the clearest: U(1) gauge symmetry → charge conservation (KCL, Ch. 11 §11.12) → current as flow; the gauge potential $\phi$ becomes the voltage as effort.

For mechanical domains: space translation symmetry → momentum conservation → velocity as flow; force (the conjugate momentum driver) as effort.

**Power = effort × flow** in every domain because this product equals the rate of energy transfer, and energy is the Hamiltonian — the conserved quantity of time translation (Ch. 1 §1.7.3). The product is invariant across domains because energy is invariant across domains.

---

## 17.3 — The Three Passive Elements: R, C, L in Every Domain

### 17.3.1 — The Resistor R: Dissipation

A resistor relates effort to flow **instantaneously** (no memory):

$$e = R\cdot f \quad\text{or}\quad f = \frac{e}{R} = G\cdot e$$

where $G = 1/R$ is the conductance. Power dissipated: $P = e\cdot f = Rf^2 = e^2/R > 0$.

The resistor is the lumped form of the **constitutive transport relation** (Kubo, Ch. 13): flux = conductivity × gradient. Lumped: $\Delta\phi/L \to \Delta\phi$, $DA/L \to 1/R$.

|Domain|Resistor $R$|Physical origin|Value|
|---|---|---|---|
|Electrical|$R$ [$\Omega$]|Ohm's law ($\sigma = ne^2\tau/m$, Ch. 13)|$\rho L/A$|
|Translational mech.|Damper $b$ [N·s/m]|Newton's viscosity (Ch. 13)|$6\pi\mu a$ (Stokes)|
|Rotational mech.|Rotational damper $b_r$ [N·m·s/rad]|Viscous torque||
|Thermal|$R_{th}$ [K/W]|Fourier's law (Ch. 13)|$L/\kappa A$|
|Hydraulic|$R_{hyd}$ [Pa·s/m³]|Hagen-Poiseuille (Ch. 15)|$8\mu L/\pi r^4$|
|Chemical|$R_{chem}$ [J·s/mol²]|Fick's law (Ch. 13)|$L/DA$|

### 17.3.2 — The Capacitor C: Potential Energy Storage

A capacitor relates effort to the **integral of flow** (has memory of past flow):

$$e = \frac{1}{C}\int f,dt \quad\Longleftrightarrow\quad f = C\frac{de}{dt}$$

Energy stored: $W_C = \frac{1}{2}Ce^2$ (effort-squared storage).

The capacitor is the lumped form of the **∂φ/∂t storage term** in the PDE.

|Domain|Capacitor $C$|Physical origin|Value|
|---|---|---|---|
|Electrical|$C$ [F]|Electric field energy ($\frac{1}{2}\epsilon_0 E^2$, Ch. 11)|$\epsilon A/d$|
|Translational mech.|Compliance $1/k$ [m/N]|Spring potential energy|$1/k$|
|Rotational mech.|Torsional compliance $1/k_r$ [rad/N·m]|Torsional spring|$1/k_r$|
|Thermal|$C_{th}$ [J/K]|Thermal energy storage (Ch. 10)|$\rho c_p V$|
|Hydraulic|$C_{hyd}$ [m³/Pa]|Fluid compressibility or vessel compliance|$V/\rho c_s^2$ or $A\Delta h/\Delta P$|
|Chemical|$C_{chem}$ [mol²/J]|Vessel/tank volume|$V/RT$ (ideal gas)|

### 17.3.3 — The Inductor L: Kinetic Energy Storage

An inductor relates flow to the **integral of effort** (has memory of past effort):

$$f = \frac{1}{L}\int e,dt \quad\Longleftrightarrow\quad e = L\frac{df}{dt}$$

Energy stored: $W_L = \frac{1}{2}Lf^2$ (flow-squared storage).

The inductor is the lumped form of the **∂²φ/∂t² inertia term** in the PDE.

|Domain|Inductor $L$|Physical origin|Value|
|---|---|---|---|
|Electrical|$L$ [H]|Magnetic field energy ($\frac{1}{2}\mu_0 H^2$, Ch. 11)|$\mu N^2 A/\ell$|
|Translational mech.|Mass $m$ [kg]|Kinetic energy $\frac{1}{2}mv^2$ (Ch. 9)|$m$|
|Rotational mech.|Moment of inertia $I_r$ [kg·m²]|Rotational KE $\frac{1}{2}I_r\omega^2$ (Ch. 9)|$\sum mr^2$|
|Hydraulic|Fluid inertance $L_{hyd}$ [kg/m⁴]|Kinetic energy of flowing fluid|$\rho L/A$|
|Pneumatic|Same|Fluid inertia|$\rho L/A$|

**Why no thermal inductor?** Pure heat conduction has no "inertia" term — the thermal diffusion equation is first-order in time, not second. Temperature does not overshoot past equilibrium in a simple thermal system (unlike mechanical oscillators). When thermal wave phenomena appear (very fast laser heating, pulsed electron beams), a "thermal inertance" can be defined — but it is rarely relevant in engineering.

---

## 17.4 — Conservation Laws at Nodes: The Kirchhoff Generalizations

### 17.4.1 — The Flow Conservation Law (KCL Generalization)

At any node (junction point), the sum of all flows must be zero. From the continuity equation (Noether conservation, Ch. 1 §1.7):

$$\boxed{\sum_k f_k = 0 \quad\text{at every node}}$$

|Domain|Statement|Physical origin|
|---|---|---|
|Electrical|$\sum I_k = 0$ — KCL|Charge conservation (Noether U(1), Ch. 11 §11.12)|
|Translational mech.|$\sum F_k = m\ddot x$ — Newton's law|Momentum conservation (Noether, translation)|
|Rotational mech.|$\sum\tau_k = I_r\dot\omega$ — rotational Newton|Angular momentum conservation|
|Thermal|$\sum\dot Q_k = C_{th}\dot T$ — energy balance|Energy conservation (Noether, time translation)|
|Hydraulic|$\sum Q_k = 0$ — continuity|Mass conservation (Noether, particle number)|
|Chemical|$\sum\dot n_k = 0$ — mole balance|Particle conservation|

For static cases (no storage: $C = 0$, $L = 0$): every conservation law becomes simply $\sum f_k = 0$ — the flows sum to zero at every node.

### 17.4.2 — The Effort Conservation Law (KVL Generalization)

Around any closed loop (cycle in the graph), the sum of all effort drops must be zero:

$$\boxed{\sum_k e_k = 0 \quad\text{around every loop}}$$

|Domain|Statement|Physical origin|
|---|---|---|
|Electrical|$\sum V_k = 0$ — KVL|Faraday's law, quasi-static (Ch. 11 §11.12)|
|Translational mech.|$\sum F_k = 0$ — force loop|D'Alembert's principle (inertia as a "force")|
|Rotational mech.|$\sum\tau_k = 0$|Torque loop balance|
|Thermal|$\sum\Delta T_k = 0$|Temperature is a potential (no thermal circulation)|
|Hydraulic|$\sum\Delta P_k = 0$|Pressure is a potential (no spontaneous pressure circuits)|

**Why does the loop law hold?** Effort variables are **potentials** — they derive from scalar potential functions. For electrical: $V = -\nabla\phi - \partial_t\mathbf{A}$ and $\oint\mathbf{E}\cdot d\mathbf{l} = -d\Phi/dt \to 0$ in quasi-static. For mechanical: force is the gradient of a potential. The loop sum is identically zero because the line integral of a gradient over a closed loop is zero — a mathematical identity.

---

## 17.5 — Bond Graphs: The Formal Multi-Domain Language

### 17.5.1 — Bond Graph Notation

A **bond** is a line connecting two subsystems, with a **half-arrow** indicating the positive flow direction. Every bond carries both an effort and a flow:

```
    e
  ────────→ (half-arrow shows positive flow convention)
    f
```

Power flows in the direction of the half-arrow when $P = ef > 0$.

**Bond graph elements:**

|Symbol|Name|Law|Domain example|
|---|---|---|---|
|R|Resistor|$e = Rf$|Resistor, damper, pipe|
|C|Capacitor|$f = C\dot e$|Capacitor, spring, thermal mass|
|I|Inductor|$e = L\dot f$|Inductor, mass, fluid inertance|
|Se|Effort source|$e = e_s(t)$|Voltage source, force source, pressure source|
|Sf|Flow source|$f = f_s(t)$|Current source, velocity source, flow source|
|TF|Transformer|$e_1 = n\cdot e_2$, $f_2 = n\cdot f_1$|Ideal transformer, gear, lever, piston|
|GY|Gyrator|$e_1 = r\cdot f_2$, $e_2 = r\cdot f_1$|Motor/generator, gyroscope, Hall sensor|

### 17.5.2 — Junctions: The Topology

Two junction types define how bonds connect:

**0-junction (common effort):** All connected bonds share the same effort. Flows sum to zero ($\sum f_k = 0$). Analog: nodes in parallel in circuits.

$$e_1 = e_2 = \cdots = e_n, \qquad \sum_k f_k = 0$$

**1-junction (common flow):** All connected bonds share the same flow. Efforts sum to zero ($\sum e_k = 0$). Analog: elements in series in circuits.

$$f_1 = f_2 = \cdots = f_n, \qquad \sum_k e_k = 0$$

### 17.5.3 — Bond Graph Examples: Identical Topology, Different Physics

**Series RLC circuit** and **mass-spring-damper** have identical bond graphs:

```
Series RLC:
Se ── 1 ── R
         ├── C
         └── I

Mass-spring-damper:
Se ── 1 ── R (damper b)
         ├── C (spring 1/k)
         └── I (mass m)
```

The 1-junction says: same current through all elements (series circuit) = same velocity for all elements (everything moves at the same velocity). The effort equation: $V_{source} = V_R + V_C + V_L$ = $F_{applied} = F_{damper} + F_{spring} + F_{mass}$.

These are **the same equation with different labels.** Every analytical result derived for one (step response, frequency response, resonance) applies directly to the other.

**Transformer and lever:**

```
Hydraulic cylinder → mechanical:
P_in ─── TF(A) ─── F_out
Q_in                 v_out

Gear train:
τ_in ─── TF(N) ─── τ_out
ω_in                 ω_out
```

Both are transformers with effort/flow transformation ratio $n = A$ (area) or $n = N$ (gear ratio): $e_1 = n\cdot e_2$, $f_2 = n\cdot f_1$, power conserved: $e_1f_1 = e_2f_2$.

**Motor/generator as gyrator:**

An electric motor converts electrical effort (voltage $V$) and flow (current $I$) to mechanical effort (torque $\tau$) and flow (angular velocity $\omega$):

$$V = K_e\omega, \qquad \tau = K_t I$$

For an ideal motor: $K_e = K_t = K$ (back-EMF constant = torque constant). This is a gyrator with $r = K$: electrical effort drives mechanical flow, and mechanical effort drives electrical flow. The gyrator is non-reciprocal — it is what makes motors and generators directional.

---

## 17.6 — Complex Impedance and Transfer Functions

### 17.6.1 — Impedance in Every Domain

For sinusoidal steady state ($e = \hat e e^{i\omega t}$, $f = \hat f e^{i\omega t}$), the **impedance** is:

$$Z(\omega) = \frac{\hat e}{\hat f}$$

For each element:

|Element|Impedance $Z(\omega)$|At DC ($\omega\to 0$)|At high $\omega$|
|---|---|---|---|
|R|$R$|$R$ (finite)|$R$ (finite)|
|C|$1/i\omega C$|$\infty$ (blocks DC)|$0$ (short)|
|L (I)|$i\omega L$|$0$ (short)|$\infty$ (blocks HF)|

**Admittance:** $Y(\omega) = 1/Z(\omega)$.

**Combination rules** (same in every domain):

- Series: $Z_{total} = Z_1 + Z_2 + \cdots$ (impedances add)
- Parallel: $Y_{total} = Y_1 + Y_2 + \cdots$ (admittances add)

### 17.6.2 — The Transfer Function

The **transfer function** $H(s) = Y(s)/X(s)$ in the Laplace domain ($s = i\omega$ for sinusoidal; $s = \sigma + i\omega$ for general transients) relates any output to any input for a linear system.

For a series RLC circuit with input voltage $V_{in}$ and output voltage across C:

$$H(s) = \frac{V_C}{V_{in}} = \frac{1/Cs}{Ls^2 + Rs + 1/C} = \frac{\omega_0^2}{s^2 + 2\zeta\omega_0 s + \omega_0^2}$$

where $\omega_0 = 1/\sqrt{LC}$ and $\zeta = R/2\sqrt{L/C}$.

The transfer function encodes:

- **Poles:** values of $s$ where $H\to\infty$ — system's natural frequencies
- **Zeros:** values of $s$ where $H\to 0$ — frequencies blocked by the system
- **Frequency response:** $H(i\omega)$ gives amplitude and phase vs. frequency (Bode plot)

The **Bode plot** (log magnitude vs. log frequency):

- Each pole at $\omega_p$: slope changes by $-20$ dB/decade
- Each zero at $\omega_z$: slope changes by $+20$ dB/decade
- Reading off poles and zeros directly from the Bode plot is a core engineering skill

**This machinery works in every domain.** A thermal system, a hydraulic network, and a mechanical vibration problem all have transfer functions of the same form — and all use the same Bode plot analysis.

---

## 17.7 — The Second-Order System: The Universal Template

### 17.7.1 — The Governing ODE

The second-order system (L-R-C, mass-spring-damper, hydraulic RCL):

$$\boxed{L\ddot q + R\dot q + \frac{q}{C} = e_{source}(t)}$$

where $q = \int f,dt$ is the generalized displacement (charge, position, volume). In standard form, dividing by $L$:

$$\ddot q + 2\zeta\omega_0\dot q + \omega_0^2 q = \frac{e_{source}}{L}$$

**Natural frequency:** $$\omega_0 = \frac{1}{\sqrt{LC}} \qquad\text{[rad/s]}$$

**Damping ratio:** $$\zeta = \frac{R}{2}\sqrt{\frac{C}{L}} = \frac{R}{2\omega_0 L} = \frac{1}{2Q}$$

**Quality factor:** $$Q = \frac{\omega_0 L}{R} = \frac{1}{R}\sqrt{\frac{L}{C}} = \frac{1}{2\zeta}$$

### 17.7.2 — Free Response (Homogeneous Solution)

Characteristic equation: $s^2 + 2\zeta\omega_0 s + \omega_0^2 = 0$

Roots: $s_{1,2} = -\zeta\omega_0 \pm \omega_0\sqrt{\zeta^2 - 1}$

**Three regimes:**

**Underdamped** ($\zeta < 1$): $s_{1,2} = -\zeta\omega_0 \pm i\omega_d$ where $\omega_d = \omega_0\sqrt{1-\zeta^2}$

$$q(t) = e^{-\zeta\omega_0 t}\left(A\cos\omega_d t + B\sin\omega_d t\right)$$

Oscillates at $\omega_d$ with exponentially decaying envelope. Time to decay: $\tau = 1/\zeta\omega_0$.

**Critically damped** ($\zeta = 1$): repeated root $s = -\omega_0$

$$q(t) = (A + Bt),e^{-\omega_0 t}$$

Fastest approach to equilibrium without overshoot.

**Overdamped** ($\zeta > 1$): two real roots $s_1 < s_2 < 0$

$$q(t) = A,e^{s_1 t} + B,e^{s_2 t}$$

Slow exponential approach; no oscillation.

### 17.7.3 — Step Response

For a unit step input $e_{source} = E_0,u(t)$:

**Underdamped ($\zeta < 1$):**

$$q(t) = E_0 C\left[1 - e^{-\zeta\omega_0 t}\left(\cos\omega_d t + \frac{\zeta}{\sqrt{1-\zeta^2}}\sin\omega_d t\right)\right]$$

- Overshoot: $M_p = e^{-\pi\zeta/\sqrt{1-\zeta^2}}$
- Rise time: $t_r \approx (1.8)/\omega_0$ (10% to 90%)
- Settling time: $t_s \approx 4/\zeta\omega_0$ (±2% band)

**The same metrics apply to every domain:** overshoot in a mass-spring system (mechanical), ringing in an RLC circuit (electrical), thermal overshoot in a temperature controller (thermal), pressure oscillation in a hydraulic ram (hydraulic).

### 17.7.4 — Frequency Response

For sinusoidal input $e_{source} = E_0\cos\omega t$:

$$|H(i\omega)| = \frac{\omega_0^2}{\sqrt{(\omega_0^2-\omega^2)^2 + 4\zeta^2\omega_0^2\omega^2}}$$

$$\angle H(i\omega) = -\arctan!\left(\frac{2\zeta\omega_0\omega}{\omega_0^2-\omega^2}\right)$$

**Resonance peak:** At $\omega_p = \omega_0\sqrt{1-2\zeta^2}$ (for $\zeta < 1/\sqrt{2}$):

$$|H_{peak}| = \frac{1}{2\zeta\sqrt{1-\zeta^2}} \approx \frac{1}{2\zeta} = Q \quad\text{(for small }\zeta\text{)}$$

The **Q factor physically means:** the resonance amplitude is $Q$ times the DC amplitude. High-Q systems are highly resonant and selective (narrow bandpass).

**Half-power bandwidth:** $\Delta\omega = \omega_0/Q$ — the frequency range around resonance where power is above $P_{max}/2$.

### 17.7.5 — The Universal Template Table

|Physical system|$L$ (inertance)|$R$ (resistance)|$C$ (compliance)|$\omega_0$|
|---|---|---|---|---|
|Series RLC circuit|Inductance $L$|Resistance $R$|Capacitance $C$|$1/\sqrt{LC}$|
|Mass-spring-damper|Mass $m$|Damping $b$|$1/k$ (spring)|$\sqrt{k/m}$|
|Pendulum (small angle)|$m\ell^2$|Air drag|$m\ell/g$|$\sqrt{g/\ell}$|
|Torsional oscillator|Inertia $I_r$|Bearing friction|$1/k_r$|$\sqrt{k_r/I_r}$|
|Hydraulic L-R-C|Fluid inertance $\rho L/A$|Pipe resistance|Accumulator $C_{hyd}$|$1/\sqrt{L_{hyd}C_{hyd}}$|
|Helmholtz resonator|Air inertance in neck|Air viscosity|Volume compliance|$c_s A/V\ell$|
|Thermal R-C|(no inductor)|$R_{th}$|$C_{th}$|(first-order only)|

**Design insight:** Every system in this table can be analyzed with identical mathematics. The engineer chooses which row to work in; the equations are the same.

---

## 17.8 — Thévenin and Norton Equivalents

### 17.8.1 — The Theorems

**Thévenin's theorem:** Any linear network seen from two terminals is equivalent to:

- An effort source $e_{Th}$ = open-circuit effort (measure effort with no load)
- A series impedance $Z_{Th}$ = impedance seen looking into the network with all sources killed

**Norton's theorem:** The same network is also equivalent to:

- A flow source $f_N = e_{Th}/Z_{Th}$ = short-circuit flow
- A parallel impedance $Z_N = Z_{Th}$

**Maximum power transfer:** Power delivered to load $Z_L$ is maximized when: $$Z_L = Z_{Th}^*$$

For resistive networks: $R_L = R_{Th}$, and $P_{max} = e_{Th}^2/4R_{Th}$.

### 17.8.2 — Thévenin/Norton in Every Domain

|Domain|Thévenin source|Thévenin impedance|Maximum power transfer|
|---|---|---|---|
|Electrical|$V_{OC}$ [V]|$R_{Th}$ [$\Omega$]|$R_L = R_{Th}$|
|Mechanical|$F_{free}$ (free deflection force)|$k_{Th}$ (stiffness)|$k_L = k_{Th}$|
|Thermal|$T_{OC}$ [K]|$R_{th,Th}$ [K/W]|$R_{th,L} = R_{th,Th}$|
|Hydraulic|$P_{OC}$ [Pa]|$R_{hyd,Th}$ [Pa·s/m³]|$R_{hyd,L} = R_{hyd,Th}$|
|Acoustic|$p_{OC}$ [Pa]|$Z_{ac,Th}$ [Pa·s/m³]|Impedance match|

**Engineering use:** Every subnetwork can be reduced to its Thévenin/Norton equivalent before connecting to the next subsystem — modularity. The impedance matching principle (maximum power transfer) governs:

- RF amplifier matching networks (EEE)
- Acoustic transducer design (ME/EEE)
- Hydraulic actuator sizing (ME)
- Heat exchanger coupling to thermal loads (ME/ChE)

---

## 17.9 — Energy and Power Accounting

### 17.9.1 — Power Balance at Every Instant

For any closed system, the power balance:

$$\underbrace{P_{source}}_{\text{input}} = \underbrace{\frac{d}{dt}\left(\frac{1}{2}Ce^2 + \frac{1}{2}Lf^2\right)}_{\text{stored}} + \underbrace{Rf^2}_{\text{dissipated}}$$

This is the first law of thermodynamics (Noether energy conservation, Ch. 1 §1.7.3) expressed in lumped-element form. It applies identically in every domain — because it follows from the same Noether theorem in every domain.

### 17.9.2 — Reactive Power and Power Factor

For sinusoidal steady state at frequency $\omega$:

**Complex power:** $\tilde S = \frac{1}{2}\hat e,\hat f^* = P + iQ_{reac}$

- $P = \text{Re}[\tilde S]$: **active power** (actually dissipated, time-averaged)
- $Q_{reac} = \text{Im}[\tilde S]$: **reactive power** (stored/returned each cycle)
- $|\tilde S|$: **apparent power**

**Power factor:** $\cos\phi = P/|\tilde S| = \text{Re}[Z]/|Z|$

For a pure R: $\phi = 0$, power factor = 1 (all power dissipated). For a pure L or C: $\phi = \pm 90°$, power factor = 0 (power oscillates, none dissipated).

**Engineering:** Electrical utilities charge for apparent power (kVA) but only deliver active power (kW). Low power factor means the utility must supply large currents for small useful power → line losses. Power factor correction capacitors reduce reactive current in inductive loads (motors) — a direct application of the impedance concepts above.

---

## 17.10 — The Bridge Zone: When Lumping Fails

### 17.10.1 — The Distributed-Parameter Models

When the lumping criterion is violated, the element must be modeled as a **distributed parameter system** — a PDE retaining spatial variation. The bridge zone models that sit between the Layer-2 PDEs (Ch. 15–16) and Layer-3 lumped elements:

|Lumped fails when|Bridge zone model|Governing equation|
|---|---|---|
|Electrical: $f > v_{em}/10L$|Transmission line|$\partial_{zz}V = L'C'\partial_{tt}V + R'C'\partial_t V$|
|Structural: $f > v_P/10L$|Euler-Bernoulli beam|$EI\partial_{xxxx}w + \rho A\partial_{tt}w = q$|
|Acoustic: $f > c_s/10L$|1D wave equation|$\partial_{tt}p = c_s^2\partial_{xx}p$|
|Thermal: $Bi > 0.1$|1D heat equation|$\partial_t T = \alpha\partial_{xx}T$|
|Hydraulic: $f > c_{water}/10L$|Water hammer equations|$\partial_{tt}p = c_w^2\partial_{xx}p$|

The transmission line and Euler-Bernoulli beam are the most important bridge zone models in engineering practice. Both retain spatial variation along one axis while lumping in the transverse directions.

### 17.10.2 — The Hierarchy: Layer 2 → Bridge Zone → Layer 3

```
Layer 2: Full PDE
(full 3D, all frequencies)
        │
        │ if L >> characteristic dimension (thin beam, long cable)
        ▼
Bridge zone: 1D PDE
(full spatial variation along primary direction)
        │
        │ if L/λ << 1 (lumping criterion satisfied)
        ▼
Layer 3: ODE / algebraic
(lumped element: R, L, C)
```

The engineer always works at the lowest layer valid for the problem. This chapter gives the explicit criteria for when to move up.

---

## 17.11 — The Complete Layer-3 Template

### 17.11.1 — The Four Engineering Disciplines as Instances

The effort-flow template, R/C/L elements, KCL/KVL analogs, and Thévenin/Norton equivalents constitute a complete mathematical framework. Each engineering discipline is one instantiation:

**EEE (Chapter 18):** Effort = voltage $V$; Flow = current $I$; $R$ = resistor; $C$ = capacitor; $L$ = inductor; KCL: $\sum I = 0$; KVL: $\sum V = 0$

**ME (Chapter 19):** Translational: Effort = force $F$; Flow = velocity $v$; $R$ = damper $b$; $C$ = spring $1/k$; $L$ = mass $m$ Rotational: Effort = torque $\tau$; Flow = angular velocity $\omega$; $R$ = friction; $C$ = torsional spring; $L$ = moment of inertia

**CE (Chapter 20):** Hydraulic: Effort = pressure $P$; Flow = volume flow $Q$; $R$ = pipe; $C$ = accumulator; $L$ = inertance Structural: Effort = force $F$; Flow = velocity $v$; $R$ = damping; $C$ = compliance; $L$ = mass

**ChE (Chapter 20):** Effort = chemical potential $\mu$; Flow = molar flow $\dot n$; $R$ = diffusion resistance; $C$ = vessel; energy balances close the system

### 17.11.2 — The Cross-Branch Identity

**Every second-order system in every domain satisfies:**

$$L\ddot q + R\dot q + q/C = e_{source}$$

with the same $\omega_0$, $\zeta$, $Q$, step response, Bode plot, and Thévenin/Norton equivalents.

**A PID controller** (Ch. 21 preview) doesn't know what domain it's in:

$$u(t) = K_p e(t) + K_i\int e,dt + K_d\dot e$$

The gains $K_p$, $K_i$, $K_d$ are tuned the same way whether the controlled variable is voltage, temperature, position, pressure, or concentration. Control theory operates at the level of the transfer function $H(s)$ — entirely above the physics. This is possible only because Bridge C has reduced all domains to the same mathematical object.

---

## 17.12 — Summary

Bridge C performed three operations:

|Step|Mathematical operation|Result|
|---|---|---|
|1. Integrate PDE over control volume|$\int_V(\partial_t\phi = D\nabla^2\phi)dV$|Flux in = rate of change|
|2. Invoke lumping criterion|$L/\lambda \ll 1$ or $Bi \ll 1$|Spatial uniformity assumed|
|3. Identify lumped parameters|$C = V$, $R = L/DA$|ODE with lumped R, C, L|

**The three laws of Layer 3:**

- Flow sum at every node = 0 (Noether conservation, KCL-type)
- Effort sum around every loop = 0 (potential structure, KVL-type)
- Element constitutive laws: $e = Rf$, $f = C\dot e$, $e = L\dot f$

**The universal result:** $L\ddot q + R\dot q + q/C = e_{source}(t)$ — the governing equation for every second-order engineering system in every physical domain.

---

## 17.13 — Engineering Thread

|Physics|Application|
|---|---|
|Lumping criterion $L/\lambda \ll 1$|When to use lumped circuit vs. transmission line; structural lumped mass vs. continuous beam|
|Effort-flow pairs|Hydraulic-electric analogy for system simulation; bond graph modeling|
|R, C, L in every domain|Cross-domain system modeling; multi-physics simulation (COMSOL, Simulink)|
|KCL/KVL analogs|Node and mesh analysis in all domains|
|Second-order ODE|Vibration design ($\omega_0$, $\zeta$ spec); filter design; control system stability|
|Overshoot $M_p = e^{-\pi\zeta/\sqrt{1-\zeta^2}}$|Structure settling time; amplifier stability margin; hydraulic ram design|
|Q factor and bandwidth|Resonator design; selectivity of filters; structural damping specification|
|Thévenin/Norton|Source-load matching; impedance matching in RF, audio, mechanical, acoustic|
|Power factor $\cos\phi$|Utility billing; power factor correction; reactive power management|
|Bond graphs|Multi-domain system modeling without domain-specific knowledge|
|Transfer function $H(s)$|Control system design; filter synthesis; structural FRF measurement|

---

## 17.14 — Looking Ahead: Layer 3 Chapters

Bridge C is complete. Layer 3 opens with the same template instantiated in each engineering discipline:

**Chapter 18 — EEE Systems:** Circuits, semiconductor devices, signals and systems. The electrical instantiation of the effort-flow template, with additional richness from nonlinear devices (diodes, transistors) built on Layer-1 physics (Ch. 6).

**Chapter 19 — ME Systems:** Machines, structures, thermofluid systems. The mechanical and thermal instantiation. Structural analysis using FEM (the discretized Navier equation, Ch. 15) and vibration design using the second-order template.

**Chapter 20 — CE and ChE Systems:** Structural systems, hydraulic networks, reactors, separations. The hydraulic and chemical instantiations.

**Chapter 21 — Feedback, Control, and the Cross-Branch Capstone:** PID control, transfer functions, stability criteria — the branch-agnostic mathematics that operates entirely at the level of the ODE, applying equally to all domains.

---

_End of Chapter 17. Bridge C complete. Layer 3 begins._

---

_Next: Chapter 18 — EEE Systems: Circuits, Devices, and Signals_