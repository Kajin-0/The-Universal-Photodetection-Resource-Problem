# The Universal Photodetection Resource Problem

**Status synchronized: 2026-08-23**

The repository is authoritative; chat history is not.

## Project split

1. Paper 1 / Rev11 — frozen.
2. Paper 2 / Rev7 — frozen.
3. Random-time spectral-resource Rev11 — frozen on `agent/temporal-information-resource-law`.
4. Autonomous temporal-information program — theorem frontier frozen at WP32/WP33; separate dynamical follow-up now at final PRA R1 publication state on `agent/autonomous-temporal-information-law`.

The PRX Quantum R3 two-regime manuscript is build-verified, standalone, and science-frozen.

The separate follow-up manuscript is also now scientifically frozen at the audited D2 theorem/proof baseline, with PRA R1 as its journal-facing publication layer.

Authoritative current handoff: `manuscript/dynamical_implementation_cost/MANUSCRIPT_HANDOFF.md`.

## Current strongest autonomous theorem

For a stationary rank-changing temporal model with a prescribed feasible positive metric-contracted target-kernel Hessian `C`,

`boxed: V_min=(1/2)Tr C`.

For the clean single-gap endpoint action,

`boxed: A_ex^(2)=hbar nu V_min`.

WP32 proves this optimum even for separable infinite-dimensional targets and arbitrary stationary spectator curvature, including curvature in target-energy shells unoccupied at baseline, while conserving total energy exactly with a semibounded ancilla.

The construction uses a classical mixture of ancilla-labelled baseline branches, proportional replication of the horizontal tangent, and nonnegative input/output ancilla-energy compensation for excess curvature flags. Finite state-weighted quadratic cost suffices for trace-norm `C^2` regularity; no fourth-moment condition is required.

**WP31 is superseded** because its zero-energy-ancilla construction omitted unoccupied target-energy spectator sectors.

## Publication status

The post-R3 theorem chain has been developed as a separate paper:

> **Exact minimum dynamical cost of prescribed rank-changing quantum-state curvature**

Canonical publication package:

- `manuscript/dynamical_implementation_cost/dynamical_rank_boundary_implementation_cost_pra_r1.tex`;
- `manuscript/dynamical_implementation_cost/dynamical_rank_boundary_implementation_cost_supplement_pra_r1.tex`;
- `manuscript/dynamical_implementation_cost/MANUSCRIPT_HANDOFF.md`;
- `manuscript/dynamical_implementation_cost/PRA_R1_FINAL_PUBLICATION_AUDIT_2026-08-23.md`.

Final observable CI run `32667189807`: **PASS** across deterministic D2 regeneration, PRA transforms, committed-source freshness, theorem/proof freeze, main compile, supplement compile, final LaTeX quality gate, and artifact upload.

Final artifact `9500374374` has SHA-256 `7bc86f37407f1a4875e0f4a6cd3aaa14db4cf61166afd2efd5df8c1f3fa7e7b4`.

The exact final PDFs are 11 pages (main) and 10 pages (supplement) and were render-inspected with no clipping, overlap, broken glyph, title mismatch, or theorem-layout defect.

## Final publication-facing audit

No theorem defect or direct known prior-art collision was identified. Priority remains **unverified, not certified**.

A current nearby result, Huang et al. (2026), arXiv:2605.27907, studies the **Riemannian curvature of the Bures metric** near rank-changing states. PRA R1 now explicitly distinguishes that geometry from this paper's prescribed state-family kernel Hessian contraction `C`.

The final publication layer also contains a methods-level `AI-Assisted Research and Verification` disclosure for substantive OpenAI ChatGPT / GPT-5.6-series use and software-aware Data Availability wording for internal numerical-validation scripts.

The D2 theorem/proof body remains unchanged by these publication-layer corrections.

## Supporting post-R3 chain

- WP21: exact implementation-coupling identity for kernel curvature.
- WP22: first-order minimum `V_min=(1/4)Tr H_SLD`.
- WP23: finite-dimensional prescribed-2-jet optimum.
- WP24: independent mixed-envelope audit; classical nonregular boundary prior art.
- WP25/WP27: approximate-gap robustness in both resource regimes.
- WP28/WP29: infinite-dimensional survival and synthesis/action laws.
- WP30: unrestricted infinite-dimensional dilation optimum.
- WP32: repaired exact energy-conserving infinite-dimensional optimum.
- WP33: hostile proof and priority audit — **PASS** under stated regularity assumptions.

## Prior-art boundary

Covariant/energy-conserving Stinespring dilation, Bures/Uhlmann horizontal geometry, Riemannian Bures curvature, QFI convex-roof variance, generic quantum speed limits/control norms, infinite-dimensional QFI/Bures theory, classical nonregular boundary statistics, and standard second-order PSD-cone/operator mathematics are prior art.

The narrow candidate contribution is the **exact minimum state-weighted quadratic implementation-coupling cost for an independently prescribed feasible rank-changing target-kernel curvature under globally conserving relational dynamics**, together with the autonomous spectral endpoint identity.

## Current work order

1. keep PRX Quantum R3 and D2 scientifically frozen;
2. treat PRA R1 as the canonical journal-facing package;
3. do not reopen theorem development merely to enlarge the paper;
4. at submission time, re-check then-current APS requirements and replace anonymous author/affiliation metadata in the submission package only;
5. resume theory only for a genuine proof/prior-art/referee issue or as a deliberately separate new research program.

## Manuscript integrity

Every public-facing paper must be scientifically standalone. Never include personal repository URLs, usernames, repository names, development history, or dependencies on internal research files.
