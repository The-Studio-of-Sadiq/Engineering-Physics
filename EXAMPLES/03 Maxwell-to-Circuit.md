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

**Step 3a — the transmission line (exact, before lumping).** For a line of
characteristic impedance $Z_0$ and phase velocity $v$:

$$\frac{\partial V}{\partial x} = -L'\frac{\partial I}{\partial t}\qquad \frac{\partial I}{\partial x} = -C'\frac{\partial V}{\partial t}$$

with $Z_0 = \sqrt{L'/C'}$ and $v = 1/\sqrt{L'C'}$. These are Maxwell's equations
with the transverse dimensions integrated out — **no approximation yet.**

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

KCL and KVL follow, and they are *not* extra postulates — they are
conservation:

$$\sum I_k = 0 \quad\left(\nabla\cdot\mathbf{J} = -\partial_t\rho \text{ integrated}\right)$$
$$\oint \mathbf{E}\cdot d\mathbf{l} = 0 \quad\left(\nabla\times\mathbf{E} = -\partial_t\mathbf{B} = 0 \text{ since quasi-static}\right)$$

**KVL is the electromagnetic loop law with the time derivative dropped.** That
is the whole cost of quasi-statics: Faraday's law is not violated, it is
suspended, and it reappears as the inductive term $L\dot I$ that the lumping
process put in by hand.

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
and $R_{eq} = 49.5\ \Omega$, giving $f_{-3\text{dB}} = 1.45$ MHz and a badly
distorted square wave. **The same design is correct or useless depending on a
load the circuit theory never mentions**, because the load is outside the
lumped element and only enters as a boundary condition.

This is the practical meaning of the lumping criterion: it is not a statement
about the circuit, it is a statement about the circuit *and its surroundings*.

---

## Step 6 — Validity limits

| Assumption | Fails when | Use instead |
|---|---|---|
| $L/\lambda \ll 1$ | Trace or interconnect length $\gtrsim \lambda/10$ | Transmission-line theory; scattering parameters |
| Quasi-static ($\dot B = 0$ in KVL) | Fast edges, high $dI/dt$ | Inductance must be retained explicitly; never "ideal" it away |
| Lumped geometry | Distributed sources, radiation, slots | Full-wave FEM (Ch. 16 §16.11) |
| Constant $\epsilon$, $\mu$ | Non-linear dielectrics, ferroelectrics | Non-linear capacitance; hysteresis |
| $R \gg 0$ | Superconductors, ideal conductors | $R=0$ gives a genuinely different topology (flux quantisation, Ch. 7 §7.8) |
| Frequency-independent $R$ | Skin effect, $f > R_{skin}$ | $Z(\omega)$, complex permittivity |

A worked confirmation of the first row: a 10 cm trace has
$\lambda/4 \approx 1.5$ cm at 500 MHz, so the lumping criterion is already
violated in ordinary FR-4 at ordinary signal rates. The "just wires" model is
an approximation with a hard frequency ceiling, and that ceiling is the reason
signal-integrity engineering exists as a discipline.

**What this example demonstrates.** Three of the four steps — integrate,
apply the divergence theorem, identify $L$ and $C$ — are exact. The entire
descent rests on one inequality, $L/\lambda \ll 1$, and everything the lumped
model cannot do (resonance, standing waves, radiation, propagation delay) is
recovered the moment that inequality fails.

---

**Model Ledger:** see [Ch. 16 §16.10](../CHAPTERS/CHAPTER%2016.md) and
[Ch. 17 §17.1.1](../CHAPTERS/CHAPTER%2017.md) for the nine-row ledgers recording
this reduction's assumptions, neglected physics, and failure modes.
