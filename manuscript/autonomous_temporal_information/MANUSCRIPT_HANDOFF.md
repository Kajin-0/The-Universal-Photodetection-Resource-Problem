# Manuscript handoff — autonomous temporal information

**Date:** 2026-08-23

**Branch:** `agent/autonomous-temporal-information-law`

## Phase

**M2R1 — audited proof integration and referee-facing statement cleanup.**

Research theorem production is paused. Do not create WP21 unless manuscript work exposes a concrete theorem defect or genuinely missing result.

## Read order

1. `../../autonomous_temporal_information/notes/PUBLICATION_THEOREM_STACK_AFTER_AUDITS.md`
2. `../../autonomous_temporal_information/notes/HOSTILE_MATHEMATICAL_AUDIT_WP18_WP20.md`
3. `../../autonomous_temporal_information/notes/FOUNDATIONAL_SIGNIFICANCE_PRIORITY_GATE_AFTER_WP20.md`
4. `M2_HOSTILE_THEOREM_LANGUAGE_AND_DIMENSION_AUDIT.md`
5. `THEOREM_PROVENANCE_MATRIX.md`
6. `autonomous_temporal_resource_law_m2r1.tex`
7. `autonomous_temporal_resource_law_supplement_m2r1.tex`
8. the R1 proof files in `proofs/`

All `_draft`, original monolithic supplement, and `_m2` manuscript roots are archival earlier stages.

## Canonical M2R1 files

- `autonomous_temporal_resource_law_m2r1.tex`
- `autonomous_temporal_resource_law_supplement_m2r1.tex`
- `proofs/finite_radius_survival_proofs.tex`
- `proofs/boundary_and_autonomous_action_proofs.tex`
- `proofs/noncommuting_mixed_bridge_proof_r1.tex`
- `proofs/multigap_action_sum_proof_r1.tex`
- `proofs/shared_kernel_qutrit_benchmark.tex`
- `proofs/wp15_exact_common_record_qutrit.tex`
- `references.bib`
- `check_m2_tex_static.py`
- `THEOREM_PROVENANCE_MATRIX.md`
- `M2_HOSTILE_THEOREM_LANGUAGE_AND_DIMENSION_AUDIT.md`
- `README.md`

## Main physical message

The manuscript is about **two physical resource regimes**, not a new generic resource theory of time:

- `R_lin > 0`: robust relative temporal Fisher information is backed by pre-existing spectral survival;
- rank-changing `R_lin = 0`: useful Fisher information is backed by positive second-order endpoint synthesis action.

For globally stationary exact clock--signal exchange, both regimes are two-sided across the relational cut.

## Headline theorem sequence

1. fixed-mean-energy high-frequency local-Fisher counterexample;
2. finite-radius robust Fisher--survival law;
3. autonomous dual-survival law;
4. one-sided/bilateral rank-changing boundary synthesis;
5. sharp autonomous dual synthesis-action law;
6. arbitrary coherent-support mixed survival/synthesis bridge;
7. multi-gap shared-Hessian spectral-action sum.

For publication framing, the one-sided/bilateral boundary pair is one logical result block.

## Audit status

### Literature/significance

**PROVISIONAL PASS for a narrow theorem paper. Priority remains unverified, not certified.**

Broad novelty claims remain prohibited. Mandatory comparisons include Page--Wootters/shared asymmetry, modes of asymmetry, QFI energetic coherence, quantitative WAY/conservation-law coherence cost, rank-changing QFI/Bures geometry, waveform Holevo bounds, and 2026 protocol-level energy-constrained metrology.

### Core mathematics

The earlier research audit passed after:

1. correcting the one-sided sine-coordinate convention to `x-i y` under `D_s=(A-A^dagger)/(2i)`;
2. canonicalizing the mixed action with
   `Pi_out=supp(A A^dagger)`,
   `Pi_in=supp(A^dagger A)`,
   `G_ex=2 hbar nu Q(Pi_out+Pi_in)Q`.

### M2 hostile theorem-language audit

The R1 source revision additionally fixes four literal statement vulnerabilities without changing the scientific coefficients:

1. **finite-dimensional scope** is explicit; no arbitrary infinite-dimensional functional-analytic extension is claimed;
2. **mixed degenerate orientations** are separated from the bilateral `Psi` formula: plus-only, minus-only, and no-synthesis cases have their own inequalities;
3. **zero shorting constants / zero restricted action costs** are handled as unavailable or vacuous scalar resource directions, never as divisions by zero;
4. **multi-gap null directions and parameter metric** are explicit: a nonzero cost-null synthesized direction has `gamma_k=0`, and all Fisher/Hessian traces use the fixed Euclidean cosine--sine quadrature metric.

The audited one-sided mixed limit recovers exactly

`A_ex^(2) >= (hbar nu/2) Tr F_N/N`,

and the bilateral clean limit remains

`A_ex^(2) >= (hbar nu/4) Tr F_N/N`.

## Self-contained qutrit benchmark

`proofs/shared_kernel_qutrit_benchmark.tex` now defines the shared-kernel model before the WP15 witness proof. It records:

- `rho0=P/2`, with rank-two support;
- `A=|1><0|-sqrt(2)|2><1|`;
- `J_B^+=J_B^-=5/4`, `J_+=7/4`, `J_-=3`;
- minimal `C_Delta=(19/4)Q`;
- canonical `G_ex/(hbar nu)=diag(2,4,2)`;
- `g_+=g_-=13 hbar nu/4`;
- `4 A_ex=247 hbar nu/16`;
- physical resource ceiling `12`;
- SLD trace `43/4`;
- followed by the exact WP15 common-record supremum `55/8`.

Thus the supplement no longer requires the research notes to define the benchmark.

## Build and source-integrity gate

Isolated workflow:

`.github/workflows/autonomous-temporal-manuscript-check.yml`

Current sequence:

1. run `python check_m2_tex_static.py` against the audited M2R1 roots;
2. compile `autonomous_temporal_resource_law_m2r1.tex`;
3. compile `autonomous_temporal_resource_law_supplement_m2r1.tex`;
4. upload M2R1 PDFs, proof modules, bibliography, static gate, and audit/handoff files.

The static script recursively expands `\input` files and checks duplicate labels, undefined refs, missing BibTeX keys, missing inputs, internal draft markers, and the known bilateral-score notation failure mode.

**Do not claim build verification until a concrete successful Actions result/log is retrieved.** This session's GitHub connector does not expose push-triggered workflow runs, and the local runtime cannot materialize GitHub repository files for an independent TeX build.

## Remaining work

1. post-rewrite hostile consistency audit of `autonomous_temporal_resource_law_m2r1.tex` against the R1 proof modules;
2. verify that every mixed special case and unavailable-resource branch is literally stated without hidden undefined quantities;
3. check bibliography coverage and manuscript wording for every standard mathematical ingredient;
4. once those gates pass, compress the abstract/introduction into publication prose and assess current journal positioning;
5. no new theorem production unless these audits reveal a genuine mathematical gap.

## Claim lock

Allowed working novelty sentence, always qualified by unverified priority:

> We derive finite-copy arbitrary-POVM spectral-resource laws for globally stationary relative temporal modes that distinguish a finite-radius regime backed by pre-existing two-sided spectral survival from a rank-changing zero-radius regime backed by positive second-order two-sided endpoint synthesis action, with sharp fixed-shell and multi-frequency constructions.

Do not strengthen this without a new priority audit.
