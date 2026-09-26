# EEE Systems: Circuits, Devices, and Signals

### The Electrical Instantiation of Layer 3

---

> _A circuit is Maxwell's equations with the spatial variation averaged out._ _Everything else is bookkeeping — elegant, powerful bookkeeping,_ _but bookkeeping nonetheless._ — teaching tradition in electrical engineering

---

## 18.0 — Overview

Chapter 17 established the universal Layer-3 template: effort and flow, R/C/L in every domain, KCL-type and KVL-type conservation at every node and loop, and the second-order ODE as the governing equation for every system.

This chapter instantiates that template in the electrical domain. Every concept introduced here already appeared in some form in earlier chapters:

|Ch. 18 concept|Physics origin|
|---|---|
|KCL, KVL|Maxwell quasi-static (Ch. 11 §11.12); Noether U(1) (Ch. 1 §1.7)|
|Impedance $Z(\omega)$|Ch. 17 §17.6 universal definition|
|Diode IV characteristic|p-n junction drift-diffusion (Ch. 6, Ch. 14)|
|MOSFET operation|Band bending, inversion layer (Ch. 6 §6.6)|
|Filter transfer function|Dispersion relation (Ch. 16 §16.4); second-order system (Ch. 17 §17.7)|
|Fourier/Laplace analysis|Plane wave decomposition (Ch. 16 §16.4); eigenmodes (Ch. 16 §16.5)|
|Sampling theorem|Nyquist from Ch. 16 (spatial frequencies → bandwidth)|
|Power electronics|Ohm + Faraday + Kirchhoff (Ch. 11) + control (Ch. 21 preview)|

This chapter is not a replacement for a full circuits course. It is the systematic connection of that course's material to the physics that underlies it.

---

## 18.1 — Circuit Analysis: Maxwell's Equations in Lumped Form

### 18.1.1 — The Two Laws, Their Origins

**Kirchhoff's Current Law (KCL):**

At any node, $\sum_k I_k = 0$, where positive convention is defined per branch.

Origin (Ch. 11 §11.12): The continuity equation $\partial_t\rho + \nabla\cdot\mathbf{J} = 0$ integrated over the node volume, with quasi-static assumption $\partial_t\rho \to 0$: $$\oint_{\partial V}\mathbf{J}\cdot d\mathbf{A} = 0 \quad\Longrightarrow\quad \sum_k I_k = 0$$

KCL is charge conservation (Noether U(1)) applied to a lumped node.

**Kirchhoff's Voltage Law (KVL):**

Around any closed loop, $\sum_k V_k = 0$.

Origin (Ch. 11 §11.12): Faraday's law $\oint\mathbf{E}\cdot d\mathbf{l} = -d\Phi_B/dt$ with quasi-static assumption ($d\Phi_B/dt \approx 0$ for circuits much smaller than the electromagnetic wavelength): $$\sum_k V_k = -\frac{d\Phi_B}{dt} \approx 0$$

KVL fails when magnetic flux through the loop changes significantly — i.e., when inductors are not lumped or at high frequencies where the distributed transmission line model (Ch. 12 §12.7) must be used.

### 18.1.2 — Nodal Analysis

Apply KCL to each non-reference node. Express all currents in terms of node voltages using Ohm's law:

$$I = \frac{V_a - V_b}{R} = (V_a - V_b)G$$

For $n$ nodes (one chosen as reference/ground), this gives $(n-1)$ equations in $(n-1)$ unknowns. In matrix form:

$$\mathbf{G}\mathbf{v} = \mathbf{i}_s$$

where $\mathbf{G}$ is the **conductance matrix** (nodal admittance matrix):

- $G_{kk} = \sum$ (all conductances connected to node $k$)
- $G_{jk} = G_{kj} = -\sum$ (all conductances between nodes $j$ and $k$)

**Nodal analysis with impedances** (AC): Replace $G$ with admittance $Y = 1/Z$ and work in phasors.

### 18.1.3 — Mesh Analysis

Apply KVL to each independent mesh (closed loop). Express all voltages using Ohm's law with mesh currents. For $m$ independent meshes:

$$\mathbf{Z}\mathbf{i}_{mesh} = \mathbf{v}_s$$

where $\mathbf{Z}$ is the **impedance matrix** (mesh impedance matrix):

- $Z_{kk} = \sum$ (all impedances in mesh $k$)
- $Z_{jk} = Z_{kj} = -\sum$ (all impedances shared between meshes $j$ and $k$)

**When to use which:** Nodal analysis works for any topology; mesh analysis is easier when there are more nodes than meshes or for planar circuits. For systematic computer-aided analysis: modified nodal analysis (MNA) handles voltage sources, op-amps, and other elements naturally.

### 18.1.4 — Superposition and Linearity

From the linearity of Maxwell's equations (Ch. 11): the response of a linear circuit to multiple independent sources equals the sum of responses to each source individually (all others killed: voltage sources → short circuits, current sources → open circuits).

**Superposition fails for:** nonlinear elements (diodes, transistors operating in nonlinear region), circuits with dependent sources that depend on the full combined response.

### 18.1.5 — Thévenin and Norton: Engineering Application

From Ch. 17 §17.8:

**Finding $V_{Th}$:** Remove the load; calculate the open-circuit voltage at the terminals.

**Finding $R_{Th}$ (or $Z_{Th}$ in AC):** Kill all independent sources (voltage sources → short, current sources → open); calculate the resistance (or impedance) seen at the terminals.

**Systematic method (with dependent sources):** Apply a test voltage $V_t$, calculate the resulting current $I_t$ → $R_{Th} = V_t/I_t$.

**Maximum power transfer:** $$R_L = R_{Th} \quad\Longrightarrow\quad P_{max} = \frac{V_{Th}^2}{4R_{Th}}$$

**Engineering use:** Every measurement instrument (voltmeter, oscilloscope, current probe) has an input impedance. The Thévenin/Norton framework tells you exactly how much the instrument loads the circuit being measured.

---

## 18.2 — AC Analysis: Phasors, Impedance, Power

### 18.2.1 — Phasor Representation

For a linear circuit driven by sinusoidal sources at frequency $\omega$, all voltages and currents are sinusoidal at the same frequency (by superposition and linearity):

$$v(t) = |V|\cos(\omega t + \phi_V) = \text{Re}[\underbrace{|V|e^{j\phi_V}}_{\tilde V}\cdot e^{j\omega t}]$$

The **phasor** $\tilde V = |V|e^{j\phi_V} = V_R + jV_I$ is a complex number encoding amplitude and phase. All circuit analysis reduces to complex algebra:

- KCL: $\sum_k\tilde I_k = 0$ (complex equation, equivalent to 2 real equations)
- KVL: $\sum_k\tilde V_k = 0$
- Ohm's law: $\tilde V = Z(\omega)\tilde I$ (complex impedance)

### 18.2.2 — Complex Power

For phasors $\tilde V$ and $\tilde I$:

$$\tilde S = \frac{1}{2}\tilde V\tilde I^* = P + jQ_{reac}$$

- **Active power** $P = \frac{1}{2}|\tilde V||\tilde I|\cos\phi$ [W] — time-averaged power dissipated
- **Reactive power** $Q_{reac} = \frac{1}{2}|\tilde V||\tilde I|\sin\phi$ [VAr] — power oscillating between source and reactive elements
- **Apparent power** $|\tilde S|$ [VA] — magnitude of complex power
- **Power factor** $\text{PF} = \cos\phi = P/|\tilde S|$

**Power factor correction:** An inductive load (motor, transformer) has $\phi > 0$ (lagging current), $Q_{reac} > 0$. Adding shunt capacitance $C_{pf} = Q_{reac}/\omega V_{rms}^2$ brings $\phi\to 0$, reducing the current the utility must supply for the same useful power.

### 18.2.3 — Resonance

**Series RLC** (from Ch. 17 §17.7.4):

$$Z(\omega) = R + j\omega L + \frac{1}{j\omega C} = R + j\left(\omega L - \frac{1}{\omega C}\right)$$

At resonance $\omega = \omega_0 = 1/\sqrt{LC}$: $\text{Im}[Z] = 0$, $|Z| = R$ (minimum). Maximum current flows; voltage across R equals source voltage.

Voltage magnification across L or C: $|V_L| = |V_C| = Q\cdot|V_{source}|$

**Parallel RLC:** Dual of series. At resonance: maximum impedance $= R_{p}$, minimum current from source. Used in bandpass filters, tank circuits.

---

## 18.3 — Semiconductor Devices: Physics to Circuit Models

### 18.3.1 — The p-n Junction Diode

From Ch. 14 §14.5.4 (drift-diffusion) and Ch. 6 §6.6 (doping):

**IV characteristic:** $$I_D = I_0\left(e^{V_D/\eta V_T} - 1\right)$$

where $I_0$ is the reverse saturation current, $\eta = 1$–$2$ is the ideality factor (1 for diffusion-dominated, 2 for recombination-dominated), and $V_T = k_BT/e \approx 26$ mV at 300 K.

**Operating regions:**

|Region|Condition|$I_D$|Application|
|---|---|---|---|
|Forward bias|$V_D > 0$|Exponentially increasing|Rectification, LED, laser|
|Reverse bias|$V_D < 0$|$\approx -I_0$ (tiny)|Blocking|
|Breakdown|$V_D < -V_{BR}$|Large (controlled for Zener)|Voltage reference, protection|

**Small-signal model** (for AC analysis around DC bias point $I_{DQ}$):

$$r_d = \frac{\partial V_D}{\partial I_D}\bigg|_{I_{DQ}} = \frac{\eta V_T}{I_{DQ}}$$

The diode becomes a resistor $r_d$ for small AC signals. At $I_{DQ} = 1$ mA: $r_d = 26;\Omega$ (η=1). At 10 mA: $r_d = 2.6;\Omega$.

**Junction capacitance:** The depletion region is a capacitor: $$C_j = C_{j0}\left(1 - \frac{V_D}{\phi_B}\right)^{-m}$$

where $\phi_B \approx 0.7$ V is the built-in potential and $m \approx 0.33$–$0.5$. Reverse bias increases depletion width → decreases $C_j$ (varactor diode, used in voltage-controlled oscillators and RF tuners).

### 18.3.2 — The Bipolar Junction Transistor (BJT)

An NPN BJT is two back-to-back p-n junctions (Emitter-Base-Collector).

**Active region operation** ($V_{BE} \approx 0.7$ V, $V_{CE} > V_{CE,sat}$):

$$I_C = \beta I_B = I_S e^{V_{BE}/V_T}$$

where $\beta = h_{FE}$ is the current gain (50–500 typical) and $I_S$ is the saturation current (from the drift-diffusion physics, Ch. 14 §14.5.3).

**Ebers-Moll model** (physics-based): connects directly to Ch. 14 minority carrier diffusion — the collector current is the minority carrier current injected from the emitter base junction and collected at the collector junction.

**Hybrid-π small-signal model:**

```
    B ──┬──── rπ ────┬──── C
        │            │
       Cπ          gm·Vπ (controlled current source)
        │            │
    E ──┴────────────┴──── E
```

Key parameters:

- $g_m = I_C/V_T$ (transconductance, from diode equation)
- $r_\pi = \beta/g_m = \beta V_T/I_C$ (input resistance)
- $r_o = V_A/I_C$ (Early voltage)
- $C_\pi + C_\mu$ (junction capacitances, from depletion region physics)

**Common-emitter amplifier:** $$A_v = -g_m R_C \approx -\frac{R_C}{r_d} = -\frac{I_C R_C}{V_T}$$

Voltage gain is proportional to $I_C R_C/V_T$ — the ratio of the DC voltage drop across $R_C$ to the thermal voltage. At $I_C R_C = 5$ V: $A_v = -192$.

### 18.3.3 — The MOSFET

An enhancement-mode NMOS transistor has a p-type substrate with an oxide layer (gate dielectric) and n+ source/drain regions. Applying $V_{GS} > V_{th}$ inverts the surface, creating an n-type channel (inversion layer, from Ch. 6 §6.6 Fermi level above conduction band edge at the surface).

**Saturation region** ($V_{GS} > V_{th}$, $V_{DS} > V_{GS} - V_{th}$):

$$I_D = \frac{\mu_n C_{ox} W}{2L}\left(V_{GS} - V_{th}\right)^2(1 + \lambda V_{DS})$$

where $C_{ox} = \epsilon_{ox}/t_{ox}$ is the gate oxide capacitance per area (from $t_{ox}$: oxide thickness), $W/L$ is the width-to-length ratio, and $\lambda$ is the channel length modulation parameter.

**Connection to physics:** $\mu_n C_{ox}$ traces directly to:

- $\mu_n$: electron mobility in the inversion layer (from scattering, Ch. 6 §6.4)
- $C_{ox}$: parallel-plate capacitance of gate oxide ($\epsilon_{ox}/t_{ox}$)
- $V_{th}$: threshold voltage from Fermi level alignment (Ch. 6 §6.5.2)

**Small-signal model:**

$$g_m = \frac{\partial I_D}{\partial V_{GS}} = \sqrt{2\mu_n C_{ox}\frac{W}{L}I_D} = \frac{2I_D}{V_{GS}-V_{th}}$$

**Common-source amplifier:** $$A_v = -g_m R_D$$

**CMOS inverter** (complementary NMOS + PMOS):

- Input HIGH ($V_{in} = V_{DD}$): NMOS ON, PMOS OFF → output LOW
- Input LOW ($V_{in} = 0$): NMOS OFF, PMOS ON → output HIGH
- Static power dissipation: near zero (only leakage current)
- Dynamic power dissipation: $P_{dyn} = \alpha C_L V_{DD}^2 f$ (switching only) where $\alpha$ is the activity factor, $C_L$ is the load capacitance

**Scaling (Moore's Law physics):** As $L$ decreases, $\mu_n C_{ox}/L$ increases → faster switching. But: short-channel effects, gate leakage (tunneling through thin oxide, Ch. 4 §4.4), drain-induced barrier lowering (DIBL) — all quantum effects that break the simple model. This is where Layer-1 physics (Ch. 6, 7) re-enters EEE practice.

---

## 18.4 — Operational Amplifiers

### 18.4.1 — The Ideal Op-Amp

A differential amplifier with:

- Open-loop gain: $A_{OL}\to\infty$
- Input impedance: $R_{in}\to\infty$
- Output impedance: $R_{out}\to 0$
- Infinite bandwidth (for ideal)

**The two golden rules** (valid with negative feedback):

1. $V_+ = V_-$ (virtual short: the feedback keeps the input differential voltage negligible)
2. $I_+ = I_- = 0$ (no current into the input terminals)

These rules follow from $A_{OL}\to\infty$ and negative feedback — they are not approximations when both conditions hold.

### 18.4.2 — Standard Op-Amp Configurations

**Inverting amplifier:**

```
         Rf
    ┌────┤├────┐
    │    R1    │
Vin ──┤├──────── V- ─── Vout
                │
               V+ (grounded)
```

Applying golden rules: $V_- = V_+ = 0$ (virtual ground); $I_{Rf} = I_{R1}$:

$$\frac{0 - V_{out}}{R_f} = \frac{V_{in} - 0}{R_1} \quad\Longrightarrow\quad \boxed{A_v = -\frac{R_f}{R_1}}$$

**Non-inverting amplifier:** $A_v = 1 + R_f/R_1$

**Voltage follower:** $A_v = 1$ (Rf = 0, R1 = ∞); presents high-Z input to source, low-Z to load — the buffer.

**Summing amplifier:** $$V_{out} = -R_f\left(\frac{V_1}{R_1} + \frac{V_2}{R_2} + \cdots\right)$$

**Integrator** (C replaces Rf): $$V_{out} = -\frac{1}{RC}\int V_{in},dt \quad\Longrightarrow\quad H(s) = -\frac{1}{sRC}$$

**Differentiator** (C replaces R1): $$V_{out} = -RC\frac{dV_{in}}{dt} \quad\Longrightarrow\quad H(s) = -sRC$$

These directly implement the integration/differentiation operations from Ch. 16 (PDE solutions) and Ch. 21 (PID control).

### 18.4.3 — Real Op-Amp Limitations

**Gain-bandwidth product (GBW):** For a single-pole op-amp: $$A_{OL}(f) = \frac{A_{DC}}{1 + jf/f_p} \quad\Longrightarrow\quad |A_v|_{closed}\cdot B_{3dB} = \text{GBW}$$

Closed-loop gain × bandwidth = constant. Gain of 100 → bandwidth = GBW/100. Typical GBW: 1 MHz (general purpose), 100 MHz (high speed), GHz (RF op-amps).

**Slew rate:** Maximum $dV_{out}/dt$ (limits large-signal performance): For $V_{out} = V_{pk}\sin(2\pi ft)$: maximum $dV/dt = 2\pi f V_{pk}$. Full power bandwidth: $f_{FP} = SR/(2\pi V_{pk})$.

**Offset voltage** $V_{OS}$: Small DC voltage at input (mismatch in input pair); amplified by closed-loop gain. Nulled by external trim or digital calibration.

---

## 18.5 — Filters: Frequency-Selective Systems

### 18.5.1 — Filter Specifications

From Ch. 17 §17.6.2: the transfer function $H(s)$ characterizes any linear system. A filter is a system designed to have a specific $|H(j\omega)|$ shape:

- **Low-pass (LPF):** Pass $\omega < \omega_c$, attenuate $\omega > \omega_c$
- **High-pass (HPF):** Pass $\omega > \omega_c$, attenuate $\omega < \omega_c$
- **Band-pass (BPF):** Pass $\omega_1 < \omega < \omega_2$
- **Band-stop (BSF/Notch):** Block $\omega_1 < \omega < \omega_2$

Specifications:

- Passband ripple: how much $|H|$ varies in the passband
- Stopband attenuation: minimum rejection in the stopband
- Transition band: slope of the transition from pass to stop

### 18.5.2 — First-Order RC Filter

The simplest LPF (RC with output across C):

$$H(s) = \frac{1/sC}{R + 1/sC} = \frac{1}{1+sRC} = \frac{1}{1+s/\omega_c}$$

where $\omega_c = 1/RC$ is the $-3$ dB cutoff frequency.

**Bode plot:** Flat at 0 dB below $\omega_c$; rolls off at $-20$ dB/decade above. Phase: $-45°$ at $\omega_c$; approaches $-90°$ asymptotically.

**Physical origin:** The RC time constant $\tau = RC$ is the thermal RC from Ch. 14 §14.7.3 in the electrical domain. The same equation, the same time constant, the same first-order step response $V_C(t) = V_{in}(1-e^{-t/RC})$.

### 18.5.3 — Classical Filter Approximations

**Butterworth** (maximally flat magnitude): $$|H_n(j\omega)|^2 = \frac{1}{1+(\omega/\omega_c)^{2n}}$$

- Monotonically decreasing $|H|$; no ripple anywhere
- $-20n$ dB/decade rolloff in stopband
- Poles equally spaced on left half-circle of radius $\omega_c$

**Chebyshev Type I** (equiripple passband):

- Steeper rolloff than Butterworth for same order
- Ripple $\delta_{p}$ dB in passband; monotonic in stopband
- Better selectivity; worse transient response (phase nonlinearity)

**Bessel** (maximally flat group delay):

- Group delay $\tau_g = -d\angle H/d\omega$ = const in passband
- Preserves pulse shape (no dispersion)
- Poorest amplitude selectivity
- Used in audio, radar pulse shaping, medical waveform preservation

**Elliptic (Cauer):** Ripple in both passband and stopband; most efficient (narrowest transition band for given order) — used when component count matters.

### 18.5.4 — Active Filters: Op-Amp Implementation

**Sallen-Key second-order LPF:**

```
Vin ─── R ─── R ─── Vout
             │
             C     (op-amp voltage follower: A=1)
             │
           ──┤├── C
```

Transfer function: $$H(s) = \frac{\omega_0^2}{s^2 + (\omega_0/Q)s + \omega_0^2}$$

with $\omega_0 = 1/RC$ and $Q$ adjustable by varying component values. No inductors needed — inductors are bulky, lossy, and non-integrable at audio and signal processing frequencies. Op-amp active filters replace them with R, C, and controlled sources.

**Higher-order filters:** Cascade second-order sections. An $n$-th order Butterworth is cascaded from $n/2$ Sallen-Key sections.

**Connection to Ch. 16:** A filter is a frequency-selective wave propagation device — it implements a chosen dispersion relation $\omega(k)$ in the frequency domain. The poles of $H(s)$ are the complex natural frequencies of the system — exactly the eigenfrequencies from Ch. 16 §16.5.

---

## 18.6 — Fourier Analysis: Signals in Frequency Domain

### 18.6.1 — Fourier Series

A periodic signal $x(t)$ with period $T_0$ (fundamental frequency $f_0 = 1/T_0$):

$$x(t) = \sum_{n=-\infty}^{\infty} c_n e^{jn\omega_0 t}, \qquad c_n = \frac{1}{T_0}\int_0^{T_0}x(t)e^{-jn\omega_0 t},dt$$

**Connection to Ch. 16 §16.5:** The Fourier series is the eigenfunction expansion for the 1D wave equation with periodic boundary conditions. The modes $e^{jn\omega_0 t}$ are eigenfunctions of $d/dt$, and the expansion is the same superposition as in Ch. 16 §16.5.2.

**Parseval's theorem (power conservation):** $$\frac{1}{T_0}\int_0^{T_0}|x(t)|^2,dt = \sum_{n=-\infty}^{\infty}|c_n|^2$$

Average power in time = sum of powers at each harmonic.

### 18.6.2 — Fourier Transform

For aperiodic signals:

$$X(f) = \int_{-\infty}^{\infty}x(t)e^{-j2\pi ft},dt, \qquad x(t) = \int_{-\infty}^{\infty}X(f)e^{j2\pi ft},df$$

**Key transform pairs:**

|$x(t)$|$X(f)$|Engineering use|
|---|---|---|
|$\delta(t)$|$1$|Impulse response, white spectrum|
|$1$|$\delta(f)$|DC signal|
|$e^{-t/\tau}u(t)$|$\tau/(1+j2\pi f\tau)$|RC filter step response|
|$\text{rect}(t/T)$|$T,\text{sinc}(fT)$|Ideal pulse, brick-wall filter|
|$e^{-\pi t^2}$|$e^{-\pi f^2}$|Gaussian pulse (minimum time-bandwidth)|
|$\cos(2\pi f_0 t)$|$\frac{1}{2}[\delta(f-f_0)+\delta(f+f_0)]$|Single tone|

**Convolution theorem:** $$y(t) = h(t)*x(t) \quad\Longleftrightarrow\quad Y(f) = H(f)\cdot X(f)$$

Convolution in time = multiplication in frequency. The output of any LTI system is the input spectrum multiplied by the transfer function — the entire filtering operation reduces to pointwise multiplication after the Fourier transform.

**Time-bandwidth product:** $\Delta t\cdot\Delta f \geq 1/(4\pi)$ (Heisenberg uncertainty principle, Ch. 3 §3.11, applied to signals instead of wavefunctions). A short pulse has a wide spectrum; a narrowband signal lasts long in time. This is the fundamental trade-off in every communications and radar system.

### 18.6.3 — Laplace Transform and System Analysis

The bilateral Laplace transform:

$$X(s) = \int_{-\infty}^{\infty}x(t)e^{-st},dt, \quad s = \sigma + j\omega$$

For causal systems (unilateral Laplace, $t \geq 0$): generalizes the Fourier transform to include exponentially growing/decaying signals.

**Key transform pairs:**

|$x(t)$|$X(s)$|
|---|---|
|$\delta(t)$|$1$|
|$u(t)$ (step)|$1/s$|
|$e^{-at}u(t)$|$1/(s+a)$|
|$\sin(\omega_0 t)u(t)$|$\omega_0/(s^2+\omega_0^2)$|
|$t^n e^{-at}u(t)$|$n!/(s+a)^{n+1}$|

**Transfer function from the circuit:** Replace each element with its Laplace impedance ($Z_R = R$, $Z_C = 1/sC$, $Z_L = sL$), apply KVL/KCL in the s-domain, and solve algebraically.

**Poles and stability:**

- All poles in the left half-plane ($\text{Re}[s_k] < 0$): stable (response decays)
- Poles on the imaginary axis: marginally stable (sustained oscillation)
- Any pole in the right half-plane: unstable (growing response)

**Initial and final value theorems:** $$x(0^+) = \lim_{s\to\infty} sX(s), \qquad x(\infty) = \lim_{s\to 0} sX(s)$$

Useful for checking step response endpoints without full inverse Laplace.

---

## 18.7 — Sampling and Digital Signals

### 18.7.1 — The Nyquist-Shannon Sampling Theorem

**Statement:** A continuous signal $x(t)$ bandlimited to $f_{max}$ Hz can be perfectly reconstructed from samples taken at rate $f_s \geq 2f_{max}$ (the Nyquist rate).

**Derivation from Fourier theory:** Sampling at interval $T_s = 1/f_s$ multiplies the signal by a train of impulses $\sum_n\delta(t-nT_s)$. In the frequency domain, this convolution creates periodic copies of $X(f)$ centered at multiples of $f_s$. If $f_s > 2f_{max}$, the copies do not overlap → perfect reconstruction by a lowpass filter.

**Aliasing:** If $f_s < 2f_{max}$, the copies overlap and frequency components above $f_s/2$ are "aliased" — they appear as false lower-frequency components. An anti-aliasing filter (LPF at $f_{max} = f_s/2$) before the ADC prevents this.

**Connection to Ch. 16:** The Nyquist criterion is the sampling version of the spatial Nyquist criterion in optics ($\theta_{min} = \lambda/D$, Ch. 12 §12.6.2) — both limit how finely a signal can be resolved given a finite aperture or sampling rate.

### 18.7.2 — Analog-to-Digital and Digital-to-Analog Conversion

**ADC quantization:** Mapping a continuous amplitude to $2^N$ discrete levels.

- **Resolution:** Voltage per bit = $V_{FSR}/2^N$
- **Dynamic range:** $\text{DR} = 20\log_{10}(2^N) = 6.02N$ dB
- **SNR (ideal ADC):** $\text{SNR} = 6.02N + 1.76$ dB (for sinusoidal input)

For 16-bit audio: DR = 96 dB (vs. human hearing ~120 dB dynamic range → 20-bit ideal). For 12-bit industrial ADC: DR = 72 dB.

**ADC architectures:** Flash (fastest, $2^N$ comparators), successive approximation (SAR, most common at moderate speeds), sigma-delta ($\Delta\Sigma$, highest resolution via oversampling + noise shaping).

### 18.7.3 — Discrete Fourier Transform (DFT) and FFT

The DFT of $N$ samples $x[n]$:

$$X[k] = \sum_{n=0}^{N-1}x[n],e^{-j2\pi kn/N}, \qquad k = 0, 1, \ldots, N-1$$

Direct computation: $O(N^2)$ operations. **Fast Fourier Transform (FFT):** Cooley-Tukey algorithm exploiting the twiddle factor symmetry → $O(N\log_2 N)$ operations.

For $N = 10^6$: DFT needs $10^{12}$ operations; FFT needs $2\times 10^7$ — 50,000× faster. The FFT is one of the most important algorithms in engineering computing.

**Frequency resolution:** $\Delta f = f_s/N$ (Hz per bin). To resolve two frequencies $\Delta f_{sep}$, need $N \geq f_s/\Delta f_{sep}$ samples.

---

## 18.8 — Power Electronics

### 18.8.1 — Rectifiers

**Half-wave rectifier:** One diode; passes only positive half-cycles. Average output: $V_{avg} = V_{pk}/\pi$. Large ripple.

**Full-wave bridge rectifier:** Four diodes; both half-cycles used. Average output: $V_{avg} = 2V_{pk}/\pi$.

**Capacitor filter:** A capacitor $C$ across the output holds the voltage between charging pulses. Ripple voltage (approximate):

$$V_{ripple} \approx \frac{I_{load}}{2fC}$$

For $I_{load} = 100$ mA, $f = 60$ Hz, $C = 1000;\mu$F: $V_{ripple} \approx 0.83$ V. Larger C → smaller ripple → larger peak current demand.

### 18.8.2 — Switching Converters

DC-DC converters use switching (transistor on/off at high frequency $f_{sw}$) plus energy storage (L and C) to efficiently change voltage levels.

**Buck converter (step-down):**

When switch ON: current through inductor ramps up; when OFF: inductor maintains current through diode. In steady state:

$$V_{out} = D\cdot V_{in}, \qquad I_{in} = D\cdot I_{out}, \qquad P_{in} = P_{out}$$

where $D = t_{on}/T_{sw}$ is the duty cycle. Efficiency: 90–99% (vs. linear regulator: $\eta = V_{out}/V_{in}$, as low as 20% for large step-down).

**Connection to physics:** The energy stored in the inductor during ON time ($W = \frac{1}{2}LI^2$, from Ch. 17 §17.9.1) is released during OFF time. The inductor "stores" kinetic energy of current, exactly as a flywheel stores mechanical kinetic energy. Faraday's law (Ch. 11) governs the inductor voltage.

**Boost converter (step-up):** $V_{out} = V_{in}/(1-D)$

**Buck-boost:** $V_{out} = -DV_{in}/(1-D)$ (inverts polarity)

**Switching frequency trade-off:**

- Higher $f_{sw}$ → smaller L, C → smaller converter
- Higher $f_{sw}$ → more switching losses → lower efficiency
- Typical: 100 kHz–10 MHz for power ICs; 20–100 kHz for large converters

**Engineering applications:**

- Laptop power adapters (AC→DC, then DC-DC regulation)
- Electric vehicle battery management (bidirectional DC-DC for cell balancing)
- Solar inverters (DC-DC boost + DC-AC inverter)
- LED drivers (constant-current buck converter)

---

## 18.9 — Where EEE Layer 3 Fails

### 18.9.1 — High-Frequency Effects

At frequencies where the lumping criterion $Lf/v_{em} \ll 1$ fails:

- **Parasitic inductance and capacitance** of component leads and PCB traces dominate
- **Transmission line effects** — signal reflections on PCB traces longer than $\lambda/10$ (at 1 GHz: $\lambda = 30$ cm; $\lambda/10 = 3$ cm — every long trace is a transmission line)
- **Radiation** — antennas radiate; circuits become radiators (EMC problems)
- **Skin effect** — current concentrates in thin surface layer, increasing effective resistance

At these frequencies, full Maxwell's equations (Ch. 11–12) or distributed models (Ch. 12 §12.7, Ch. 17 §17.10) are required.

### 18.9.2 — Quantum Device Limits

As transistor gate lengths approach $\sim 3$–$5$ nm:

- **Gate oxide tunneling** (Ch. 4 §4.4): $\sim 1$ nm SiO₂ gates have unacceptable leakage → replaced by high-κ dielectrics (HfO₂)
- **Ballistic transport** (Ch. 13 §13.11.1): mean free path exceeds channel length → Landauer formula, not Drude
- **Random dopant fluctuations**: at 5 nm gate lengths, the depletion region may contain 0 or 1 dopant atoms → statistical variation in $V_{th}$
- **Quantum confinement**: 2D electron gas at the interface behaves quantum mechanically → need Ch. 6–7 band theory, not bulk MOSFET model

The simple MOSFET equations from §18.3.3 break down. The physicist who derived them from Ch. 6 physics will know which Layer-1 effects are responsible and what the corrected model should be.

### 18.9.3 — Topological and Quantum Devices

Some devices are inherently beyond Layer-3 description:

- **Josephson junction** (Ch. 7 §7.8): superconducting quantum switch; the current-phase relation $I = I_c\sin(\Delta\phi)$ cannot be captured by any R, C, L model
- **Quantum dot single-electron transistor** (Ch. 7 §7.9): Coulomb blockade gives a conductance that oscillates with gate voltage — no DC operating point
- **Topological qubit** (Ch. 7 §7.4): information encoded in Majorana modes, non-local and topologically protected — no equivalent classical circuit

These devices require returning to Layer 1 (Chs. 6–7) for design.

---

## 18.10 — Summary

|Layer-3 concept|Physical origin|Chapter|
|---|---|---|
|KCL $\sum I = 0$|Noether U(1) / charge conservation|Ch. 1, 11, 17|
|KVL $\sum V = 0$|Faraday's law, quasi-static|Ch. 11, 17|
|Complex impedance $Z(\omega)$|Lumped L, R, C from Wave/diffusion PDE|Ch. 16, 17|
|Diode $I = I_0(e^{V/V_T}-1)$|p-n junction drift-diffusion|Ch. 6, 14|
|MOSFET $I_D \propto (V_{GS}-V_{th})^2$|Inversion layer, surface charge|Ch. 6|
|Op-amp golden rules|$A_{OL}\to\infty$ + negative feedback|Ch. 17 (Thévenin)|
|Filter $H(s)$ poles|Natural frequencies of LC network|Ch. 16, 17|
|Butterworth $\|H\|^2 = 1/(1+(ω/ω_c)^{2n})$|Optimal flat passband|Ch. 17 (2nd-order)|
|Fourier transform $X(f) = \mathcal{F}{x(t)}$|Eigenfunction expansion|Ch. 16 §16.5|
|Nyquist $f_s \geq 2f_{max}$|Spectral aliasing / Fourier sampling|Ch. 16|
|Buck converter $V_{out} = DV_{in}$|Faraday (inductor) + KVL|Ch. 11, 17|
|GBW product|Single-pole op-amp rolloff|Ch. 17 (Bode)|
|ADC dynamic range $6.02N$ dB|$2^N$ quantization levels|Ch. 10 (information)|

---

## 18.11 — Engineering Thread

|Concept|Engineering system|
|---|---|
|KVL/KCL + Thévenin|All circuit simulation (SPICE, LTspice, Cadence)|
|Phasors + power factor|Grid-connected inverters, motor drives, utility metering|
|Diode model|Rectifiers; photodetectors; LED drivers; solar cell characterization|
|BJT small-signal|RF amplifier design; audio amplifiers; discrete analog design|
|MOSFET saturation|Digital logic (CMOS); analog VLSI; power switching|
|Op-amp golden rules|Instrumentation amplifiers; ADC input stages; active filters|
|Butterworth/Chebyshev|Anti-aliasing filters; audio equalizers; IF filters in receivers|
|Fourier/FFT|Spectrum analyzers; software-defined radio; vibration analysis|
|Nyquist + ADC specs|Data acquisition system design; audio codec selection|
|Buck/boost converters|Power management ICs in phones, laptops, EVs|
|Laplace poles/zeros|Control system design (Ch. 21); stability analysis; loop shaping|

---

## 18.12 — Looking Ahead

Chapter 18 established EEE as the electrical instantiation of the Layer-3 template from Ch. 17. The same template — different labels — drives Chapters 19 and 20.

**Chapter 19** covers **ME Systems**: the mechanical and thermal instantiation. Mass replaces inductance; spring compliance replaces capacitance; damping replaces resistance. The same $\omega_0$, $\zeta$, $Q$, Bode plots, and Thévenin equivalents appear, now governing vibrating structures, rotating machinery, and thermofluid systems.

**Chapter 20** covers **CE and ChE Systems**: the hydraulic, structural, and chemical process instantiations.

**Chapter 21** then closes the book with feedback and control — the branch-agnostic mathematics that sits above all domains and applies equally to every engineering system.

---

_End of Chapter 18._

---

_Next: Chapter 19 — ME Systems: Machines, Structures, and Thermofluid Systems_