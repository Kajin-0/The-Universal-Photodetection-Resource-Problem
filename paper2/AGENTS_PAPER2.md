# AGENTS — Paper 2 General-Channel Program

## Purpose

Durable handoff for the active second-paper program in **The Universal Photodetection Resource Problem**. The repository, not chat history, is authoritative.

Active branch: `agent/uprp-core-theorem-round10`.

Paper 1 / Rev11 is scientifically frozen by default. Research remains analytical/theoretical; numerical work is for derivation checks, calibration, or published-data analysis. Do not make experiments, fabrication, procurement, or laboratory campaigns required next steps.

## Read first — authoritative recovery order

1. `paper2/notes/RESEARCH_LOG_ROUND04_WP21_WP26_CHECKPOINT.md`
2. `paper2/notes/WP26_FINITE_MEAN_STATIONARY_WINDOW_FISHER_RATE.md`
3. `paper2/notes/WP25_FINITE_MEAN_CYCLE_DQM_AND_HEAVY_TAIL_HARDENING.md`
4. `paper2/notes/WP24_ATOMIC_SCORE_RESIDUE_PRIOR_ART_AUDIT.md`
5. `paper2/notes/WP23_CAUSAL_SCORE_MARTINGALE_AND_ATOMIC_MEMORY_PATHS.md`
6. `paper2/notes/WP22_CONDITIONAL_SCORE_ATOM_THEOREM_AND_SELECTOR_COROLLARY.md`
7. `paper2/notes/WP21_HISTORICAL_INVERSE_OUTPUT_IDENTIFIABILITY_AUDIT.md`
8. `paper2/notes/WP19_EXACT_VARIANCE_INSUFFICIENCY_COUNTEREXAMPLE.md`
9. `paper2/notes/WP17_PUBLICATION_GRADE_WP10_FORMALIZATION.md`
10. `paper2/notes/WP07_CONTINUOUS_PARALYZABLE_SPECTRAL_SURVIVAL.md`
11. `paper2/notes/WP10_GENERAL_AUTONOMOUS_CHANNEL_THEOREM_HARDENED.md`

Older WP13–WP18 and WP20 remain supporting/provenance material; WP15 pair-correlation identity is prior art and supporting only.

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

For deterministic paralyzable dead time `tau`, `rho=lambda*tau`. At `rho=1`:

`G_1(0)=0`,

`G_1(omega)>0` for every `omega!=0`,

`lim_|omega|->infty G_1(omega)=1/e`.

At `omega*tau=pi`, the analytic lower bound is `0.516975...`; exact complete-record Volterra numerics give about `0.52814`.

This remains the strongest concrete physical spectral theorem.

### WP25/WP26 — finite-mean generalized Type-II singularity theorem

Let iid recovery `T` have only

`0<m=E[T]<infinity`.

Classical formulas are

`r(lambda)=lambda exp(-lambda m)`,

`E[D]=1/r`,

and the random-Type-II busy-cycle renewal formulas. These are prior art.

#### Regularity-free bounded-statistic separation — WP25

At the common count maximum `lambda_*=1/m`, for every `s>0`,

`dot phi_s = W_s/(1+u_s)^2`,

where `phi_s=E[exp(-sD)]`.

For every genuinely nondegenerate recovery law, `W_s>0`; for deterministic recovery, all `W_s=0`.

Thus every nondegenerate finite-mean recovery law is first-order separated from the deterministic singular case by the bounded statistic `exp(-sD)`, even without assuming a density, DQM, finite variance, or finite FI.

#### Universal Palm-cycle FI — WP25

Palm-initialize at a registered cluster start and stop at the next one. The latent marked-Poisson cycle has score

`S_cyc=N_D-lambda D`

and exact FI

`E[S_cyc^2]=lambda E[D]=lambda/r`.

The observed interval `D` is a statistic, so

`I_D<=lambda/r`.

Define

`G_cyc=(r/lambda)I_D`.

Then for every finite-mean recovery law

`0<=G_cyc<=1`,

and at `lambda*m=1`,

`G_cyc=0 iff T=m almost surely`.

This covers atomic, singular, infinite-variance, and heavy-tailed recovery.

#### Stationary fixed-window rate — WP26

WP26 closes the last major regularity caveat.

For an ordinary renewal process started at a renewal, progressively censoring the next interval at residual horizon `t` gives information `J(t)` with

`J(t) increasing to I_D`.

Sequential score orthogonality plus the elementary renewal theorem yields

`I_ord(t)/t -> r I_D`

under only finite `E[D]` and finite `I_D`.

For the **stationary Type-II** random-origin boundary, the relevant pre-zero detector state is exactly the finite marked-Poisson cloud of recovery intervals active at time zero. Its total mean population is `lambda m`, so its fractional-rate FI is `lambda m`.

If `Y` is the forward recurrence to the first registered event, the censored first-stage observation satisfies

`I(C_L(Y)) <= lambda m + lambda E[min(Y,L)]`.

Because `Y<infinity` a.s.,

`E[min(Y,L)]/L ->0`

even when `E[Y]=infinity`.

DQM chain rule then gives

`I_stat(L)=I(C_L(Y))+E[1{Y<L}I_ord(L-Y)]`,

and therefore

`boxed: lim_{L->infinity} I_stat(L)/L = r I_D`.

Hence throughout the entire finite-mean iid-recovery Type-II class,

`boxed: G_DC=G_cyc=(r/lambda)I_D`,

and at the universal count maximum

`boxed: G_DC=0 iff T=E[T] almost surely`.

No density, finite variance, finite forward-recurrence mean, or separate FRT-FI assumption remains.

Zhao–Nagaraja (2011) prove the analogous generic window-censored renewal asymptotic under stronger FRT regularity; do not claim the generic renewal result as new. The project-specific hardening is the use of the finite stationary `M/G/infinity` boundary state to remove that caveat for this detector class.

### WP19 — exact mean/variance insufficiency no-go

Two explicit recovery laws have identical `E[T]=1`, `Var(T)=1/4`, `CV=0.5`, and identical conventional curve `r(lambda)=lambda exp(-lambda)`, but different registered-timestamp experiments.

A common interval coarse-graining has zero FI for one and normalized per-time FI `~0.00443520488427` for the other at `lambda=1`. Converged full static retentions differ by about `8.78%`.

Mean + variance/CV + full mean saturation curve are not resource-complete.

### WP22/WP23/WP24 — conditional-score atomic residue bridge

WP22 gives the abstract zero-lag conditional-score covariance atom / high-frequency Cesaro residue statement. WP23 shows causality alone is insufficient because exact delayed score paths add atomic timing energy. WP24 finds the mathematical ingredients are strongly classical.

Keep this stack as **bridge/structural theory**, not a standalone breakthrough claim.

## Historical novelty state — WP21

Generic queue-output identifiability is classical by at least 1965 and textbook material by 1982. Afanaseva & Mikhailova (1973) remains an inaccessible direct Type-II-lineage blocker.

Do not claim generic output identifiability, hidden-service reconstruction, or the broad existence of exceptional information-degenerate service laws as new.

No verified predecessor has yet been found for the exact finite-mean zero-IFF-deterministic Type-II Fisher theorem at the universal count maximum.

## Current novelty hierarchy

1. **WP10/WP17** — organizing photodetection-channel Fisher-spectrum synthesis.
2. **WP07** — strongest concrete physical novelty candidate: deterministic Type-II static blindness with dynamic information survival.
3. **WP25/WP26** — strongest class-wide physical theorem candidate: finite-mean deterministic recovery is the unique zero of complete stationary static Fisher retention at the common Type-II maximum.
4. **WP19** — strong exact resource no-go: recovery mean and variance are insufficient.
5. **WP22/WP23** — valuable bridge/interpretive theory; standalone novelty downgraded by WP24.

## Immediate next gate

The heavy-tail/fixed-window proof program is **closed unless a concrete flaw is found**.

Perform one integrated hostile review of the candidate Paper-2 stack:

1. proof correctness and hidden assumptions across WP10/WP07/WP25/WP26/WP19;
2. notation/experiment consistency between spectral `G(omega)`, Palm-cycle `G_cyc`, and stationary static `G_DC`;
3. targeted novelty collision search focused specifically on WP07 and the exact WP25/WP26 finite-mean zero-IFF-deterministic theorem;
4. significance/coherence: determine whether WP07 + WP25/WP26 + WP19 form one resource-theory story rather than a collection of dead-time facts;
5. decide whether manuscript drafting is now justified.

Do **not** begin manuscript drafting before this integrated review is completed.

## Mandatory documentation rule

Do not allow material research state to exist only in chat.

After any material theorem, proof repair, prior-art collision, numerical result used in an argument, or change to the next-gate decision:

1. create/update the relevant `paper2/notes/WP*.md` or research log;
2. update this file when recovery order, novelty hierarchy, or immediate gates change;
3. update `docs/CURRENT_RESEARCH_STATE.md` when project-level status changes.
