# Dynamical implementation cost — follow-up manuscript workspace

## Status

**PRA R1 publication-facing package is promoted, final-CI verified, render-inspected, and deterministically source-locked.**

The PRX Quantum R3 autonomous temporal-resource manuscript remains science-frozen and untouched. The audited D2 theorem manuscript also remains the scientific baseline; PRA R1 is a publication-facing transform of that frozen theorem body, not a new theorem revision.

Current journal-facing title:

> **Exact minimum dynamical cost of prescribed rank-changing quantum-state curvature**

## Scientific center

The paper answers one question:

> Given a rank-changing quantum-state family with prescribed first-order tangent and prescribed feasible metric-contracted second-order population in the baseline-empty target sector, what is the least state-weighted quadratic dynamical coupling needed to realize it?

Central theorem:

`V_min=(1/2)Tr C`

for a prescribed feasible metric-contracted target-kernel Hessian `C`, with `C>=C_min`.

Clean autonomous temporal specialization:

`A_ex^(2)=hbar nu V_min`.

Exact total-energy conservation does not increase the optimum, including in the repaired separable infinite-dimensional construction with unbounded occupied target energies and stationary excess curvature in target-energy shells empty at baseline.

## Canonical source chain

### Frozen theorem/audit layer

- `dynamical_rank_boundary_implementation_cost_draft.tex` — D1 theorem source.
- `dynamical_rank_boundary_implementation_cost_supplement.tex` — D1 proof source.
- `apply_d2_audit_repairs.py` — deterministic D2 theorem-language / implementation-topology repairs.
- `dynamical_rank_boundary_implementation_cost_d2.tex` — committed audited D2 main.
- `dynamical_rank_boundary_implementation_cost_supplement_d2.tex` — committed audited D2 supplement.
- `D2_HOSTILE_THEOREM_LANGUAGE_AUDIT.md` — theorem-language audit.

### Publication-facing PRA R1 layer

- `apply_pra_r1_frontmatter.py` — transforms only the journal-facing main title, abstract/introduction, AI-assisted research disclosure, acknowledgments, and Data Availability layer while freezing the theorem body against D2.
- `apply_pra_r1_supplement_title.py` — changes only the supplement title to the PRA-facing title.
- `dynamical_rank_boundary_implementation_cost_pra_r1.tex` — committed canonical PRA R1 main.
- `dynamical_rank_boundary_implementation_cost_supplement_pra_r1.tex` — committed canonical PRA R1 supplement.
- `check_pra_r1_static.py` — publication identity, title consistency, theorem/proof freeze, disclosure, prior-art marker, reference, and citation gate.
- `check_pra_build_logs.py` — final-pass LaTeX quality gate.
- `references.bib` — standalone bibliography.
- `PRA_R1_FINAL_PUBLICATION_AUDIT_2026-08-23.md` — final publication-facing hostile audit and policy record.
- `MANUSCRIPT_HANDOFF.md` — authoritative current state.

The CI workflow regenerates both committed PRA R1 TeX roots and runs `git diff --exit-code` on them. A transform/source mismatch is therefore a hard failure.

PDFs are reproducible GitHub Actions artifacts rather than committed repository binaries.

## Final verified publication package

Final observable PR-triggered verification:

- workflow run `32667189807`;
- base canonical commit at verification: `d100d526b823ed6a7807d0d4cb344b3ba92a5f42`;
- D2 deterministic generation/static gate: **PASS**;
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

Both exact final PDFs were rendered at 180 dpi and visually inspected. No clipping, overlap, broken glyph, title mismatch, or theorem-layout defect was found. The new `AI-Assisted Research and Verification` / Data Availability page was separately inspected at full resolution and is clean.

### Render-QA correction that must not be undone

An earlier green build was deliberately not promoted because visual inspection caught a package inconsistency: the main used the new PRA title while the supplement still displayed the older D2 “quantum-state jet” title.

The repair is intentionally narrow:

1. `apply_pra_r1_supplement_title.py` creates a publication-facing supplement with the exact PRA main title;
2. `check_pra_r1_static.py` requires title equality and forbids `jet` in either publication title;
3. the same gate requires everything in the publication supplement from `\author{Anonymous}` onward to remain byte-for-byte identical to audited D2.

Do not “simplify” this by compiling the D2 supplement directly for PRA R1.

## Final publication-facing hostile audit

The final audit did not reveal a theorem defect or a direct known collision with the prescribed-curvature optimization theorem. Priority remains **unverified, not certified**.

Two publication-layer corrections were made:

1. **Rank-changing Bures curvature:** Huang et al. (2026), arXiv:2605.27907, studies the Riemannian curvature of the Bures metric near rank-changing states. PRA R1 now explicitly distinguishes that object from this paper's `C`, which is the physical-metric contraction of the second derivative of a specified state family projected into the baseline kernel.
2. **APS disclosure/data policy:** because AI assistance was substantive in derivation exploration, adversarial algebra checks, literature organization, and internal numerical-validation code, PRA R1 now contains a dedicated `AI-Assisted Research and Verification` section rather than relying only on acknowledgments. Data Availability now states that no empirical data were produced, identifies the internal validation scripts, explains that they are not required to reproduce the analytic results, and makes them available from the author on reasonable request.

These changes are publication-layer only. The D2 theorem/proof body remains statically frozen.

## Scope / novelty lock

Do not claim novelty for:

- Bures/Uhlmann or `QFI/4` horizontal purification geometry;
- Riemannian curvature of the Bures metric near rank-changing states;
- channel Fisher/Kraus-gauge/fibre-bundle geometry;
- covariant or energy-conserving Stinespring dilation;
- generic quantum-speed-limit/control-norm inequalities;
- PSD-cone second-order tangent geometry;
- classical nonregular boundary statistics;
- infinite-dimensional QFI/Bures functional analysis.

Candidate distinct content is the exact minimum state-weighted quadratic coupling for an independently prescribed feasible rank-changing target-kernel curvature, its exact energy-conserving attainability, and the autonomous spectral endpoint identity.

## Read first

1. `MANUSCRIPT_HANDOFF.md`
2. `PRA_R1_FINAL_PUBLICATION_AUDIT_2026-08-23.md`
3. `D2_HOSTILE_THEOREM_LANGUAGE_AUDIT.md`
4. `../../autonomous_temporal_information/notes/FOLLOWUP_DYNAMICAL_FINAL_PRIORITY_SEARCH_2026-08-23.md`
5. `../../autonomous_temporal_information/notes/WP33_HOSTILE_AUDIT_WP32_AND_PRIORITY_BOUNDARY.md`
6. `../../autonomous_temporal_information/notes/WP32_REPAIRED_INFINITE_DIMENSIONAL_ENERGY_CONSERVING_2JET_COST.md`

## Immediate work order

1. do **not** reopen theorem development merely to enlarge the manuscript;
2. close disposable verification PRs unmerged after recording their successful runs;
3. immediately before actual submission, re-check current APS submission metadata/policy and replace anonymous author/affiliation metadata in the submission package only;
4. preserve the final promoted PRA R1 sources unless a genuine prior-art, referee, proof, or journal-policy defect requires a revision;
5. keep R3 and D2 scientifically frozen.

## Manuscript integrity

The public manuscript and supplement must remain scientifically standalone. They must contain no personal repository URL, username, repository/project name, internal work-package labels, development history, or instruction that a reader consult internal research files.
