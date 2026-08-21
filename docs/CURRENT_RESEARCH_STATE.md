# Current Research State

**Date:** 2026-08-21

Active branch: `agent/uprp-core-theorem-round10`

## Project-level status

1. **Paper 1 / Rev11:** scientifically frozen and technically validated for Physical Review Applied; only factual/personal submission metadata remain.
2. **Paper 2 / Rev7:** preferred frozen science draft. Rev7 is locally build-verified, preflighted, source-diff inspected, and visually inspected. It incorporates the latest favorable external adversarial review without changing any theorem, proof conclusion, figure data, or numerical result.

Do not reopen broad Paper-2 theorem exploration unless a concrete defect, referee objection, or serious novelty collision appears.

## Read first

1. `AGENTS.md`
2. `paper2/AGENTS_PAPER2.md`
3. `paper2/notes/PAPER2_REV7_LOCAL_VALIDATION.md`
4. `paper2/notes/REVIEW_RESPONSE_REV6_APPLIED_READABILITY_2026-08-21.md`
5. `paper2/notes/PAPER2_REV6_LOCAL_VALIDATION.md`
6. `paper2/notes/WP28_MANUSCRIPT_LEVEL_HOSTILE_REVIEW.md`
7. `paper2/notes/WP27_INTEGRATED_HOSTILE_REVIEW_AND_MANUSCRIPT_GATE.md`
8. `paper2/notes/WP26_FINITE_MEAN_STATIONARY_WINDOW_FISHER_RATE.md`
9. `paper2/notes/WP25_FINITE_MEAN_CYCLE_DQM_AND_HEAVY_TAIL_HARDENING.md`
10. `paper2/notes/WP19_EXACT_VARIANCE_INSUFFICIENCY_COUNTEREXAMPLE.md`
11. `paper2/notes/WP07_CONTINUOUS_PARALYZABLE_SPECTRAL_SURVIVAL.md`
12. `paper2/notes/WP17_PUBLICATION_GRADE_WP10_FORMALIZATION.md`
13. `paper2/MANUSCRIPT_ARCHITECTURE.md`

# Paper 1 — frozen Rev11

Preferred candidate remains Rev11. Do not reopen science absent a concrete defect or referee request.

# Paper 2 — preferred Rev7 science draft

Working title:

> **Fisher Spectra and Information Singularities in Photodetectors with Memory**

Revision chain:

- Rev1 — first complete science draft;
- Rev2 — Latin `u_s` notation repair;
- Rev3 — mechanical polish and stopped-counting-process references;
- Rev4 — final-form publication figures;
- Rev5 — manuscript-level hostile-review proof/exposition hardening;
- Rev6 — conservative queue-output prior-art positioning;
- **Rev7 — applied-readability/scope-protection revision:** one technology-neutral dimensionful Type-II scale example, tighter scope qualifiers around `complete`, and one short future-validation paragraph. No theorem/data changes.

The dedicated Paper-2 CI now generates through Rev7 and compiles Rev7. Paper-1 CI remains untouched.

## Rev7 local validation

Validated result:

- **21 pages**;
- letter page size `612 x 792 pt`;
- all citations and cross-references resolved;
- zero overfull/underfull boxes;
- no clipping, equation/text overlap, margin overflow, figure changes, broken glyphs, or abnormal page breaks;
- only benign `nameref` warning remains;
- full 21-page render inspected;
- changed pages 8, 9, 15, and 16 inspected at readable scale.

Generated Rev7 source SHA-256:

`a317663c626a1d0597d047ec99da55f2779bc376c320ce609d7ae6ae6cce67b3`

Generated Rev7 PDF SHA-256:

`edc4ea88d644b20196ba09f77c993ed25d9fe82a0f51877b74ffe69f4daa1db2`

Rev7 source ZIP SHA-256:

`81b33249a784b7ddafe6073c9c05a57e1529245fc6b3e5a3638f5f0a7fb6378b`

Details: `paper2/notes/PAPER2_REV7_LOCAL_VALIDATION.md`.

**Verification boundary:** the actual push-triggered GitHub Actions Rev7 run has not been directly inspected through the connector.

# Scientific core

## WP10/WP17 — autonomous-channel Fisher spectrum

For homogeneous Poisson baseline `Phi0`, any parameter-independent autonomous detector channel has output score

`S_u^out=E[S_u|Y]`

and a bounded translation-invariant Fisher operator on the temporal tangent completion. Hence

`F_out[u,v]=Phi0/(2*pi) int G(omega)U*(omega)V(omega)domega`,

with `0<=G<=1` a.e.

Rev7 explicitly qualifies completeness to the admitted classical Poisson weak-intensity-waveform tangent model and stated accessible-record definition.

## WP07 — deterministic Type-II dynamic spectral escape

At `lambda*tau=1`:

- `G_DC=0` for the homogeneous/static timestamp experiment;
- every nonzero temporal frequency has positive model-specific narrowband FI retention;
- `lim_|omega|->infinity G(omega)=1/e`;
- at `omega*tau=pi`, rigorous lower bound `0.516975...`, exact Volterra value about `0.52814`.

Rev7 adds the technology-neutral scale translation:

`tau=10 ns -> lambda_*=100 MHz`,

and

`omega*tau=pi -> f=50 MHz`.

The manuscript explicitly says this does not assert that a particular detector technology realizes the ideal Type-II model.

## WP25/WP26 — finite-mean recovery singularity

For iid recovery with only `0<E[T]=m<infinity`, all laws share

`r(lambda)=lambda exp(-lambda m)`.

For the complete stationary timestamp record,

`G_DC=G_cyc=(r/lambda)I_D`

throughout the finite-mean iid Type-II class, including atomic, singular, infinite-variance, and heavy-tailed recovery laws.

At `lambda*m=1`:

`G_DC=0 iff T=m almost surely`.

## WP19 — exact resource incompleteness

Recovery mean + variance/CV + the entire conventional mean saturation curve do not determine the timestamp information experiment. The exact common-statistic construction proves this; the ~`8.78%` complete-FI numerical difference is supporting calibration only.

# Latest adversarial-review decision

The latest external adversarial review was favorable and found no central mathematical failure. Its useful recommendations have been implemented in Rev7:

1. a dimensionful Type-II scale conversion for applied readers;
2. stronger qualification of `complete` to the declared source/record model;
3. a short experimental-outlook paragraph that is explicitly not a required research step.

The review explicitly advised **against** adding more recovery families, higher-moment examples, nonparalyzable calculations, arrays, quantum-source extensions, thermodynamic resource theory, or simulations. The project adopts that recommendation.

# Novelty position

No exact predecessor has been located for the combined narrow claims in WP07, WP25/WP26, and WP19. Priority is **not certified**.

Do not claim novelty for generic Fisher data processing, function-valued FI operators, translation-invariant multipliers, point-process likelihood martingales, renewal FI, random Type-II cycle laws, generic queue-output identifiability, Bartlett spectra, pair-correlation inversion, or dead-time information theory generally.

Afanaseva & Mikhailova 1973 remains an inaccessible direct Type-II-lineage historical risk.

# Immediate next actions

Science is frozen again at Rev7 unless a concrete defect appears.

Remaining work is submission-stage:

1. inspect the actual Rev7 GitHub Actions run when connector access permits;
2. insert factual author/affiliation/correspondence/ORCID metadata;
3. add truthful funding/conflict/data-code/AI-disclosure statements as required;
4. choose/finalize target-journal formatting and submission package;
5. perform one final referee-style read after metadata are inserted.

# Documentation requirement

Material theorem results, proof repairs, prior-art collisions, numerical results used in arguments, build/visual-validation changes, external review responses, or changes in manuscript strategy must be committed immediately. Keep `paper2/AGENTS_PAPER2.md` and this file synchronized.
