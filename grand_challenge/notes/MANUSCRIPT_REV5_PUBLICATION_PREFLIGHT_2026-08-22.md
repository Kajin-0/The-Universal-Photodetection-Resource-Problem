# Grand Challenge Manuscript Rev5 — Publication Preflight

**Date:** 2026-08-22

**Scientific checkpoint:** WP24 integrated hostile review PASS

**Preferred science content:** unchanged from Rev4

**Preferred publication draft:** **Rev5**

**Status:** **Locally build-verified, bibliography-resolved, visually inspected, and publication-preflight passed.** Rev5 adds one conceptual figure and nonintrusive hyperlink styling only; it changes no theorem, equation, numerical coefficient, source-class hypothesis, or novelty claim.

---

## 1. Deterministic generation chain

Rev5 is generated from the committed base manuscript by:

1. `energy_survival_temporal_fisher_rev1.tex`
2. `apply_rev2_mechanical.py` -> Rev2
3. `apply_rev3_hostile_review.py` -> Rev3
4. `apply_rev4_final_polish.py` -> Rev4
5. `apply_rev5_publication_figure.py` -> Rev5

Figure source:

`figure1_operational_architecture_body.tex`

Dedicated workflow:

`.github/workflows/grand-challenge-manuscript-check.yml`

The workflow now targets Rev5 and also runs the deterministic numerical theorem validator before compilation.

---

## 2. Exact final local build

The final Rev5 source was regenerated from the latest committed Rev3 -> Rev4 -> Rev5 transformations, using the corrected bibliography.

Build sequence:

`pdflatex -> /usr/bin/bibtex.original -> pdflatex -> pdflatex`

The local `/usr/bin/bibtex` alternatives link is broken, so `/usr/bin/bibtex.original` was used directly. This is an environment issue; the executable is the normal BibTeX binary.

Final output:

- pages: **7**;
- page size: **US Letter, 612 x 792 pt**;
- final PDF size: **393,530 bytes**;
- unresolved citations/references: **0**;
- overfull `hbox`: **0**;
- overfull `vbox`: **0**;
- undefined controls/fatal TeX errors: **0**;
- generated `boxed{...}` markup: **0**;
- `hyperref` mode: `hidelinks`.

BibTeX emitted only the REVTeX style's internal `jnrlst ... set 1` warning; bibliography generation and all citations completed correctly.

---

## 3. Visual verification

The final Rev5 PDF was rendered with the repository PDF verification tool at **160 dpi** and all seven pages were visually inspected.

### Overall

PASS:

- no clipped text;
- no equation overlap;
- no broken glyphs;
- no page-number collision;
- no overfull visual spill;
- no red/cyan hyperlink rectangles;
- no bibliography-link decoration;
- no figure/caption collision.

### Figure 1

Figure 1 appears at the top of page 3 as a two-column-width schematic and is readable without increasing the manuscript page count.

It shows the full theorem architecture:

1. latent random-time law `p_epsilon(t)` and Fourier mode `k`;
2. fixed excitation / encoded state and energy tail `T_k`;
3. arbitrary parameter-independent source-to-field/detector channel `Gamma`;
4. accessible POVM record / Fisher block;
5. operational law
   `R_N(k) <= min(D_k,U_k) <= T_k`;
6. controlled-limit continuum law
   `R(nu)<=P(Omega>=nu)` and `Ebar^+>=hbar nu R(nu)`;
7. explicit excluded class: parameter-dependent waveform-state synthesis.

The figure therefore earns its space: it compresses the source-class boundary and downstream-data-processing logic into one immediately visible object. It is not decorative.

### Bibliography page

Page 7 is clean after `hidelinks`:

- no colored link boxes;
- corrected Pocovnicu title renders correctly;
- Gill published chapter entry fits without overflow;
- all ten references resolve.

---

## 4. Publication-only changes from Rev4

Rev5 changes only presentation:

1. adds `graphicx` and `tikz` for Figure 1;
2. adds `\hypersetup{hidelinks}`;
3. inserts the operational-architecture figure after the Introduction;
4. includes a caption that restates the theorem scope conservatively.

No mathematical or scientific text outside the figure/caption is altered by the Rev5 generator.

---

## 5. CI hardening

The Rev5 CI workflow now explicitly:

- installs Python 3.12;
- installs NumPy;
- generates Rev2, Rev3, Rev4, and Rev5 in order;
- runs `grand_challenge/numerics/verify_operational_tail_bound.py`;
- compiles Rev5;
- fails on unresolved citations/references;
- fails on overfull boxes;
- fails if literal `\boxed{` markup remains;
- uploads Rev1--Rev5 sources, generators, bibliography, figure source, numerical validator, and Rev5 PDF.

The available GitHub connector does not expose the relevant branch-push workflow run, so this note does **not** claim direct remote Actions inspection. The equivalent final local build has been reproduced and inspected.

---

## 6. Science status remains frozen

Rev5 introduces no new scientific result. The governing science record remains:

- WP20: direct arbitrary finite-copy joint-POVM Fisher-tail proof;
- WP22: controlled large-period continuum survival law;
- WP23: independent compound-Poisson to bosonic-field channel embedding;
- WP24: integrated hostile review / prior-art boundary PASS;
- Rev4: final science/claim hardening;
- Rev5: publication-only figure and link-style pass.

The strongest claim remains:

> In the exact periodic random-time statistical experiment, every finite-copy joint measurement has a two-quadrature Fisher trace bounded by paired energy-sector population and hence by the upper excitation-energy tail; controlled large-period limits inherit the survival-function and mean-energy resource laws.

Priority remains **unverified, not certified**.

---

## 7. Decision

**Rev5 is now the preferred frozen publication draft.**

Reopen the science or create Rev6 only for a concrete reason:

1. theorem/proof defect;
2. historical-priority collision;
3. build or rendering defect;
4. referee-level clarity objection;
5. factual submission requirement that cannot be handled without source change.

Do not create another revision merely to accumulate polish.

The next work is submission engineering rather than theorem accumulation: remote CI inspection if it becomes accessible, journal targeting/format checks, and factual author/funding/disclosure metadata when supplied.
