# AGENTS.md

## Purpose

Durable project handoff for The Universal Photodetection Resource Problem. The repository, not chat history, is authoritative.

Research is analytical/theoretical. Numerical validation is allowed. Do not make experiments, fabrication, procurement, or laboratory campaigns necessary next steps.

## Current project split

1. Paper 1 / Rev11 — frozen.
2. Paper 2 / Rev7 — frozen.
3. Random-time spectral-resource Rev11 — frozen on `agent/temporal-information-resource-law`.
4. Autonomous temporal-information program — theorem frontier frozen at WP32/WP33; separate dynamical-cost follow-up now at final PRA R1 publication state on `agent/autonomous-temporal-information-law`.

**WP31 is superseded.**

## Read first

1. `manuscript/dynamical_implementation_cost/MANUSCRIPT_HANDOFF.md`
2. `manuscript/dynamical_implementation_cost/PRA_R1_FINAL_PUBLICATION_AUDIT_2026-08-23.md`
3. `autonomous_temporal_information/AGENTS.md`
4. `autonomous_temporal_information/notes/WP33_HOSTILE_AUDIT_WP32_AND_PRIORITY_BOUNDARY.md`
5. `autonomous_temporal_information/notes/WP32_REPAIRED_INFINITE_DIMENSIONAL_ENERGY_CONSERVING_2JET_COST.md`
6. `manuscript/autonomous_temporal_information/MANUSCRIPT_HANDOFF.md`

## Current strongest theorem

For a stationary rank-changing temporal family with a prescribed feasible metric-contracted target-kernel Hessian `C`,

`boxed: V_min=(1/2)Tr C`.

In the clean single-gap endpoint geometry,

`boxed: A_ex^(2)=hbar nu V_min`.

WP32 proves this even in separable infinite dimension and under exact total-energy conservation with a semibounded ancilla, including arbitrary stationary spectator curvature in target-energy shells empty at baseline.

The proof uses a countable joint energy/eigenvalue basis of the stationary trace-class baseline, classical splitting of one baseline eigenstate into ancilla-labelled copies, proportional horizontal-tangent replication, and nonnegative ancilla input/output energy compensation for arbitrary excess-curvature modes.

Finite state-weighted quadratic cost yields the required trace-norm `C^2` regularity even when the direct-sum generator is unbounded.

## Audit status

WP33: **PASS** under the stated finite-information assumptions.

Final publication-facing hostile audit: **PASS** for the current PRA R1 package, with priority still **unverified, not certified**.

Novelty boundary:

- generic covariant/energy-conserving Stinespring dilation is prior art;
- Bures/Uhlmann/QFI horizontal geometry is prior art;
- Riemannian curvature of the Bures metric near rank-changing states is prior art / adjacent geometry;
- classical nonregular boundary statistics are prior art;
- second-order PSD-cone tangent geometry is prior art;
- the candidate distinct result is the state-specific **prescribed rank-changing target-kernel-curvature minimum implementation cost**, its exact conserving attainability, and its autonomous spectral endpoint identity.

A current nearby 2026 paper, Huang et al. arXiv:2605.27907, is explicitly separated in PRA R1: it concerns Bures Riemannian curvature, not the prescribed state-family kernel Hessian contraction `C` optimized here.

## Frozen manuscript status

The autonomous PRX Quantum R3 paper is build-verified, standalone, and science-frozen. Do not import WP21--WP32 wholesale.

The separate dynamical-cost follow-up is now also scientifically frozen:

> **Exact minimum dynamical cost of prescribed rank-changing quantum-state curvature**

The audited D2 source is the theorem/proof baseline. PRA R1 is the journal-facing transform.

Final observable workflow run `32667189807` passed:

- D2 generation/static theorem gate;
- PRA main and supplement generation;
- committed-source freshness;
- theorem/proof freeze;
- both LaTeX compiles;
- final LaTeX-quality gate;
- artifact upload.

Final artifact `9500374374`, SHA-256 `7bc86f37407f1a4875e0f4a6cd3aaa14db4cf61166afd2efd5df8c1f3fa7e7b4`, contains the 11-page main and 10-page supplement. Both exact PDFs were render-inspected cleanly.

The final PRA publication layer contains a dedicated `AI-Assisted Research and Verification` disclosure for substantive OpenAI ChatGPT / GPT-5.6-series use and software-aware Data Availability language for internal numerical-validation scripts. These changes do not alter the frozen D2 theorem/proof body.

## Current work order

1. preserve R3, D2, and PRA R1 as frozen scientific/publication states;
2. do not reopen theorem production merely to increase manuscript size;
3. immediately before actual submission, re-check then-current APS requirements and replace anonymous author/affiliation metadata in the submission package only;
4. reopen this theorem stack only for a genuine proof defect, direct prior-art collision, referee requirement, or changed journal policy;
5. if new research is desired, start it as a deliberately separate program (highest-value deferred targets: noisy/CPTP implementation cost, approximate-exchange dynamical cost, unbounded-relative-tangent quadratic-form theory, Gaussian/CV specialization).

## Manuscript integrity

Every public-facing paper must be scientifically standalone. Never include personal repository URLs, usernames, repository names, development history, or dependencies on internal research files.

## Documentation rule

Every material theorem, counterexample, proof repair, validator, prior-art collision, publication-policy change, or publication decision must update the dedicated notes, autonomous landing files, manuscript handoff, and top-level landing files.
