# WP13 — R5 figure-integration freeze

**Date:** 2026-08-25

**Status:** **FROZEN PASS.** The figure-integrated practical manuscript has passed the complete R1-to-R5 provenance chain, exact frozen-figure identity gate, additive byte-isolation gate, clean LaTeX compilation, warning gate, artifact upload, and full 10-page render audit.

## Purpose

Integrate the frozen WP12 four-figure package into the frozen R4 manuscript without changing any pre-existing scientific sentence, equation, theorem, proof, citation, disclosure, or bibliography entry.

## Source discipline

R5 is generated from R4 by:

- `manuscript/practical_temporal_information/r5_figure_blocks.py`
- `manuscript/practical_temporal_information/apply_r5_figure_integration.py`
- `manuscript/practical_temporal_information/check_practical_r5.py`

The checker removes the four exact figure/caption blocks from generated R5 and requires the remainder to equal R4 byte-for-byte. It also requires exactly four wide `figure*` floats, exactly one expected path and label for each frozen figure, and explicit provenance/scope language in the captions.

The support section remains an external `\input{sections/support_crossover_r2}` in the main generated source. Figure 3 is therefore inserted immediately before `\section{Standard Hamiltonian implementation benchmark}`, which places it after the complete externally input support/crossover section. This corrected a first-run mechanical marker mismatch without altering figure content or manuscript science.

## Frozen figure identity gate

Before R5 generation, manuscript CI regenerates the WP12 figures using the same pinned environment and requires the exact canonical vector-PDF hashes:

1. Fig. 1: `9b1f3b05552a91e6a57f08034d9275f450496138738f48eb654c6952e401b48e`
2. Fig. 2: `ffdb3a32ae3a571366b1eaf915ec8842eecc9bd48725219848f8fa233a64713e`
3. Fig. 3: `a7440d615fce70e8890af9d493fecf37b610938b1ec05ef53493f7f367195394`
4. Fig. 4: `7eafd153221f3617cd6fcc38c71ef92b6d2df21087490e6b3cd4c159615241f0`

All four identities passed in the final R5 run.

## Final clean-CI verification

Workflow run: `32915363157`

Job: `98017843874`

Source commit: `55ec3af3bd9d57830c03f65655180936eb85eda9`

All steps passed:

1. static draft integrity gate;
2. R1 mechanical generation;
3. R2 support-theorem generation;
4. R2 isolation gate;
5. R3 hostile-review repair generation;
6. R3 isolation gate;
7. R4 presentation cleanup;
8. R4 isolation gate;
9. pinned figure dependency installation;
10. frozen WP12 figure regeneration;
11. exact four-PDF SHA-256 identity gate;
12. R5 generation;
13. R5 additive byte-isolation/caption-provenance gate;
14. R5 LaTeX compile;
15. unresolved-reference/citation and overfull-box gate;
16. artifact upload.

## Canonical R5 artifact

Artifact:

- ID: `9588018384`
- name: `practical-temporal-information-r5`
- archive size: `615446` bytes
- archive digest: `sha256:06e1de8d8f5e44f9d62e6ebd06362d2cfbc93132014718398e57b877c784c281`

Exact built manuscript PDF:

- file: `operational_temporal_information_r5.pdf`
- pages: `10`
- bytes: `429432`
- SHA-256: `fd451a59ca5b70731b61f7ce237bd06a1d5f7105305e064cfe21bbb588e6bf48`

## Full render audit

The exact artifact PDF was rendered independently at 200 dpi and all ten pages were inspected.

PASS:

- no clipped text or figures;
- no overlaps;
- no broken glyphs or black squares;
- no equation overflow;
- no unresolved references/citations;
- no visible hyperlink rectangles;
- all four figures legible in grayscale;
- all four captions legible and correctly attributed/scoped;
- Fig. 1 does not clip the Fisher-information peak;
- Fig. 2 retains the companion-memory attribution and numerical labels;
- Fig. 3 support/radius/resource/noncircular-protocol panels are legible;
- Fig. 4 fixed-energy benchmark and Level-I/III/II failure hierarchy are legible;
- theorem/proof flow around Fig. 2 and Fig. 3 remains readable;
- Data Availability and AI-assisted-research disclosures remain intact;
- bibliography renders cleanly.

## Freeze rule

R5 is now the canonical figure-integrated manuscript baseline.

Do not change theorem statements, equations, proof language, companion provenance, figure values, figure geometry, or captions during ordinary publication cleanup. A genuine scientific or figure defect requires a new isolated revision with its own gate and render audit.

## Next work order

The next permitted phase is **publication-style compression and submission packaging**, not new theorem development.

1. hostile-read R5 for redundant/tutorial prose that can be removed without narrowing assumptions or changing claims;
2. if compression is worthwhile, define a deterministic R6 text-only transform from R5 with an explicit allowed-edit map and byte/section gates;
3. preserve all four frozen figure blocks exactly;
4. preserve theorem/proposition/equation content unless a genuine defect is found;
5. compile/render/audit R6 independently;
6. fresh-check then-current APS/PRA policies before submission packaging;
7. replace anonymous author/companion metadata only when actual public/submission status is known.
