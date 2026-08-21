# Current Research State

**Date:** 2026-08-21

Active branch: `agent/uprp-core-theorem-round10`

## Project-level status

1. **Paper 1 / Rev11:** scientifically frozen and technically validated for Physical Review Applied; only factual/personal submission metadata remain.
2. **Paper 2:** complete Rev6 science draft exists, is locally build-verified and visually inspected, and has passed a second external adversarial review without a central mathematical failure. The only justified next revision is narrow applied-readability/scope protection (Rev7).

Do not reopen broad Paper-2 theorem exploration unless a concrete defect or serious novelty collision appears.

## Read first

1. `AGENTS.md`
2. `paper2/AGENTS_PAPER2.md`
3. `paper2/notes/REVIEW_RESPONSE_REV6_APPLIED_READABILITY_2026-08-21.md`
4. `paper2/notes/PAPER2_REV6_LOCAL_VALIDATION.md`
5. `paper2/notes/WP28_MANUSCRIPT_LEVEL_HOSTILE_REVIEW.md`
6. `paper2/notes/WP27_INTEGRATED_HOSTILE_REVIEW_AND_MANUSCRIPT_GATE.md`
7. `paper2/notes/WP26_FINITE_MEAN_STATIONARY_WINDOW_FISHER_RATE.md`
8. `paper2/notes/WP25_FINITE_MEAN_CYCLE_DQM_AND_HEAVY_TAIL_HARDENING.md`
9. `paper2/notes/WP19_EXACT_VARIANCE_INSUFFICIENCY_COUNTEREXAMPLE.md`
10. `paper2/notes/WP07_CONTINUOUS_PARALYZABLE_SPECTRAL_SURVIVAL.md`
11. `paper2/notes/WP17_PUBLICATION_GRADE_WP10_FORMALIZATION.md`
12. `paper2/MANUSCRIPT_ARCHITECTURE.md`

# Paper 1 — frozen Rev11

Preferred candidate remains Rev11. Do not reopen science absent a concrete defect or referee request.

# Paper 2 — current manuscript state

Working title:

> **Fisher Spectra and Information Singularities in Photodetectors with Memory**

Revision chain:

- Rev1 — first complete science draft;
- Rev2 — Latin `u_s` notation repair;
- Rev3 — mechanical polish and stopped-counting-process references;
- Rev4 — publication figures;
- Rev5 — manuscript-level hostile-review proof/exposition hardening;
- Rev6 — conservative queue-output prior-art positioning;
- **Rev7 planned** — technology-neutral dimensionful scale conversion, tighter scope qualifier around `complete`, and one short experimental-outlook paragraph. No theorem/data changes.

## Rev6 validation

Generated Rev6 is locally build-verified, preflighted, and visually inspected:

- 21 pages;
- all citations and cross-references resolved;
- zero overfull/underfull boxes;
- no clipping, figure spill, label collision, broken glyph, or visible hyperlink box;
- only benign `nameref` warning remains.

Generated Rev6 source SHA-256:

`ebbecd8e3d82ad7bffdb3209ab125058b1c6400733ce9ccd82ba0163ff4df2dd`

Generated Rev6 PDF SHA-256:

`9ec937f2a7352f53869c03e3af13030174d97c870855e131e7de022f49719d4e`

Details: `paper2/notes/PAPER2_REV6_LOCAL_VALIDATION.md`.

**Verification boundary:** the push-triggered GitHub Actions Rev6 run itself has not been directly inspected through the connector.

# Scientific core

## WP10/WP17 — autonomous-channel Fisher spectrum

For homogeneous Poisson baseline `Phi0`, any parameter-independent autonomous detector channel has output score

`S_u^out=E[S_u|Y]`

and a bounded translation-invariant Fisher operator on the temporal tangent completion. Hence

`F_out[u,v]=Phi0/(2*pi) int G(omega)U*(omega)V(omega)domega`,

with `0<=G<=1` a.e.

Interpret completeness only within the admitted classical Poisson weak-intensity tangent model and accessible-record definition.

## WP07 — deterministic Type-II dynamic spectral escape

At `lambda*tau=1`:

- `G_DC=0` for the homogeneous/static experiment;
- every nonzero temporal frequency has positive model-specific narrowband FI retention;
- `lim_|omega|->infinity G(omega)=1/e`;
- at `omega*tau=pi`, rigorous lower bound `0.516975...`, exact Volterra value about `0.52814`.

## WP25/WP26 — finite-mean recovery singularity

For iid recovery with only `0<E[T]=m<infinity`, all laws share

`r(lambda)=lambda exp(-lambda m)`.

For the complete stationary timestamp record,

`G_DC=G_cyc=(r/lambda)I_D`

throughout the finite-mean iid Type-II class, including atomic, singular, infinite-variance, and heavy-tailed recovery laws.

At `lambda*m=1`:

`G_DC=0 iff T=m almost surely`.

## WP19 — exact resource incompleteness

Recovery mean + variance/CV + the entire conventional mean saturation curve do not determine the timestamp information experiment. The exact common-statistic construction proves this; the ~`8.78%` complete-FI numerical difference is calibration only.

# External Rev6 review decision

The latest adversarial review was favorable overall and found no central mathematical failure. It recommended only one optional applied-significance addition and two scope/readability protections:

1. a technology-neutral dimensionful example (`tau=10 ns` -> `lambda_*=100 MHz`, `omega*tau=pi` -> `f=50 MHz`);
2. consistent qualification of `complete` to the declared classical Poisson intensity-tangent model;
3. one short experimental-outlook paragraph, explicitly not a required next step.

Do not add further recovery distributions, higher-moment no-go examples, nonparalyzable calculations, arrays, quantum extensions, thermodynamic resource theory, or simulations.

# Novelty position

No exact predecessor has been located for the combined narrow claims in WP07, WP25/WP26, and WP19. Priority is **not certified**.

Do not claim novelty for generic Fisher data processing, function-valued FI operators, translation-invariant multipliers, point-process likelihood martingales, renewal FI, random Type-II cycle laws, generic queue-output identifiability, Bartlett spectra, pair-correlation inversion, or dead-time information theory generally.

Afanaseva & Mikhailova 1973 remains an inaccessible direct Type-II-lineage historical risk.

# Immediate next actions

1. Generate Rev7 reproducibly from Rev6 with only the three review-response edits above.
2. Advance Paper-2 CI to Rev7.
3. Rebuild locally, resolve citations/references, enforce zero box overflow, and visually inspect changed pages.
4. Record Rev7 hashes/validation and freeze science again unless a concrete defect appears.

# Documentation requirement

Material theorem results, proof repairs, prior-art collisions, numerical results used in arguments, build/visual-validation changes, external review responses, or changes in manuscript strategy must be committed immediately. Keep `paper2/AGENTS_PAPER2.md` and this file synchronized.
