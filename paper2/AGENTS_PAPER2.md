# AGENTS — Paper 2 General-Channel Program

## Purpose

Durable handoff for the active second-paper program in **The Universal Photodetection Resource Problem**. The repository, not chat history, is authoritative.

Active branch: `agent/uprp-core-theorem-round10`.

Paper 1 / Rev11 is scientifically frozen by default. Research remains analytical/theoretical. Do not make experiments, fabrication, procurement, or laboratory campaigns required next steps.

## Current phase

**Paper 2 has a complete science draft and generated Rev3 is locally build-verified and visually inspected.**

The active task is now **publication figures followed by a manuscript-level hostile review**. Do not return to open-ended theorem accumulation unless drafting exposes a concrete proof defect or novelty collision.

## Read first — authoritative recovery order

1. `paper2/notes/PAPER2_REV3_LOCAL_VALIDATION.md`
2. `paper2/notes/RESEARCH_LOG_ROUND05_MANUSCRIPT_REV1_REV2.md`
3. `paper2/MANUSCRIPT_ARCHITECTURE.md`
4. `paper2/manuscript/fisher_spectra_memory_photodetectors_rev1.tex`
5. `paper2/manuscript/apply_rev2_science_fix.py`
6. `paper2/manuscript/apply_rev3_mechanical_polish.py`
7. `paper2/manuscript/paper2_refs.bib`
8. `paper2/notes/WP27_INTEGRATED_HOSTILE_REVIEW_AND_MANUSCRIPT_GATE.md`
9. `paper2/notes/WP26_FINITE_MEAN_STATIONARY_WINDOW_FISHER_RATE.md`
10. `paper2/notes/WP25_FINITE_MEAN_CYCLE_DQM_AND_HEAVY_TAIL_HARDENING.md`
11. `paper2/notes/WP19_EXACT_VARIANCE_INSUFFICIENCY_COUNTEREXAMPLE.md`
12. `paper2/notes/WP07_CONTINUOUS_PARALYZABLE_SPECTRAL_SURVIVAL.md`
13. `paper2/notes/WP17_PUBLICATION_GRADE_WP10_FORMALIZATION.md`

WP22/WP23 are structural bridge theory. WP13–WP18/WP20 remain proof/provenance material. WP15's central pair-correlation identity is prior art and supporting only.

## Manuscript state

Working title:

> **Fisher Spectra and Information Singularities in Photodetectors with Memory**

Revision chain:

- Rev1: first complete science draft.
- Rev2: assertion-checked repair of Greek `\nu_s` versus intended Latin `u_s`.
- Rev3: assertion-checked mechanical polish: hidden hyperlink boxes, removal of internal drafting language, and explicit counting-process likelihood references.

The separate Paper-2 CI workflow generates Rev2 then Rev3 and compiles Rev3. The frozen Paper-1 CI is untouched.

## Rev3 local validation

A clean local `latexmk`/pdfLaTeX build of generated Rev3 succeeded. The local environment's `bibtex` alternative was broken, so installed `bibtex8` was used through a PATH shim; this is an environment workaround only.

Result:

- 19 pages;
- all citations/cross-references resolved;
- no overfull or underfull boxes;
- only warning is the benign `nameref` label-definition warning;
- rendered 19-page contact sheet shows no clipping, overlap, broken glyphs, or margin overflow.

Hashes from the locally validated generation are recorded in `PAPER2_REV3_LOCAL_VALIDATION.md`.

**Verification boundary:** Rev3 is locally build-verified and visually inspected, but the branch push-triggered GitHub Actions run itself has not been directly inspected through the connector in this session.

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

WP24 found the ingredients strongly classical. Use this material for interpretation, not as a lead novelty claim.

## Novelty boundaries

Do **not** claim novelty for generic Fisher data processing/score projection, function-valued FI operators, translation-invariant multipliers, point-process martingale likelihoods, generic renewal/window-censored renewal FI, random Type-II / `M/G/infinity` modeling, Type-II cycle transforms/busy-cycle laws, random-paralyzable pair correlations, generic queue-output identifiability, Bartlett spectra, Wiener/Rajchman theory, or dead-time information theory generally.

Keep close prior art visible: Teich/Vannucci 1978; Vannucci/Teich 1978; Teich/Cantor 1978; Dvurecenskij/Ososkov 1984 and 1985; Zhao/Nagaraja 2011; Barat/Dautremer/Trigano 2006; Jorgensen/Johnson 2026; Clark 2026; Andersen/Borgan/Gill/Keiding 1993; Jacobsen 2006; older inverse-output queue literature.

Afanaseva & Mikhailova 1973 remains an inaccessible direct Type-II-lineage historical risk. Never make a priority claim that depends on excluding it.

## Current manuscript thesis

> **A detector's conventional saturation curve is not an information-transfer law. For autonomous classical photodetection, temporal Fisher information is a property of the complete trajectory channel: deterministic Type-II paralysis can erase the static tangent while preserving every nonzero temporal mode, random recovery generically breaks that singularity despite the same mean saturation curve, and even recovery mean plus variance do not determine the information channel.**

## Immediate next action

1. Replace Figure 1 placeholder with a clean conceptual trajectory-channel versus saturation-curve diagram.
2. Replace Figure 2 placeholder with the validated deterministic Type-II exact-spectrum / rigorous-lower-bound plot.
3. Replace Figure 3 placeholder with the common saturation curve plus deterministic/random static-FI comparison.
4. Replace Figure 4 placeholder with the exact mean/variance-matched recovery counterexample.
5. Rebuild and re-render after figure insertion.
6. Perform a manuscript-level hostile review of proof handoffs, novelty language, significance, exposition, and figure accuracy.
7. Only after that decide whether another science revision is justified.

## Mandatory documentation rule

Material theorem results, proof repairs, prior-art collisions, numerical results used in arguments, build/visual-validation changes, or changes in manuscript strategy must be committed immediately. Keep this file and `docs/CURRENT_RESEARCH_STATE.md` synchronized.
