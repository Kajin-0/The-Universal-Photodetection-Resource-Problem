# Autonomous temporal information manuscript workspace

**Branch:** `agent/autonomous-temporal-information-law`

## Current state

**PRX Quantum R4 is the current journal-facing flagship. R3 remains the frozen scientific theorem/proof baseline.**

Flagship title:

> **Two spectral-resource regimes for autonomous temporal information**

R4 is intentionally narrow. It is generated from R3 only to connect the already-proved kinematic rank-boundary synthesis action to the separately proved unitary-coupling variational theorem. It does not import the companion proof or alter the theorem stack.

Authoritative handoff:

`MANUSCRIPT_HANDOFF.md`

Program-level publication strategy:

`../THREE_PAPER_PUBLICATION_ARCHITECTURE_2026-08-23.md`

## Scientific center

The flagship establishes two resource regimes for autonomous relative temporal information:

- `R_lin > 0`: Fisher information over a finite physical tangent neighborhood requires pre-existing two-sided spectral survival;
- rank-changing `R_lin = 0`: useful temporal information is supported by positive second-order endpoint synthesis, with sharp autonomous action coefficients.

R3 contains the complete frozen theorem story, including finite-copy collective measurements, bilateral/one-sided boundary laws, SLD-QFI boundary corollary, spectator-curvature no-go, coherent-support mixed geometry, qutrit benchmark hierarchy, and multi-gap shared-Hessian action sum.

## R4 bridge

R4 corrects one now-obsolete scope statement. The R3 Discussion had listed derivation of a dynamical implementation cost for the kinematic action as an open problem.

The separate companion paper now proves, for its stated unitary-dilation implementation class,

`V_min(C)=(1/2)Tr C`,

and in the clean single-gap autonomous specialization,

`A_ex^(2)=hbar nu V_min`.

R4 therefore states that the action is still **kinematic in definition** in the flagship, but has an exact **minimum unitary-coupling interpretation** in the companion implementation problem.

The bridge explicitly does **not** identify the action with thermodynamic work, peak/operator-norm coupling, controller bandwidth, ancilla dimension, or the optimum for an externally fixed controller spectrum.

## Deterministic source chain

1. `apply_m2r2_review_repairs.py`
2. `apply_submission_cleanup_r2.py`
3. `apply_m2r3_boundary_strengthening.py`
4. `apply_prxq_frontmatter_r3.py` -> frozen R3
5. `apply_prxq_r4_dynamical_bridge.py` -> current R4

Integrity gates:

- `check_m2_tex_static.py` — R3 theorem/identity/standalone gate;
- `check_prxq_r4_bridge.py` — freezes the theorem/proof prefix byte-for-byte to R3, preserves the late disclosure/data source tail, preserves theorem/proposition/corollary counts, and requires the bridge/scope markers.

The supplement remains the unchanged M2R3 supplement.

## Final R4 verification

Workflow run `32674844366`: **PASS**.

Passed stages:

- R3 regeneration;
- R3 static theorem/identity gate;
- R4 bridge generation;
- R4 byte-freeze/title/scope gate;
- R4 main compile;
- unchanged M2R3 supplement compile;
- artifact upload.

Artifact:

- ID `9502376602`;
- SHA-256 `8e32c8248050ffa8be254d86f2f0a5724ef0e3edd1a9e2cf38cbc3a17ca3ed76`;
- R4 main: 20 pages;
- supplement: 25 pages.

Render QA at 180 dpi: **PASS**. The bridge equation, revised Discussion, and explicit companion reference all render cleanly. No clipping, overlap, broken glyphs, or package-title mismatch was found on the modified pages.

## Three-paper architecture

Do not concatenate the program.

1. **PRX Quantum:** *Two spectral-resource regimes for autonomous temporal information* — conceptual flagship.
2. **Independent broad spectral paper:** *Spectral Resource Laws for Temporal Fisher Information* — random-time/spectral-survival and photodetection-facing theory.
3. **PRA companion:** *Exact minimum unitary coupling cost of prescribed rank-changing quantum-state curvature* — exact dynamical completion.

The intended logical chain is

`survival` **versus** `synthesis -> minimum unitary coupling`.

A later unification paper should be considered only after the component papers survive external review and genuinely new synthesis becomes possible; do not create an omnibus manuscript now.

## Claim discipline

Priority remains **unverified, not certified**.

Do not claim a new general resource theory of time, new Page-Wootters mechanism, new generic QFI principle, generic Bures geometry, generic covariant dilation theory, or universal implementation-energy law.

Do not use Nobel/prize-level framing in publication-facing material.

## Immediate work

1. preserve R3 theorem/proof content unchanged;
2. preserve R4 as the current journal-facing bridge revision;
3. replace the anonymous companion citation with public arXiv/DOI metadata when available;
4. immediately before submission, re-check current APS/PRX Quantum requirements and replace anonymous author/affiliation metadata;
5. do not add the full unitary-coupling proof to the flagship.
