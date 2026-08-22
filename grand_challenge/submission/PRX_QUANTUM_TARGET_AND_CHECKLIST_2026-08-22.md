# PRX Quantum Target Decision and Submission Checklist

**Updated:** 2026-08-22

**Science checkpoint:** WP24

**Preferred submission manuscript:** **Rev7 PRX Quantum**

## Decision

### First target: PRX Quantum — Research Article

PRX Quantum remains the strongest realistic first target. The manuscript sits directly at the intersection of quantum metrology/sensing, quantum measurement, resource-style constraints, `U(1)` time-translation structure, photon wavepackets, and detector/source physics.

The strongest editorial case is an **exceptional connection/insight**:

- modes-of-asymmetry theory identifies available energy-gap components;
- the manuscript converts that kinematic structure into a sharp **operational classical-Fisher ceiling for any actual POVM**;
- the result remains valid for arbitrary finite-copy collective measurements;
- one common measurement saturates the full geometric harmonic hierarchy;
- an explicit nonextremal single-photon example approaches the survival ceiling closely;
- the normalized source law survives arbitrary parameter-independent field formation and detector processing for the stated independent-event source class.

Do not pitch the paper merely as “mean energy bounds temporal Fisher information.” The principal theorem is the population-survival law.

### Preferred fallback: Physical Review A — Regular Article

If PRX Quantum declines on selectivity rather than correctness, Physical Review A is the preferred fallback/transfer target. Do not broaden the claims to chase editorial novelty.

### PRL

PRL remains a stretch requiring a deliberate Letter rewrite. Do not compress Rev7 by hiding essential hypotheses or proof structure.

---

# Rev7 scientific framing for submission

## Exact finite-copy theorem

For exact periodic random-time encoding,

`Tr F_N^(k)/N <= min(D_k,U_k) <= T_k`

for any finite number of independently encoded copies and any joint POVM, including entangled collective measurements.

## Controlled continuum theorem

For controlled periodic-to-continuum limits,

`R(nu) <= Pr(Omega>=nu)`.

This is the main continuum statement.

`Ebar+=hbar<Omega>` is mean **excess energy above the participating lower edge**, not a common carrier offset.

The integrated and pointwise energy inequalities are first-moment corollaries, not the independent core theorem.

## Modes-of-asymmetry distinction

Acceptable submission framing:

> Established modes-of-asymmetry theory identifies which `U(1)` energy-gap components can occur. The present theorem instead bounds the classical Fisher information that any actual measurement can extract about a perturbation of the random-time mixing distribution, with a sharp coefficient determined by participating energy populations.

## Nonextremal photon example

Rev7 includes a transform-limited truncated-Gaussian single-photon spectrum. Canonical covariant timing reaches approximately:

- 96.6% of the survival ceiling at `nu=0.5 sigma`;
- 88.5% at `nu=sigma`.

This is a physical significance example, not a new theorem or equality claim.

---

# Claim discipline

Use:

- “operational Fisher-information ceiling”;
- “for the random-time source class considered here”;
- “controlled periodic-to-continuum limit”;
- “mean excess energy above the participating lower edge”;
- “targeted searches did not identify an exact predecessor”;
- “sharp within the stated model and attained by…”

Avoid:

- “universal law for arbitrary optical waveforms”;
- “all quantum detectors obey…” without the source hypothesis;
- “new `U(1)` mode decomposition”;
- “new Hardy--Hilbert inequality”;
- treating the `hfR` first-moment corollary as the deepest theorem;
- treating `Ebar+` as total laboratory/carrier energy;
- unqualified direct-continuum claims outside the controlled construction.

**Priority remains unverified, not certified.**

---

# Rev7 package status

Generation chain:

`Rev1 -> Rev2 -> Rev3 -> Rev4 -> Rev5 -> Rev6 PRX packaging -> Rev7 referee hardening -> Rev7 layout repair`.

Final local Rev7 preflight:

- full `pdflatex -> BibTeX -> pdflatex -> pdflatex`: **PASS**;
- **8 pages**;
- file size: **403,102 bytes**;
- SHA-256: `d168c3901faa6f29bda0eba71abe8049cc9819d91843273beeeeffb9443818ae`;
- unresolved citations/references: **0**;
- overfull boxes: **0**;
- fatal/undefined controls: **0**;
- all pages rendered at 200 dpi and visually inspected: **PASS**;
- Figure 1: **PASS**;
- photon-example closed forms and periodic-approximant convergence: **PASS**.

Dedicated CI generates Rev7, runs the finite-copy theorem validator and photon-example validator, compiles the PRX source, and applies reference/layout/style gates.

Detailed preflight:

`grand_challenge/notes/MANUSCRIPT_REV7_REFEREE_HARDENING_2026-08-22.md`.

---

# Submission materials

- [x] Rev7 PRX Quantum manuscript source generated.
- [x] Figure 1 source committed and visually verified.
- [x] Bibliography DOI/title audit completed.
- [x] Added single-photon/time-frequency context references audited.
- [x] Finite-copy numerical adversarial validator committed.
- [x] Truncated-Gaussian photon validator committed.
- [x] PRX Quantum cover letter updated for Rev7.
- [x] PRX Quantum Popular Summary updated for Rev7.
- [x] AI-use/Data Availability disclosure draft prepared from the documented workflow.
- [x] Full local build and visual gate passed.

Administrative fields that cannot be known without user-supplied facts may remain placeholders and are handled at submission. Do not invent author affiliation, funding, conflicts, prior-submission history, or similar metadata.

---

# AI-use / Data Availability package

The repository contains a factual disclosure draft documenting OpenAI ChatGPT (GPT-5.6 Sol) use for theoretical exploration, literature synthesis, proof checking, code assistance, manuscript editing, figure development, and build engineering, together with the validation actually performed in the workflow.

Do **not** add a separate “human verification” project gate. Any portal-specific author attestation is part of the human act of submission, not another research cycle.

Recommended Data Availability form once a stable repository state is cited:

> No experimental data were created or analyzed in this study. Source code used for numerical validation and the manuscript and figure source files supporting the analytical results are publicly available in the project repository at [STABLE COMMIT / RELEASE / ARCHIVAL CITATION].

---

# Journal ladder

1. **PRX Quantum — Research Article**.
2. **Physical Review A — Regular Article**.
3. Physical Review Research — secondary alternative.
4. PRL — only after a separate deliberate Letter rewrite.

Do not shotgun-submit the same manuscript simultaneously to multiple journals.

# Current action

**Freeze Rev7.** The manuscript and submission materials are complete to the fullest extent currently justified. Reopen only for a concrete theorem defect, historical-priority collision, build/rendering defect, unavoidable journal-format requirement, or new referee-level objection.
