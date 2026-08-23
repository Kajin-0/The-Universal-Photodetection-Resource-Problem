# Manuscript handoff — autonomous temporal information

**Date:** 2026-08-23

**Branch:** `agent/autonomous-temporal-information-law`

## Canonical manuscript state

The scientific theorem/proof baseline remains **PRX Quantum R3**, build-verified and science-frozen.

The current journal-facing flagship is now **PRX Quantum R4**, a deliberately narrow publication-layer bridge revision generated from R3. R4 does **not** import the companion implementation-cost proof or alter any earlier theorem/proof statement.

Flagship title remains:

> **Two spectral-resource regimes for autonomous temporal information**

Canonical generation chain:

- `apply_m2r2_review_repairs.py`
- `apply_submission_cleanup_r2.py`
- `apply_m2r3_boundary_strengthening.py`
- `apply_prxq_frontmatter_r3.py` -> frozen R3 baseline
- `apply_prxq_r4_dynamical_bridge.py` -> R4 publication-layer bridge

Integrity gates:

- `check_m2_tex_static.py` — existing R3 theorem/identity/standalone gate;
- `check_prxq_r4_bridge.py` — requires all text before `Relation to prior work and scope` to remain byte-for-byte identical to R3, keeps the disclosure/data/bibliography source tail fixed, preserves theorem/proposition/corollary counts, and requires the exact bridge/scope markers.

The canonical supplement remains the unchanged `autonomous_temporal_resource_law_supplement_m2r3.tex`.

## R3 scientific scope — frozen

R3 establishes the finite-radius survival / rank-boundary synthesis resource split, including:

- arbitrary-finite-copy collective-measurement survival laws;
- autonomous two-sided survival;
- one-sided/bilateral rank-boundary synthesis;
- sharp `hbar nu/4` and `hbar nu/2` action coefficients;
- pure-boundary SLD-QFI action corollary;
- spectator-curvature no-go;
- coherent-support mixed theorem and audited `Psi_a` envelope;
- exact qutrit hierarchy `12 > 43/4 > 55/8`;
- multi-gap shared-Hessian action sum.

Do not modify this theorem/proof layer merely because the companion paper exists.

## R4 dynamical bridge — publication layer only

R3 previously described the endpoint synthesis action as kinematic and listed derivation of a dynamical implementation cost as an open problem.

That particular open problem has now been solved in the separate implementation-cost manuscript. R4 therefore adds one late-scope bridge:

`V_min(C)=(1/2)Tr C`

and, for the clean single-gap autonomous specialization,

`A_ex^(2)=hbar nu V_min`.

The bridge states explicitly that:

- the flagship action remains kinematic in definition;
- the companion variational theorem is not used in any R3/R4 proof;
- the result applies to the companion paper's stated unitary-dilation implementation class;
- the coupling functional is not thermodynamic work;
- it is not a peak/operator-norm coupling bound;
- it does not optimize controller bandwidth, ancilla dimension, or a fixed external controller spectrum.

The companion citation is currently anonymous for review preparation:

> *Exact minimum unitary coupling cost of prescribed rank-changing quantum-state curvature*, companion manuscript.

Replace that entry with public arXiv/DOI metadata as soon as a citable public identifier exists.

## Final R4 verification

Final PR-triggered run:

- workflow run `32674844366`;
- R3 deterministic regeneration: **PASS**;
- R3 theorem/static identity gate: **PASS**;
- R4 deterministic generation: **PASS**;
- R4 byte-freeze/title/scope gate: **PASS**;
- R4 main compile: **PASS**;
- unchanged M2R3 supplement compile: **PASS**;
- artifact upload: **PASS**.

Final artifact:

- ID `9502376602`;
- SHA-256 `8e32c8248050ffa8be254d86f2f0a5724ef0e3edd1a9e2cf38cbc3a17ca3ed76`;
- R4 main: **20 pages**;
- M2R3 supplement: **25 pages**.

Render QA at 180 dpi checked the modified main pages and package identity:

- title page clean and unchanged;
- bridge Eq. (56) clean;
- revised Discussion clean;
- Ref. 18 visibly gives the companion title;
- no clipping, overlap, black squares, or broken glyphs on modified pages;
- supplement title remains consistent with the flagship title.

Disposable PR #34 was closed unmerged after verification.

## Three-paper publication architecture

Authoritative strategy note:

`../THREE_PAPER_PUBLICATION_ARCHITECTURE_2026-08-23.md`

Do **not** concatenate the program into one omnibus manuscript.

1. **PRX Quantum flagship:** *Two spectral-resource regimes for autonomous temporal information* — conceptual survival/synthesis law; R4 adds only the compact dynamical bridge.
2. **Broad operational paper:** *Spectral Resource Laws for Temporal Fisher Information* — random-time/spectral-survival and photodetection-facing theory; keep independent.
3. **PRA dynamical completion:** *Exact minimum unitary coupling cost of prescribed rank-changing quantum-state curvature* — exact variational implementation theorem and energy-conserving attainability.

The logical chain is:

`finite radius -> spectral survival`

versus

`rank boundary -> synthesis action -> exact minimum unitary coupling`.

The last arrow is supplied by the separate companion paper, not by expanding the flagship proof stack.

## Post-R3 theorem status

WP32 remains the canonical exact energy-conserving infinite-dimensional implementation theorem; WP33 hostile audit remains PASS. WP31 is superseded.

For prescribed feasible positive metric-contracted target-kernel Hessian `C`,

`V_min=(1/2)Tr C`.

The exact optimum survives under total-energy conservation in the companion implementation model, including the stated separable infinite-dimensional setting and spectator curvature in target-energy shells unoccupied at baseline.

## Claim / significance discipline

Do not claim novelty for generic Bures/Uhlmann/SLD geometry, covariant Stinespring dilation, Bures Riemannian curvature, generic QSL/control-norm bounds, classical nonregular boundary statistics, or standard PSD-cone second-order geometry.

Priority remains **unverified, not certified**.

Do not use Nobel/prize-level framing in the paper, cover letter, abstract, or scientific repository claims. The immediate objective is independent peer-review survival and external uptake.

## Immediate work order

1. treat R3 theorem/proof content as frozen;
2. treat R4 as the current PRXQ journal-facing flagship package;
3. do not import the companion proof into R4;
4. keep the random-time spectral-resource paper and unitary-coupling paper on separate publication tracks;
5. before actual submission, replace anonymous author/affiliation metadata and update the companion citation if public metadata exists;
6. re-check then-current APS/PRX Quantum submission and disclosure requirements immediately before submission;
7. reopen R4 theorem content only for a genuine proof defect, direct prior-art collision, or referee/editor requirement.

## Manuscript integrity

Every public-facing file must remain scientifically standalone and free of personal repository URLs, usernames, repository/project names, internal work-package labels, development history, or instructions to consult internal research files.
