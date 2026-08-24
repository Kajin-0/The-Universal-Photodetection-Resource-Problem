# The Universal Photodetection Resource Problem

**Status synchronized:** 2026-08-23

The repository is authoritative; chat history is not.

## Current publication architecture

The three mature temporal-information papers remain separate and scientifically frozen in their current theorem/proof layers:

1. **PRX Quantum flagship:** *Two spectral-resource regimes for autonomous temporal information* — R3 frozen theorem/proof baseline, R4 current journal-facing bridge layer.
2. **Broad operational paper:** *Spectral Resource Laws for Temporal Fisher Information* — random-time/spectral-survival and photodetection-facing theory.
3. **PRA dynamical completion:** *Exact minimum unitary coupling cost of prescribed rank-changing quantum-state curvature* — exact prescribed-curvature unitary-coupling theorem.

A fourth, deliberately grounded program is active on this branch:

4. **Practical/falsifiability bridge:** working title *Operational benchmarks for temporal information in photodetection*.
   - translates Fisher/resource statements into responsivity, noise PSD, NEP, bandwidth, timestamp, jitter, dead-time, and optical-sideband observables;
   - requires explicit falsification criteria;
   - must remain useful in standard detector language even if a reader does not adopt the full abstract resource framework;
   - does not modify the frozen scientific content of Papers 1–3 unless it exposes a genuine defect.

Paper-4 workspace:

- `practical_temporal_information/README.md`;
- `practical_temporal_information/AGENTS.md`;
- `practical_temporal_information/notes/`.

## Paper 4 current frontier

### WP01 — linear Gaussian Fisher/NEP bridge

For peak optical-power quadratures `x,y`, linear responsivity `R(f)`, and one-sided additive stationary Gaussian output-noise PSD `S_n(f)`,

`F_xx/T = F_yy/T = |R(f)|^2/S_n(f)`

and

`Tr F/T = 2 |R(f)|^2/S_n(f)`.

When conventional frequency-resolved NEP is valid,

`NEP(f)=sqrt(S_n(f))/|R(f)|`,

so

**`F_xx/T = 1/NEP(f)^2`**

and

**`Tr F/T = 2/NEP(f)^2`.**

For arbitrary weak waveform coordinates,

`F_ij = 4 Re integral_0^infinity q_i*(f) q_j(f) / NEP(f)^2 df`.

The practical information response is therefore `|R|^2/S_n=1/NEP^2`, so responsivity 3-dB bandwidth and task-specific Fisher-information bandwidth need not coincide when noise is frequency dependent.

Authoritative note: `practical_temporal_information/notes/WP01_LINEAR_GAUSSIAN_FISHER_NEP_BRIDGE.md`.

### WP02 — ideal Poisson timestamps and timing jitter

For

`lambda(t)=lambda_0[1+x cos(Omega t)+y sin(Omega t)]`

with fractional peak quadratures, the continuously illuminated inhomogeneous-Poisson model gives

**`Tr F/T=lambda_0`**

exactly. For integer-period/long records,

`F_xx/T=F_yy/T=lambda_0/2`, `F_xy/T -> 0`.

For optical-power quadratures with `lambda_0=eta P_0/(hbar omega_opt)`,

`Tr F_P/T=eta/(hbar omega_opt P_0)`.

This exactly equals WP01's `2/NEP_shot^2` result for an ideal shot-noise-limited photodiode using one-sided `S_I=2qI_0`.

If each timestamp is independently displaced by jitter `J` with characteristic function `Phi_J(Omega)`,

**`Tr F_jitter/T=lambda_0 |Phi_J(Omega)|^2`.**

For Gaussian jitter standard deviation `sigma_t`,

`Tr F/T=lambda_0 exp[-Omega^2 sigma_t^2]`

and

`f_F,3dB=sqrt(ln 2)/(2 pi sigma_t) ~= 0.1325/sigma_t`.

Independent unmodulated dark counts give `Tr F/T=lambda_s^2/(lambda_s+lambda_d)` before the jitter factor.

Authoritative note: `practical_temporal_information/notes/WP02_POISSON_TIMESTAMPS_AND_JITTER.md`.

## Why the practical program may be publishable

WP01–WP02 by themselves are mostly a rigorous bridge, not yet sufficient novelty. The stronger target is WP03–WP04: identify detector-memory information invisible in mean count curves and construct a measurable transition between pre-existing spectral survival and baseline-empty sideband synthesis. Paper 4 is justified only if those produce a nontrivial falsifiable result beyond tutorial translation.

## Existing flagship / companion status

PRXQ R4 final verification: run `32674844366` PASS; artifact `9502376602`; SHA-256 `8e32c8248050ffa8be254d86f2f0a5724ef0e3edd1a9e2cf38cbc3a17ca3ed76`; 20-page main / 25-page supplement; render QA PASS.

PRA R1 final verification: run `32673160217` PASS; artifact `9501942180`; SHA-256 `4236d6f514b2f290d302062ab4c7a599c03c817da259f3d9715b787a4d37d640`; 11-page main / 10-page supplement; render QA PASS.

## Scientific and novelty discipline

Priority remains **unverified, not certified**.

Do not use Nobel/prize-level framing in manuscripts, cover letters, abstracts, or scientific repository claims. Do not claim novelty for standard NEP/detectivity, matched filtering, generic Fisher sensing, Poisson-process Fisher information, shot-noise formulas, timing-jitter transfer functions, Bures/Uhlmann/SLD geometry, covariant dilation theory, or standard PSD-cone mathematics.

## Current work order

1. preserve the three mature papers' scientific theorem/proof layers;
2. execute WP03: dead time/recovery/memory benchmarks and connect them to the random-time spectral-resource paper;
3. construct WP04 seeded-to-empty optical-sideband survival/synthesis crossover;
4. translate the PRA implementation cost into a textbook resonant-exchange model;
5. build an integrated falsification matrix;
6. perform a dedicated prior-art/significance gate before drafting Paper 4;
7. update practical-program notes and top-level handoffs after every material advance.

## Manuscript integrity

Every public-facing paper must remain scientifically standalone and free of personal repository identifiers, internal development labels, or dependencies on private research files.
