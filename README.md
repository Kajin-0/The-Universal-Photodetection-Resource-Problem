# The Universal Photodetection Resource Problem

**Status synchronized:** 2026-08-23

The repository is authoritative; chat history is not.

## Current publication architecture

The active temporal-information program is intentionally split into **three papers rather than one omnibus manuscript**:

1. **PRX Quantum flagship:** *Two spectral-resource regimes for autonomous temporal information*.
   - R3 is the frozen scientific theorem/proof baseline.
   - R4 is the current journal-facing publication layer and adds only a compact dynamical bridge.
2. **Broad operational paper:** *Spectral Resource Laws for Temporal Fisher Information*.
   - random-time/spectral-survival theory and photodetection-facing consequences;
   - remains on its own publication track.
3. **PRA dynamical completion:** *Exact minimum unitary coupling cost of prescribed rank-changing quantum-state curvature*.
   - final reviewer-repaired PRA R1 package;
   - proves the exact variational implementation result.

Authoritative architecture note:

`manuscript/THREE_PAPER_PUBLICATION_ARCHITECTURE_2026-08-23.md`

Authoritative manuscript handoffs:

- flagship: `manuscript/autonomous_temporal_information/MANUSCRIPT_HANDOFF.md`;
- dynamical companion: `manuscript/dynamical_implementation_cost/MANUSCRIPT_HANDOFF.md`.

Paper 1 / Rev11 and Paper 2 / Rev7 remain frozen. WP31 is superseded; WP32 is the canonical exact energy-conserving implementation theorem and WP33 is its hostile-audit PASS.

## Flagship conceptual law

The flagship separates two mechanisms that a local Fisher metric alone conflates:

`finite affine physical radius -> pre-existing spectral survival`

versus

`rank-changing zero radius -> positive second-order synthesis action`.

For the clean autonomous boundary problem, the separate unitary-coupling companion now supplies the missing dynamical interpretation:

`V_min(C)=(1/2)Tr C`,

`A_ex^(2)=hbar nu V_min`.

R4 mentions this equality only in its late scope/discussion layer. The companion theorem is **not used in any flagship proof** and its proof machinery is not imported into the PRXQ paper.

## PRX Quantum R4 status

Title remains:

> **Two spectral-resource regimes for autonomous temporal information**

R4 is generated deterministically from the frozen R3 paper by

`manuscript/autonomous_temporal_information/apply_prxq_r4_dynamical_bridge.py`.

The gate `check_prxq_r4_bridge.py` requires the entire R3 theorem/proof prefix to remain byte-for-byte unchanged, preserves theorem/proposition/corollary counts, and confines the revision to the late prior-work/scope and Discussion layer.

Final R4 verification:

- workflow run `32674844366` — **PASS**;
- frozen R3 regeneration/static theorem gate — **PASS**;
- R4 bridge generation/freeze gate — **PASS**;
- R4 main compile — **PASS**;
- unchanged M2R3 supplement compile — **PASS**;
- artifact upload — **PASS**.

Final R4 artifact:

- ID `9502376602`;
- SHA-256 `8e32c8248050ffa8be254d86f2f0a5724ef0e3edd1a9e2cf38cbc3a17ca3ed76`;
- main: **20 pages**;
- supplement: **25 pages**;
- render QA: **PASS**.

The bridge equation, revised Discussion, and explicit anonymous companion reference were visually inspected. The companion reference should be replaced with public arXiv/DOI metadata when available.

## PRA dynamical completion

Journal-facing title:

> **Exact minimum unitary coupling cost of prescribed rank-changing quantum-state curvature**

Central theorem:

`V_min(C;D,rho_0)=(1/2)Tr C`.

The final hostile review found no blocking mathematical error. The reviewer-repaired package also makes explicit that the infinite-dimensional optimizer may use an unbounded generator and an optimized ancilla spectrum; no peak/operator-norm coupling, controller-bandwidth, ancilla-dimension, or fixed-controller-spectrum optimum is claimed.

Final PRA verification:

- workflow run `32673160217` — **PASS**;
- artifact `9501942180`;
- SHA-256 `4236d6f514b2f290d302062ab4c7a599c03c817da259f3d9715b787a4d37d640`;
- 11-page main / 10-page supplement;
- render QA: **PASS**.

## Scientific and novelty discipline

Priority remains **unverified, not certified**.

Do not claim novelty for generic Bures/Uhlmann/SLD-QFI purification geometry, Riemannian Bures curvature, covariant Stinespring dilation, generic quantum-speed-limit/control-norm bounds, classical nonregular boundary statistics, or standard second-order PSD-cone geometry.

Do not use Nobel/prize-level framing in manuscripts, cover letters, abstracts, or scientific repository claims. The objective is independent peer-review survival, external use, and physical consequences.

## Current work order

1. preserve R3 theorem/proof content unchanged;
2. preserve R4 as the current PRXQ submission layer;
3. preserve the reviewer-repaired PRA companion as a separate paper;
4. keep *Spectral Resource Laws for Temporal Fisher Information* independent rather than concatenating the program;
5. replace the anonymous R4 companion citation with public metadata when available;
6. immediately before each submission, re-check then-current journal policies and replace anonymous author/affiliation metadata;
7. reopen scientific theorem development only for a genuine proof defect, direct prior-art collision, referee/editor requirement, or a deliberately separate new research program.

## Manuscript integrity

Every public-facing paper must remain scientifically standalone and free of personal repository identifiers, internal development labels, or dependencies on private research files.
