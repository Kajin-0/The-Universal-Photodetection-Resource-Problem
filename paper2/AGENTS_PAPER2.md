# AGENTS — Paper 2 General-Channel Program

## Scope and branch

Durable handoff for the second paper in **The Universal Photodetection Resource Problem**.

Active branch: `agent/uprp-core-theorem-round10`.

Paper 1 / Rev11 is scientifically frozen by default. Do not alter Paper 1 unless a concrete defect or referee request requires it.

Research is analytical/theoretical. Numerical work may validate derivations or analyze published data. Do not make new experiments, fabrication, procurement, or laboratory campaigns required next steps.

## Read first — authoritative order

1. `paper2/notes/WP19_EXACT_VARIANCE_INSUFFICIENCY_COUNTEREXAMPLE.md`
2. `paper2/notes/WP18_LAPLACE_PROOF_REPAIR_FOR_RECOVERY_SINGULARITY.md`
3. `paper2/notes/WP17_PUBLICATION_GRADE_WP10_FORMALIZATION.md`
4. `paper2/notes/WP16_HOSTILE_RANDOM_TYPEII_PRIOR_ART_AUDIT.md`
5. `paper2/notes/WP13_RENEWAL_FISHER_DECOMPOSITION_AND_RECOVERY_UNIQUENESS.md`
6. `paper2/notes/WP14_RECOVERY_SHAPE_FISHER_WITNESS.md`
7. `paper2/notes/WP07_CONTINUOUS_PARALYZABLE_SPECTRAL_SURVIVAL.md`
8. `paper2/notes/WP10_GENERAL_AUTONOMOUS_CHANNEL_THEOREM_HARDENED.md`
9. `paper2/notes/WP08_VISIBLE_EVENT_HIGH_FREQUENCY_RESIDUE.md` — provisional
10. `paper2/notes/WP15_PAIR_CORRELATION_RATE_IDENTIFIABILITY.md` — read only with WP16; its central pair-correlation identity is prior art
11. `paper2/notes/WP06_CLOSED_FORM_HIGH_PASS_THEOREM.md`
12. `paper2/notes/WP09_TYPEII_AND_FISHER_OPERATOR_PRIOR_ART_AUDIT.md`
13. `paper2/README.md` — historical overview; may lag this handoff

## Current organizing theorem — WP10/WP17

For homogeneous Poisson baseline flux `Phi0`, use primitive source tangents `u in C_c^infty(R)`:

`lambda_epsilon(t)=Phi0[1+epsilon u(t)]`.

The source score is

`S_u = int u(t)[N(dt)-Phi0 dt]`,

with

`E[S_u S_v]=Phi0 <u,v>_L2`.

For any parameter-independent stochastic detector channel `K`, the output score is

`S_u^out=E[S_u|Y]`.

This induces a unique positive contraction `A_K` on scalar `L2(R)`:

`F_out[u,v]=Phi0 <u,A_K v>`, `0<=A_K<=I`.

If the channel is autonomous/time-translation covariant, `A_K` commutes with translations. Therefore

`F_out[u,v]=Phi0/(2*pi) int G_{Phi0,K}(omega) U*(omega)V(omega)domega`,

with

`0<=G_{Phi0,K}(omega)<=1` a.e. and `G(-omega)=G(omega)` a.e.

The detector may have arbitrary hidden state, dead time, saturation, recovery, afterpulsing, state-dependent capture, multiple output events, analog marks, and high-flux nonlinear history dependence. No independent-event delay kernel is assumed.

WP17 closes the main formal gaps:

- incident trajectories: locally finite counting measures on `R` with vague topology;
- output: arbitrary standard-Borel accessible record with measurable shifts;
- Kallenberg kernel randomization converts an arbitrary stochastic kernel to a statistic on an enlarged experiment;
- Pollard DQM-under-statistics gives the conditional-score identity rigorously;
- Stein's `L2` translation-invariant operator theorem gives the Fourier multiplier;
- pure infinite sinusoids are replaced by narrowband wavepacket limits at Lebesgue points of `G`.

Paper 1 is recovered exactly as the marked-Poisson special case:

`G(omega)=int |H_m(omega)|^2 kappa(dm)`.

Candidate message:

> **Spectral completeness is symmetry-driven, not independent-event-driven.**

All mathematical ingredients above are standard. The possible contribution is the photodetection-channel synthesis plus nontrivial hidden-memory consequences.

## Strongest exact hidden-memory spectral results

### Discrete one-bin Type II — WP06

`Y_n=X_n(1-X_{n-1})`, `p=1/2`.

Let `x=1-cos(omega)`:

`G(omega)=1-1/(2x)+ln(1+4x)/(8x^2)`.

It satisfies

`G(0)=0`,

is strictly increasing on `0<omega<pi`, and

`G(pi)=3/4+ln(3)/16=0.818663268...`.

### Continuous deterministic Type II — WP07

Poisson rate `lambda`, deterministic paralyzable dead time `tau`, `rho=lambda*tau`, output rate

`r=lambda exp(-rho)`.

At the paralysis maximum `rho=1`:

`G_1(0)=0`,

`G_1(omega)>0` for every nonzero frequency, and

`lim_|omega|->infty G_1(omega)=1/e`.

At `omega=pi/tau`,

`G_1(pi/tau)>=exp(-1)(1+4/pi^2)=0.516975...`.

Independent complete-record Volterra numerics give

`G_1(pi/tau)~0.52814`.

This is currently the strongest physical information-spectral result.

## General iid Type-II recovery — WP13/WP14/WP18

Each incident Poisson event starts iid recovery interval `T` with finite mean

`m=E[T]`.

The detector is dead whenever any recovery interval remains active. Registered events are starts of `M/G/infinity` busy clusters.

Classical theory gives

`r(lambda)=lambda exp(-lambda m)`

and the busy-cycle renewal density

`U_lambda(t)=lambda F(t) exp[-lambda A(t)]`,

where

`A(t)=E[min(T,t)]`.

**These stochastic-process formulas are prior art.**

### Static Fisher notation

WP10's universal `G(omega)` is only an `L^infinity` multiplier a.e., so do not casually use its point value at zero.

For the homogeneous fractional rate experiment define the static per-time retention

`G_DC = lim_{L->infty} F_out^[0,L]/(lambda L)`

whenever the regular renewal limit exists.

Under interval DQM, finite interval FI `I_D`, and ordinary window-boundary regularity:

`G_DC=(r/lambda) I_D`.

### Rate-versus-shape decomposition

`I_D=dot(mu)^2/sigma_D^2 + I_shape`,

and

`G_rate=lambda[r'(lambda)]^2/(r^3 sigma_D^2)`.

At the universal mean-rate maximum `lambda*m=1`, `r'=0`, so every surviving static bit is interval-shape information.

### Repaired deterministic-recovery singularity theorem — WP18

At `lambda*m=1`, define

`R(t)=m-A(t)=E[(T-t)_+]`,

`g(t)=R(t)/m`,

`u_s=int exp(-s t)U_*(t)dt`,

`W_s=int exp(-s t)U_*(t)g(t)dt`.

The interval Laplace transform satisfies

`phi_s=u_s/(1+u_s)`

and the fractional-rate derivative is

`dot(phi_s)=W_s/(1+u_s)^2`.

For every genuinely nondegenerate recovery law, `W_s>0` for every `s>0`; for deterministic recovery, `W_s=0` for every `s>0`.

If `G_DC=0`, then the interval score is zero and therefore the derivative of every bounded statistic must vanish. Applying this to `exp(-sD)` forces `W_s=0`, hence deterministic recovery.

Thus, under the stated renewal-DQM/FI-rate regularity,

`G_DC=0 iff T=m almost surely`.

Use this **Laplace-statistic proof**, not the older pointwise-density necessity argument in WP13.

The quantitative witness is

`G_DC >= e^{-1} W_s^2/[(1+u_s)^4(phi_2s-phi_s^2)]`

and in particular

`G_DC >= (4/e) W_s^2/(1+u_s)^4`.

Deterministic recovery is therefore the unique zero/minimizer of static complete-record FI at the common mean-rate maximum within the regular fixed-mean iid-recovery class.

### Global branch aliasing

For a fixed known recovery law, two distinct incident rates with equal conventional output rate produce identical complete stationary timestamp laws **iff recovery is deterministic**.

The necessity half follows immediately from the classical random-paralyzable pair-correlation formula, so this should be presented as an identifiability corollary rather than deep new queueing theory.

## Exact variance-insufficiency no-go — WP19

The old handoff mentioned a gamma/lognormal same-CV numerical comparison, but it was not durable. WP19 replaces it with an exact construction.

Law A:

`P(T=1/2)=1/2`, `P(T=3/2)=1/2`.

Law B:

`P(T=1/4)=2/9`, `P(T=1)=5/9`, `P(T=7/4)=2/9`.

Both have exactly

`E[T]=1`, `Var(T)=1/4`, `CV=0.5`,

and therefore exactly the same conventional mean curve

`r(lambda)=lambda exp(-lambda)`.

Yet their registered timestamp experiments differ.

At `lambda=1`, `t=3/4`:

`g_A^(2)=0.5 exp(3/8) ~ 0.7274957073`,

`g_B^(2)=(2/9) exp(13/36) ~ 0.3188717529`.

Their local pair-response derivatives are likewise different.

### Exact common-coarse-graining Fisher difference

Use one observed interval and retain only

`Z=1{D<=2/5}`.

For law A, `D>=1/2` a.s., so this statistic is constant and has zero FI for every incident rate.

For law B,

`P_lambda(D<=2/5)=(2/7)[exp(-lambda/4)-exp(-11 lambda/30)]`.

At `lambda=1`, the same statistic has normalized per-time Fisher witness

`G_Z^(B) ~ 0.00443520488427 > 0`.

Therefore `(E[T],Var(T))` cannot determine the complete registered-timestamp information channel or the Fisher information of all accessible timestamp coarse-grainings.

This is the rigorous no-go needed by the resource program. **Stop expanding the variance branch by default.**

### Full-FI numerical calibration

Reproduction assets:

- `paper2/numerics/same_mean_variance_recovery_fisher.py`
- `paper2/numerics/same_mean_variance_recovery_fisher.csv`

At finest stored grid `h=0.0003125`:

`G_DC^A ~ 0.01765400847`,

`G_DC^B ~ 0.01920433799`,

an approximately **8.78%** difference despite identical mean and variance.

This scalar full-FI inequality is a strongly converged numerical result; the experiment/coarse-graining no-go above is analytic.

## Major prior-art corrections — WP16

Do **not** claim novelty for:

- random Type-II/paralyzable recovery;
- `M/G/infinity` modeling and busy-cycle renewal theory;
- `U_lambda(t)=lambda F(t)exp[-lambda A(t)]`;
- random-paralyzable registered pair-correlation formulas;
- `g_Y^(2)(t)=F(t)exp[lambda E[(T-t)_+]]`;
- generic pair-correlation dead-time inversion;
- recovery/service-distribution inference in `M/G/infinity` systems;
- renewal FI or generic timing-vs-rate FI ideas;
- conditional-score/Fisher data processing;
- function-valued FI operators;
- translation-invariant `L2` multipliers;
- dead-time information theory generally;
- modulated paralyzable photon counting generally.

The exact pair-correlation identity in WP15 is already contained in Apanasovich & Paltsev, JOSA B 12, 1550–1554 (1995), after stationary specialization and normalization. WP15 is therefore operational/supporting only.

### Critical unresolved historical blocker

Afanaseva & Mikhailova (1973), approximately **“On recovering characteristics of some queueing systems from the output flow,”** is cited by classical Type-II literature. A readable full text has not yet been located.

Because its title directly concerns inverse recovery from output flow, it must be checked before any priority language for the deterministic full-law uniqueness theorem.

Absence of accessible full text is not evidence of novelty.

## WP08 visible-event residue — provisional

For an autonomous exact-timestamp selector `Y<=N`, under explicit diffuse-posterior and integrable covariance/mixing assumptions,

`lim_|omega|->infty G(omega)=r/lambda`.

This matches independent thinning, nonparalyzable dead time, and deterministic paralyzable dead time.

Autonomy alone does **not** imply the present mixing hypotheses. Keep WP08 provisional until it is hardened or replaced by a weaker Cesaro/Wiener statement.

## Current novelty hierarchy

### Organizing candidate

1. **WP10/WP17:** arbitrary-autonomous-channel temporal Fisher spectrum as a photodetection-channel synthesis, with exact pointwise local Fisher ordering/data processing.

### Strong physical theorem candidates

2. **WP07:** continuous deterministic Type-II spectral survival — complete static blindness at paralysis but positive information at every nonzero frequency, with high-frequency residue `1/e`.
3. **WP13/WP18:** deterministic recovery as the unique static Fisher-singular fixed-mean iid Type-II recovery law at the common mean-rate maximum.

### Strong supporting no-go

4. **WP19:** mean recovery + variance/CV + the complete conventional mean saturation curve still do not determine the timestamp information channel.

### Supporting, not lead novelty

5. WP14 recovery-shape witness.
6. WP15 pair-correlation inversion/interpretation.
7. WP08 only if its proof is strengthened.

## Current thesis

> Temporal Fisher transfer for an autonomous detector is a property of the complete trajectory channel, not of a scalar timing width or saturation curve. Time-translation symmetry yields a complete local Fisher spectrum even with arbitrary detector memory; hidden Type-II dynamics can erase a static tangent while retaining dynamic information; and within generalized iid Type-II recovery, deterministic recovery is an information-singular boundary despite all equal-mean recovery laws sharing the same conventional paralysis curve. Even adding recovery variance does not complete that characterization.

## Next decisive gates

1. **Finish the historical inverse-output audit**, especially Afanaseva–Mikhailova (1973), before assigning priority confidence to the WP13/WP18 uniqueness theorem.
2. Recheck WP13/WP18 renewal-DQM and window-censoring assumptions against heavy-tailed/atomic recovery laws; keep the Fisher theorem explicitly regularity-qualified.
3. **Harden WP08 or replace it with a weaker Cesaro/Wiener high-frequency residue theorem** under weaker assumptions.
4. After those gates, decide whether the combined WP10/WP07/WP18/WP19 stack has earned manuscript drafting.

## Breakthrough criterion

Proceed to a manuscript only if:

- WP10/WP17 is not preempted as merely a standard stationary-channel FI theorem in photodetection notation;
- WP07 remains unpreempted as a complete-record Type-II Fisher-spectrum phenomenon;
- WP18's deterministic-recovery Fisher singularity is not already contained in inverse Type-II/`M/G/infinity` literature.

Current status: **scientifically strong and increasingly focused; not yet ready for priority language or manuscript drafting.**
