# Autonomous temporal information manuscript workspace

**Branch:** `agent/autonomous-temporal-information-law`

This directory is the manuscript workspace for the post-Rev11 autonomous temporal-information theorem package. It is intentionally separate from the frozen Rev11 manuscript lineage in `manuscript/`.

## Current phase

**Phase M2R1: audited proof integration and referee-facing statement cleanup.**

Research theorem production is paused. Do not create WP21 unless manuscript work exposes a concrete mathematical defect or genuinely missing theorem.

Authoritative research scope lock:

`../../autonomous_temporal_information/notes/PUBLICATION_THEOREM_STACK_AFTER_AUDITS.md`

Mandatory audit records:

- `../../autonomous_temporal_information/notes/HOSTILE_MATHEMATICAL_AUDIT_WP18_WP20.md`
- `../../autonomous_temporal_information/notes/FOUNDATIONAL_SIGNIFICANCE_PRIORITY_GATE_AFTER_WP20.md`
- `M2_HOSTILE_THEOREM_LANGUAGE_AND_DIMENSION_AUDIT.md`
- `THEOREM_PROVENANCE_MATRIX.md`
- `MANUSCRIPT_HANDOFF.md`

## Canonical M2R1 sources

- `autonomous_temporal_resource_law_m2r1.tex` — canonical audited main manuscript.
- `autonomous_temporal_resource_law_supplement_m2r1.tex` — canonical audited supplement master.
- `proofs/finite_radius_survival_proofs.tex` — WP02/WP03/WP06 proof block.
- `proofs/boundary_and_autonomous_action_proofs.tex` — WP07/WP09/WP18 proof block.
- `proofs/noncommuting_mixed_bridge_proof_r1.tex` — audited WP11/WP13/WP19 bridge including degenerate orientations and zero-cost obstruction.
- `proofs/multigap_action_sum_proof_r1.tex` — audited WP20 proof including null-cost mode handling and fixed quadrature metric.
- `proofs/shared_kernel_qutrit_benchmark.tex` — self-contained physical/resource/QFI benchmark definition.
- `proofs/wp15_exact_common_record_qutrit.tex` — exact `55/8` common-record witness and limiting projective sequence.
- `references.bib` — verified seed bibliography including PSD-cone and shorted-operator prior mathematics.
- `check_m2_tex_static.py` — recursive M2R1 static source-integrity gate.

Files with names ending in `_draft`, `_m2`, or the original monolithic supplement are archival earlier manuscript stages and are not current drafting targets.

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

## M2R1 hostile-audit corrections

The audited sources now state explicitly:

1. the current theorem package is finite dimensional;
2. the compact mixed `Psi` formula applies to bilateral nonzero synthesized orientations with positive restricted costs, while plus-only, minus-only, and no-synthesis cases have separate formulas;
3. a zero shorting constant makes that local scalar survival ceiling unavailable rather than producing a division by zero;
4. a nonzero synthesized direction with zero restricted cost is not controlled by that scalar action; in the multi-gap theorem its effective scalar mode price is `gamma_k=0`;
5. Fisher/Hessian traces use the fixed Euclidean metric of the physical cosine--sine quadratures and are not claimed to be invariant under arbitrary anisotropic reparameterization.

None of these corrections changes the headline `hbar nu/4` bilateral coefficient, `hbar nu/2` one-sided coefficient, qutrit hierarchy, or multi-gap Fourier extremizer.

## Claim discipline

Do not claim a new resource theory of time, a new Page--Wootters mechanism, new modes-of-asymmetry theory, a new generic QFI principle, or a universal implementation-energy law.

Priority remains **unverified, not certified**. The literature gate supports only a narrow theorem-paper claim.

## Build and integrity gate

`.github/workflows/autonomous-temporal-manuscript-check.yml` is isolated from the frozen Rev11 workflow. It now:

1. runs `python check_m2_tex_static.py` against the M2R1 pair;
2. compiles `autonomous_temporal_resource_law_m2r1.tex`;
3. compiles `autonomous_temporal_resource_law_supplement_m2r1.tex`;
4. uploads the M2R1 sources, PDFs, proof modules, and audit/handoff artifacts.

Do not call M2R1 build-verified until a concrete successful Actions job result/log is retrieved. The current connector cannot expose push-triggered run status directly.

## Next work

1. post-rewrite hostile consistency audit of the M2R1 main against the R1 proof modules;
2. verify all special-case mixed formulas, unavailable shorting branches, and multi-gap null directions are worded literally correctly;
3. only after that gate, perform publication-style abstract/introduction compression and current journal positioning;
4. no new theorem work unless the audit exposes a real mathematical gap.
