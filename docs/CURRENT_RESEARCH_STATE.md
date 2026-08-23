# Current Research State

**Last synchronized:** 2026-08-23

**Active branch:** `agent/autonomous-temporal-information-law`

## Frozen scientific layers

- Paper 1 Rev11;
- Paper 2 Rev7;
- random-time spectral-resource Rev11;
- autonomous temporal-information **R3 theorem/proof baseline**;
- audited D2 unitary-coupling theorem/proof baseline.

**Canonical post-R3 implementation theorem:** WP32.

**Hostile theorem audit:** WP33 — PASS under stated assumptions.

**WP31 is superseded.**

## Current publication architecture

Do **not** concatenate the active temporal-information results into one omnibus paper.

1. **PRX Quantum flagship:** *Two spectral-resource regimes for autonomous temporal information*.
   - R3 = frozen scientific baseline.
   - R4 = current journal-facing bridge revision.
2. **Broad operational spectral paper:** *Spectral Resource Laws for Temporal Fisher Information*.
   - random-time/spectral-survival and photodetection-facing theory;
   - independent publication track.
3. **PRA dynamical completion:** *Exact minimum unitary coupling cost of prescribed rank-changing quantum-state curvature*.
   - final reviewer-repaired PRA R1 package.

Architecture record:

`manuscript/THREE_PAPER_PUBLICATION_ARCHITECTURE_2026-08-23.md`.

## Unified scientific picture

The flagship establishes

`finite affine radius -> pre-existing spectral survival`

versus

`rank boundary -> positive second-order synthesis action`.

The separate implementation paper closes the principal dynamical question:

`V_min(C)=(1/2)Tr C`,

and in the clean autonomous single-gap specialization,

`A_ex^(2)=hbar nu V_min`.

Thus the flagship's synthesis action remains kinematic in definition but has an exact minimum state-weighted quadratic unitary-coupling interpretation in the companion implementation problem.

## PRX Quantum R4

R4 is a controlled publication-layer revision generated from frozen R3 by

`manuscript/autonomous_temporal_information/apply_prxq_r4_dynamical_bridge.py`.

Its integrity gate requires the entire theorem/proof prefix before `Relation to prior work and scope` to remain byte-for-byte identical to R3, keeps theorem/proposition/corollary counts unchanged, and requires the scope limitations around the companion result.

The bridge explicitly says the companion theorem:

- is not used in any flagship proof;
- is not a thermodynamic-work identity;
- does not bound peak/operator-norm coupling;
- does not optimize controller bandwidth or ancilla dimension;
- does not claim exact attainment for an externally fixed controller spectrum.

Final R4 verification:

- workflow run `32674844366` — **PASS**;
- R3 regeneration/static theorem gate — **PASS**;
- R4 deterministic bridge/freeze gate — **PASS**;
- R4 main compile — **PASS**;
- unchanged M2R3 supplement compile — **PASS**;
- artifact upload — **PASS**.

Artifact:

- ID `9502376602`;
- SHA-256 `8e32c8248050ffa8be254d86f2f0a5724ef0e3edd1a9e2cf38cbc3a17ca3ed76`;
- R4 main: **20 pages**;
- M2R3 supplement: **25 pages**;
- render QA: **PASS**.

## PRA unitary-coupling companion

Title:

> **Exact minimum unitary coupling cost of prescribed rank-changing quantum-state curvature**

Central result:

`V_min(C;D,rho_0)=(1/2)Tr C`.

WP32 proves the exact optimum under total-energy conservation in the stated separable infinite-dimensional model, including spectator curvature in target-energy shells unoccupied at baseline.

Final reviewer-repair verification:

- workflow run `32673160217` — **PASS**;
- artifact ID `9501942180`;
- SHA-256 `4236d6f514b2f290d302062ab4c7a599c03c817da259f3d9715b787a4d37d640`;
- 11-page main / 10-page supplement;
- render QA: **PASS**.

## Prior-art / claim boundary

Priority remains **unverified, not certified**.

Do not claim novelty for Bures/Uhlmann/SLD-QFI horizontal geometry, Riemannian Bures curvature, covariant Stinespring dilation, generic QSL/control-norm results, classical nonregular boundary statistics, or standard PSD-cone second-order tangent geometry.

The candidate distinct content is the survival/synthesis resource split and sharp spectral laws, together with the separate exact prescribed-curvature unitary-coupling completion under its stated implementation class.

Do not use Nobel/prize-level framing in scientific or submission-facing materials.

## Immediate work

1. preserve R3 theorem/proof content;
2. treat R4 as the current PRXQ journal-facing package;
3. keep the broad random-time paper and PRA companion independent;
4. replace the anonymous R4 companion reference with public arXiv/DOI metadata when available;
5. immediately before submission, re-check current journal metadata/disclosure requirements and replace anonymous author/affiliation data;
6. reopen theory only for a genuine defect, direct prior-art collision, referee/editor requirement, or deliberately separate research program.

All public-facing manuscripts must remain standalone and free of personal repository identifiers or internal dependencies.
