# Research Log — Round 14

**Date:** 2026-08-20

## Purpose
Checkpoint the autonomous-event project after the WP35 manuscript correction and final Rev5 publication audit.

---

## 1. Project remained on the publication path

No new foundational branch was opened.

Frozen unless explicitly needed by review:

- HgCdTe/Kane WP17–24;
- coherent quantum pointers;
- continuous analog detectors;
- non-Poisson/nonclassical source extensions.

The first-paper class remains the autonomous/time-translation-invariant, independent-event, one-primary-registration marked event detector under weak coherent/Poisson direct-detection intensity modulation.

---

## 2. WP35 repaired the only new scientific wording defect

A final hostile read of Rev4 found that a successful-registration edge rate does not generically bound the complete mark-conditioned registration hazard when other exits compete.

For a finite-state CTMC, the safe uniform quantity is

\[
q_{\max}
=\max_{x\in S_{\rm pre}}
\sum_{y\ne x}W_{yx},
\]

the maximum **total pre-registration escape rate**, under the restriction that the accessible mark does not independently expose the realized pre-registration holding times.

The first manuscript no longer makes the generic quantum-jump operator-norm claim.

The main theorem and WP29 are unchanged.

---

## 3. Rev5 created reproducibly

`manuscript/apply_rev5.py`

is an assertion-based Rev4 -> Rev5 transformer.

It performs four publication-hardening changes:

1. applies WP35 and removes the quantum-jump sentence;
2. adds an explicit prose reference to the resource-hierarchy figure;
3. adds an explicit prose reference to the exact jitter-no-go figure;
4. tightens the Dechant comparison to the finite-frequency response/fluctuation and broadband-SNR claims directly needed from that citation.

The hierarchy figure is versioned as

`manuscript/figure_resource_hierarchy_rev5.tex`

and describes its final layer as a `microscopic sufficient local-rate resource`.

---

## 4. Latest Rev5 mechanical gate passed

The final manuscript-transformer commit

`0b464b3914bf358a4b296d1942df09b5aea9a5e5`

received a GitHub Actions bot success report after:

- Rev5 generation;
- full LaTeX compilation;
- artifact upload.

Thus the exact source state containing the WP35 correction, both figure references, conservative Dechant wording, and explicit `S_pre` definition is mechanically verified.

---

## 5. Final claim/citation pass

The bibliography and all externally comparative manuscript claims were reviewed again.

No direct theorem collision was identified beyond the already-recorded prior-art neighborhoods.

Publication-safe posture remains:

- Poisson marking/FI: established;
- Wiener theorem: established;
- Parseval: established;
- survival/hazard calculus: established;
- TCSPC/IRF information loss: established;
- finite-frequency response/noise inequalities: established;
- synchronous detection/reference clocks: established.

Candidate contribution is the **combined resource-completeness architecture** and its explicit no-go/repair logic for autonomous photodetection event channels.

---

## 6. Durable state files synchronized

The following were refreshed so a replacement agent does not regress to stale Rev4-build or registration-edge claims:

- `AGENTS.md`
- `docs/CURRENT_RESEARCH_STATE.md`
- `ROADMAP.md`

A dedicated final audit was added:

- `docs/MANUSCRIPT_REV5_FINAL_AUDIT.md`

---

## 7. Current publication decision

The autonomous-event theorem no longer needs additional foundational derivations before a submission-package decision.

The next work should be packaging/editorial:

1. persist the verified generated Rev5 source;
2. return CI to a clean read-only compile of committed Rev5;
3. prepare journal/submission source packaging;
4. only reopen theory if a concrete referee-style objection exposes a missing assumption or theorem defect.

---

## Status

**AUTONOMOUS EVENT THEOREM: SCIENTIFICALLY CLOSED FOR FIRST-PAPER SCOPE**

**WP35: APPLIED AND BUILD VERIFIED**

**FINAL CLAIM/CITATION PASS: PASSED**

**REV5 GENERATED BUILD + ARTIFACT UPLOAD: VERIFIED PASSED**

**NEXT STATE: SUBMISSION PACKAGE**
