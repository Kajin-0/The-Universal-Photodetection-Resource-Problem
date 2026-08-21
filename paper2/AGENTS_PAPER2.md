# AGENTS — Paper 2 General-Channel Program

## Scope

Durable handoff for the **second paper** in The Universal Photodetection Resource Problem repository.

Paper 1 / Rev11 is scientifically frozen by default. Do not alter it while working on Paper 2 unless a concrete Paper-1 defect is identified.

Research remains analytical/theoretical. Numerical work may validate derivations or analyze published data. Do not make new experiments, fabrication, procurement, or laboratory campaigns required next steps.

## Read first

1. `paper2/README.md`
2. `paper2/notes/RESEARCH_LOG_ROUND02.md`
3. `paper2/notes/WP10_GENERAL_AUTONOMOUS_CHANNEL_THEOREM_HARDENED.md`
4. `paper2/notes/WP07_CONTINUOUS_PARALYZABLE_SPECTRAL_SURVIVAL.md`
5. `paper2/notes/WP12_RANDOM_RECOVERY_BREAKS_STATIC_FISHER_ZERO.md`
6. `paper2/notes/WP08_VISIBLE_EVENT_HIGH_FREQUENCY_RESIDUE.md`
7. `paper2/notes/WP11_GLOBAL_STATIC_NONIDENTIFIABILITY_PARALYZABLE.md`
8. `paper2/notes/WP09_TYPEII_AND_FISHER_OPERATOR_PRIOR_ART_AUDIT.md`
9. `paper2/notes/WP06_CLOSED_FORM_HIGH_PASS_THEOREM.md`
10. `paper2/notes/WP05_PARALYZABLE_ONEBIN_EXACT_SPECTRUM.md`
11. `paper2/notes/WP03_PRIOR_ART_AND_NOVELTY_AUDIT.md`
12. `paper2/notes/WP01_GENERAL_FISHER_CHANNEL_OPERATOR.md`
13. `paper2/notes/WP04_NONPARALYZABLE_DEAD_TIME_EXACT_EXAMPLE.md`

## Central theorem candidate — now proof-hardened

For a stationary Poisson source of baseline flux `Phi0` and bounded compactly supported local intensity tangent `u`,

`S_u = int u(t)[N(dt)-Phi0 dt]`,

`E[S_u S_v] = Phi0 <u,v>_{L2}`.

For any parameter-independent stochastic detector channel `K`, the Markov-image score is the standard conditional expectation

`S_u^out = E[S_u|Y]`.

This induces a unique positive contraction `A_K` on scalar `L2(R)`:

`F_out[u,v] = Phi0 <u,A_K v>`, `0 <= A_K <= I`.

If `K` is autonomous/time-translation covariant, `A_K` commutes with all translations. Therefore it is a Fourier multiplier:

`F_out[u,v] = Phi0/(2*pi) int G_{Phi0,K}(omega) U*(omega)V(omega) d omega`,

with

`0 <= G_{Phi0,K}(omega) <= 1` a.e., and `G(-omega)=G(omega)` a.e.

The detector may have arbitrary dead time, saturation, recovery, afterpulsing, hidden-state memory, state-dependent capture, multiple output events, analog marks, and high-flux nonlinear history dependence. No independent-event delay kernel is assumed.

Long sinusoidal performance is obtained afterward by narrowband wavepacket limits at Lebesgue points of `G`; pure infinite sinusoids are not primitive admissible tangents.

Paper 1 is recovered exactly as the marked-Poisson special case:

`G(omega)=int |H_m(omega)|^2 kappa(dm)`.

Candidate conceptual message:

> **Spectral completeness is symmetry-driven, not independent-event-driven.**

The conditional-score identity, Fisher monotonicity, function-valued Fisher operators, and translation-invariant multiplier theorem are standard and must not be claimed as new.

## Exact discrete hidden-memory theorem

One-bin Type-II detector:

`Y_n=X_n(1-X_{n-1})`, `X_n~Bernoulli(p_n)`.

At `p=1/2`, let `x=1-cos(omega)`. Complete local Fisher spectrum:

`G(omega)=1-1/(2x)+ln(1+4x)/(8x^2)`, with `G(0)=0`.

It is strictly increasing for `0<omega<pi` and

`G(pi)=3/4+ln(3)/16=0.818663268...`.

This is an exact saturation-induced **information high-pass** theorem.

## Continuous deterministic Type-II theorem — strongest physical result

Poisson rate `lambda`, deterministic paralyzable dead time `tau`, `rho=lambda*tau`.

Recorded timestamps are renewal cluster starts with

`r=lambda exp(-rho)`

and interval Laplace transform

`psi(s)=r exp(-s tau)/[s+r exp(-s tau)]`.

At the classical paralysis maximum `rho=1`, the entire homogeneous output timestamp law is locally insensitive to uniform intensity:

`G_1(0)=0`.

For `y=omega*tau`, the exact first-moment mode response is

`M_rho(y)=1-rho(1-exp(-iy))/(iy)`.

A single optimally phased Fourier statistic gives the rigorous complete-record lower bound

`G_rho(omega) >= exp(-rho)|M_rho(y)|^2/[1-2 rho exp(-rho) sin(y)/y]`.

At `rho=1` this is strictly positive for every `omega != 0`. In particular,

`G_1(pi/tau) >= exp(-1)(1+4/pi^2)=0.516975...`.

The exact renewal-score representation gives

`lim_|omega|->infty G_rho(omega)=exp(-rho)`.

Thus at saturation:

`G_1(0)=0`, `G_1(omega)>0` for all nonzero `omega`, and `G_1(infty)=1/e`.

Independent Volterra solver:

- `paper2/numerics/continuous_paralyzable_volterra_exact.py`
- convergence table and spectrum snapshot in the same directory.

At `omega*tau=pi`, grid refinement extrapolates to about `G~0.52814`, above the analytic lower bound. The exact continuous spectrum rises from zero, peaks near `omega*tau~3.3`, then oscillates toward `1/e`; unlike the discrete model it is not strictly monotone.

## Global static branch aliasing

For deterministic Type II, the **complete stationary timestamp law** depends on `lambda` only through

`r=lambda exp(-lambda tau)`.

Therefore two Lambert-W branches with equal `r` generate identical full stationary timestamp processes:

`lambda_-=-W_0(-r tau)/tau`,
`lambda_+=-W_{-1}(-r tau)/tau`.

The usual count-rate ambiguity is therefore a complete static-experiment ambiguity in the ideal model. At `lambda tau=1` the branches coalesce and `G(0)=0` is the local Fisher signature. Temporal modulation breaks the static equivalence.

## Visible-event high-frequency residue — provisional general theorem

For an autonomous exact-timestamp selector `Y<=N` of incident Poisson events, input rate `lambda`, output rate `r`, under explicit diffuse-posterior and short-memory covariance assumptions,

`lim_|omega|->infty G(omega)=r/lambda`.

Interpretation: the high-frequency FI residue is the fraction of incident timestamps remaining directly visible, despite history-dependent selection.

Checks:

- independent exact-timestamp thinning: `G=eta=r/lambda`;
- nonparalyzable dead time: flat `G=r/lambda=1/(1+lambda tau)`;
- deterministic paralyzable dead time: high-frequency `G->r/lambda=exp(-rho)`.

Treat WP08 as provisional until the random-measure proof and dependent-thinning novelty search are stronger.

## Random recovery result — same paralysis curve, different information

Generalized Type II: every incident event starts iid dead interval `T`; detector is dead while any event-generated interval is active (`M/G/infinity` cluster-start model). For **every** recovery distribution with mean `m`,

`r(lambda)=lambda exp(-lambda m)`.

So equal-mean recovery laws have identical conventional saturation curves and the same zero count-rate slope at `lambda m=1`.

But complete-record FI differs:

- deterministic `T=m`: `G(0)=0` at `lambda m=1`;
- exponential `T~Exp(mu)`, `m=1/mu`: short-cycle probability
  `P(D<=delta)=lambda mu delta^2/2+O(delta^3)`, yielding
  `G_exp(0) >= r mu delta^2/2+O(delta^3)>0` for small `delta`; at `lambda=mu`,
  `G_exp(0) >= (mu delta)^2/(2e)+O((mu delta)^3)>0`.

Therefore:

`same mean paralysis curve != same complete-record information`.

Recovery-law shape is an information resource invisible to the ordinary mean input-output characteristic.

## Mandatory novelty boundaries

Do **not** claim novelty for:

- score-out = conditional expectation of score-in;
- Fisher monotonicity / Markov data processing;
- function-valued Fisher-information operators;
- translation-invariant `L2` multipliers;
- dead-time FI or information theory in general;
- modulated paralyzable photon counting;
- Type-II renewal/counting theory;
- random dead-time / `M/G/infinity` modeling;
- count-rate, interval, correlation, or PSD formulas.

Close prior art includes:

- Teich & Vannucci, JOSA 68, 1338 (1978), DOI `10.1364/JOSA.68.001338`.
- Teich & Cantor, IEEE JQE 14, 993 (1978), DOI `10.1109/JQE.1978.1069731`.
- Dvurecenskij & Ososkov, Aplikace matematiky 29, 237 (1984), DOI `10.21136/AM.1984.104092`.
- Apanasovich & Paltsev, JOSA B 12, 1550 (1995), DOI `10.1364/JOSAB.12.001550`.
- Mandalapu & Jagannathan, NCC 2021, DOI `10.1109/NCC52529.2021.9530152`.
- Jorgensen & Johnson, arXiv:2605.23210 (2026), nonparalyzable LAN/FI; Type II left open.
- Clark, Statistics & Probability Letters 236, 110779 (2026), DOI `10.1016/j.spl.2026.110779`.

No targeted search has yet found the exact WP06/WP07 Fisher-spectrum phenomena or WP08/WP12 information laws, but **no priority claim is certified**.

## Current research thesis

> Temporal Fisher transfer for autonomous detectors is a property of the full trajectory channel, not of a scalar timing or saturation summary. Time-translation symmetry gives a complete Fisher spectrum even with arbitrary memory; hidden Type-II dynamics can erase static information while retaining dynamic information; exact timestamp visibility fixes a broad high-frequency residue; and recovery-law shape can change identifiability even when the conventional paralysis curve is unchanged.

This is materially broader than Paper 1 if it survives hostile proof and novelty review.

## Next decisive gates

1. Derive an exact **renewal-output DC Fisher formula** separating count-rate and interval-shape information.
2. Quantify exponential-recovery DC FI more sharply using `M/M/infinity` busy-cycle theory.
3. Determine whether deterministic recovery is essentially unique in producing complete static branch aliasing.
4. Harden WP08 and seek a weaker Cesaro/Wiener residue statement.
5. Search dependent thinning, refractory-neuron/spike-train FI spectra, stationary nonlinear system-identification FI, and point-process LAN.
6. Add theorem-grade sources for DQM-under-Markov maps, Poisson DQM, renewal Bartlett spectra, and translation-invariant multipliers.
7. Only after these gates decide whether Paper 2 has earned a manuscript.

## Breakthrough criterion

Proceed to a manuscript only if at least one survives hostile review:

- the arbitrary-autonomous-channel Fisher-spectrum theorem is genuinely new in photodetection/information theory;
- Type-II hidden memory yields a new exact information-spectral phenomenon with substantial scope;
- the visible-event residue becomes a robust general theorem;
- recovery-law shape yields a new universal identifiability/resource theorem.

Current status: **strong enough to continue aggressively; not yet strong enough for priority language or manuscript drafting.**
