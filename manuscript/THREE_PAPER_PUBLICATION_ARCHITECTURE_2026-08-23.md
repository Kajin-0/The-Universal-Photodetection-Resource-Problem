# Three-paper publication architecture — 2026-08-23

## Decision

Do **not** concatenate the temporal-information results into one omnibus manuscript.

The program is stronger as three distinct papers with explicit logical links:

1. **Flagship conceptual paper — PRX Quantum**
   - *Two spectral-resource regimes for autonomous temporal information*
   - establishes the survival/synthesis split;
   - R3 is the frozen scientific theorem/proof baseline;
   - R4 is a narrow publication-layer bridge revision only.

2. **Broad operational survival paper**
   - *Spectral Resource Laws for Temporal Fisher Information*
   - establishes the broader random-time / spectral-survival theory and photodetection-facing consequences;
   - remains scientifically independent rather than being absorbed into the flagship.

3. **Dynamical completion — Physical Review A**
   - *Exact minimum unitary coupling cost of prescribed rank-changing quantum-state curvature*
   - proves the exact implementation variational theorem
     `V_min(C)=(1/2)Tr C`;
   - in the clean autonomous single-gap specialization,
     `A_ex^(2)=hbar nu V_min`;
   - supplies the dynamical meaning of the flagship paper's rank-boundary synthesis resource.

## Why this architecture is preferred

The flagship paper carries the broad conceptual thesis:

`finite affine radius -> pre-existing spectral survival`

versus

`rank boundary -> positive second-order synthesis`.

The implementation-cost paper answers the most important follow-up objection without forcing its full proof machinery into the flagship:

> Is the boundary synthesis action only a kinematic positivity/Hessian quantity, or does it correspond to an actual minimum physical implementation strength?

Within the stated unitary-dilation implementation class the answer is exact:

`A_ex^(2)=hbar nu V_min`.

The random-time spectral-resource paper remains broader in operational scope and direct photodetection relevance. Combining all three would blur the main thesis, enlarge referee surface area, and make each result harder to evaluate independently.

## Controlled PRXQ R4 bridge

R4 is generated deterministically from the frozen R3 manuscript by

`manuscript/autonomous_temporal_information/apply_prxq_r4_dynamical_bridge.py`.

It changes only the late `Relation to prior work and scope` / `Discussion` layer. All theorem/proof material before that section is required to remain byte-for-byte identical to R3 by

`manuscript/autonomous_temporal_information/check_prxq_r4_bridge.py`.

The bridge states the companion result

`V_min(C)=(1/2)Tr C,    A_ex^(2)=hbar nu V_min`

and explicitly says:

- the action remains kinematic in its definition in the flagship paper;
- the companion result is not used in any flagship proof;
- the coupling functional is not thermodynamic work;
- no peak/operator-norm coupling, controller bandwidth, ancilla dimension, or externally fixed controller-spectrum optimum is claimed.

The companion is cited anonymously during anonymous-review preparation. Replace the anonymous companion entry with the actual public preprint/article metadata as soon as a citable identifier exists.

## R4 verification

Final PR-triggered verification:

- run `32674844366`;
- R3 deterministic regeneration: PASS;
- existing R3 theorem/static identity gate: PASS;
- R4 deterministic bridge generation: PASS;
- R4 byte-freeze/title/scope gate: PASS;
- R4 main compile: PASS;
- unchanged M2R3 supplement compile: PASS;
- artifact upload: PASS.

Final artifact:

- ID `9502376602`;
- SHA-256 `8e32c8248050ffa8be254d86f2f0a5724ef0e3edd1a9e2cf38cbc3a17ca3ed76`;
- R4 main: 20 pages;
- M2R3 supplement: 25 pages.

Render QA at 180 dpi verified:

- unchanged title presentation;
- clean bridge Eq. (56);
- clean revised Discussion;
- explicit rendered companion title in Ref. 18;
- no clipping, overlap, black squares, or broken glyphs in the modified pages;
- unchanged supplement title remains consistent with the flagship title.

## Submission order

Default strategy:

1. submit the PRX Quantum flagship first;
2. keep *Spectral Resource Laws for Temporal Fisher Information* as the broad operational/spectral paper on its own publication track;
3. submit the exact unitary-coupling paper as the dynamical completion, naturally targeted to PRA.

If papers 1 and 3 become public close together, replace the anonymous companion citation in R4 with the public arXiv/DOI metadata before final submission or revision.

## Future unification

Do not create an omnibus paper now. A later synthesis/resource-theory article becomes justified only after the component results have survived external peer review and there is genuinely new unifying structure, applications, or independent uptake. Such a future article should derive a broader framework rather than concatenate already-published manuscripts.

## Significance discipline

Do not use prize-level or Nobel framing in manuscripts, cover letters, abstracts, or repository scientific claims. The present objective is to make each result independently rigorous, falsifiable where applicable, and difficult to overturn. Broader historical significance can only be assessed after independent scrutiny, adoption, and physical consequences.
