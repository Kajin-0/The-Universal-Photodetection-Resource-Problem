# Current Research State

**Date:** 2026-08-21

Active branch: `agent/uprp-core-theorem-round10`

## Immediate status

The first-paper scientific phase is **closed by default**.

Current preferred submission candidate: **Rev11**.

Rev11 preserves the complete Rev10 theorem stack and worked published-IRF demonstration. It adds the final literature/positioning correction that the single-unresolved-mark Fisher-equivalent bandwidth is mathematically the conventional one-sided equivalent noise bandwidth (ENBW) of the normalized timing transfer function. No theorem, proof, resource inequality, or Spinelli worked-example number changed.

Read first:

1. `AGENTS.md`
2. `notes/RESEARCH_LOG_ROUND21_ENBW_POSITIONING.md`
3. `submission/PRAPPLIED_PACKAGE_VALIDATION_REV11.md`
4. `submission/SUBMISSION_PACKAGE_CHECKLIST_REV11.md`
5. `manuscript/apply_rev11_enbw_positioning.py`
6. `manuscript/REV11_SHA256SUMS.txt`

## Reproducible source chain

1. Rev7 frozen theorem source -> Rev8 via `apply_rev8_referee_surgical.py`.
2. Rev8 -> Rev9 via `apply_rev9_grounding.py`.
3. Rev9 -> Rev10 via `apply_rev10_literature_example.py`.
4. Rev10 -> Rev11 via `apply_rev11_enbw_positioning.py`.

Expected hashes are pinned in `REV8_SHA256SUMS.txt` through `REV11_SHA256SUMS.txt`.

## Rev11 ENBW positioning

For one unresolved mark,

`G(ω)=η|H(ω)|²`, `H(0)=1`, hence

`B_FI = ∫_0^∞ |H(2πf)|² df = B_ENBW`.

Rev11 explicitly acknowledges that this scalar integral and the first-order `π/2` ratio are conventional ENBW results. Standard reference added: C. D. Motchenbacher and J. A. Connelly, *Low-Noise Electronic System Design* (Wiley, 1993), ISBN 9780471577423.

The distinct contribution remains the event-registration/Fisher interpretation, retained-mark transfer `G=∫|H_m|²κ(dm)`, collision-resource identity, microscopic hazard bounds, complete weak-waveform Fisher ordering, inverse resource costs, no-go results, and direct detector/histogram applications.

Rev11 also adds a multinomial plug-in bootstrap prescription for finite-count uncertainty of the binned pair-collision estimator, explicitly excluding systematic instrument/deconvolution uncertainty.

## Rev10 worked detector result retained

Spinelli et al., IEEE JQE 34, 817–821 (1998), DOI `10.1109/3.668769`:

- DJ-SPAD: FWHM `35 ps`, Gaussian-from-FWHM `9.49 GHz`, figure-digitized `B_FI=9.160 GHz`;
- MCP: FWHM `25 ps`, Gaussian-from-FWHM `13.29 GHz`, figure-digitized `B_FI=5.977 GHz`;
- ranking reversal: `B_FI(DJ)/B_FI(MCP)=1.533`.

This is explicitly approximate figure digitization, not raw-TCSPC reanalysis.

## Validation

Canonical Rev11:

- 33 pages;
- generated source SHA-256 `fe966f4ab3fa067bb94d200ed09605a1ed3a2cdef9b4488fd0d18a55e95ccb6e`;
- practical-section SHA-256 `ae596eb3866fb0d4d628cb0b527e281d802badc6262e68d3618366bb49903ce3`;
- PDF SHA-256 `9eedbf562ed5fa70b78a8c1c63627e1c578f149074f7f25f3fd3988c8668ecef`;
- no undefined citations/references;
- only inherited ~2.45667 pt `timing-concentration` Appendix overfull warning;
- affected pages visually inspected.

PRApplied Rev11:

- 33 pages;
- PDF SHA-256 `d9e4a3330543106a272d4aa7b26cf6187bbd2f6ef170db4a8927b06edb824db7`;
- package ZIP SHA-256 `b9f1abff76bbcc7a97ca8b2c3038f1e44e5adbb68f230cdb7d13c02431b6183e`;
- Data Availability remains truthful for the published-figure analysis;
- ENBW, estimator, Data Availability/Appendix, and reference pages visually inspected.

Steady-state CI remains read-only and now generates/hash-checks Rev8, Rev9, Rev10, reproduces the Spinelli calculation, generates/hash-checks Rev11, compiles Rev11, and uploads the artifact.

## Theorem status

No Rev11 theorem changes were made.

The theorem class remains autonomous/time-translation-invariant, independent-event/low-overlap, one-primary-registration photodetection under weak coherent/Poisson direct-detection intensity modulation with complete accessible primary-event marks.

Core exact transfer:

`G(ω)=∫|H_m(ω)|² κ(dm)`.

Complete local weak-waveform Fisher operator:

`[F_out]_{ab}=Φ0/(2π)∫G(ω)S_a*(ω)S_b(ω)dω`.

Pointwise ordering of `G` is necessary and sufficient for local Fisher dominance over every admitted finite weak temporal waveform task.

For square-integrable timing densities:

`B_FI=R2/(4η)<=H/(4η)`.

Inverse resource cost:

`R2>=4Bq`, `H>=4Bq`.

## Submission state

Primary target remains **Physical Review Applied — Regular Article**.

Remaining blockers are factual/personal only:

- author name/order;
- affiliation(s);
- corresponding-author email;
- ORCID;
- truthful substantive-AI acknowledgment describing human direction and verification;
- applicable funding/conflict/prior-submission declarations.

Do not start another science/literature revision unless a new concrete defect or specific referee request is identified.
