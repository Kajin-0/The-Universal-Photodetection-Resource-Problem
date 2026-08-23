# The Universal Photodetection Resource Problem

**Status synchronized: 2026-08-23**

The repository is authoritative; chat history is not.

## Project split

1. Paper 1 / Rev11 — frozen.
2. Paper 2 / Rev7 — frozen.
3. Random-time spectral-resource Rev11 — frozen on `agent/temporal-information-resource-law`.
4. Autonomous temporal-information program — theorem frontier frozen at WP32/WP33; separate follow-up now at final reviewer-repaired PRA R1 state on `agent/autonomous-temporal-information-law`.

The PRX Quantum R3 two-regime manuscript is build-verified, standalone, and science-frozen. The follow-up theorem/proof layer is likewise frozen after D2/WP32/WP33, with PRA R1 as the journal-facing publication package.

Authoritative handoff: `manuscript/dynamical_implementation_cost/MANUSCRIPT_HANDOFF.md`.

## Current strongest theorem

For a stationary rank-changing temporal model with prescribed feasible metric-contracted target-kernel Hessian `C`,

`V_min=(1/2)Tr C`.

For the clean single-gap autonomous endpoint action,

`A_ex^(2)=hbar nu V_min`.

WP32 proves the same optimum under exact total-energy conservation with a semibounded ancilla in separable infinite dimension, including unbounded occupied target energies and stationary excess curvature in target-energy shells unoccupied at baseline.

## Final follow-up paper

Current journal-facing title:

> **Exact minimum unitary coupling cost of prescribed rank-changing quantum-state curvature**

The final hostile review found no blocking mathematical error and led to three implemented refinements:

- Theorem 2 explicitly cites all stationarity/covariance assumptions as `Eqs. (17)-(19)`;
- the limitations section states that the infinite-dimensional optimizer may use an unbounded generator and freely optimized ancilla spectrum, with no claimed bound on peak/operator-norm coupling, ancilla dimension, controller bandwidth, or spectral complexity, and no exact-attainment claim for a fixed external controller spectrum;
- the title was narrowed from generic “dynamical cost” to **“unitary coupling cost.”**

No theorem coefficient or construction changed.

Canonical package:

- `manuscript/dynamical_implementation_cost/dynamical_rank_boundary_implementation_cost_pra_r1.tex`;
- `manuscript/dynamical_implementation_cost/dynamical_rank_boundary_implementation_cost_supplement_pra_r1.tex`;
- `manuscript/dynamical_implementation_cost/MANUSCRIPT_HANDOFF.md`;
- `manuscript/dynamical_implementation_cost/PRA_R1_FINAL_PUBLICATION_AUDIT_2026-08-23.md`.

Final reviewer-repair CI:

- workflow run `32673160217` — **PASS**;
- committed-source freshness — **PASS**;
- D2 theorem gate — **PASS**;
- PRA title/scope/theorem/proof/publication gate — **PASS**;
- main compile — **PASS**;
- supplement compile — **PASS**;
- final LaTeX-quality gate — **PASS**;
- artifact upload — **PASS**.

Artifact `9501942180`, SHA-256 `4236d6f514b2f290d302062ab4c7a599c03c817da259f3d9715b787a4d37d640`, contains the 11-page main and 10-page supplement. Both were rendered at 180 dpi and visually inspected with no clipping, overlap, broken glyphs, title mismatch, or theorem-layout defect.

## Prior-art boundary

No direct known prior-art collision was identified for the exact prescribed-curvature unitary-coupling optimization theorem. Priority remains **unverified, not certified**.

Do not claim novelty for Bures/Uhlmann/SLD-QFI horizontal purification geometry, Riemannian Bures curvature, channel Fisher/Kraus-gauge geometry, covariant/energy-conserving Stinespring dilation as such, generic quantum speed limits/control norms, infinite-dimensional QFI/Bures theory, classical nonregular boundary statistics, or standard second-order PSD-cone/operator mathematics.

The narrow candidate contribution remains the exact minimum state-weighted quadratic unitary-coupling cost for independently prescribed feasible rank-changing target-kernel curvature, its exact globally conserving realization under the stated optimization class, and the autonomous spectral endpoint identity.

The final publication layer also contains the current `AI-Assisted Research and Verification` disclosure and software-aware Data Availability wording recorded in the final audit.

## Current work order

1. keep R3 and D2 scientifically frozen;
2. treat the reviewer-repaired PRA R1 package as canonical;
3. do not reopen theorem development merely to enlarge the paper;
4. at submission time, re-check then-current APS requirements and replace anonymous author/affiliation metadata only in the submission package;
5. resume theory only for a genuine proof/prior-art/referee issue or as a deliberately separate new research program.

## Manuscript integrity

Every public-facing paper must be scientifically standalone. Never include personal repository URLs, usernames, repository names, development history, or dependencies on internal research files.
