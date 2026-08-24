# AGENTS — Practical Temporal-Information Benchmarks

**Active branch:** `agent/practical-temporal-information-benchmarks`

The repository, not chat history, is authoritative.

## Mission

Create a fourth paper that translates the temporal-information resource program into standard detector physics and explicit falsification tests. Every central result should state what is measured, what is predicted, and what observation would contradict it.

Do not modify the frozen scientific theorem/proof layers of the PRXQ flagship, random-time timestamp paper, or PRA unitary-coupling paper unless this program exposes a genuine defect.

## Read first

1. `README.md`
2. `notes/WP01_LINEAR_GAUSSIAN_FISHER_NEP_BRIDGE.md`
3. `notes/WP02_POISSON_TIMESTAMPS_AND_JITTER.md`
4. `notes/WP03_DEAD_TIME_RECOVERY_INFORMATION_BENCHMARKS.md`
5. `notes/WP04_OPTICAL_SIDEBAND_SURVIVAL_SYNTHESIS_CROSSOVER.md`
6. root `docs/CURRENT_RESEARCH_STATE.md`

## Current result stack

### WP01 — analog Gaussian detector

For peak optical-power quadratures and one-sided output PSD,

`F_xx/T=F_yy/T=|R(f)|^2/S_n(f)=1/NEP(f)^2`,

`Tr F/T=2/NEP(f)^2`.

The full weak-waveform Fisher matrix is the `1/NEP(f)^2` noise-weighted matched-filter metric. Response bandwidth and information bandwidth need not coincide.

### WP02 — ideal timestamps and independent jitter

For fractional sinusoidal modulation of an ideal Poisson rate,

`Tr F/T=lambda_0`.

For optical-power coordinates this exactly matches the analog shot-noise result. Independent timing jitter multiplies the two-quadrature spectrum by `|Phi_J(Omega)|^2`.

### WP03 — dead time/recovery

For deterministic paralyzable recovery at `lambda tau=1`, the complete timestamp channel has `G(0)=0` but `G(omega)>0` at every nonzero frequency. At `f=1/(2tau)`, `G>=0.51697536`; high-frequency `G->1/e`.

For arbitrary finite-mean iid recovery, every law with mean `m` shares `r=lambda exp(-lambda m)`, yet at `lambda m=1`, `G_DC=0 iff recovery is deterministic`.

An exact same-mean/same-variance example shows identical mean, variance/CV, and complete saturation curve do not determine pair correlations or accessible timestamp FI.

### WP04 — exact optical survival-to-synthesis crossover

Use carrier/sideband baseline

`rho_p=(1-p)|c><c|+p|s><s|`, `0<=p<1/2`,

with calibrated two-mode mixing coefficient `kappa`.

Exact sideband population:

`P_s=p+(1-2p)sin^2(kappa sqrt(x^2+y^2))`.

For `p>0`,

**`R_lin^2=p(1-p)/[kappa^2(1-2p)^2]`**

and the survival theorem is

**`(R_lin^2/4)Tr F<=p`.**

At `p=0`,

**`Delta P_s(0)=4kappa^2`**

and

**`Tr F<=Delta P_s(0)`.**

The crossover is exact:

**`lim_(p->0+)4p/R_lin^2=Delta P_s(0)=4kappa^2`.**

A fixed four-outcome frequency-bin POVM saturates the empty-sideband one-sided bound.

Ordinary ideal weak phase modulation of a single-frequency photon gives two empty first sidebands with

`Delta P_+=Delta P_-=1`,

and a fixed three-mode interferometric measurement attains

**`Tr F=4=[sqrt(Delta P_+)+sqrt(Delta P_-)]^2`.**

Thus ordinary optical sideband generation is an exact ideal saturation example of the bilateral rank-boundary curvature law.

Important: direct sideband-power measurement estimates curvature but does not recover both phase quadratures. FI must be measured with a phase-sensitive frequency-bin interferometer/coherent equivalent on identically prepared trials.

Also important: an externally driven EOM is not automatically an autonomous clock-signal system. Do not equate its RF power with the flagship synthesis action. The verified autonomous normalization is reserved for WP05.

## Current publication assessment

WP03 and WP04 are the two likely publication-level practical cores:

1. conventional detector saturation/low-order recovery characterization can provably fail to determine temporal-information transfer;
2. the flagship survival/synthesis transition has an exact measurable sideband realization with a continuous crossover and ideal saturation.

WP01/WP02 provide the common analog/timestamp language around those results.

## Immediate work order

1. **WP05:** include a controller/clock explicitly and reduce `V_min=(1/2)Tr C`, `A_ex=hbar nu V_min` to a textbook resonant-exchange Hamiltonian.
2. **WP06:** integrated falsification matrix and minimal practical theorem/result stack.
3. **WP07:** dedicated prior-art/significance gate before manuscript drafting.

Do not create sidequests that do not improve measurement accessibility, falsifiability, or standard-physics interpretation.

## Claim discipline

No prize-level framing. No novelty claim for standard NEP, Fisher sensing, Poisson/dead-time formulas, renewal spectra, electro-optic phase modulation, sideband generation, SU(2) frequency conversion, or standard frequency-bin interferometry. Assign novelty only after WP07.

## Documentation rule

After every material advance, update the corresponding note and this handoff. When the frontier changes, also update root `README.md`, `AGENTS.md`, `ROADMAP.md`, and `docs/CURRENT_RESEARCH_STATE.md`.
