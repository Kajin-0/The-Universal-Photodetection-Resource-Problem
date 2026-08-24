# The Universal Photodetection Resource Problem

**Status synchronized:** 2026-08-23

The repository is authoritative; chat history is not.

## Current publication architecture

The three mature temporal-information papers remain separate and scientifically frozen in their current theorem/proof layers:

1. **PRX Quantum flagship:** *Two spectral-resource regimes for autonomous temporal information* — R3 frozen theorem/proof baseline, R4 current journal-facing bridge layer.
2. **Broad operational paper:** *Spectral Resource Laws for Temporal Fisher Information* / frozen random-time timestamp-information program.
3. **PRA dynamical completion:** *Exact minimum unitary coupling cost of prescribed rank-changing quantum-state curvature*.

A fourth, deliberately grounded program is active:

4. **Practical/falsifiability bridge:** working title *Operational benchmarks for temporal information in photodetection*.

Paper-4 workspace: `practical_temporal_information/`.

## Paper 4 current frontier

### WP01 — linear Gaussian detector

For peak optical-power quadratures and one-sided output noise PSD,

`F_xx/T=F_yy/T=|R(f)|^2/S_n(f)=1/NEP(f)^2`,

`Tr F/T=2/NEP(f)^2`.

For arbitrary weak waveform coordinates,

`F_ij=4 Re integral_0^infinity q_i*(f)q_j(f)/NEP(f)^2 df`.

Thus response bandwidth and task-specific Fisher-information bandwidth need not coincide when noise is frequency dependent.

### WP02 — ideal event timestamps and timing jitter

For fractional sinusoidal modulation of an ideal Poisson event rate,

`Tr F/T=lambda_0`.

For optical-power coordinates this exactly matches the analog shot-noise result `2/NEP_shot^2`.

Independent timestamp jitter gives

`Tr F/T=lambda_0|Phi_J(Omega)|^2`.

For Gaussian jitter,

`f_F,3dB=sqrt(ln2)/(2 pi sigma_t)`.

### WP03 — dead time/recovery: conventional saturation is not an information-transfer law

For deterministic paralyzable Type-II recovery at `lambda tau=1`, the full stationary timestamp channel is DC-blind,

`G(0)=0`,

but retains information at every nonzero temporal frequency. At `f=1/(2tau)`,

`G>=0.51697536`

and the exact model value is about `0.52814`; at high frequency `G->1/e`.

For `tau=10 ns`, this means a detector at the `100 MHz` incident-rate paralysis maximum is DC-information blind while retaining more than half the source Fisher information for a `50 MHz` modulation.

For arbitrary iid recovery with finite mean `m`, every recovery law shares the identical conventional curve

`r(lambda)=lambda exp(-lambda m)`.

At the common maximum `lambda m=1`,

**`G_DC=0 iff recovery is deterministic`.**

Every nondegenerate recovery law retains positive timestamp information despite the same zero count-rate slope.

A simple bounded interval statistic `Z_s=exp(-sD)` provides an experimentally legible witness: its derivative with respect to a small fractional source-rate dither at the count maximum is zero iff recovery is deterministic and strictly positive for every nondegenerate finite-mean recovery law.

WP03 also gives a dimensional exact counterexample at mean recovery `m=10 ns`. Two recovery laws have the same mean, variance `25 ns^2`, CV `0.5`, and the entire same saturation curve, yet at the common maximum their registered pair correlation at `7.5 ns` is

`0.7274957` versus `0.3188718`.

A one-bit statistic `1{D<=4 ns}` has zero FI for one detector and positive FI for the other.

This is the first clear publication-level practical message: **mean recovery, variance/CV, maximum count rate, and even the full homogeneous saturation curve do not determine temporal-information transfer.**

Authoritative notes:

- `practical_temporal_information/notes/WP01_LINEAR_GAUSSIAN_FISHER_NEP_BRIDGE.md`;
- `practical_temporal_information/notes/WP02_POISSON_TIMESTAMPS_AND_JITTER.md`;
- `practical_temporal_information/notes/WP03_DEAD_TIME_RECOVERY_INFORMATION_BENCHMARKS.md`.

## Why Paper 4 may now be worthwhile

WP01–WP02 build a common analog/timestamp information language. WP03 adds a nontrivial detector-physics result that standard saturation characterization can provably miss. The next test is whether the flagship survival/synthesis distinction can be made equally concrete with ordinary optical sidebands.

## Existing flagship / companion status

PRXQ R4 final verification: run `32674844366` PASS; artifact `9502376602`; 20-page main / 25-page supplement; render QA PASS.

PRA R1 final verification: run `32673160217` PASS; artifact `9501942180`; 11-page main / 10-page supplement; render QA PASS.

## Scientific and novelty discipline

Priority remains **unverified, not certified**. Do not use Nobel/prize-level framing. Do not claim novelty for standard NEP/detectivity, matched filtering, generic Fisher sensing, Poisson-process FI, dead-time count laws, renewal spectra, random-dead-time pair-correlation formulas, or timing-jitter filtering.

## Current work order

1. preserve the three mature papers' scientific theorem/proof layers;
2. execute WP04: seeded-to-empty optical-sideband survival/synthesis crossover;
3. execute WP05: textbook resonant-exchange interpretation of the PRA unitary-coupling theorem;
4. build WP06 integrated falsification matrix;
5. perform WP07 prior-art/significance gate before manuscript drafting;
6. update practical notes and all landing files after every material advance.
