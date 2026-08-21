# AGENTS — Paper 2 General-Channel Program

## Purpose

Durable handoff for the active second-paper program in **The Universal Photodetection Resource Problem**. The repository, not chat history, is authoritative.

Active branch: `agent/uprp-core-theorem-round10`.

Paper 1 / Rev11 is scientifically frozen by default. Research remains analytical/theoretical. Do not make experiments, fabrication, procurement, or laboratory campaigns required next steps.

## Current phase

**Paper 2 has a complete, locally build-verified Rev6 science draft.** A new external adversarial review found no central mathematical failure and recommended only minor applied-readability/scope-protection changes.

The active task is therefore **Rev7 applied polish**, not theorem accumulation.

## Read first — authoritative recovery order

1. `paper2/notes/REVIEW_RESPONSE_REV6_APPLIED_READABILITY_2026-08-21.md`
2. `paper2/notes/PAPER2_REV6_LOCAL_VALIDATION.md`
3. `paper2/notes/WP28_MANUSCRIPT_LEVEL_HOSTILE_REVIEW.md`
4. `paper2/notes/WP27_INTEGRATED_HOSTILE_REVIEW_AND_MANUSCRIPT_GATE.md`
5. `paper2/notes/RESEARCH_LOG_ROUND04_WP21_WP26_CHECKPOINT.md`
6. `paper2/notes/WP26_FINITE_MEAN_STATIONARY_WINDOW_FISHER_RATE.md`
7. `paper2/notes/WP25_FINITE_MEAN_CYCLE_DQM_AND_HEAVY_TAIL_HARDENING.md`
8. `paper2/notes/WP19_EXACT_VARIANCE_INSUFFICIENCY_COUNTEREXAMPLE.md`
9. `paper2/notes/WP07_CONTINUOUS_PARALYZABLE_SPECTRAL_SURVIVAL.md`
10. `paper2/notes/WP17_PUBLICATION_GRADE_WP10_FORMALIZATION.md`
11. `paper2/MANUSCRIPT_ARCHITECTURE.md`
12. `paper2/manuscript/apply_rev2_science_fix.py`
13. `paper2/manuscript/apply_rev3_mechanical_polish.py`
14. `paper2/manuscript/apply_rev4_figures.py`
15. `paper2/manuscript/apply_rev5_hostile_review.py`
16. `paper2/manuscript/apply_rev6_prior_art_positioning.py`

WP22/WP23 are structural bridge theory. WP13–WP18/WP20 remain proof/provenance material. WP15's pair-correlation identity is prior art and supporting only.

## Manuscript state

Working title:

> **Fisher Spectra and Information Singularities in Photodetectors with Memory**

Revision chain:

- Rev1 — first complete science draft.
- Rev2 — `nu_s` / intended Latin `u_s` notation repair.
- Rev3 — mechanical polish, hidden hyperlinks removed, internal drafting language removed, stopped-counting-process references added.
- Rev4 — all four publication figures inserted and visually repaired.
- Rev5 — manuscript-level hostile-review hardening: `L2` extension wording, self-contained Volterra equations, stationary-window domination, removal of internal repository wording.
- Rev6 — conservative queue-output prior-art positioning using Daley (1976).
- **Rev7 planned** — dimensionful Type-II scale conversion, tighter scope qualifiers around `complete`, and one short experimental-outlook sentence. No theorem/data changes.

The dedicated Paper-2 CI generates the revision chain and currently compiles through Rev6. Paper-1 CI is untouched.

## Rev6 validation

Rev6 is locally build-verified and visually inspected:

- 21 pages;
- all citations/cross-references resolved;
- zero overfull or underfull boxes;
- no clipping, figure spill, label collisions, broken glyphs, or hyperlink boxes;
- only benign `nameref` label-definition warning remains.

Generated Rev6 source SHA-256:

`ebbecd8e3d82ad7bffdb3209ab125058b1c6400733ce9ccd82ba0163ff4df2dd`

Generated Rev6 PDF SHA-256:

`9ec937f2a7352f53869c03e3af13030174d97c870855e131e7de022f49719d4e`

Full validation details: `paper2/notes/PAPER2_REV6_LOCAL_VALIDATION.md`.

**Verification boundary:** the actual push-triggered GitHub Actions Rev6 job has not been directly inspected through the connector. Do not claim Actions-run verification until that job is read.

## Core theorem stack

### 1. General autonomous-channel Fisher spectrum — WP10/WP17

For homogeneous Poisson baseline `Phi0`, any parameter-independent autonomous detector channel satisfies

`S_u^out=E[S_u|Y]`,

and the induced positive contraction on the temporal `L2` tangent completion commutes with translations. Therefore

`F_out[u,v]=Phi0/(2*pi) int G(omega)U*(omega)V(omega)domega`,

with `0<=G<=1` a.e.

The conditional-score, DQM, Riesz, and Fourier-multiplier ingredients are standard. Contribution = photodetection-channel synthesis and consequences.

### 2. Deterministic Type-II spectral escape — WP07

At `lambda*tau=1`:

- stationary homogeneous retention `G_DC=0`;
- the model-specific narrowband/continuous representative has `G(omega)>0` for every `omega!=0`;
- `lim_|omega|->infinity G(omega)=1/e`;
- at `omega*tau=pi`, rigorous lower bound `0.516975...`, exact Volterra value about `0.52814`.

Keep `G_DC` distinct from the a.e. general multiplier.

### 3. Finite-mean random-recovery singularity — WP25/WP26

For iid recovery `T` with only `0<E[T]=m<infinity`, all laws share

`r(lambda)=lambda exp(-lambda m)`.

The complete stationary timestamp record obeys

`G_DC=G_cyc=(r/lambda)I_D`

throughout the full finite-mean iid-recovery class, including atomic, singular, infinite-variance, and heavy-tailed laws.

At the common count maximum:

`G_DC=0 iff T=E[T] almost surely`.

Every nondegenerate law also has an explicit bounded-Laplace first-order witness.

### 4. Exact resource incompleteness — WP19

Two recovery laws have identical mean, variance/CV, and identical full conventional saturation curve but different timestamp information experiments. The analytic common-statistic construction is the theorem; the approximately `8.78%` full-FI difference is supporting numerical calibration.

## Novelty boundaries

Do **not** claim novelty for generic Fisher data processing/score projection, function-valued FI operators, translation-invariant multipliers, point-process likelihood martingales, generic renewal/window-censored renewal FI, random Type-II / `M/G/infinity` modeling, Type-II cycle transforms/busy-cycle laws, random-paralyzable pair correlations, generic queue-output identifiability, Bartlett spectra, Wiener/Rajchman theory, or dead-time information theory generally.

Keep close prior art visible: Teich/Vannucci 1978; Vannucci/Teich 1978; Teich/Cantor 1978; Dvurecenskij/Ososkov 1984 and 1985; Zhao/Nagaraja 2011; Barat/Dautremer/Trigano 2006; Jorgensen/Johnson 2026; Clark 2026; Andersen/Borgan/Gill/Keiding 1993; Jacobsen 2006; Daley 1976; older inverse-output queue literature.

Afanaseva & Mikhailova 1973 remains an inaccessible direct Type-II-lineage historical risk. Never make a priority claim that depends on excluding it.

## Current manuscript thesis

> **A detector's conventional saturation curve is not an information-transfer law. Within the admitted classical Poisson weak-intensity waveform model, temporal Fisher information is a property of the full accessible trajectory channel: deterministic Type-II paralysis can erase the static tangent while preserving every nonzero temporal mode, random recovery generically breaks that singularity despite the same mean saturation curve, and even recovery mean plus variance do not determine the information channel.**

## Immediate next action — Rev7 only

1. Generate Rev7 reproducibly from Rev6.
2. Add one technology-neutral scale example: `tau=10 ns` -> `lambda_*=100 MHz`, `omega*tau=pi` -> `f=50 MHz`, with the existing rigorous FI bound `0.516975...`.
3. Tighten `complete` terminology to the admitted classical Poisson intensity-tangent/access-record scope.
4. Add one short experimental-outlook paragraph; do not make experiments a required next step.
5. Update CI to generate/compile Rev7.
6. Rebuild and visually inspect affected pages.
7. Freeze science again unless a concrete defect appears.

Do **not** add more recovery families, higher-moment examples, nonparalyzable theory, arrays, quantum-source extensions, thermodynamic resource theory, or simulations.

## Mandatory documentation rule

Material theorem results, proof repairs, prior-art collisions, numerical results used in arguments, build/visual-validation changes, external review responses, or changes in manuscript strategy must be committed immediately. Keep this file and `docs/CURRENT_RESEARCH_STATE.md` synchronized.
