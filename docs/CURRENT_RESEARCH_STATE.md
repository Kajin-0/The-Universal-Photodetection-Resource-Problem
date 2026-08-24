# Current Research State

**Last synchronized:** 2026-08-23

**Active branch:** `agent/practical-temporal-information-benchmarks`

## Frozen upstream scientific layers

The three mature temporal-information papers remain scientifically frozen in their theorem/proof layers. WP31 is superseded; WP32 remains canonical and WP33 remains PASS under stated assumptions.

## New active frontier — practical/falsifiability Paper 4

Working title:

> **Operational benchmarks for temporal information in photodetection**

Purpose: translate the temporal Fisher/resource program into ordinary detector observables and explicit falsification tests.

Workspace: `practical_temporal_information/`.

## WP01 — linear Gaussian detector

For peak optical-power quadratures and one-sided output noise PSD,

`F_xx/T=F_yy/T=|R(f)|^2/S_n(f)=1/NEP(f)^2`,

`Tr F/T=2/NEP(f)^2`.

For arbitrary weak waveform coordinates,

`F_ij=4 Re integral_0^infinity q_i*(f)q_j(f)/NEP(f)^2 df`.

Thus inverse-square NEP is the local Gaussian input-waveform Fisher weighting, and responsivity bandwidth is not generally identical to information bandwidth.

## WP02 — ideal timestamps and timing jitter

For fractional sinusoidal modulation of an ideal Poisson event rate,

`Tr F/T=lambda_0`.

For optical-power coordinates this exactly equals the analog shot-noise result `2/NEP_shot^2`.

Independent timestamp jitter with characteristic function `Phi_J(Omega)` gives

`Tr F/T=lambda_0|Phi_J(Omega)|^2`.

Gaussian jitter gives `f_F,3dB=sqrt(ln2)/(2 pi sigma_t)`.

## WP03 — dead time/recovery: standard saturation is insufficient

### Deterministic paralyzable recovery

At the classical count maximum `lambda tau=1`, the complete stationary timestamp channel satisfies

`G(0)=0`

but retains information at every nonzero temporal frequency.

At `omega tau=pi` (`f=1/(2tau)`),

`G>=0.51697536`,

with exact model value about `0.52814`; high-frequency `G->1/e`.

For `tau=10 ns`, the benchmark is `lambda=100 MHz`, registered rate `36.79 MHz`, and test frequency `50 MHz`.

### Random iid recovery

Every finite-mean iid recovery law with mean `m` shares

`r(lambda)=lambda exp(-lambda m)`.

At the common count maximum `lambda m=1`,

**`G_DC=0 iff T=m almost surely`.**

Every nondegenerate recovery distribution retains positive timestamp information although the conventional count-rate slope is zero for all distributions.

A practical bounded witness is `Z_s=exp(-sD)`: the local fractional-rate derivative of `E[Z_s]` at the count maximum is zero iff recovery is deterministic and strictly positive for every nondegenerate finite-mean recovery law.

### Exact same-mean/same-variance counterexample

At mean recovery `m=10 ns`:

- Law A: `5 ns` or `15 ns`, each probability `1/2`;
- Law B: `2.5 ns` (`2/9`), `10 ns` (`5/9`), `17.5 ns` (`2/9`).

Both have variance `25 ns^2`, CV `0.5`, identical maximum count rate, and the entire same saturation curve.

Yet at the common maximum and lag `7.5 ns`,

`g_A^(2)=0.7274957`,

`g_B^(2)=0.3188718`.

The one-bit interval statistic `1{D<=4 ns}` has zero FI for A and positive FI for B (`G_Z=0.00443520`).

This proves in a detector-facing form that mean recovery, variance/CV, maximum count rate, and even the complete homogeneous saturation curve do not determine temporal-information transfer.

Authoritative note: `practical_temporal_information/notes/WP03_DEAD_TIME_RECOVERY_INFORMATION_BENCHMARKS.md`.

## Significance assessment after WP03

WP01–WP02 are primarily a rigorous common-language bridge. WP03 supplies the first strong practical result capable of supporting a fourth paper: conventional dead-time/saturation characterization can provably discard information needed to characterize temporal sensing.

The next decisive test is WP04: whether the flagship survival/synthesis distinction can be made equally concrete through ordinary optical sideband physics.

## Immediate next work

1. WP04 — seeded-to-empty optical-sideband survival/synthesis crossover.
2. WP05 — standard resonant-exchange interpretation of the unitary-coupling theorem.
3. WP06 — integrated falsification matrix.
4. WP07 — dedicated prior-art/significance gate before manuscript drafting.

## Claim discipline

No novelty claim for standard NEP, detectivity, matched filtering, generic Fisher sensing, Poisson/dead-time count laws, renewal spectra, random-dead-time pair-correlation formulas, or timing-jitter filtering. No prize-level framing. No experimental validation may be implied without data.

Every material Paper-4 advance must update the practical notes and all top-level landing files so a future agent can continue without chat history.
