# AGENTS.md

## Purpose

Durable handoff for **The Universal Photodetection Resource Problem (UPRP)**. The repository, not chat history, is authoritative.

Research is analytical/theoretical. Numerical analysis of published data is allowed for validation and illustration. Do not make new experiments, fabrication, procurement, or laboratory campaigns necessary next steps.

Active branch: `agent/uprp-core-theorem-round10`

## Read first

1. `docs/CURRENT_RESEARCH_STATE.md`
2. `notes/RESEARCH_LOG_ROUND21_ENBW_POSITIONING.md`
3. `submission/PRAPPLIED_PACKAGE_VALIDATION_REV11.md`
4. `submission/SUBMISSION_PACKAGE_CHECKLIST_REV11.md`
5. `manuscript/apply_rev11_enbw_positioning.py`
6. `manuscript/REV11_SHA256SUMS.txt`
7. `notes/RESEARCH_LOG_ROUND20_LITERATURE_IRF_EXAMPLE.md`
8. `notes/RESEARCH_LOG_ROUND19_EMPIRICAL_GROUNDING.md`
9. `notes/RESEARCH_LOG_ROUND18_TRANSLATIONAL_GROUNDING.md`

## Current publication state — Rev11

**Rev11 is the preferred first-paper submission candidate.**

Reproducible source chain:

1. frozen theorem source: `manuscript/event_resource_theorem_rev7.tex`;
2. Rev8 referee repair: `manuscript/apply_rev8_referee_surgical.py`;
3. Rev9 operational/empirical grounding: `manuscript/apply_rev9_grounding.py`;
4. Rev10 published-IRF worked example: `manuscript/apply_rev10_literature_example.py`;
5. Rev11 ENBW positioning: `manuscript/apply_rev11_enbw_positioning.py`.

Hash manifests: `REV8_SHA256SUMS.txt`, `REV9_SHA256SUMS.txt`, `REV10_SHA256SUMS.txt`, `REV11_SHA256SUMS.txt`.

Rev11 changes **no theorem, proof, resource inequality, or worked-example number**. It makes the final positioning correction that, for one unresolved mark,

`B_FI = ∫_0^∞ |H(2πf)|² df = B_ENBW`

because `H(0)=1`. This is explicitly acknowledged as the standard one-sided equivalent-noise-bandwidth integral. Do **not** claim novelty for the scalar integral or for the familiar first-order `π/2` ratio.

What remains genuinely distinct is the stochastic event-registration/Fisher interpretation, retained-mark transfer

`G(ω)=∫|H_m(ω)|² κ(dm)`,

its collision-resource area identity, microscopic hazard bounds, universal local weak-waveform Fisher ordering, and inverse resource costs. In general the retained-mark `G` is not the ENBW of the mark-discarded scalar timing law.

Rev11 also adds a practical multinomial plug-in bootstrap for finite-count uncertainty of the binned histogram estimator. It is explicitly limited to counting uncertainty and does not include systematic instrument/deconvolution uncertainty.

Canonical Rev11:

- 33 pages;
- generated source SHA-256 `fe966f4ab3fa067bb94d200ed09605a1ed3a2cdef9b4488fd0d18a55e95ccb6e`;
- PDF SHA-256 `9eedbf562ed5fa70b78a8c1c63627e1c578f149074f7f25f3fd3988c8668ecef`.

PRApplied Rev11:

- 33 pages;
- PDF SHA-256 `d9e4a3330543106a272d4aa7b26cf6187bbd2f6ef170db4a8927b06edb824db7`;
- package ZIP SHA-256 `b9f1abff76bbcc7a97ca8b2c3038f1e44e5adbb68f230cdb7d13c02431b6183e`.

Steady-state CI is read-only. It regenerates/hash-checks Rev8, Rev9, Rev10, reproduces the Spinelli calculation, generates/hash-checks Rev11, compiles Rev11, and uploads the artifact.

## First-paper theorem class

Autonomous/time-translation-invariant, independent-event / low-overlap, one-primary-registration photodetection under weak coherent/Poisson direct-detection intensity modulation, retaining the complete accessible primary-event mark.

Do **not** describe this as a universal speed limit for all photodetectors.

Core exact transfer:

`G(ω)=∫ |H_m(ω)|² κ(dm)`, with `G(0)=η`.

Complete local weak-waveform Fisher operator:

`[F_out]_{ab}=Φ0/(2π)∫G(ω)S_a*(ω)S_b(ω)dω`.

Pointwise `G_A>=G_B` iff detector A locally Fisher-dominates B for every admitted finite weak-waveform task. This is **not** generic Blackwell dominance.

For square-integrable timing densities:

`R2=2∫κ(dm)∫f_m²dt`,

`B_FI=R2/(4η)<=H/(4η)`.

A common hazard ceiling gives `B_FI<=Λ/4`. Band-retention inverse costs remain `R2>=4Bq` and `H>=4Bq`.

For one unresolved mark:

`B_FI=(1/2)∫f²dt=B_ENBW` for the normalized timing transfer.

Histogram estimator:

`B_FI^(Δt)=[1/(2Δt)]Σp_i²`,

`Bhat_FI,U^(Δt)=[1/(2Δt)]Σn_i(n_i-1)/[N(N-1)]`.

Finite binning lowers the inferred value. Finite support of length `T` gives `B_FI>=1/(2T)`, not an upper bound. A separate density ceiling `||f||∞<=M` gives `B_FI<=M/2`.

A perfect latency-resolving primary mark gives `G=η` at all frequency. A downstream TDC does not recreate information already lost before the primary record. The cascade product law applies to independent unresolved stochastic delay stages, not automatically to deterministic TIA transfer functions.

## Rev10 worked published-IRF result

Spinelli et al. 1998, DOI `10.1109/3.668769`:

- FWHM: MCP `25 ps`, DJ-SPAD `35 ps` -> FWHM ranks MCP faster;
- Gaussian-from-FWHM `B_FI`: MCP `13.29 GHz`, DJ-SPAD `9.49 GHz`;
- approximate figure-digitized full-shape `B_FI`: MCP `5.977 GHz`, DJ-SPAD `9.160 GHz`;
- ranking reverses: `B_FI(DJ)/B_FI(MCP)=1.533`.

This remains approximate published-figure digitization, not raw-event reanalysis.

## Rev8 thermodynamic repair — mandatory

Appendix A must keep `acp >= bqs`, ensuring `f_R-r_R=R(acp-bqs)/(RD+E)>=0` for every `R>0`.

Stationary one-way activity is total directed stationary jump traffic. Aggregate stationary activity/EPR/throughput alone do not set an absolute microscopic time scale.

## Novelty posture

Do not claim:

- first information-theoretic detector timing analysis;
- first IRF-information result;
- first generic FI transfer function;
- novelty of the scalar ENBW integral `∫|H|²df`;
- novelty of the first-order ENBW ratio `π/2`;
- generic Blackwell dominance;
- arbitrary fixed-FWHM no-go;
- universal all-detector speed limit.

Defensible contribution: a temporal-information resource theory for autonomous marked photodetection event channels in which the exact marked-delay spectrum is the complete local weak-waveform Fisher multiplier; pointwise ordering completely characterizes local weak-waveform Fisher dominance; collision and hazard resources give exact/inverse bandwidth laws; and the framework is directly computable from timing laws, histograms, and a worked published-IRF example that reverses a conventional FWHM ranking.

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
