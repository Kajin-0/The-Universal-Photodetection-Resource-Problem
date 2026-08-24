# The Universal Photodetection Resource Problem

**Status synchronized:** 2026-08-23

The repository is authoritative; chat history is not.

## Current publication architecture

The three mature temporal-information papers remain separate and scientifically frozen in their current theorem/proof layers:

1. **PRX Quantum flagship:** *Two spectral-resource regimes for autonomous temporal information* — R3 frozen theorem/proof baseline, R4 current journal-facing bridge layer.
2. **Broad operational paper:** *Spectral Resource Laws for Temporal Fisher Information* — random-time/spectral-survival and photodetection-facing theory.
3. **PRA dynamical completion:** *Exact minimum unitary coupling cost of prescribed rank-changing quantum-state curvature* — exact prescribed-curvature unitary-coupling theorem.

A fourth, deliberately grounded program is now active on this branch:

4. **Practical/falsifiability bridge:** working title *Operational benchmarks for temporal information in photodetection*.
   - translates Fisher/resource statements into responsivity, noise PSD, NEP, bandwidth, timestamp, jitter, dead-time, and optical-sideband observables;
   - must contain explicit falsification criteria;
   - must remain useful in standard detector language even if a reader does not adopt the full abstract resource framework;
   - does not modify the frozen scientific content of Papers 1–3 unless it exposes a genuine defect.

Paper-4 workspace:

- `practical_temporal_information/README.md`;
- `practical_temporal_information/AGENTS.md`;
- `practical_temporal_information/notes/`.

The earlier three-paper architecture remains recorded in `manuscript/THREE_PAPER_PUBLICATION_ARCHITECTURE_2026-08-23.md`; Paper 4 is an applications/falsifiability bridge, not an omnibus replacement.

## Paper 4 current frontier — WP01

For the standard weak sinusoidal detector model

`delta P(t)=x cos(2 pi f t)+y sin(2 pi f t)`

with **peak** quadrature amplitudes `x,y`, linear responsivity `R(f)`, and **one-sided** additive stationary Gaussian output-noise PSD `S_n(f)`, WP01 derives

`F_xx/T = F_yy/T = |R(f)|^2/S_n(f)`

and therefore

`Tr F/T = 2 |R(f)|^2/S_n(f)`.

When conventional frequency-resolved NEP is valid,

`NEP(f)=sqrt(S_n(f))/|R(f)|`,

so

**`F_xx/T = 1/NEP(f)^2`**

and

**`Tr F/T = 2/NEP(f)^2`.**

The arbitrary-waveform Gaussian Fisher matrix becomes

`F_ij = 4 Re integral_0^infinity q_i*(f) q_j(f) / NEP(f)^2 df`.

Thus inverse-square frequency-resolved NEP is exactly the matched-filter Fisher weighting in the linear stationary Gaussian regime.

WP01 also shows that conventional responsivity bandwidth need not equal task-specific Fisher-information bandwidth when output noise is frequency dependent. If signal and dominant input noise are filtered by the same invertible transfer function, responsivity may roll off while the ideal matched-filter Fisher information remains unchanged until post-filter/readout noise dominates.

Authoritative derivation:

`practical_temporal_information/notes/WP01_LINEAR_GAUSSIAN_FISHER_NEP_BRIDGE.md`.

No novelty claim is made for NEP, detectivity, Fisher information in optical sensing, or the generic fact that detector noise limits Fisher precision. Dedicated prior-art review is required before any generalized information-equivalent detector metric is claimed as new.

## Existing flagship / companion status

PRXQ R4 final verification: run `32674844366` PASS; artifact `9502376602`; SHA-256 `8e32c8248050ffa8be254d86f2f0a5724ef0e3edd1a9e2cf38cbc3a17ca3ed76`; 20-page main / 25-page supplement; render QA PASS.

PRA R1 final verification: run `32673160217` PASS; artifact `9501942180`; SHA-256 `4236d6f514b2f290d302062ab4c7a599c03c817da259f3d9715b787a4d37d640`; 11-page main / 10-page supplement; render QA PASS.

## Scientific and novelty discipline

Priority remains **unverified, not certified**.

Do not use Nobel/prize-level framing in manuscripts, cover letters, abstracts, or scientific repository claims. Do not claim novelty for generic Bures/Uhlmann/SLD geometry, covariant dilation theory, standard NEP/detectivity definitions, Fisher information as a generic sensing metric, classical nonregular boundary statistics, or standard PSD-cone mathematics.

## Current work order

1. preserve the three mature papers' scientific theorem/proof layers;
2. execute Paper-4 WP02: ideal Poisson timestamps and independent timing jitter;
3. then derive dead-time/recovery/memory benchmarks and connect them to the random-time spectral-resource paper;
4. construct a seeded-to-empty optical-sideband survival/synthesis crossover with measurable falsification conditions;
5. perform a dedicated prior-art/significance gate before drafting Paper 4;
6. update practical-program notes and top-level handoffs after every material advance.

## Manuscript integrity

Every public-facing paper must remain scientifically standalone and free of personal repository identifiers, internal development labels, or dependencies on private research files.
