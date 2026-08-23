# Manuscript handoff — exact minimum dynamical cost

**Branch:** `agent/autonomous-temporal-information-law`

## Phase

**PRA R1 — final publication-facing package promoted, final-CI verified, render-inspected, and deterministically source-locked.**

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

- `apply_pra_r1_frontmatter.py` — publication-facing main title/abstract/introduction/AI-assisted research disclosure/acknowledgments/Data Availability transform;
- `apply_pra_r1_supplement_title.py` — title-only supplement transform;
- `dynamical_rank_boundary_implementation_cost_pra_r1.tex` — committed canonical PRA R1 main;
- `dynamical_rank_boundary_implementation_cost_supplement_pra_r1.tex` — committed canonical PRA R1 supplement;
- `check_pra_r1_static.py` — publication identity, title consistency, D2 theorem/proof freeze, disclosure/policy, prior-art marker, label/ref/citation gate;
- `check_pra_build_logs.py` — final LaTeX quality gate;
- `PRA_R1_FINAL_PUBLICATION_AUDIT_2026-08-23.md` — final hostile publication audit and policy record;
- `.github/workflows/dynamical-implementation-manuscript-check.yml` — isolated deterministic build.

The workflow regenerates the committed PRA R1 main and supplement and requires a zero `git diff` before compilation. A stale promoted source is therefore a hard CI failure.

PDFs remain reproducible Actions artifacts rather than committed repository binaries.

## Final mechanical verification

Observable final PR-triggered run:

- workflow run `32667189807`;
- canonical package commit verified by the disposable PR base: `d100d526b823ed6a7807d0d4cb344b3ba92a5f42`;
- D2 deterministic generation/static theorem gate: **PASS**;
- PRA R1 main generation: **PASS**;
- PRA R1 publication-facing supplement generation: **PASS**;
- committed PRA source freshness (`git diff --exit-code`): **PASS**;
- PRA R1 standalone/theorem-and-proof freeze gate: **PASS**;
- PRA R1 main compile: **PASS**;
- PRA R1 supplement compile: **PASS**;
- final PRA R1 build-log quality gate: **PASS**;
- artifact upload: **PASS**.

Final artifact:

- artifact ID `9500374374`;
- artifact SHA-256 `7bc86f37407f1a4875e0f4a6cd3aaa14db4cf61166afd2efd5df8c1f3fa7e7b4`;
- main PDF: **11 pages**, `227654` bytes;
- supplement PDF: **10 pages**, `229237` bytes.

The exact final main and supplement PDFs were rendered at 180 dpi and visually inspected. No clipping, overlap, broken glyph, title mismatch, or theorem-layout defect was found. The final main page containing `AI-Assisted Research and Verification`, Acknowledgments, and Data Availability was separately inspected at full resolution and is clean.

## Render-QA correction that must not be undone

An earlier build passed every static/LaTeX gate but was **not promoted** because visual inspection caught a package inconsistency: the main used the new PRA title while the supplement still displayed the older D2 “quantum-state jet” title.

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

## Final publication / novelty audit

No theorem defect or direct known collision was found in the final publication-facing hostile pass. Priority remains **unverified, not certified**.

A current nearby result had to be separated explicitly: Huang et al. (2026), arXiv:2605.27907, analyzes the **Riemannian curvature of the Bures metric itself** near rank-changing density matrices. That is not this paper's `C`: here `C` is the physical-metric contraction of a particular state family's second derivative projected into the baseline kernel. The PRA R1 introduction now states this distinction explicitly and the static gate requires the `HuangEtAl2026` citation.

Do not claim novelty for:

- Bures/Uhlmann or `QFI/4` horizontal purification geometry;
- Riemannian curvature of the Bures metric near rank-changing states;
- channel Fisher/Kraus-gauge/fibre-bundle geometry;
- covariant or energy-conserving Stinespring dilation;
- generic quantum-speed-limit/control-norm inequalities;
- PSD-cone second-order tangent geometry;
- classical nonregular boundary statistics;
- infinite-dimensional QFI/Bures functional analysis.

Current allowed working novelty sentence, always qualified by unverified priority:

> We determine the exact minimum state-weighted quadratic coupling required to realize a prescribed feasible rank-changing kernel second-order curvature of a quantum state, show that the minimum can be attained under exact total-energy conservation even in separable infinite dimension, and identify the frequency-resolved endpoint synthesis action of an autonomous temporal mode as precisely `hbar nu` times this minimum cost.

## APS publication-policy lock

The final PRA R1 publication layer reflects the August 23, 2026 policy audit:

- substantive AI assistance in derivation exploration, adversarial algebra checks, literature organization, generation/debugging of internal numerical-validation code, and manuscript preparation is disclosed in a dedicated `AI-Assisted Research and Verification` section;
- the section names OpenAI ChatGPT and the GPT-5.6-series models, including GPT-5.6 Sol;
- it states that AI outputs were provisional, the author directed the scientific questions/proof strategy, independently checked claims against analytic derivations/examples/validators/primary literature, and takes full responsibility;
- Acknowledgments remain anonymous-review safe rather than duplicating the substantive disclosure;
- Data Availability says that no empirical data were created or analyzed, identifies the internal validation scripts, states that they are not required to reproduce the analytic results, and offers them from the author upon reasonable request.

These are publication-layer statements only. They do not alter the frozen D2 theorem/proof body.

Immediately before actual submission, re-check the then-current APS instructions rather than assuming any policy wording is permanent.

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
2. Close disposable final verification PRs unmerged once their successful runs are recorded.
3. Preserve the promoted PRA R1 package as the canonical journal-facing state.
4. At actual submission time, re-check current APS metadata/policy and replace anonymous author/affiliation information in the submission package only.
5. Keep R3 and D2 scientifically frozen unless prior art, a referee, or a genuine proof defect requires a correction.
