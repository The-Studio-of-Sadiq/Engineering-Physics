# Electromagnetic Waves, Optics, and Photonics

### One Wave Equation, the Entire Electromagnetic Spectrum

---

> _We have reason to conclude that light itself, including radiant heat and_ _other radiations, is an electromagnetic disturbance in the form of waves_ _propagated through the electromagnetic field according to electromagnetic laws._ — James Clerk Maxwell, _A Dynamical Theory of the Electromagnetic Field_, 1865

---

## 12.0 — Overview

Chapter 11 derived Maxwell's equations from the U(1) gauge sector of $\mathcal{L}_{SM}$. The vacuum wave equation fell out immediately: $\Box\mathbf{E} = 0$, predicting wave solutions propagating at $c = 1/\sqrt{\mu_0\epsilon_0}$.

This chapter does four things with that result:

1. **Extends** the wave equation to material media — showing how $\epsilon(\omega)$ and $\mu(\omega)$ modify propagation, giving dispersion, attenuation, and the refractive index
    
2. **Applies** Maxwell's boundary conditions to derive, not postulate, the laws of reflection, refraction (Snell's law), Brewster's angle, total internal reflection, and the Fresnel equations
    
3. **Identifies** waveguides as the bridge zone between Layer 2 (Maxwell's PDEs) and Layer 3 (lumped circuit theory) — the transmission line is the distributed- parameter model that sits between them
    
4. **Connects** to engineering photonics: optical fiber, lasers, integrated photonics, and nonlinear optics
    

Every named optical phenomenon from the Chapter 2 catalogue appears here with its derivation. Students who return to the catalogue after this chapter will find every optical entry fully grounded.

---

## 12.1 — Wave Equations in Material Media

### 12.1.1 — Maxwell in a Linear Isotropic Medium

In a homogeneous, isotropic, linear medium with constitutive relations $\mathbf{D} = \epsilon\mathbf{E}$, $\mathbf{B} = \mu\mathbf{H}$, $\mathbf{J}_f = \sigma\mathbf{E}$ (no free charges, $\rho_f = 0$), Maxwell's equations become:

$$\nabla\cdot\mathbf{E} = 0, \qquad \nabla\times\mathbf{H} = \sigma\mathbf{E} + \epsilon\frac{\partial\mathbf{E}}{\partial t}$$ $$\nabla\cdot\mathbf{H} = 0, \qquad \nabla\times\mathbf{E} = -\mu\frac{\partial\mathbf{H}}{\partial t}$$

Taking the curl of Faraday's law and using Ampere-Maxwell:

$$\boxed{\nabla^2\mathbf{E} = \mu\epsilon\frac{\partial^2\mathbf{E}}{\partial t^2} + \mu\sigma\frac{\partial\mathbf{E}}{\partial t}}$$

This is the **electromagnetic wave equation in a lossy medium**:

- $\mu\epsilon,\partial^2_t\mathbf{E}$: wave propagation term (speed $v = 1/\sqrt{\mu\epsilon}$)
- $\mu\sigma,\partial_t\mathbf{E}$: damping term from Ohmic loss ($\sigma > 0$)

### 12.1.2 — The Complex Wavenumber

For a monochromatic plane wave $\mathbf{E} = \mathbf{E}_0 e^{i(\tilde k z - \omega t)}$:

$$\tilde k^2 = \mu\epsilon\omega^2 + i\mu\sigma\omega = \mu\omega^2\left(\epsilon + i\frac{\sigma}{\omega}\right) \equiv \mu\omega^2\tilde\epsilon$$

Define the **complex permittivity** $\tilde\epsilon = \epsilon' - i\epsilon''$:

$$\tilde\epsilon = \epsilon + i\frac{\sigma}{\omega} = \epsilon_0\tilde\epsilon_r, \qquad \tilde\epsilon_r = \epsilon_r + i\frac{\sigma}{\omega\epsilon_0}$$

The complex wavenumber $\tilde k = \beta + i\alpha$ gives:

$$\mathbf{E}(z,t) = \mathbf{E}_0,e^{-\alpha z},e^{i(\beta z - \omega t)}$$

- **$\beta$ (phase constant):** determines the phase velocity $v_p = \omega/\beta$ and wavelength $\lambda = 2\pi/\beta$ in the medium
- **$\alpha$ (attenuation constant):** the field decays as $e^{-\alpha z}$; intensity decays as $e^{-2\alpha z}$
- **Skin depth:** $\delta = 1/\alpha$ — the depth at which the field amplitude falls to $1/e$ of its surface value

### 12.1.3 — The Complex Refractive Index

$$\tilde n = \sqrt{\tilde\epsilon_r\mu_r} = n + i\kappa$$

where $n$ is the **refractive index** (determines phase velocity) and $\kappa$ is the **extinction coefficient** (determines absorption):

$$v_p = \frac{c}{n}, \qquad \alpha = \frac{\omega\kappa}{c} = \frac{2\pi\kappa}{\lambda_0}$$

The **Beer-Lambert law** for intensity: $I = I_0 e^{-2\alpha z} = I_0 e^{-\mu_a z}$ where $\mu_a = 2\alpha$ is the absorption coefficient (m$^{-1}$).

**Material classification by $\tilde n$:**

|Material type|$n$|$\kappa$|Example|
|---|---|---|---|
|Transparent dielectric|$n > 1$|$\kappa \approx 0$|Glass, water at optical freq.|
|Weakly absorbing|$n > 1$|$\kappa \ll n$|Optical glass with defects|
|Metal (optical freq.)|$n \sim \kappa \sim 1$–$10$|large|Cu, Al, Au at visible|
|Good conductor (RF)|$n = \kappa = \sqrt{\sigma/2\omega\epsilon_0}$|$n = \kappa \gg 1$|Copper at GHz|

For a good conductor ($\sigma \gg \omega\epsilon$): $$\alpha = \beta = \sqrt{\frac{\omega\mu\sigma}{2}} = \frac{1}{\delta}, \qquad \delta = \sqrt{\frac{2}{\omega\mu\sigma}}$$

This recovers the **skin depth** from Ch. 11 §11.10 — confirming that the skin effect is a direct consequence of the complex refractive index of conductors.

---

## 12.2 — Dispersion: Phase and Group Velocity

### 12.2.1 — The Two Velocities

A monochromatic wave at frequency $\omega$ propagates at the **phase velocity** $v_p = \omega/k(\omega) = c/n(\omega)$.

A pulse — a superposition of frequencies — travels at the **group velocity**:

$$\boxed{v_g = \frac{d\omega}{dk} = \frac{c}{n + \omega,dn/d\omega} = \frac{c}{n_g}}$$

where $n_g = n + \omega,dn/d\omega$ is the **group index**.

When $n$ is frequency-independent: $v_g = v_p = c/n$ (no dispersion). When $n = n(\omega)$: $v_g \neq v_p$ and different frequency components travel at different speeds — **dispersion**.

### 12.2.2 — Types of Dispersion

**Normal dispersion** ($dn/d\omega > 0$, $v_g < v_p$): occurs in most transparent materials at optical frequencies. A prism separates white light because the refractive index is higher at shorter wavelengths (blue light bends more than red).

**Anomalous dispersion** ($dn/d\omega < 0$, $v_g > v_p$): occurs near absorption resonances. The Sellmeier equation for glass:

$$n^2(\lambda) = 1 + \sum_i\frac{B_i\lambda^2}{\lambda^2 - C_i}$$

where $(B_i, C_i)$ are material-specific constants fitted to absorption resonances.

### 12.2.3 — Pulse Spreading in Optical Fibers

A pulse of spectral width $\Delta\omega$ propagates through a fiber of length $L$. Different frequency components arrive at different times. The temporal spread:

$$\Delta\tau = L\left|\frac{d^2k}{d\omega^2}\right|\Delta\omega = L|\beta_2|\Delta\omega$$

where $\beta_2 = d^2k/d\omega^2$ is the **group velocity dispersion** (GVD) parameter.

For standard SMF-28 fiber at 1550 nm: $\beta_2 = -21.7$ ps²/km. For a 10 Gb/s signal ($\Delta\omega \sim 60$ GHz), pulse spreads by $\sim 13$ ps/km — limiting the transmission distance before regeneration.

**Dispersion management:** Alternating sections of normal and anomalous dispersion fiber (dispersion-shifted or compensating fiber) can reduce $\beta_2^{eff}$ to near zero over long spans.

---

## 12.3 — Boundary Conditions and the Laws of Optics

### 12.3.1 — Maxwell Boundary Conditions

At an interface between medium 1 and medium 2, integrating Maxwell's equations over a pillbox (normal to surface) and a loop (tangential to surface):

$$\boxed{\hat n\times(\mathbf{E}_2 - \mathbf{E}_1) = 0} \quad\text{(tangential E continuous)}$$ $$\boxed{\hat n\times(\mathbf{H}_2 - \mathbf{H}_1) = \mathbf{K}} \quad\text{(tangential H discontinuous by surface current)}$$ $$\boxed{\hat n\cdot(\mathbf{D}_2 - \mathbf{D}_1) = \sigma_f} \quad\text{(normal D discontinuous by surface charge)}$$ $$\boxed{\hat n\cdot(\mathbf{B}_2 - \mathbf{B}_1) = 0} \quad\text{(normal B always continuous)}$$

For non-conducting dielectric interfaces: $\mathbf{K} = 0$, $\sigma_f = 0$, and both tangential components of $\mathbf{E}$ and $\mathbf{H}$ are continuous.

### 12.3.2 — Snell's Law from Phase Matching

At a planar interface, the boundary conditions must be satisfied for all positions on the interface and for all time. This forces all three waves (incident, reflected, transmitted) to have the **same frequency** (obvious) and the **same tangential component of $\mathbf{k}$** (phase matching):

$$k_1\sin\theta_i = k_r\sin\theta_r = k_2\sin\theta_t$$

Since $k = n\omega/c$ and $k_1 = k_r$ (same medium):

$$\theta_r = \theta_i \qquad\text{(law of reflection)}$$ $$\boxed{n_1\sin\theta_i = n_2\sin\theta_t} \qquad\text{(Snell's law)}$$

**Snell's law is a consequence of translational symmetry** of the interface — Noether's theorem applied to the tangential spatial direction. The component of momentum parallel to the interface is conserved. This is not an empirical law; it is a Noether consequence of planar geometry.

### 12.3.3 — Fresnel Equations

Applying the tangential boundary conditions with the phase-matching constraint, we get the **Fresnel amplitude coefficients** for each polarization:

**s-polarization** (TE: E field ⊥ to plane of incidence):

$$r_s = \frac{n_1\cos\theta_i - n_2\cos\theta_t}{n_1\cos\theta_i + n_2\cos\theta_t}, \qquad t_s = \frac{2n_1\cos\theta_i}{n_1\cos\theta_i + n_2\cos\theta_t}$$

**p-polarization** (TM: E field in plane of incidence):

$$r_p = \frac{n_2\cos\theta_i - n_1\cos\theta_t}{n_2\cos\theta_i + n_1\cos\theta_t}, \qquad t_p = \frac{2n_1\cos\theta_i}{n_2\cos\theta_i + n_1\cos\theta_t}$$

**Reflectance and transmittance** (power, accounting for beam cross-section change):

$$R_s = |r_s|^2, \quad R_p = |r_p|^2$$ $$T_s = \frac{n_2\cos\theta_t}{n_1\cos\theta_i}|t_s|^2, \quad T_p = \frac{n_2\cos\theta_t}{n_1\cos\theta_i}|t_p|^2$$

**Energy conservation:** $R + T = 1$ for each polarization (lossless interface).

### 12.3.4 — Brewster's Angle

When $r_p = 0$: the numerator $n_2\cos\theta_i - n_1\cos\theta_t = 0$. Using Snell's law: this occurs when $\theta_i + \theta_t = 90°$, giving:

$$\tan\theta_B = \frac{n_2}{n_1}$$

At Brewster's angle, the p-polarization is completely transmitted — reflected light is purely s-polarized. **Physical origin:** The refracted wave tries to radiate back as the reflected wave, but the oscillating dipoles in the medium cannot radiate in the direction of their own oscillation (a transverse dipole does not radiate along its axis). When the reflected and refracted beams are perpendicular, the dipoles cannot radiate into the reflection direction.

**Engineering applications:** Brewster windows in laser cavities eliminate reflection losses for one polarization; polarizing beam splitter cubes use Brewster-angle stacks; anti-glare coatings exploit Brewster's angle for horizontal polarization.

### 12.3.5 — Total Internal Reflection

For $n_1 > n_2$ (denser medium), at incidence angle $\theta_i > \theta_c$:

$$\theta_c = \arcsin\left(\frac{n_2}{n_1}\right)$$

Snell's law gives $\sin\theta_t > 1$ — no real solution. The transmitted wave becomes **evanescent**: it decays exponentially into medium 2 with no time-averaged power transmitted.

The evanescent field: $$\mathbf{E}_t \propto \exp!\left(-\frac{z}{\delta_{ev}}\right)\exp(ik_x x), \qquad \delta_{ev} = \frac{\lambda_0}{2\pi\sqrt{n_1^2\sin^2\theta_i - n_2^2}}$$

- At $\theta_i = \theta_c$: $\delta_{ev}\to\infty$ (grazing transmission)
- For typical glass-air TIR at $\theta_i = 60°$, $n_1 = 1.5$: $\delta_{ev} \approx 100$ nm

**Frustrated TIR:** Bringing a second medium within the evanescent decay length couples the evanescent field back into propagating waves — tunneling of light (cf. quantum tunneling, Ch. 4 §4.4, same mathematics). Used in ATR (attenuated total reflectance) spectroscopy and fiber coupling.

---

## 12.4 — Polarization

### 12.4.1 — The Jones Vector

The polarization state of a plane wave is described by the **Jones vector**:

$$\mathbf{J} = \begin{pmatrix}E_x\E_y\end{pmatrix}$$

where $E_x$ and $E_y$ are complex amplitudes. Standard polarization states:

|Polarization|Jones vector|
|---|---|
|Linear (horizontal)|$(1,,0)^T$|
|Linear (vertical)|$(0,,1)^T$|
|Linear ($45°$)|$(1,,1)^T/\sqrt{2}$|
|Right circular|$(1,,-i)^T/\sqrt{2}$|
|Left circular|$(1,,+i)^T/\sqrt{2}$|

### 12.4.2 — Waveplates and Birefringence

A birefringent medium has different refractive indices for orthogonal polarizations: $n_x \neq n_y$ (ordinary and extraordinary axes). A wave propagating through thickness $d$ accumulates a **phase retardation**:

$$\delta = \frac{2\pi d}{\lambda_0}(n_e - n_o)$$

**Quarter-wave plate** ($\delta = \pi/2$): converts linear to circular polarization. Jones matrix: $\text{QWP} = e^{i\pi/4}\begin{pmatrix}1&0\0&-i\end{pmatrix}$

**Half-wave plate** ($\delta = \pi$): rotates linear polarization by $2\alpha$, where $\alpha$ is the angle between the fast axis and the input polarization. Jones matrix: $\text{HWP} = \begin{pmatrix}\cos 2\alpha & \sin 2\alpha\\sin 2\alpha & -\cos 2\alpha\end{pmatrix}$

**Malus's law:** Intensity transmitted through an analyzer at angle $\theta$ to a linearly polarized input: $$I = I_0\cos^2\theta$$

This follows from the Jones vector projection: $I \propto |E_x|^2 = |E_0\cos\theta|^2$.

**Engineering applications:** LCD displays (electrically controlled birefringence to rotate polarization); ellipsometry (polarization analysis for thin film measurement); optical isolators (Faraday rotation + polarizers).

---

## 12.5 — Interference

### 12.5.1 — Two-Beam Interference

The superposition of two coherent waves with intensities $I_1$, $I_2$, and phase difference $\delta$:

$$I_{total} = I_1 + I_2 + 2\sqrt{I_1 I_2}\cos\delta$$

Maximum ($\delta = 2m\pi$): $I_{max} = (\sqrt{I_1}+\sqrt{I_2})^2$ Minimum ($\delta = (2m+1)\pi$): $I_{min} = (\sqrt{I_1}-\sqrt{I_2})^2$

**Visibility:** $\mathcal{V} = (I_{max}-I_{min})/(I_{max}+I_{min})$ — measures contrast. For $I_1 = I_2$: $\mathcal{V} = 1$ (perfect contrast); $I_{min} = 0$.

The phase difference from an optical path difference $\Delta L$: $$\delta = \frac{2\pi}{\lambda_0}\Delta L = k_0\Delta L$$

### 12.5.2 — Young's Double Slit

Two slits separated by distance $d$, at distance $L$ from screen:

Bright fringes at: $y_m = m\lambda L/d$ (fringe spacing $\Delta y = \lambda L/d$)

The intensity pattern is the Fourier transform of the two-slit aperture: $$I(\theta) = 4I_0\cos^2!\left(\frac{\pi d\sin\theta}{\lambda}\right)$$

**From linearity of Maxwell:** The superposition principle — which makes interference possible — is a direct consequence of Maxwell's equations being linear. Nonlinear media ($\chi^{(2)}, \chi^{(3)}$) modify this.

### 12.5.3 — Thin Film Interference

For a film of refractive index $n$, thickness $t$, at near-normal incidence:

$$\delta = \frac{4\pi nt}{\lambda_0} + \delta_{phase}$$

Phase shifts at reflection: $\pi$ at low-to-high $n$ interface; $0$ at high-to-low. For a film (air–film–substrate with $n_{film} < n_{sub}$): both reflections have $\pi$ phase shift, net phase shift = 0:

- **Destructive reflection** (anti-reflection): $2nt = (m+\frac{1}{2})\lambda_0$
- **Constructive reflection:** $2nt = m\lambda_0$

**Quarter-wave anti-reflection coating:** $n_f = \sqrt{n_1 n_2}$, $t = \lambda/4n_f$. For glass ($n = 1.5$) in air: optimal coating index $n_f = 1.22$ (MgF₂ has $n = 1.38$ — close enough for broadband AR).

**High-reflectance stack:** Alternating quarter-wave layers of high and low index: $R \to 1$ as the number of pairs increases. Distributed Bragg reflectors (DBR) in VCSELs use this principle.

### 12.5.4 — Fabry-Perot Etalon

Two partially reflecting mirrors of reflectance $R$ separated by spacing $d$:

$$I_T = \frac{I_0}{1 + F\sin^2(\delta/2)}, \qquad F = \frac{4R}{(1-R)^2}$$

where $\delta = 4\pi nd\cos\theta/\lambda_0$ is the round-trip phase and $F$ is the **coefficient of finesse**.

The resonances (full transmission) occur at $\delta = 2m\pi$: $$\text{FSR} = \frac{c}{2nd} \quad\text{(free spectral range)}$$

**Finesse:** $\mathcal{F} = \pi\sqrt{F}/2 = \pi\sqrt{R}/(1-R)$ — the ratio of FSR to linewidth. For $R = 0.99$: $\mathcal{F} \approx 313$.

**Resolving power:** $\mathcal{R} = m\mathcal{F}$ — the Fabry-Perot can resolve wavelength differences $\Delta\lambda = \lambda/\mathcal{R}$.

**Engineering:** Fabry-Perot cavities are the resonators in all lasers; optical spectrum analyzers use scanning FP etalons; wavelength-selective filters in DWDM fiber systems.

---

## 12.6 — Diffraction and Fourier Optics

### 12.6.1 — The Huygens-Fresnel Principle

Every point on a wavefront is the source of a secondary spherical wavelet. The field at any subsequent point is the coherent superposition of all wavelets — the Kirchhoff diffraction integral:

$$U(\mathbf{r}) = \frac{-i}{\lambda}\iint_\Sigma U(\mathbf{r}')\frac{e^{ik|\mathbf{r}-\mathbf{r}'|}}{|\mathbf{r}-\mathbf{r}'|}\cos\theta,dS'$$

This follows from Green's second identity applied to the wave equation from Ch. 11 — not a new assumption.

### 12.6.2 — Fraunhofer Diffraction: The Fourier Transform

In the far field ($z \gg a^2/\lambda$, Fraunhofer regime), the Kirchhoff integral simplifies to a **Fourier transform** of the aperture function $t(x,y)$:

$$U(f_x, f_y) \propto \iint t(x,y),e^{-i2\pi(f_x x + f_y y)}dx,dy = \mathcal{F}{t}$$

where $f_x = \sin\theta_x/\lambda$, $f_y = \sin\theta_y/\lambda$ are spatial frequencies.

**Single slit** (width $a$): $t(x) = \text{rect}(x/a)$

$$I(\theta) = I_0\left(\frac{\sin(\pi a\sin\theta/\lambda)}{\pi a\sin\theta/\lambda}\right)^2 = I_0,\text{sinc}^2!\left(\frac{a\sin\theta}{\lambda}\right)$$

First zero at $\sin\theta = \lambda/a$.

**Circular aperture** (diameter $D$): Fourier transform is an Airy function.

First zero at $\sin\theta = 1.22\lambda/D$ → **Rayleigh criterion** for angular resolution:

$$\boxed{\theta_{min} = 1.22\frac{\lambda}{D}}$$

A 1 m telescope at $\lambda = 550$ nm: $\theta_{min} = 0.14''$ of arc. A microwave radar dish of 3 m at 10 GHz ($\lambda = 3$ cm): $\theta_{min} = 1.2°$.

**Diffraction grating** (N slits, spacing $d$): principal maxima at $d\sin\theta = m\lambda$, spectral resolving power $\mathcal{R} = mN$.

### 12.6.3 — Fourier Optics: A Lens as an Analog Computer

A converging lens of focal length $f$ **computes the Fourier transform** of the field in its front focal plane, producing the transform in its back focal plane:

$$U_{back}(x', y') \propto \mathcal{F}\left{U_{front}(x, y)\right}_{f_x = x'/\lambda f,, f_y = y'/\lambda f}$$

Two lenses in succession perform the inverse Fourier transform — restoring the original image. Between the two lenses, the **Fourier plane** contains the spatial frequency spectrum of the object: low frequencies near the center, high frequencies (fine detail) far from the center.

**Spatial filtering** (optical image processing):

- Block high spatial frequencies (low-pass filter) → blur the image
- Block low spatial frequencies (high-pass filter) → edge enhancement
- Block specific spatial frequencies → remove periodic noise
- All implemented with physical apertures in the Fourier plane

This is a direct connection to signal processing (Ch. 18): the same Fourier mathematics that describes digital filters here operates in analog light.

---

## 12.7 — Waveguides: The Bridge Zone

Waveguides sit in the bridge zone between Layer 2 (full Maxwell PDEs) and Layer 3 (lumped circuit elements). They retain spatial variation along the propagation direction while being "lumped" in the transverse directions.

### 12.7.1 — The Rectangular Metallic Waveguide

A metallic rectangular waveguide (width $a > b$) has perfect-conductor walls where $\mathbf{E}_{tangential} = 0$ (boundary condition from Maxwell).

The wave equation separates: $E_z = X(x)Y(y)e^{i(\beta z - \omega t)}$. Applying BCs:

$$\beta_{mn}^2 = \left(\frac{\omega}{c}\right)^2 - \left(\frac{m\pi}{a}\right)^2 - \left(\frac{n\pi}{b}\right)^2$$

A mode propagates ($\beta$ real) only above its **cutoff frequency**:

$$f_{c,mn} = \frac{c}{2}\sqrt{\left(\frac{m}{a}\right)^2 + \left(\frac{n}{b}\right)^2}$$

**Dominant mode (TE₁₀):** $m=1$, $n=0$; cutoff at $f_c = c/2a$.

Below cutoff: $\beta$ imaginary → exponential decay (evanescent). This is the waveguide analog of quantum tunneling (Ch. 4): the wave decays through the cutoff region as $e^{-|\beta|z}$ exactly as $e^{-\kappa d}$ in §4.4.

**The Brillouin zone boundary** in a crystal (Ch. 6) is the k-space analog of the cutoff: at the BZ boundary, Bragg reflection opens a gap just as the waveguide cutoff prevents propagation below $f_c$.

**Group velocity in the waveguide:**

$$v_g = c\sqrt{1 - (f_c/f)^2} < c$$

At $f \gg f_c$: $v_g \to c$. Near cutoff $f \to f_c^+$: $v_g \to 0$ (energy "stagnates").

### 12.7.2 — Optical Fiber: Guided Waves by Total Internal Reflection

A step-index optical fiber has a core (index $n_1$, radius $a$) surrounded by cladding ($n_2 < n_1$). Light launched at angle $\theta < \theta_{acc}$ from the axis undergoes TIR at the core-cladding interface and is guided.

**Numerical aperture:** $$\text{NA} = n_0\sin\theta_{acc} = \sqrt{n_1^2 - n_2^2}$$

**V-number** (normalized frequency): $$V = \frac{2\pi a}{\lambda}\text{NA} = \frac{2\pi a}{\lambda}\sqrt{n_1^2 - n_2^2}$$

- $V < 2.405$: **single-mode fiber** (one guided mode, HE₁₁)
- $V \gg 2.405$: **multimode fiber** (~$V^2/2$ modes)

**Single-mode fiber (SMF-28) at 1550 nm:** $a = 4.1;\mu$m, $\Delta n = 0.0036$, $V = 2.1$. One mode only — no modal dispersion.

**Why 1550 nm?** Silica fiber has minimum attenuation at 1550 nm ($\alpha \approx 0.2$ dB/km from Rayleigh scattering $\propto\lambda^{-4}$ plus infrared absorption). The entire global internet runs on 1550 nm light.

### 12.7.3 — Transmission Lines: EM Bridge Between Layers 2 and 3

A transmission line (coaxial cable, microstrip, twin-wire) is the most important bridge-zone model in electrical engineering. Derived by integrating Maxwell's equations over the cross-section, it retains spatial variation along $z$:

$$\frac{\partial V}{\partial z} + L'\frac{\partial I}{\partial t} + R'I = 0$$ $$\frac{\partial I}{\partial z} + C'\frac{\partial V}{\partial t} + G'V = 0$$

where $L'$, $C'$, $R'$, $G'$ are per-unit-length inductance, capacitance, resistance, and conductance — obtained from the static field solutions of Maxwell.

For a lossless line ($R' = G' = 0$): $$v = \frac{1}{\sqrt{L'C'}} = \frac{c}{\sqrt{\epsilon_r\mu_r}}, \qquad Z_0 = \sqrt{\frac{L'}{C'}}$$

The transmission line equations are **Maxwell's equations in one dimension**: $V$ plays the role of $E$ and $I$ plays the role of $H$. In the limit $z \to 0$ (lumped element), the partial derivatives become ordinary derivatives, and the transmission line equations collapse to KVL and KCL (Ch. 11 §11.12).

**The bridge zone explicitly:** A short line ($\ell \ll \lambda$): lumped. A long line ($\ell \sim \lambda$): distributed (transmission line equations). A very long line ($\ell \gg \lambda$): must be treated as a continuous medium (full Maxwell).

---

## 12.8 — Lasers and Coherent Light

### 12.8.1 — Population Inversion and the Laser Condition

From Ch. 5 §5 (Einstein A and B coefficients): in a medium with $N_2$ atoms in the upper level and $N_1$ in the lower, the **gain coefficient** for a wave at frequency $\nu_{21} = (E_2 - E_1)/h$:

$$g(\nu) = \frac{c^2}{8\pi\nu^2 n^2}A_{21}(N_2 - N_1)g(\nu)$$

For $N_2 > N_1$ (**population inversion**): $g > 0$ — the medium amplifies. For $N_2 < N_1$ (thermal equilibrium): $g < 0$ — the medium absorbs.

**Population inversion requires pumping:** A two-level system cannot achieve inversion (Einstein showed this in 1917). Practical lasers use three or four energy levels.

**Threshold condition** for lasing (round-trip gain equals round-trip loss):

$$2gL = 2\alpha_i L + \ln\frac{1}{R_1 R_2}$$

where $L$ is cavity length, $\alpha_i$ is internal loss, $R_1 R_2$ is the product of mirror reflectances. Below threshold: spontaneous emission only. Above threshold: stimulated emission dominates and the output power rises sharply.

### 12.8.2 — Laser Properties

**Spectral coherence:** A laser oscillates on one or a few longitudinal cavity modes, separated by $\Delta\nu = c/2nL$ (FSR of the Fabry-Perot cavity from §12.5.4). Linewidth can be $< 1$ Hz for stabilized lasers — $10^{14}$ times narrower than thermal emission at the same frequency.

**Spatial coherence:** The cavity selects a transverse mode (usually TEM₀₀ — a Gaussian beam). The beam propagates with well-defined phase across its full diameter.

**Directionality:** Diffraction-limited beam divergence $\theta_{div} = \lambda/\pi w_0$, where $w_0$ is the beam waist. For a 1 mm beam at 633 nm: $\theta_{div} = 0.2$ mrad.

### 12.8.3 — Semiconductor Lasers

From Ch. 6 §6.6.3: a direct-gap semiconductor (GaAs, InP, GaN) under forward-bias injection has:

- Electrons pumped into the conduction band
- Holes pumped into the valence band
- Population inversion for frequencies near $E_g/h$

**Double heterostructure:** Sandwiching a thin active layer (e.g., GaAs, $E_g = 1.42$ eV) between wider-gap cladding layers (AlGaAs) confines both carriers (via potential wells) and the optical mode (via index step → waveguiding). This reduces the threshold current density by $\sim 1000\times$ compared to bulk homojunction lasers.

**Quantum well lasers:** Active layer $\sim 10$ nm thick — quantum confinement (Ch. 4 particle-in-a-box) shifts the energy levels and narrows the gain spectrum. Threshold current densities $< 100$ A/cm² routinely achieved.

**Edge-emitting vs. VCSEL:**

- Edge-emitting: cleaved facets form the FP cavity; beam from the edge
- VCSEL (Vertical-Cavity Surface-Emitting Laser): DBR mirrors top and bottom; beam from the surface; easier to test, cheaper, used in data centers

---

## 12.9 — Nonlinear Optics

At high intensities, the polarization response becomes nonlinear:

$$\mathbf{P} = \epsilon_0\left(\chi^{(1)}\mathbf{E} + \chi^{(2)}\mathbf{E}^2 + \chi^{(3)}\mathbf{E}^3 + \cdots\right)$$

### 12.9.1 — Second-Order Effects ($\chi^{(2)}$)

$\chi^{(2)} \neq 0$ only in **non-centrosymmetric crystals** (broken inversion symmetry, from Ch. 5 §5.8.3 and Ch. 6 bonding). The crystal symmetry requirement is exactly the same as for piezoelectricity.

**Second harmonic generation (SHG):** Input at $\omega$, output at $2\omega$. Requires **phase matching** $k(2\omega) = 2k(\omega)$ for efficient conversion. Since $n(2\omega) \neq n(\omega)$ (dispersion), phase matching uses birefringence.

Power conversion (phase-matched, length $L$): $$P_{2\omega} = \frac{\omega^2 d^2 L^2}{n^3\epsilon_0 c^3 A}P_\omega^2$$

Proportional to $P_\omega^2$ — a quadratic process. Efficiency increases with intensity and crystal length.

**Engineering:** 532 nm green lasers (used in laser pointers, projectors) are SHG of 1064 nm Nd:YAG lasers in KTP or LBO crystals.

### 12.9.2 — Third-Order Effects ($\chi^{(3)}$)

Present in **all materials** (including isotropic media, glasses, fibers — no symmetry requirement).

**Kerr effect:** $n = n_0 + n_2 I$ (intensity-dependent refractive index). For silica fiber: $n_2 = 2.6\times 10^{-20}$ m²/W.

**Self-phase modulation (SPM):** A pulse propagating in a Kerr medium acquires an intensity-dependent phase $\phi(t) = -n_2 I(t)\omega L/c$. This broadens the spectrum of the pulse.

**Optical soliton:** When SPM (spectral broadening) exactly cancels the GVD (temporal broadening), the pulse shape is preserved indefinitely:

$$|E(t)| \propto \text{sech}(t/T_0)$$

Soliton communication systems exploit this balance for lossless (amplifier-compensated) dispersion-free propagation. They are solutions to the **Nonlinear Schrödinger Equation (NLSE)**:

$$\frac{\partial A}{\partial z} = -\frac{\alpha}{2}A - \frac{i\beta_2}{2}\frac{\partial^2 A}{\partial t^2} + i\gamma|A|^2 A$$

The NLSE is itself an engineering approximation to Maxwell's equations in a slowly-varying envelope approximation — a bridge zone between the full Maxwell PDE (Layer 2) and the simplified propagation model used in system design.

---

## 12.10 — Scattering

### 12.10.1 — Rayleigh Scattering

A small dielectric sphere ($a \ll \lambda$) in an electric field develops a dipole moment $\mathbf{p} = \alpha_{pol}\mathbf{E}$, where $\alpha_{pol}$ is the polarizability (from Ch. 4: the quantum-mechanical response of the electron cloud to an applied field).

The oscillating dipole radiates (Hertz dipole radiation):

$$\frac{d P_{rad}}{d\Omega} = \frac{\alpha_{pol}^2\omega^4}{32\pi^2\epsilon_0 c^3}\sin^2\Phi$$

Total scattered power $\propto \omega^4 \propto \lambda^{-4}$: **Rayleigh scattering.**

- Blue light (450 nm): scattered 5.5× more than red (700 nm)
- Sky is blue: sunlight scattered by air molecules; $N_2$ and $O_2$ preferentially scatter short wavelengths toward the observer
- Sunsets are red: long path through atmosphere removes blue, leaving red
- Fiber attenuation: Rayleigh scattering from density fluctuations in silica limits attenuation to $0.2$ dB/km floor at 1550 nm

### 12.10.2 — Raman Scattering

Inelastic scattering with energy exchange with a molecular vibration (phonon):

**Stokes Raman:** Photon loses energy $\hbar\omega_{vib}$ → phonon created $\nu_{Stokes} = \nu_{inc} - \nu_{vib}$

**Anti-Stokes Raman:** Photon gains energy $\hbar\omega_{vib}$ from a thermal phonon $\nu_{anti-Stokes} = \nu_{inc} + \nu_{vib}$

The Stokes-to-anti-Stokes ratio: $$\frac{I_{aS}}{I_S} = \exp!\left(-\frac{\hbar\omega_{vib}}{k_BT}\right)$$

This is directly the Boltzmann factor from Ch. 10 §10.3 — measuring the ratio directly gives the sample temperature (Raman thermometry).

**Engineering:** Raman spectroscopy identifies molecular species through vibrational fingerprints; distributed Raman sensing measures temperature along optical fibers by backscattered Stokes/anti-Stokes ratio; Raman amplifiers in fiber systems use stimulated Raman scattering to amplify signals at 1550 nm.

---

## 12.11 — The Doppler Effect for Electromagnetic Waves

For a source moving with velocity $v$ relative to the observer, the relativistic Doppler shift (from Ch. 8 — special relativity, $g_{\mu\nu} = \eta_{\mu\nu}$):

$$\nu_{obs} = \nu_0\sqrt{\frac{1 - v/c}{1 + v/c}} \approx \nu_0\left(1 - \frac{v}{c}\right) \quad\text{(recession, }v \ll c\text{)}$$

The EM Doppler formula differs from the acoustic one (Ch. 9 §9.9) because light has no preferred medium — only the relative velocity between source and observer matters.

**Radar Doppler:** Transmitted frequency $f_0$, received frequency from target moving at $v_r$ (radial component):

$$\Delta f = f_{Doppler} = \frac{2v_r f_0}{c}$$

For X-band radar ($f_0 = 10$ GHz) and $v_r = 30$ m/s: $\Delta f = 2$ kHz. **Engineering:** Speed cameras, police radar, weather Doppler radar (measures precipitation velocity), air traffic control, automotive adaptive cruise control.

---

## 12.12 — Summary

One wave equation from Ch. 11 — extended to matter and systematically applied:

|Result|Derivation|
|---|---|
|Wave equation in matter|Maxwell + constitutive relations: $\nabla^2\mathbf{E} = \mu\epsilon\ddot{\mathbf{E}} + \mu\sigma\dot{\mathbf{E}}$|
|Complex refractive index $\tilde n = n+i\kappa$|Complex $\tilde\epsilon = \epsilon + i\sigma/\omega$|
|Skin depth $\delta = 1/\alpha$|Imaginary part of $\tilde k$ in good conductor|
|Phase vs. group velocity|$v_p = \omega/\beta$; $v_g = d\omega/dk$|
|Snell's law $n_1\sin\theta_i = n_2\sin\theta_t$|Phase matching at boundary (Noether, translational symmetry)|
|Fresnel equations|Maxwell boundary conditions applied|
|Brewster's angle $\tan\theta_B = n_2/n_1$|$r_p = 0$ condition on Fresnel equation|
|TIR, evanescent field|$\sin\theta_t > 1$; field decays as $e^{-z/\delta_{ev}}$|
|Interference $I = I_1+I_2+2\sqrt{I_1I_2}\cos\delta$|Superposition (linearity of Maxwell)|
|Fraunhofer diffraction = Fourier transform|Kirchhoff integral in far field|
|Rayleigh criterion $\theta_{min} = 1.22\lambda/D$|Airy disk first zero|
|Waveguide cutoff $f_c = c/2a$|TM/TE mode BCs in rectangular guide|
|TIR fiber, V-number|Total internal reflection + waveguide mode analysis|
|Transmission line equations|Maxwell equations averaged over cross-section|
|Laser threshold|Round-trip gain = round-trip loss|
|Semiconductor laser|Direct-gap + population inversion + FP or DBR cavity|
|SHG $\propto P_\omega^2$|$\chi^{(2)}$ nonlinear polarization, phase matching|
|Optical soliton|SPM balanced by GVD → NLSE|
|Rayleigh scattering $\propto \lambda^{-4}$|Hertz dipole radiation from $\alpha_{pol}$|
|Raman: Stokes/anti-Stokes ratio $= e^{-\hbar\omega/kT}$|Boltzmann factor (Ch. 10)|
|EM Doppler $\Delta f = 2v_r f_0/c$|Relativistic phase shift|

---

## 12.13 — Engineering Thread

|Physics|Application|
|---|---|
|$v_p = c/n(\omega)$, dispersion|Fiber optic system design; pulse spreading; WDM channel spacing|
|Skin depth $\delta = \sqrt{2/\omega\mu\sigma}$|RF conductor sizing; shielding; induction heating|
|Fresnel equations + anti-reflection coatings|Camera lenses; solar panels; display screens|
|TIR in optical fiber|Global internet; endoscopes; optical interconnects|
|Rayleigh criterion $1.22\lambda/D$|Telescope, microscope, camera, satellite resolution|
|Waveguide cutoff|Microwave oven shielding (holes < cutoff); radar waveguides; MRI coils|
|Fabry-Perot cavity|All laser design; optical spectrum analyzers; DWDM filters|
|Semiconductor laser + fiber|Fiber communications; LIDAR; barcode scanners; laser machining|
|SHG|Green/blue lasers; OCT medical imaging; nonlinear characterization|
|Raman scattering|Material identification (pharmacy, security); fiber temperature sensing|
|Doppler radar|Traffic enforcement; weather forecasting; automotive safety|
|Transmission line $Z_0 = \sqrt{L'/C'}$|PCB trace impedance matching; RF amplifier design; coaxial systems|
|Soliton / NLSE|Long-haul undersea fiber transmission; ultrafast pulse compression|

---

## 12.14 — Looking Ahead

Chapter 12 has deployed Maxwell's equations across the electromagnetic spectrum, from waveguides to lasers to nonlinear photonics.

**Chapter 13 performs Bridge B.e:** the final Bridge B path. Starting from the quantum scattering theory of Ch. 6, applying the Kubo formula, and taking the statistical average gives the **generalized transport law** — Ohm's law, Fourier's law, Fick's law, Newton's viscosity, and Hooke's law, all from one Green-Kubo calculation. The conductivity $\sigma$ that appeared in this chapter as a constitutive parameter will be derived from first principles in Ch. 13.

After Ch. 13, all five Bridge B paths are complete, and Layer 2 is fully assembled. Bridge C (Ch. 17) then begins the lumping operation that converts the PDEs of Layer 2 into the ODE systems of Layer 3.

---

_End of Chapter 12._

---

_Next: Chapter 13 — Bridge B.e: The Kubo Formula and the Generalized Transport Law_