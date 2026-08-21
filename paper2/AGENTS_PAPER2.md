# AGENTS — Paper 2 General-Channel Program

## Purpose

Durable handoff for the active second-paper program in **The Universal Photodetection Resource Problem**. The repository, not chat history, is authoritative.

Active branch: `agent/uprp-core-theorem-round10`.

Paper 1 / Rev11 is scientifically frozen by default. Research remains analytical/theoretical. Do not make experiments, fabrication, procurement, or laboratory campaigns required next steps.

## Current phase

**Paper 2 Rev7 is the preferred frozen science draft.** It is locally build-verified, preflighted, source-diff inspected, and visually inspected. Rev7 implements only the applied-readability/scope-protection changes justified by the latest external adversarial review; no theorem, proof conclusion, figure data, or numerical result changed.

Do not return to open-ended theorem accumulation unless a concrete defect, referee objection, or verified novelty collision appears.

## Read first — authoritative recovery order

1. `paper2/notes/PAPER2_REV7_LOCAL_VALIDATION.md`
2. `paper2/notes/REVIEW_RESPONSE_REV6_APPLIED_READABILITY_2026-08-21.md`
3. `paper2/notes/PAPER2_REV6_LOCAL_VALIDATION.md`
4. `paper2/notes/WP28_MANUSCRIPT_LEVEL_HOSTILE_REVIEW.md`
5. `paper2/notes/WP27_INTEGRATED_HOSTILE_REVIEW_AND_MANUSCRIPT_GATE.md`
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
17. `paper2/manuscript/apply_rev7_applied_readability.py`

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
- **Rev7 — preferred frozen science draft:** technology-neutral dimensionful Type-II scale conversion, tighter scope qualifiers around `complete`, and one short experimental-outlook paragraph. No theorem/data changes.

The dedicated Paper-2 CI now generates through Rev7 and compiles Rev7. Paper-1 CI is untouched.

## Rev7 local validation

Validated result:

- **21 pages**;
- all citations/cross-references resolved;
- zero overfull or underfull boxes;
- no clipping, equation/text overlap, margin overflow, figure changes, broken glyphs, or abnormal page breaks;
- only benign `nameref` warning remains;
- full 21-page contact sheet inspected;
- pages 8, 9, 15, and 16 inspected at readable scale because Rev7 changes text there.

Generated Rev7 source SHA-256:

`a317663c626a1d0597d047ec99da55f2779bc376c320ce609d7ae6ae6cce67b3`

Generated Rev7 PDF SHA-256:

`edc4ea88d644b20196ba09f77c993ed25d9fe82a0f51877b74ffe69f4daa1db2`

Rev7 source ZIP SHA-256:

`81b33249a784b7ddafe6073c9c05a57e1529245fc6b3e5a3638f5f0a7fb6378b`

Full details: `paper2/notes/PAPER2_REV7_LOCAL_VALIDATION.md`.

**Verification boundary:** the actual push-triggered GitHub Actions Rev7 job has not been directly inspected through the connector. Do not claim Actions-run verification until that job is read.

## Rev7 applied-readability additions

The Type-II result now includes a technology-neutral dimensional translation:

- `tau=10 ns`;
- `lambda_*=1/tau=100 MHz`;
- `omega*tau=pi` corresponds to `f=1/(2 tau)=50 MHz`;
- existing rigorous FI lower bound remains `0.516975...`;
- existing high-frequency residue remains `1/e approximately 0.3679`.

The manuscript explicitly says this is only a dimensional translation of the ideal Type-II theorem and is not a claim about a specific detector technology.

The Discussion also notes a possible future validation comparing quasi-static and finite-frequency perturbations in a genuinely paralyzable detector near `lambda*tau=1`. It explicitly states that such an experiment is not required for the analytical conclusions and is not an active project requirement.

## Core theorem stack

### 1. General autonomous-channel Fisher spectrum — WP10/WP17

For homogeneous Poisson baseline `Phi0`, any parameter-independent autonomous detector channel satisfies

`S_u^out=E[S_u|Y]`,

and the induced positive contraction on the temporal `L2` tangent completion commutes with translations. Therefore

`F_out[u,v]=Phi0/(2*pi) int G(omega)U*(omega)V(omega)domega`,

with `0<=G<=1` a.e.

Interpret completeness only within the admitted classical Poisson weak-intensity-waveform tangent model and stated accessible-record definition. Conditional-score projection, DQM, Riesz representation, and the Fourier-multiplier theorem are standard.

### 2. Deterministic Type-II spectral escape — WP07

At `lambda*tau=1`:

- stationary homogeneous retention `G_DC=0`;
- model-specific narrowband/continuous representative `G(omega)>0` for every `omega!=0`;
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

## Immediate next action

Science is frozen again at Rev7 unless a concrete defect appears.

Remaining work is submission-stage:

1. inspect the actual Rev7 GitHub Actions run when connector access permits;
2. insert factual author/affiliation/correspondence/ORCID metadata;
3. add funding/conflict/data-code/AI-disclosure statements as truthfully required;
4. choose/finalize target-journal formatting and submission package;
5. perform one final referee-style read after metadata are inserted.

Do **not** add more recovery families, higher-moment examples, nonparalyzable theory, arrays, quantum-source extensions, thermodynamic resource theory, or simulations merely to increase apparent significance.

## Mandatory documentation rule

Material theorem results, proof repairs, prior-art collisions, numerical results used in arguments, build/visual-validation changes, external review responses, or changes in manuscript strategy must be committed immediately. Keep this file and `docs/CURRENT_RESEARCH_STATE.md` synchronized.
