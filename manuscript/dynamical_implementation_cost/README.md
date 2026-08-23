# Dynamical implementation cost — follow-up manuscript workspace

## Status

**PRA R1 publication-facing package promoted, build-verified, render-inspected, and deterministically source-locked.**

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

- `apply_pra_r1_frontmatter.py` — transforms only the journal-facing main title, abstract/introduction, acknowledgments/disclosure, and Data Availability layer while freezing the theorem body against D2.
- `apply_pra_r1_supplement_title.py` — changes only the supplement title to the PRA-facing title.
- `dynamical_rank_boundary_implementation_cost_pra_r1.tex` — committed canonical PRA R1 main.
- `dynamical_rank_boundary_implementation_cost_supplement_pra_r1.tex` — committed canonical PRA R1 supplement.
- `check_pra_r1_static.py` — publication identity, title consistency, theorem/proof freeze, disclosure, reference, and citation gate.
- `check_pra_build_logs.py` — final-pass LaTeX quality gate.
- `references.bib` — standalone bibliography.
- `MANUSCRIPT_HANDOFF.md` — authoritative current state.

The CI workflow regenerates both committed PRA R1 TeX roots and runs `git diff --exit-code` on them. A transform/source mismatch is therefore a hard failure.

PDFs are reproducible GitHub Actions artifacts rather than committed repository binaries.

## Verified publication package

Corrected PRA R1 verification run:

- workflow run `32666263610`;
- PRA R1 deterministic main generation: **PASS**;
- PRA R1 deterministic supplement generation: **PASS**;
- standalone/theorem-and-proof freeze gate: **PASS**;
- main LaTeX compile: **PASS**;
- supplement LaTeX compile: **PASS**;
- final build-log quality gate: **PASS**;
- artifact upload: **PASS**.

Corrected artifact:

- artifact ID `9500112341`;
- SHA-256 `6dccb86d7310c15fc25d36927f91c031bc8002a4c709b18e8637d5f3640a73fb`;
- main: **11 pages**;
- supplement: **10 pages**.

Both PDFs were rendered and visually inspected. No clipping, overlap, broken glyph, or theorem-layout defect was found.

A prior green build was deliberately not promoted because render QA caught a stale D2 title on the supplement. The publication-facing supplement is now generated separately, and the static gate requires its title to match the main paper while keeping everything from the author declaration onward byte-for-byte identical to audited D2.

## Scope / novelty lock

Do not claim novelty for:

- Bures/Uhlmann or `QFI/4` horizontal purification geometry;
- channel Fisher/Kraus-gauge/fibre-bundle geometry;
- covariant or energy-conserving Stinespring dilation;
- generic quantum-speed-limit/control-norm inequalities;
- PSD-cone second-order tangent geometry;
- classical nonregular boundary statistics;
- infinite-dimensional QFI/Bures functional analysis.

Candidate distinct content is the exact minimum state-weighted quadratic coupling for an independently prescribed feasible rank-changing target-kernel curvature, its exact energy-conserving attainability, and the autonomous spectral endpoint identity. Priority remains **unverified, not certified**.

## Read first

1. `MANUSCRIPT_HANDOFF.md`
2. `D2_HOSTILE_THEOREM_LANGUAGE_AUDIT.md`
3. `../../autonomous_temporal_information/notes/FOLLOWUP_DYNAMICAL_FINAL_PRIORITY_SEARCH_2026-08-23.md`
4. `../../autonomous_temporal_information/notes/WP33_HOSTILE_AUDIT_WP32_AND_PRIORITY_BOUNDARY.md`
5. `../../autonomous_temporal_information/notes/WP32_REPAIRED_INFINITE_DIMENSIONAL_ENERGY_CONSERVING_2JET_COST.md`

## Immediate work order

1. do not reopen theorem development merely to enlarge the paper;
2. run one final publication-facing hostile significance/claim/citation read on PRA R1 as actually written;
3. verify the current APS submission/disclosure requirements immediately before submission;
4. replace anonymous author/affiliation metadata only at submission packaging time;
5. keep R3 and D2 scientifically frozen unless a genuine referee/prior-art defect requires a correction.

## Manuscript integrity

The public manuscript and supplement must remain scientifically standalone. They must contain no personal repository URL, username, repository/project name, internal work-package labels, development history, or instruction that a reader consult internal research files.
