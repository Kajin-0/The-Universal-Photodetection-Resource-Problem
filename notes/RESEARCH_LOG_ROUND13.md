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

The scientific base manuscript remains:

`manuscript/event_resource_theorem_rev3.tex`

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

## 3. Rev4 integration strategy

Rev3 is deliberately left immutable.

`manuscript/apply_rev4.py` deterministically generates a Rev4 candidate from Rev3. The script uses exact single-occurrence replacement assertions and adds only:

- figure packages;
- resource-hierarchy figure;
- WP34 resource-cost corollary;
- exact jitter-no-go figure;
- one Discussion sentence highlighting `mathfrak H >= 4 B q`.

Python syntax check: PASSED.

All generator anchors were checked against the reconstructed Rev3 source.

---

## 4. Figure validation

Two theorem figures are retained.

### `figure_resource_hierarchy.tex`

Final design contains only the intrinsic event theorem layers:

1. incident Poisson source -> autonomous marked kernel -> primary electrical record;
2. atomic timing mass;
3. collision resource `mathfrak R_2`;
4. local hazard capacity `mathfrak H`.

The source-synchronous clock/control box was deliberately removed from the diagram because it was visually competitive and conceptually belongs to a separate no-go theorem.

Local minimal RevTeX/TikZ compile: PASSED.

Visual overlap/clipping audit: PASSED.

Overfull/underfull warning audit: PASSED.

### `figure_jitter_no_go.tex`

Uses exact WP33 data for three progressively more extreme prompt/rare-tail families at the same mean `mu0=2 sigma` and exact variance `sigma^2`.

CSV values were checked against the exact formula.

Default point markers were removed; line styles now distinguish the three curves cleanly.

Local minimal RevTeX/pgfplots compile: PASSED.

Visual audit: PASSED.

---

## 5. CI experiment and final safe workflow

The branch workflow now targets generated Rev4:

`.github/workflows/manuscript-check.yml`

It performs:

1. checkout;
2. `python manuscript/apply_rev4.py`;
3. LaTeX compile of `event_resource_theorem_rev4.tex`;
4. artifact upload of PDF and generated TeX.

Two temporary observability experiments were attempted because the available connector does not expose ordinary push-triggered run listing:

- post a success marker to Issue #12;
- persist the generated Rev4 source after successful compile.

Neither produced an observable run from connector-authored commits. Both temporary reporting/persistence behaviors were removed so future human pushes are not surprised by side effects.

Current workflow is read-only except artifact upload.

**Do not claim a verified full Actions compile.**

---

## 6. What is currently verified

### Scientifically

Rev3 theorem/proof structure remains verified:

- input Poisson FI normalization;
- exact marked-event transfer;
- Wiener atomic residue;
- Parseval prefactor;
- weighted timing-collision resource;
- hazard-to-collision inequality;
- exact fixed-mean/fixed-variance no-go;
- free-clock no-go;
- restricted thermodynamic bridge;
- rare-fast stationary-thermodynamic no-go.

### Mechanically

Verified locally:

- Rev4 generator Python syntax;
- Rev4 replacement anchors against Rev3;
- both theorem figures compile;
- both figures visually pass overlap/clipping audit;
- figure test produces no layout warnings.

Not yet directly verified:

- complete Rev4 bibliography-resolved manuscript build through GitHub Actions.

---

## 7. Publication posture

Do not reopen broad theory or materials work before finishing manuscript mechanics.

Immediate priority:

1. obtain a full Rev4 build result when an observable trigger is available;
2. perform final line-by-line claim/citation audit of the generated Rev4 text;
3. decide whether a submission package is justified;
4. defer non-Poisson/nonclassical source extension unless a referee-style review identifies it as necessary.

Supporting audit:

`docs/MANUSCRIPT_REV4_INTEGRATION_AUDIT.md`

---

## Status

**AUTONOMOUS EVENT THEOREM MATHEMATICS: SUBSTANTIALLY CLOSED**

**REV3 SCIENTIFIC MANUSCRIPT BASE: VERIFIED**

**REV4 FIGURE + WP34 INTEGRATION: STAGED AND LOCALLY AUDITED**

**FULL REV4 BUILD: OPEN MECHANICAL GATE**
