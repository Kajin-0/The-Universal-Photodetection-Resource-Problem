# Dynamical implementation cost — follow-up manuscript workspace

## Status

**PRA R1 is final-CI verified, render-inspected, and deterministically source-locked after an additional extreme adversarial review.**

The PRX Quantum R3 autonomous temporal-resource manuscript remains science-frozen. The regenerated D2 theorem/proof layer remains the scientific baseline; the final PRA R1 package is the journal-facing form.

Current journal-facing title:

> **Exact minimum unitary coupling cost of prescribed rank-changing quantum-state curvature**

The title was narrowed from “dynamical cost” because the optimized object is specifically the local state-weighted quadratic unitary-coupling functional

`V_impl=sum_j Var_{Omega_0}(K_j)`.

## Scientific center

For a prescribed feasible physical-metric contraction of the target-kernel Hessian,

`C >= C_min`,

we prove

`V_min(C;D,rho_0)=(1/2)Tr C`.

Exact total-energy conservation does not increase the optimum under the stated ancilla assumptions, including the repaired separable infinite-dimensional construction. For the clean autonomous exchange,

`A_ex^(2)=hbar nu V_min`.

## Final adversarial-review repairs

The final hostile review found no blocking mathematical error and recommended three changes. All three are now implemented and statically gated:

1. **Covariance cross-reference:** Theorem 2 now explicitly assumes `Eqs. (17)-(19)`, rather than visually citing only the final line of the three-equation stationarity/covariance block.
2. **Scope of the optimizer:** the paper now states that the infinite-dimensional attaining generator may be unbounded, that the ancillary Hamiltonian is part of the optimization rather than externally fixed, and that no bound is claimed on peak/operator-norm coupling, ancilla dimension, controller bandwidth, or controller spectral complexity. Exact attainment is not claimed for an externally fixed controller spectrum.
3. **Title precision:** “dynamical cost” was replaced by **“unitary coupling cost.”**

No theorem coefficient or construction changed.

## Canonical source chain

### D1 -> audited D2 layer

- `dynamical_rank_boundary_implementation_cost_draft.tex`
- `dynamical_rank_boundary_implementation_cost_supplement.tex`
- `apply_d2_audit_repairs.py`
- `dynamical_rank_boundary_implementation_cost_d2.tex`
- `dynamical_rank_boundary_implementation_cost_supplement_d2.tex`
- `D2_HOSTILE_THEOREM_LANGUAGE_AUDIT.md`

### D2 -> PRA R1 publication layer

- `apply_pra_r1_frontmatter.py`
- `apply_pra_r1_supplement_title.py`
- `dynamical_rank_boundary_implementation_cost_pra_r1.tex`
- `dynamical_rank_boundary_implementation_cost_supplement_pra_r1.tex`
- `check_pra_r1_static.py`
- `check_pra_build_logs.py`
- `references.bib`
- `PRA_R1_FINAL_PUBLICATION_AUDIT_2026-08-23.md`
- `MANUSCRIPT_HANDOFF.md`

The CI workflow regenerates the committed PRA R1 TeX roots and requires a zero `git diff` before compilation. Stale promoted sources are therefore a hard failure.

## Final verified package

Final hostile-review verification:

- workflow run `32673160217`;
- verified canonical base commit `1e03374d8ee20ca0a058b2b054acf463db3c3e08` plus a disposable CI marker;
- D2 generation/static theorem gate: **PASS**;
- PRA main/supplement generation: **PASS**;
- committed-source freshness: **PASS**;
- hostile-review publication/title/scope/theorem/proof gate: **PASS**;
- main compile: **PASS**;
- supplement compile: **PASS**;
- final LaTeX-quality gate: **PASS**;
- artifact upload: **PASS**.

Final artifact:

- ID `9501942180`;
- SHA-256 `4236d6f514b2f290d302062ab4c7a599c03c817da259f3d9715b787a4d37d640`;
- main: **11 pages**, `227942` bytes;
- supplement: **10 pages**, `229240` bytes.

The exact PDFs were rendered at 180 dpi. The new title, `Eqs. (17)-(19)` theorem wording, expanded limitations paragraph, disclosure page, equations, bibliography, and supplement were visually clean. No clipping, overlap, broken glyph, title mismatch, or theorem-layout defect was found.

## Prior-art / policy lock

Do not claim novelty for first-order Bures/Uhlmann/SLD-QFI purification geometry, Riemannian Bures curvature, channel Fisher/Kraus-gauge geometry, covariant Stinespring dilation, generic energy-conserving dilation theory, generic QSL/control-norm bounds, PSD-cone second-order tangent geometry, classical nonregular boundary statistics, or infinite-dimensional Bures/QFI functional analysis.

The narrow candidate contribution remains the exact prescribed rank-changing target-kernel-curvature unitary-coupling minimum, its exact globally conserving realization under the stated optimization class, and the autonomous spectral endpoint identity. Priority is **unverified, not certified**.

The final main also contains the current substantive-AI disclosure and software-aware Data Availability wording recorded in `PRA_R1_FINAL_PUBLICATION_AUDIT_2026-08-23.md`.

## Immediate work order

1. keep R3 and D2 scientifically frozen;
2. treat this reviewer-repaired PRA R1 package as canonical;
3. do not add theorem material merely to enlarge the paper;
4. at actual submission time, re-check then-current APS metadata/disclosure requirements and replace anonymous author/affiliation metadata only in the submission package;
5. reopen theory only for a genuine proof defect, direct prior-art collision, referee requirement, or a deliberately new research program.
