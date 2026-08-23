# Manuscript handoff — minimum dynamical coupling cost

**Branch:** `agent/autonomous-temporal-information-law`

## Phase

**D2 — theorem-first standalone manuscript build-verified, render-inspected, and theorem-language audited.**

This is a separate follow-up paper. The existing R3 temporal-resource manuscript remains frozen and must not be expanded merely because this follow-up exists.

## Canonical source chain

Audited D2 sources are generated deterministically from the D1 theorem-first roots:

- `dynamical_rank_boundary_implementation_cost_draft.tex` — D1 theorem source;
- `dynamical_rank_boundary_implementation_cost_supplement.tex` — D1 proof source;
- `apply_d2_audit_repairs.py` — D2 implementation-topology and presentation repair;
- generated `dynamical_rank_boundary_implementation_cost_d2.tex`;
- generated `dynamical_rank_boundary_implementation_cost_supplement_d2.tex`;
- `references.bib`;
- `check_tex_static_d2.py`;
- `check_build_logs.py`;
- `D2_HOSTILE_THEOREM_LANGUAGE_AUDIT.md`;
- this handoff.

Isolated CI:

- `.github/workflows/dynamical-implementation-manuscript-check.yml`.

## Mechanical verification

Observable PR-triggered D2 build:

- workflow run `32659447097`;
- static standalone theorem/identity gate: **PASS**;
- D2 main compile: **PASS**;
- D2 supplement compile: **PASS**;
- artifact upload: **PASS**.

Compiled D2 package:

- main: **10 pages**;
- supplement: **10 pages**.

The theorem-heavy main pages and the repaired infinite-dimensional supplement pages were rendered and visually inspected. No clipping, overlap, broken glyph, or theorem-layout defect was found.

D1 had three presentation warnings: a small overfull central-theorem line, an overlong supplement heading, and a math-bearing PDF bookmark. D2 removes all three. The workflow now also includes `check_build_logs.py`, which fails future builds on overfull boxes, PDF-string math warnings, unresolved final references/citations, or multiply-defined labels.

The remaining REVTeX/hyperref `nameref` compatibility warning and the APS BibTeX `jnrlst` control warning are package-level and do not indicate manuscript defects.

## Scientific center

The paper answers:

> Given a rank-changing quantum-state family with prescribed first-order tangent and prescribed feasible metric-contracted second-order population in the baseline-empty target sector, what is the least state-weighted quadratic dynamical coupling needed to realize that local state jet?

Central theorem:

`V_min = (1/2) Tr C`,

where

`C = Q sum_j partial_j^2 rho(0) Q`

is the prescribed physical-metric contraction of the target kernel Hessian.

Feasibility requires

`C >= C_min`,

with

`C_min = 2 sum_j Q D_j P rho_0^+ P D_j Q`

in finite dimension, or the Hilbert--Schmidt trace-class analogue in separable infinite dimension.

Exact energy-conserving attainability survives in separable infinite dimension, including unbounded occupied target energies and spectator curvature in target-energy shells empty at baseline.

Autonomous temporal specialization:

`A_ex^(2) = hbar nu V_min`.

## D2 implementation-class clarification

The D1 shorthand “smooth unitary dilation with `partial_j U=-iK_j`” was too strong/ambiguous for an unbounded direct-sum generator.

D2 states the actual proof class:

- self-adjoint tangent generators on the baseline domain;
- finite baseline generator second moments;
- trace-norm `C^2` implemented reduced state at the origin;
- ordinary operator differentiation for bounded generators;
- state-weighted quadratic-form/spectral-truncation interpretation for the kernel identity with unbounded generators;
- branchwise trace-norm dominated convergence for the energy-conserving direct-sum construction.

The infinite-dimensional energy-conserving unitary is strongly continuous; smoothness is asserted statewise on the finite-cost baseline, not as operator-norm differentiability of the unbounded unitary group.

This clarification changes no coefficient or construction.

## Critical proof correction inherited from WP32

Never use the superseded shortcut that normalizes a curvature block by baseline population in the same target-energy shell. A prescribed stationary curvature block can be nonzero where baseline population is zero.

The canonical energy-conserving proof instead:

1. uses the countable joint eigenbasis of stationary trace-class `rho_0` and target time translations on occupied support;
2. decomposes excess positive curvature into energy-adapted modes, including modes in unoccupied target-energy shells;
3. splits one occupied baseline eigenstate into countably many classically incoherent ancilla-labelled copies;
4. chooses nonnegative ancilla input/output energies satisfying `E_in+a_r=F_r+b_r`;
5. realizes excess curvature with first-order-invisible orthogonal flags;
6. uses finite quadratic cost to dominate all first and mixed second trace-norm derivatives of the classical branch series.

No fourth-moment condition is needed.

## Novelty / prior-art lock

Do not claim novelty for:

- Bures/Uhlmann or `QFI/4` horizontal purification geometry;
- channel Fisher/Kraus-gauge/fibre-bundle geometry;
- covariant Stinespring dilation;
- generic quantum-speed-limit/control-norm inequalities;
- PSD-cone second-order tangent geometry;
- classical nonregular boundary statistics;
- infinite-dimensional QFI/Bures functional analysis.

Current allowed working novelty sentence, always qualified by unverified priority:

> We determine the exact minimum state-weighted quadratic coupling required to realize a prescribed feasible rank-changing kernel second-order jet of a quantum state, show that the minimum can be attained under exact total-energy conservation even in separable infinite dimension, and identify the frequency-resolved endpoint synthesis action of an autonomous temporal mode as precisely `hbar nu` times this minimum cost.

Priority remains unverified, not certified.

## Manuscript integrity rules

The manuscript and supplement are fully standalone.

Never include:

- personal repository URLs;
- usernames;
- repository/project names;
- internal work-package labels;
- development history;
- instructions that a reader must consult internal research files.

The D2 static gate enforces these restrictions and also fails if the superseded energy-shell shortcut is reintroduced.

## Immediate work order

1. validate the new post-build log gate on one observable CI run;
2. close the temporary verification PR after the gate passes;
3. rewrite the abstract/introduction from theorem-first D2 into publication prose for the selected journal target;
4. add APS-required standalone submission disclosures only after checking current policy;
5. run a final hostile significance/prior-art read on the compressed publication-facing version;
6. do not add new theorem work unless manuscript compression or prior art reveals a genuine gap.
