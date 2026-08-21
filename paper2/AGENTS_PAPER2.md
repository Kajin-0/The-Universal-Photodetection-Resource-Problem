# AGENTS — Paper 2 General-Channel Program

## Scope

This file is the durable handoff for the **second paper** in The Universal Photodetection Resource Problem repository.

Paper 1 / Rev11 is scientifically frozen by default. Do not alter it while working on Paper 2 unless a concrete Paper-1 defect is identified.

Research remains analytical/theoretical. Numerical work may validate derivations or analyze published data. Do not make new experiments, fabrication, procurement, or laboratory campaigns required next steps.

## Read first

1. `paper2/README.md`
2. `paper2/notes/WP07_CONTINUOUS_PARALYZABLE_SPECTRAL_SURVIVAL.md`
3. `paper2/notes/WP08_VISIBLE_EVENT_HIGH_FREQUENCY_RESIDUE.md`
4. `paper2/notes/WP09_TYPEII_AND_FISHER_OPERATOR_PRIOR_ART_AUDIT.md`
5. `paper2/notes/WP06_CLOSED_FORM_HIGH_PASS_THEOREM.md`
6. `paper2/notes/WP05_PARALYZABLE_ONEBIN_EXACT_SPECTRUM.md`
7. `paper2/notes/WP02_STATIONARY_POISSON_SPECTRAL_THEOREM.md`
8. `paper2/notes/WP03_PRIOR_ART_AND_NOVELTY_AUDIT.md`
9. `paper2/notes/WP01_GENERAL_FISHER_CHANNEL_OPERATOR.md`
10. `paper2/notes/WP04_NONPARALYZABLE_DEAD_TIME_EXACT_EXAMPLE.md`
11. latest `paper2/notes/RESEARCH_LOG_*.md`

## Central candidate theorem

For weak deterministic intensity perturbations of a stationary Poisson optical input at baseline flux `Phi0`, any parameter-independent **autonomous stochastic detector channel** should induce a positive contraction on the temporal source tangent space. Because that source tangent is scalar `L^2(R)` and autonomy makes the operator commute with translations, the operator is a Fourier multiplier:

`0 <= G_Phi0(omega) <= 1` a.e.

and

`F_out[u,v] = Phi0/(2*pi) int G_Phi0(omega) U*(omega)V(omega) d omega`.

The detector may have dead time, saturation, recovery, afterpulsing, hidden-state memory, state-dependent capture, multiple registrations, and arbitrary high-flux history dependence. No independent-event delay kernel is assumed.

Candidate conceptual message:

> **Spectral completeness is symmetry-driven, not independent-event-driven.**

This is not yet certified novel. The statistical and harmonic-analysis ingredients are standard; novelty must lie in the photodetection specialization, exact consequences, recovery of Paper 1, and new high-flux theorems.

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
- function-valued Fisher-information operators for point processes;
- dead-time Fisher-information analysis in general;
- modulated paralyzable photon counting in general;
- count-rate, renewal, mean/variance, or power-spectrum formulas for paralyzable counters;
- nonparalyzable live-time / activation-fraction FI penalties.

Especially important prior art:

- Teich & Vannucci, JOSA 68, 1338 (1978), DOI `10.1364/JOSA.68.001338`: modulated laser photocounting including paralyzable dead time.
- Teich & Cantor, IEEE JQE 14, 993 (1978), DOI `10.1109/JQE.1978.1069731`: likelihood/error/mutual-information/channel-capacity analysis with nonparalyzable dead time.
- Jorgensen & Johnson, arXiv:2605.23210 (2026): LAN/FI rates for discrete periodic **nonparalyzable** dead-time event detection with arbitrary causal gating; paralyzable/Type-II left as future work.
- Clark, Statistics & Probability Letters 236, 110779 (2026), DOI `10.1016/j.spl.2026.110779`: function-valued score/Fisher operators for point processes.

## WP04 validation example — nonparalyzable

Ideal deterministic nonparalyzable dead time `tau_d`, complete timestamps:

`G_lambda0(omega) = 1/(1 + lambda0*tau_d)` for every frequency.

Interpretation: predictable dead time removes exposure but does not make a Fisher low-pass. Treat this as a validation/corollary, not the central novelty claim.

## WP05/WP06 exact hidden-state result — discrete Type II

Discrete one-bin paralyzable detector:

`X_n ~ Bernoulli(p_n)` independently,

`Y_n = X_n(1-X_{n-1})`.

At `p=1/2`, define `x=1-cos(omega)`. The complete output Fisher spectrum is

`G(omega)=1-1/(2x)+ln(1+4x)/(8x^2)`

with continuous extension `G(0)=0`.

It is **strictly increasing** on `0<omega<pi`, with

`G(pi)=3/4+ln(3)/16=0.818663268...`.

Thus a detector can be completely blind to DC intensity changes while retaining >81% of incident FI in the fastest alternating temporal mode.

Repository reproduction:

- `paper2/numerics/paralyzable_onebin_spectrum.py`
- `paper2/numerics/paralyzable_onebin_spectrum_p_half.csv`

## WP07 continuous Type-II theorem — highest-priority current result

Continuous Poisson input, deterministic paralyzable dead time `tau`, operating point `rho=lambda*tau`.

At baseline the recorded timestamps form a renewal process with

`r=lambda*exp(-rho)`

and inter-recording Laplace transform

`psi(s)=r*exp(-s*tau)/(s+r*exp(-s*tau))`.

At the classical paralysis maximum `rho=1`, the **entire homogeneous output renewal law** is locally insensitive to a uniform rate perturbation, hence

`G_1(0)=0`.

For `y=omega*tau`, a single optimally phased Fourier statistic gives the rigorous complete-record lower bound

`G_rho(omega) >= exp(-rho)*|M_rho(y)|^2/[1-2*rho*exp(-rho)*sin(y)/y]`

where

`M_rho(y)=1-rho*(1-exp(-i y))/(i y)`.

At `rho=1`, this lower bound is strictly positive for **every nonzero frequency**. In particular,

`G_1(pi/tau) >= exp(-1)*(1+4/pi^2) = 0.516975...`.

The exact complete-record renewal-score representation further gives

`lim_{|omega|->infty} G_rho(omega)=exp(-rho)`.

Therefore at saturation

`G_1(0)=0` but `G_1(omega)>0` for all `omega != 0`, and `G_1(infty)=1/e`.

This is the strongest current physical high-flux theorem.

Reproduction:

- `paper2/numerics/continuous_paralyzable_spectral_survival.py`

## WP08 visible-event high-frequency residue — provisional general theorem

For an autonomous history-dependent detector that outputs a subset `Y<=N` of incident Poisson events **at their exact incident timestamps**, let `r` be the output rate and `lambda` the input rate.

Under explicit diffuse-posterior and short-memory covariance hypotheses, the complete Fisher spectrum satisfies

`lim_{|omega|->infty} G(omega)=r/lambda`.

Interpretation: the high-frequency FI residue is the fraction of incident timestamps that remain directly visible, regardless of the memoryful selection rule.

This unifies independent exact-timestamp thinning, nonparalyzable dead time, and the continuous paralyzable high-frequency limit.

Treat this as provisional until the random-measure proof and dependent-thinning prior-art search are stronger.

## Current novelty posture

The possible breakthrough is **not** `dead time + Fisher information`.

The strongest defensible research thesis is now:

> An arbitrary autonomous detector channel driven by weak Poisson temporal perturbations possesses a complete local Fisher-retention spectrum; hidden detector memory can create information spectra qualitatively unlike conventional bandwidth response, including exact saturation points with zero DC information but substantial finite/high-frequency information; and exact-timestamp event visibility controls a broad high-frequency residue.

No `first` or priority claim yet.

## Next decisive research gates

1. **Theorem-grade regularity for WP02:** close DQM, increasing-window limits, shift covariance, real/even multiplier, and Paper-1 recovery.
2. **Independent WP07 validation:** implement the Volterra interval-score solver with grid convergence and/or a second renewal calculation.
3. **Continuous Type-II shape:** determine analytic extrema/oscillation properties of `G_1(omega)` beyond the exact endpoints/limit and lower bound.
4. **WP08 proof hardening:** random-measure formulation and minimal mixing assumptions; seek a weaker Cesaro/Wiener version.
5. **Dependent-thinning novelty search:** point-process missing-event inference, neural refractory FI spectra, system identification, and stationary-channel LAN.
6. **Recovery-time generalization:** replace deterministic `tau` by a distribution and identify which spectral-survival/residue statements persist.
7. **Only after these gates:** decide whether to draft Paper 2. Do not write a grandiose manuscript around standard ingredients.

## Breakthrough criterion

Paper 2 should proceed to a manuscript only if at least one survives hostile review:

- the arbitrary-autonomous-channel Fisher-spectrum theorem is genuinely new in photodetection/information theory;
- the hidden-state Type-II results yield a new exact information-spectral phenomenon with substantial scope;
- the visible-event residue becomes a robust general theorem;
- a new universal resource/order theorem emerges beyond Paper 1.

Current status: **the Type-II branch is strong enough to continue aggressively, but not yet enough for priority language.**
