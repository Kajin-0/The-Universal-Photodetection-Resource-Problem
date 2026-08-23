# PRX Quantum submission compliance checklist

**Date:** 2026-08-23

**Purpose:** record current APS/PRX Quantum submission requirements separately from the scientific theorem audit. This file is a packaging checklist, not part of the manuscript claim.

## Already implemented in the repository

- [x] PRX Quantum-focused abstract: `sections/prxq_abstract_r1.tex`.
- [x] PRX Quantum-focused introduction: `sections/prxq_introduction_r1.tex`.
- [x] Nontechnical Popular Summary near the recommended 150-word length: `PRXQ_POPULAR_SUMMARY_R1.md`.
- [x] Cover-letter draft with context, key findings, significance case, and fields for submission history/referee metadata: `PRXQ_COVER_LETTER_R1.md`.
- [x] Data Availability Statement: `sections/data_availability_r1.tex`.
- [x] Public repository citation in `references.bib`: `UniversalPhotodetectionResourceRepo2026`.
- [x] Substantive AI-use disclosure: `sections/ai_use_disclosure_r1.tex`.
- [x] Deterministic generator inserts PRXQ abstract, introduction, AI disclosure, and Data Availability Statement without modifying the audited theorem body: `apply_prxq_frontmatter_r1.py`.
- [x] Static gate enforces that every citation used by Supplemental Material also appears in the generated main-paper bibliography.
- [x] Supplement is self-contained at the mathematical level and main paper is intended to stand alone conceptually.

## Current APS requirements checked against official guidance

### Cover letter

PRX Quantum requests context, a summary of key findings, relevant Physical Review submission history including joint submissions, and any recommended/excluded referees. The draft contains all four categories, with author-specific fields left explicit rather than invented.

### Popular Summary

PRX Quantum requires a nontechnical summary before publication and recommends approximately 150 words, no equations, low jargon, with problem -> advance -> implications -> broader importance. The R1 summary follows that structure.

### Data Availability Statement

All Physical Review articles require a Data Availability Statement. This theoretical work reports no experimental or observational data, but it does use original validation software. The current statement therefore identifies the public repository containing manuscript sources, research notes, and custom numerical validators.

**Pre-submission improvement recommended:** archive the exact submission commit/release in a persistent repository such as Zenodo and replace or supplement the GitHub URL citation with the resulting DOI. APS prefers persistent identifiers for public data/software citations.

### Supplemental-Material references

PRX Quantum requires references cited in Supplemental Material to appear in the main article's reference list. `check_m2_tex_static.py` now enforces this automatically after the PRXQ manuscript is generated.

### Substantive AI use

APS currently defines substantive AI use to include scientific reasoning or interpretation, drafting/revising scientific claims, literature synthesis, derivations/calculations, material code generation/debugging, simulations/numerical analysis, and data/statistical analysis. This project used AI in several of those ways, so disclosure is mandatory.

The current disclosure states:

- tool: OpenAI ChatGPT;
- version/configuration: manuscript-stage GPT-5.6 Sol, with earlier GPT-5.6-series sessions;
- assistance: exploratory derivations, counterexample searches, literature synthesis, algebraic checks, validator code, adversarial review, and manuscript drafting;
- direction/verification: explicit human problem specifications and review decisions, with AI outputs treated as provisional and subjected to analytic proofs, separate re-derivation passes, counterexample searches, source verification, and numerical validators;
- responsibility: final scientific responsibility remains with the author.

## Items that cannot be certified by the repository and must be confirmed by the author

- [ ] **AI rights/privacy terms:** confirm immediately before submission that the OpenAI account/settings and governing terms used for the work satisfy APS's requirement that the AI tool claim no rights over submitted content and that applicable data-use/privacy settings are acceptable. APS specifically asks authors to revisit current terms because they can change.
- [ ] **Human final review:** read and approve every theorem statement, proof, citation, AI disclosure, and generated manuscript before submission; APS places full responsibility on the human author.
- [ ] **Submission history:** fill the cover-letter statement accurately.
- [ ] **Joint-submission status:** fill the cover-letter statement accurately.
- [ ] **Corresponding-author metadata:** name, affiliation, active email, and verified ORCID as required by APS.
- [ ] **Referee suggestions/exclusions:** supply only after a conflict-of-interest check; do not invent names for completeness.
- [ ] **Funding/conflict statements:** add if applicable.
- [ ] **Persistent archive:** preferably mint an immutable DOI-backed archive for the exact submission code/source snapshot and update the Data Availability citation.
- [ ] **Successful LaTeX/BibTeX CI result:** retrieve a concrete successful GitHub Actions run before calling the submission build verified.

## Official policy sources checked on 2026-08-23

- PRX Quantum Information for Authors: `https://journals.aps.org/prxquantum/authors`
- APS Data Availability Statement guidelines: `https://journals.aps.org/authors/data-availability-statements`
- APS Appropriate Use of AI Tools: `https://journals.aps.org/authors/appropriate-use-ai-tools`
- APS Editorial Policies and Practices: `https://journals.aps.org/authors/editorial-policies`

Because these policies can change, re-check them on the actual submission date.
