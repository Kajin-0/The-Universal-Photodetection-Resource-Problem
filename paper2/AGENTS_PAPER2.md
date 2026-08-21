# AGENTS — Paper 2 General-Channel Program

## Purpose

Durable handoff for the active second-paper program in **The Universal Photodetection Resource Problem**. The repository, not chat history, is authoritative.

Active branch: `agent/uprp-core-theorem-round10`.

Paper 1 / Rev11 is scientifically frozen by default. Research remains analytical/theoretical; numerical work is for derivation checks, calibration, or published-data analysis. Do not make experiments, fabrication, procurement, or laboratory campaigns required next steps.

## Read first — authoritative recovery order

1. `paper2/notes/WP24_ATOMIC_SCORE_RESIDUE_PRIOR_ART_AUDIT.md`
2. `paper2/notes/WP23_CAUSAL_SCORE_MARTINGALE_AND_ATOMIC_MEMORY_PATHS.md`
3. `paper2/notes/WP22_CONDITIONAL_SCORE_ATOM_THEOREM_AND_SELECTOR_COROLLARY.md`
4. `paper2/notes/WP21_HISTORICAL_INVERSE_OUTPUT_IDENTIFIABILITY_AUDIT.md`
5. `paper2/notes/WP19_EXACT_VARIANCE_INSUFFICIENCY_COUNTEREXAMPLE.md`
6. `paper2/notes/WP18_LAPLACE_PROOF_REPAIR_FOR_RECOVERY_SINGULARITY.md`
7. `paper2/notes/WP17_PUBLICATION_GRADE_WP10_FORMALIZATION.md`
8. `paper2/notes/WP07_CONTINUOUS_PARALYZABLE_SPECTRAL_SURVIVAL.md`
9. `paper2/notes/WP10_GENERAL_AUTONOMOUS_CHANNEL_THEOREM_HARDENED.md`
10. `paper2/notes/RESEARCH_LOG_ROUND03_WP13_WP20_CHECKPOINT.md`

Older WP13–WP16 and WP20 remain supporting/provenance material; WP15 pair-correlation identity is prior art and supporting only.

## Current theorem stack

### WP10/WP17 — general autonomous-channel Fisher spectrum

For homogeneous Poisson source baseline `Phi0`,

`S_u=int u(t)[N(dt)-Phi0 dt]`.

For any parameter-independent stochastic detector channel with complete accessible record `Y`,

`S_u^out=E[S_u|Y]`.

This defines a positive contraction on scalar `L2(R)`. Autonomy/time-translation covariance makes it a Fourier multiplier:

`F_out[u,v]=Phi0/(2*pi) int G_{Phi0,K}(omega)U*(omega)V(omega)domega`,

with `0<=G<=1` a.e.

WP17 closes the main formal proof gaps. The mathematics is standard functional/statistical machinery; any contribution is the photodetection-channel synthesis and its consequences.

### WP07 — continuous deterministic Type-II spectral survival

For deterministic paralyzable dead time `tau`, `rho=lambda*tau`. At the classical paralysis maximum `rho=1`:

`G_1(0)=0`,

`G_1(omega)>0` for every `omega!=0`,

`lim_|omega|->infty G_1(omega)=1/e`.

At `omega*tau=pi`, analytic lower bound is `0.516975...`; exact complete-record Volterra numerics give about `0.52814`.

This remains the strongest concrete physical spectral theorem.

### WP18 — generalized iid Type-II recovery Fisher singularity

For iid recovery `T` with mean `m`, classical theory gives

`r(lambda)=lambda exp(-lambda m)`

and

`U_lambda(t)=lambda F(t)exp[-lambda A(t)]`, `A(t)=E[min(T,t)]`.

Under renewal DQM/window regularity,

`G_DC=(r/lambda)I_D`.

At `lambda*m=1`, rate/count FI vanishes. The preferred bounded-Laplace-statistic proof gives

`G_DC=0 iff T=m almost surely`

under the stated regularity.

The next active proof gate is to separate what remains true for all finite-mean nondegenerate laws from what requires finite interval FI / renewal DQM / window regularity, especially for atomic and heavy-tailed recovery.

### WP19 — exact mean/variance insufficiency no-go

Two explicit recovery laws have identical `E[T]=1`, `Var(T)=1/4`, `CV=0.5`, and identical conventional curve `r(lambda)=lambda exp(-lambda)`, but different registered-timestamp experiments.

A common interval coarse-graining has zero FI for one and normalized per-time FI `~0.00443520488427` for the other at `lambda=1`.

Converged full static retentions differ by about `8.78%`.

Mean + variance/CV + full mean saturation curve are not resource-complete.

### WP22/WP23 — conditional-score atomic residue

Abstract WP22 theorem: if the centered stationary conditional-score random measure has covariance

`Gamma_M=a delta_0+nu`,

with finite-TV `nu` and `nu({0})=0`, then

`lambda G(omega)=a+nu_hat(omega)`

and every proportional high-frequency Cesaro band average tends to

`a/lambda`.

If `nu` is atomless, Wiener gives high-frequency mean-square convergence; if Rajchman, pointwise convergence follows.

For regular exact-timestamp selectors with diffuse posterior hidden-event mean and Palm/field regularity, `a=r`, hence residue `r/lambda`.

WP23 proves causality alone is insufficient: an exact delayed score path `c u(t-tau)` contributes additional atomic timing energy, so the correct interpretation is **total atomic timing-path energy in the conditional score**, not merely visible-event fraction.

### WP24 — novelty audit of atomic residue theory

This audit is now **closed for strategy**.

Classical prior art already covers:

- Fisher information as score covariance / Bartlett identities;
- counting-process score martingales and predictable quadratic variation;
- function-valued point-process Fisher kernels;
- Bartlett spectra and the point-process high-frequency shot-noise plateau;
- Fourier-Stieltjes atom/Cesaro/Wiener/Rajchman facts;
- frequency-domain Fisher information and derivative-system formulations;
- neural/spike-train frequency-resolved information generally.

The closest collision is the combination of Clark's functional Fisher-kernel work with classical stationary point-process spectral theory. No source located states the full UPRP construction in terms of the **conditional incident-source score after arbitrary detector processing**, but the ingredients are standard enough that WP22/WP23 should be treated as **bridge/structural theory**, not a standalone mathematical breakthrough.

No priority claim is certified.

## Historical novelty state — WP21

Generic queue-output identifiability is classical by at least 1965 and textbook material by 1982. Afanaseva & Mikhailova (1973) remains an inaccessible direct Type-II-lineage blocker.

Do not claim generic output identifiability, hidden-service reconstruction, or the broad existence of exceptional information-degenerate service laws as new.

No verified predecessor has yet been found for the narrow WP18 static Fisher singularity at the universal Type-II count maximum.

## Current novelty hierarchy

1. **WP10/WP17** — organizing photodetection-channel Fisher-spectrum synthesis.
2. **WP07** — strongest concrete new-physics candidate: deterministic Type-II static blindness with dynamic information survival.
3. **WP18** — strongest class-wide physical theorem candidate: deterministic recovery as unique regular static Fisher singularity at the common Type-II maximum.
4. **WP19** — strong exact resource no-go: mean and variance are insufficient.
5. **WP22/WP23** — valuable bridge/interpretive theory; standalone novelty downgraded by WP24.

Supporting only: WP14 witness, WP20 intermediate derivation, rate/shape decomposition, branch aliasing, WP15 pair inversion.

## Immediate next gates

1. **Harden WP18 for atomic and heavy-tailed recovery laws.** Separate broad bounded-statistic sensitivity/identifiability from finite Fisher-rate claims.
2. Determine minimal conditions for `G_DC=(r/lambda)I_D` and rigorously account for finite-window boundary/censoring.
3. Determine what survives when `E[T]<infinity` but `Var(T)=infinity`, interval FI is infinite, or DQM fails.
4. Only after that proof gate decide whether the WP10/WP07/WP18/WP19 stack, with WP22/WP23 as bridge theory, has earned manuscript drafting.

## Mandatory documentation rule

Do not allow material research state to exist only in chat.

After any material theorem, proof repair, prior-art collision, numerical result used in an argument, or change to the next-gate decision:

1. create/update the relevant `paper2/notes/WP*.md` or research log;
2. update this file when recovery order, novelty hierarchy, or immediate gates change;
3. update `docs/CURRENT_RESEARCH_STATE.md` when project-level status changes.
