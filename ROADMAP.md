# Research Roadmap

**Updated:** 2026-08-23

**Active branch:** `agent/practical-temporal-information-benchmarks`

## Mature publication program — frozen

The three developed temporal-information papers remain independent and should not be concatenated:

1. PRX Quantum flagship — survival/synthesis conceptual law;
2. broad random-time/timestamp spectral-information paper;
3. PRA exact unitary-coupling completion.

## Active Paper 4 — practical/falsifiability bridge

Working title:

> **Operational benchmarks for temporal information in photodetection**

Goal: translate temporal Fisher/resource results into standard detector measurements and explicit falsification conditions.

## Completed work

### WP01 — linear Gaussian Fisher/NEP bridge

`F_xx/T=F_yy/T=|R(f)|^2/S_n(f)=1/NEP(f)^2`,

`Tr F/T=2/NEP(f)^2`.

For arbitrary weak waveform coordinates,

`F_ij=4 Re integral_0^infinity q_i*(f)q_j(f)/NEP(f)^2 df`.

Response bandwidth and information bandwidth need not coincide.

### WP02 — ideal Poisson timestamps and timing jitter

For fractional sinusoidal modulation,

`Tr F/T=lambda_0`.

The optical-power result exactly matches ideal shot-noise `2/NEP_shot^2`.

Independent timestamp jitter gives

`Tr F/T=lambda_0|Phi_J(Omega)|^2`.

### WP03 — dead time/recovery information benchmarks

For deterministic paralyzable recovery at the count maximum `lambda tau=1`,

`G(0)=0`

while `G(omega)>0` for every nonzero frequency. At `f=1/(2tau)`,

`G>=0.51697536`,

exact model value about `0.52814`; high-frequency `G->1/e`.

For arbitrary iid finite-mean recovery `T`, every law with mean `m` has the same conventional curve

`r(lambda)=lambda exp(-lambda m)`.

At `lambda m=1`,

**`G_DC=0 iff recovery is deterministic`.**

A bounded interval statistic `exp(-sD)` gives a direct rate-dither witness without fitting the full timestamp likelihood.

The exact same-mean/same-variance dimensional counterexample at `m=10 ns` has identical mean, variance `25 ns^2`, CV `0.5`, and full saturation curve but pair correlations `0.7274957` versus `0.3188718` at `7.5 ns`. A one-bit interval statistic has zero FI for one recovery law and positive FI for the other.

This supplies the first clearly nontrivial practical result: standard saturation and low-order recovery summaries can provably fail to determine temporal-information transfer.

## Next work packages

### WP04 — optical sideband survival-to-synthesis crossover

Use standard phase/amplitude modulation and measurable carrier/sideband populations. Construct a one-parameter family that moves from pre-seeded sideband support to a baseline-empty sideband while preserving a finite temporal-information tangent. Identify the exact observable corresponding to the flagship's second-order synthesis action and state a laboratory-level falsification inequality.

### WP05 — standard Hamiltonian implementation bridge

Translate `V_min=(1/2)Tr C` into at least one textbook resonant-exchange model such as beam-splitter/frequency-conversion coupling, preserving all theorem limitations.

### WP06 — integrated falsification matrix

For every headline result specify measured inputs, predicted equality/inequality, nuisance assumptions, statistical test, and contradiction criterion.

### WP07 — prior-art/significance gate

Determine whether Paper 4 is genuinely publishable rather than merely pedagogical. No manuscript drafting before this gate.

## Candidate paper thesis after WP03

> Conventional detector figures of merit can fail to determine temporal-information transfer. Frequency-resolved response/noise and full timestamp structure supply a common falsifiable benchmark, while the survival/synthesis theory predicts whether that information is supported by pre-existing spectral occupation or by dynamically generated boundary population.

## Claim discipline

No novelty claim for standard NEP/detectivity, matched filtering, generic Fisher sensing, Poisson/dead-time count laws, renewal spectra, random-dead-time pair correlations, or timing-jitter transfer functions. No implied experimental validation without data. No prize-level framing.

## Documentation cadence

Update `practical_temporal_information/notes/`, `practical_temporal_information/AGENTS.md`, and all top-level landing files after every material advance.
