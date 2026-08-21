# Research Roadmap — Rev8 Submission Freeze

**Updated:** 2026-08-20

## Guiding principle

The autonomous marked-event first paper has passed theorem construction, hostile review, significance upgrade, proof hardening, and the final Rev8 surgical referee-repair gate.

**Do not perform another broad first-paper theory revision unless a new concrete defect is identified.**

Primary target: **Physical Review Applied — Regular Article**.

---

# Publication gates

## Core marked-event theorem stack
**PASSED**

The exact marked delay spectrum

`G(omega)=integral |H_m(omega)|^2 kappa(dm)`

is the source-normalized sinusoidal transfer and the spectral multiplier of the complete local weak-waveform Fisher operator in the declared autonomous independent-event detector class.

## Universal local Fisher ordering
**PASSED**

Pointwise `G_A>=G_B` is necessary and sufficient for detector A to Fisher-dominate B for every admissible finite weak temporal task in the model.

## Exact band-subspace guarantee
**PASSED**

Worst-case retention over a compact band equals the minimum of `G` on that band. Uniform retention `q` is therefore equivalent to `G(omega)>=q` throughout the band.

## Timing-resource hierarchy
**PASSED, REV8 CLARIFIED**

General timing measures are first classified through the Wiener atomic-residue theorem.

On the absolutely continuous square-integrable finite-area branch:

- Parseval gives `integral G d omega = pi R_2`;
- `B_FI = R_2/(4 eta)`;
- capture-weighted hazard gives `R_2 <= H`;
- inverse band resource cost gives `R_2 >= 4Bq`, `H >= 4Bq`.

Rev8 explicitly records this branch structure so atomic/singular timing measures are not visually or verbally implied to possess all finite-area resources.

## Fixed-moment timing no-go
**PASSED**

Exact mean and variance/RMS jitter do not determine finite temporal information bandwidth. No fixed-FWHM counterexample is claimed.

## Synchronous-clock no-go
**PASSED**

A free source-synchronous temporal reference can retain source phase information despite arbitrarily slow final registration. Autonomy is therefore a genuine resource assumption.

## Finite-state CTMC hazard completion
**PASSED**

The successful-registration edge rate alone is insufficient with competing exits; the relevant sufficient local ceiling uses total pre-registration exit rates.

## Thermodynamic isolated-event bridge
**PASSED**

Stationary thermodynamic quantities constrain microscopic rates only before an explicit isolated-event/low-overlap reduction is used to construct the per-photon kernel.

Rev8 defines stationary one-way activity as total directed stationary jump traffic, eliminating the factor-of-two convention ambiguity.

## Rare-fast thermodynamic counterexample
**PASSED — REV8 REPAIRED**

Rev8 imposes `acp>=bqs`, yielding exactly

`f_R-r_R = R(acp-bqs)/(RD+E) >= 0`

for every `R>0`. The counterexample therefore lies inside the main section's assumed `f>=r` sector. Its rare-fast scaling remains unchanged.

---

# Mechanical / hostile-review gates

- Rev6 hostile-referee model-class repairs — **PASSED**
- Rev7 complete weak-waveform significance upgrade — **PASSED**
- Rev7 hostile re-review of principal derivations — **PASSED**
- Rev8 three surgical repairs — **PASSED**
- Rev8 full LaTeX + bibliography/cross-reference build — **PASSED**
- Rev8 affected-page visual inspection — **PASSED**
- Rev8 PRApplied submission-copy build — **PASSED**
- Rev8 PRApplied affected-page/Data Availability visual inspection — **PASSED**
- steady-state read-only hash-checked CI configuration — **PASSED**

See `notes/RESEARCH_LOG_ROUND17.md` and `submission/PRAPPLIED_PACKAGE_VALIDATION_REV8.md`.

---

# Frozen first-paper branches

Do not reopen by default:

- HgCdTe/Kane material-specific WP17–24;
- coherent quantum pointers;
- continuous analog detectors;
- non-Poisson/nonclassical sources;
- high-flux/history-dependent capture/recovery;
- generic QFI/channel-capacity extensions.

Those are second-paper programs unless a specific first-paper referee defect requires otherwise.

---

# Current gate — administrative submission finalization

Required factual inputs from the human author:

1. author name and order;
2. affiliation;
3. corresponding-author email;
4. ORCID;
5. truthful substantive-AI disclosure describing how the human author verified AI-assisted reasoning, derivations, literature synthesis, citations, and manuscript claims;
6. applicable funding/conflict/prior-submission declarations.

After those are supplied:

1. insert metadata and finalized acknowledgment into Rev8 submission copy;
2. regenerate and compile once;
3. inspect only the pages affected by metadata/compliance changes plus first/last pages;
4. freeze final portal-upload ZIP;
5. submit to Physical Review Applied.

Fallback venue if needed: **Physical Review Research**; PRA remains secondary.
