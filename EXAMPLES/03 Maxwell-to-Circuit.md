# Example 3 — Maxwell → Circuit

**A complete worked descent in six steps.**

**Source chapters:** [Ch. 11](../CHAPTERS/CHAPTER%2011.md) §§11.2–11.4 (Maxwell) →
[Ch. 16](../CHAPTERS/CHAPTER%2016.md) §§16.3.2, 16.10 (telegraph equation, lumping) →
[Ch. 17](../CHAPTERS/CHAPTER%2017.md) §§17.1–17.3 (R/C/L) → [Ch. 18](../CHAPTERS/CHAPTER%2018.md) (circuits)

**Question answered:** What exactly is thrown away when Maxwell's equations
become a circuit diagram?

---

## Step 1 — Theory

Maxwell's equations, in vacuum, in differential form:

$$\nabla\cdot\mathbf{E} = 0\qquad \nabla\times\mathbf{B} = \mu_0\epsilon_0\frac{\partial\mathbf{E}}{\partial t}\qquad \nabla\times\mathbf{E} = -\frac{\partial\mathbf{B}}{\partial t}\qquad \nabla\cdot\mathbf{B}=0$$

Take the curl of the Faraday–Ampère pair and use $\nabla\times(\nabla\times\mathbf{A}) = \nabla(\nabla\cdot\mathbf{A}) - \nabla^2\mathbf{A}$. On a source-free region, $\mathbf{E}$ and $\mathbf{B}$ both satisfy the wave equation:

$$\nabla^2\mathbf{E} = \mu_0\epsilon_0\frac{\partial^2\mathbf{E}}{\partial t^2},\qquad c = \frac{1}{\sqrt{\mu_0\epsilon_0}}$$

Maxwell did not assume light is electromagnetic. It fell out.

---

## Step 2 — Approximation

Circuit theory requires a **geometry** that Maxwell does not have. Three
assumptions must be added before any of this becomes a diagram:

| # | Assumption | Kind | Why it is needed |
|---|---|---|---|
| A | Quasi-static: $\ell \ll \lambda$, so $L/\lambda \ll 1$ | `[APPROXIMATION]` | lets $\nabla\to$ a difference over a lump length |
| B | Lumped geometry: a single path, a single pair of conductors | `[APPROXIMATION]` | a circuit element has one voltage and one current |
| C | Linear, instantaneous medium: $\epsilon$, $\mu$ constant | `[APPROXIMATION]` | makes $Q = CV$ and $\Phi = LI$ reversible, single-valued |

Assumption A is the one that fails first, and its failure is named: beyond
$L/\lambda \sim 1$ you have **transmission line** behaviour, where voltage is a
function of position, and the correct object is the telegrapher's equations, not
Kirchhoff's laws.

---

## Step 3 — Mathematical reduction

**Step 3a — the transmission line: an already-reduced distributed model.** For a
line with distributed (per-unit-length) parameters $R'$, $L'$, $G'$, $C'$:

$$\frac{\partial V}{\partial x} = -R'I - L'\frac{\partial I}{\partial t}\qquad \frac{\partial I}{\partial x} = -G'V - C'\frac{\partial V}{\partial t}$$

In the **lossless** case ($R' = G' = 0$), which is the form usually quoted:

$$\frac{\partial V}{\partial x} = -L'\frac{\partial I}{\partial t}\qquad \frac{\partial I}{\partial x} = -C'\frac{\partial V}{\partial t}, \qquad Z_0 = \sqrt{L'/C'},\qquad v = \frac{1}{\sqrt{L'C'}}$$

**Be precise about the epistemic status here, because "before lumping" is not the
same as "exact."** These are *not* Maxwell's equations verbatim with the transverse
dimensions integrated out. Getting here has already cost something: the transverse
field structure has been replaced by a single voltage and a single current (a
single-mode, quasi-TEM idealisation), $R'$, $L'$, $G'$, $C'$ are being treated as
constants lumped per unit length, and the conductor geometry is assumed benign
enough that the line can be described by distributed scalars at all. Each of those
is a modelling choice. What is exact is the *reduction* — once the line model is
granted, the relations below are consequences of it, which is why the $R$ and $G$
terms already present here reappear in step 3c without any new assumption.

**Step 3b — integrate over a segment of length $\ell$.** Exact, by the
divergence theorem:

$$\ell L'\frac{dI}{dt} = V(x) - V(x+\ell)\qquad \ell C'\frac{dV}{dt} = I(x) - I(x+\ell)$$

**Step 3c — invoke lumping.** If $\ell \ll \lambda$, the spatial differences
become derivatives scaled by $\ell$:

$$L\frac{dI}{dt} + RI = V,\qquad C\frac{dV}{dt} + G V = I$$

Step 3b is an identity. **Step 3c is the approximation** — and it is the entire
content of the descent. Note also that $L = L'\ell$, $C = C'\ell$, $R = \ell/(\sigma A)$:
the lumped parameters are *definitions by correspondence*, not derived
quantities.

---

## Step 4 — Reduced model

Three constitutive laws, one per element type:

| Element | Law | Energy | Physics |
|---|---|---|---|
| Resistor | $V = RI$ | dissipated, $I^2R$ | conductivity, scattering |
| Capacitor | $I = C\dot V$ | stored, $\tfrac12 CV^2$ | field energy, polarisation |
| Inductor | $V = L\dot I$ | stored, $\tfrac12 LI^2$ | magnetic field, inertia |

KCL and KVL follow, and they are *not* extra postulates — but each is a specific
conservation law, and KVL's identity in particular is usually mis-stated:

$$\sum_k I_k = 0 \qquad\text{(charge conservation: }\nabla\cdot\mathbf{J} = -\partial_t\rho\text{ integrated over a node)}$$

$$\sum_k V_k = 0 \qquad\text{(Faraday's law expressed in the lumped-element representation)}$$

**KVL is a loop statement about $\mathbf{E}$, not a statement about energy.** It is
Faraday's law $\oint\mathbf{E}\cdot d\mathbf{l} = -d\Phi_B/dt$, rewritten once every
branch has been assigned a terminal voltage — which is the content of the chain
below. Calling it "energy conservation" conflates two different laws: the
conservation of energy in the electromagnetic field is **Poynting's theorem**,

$$\frac{\partial}{\partial t}\left(u_{\rm em}\right) + \nabla\cdot\mathbf{S} = -\mathbf{J}\cdot\mathbf{E}, \qquad \mathbf{S} = \frac{1}{\mu_0}\mathbf{E}\times\mathbf{B}$$

which is a *local, volumetric* statement involving the energy density $u_{\rm em}$ and
the flux $\mathbf{S}$. KVL is an *integrated, topological* statement around a loop.

The two are related, but the relation runs through the circuit elements rather than
through identity: once the three constitutive laws of step 4 are substituted, the
resulting $RC$, $RL$ and $RLC$ equations do satisfy an energy balance — each element
either stores ($\tfrac12CV^2$, $\tfrac12LI^2$) or dissipates ($I^2R$). That
consistency is a *result* of the reduction, and a useful check on it. It is not what
KVL states.

**The correct chain is Faraday → flux linkage → induced EMF → KVL.** Start from

$$\oint\mathbf{E}\cdot d\mathbf{l} = -\frac{d\Phi_B}{dt}$$

In a lumped inductor, $\Phi_B$ is *proportional to the current* by construction — that
proportionality is the definition of the inductance, $L = N\Phi_B/I$. Differentiating
gives the terminal voltage of the inductor itself:

$$V_L = -\frac{d\Phi_B}{dt} = L\frac{dI}{dt}$$

(or $N\,d\Phi/dt$ for an $N$-turn coil). So the induced EMF **is** the inductor's
contribution to the loop sum, and Kirchhoff's voltage law is simply what that loop
integral becomes once every branch has been given a terminal voltage:

$$\oint\mathbf{E}\cdot d\mathbf{l} = \sum_k V_k \;\Longrightarrow\; \sum_k V_k = 0$$

**The thing to unlearn is the tempting shortcut** — "KVL is the loop law with the
time derivative dropped," i.e. $\nabla\times\mathbf{E} = -\partial_t\mathbf{B} = 0$.
That is wrong, and wrong in a self-defeating way: setting $\partial_t\mathbf{B} = 0$
is precisely the condition that makes $V_L = L\dot I = 0$. You would be deleting the
inductor in the act of deriving the law that has to accommodate it. The
quasi-static approximation in circuit theory does **not** mean the magnetic field
stops changing; it means the *radiation* and *displacement* effects can be neglected
so that $\mathbf{B}$ is slaved to $\mathbf{I}$ by the constitutive relation rather
than solved independently. The changing flux is not dropped — it is *accounted for*,
in the inductor term.

---

## Step 5 — Engineering equation

**Worked problem.** A 10 nF capacitor and a 2.2 kΩ resistor form an RC stage
driving a 1 MΩ oscilloscope input. What is the −3 dB bandwidth, and what does
the scope's loading do to it?

$$\tau = RC = 2.2\times 10^3 \times 10\times 10^{-9} = 22\ \mu\text{s}$$
$$f_{-3\text{dB}} = \frac{1}{2\pi\tau} = 7.2\ \text{kHz}$$

Now the loading. The scope presents 1 MΩ in parallel with the 2.2 kΩ:

$$R_{eq} = \frac{2.2\times 10^3 \times 10^6}{2.2\times 10^3 + 10^6} = 2.195\ \text{k}\Omega$$

A 0.2% change. Negligible — *because* 1 MΩ ≫ 2.2 kΩ. Swap in a 50 Ω scope input
and $R_{eq} = \frac{2.2\times 10^3 \times 50}{2.2\times 10^3 + 50} = 48.89\ \Omega$.
The source now sees a ~45:1 divider (2.2 kΩ into 50 Ω), so the signal reaching the
scope is attenuated ~45-fold, and the time constant collapses from 22 µs to
$48.89\times 10\times 10^{-9} = 0.49\ \mu$s, pushing
$f_{-3\text{dB}} = \frac{1}{2\pi \times 48.89 \times 10\times 10^{-9}} = 325$ kHz
— 45$\times$ *higher* than the designed corner. The design is no longer the
circuit that was analysed. **The same design is correct or useless depending on a
load the circuit theory never mentions**, because the load is outside the
lumped element and only enters as a boundary condition.

This is the practical meaning of the lumping criterion: it is not a statement
about the circuit, it is a statement about the circuit *and its surroundings*.

---

## Step 6 — Validity limits

| Assumption | Fails when | Use instead |
|---|---|---|
| $L/\lambda \ll 1$ | Trace or interconnect length $\gtrsim \lambda/10$ | Transmission-line theory; scattering parameters |
| Quasi-static ($V_L = L\dot I$ treated as lumped) | Fast edges, high $dI/dt$ | Retain distributed L explicitly; transmission-line or full-wave treatment |
| Lumped geometry | Distributed sources, radiation, slots | Full-wave FEM (Ch. 16 §16.11) |
| Constant $\epsilon$, $\mu$ | Non-linear dielectrics, ferroelectrics | Non-linear capacitance; hysteresis |
| $R \gg 0$ | Superconductors, ideal conductors | $R=0$ gives a genuinely different topology (flux quantisation, Ch. 7 §7.8) |
| Frequency-independent $R$ | Skin effect, $f > R_{skin}$ | $Z(\omega)$, complex permittivity |

A worked confirmation of the first row: on FR-4 ($\epsilon_r \approx 4$, effective
permittivity somewhat lower on microstrip, so $\epsilon_{eff}\approx 3$–3.5) a trace
on 500 MHz has a guided wavelength of only
$\lambda = c/(f\sqrt{\epsilon_{eff}}) \approx 0.32$–0.35 m, so
$\lambda/4 \approx 8$–9 cm. A 10 cm trace therefore exceeds a quarter wavelength —
$L/\lambda \approx 0.3$ — and the lumping criterion is already violated in ordinary
FR-4 at ordinary signal rates. The "just wires" model is an approximation with a
hard frequency ceiling, and that ceiling is the reason signal-integrity engineering
exists as a discipline.

**What this example demonstrates.** Three of the four steps — integrate,
apply the divergence theorem, identify $L$ and $C$ — are exact. The entire
descent rests on one inequality, $L/\lambda \ll 1$, and everything the lumped
model cannot do (resonance, standing waves, radiation, propagation delay) is
recovered the moment that inequality fails.

---

**Model Ledger:** see [Ch. 16 §16.10](../CHAPTERS/CHAPTER%2016.md) and
[Ch. 17 §17.1.1](../CHAPTERS/CHAPTER%2017.md) for the nine-row ledgers recording
this reduction's assumptions, neglected physics, and failure modes.
