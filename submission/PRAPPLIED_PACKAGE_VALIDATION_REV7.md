# Physical Review Applied Package Validation — Rev7

**Date:** 2026-08-20

## Purpose

Record the mechanical and visual verification of the submission-specific Physical Review Applied copy generated from the frozen canonical Rev7 manuscript.

Canonical science source:

`manuscript/event_resource_theorem_rev7.tex`

Submission generator:

`manuscript/make_prapplied_submission.py`

Generated submission source is intentionally **not** committed to the canonical branch. It is reproduced by the assertion-based generator from frozen Rev7.

---

# Validation route

Temporary validation branch:

`agent/rev7-prapplied-validation`

Temporary draft PR:

`#14` — validation-only, not intended for merge.

Trigger SHA:

`9f74f1178aaea4595ca20d682dad840fc532d8c8`

GitHub Actions run:

`32434850102`

Job:

`96633863739`

Result:

**SUCCESS**

The validation job performed, in order:

1. compile canonical committed Rev7;
2. upload canonical Rev7 artifact;
3. run the assertion-based Physical Review Applied submission generator;
4. compile the generated submission copy independently;
5. upload the complete submission bundle.

All five functional stages completed successfully.

---

# Submission artifact

Artifact name:

`event-resource-theorem-rev7-prapplied`

Artifact ID:

`9430408451`

Artifact ZIP size:

`384207 bytes`

Artifact ZIP SHA-256:

`0ce70d971c0038fe5eb13eccb95b4ede45272e4a2dcb8297d212eff579e2418f`

The downloaded archive contained the generated submission PDF/TeX, supporting Rev7 source modules, figure sources/data, bibliography, cover letter, 100-word justification, Data Availability draft, AI-disclosure draft, checklist, and bibliography audit.

---

# Generated submission PDF

File:

`event_resource_theorem_rev7_prapplied.pdf`

Pages:

`24`

Size:

`361041 bytes`

SHA-256:

`e80562d69146514dede7c201c6aff29040002296ae10e4e8ff9876120dc6a2b8`

The PDF is unencrypted and contains no interactive forms or JavaScript.

## Visual inspection

All 24 pages were rendered and inspected in three contact-sheet groups:

- pages 1--8: **PASS**;
- pages 9--16: **PASS**;
- pages 17--24: **PASS**.

Observed:

- no clipping or truncated text;
- no malformed displayed equations;
- no figure overlap or broken figure rendering;
- title/abstract and theorem sections render normally;
- resource-hierarchy and jitter figures render correctly;
- thermodynamic sections and appendix render normally;
- the Data Availability section appears on page 21 immediately before the appendix, as intended;
- bibliography pages 23--24 render cleanly;
- no new visually apparent layout defect was introduced by submission packaging.

---

# Generated submission TeX

File:

`event_resource_theorem_rev7_prapplied.tex`

SHA-256:

`3a26badedf7c1155801447f0dd803d2f93da09a574361998c26cea8dfabe4979`

An independent unified-diff comparison against canonical
`event_resource_theorem_rev7.tex` found exactly one intentional insertion immediately before `\\appendix`:

1. a **non-rendered comment-only** APS submission reminder that substantive AI use must be disclosed with truthful human-verification language before actual submission;
2. the rendered unnumbered Data Availability section:

> This is a purely mathematical work and no data were created or analyzed in this study. All figures can be reproduced directly from the presented equations.

No theorem, proof, abstract, introduction, conclusion, figure, bibliography entry, or scientific claim was changed by the submission generator.

Canonical Rev7 therefore remains scientifically identical to the compiled submission copy except for the submission-compliance insertion above.

---

# Supporting-file hashes from downloaded artifact

Rev7 appendix SHA-256:

`90d057c5f1636ab659600a9657fd66aaecca42db70653b9752af8399ded90ef9`

`references.bib` SHA-256:

`600f9640d4a832d3f049451e2be8e2363d43a8df8809b0208802fa29eb47c63e`

---

# Warning / compile posture

The GitHub Actions job completed successfully through full LaTeX/BibTeX convergence for both the canonical manuscript and generated submission copy. The final 24-page PDF was produced and subsequently passed full visual inspection.

The exact warning text was not retained in a compact durable connector response during this pass, so this record does **not** assert an exhaustive warning inventory beyond the verified compile-success and visual-layout results. The canonical Rev7 validation immediately preceding this submission pass had only the inherited approximately `2.45667 pt` appendix overfull line involving “timing-concentration”; no new submission-package defect was observed visually.

If an exact warning inventory is needed before upload to the journal portal, rerun the read-only package compile and persist the final `.log` as an artifact rather than relying on connector log compaction.

---

# Scientific immutability check

**PASSED.**

The Physical Review Applied package is a compliance wrapper around frozen Rev7, not a new manuscript revision.

The canonical theorem source remains:

`manuscript/event_resource_theorem_rev7.tex`

No additional foundational derivation is required by this packaging pass.

---

# Remaining blockers before actual journal submission

All remaining blockers are personal/administrative rather than scientific:

- replace `Anonymous` author/affiliation with truthful metadata;
- designate corresponding author and active email;
- supply/authenticate corresponding-author ORCID;
- finalize a truthful APS substantive-AI disclosure including how the human author directed and verified AI output;
- insert that finalized disclosure into the submission copy;
- confirm funding acknowledgments, conflicts, related manuscripts/preprints, and prior submission history as applicable;
- optionally choose recommended/excluded referees after conflict review.

Status:

**PHYSICAL REVIEW APPLIED SUBMISSION PACKAGE MECHANICALLY AND VISUALLY VALIDATED; PERSONAL/ADMINISTRATIVE METADATA REMAIN.**
