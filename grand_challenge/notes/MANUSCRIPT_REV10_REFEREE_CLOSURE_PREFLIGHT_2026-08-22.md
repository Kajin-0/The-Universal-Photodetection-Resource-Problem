# Manuscript Rev10 referee-closure preflight

**Date:** 2026-08-22

**Manuscript:** *Spectral Resource Laws for Temporal Fisher Information*

**Status:** local publication gate PASS; Rev10 is the preferred PRX Quantum manuscript.

## Scientific delta from Rev9

Rev10 responds directly to the extreme adversarial Rev9 re-review. The review found no central mathematical failure and identified two mandatory-looking precision repairs plus one optional high-value significance opportunity.

Rev10 implements all three:

1. the continuum Herglotz extension invokes Bochner only when the controlled limit is normalized positive definite **and continuous at the origin**;
2. the Discussion and theorem hierarchy consistently identify the Herglotz/high-retention law as a **fixed one-copy common-POVM** result, distinct from the arbitrary finite-copy collective-measurement tail theorem;
3. a finite-chain sine-profile family proves that the near-lossless `(1-R)^(-1/2)` energy-divergence exponent is sharp.

No coefficient, hypothesis, or proof in the original finite-copy Fisher-tail theorem was altered.

## Sharp-exponent result

For

`a_n=sqrt(2/(L+1)) sin((n+1)pi/(L+1))`, `n=0,...,L-1`,

canonical phase measurement gives exactly

`R_L(1)=cos^2(pi/(L+1))`,

`nbar_L=(L-1)/2`.

Therefore

`nbar_L = pi/[2 arccos sqrt(R_L(1))] - 1`

and

`nbar_L ~ pi/[2 sqrt(1-R_L(1))]`.

Combined with the universal fixed-one-copy/common-measurement lower law

`nbar >= A(R) ~ 1/sqrt(2(1-R))`,

this proves that the inverse-square-root divergence exponent is optimal. The global asymptotic prefactor remains open and is **not claimed**.

Finite sine states are established phase-estimation prior art (Berry--Wiseman 2000); Rev10 uses them only as an achievability witness for the new retention--energy law.

## Deterministic source reconstruction check

The preserved Rev8 source package was combined with the committed Rev9 spectral-theory transformation, compressed-abstract pass, Rev9 theorem/figure inputs, and Rev10 referee-closure transformation.

Before evaluating Rev10, the reconstructed Rev9 was compiled and visually compared against the previously frozen Rev9 PDF using the PDF render-diff workflow at 120 dpi.

Result:

- pages compared: **11**;
- changed pages: **0**;
- pixel-change percentage on every page: **0.0%**.

Thus the local source reconstruction reproduces the frozen Rev9 layout exactly; differing PDF binary hashes are attributable to PDF build metadata rather than content/layout.

## Rev10 full build

Build sequence:

`pdflatex -> /usr/bin/bibtex.original -> pdflatex -> pdflatex`.

Result:

- build: **PASS**;
- pages: **11**;
- PDF file size: **444,063 bytes**;
- unresolved references/citations: **0**;
- overfull hbox/vbox: **0**;
- fatal/undefined controls: **0**;
- PDF opens normally and is not encrypted/XFA/scanned.

Final PDF SHA-256:

`a5c2d9e12bba045b76bbfb710428e5424e2c5cb5eb83d6aec6215a5996dbc6fb`

## Visual inspection

The final PDF was rendered at 200 dpi using the project PDF workflow.

All **11 pages** were inspected. No clipping, overlaps, broken glyphs, malformed equations, or figure failures were observed.

Particular attention was given to:

- page 1: compact abstract now includes the sharp-exponent statement without layout crowding;
- page 6: Corollary 3, Proposition 1, sine-profile equations, proof continuation, and Bochner continuity-at-origin wording;
- pages 6--8: transition from the sharpness proposition into the complete-extremizer theorem;
- page 11: Berry--Wiseman and the expanded bibliography render cleanly.

Visual gate: **PASS**.

## New numerical validator

`grand_challenge/numerics/verify_sine_profile_divergence_sharpness.py`

checks normalization, adjacent-overlap identity, mean excitation, compatibility with the universal Herglotz/tail bound, and the limits

`nbar sqrt(1-R) -> pi/2`,

`(1-R)nbar^2 -> pi^2/4`.

Local result: **PASS**.

## Source package

A minimal self-contained Rev10 source package contains:

- `energy_survival_temporal_fisher_rev10_prxq.tex`;
- `rev10_spectral_theorems.tex`;
- `figure1_operational_architecture_body_rev9.tex`;
- `references.bib`;
- `apply_rev10_referee_closure.py`;
- `verify_sine_profile_divergence_sharpness.py`;
- source README.

Local source ZIP SHA-256:

`cfa2452f9ce4e99d0cd56f931151f6bb166fd90d4332d86faf3ea2485dec1db9`

## CI status

The dedicated branch workflow has been advanced to Rev10 and includes the proposition environment, all five validators, LaTeX compilation, and explicit regression gates for:

- continuity at the origin before Bochner;
- fixed one-copy/common-POVM scope;
- sharp-exponent proposition;
- local-Fisher scope;
- exclusion of the previously rejected recycled positive-cosine-lobe claim.

The current GitHub connector does not expose branch-push workflow runs through its available run lookup, so no direct remote-run result is claimed here. The full equivalent generation/build/render gate was executed locally and passed.

## Freeze decision

**Freeze Rev10 as the preferred PRX Quantum manuscript.**

Do not start a prefactor-optimization project, add another example, or broaden the source class by default. Reopen only for a concrete theorem defect, priority collision, build/journal-format problem, or a new referee-level objection.
