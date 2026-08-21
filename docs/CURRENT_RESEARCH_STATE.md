# Current Research State

**Date:** 2026-08-20

Active branch: `agent/uprp-core-theorem-round10`

## Immediate status

The first-paper foundational research phase is **closed by default**.

Current preferred submission candidate: **Rev10**.

Rev10 preserves the complete Rev9 theorem stack and adds one worked applied demonstration using approximate graphical digitization of a published detector IRF. No theorem, proof, or resource inequality changed.

Read first:

1. `AGENTS.md`
2. `notes/RESEARCH_LOG_ROUND20_LITERATURE_IRF_EXAMPLE.md`
3. `submission/PRAPPLIED_PACKAGE_VALIDATION_REV10.md`
4. `submission/SUBMISSION_PACKAGE_CHECKLIST_REV10.md`
5. `manuscript/section_worked_irf_example_rev10.tex`
6. `manuscript/analyze_spinelli1998_fig3_rev10.py`

## Reproducible source chain

1. Rev7 frozen theorem source -> Rev8 via `apply_rev8_referee_surgical.py`.
2. Rev8 -> Rev9 via `apply_rev9_grounding.py`.
3. Rev9 -> Rev10 via `apply_rev10_literature_example.py`.

Expected hashes are pinned in `REV8_SHA256SUMS.txt`, `REV9_SHA256SUMS.txt`, and `REV10_SHA256SUMS.txt`.

Generated Rev10 main source SHA-256:

`9d9e8b1a773121dd69e0a378cf235e90e7d89dc01ebe426222a78a8c20500501`

## New Rev10 applied result

Source: Spinelli et al., *Avalanche Detector with Ultraclean Response for Time-Resolved Photon Counting*, IEEE JQE 34, 817–821 (1998), DOI `10.1109/3.668769`.

The paper reports normalized IRFs for a DJ-SPAD and MCP in the same figure and FWHM values of 35 ps and 25 ps, respectively. FWHM therefore ranks the MCP as faster.

Approximate graphical digitization of the published full response shapes gives:

- DJ-SPAD: `B_FI = 9.160 GHz`;
- MCP: `B_FI = 5.977 GHz`;
- ratio: `B_FI(DJ)/B_FI(MCP)=1.533`.

Assuming Gaussian timing laws from FWHM alone would instead give 9.49 GHz and 13.29 GHz. Thus a conventional FWHM ranking reverses when the full IRF shape is used. The manuscript explicitly labels this as approximate figure digitization, not raw-TCSPC reanalysis.

The digitized points and dependency-free analysis script are included in `manuscript/`.

## Validation

Canonical Rev10 build:

- 32 pages;
- PDF SHA-256 `fe261ba21db5ac04f76e57dd61bc37b105616fe4c3ccabc5bd6b211145055c29`;
- no undefined citations or cross-references;
- only material overfull warning is the inherited approximately `2.45667 pt` `timing-concentration` line in Appendix A;
- worked-example and shifted neighboring pages visually inspected.

PRApplied Rev10 copy:

- 33 pages;
- PDF SHA-256 `5ff01f6c9d50fcf6e7e0fd59be34e65911a9abd7459a6a348df3e2c70f63e467`;
- package ZIP SHA-256 `5ab6c380c3f9efd4b52babb1ec1d6249229abda06dd5483f14771a750b12b42b`;
- Data Availability updated because the manuscript now analyzes a published figure;
- worked-example, Data Availability/Appendix transition, and final reference pages visually inspected.

Steady-state CI remains read-only and now regenerates/hash-checks Rev8, Rev9, and Rev10, reproduces the Spinelli calculation, compiles Rev10, and uploads the artifact.

## Theorem status

No Rev10 theorem changes were made.

The theorem class remains autonomous/time-translation-invariant, independent-event/low-overlap, one-primary-registration photodetection under weak coherent/Poisson direct-detection intensity modulation with complete accessible primary-event marks.

Core exact transfer:

`G(ω)=∫|H_m(ω)|^2 κ(dm)`.

Complete local weak-waveform Fisher operator:

`[F_out]_{ab}=Φ0/(2π)∫G(ω)S_a*(ω)S_b(ω)dω`.

Pointwise ordering of `G` is necessary and sufficient for local Fisher dominance over every admitted finite weak temporal waveform task.

For square-integrable timing densities:

`B_FI = R2/(4η) <= H/(4η)`.

Inverse resource cost:

`R2 >= 4Bq`, `H >= 4Bq`.

For a single unresolved mark:

`B_FI = (1/2)∫f^2 dt`.

## Submission state

Primary target remains **Physical Review Applied — Regular Article**.

Data Availability is no longer the old “purely mathematical/no data analyzed” sentence. Rev10 truthfully states that no new experiments were generated, but the worked example uses an approximate graphical digitization of a published detector figure and supplies the digitized points/script.

Remaining blockers are factual/personal only:

- author name/order;
- affiliation(s);
- corresponding-author email;
- ORCID;
- truthful substantive-AI acknowledgment describing human direction and verification;
- applicable funding/conflict/prior-submission declarations.

Do not start another science/literature revision unless a new concrete defect or specific referee request is identified.
