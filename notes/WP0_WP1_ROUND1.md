# WP0/WP1 Round 1 — Invariant Information Efficiency and Exact Markov Response/Noise

**Date:** 2026-08-19

## Status summary

- **WP0 normalization:** substantial progress. A coordinate-invariant information-transfer efficiency is identified. In the coherent/Poisson weak-modulation limit it reduces to a temporal detective-quantum-efficiency (DQE) quantity.
- **WP1 Markov response/noise:** exact formulas for jump-current susceptibility and finite-frequency PSD are derived below and validated on a two-state model.
- **Novelty warning:** finite-frequency fluctuation-response bounds themselves are already occupied by Dechant (PRL 2026) and by Gu & Liu (arXiv:2605.03340) in the open-quantum input-output setting. The project must target a narrower photodetection-specific resource theorem or counterexample.

---

# 1. WP0: invariant information-transfer efficiency

## 1.1 Why raw Fisher-information rate is not the right universal left-hand side

A raw Fisher information \(F_\theta\) changes under reparameterization \(\theta\mapsto f(\theta)\). A raw response-to-noise kernel

\[
K_u(\omega)=\frac{|\chi_{Yu}(\omega)|^2}{S_Y(\omega)}
\]

also changes when the input coordinate \(u\) is rescaled. Therefore neither is by itself a coordinate-free detector quality measure.

The natural fix is to normalize the output information by the information physically available in the incident optical field under the same parameterization.

## 1.2 Definition

For observation time \(T\), let \(F_Y^{(T)}(\theta)\) be the classical Fisher information in the complete measured detector record \(Y_{[0,T]}\), and let \(F_{\rm in}^{Q,(T)}(\theta)\) be the quantum Fisher information of the incident optical field family \(\rho_{\rm in}^{(T)}(\theta)\).

Define

\[
\boxed{
\eta_{\mathcal I}^{(T)}(\theta)
=\frac{F_Y^{(T)}(\theta)}{F_{\rm in}^{Q,(T)}(\theta)}
}
\]

whenever the denominator is nonzero. In a stationary asymptotic regime,

\[
\boxed{
\eta_{\mathcal I}(\theta)
=\frac{\dot F_Y(\theta)}{\dot F_{\rm in}^{Q}(\theta)}.
}
\]

For a physical detector viewed as a quantum channel followed by a measurement, data processing / the quantum Cramer-Rao hierarchy gives

\[
0\le \eta_{\mathcal I}\le 1.
\]

This ceiling is not the sought UPRP theorem; it is the normalization ceiling.

## 1.3 Invariance properties

This ratio passes the immediate invariance tests:

1. **Parameter redefinition.** Under \(\vartheta=f(\theta)\), both numerator and denominator acquire the same Jacobian factor \((d\theta/d\vartheta)^2\), so the ratio is invariant.
2. **Deterministic invertible output gain or reparameterization.** Full classical Fisher information is invariant under an invertible transformation of the observed record, hence so is \(\eta_{\mathcal I}\).
3. **Source-resource accounting.** Increasing incident photon number increases the denominator as well as the potentially available output information; unlimited source power cannot create an apparent detector improvement merely by changing normalization.
4. **Parallel replication.** If detector copies are supplied with proportionally more independent optical resources, numerator and denominator are both extensive. If a fixed incident field is merely split among copies, data processing prevents information creation.

These properties make \(\eta_{\mathcal I}\) a stronger starting point than raw \(\dot F\).

---

# 2. Coherent/Poisson specialization and relation to DQE

Let the incident photon flux be weakly fractionally modulated,

\[
\Phi(t)=\Phi_0\big[1+\epsilon s(t)\big],
\qquad |\epsilon|\ll 1,
\]

where \(\epsilon\) is dimensionless and \(s(t)\) is a specified unit-normalized temporal mode or sinusoid.

For a linear detector output,

\[
\delta\langle Y(\omega)\rangle
=\chi_{Y\Phi}(\omega)\,\delta\Phi(\omega),
\]

with two-sided output PSD \(S_Y(\omega)\).

For a coherent incident field, direct photon-number fluctuations are Poissonian. For the same temporal modulation mode, the input quantum Fisher information rate is proportional to the incident photon flux, while the output Fisher information rate in the linear Gaussian/matched-filter limit is proportional to

\[
\Phi_0^2\frac{|\chi_{Y\Phi}(\omega)|^2}{S_Y(\omega)}.
\]

The temporal-mode normalization factor cancels in the ratio, giving

\[
\boxed{
\eta_{\mathcal I}(\omega)
=\Phi_0\frac{|\chi_{Y\Phi}(\omega)|^2}{S_Y(\omega)}
=\Phi_0 K_\Phi(\omega).
}
\]

Thus the natural dimensionless version of the input-referred kernel is photon flux times \(K_\Phi\).

This is the temporal analogue of **detective quantum efficiency (DQE)**,

\[
\mathrm{DQE}=\frac{\mathrm{SNR}_{\rm out}^2}{\mathrm{SNR}_{\rm in}^2},
\]

widely used in imaging-detector theory. Therefore this normalization is **not a novelty claim**. Its value here is that it supplies a rigorous bridge from NEP/response language to information theory.

## 2.1 Sanity checks

### Ideal photon counter

For an ideal Poisson counter,

\[
\bar I=\Phi_0,\qquad
\chi_{I\Phi}=1,\qquad
S_I=\Phi_0,
\]

so

\[
\eta_{\mathcal I}=1.
\]

### Loss-only detector

For independent quantum efficiency \(\eta_q\),

\[
\bar I=\eta_q\Phi_0,\qquad
\chi_{I\Phi}=\eta_q,\qquad
S_I=\eta_q\Phi_0,
\]

hence

\[
\eta_{\mathcal I}=\eta_q.
\]

### Loss plus Poisson dark counts

With dark-count rate \(d\),

\[
S_I=\eta_q\Phi_0+d,
\]

and therefore

\[
\boxed{
\eta_{\mathcal I}
=\frac{\eta_q^2\Phi_0}{\eta_q\Phi_0+d}
=\frac{\eta_q}{1+d/(\eta_q\Phi_0)}.
}
\]

This correctly penalizes dark noise as well as missed photons.

---

# 3. Candidate broadband objective

The pointwise ceiling \(0\le\eta_{\mathcal I}(\omega)\le1\) is trivial from information data processing. The nontrivial UPRP question should concern how much **frequency range** can maintain high information transfer for bounded detector resources.

Define provisionally

\[
\boxed{
B_{\mathcal I}
=\int_{-\infty}^{\infty}\frac{d\omega}{2\pi}\,\eta_{\mathcal I}(\omega).
}
\]

\(B_{\mathcal I}\) has units of inverse time. It is an information-equivalent bandwidth: a detector with \(\eta_{\mathcal I}=1\) over an ideal rectangular angular-frequency band of width \(2\Omega\) and zero elsewhere has \(B_{\mathcal I}=\Omega/\pi\).

**Status:** DEFINITION / candidate objective. No universal resource bound on \(B_{\mathcal I}\) has been proved.

The sharpened project question is now:

> For a physically admissible finite-temperature photodetector, what thermodynamic/kinetic/optical resources are necessary to support a specified \(\eta_{\mathcal I}(\omega)\) spectrum or \(B_{\mathcal I}\)?

---

# 4. WP1: exact finite-state Markov jump-current formulas

## 4.1 Convention

Use column probabilities,

\[
\dot p=Wp,
\qquad \mathbf 1^T W=0,
\qquad W\pi=0,
\qquad \mathbf 1^T\pi=1.
\]

For \(i\neq j\), \(W_{ij}\) is the rate \(j\to i\).

Use Fourier transform

\[
f(\omega)=\int_{-\infty}^{\infty}dt\,e^{-i\omega t}f(t).
\]

Define

\[
\Pi=\pi\mathbf 1^T,
\qquad Q=I-\Pi,
\]

and the reduced resolvent

\[
\boxed{
R(\omega)=Q(i\omega I-W)^{-1}Q,
}
\]

with its continuous Drazin/group-inverse extension at \(\omega=0\).

## 4.2 Counted jump current

Assign increment \(q_{ij}\) to jump \(j\to i\), and define the point current

\[
I(t)=\sum_{i\neq j}q_{ij}\frac{dN_{ij}}{dt}.
\]

Introduce the tilted generator with unchanged escape-rate diagonal,

\[
W(\chi)_{ij}=W_{ij}e^{i\chi q_{ij}},\quad i\neq j.
\]

Define jump-weighted operators

\[
\mathcal J^{(n)}
=\left.\partial_{(i\chi)}^n W(\chi)\right|_{\chi=0},
\]

so that for \(i\neq j\),

\[
\mathcal J^{(n)}_{ij}=q_{ij}^n W_{ij},
\]

and the diagonal entries vanish for pure jump counting.

The stationary mean current is exactly

\[
\boxed{
\bar I=\mathbf 1^T\mathcal J^{(1)}\pi.
}
\]

## 4.3 Exact finite-frequency PSD

For positive time lag, the connected two-jump correlation is generated by propagation after the first counted jump. Separating the equal-time self-correlation gives

\[
C_I(t>0)
=\mathbf 1^T\mathcal J^{(1)}e^{Wt}Q\mathcal J^{(1)}\pi,
\]

plus the singular term

\[
\mathbf 1^T\mathcal J^{(2)}\pi\,\delta(t).
\]

Fourier transformation yields the two-sided PSD

\[
\boxed{
S_I(\omega)
=\mathbf 1^T\mathcal J^{(2)}\pi
+2\operatorname{Re}\!\left[
\mathbf 1^T\mathcal J^{(1)}R(\omega)\mathcal J^{(1)}\pi
\right].
}
\]

This is the exact jump-current PSD for the stated convention.

**Status:** PROVED within the finite-state stationary Markov jump model; two-state validation below.

## 4.4 Exact susceptibility to a weak input perturbation

Let a scalar input \(u(t)\) perturb both the generator and, potentially, the counted-edge weights/rates:

\[
W(u)=W_0+uW_u+O(u^2),
\]

\[
\mathcal J^{(1)}(u)
=\mathcal J_0^{(1)}+u\mathcal J_u^{(1)}+O(u^2).
\]

The state response is

\[
\delta p(\omega)
=R(\omega)W_u\pi\,\delta u(\omega).
\]

The current has a direct term from immediate rate modulation and an indirect term from changed state occupation. Therefore

\[
\boxed{
\chi_{Iu}(\omega)
=\mathbf 1^T\mathcal J_u^{(1)}\pi
+\mathbf 1^T\mathcal J_0^{(1)}R(\omega)W_u\pi.
}
\]

This is the exact linear susceptibility for a counted Markov jump current.

**Status:** PROVED within the stated model.

---

# 5. Exact two-state unit test

Consider states \(0,1\) with excitation rate \(a\) and relaxation/readout rate \(b\):

\[
W=
\begin{pmatrix}
-a & b\\
a & -b
\end{pmatrix}.
\]

The stationary distribution is

\[
\pi_0=\frac{b}{a+b},
\qquad
\pi_1=\frac{a}{a+b}.
\]

Count only the \(1\to0\) relaxation jump with unit increment. Then

\[
\bar I=\frac{ab}{a+b}.
\]

Let the optical input modulate the excitation rate,

\[
a=a_0+\kappa u(t).
\]

There is no direct modulation of the counted \(1\to0\) edge, so the response is entirely occupation mediated. Exact substitution into the general formula gives

\[
\boxed{
\chi_{Iu}(\omega)
=\frac{\kappa b^2}{(a+b)(a+b+i\omega)}.
}
\]

The exact current PSD is

\[
\boxed{
S_I(\omega)
=\frac{ab}{a+b}
\frac{a^2+b^2+\omega^2}{(a+b)^2+\omega^2}.
}
\]

Therefore

\[
\boxed{
K_u(\omega)
=\frac{|\chi_{Iu}(\omega)|^2}{S_I(\omega)}
=\frac{\kappa^2b^3}
{a(a+b)(a^2+b^2+\omega^2)}.
}
\]

## 5.1 PSD checks

At zero frequency,

\[
\frac{S_I(0)}{\bar I}
=\frac{a^2+b^2}{(a+b)^2},
\]

which is the standard sub-Poisson renewal-process Fano factor for sequential two-step events.

At high frequency,

\[
S_I(\omega\to\infty)\to\bar I,
\]

recovering the point-process self-shot-noise level.

At zero frequency,

\[
\chi_{Iu}(0)
=\kappa\frac{b^2}{(a+b)^2}
=\kappa\frac{\partial}{\partial a}\left(\frac{ab}{a+b}\right),
\]

as required.

These independent limits validate the sign and factor conventions in the general formulas.

---

# 6. Two-state information efficiency

Let excitation be caused by incident photons,

\[
a=\alpha\Phi_0,
\]

where \(0\le\alpha\le1\) is a dimensionless single-absorber coupling/absorption probability in the simple rate model. For perturbations in photon flux, \(\kappa=\alpha\).

Then

\[
\boxed{
\eta_{\mathcal I}(\omega)
=\Phi_0K_\Phi(\omega)
=\frac{\alpha b^3}
{(a+b)(a^2+b^2+\omega^2)}.
}
\]

At low photon flux \(a\ll b\),

\[
\eta_{\mathcal I}(0)\to\alpha,
\]

so the information efficiency reduces to the expected absorption/quantum efficiency.

The information-equivalent bandwidth is

\[
\boxed{
B_{\mathcal I}
=\int_{-\infty}^{\infty}\frac{d\omega}{2\pi}\eta_{\mathcal I}(\omega)
=\frac{\alpha b^3}
{2(a+b)\sqrt{a^2+b^2}}.
}
\]

In the weak-flux, fast-readout limit \(a\ll b\),

\[
B_{\mathcal I}\simeq \frac{\alpha b}{2}.
\]

Thus high information bandwidth requires a fast internal reset/readout rate in this minimal model.

---

# 7. First adversarial result: stationary activity alone does not encode latent reset speed

For the idealized two-state model, the total stationary jump activity is

\[
\mathcal A
=a\pi_0+b\pi_1
=\frac{2ab}{a+b}.
\]

Holding \(a\) fixed while taking \(b\to\infty\),

\[
\mathcal A\to 2a
\]

but

\[
B_{\mathcal I}\sim \frac{\alpha b}{2}\to\infty.
\]

Hence a bound of the form

\[
B_{\mathcal I}\le C\mathcal A
\]

cannot hold for this unconstrained kinetic model.

However, this is **not yet an admissible counterexample to the full UPRP resource set**, because the model treats excitation and reset as ideal directed channels. If they are embedded into finite-temperature reservoirs with local detailed balance and finite entropy production, making \(b\) arbitrarily large while suppressing the reverse dark process may require diverging affinity/dissipation. Conversely, keeping the affinity finite tends to make reverse traffic and therefore activity grow with \(b\).

**Status:** COUNTEREXAMPLE to an activity-only broadband bound in the unconstrained Markov kinetic class; **OPEN** for the finite-temperature, finite-entropy-production admissible class.

This observation identifies a key structural issue: stationary activity counts events that actually occur, but broadband response can depend on very fast rates attached to states that are rarely occupied. A universal bandwidth theorem may therefore require entropy production, a kinetic-capacity/escape-rate variable, a spectral quantity, or a suitable combination rather than stationary activity alone.

---

# 8. Critical 2026 literature overlap

Two results discovered during this round materially narrow the novelty target.

## Dechant, PRL 136, 207101 (2026)

**Finite-Frequency Fluctuation-Response Inequality**, DOI `10.1103/3hs9-dz3d`.

The paper proves a finite-frequency inequality of the schematic form

\[
\mathcal R^\dagger(\omega)\mathcal S^{-1}(\omega)\mathcal R(\omega)
\preceq \mathcal A_{\rm pert}
\]

for broad Markovian dynamics, explicitly including jump processes, and derives a broadband SNR consequence. Therefore a generic claim that response-to-noise admits a universal finite-frequency Markov bound is already occupied.

## Gu & Liu, arXiv:2605.03340 (2026)

**Finite-frequency fluctuation-response bounds for open quantum systems**.

They establish a hierarchy of the form

\[
\text{measured response precision}
\le
\text{output-field QFI rate}
\le
\text{signal-channel activity}
\]

for Markovian open quantum systems in an input-output setting, with the first inequality independent of downstream detection scheme. They explicitly state that their classical counting limit connects to Dechant's finite-frequency FRI.

Consequences for UPRP:

- `response/noise <= activity` is not a novel project endpoint;
- `output FI <= optical/output-field QFI` is not novel;
- the surviving research target must involve the **incoming optical field -> physical detector transduction -> electrical record** with explicit finite-temperature resource accounting, or a no-go/counterexample theorem that identifies which detector resources are indispensable for broadband information transfer.

---

# 9. Revised immediate target

Construct the smallest thermodynamically admissible detector cycle with:

1. an explicit optical absorption channel;
2. an explicit electrical/readout channel;
3. finite reverse rates satisfying local detailed balance;
4. finite temperature and finite entropy production;
5. an electrical counted output;
6. exact \(\eta_{\mathcal I}(\omega)\), \(B_{\mathcal I}\), activity, entropy production, dark-count rate, and spectral gap.

Then take controlled asymptotic limits to answer:

> Can \(B_{\mathcal I}\) diverge while \(\dot\Sigma\), stationary activity, incident photon flux, and detection efficiency remain bounded?

If yes, the proposed resource set is incomplete and the asymptotic family is a publishable counterexample/missing-resource result. If no for the minimal cycle, derive the strongest inequality the cycle satisfies and test it on larger networks.

**Next status:** OPEN — begin reversible two-reservoir model.