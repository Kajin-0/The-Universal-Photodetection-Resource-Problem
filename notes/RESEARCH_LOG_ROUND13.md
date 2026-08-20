# Research Log — Round 13

**Date:** 2026-08-20

## Purpose
Checkpoint the autonomous-event project after theorem discovery gave way to publication hardening.

The detailed HgCdTe/Kane WP17–24 branch remains frozen.

---

## 1. No new detector-physics branch was opened

The project stayed on the original UPRP publication path.

Current mature detector class:

- autonomous/time-translation-invariant;
- weak coherent/direct-detection intensity modulation;
- independent low-overlap incident events;
- one sufficient primary electrical registration per incident photon;
- complete accessible primary-event mark retained.

The scientifically audited base remains Rev3; the current manuscript source is now compiled Rev4.

---

## 2. WP34 inverse resource-cost theorem promoted

WP34 is the inverse of the WP32/WP25 timing-resource ceiling.

For target source-normalized average information transfer `q` over a flat two-sided band `|omega|<=Omega`, with ordinary-frequency half-band

\[
B=\frac{\Omega}{2\pi},
\]

one necessarily has

\[
\boxed{\mathfrak R_2\ge4Bq,\qquad \mathfrak H\ge4Bq.}
\]

If all conditional hazards satisfy a common ceiling `Lambda`, then

\[
\mathfrak H\le\eta\Lambda
\]

and therefore

\[
\boxed{\Lambda\ge4Bq/\eta.}
\]

For retention `q=r eta` relative to captured DC information,

\[
\boxed{\Lambda\ge4Br.}
\]

This is likely the cleanest operational equation in the paper but must always be presented with the event-channel assumptions and definitions.

The earlier duplicate numbering mistake was repaired: WP33 remains the exact fixed-mean/fixed-variance jitter no-go; the inverse cost theorem is WP34.

Primary note:

`notes/WP34_MINIMUM_TIMING_RESOURCE_COST_THEOREM.md`

---

## 3. Rev4 integration

Rev3 was deliberately preserved as the audited scientific base.

`manuscript/apply_rev4.py` deterministically generated

`manuscript/event_resource_theorem_rev4.tex`.

The script uses exact single-occurrence replacement assertions and added only:

- figure packages;
- resource-hierarchy figure;
- WP34 resource-cost corollary;
- exact jitter-no-go figure;
- one Discussion sentence highlighting `mathfrak H >= 4 B q`.

Python syntax check: PASSED.

All generator anchors were checked against the reconstructed Rev3 source.

The generated Rev4 source was subsequently persisted to the working branch by the temporary verification workflow.

---

## 4. Figure validation

Two theorem figures are retained.

### `figure_resource_hierarchy.tex`

Final design contains only the intrinsic event theorem layers:

1. incident Poisson source -> autonomous marked kernel -> primary electrical record;
2. atomic timing mass;
3. collision resource `mathfrak R_2`;
4. local hazard capacity `mathfrak H`.

The source-synchronous clock/control box was deliberately removed because it was visually competitive and conceptually belongs to a separate no-go theorem.

Local minimal RevTeX/TikZ compile: PASSED.

Visual overlap/clipping audit: PASSED.

Overfull/underfull warning audit: PASSED.

### `figure_jitter_no_go.tex`

Uses exact WP33 data for three progressively more extreme prompt/rare-tail families at the same mean `mu0=2 sigma` and exact variance `sigma^2`.

CSV values were checked against the exact formula.

Default point markers were removed; line styles distinguish the three curves cleanly.

Local minimal RevTeX/pgfplots compile: PASSED.

Visual audit: PASSED.

---

## 5. Full Rev4 CI compile verified

Because ordinary push-run listing was not exposed through the connector, a temporary one-shot reporting step was added after the Rev4 compile and artifact-upload steps.

GitHub Actions bot subsequently posted to Issue #12:

> `Rev4 manuscript verification succeeded for commit 0acd8ca6304585e44c89130ca6b31826884c85a8: deterministic Rev4 generation, LaTeX compilation, and artifact upload all completed successfully.`

This closes the full manuscript mechanical gate for that Rev4 branch state.

A subsequent temporary workflow also persisted the generated Rev4 source to the branch.

After verification, all temporary side effects were removed. The current workflow now simply:

1. checks out the branch;
2. compiles committed `manuscript/event_resource_theorem_rev4.tex`;
3. uploads the PDF and TeX artifacts.

Current workflow:

`.github/workflows/manuscript-check.yml`

---

## 6. What is verified

### Scientifically

The theorem/proof structure remains verified:

- input Poisson FI normalization;
- exact marked-event transfer;
- Wiener atomic residue;
- Parseval prefactor;
- weighted timing-collision resource;
- hazard-to-collision inequality;
- WP34 inverse resource cost;
- exact fixed-mean/fixed-variance no-go;
- free-clock no-go;
- restricted thermodynamic bridge;
- rare-fast stationary-thermodynamic no-go.

### Mechanically

Verified:

- Rev4 generator Python syntax;
- Rev4 replacement anchors against Rev3;
- both theorem figures compile;
- both figures visually pass overlap/clipping audit;
- figure test produces no layout warnings;
- full Rev4 LaTeX compile through GitHub Actions;
- Rev4 artifact upload;
- committed Rev4 source exists on the branch.

---

## 7. Publication posture

The autonomous event theorem mathematics and manuscript mechanics are now substantially closed.

Immediate priority is no longer another derivation. It is:

1. final line-by-line claim/citation audit of committed Rev4;
2. decide journal positioning and submission packaging;
3. clean obsolete draft/build-helper files only if doing so improves submission clarity;
4. defer non-Poisson/nonclassical source extension unless referee-style review identifies it as necessary.

Supporting audit:

`docs/MANUSCRIPT_REV4_INTEGRATION_AUDIT.md`

---

## Status

**AUTONOMOUS EVENT THEOREM MATHEMATICS: SUBSTANTIALLY CLOSED**

**REV3 SCIENTIFIC MANUSCRIPT BASE: VERIFIED**

**REV4 FIGURE + WP34 INTEGRATION: VERIFIED**

**FULL REV4 BUILD + ARTIFACT UPLOAD: VERIFIED PASSED**
