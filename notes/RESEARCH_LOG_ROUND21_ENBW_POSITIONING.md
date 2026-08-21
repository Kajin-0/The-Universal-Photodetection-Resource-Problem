# Research Log Round 21 — ENBW Positioning Correction

**Date:** 2026-08-21

## Trigger

A final external review identified one important literature/positioning issue: in the single-unresolved-mark case, the manuscript's Fisher-equivalent bandwidth is mathematically the conventional one-sided equivalent noise bandwidth (ENBW) of the normalized timing transfer function. The manuscript had not stated this explicitly.

## Resolution

Created Rev11 as a positioning-only revision from Rev10. No theorem, proof, resource inequality, or worked Spinelli example was altered.

For one unresolved mark,

`G(ω)=η|H(ω)|²`, `H(0)=1`,

so

`B_FI = ∫_0^∞ |H(2πf)|² df = B_ENBW`.

Rev11 now explicitly acknowledges this identity and cites the standard electronics reference:

C. D. Motchenbacher and J. A. Connelly, *Low-Noise Electronic System Design* (Wiley, 1993), ISBN 9780471577423.

The manuscript simultaneously states the non-ENBW contribution precisely: the timing transfer comes from stochastic event-registration delay; retained marks produce `G(ω)=∫|H_m|²κ(dm)` rather than the mark-discarded scalar transfer; the spectral area has the collision-resource identity; and the framework supplies exact weak-waveform Fisher ordering, microscopic hazard bounds, and inverse resource costs.

This also contextualizes the first-order result `B_FI/f_3dB = π/2` as the familiar single-pole ENBW ratio rather than implying novelty for that integral.

## Histogram uncertainty

A short practical uncertainty prescription was added without deriving another theorem. For observed bin probabilities `p_hat`, sample replicate count vectors from `Multinomial(N,p_hat)`, recompute the unbiased pair-collision estimator, and use the empirical replicate distribution for intervals. The manuscript explicitly limits this to finite-count uncertainty of the binned estimator and excludes systematic instrument jitter, background subtraction, digitization, and deconvolution errors.

## Validation

Canonical Rev11:

- 33 pages;
- source SHA-256 `fe966f4ab3fa067bb94d200ed09605a1ed3a2cdef9b4488fd0d18a55e95ccb6e`;
- practical-section SHA-256 `ae596eb3866fb0d4d628cb0b527e281d802badc6262e68d3618366bb49903ce3`;
- PDF SHA-256 `9eedbf562ed5fa70b78a8c1c63627e1c578f149074f7f25f3fd3988c8668ecef`.

PRApplied Rev11:

- 33 pages;
- PDF SHA-256 `d9e4a3330543106a272d4aa7b26cf6187bbd2f6ef170db4a8927b06edb824db7`;
- package ZIP SHA-256 `b9f1abff76bbcc7a97ca8b2c3038f1e44e5adbb68f230cdb7d13c02431b6183e`.

No undefined citations or references remain. The only material overfull warning remains the inherited approximately 2.45667 pt `timing-concentration` line in Appendix A. New ENBW/histogram pages and the PRApplied Data Availability/reference pages were visually inspected.

## Decision

Rev11 is the preferred submission candidate. Do not add more theory, detector architectures, thermodynamic branches, or worked examples by default. Reopen science only for a concrete defect or specific referee request.
