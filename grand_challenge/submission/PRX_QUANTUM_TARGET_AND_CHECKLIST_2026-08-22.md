# PRX Quantum Target Decision and Submission Checklist

**Verified:** 2026-08-22

**Science checkpoint:** WP24

**Frozen science content:** Rev4

**Preferred publication draft:** Rev5

## Decision

### First target: PRX Quantum — Research Article

PRX Quantum is the strongest realistic first target for the present manuscript.

The fit is unusually direct. Its stated scope includes:

- fundamental concepts in quantum information;
- resource theories;
- quantum metrology and sensing;
- quantum emitters, photon sources, and detectors;
- open quantum systems and quantum control.

The manuscript connects quantum statistical inference, temporal-mode information, semibounded energy resources, and detector/source physics. Its strongest pitch is therefore not generic photodetection, but an **operational quantum-metrology/resource theorem** that is then inherited by an explicit photodetection source class.

PRX Quantum states that accepted papers should satisfy at least one exceptional-impact criterion: exceptional advance, connection, capabilities, or insight. The defensible case here is primarily:

1. **exceptional insight** — a pointwise operational Fisher-information ceiling equal to an excitation-energy survival probability, valid for arbitrary finite-copy collective measurement within the source class;
2. **exceptional connection** — a direct bridge between random-time `U(1)` mixing, quantum metrology, resource-style energy bounds, and source-to-record photodetection.

Do **not** claim that the general `U(1)` mode decomposition, weighted twirling, canonical phase measurement, QFI, or Hardy--Hilbert mathematics is new.

Official sources checked:

- https://journals.aps.org/prxquantum/about
- https://journals.aps.org/prxquantum/scope
- https://journals.aps.org/prxquantum/authors
- https://journals.aps.org/prxquantum/abstract/10.1103/PRXQuantum.6.020001

## Why not Physical Review Letters first

PRL is a credible stretch venue, but it is **not the recommended first submission in the current form**.

Current PRL Letters are limited to 3750 words, approximately four journal pages for the core article, with up to two pages of End Matter. PRL also requires broad impact, innovation, and interest across physics.

The present seven-page theorem paper could probably be compressed into a PRL architecture only by moving substantial proof/scope material to End Matter and rewriting for a broader physics audience. That would create a second manuscript-engineering project and could weaken the unusually clean theorem/scope presentation.

More importantly, historical priority for the exact operational tail theorem remains unverified. A PRL pitch would create pressure to use broader significance language than is presently justified.

Therefore:

- do not submit Rev5 directly to PRL;
- reconsider PRL only if an editor/referee or independent expert judges the theorem to have broad cross-physics importance and a four-page core can be created without hiding essential hypotheses.

Official source: https://journals.aps.org/prl/authors

## Fallback: Physical Review A — Regular Article

If PRX Quantum declines the manuscript on selectivity rather than correctness, the preferred fallback is **Physical Review A, Regular Article**.

PRA explicitly covers:

- fundamental concepts;
- quantum measurements and estimation;
- quantum information science;
- photonics;
- quantum optics.

Regular Articles have no length limit. The current Rev5 architecture is already close to an appropriate PRA article.

APS supports transfers between Physical Review journals. If PRX Quantum offers a transfer, preserve any useful editorial/referee history unless there is a strategic reason not to.

Official sources:

- https://journals.aps.org/pra/about
- https://journals.aps.org/pra/authors
- https://journals.aps.org/pra/authors/guidelines-section-selection-physical-review-a

## Cost / open-access consequence

PRX Quantum is fully open access. APS lists the **2026 PRX Quantum APC as USD 3,590**. The charge is due only after acceptance; institutional agreements or eligible country waivers may cover it.

PRA is hybrid. Gold open access is optional; APS lists a 2026 PRA gold-OA APC of USD 2,910.

Official source: https://journals.aps.org/authors/apcs

Do not assume an APC is covered. This is an administrative item for the human author to resolve before acceptance, not a scientific reason to alter the paper.

---

# PRX Quantum submission requirements relevant to this paper

## Article type and length

Submit as **Research Article**.

PRX Quantum currently lists **no length limit** for Research Articles.

Rev5's seven-page length is therefore acceptable in principle.

## Audience

PRX Quantum asks authors to write for the broad quantum information science and technology community.

The current manuscript is already much closer to this audience after Rev3--Rev5, but the cover letter must foreground:

1. the random-time statistical experiment;
2. the arbitrary-measurement operational theorem;
3. the exact energy-survival interpretation;
4. the connection to quantum metrology and photodetection;
5. the explicit coherent-waveform no-go boundary.

## Formatting

Current Rev5 is scientifically frozen but uses the REVTeX `pra` journal option inherited from the original build skeleton.

For a PRX Quantum package:

- create a **journal-target packaging revision only**;
- change the journal option from `pra` to `prx` in REVTeX 4.2;
- preserve all theorem/proof text, equations, citations, figure, and scientific scope;
- regenerate and re-run the same full build/visual gates.

APS currently states that a PDF alone is sufficient for peer review, although source files are preferred. REVTeX 4.2 is the correct APS source format.

Official sources:

- https://journals.aps.org/prxquantum/authors
- https://journals.aps.org/revtex

## Cover letter

PRX Quantum asks the cover letter to include:

- context of the results;
- summary of key findings;
- relevant Physical Review submission history;
- recommended or excluded referees, if any.

A draft is stored separately in this directory.

## Popular Summary

PRX Quantum requires a nontechnical Popular Summary before publication, approximately 150 words, with no mathematical expressions and minimal jargon.

A draft is stored separately in this directory.

## Data Availability Statement

All published Physical Review articles require a Data Availability Statement.

This work is analytical, but custom numerical sanity-check software and manuscript/figure source files were created. Therefore the most transparent statement is **not** simply “No data were created or analyzed.”

Recommended submission-stage statement, after choosing the stable repository commit/archive:

> No experimental data were created or analyzed in this study. Source code used for the numerical sanity checks and the manuscript/figure source files supporting the analytical results are publicly available at [repository/archive citation].

APS states that publicly shared software should be cited in the reference list and named in the Data Availability Statement. Before final acceptance, preferably create an archival DOI (for example through an appropriate software/data archive) or otherwise cite a stable repository commit.

Official source: https://journals.aps.org/authors/data-availability-statements

## Preprints

APS submission policy explicitly asks authors to disclose an e-print identifier when related work has been deposited on a preprint server. Posting an e-print is therefore compatible with the submission workflow; if a preprint is posted, enter its identifier in the APS submission information and maintain version consistency.

Official source: https://journals.aps.org/authors/editorial-policies

---

# Mandatory APS AI-use compliance

APS updated its AI policy on 2026-06-17.

Substantive AI uses must be disclosed. APS explicitly lists scientific reasoning, literature synthesis, derivations/calculations, code generation/debugging affecting results, simulations/numerical analysis, drafting/revising scientific claims, and figure generation as substantive uses.

This project has used AI substantively in several of those categories. Therefore **an AI-use disclosure is mandatory for an APS submission**.

APS requires disclosure to state:

- tool name and version;
- how it assisted;
- how the human author(s) directed and verified the output.

AI used in the research itself should be described where methods are described. Other substantive manuscript use belongs in the Acknowledgments. AI assistance in figure generation should be stated in the figure caption.

Official sources:

- https://www.aps.org/about/news/2026/06/releases-updated-ai-policy-journals
- https://journals.aps.org/authors/appropriate-use-ai-tools

A draft disclosure framework is stored separately. **Do not submit it unchanged until the human author has truthfully filled in how they personally verified the AI-assisted derivations, literature, code, and figure.**

---

# Scientific claim discipline for the submission

The following phrases are acceptable:

- “We derive an operational Fisher-information ceiling…”
- “For the random-time source class considered here…”
- “Targeted literature searches did not identify an exact predecessor…”
- “The theorem links…”
- “The coefficient is sharp within the stated model and is attained by…”

Avoid:

- “the first universal quantum limit on photodetection bandwidth”;
- “a universal law for arbitrary optical waveforms”;
- “a new `U(1)` mode decomposition”;
- “a new Hardy--Hilbert inequality”;
- “all quantum detectors obey…” without the random-time source hypothesis;
- unqualified direct-continuum claims outside the controlled large-period construction;
- claims that the two-quadrature coefficient automatically governs a pre-known single scalar quadrature.

---

# Submission package checklist

## Scientific files

- [x] Rev5 publication draft generated and locally build-verified.
- [x] Figure 1 source committed and visually verified.
- [x] Bibliography DOI/title audit completed.
- [x] Numerical theorem sanity-check code committed.
- [ ] Generate PRX-target source using REVTeX `prx` option only.
- [ ] Re-run full LaTeX/BibTeX and seven-page visual gate after target-style conversion.
- [ ] Add final Data Availability Statement to manuscript/package.
- [ ] Add truthful APS AI disclosure after human verification.
- [ ] Add figure-caption AI disclosure if required by final human verification record.
- [ ] Add stable repository/software citation to bibliography and DAS.

## Human administrative metadata — do not invent

- [ ] final author name(s) and order;
- [ ] affiliation(s) where the work was performed;
- [ ] contact-author email;
- [ ] ORCID iD(s), if desired;
- [ ] funding/grant information, or truthful statement that no specific funding supported the work if appropriate;
- [ ] conflict-of-interest disclosures if required;
- [ ] previous APS submission history, if any;
- [ ] preprint/e-print identifier, if posted;
- [ ] recommended referees;
- [ ] excluded referees/institutions, if any;
- [ ] APC coverage/institutional agreement decision.

## Portal materials

- [ ] journal: PRX Quantum;
- [ ] article type: Research Article;
- [ ] cover letter finalized;
- [ ] Popular Summary finalized (~150 words, no equations);
- [ ] Data Availability Statement entered;
- [ ] AI-use disclosure present in manuscript and figure caption as applicable;
- [ ] subject classifications / keywords selected;
- [ ] source files uploaded or clean PDF submitted for initial review;
- [ ] all authors approve submission.

---

# Target ladder

1. **PRX Quantum — Research Article**: first target; high selectivity, strongest realistic fit.
2. **Physical Review A — Regular Article**: preferred fallback, especially after a PRX Quantum selectivity rejection or transfer offer.
3. **Physical Review Research**: reasonable broad/open-access alternative, but not preferred over PRA for this exact theoretical/quantum-optics positioning.
4. **PRL**: stretch only after a deliberate Letter rewrite and independent confidence that the result has sufficiently broad physics impact.

Do not shotgun-submit. APS and standard publication ethics prohibit simultaneous consideration of the same manuscript by multiple journals.