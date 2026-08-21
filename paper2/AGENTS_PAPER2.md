# AGENTS — Paper 2 General-Channel Program

## Purpose

Durable handoff for the active second-paper program in **The Universal Photodetection Resource Problem**. The repository, not chat history, is authoritative.

Active branch: `agent/uprp-core-theorem-round10`.

Paper 1 / Rev11 is scientifically frozen by default. Research remains analytical/theoretical; numerical work is for derivation checks, calibration, or published-data analysis. Do not make experiments, fabrication, procurement, or laboratory campaigns required next steps.

## Read first — authoritative recovery order

1. `paper2/notes/WP21_HISTORICAL_INVERSE_OUTPUT_IDENTIFIABILITY_AUDIT.md`
2. `paper2/notes/RESEARCH_LOG_ROUND03_WP13_WP20_CHECKPOINT.md`
3. `paper2/notes/WP20_CESARO_VISIBLE_EVENT_RESIDUE.md`
4. `paper2/notes/WP19_EXACT_VARIANCE_INSUFFICIENCY_COUNTEREXAMPLE.md`
5. `paper2/notes/WP18_LAPLACE_PROOF_REPAIR_FOR_RECOVERY_SINGULARITY.md`
6. `paper2/notes/WP17_PUBLICATION_GRADE_WP10_FORMALIZATION.md`
7. `paper2/notes/WP16_HOSTILE_RANDOM_TYPEII_PRIOR_ART_AUDIT.md`
8. `paper2/notes/WP13_RENEWAL_FISHER_DECOMPOSITION_AND_RECOVERY_UNIQUENESS.md`
9. `paper2/notes/WP14_RECOVERY_SHAPE_FISHER_WITNESS.md`
10. `paper2/notes/WP07_CONTINUOUS_PARALYZABLE_SPECTRAL_SURVIVAL.md`
11. `paper2/notes/WP10_GENERAL_AUTONOMOUS_CHANNEL_THEOREM_HARDENED.md`
12. `paper2/notes/WP06_CLOSED_FORM_HIGH_PASS_THEOREM.md`
13. `paper2/notes/WP15_PAIR_CORRELATION_RATE_IDENTIFIABILITY.md` — supporting only; read with WP16/WP21
14. `paper2/README.md`

## Current theorem stack

### A. General autonomous-channel Fisher spectrum — WP10/WP17

For homogeneous Poisson baseline flux `Phi0` and compactly supported smooth temporal tangents `u`,

`S_u = int u(t)[N(dt)-Phi0 dt]`,

`E[S_u S_v]=Phi0 <u,v>_L2`.

For any parameter-independent stochastic detector channel with complete accessible record `Y`,

`S_u^out=E[S_u|Y]`.

This defines a positive contraction `A_K` on scalar `L2(R)`. Autonomy/time-translation covariance implies `A_K` commutes with translations, hence

`F_out[u,v]=Phi0/(2*pi) int G_{Phi0,K}(omega) U*(omega)V(omega)domega`,

with `0<=G<=1` a.e. and even real representative a.e.

WP17 closes the main formal proof gaps using standard-Borel trajectory spaces, Kallenberg kernel randomization, DQM under statistics, the classical translation-invariant `L2` multiplier theorem, and narrowband wavepacket limits.

Paper 1 is recovered exactly as the marked-Poisson independent-event special case.

Candidate conceptual message:

> **Spectral completeness is symmetry-driven, not independent-event-driven.**

The mathematical ingredients are standard; novelty, if any, lies in the photodetection-channel synthesis and consequences.

### B. Exact hidden-memory spectral inversion — WP06/WP07

Discrete one-bin Type II at `p=1/2`:

`G(omega)=1-1/(2x)+ln(1+4x)/(8x^2)`, `x=1-cos(omega)`.

`G(0)=0`, it is strictly increasing on `(0,pi)`, and

`G(pi)=3/4+ln(3)/16=0.818663268...`.

Continuous deterministic paralyzable Type II with `rho=lambda*tau`:

at `rho=1`,

`G_1(0)=0`,

`G_1(omega)>0` for every `omega!=0`,

`lim_|omega|->infty G_1(omega)=1/e`.

At `omega=pi/tau`,

`G_1>=exp(-1)(1+4/pi^2)=0.516975...`,

while independent complete-record Volterra numerics give about `0.52814`.

WP07 remains the strongest concrete physical spectral theorem.

### C. General iid Type-II recovery singularity — WP13/WP14/WP18

Every incident Poisson event starts iid recovery interval `T`, `m=E[T]`. Registered events are starts of `M/G/infinity` busy clusters.

Classical prior art gives

`r(lambda)=lambda exp(-lambda m)`

and

`U_lambda(t)=lambda F(t) exp[-lambda A(t)]`,

`A(t)=E[min(T,t)]`.

Do not claim these formulas.

Use a separate homogeneous static FI-rate quantity `G_DC`; WP10's universal `G(omega)` is only defined a.e. without extra continuity.

Under renewal DQM/window regularity,

`G_DC=(r/lambda) I_D`.

At the common mean-rate maximum `lambda*m=1`, the count/rate component vanishes, so surviving static FI is entirely interval-shape information.

WP18 supplies the preferred necessity proof. Define

`R(t)=m-A(t)=E[(T-t)_+]`,

`g(t)=R(t)/m`,

`u_s=int exp(-s t)U_*(t)dt`,

`W_s=int exp(-s t)U_*(t)g(t)dt`.

The observed interval Laplace transform has

`phi_s=u_s/(1+u_s)`,

`dot(phi_s)=W_s/(1+u_s)^2`.

For deterministic recovery, all `W_s=0`; for any genuinely nondegenerate law, all `W_s>0`. Since zero interval FI forces zero derivative of every bounded statistic, applying this to `exp(-sD)` gives

`G_DC=0 iff T=m almost surely`

under the stated regularity.

Quantitative witness:

`G_DC >= e^{-1} W_s^2/[(1+u_s)^4(phi_2s-phi_s^2)]`

and

`G_DC >= (4/e)W_s^2/(1+u_s)^4`.

For a fixed known recovery law, complete Lambert-W branch aliasing occurs iff recovery is deterministic. Treat this as an identifiability corollary of classical renewal/correlation structure, not as new queueing theory.

### D. Mean/variance insufficiency — WP19

Two exact recovery laws have the same

`E[T]=1`, `Var(T)=1/4`, `CV=0.5`,

and therefore the same entire conventional curve `r(lambda)=lambda exp(-lambda)`, but different registered-timestamp experiments.

Law A:

`P(T=1/2)=1/2`, `P(T=3/2)=1/2`.

Law B:

`P(T=1/4)=2/9`, `P(T=1)=5/9`, `P(T=7/4)=2/9`.

The common coarse-graining `Z=1{D<=2/5}` has zero FI for A but normalized per-time FI about

`0.00443520488427`

for B at `lambda=1`.

Converged full static calculations give

`G_DC^A~0.01765400847`,

`G_DC^B~0.01920433799`,

about `8.78%` apart.

Conclusion: mean + variance/CV + the entire mean saturation curve do not determine the timestamp information channel. This closes the variance branch at the needed resource-no-go level.

### E. Visible-event high-frequency residue — WP20 supersedes WP08

For an exact-timestamp selector `Y<=N`, package the conditional source score into a stationary random measure `M`. If its covariance measure is

`Gamma_M = r delta_0 + nu`,

where `nu` has finite total variation and no atom at zero, then

`lambda G(omega)=r+nu_hat(omega)`

for the continuous representative in this class.

Finite total variation does **not** imply the pointwise limit `nu_hat->0`. The robust theorem is the moving-band Cesaro law:

`lim_{Omega->infty} 1/[(b-a)Omega] int_{aOmega}^{bOmega} G(omega)domega = r/lambda`

for every fixed `0<a<b`.

Hierarchy:

1. finite correction covariance measure -> exact high-frequency band-average residue `r/lambda`;
2. atomless correction -> high-frequency mean-square/Cesaro convergence via Wiener;
3. Rajchman correction, e.g. `L1` density -> pointwise `G(omega)->r/lambda`.

Interpretation: the visible-event fraction is the coefficient of the zero-lag conditional-score covariance atom. Use WP20 as the preferred general residue statement; WP08 is the stronger Level-III corollary only.

## Major prior-art corrections

Do **not** claim novelty for:

- random Type-II/paralyzable recovery or `M/G/infinity` modeling;
- busy-period/busy-cycle renewal formulas;
- `U_lambda(t)=lambda F(t)exp[-lambda A(t)]`;
- the random-paralyzable pair-correlation identity `g_Y^(2)(t)=F(t)exp[lambda E[(T-t)_+]]`;
- generic pair-correlation dead-time inversion;
- service/recovery-distribution inference from queue outputs generally;
- generic queue-output identifiability or “structural information in the output”;
- the broad phenomenon that a special service-law subfamily can be output-nonidentifiable while a generic class is recoverable;
- renewal-process FI or generic rate-vs-timing information distinctions;
- conditional-score projection or Fisher data processing;
- function-valued FI operators;
- translation-invariant Fourier multipliers;
- stationary random-measure spectral theory, covariance atoms, or Wiener's theorem;
- dead-time information theory generally;
- modulated paralyzable photocounting generally.

WP15's pair-correlation identity is already contained in Apanasovich & Paltsev (JOSA B 12, 1550–1554, 1995) after stationary specialization. Keep WP15 operational/supporting only.

## Historical audit state — WP21

The historical inverse-output gate is **closed for manuscript strategy but not for priority certification**.

Established facts:

- queue-output identifiability was an explicit research topic by at least 1965;
- Kovalenko (1965) is described by later Soviet inverse-problem literature as recovering the Poisson input rate and service-time distribution from the **output process of `M/G/1`**, with `M/M/1` exceptional;
- Kendall & Lewis (1965), Ivnitskii (1969/1977), Brown (1970), Ross (1970), George & Agrawal (1973), Shanbhag (1973), and others occupy adjacent inverse-output territory;
- by 1982, Ivchenko–Kashtanov–Kovalenko's queueing textbook had a dedicated section on recovering system characteristics from output-flow observations;
- Afanaseva & Mikhailova (1973) remains a direct Type-II-lineage blocker whose readable theorem text has not been located.

Therefore do **not** frame WP18 as a new generic identifiability result or as the first example of an exceptional information-degenerate service law.

No verified predecessor has yet been found for the narrow statement

`G_DC=0 iff T deterministic`

**at the universal Type-II mean-count maximum**, with `G_DC` the complete registered-cluster-start static Fisher retention, or for the combined WP07 dynamic spectral-escape result. Priority remains uncertified.

Further historical searching is low priority unless a realistic path to the Afanaseva–Mikhailova theorem text appears.

## Current novelty hierarchy

1. **WP10/WP17** — arbitrary-autonomous-channel local Fisher spectrum as a photodetection-channel synthesis.
2. **WP07** — continuous Type-II static blindness with positive FI at every nonzero temporal frequency and residue `1/e`.
3. **WP18** — deterministic recovery as the unique regular static Fisher-singular fixed-mean iid Type-II recovery law at the common mean-rate maximum.
4. **WP20** — visible-event zero-lag covariance-atom/Cesaro residue theorem, pending targeted novelty/proof audit.
5. **WP19** — rigorous resource no-go showing recovery mean and variance are insufficient.

Supporting only: rate/shape decomposition, `W_s` witness, branch aliasing, WP15 pair inversion.

## Immediate next gates

1. **Audit WP20 adversarially** against dependent thinning, missing-event point-process inference, score spectra, stationary random-measure spectral theory, Palm/compensator theory, and point-process information literature.
2. Recheck WP20's covariance-measure decomposition `Gamma_M=r delta_0+nu` and the claim that diffuse posterior-hidden intensity/cross terms cannot generate or cancel a zero-lag atom.
3. Recheck WP18 renewal-DQM/window-censoring assumptions for atomic and heavy-tailed recovery laws; retain explicit regularity qualifications.
4. Only after these gates decide whether WP10/WP07/WP18/WP20/WP19 has earned a Paper-2 manuscript.

## Documentation rule — mandatory

Do not allow material research state to exist only in chat.

After any material theorem, proof repair, prior-art collision, numerical result used in an argument, or change to the next-gate decision:

1. create/update the relevant `paper2/notes/WP*.md` or research log;
2. update this file when the recovery order, novelty hierarchy, or immediate gates change;
3. update `docs/CURRENT_RESEARCH_STATE.md` when project-level status changes.

If context is lost, a new agent should be able to recover the active program from the repository alone.
