# AGENTS.md

## Purpose

Durable handoff for **The Universal Photodetection Resource Problem (UPRP)**. The repository, not chat history, is authoritative.

Research is analytical/theoretical. Numerical analysis of published data is allowed for validation and illustration. Do not make new experiments, fabrication, procurement, or laboratory campaigns necessary next steps.

Active branch: `agent/uprp-core-theorem-round10`

## Read first

1. `docs/CURRENT_RESEARCH_STATE.md`
2. `notes/RESEARCH_LOG_ROUND20_LITERATURE_IRF_EXAMPLE.md`
3. `submission/PRAPPLIED_PACKAGE_VALIDATION_REV10.md`
4. `submission/SUBMISSION_PACKAGE_CHECKLIST_REV10.md`
5. `manuscript/section_worked_irf_example_rev10.tex`
6. `manuscript/section_practical_grounding_rev9.tex`
7. `notes/RESEARCH_LOG_ROUND19_EMPIRICAL_GROUNDING.md`
8. `notes/RESEARCH_LOG_ROUND18_TRANSLATIONAL_GROUNDING.md`
9. `notes/RESEARCH_LOG_ROUND17.md`
10. `notes/RESEARCH_LOG_ROUND16.md`

## Current publication state — Rev10

**Rev10 is the preferred first-paper submission candidate.**

Reproducible source chain:

1. frozen theorem source: `manuscript/event_resource_theorem_rev7.tex`;
2. Rev8 referee repair: `manuscript/apply_rev8_referee_surgical.py`;
3. Rev9 operational/empirical grounding: `manuscript/apply_rev9_grounding.py`;
4. Rev10 published-IRF worked example: `manuscript/apply_rev10_literature_example.py`.

Hash manifests: `REV8_SHA256SUMS.txt`, `REV9_SHA256SUMS.txt`, `REV10_SHA256SUMS.txt`.

Rev10 changes **no theorem or proof**. It adds one worked example using approximate graphical digitization of Spinelli et al. 1998 Fig. 3.

Key applied result:

- reported FWHM: MCP `25 ps`, DJ-SPAD `35 ps` -> FWHM ranks MCP faster;
- Gaussian-from-FWHM `B_FI`: MCP `13.29 GHz`, DJ-SPAD `9.49 GHz`;
- figure-digitized full-shape `B_FI`: MCP `5.977 GHz`, DJ-SPAD `9.160 GHz`;
- ranking reverses: `B_FI(DJ)/B_FI(MCP)=1.533`.

This is an approximate published-figure digitization, not raw-event reanalysis. Source DOI: `10.1109/3.668769`.

Canonical Rev10 build:

- 32 pages;
- PDF SHA-256 `fe261ba21db5ac04f76e57dd61bc37b105616fe4c3ccabc5bd6b211145055c29`;
- generated source SHA-256 `9d9e8b1a773121dd69e0a378cf235e90e7d89dc01ebe426222a78a8c20500501`.

PRApplied Rev10 copy:

- 33 pages;
- PDF SHA-256 `5ff01f6c9d50fcf6e7e0fd59be34e65911a9abd7459a6a348df3e2c70f63e467`;
- final assembled package ZIP SHA-256 `6670b3e1bd1c0ef133e052bb74c515ca670c6337be43d3805f09f0e627ce201f`.

Steady-state CI is read-only. It regenerates Rev8, verifies hashes, regenerates Rev9, verifies hashes, generates Rev10, verifies hashes, reproduces the literature-example numbers, compiles Rev10, and uploads the artifact.

## First-paper theorem class

Autonomous/time-translation-invariant, independent-event / low-overlap, one-primary-registration photodetection under weak coherent/Poisson direct-detection intensity modulation, retaining the complete accessible primary-event mark.

Do **not** describe this as a universal speed limit for all photodetectors.

Per incident photon,

`K(dm,dτ)=κ(dm) μ_m(dτ)`, `η=κ(M)<=1`.

Exact transfer:

`G(ω)=∫ |H_m(ω)|^2 κ(dm)`.

Exact DC: `G(0)=η`.

Complete local weak-waveform Fisher operator:

`[F_out]_{ab} = Φ0/(2π) ∫ G(ω) S_a*(ω) S_b(ω) dω`.

Pointwise `G_A>=G_B` iff detector A locally Fisher-dominates B for every admitted finite weak-waveform task. This is **not** generic Blackwell dominance.

For square-integrable timing densities:

`R2 = 2∫κ(dm)∫f_m^2 dt`,

`B_FI = R2/(4η) <= H/(4η)`.

A common hazard ceiling gives `B_FI <= Λ/4`.

Band-retention inverse costs:

`R2 >= 4Bq`, `H >= 4Bq`.

For one unresolved mark:

`B_FI = (1/2)∫f^2 dt`.

Histogram estimator with equal bins `Δt`:

`B_FI^(Δt)= [1/(2Δt)] Σ p_i^2`,

unbiased finite-count estimator:

`Bhat_FI,U^(Δt)= [1/(2Δt)] Σ n_i(n_i-1)/[N(N-1)]`.

Finite binning lowers the inferred value. Finite support of length `T` gives `B_FI >= 1/(2T)`, not an upper bound. A separate density ceiling `||f||∞<=M` gives `B_FI<=M/2`.

A perfect latency-resolving primary mark gives `G=η` at all frequency. A downstream TDC does not recreate information already lost before the primary record.

The cascade product law applies to independent unresolved stochastic delay stages, not automatically to deterministic TIA transfer functions.

## Rev8 thermodynamic repair — mandatory

Appendix A must keep `acp >= bqs`, ensuring `f_R-r_R = R(acp-bqs)/(RD+E) >= 0` for every `R>0`.

Stationary one-way activity is total directed stationary jump traffic. Aggregate stationary activity/EPR/throughput alone do not set an absolute microscopic time scale.

## Novelty posture

Do not claim first information-theoretic detector timing analysis, first IRF-information result, first generic FI transfer function, generic Blackwell dominance, arbitrary fixed-FWHM no-go, or a universal all-detector speed limit.

Defensible contribution: a temporal-information resource theory for autonomous marked photodetection event channels in which the exact marked-delay spectrum is the complete local weak-waveform Fisher multiplier; pointwise ordering completely characterizes local weak-waveform Fisher dominance; collision and hazard resources give exact/inverse bandwidth laws; and the framework is directly computable from timing laws, histograms, and now a worked published-IRF example showing that FWHM can reverse a real detector ranking.

## Immediate next action

**Stop adding first-paper theory, literature, or worked examples by default.**

Remaining submission blockers are factual/personal:

- author name/order;
- affiliation(s);
- corresponding-author email;
- ORCID;
- truthful substantive-AI disclosure describing human direction and verification;
- applicable funding/conflict/prior-submission declarations.

Do not submit until these are supplied. Reopen science only for a concrete defect or specific referee request.
