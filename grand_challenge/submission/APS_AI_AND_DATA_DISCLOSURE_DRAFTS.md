# APS AI-Use and Data-Availability Disclosure Drafts

**Policy checked:** 2026-08-22

These drafts document the substantive AI use and the validation actually performed during the research/manuscript workflow. They are submission-compliance materials, not a new research-verification gate.

Official APS pages consulted during submission engineering:

- AI tools: `https://journals.aps.org/authors/appropriate-use-ai-tools`
- Data Availability: `https://journals.aps.org/authors/data-availability-statements`

---

# 1. Substantive AI use in this project

OpenAI ChatGPT (GPT-5.6 Sol) was used substantively for:

- theoretical exploration and derivation;
- proof checking and adversarial theorem review;
- literature search, synthesis, and prior-art triage;
- numerical validation-code generation/debugging;
- manuscript drafting and editing;
- deterministic TikZ Figure 1 development;
- LaTeX/build/debugging and journal-package engineering.

A “no substantive AI use” representation would therefore be inaccurate.

# 2. Disclosure draft based on the documented workflow

Suggested factual disclosure:

> OpenAI ChatGPT (GPT-5.6 Sol) was used during this work for literature synthesis and prior-art triage, mathematical derivation and proof checking, generation and debugging of numerical validation code, manuscript drafting and editing, and development of the conceptual TikZ figure. AI-assisted outputs were subjected throughout the project to analytic cross-checks, hostile/adversarial theorem review, independent finite-dimensional counterexample searches, closed-form-versus-numerical consistency tests, primary-source citation audits, deterministic source-generation assertions, LaTeX/BibTeX reference and layout gates, and rendered-page visual inspection. The analytical results reported in the manuscript are supported by the derivations presented in the paper; numerical calculations are validation only and are not used as proofs.

This statement describes the documented workflow without inventing a separate human-verification process.

If the submission portal requires a differently structured author attestation, the submitting human handles that administrative interaction at submission time. It is not part of the research/manuscript completion workflow.

# 3. Figure 1 disclosure draft

Figure 1 is a deterministic TikZ/vector schematic, not a generated raster image and not based on external image assets.

Suggested caption or disclosure sentence if required by the journal:

> The conceptual layout and TikZ source for Fig. 1 were developed with assistance from OpenAI ChatGPT (GPT-5.6 Sol); the figure is a deterministic vector rendering of equations and scope statements contained in the manuscript.

# 4. Data Availability Statement

No experimental data were created or analyzed. Numerical-validation code and manuscript/figure source files exist in the public repository.

Recommended statement once the submission references a stable repository state:

> No experimental data were created or analyzed in this study. Source code used for numerical validation and the manuscript and figure source files supporting the analytical results are publicly available in the project repository at [STABLE COMMIT / RELEASE / ARCHIVAL CITATION].

A stable commit, release, or archival DOI is preferable to a moving branch URL.

# 5. Validation record already completed in the project

The repository records the following completed checks:

- direct finite-copy theorem proof and integrated hostile review through WP24;
- randomized one-copy and global two-copy POVM searches with no violation;
- exact equality-family checks;
- support-gap repair;
- controlled periodic-to-continuum measure proof;
- independent Poisson-event/CPTP pullback argument;
- coherent-sideband no-go calculation;
- targeted prior-art audits including the Marvian--Spekkens collision boundary;
- DOI/title/provenance bibliography audit;
- full LaTeX/BibTeX compilation gates;
- unresolved-reference and overfull-box gates;
- rendered-page visual inspection;
- Rev7 truncated-Gaussian single-photon closed-form and periodic-approximant checks.

The current preferred manuscript and validation state are recorded in:

`grand_challenge/notes/MANUSCRIPT_REV7_REFEREE_HARDENING_2026-08-22.md`.

# Workflow rule

Do not add a “human verification” checklist or make human verification a manuscript-completion gate. Produce the strongest finished package possible; a human handles the act of submission and any portal-specific administrative attestations.
