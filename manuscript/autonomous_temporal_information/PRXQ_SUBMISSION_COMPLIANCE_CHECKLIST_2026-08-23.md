# PRX Quantum submission compliance checklist

**Date:** 2026-08-23

**Purpose:** submission-packaging checklist for the current PRX Quantum R4 flagship. This file is not part of the scientific claim and must be re-checked against then-current APS/PRX Quantum instructions on the actual submission date.

## Current manuscript package

- [x] Scientific theorem/proof baseline is frozen at PRXQ R3.
- [x] Current journal-facing main is the deterministic R4 bridge revision.
- [x] R4 title remains **Two spectral-resource regimes for autonomous temporal information**.
- [x] Canonical supplement remains the unchanged M2R3 supplement.
- [x] R4 adds only the late-scope companion bridge; it does not import the companion proof.
- [x] `check_prxq_r4_bridge.py` freezes the R3 theorem/proof prefix byte-for-byte and preserves theorem/proposition/corollary counts.
- [x] Final PR-triggered verification run `32674844366` passed R3 regeneration/static gate, R4 generation/freeze gate, R4 compile, supplement compile, and artifact upload.
- [x] Final artifact `9502376602`, SHA-256 `8e32c8248050ffa8be254d86f2f0a5724ef0e3edd1a9e2cf38cbc3a17ca3ed76`.
- [x] Exact R4 main (20 pages) and supplement (25 pages) render-inspected; modified pages PASS visual QA.

## Companion-manuscript handling

R4 cites the separate manuscript

> *Exact minimum unitary coupling cost of prescribed rank-changing quantum-state curvature*.

The current review-preparation bibliography entry is anonymous and labels it a companion manuscript.

Before actual submission:

- [ ] determine the companion's exact public/submission status;
- [ ] if an arXiv identifier, DOI, accepted-paper record, or other citable public metadata exists, replace the anonymous companion entry with that metadata;
- [ ] if the companion is simultaneously under consideration or jointly submitted, disclose that status accurately in the cover letter and submission system as required by then-current journal instructions;
- [ ] if the companion is not public, confirm that the citation form and editor disclosure are acceptable under then-current APS policy;
- [ ] do not imply that the flagship theorem depends on the companion: R4 explicitly states that the companion result is not used in the flagship proofs.

## Cover letter

Current draft:

`PRXQ_COVER_LETTER_R1.md`

The R4 cover-letter draft now:

- summarizes the two-regime survival/synthesis principle;
- gives the sharp bilateral/one-sided action coefficients;
- mentions the companion equality `A_ex^(2)=hbar nu V_min` as an independent dynamical completion;
- explicitly says the flagship is self-contained and does not rely on the companion proof;
- leaves submission history, companion status, joint-submission status, and referee metadata for the author to confirm rather than inventing them.

## Popular Summary

- [x] A nontechnical Popular Summary exists: `PRXQ_POPULAR_SUMMARY_R1.md`.
- [ ] Re-read it immediately before submission and confirm it still matches the final R4 framing; do not add implementation-cost detail unless it improves rather than obscures the two-regime concept.

## AI disclosure and Data Availability

The current package contains dedicated AI-use and Data Availability material generated through the existing PRXQ front-matter chain.

Before submission:

- [ ] re-check the current APS Appropriate Use of AI Tools policy;
- [ ] verify the tool/provider/model description and the human-direction/verification statement remain accurate;
- [ ] confirm the applicable OpenAI account/privacy/rights terms satisfy the then-current journal requirements;
- [ ] re-check the current APS Data Availability Statement guidance;
- [ ] ensure any software/code availability statement accurately describes what is public at submission time;
- [ ] if an immutable DOI-backed software/source archive is created, use the persistent identifier where appropriate.

## Author-controlled metadata that the repository cannot certify

- [ ] corresponding-author name, affiliation, active email, and ORCID;
- [ ] all coauthor metadata if applicable;
- [ ] funding and conflict-of-interest statements;
- [ ] accurate Physical Review submission history;
- [ ] exact related/companion-manuscript status;
- [ ] joint-submission status;
- [ ] suggested/excluded referees only after conflict-of-interest review;
- [ ] final human read and approval of every theorem statement, proof, citation, disclosure, and generated submission file.

## Scientific scope lock for submission

Do not enlarge R4 merely because the companion theorem exists.

The allowed bridge is:

`V_min(C)=(1/2)Tr C`,

`A_ex^(2)=hbar nu V_min`,

with the explicit limitations already present in R4.

Do not import the infinite-dimensional implementation proof, ancillary construction, or full PRA theorem stack into the PRXQ submission.

Do not use Nobel/prize-level framing in the manuscript, Popular Summary, cover letter, or submission metadata.

## Official policy pages recorded for re-checking

These were the policy locations used in the August 23, 2026 packaging audit and must be revisited on the actual submission date because requirements can change:

- PRX Quantum Information for Authors: `https://journals.aps.org/prxquantum/authors`
- APS Data Availability Statement guidelines: `https://journals.aps.org/authors/data-availability-statements`
- APS Appropriate Use of AI Tools: `https://journals.aps.org/authors/appropriate-use-ai-tools`
- APS Editorial Policies and Practices: `https://journals.aps.org/authors/editorial-policies`
