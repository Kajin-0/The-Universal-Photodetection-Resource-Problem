# Manuscript handoff — exact minimum dynamical cost

**Branch:** `agent/autonomous-temporal-information-law`

## Phase

**PRA R1 — publication-facing package promoted, build-verified, render-inspected, and deterministically source-locked.**

This remains a separate follow-up paper. The existing PRX Quantum R3 temporal-resource manuscript is science-frozen and must not be expanded merely because this follow-up exists.

The audited D2 theorem manuscript is also frozen as the scientific/proof baseline. PRA R1 changes publication-facing prose and title presentation only; its theorem body is statically required to remain identical to D2 from the fixed setup paragraph through the acknowledgments boundary, and its supplement is title-only relative to audited D2 from the author declaration onward.

Current journal-facing title:

> **Exact minimum dynamical cost of prescribed rank-changing quantum-state curvature**

## Canonical source chain

### D1 -> audited D2 theorem layer

- `dynamical_rank_boundary_implementation_cost_draft.tex` — D1 theorem source;
- `dynamical_rank_boundary_implementation_cost_supplement.tex` — D1 proof source;
- `apply_d2_audit_repairs.py` — deterministic D2 implementation-topology and presentation repair;
- `dynamical_rank_boundary_implementation_cost_d2.tex` — committed audited D2 main;
- `dynamical_rank_boundary_implementation_cost_supplement_d2.tex` — committed audited D2 supplement;
- `references.bib`;
- `check_tex_static_d2.py`;
- `check_build_logs.py`;
- `D2_HOSTILE_THEOREM_LANGUAGE_AUDIT.md`.

### D2 -> PRA R1 publication layer

- `apply_pra_r1_frontmatter.py` — publication-facing main title/abstract/introduction/disclosure/Data Availability transform;
- `apply_pra_r1_supplement_title.py` — title-only supplement transform;
- `dynamical_rank_boundary_implementation_cost_pra_r1.tex` — committed canonical PRA R1 main;
- `dynamical_rank_boundary_implementation_cost_supplement_pra_r1.tex` — committed canonical PRA R1 supplement;
- `check_pra_r1_static.py` — publication identity, title consistency, D2 theorem/proof freeze, disclosure, label/ref/citation gate;
- `check_pra_build_logs.py` — final LaTeX quality gate;
- `.github/workflows/dynamical-implementation-manuscript-check.yml` — isolated deterministic build.

The workflow regenerates the committed PRA R1 main and supplement and requires a zero `git diff` before compilation. A stale promoted source is therefore a hard CI failure.

PDFs remain reproducible Actions artifacts rather than committed repository binaries.

## Mechanical verification

### Corrected publication-package verification

Observable PR-triggered run:

- workflow run `32666263610`;
- D2 deterministic generation/static gate: **PASS**;
- PRA R1 main generation: **PASS**;
- PRA R1 publication-facing supplement generation: **PASS**;
- PRA R1 standalone/theorem-and-proof freeze gate: **PASS**;
- PRA R1 main compile: **PASS**;
- PRA R1 supplement compile: **PASS**;
- final PRA R1 build-log quality gate: **PASS**;
- artifact upload: **PASS**.

Corrected artifact:

- artifact ID `9500112341`;
- SHA-256 `6dccb86d7310c15fc25d36927f91c031bc8002a4c709b18e8637d5f3640a73fb`;
- main: **11 pages**;
- supplement: **10 pages**.

The main and corrected supplement were rendered and visually inspected. No clipping, overlap, broken glyph, or theorem-layout defect was found.

### Render-QA correction that must not be undone

An earlier build had passed every static/LaTeX gate but was **not promoted** because visual inspection caught a package inconsistency: the main used the new PRA title while the supplement still displayed the older D2 “quantum-state jet” title.

The repair is intentionally narrow:

1. `apply_pra_r1_supplement_title.py` creates a publication-facing supplement with the exact PRA main title;
2. `check_pra_r1_static.py` requires title equality and forbids `jet` in either publication title;
3. the same gate requires everything in the publication supplement from `\author{Anonymous}` onward to remain byte-for-byte identical to audited D2.

Do not “simplify” this by compiling the D2 supplement directly for PRA R1.

## Scientific center

The paper answers:

> Given a rank-changing quantum-state family with prescribed first-order tangent and prescribed feasible metric-contracted second-order population in the baseline-empty target sector, what is the least state-weighted quadratic dynamical coupling needed to realize that local physical datum?

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

## Implementation-class lock

The D1 shorthand “smooth unitary dilation with `partial_j U=-iK_j`” is too strong/ambiguous for an unbounded direct-sum generator.

The frozen D2/PRA theorem class is:

- self-adjoint tangent generators on the baseline domain;
- finite baseline generator second moments;
- trace-norm `C^2` implemented reduced state at the origin;
- ordinary operator differentiation for bounded generators;
- state-weighted quadratic-form/spectral-truncation interpretation for the kernel identity with unbounded generators;
- branchwise trace-norm dominated convergence for the energy-conserving direct-sum construction.

The infinite-dimensional energy-conserving unitary is strongly continuous; smoothness is asserted statewise on the finite-cost baseline, not as operator-norm differentiability of the unbounded unitary group.

This clarification changes no coefficient or construction.

## Critical WP32 proof correction

Never use the superseded shortcut that normalizes a curvature block by baseline population in the same target-energy shell. A prescribed stationary curvature block can be nonzero where baseline population is zero.

The canonical energy-conserving proof instead:

1. uses the countable joint eigenbasis of stationary trace-class `rho_0` and target time translations on occupied support;
2. decomposes excess positive curvature into energy-adapted modes, including modes in unoccupied target-energy shells;
3. splits one occupied baseline eigenstate into countably many classically incoherent ancilla-labelled copies;
4. chooses nonnegative ancilla input/output energies satisfying `E_in+a_r=F_r+b_r`;
5. realizes excess curvature with first-order-invisible orthogonal flags;
6. uses finite quadratic cost to dominate all first and mixed second trace-norm derivatives of the classical branch series.

No fourth-moment condition is needed.

## Publication / novelty lock

Do not claim novelty for:

- Bures/Uhlmann or `QFI/4` horizontal purification geometry;
- channel Fisher/Kraus-gauge/fibre-bundle geometry;
- covariant or energy-conserving Stinespring dilation;
- generic quantum-speed-limit/control-norm inequalities;
- PSD-cone second-order tangent geometry;
- classical nonregular boundary statistics;
- infinite-dimensional QFI/Bures functional analysis.

Current allowed working novelty sentence, always qualified by unverified priority:

> We determine the exact minimum state-weighted quadratic coupling required to realize a prescribed feasible rank-changing kernel second-order curvature of a quantum state, show that the minimum can be attained under exact total-energy conservation even in separable infinite dimension, and identify the frequency-resolved endpoint synthesis action of an autonomous temporal mode as precisely `hbar nu` times this minimum cost.

Priority remains **unverified, not certified**.

## PRA R1 publication layer

The publication-facing main uses a less internal/geometric title and a compressed abstract/introduction, while retaining the theorem body exactly.

The abstract must retain all of these points:

- exact result `V_min=(1/2)Tr C`;
- exact total-energy conservation does not raise the optimum;
- separable infinite-dimensional scope;
- autonomous identity `A_ex^(2)=hbar nu V_min`;
- explicit statement that the result is not a thermodynamic-work bound.

The main currently includes:

- substantive OpenAI ChatGPT / GPT-5.6-series use disclosure;
- explicit author responsibility;
- standalone Data Availability statement.

Before actual submission, verify the then-current APS disclosure/submission policy rather than assuming this wording is permanently sufficient.

## Manuscript integrity rules

The public manuscript and supplement are fully standalone.

Never include:

- personal repository URLs;
- usernames;
- repository/project names;
- internal work-package labels;
- development history;
- instructions that a reader must consult internal research files.

The static gates enforce these restrictions and also prevent reintroduction of the superseded energy-shell shortcut.

## Immediate work order

1. **Do not reopen theorem development** merely to enlarge the manuscript.
2. Run one final hostile **publication-facing** significance/claim/citation review of PRA R1 as actually written.
3. Check the current APS submission and AI-disclosure requirements immediately before submission.
4. Replace anonymous author/affiliation metadata only in the final submission package.
5. Keep R3 and D2 scientifically frozen unless prior art, a referee, or a genuine proof defect requires a correction.
