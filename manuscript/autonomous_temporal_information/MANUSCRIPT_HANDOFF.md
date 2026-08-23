# Manuscript handoff — autonomous temporal information

**Date:** 2026-08-23

**Branch:** `agent/autonomous-temporal-information-law`

## Phase

**M1 — theorem-first manuscript formation.**

Research theorem production is paused. Do not create WP21 unless manuscript drafting exposes a concrete missing theorem or defect.

## Authoritative scope

Read in this order:

1. `../../autonomous_temporal_information/notes/PUBLICATION_THEOREM_STACK_AFTER_AUDITS.md`
2. `../../autonomous_temporal_information/notes/HOSTILE_MATHEMATICAL_AUDIT_WP18_WP20.md`
3. `../../autonomous_temporal_information/notes/FOUNDATIONAL_SIGNIFICANCE_PRIORITY_GATE_AFTER_WP20.md`
4. `THEOREM_PROVENANCE_MATRIX.md`
5. `autonomous_temporal_resource_law_draft.tex`
6. `autonomous_temporal_resource_law_supplement.tex`

## Current files

- `autonomous_temporal_resource_law_draft.tex` — theorem-first main manuscript.
- `autonomous_temporal_resource_law_supplement.tex` — proof-first supplement skeleton.
- `references.bib` — verified seed bibliography.
- `THEOREM_PROVENANCE_MATRIX.md` — assumption/source/validator/prior-art control matrix.
- `README.md` — workspace scope lock.

## Main theorem sequence already drafted

1. fixed-mean-energy high-frequency local-Fisher counterexample;
2. finite-radius robust Fisher--survival law;
3. autonomous dual-survival law;
4. one-sided rank-changing boundary synthesis law;
5. bilateral boundary Minkowski law;
6. sharp autonomous dual synthesis-action law;
7. arbitrary coherent-support mixed survival/synthesis bridge;
8. multi-gap shared-Hessian spectral-action sum.

The numbering will later be compressed into six headline results; the boundary one-sided/bilateral pair are logically one result block.

## Main physical message

The manuscript is about **two resource regimes**, not about inventing a new resource theory of time:

- `R_lin > 0`: robust relative temporal Fisher information is backed by pre-existing spectral survival;
- `R_lin = 0` at a physical rank-changing boundary: useful Fisher information is backed by positive second-order endpoint synthesis action.

For globally stationary exact clock--signal exchange, both regimes are two-sided across the relational cut.

## Audit status

### Literature/significance

**PROVISIONAL PASS for a narrow theorem paper.** Priority is unverified, not certified.

Broad novelty claims are prohibited. Mandatory comparisons include Page--Wootters/shared asymmetry, modes of asymmetry, QFI energetic coherence, quantitative WAY/conservation-law coherence cost, rank-changing QFI/Bures geometry, waveform Holevo bounds, and 2026 total-protocol energy-constrained metrology.

### Mathematics

**PASS after two targeted research-note corrections:**

1. one-sided sine-coordinate sign corrected (`x-i y` under the branch convention);
2. WP19 action canonicalized with
   `Pi_out=supp(A A^dagger)`,
   `Pi_in=supp(A^dagger A)`,
   `G_ex=2 hbar nu Q(Pi_out+Pi_in)Q`.

A later source audit found the same harmless sine-coordinate reversal already present in WP07's illustrative ket; this is recorded in

`../../autonomous_temporal_information/notes/WP07_WP18_SINE_COORDINATE_CONVENTION_ERRATUM.md`.

## Compilation gate

An isolated workflow exists:

`.github/workflows/autonomous-temporal-manuscript-check.yml`.

It is now configured to compile **both** the main manuscript and supplement and upload both PDFs.

Do not claim build verification until a concrete GitHub Actions job result/log has been retrieved. The current connector's commit-run lookup only exposes PR-triggered runs and has not returned a push run.

## Known M1 blockers / TODOs

### 1. One supplement notation typo — must fix before declaring M1 clean

In the bilateral-score section of `autonomous_temporal_resource_law_supplement.tex`, the source currently reads

`\begin{equation}\nu_y=...`

while the following norm uses `u`.

The intended variable is

`u_y=Tr(XM_y)/sqrt(p_y)`.

This is a semantic notation defect, not a theorem defect. It may compile because `\nu` is valid TeX. Fix it before the supplement is considered notation-clean.

### 2. WP15 exact witness proof not yet inserted

The supplement records the exact hierarchy

`12 > 43/4 > 55/8`

but currently only states that the full Hermitian quadratic witness proof will be inserted in M2. This is acceptable for the M1 skeleton but must be completed before submission.

### 3. Full main-text proofs are not yet written

The main draft contains theorem statements, proof summaries, extremizers, scope text, and internal proof-map comments. M2 should replace internal proof-map comments by concise proof cores and move full derivations to the supplement.

### 4. Bibliography is a verified seed, not final literature coverage

Citation keys currently used by the main and supplement are present in `references.bib`. The final manuscript will require additional direct citations for PSD-cone second-order geometry, Anderson--Trapp shorting, and any quantitative WAY/relative-phase references used in prose.

## M1 checks already completed

- Main theorem statements checked directly against WP02, WP03/WP06, WP07, WP09, audited WP18, WP19, and WP20 notes.
- Finite-copy factor conventions rechecked.
- Boundary coefficient `J <= Delta T` rechecked directly from WP07.
- Citation-key audit: all currently cited keys exist in `references.bib`.
- Supplement now gives all four noncommuting-support shorting constants and explicit formulas for `a_+` and `a_-`.
- Isolated CI does not modify or depend on the frozen Rev11 generation pipeline.

## Next work order

1. Fix the single `\nu_y` / `u_y` supplement typo.
2. Retrieve or otherwise establish a concrete CI compilation result; fix any LaTeX/BibTeX errors.
3. Run a notation audit across main and supplement (`P,Q,A,X,Y,J_\pm,C_\Delta,G_{ex},A^{(2)}` especially).
4. Begin M2: insert concise main proofs and complete the supplement proof blocks.
5. Add the exact WP15 `55/8` witness proof to the supplement.
6. Only after the theorem/proof text is stable, rewrite the working abstract and introduction for publication style.

## Claim lock

Allowed working novelty sentence, always qualified by unverified priority:

> We derive finite-copy arbitrary-POVM spectral-resource laws for globally stationary relative temporal modes that distinguish a finite-radius regime backed by pre-existing two-sided spectral survival from a rank-changing zero-radius regime backed by positive second-order two-sided endpoint synthesis action, with sharp fixed-shell and multi-frequency constructions.

Do not strengthen this without a new priority audit.
