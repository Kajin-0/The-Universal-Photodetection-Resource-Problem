# AGENTS.md

## Purpose

Durable handoff for **The Universal Photodetection Resource Problem (UPRP)**. The repository, not chat history, is authoritative.

Research is analytical/theoretical only. Numerical work may be used for validation. Do not make experiments, fabrication, procurement, or laboratory campaigns necessary next steps.

Active branch:

`agent/uprp-core-theorem-round10`

## Read first

1. `docs/CURRENT_RESEARCH_STATE.md`
2. `notes/RESEARCH_LOG_ROUND17.md`
3. `submission/PRAPPLIED_PACKAGE_VALIDATION_REV8.md`
4. `notes/REV8_SURGICAL_REVIEW_REPAIRS.md`
5. `manuscript/apply_rev8_referee_surgical.py`
6. `manuscript/REV8_SHA256SUMS.txt`
7. `manuscript/event_resource_theorem_rev7.tex` — frozen Rev8 input / Rev7 predecessor
8. `notes/RESEARCH_LOG_ROUND16.md`
9. `notes/WP36_COMPLETE_WEAK_WAVEFORM_FISHER_OPERATOR.md`
10. `notes/WP36A_BAND_SUBSPACE_FISHER_GUARANTEE.md`
11. `docs/MANUSCRIPT_REV6_REFEREE_REPAIR_AUDIT.md`
12. `notes/WP35_MARK_CONDITIONED_MARKOV_RATE_CORRECTION.md`
13. `notes/WP34_MINIMUM_TIMING_RESOURCE_COST_THEOREM.md`
14. `notes/WP33_EXACT_FIXED_MEAN_VARIANCE_JITTER_NO_GO.md`
15. `notes/WP32_GENERAL_MARKED_POISSON_EVENT_KERNEL_THEOREM.md`
16. `docs/NOVELTY_AUDIT_ROUND5_EVENT_THEOREM_STACK.md`

---

# Current publication state — Rev8

**Rev8 is the current first-paper submission candidate.**

Rev8 is deliberately a reproducible derived source rather than a broad new science round:

- frozen input: `manuscript/event_resource_theorem_rev7.tex`;
- frozen Appendix input: `manuscript/appendix_rare_fast_counterexample_rev7.tex`;
- assertion-based transform: `manuscript/apply_rev8_referee_surgical.py`;
- expected generated hashes: `manuscript/REV8_SHA256SUMS.txt`.

Expected generated-source SHA-256 values:

- `event_resource_theorem_rev8.tex`: `07068067744c8cff464931739505e49850c97d68a9c5b9fa63324c6251711a09`
- `appendix_rare_fast_counterexample_rev8.tex`: `f9afbdf7e0fd6cc1b57a3a4e00197148e907fc9ed7691a7f9dd42106e16ba665`

Independent local manuscript verification:

- Rev8 PDF: 25 pages, 364825 bytes;
- PDF SHA-256: `bb7dba5a12f5b74181968060b0a6776d7847fad69dfb00090c76425d35974f86`;
- full bibliography/cross-reference compile passed;
- affected pages visually inspected;
- only inherited material warning: approximately `2.45667 pt` overfull line involving `timing-concentration`.

PRApplied submission-copy verification:

- 25 pages, 365072 bytes;
- PDF SHA-256: `60da4f9a3919ffdf64d450b5397755a75109d4fc2a0a374a8132a93931092c37`;
- package ZIP SHA-256: `9ed6b408a9b27da8c6bc6cbc7f4aea869ec4ebb4e394dc286fbeb6a0c5ad96ca`.

Temporary PR `#15` was closed unmerged. Temporary validation branches were neutralized to the clean publication head.

Steady-state `.github/workflows/manuscript-check.yml` is read-only. It generates Rev8, checks the exact hashes, compiles it, and uploads the artifact. It does not self-commit or mutate source.

---

# Why Rev8 exists

A hostile Rev7 re-review found no blocking error in the principal theorem stack. It requested exactly three surgical repairs.

## 1. Rare-fast Appendix orientation

The main thermodynamic section assumes `f >= r`. Rev7 allowed arbitrary positive rare-fast parameters. Rev8 imposes

`acp >= bqs`.

Using the exact stationary distribution,

`f_R-r_R = R(acp-bqs)/(RD+E) >= 0`

for every `R>0`. Strict `acp>bqs` gives strict forward bias. The rare-fast scaling and counterexample are otherwise unchanged.

## 2. Finite-area timing branch

Rev8 explicitly states that `R_2`, `B_FI`, and the hazard resource belong to the absolutely continuous square-integrable timing branch. Atomic or more singular timing measures are classified first by the Wiener residue theorem and need not possess finite Fisher spectral area.

## 3. Activity convention

Rev8 defines stationary one-way activity as total directed stationary jump traffic,

`A_tot = sum_x pi_x sum_{y != x} W_yx`,

with each directed jump counted once. This removes factor-of-two ambiguity and makes `pi_1 lambda_1 <= A` explicit.

No other theorem or model-class change belongs in Rev8.

---

# First-paper theorem class

The theorem concerns autonomous/time-translation-invariant, independent-event / low-overlap, one-primary-registration photodetection under weak coherent/Poisson direct-detection intensity modulation, retaining the complete accessible primary-event mark.

Do **not** describe it as a universal all-detector speed limit.

Per incident photon,

`K(dm,dτ)=κ(dm) μ_m(dτ)`, with `η=κ(M)<=1`.

For sinusoidal modulation,

`G(ω)=∫ |H_m(ω)|^2 κ(dm)`.

For arbitrary finite-dimensional weak temporal perturbations, `G(ω)` is the spectral multiplier of the complete local weak-waveform Fisher operator. Pointwise `G_A >= G_B` is necessary and sufficient for local Fisher dominance over every admitted weak temporal task.

At exact DC the input FI rate is `Phi_0`, not `Phi_0/2`, while normalized transfer remains `G(0)=η`.

---

# Resource stack that remains valid

## Atomic timing residue

Wiener theory gives the exact asymptotic flat-band residue from atomic delay mass. This is an average theorem; do not claim generic pointwise Fourier decay for singular continuous measures.

## Finite-area L2 branch

For square-integrable conditional delay densities,

`R_2 = 2 ∫κ(dm)∫ f_m(t)^2 dt`

and

`∫ G(ω)dω = π R_2`.

For `η>0`,

`B_FI = R_2/(4η)`.

`B_FI` is an equivalent rectangular Fisher-information area bandwidth, not an amplitude or `-3 dB` bandwidth.

## Capture-weighted hazard

If `h_m(t)<=Λ(m)`,

`H = ∫Λ(m)κ(dm)`, and `R_2 <= H`.

A common ceiling gives `B_FI <= Λ/4`; a single exponential saturates it.

## Inverse resource cost

For ordinary-frequency half-band `B` and required absolute retention `q`,

`q<=η`, `R_2>=4Bq`, `H>=4Bq`.

The same coefficient is necessary for guaranteeing `G(ω)>=q` throughout the whole band.

## Conventional-jitter no-go

Exact mean delay plus exact variance/RMS jitter do not determine finite information bandwidth. No fixed-FWHM counterexample is claimed.

## Finite-state CTMC completion

The successful-registration edge rate alone is insufficient with competing exits. The sufficient local ceiling is based on total pre-registration exit rate `q_max`.

## Thermodynamic bridge

Use **bidirectionally connected**, not `reversible`, for the nonequilibrium CTMC network. Apply stationary thermodynamic bounds to the event theorem only through the explicit isolated-event / low-overlap reduction. If capture/recovery is history dependent, the independent-event thermodynamic information bound is not claimed.

The absolute microscopic reverse optical rate remains an independent temporal resource; aggregate stationary thermodynamic budgets alone do not determine the local timing scale.

---

# Novelty posture

Do not claim:

- first information-theoretic detector timing analysis;
- first IRF-information result;
- first sensitivity-bandwidth tradeoff;
- generic finite-frequency response/noise novelty;
- generic Fisher-information transfer-function novelty;
- Blackwell ordering;
- arbitrary fixed-FWHM no-go;
- universal all-detector speed limit.

Defensible contribution:

> A temporal-information resource theory for autonomous marked photodetection event channels in which the exact marked-delay spectrum is the complete local weak-waveform Fisher multiplier; pointwise spectral ordering is necessary and sufficient for universal local weak-waveform Fisher dominance; atomic timing, collision concentration, and capture-weighted hazard provide a branched resource hierarchy; exact Fisher-equivalent bandwidth and inverse band-resource costs make that hierarchy operational; and explicit no-go/repair results show why low-order jitter metrics, free synchronous control, and aggregate stationary thermodynamics are incomplete resources.

Novelty is strongest in the combined theorem stack.

---

# Immediate next action

**Do not continue foundational expansion of the first paper unless a new concrete defect is found.**

The remaining submission blockers are factual/administrative:

- author name/order;
- affiliation;
- corresponding-author email;
- ORCID;
- truthful substantive-AI disclosure describing how the human author verified AI-assisted derivations, citations, and manuscript claims;
- applicable funding, conflict, and prior-submission declarations.

Physical Review Applied remains the primary target; PR Research is the principal APS fallback.

Potential QFI/capacity/high-flux-memory/general detector extensions belong to a second-paper program.
