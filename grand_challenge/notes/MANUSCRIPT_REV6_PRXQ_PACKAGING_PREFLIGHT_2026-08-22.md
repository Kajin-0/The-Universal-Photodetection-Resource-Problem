# Grand Challenge Manuscript Rev6 — PRX Quantum Packaging Preflight

**Date:** 2026-08-22

**Science checkpoint:** WP24

**Frozen science content:** Rev4

**Preferred publication content:** Rev5

**PRX Quantum target package:** Rev6 (`energy_survival_temporal_fisher_rev6_prxq.tex`), style-only conversion from Rev5

## Status

**PRX QUANTUM PACKAGING PREFLIGHT: PASS, subject to human administrative/compliance completion.**

Rev6 changes only the REVTeX journal style from `pra` to `prx`. It changes no theorem, proof, equation, numerical coefficient, source hypothesis, scope qualifier, citation claim, Figure 1 content, or novelty language.

Generation chain:

`Rev1 -> Rev2 -> Rev3 -> Rev4 -> Rev5 -> Rev6 PRX style package`.

---

## Journal-target decision

Primary target: **PRX Quantum — Research Article**.

Preferred fallback: **Physical Review A — Regular Article**.

PRL is not recommended as the first target in the current form because its four-page/3750-word core format would require a distinct compression project and stronger broad-physics positioning than is currently justified.

Full rationale and current journal requirements are recorded in:

`grand_challenge/submission/PRX_QUANTUM_TARGET_AND_CHECKLIST_2026-08-22.md`.

---

## Rev6 mechanical audit

The target-style source uses:

`\documentclass[aps,prx,reprint,amsmath,amssymb,longbibliography]{revtex4-2}`.

Local target-style reproduction gives:

- pages: **7**;
- overfull boxes: **0**;
- fatal/undefined controls: **0**;
- visual page-flow regression relative to Rev5: **none found**;
- Figure 1 remains readable and correctly placed;
- bibliography page remains visually clean.

The current execution image no longer exposes a `bibtex` executable, so the target-style local check reused the already fully audited Rev5 `.bbl`; the source bibliography itself is unchanged from the Rev5 build that previously passed the complete `pdflatex -> BibTeX -> pdflatex -> pdflatex` cycle. The dedicated repository CI generates the full chain and is configured to compile Rev6 with the normal LaTeX action, which supplies the bibliography toolchain.

Do not misstate this as direct inspection of a remote GitHub Actions push run; the current connector still does not expose those branch-push runs.

---

## Fresh theorem sanity check at submission checkpoint

A fresh deterministic/randomized finite-dimensional validation was rerun with seed `20260822`.

Sampled:

- **11,825** one-copy random frame-POVM cases;
- **936** global two-copy random frame-POVM cases;
- dimensions through 5 for one copy and 3 for two copies;
- random sector populations including support gaps.

No violation of

`Tr F_N^(k) <= N min(D_k,U_k) <= N T_k`

was found.

Largest sampled ratios to the tight bound:

- one copy: approximately `0.999274139`;
- two-copy global measurement: approximately `0.966617918`.

These ratios have no theorem status; they only demonstrate that the randomized search approached the boundary without crossing it.

The geometric/canonical-phase equality check satisfies

`R(k)=r^k`

at machine precision, with maximum absolute discrepancy approximately `3.3e-16` over the tested values.

The theorem remains analytic; numerical work is validation only.

---

## Submission support files now present

- `grand_challenge/submission/PRX_QUANTUM_TARGET_AND_CHECKLIST_2026-08-22.md`
- `grand_challenge/submission/PRX_QUANTUM_COVER_LETTER_DRAFT.md`
- `grand_challenge/submission/PRX_QUANTUM_POPULAR_SUMMARY_DRAFT.md`
- `grand_challenge/submission/APS_AI_AND_DATA_DISCLOSURE_DRAFTS.md`
- `grand_challenge/manuscript/apply_rev6_prxquantum_packaging.py`
- dedicated CI updated to generate/compile Rev6.

---

## Mandatory human blockers before actual submission

These are intentionally **not** guessed or generated as facts:

1. final author name(s) and order;
2. affiliation(s) where the work was performed;
3. contact-author email;
4. ORCID(s), if used;
5. funding/grant statement;
6. conflict-of-interest information if applicable;
7. prior APS submission history;
8. preprint/e-print identifier if posted;
9. referee recommendations/exclusions if desired;
10. APC coverage/institutional agreement status.

### APS AI disclosure is mandatory

Under APS's June 2026 AI policy, this project contains substantive AI use and must disclose it.

The human author must personally verify the AI-assisted derivations, literature synthesis, numerical code, manuscript text, and figure content and then replace the bracketed verification language in:

`grand_challenge/submission/APS_AI_AND_DATA_DISCLOSURE_DRAFTS.md`.

Do **not** submit an AI disclosure that falsely states human verification that has not actually occurred.

### Data Availability

The preferred statement acknowledges that no experimental data were created while providing a stable citation for the numerical-validation and manuscript/figure source code. A stable release/commit or archival DOI should be selected and cited before final submission/acceptance.

---

## Decision

The manuscript should now be treated as **scientifically frozen and publication-engineered for PRX Quantum**.

No additional theorem work is recommended by default.

The next actions are human submission completion:

1. perform/record the human verification required for APS AI disclosure;
2. supply author/affiliation/contact/funding/submission-history metadata;
3. finalize Data Availability with a stable repository/archive citation;
4. generate the final Rev6 package;
5. perform one final PDF/source checksum and page inspection;
6. submit to PRX Quantum as a Research Article.

If PRX Quantum declines on selectivity rather than correctness, prefer an APS transfer to Physical Review A rather than weakening or broadening the scientific claims.