# Manuscript handoff — exact minimum unitary coupling cost

**Branch:** `agent/autonomous-temporal-information-law`

## Phase

**PRA R1 — final publication-facing package reviewer-repaired, final-CI verified, render-inspected, and deterministically source-locked.**

The PRX Quantum R3 temporal-resource manuscript remains science-frozen. The regenerated D2 theorem/proof layer remains the scientific baseline. Do not reopen either merely to enlarge this follow-up.

Current journal-facing title:

> **Exact minimum unitary coupling cost of prescribed rank-changing quantum-state curvature**

## Scientific center

The paper optimizes the local state-weighted quadratic unitary-coupling functional

`V_impl = sum_j Var_{Omega_0}(K_j)`

over finite-cost unitary dilations realizing prescribed first derivatives and prescribed feasible metric-contracted kernel curvature `C`.

Central theorem:

`V_min(C;D,rho_0) = (1/2) Tr C`,

with feasibility

`C >= C_min`.

Exact total-energy conservation does not increase the optimum under the stated optimization class. In the clean autonomous temporal exchange,

`A_ex^(2) = hbar nu V_min`.

## Final extreme-adversarial-review response

A subsequent hostile review found no blocking mathematical error and rated the theorem/proof package strongly. It identified three publication/scope improvements. All are now implemented.

### 1. Theorem 2 covariance reference — mandatory textual fix

The rendered stationarity/covariance block is numbered `(17)-(19)`. The prior theorem sentence referred through a label attached only to the final line, so it visually read as though only Eq. (19) were assumed.

The deterministic D2 transform now labels the first line and Theorem 2 states:

`Eqs. (17)-(19)`.

This is a textual correction only; the theorem always used stationarity/covariance of `rho_0`, every `D_j`, and `C`.

### 2. Ancilla/peak-coupling scope — explicit limitation

The final paper states that in the separable infinite-dimensional attaining construction:

- the direct-sum generator may be unbounded;
- the ancillary Hamiltonian is part of the optimization rather than externally fixed;
- no bound is claimed on peak/operator-norm coupling;
- no bound is claimed on ancilla dimension;
- no bound is claimed on controller bandwidth or spectral complexity;
- exact attainment is not asserted for an externally fixed controller spectrum.

Finite `V_impl` is therefore a state-weighted quadratic-cost statement, not an operator-norm/control-hardware bound.

### 3. Title precision

The prior title used “dynamical cost.” The final title uses **“unitary coupling cost”** because this names the optimized functional more precisely and preempts the objection that the theorem minimizes every possible dynamical resource.

## Canonical source chain

### D1 -> regenerated audited D2 layer

- `dynamical_rank_boundary_implementation_cost_draft.tex`
- `dynamical_rank_boundary_implementation_cost_supplement.tex`
- `apply_d2_audit_repairs.py`
- `dynamical_rank_boundary_implementation_cost_d2.tex`
- `dynamical_rank_boundary_implementation_cost_supplement_d2.tex`
- `check_tex_static_d2.py`
- `check_build_logs.py`
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
- `.github/workflows/dynamical-implementation-manuscript-check.yml`

The workflow regenerates the committed PRA R1 sources and requires a zero `git diff`. The PRA main theorem body is compared against the regenerated D2 body; the PRA supplement remains title-only relative to D2 from `\author{Anonymous}` onward.

## Final mechanical verification

Observable final reviewer-repair run:

- workflow run `32673160217`;
- canonical base commit verified: `1e03374d8ee20ca0a058b2b054acf463db3c3e08`;
- D2 generation/static theorem gate: **PASS**;
- PRA main generation: **PASS**;
- PRA supplement generation: **PASS**;
- committed-source freshness: **PASS**;
- hostile-review title/scope/theorem/proof/publication gate: **PASS**;
- main compile: **PASS**;
- supplement compile: **PASS**;
- final LaTeX-quality gate: **PASS**;
- artifact upload: **PASS**.

Final artifact:

- artifact ID `9501942180`;
- SHA-256 `4236d6f514b2f290d302062ab4c7a599c03c817da259f3d9715b787a4d37d640`;
- main PDF: **11 pages**, `227942` bytes;
- supplement PDF: **10 pages**, `229240` bytes.

## Final render inspection

The exact final artifact was rendered at 180 dpi.

Verified visually:

- main title clean and balanced;
- supplement title matches the new main title;
- Theorem 2 visibly reads `Eqs. (17)-(19)`;
- expanded limitations paragraph is clean and unclipped;
- theorem boxes/equations remain within page bounds;
- no overlap or broken glyphs;
- bibliography clean;
- AI-assisted research / Acknowledgments / Data Availability page clean;
- supplement proof layout unchanged except title.

## Infinite-dimensional implementation-class lock

The valid theorem class remains:

- self-adjoint tangent generators on the baseline domain;
- finite baseline generator second moments;
- trace-norm `C^2` implemented reduced state at the origin;
- ordinary operator differentiation for bounded generators;
- state-weighted quadratic-form/spectral-truncation interpretation for unbounded generators;
- branchwise dominated convergence for the energy-conserving direct-sum construction.

The unitary is strongly continuous; no operator-norm differentiability claim is made for the unbounded direct-sum generator.

## Critical WP32 proof correction

Never restore the superseded WP31 shortcut that normalizes curvature by baseline population in the same target-energy shell. Stationary prescribed excess curvature can occupy target-energy shells unoccupied at baseline.

The correct construction uses:

1. the countable joint energy/eigenvalue basis of the stationary trace-class baseline;
2. energy-adapted excess-curvature modes;
3. classical splitting of an occupied baseline eigenstate into ancilla-labelled copies;
4. nonnegative input/output ancilla-energy compensation;
5. first-order-invisible orthogonal flags;
6. finite quadratic cost to dominate trace-norm first/mixed-second derivatives.

No fourth-moment condition is required.

## Prior-art / novelty lock

Do not claim novelty for Bures/Uhlmann/SLD-QFI horizontal geometry, Riemannian Bures curvature, channel Fisher/Kraus-gauge geometry, covariant Stinespring dilation, generic energy-conserving dilation theory, generic quantum speed limits/control norms, PSD-cone second-order tangent geometry, classical nonregular boundary statistics, or infinite-dimensional Bures/QFI analysis.

Huang et al. (2026), arXiv:2605.27907, studies Riemannian curvature of the Bures metric near rank-changing states. It is explicitly separated from this paper's prescribed state-family kernel Hessian contraction.

Priority remains **unverified, not certified**.

## Publication-policy lock

The final PRA main contains:

- `AI-Assisted Research and Verification` for substantive OpenAI ChatGPT / GPT-5.6-series use;
- explicit author verification/responsibility language;
- software-aware Data Availability wording for internal validation scripts.

Re-check then-current APS requirements immediately before submission.

## Immediate work order

1. close disposable PR #33 unmerged after recording the successful run;
2. keep this reviewer-repaired PRA R1 state canonical;
3. do not reopen theorem development merely to enlarge the paper;
4. replace anonymous author/affiliation metadata only in the actual submission package;
5. reopen the science only for a genuine proof defect, direct prior-art collision, referee requirement, or deliberately new research program.
