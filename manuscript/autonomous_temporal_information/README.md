# Autonomous temporal information manuscript workspace

**Branch:** `agent/autonomous-temporal-information-law`

This directory is the manuscript workspace for the post-Rev11 autonomous temporal-information theorem package. It is intentionally separate from the frozen Rev11 manuscript lineage in `manuscript/`.

## Current phase

**Phase M2: proof integration and hostile manuscript audit.**

Research theorem production is paused. Do not create WP21 unless manuscript drafting exposes a concrete mathematical defect or genuinely missing theorem.

Authoritative research scope lock:

`../../autonomous_temporal_information/notes/PUBLICATION_THEOREM_STACK_AFTER_AUDITS.md`

Mandatory audit records:

- `../../autonomous_temporal_information/notes/HOSTILE_MATHEMATICAL_AUDIT_WP18_WP20.md`
- `../../autonomous_temporal_information/notes/FOUNDATIONAL_SIGNIFICANCE_PRIORITY_GATE_AFTER_WP20.md`
- `THEOREM_PROVENANCE_MATRIX.md`
- `MANUSCRIPT_HANDOFF.md`

## Canonical M2 sources

- `autonomous_temporal_resource_law_m2.tex` — canonical main manuscript; theorem statements plus concise proof cores.
- `autonomous_temporal_resource_law_supplement_m2.tex` — canonical supplement master.
- `proofs/finite_radius_survival_proofs.tex` — WP02/WP03/WP06 proof block.
- `proofs/boundary_and_autonomous_action_proofs.tex` — WP07/WP09/WP18 proof block.
- `proofs/noncommuting_mixed_bridge_proof.tex` — WP11/WP13/WP19 mixed bridge.
- `proofs/multigap_action_sum_proof.tex` — WP20 shared-Hessian sum and simultaneous Fourier saturation.
- `proofs/wp15_exact_common_record_qutrit.tex` — exact `55/8` common-record witness and limiting projective sequence.
- `references.bib` — verified seed bibliography including PSD-cone and shorted-operator prior mathematics.
- `check_m2_tex_static.py` — recursive static gate for labels, refs, citations, inputs, and draft markers.

The earlier files `autonomous_temporal_resource_law_draft.tex` and `autonomous_temporal_resource_law_supplement.tex` are **archival M1 snapshots**, not current drafting targets.

## Working title

**Two spectral-resource regimes for autonomous temporal information**

Alternative retained for later comparison:

**Pre-existing survival and synthesis action constrain relational temporal information**

## Main-text scope

1. fixed-mean-energy local-Fisher no-go and tangent-radius repair;
2. autonomous dual survival;
3. rank-changing one-sided/bilateral synthesis;
4. sharp autonomous dual synthesis action;
5. arbitrary coherent-support mixed bridge;
6. sharp multi-gap spectral-action sum.

## Main physical claim

The candidate contribution is a two-regime local resource principle for globally stationary relative temporal information:

- `R_lin > 0`: Fisher information weighted by affine physical radius is bounded by pre-existing two-sided spectral survival;
- rank-changing `R_lin = 0`: useful Fisher information is bounded by positive second-order endpoint synthesis, producing a two-sided autonomous synthesis-action law.

The action is a **kinematic state-family endpoint-incidence resource**. It is not claimed to equal total implementation energy.

## Claim discipline

Do not claim a new resource theory of time, a new Page--Wootters mechanism, new modes-of-asymmetry theory, a new generic QFI principle, or a universal implementation-energy law.

Priority remains **unverified, not certified**. The literature gate supports only a narrow theorem-paper claim.

## Build and integrity gate

`.github/workflows/autonomous-temporal-manuscript-check.yml` is isolated from the frozen Rev11 workflow. It now:

1. runs `python check_m2_tex_static.py`;
2. compiles `autonomous_temporal_resource_law_m2.tex`;
3. compiles `autonomous_temporal_resource_law_supplement_m2.tex`;
4. uploads the M2 sources, PDFs, proof modules, and handoff artifacts.

Do not call the M2 manuscript build-verified until a concrete successful Actions job result/log is retrieved. The current connector cannot expose push-triggered run status directly.

## Next work

1. hostile theorem-language audit of the M2 main against the exact proof modules;
2. source-level notation and dimensional audit across main/supplement;
3. add any missing benchmark definitions required for the supplement to be self-contained;
4. only after those gates, perform publication-style abstract/introduction compression and journal positioning;
5. no new theorem work unless one of these audits exposes a real gap.
