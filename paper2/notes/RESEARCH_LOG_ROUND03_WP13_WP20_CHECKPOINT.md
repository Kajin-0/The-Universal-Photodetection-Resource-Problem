# Paper 2 Research Log — Round 03: WP13–WP20 Context Checkpoint

**Date:** 2026-08-21

## Purpose

Durable recovery checkpoint for the active Paper-2 program. This file records the current theorem stack, proof repairs, prior-art corrections, numerical calibration, and next gates so that work can resume from the repository without chat history.

Paper 1 / Rev11 remains scientifically frozen. All active science below is Paper 2.

## 1. General autonomous-channel theorem — WP10/WP17

For a homogeneous Poisson source with local temporal tangent `u`, the incident score is

`S_u = int u(t)[N(dt)-Phi0 dt]`,

with source Fisher form `Phi0 <u,v>_L2`.

For any parameter-independent stochastic detector channel, the output score is the conditional expectation `E[S_u|Y]`, giving a positive contraction `A_K` on scalar `L2(R)`. If the detector channel is autonomous/time-translation covariant, `A_K` commutes with translations and therefore is a Fourier multiplier:

`F_out[u,v]=Phi0/(2*pi) int G_{Phi0,K}(omega) U*(omega)V(omega)domega`,

`0 <= G <= 1` a.e.

WP17 closes the main formal gaps using:

- locally finite counting-measure configuration spaces with vague topology;
- standard-Borel output record spaces;
- Kallenberg kernel randomization for arbitrary stochastic kernels;
- DQM under statistics / conditional-score projection;
- the classical translation-invariant `L2` multiplier theorem;
- narrowband wavepackets at Lebesgue points instead of primitive infinite sinusoids.

Paper 1 is recovered exactly as the marked-Poisson independent-event special case.

Current issue: novelty/positioning, not the basic proof architecture.

## 2. Exact hidden-memory spectral results — WP06/WP07

### Discrete one-bin Type II

At `p=1/2`, with `x=1-cos(omega)`, the exact complete-record spectrum is

`G(omega)=1-1/(2x)+ln(1+4x)/(8x^2)`.

It is strictly increasing on `(0,pi)`, with

`G(0)=0`,

`G(pi)=3/4+ln(3)/16=0.818663268...`.

### Continuous deterministic Type II

For deterministic paralyzable dead time `tau`, `rho=lambda*tau`, output rate `r=lambda exp(-rho)`.

At the classical paralysis maximum `rho=1`:

`G_1(0)=0`,

`G_1(omega)>0` for every nonzero frequency,

`lim_|omega|->infty G_1(omega)=1/e`.

At `omega=pi/tau`, the rigorous bound is

`G_1(pi/tau)>=exp(-1)(1+4/pi^2)=0.516975...`,

and independent complete-record Volterra numerics give about `0.52814`.

This remains the strongest concrete physical spectral theorem.

## 3. General iid Type-II recovery — WP13/WP14/WP18

Every incident Poisson event starts an iid recovery interval `T` of finite mean `m`. Registered events are starts of `M/G/infinity` busy clusters.

Classical prior art gives

`r(lambda)=lambda exp(-lambda m)`

and the renewal density

`U_lambda(t)=lambda F(t) exp[-lambda A(t)]`,

`A(t)=E[min(T,t)]`.

These formulas are not novel.

### Static Fisher rate

Use the homogeneous fractional-rate experiment and define the static per-time retention `G_DC` separately from the a.e.-defined WP10 multiplier.

Under renewal DQM and ordinary window-boundary regularity,

`G_DC=(r/lambda) I_D`,

where `I_D` is Fisher information in one observed renewal interval.

The interval score decomposes orthogonally into mean/rate and shape directions:

`I_D=dot(mu)^2/sigma_D^2 + I_shape`.

At `lambda*m=1`, `r'(lambda)=0`, so all surviving static information is interval-shape information.

### WP18 proof repair

At the common maximum, define

`R(t)=m-A(t)=E[(T-t)_+]`,

`g(t)=R(t)/m`,

`u_s=int exp(-s t)U_*(t)dt`,

`W_s=int exp(-s t)U_*(t)g(t)dt`.

The observed interval Laplace transform obeys

`phi_s=u_s/(1+u_s)`,

`dot(phi_s)=W_s/(1+u_s)^2`.

For deterministic recovery, `W_s=0` for every `s>0`. For every genuinely nondegenerate recovery law, `W_s>0` for every `s>0`.

If `G_DC=0`, the interval score is zero, so the derivative of every bounded interval statistic must vanish. Applying this to `exp(-sD)` forces `W_s=0`. Therefore, under stated DQM/FI-rate regularity,

`G_DC=0 iff T=m almost surely`.

Use this bounded-Laplace-statistic proof rather than the older pointwise-density necessity argument.

Quantitative witness:

`G_DC >= e^{-1} W_s^2/[(1+u_s)^4(phi_2s-phi_s^2)]`

and in particular

`G_DC >= (4/e) W_s^2/(1+u_s)^4`.

Deterministic recovery is the unique zero/minimizer of static complete-record FI at the common mean-rate maximum within the regular fixed-mean iid-recovery class.

### Global branch aliasing

For a fixed known recovery law, two distinct incident rates with equal conventional output rate produce identical complete stationary registered-timestamp laws iff recovery is deterministic.

Because the underlying renewal/pair-correlation formulas are classical, treat this as an identifiability corollary rather than as new queueing theory.

## 4. Numerical calibration

For mean recovery `m=1`, common maximum `lambda=1`:

- exponential recovery: converged `G_DC ~ 0.06915579`;
- gamma-family calculations decrease toward the deterministic limit as gamma shape increases, but this monotonicity is family-specific only.

The earlier chat-only gamma-vs-lognormal same-CV comparison was never durable and must not be relied upon.

## 5. Exact variance-insufficiency no-go — WP19

WP19 replaces the missing gamma/lognormal comparison with an exact construction.

Law A:

`P(T=1/2)=1/2`, `P(T=3/2)=1/2`.

Law B:

`P(T=1/4)=2/9`, `P(T=1)=5/9`, `P(T=7/4)=2/9`.

Both satisfy exactly

`E[T]=1`, `Var(T)=1/4`, `CV=0.5`,

and therefore have the same entire conventional mean curve

`r(lambda)=lambda exp(-lambda)`.

Yet the registered timestamp experiments differ. A common coarse-graining

`Z=1{D<=2/5}`

has zero FI for law A because `D>=1/2` a.s., while law B has normalized per-time Fisher witness

`G_Z^(B) ~ 0.00443520488427 > 0`

at `lambda=1`.

Therefore mean recovery plus variance/CV plus the entire conventional saturation curve do not determine the complete timestamp information channel.

Converged full static FI numerics also differ:

`G_DC^A ~ 0.01765400847`,

`G_DC^B ~ 0.01920433799`,

about an `8.78%` difference.

The analytic coarse-graining theorem is the rigorous no-go; the full-FI values are calibration.

## 6. Pair-correlation prior-art correction — WP15/WP16

The exact identity

`g_Y^(2)(t)=F(t) exp[lambda E[(T-t)_+]]`

is not new. Apanasovich & Paltsev, JOSA B 12, 1550–1554 (1995), contain the equivalent random-paralyzable second-order product-density formula; stationary normalization gives the WP15 identity.

Pair-correlation dead-time inversion is also established prior art, including Larsen & Kostinski (2009).

Therefore do not use WP15 as a lead novelty theorem. Its one-lag inversion is an operational corollary of classical formulas.

## 7. Visible-event residue hardening — WP20

WP20 replaces the over-strong version of WP08.

For an exact-timestamp selector `Y<=N`, form the conditional-score random measure `M`. Suppose its stationary covariance measure is

`Gamma_M = r delta_0 + nu`,

where `nu` has finite total variation and no atom at zero.

Then

`lambda G(omega)=r+nu_hat(omega)`

for a continuous representative under this finite-measure assumption.

Finite total variation alone does not force `nu_hat(omega)->0` pointwise. The robust theorem is instead the moving high-frequency band average:

`lim_{Omega->infty} 1/[(b-a)Omega] int_{a Omega}^{b Omega} G(omega)domega = r/lambda`

for every fixed `0<a<b`.

If `nu` is atomless, Wiener's theorem gives high-frequency mean-square convergence of `G` to `r/lambda` in Cesaro average. If `nu` is Rajchman—for example has an `L1` density—the stronger pointwise limit follows.

Interpretation: exact visible timestamps create a zero-lag Fisher covariance atom of weight `r`; finite non-diagonal covariance structure averages away over expanding high-frequency bands.

Recommended hierarchy:

1. finite correction covariance measure -> Cesaro band-average residue `r/lambda`;
2. atomless correction -> mean-square Cesaro convergence;
3. Rajchman/L1 correction -> pointwise `G(omega)->r/lambda`.

Use WP20 rather than WP08 as the primary general residue statement.

## 8. Hostile novelty state

Classical / must be credited:

- random Type-II/paralyzable recovery;
- `M/G/infinity` representation and busy-cycle theory;
- the random-recovery renewal density;
- random-paralyzable pair-correlation formulas;
- pair-correlation dead-time inversion generally;
- inverse/service-distribution inference for infinite-server queues;
- renewal-process Fisher information and generic rate-vs-interval timing distinctions;
- conditional-score projection and Fisher data processing;
- function-valued FI operators;
- translation-invariant Fourier multipliers;
- stationary random-measure spectral theory and Wiener's theorem;
- dead-time information theory generally;
- modulated paralyzable photocounting generally.

Unresolved historical risk:

Afanaseva & Mikhailova (1973), approximately `On recovering characteristics of some queueing systems from the output flow`, is cited in the direct Type-II lineage but a readable theorem text has not yet been located. Older inverse-output literature also includes Kendall & Lewis and related infinite-server identifiability work. Do not infer novelty from inaccessible full text.

No verified predecessor has yet been found for the exact fixed-recovery-law Fisher singularity

`G_DC=0 iff T deterministic`

at the universal Type-II mean-rate maximum, nor for the combined continuous Type-II dynamic spectral escape theorem of WP07. Priority remains uncertified.

## 9. Current novelty hierarchy

1. **WP10/WP17:** general autonomous-channel local Fisher spectrum as a photodetection-channel synthesis.
2. **WP07:** continuous Type-II static blindness with positive information at every nonzero temporal frequency and high-frequency residue `1/e`.
3. **WP18:** deterministic recovery as unique static Fisher-singular fixed-mean iid Type-II recovery at the common mean-rate maximum.
4. **WP20:** zero-lag covariance-atom / visible-event Cesaro residue theorem, subject to novelty audit.
5. **WP19:** rigorous resource no-go: mean + variance/CV + entire mean saturation curve do not determine timestamp information.

Supporting only: rate/shape decomposition, `W_s` witness, WP15 pair inversion.

## 10. Immediate next gates

1. Continue the historical inverse-output audit, especially Afanaseva–Mikhailova and old Type-II/infinite-server identifiability papers.
2. Audit WP20 specifically against stationary point-process score spectra / dependent thinning / missing-event inference; its harmonic-analysis ingredients are standard, so novelty must be detector-specific.
3. Recheck WP18 renewal DQM and window-censoring assumptions for atomic and heavy-tailed recovery laws; keep the theorem explicitly regularity-qualified.
4. Decide whether the combined WP10/WP07/WP18/WP20/WP19 stack has earned manuscript drafting only after these audits.

## 11. Operating rule

After every material theorem, proof repair, prior-art collision, numerical result used in an argument, or change in the next-gate decision, update this research log or a newer one plus `paper2/AGENTS_PAPER2.md`. Do not allow important state to exist only in chat.
