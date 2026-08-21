# AGENTS — Paper 2 General-Channel Program

## Purpose

Durable handoff for the active second-paper program in **The Universal Photodetection Resource Problem**. The repository, not chat history, is authoritative.

Active branch: `agent/uprp-core-theorem-round10`.

Paper 1 / Rev11 is scientifically frozen by default. Research remains analytical/theoretical. Do not make experiments, fabrication, procurement, or laboratory campaigns required next steps.

## Current phase

**Paper 2 has passed the manuscript threshold. A complete science draft exists.**

The active task is now **Rev2 mechanical validation, figures, and manuscript-level adversarial review**. Do not return to open-ended theorem accumulation unless drafting exposes a concrete proof defect or novelty collision.

## Read first — authoritative recovery order

1. `paper2/notes/RESEARCH_LOG_ROUND05_MANUSCRIPT_REV1_REV2.md`
2. `paper2/manuscript/fisher_spectra_memory_photodetectors_rev1.tex`
3. `paper2/manuscript/apply_rev2_science_fix.py`
4. `paper2/manuscript/paper2_refs.bib`
5. `paper2/MANUSCRIPT_ARCHITECTURE.md`
6. `paper2/notes/WP27_INTEGRATED_HOSTILE_REVIEW_AND_MANUSCRIPT_GATE.md`
7. `paper2/notes/RESEARCH_LOG_ROUND04_WP21_WP26_CHECKPOINT.md`
8. `paper2/notes/WP26_FINITE_MEAN_STATIONARY_WINDOW_FISHER_RATE.md`
9. `paper2/notes/WP25_FINITE_MEAN_CYCLE_DQM_AND_HEAVY_TAIL_HARDENING.md`
10. `paper2/notes/WP19_EXACT_VARIANCE_INSUFFICIENCY_COUNTEREXAMPLE.md`
11. `paper2/notes/WP07_CONTINUOUS_PARALYZABLE_SPECTRAL_SURVIVAL.md`
12. `paper2/notes/WP17_PUBLICATION_GRADE_WP10_FORMALIZATION.md`

WP22/WP23 are structural bridge theory. WP13–WP18/WP20 remain proof/provenance material. WP15's central pair-correlation identity is prior art and supporting only.

## Manuscript state

Working title:

> **Fisher Spectra and Information Singularities in Photodetectors with Memory**

Rev1 is the first complete science draft. It contains:

1. the general autonomous-channel Fisher-spectrum theorem;
2. deterministic Type-II static blindness with dynamic spectral escape;
3. the finite-mean random-recovery zero-IFF-deterministic theorem;
4. the exact mean+variance resource-incompleteness theorem;
5. discussion/limitations and proof appendices.

`paper2/manuscript/paper2_refs.bib` contains every citation key presently used by Rev1.

### Rev2 science fix

Rev1 contains one known notation defect: the renewal-density Laplace transform is introduced as Greek `\nu_s` while subsequent equations use Latin `u_s`.

`apply_rev2_science_fix.py` is the assertion-checked generator for Rev2. The first version of this generator accidentally replaced `\nu_s` with itself; this was caught before build verification and corrected.

The corrected generator now:

- replaces Greek `\nu_s` with Latin `u_s` exactly once;
- fails if Greek `\nu_s` survives;
- fails if the Latin `u_s` definition is absent;
- guards the mandatory distinctions `G(omega)`, `G_cyc`, and `G_DC` and the WP07 all-nonzero-frequency statement.

Treat generated Rev2 as the current manuscript once compilation is verified.

## Core theorem stack

### 1. General autonomous-channel Fisher spectrum — WP10/WP17

For homogeneous Poisson baseline `Phi0`, any parameter-independent autonomous detector channel satisfies

`S_u^out=E[S_u|Y]`,

and the induced positive contraction on `L2(R)` commutes with translations. Therefore

`F_out[u,v]=Phi0/(2*pi) int G(omega)U*(omega)V(omega)domega`,

with `0<=G<=1` a.e.

This is the organizing synthesis. Conditional-score projection, DQM, Riesz representation, and the Fourier-multiplier theorem are standard and must not be claimed as new.

### 2. Deterministic Type-II spectral escape — WP07

At `lambda*tau=1`:

- stationary homogeneous retention `G_DC=0`;
- the model-specific continuous/narrowband spectral representative has `G(omega)>0` for every `omega!=0`;
- `lim_|omega|->infinity G(omega)=1/e`;
- at `omega*tau=pi`, `G>=0.516975...`, with exact Volterra numerics about `0.52814`.

Do not conflate the universal a.e. multiplier with a primitive point value at zero. Use `G_DC` for the static experiment and narrowband/model-specific continuity for spectral statements.

### 3. Finite-mean random-recovery singularity — WP25/WP26

For iid recovery `T` with only `0<E[T]=m<infinity`, all laws share

`r(lambda)=lambda exp(-lambda m)`.

The Palm interval information satisfies

`I_D<=lambda/r`,

and

`G_cyc=(r/lambda)I_D`.

WP26 proves for the stationary timestamp record

`G_DC=G_cyc=(r/lambda)I_D`

throughout the entire finite-mean iid-recovery class, including atomic, singular, infinite-variance, and heavy-tailed laws.

At the common count maximum:

`G_DC=0 iff T=E[T] almost surely`.

Every nondegenerate recovery law also has an explicit bounded-Laplace first-order witness independent of density/variance assumptions.

### 4. Exact resource incompleteness — WP19

Two explicit recovery laws have identical

`E[T]=1`, `Var(T)=1/4`, `CV=0.5`,

and identical full conventional saturation curve, yet different timestamp information experiments.

A common interval coarse-graining has zero FI for one and positive normalized FI `~0.00443520488427` for the other. Full static FI differs by about `8.78%` numerically.

The analytic common-statistic construction is the theorem; the numerical difference is supporting calibration.

## Structural bridge — WP22/WP23/WP24

High-frequency Cesaro retention can be interpreted through zero-lag atomic timing energy in the conditional source score. Exact delayed score paths can add atomic residue, so causality alone does not imply a visible-event-fraction theorem.

WP24 found the ingredients to be strongly classical. Use this material for interpretation, not as a lead novelty claim.

## Novelty boundaries

Do **not** claim novelty for:

- generic Fisher data processing / score projection;
- function-valued FI operators;
- translation-invariant Fourier multipliers;
- point-process martingale likelihoods;
- generic renewal/window-censored renewal FI;
- random Type-II / `M/G/infinity` modeling;
- Type-II cycle transforms / busy-cycle laws;
- random-paralyzable pair correlations / generic dead-time inversion;
- generic queue-output identifiability;
- Bartlett spectra / shot-noise plateaus / Wiener-Rajchman theory;
- dead-time information theory generally;
- modulated paralyzable photocounting generally.

Keep close prior art visible: Teich/Vannucci 1978; Vannucci/Teich 1978; Teich/Cantor 1978; Dvurecenskij/Ososkov 1984 and 1985; Zhao/Nagaraja 2011; Barat/Dautremer/Trigano 2006; Jorgensen/Johnson 2026; Clark 2026; older inverse-output queue literature.

Afanaseva & Mikhailova 1973 remains an inaccessible direct Type-II-lineage historical risk. Never make a priority claim that depends on excluding it.

## Current manuscript thesis

> **A detector's conventional saturation curve is not an information-transfer law. For autonomous classical photodetection, temporal Fisher information is a property of the complete trajectory channel: deterministic Type-II paralysis can erase the static tangent while preserving every nonzero temporal mode, random recovery generically breaks that singularity despite the same mean saturation curve, and even recovery mean plus variance do not determine the information channel.**

## Verification state

Verified:

- manuscript architecture exists;
- Rev1 is a complete science draft;
- all citation keys used in Rev1 are present in `paper2_refs.bib`;
- the Rev2 notation-generator defect has been repaired and guarded;
- Paper-1 CI remains untouched;
- a separate read-only Paper-2 LaTeX workflow exists.

Not yet verified:

- successful Rev2 LaTeX/BibTeX compilation;
- compiler-warning inventory;
- rendered-page visual inspection;
- final figures.

Do **not** call Rev2 build-verified until the actual compiler result has been inspected.

## Immediate next action

1. Obtain/inspect the Paper-2 compile job by any available connector path; if unavailable, use another reproducible compilation route.
2. Patch the first genuine LaTeX/BibTeX defect, if any, through a reproducible revision step.
3. Persist generated Rev2 or a hash-pinned equivalent after successful build and record page count/warnings/artifact hash.
4. Render and visually inspect every page.
5. Replace the four figure placeholders with publication-quality figures from validated assets.
6. Perform a manuscript-level hostile review after mechanical/visual validation.

## Mandatory documentation rule

Material theorem results, proof repairs, prior-art collisions, numerical results used in arguments, or changes in manuscript strategy must be committed immediately. Keep this file and `docs/CURRENT_RESEARCH_STATE.md` synchronized.
