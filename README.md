# Engineering Physics: Top Down

### A conceptual descent from fundamental fields to engineering systems

> **How far can you descend from fundamental physical principles before you reach the equations engineers use every day?**

This repository is a personal academic knowledge system that answers that question by following one connected chain of theories, approximations, and reductions: from the Standard Model and the Einstein–Hilbert action, through quantum, classical, and continuum physics, to the lumped models, circuits, machines, structures, reactors, and control systems that four engineering disciplines actually use. Its subject is not physics *or* engineering. It is the **chain of named reductions between them**, and the exact point at which each reduction stops being valid.

**The hierarchy represents a hierarchy of physical descriptions and approximations, not a claim that every higher-level theory has been quantitatively derived from fundamental physics.** Some connections in this book are exact mathematical reductions. Many are controlled approximations. Some are structural correspondences — two different systems sharing one piece of mathematics without one producing the other. A few are honest analogies, and some are phenomenological models fit to experiment. Every connection that carries weight is tagged so you always know which kind you are looking at.

---

## Core architecture

The descent is not a single vertical stack. It branches, runs in parallel, and reconverges — and the reconvergence points are the interesting part.

```
                        FUNDAMENTAL PHYSICS
                    L₀   fields, symmetries, action
                               │
                ┌──────────────┴──────────────┐
                ↓                             ↓
      QUANTUM FIELD THEORY            GENERAL RELATIVITY
      gauge, matter, θ-term            metric, curvature
                │                             │
                └──────────────┬──────────────┘
                               ↓
                    ── BRIDGE A ──
              single particle,  E ≪ mc²,  v ≪ c
                               ↓
                    QUANTUM PHYSICS
              L₁   wavefunctions, atoms, bands, nuclei
                               │
        ┌──────────────────────┼──────────────────────┐
        ↓                      ↓                      ↓
     MATTER               SCATTERING               FIELDS
   orbitals, bands     S-matrix, rates 1/τ      Berry phase, Chern
   bonding, nuclei     phonons, defects         topological bands
        │                      │                      │
        └──────────────────────┼──────────────────────┘
                               ↓
                    ── BRIDGE B ──
        four named limits, applied simultaneously, not one at a time:
         ħ→0  ·  N→∞  ·  classical EM field  ·  weak-field  ·  Kubo
                               ↓
              STATISTICAL / CLASSICAL PHYSICS
              L₂   Newton · Maxwell · thermo · continuum
                               │
        ┌──────────────────────┼──────────────────────┐
        ↓                      ↓                      ↓
    MECHANICS                 EM                THERMODYNAMICS
   N-body, rigid body      Maxwell, waves       laws, ensembles
   elasticity, fluids      optics, circuits    transport, phase
        │                      │                      │
        └──────────────────────┼──────────────────────┘
                               ↓
                    CONTINUUM PHYSICS
              PDEs: Navier–Stokes, elasticity,
              wave, diffusion, Maxwell
                               │
                    ── BRIDGE C ──
        control-volume integration, spatial discretisation,
         lumping, linearisation   (criterion: domain-specific — L≪λ, Bi≪1, modal separation)
                               ↓
        ┌──────────────────────┼──────────────────────┐
        ↓                      ↓                      ↓
       PDE                 FEM / discretised       NETWORK models
   retained as PDE      stiffness, FD, FEM      R/C/L in every domain
                               │                      │
        └──────────────────────┼──────────────────────┘
                               ↓
                   ENGINEERING SYSTEMS
                     L₃   effort / flow pairs
                               │
       ┌───────────┬───────────┼───────────┬───────────┐
       ↓           ↓           ↓           ↓           ↓
    Electrical  Mechanical   Civil     Chemical    Control
      (Ch 18)     (Ch 19)    (Ch 20)     (Ch 20)    (Ch 21)
```

Two features of this diagram carry the argument:

- **The reconvergence is real.** Several apparently independent fundamental threads — gauge structure, gravity, quantum statistics, scattering, and field topology — converge on a small set of classical continuum descriptions used throughout engineering. The Generalized Transport Law (Ch. 13) is where this is stated most sharply: Ohm, Fourier, Fick and Newton viscosity are instances of one linear-response framework with different operators and closures, while Hooke's law enters only as a static limit. This is a shared *framework*, not one calculation producing five results.
- **The four engineering branches reconverge too.** They are not four subjects that happen to share methods. They are four choices of effort/flow pair, instantiated on one R/C/L template — a statement about representations rather than about shared physics, and strongest exactly where the lumping criterion holds. Chapters 18–21 are the proof of concept for everything Chapters 0–17 set up.

The full tagged version of this graph — every arrow labelled, every discarded term named — is in the [Master Map](METADATA/00%20Map.md).

---

## Layers and bridges

| | Name | What happens |
|---|---|---|
| **L₀** | Framework | $S_{\text{eff}} = S_{EH} + S_{SM} + S_{\text{unknown}}$, with $S_{\text{unknown}} \equiv \int d^4x\,\sqrt{-g}\,\mathcal{F}[\ldots]$ — the best available framework, with an explicit placeholder for what we do not know. Canonical form: Ch. 0 §0.10 |
| **A** | Bridge A | Isolate matter fields; take $E \ll mc^2$, $v \ll c$. Bridge zone: the Dirac equation and the Foldy–Wouthuysen expansion |
| **L₁** | Quantum / atomic | Wavefunctions, spin, exchange, atoms, molecules, bands, nuclei, quantum scattering, topology |
| **B** | Bridge B | Four simultaneous descents: $\hbar\to0$ (classical mechanics), $N\to\infty$ (statistical mechanics), classical $U(1)$ (Maxwell), weak-field metric (Newton). Plus Kubo linear response (transport) |
| **L₂** | Classical continuum & statistical | Lagrangian and Hamiltonian mechanics, thermodynamics, electromagnetism, fluid mechanics, elasticity, heat and mass transfer, wave and diffusion equations |
| **C** | Bridge C | Integrate the L₂ PDEs over control volumes; discretise; lump. Bridge zone: transmission lines, Euler–Bernoulli beams |
| **L₃** | Engineering systems | Electrical, mechanical/thermal, civil, chemical — and the control abstraction that unifies them |

---

## Chapter map

| Chapter | Subject | Layer |
|---|---|---|
| 00 | The equation; the whole architecture; the five cross-layer threads | L₀ |
| 01 | The action principle and the mathematical machinery | L₀ |
| 02 | Phenomena catalogue — the index of everything the book explains, and where it is explained | — |
| 03 | **Bridge A** — Dirac → Schrödinger → Pauli, via the Foldy–Wouthuysen expansion | A |
| 04 | Schrödinger equation; hydrogen; the ladder of bound states | L₁ |
| 05 | Spin, exchange statistics, many-electron atoms, the periodic table | L₁ |
| 06 | Bonding, band theory, nuclear physics, fission and fusion | L₁ |
| 07 | Topology — Berry phase, Chern numbers, quantum Hall, superconductivity | L₁ |
| 08 | **Bridge B.d** — GR → Newton's law; the measurable corrections | B |
| 09 | **Bridge B.a** — quantum mechanics → classical mechanics | B |
| 10 | **Bridge B.b** — quantum statistics → statistical mechanics and thermodynamics | B |
| 11 | **Bridge B.c** — classical $U(1)$ → Maxwell's equations | B |
| 12 | Electromagnetic waves, optics, waveguides, photonics | L₂ |
| 13 | **Bridge B.e** — Kubo → the Generalized Transport Law *(the convergence chapter)* | B |
| 14 | Sensors, semiconductor devices, thermal and electrical metrology | L₂ |
| 15 | Fluid mechanics: Navier–Stokes, viscous flow, dimensional analysis, turbulence | L₂ |
| 16 | Solid and continuum mechanics: elasticity, waves, FEM discretisation, PDE forms | L₂ |
| 17 | **Bridge C** — the R/C/L template, effort/flow pairs, distributed-parameter models | C |
| 18 | Electrical engineering systems: circuits, AC, power, machines, signals | L₃ |
| 19 | Mechanical and thermal systems: dynamics, machines, heat transfer, fluids, acoustics | L₃ |
| 20 | Civil and chemical systems: structures, hydraulics, geotechnics, reactors, separations | L₃ |
| 21 | Feedback, control, and the cross-branch capstone | L₃ |
| — | Epilogue — the unfinished equation, and what the unknown sector $\mathcal{F}[\ldots]$ still hides | — |

Chapters 18–21 are the load-bearing part. Without them this is an unconventional physics textbook; with them it is a physics-to-engineering abstraction framework.

**Worked demonstrations** of single descents, end to end, are in [`EXAMPLES/`](EXAMPLES/) — each one takes a starting theory, names the approximation, shows the reduction, lands on the engineering equation, and states the validity limits.

---

## How connections are marked

Every load-bearing arrow in this book carries one of five tags. This is the mechanism that prevents the central failure mode of interdisciplinary writing — confusing *"these equations have the same mathematical structure"* with *"these phenomena have the same physical origin."*

| Tag | Meaning |
|---|---|
| `[DERIVATION]` | An exact or controlled mathematical reduction. Apply calculus under the stated assumptions and this follows. |
| `[APPROXIMATION]` | Obtained by dropping terms under an explicit, named limit. The small parameter and the regime are stated. |
| `[STRUCTURAL CONNECTION]` | Two different physical systems obey the same mathematics because both are instances of one underlying mathematical object — not because one causes the other. |
| `[ANALOGY]` | A conceptual correspondence for intuition or pedagogy. Not identity. |
| `[PHENOMENOLOGICAL]` | Form or parameters come from experiment or an effective theory, not from a controlled derivation. |

Applied inline, a tag is a blockquote attached to the equation it qualifies:

> **[APPROXIMATION]** Dirac equation → nonrelativistic expansion in $(v/c)^2$ → Pauli equation, retaining the Zeeman and spin–orbit terms to order $(v/c)^2$.

> **[STRUCTURAL CONNECTION]** An electrical RC network and a thermal RC network obey the same lumped first-order form, $C_x\,dx/dt=(x_{in}-x)/R_x$, with $x=V$ and $C_x=C$ for the electrical case and $x=T$ and $C_x=\rho c_p V$ for the thermal case. Same differential-equation structure, different physical variables, constitutive parameters, and energy-storage mechanisms.

---

## Model validity

The book's central rule:

> **Every useful engineering model has a domain of validity.**

A model is never presented as an isolated equation. At every major model transition the book records a **Model Ledger**:

| Property | Description |
|---|---|
| Parent theory | The deeper model this came from |
| Reduction | The named operation or limit applied |
| Assumptions | What must hold for the reduction to be legal |
| Retained | The physics that survives |
| Neglected | The physics that was discarded |
| Valid when | The regime where the model is trustworthy |
| Fails when | The regime where it must be replaced |
| Next model | What to reach for when it fails |

```text
Parent theory       3D elastodynamics (Ch. 15, 16)
Reduction           slender-beam assumption,  L / r ≫ 1
Model               Euler–Bernoulli beam,  EI ∂⁴w/∂x⁴ = q
Retained            bending deformation
Neglected          transverse shear deformation, rotary inertia
Valid when          slender, low-frequency, small-deflection
Fails when          thick beams (L/r ≲ 10), or high-frequency
Next model          Timošenko beam theory
```

The goal is to make **model selection** part of learning physics and engineering: not *what is the equation* but *what was assumed, what was thrown away, and when does it stop working.*

---

## How to navigate

**Sequential** — the intended descent:

```text
Master Map  →  Chapter 0  →  Chapter 1  →  …  →  Chapter 21  →  Epilogue
```

> [!note] Two different "0" documents
> The **Master Map** (`METADATA/00 Map.md`) is navigation and provenance — the
> dependency graph, tagged arrows, and break points. It is not part of the
> conceptual sequence. **Chapter 0** (`CHAPTERS/CHAPTER 0.md`) is the first
> chapter of the descent, where the action and the Mexican hat are introduced.
> They are numbered in different systems and are easy to confuse; "Chapter 0"
> always means the chapter.

**Reverse** — start from an equation you use at work and walk it backwards to its origin. This is the more useful direction for a working engineer:

```text
PID gain tuning
      ↓
transfer function
      ↓
lumped ODE
      ↓
PDE / conservation law
      ↓
Noether's theorem
      ↓
U(1) gauge invariance
```

**Single descent** — one chain, fully worked, with validity limits: see [`EXAMPLES/`](EXAMPLES/).

Conventions used throughout: SI units; standard mathematical notation; approximation limits stated where relevant; dimensional consistency maintained; sign conventions stated where they affect the result. There is no equation numbering — cross-references are by chapter and section, e.g. *"Ch. 16 §16.7.2"*.

---

## Status

**Physics Core — Chapters 0–21 + Epilogue. The architecture is frozen at 21 chapters.**

The chapter count will not grow. What the project needs now is rigour, not breadth:

- [x] Four-layer architecture, three named bridges, five cross-layer threads
- [x] Chapters 0–21 and the Epilogue
- [x] Connection-type tagging applied at load-bearing transitions
- [x] Model Ledgers on the major model transitions
- [x] `REFERENCES.md` — load-bearing claims traced to sources, with unverified items flagged rather than guessed
- [x] `EXAMPLES/` — worked single-descent demonstrations
- [ ] Extend tagging coverage to the remaining heuristic sections
- [ ] Pin CODATA / PDG citations to fixed dataset editions
- [ ] Second-pass verification of Chapters 16, 17, 19, 20 against primary sources

Read it as a **research and study map**, not as an authoritative replacement for specialist textbooks. The detailed conceptual argument — every layer expanded, every discarded term named, every arrow tagged — lives in [`00 Map.md`](METADATA/00%20Map.md). Writing rules for extending it are in [`AUTHORING.md`](CONTRIBUTING.md).

---

## License

**Copyright © 2026 Golam Kuadir Khan Prince.**

Licensed under the **Creative Commons Attribution 4.0 International License (CC BY 4.0)**. The full legal text is in [`LICENSE`](LICENSE).

You are free to share and adapt this work, including commercially, provided you give appropriate credit, indicate whether changes were made, and link to the license. The license does not cover patent or trademark rights.
