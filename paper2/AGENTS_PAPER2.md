# AGENTS — Paper 2 General-Channel Program

## Scope

This file is the durable handoff for the **second paper** in The Universal Photodetection Resource Problem repository.

Paper 1 / Rev11 is scientifically frozen by default. Do not alter it while working on Paper 2 unless a concrete Paper-1 defect is identified.

Research remains analytical/theoretical. Numerical work may validate derivations or analyze published data. Do not make new experiments, fabrication, procurement, or laboratory campaigns required next steps.

## Read first

1. `paper2/README.md`
2. `paper2/notes/WP02_STATIONARY_POISSON_SPECTRAL_THEOREM.md`
3. `paper2/notes/WP03_PRIOR_ART_AND_NOVELTY_AUDIT.md`
4. `paper2/notes/WP05_PARALYZABLE_ONEBIN_EXACT_SPECTRUM.md`
5. `paper2/notes/WP01_GENERAL_FISHER_CHANNEL_OPERATOR.md`
6. `paper2/notes/WP04_NONPARALYZABLE_DEAD_TIME_EXACT_EXAMPLE.md`
7. `paper2/notes/RESEARCH_LOG_ROUND01.md`

## Central candidate theorem

For weak deterministic intensity perturbations of a stationary Poisson optical input at baseline flux `Phi0`, any parameter-independent **autonomous stochastic detector channel** should induce a positive contraction on the temporal source tangent space. Because that source tangent is scalar `L^2(R)` and autonomy makes the operator commute with translations, the operator is a Fourier multiplier:

`0 <= G_Phi0(omega) <= 1` a.e.

and

`F_out[u,v] = Phi0/(2*pi) int G_Phi0(omega) U*(omega)V(omega) d omega`.

The detector may have dead time, saturation, recovery, afterpulsing, hidden-state memory, state-dependent capture, multiple registrations, and arbitrary high-flux history dependence. No independent-event delay kernel is assumed.

Candidate conceptual message:

> **Spectral completeness is symmetry-driven, not independent-event-driven.**

This is not yet certified novel. The statistical and harmonic-analysis ingredients are standard; novelty must lie in the photodetection specialization, full theorem combination, exact consequences, and recovery of Paper 1.

## General Fisher-channel operator

For source score space `S` and detector channel `K`,

`T_K s = E[s(X)|Y]`

and

`M_K = T_K^dagger T_K`, with `0 <= M_K <= I`.

For any finite tangent family,

`[F_out]_{ab} = <S_a, M_K S_b>`.

Universal local Fisher dominance is exactly operator order on the source score space. This is **not generic Blackwell dominance**.

A coarse-grained accessible record cannot increase `M_K`.

## Close prior art — mandatory novelty boundary

Do not claim novelty for:

- output score = conditional expectation of input score;
- Fisher monotonicity under Markov processing;
- conditional expectation as an `L^2` contraction;
- translation-invariant bounded `L^2` operators being Fourier multipliers;
- dead-time Fisher-information analysis in general;
- nonparalyzable live-time / activation-fraction FI penalties.

Especially important:

Frederic J. N. Jorgensen and Steven G. Johnson, arXiv:2605.23210 (2026), develop LAN and FI rates for discrete periodic **nonparalyzable** dead-time event detection with arbitrary causal gating. Their result is close to WP04's flat live-fraction example. They explicitly leave paralyzable/Type-II dead time for future work.

## WP04 validation example — nonparalyzable

Ideal deterministic nonparalyzable dead time `tau_d`, complete timestamps:

`G_lambda0(omega) = 1/(1 + lambda0*tau_d)` for every frequency.

Interpretation: predictable dead time removes exposure but does not make a Fisher low-pass. Treat this as a continuous-time validation/corollary, not the central novelty claim.

## WP05 exact hidden-state result — high priority

Discrete one-bin paralyzable detector:

`X_n ~ Bernoulli(p_n)` independently,

`Y_n = X_n(1-X_{n-1})`.

At the symmetric operating point `p=1/2`, the complete output Fisher spectrum obeys

`G(0)=0`

but

`G(pi) = 3/4 + ln(3)/16 = 0.818663268...`.

Thus a detector can be locally **completely blind to DC intensity changes while retaining >81% of incident FI in the fastest alternating temporal mode**.

This is a genuine hidden-state/high-flux effect. The detector's output law is locally symmetric under `p <-> 1-p` for uniform perturbations, causing DC nonidentifiability, while alternating perturbations break that symmetry.

Repository reproduction:

- `paper2/numerics/paralyzable_onebin_spectrum.py`
- `paper2/numerics/paralyzable_onebin_spectrum_p_half.csv`

Do not claim priority until the dedicated Type-II prior-art search is deeper.

## Next decisive research gates

1. **Continuous-time paralyzable detector:** derive `G_lambda0(omega)` or rigorous endpoint/bound results when hidden arrivals restart a deterministic dead interval.
2. **Full one-bin spectrum:** simplify/prove properties of `G_{1/2}(omega)`; numerics indicate a monotone high-pass curve from 0 to `0.818663...` on `[0,pi]`, but monotonicity is not yet proved.
3. **d-bin Type-II generalization:** look for exact spectral zeros/passbands and scaling with dead-time length.
4. **Theorem-grade regularity:** close DQM, whole-line/increasing-window, covariance, real/even multiplier, and Paper-1 recovery proofs.
5. **Novelty audit:** search stationary statistical experiments, HMM waveform FI, system identification, spike-train Fisher kernels, and continuous measurement theory.
6. **Only after these gates:** decide whether a Paper-2 manuscript is warranted. Do not draft a grandiose paper around standard ingredients.

## Breakthrough criterion

Paper 2 should proceed to a manuscript only if at least one of the following survives hostile review:

- the arbitrary-autonomous-channel Fisher-spectrum theorem is genuinely new in photodetection/information theory;
- the hidden-state Type-II results yield a new exact information-spectral phenomenon with substantial scope;
- a new universal resource bound emerges for the general channel class;
- an exact architecture-optimization or side-information tradeoff theorem emerges that goes beyond Paper 1.

The goal is not another incremental extension. If novelty collapses under prior art, record that result and pivot.
