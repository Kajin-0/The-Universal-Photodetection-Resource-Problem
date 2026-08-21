# AGENTS — Paper 2 General-Channel Program

## Purpose

Durable handoff for the active second-paper program in **The Universal Photodetection Resource Problem**. The repository, not chat history, is authoritative.

Active branch: `agent/uprp-core-theorem-round10`.

Paper 1 / Rev11 is scientifically frozen by default. Research remains analytical/theoretical. Do not make experiments, fabrication, procurement, or laboratory campaigns required next steps.

## Current phase

**Paper 2 has passed the manuscript threshold after WP27's integrated hostile review.**

Do not return to open-ended theorem accumulation unless a concrete manuscript defect or novelty collision appears. The active task is now **manuscript architecture and conservative drafting**.

## Read first — authoritative recovery order

1. `paper2/notes/WP27_INTEGRATED_HOSTILE_REVIEW_AND_MANUSCRIPT_GATE.md`
2. `paper2/notes/RESEARCH_LOG_ROUND04_WP21_WP26_CHECKPOINT.md`
3. `paper2/notes/WP26_FINITE_MEAN_STATIONARY_WINDOW_FISHER_RATE.md`
4. `paper2/notes/WP25_FINITE_MEAN_CYCLE_DQM_AND_HEAVY_TAIL_HARDENING.md`
5. `paper2/notes/WP19_EXACT_VARIANCE_INSUFFICIENCY_COUNTEREXAMPLE.md`
6. `paper2/notes/WP07_CONTINUOUS_PARALYZABLE_SPECTRAL_SURVIVAL.md`
7. `paper2/notes/WP17_PUBLICATION_GRADE_WP10_FORMALIZATION.md`
8. `paper2/notes/WP10_GENERAL_AUTONOMOUS_CHANNEL_THEOREM_HARDENED.md`
9. `paper2/notes/WP24_ATOMIC_SCORE_RESIDUE_PRIOR_ART_AUDIT.md`
10. `paper2/notes/WP21_HISTORICAL_INVERSE_OUTPUT_IDENTIFIABILITY_AUDIT.md`

WP22/WP23 are structural bridge theory. WP13–WP18/WP20 remain proof/provenance material. WP15's central pair-correlation identity is prior art and supporting only.

## Manuscript core

### 1. General autonomous-channel Fisher spectrum — WP10/WP17

For homogeneous Poisson source baseline `Phi0`, any parameter-independent autonomous detector channel satisfies

`S_u^out=E[S_u|Y]`,

with

`S_u=int u(t)[N(dt)-Phi0dt]`.

The induced positive contraction on `L2(R)` commutes with translations, hence

`F_out[u,v]=Phi0/(2*pi) int G(omega)U*(omega)V(omega)domega`,

`0<=G<=1` a.e.

This is the organizing photodetection-channel synthesis. The conditional-score, DQM, Riesz, and Fourier-multiplier ingredients are standard and must not be claimed as new.

### 2. Deterministic Type-II dynamic spectral escape — WP07

For deterministic paralyzable dead time `tau`, at `lambda*tau=1`:

- stationary homogeneous retention `G_DC=0`;
- the model-specific narrowband/continuous spectral representative has `G(omega)>0` for every `omega!=0`;
- `lim_|omega|->infinity G(omega)=1/e`;
- at `omega*tau=pi`, `G>=0.516975...`, while exact Volterra numerics give about `0.52814`.

Mandatory drafting repair: do not write the universal WP10 a.e. multiplier as though an infinite sinusoid or its point value at zero were primitive. Use `G_DC` for static FI and narrowband limits for finite frequency. Model-specific continuity at zero may be proved from the exact transition-score representation.

### 3. Finite-mean random-recovery singularity — WP25/WP26

For iid recovery `T` with only `0<E[T]=m<infinity`, all laws share the classical mean curve

`r(lambda)=lambda exp(-lambda m)`.

At `lambda*m=1`, every nondegenerate law has a strictly positive bounded-Laplace interval response, while deterministic recovery has zero.

The Palm-cycle interval FI satisfies

`I_D<=lambda/r`,

and

`G_cyc=(r/lambda)I_D`.

WP26 proves for the stationary timestamp window

`G_DC=G_cyc=(r/lambda)I_D`

throughout the entire finite-mean iid-recovery class, including atomic, singular, infinite-variance, and heavy-tailed laws.

Therefore at the universal count maximum:

`G_DC=0 iff T=E[T] almost surely`.

Mandatory drafting details:

- state the stopped-counting-process DQM localization theorem/citation explicitly;
- justify proper stationary forward recurrence using ergodicity/positive empty-state probability of finite-mean `M/G/infinity`;
- credit generic renewal-window FI prior art and broad random Type-II cycle transforms.

### 4. Exact resource incompleteness — WP19

Two explicit recovery laws have identical

`E[T]=1`, `Var(T)=1/4`, `CV=0.5`,

and identical full conventional saturation curve, yet different timestamp information experiments.

A common interval coarse-graining has zero FI for one law and positive normalized FI `~0.00443520488427` for the other. Full static FI differs by about `8.78%` numerically.

The analytic coarse-graining argument is the theorem; the numerical difference is supporting calibration.

## Structural bridge — WP22/WP23/WP24

The high-frequency Cesaro residue is controlled by zero-lag atomic timing energy in the conditional source score. Exact delayed score paths can add atomic residue, so causality alone does not imply visible-event fraction `r/lambda`.

WP24 found the mathematical ingredients to be strongly classical. Use this material for interpretation/connection, not as a lead novelty claim.

## Novelty/positioning boundaries

Do **not** claim novelty for:

- generic Fisher data processing or score projection;
- function-valued FI operators;
- translation-invariant Fourier multipliers;
- point-process martingale likelihoods;
- generic renewal or window-censored renewal FI;
- random Type-II / `M/G/infinity` modeling;
- Type-II cycle transforms/busy-cycle laws;
- random-paralyzable pair correlations or generic dead-time inversion;
- generic queue-output identifiability;
- Bartlett spectra / shot-noise plateaus / Wiener-Rajchman theory;
- dead-time information theory generally;
- modulated paralyzable photocounting generally.

Important close prior art to keep visible includes Teich/Vannucci 1978, Vannucci/Teich 1978, Teich/Cantor 1978, Dvurecenskij/Ososkov 1984 and 1985, Zhao/Nagaraja 2011, Barat/Dautremer/Trigano 2006, Jorgensen/Johnson 2026, Clark 2026, and the older inverse-output queue literature.

Afanaseva & Mikhailova 1973 remains an inaccessible direct Type-II-lineage historical risk. Never make a priority claim that depends on excluding it.

## Current manuscript thesis

> **A detector's conventional saturation curve is not an information-transfer law. For autonomous classical photodetection, temporal Fisher information is a property of the complete trajectory channel: deterministic Type-II paralysis can erase the static tangent while preserving every nonzero temporal mode, random recovery generically breaks that singularity despite the same mean saturation curve, and even recovery mean plus variance do not determine the information channel.**

## Immediate next action

1. Create a manuscript architecture file with title candidates, one-sentence thesis, theorem order, figure plan, appendix split, and claim/prior-art matrix.
2. Choose one primary title and a conservative abstract skeleton.
3. Only then create the LaTeX source.
4. Preserve all WP notes as provenance; do not rewrite proof history away.

## Mandatory documentation rule

Material theorem results, proof repairs, prior-art collisions, numerical results used in arguments, or changes in manuscript strategy must be committed immediately. Keep this file and `docs/CURRENT_RESEARCH_STATE.md` synchronized.
