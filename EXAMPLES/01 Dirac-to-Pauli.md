# Example 1 — Dirac → Pauli

**A complete worked descent in six steps.** Follows the shape every example in
this folder uses: theory → approximation → mathematical reduction → reduced
model → engineering equation → validity limits.

**Source chapters:** [Ch. 0](../CHAPTERS/CHAPTER%200.md) (the Lagrangian) →
[Ch. 3](../CHAPTERS/CHAPTER%203.md) §§3.2–3.6 (Dirac, Foldy–Wouthuysen, Pauli)

**Question answered:** Where does the Pauli equation come from, and what was
given up to get it?

---

## Step 1 — Theory

The electron's dynamics start from a Lagrangian density. Keeping only the
U(1)-coupled fermion sector and treating the gauge field classically:

$$\mathcal{L} = \bar\psi\left(i\hbar\gamma^\mu D_\mu - m_ec^2\right)\psi,\qquad D_\mu = \partial_\mu + \frac{ie}{\hbar}A_\mu$$

Vary with respect to $\bar\psi$ and the Euler–Lagrange equation is immediate:

$$i\hbar\gamma^\mu D_\mu\psi - m_ec^2\psi = 0$$

Written with $\gamma^0$ on the left, this is the Dirac equation in Hamiltonian
form. **This step is a derivation** — `[DERIVATION]` — and nothing has been
discarded. Four-component spinor, antiparticles, relativistic dispersion: all
present.

**Status:** exact within the assumed Lagrangian.

---

## Step 2 — Approximation

Two independent things now have to go wrong before a 2×2 equation appears, and
they are often conflated:

| # | Reduction | Kind | Cost |
|---|---|---|---|
| A | Non-relativistic limit, $v/c \ll 1$ | `[APPROXIMATION]` | antiparticle sector suppressed |
| B | Project onto the large component | `[APPROXIMATION]` | $\chi$ discarded; $\alpha^4$ terms either kept or dropped |

Reduction B is subtle. The Dirac spinor has large and small components, and they
are *not* independent — $\chi$ is coupled to $\phi$ by $c\boldsymbol{\sigma}\cdot\hat{\boldsymbol{\pi}}$.
You cannot simply set $\chi=0$. The Foldy–Wouthuysen transformation is what
makes the decoupling legitimate, and it is worth being precise about how it works,
because the usual shorthand attaches the eigenvalues to the wrong operator.

The Dirac Hamiltonian splits by parity:

$$H = \underbrace{\beta m_ec^2 + \mathcal{E}}_{\text{even}} + \underbrace{\mathcal{O}}_{\text{odd}}, \qquad \mathcal{O} = c\boldsymbol{\alpha}\cdot\hat{\boldsymbol{\pi}} - e\boldsymbol{\sigma}\cdot\mathbf{E}$$

The Foldy–Wouthuysen transformation is an **exact** unitary change of basis,
$U^\dagger\mathcal{O}U = 0$. Note what it does *not* do: it does not diagonalise
$\mathcal{O}$. It annihilates it. That is the entire content of the trick — once
the odd operator is gone, what remains is even, and an even operator is block
diagonal in $\beta$.

**The $\pm m_ec^2$ eigenvalues belong to the mass term $\beta m_ec^2$, not to
$\mathcal{O}$.** The odd operator has no such spectrum at all: $\mathcal{O}^2$ is
assembled from $\hat\pi^2$ and the spin–electric terms, and is suppressed by
$\alpha^2$ relative to $m_e^2c^2$. Carrying the positive/negative energy
separation is the job of $\beta m_ec^2$, and the selection rule that follows is a
projection onto a $\beta$ block.

Projecting onto $\beta = +1$ and iterating once on the transformed correction
produces the order-$(v/c)^2$ effective Hamiltonian of step 3.

---

## Step 3 — Mathematical reduction

With the odd terms squared once and dropped:

$$\boxed{\hat H_{FW} = m_ec^2 + \frac{\hat\pi^2}{2m_e} + eV \underbrace{-\frac{e\hbar}{2m_ec}\boldsymbol{\sigma}\cdot\mathbf{B}}_{\text{Zeeman}} \underbrace{-\frac{\hat\pi^4}{8m_e^3c^2}}_{\text{relativistic mass}} \underbrace{-\frac{e\hbar}{4m_e^2c^2}\boldsymbol{\sigma}\cdot(\mathbf{E}\times\hat{\mathbf{p}})}_{\text{spin-orbit}} \underbrace{+\frac{e\hbar^2}{8m_e^2c^2}\nabla\cdot\mathbf{E}}_{\text{Darwin}}}$$

where $\hat{\boldsymbol{\pi}} = \hat{\mathbf{p}} - e\mathbf{A}/c$.

Now truncate *again*, to reach the Pauli equation: drop the three $\alpha^4$
terms and the rest-mass constant, keep the Zeeman term.

---

## Step 4 — Reduced model

$$\boxed{i\hbar\frac{\partial\phi}{\partial t} = \left[\frac{(\hat{\mathbf{p}} - e\mathbf{A}/c)^2}{2m_e} - \frac{e\hbar}{2m_ec}\boldsymbol{\sigma}\cdot\mathbf{B} + eV\right]\phi,\qquad \phi = \begin{pmatrix}\phi_\uparrow\\ \phi_\downarrow\end{pmatrix}}$$

Two components, not four. Spin now lives in a $2\times2$ matrix, so
spin-dependent physics becomes algebra.

**Check that $g=2$ was not put in by hand — from the right place.** The obvious
place to look is the orbital minimal-coupling term, and that is exactly where the
check fails. In the Coulomb gauge ($\nabla\cdot\mathbf{A}=0$):

$$\frac{1}{2m_e}\left(\hat{\mathbf{p}} - \frac{e}{c}\mathbf{A}\right)^2 = \frac{\hat p^2}{2m_e} - \frac{e}{m_ec}\mathbf{A}\cdot\hat{\mathbf{p}} + \frac{e^2}{2m_ec^2}\mathbf{A}^2$$

No $\hat{\mathbf{S}}$ appears anywhere in this — unsurprisingly, because the term
is spin-free by construction. It also retains the diamagnetic $A^2$ piece. So a
derivation that "finds" $g=2$ by expanding this square has smuggled the spin term
into an expression that cannot contain it. (As written it does not even have the
right units: pairing $\hat{\mathbf{S}}$ with $\frac{e}{2m_ec}$ yields a length, not
an energy.)

The spin coupling comes from a *different* piece of the Dirac equation. The
time-derivative half of the interaction, $-\frac{e}{c}\boldsymbol{\alpha}\cdot\mathbf{A}$,
is an **odd** operator, so it belongs to $\mathcal{O}$ and not to the even kinetic
term. Iterating that odd piece once in the Foldy–Wouthuysen reduction generates
*both* magnetic couplings at once:

$$H_{\text{Zeeman}} = \frac{e}{2m_e}\left(\hat{\mathbf{L}} + g_e\,\hat{\mathbf{S}}\right)\cdot\mathbf{B}, \qquad g_e = 2$$

The orbital piece and the spin piece descend from the *same* operator
$\boldsymbol{\alpha}\cdot\mathbf{A}$, and the algebra fixes their ratio at exactly
2. That ratio is the $g_e = 2$ of §3.4.2, and it is the same number as
$-\frac{e\hbar}{2m_ec}\boldsymbol{\sigma}\cdot\mathbf{B}$ in step 3, since
$2\hat{\mathbf{S}} = \hbar\boldsymbol{\sigma}$.

So $g=2$ really does fall out — it was never inserted — but it falls out of the
**odd** sector, and only after the projection onto the large component. The
kinetic term is where a careless derivation goes looking for it and finds a
spurious answer. That is the single best test of whether a descent is real: the
new structure should appear whether or not you were looking for it, *and from the
term that can actually produce it.*

---

## Step 5 — Engineering equation

Expanding in $\hat{\mathbf{L}}$ on a hydrogen-like state, $\hat{\mathbf{L}} \to 0$, leaves
the Zeeman splitting:

$$\Delta E = \mu_B\,g_J\,m_J\,B,\qquad \mu_B = \frac{e\hbar}{2m_ec} = 9.274\times 10^{-24}\ \text{J/T},\qquad g_J = 1 + \frac{J(J+1)+S(S+1)-L(L+1)}{2J(J+1)}$$

Note the structure: the coefficient multiplying $m_JB$ is the **Bohr magneton**, and
the reduction has produced it rather than assumed it. This is the equation
worked through in full — weak field, strong field, Paschen–Back — in
[Ch. 5 §5.6](../CHAPTERS/CHAPTER%205.md), and it is the equation behind every
NMR and MRI system.

**Design consequence.** A permanent magnet of flux density $B$ across a sample
splits spin levels by $2\mu_B B$. The engineering move — choose $B$ to set the
splitting you need — follows from the reduced model, and would not follow from
the Dirac equation without all of steps 1–4.

---

## Step 6 — Validity limits

| Regime | Correct equation |
|---|---|
| $E \gtrsim m_ec^2$ (511 keV) | Dirac; pair creation is available |
| $E \ll m_ec^2$, spin observed | **Pauli** |
| $E \ll m_ec^2$, spin irrelevant | Schrödinger (Ch. 3 §3.7) |
| Binding energies, Lamb shift resolved | Dirac or full FW — Pauli is insufficient |

The criterion is $v \ll c$, not "small". For hydrogen ground state
$v/c = \alpha \approx 1/137$, so the relative kinetic-energy error is
$\alpha^2 \approx 5\times 10^{-5}$. For heavy nuclei and high-$Z$ ions this
stops being small and the Pauli equation is simply wrong.

**What this example demonstrates.** A working 2×2 model with a famously
correct $g=2$ was obtained by discarding the antiparticle sector and three
correction terms. The discarded terms are recoverable — add them back and you
have fine structure. "Valid in a regime" and "true" are different claims, and
the ledger format separates them.

---

**Model Ledger:** see [Ch. 3 §3.5.3 and §3.6](../CHAPTERS/CHAPTER%203.md) for the
full nine-row ledgers with assumptions, neglected physics, and failure modes.
