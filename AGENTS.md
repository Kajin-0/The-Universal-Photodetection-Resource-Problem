# AGENTS.md

## Purpose

Durable project handoff for The Universal Photodetection Resource Problem. The repository, not chat history, is authoritative.

Research is analytical/theoretical. Numerical validation is allowed. Do not make experiments, fabrication, procurement, or laboratory campaigns necessary next steps.

## Current project split

1. Paper 1 / Rev11 — frozen.
2. Paper 2 / Rev7 — frozen.
3. Random-time spectral-resource Rev11 — frozen on `agent/temporal-information-resource-law`.
4. Autonomous temporal-information program — theorem frontier frozen at WP32/WP33; separate follow-up now at final reviewer-repaired PRA R1 state on `agent/autonomous-temporal-information-law`.

**WP31 is superseded.**

## Read first

1. `manuscript/dynamical_implementation_cost/MANUSCRIPT_HANDOFF.md`
2. `manuscript/dynamical_implementation_cost/PRA_R1_FINAL_PUBLICATION_AUDIT_2026-08-23.md`
3. `docs/CURRENT_RESEARCH_STATE.md`
4. `autonomous_temporal_information/AGENTS.md`
5. `autonomous_temporal_information/notes/WP33_HOSTILE_AUDIT_WP32_AND_PRIORITY_BOUNDARY.md`
6. `autonomous_temporal_information/notes/WP32_REPAIRED_INFINITE_DIMENSIONAL_ENERGY_CONSERVING_2JET_COST.md`

## Current strongest theorem

For a stationary rank-changing temporal family with prescribed feasible metric-contracted target-kernel Hessian `C`,

`V_min=(1/2)Tr C`.

In the clean single-gap endpoint geometry,

`A_ex^(2)=hbar nu V_min`.

WP32 proves this in separable infinite dimension under exact total-energy conservation with a semibounded ancilla, including stationary excess curvature in target-energy shells empty at baseline.

## Publication state

Final journal-facing paper:

> **Exact minimum unitary coupling cost of prescribed rank-changing quantum-state curvature**

The final extreme adversarial review found no blocking mathematical error and produced three implemented repairs:

1. Theorem 2 now explicitly cites `Eqs. (17)-(19)` for the full stationarity/covariance assumption block.
2. The limitations section now states that the infinite-dimensional attaining generator may be unbounded; the ancillary Hamiltonian is part of the optimization rather than externally fixed; no bound is claimed on peak/operator-norm coupling, ancilla dimension, controller bandwidth, or spectral complexity; and exact attainment is not asserted for an externally fixed controller spectrum.
3. The title was narrowed from generic “dynamical cost” to **“unitary coupling cost.”**

No theorem coefficient or construction changed.

Final observable verification:

- workflow run `32673160217` — **PASS**;
- source freshness — **PASS**;
- D2 theorem gate — **PASS**;
- PRA title/scope/theorem/proof/publication gate — **PASS**;
- main/supplement compile — **PASS**;
- final LaTeX-quality gate — **PASS**;
- artifact upload — **PASS**.

Artifact `9501942180`, SHA-256 `4236d6f514b2f290d302062ab4c7a599c03c817da259f3d9715b787a4d37d640`, contains the 11-page main and 10-page supplement. Both were rendered at 180 dpi and visually inspected cleanly.

## Audit / novelty boundary

WP33: **PASS** under stated assumptions.

Final publication-facing hostile audit: **PASS**. Priority remains **unverified, not certified**.

Do not claim novelty for generic covariant/energy-conserving Stinespring dilation, Bures/Uhlmann/SLD-QFI horizontal geometry, Riemannian Bures curvature, classical nonregular boundary statistics, generic quantum speed limits/control norms, second-order PSD-cone tangent geometry, or infinite-dimensional Bures/QFI analysis.

The candidate distinct result is the exact prescribed rank-changing target-kernel-curvature minimum **unitary coupling cost**, its exact conserving attainability under the stated optimization class, and the autonomous spectral endpoint identity.

Huang et al. (2026), arXiv:2605.27907, is explicitly separated: it concerns Bures Riemannian curvature, not the prescribed state-family kernel Hessian contraction optimized here.

## Policy / integrity lock

The final PRA publication layer contains:

- `AI-Assisted Research and Verification` for substantive OpenAI ChatGPT / GPT-5.6-series use;
- explicit author verification/responsibility language;
- software-aware Data Availability wording for internal validation scripts.

Every public-facing paper must be scientifically standalone. Never include personal repository URLs, usernames, repository names, development history, or dependencies on internal research files.

## Current work order

1. preserve R3, D2, and the reviewer-repaired PRA R1 package;
2. do not reopen theorem production merely to increase manuscript size;
3. immediately before actual submission, re-check then-current APS requirements and replace anonymous author/affiliation metadata only in the submission package;
4. reopen this theorem stack only for a genuine proof defect, direct prior-art collision, referee requirement, or changed journal policy;
5. if new research is desired, start it as a separate program.

## Documentation rule

Every material theorem, counterexample, proof repair, validator, prior-art collision, publication-policy change, hostile-review repair, or publication decision must update the dedicated notes, autonomous landing files, manuscript handoff, and top-level landing files.
