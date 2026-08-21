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
3. `paper2/notes/WP25_FINITE_MEAN_CYCLE_DQM_AND_HEAVY_TAIL_HARDENING.md`
4. `paper2/notes/WP24_ATOMIC_SCORE_RESIDUE_PRIOR_ART_AUDIT.md`
5. `paper2/notes/WP23_CAUSAL_SCORE_MARTINGALE_AND_ATOMIC_MEMORY_PATHS.md`
6. `paper2/notes/WP22_CONDITIONAL_SCORE_ATOM_THEOREM_AND_SELECTOR_COROLLARY.md`
7. `paper2/notes/WP21_HISTORICAL_INVERSE_OUTPUT_IDENTIFIABILITY_AUDIT.md`
8. `paper2/notes/WP19_EXACT_VARIANCE_INSUFFICIENCY_COUNTEREXAMPLE.md`
9. `paper2/notes/WP18_LAPLACE_PROOF_REPAIR_FOR_RECOVERY_SINGULARITY.md`
10. `paper2/notes/WP17_PUBLICATION_GRADE_WP10_FORMALIZATION.md`
11. `paper2/notes/WP07_CONTINUOUS_PARALYZABLE_SPECTRAL_SURVIVAL.md`

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

## WP25 — finite-mean generalized Type-II singularity theorem

This supersedes the main regularity concern in WP18 at the **Palm-cycle** level.

Let iid recovery `T` have only finite positive mean

`m=E[T] in (0,infinity)`.

At the common count-rate maximum `lambda_*=1/m`, for every `s>0`, the one-interval bounded statistic

`Z_s=exp(-sD)`

has exact fractional-rate derivative

`dot phi_s=W_s/(1+u_s)^2`.

For every nondegenerate recovery law, `W_s>0`; for deterministic `T=m` a.s., `W_s=0`.

Therefore nondegenerate recovery is first-order separated from the base experiment in total variation and Hellinger distance **without requiring DQM, a density, finite variance, or finite Fisher information**.

### Palm-cycle Fisher bound

Palm-initialize at a registered cluster start and stop at the next registered event. The latent marked-Poisson cycle has score

`S_cyc=N_D-lambda D`

and exact information

`E[S_cyc^2]=lambda E[D]=lambda/r<infinity`.

Localization at `D wedge K` uses only `E[D]<infinity`, which follows from finite recovery mean. Since the observed interval `D` is a statistic,

`I_D<=lambda/r`.

Define

`G_cyc=(r/lambda)I_D`.

Then for **every finite-mean recovery law**, including atomic, singular, infinite-variance, and heavy-tailed laws,

`0<=G_cyc<=1`,

and at `lambda*m=1`,

`G_cyc=0 iff T=m almost surely`.

This is now the strongest class-wide Type-II theorem.

### Remaining fixed-window issue

The unresolved question is narrower:

Does finite mean alone imply the stationary long-window Fisher-rate identity

`F_window(L)=rI_D L+o(L)`

and hence

`G_DC=G_cyc`?

WP25 does **not** assume this. Very heavy-tailed stationary renewal boundary/censoring terms may require additional regularity even though the Palm-cycle theorem is fully finite-mean.

This fixed-window boundary question is the active proof gate.

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
2. **WP07:** strongest concrete physical novelty candidate.
3. **WP25:** strongest class-wide physical theorem candidate; finite-mean Palm-cycle singularity plus regularity-free bounded-statistic separation.
4. **WP19:** exact resource incompleteness/no-go result.
5. **WP22/WP23:** useful structural bridge; standalone novelty downgraded by WP24.

# Immediate next gates

1. **Resolve the stationary fixed-window Fisher-rate question.** Determine whether finite recovery mean alone implies `G_DC=G_cyc`.
2. Audit random-origin/window-censored renewal likelihood theory for heavy-tailed intervals, especially `E[D]<infinity` with `E[D^2]=infinity`.
3. If finite mean is insufficient, state the weakest defensible boundary/censoring hypothesis and keep the Palm-cycle theorem separate.
4. After this gate, perform one integrated hostile proof/novelty review of WP10/WP07/WP25/WP19 before deciding whether Paper 2 has earned manuscript drafting.

# Documentation requirement

Material theorem results, proof repairs, prior-art collisions, numerical results used in arguments, and changes in next-gate decisions must be committed immediately. Keep `paper2/AGENTS_PAPER2.md` and this file synchronized with the active frontier.
