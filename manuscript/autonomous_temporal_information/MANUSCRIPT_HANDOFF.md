# Manuscript handoff — autonomous temporal information

**Date:** 2026-08-23

**Branch:** `agent/autonomous-temporal-information-law`

## Phase

**M2 — proof integration and hostile manuscript audit.**

Research theorem production is paused. Do not create WP21 unless manuscript work exposes a concrete theorem defect or genuinely missing result.

## Read order

1. `../../autonomous_temporal_information/notes/PUBLICATION_THEOREM_STACK_AFTER_AUDITS.md`
2. `../../autonomous_temporal_information/notes/HOSTILE_MATHEMATICAL_AUDIT_WP18_WP20.md`
3. `../../autonomous_temporal_information/notes/FOUNDATIONAL_SIGNIFICANCE_PRIORITY_GATE_AFTER_WP20.md`
4. `THEOREM_PROVENANCE_MATRIX.md`
5. `autonomous_temporal_resource_law_m2.tex`
6. `autonomous_temporal_resource_law_supplement_m2.tex`
7. the files in `proofs/`

The earlier `autonomous_temporal_resource_law_draft.tex` and `autonomous_temporal_resource_law_supplement.tex` are archival M1 snapshots.

## Canonical M2 files

- `autonomous_temporal_resource_law_m2.tex` — main paper with theorem statements and concise proof cores.
- `autonomous_temporal_resource_law_supplement_m2.tex` — supplement master that inputs modular proofs.
- `proofs/finite_radius_survival_proofs.tex`
- `proofs/boundary_and_autonomous_action_proofs.tex`
- `proofs/noncommuting_mixed_bridge_proof.tex`
- `proofs/multigap_action_sum_proof.tex`
- `proofs/wp15_exact_common_record_qutrit.tex`
- `references.bib`
- `check_m2_tex_static.py`
- `THEOREM_PROVENANCE_MATRIX.md`
- `README.md`

## Current theorem sequence

1. fixed-mean-energy high-frequency local-Fisher counterexample;
2. finite-radius robust Fisher--survival law;
3. autonomous dual-survival law;
4. one-sided rank-changing boundary synthesis;
5. bilateral boundary Minkowski law;
6. sharp autonomous dual synthesis-action law;
7. arbitrary coherent-support mixed survival/synthesis bridge;
8. multi-gap shared-Hessian spectral-action sum.

For publication framing, items 4--5 are one logical boundary-result block, giving a six-result narrative.

## Main physical message

The manuscript is about **two physical resource regimes**, not a new generic resource theory of time:

- `R_lin > 0`: robust relative temporal Fisher information is backed by pre-existing spectral survival;
- rank-changing `R_lin = 0`: useful Fisher information is backed by positive second-order endpoint synthesis action.

For globally stationary exact clock--signal exchange, both regimes are two-sided across the relational cut.

## Audit status

### Literature/significance

**PROVISIONAL PASS for a narrow theorem paper. Priority remains unverified, not certified.**

Broad novelty claims are prohibited. Mandatory comparisons remain Page--Wootters/shared asymmetry, modes of asymmetry, QFI energetic coherence, quantitative WAY/conservation-law coherence cost, rank-changing QFI/Bures geometry, waveform Holevo bounds, and 2026 total-protocol energy-constrained metrology.

### Mathematics

**PASS after the recorded research-note corrections:**

1. convention-consistent one-sided family uses `x-i y` under `D_s=(A-A^dagger)/(2i)`;
2. canonical mixed action uses
   `Pi_out=supp(A A^dagger)`,
   `Pi_in=supp(A^dagger A)`,
   `G_ex=2 hbar nu Q(Pi_out+Pi_in)Q`.

The inherited WP07/WP18 sine-coordinate erratum is recorded in
`../../autonomous_temporal_information/notes/WP07_WP18_SINE_COORDINATE_CONVENTION_ERRATUM.md`.

## M2 integration completed

### Main paper

`autonomous_temporal_resource_law_m2.tex` removes the M1 `SOURCE` and internal proof-map comments and adds concise proof cores for every headline theorem. The fixed-shell sharp constructions remain in the main text because they are part of the physical claim, not merely technical proof detail.

### Supplement

`autonomous_temporal_resource_law_supplement_m2.tex` is the canonical modular master. It inputs:

- finite-radius arbitrary-POVM and exact finite-copy scaling proof;
- rank-changing PSD curvature, bilateral Minkowski, and autonomous `1/4` / `1/2` coefficients;
- arbitrary-support shorted-survival + canonical endpoint-incidence `Psi_a` bridge;
- shared-Hessian multi-gap action sum and full Fourier Fisher matrix;
- exact WP15 `55/8` common-record quadratic witness and limiting projective sequence.

### Standard mathematical prior art now seeded explicitly

The bibliography includes verified entries for:

- Anderson--Trapp shorted operators, DOI `10.1137/0128007`;
- Shapiro nonlinear-SDP second-order analysis, DOI `10.1007/BF02614439`;
- Bonnans--Cominetti--Shapiro parabolic second-order tangent sets, DOI `10.1137/S1052623496306760`.

These are infrastructure, not novelty claims.

## Build and source-integrity gate

Isolated workflow:

`.github/workflows/autonomous-temporal-manuscript-check.yml`

Current sequence:

1. run `python check_m2_tex_static.py`;
2. compile `autonomous_temporal_resource_law_m2.tex`;
3. compile `autonomous_temporal_resource_law_supplement_m2.tex`;
4. upload M2 PDFs and all proof/control files.

The static script recursively expands `\input` files and checks duplicate labels, undefined refs, missing BibTeX keys, missing inputs, and known draft/notation failure modes.

**Do not claim build verification until a concrete successful Actions result/log is retrieved.** This session's GitHub connector does not expose push-triggered workflow runs, and the local runtime cannot materialize GitHub repository files for an independent TeX build.

## Resolved false alarm

A previously suspected literal `\nu_y` score-variable defect was a connector JSON rendering ambiguity (`\n` newline followed by `u_y`), not a source-level Greek-nu command. The canonical M2 static gate nevertheless checks for that specific failure mode.

## Remaining M2 tasks

1. hostile line-by-line theorem-language audit of `autonomous_temporal_resource_law_m2.tex` against the proof modules;
2. dimensional/unit audit of every action coefficient and every `g`, `gamma`, `Psi` argument;
3. ensure the WP15 qutrit proof module is self-contained enough for a referee without requiring the research notes;
4. check bibliography coverage for every standard mathematical ingredient invoked in prose;
5. only then perform publication-style abstract/introduction compression and journal positioning;
6. no new theorem production unless one of these audits reveals a real mathematical gap.

## Claim lock

Allowed working novelty sentence, always qualified by unverified priority:

> We derive finite-copy arbitrary-POVM spectral-resource laws for globally stationary relative temporal modes that distinguish a finite-radius regime backed by pre-existing two-sided spectral survival from a rank-changing zero-radius regime backed by positive second-order two-sided endpoint synthesis action, with sharp fixed-shell and multi-frequency constructions.

Do not strengthen this without a new priority audit.
