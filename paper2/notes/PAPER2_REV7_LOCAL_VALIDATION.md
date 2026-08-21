# Paper 2 Rev7 — Local build and visual validation

**Date:** 2026-08-21

## Status

Generated Rev7 is the current preferred Paper-2 science draft. It is a narrow applied-readability/scope-protection revision of Rev6 in response to an external adversarial review that found no central mathematical failure.

Title:

> **Fisher Spectra and Information Singularities in Photodetectors with Memory**

## Rev7 changes relative to Rev6

No theorem, proof conclusion, figure data, or numerical result changed.

Rev7 makes only three classes of edits:

1. **Technology-neutral scale translation.** For `tau=10 ns`, the deterministic Type-II theorem is translated to ordinary units:
   - `lambda_*=1/tau=100 MHz`;
   - `omega*tau=pi` corresponds to `f=1/(2 tau)=50 MHz`;
   - the existing rigorous lower bound remains `G>=0.516975...`;
   - the existing high-frequency residue remains `1/e approximately 0.3679`.
   The manuscript explicitly says this does not assert that any particular detector technology realizes the ideal Type-II model.
2. **Scope protection around `complete`.** Broad phrases are qualified so completeness is explicitly within the admitted classical Poisson weak-intensity waveform tangent model and the stated accessible-record definition.
3. **Short experimental outlook.** The Discussion notes that a future genuinely paralyzable-detector test could compare quasi-static and finite-frequency perturbations near `lambda*tau=1`. The manuscript explicitly states that such an experiment is not required for the analytical conclusions.

The external-review response is recorded in:

`paper2/notes/REVIEW_RESPONSE_REV6_APPLIED_READABILITY_2026-08-21.md`.

## Reproducibility

Rev7 is generated assertion-checkably from Rev6 by:

`paper2/manuscript/apply_rev7_applied_readability.py`.

The generator guards the principal science invariants, including:

- `G_DC=G_cyc=(r/lambda)I_D`;
- `G_1(omega)>0` for every nonzero frequency;
- the dimensionful scale-conversion text;
- the tightened scope qualifier;
- removal of broad/unqualified drafting phrases targeted by the review.

A direct source diff from generated Rev6 to generated Rev7 was inspected. It contains only the intended prose insertions/replacements above.

## Local build result

A clean local pdfLaTeX/BibTeX8 build succeeded.

Result:

- **21 pages**;
- letter page size, `612 x 792 pt`;
- PDF openable and unencrypted;
- all citations resolved;
- all cross-references resolved;
- zero overfull hboxes/vboxes;
- zero underfull boxes;
- only remaining package warning: benign `nameref` warning concerning the redefinition of `\label`.

PDF preflight:

- encrypted: no;
- openable with PyMuPDF: yes;
- scanned: no;
- XFA: no.

## Local hashes

Generated Rev7 source SHA-256:

`a317663c626a1d0597d047ec99da55f2779bc376c320ce609d7ae6ae6cce67b3`

Generated Rev7 PDF SHA-256:

`edc4ea88d644b20196ba09f77c993ed25d9fe82a0f51877b74ffe69f4daa1db2`

Local Rev7 generator SHA-256:

`7af045d7664a3bdb338ce85fbb908a4ad219457d22affce852e087e53eb0651c`

Local self-contained Rev7 source ZIP SHA-256:

`81b33249a784b7ddafe6073c9c05a57e1529245fc6b3e5a3638f5f0a7fb6378b`

## Visual inspection

The full 21-page PDF was rendered at 120 dpi and inspected as a contact sheet. Pages changed by Rev7 were additionally inspected at 150 dpi:

- page 8: beginning of the dimensionful Type-II scale example;
- page 9: continuation/completion of the scale example;
- page 15: experimental-outlook paragraph and adjacent scope text;
- page 16: tightened conclusion terminology.

No observed:

- clipped text;
- equation/text overlap;
- margin overflow;
- figure changes or data spill;
- broken glyphs or black boxes;
- abnormal page breaks beyond an ordinary paragraph continuation from page 8 to page 9.

All four Rev6 publication figures remain unchanged in data and layout.

## Verification boundary

Rev7 is **locally build-verified, preflighted, source-diff inspected, and visually inspected**.

The dedicated Paper-2 GitHub Actions workflow has been advanced to generate and compile Rev7. The actual push-triggered Rev7 Actions job has not been directly inspected through the connector in this session. Do not claim Actions-run verification until that job itself is read.

## Current decision

Rev7 is the preferred **frozen science draft**.

Further science changes should require a concrete defect, a referee objection, or a verified novelty collision. Submission-stage metadata/package work remains separate.
