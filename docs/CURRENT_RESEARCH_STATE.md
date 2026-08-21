# Current Research State

**Date:** 2026-08-20

Active branch:

`agent/uprp-core-theorem-round10`

## Immediate status

The first-paper foundational research phase is **closed by default**.

Current submission candidate: **Rev8**.

Rev8 is generated reproducibly from frozen Rev7 using:

- `manuscript/apply_rev8_referee_surgical.py`
- `manuscript/REV8_SHA256SUMS.txt`

Read first:

1. `notes/RESEARCH_LOG_ROUND17.md`
2. `submission/PRAPPLIED_PACKAGE_VALIDATION_REV8.md`
3. `notes/REV8_SURGICAL_REVIEW_REPAIRS.md`
4. `AGENTS.md`

Primary submission target:

**Physical Review Applied — Regular Article**

The Rev8 manuscript and PRApplied submission copy have both been fully compiled and visually inspected. Remaining blockers before actual submission are factual/administrative metadata and the final truthful APS substantive-AI disclosure. No additional theorem work is currently required.

---

# Why Rev8 supersedes Rev7

A new hostile Rev7 re-review independently rechecked the principal derivations and found no blocking main-theorem error. It identified exactly one formal Appendix defect and two clarifications.

Rev8 contains only these three changes:

1. **Rare-fast orientation condition.** The Appendix now imposes `acp >= bqs`, which gives exactly

   `f_R-r_R = R(acp-bqs)/(RD+E) >= 0`

   for every `R>0`, placing the family inside the main thermodynamic section's `f>=r` assumption. Strict `acp>bqs` gives strict forward bias.

2. **Branched timing-resource hierarchy.** `R_2`, `B_FI`, and `H` are explicitly identified as the finite-area resources of the absolutely continuous square-integrable timing branch. Atomic or more singular timing measures are classified first by the Wiener residue result and need not have finite Fisher spectral area.

3. **One-way activity definition.** The stationary activity convention is now explicit:

   `A_tot = sum_x pi_x sum_{y != x} W_yx`,

   counting each directed jump once. This makes the normalization of the state-1 activity bound unambiguous.

Nothing else in the theorem stack changed.

---

# Rev8 verification

Frozen Rev7 input had already been independently artifact-verified. Rev8 was generated from that verified artifact and then compiled with bibliography and cross-references.

Generated source hashes:

- main TeX: `07068067744c8cff464931739505e49850c97d68a9c5b9fa63324c6251711a09`
- rare-fast Appendix: `f9afbdf7e0fd6cc1b57a3a4e00197148e907fc9ed7691a7f9dd42106e16ba665`

Canonical generated Rev8 PDF:

- 25 pages
- 364825 bytes
- SHA-256 `bb7dba5a12f5b74181968060b0a6776d7847fad69dfb00090c76425d35974f86`

Visual inspection passed on the finite-area branch paragraph, thermodynamic activity definition, Appendix orientation condition/proof, and shifted reference pages.

Only inherited material TeX warning:

- approximately `2.45667 pt` overfull line involving `timing-concentration`.

No new layout defect was introduced.

---

# PRApplied package

Rev8 PRApplied submission PDF:

- 25 pages
- 365072 bytes
- SHA-256 `60da4f9a3919ffdf64d450b5397755a75109d4fc2a0a374a8132a93931092c37`

Complete Rev8 package ZIP SHA-256:

`5e9085aa99186e9d60f21ca9e7c3daa0661e871ed84248ce54f7c8be30812c81`

The purely mathematical Data Availability statement is included.

The AI acknowledgment remains intentionally unfinished until the human author supplies a literally truthful description of how AI-assisted scientific reasoning, derivations, literature synthesis, and manuscript claims were personally verified.

---

# Steady-state CI

`.github/workflows/manuscript-check.yml` is read-only (`contents: read`).

It:

1. generates Rev8 from frozen Rev7;
2. checks the exact generated-source hashes;
3. compiles Rev8;
4. uploads the verified artifact;
5. performs no source mutation or self-commit.

Temporary PR `#15` is closed unmerged. Temporary validation branch refs were neutralized to the clean publication head.

---

# Core theorem state

For the autonomous, time-translation-invariant, independent-event / low-overlap, one-primary-registration detector class with complete accessible primary-event marks and weak coherent/Poisson direct-detection intensity perturbations:

`G(omega)=integral |H_m(omega)|^2 kappa(dm)`

is the exact source-normalized marked-event transfer spectrum and the spectral multiplier of the complete local weak-waveform Fisher operator.

Pointwise `G_A >= G_B` is necessary and sufficient for local Fisher dominance across every admitted finite weak temporal task.

For square-integrable delay densities,

`integral G d omega = pi R_2`,

and

`B_FI = R_2/(4 eta)`.

If conditional hazards satisfy `h_m<=Lambda(m)`, then `R_2<=H`, giving `B_FI<=H/(4 eta)` and the inverse timing-resource cost `H>=4Bq` for absolute band retention `q` over ordinary-frequency half-band `B`.

Exact mean and variance do not bound finite temporal information bandwidth. A free synchronous reference defeats detector-only timing bounds. Aggregate stationary thermodynamic quantities alone do not supply the missing absolute local time scale.

---

# Scope discipline

Do not call this a universal all-detector speed limit.

Do not claim generic Blackwell dominance, generic Fisher-transfer novelty, a fixed-FWHM no-go, or generic finite-frequency response/noise novelty.

High-flux/history-dependent capture, coherent pointers, continuous analog detectors, nonclassical sources, and QFI/capacity generalizations remain outside this first paper unless a concrete referee defect forces reopening.

---

# Next action

**Stop broad first-paper revision.**

Remaining submission inputs required from the human author:

- author name/order;
- affiliation;
- corresponding-author email;
- ORCID;
- truthful human-verification wording for APS substantive-AI disclosure;
- applicable funding, conflict, and prior-submission declarations.

After those are supplied: insert metadata, finalize acknowledgment, compile once, inspect changed pages, and produce the portal-upload bundle.
