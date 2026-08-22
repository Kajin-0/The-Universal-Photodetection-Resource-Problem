# APS AI-Use and Data-Availability Disclosure Drafts

**Verified against APS policy:** 2026-08-22

These are compliance drafts, not final factual declarations. The submitting human author must personally verify the scientific content and replace all bracketed text truthfully before submission.

Official APS AI policy:

- https://journals.aps.org/authors/appropriate-use-ai-tools
- https://www.aps.org/about/news/2026/06/releases-updated-ai-policy-journals

Official APS Data Availability guidance:

- https://journals.aps.org/authors/data-availability-statements

---

# 1. Why disclosure is mandatory for this project

APS's 2026 policy defines the following as substantive AI uses requiring disclosure, among others:

- scientific reasoning or interpretation;
- literature synthesis;
- derivations or calculations;
- drafting/revising scientific claims or explanations;
- code generation/debugging that materially affects results;
- numerical analysis;
- figure generation.

AI assistance in this project has included several of these categories. Therefore an APS submission must not use a “no substantive AI use” representation.

APS requires the disclosure to identify:

1. the AI tool and version;
2. how it assisted;
3. how the human author(s) directed and verified the output.

The third point cannot be filled in by the AI itself. It must describe actual human verification performed before submission.

---

# 2. Draft acknowledgment disclosure

The following is an appropriate **framework**, but the verification clause must be replaced with a truthful human-authored description:

> OpenAI ChatGPT (GPT-5.6 Sol) was used during this work to assist with literature synthesis, mathematical derivation and proof checking, generation and debugging of numerical sanity-check code, and drafting and editing of the manuscript. The author directed the AI-assisted tasks and [INSERT TRUTHFUL DESCRIPTION OF HUMAN VERIFICATION: e.g., independently checked the analytical derivations, verified cited sources against the original literature, reproduced the numerical checks, and reviewed all manuscript text for scientific accuracy]. The author takes full responsibility for the scientific content.

Do not retain the example verification wording unless it is literally true.

Because AI assisted with scientific reasoning/derivation, APS policy indicates that substantive research use should also be described where methods are described. For this theoretical paper, a compact statement near the numerical-validation/methodological description may be appropriate, for example:

> AI-assisted tools were used during derivation/proof checking and to generate portions of the numerical validation code; all analytical statements presented as results are supported by the derivations given in the paper. [ADD TRUTHFUL HUMAN VERIFICATION DETAILS.]

Before adding this sentence, ensure it does not imply that the numerical code proves the theorem; the code is validation only.

---

# 3. Figure 1 disclosure framework

APS states that AI use in figure generation should be mentioned in the figure caption.

The current Figure 1 is a deterministic TikZ/vector schematic whose layout and source were developed with AI assistance. It is not an AI-raster image and contains no external image assets.

Suggested caption suffix, after human verification:

> The conceptual layout and TikZ source for this schematic were developed with assistance from OpenAI ChatGPT (GPT-5.6 Sol); all scientific content and labels were [INSERT TRUTHFUL HUMAN VERIFICATION DESCRIPTION].

Keep this sentence out of the frozen science-content claim structure; it is a publication-compliance annotation.

---

# 4. Data Availability Statement

A bare “No data were created or analyzed” statement is not the most transparent choice because custom numerical-checking software and manuscript/figure source files were created and are publicly stored.

Recommended statement after choosing a stable repository citation:

> No experimental data were created or analyzed in this study. Source code used for the numerical sanity checks and the manuscript and figure source files supporting the analytical results are publicly available at [STABLE REPOSITORY OR ARCHIVE CITATION].

APS states that publicly shared software should be cited in the reference list and included in the Data Availability Statement.

## Preferred archival workflow

Before acceptance, preferably:

1. freeze the submission code/source state;
2. create an immutable public archive or release with a DOI if practical;
3. add the archival citation to the bibliography;
4. use that citation in the Data Availability Statement.

If no DOI archive is created, cite a stable Git commit rather than only a moving branch URL.

---

# 5. Human verification checklist before APS submission

The submitting author should personally confirm each item and retain a private record sufficient to support the APS disclosure if editors ask for more documentation.

- [ ] Read and verify every theorem statement and hypothesis.
- [ ] Re-derive or independently check the core finite-copy Cauchy--Schwarz proof.
- [ ] Check the normalization of the cosine/sine Fisher block and the phase-average interpretation.
- [ ] Check the controlled periodic-to-continuum construction and atom convention.
- [ ] Check the compound-Poisson/CPTP pullback argument.
- [ ] Check the coherent-sideband no-go calculation.
- [ ] Verify every citation used for a priority/provenance statement against the primary source.
- [ ] Run the committed numerical validation script and inspect its output.
- [ ] Build the final submission source and inspect every page.
- [ ] Inspect Figure 1 labels/arrows and verify that it accurately represents the theorem scope.
- [ ] Review the cover letter, Popular Summary, Data Availability Statement, and AI disclosure for factual accuracy.

Only after these human checks should the bracketed disclosure language be finalized.