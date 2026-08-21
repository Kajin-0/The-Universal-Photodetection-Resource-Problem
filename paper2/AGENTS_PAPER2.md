# AGENTS — Paper 2 General-Channel Program

## Purpose

Durable handoff for the active second-paper program in **The Universal Photodetection Resource Problem**. The repository, not chat history, is authoritative.

Active branch: `agent/uprp-core-theorem-round10`.

Paper 1 / Rev11 is scientifically frozen by default. Research remains analytical/theoretical; numerical work is for derivation checks, calibration, or published-data analysis. Do not make experiments, fabrication, procurement, or laboratory campaigns required next steps.

## Read first — authoritative recovery order

1. `paper2/notes/WP23_CAUSAL_SCORE_MARTINGALE_AND_ATOMIC_MEMORY_PATHS.md`
2. `paper2/notes/WP22_CONDITIONAL_SCORE_ATOM_THEOREM_AND_SELECTOR_COROLLARY.md`
3. `paper2/notes/WP21_HISTORICAL_INVERSE_OUTPUT_IDENTIFIABILITY_AUDIT.md`
4. `paper2/notes/RESEARCH_LOG_ROUND03_WP13_WP20_CHECKPOINT.md`
5. `paper2/notes/WP19_EXACT_VARIANCE_INSUFFICIENCY_COUNTEREXAMPLE.md`
6. `paper2/notes/WP18_LAPLACE_PROOF_REPAIR_FOR_RECOVERY_SINGULARITY.md`
7. `paper2/notes/WP17_PUBLICATION_GRADE_WP10_FORMALIZATION.md`
8. `paper2/notes/WP16_HOSTILE_RANDOM_TYPEII_PRIOR_ART_AUDIT.md`
9. `paper2/notes/WP07_CONTINUOUS_PARALYZABLE_SPECTRAL_SURVIVAL.md`
10. `paper2/notes/WP10_GENERAL_AUTONOMOUS_CHANNEL_THEOREM_HARDENED.md`
11. `paper2/notes/WP20_CESARO_VISIBLE_EVENT_RESIDUE.md` — intermediate; superseded by WP22/WP23
12. `paper2/notes/WP13_RENEWAL_FISHER_DECOMPOSITION_AND_RECOVERY_UNIQUENESS.md`
13. `paper2/notes/WP14_RECOVERY_SHAPE_FISHER_WITNESS.md`
14. `paper2/notes/WP15_PAIR_CORRELATION_RATE_IDENTIFIABILITY.md` — supporting/prior-art-limited
15. `paper2/README.md`

## Current theorem stack

### A. General autonomous-channel Fisher spectrum — WP10/WP17

For homogeneous Poisson baseline flux `Phi0` and compactly supported smooth waveform tangent `u`,

`S_u=int u(t)[N(dt)-Phi0 dt]`.

For any parameter-independent stochastic detector channel with complete record `Y`,

`S_u^out=E[S_u|Y]`.

This induces a positive contraction `A_K` on scalar `L2(R)`. Autonomy/time-translation covariance implies `A_K` commutes with translations and therefore

`F_out[u,v]=Phi0/(2*pi) int G_{Phi0,K}(omega)U*(omega)V(omega)domega`,

with `0<=G<=1` a.e.

WP17 closes the principal formal gaps using standard-Borel trajectory spaces, Kallenberg kernel randomization, DQM under statistics, the classical translation-invariant `L2` multiplier theorem, and narrowband wavepacket/Lebesgue-point limits.

Candidate message:

> **Spectral completeness is symmetry-driven, not independent-event-driven.**

The mathematical ingredients are standard; any contribution is the photodetection-channel synthesis and consequences.

### B. Exact hidden-memory spectral inversion — WP06/WP07

Continuous deterministic Type II remains the strongest concrete physical result. With `rho=lambda*tau`, at `rho=1`:

`G_1(0)=0`,

`G_1(omega)>0` for every `omega!=0`,

`lim_|omega|->infty G_1(omega)=1/e`.

At `omega=pi/tau`, analytic lower bound is `0.516975...`; exact complete-record Volterra numerics give about `0.52814`.

The discrete one-bin Type-II model at `p=1/2` has the exact monotone information-high-pass spectrum

`G(omega)=1-1/(2x)+ln(1+4x)/(8x^2)`, `x=1-cos(omega)`,

with `G(pi)=0.818663268...`.

### C. General iid Type-II recovery singularity — WP18

For iid recovery `T` with mean `m`, classical theory gives

`r(lambda)=lambda exp(-lambda m)`

and

`U_lambda(t)=lambda F(t)exp[-lambda A(t)]`, `A(t)=E[min(T,t)]`.

These formulas are prior art.

Use homogeneous static retention `G_DC` separately from WP10's a.e.-defined `G(omega)`. Under renewal DQM/window regularity,

`G_DC=(r/lambda)I_D`.

At `lambda*m=1`, count/rate FI vanishes. WP18's bounded-Laplace-statistic proof gives

`G_DC=0 iff T=m almost surely`

under the stated regularity.

The witness includes

`G_DC >= (4/e)W_s^2/(1+u_s)^4`.

Do not present branch aliasing or generic recovery identifiability as lead novelty.

### D. Mean/variance insufficiency — WP19

Two explicit recovery laws have identical

`E[T]=1`, `Var(T)=1/4`, `CV=0.5`,

and identical conventional saturation curve `r(lambda)=lambda exp(-lambda)`, but different timestamp information channels.

A common interval coarse-graining has zero FI for one law and normalized per-time FI `~0.00443520488427` for the other at `lambda=1`.

Converged full static retentions differ by about `8.78%`:

`G_DC^A~0.01765400847`,

`G_DC^B~0.01920433799`.

This closes the mean+variance resource-completeness question: they are insufficient.

### E. Conditional-score covariance-atom theorem — WP22

Let the complete output score admit a centered stationary random measure `M` with covariance measure

`Gamma_M=a delta_0+nu`,

where `nu` has finite total variation and `nu({0})=0`.

Then

`lambda G(omega)=a+nu_hat(omega)`

for the Fourier-Stieltjes representative in this regularity class, and for every fixed `0<a0<b0`,

`lim_{Omega->infty} 1/[(b0-a0)Omega] int_{a0Omega}^{b0Omega}G(omega)domega = a/lambda`.

Thus the robust invariant is

> **zero-lag conditional-score covariance atom / incident Fisher normalization.**

If `nu` is atomless, Wiener gives high-frequency mean-square convergence. If `nu` is Rajchman, pointwise convergence follows.

For a regular exact-timestamp selector `Y<=N` of rate `r`, diffuse posterior hidden-event conditional mean plus Palm/field regularity imply `Gamma_M({0})=r`, hence residue `r/lambda`.

Important withdrawal: `Y<=N` alone does **not** prove `a=r`.

### F. Causal score martingale and atomic memory paths — WP23

Standard counting-process likelihood gives, for output intensity `q_t^epsilon`,

`S_u^Y=int dot(log q_t)[u] [dY_t-q_tdt]`,

and

`F_Y[u,v]=E int q_t h_t[u]h_t[v]dt`.

For a causal exact-timestamp selector with

`q_t^epsilon=lambda_epsilon(t) alpha_t^epsilon`,

one has

`h_t[u]=u(t)+B_t[u]`,

where `B` is the causal acceptance-memory response.

**Causality alone is insufficient** to imply residue `r/lambda`. If

`B_t[u]=c u(t-tau)`,

then

`G(omega) proportional to |1+c exp(-i omega tau)|^2`,

so its high-frequency band average contains `1+c^2`, not merely `1`. The delayed atomic path contributes its own zero-lag Fisher covariance through `B*B`.

Hence the correct physical interpretation is:

> **the high-frequency Cesaro residue measures total atomic timing-path energy in the conditional score.**

Immediate visible timestamps are one atomic path; perfectly sharp delayed memory paths can add more. Diffuse/smoothing memory averages away under the WP22 regularity.

For an idealized deterministic impulse response

`k(dt)=sum_j c_j delta_{tau_j}(dt)+k_c(t)dt`,

with diffuse finite-energy `k_c`,

`lim <G>_high=(r/lambda) sum_j |c_j|^2`.

For a regular exact-timestamp selector the direct path has `c_0=1`, `tau_0=0`. Additional nonzero atomic delays add to the residue.

Do **not** replace WP22's diffuse/non-atomic memory assumptions with merely “causal.”

## Historical audit — WP21

The historical inverse-output gate is **closed for manuscript strategy but not priority certification**.

Generic queue-output identifiability is classical. Kovalenko (1965) is described as recovering Poisson input rate and service distribution from an `M/G/1` output process with `M/M/1` exceptional. Kendall & Lewis, Ivnitskii, Brown, Ross, George & Agrawal, Shanbhag and others occupy adjacent territory. By 1982 output-flow reconstruction was textbook material.

Afanaseva & Mikhailova (1973) remains a direct Type-II-lineage blocker whose readable theorem text has not been located.

Therefore do not claim generic identifiability, output reconstruction, or the broad existence of an exceptional information-degenerate service law as new.

No verified predecessor has yet been found for the narrow WP18 Fisher singularity at the universal Type-II count maximum.

## Major novelty boundaries

Do **not** claim novelty for:

- random Type-II / `M/G/infinity` modeling and busy-cycle formulas;
- random-paralyzable pair-correlation identities or generic dead-time inversion;
- queue-output identifiability or hidden-service reconstruction generally;
- renewal-process FI or generic rate-vs-timing distinctions;
- score-out as conditional expectation / Fisher data processing;
- point-process likelihood scores as innovation-martingale integrals;
- martingale isometry for Fisher information;
- function-valued score/Fisher kernels;
- translation-invariant Fourier multipliers;
- point-process covariance/Bartlett spectra;
- Campbell/Palm formulas;
- Fourier-Stieltjes, Wiener, Rajchman, or atomic/diffuse measure decompositions;
- dead-time information theory generally;
- modulated paralyzable photocounting generally.

## Current novelty hierarchy

1. **WP10/WP17** — arbitrary-autonomous-channel local Fisher spectrum as a photodetection-channel synthesis.
2. **WP07** — continuous Type-II static blindness with positive FI at every nonzero temporal frequency and residue `1/e`.
3. **WP18** — deterministic recovery as unique regular static Fisher-singular iid Type-II recovery at the common mean-rate maximum.
4. **WP22/WP23** — conditional-score covariance-atom theorem and atomic timing-path interpretation, pending targeted novelty audit.
5. **WP19** — exact resource no-go showing recovery mean and variance are insufficient.

Supporting only: WP20 intermediate derivation, WP14 witness, rate/shape decomposition, branch aliasing, WP15 pair inversion.

## Immediate next gates

1. Continue **targeted novelty audit of WP22/WP23**, specifically seeking prior statements connecting score/innovation spectra, conditional-score covariance atoms, and high-frequency Fisher residue.
2. Compare against classical counting-process martingale likelihood theory, point-process innovations/residuals, Bartlett spectra, neural frequency-resolved information, and photodetection dead-time FI. The standard ingredients are already prior art; the question is whether their exact UPRP synthesis is also old.
3. Determine whether a physically useful microscopic condition stronger than causality but weaker/more natural than WP22's diffuse-posterior condition guarantees non-atomic memory for ordinary event-driven selectors. Do not force this if it merely renames the assumption.
4. Recheck WP18 renewal-DQM/window-censoring assumptions for atomic and heavy-tailed recovery laws.
5. Only then decide whether WP10/WP07/WP18/WP22-WP23/WP19 has earned manuscript drafting.

## Documentation rule — mandatory

Do not allow material research state to exist only in chat.

After any material theorem, proof repair, prior-art collision, numerical result used in an argument, or change to the next-gate decision:

1. create/update the relevant `paper2/notes/WP*.md` or research log;
2. update this file when recovery order, novelty hierarchy, or immediate gates change;
3. update `docs/CURRENT_RESEARCH_STATE.md` when project-level status changes.

If context is lost, a new agent must be able to recover the active program from the repository alone.
