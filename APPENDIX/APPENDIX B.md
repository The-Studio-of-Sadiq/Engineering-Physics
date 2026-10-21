# Appendix B — Relativistic to Nonrelativistic Quantum Mechanics: Dirac, Foldy–Wouthuysen, Pauli

This appendix carries out in full the descent that Bridge A states. It starts from the Dirac equation with minimal coupling, separates the Hamiltonian into even and odd operators, and performs the Foldy–Wouthuysen (FW) transformation order by order to $(v/c)^2$. From the result it reads off five terms: the Pauli Hamiltonian with its Zeeman coupling and $g = 2$, the relativistic mass correction, the spin–orbit coupling (Thomas factor included automatically), and the Darwin term. Applied to hydrogen in first-order perturbation theory, these terms give the fine-structure formula to order $\alpha^4$. The appendix then checks that formula against the expansion of the exact Dirac–Coulomb energy and closes with the Gordon decomposition, the cleanest statement of where $g = 2$ comes from. The chapters that rely on it are [Ch. 3](../CHAPTERS/CHAPTER%203.md) §§3.2–3.6 (Bridge A itself), [Ch. 4](../CHAPTERS/CHAPTER%204.md) §4.7 (the Bohr levels as the zeroth-order problem), [Ch. 5](../CHAPTERS/CHAPTER%205.md) §§5.5–5.6 (spin–orbit, Zeeman, Landé), and [Example 01](../EXAMPLES/01%20Dirac-to-Pauli.md).

The FW series derived here is **truncated**. The truncation error and the conditions under which the series fails altogether are stated explicitly in §B.11.

---

## B.1 — Conventions and the Dirac Equation

**Assumptions and conventions.**

1. **Units: Gaussian**, as in Ch. 3. The fine-structure constant is $\alpha = e^2/\hbar c$ and the Bohr radius is $a_0 = \hbar^2/m e^2$. To convert to SI (Ch. 4, Ch. 5), replace $e^2 \to e^2/4\pi\epsilon_0$, $q\mathbf{A}/c \to q\mathbf{A}$, $q\hbar/2mc \to q\hbar/2m$ in magnetic terms, and $\nabla\cdot\mathbf E = 4\pi\rho \to \rho/\epsilon_0$. Terms built from $\mathbf E$ and $1/c^2$ keep their form.
2. **Charge.** The particle has signed charge $q$. For the electron $q = -e$, with $e > 0$. The formulas of Ch. 3 §§3.2–3.5 are those below with $q$ written as $e$, which is the signed-charge convention of Bjorken & Drell.
3. **Matrices.** Bold $\boldsymbol\alpha$ and $\beta$ are the Dirac matrices. Plain $\alpha$ is always the fine-structure constant. $\boldsymbol\Sigma = \mathrm{diag}(\boldsymbol\sigma,\boldsymbol\sigma)$.
4. **Signature for gamma matrices.** With $\gamma^0 = \beta$ and $\gamma^i = \beta\alpha_i$ one finds $(\gamma^0)^2 = 1$ and $(\gamma^i)^2 = -\beta^2\alpha_i^2 = -1$. So $\{\gamma^\mu,\gamma^\nu\} = 2\,\mathrm{diag}(1,-1,-1,-1)$. This is $2\eta^{\mu\nu}$ in the $(+,-,-,-)$ signature, which is the form Ch. 3 §3.3.1 writes, and $-2\eta^{\mu\nu}$ in the book's $(-,+,+,+)$ signature (Appendix A §A.1). The covariant formulas in §B.1 and §B.10 use $(+,-,-,-)$ and say so. Everything else is in Hamiltonian form, which does not depend on the signature.

**The Dirac Hamiltonian.** With $\Phi$ the scalar potential and $\mathbf A$ the vector potential:

$$i\hbar\,\partial_t\psi = H_D\psi, \qquad H_D = c\,\boldsymbol\alpha\cdot\boldsymbol\pi + \beta mc^2 + q\Phi, \qquad \boldsymbol\pi = \mathbf p - \frac{q}{c}\mathbf A, \quad \mathbf p = -i\hbar\nabla$$

In the Dirac representation (Ch. 3 §3.3.1):

$$\beta = \begin{pmatrix}\mathbb 1 & 0\\ 0 & -\mathbb 1\end{pmatrix}, \qquad \boldsymbol\alpha = \begin{pmatrix}0 & \boldsymbol\sigma\\ \boldsymbol\sigma & 0\end{pmatrix}$$

The defining algebra, which holds in any representation, is

$$\alpha_i^2 = \beta^2 = 1, \qquad \{\alpha_i,\alpha_j\} = 2\delta_{ij}, \qquad \{\alpha_i,\beta\} = 0, \qquad \alpha_i^\dagger = \alpha_i,\;\;\beta^\dagger = \beta$$

**Why this algebra.** For a free particle,

$$(c\boldsymbol\alpha\cdot\mathbf p + \beta mc^2)^2 = c^2\alpha_i\alpha_jp_ip_j + mc^3\{\alpha_i,\beta\}p_i + \beta^2m^2c^4 = c^2p^2 + m^2c^4$$

So every component obeys the Klein–Gordon dispersion relation $E^2 = c^2p^2 + m^2c^4$. The Clifford algebra is exactly the condition for a first-order Hamiltonian to square to the relativistic dispersion relation, and $4\times4$ is the smallest dimension in which four mutually anticommuting Hermitian matrices exist.

**From the Lagrangian.** In $(+,-,-,-)$ with $A^\mu = (\Phi,\mathbf A)$, take $\mathcal L = \bar\psi\,(i\hbar c\,\gamma^\mu D_\mu - mc^2)\,\psi$ with $D_\mu = \partial_\mu + (iq/\hbar c)A_\mu$. The spatial components give $-i\hbar D_i = p^i - (q/c)A^i = \pi^i$ (using $A_i = -A^i$), and the time component gives $i\hbar c\,D_0 = i\hbar\partial_t - q\Phi$. Varying with respect to $\bar\psi$ and multiplying by $\gamma^0$ gives $H_D$ exactly. Dividing by $c$, this is the equation of Ch. 3 §3.2.2 with $e \to q$.

> **[DERIVATION]** The Euler–Lagrange equation of the minimally coupled Dirac Lagrangian is the Hamiltonian equation $i\hbar\partial_t\psi = H_D\psi$. No approximation has been made.

**Conserved current.** Since $H_D$ is Hermitian, $\partial_t(\psi^\dagger\psi) + \nabla\cdot(c\,\psi^\dagger\boldsymbol\alpha\psi) = 0$. Multiplied by $q$, this is the Noether current of the global phase symmetry (Appendix A §A.6.2): $\rho = q\psi^\dagger\psi$ and $\mathbf J = qc\,\psi^\dagger\boldsymbol\alpha\psi$. The density $\psi^\dagger\psi \ge 0$ is conserved. Reading it as a probability density is the Born postulate (Ch. 3 §3.9.2).

---

## B.2 — Minimal Coupling: The Operator Identities

**Gauge covariance.** Under $\mathbf A \to \mathbf A + \nabla\chi$, $\Phi \to \Phi - c^{-1}\partial_t\chi$ and $\psi \to e^{iq\chi/\hbar c}\psi$, the operator $\boldsymbol\pi$ acting on $\psi$ transforms covariantly: $\boldsymbol\pi\,(e^{iq\chi/\hbar c}\psi) = e^{iq\chi/\hbar c}\,\boldsymbol\pi_{\rm old}\psi$. The combination $i\hbar\partial_t - q\Phi$ does the same. So the Dirac equation is gauge covariant, and the physical fields $\mathbf E = -\nabla\Phi - c^{-1}\partial_t\mathbf A$ and $\mathbf B = \nabla\times\mathbf A$ are gauge invariant.

**Three commutators** used throughout. Each follows from $[p_i,f(\mathbf r)] = -i\hbar\,\partial_if$.

$$[\pi_i,\,f(\mathbf r)] = -i\hbar\,\partial_if$$

$$[\pi_i,\pi_j] = -\frac{q}{c}\left([p_i,A_j] + [A_i,p_j]\right) = \frac{i\hbar q}{c}\left(\partial_iA_j - \partial_jA_i\right) = \frac{i\hbar q}{c}\,\epsilon_{ijk}B_k$$

$$(\boldsymbol\pi\times\boldsymbol\pi)_k = \epsilon_{ijk}\pi_i\pi_j = \tfrac12\epsilon_{ijk}[\pi_i,\pi_j] = \frac{i\hbar q}{c}B_k$$

**Pauli identity, with operators.** Let $\mathbf a$ and $\mathbf b$ be vector operators whose components commute with $\boldsymbol\sigma$, but not necessarily with each other. Using $\sigma_i\sigma_j = \delta_{ij} + i\epsilon_{ijk}\sigma_k$ and keeping the order $a_ib_j$:

$$(\boldsymbol\sigma\cdot\mathbf a)(\boldsymbol\sigma\cdot\mathbf b) = \mathbf a\cdot\mathbf b + i\boldsymbol\sigma\cdot(\mathbf a\times\mathbf b), \qquad (\mathbf a\times\mathbf b)_k \equiv \epsilon_{ijk}a_ib_j$$

Since $\alpha_i\alpha_j = \mathrm{diag}(\sigma_i\sigma_j,\,\sigma_i\sigma_j)$, the same identity holds with $\boldsymbol\sigma \to \boldsymbol\alpha$ on the left and $\boldsymbol\sigma \to \boldsymbol\Sigma$ on the right.

**The key identity.** Set $\mathbf a = \mathbf b = \boldsymbol\pi$:

$$\boxed{(\boldsymbol\sigma\cdot\boldsymbol\pi)^2 = \boldsymbol\pi^2 - \frac{q\hbar}{c}\,\boldsymbol\sigma\cdot\mathbf B}$$

This one line is where the spin coupling and $g = 2$ come from (§B.6). The spin term arises only because $\pi_i$ and $\pi_j$ fail to commute when $\mathbf B \neq 0$.

---

## B.3 — Even and Odd Operators

**Definitions.** An operator is **even** if it commutes with $\beta$. It is then block diagonal and does not mix upper and lower components. An operator is **odd** if it anticommutes with $\beta$. It is then block off-diagonal. Even·even and odd·odd products are even. Even·odd products are odd. The commutator of an odd operator with an even one is odd.

$$H_D = \beta mc^2 + \mathcal E + \mathcal O, \qquad \mathcal E = q\Phi, \qquad \mathcal O = c\,\boldsymbol\alpha\cdot\boldsymbol\pi, \qquad \beta\mathcal E = \mathcal E\beta, \quad \beta\mathcal O = -\mathcal O\beta$$

**What is in $\mathcal O$, and what is not.** The odd part of $H_D$ is *exactly* $c\boldsymbol\alpha\cdot\boldsymbol\pi$. The electric field does **not** appear in $\mathcal O$, as $\boldsymbol\sigma\cdot\mathbf E$ or in any other form. The reason is that $\mathbf E$ does not appear in $H_D$ at all: only the potentials $\Phi$ and $\mathbf A$ do. $\mathbf E$ first appears in §B.4 as the gauge-covariant combination generated when $\mathcal O$ fails to commute with $\mathcal E$ and with $\partial_t$:

$$[\mathcal O,\mathcal E] + i\hbar\dot{\mathcal O} = i\hbar qc\,\boldsymbol\alpha\cdot\mathbf E$$

To verify this, note $[c\alpha_k\pi_k,\,q\Phi] = -i\hbar qc\,\boldsymbol\alpha\cdot\nabla\Phi$ and $i\hbar\dot{\mathcal O} = i\hbar c\,\alpha_k\partial_t(-qA_k/c) = -i\hbar q\,\boldsymbol\alpha\cdot\partial_t\mathbf A$. Their sum is $-i\hbar qc\,\boldsymbol\alpha\cdot(\nabla\Phi + c^{-1}\partial_t\mathbf A) = i\hbar qc\,\boldsymbol\alpha\cdot\mathbf E$. This generated odd term carries the $4\times4$ matrix $\boldsymbol\alpha$, not $\boldsymbol\sigma$.

Adding an independent odd field term by hand would change the theory. An odd term proportional to $i\beta\boldsymbol\alpha\cdot\mathbf E$ is part of the Pauli anomalous-moment coupling, whose Hamiltonian form is proportional to $\beta(\boldsymbol\Sigma\cdot\mathbf B - i\boldsymbol\alpha\cdot\mathbf E)$. That coupling shifts $g$ away from 2. Minimal coupling excludes it by assumption.

**Power counting.** For a bound state of size $r$ and speed $v$: $\lvert\mathcal O\rvert \sim cp \sim mc^2(v/c)$ and $\lvert\mathcal E\rvert \sim mv^2 = mc^2(v/c)^2$ (by the virial theorem), with $\hbar/r \sim p$. The FW expansion is an expansion in $\mathcal O/mc^2 \sim v/c$. For hydrogen-like ions, $v/c \sim Z\alpha$.

---

## B.4 — The Foldy–Wouthuysen Transformation

### B.4.1 — Transformation law for a time-dependent unitary

Let $\psi' = e^{iS}\psi$ with $S$ Hermitian and possibly time dependent. Then

$$i\hbar\partial_t\psi' = e^{iS}\,i\hbar\partial_t\psi + i\hbar\,(\partial_te^{iS})\psi = \left[e^{iS}H e^{-iS} + i\hbar\,(\partial_te^{iS})\,e^{-iS}\right]\psi'$$

so $H' = e^{iS}He^{-iS} + i\hbar(\partial_te^{iS})e^{-iS}$. Unitarity is exact. Expanding with the Baker–Campbell–Hausdorff series:

$$H' = H + [iS,H] + \frac{1}{2!}[iS,[iS,H]] + \frac{1}{3!}[iS,[iS,[iS,H]]] + \frac{1}{4!}[iS,[iS,[iS,[iS,H]]]] + \dots - \hbar\dot S - \frac{i\hbar}{2}[S,\dot S] + \dots$$

### B.4.2 — First transformation

Write $M \equiv mc^2$ and choose

$$S = -\frac{i\beta\mathcal O}{2M}, \qquad iS = \frac{\beta\mathcal O}{2M}$$

$S$ is Hermitian because $(\beta\mathcal O)^\dagger = \mathcal O\beta = -\beta\mathcal O$. The building blocks follow from $\beta\mathcal O\beta = -\mathcal O$ and $[\beta,\mathcal E] = 0$:

$$[iS,\beta M] = \tfrac12(\beta\mathcal O\beta - \mathcal O) = -\mathcal O, \qquad [iS,\mathcal E] = \frac{\beta}{2M}[\mathcal O,\mathcal E], \qquad [iS,\mathcal O] = \frac{\beta\mathcal O^2}{M}$$

The first identity is the design condition: the first commutator cancels the odd term. Denote the BCH terms by $X_n = \frac1n[iS,X_{n-1}]$ with $X_0 = H$, and keep everything through $1/M^2$, together with the kinetic $1/M^3$ term $\mathcal O^4/M^3$, which is of the same order as the $1/M^2$ terms for bound states.

$$X_1 = -\mathcal O + \frac{\beta}{2M}[\mathcal O,\mathcal E] + \frac{\beta\mathcal O^2}{M}$$

$$X_2 = \frac12\left[\frac{\beta\mathcal O}{2M},\,X_1\right] = -\frac{\beta\mathcal O^2}{2M} - \frac{\mathcal O^3}{2M^2} - \frac{1}{8M^2}[\mathcal O,[\mathcal O,\mathcal E]]$$

In the last term we used $\beta[\mathcal O,\mathcal E]\beta = -[\mathcal O,\mathcal E]$, so $\big[\beta\mathcal O,\,\beta[\mathcal O,\mathcal E]\big] = -[\mathcal O,[\mathcal O,\mathcal E]]$.

$$X_3 = \frac{\mathcal O^3}{6M^2} - \frac{\beta\mathcal O^4}{6M^3} + \dots, \qquad X_4 = \frac{\beta\mathcal O^4}{24M^3} + \dots$$

The time-derivative terms, with $\dot S = -i\beta\dot{\mathcal O}/2M$, are

$$-\hbar\dot S = \frac{i\hbar\beta\dot{\mathcal O}}{2M}, \qquad -\frac{i\hbar}{2}[S,\dot S] = -\frac{i\hbar}{8M^2}[\mathcal O,\dot{\mathcal O}]$$

The second uses $[\beta\mathcal O,\beta\dot{\mathcal O}] = -[\mathcal O,\dot{\mathcal O}]$. Collecting terms, with the coefficients $\tfrac1M - \tfrac1{2M} = \tfrac1{2M}$ for $\beta\mathcal O^2$, $-\tfrac16 + \tfrac1{24} = -\tfrac18$ for $\beta\mathcal O^4/M^3$, and $-\tfrac12 + \tfrac16 = -\tfrac13$ for $\mathcal O^3/M^2$:

$$H' = \beta M + \mathcal E' + \mathcal O'$$

$$\mathcal E' = \mathcal E + \beta\left(\frac{\mathcal O^2}{2M} - \frac{\mathcal O^4}{8M^3}\right) - \frac{1}{8M^2}\Big[\mathcal O,\;[\mathcal O,\mathcal E] + i\hbar\dot{\mathcal O}\Big]$$

$$\mathcal O' = \frac{\beta}{2M}\Big([\mathcal O,\mathcal E] + i\hbar\dot{\mathcal O}\Big) - \frac{\mathcal O^3}{3M^2}$$

The original odd operator, of order $M(v/c)$, has been replaced by $\mathcal O'$, of order $M(v/c)^3$. Ch. 3 §3.5.2 states the same reduction.

### B.4.3 — Second and third transformations

$H'$ has the same structure as $H$, with $\mathcal O \to \mathcal O'$ and $\mathcal E \to \mathcal E'$. Repeat with $S' = -i\beta\mathcal O'/2M$:

$$H'' = \beta M + \mathcal E' + \underbrace{\frac{\beta}{2M}\Big([\mathcal O',\mathcal E'] + i\hbar\dot{\mathcal O}'\Big)}_{\mathcal O''\,\sim\,1/M^2} + \underbrace{\frac{\beta\mathcal O'^2}{2M} + \dots}_{\text{even},\;\sim M(v/c)^6}$$

A third transformation with $S'' = -i\beta\mathcal O''/2M$ removes $\mathcal O''$ and leaves only even corrections of order $M(v/c)^6$. To the order retained, the result is

$$\boxed{H_{FW} = \beta\left(mc^2 + \frac{\mathcal O^2}{2mc^2} - \frac{\mathcal O^4}{8m^3c^6}\right) + \mathcal E - \frac{1}{8m^2c^4}\Big[\mathcal O,\;[\mathcal O,\mathcal E] + i\hbar\dot{\mathcal O}\Big] + \mathcal{O}\!\left(mc^2(v/c)^6\right)}$$

This is the general result of Foldy & Wouthuysen (1950), in the form given by Bjorken & Drell, *Relativistic Quantum Mechanics*. Every term is even, so the Hamiltonian is block diagonal.

> **[APPROXIMATION]** Each FW step is an exact unitary transformation, but the generators are fixed order by order, and the sequence is stopped after removing odd terms through $1/M^2$. The small parameter is $v/c$ (equivalently $\lvert\mathcal O\rvert/mc^2$). The boxed $H_{FW}$ is exact through relative order $(v/c)^2$ beyond the Schrödinger terms and wrong at order $(v/c)^4$. It also requires the field conditions of §B.11.

### B.4.4 — Check: the free particle, exactly

For $\Phi = 0$ and $\mathbf A = 0$, $\mathcal O = c\boldsymbol\alpha\cdot\mathbf p$ commutes with itself at all times and $\mathcal O^2 = c^2p^2$. Foldy and Wouthuysen found the exact transformation $e^{iS} = \exp(\beta\boldsymbol\alpha\cdot\hat{\mathbf p}\,\theta)$, with $\tan 2\theta = p/mc$. Since $(\beta\boldsymbol\alpha\cdot\hat{\mathbf p})^2 = -1$, this equals $\cos\theta + \beta\boldsymbol\alpha\cdot\hat{\mathbf p}\sin\theta$. It gives

$$H_{FW}^{\rm free} = \beta\sqrt{c^2p^2 + m^2c^4} = \beta\left(mc^2 + \frac{p^2}{2m} - \frac{p^4}{8m^3c^2} + \dots\right)$$

This agrees term by term with the boxed series. For the free particle the expansion converges for $p < mc$. For a general external field no closed form exists, and the series is at best asymptotic.

---

## B.5 — Evaluating $H_{FW}$ for Electromagnetic Fields

**Kinetic term.** By §B.2 with $\boldsymbol\alpha\boldsymbol\alpha \to \boldsymbol\Sigma$,

$$\frac{\beta\mathcal O^2}{2mc^2} = \frac{\beta(\boldsymbol\alpha\cdot\boldsymbol\pi)^2}{2m} = \beta\left(\frac{\boldsymbol\pi^2}{2m} - \frac{q\hbar}{2mc}\boldsymbol\Sigma\cdot\mathbf B\right)$$

$$-\frac{\beta\mathcal O^4}{8m^3c^6} = -\frac{\beta}{8m^3c^2}\left(\boldsymbol\pi^2 - \frac{q\hbar}{c}\boldsymbol\Sigma\cdot\mathbf B\right)^2 = -\beta\frac{\boldsymbol\pi^4}{8m^3c^2} + (\text{terms} \propto \mathbf B)$$

The dropped $\mathbf B$-dependent pieces are relativistic corrections to the Zeeman term. Relative to it they are of order $(v/c)^2$, plus a term of order $\hbar\lvert q\rvert B/m^2c^3$. They are negligible for laboratory fields and are not retained in Ch. 3.

**The commutator term.** By §B.3, $[\mathcal O,\mathcal E] + i\hbar\dot{\mathcal O} = i\hbar qc\,\boldsymbol\alpha\cdot\mathbf E$, so

$$-\frac{1}{8m^2c^4}\Big[c\boldsymbol\alpha\cdot\boldsymbol\pi,\;i\hbar qc\,\boldsymbol\alpha\cdot\mathbf E\Big] = -\frac{i\hbar q}{8m^2c^2}\,\big[\boldsymbol\alpha\cdot\boldsymbol\pi,\;\boldsymbol\alpha\cdot\mathbf E\big]$$

Evaluate the commutator with the Pauli identity in $\boldsymbol\Sigma$ form, keeping operator order:

$$(\boldsymbol\alpha\cdot\boldsymbol\pi)(\boldsymbol\alpha\cdot\mathbf E) = \boldsymbol\pi\cdot\mathbf E + i\boldsymbol\Sigma\cdot(\boldsymbol\pi\times\mathbf E), \qquad (\boldsymbol\alpha\cdot\mathbf E)(\boldsymbol\alpha\cdot\boldsymbol\pi) = \mathbf E\cdot\boldsymbol\pi + i\boldsymbol\Sigma\cdot(\mathbf E\times\boldsymbol\pi)$$

Two reorderings follow from $[\pi_i,E_j] = -i\hbar\partial_iE_j$:

$$\boldsymbol\pi\cdot\mathbf E - \mathbf E\cdot\boldsymbol\pi = -i\hbar\,\nabla\cdot\mathbf E, \qquad \boldsymbol\pi\times\mathbf E = -\mathbf E\times\boldsymbol\pi - i\hbar\,\nabla\times\mathbf E$$

Hence

$$\big[\boldsymbol\alpha\cdot\boldsymbol\pi,\;\boldsymbol\alpha\cdot\mathbf E\big] = -i\hbar\,\nabla\cdot\mathbf E - 2i\,\boldsymbol\Sigma\cdot(\mathbf E\times\boldsymbol\pi) + \hbar\,\boldsymbol\Sigma\cdot(\nabla\times\mathbf E)$$

Multiplying by $-i\hbar q/8m^2c^2$:

$$-\frac{q\hbar^2}{8m^2c^2}\nabla\cdot\mathbf E \;-\; \frac{q\hbar}{4m^2c^2}\boldsymbol\Sigma\cdot(\mathbf E\times\boldsymbol\pi) \;-\; \frac{iq\hbar^2}{8m^2c^2}\boldsymbol\Sigma\cdot(\nabla\times\mathbf E)$$

The last two terms combine into a manifestly Hermitian operator, $-\frac{q\hbar}{8m^2c^2}\boldsymbol\Sigma\cdot(\mathbf E\times\boldsymbol\pi - \boldsymbol\pi\times\mathbf E)$. Neither is Hermitian alone. For static fields, $\nabla\times\mathbf E = -c^{-1}\partial_t\mathbf B = 0$, and the spin–orbit term reduces to its familiar form.

**Projection onto the positive-energy block.** $H_{FW}$ is block diagonal. Its $\beta = +1$ block acts on two-component spinors, which are the large components in the FW basis, with $\boldsymbol\Sigma \to \boldsymbol\sigma$. The result is

$$\boxed{H_{FW}^{(+)} = mc^2 + \frac{\boldsymbol\pi^2}{2m} + q\Phi \underbrace{- \frac{q\hbar}{2mc}\boldsymbol\sigma\cdot\mathbf B}_{\text{Zeeman}} \underbrace{- \frac{\boldsymbol\pi^4}{8m^3c^2}}_{\text{mass}} \underbrace{- \frac{q\hbar}{8m^2c^2}\boldsymbol\sigma\cdot(\mathbf E\times\boldsymbol\pi - \boldsymbol\pi\times\mathbf E)}_{\text{spin–orbit}} \underbrace{- \frac{q\hbar^2}{8m^2c^2}\nabla\cdot\mathbf E}_{\text{Darwin}}}$$

**In terms of the potential energy.** For a static electric field write $V = q\Phi$, so that $q\mathbf E = -\nabla V$. The two electric terms become **independent of the sign of $q$**:

$$H_{SO} = \frac{\hbar}{4m^2c^2}\,\boldsymbol\sigma\cdot(\nabla V\times\mathbf p) \;\xrightarrow{\;V = V(r)\;}\; \frac{1}{2m^2c^2}\,\frac{1}{r}\frac{dV}{dr}\,\mathbf L\cdot\mathbf S, \qquad H_{D} = \frac{\hbar^2}{8m^2c^2}\,\nabla^2V$$

Here $\mathbf S = \hbar\boldsymbol\sigma/2$, and for a central field $\nabla V = (V'/r)\,\mathbf r$, so $\nabla V\times\mathbf p = (V'/r)\,\mathbf L$. The central-field form is the one used in Ch. 5 §5.5.

**For the electron** ($q = -e$): the Zeeman term is $+\frac{e\hbar}{2mc}\boldsymbol\sigma\cdot\mathbf B$, the spin–orbit term is $+\frac{e\hbar}{4m^2c^2}\boldsymbol\sigma\cdot(\mathbf E\times\mathbf p)$ (static field), and the Darwin term is $+\frac{e\hbar^2}{8m^2c^2}\nabla\cdot\mathbf E$. In the Coulomb field of a nucleus, $V = -Ze^2/r$, so $V' > 0$ and $\nabla^2V = 4\pi Ze^2\,\delta^3(\mathbf r)$. Both $H_{SO}$ and $H_D$ are then positive operators on the relevant states.

> **[DERIVATION]** Given the truncated FW Hamiltonian of §B.4.3, the five terms above follow by exact operator algebra, with no further approximation apart from dropping the $\mathbf B$-dependent parts of $\mathcal O^4$. **Convention check against Ch. 3 §3.5.3:** the Zeeman and spin–orbit terms there match the boxed expression with $q \to e$. The Darwin term as printed there carries the opposite sign, $+e\hbar^2\nabla\cdot\mathbf E/8m^2c^2$, which is the electron value with $e > 0$. The $V$ form above is free of this ambiguity.

---

## B.6 — The Pauli Hamiltonian, the Zeeman Term, and $g = 2$

**Truncation.** Drop the rest energy and the three terms of relative order $(v/c)^2$:

$$H_{\rm Pauli} = \frac{\boldsymbol\pi^2}{2m} + q\Phi - \frac{q\hbar}{2mc}\boldsymbol\sigma\cdot\mathbf B = \frac{(\boldsymbol\sigma\cdot\boldsymbol\pi)^2}{2m} + q\Phi$$

> **[APPROXIMATION]** Pauli from FW: discard terms of order $mc^2(v/c)^4$, that is, relative order $(v/c)^2 \sim (Z\alpha)^2$ for bound states. Valid when fine structure need not be resolved (Ch. 3 §3.6 Ledger).

**Orbital and spin moments.** Expand $\boldsymbol\pi^2 = p^2 - \frac qc(\mathbf p\cdot\mathbf A + \mathbf A\cdot\mathbf p) + \frac{q^2}{c^2}A^2$, with $\mathbf p\cdot\mathbf A = \mathbf A\cdot\mathbf p - i\hbar\nabla\cdot\mathbf A$. For a uniform field, choose $\mathbf A = \tfrac12\mathbf B\times\mathbf r$. It satisfies $\nabla\cdot\mathbf A = 0$, and $\mathbf A\cdot\mathbf p = \tfrac12(\mathbf B\times\mathbf r)\cdot\mathbf p = \tfrac12\mathbf B\cdot\mathbf L$. Then

$$H_{\rm Pauli} = \frac{p^2}{2m} + q\Phi - \frac{q}{2mc}\left(\mathbf L + 2\mathbf S\right)\cdot\mathbf B + \frac{q^2}{8mc^2}(\mathbf B\times\mathbf r)^2$$

The magnetic moment operator is therefore $\boldsymbol\mu = \frac{q}{2mc}(g_L\mathbf L + g_S\mathbf S)$ with $g_L = 1$ and $g_S = 2$. For the electron this is $+\frac{\mu_B}{\hbar}(\mathbf L + 2\mathbf S)\cdot\mathbf B$, with $\mu_B = e\hbar/2mc$ (Gaussian), which is $e\hbar/2m = 9.274\times10^{-24}$ J/T in SI. That is the Hamiltonian of Ch. 5 §5.6.1. The last term is the diamagnetic term. Relative to the Zeeman term it is of order $B/B_{\rm at}$, with $B_{\rm at} = \hbar/(ea_0^2) \approx 2.35\times10^5$ T in SI, so it is negligible for atoms in laboratory fields.

**Where $g = 2$ comes from.** The factor 2 is the coefficient in the identity $(\boldsymbol\sigma\cdot\boldsymbol\pi)^2 = \boldsymbol\pi^2 - (q\hbar/c)\boldsymbol\sigma\cdot\mathbf B$. The FW kinetic term is $\mathcal O^2/2mc^2 = (\boldsymbol\alpha\cdot\boldsymbol\pi)^2/2m$: the Dirac Hamiltonian is linear in $\boldsymbol\pi$, so its square necessarily produces the spin term with this coefficient. Three qualifications prevent an overclaim.

1. **Minimal coupling is an input.** A Pauli term $\propto\bar\psi\sigma^{\mu\nu}F_{\mu\nu}\psi$ is Lorentz and gauge invariant and would add an arbitrary anomalous moment. It is excluded from the fundamental Lagrangian because it has mass dimension five and is non-renormalizable. So $g = 2$ is the prediction of the **minimally coupled** Dirac equation, not of the Clifford algebra alone (compare Ch. 3 §3.4.2).
2. **It is not specifically relativistic.** Lévy-Leblond (1967) showed that a Galilean-invariant first-order linearization of the Schrödinger equation, minimally coupled, also gives $g = 2$. What forces $g = 2$ is linearity in $\boldsymbol\pi$, and the Dirac equation is the relativistic instance of that structure.
3. **QED corrects it.** Radiative corrections give $a_e = (g-2)/2 = \alpha/2\pi + \mathcal O(\alpha^2)$ (Schwinger, 1948), so that $g_e \approx 2.00231930$. This was discarded in Ch. 3 §3.1.2.

> **[DERIVATION]** Within the minimally coupled Dirac theory, $g_S = 2$ and $g_L = 1$ follow exactly from the operator identity of §B.2. The **[APPROXIMATION]** is only the truncation of the FW series that brings the Hamiltonian into Pauli form.

---

## B.7 — The Three $(v/c)^2$ Terms

**Relativistic mass correction.** For the free particle (§B.4.4), $-p^4/8m^3c^2$ is the second term of $\sqrt{c^2p^2 + m^2c^4}$. It is the relativistic kinetic-energy correction. In a field, $\mathbf p \to \boldsymbol\pi$.

**Spin–orbit coupling and the Thomas factor.** The following semiclassical estimate serves as a check. In the particle's instantaneous rest frame there is, to first order in $v/c$, a magnetic field $\mathbf B' = -\frac{1}{c}\mathbf v\times\mathbf E$. A moment $\boldsymbol\mu = g\frac{q}{2mc}\mathbf S$ in that field has energy

$$-\boldsymbol\mu\cdot\mathbf B' = -\frac{gq}{2m^2c^2}\,\mathbf S\cdot(\mathbf E\times\mathbf p)$$

With $g = 2$ this is **twice** the FW result $-\frac{q}{2m^2c^2}\mathbf S\cdot(\mathbf E\times\mathbf p)$ (from §B.5 with $\hbar\boldsymbol\sigma = 2\mathbf S$). The discrepancy is the **Thomas precession**. The rest frame of an accelerated particle rotates relative to the lab at $\boldsymbol\omega_T \approx \frac{1}{2c^2}\mathbf a\times\mathbf v$. Transforming the spin energy to the lab frame replaces $g$ by $g - 1$, so that $H_{SO} = -\frac{(g-1)q}{2m^2c^2}\mathbf S\cdot(\mathbf E\times\mathbf p)$. See Jackson, *Classical Electrodynamics*, Ch. 11. For $g = 2$ the factor is $1$, which is exactly the FW coefficient.

> **[STRUCTURAL CONNECTION]** The FW derivation and the semiclassical rest-frame-plus-Thomas argument are independent calculations that agree. In the FW derivation the factor ½ is not inserted. It is the coefficient $-1/8M^2$ of the double commutator, doubled by the two orderings in $\boldsymbol\Sigma\cdot(\mathbf E\times\boldsymbol\pi - \boldsymbol\pi\times\mathbf E)$. The semiclassical argument shows **what that factor means**.

**Darwin term.** $H_D = \frac{\hbar^2}{8m^2c^2}\nabla^2V$ has no nonrelativistic analogue and acts only where $\nabla^2V \neq 0$. For a point Coulomb source that is the origin, so it shifts only $s$ states.

> **[ANALOGY]** Here is a picture, not a derivation. If the electron's effective position fluctuates isotropically by $\delta\mathbf r$ with $\langle\delta r^2\rangle$ of order the squared reduced Compton wavelength $(\hbar/mc)^2$, then $\langle V(\mathbf r + \delta\mathbf r)\rangle \approx V + \tfrac16\langle\delta r^2\rangle\nabla^2V$. This matches the Darwin form if $\langle\delta r^2\rangle = \tfrac34(\hbar/mc)^2$. The coefficient is not fixed by the picture. The precise statement is that the FW-basis position operator is a nonlocal transform of the Dirac position operator, smeared over $\sim\hbar/mc$ (the Newton–Wigner position).

---

## B.8 — Hydrogen Fine Structure to Order $\alpha^4$

### B.8.1 — Setup

**Assumptions.**
- (H1) A point nucleus of charge $Ze$ and infinite mass (no recoil and no reduced mass), so $V = -Ze^2/r$.
- (H2) $\mathbf B = 0$, and the fields are static.
- (H3) No hyperfine structure and no QED corrections.
- (H4) $(Z\alpha)^2 \ll 1$.

The Hamiltonian is $H = H_0 + H_1$, with $H_0 = p^2/2m + V$ and $E_n^{(0)} = -mc^2(Z\alpha)^2/2n^2$ (Ch. 4 §4.7.3 with $Z = 1$), and

$$H_1 = H_{\rm rel} + H_{SO} + H_D = -\frac{p^4}{8m^3c^2} + \frac{Ze^2}{2m^2c^2}\frac{1}{r^3}\,\mathbf L\cdot\mathbf S + \frac{\pi\hbar^2Ze^2}{2m^2c^2}\,\delta^3(\mathbf r)$$

**Why first-order perturbation theory in the $\lvert n\,\ell\,j\,m_j\rangle$ basis is legitimate.** The level $n$ is $2n^2$-fold degenerate, so degenerate perturbation theory is required in principle. $H_{\rm rel}$ and $H_D$ are spin independent and rotationally scalar. $H_{SO} \propto \xi(r)\,\mathbf L\cdot\mathbf S$ commutes with $\mathbf L^2$, $\mathbf S^2$, $\mathbf J^2$ and $J_z$. All three are parity even. Within the shell, states with equal $(j,m_j)$ but different $\ell = j\pm\tfrac12$ have opposite parity and cannot mix. So $H_1$ is already diagonal in $\lvert n\,\ell\,j\,m_j\rangle$, and the first-order shifts are its diagonal expectation values. They are of order $(Z\alpha)^2E_n^{(0)}$. Second-order shifts would be of order $(Z\alpha)^4E_n^{(0)}$, which is the same order as the FW terms already discarded, so including them without the next FW order would be inconsistent.

### B.8.2 — Radial expectation values

With $a \equiv a_0/Z$:

$$\Big\langle\frac1r\Big\rangle = \frac{1}{n^2a}, \qquad \Big\langle\frac1{r^2}\Big\rangle = \frac{1}{n^3(\ell+\frac12)a^2}, \qquad \Big\langle\frac1{r^3}\Big\rangle = \frac{1}{n^3\,\ell(\ell+\frac12)(\ell+1)\,a^3}\;\;(\ell\ge1), \qquad \lvert\psi_{n00}(0)\rvert^2 = \frac{1}{\pi n^3a^3}$$

*Proofs.* (i) **Virial theorem.** For a $1/r$ potential, $\langle V\rangle = 2E_n^{(0)}$, which gives $\langle 1/r\rangle$. (ii) **Feynman–Hellmann in $\ell$.** The radial Hamiltonian is $H_\ell = p_r^2/2m + \hbar^2\ell(\ell+1)/2mr^2 - Ze^2/r$, with $E = -Ze^2/(2a\,n^2)$ and $n = n_r + \ell + 1$. Treat $\ell$ as a continuous parameter at fixed $n_r$. Then $\partial E/\partial\ell = Ze^2/(a\,n^3)$ and $\partial H_\ell/\partial\ell = \hbar^2(2\ell+1)/2mr^2$. Equating them and using $me^2/\hbar^2 = 1/a_0$ gives $\langle1/r^2\rangle$. (iii) **Radial commutator.** $\langle[H_\ell,p_r]\rangle = 0$ in a bound state implies $\langle dV_{\rm eff}/dr\rangle = 0$ for $\ell\ge1$, that is $\hbar^2\ell(\ell+1)\langle r^{-3}\rangle/m = Ze^2\langle r^{-2}\rangle$, which gives $\langle1/r^3\rangle$. For $\ell = 0$ the same identity acquires a boundary term at $r = 0$. It becomes $\lvert\psi(0)\rvert^2 = \frac{m}{2\pi\hbar^2}\langle dV/dr\rangle$, which with (ii) gives the last formula. A standard reference is Bethe & Salpeter, *Quantum Mechanics of One- and Two-Electron Atoms*.

It is convenient to note $\big(E_n^{(0)}\big)^2/mc^2 = mc^2(Z\alpha)^4/4n^4$.

### B.8.3 — The three shifts

**Mass correction.** Write $p^4/4m^2 = (H_0 - V)^2$. The expectation value is computed as $\langle p^2\psi\,\vert\,p^2\psi\rangle$, using the hermiticity of $p^2$. That avoids the $\delta$-function subtleties of applying $p^4$ to $s$ states.

$$\Delta E_{\rm rel} = -\frac{1}{2mc^2}\left[(E_n^{(0)})^2 - 2E_n^{(0)}\langle V\rangle + \langle V^2\rangle\right] = -\frac{(E_n^{(0)})^2}{2mc^2}\left[\frac{4n}{\ell+\frac12} - 3\right]$$

This uses $\langle V\rangle = 2E_n^{(0)}$ and $\langle V^2\rangle = Z^2e^4\langle r^{-2}\rangle = 4(E_n^{(0)})^2\,n/(\ell+\tfrac12)$.

**Spin–orbit** ($\ell\ge1$). $\langle\mathbf L\cdot\mathbf S\rangle = \frac{\hbar^2}{2}\left[j(j+1) - \ell(\ell+1) - \tfrac34\right]$, which equals $\frac{\hbar^2}{2}\ell$ for $j = \ell+\tfrac12$ and $-\frac{\hbar^2}{2}(\ell+1)$ for $j = \ell-\tfrac12$. With $\hbar^2 = me^2a_0$:

$$\Delta E_{SO} = \frac{(E_n^{(0)})^2}{2mc^2}\cdot\frac{2n\left[j(j+1) - \ell(\ell+1) - \frac34\right]}{\ell(\ell+\frac12)(\ell+1)} = \frac{(E_n^{(0)})^2}{2mc^2}\times\begin{cases}\dfrac{2n}{(\ell+\frac12)(\ell+1)} & j = \ell+\frac12\\[2ex] -\dfrac{2n}{\ell(\ell+\frac12)} & j = \ell-\frac12\end{cases}$$

For $\ell = 0$, $\mathbf L\cdot\mathbf S = 0$ exactly, while $\langle r^{-3}\rangle$ diverges. The product is assigned the value 0. The Darwin term then supplies the $s$-state shift.

**Darwin** ($\ell = 0$ only):

$$\Delta E_D = \frac{\pi\hbar^2Ze^2}{2m^2c^2}\lvert\psi_{n00}(0)\rvert^2 = \frac{(E_n^{(0)})^2}{2mc^2}\cdot4n\;\delta_{\ell0}$$

### B.8.4 — The sum

For $j = \ell+\tfrac12$:

$$\frac{4n}{\ell+\frac12}\left(1 - \frac{1}{2(\ell+1)}\right) = \frac{4n}{\ell+\frac12}\cdot\frac{2\ell+1}{2(\ell+1)} = \frac{4n}{\ell+1} = \frac{4n}{j+\frac12}$$

For $j = \ell-\tfrac12$:

$$\frac{4n}{\ell+\frac12}\left(1 + \frac{1}{2\ell}\right) = \frac{4n}{\ell} = \frac{4n}{j+\frac12}$$

For $\ell = 0$ the Darwin term contributes $+4n$ and $\Delta E_{\rm rel}$ contributes $-(8n - 3)$, so the bracket is $3 - 4n = 3 - 4n/(j+\tfrac12)$ with $j = \tfrac12$. The Darwin shift has exactly the value that the $j = \ell+\frac12$ spin–orbit formula would give if continued to $\ell = 0$. All cases collapse to

$$\boxed{\Delta E_{nj} = \frac{(E_n^{(0)})^2}{2mc^2}\left[3 - \frac{4n}{j+\frac12}\right] = -\frac{mc^2(Z\alpha)^4}{2n^4}\left(\frac{n}{j+\frac12} - \frac34\right)}$$

The shift depends on $n$ and $j$ only, not on $\ell$. So $2S_{1/2}$ and $2P_{1/2}$ remain degenerate.

> **[DERIVATION]** The fine-structure formula follows by first-order perturbation theory from the truncated FW Hamiltonian under (H1)–(H4). It agrees with the $\alpha^4$ term of the exact Dirac energy (§B.9), which is the check stated in Ch. 3 §3.4.4.

**Numbers, hydrogen ($Z = 1$).** $mc^2\alpha^4 = 1.449\times10^{-3}$ eV.
- Ground state: $\Delta E_{1,1/2} = -mc^2\alpha^4/8 = -1.81\times10^{-4}$ eV.
- $n = 2$: $\Delta E_{2,1/2} = -5mc^2\alpha^4/128$ and $\Delta E_{2,3/2} = -mc^2\alpha^4/128$, so the $2P_{3/2}$–$2P_{1/2}$ splitting is $mc^2\alpha^4/32 = 4.53\times10^{-5}$ eV $\approx 10.95$ GHz. This is the value quoted in Ch. 5 §5.5.4. The measured interval is $\approx 10.97$ GHz. The $\approx 0.2\%$ residual is dominated by QED, chiefly the anomalous moment, which scales the spin–orbit term by $\approx 1 + 2a_e$. The $2S_{1/2}$–$2P_{1/2}$ Lamb shift, $\approx 1.06$ GHz, is pure QED and is absent here.

**Where it fails.** For large $Z$ the neglected $(Z\alpha)^6$ terms grow (§B.9). Recoil enters at relative order $m/M_N$, and the leading part is captured by using the reduced mass in $E_n^{(0)}$. Hyperfine structure enters at order $\alpha^4(m/m_p)g_p$. Finite nuclear size modifies the $s$-state Darwin term. In many-electron atoms, $V$ is a screened potential and the shifts must be recomputed with it (Ch. 5 §5.5).

---

## B.9 — The Exact Dirac–Coulomb Energy and Its Expansion

**Separation.** With $V(r) = -Ze^2/r = -Z\alpha\hbar c/r$, the conserved quantities are $\mathbf J^2$, $J_z$, parity, and Dirac's operator $K = \beta(\boldsymbol\Sigma\cdot\mathbf L + \hbar)$. The eigenvalue of $K$ is $-\hbar\kappa$ with $\kappa = \mp(j+\tfrac12)$ for $j = \ell\pm\tfrac12$. Write $\psi = r^{-1}\big(G(r)\,\Omega_{\kappa m},\; iF(r)\,\Omega_{-\kappa m}\big)$, with spin–angular functions $\Omega$. The radial equations are

$$\frac{dG}{dr} + \frac{\kappa}{r}G - \frac{E + mc^2 - V}{\hbar c}F = 0, \qquad \frac{dF}{dr} - \frac{\kappa}{r}F + \frac{E - mc^2 - V}{\hbar c}G = 0$$

Sign conventions for $\kappa$ differ between texts. These equations are consistent with the stated $\kappa$: for $E \approx mc^2$, eliminating $F \approx \frac{\hbar}{2mc}(G' + \kappa G/r)$ gives $G'' - \frac{\kappa(\kappa+1)}{r^2}G + \frac{2m}{\hbar^2}(E - mc^2 - V)G = 0$. Since $\kappa(\kappa+1) = \ell(\ell+1)$ in both cases, this is the Schrödinger radial equation of Ch. 4 §4.7.

**Behaviour at the origin.** For $r \to 0$, $(E \pm mc^2 - V)/\hbar c \to Z\alpha/r$. Try $G \sim a\,r^s$ and $F \sim b\,r^s$:

$$(s+\kappa)\,a - Z\alpha\,b = 0, \qquad Z\alpha\,a + (s-\kappa)\,b = 0 \quad\Longrightarrow\quad s^2 = \kappa^2 - (Z\alpha)^2$$

The regular solution has $s = \sqrt{\kappa^2 - (Z\alpha)^2}$. It is real only for $Z\alpha < \lvert\kappa\rvert$.

**Quantization.** At large $r$ the solutions decay as $e^{-\lambda r}$, with $\hbar c\lambda = \sqrt{m^2c^4 - E^2}$. Writing $G$ and $F$ as $r^se^{-\lambda r}$ times power series, normalizability requires both series to terminate. That condition yields

$$E_{n_r\kappa} = mc^2\left[1 + \frac{(Z\alpha)^2}{\left(n_r + \sqrt{\kappa^2 - (Z\alpha)^2}\right)^2}\right]^{-1/2}, \qquad n_r = 0,1,2,\dots$$

with $n_r = 0$ allowed only for $\kappa < 0$. The termination argument, a confluent-hypergeometric analysis, is lengthy and is **not reproduced here**. See Bjorken & Drell, *Relativistic Quantum Mechanics*; Berestetskii, Lifshitz & Pitaevskii, *Quantum Electrodynamics*; or Sakurai, *Advanced Quantum Mechanics*. With $n = n_r + \lvert\kappa\rvert$ and $\lvert\kappa\rvert = j+\frac12$, this is the formula of Ch. 3 §3.4.4.

**Expansion.** Let $x = Z\alpha$ and $k = j+\tfrac12$. Then $\sqrt{k^2 - x^2} = k - \frac{x^2}{2k} + \mathcal O(x^4)$, so $n_r + \sqrt{k^2-x^2} = n - \frac{x^2}{2k} + \mathcal O(x^4)$, and

$$y \equiv \frac{x^2}{(n - x^2/2k)^2} = \frac{x^2}{n^2} + \frac{x^4}{n^3k} + \mathcal O(x^6), \qquad (1+y)^{-1/2} = 1 - \frac y2 + \frac{3y^2}{8} + \mathcal O(y^3)$$

$$\boxed{E_{nj} = mc^2\left[1 - \frac{(Z\alpha)^2}{2n^2} - \frac{(Z\alpha)^4}{2n^4}\left(\frac{n}{j+\frac12} - \frac34\right) + \mathcal O\big((Z\alpha)^6\big)\right]}$$

The second term is the Bohr energy. The third is **identical** to the FW perturbative result of §B.8.4.

> **[DERIVATION]** The $\alpha^4$ fine structure obtained from the truncated FW Hamiltonian agrees with the expansion of the exact Dirac eigenvalue. Two independent routes, an exact solution and a systematic expansion, give the same coefficient. Agreement at this order does not validate the FW series at higher orders, where it must be handled with care (§B.11).

**Where the expansion fails: a heavy-atom example.** For the $1s$ state, $E = mc^2\sqrt{1-(Z\alpha)^2}$, so the binding energy is $mc^2\big(1 - \sqrt{1-x^2}\big) = mc^2\big(\tfrac{x^2}{2} + \tfrac{x^4}{8} + \tfrac{x^6}{16} + \dots\big)$. For $Z = 82$, $x = 0.598$. The exact point-nucleus value is $0.1988\,mc^2 \approx 101.6$ keV, while the series truncated at $x^4$ gives $0.1951\,mc^2 \approx 99.7$ keV. The error is about 2%, and the $x^6$ term already accounts for most of it. As $Z\alpha \to 1$, $s \to 0$ for $\lvert\kappa\rvert = 1$ and the point-nucleus solution ceases to exist. With a finite nucleus the $1s$ level reaches $E = -mc^2$ near $Z \approx 170$. Beyond that point the vacuum becomes unstable to pair creation, and single-particle theory is meaningless (Ch. 3 §3.8).

---

## B.10 — The Gordon Decomposition and $g = 2$

**Assumptions.** Natural units $\hbar = c = 1$ for this section, signature $(+,-,-,-)$, $D_\mu = \partial_\mu + iqA_\mu$, and $\sigma^{\mu\nu} = \frac{i}{2}[\gamma^\mu,\gamma^\nu]$, so that $\gamma^\mu\gamma^\nu = \eta^{\mu\nu} - i\sigma^{\mu\nu}$ and $\gamma^\nu\gamma^\mu = \eta^{\mu\nu} + i\sigma^{\mu\nu}$. The field $\psi$ satisfies $i\gamma^\nu D_\nu\psi = m\psi$, and its adjoint satisfies $-i\,(\partial_\nu - iqA_\nu)\bar\psi\,\gamma^\nu = m\bar\psi$.

**Derivation.** Write $\bar\psi\gamma^\mu\psi$ half with $\psi = m^{-1}i\gamma^\nu D_\nu\psi$ and half with the adjoint equation:

$$\bar\psi\gamma^\mu\psi = \frac{1}{2m}\Big[\bar\psi\gamma^\mu\gamma^\nu(iD_\nu\psi) + \big(-i\overline{D_\nu\psi}\big)\gamma^\nu\gamma^\mu\psi\Big]$$

Insert the two product formulas. The $\eta^{\mu\nu}$ pieces give $\frac{i}{2m}\big[\bar\psi D^\mu\psi - \overline{D^\mu\psi}\,\psi\big]$. The $\sigma^{\mu\nu}$ pieces give $\frac{1}{2m}\big[\bar\psi\sigma^{\mu\nu}D_\nu\psi + \overline{D_\nu\psi}\,\sigma^{\mu\nu}\psi\big]$. In the second bracket the gauge terms $\pm iqA_\nu$ cancel, leaving a total derivative:

$$\boxed{J^\mu = q\bar\psi\gamma^\mu\psi = \underbrace{\frac{iq}{2m}\Big[\bar\psi D^\mu\psi - \overline{D^\mu\psi}\,\psi\Big]}_{\text{convective}} + \underbrace{\frac{q}{2m}\,\partial_\nu\big(\bar\psi\sigma^{\mu\nu}\psi\big)}_{\text{spin (magnetization/polarization)}}}$$

For plane waves $\psi = u(p)e^{-ip\cdot x}$ and $\bar\psi = \bar u(p')e^{ip'\cdot x}$ with $A = 0$, this becomes the familiar
$$\bar u(p')\gamma^\mu u(p) = \bar u(p')\left[\frac{(p+p')^\mu}{2m} + \frac{i\sigma^{\mu\nu}(p'-p)_\nu}{2m}\right]u(p)$$

**Reading off $g = 2$.** In the Dirac representation $\sigma^{ij} = \epsilon_{ijk}\Sigma_k$ (for example, $\sigma^{12} = \tfrac i2[\gamma^1,\gamma^2] = \Sigma_3$) and $\sigma^{0i} = i\alpha_i$. The spatial part of the spin term is

$$\frac{q}{2m}\partial_j\big(\bar\psi\sigma^{ij}\psi\big) + \frac{q}{2m}\partial_0\big(\bar\psi\sigma^{i0}\psi\big) = \big(\nabla\times\mathbf M\big)^i + \partial_t P^i, \qquad \mathbf M = \frac{q}{2m}\bar\psi\boldsymbol\Sigma\psi$$

The polarization piece $\mathbf P$ involves $\bar\psi\boldsymbol\alpha\psi$, which mixes large and small components, and is suppressed by $v/c$. In the nonrelativistic limit, $\bar\psi\boldsymbol\Sigma\psi = \phi^\dagger\boldsymbol\sigma\phi - \chi^\dagger\boldsymbol\sigma\chi \to \phi^\dagger\boldsymbol\sigma\phi$. Restoring units, $\mathbf M = \frac{q\hbar}{2mc}\,\phi^\dagger\boldsymbol\sigma\phi = 2\cdot\frac{q}{2mc}\,\phi^\dagger\mathbf S\phi$ in Gaussian units. A magnetization current $c\nabla\times\mathbf M$ couples to an external field through $-\frac1c\int\mathbf J\cdot\mathbf A\,d^3x = -\int\mathbf M\cdot\mathbf B\,d^3x$ after integrating by parts. That is a spin moment with $g_S = 2$. The convective term carries the orbital current, with $g_L = 1$.

> **[DERIVATION]** The Gordon decomposition is an exact identity on solutions of the minimally coupled Dirac equation. It shows that the Dirac current already contains a spin-magnetization current with gyromagnetic ratio $2\times q/2mc$. This is the same $g = 2$ found in §B.6, obtained here without any FW truncation.

---

## B.11 — Where the FW Series Fails

The FW Hamiltonian of §B.4.3 is a truncated asymptotic expansion. Each item below names the condition under which the truncation, or the expansion itself, breaks down.

1. **Speed.** The expansion parameter is $v/c$, which is $Z\alpha$ for bound states. The truncation error is of relative order $(Z\alpha)^2$ beyond the retained terms. It is negligible for light atoms, about 2% of the $1s$ binding energy at $Z = 82$ (§B.9), and the expansion is useless as $Z\alpha \to 1$. Use the exact Dirac equation, or Dirac–Fock and Dirac–Coulomb–Breit methods for many-electron atoms.
2. **Field strength.** The generated odd term $i\hbar qc\,\boldsymbol\alpha\cdot\mathbf E/2mc^2$ must be small compared with $mc^2$. This requires $\lvert\mathbf E\rvert \ll E_S = m^2c^3/(e\hbar) \approx 1.3\times10^{18}$ V/m (SI), the Schwinger field. Similarly, $\hbar\lvert q\rvert B/mc \ll mc^2$ requires $B \ll m^2c^2/(e\hbar) \approx 4.4\times10^9$ T (SI).
3. **Field variation.** Potentials must not change by $\gtrsim 2mc^2$ over a reduced Compton wavelength $\hbar/mc = 3.86\times10^{-13}$ m. Otherwise the upper and lower blocks cannot be separated perturbatively: this is the Klein-paradox regime.
4. **Frequency.** Time-dependent fields must have $\hbar\omega \ll mc^2$. The $\dot{\mathcal O}$ terms were expanded on this assumption.
5. **Pair creation.** When any of conditions 2–4 fails, electron–positron pairs can be created, the number of particles is not conserved, and no single-particle Hamiltonian is correct. QED is required (Ch. 3 §3.1.2, §3.8).
6. **Singular potentials.** For a point Coulomb potential, successive FW orders produce increasingly singular operators at $r = 0$. The Darwin $\delta$-function is the first. At order $(Z\alpha)^6$, naive term-by-term expectation values for $s$ states are not finite, and the expansion must be reorganized, for example by regularizing with a finite nucleus. The $\alpha^4$ results of §B.8 are unaffected.
7. **Picture change.** The FW transformation also changes the operators. Position, spin and contact densities in the FW basis differ from the Dirac ones at order $(v/c)^2$. Computing a property with a Dirac-basis operator and FW-basis states (or the reverse) introduces a "picture-change" error of the same order as the effects being computed.
8. **Closed forms are rare.** Exact FW transformations are known for the free particle (§B.4.4) and for a pure magnetic field (Case, 1954), where the result is $\beta\sqrt{m^2c^4 + c^2(\boldsymbol\sigma\cdot\boldsymbol\pi)^2}$. For combined electric and magnetic fields only the series exists.

---

## B.12 — Summary

| Result | Statement | Assumptions | Used in |
|---|---|---|---|
| Dirac Hamiltonian | $H_D = c\boldsymbol\alpha\cdot\boldsymbol\pi + \beta mc^2 + q\Phi$, $\boldsymbol\pi = \mathbf p - q\mathbf A/c$ | minimal coupling; external classical field | Ch. 3 §3.2–3.3; Ex. 01 Step 1 |
| Clifford algebra | $\{\alpha_i,\alpha_j\} = 2\delta_{ij}$, $\{\alpha_i,\beta\} = 0$, $\beta^2 = 1$; $\{\gamma^\mu,\gamma^\nu\} = 2\eta^{\mu\nu}_{(+---)}$ | first-order $H$ squaring to $c^2p^2 + m^2c^4$ | Ch. 0 §0.5; Ch. 3 §3.3.1 |
| Spin identity | $(\boldsymbol\sigma\cdot\boldsymbol\pi)^2 = \boldsymbol\pi^2 - (q\hbar/c)\boldsymbol\sigma\cdot\mathbf B$ | exact | Ch. 3 §3.4.2, §3.6 |
| Odd operator | $\mathcal O = c\boldsymbol\alpha\cdot\boldsymbol\pi$ only; $\mathbf E$ enters via $[\mathcal O,\mathcal E] + i\hbar\dot{\mathcal O} = i\hbar qc\,\boldsymbol\alpha\cdot\mathbf E$ | minimal coupling | Ch. 3 §3.5.1; Ex. 01 Step 2 |
| General FW | $\beta(mc^2 + \mathcal O^2/2mc^2 - \mathcal O^4/8m^3c^6) + \mathcal E - [\mathcal O,[\mathcal O,\mathcal E] + i\hbar\dot{\mathcal O}]/8m^2c^4$ | truncated at $mc^2(v/c)^4$; §B.11 conditions | Ch. 3 §3.5.2–3.5.3 |
| FW Hamiltonian (EM) | Zeeman, $-\boldsymbol\pi^4/8m^3c^2$, spin–orbit, Darwin (§B.5) | as above; static fields for the simple SO form | Ch. 3 §3.5.3; Ex. 01 Step 3 |
| Pauli Hamiltonian | $(\boldsymbol\sigma\cdot\boldsymbol\pi)^2/2m + q\Phi$; $\boldsymbol\mu = (q/2mc)(\mathbf L + 2\mathbf S)$ | drop $(v/c)^2$ terms | Ch. 3 §3.6; Ch. 5 §5.6; Ex. 01 Steps 4–5 |
| $g = 2$ | $g_S = 2$, $g_L = 1$ (FW and Gordon) | minimal coupling; no Pauli term; no QED | Ch. 3 §3.4.2; Ch. 5 §5.6 |
| Spin–orbit | $\frac{1}{2m^2c^2}\frac1r\frac{dV}{dr}\mathbf L\cdot\mathbf S$; Thomas factor automatic | static central $V$ | Ch. 5 §5.5 |
| Darwin | $\frac{\hbar^2}{8m^2c^2}\nabla^2V$; Coulomb: $\frac{\pi\hbar^2Ze^2}{2m^2c^2}\delta^3(\mathbf r)$ | static $V$ | Ch. 3 §3.5.3 |
| Fine structure | $\Delta E_{nj} = -\frac{mc^2(Z\alpha)^4}{2n^4}\left(\frac{n}{j+\frac12} - \frac34\right)$ | (H1)–(H4); first-order PT | Ch. 3 §3.4.4; Ch. 5 §5.5.4 |
| Exact Dirac–Coulomb | $E = mc^2[1 + (Z\alpha)^2/(n_r + \sqrt{\kappa^2 - (Z\alpha)^2})^2]^{-1/2}$ | point nucleus; $Z\alpha < \lvert\kappa\rvert$ | Ch. 3 §3.4.4 |
| Expansion check | exact energy $= mc^2[1 - (Z\alpha)^2/2n^2 + \text{FW } \alpha^4 \text{ term} + \mathcal O((Z\alpha)^6)]$ | $Z\alpha \ll 1$ | Ch. 3 §3.4.4, §3.5.3 |
| Gordon decomposition | $J^\mu$ = convective + $\frac{q}{2m}\partial_\nu(\bar\psi\sigma^{\mu\nu}\psi)$ | on-shell Dirac fields | Ch. 3 §3.4.2, §3.9.2 |
| FW failure | $Z\alpha \to 1$; $E \gtrsim E_S$; $B \gtrsim 4.4\times10^9$ T; $\Delta V \gtrsim 2mc^2$ over $\hbar/mc$; $\hbar\omega \gtrsim mc^2$ | — | Ch. 3 §3.5.3 and §3.8 Ledgers |

---

**References** (standard texts; no claim depends on a single page): Foldy, L.L. & Wouthuysen, S.A., *Phys. Rev.* 78, 29 (1950) [R9]; Dirac, *Proc. R. Soc. A* 117, 610 (1928) [R7]; Bjorken & Drell, *Relativistic Quantum Mechanics* (1964); Sakurai, *Advanced Quantum Mechanics* (1967); Berestetskii, Lifshitz & Pitaevskii, *Quantum Electrodynamics* (Landau–Lifshitz Vol. 4); Bethe & Salpeter, *Quantum Mechanics of One- and Two-Electron Atoms* (1957); Thaller, *The Dirac Equation* (Springer, 1992); Jackson, *Classical Electrodynamics*, 3rd ed. (Thomas precession); Lévy-Leblond, *Commun. Math. Phys.* 6, 286 (1967); Case, *Phys. Rev.* 95, 1323 (1954); Schwinger, *Phys. Rev.* 73, 416 (1948).

End of Appendix B
