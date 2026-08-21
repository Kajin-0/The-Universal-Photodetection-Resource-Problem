# Current Research State

**Date:** 2026-08-21

Active branch: `agent/uprp-core-theorem-round10`

## Project-level status

1. **Paper 1 / Rev11:** scientifically frozen and technically validated for Physical Review Applied; only factual/personal submission metadata remain.
2. **Paper 2:** theorem-development phase passed WP27's integrated hostile review. A complete science manuscript draft now exists. The active phase is **Rev2 mechanical validation, figures, and manuscript-level adversarial review**.

Do not reopen broad Paper-2 theorem exploration unless the manuscript exposes a concrete defect or a serious novelty collision.

## Read first

1. `AGENTS.md`
2. `paper2/AGENTS_PAPER2.md`
3. `paper2/notes/RESEARCH_LOG_ROUND05_MANUSCRIPT_REV1_REV2.md`
4. `paper2/manuscript/fisher_spectra_memory_photodetectors_rev1.tex`
5. `paper2/manuscript/apply_rev2_science_fix.py`
6. `paper2/manuscript/paper2_refs.bib`
7. `paper2/MANUSCRIPT_ARCHITECTURE.md`
8. `paper2/notes/WP27_INTEGRATED_HOSTILE_REVIEW_AND_MANUSCRIPT_GATE.md`
9. `paper2/notes/WP26_FINITE_MEAN_STATIONARY_WINDOW_FISHER_RATE.md`
10. `paper2/notes/WP25_FINITE_MEAN_CYCLE_DQM_AND_HEAVY_TAIL_HARDENING.md`
11. `paper2/notes/WP19_EXACT_VARIANCE_INSUFFICIENCY_COUNTEREXAMPLE.md`
12. `paper2/notes/WP07_CONTINUOUS_PARALYZABLE_SPECTRAL_SURVIVAL.md`

# Paper 1 — frozen Rev11

Preferred candidate remains Rev11. Do not reopen science absent a concrete defect or referee request.

# Paper 2 — current manuscript state

Working title:

> **Fisher Spectra and Information Singularities in Photodetectors with Memory**

`paper2/manuscript/fisher_spectra_memory_photodetectors_rev1.tex` is the first complete science draft. It already contains the abstract, introduction, core theorem sequence, discussion, conclusion, and proof appendices.

A dedicated bibliography exists at `paper2/manuscript/paper2_refs.bib`. Static inspection confirms that all citation keys presently used by Rev1 are present in the bibliography.

## Rev2 science correction

Rev1 contains one known notation defect: the renewal-density Laplace transform is introduced as Greek `\nu_s` while subsequent equations use the intended Latin `u_s`.

The first version of `apply_rev2_science_fix.py` accidentally replaced `\nu_s` with itself. That generator defect was caught before build verification and has been repaired.

The corrected Rev2 generator now:

- replaces Greek `\nu_s` with Latin `u_s` exactly once;
- fails if Greek `\nu_s` remains;
- fails if the Latin `u_s` definition is missing;
- guards the mandatory distinctions `G(omega)`, `G_cyc`, `G_DC`, and the WP07 all-nonzero-frequency statement.

Generated Rev2 is the current science draft once compilation succeeds.

## Paper-2 CI

A separate read-only workflow exists at

`.github/workflows/paper2-manuscript-check.yml`.

It generates Rev2, compiles it with the same LaTeX action family used for Paper 1, checks unresolved references/citations, and uploads the manuscript artifact. The frozen Paper-1 workflow is untouched.

**Do not yet call Rev2 build-verified.** The actual push-triggered Actions job has not been inspectable through the available connector route in this session, and local container networking cannot clone GitHub.

# Scientific core

## WP10/WP17 — autonomous-channel Fisher spectrum

For homogeneous Poisson baseline `Phi0`, any parameter-independent autonomous detector channel has output score

`S_u^out=E[S_u|Y]`

and a bounded translation-invariant Fisher operator. Hence

`F_out[u,v]=Phi0/(2*pi) int G(omega)U*(omega)V(omega)domega`,

with `0<=G<=1` a.e.

The statistical and harmonic-analysis ingredients are standard; the contribution is the detector-channel synthesis and consequences.

## WP07 — deterministic Type-II dynamic spectral escape

At `lambda*tau=1`:

- stationary homogeneous retention `G_DC=0`;
- every nonzero temporal frequency has positive model-specific narrowband FI retention;
- `lim_|omega|->infinity G(omega)=1/e`;
- at `omega*tau=pi`, a rigorous lower bound is `0.516975...`, with exact numerical validation about `0.52814`.

The manuscript must keep the a.e. universal spectrum separate from the model-specific continuous/narrowband representative and from static `G_DC`.

## WP25/WP26 — finite-mean recovery singularity

For iid recovery with only `0<E[T]=m<infinity`, all laws share

`r(lambda)=lambda exp(-lambda m)`.

WP25 gives finite Palm-cycle FI and regularity-free bounded-statistic separation. WP26 proves the stationary long-window equality

`G_DC=G_cyc=(r/lambda)I_D`

for the entire finite-mean iid Type-II class, including atomic, singular, infinite-variance, and heavy-tailed recovery laws.

At `lambda*m=1`:

`G_DC=0 iff T=m almost surely`.

## WP19 — exact resource incompleteness

Two explicit recovery laws have identical mean, variance/CV, and identical full conventional saturation curve but different timestamp information experiments. The analytic common-statistic construction is the theorem; the approximately `8.78%` complete-FI difference is supporting numerical calibration.

## WP22/WP23/WP24 — structural bridge

Conditional-score atomic timing energy gives useful high-frequency interpretation. WP24 found the ingredients strongly classical, so this material is not a standalone novelty pillar.

# Novelty position

No exact predecessor has been located for the combined narrow claims in WP07, WP25/WP26, and WP19. Priority is **not certified**.

Do not claim novelty for generic Fisher data processing, function-valued FI operators, translation-invariant multipliers, point-process likelihood martingales, renewal FI, random Type-II cycle laws, generic queue-output identifiability, Bartlett spectra, pair-correlation inversion, or dead-time information theory generally.

Afanaseva & Mikhailova 1973 remains an inaccessible direct Type-II-lineage historical risk. Never make a priority claim that depends on excluding it.

# Current thesis

> A conventional detector saturation curve is not an information-transfer law. For autonomous classical photodetection, information belongs to the complete trajectory channel: deterministic Type-II paralysis can erase a static source tangent while preserving every nonzero temporal mode; random recovery generically destroys that singularity despite the same mean saturation curve; and even recovery mean plus variance do not determine the timestamp information channel.

# Immediate next actions

1. Inspect the actual Paper-2 compile job if a connector route becomes available; otherwise use another reproducible compile path.
2. Patch the first genuine LaTeX/BibTeX defect, if any, through a reproducible revision step.
3. Persist/hash-pin generated Rev2 after successful build and record page count, warnings, and artifact hash.
4. Render and visually inspect all pages.
5. Replace four figure placeholders with publication-quality figures based on validated theoretical/numerical assets.
6. Perform a manuscript-level hostile review after mechanical and visual validation.

# Documentation requirement

Material theorem results, proof repairs, prior-art collisions, numerical results used in arguments, or changes in manuscript strategy must be committed immediately. Keep `paper2/AGENTS_PAPER2.md` and this file synchronized.
