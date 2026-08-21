# Current Research State

**Date:** 2026-08-21

Active branch: `agent/uprp-core-theorem-round10`

## Project-level status

1. **Paper 1 / Rev11:** scientifically frozen and technically validated for Physical Review Applied; only factual/personal submission metadata remain.
2. **Paper 2:** theorem-development phase passed WP27's integrated hostile review. A complete manuscript draft exists. Generated **Rev3 is locally build-verified and visually inspected**. The active phase is publication figures followed by manuscript-level adversarial review.

Do not reopen broad Paper-2 theorem exploration unless the manuscript exposes a concrete defect or serious novelty collision.

## Read first

1. `AGENTS.md`
2. `paper2/AGENTS_PAPER2.md`
3. `paper2/notes/PAPER2_REV3_LOCAL_VALIDATION.md`
4. `paper2/notes/RESEARCH_LOG_ROUND05_MANUSCRIPT_REV1_REV2.md`
5. `paper2/MANUSCRIPT_ARCHITECTURE.md`
6. `paper2/manuscript/fisher_spectra_memory_photodetectors_rev1.tex`
7. `paper2/manuscript/apply_rev2_science_fix.py`
8. `paper2/manuscript/apply_rev3_mechanical_polish.py`
9. `paper2/manuscript/paper2_refs.bib`
10. `paper2/notes/WP27_INTEGRATED_HOSTILE_REVIEW_AND_MANUSCRIPT_GATE.md`
11. `paper2/notes/WP26_FINITE_MEAN_STATIONARY_WINDOW_FISHER_RATE.md`
12. `paper2/notes/WP25_FINITE_MEAN_CYCLE_DQM_AND_HEAVY_TAIL_HARDENING.md`
13. `paper2/notes/WP19_EXACT_VARIANCE_INSUFFICIENCY_COUNTEREXAMPLE.md`
14. `paper2/notes/WP07_CONTINUOUS_PARALYZABLE_SPECTRAL_SURVIVAL.md`

# Paper 1 — frozen Rev11

Preferred candidate remains Rev11. Do not reopen science absent a concrete defect or referee request.

# Paper 2 — manuscript state

Working title:

> **Fisher Spectra and Information Singularities in Photodetectors with Memory**

Revision chain:

- Rev1 — first complete science draft;
- Rev2 — assertion-checked `\nu_s` -> Latin `u_s` science notation repair;
- Rev3 — assertion-checked mechanical polish: hidden hyperlink boxes, internal drafting-language removal, and explicit stopped-counting-process likelihood references.

The dedicated Paper-2 CI generates Rev2 then Rev3 and compiles Rev3. Paper-1 CI is untouched.

## Local Rev3 validation

A clean local `latexmk`/pdfLaTeX build of generated Rev3 succeeded. Because the container's `bibtex` alternative was broken, installed `bibtex8` was used through a PATH shim. This was only a local environment workaround.

Validated result:

- **19 pages**;
- all citations and cross-references resolved;
- no overfull or underfull boxes;
- only remaining warning: benign `nameref` label-definition warning;
- all 19 pages rendered and inspected;
- no clipping, overlap, broken glyphs, black boxes, or margin overflow;
- hyperlink boxes removed in Rev3.

Hashes and validation details are recorded in `paper2/notes/PAPER2_REV3_LOCAL_VALIDATION.md`.

**Verification boundary:** Rev3 is locally build-verified and visually inspected. The branch push-triggered GitHub Actions run itself has not been directly inspected through the available connector in this session.

The four figure placeholders are now the principal mechanical/publication-quality deficiency.

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
- at `omega*tau=pi`, rigorous lower bound `0.516975...`, exact numerical validation about `0.52814`.

The manuscript correctly separates the a.e. universal spectrum, model-specific continuous/narrowband representation, and static `G_DC`.

## WP25/WP26 — finite-mean recovery singularity

For iid recovery with only `0<E[T]=m<infinity`, all laws share

`r(lambda)=lambda exp(-lambda m)`.

WP25 gives finite Palm-cycle FI and regularity-free bounded-statistic separation. WP26 proves

`G_DC=G_cyc=(r/lambda)I_D`

for the entire finite-mean iid Type-II class, including atomic, singular, infinite-variance, and heavy-tailed recovery laws.

At `lambda*m=1`:

`G_DC=0 iff T=m almost surely`.

Rev3 now cites standard counting-process likelihood/point-process references for the stopped-martingale localization.

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

1. Replace Figure 1 placeholder with a clean trajectory-channel versus saturation-curve conceptual diagram.
2. Replace Figure 2 placeholder with the validated deterministic Type-II exact-spectrum / rigorous-lower-bound plot.
3. Replace Figure 3 placeholder with the shared saturation curve plus deterministic/random static-FI comparison.
4. Replace Figure 4 placeholder with the exact mean/variance-matched recovery counterexample.
5. Rebuild and visually re-inspect after figures are inserted.
6. Perform a manuscript-level hostile review of proof handoffs, novelty language, significance, exposition, and figure accuracy.
7. Only after that decide whether another science revision is justified.

# Documentation requirement

Material theorem results, proof repairs, prior-art collisions, numerical results used in arguments, build/visual-validation changes, or changes in manuscript strategy must be committed immediately. Keep `paper2/AGENTS_PAPER2.md` and this file synchronized.
