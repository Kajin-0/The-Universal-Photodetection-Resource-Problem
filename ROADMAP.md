# Research Roadmap — Rev11 Submission Freeze

**Updated:** 2026-08-21

## Guiding principle

The autonomous marked-event first paper has passed:

- theorem construction;
- hostile review and model-class repair;
- weak-waveform significance upgrade;
- proof hardening;
- Rev8 thermodynamic Appendix repair;
- Rev9 translational grounding and empirical citation anchors;
- Rev10 worked published-IRF demonstration;
- Rev11 ENBW positioning correction and practical histogram uncertainty note;
- full LaTeX/BibTeX/cross-reference validation;
- visual inspection of all newly affected pages.

**Do not perform another broad first-paper revision unless a new concrete defect or specific referee request is identified.**

Primary target: **Physical Review Applied — Regular Article**.

---

# Closed scientific gates

## G0 — Exact autonomous marked-event transfer
**PASSED**

`G(ω)=∫|H_m(ω)|² κ(dm)`.

## G1 — Complete local weak-waveform Fisher operator
**PASSED**

`[F_out]_{ab}=Φ0/(2π)∫G(ω)S_a*(ω)S_b(ω)dω`.

## G2 — Universal local Fisher detector ordering
**PASSED**

Pointwise `G_A>=G_B` iff detector A Fisher-dominates B for every admitted finite weak-waveform task.

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

`B_FI^(Δt)=[1/(2Δt)]Σp_i²` with unbiased finite-count pair-collision estimator.

## T3 — Physical support clarification
**PASSED**

Finite support gives `B_FI>=1/(2T)`, not an upper speed limit.

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

Spinelli et al. 1998, DOI `10.1109/3.668769`:

- DJ-SPAD FWHM 35 ps, `B_FI≈9.160 GHz`;
- MCP FWHM 25 ps, `B_FI≈5.977 GHz`;
- FWHM ranks MCP first, while full-shape `B_FI` ranks DJ-SPAD first.

## A2 — Reproducibility and scope
**PASSED**

Digitized points and a dependency-free analysis script are included and hash-pinned. The calculation is explicitly approximate graphical digitization, not raw-event precision metrology.

## A3 — Data Availability
**PASSED**

The submission copy truthfully discloses the published-figure analysis and supplied digitization/script.

---

# Rev11 positioning gate

## P1 — Conventional ENBW identity
**PASSED**

For a single unresolved mark,

`B_FI = ∫_0^∞|H(2πf)|²df = B_ENBW`

because `H(0)=1`. Rev11 now says this explicitly and cites Motchenbacher & Connelly (1993).

## P2 — Novelty narrowing
**PASSED**

The paper no longer leaves any implication that the scalar `∫|H|²df` integral or the first-order `π/2` relation is novel. The contribution is explicitly located in the stochastic registration-delay/Fisher interpretation, retained-mark generalization, collision identity, hazard bounds, detector ordering, and inverse resource costs.

## P3 — Histogram uncertainty prescription
**PASSED**

A multinomial plug-in bootstrap is given for finite-count uncertainty of the binned pair-collision estimator. Its scope excludes systematic instrument jitter, background subtraction, digitization, and deconvolution error.

---

# Mechanical validation

Canonical Rev11:

- 33 pages;
- PDF SHA-256 `9eedbf562ed5fa70b78a8c1c63627e1c578f149074f7f25f3fd3988c8668ecef`.

PRApplied Rev11:

- 33 pages;
- PDF SHA-256 `d9e4a3330543106a272d4aa7b26cf6187bbd2f6ef170db4a8927b06edb824db7`;
- package ZIP SHA-256 `b9f1abff76bbcc7a97ca8b2c3038f1e44e5adbb68f230cdb7d13c02431b6183e`.

No undefined citations/references. Only inherited ~2.45667 pt Appendix overfull warning remains. Affected canonical and PRApplied pages were visually inspected.

Steady-state CI is read-only and regenerates/hash-checks Rev8 through Rev11, reproduces the Spinelli example, compiles Rev11, and uploads the artifact.

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

Rev11 should now be treated as scientifically frozen by default.
