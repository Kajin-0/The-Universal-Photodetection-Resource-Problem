# Current Research State

**Date:** 2026-08-21

Active branch: `agent/uprp-core-theorem-round10`

## Project-level status

1. **Paper 1 / Rev11:** scientifically frozen and technically validated for Physical Review Applied; only factual/personal submission metadata remain.
2. **Paper 2:** active theoretical program on arbitrary autonomous detector channels, hidden-memory Fisher spectra, Type-II recovery information singularities, and temporal information resources.

The active scientific frontier is Paper 2.

## Read first

1. `AGENTS.md`
2. `paper2/AGENTS_PAPER2.md`
3. `paper2/notes/RESEARCH_LOG_ROUND04_WP21_WP26_CHECKPOINT.md`
4. `paper2/notes/WP26_FINITE_MEAN_STATIONARY_WINDOW_FISHER_RATE.md`
5. `paper2/notes/WP25_FINITE_MEAN_CYCLE_DQM_AND_HEAVY_TAIL_HARDENING.md`
6. `paper2/notes/WP24_ATOMIC_SCORE_RESIDUE_PRIOR_ART_AUDIT.md`
7. `paper2/notes/WP23_CAUSAL_SCORE_MARTINGALE_AND_ATOMIC_MEMORY_PATHS.md`
8. `paper2/notes/WP22_CONDITIONAL_SCORE_ATOM_THEOREM_AND_SELECTOR_COROLLARY.md`
9. `paper2/notes/WP21_HISTORICAL_INVERSE_OUTPUT_IDENTIFIABILITY_AUDIT.md`
10. `paper2/notes/WP19_EXACT_VARIANCE_INSUFFICIENCY_COUNTEREXAMPLE.md`
11. `paper2/notes/WP17_PUBLICATION_GRADE_WP10_FORMALIZATION.md`
12. `paper2/notes/WP07_CONTINUOUS_PARALYZABLE_SPECTRAL_SURVIVAL.md`

# Paper 1 — frozen Rev11

Preferred candidate remains Rev11. Do not reopen science absent a concrete defect or referee request.

# Paper 2 — current core

## WP10/WP17 — autonomous-channel Fisher spectrum

For homogeneous Poisson baseline `Phi0`, any parameter-independent stochastic detector channel has output score

`S_u^out=E[S_u|Y]`,

with incident score

`S_u=int u(t)[N(dt)-Phi0dt]`.

Autonomy/time-translation covariance yields the scalar Fisher multiplier

`F_out[u,v]=Phi0/(2*pi)int G_{Phi0,K}(omega)U*(omega)V(omega)domega`,

`0<=G<=1` a.e.

WP17 closes the principal formal gaps. This is the organizing synthesis, not a claim that the underlying functional-analysis/statistical ingredients are new.

## WP07 — deterministic Type-II spectral survival

At deterministic paralyzable saturation `lambda*tau=1`:

`G_1(0)=0`,

`G_1(omega)>0` for every nonzero frequency,

`lim_|omega|->infty G_1(omega)=1/e`.

At `omega*tau=pi`, analytic lower bound is `0.516975...`; exact complete-record Volterra numerics give about `0.52814`.

This remains the strongest concrete physical spectral result.

## WP25/WP26 — finite-mean generalized Type-II singularity theorem

Let iid recovery `T` have only finite positive mean

`m=E[T] in (0,infinity)`.

### WP25: Palm-cycle theorem

At the common count-rate maximum `lambda_*=1/m`, for every `s>0`, the bounded interval statistic

`Z_s=exp(-sD)`

has exact derivative

`dot phi_s=W_s/(1+u_s)^2`.

For every nondegenerate recovery law, `W_s>0`; for deterministic `T=m` a.s., `W_s=0`.

Thus nondegenerate recovery is first-order separated from the deterministic singular case in total variation/Hellinger without requiring a density, DQM, finite variance, or finite Fisher information.

Palm-initialize at a registered cluster start. The latent marked-Poisson cycle score is

`S_cyc=N_D-lambda D`

with exact FI

`E[S_cyc^2]=lambda E[D]=lambda/r`.

The observed interval is a statistic, so

`I_D<=lambda/r`.

Define

`G_cyc=(r/lambda)I_D`.

Then for every finite-mean recovery law, including atomic, singular, infinite-variance, and heavy-tailed laws,

`0<=G_cyc<=1`,

and at `lambda*m=1`,

`G_cyc=0 iff T=m almost surely`.

### WP26: stationary long-window equality

The fixed-window regularity gate is now **closed**.

For an ordinary renewal process started at a renewal, progressively censored next-interval information `J(t)` increases to `I_D`. Sequential score orthogonality plus the elementary renewal theorem gives

`I_ord(t)/t -> r I_D`

under only finite `E[D]` and finite `I_D`.

For the stationary Type-II random-origin boundary, the complete relevant pre-zero state is the finite marked-Poisson cloud of recovery intervals active at time zero. Its mean population is `lambda m`, hence its fractional-rate FI is `lambda m`.

If `Y` is the forward recurrence to the first registered event,

`I(C_L(Y)) <= lambda m + lambda E[min(Y,L)]`.

Since `Y<infinity` a.s.,

`E[min(Y,L)]/L ->0`

even when `E[Y]=infinity`.

The stationary window therefore obeys

`I_stat(L)=I(C_L(Y))+E[1{Y<L}I_ord(L-Y)]`,

so

`boxed: lim_{L->infinity}I_stat(L)/L=rI_D`.

Equivalently, throughout the entire finite-mean iid-recovery Type-II class,

`boxed: G_DC=G_cyc=(r/lambda)I_D`.

At `lambda*m=1`,

`boxed: G_DC=0 iff T=E[T] almost surely`.

No density, finite recovery variance, finite forward-recurrence mean, or separate finite-FRT-FI assumption remains.

Zhao–Nagaraja (2011) establish the analogous generic window-censored renewal asymptotic under stronger FRT regularity. WP26's improvement is Type-II-specific and uses the finite stationary `M/G/infinity` latent boundary state; do not claim a new generic renewal theorem.

This is now the strongest class-wide physical theorem in Paper 2.

## WP19 — exact mean/variance insufficiency

Two explicit recovery laws have identical mean `1`, variance `1/4`, CV `0.5`, and identical conventional saturation curve, but different registered-timestamp information experiments. A common coarse-graining has zero FI for one and normalized FI `~0.00443520488427` for the other; converged full static FI differs by about `8.78%`.

Mean + variance/CV + conventional mean curve are not resource-complete.

## WP21 — historical inverse-output audit

Generic output-flow identifiability is classical from at least the 1960s and textbook material by 1982. Afanaseva & Mikhailova (1973) remains a direct Type-II-lineage historical blocker whose theorem text is inaccessible.

Do not claim generic queue-output identifiability, hidden-service reconstruction, or exceptional information-degenerate service laws as new.

## WP22/WP23/WP24 — conditional-score atomic residue bridge

WP22 gives the abstract zero-lag conditional-score covariance atom/Cesaro residue theorem. WP23 shows causality alone is insufficient because exact delayed score paths add atomic timing energy. WP24 finds that the mathematical ingredients are strongly classical, so this stack is retained as structural bridge theory, not standalone breakthrough material.

# Current novelty hierarchy

1. **WP10/WP17:** organizing photodetection-channel Fisher-spectrum synthesis.
2. **WP07:** strongest concrete dynamic physical novelty candidate.
3. **WP25/WP26:** strongest class-wide physical theorem candidate; arbitrary finite-mean deterministic recovery is the unique zero of stationary static Fisher retention at the common Type-II maximum.
4. **WP19:** exact resource incompleteness/no-go result.
5. **WP22/WP23:** useful structural bridge; standalone novelty downgraded by WP24.

# Immediate next gate

The heavy-tail/fixed-window proof program is closed unless a concrete flaw is found.

Perform one integrated hostile proof/novelty review of the candidate Paper-2 stack:

1. proof correctness and hidden assumptions across WP10/WP07/WP25/WP26/WP19;
2. consistency between spectral `G(omega)`, Palm-cycle `G_cyc`, and stationary static `G_DC`;
3. targeted prior-art collision search focused on WP07 and the exact WP25/WP26 finite-mean zero-IFF-deterministic theorem;
4. significance/coherence: whether WP07 + WP25/WP26 + WP19 form a genuine temporal-information resource theory rather than disconnected dead-time results;
5. manuscript threshold decision.

Do not begin manuscript drafting before this integrated review is complete.

# Documentation requirement

Material theorem results, proof repairs, prior-art collisions, numerical results used in arguments, and changes in next-gate decisions must be committed immediately. Keep `paper2/AGENTS_PAPER2.md` and this file synchronized with the active frontier.
