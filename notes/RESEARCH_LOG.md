# Research Log

This file is append-only in spirit. Correct earlier entries by adding a later correction rather than silently erasing important failed reasoning.

---

## 2026-08-19 — Project initialization

### Question

Can there be a universal, material-independent physical bound on the rate at which a finite-temperature photodetector extracts information from an optical field, expressed in terms of thermodynamic, kinetic, optical, and quantum resources?

### Initial hypothesis

A detector may be represented in the stationary linear regime by

\[
Y(\omega)=\chi_{YP}(\omega)P(\omega)+N(\omega),
\]

with input-referred response-to-noise kernel

\[
K(\omega)=\frac{|\chi_{YP}(\omega)|^2}{S_Y(\omega)}
=\frac{1}{\mathrm{NEP}^2(\omega)}.
\]

For parameterized optical signals, Fisher-information rate is a candidate way to quantify useful sensitivity across bandwidth.

### Immediate caveat discovered

The raw Fisher-information-rate expression is not yet suitable for a universal theorem because it depends on the normalization/units of the optical parameter and can mix source resources with detector resources.

**Status:** VERIFIED conceptual issue.

### Consequence

The first task is not to guess a sensitivity-bandwidth-temperature product. It is to construct an invariant, normalized detector performance functional.

### Candidate resource set

Initial variables under consideration:

\[
T,\quad
\hbar\omega_{\rm opt},\quad
\Phi_\gamma,\quad
\dot\Sigma,\quad
\mathcal A,\quad
\eta_{\rm abs},\quad
N_{\rm ch},\quad
\text{bias/free-energy rate},\ldots
\]

No claim is made that this set is sufficient or minimal.

### First solvable model class

Finite-state continuous-time Markov jump photodetectors with local detailed balance, explicit optical transition bookkeeping, stationary dark state, causal response, finite entropy production, finite activity, and an explicit output current/counting record.

**Status:** DECISION.

### Literature warning from initial audit

The broad territory is already occupied by several important lines of work:

- Young, Sarovar, Léonard (2018): fully quantum photodetector frameworks and coherence/backaction performance tradeoffs;
- Hasegawa (2020/2021): quantum thermodynamic uncertainty relations for continuous measurement/general open systems;
- Schwarzhans et al. (2025): detector quality versus nonequilibrium thermodynamic resources;
- Liu and Gu (2026): response kinetic uncertainty relation for monitored Markovian open quantum systems;
- Blasi et al. (2026): quantum KURs/generalized activity at strong coupling;
- Vu, Honma, Saito (2026): general open-quantum-system precision limits.

**Status:** VERIFIED existence/relevance at abstract level. Full theorem-level comparison remains OPEN.

### Refined novelty hypothesis

The plausible gap is not “detectors have fundamental tradeoffs.” The target is instead:

> a photodetection-specific, architecture-independent bound on normalized optical information acquisition in detector-native response/noise variables with explicit optical and thermokinetic resource accounting, or a rigorous proof that no finite bound exists for a proposed resource set.

**Status:** CONJECTURE / novelty hypothesis only.

### Key adversarial insight

Entropy production alone is not assumed to be sufficient. High-activity/low-affinity processes, detector replication, hidden resources, and source-resource leakage are immediate counterexample directions.

**Status:** OPEN until explicit models are calculated.

### Next mathematical action

Derive and independently verify exact expressions for:

1. \(\chi_{IP}(\omega)\) for an arbitrary finite-state Markov jump detector;
2. \(S_I(\omega)\) for an arbitrary counted transition current;
3. \(\dot\Sigma\) and \(\mathcal A\) in the same edge notation;
4. the complete two-state example as a unit test.

Then test whether existing response/KUR/TUR inequalities can bound \(K(\omega)\) or an invariant normalized integral of it.

**Status:** OPEN — immediate next work.

---

## 2026-08-19 — WP0/WP1 Round 1

### WP0 normalization result

The raw Fisher-information rate is replaced by the information-transfer efficiency

\[
\eta_{\mathcal I}=\frac{\dot F_{\rm out}}{\dot F_{\rm in}^{Q}}.
\]

This ratio is dimensionless, invariant under reparameterization of the encoded optical parameter, invariant under deterministic invertible output transformations when the complete record is retained, and automatically accounts for source information resources.

For coherent/Poisson weak fractional photon-flux modulation,

\[
\eta_{\mathcal I}(\omega)=\Phi_0\frac{|\chi_{Y\Phi}(\omega)|^2}{S_Y(\omega)}=\Phi_0K_\Phi(\omega).
\]

This is the temporal analogue of detective quantum efficiency (DQE). Therefore the normalization is useful but **not itself novel**.

**Status:** VERIFIED/DERIVED for the coherent-Poisson linear regime; general quantum definition follows the QFI/data-processing hierarchy.

### Candidate broadband objective

Define

\[
B_{\mathcal I}=\int_{-\infty}^{\infty}\frac{d\omega}{2\pi}\eta_{\mathcal I}(\omega).
\]

This has units of inverse time and measures information-equivalent bandwidth. A nontrivial UPRP theorem would need to constrain this quantity, or a related task-normalized functional, using detector resources.

**Status:** DEFINITION / OPEN theorem target.

### WP1 exact Markov formulas

For a stationary finite-state jump process, jump-current operator \(\mathcal J^{(1)}\), shot operator \(\mathcal J^{(2)}\), stationary state \(\pi\), and reduced resolvent

\[
R(\omega)=Q(i\omega I-W)^{-1}Q,
\]

the exact two-sided jump-current PSD is

\[
S_I(\omega)=\mathbf 1^T\mathcal J^{(2)}\pi+2\operatorname{Re}[\mathbf 1^T\mathcal J^{(1)}R(\omega)\mathcal J^{(1)}\pi].
\]

For a weak input \(u\) perturbing \(W\) and possibly the counted edges,

\[
\chi_{Iu}(\omega)=\mathbf 1^T\mathcal J_u^{(1)}\pi+\mathbf 1^T\mathcal J_0^{(1)}R(\omega)W_u\pi.
\]

**Status:** PROVED within the finite-state stationary Markov jump model; checked on a solvable two-state detector.

### Two-state unit test

For excitation \(a\), readout/reset \(b\), counting the \(1\to0\) jump, and \(a=a_0+\kappa u\):

\[
\bar I=\frac{ab}{a+b},
\]

\[
\chi_{Iu}(\omega)=\frac{\kappa b^2}{(a+b)(a+b+i\omega)},
\]

\[
S_I(\omega)=\frac{ab}{a+b}\frac{a^2+b^2+\omega^2}{(a+b)^2+\omega^2},
\]

\[
K_u(\omega)=\frac{\kappa^2b^3}{a(a+b)(a^2+b^2+\omega^2)}.
\]

With \(a=\alpha\Phi_0\), \(\kappa=\alpha\),

\[
\eta_{\mathcal I}(\omega)=\frac{\alpha b^3}{(a+b)(a^2+b^2+\omega^2)},
\]

and

\[
B_{\mathcal I}=\frac{\alpha b^3}{2(a+b)\sqrt{a^2+b^2}}.
\]

The zero-frequency Fano factor reduces to \((a^2+b^2)/(a+b)^2\), and the high-frequency PSD tends to the mean point-process rate, independently validating the PSD convention.

**Status:** VERIFIED exact unit test.

### First counterexample direction

The idealized two-state model has total stationary activity

\[
\mathcal A=\frac{2ab}{a+b}.
\]

For fixed \(a\) and \(b\to\infty\), \(\mathcal A\to2a\) while \(B_{\mathcal I}\sim\alpha b/2\to\infty\). Therefore stationary activity alone cannot bound broadband information transfer in the unconstrained kinetic model.

However, the directed-channel model is not yet an admissible finite-temperature/finite-entropy counterexample; enforcing local detailed balance may force either reverse dark traffic or affinity/dissipation to grow with \(b\).

**Status:** COUNTEREXAMPLE to activity-only broadband bound in unconstrained kinetic class; OPEN for full admissible class.

### Critical novelty correction

Two close 2026 works materially narrow the project:

- Andreas Dechant, *Finite-Frequency Fluctuation-Response Inequality*, PRL 136, 207101 (2026), DOI `10.1103/3hs9-dz3d`: general finite-frequency response/noise inequality for Markovian dynamics including jump processes, plus broadband SNR consequences.
- Jie Gu and Kangqiao Liu, *Finite-frequency fluctuation-response bounds for open quantum systems*, arXiv:2605.03340 (2026): measured finite-frequency response precision is bounded by output-field QFI, which is in turn bounded by signal-channel activity for specified dissipative modulation.

Thus generic `response/noise <= activity` and generic finite-frequency response/noise bounds are **not novel targets**.

The surviving target is narrower: explicit **incoming optical field -> finite-temperature transducer -> electrical record** information transfer, with detector-native performance and thermodynamic/kinetic resources, or a rigorous missing-resource counterexample.

**Status:** VERIFIED novelty constraint.

### Next action

Build the smallest reversible two-reservoir (or three-state if necessary) photodetector cycle satisfying local detailed balance with finite reverse rates. Derive exact \(\eta_{\mathcal I}(\omega)\), \(B_{\mathcal I}\), dark counts, activity, entropy production, and spectral gap. Search asymptotic families for bounded \(\{\dot\Sigma,\mathcal A,\Phi_0,\eta(0)\}\) with divergent \(B_{\mathcal I}\).

**Status:** OPEN — immediate next derivation.

---

## 2026-08-19 — WP2 reversible two-channel result

### Minimal reversible two-state detector

Introduced two distinct reversible channels between states 0 and 1: optical rates \(u,d\) and electrical/readout rates \(r,s\). Exact formulas for response, forward-count PSD, information efficiency, activity, cycle current, and EPR were derived in `notes/WP2_REVERSIBLE_TWO_CHANNEL.md`.

### Fast-reset lemma

For fixed \(u,d>0\), if \(r\to\infty\) then one cannot keep both total stationary activity and entropy-production rate bounded for arbitrary \(s(r)>0\).

If \(s\) stays bounded, activity stays bounded but the cycle affinity grows as \(\ln r\) and EPR diverges. If \(s\to\infty\), bidirectional traffic/activity diverges.

**Status:** PROVED for the two-state/two-channel reversible model.

### Important obstruction

In the bounded-\(s\) branch, \(B_{\mathcal I}\propto r\) while \(\sigma\propto\ln r\). Therefore no simple linear bound \(B_{\mathcal I}\le C_1\mathcal A+C_2\sigma\) can be universal even in this minimal family.

**Status:** VERIFIED asymptotic obstruction.

---

## 2026-08-19 — WP2 three-state rare-fast counterexample

### Construction

Built a reversible unicyclic three-state model with rates

\[
0\xrightleftharpoons[cR]{u}1,
\qquad
1\xrightleftharpoons[q]{R}2,
\qquad
2\xrightleftharpoons[s]{b}0,
\]

counting the forward \(1\to2\) jump. The signal perturbs \(u\). All rates are positive.

The stationary intermediate occupation scales as \(\pi_1\sim R^{-1}\), while the counted forward rate is \(R\), leaving a finite mean output current.

### Bounded activity and bounded EPR

The total stationary activity has a finite \(R\to\infty\) limit because the fast rates act on the rare state.

The cycle affinity is

\[
\mathcal F=\ln\frac{ub}{cqs},
\]

independent of \(R\). The cycle current also tends to a finite constant, so the net EPR is bounded.

### Divergent information bandwidth

At scaled frequency \(\omega=Rx\), fixed \(x\neq0\), the count response tends to

\[
\chi_{I\Phi}(Rx)
\to
\frac{\alpha\pi_{0,\infty}}{c+1+ix},
\]

while the count PSD tends to its finite shot-noise level \(I_\infty\). Therefore the coherent-input information efficiency has a strictly positive scaled-frequency limit,

\[
\eta_{\mathcal I}(Rx)
\to
\frac{\alpha u\pi_{0,\infty}^2}
{I_\infty[(c+1)^2+x^2]}.
\]

Any fixed interval in scaled frequency therefore contributes \(O(R)\) to \(B_{\mathcal I}\), proving

\[
\boxed{B_{\mathcal I}\to\infty\ \text{at least linearly in }R}
\]

while \(\mathcal A\) and \(\sigma\) remain bounded.

**Status:** COUNTEREXAMPLE / PROVED for the abstract reversible Markov class.

### Numerical verification

For \(u=0.2,b=0.7,q=0.3,s=0.1,c=2,\alpha=0.5\),

\[
\mathcal A_\infty=0.625,
\qquad
\sigma_\infty=0.02118245\ldots,
\]

while the predicted asymptotic bandwidth coefficient is

\[
\lim_{R\to\infty}B_{\mathcal I}/R=0.1650815217\ldots.
\]

Exact numerical integration gives \(B_{\mathcal I}/R=0.1650629350\) at \(R=1000\), relative error approximately \(1.13\times10^{-4}\).

**Status:** VERIFIED numerical support for the asymptotic coefficient; linear divergence is analytically proved.

### Missing resource identified

The cycle affinity stays finite only because individual rate-ratio affinities diverge with opposite signs:

\[
\ln[u/(cR)]\sim-\ln R,
\qquad
\ln(R/q)\sim+\ln R.
\]

Hence net EPR is too coarse to see the growing microscopic energetic/kinetic scale. A universal photodetection bound likely needs an edge-resolved energetic force, kinetic-prefactor/coupling scale, generator-capacity norm, or microscopic optical/material sum-rule resource.

### Physical caveat

The signal-facing reverse rate \(cR\) grows while the forward optical baseline \(u\) is fixed. A literal fixed-frequency optical absorption/emission reservoir may forbid this scaling through Einstein/detailed-balance relations. Thus this is not yet a counterexample for a fully microscopic fixed-\(\hbar\omega\) photodetector.

**Status:** OPEN physical embedding.

### Literature distinction clarified

Zheng and Lu, arXiv:2602.18631 (2026), derive finite-frequency kinetic and thermodynamic response bounds for barrier/entropic perturbations. Dechant's 2026 FRI and related work place pointwise ceilings on response precision. These results do not automatically bound the present \(B_{\mathcal I}=\int d\omega\,|\chi|^2/S(\omega)\), because their frequency-integrated inequalities use squared response normalized by a time-domain variance rather than the frequency-resolved noise PSD in the denominator.

This distinction must be checked theorem-by-theorem; no novelty should be claimed from notation alone.

### Immediate next action

Construct a stronger counterexample or theorem under a fixed optical reservoir:

- fix \(\hbar\omega_{\rm opt}\), optical occupation/flux, and the absorption/emission rate relation;
- retain finite temperature and all reverse rates;
- vary only internal detector kinetics;
- ask whether \(B_{\mathcal I}\) can still diverge with bounded activity, EPR, and edge-level thermodynamic forces.

This is now the highest-priority gate.
