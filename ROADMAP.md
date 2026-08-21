# Research Roadmap — Rev10 Submission Freeze

**Updated:** 2026-08-20

## Guiding principle

The autonomous marked-event first paper has passed:

- theorem construction;
- hostile review and model-class repair;
- weak-waveform significance upgrade;
- proof hardening;
- Rev8 thermodynamic Appendix repair;
- Rev9 translational grounding and empirical citation anchors;
- Rev10 worked published-IRF demonstration;
- full LaTeX/bibliography/cross-reference validation;
- visual inspection of all newly affected pages.

**Do not perform another broad first-paper revision unless a new concrete defect or specific referee request is identified.**

Primary target: **Physical Review Applied — Regular Article**.

---

# Closed scientific gates

## G0 — Exact autonomous marked-event transfer
**PASSED**

`G(ω)=∫|H_m(ω)|^2 κ(dm)`.

## G1 — Complete local weak-waveform Fisher operator
**PASSED**

`[F_out]_{ab}=Φ0/(2π)∫G(ω)S_a*(ω)S_b(ω)dω`.

## G2 — Universal local Fisher detector ordering
**PASSED**

Pointwise `G_A >= G_B` iff detector A Fisher-dominates B for every admitted finite weak-waveform task.

## G3 — Exact band-subspace guarantee
**PASSED**

Worst-case retention over a compact band equals `min G` on that band.

## G4 — Timing-resource hierarchy
**PASSED**

Atomic residue, collision resource `R_2`, hazard resource `H`, equivalent Fisher bandwidth, and inverse cost theorem all closed.

## G5 — Conventional-jitter no-go
**PASSED**

Exact fixed mean + exact variance do not bound finite temporal information bandwidth. No fixed-FWHM theorem is claimed.

## G6 — Clock/control no-go
**PASSED**

A free source-synchronous reference is a separate resource.

## G7 — CTMC microscopic-rate repair
**PASSED**

The finite-state sufficient hazard ceiling is the maximum total first-exit rate from relevant pre-registration states.

## G8 — Thermodynamic bridge and rare-fast counterexample
**PASSED**

Rev8 enforces `acp >= bqs`, fixes the directed activity convention, and preserves the isolated-event/low-overlap bridge.

---

# Rev9 translational gate

## T1 — Canonical timing-law library
**PASSED**

Gaussian, exponential, uniform, Erlang, and Gaussian–exponential closed forms checked.

## T2 — Existing-data estimator
**PASSED**

`B_FI^(Δt)=[1/(2Δt)]Σp_i^2` with unbiased finite-count pair-collision estimator.

## T3 — Physical support clarification
**PASSED**

Finite support gives `B_FI >= 1/(2T)`, not an upper speed limit.

## T4 — Mark resource gradient
**PASSED**

Fine accessible event marks can preserve more FI; perfect primary latency side information gives `G=η`.

## T5 — Preamplifier/readout interpretation
**PASSED**

Stochastic-delay cascade law is distinguished from deterministic invertible TIA filtering.

## T6 — DC normalization
**PASSED**

`G(0)=η` remains correctly normalized.

## T7 — Empirical citation anchors
**PASSED**

Full-text SPAD literature verifies real Gaussian-like cores, exponential/diffusive tails, spatially conditioned latency, threshold dependence, and stochastic avalanche-spreading timing mechanisms.

---

# Rev10 applied-demonstration gate

## A1 — Real published IRF example
**PASSED**

Source: Spinelli et al., IEEE JQE 34, 817–821 (1998), DOI `10.1109/3.668769`.

Reported FWHM:

- DJ-SPAD: 35 ps;
- MCP: 25 ps.

Approximate figure-digitized full-shape Fisher bandwidth:

- DJ-SPAD: `9.160 GHz`;
- MCP: `5.977 GHz`.

Thus FWHM ranks the MCP first, while `B_FI` ranks the DJ-SPAD first. The ranking reversal is the central applied demonstration.

## A2 — Reproducibility
**PASSED**

Digitized points and dependency-free analysis script are included and hash-pinned. CI reproduces the numbers.

## A3 — Scope/caveat
**PASSED**

The manuscript explicitly labels the calculation approximate graphical digitization of a published figure, not raw-event precision metrology.

## A4 — Data Availability
**PASSED**

Rev10 no longer claims that no data were analyzed. It truthfully states that no new experiments were generated and identifies the published figure used, with digitized points/script supplied.

---

# Mechanical validation

Canonical Rev10:

- 32 pages;
- PDF SHA-256 `fe261ba21db5ac04f76e57dd61bc37b105616fe4c3ccabc5bd6b211145055c29`.

PRApplied Rev10:

- 33 pages;
- PDF SHA-256 `5ff01f6c9d50fcf6e7e0fd59be34e65911a9abd7459a6a348df3e2c70f63e467`;
- package ZIP SHA-256 `5ab6c380c3f9efd4b52babb1ec1d6249229abda06dd5483f14771a750b12b42b`.

No undefined citations/references. Only inherited ~2.45667 pt Appendix overfull warning remains. Affected pages visually inspected.

Steady-state CI is read-only and regenerates/hash-checks Rev8, Rev9, and Rev10, reproduces the Spinelli example, compiles Rev10, and uploads the artifact.

---

# Remaining submission work

Only factual/personal items remain:

1. author name/order;
2. affiliation(s);
3. corresponding-author email;
4. ORCID;
5. truthful substantive-AI acknowledgment describing the author's actual direction and verification;
6. applicable funding/conflict/prior-submission disclosures;
7. optional referee suggestions/exclusions after conflict review;
8. one final metadata-stage compile/visual inspection.

---

# Explicitly deferred to later papers

Do not add to the first paper absent a concrete referee demand:

- high-flux/history-dependent detection;
- arbitrary semi-Markov detectors;
- coherent continuous quantum pointers;
- nonclassical-light/QFI extensions;
- general Shannon-capacity theory;
- material-specific detector optimization;
- additional literature worked examples.

Rev10 should now be treated as scientifically frozen by default.
