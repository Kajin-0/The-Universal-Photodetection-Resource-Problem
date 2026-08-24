# Practical temporal-information benchmarks

**Branch:** `agent/practical-temporal-information-benchmarks`

## Purpose

Develop a fourth, deliberately grounded paper that translates the existing temporal-information resource program into standard detector physics and explicit falsification tests.

This program is **not** another abstraction layer and does not alter the frozen theorem/proof stacks of the three existing papers.

Working title:

> **Operational benchmarks for temporal information in photodetection**

Alternative retained:

> **Falsifiable temporal-information bounds for photodetection: from noise-equivalent power to spectral survival and sideband synthesis**

## Current practical thesis

The work now has four linked detector-language results:

1. linear Gaussian analog detection: `1/NEP(f)^2` is the frequency weighting of the weak-waveform Fisher metric;
2. ideal event detection: timestamp Fisher information reproduces the same shot-noise limit, with independent timing jitter entering through `|Phi_J|^2`;
3. memoryful dead-time detection: conventional saturation curves and low-order recovery statistics can fail to determine temporal-information transfer;
4. optical sidebands: a pre-seeded spectral bin realizes the finite-radius survival regime, while an empty sideband realizes the rank-boundary synthesis regime, with an exact continuous crossover of the Fisher ceiling.

The next step is to add the standard Hamiltonian/controller layer needed to interpret the companion unitary-coupling theorem without confusing it with RF power or thermodynamic work.

## WP01 — linear Gaussian Fisher/NEP bridge

For peak optical-power quadratures, linear responsivity `R(f)`, and one-sided output-noise PSD `S_n(f)`,

`F_xx/T=F_yy/T=|R(f)|^2/S_n(f)=1/NEP(f)^2`,

`Tr F/T=2/NEP(f)^2`.

For arbitrary weak waveform coordinates,

`F_ij=4 Re integral_0^infinity q_i*(f)q_j(f)/NEP(f)^2 df`.

Thus responsivity bandwidth and task-specific information bandwidth need not coincide when the noise spectrum is frequency dependent.

## WP02 — Poisson timestamps and independent jitter

For fractional sinusoidal modulation of an ideal Poisson event stream,

`Tr F/T=lambda_0`.

For optical-power coordinates this exactly matches the WP01 ideal shot-noise result `2/NEP_shot^2`.

Independent timestamp jitter gives

`Tr F/T=lambda_0|Phi_J(Omega)|^2`.

For Gaussian jitter,

`f_F,3dB=sqrt(ln2)/(2 pi sigma_t)`.

## WP03 — dead time/recovery information benchmarks

For deterministic paralyzable recovery at `lambda tau=1`,

`G(0)=0`

but `G(omega)>0` for every nonzero frequency. At `f=1/(2tau)`,

`G>=0.51697536`,

with exact model value about `0.52814`; high-frequency `G->1/e`.

For arbitrary finite-mean iid recovery with mean `m`, every law has the same conventional count curve

`r(lambda)=lambda exp(-lambda m)`,

but at `lambda m=1`

`G_DC=0 iff recovery is deterministic`.

An exact same-mean/same-variance example shows two detectors with identical mean, variance/CV, and complete saturation curve but very different timestamp pair correlations and accessible Fisher information.

## WP04 — optical sideband survival-to-synthesis crossover

### Exact seeded two-bin model

Use carrier `|c>` and sideband `|s>` with baseline

`rho_p=(1-p)|c><c|+p|s><s|`, `0<=p<1/2`,

and calibrated lossless frequency-bin mixing coefficient `kappa`.

The exact sideband population is

`P_s(p;r)=p+(1-2p)sin^2(kappa r)`, `r=sqrt(x^2+y^2)`.

For `p>0`, the exact affine tangent radius is

**`R_lin^2=p(1-p)/[kappa^2(1-2p)^2]`.**

The finite-radius survival theorem becomes the directly measurable inequality

**`(R_lin^2/4) Tr F <= p`.**

At `p=0`, the sideband is baseline empty and

`Delta P_s(0)=4kappa^2`,

so the rank-boundary theorem becomes

**`Tr F <= Delta P_s(0)=4kappa^2`.**

The crossover is exact:

**`lim_(p->0+) 4p/R_lin^2 = Delta P_s(0)=4kappa^2`.**

A fixed four-outcome frequency-bin POVM attains `Tr F=4kappa^2` at the empty-sideband boundary.

### Ordinary weak phase modulation

For a single-frequency photon with ideal weak phase modulation `exp{i[x cos(Omega t)+y sin(Omega t)]}`,

`P_+=(x^2+y^2)/4+O(r^4)`,

`P_-=(x^2+y^2)/4+O(r^4)`,

hence

`Delta P_+(0)=Delta P_-(0)=1`.

A fixed three-mode interferometric measurement attains

`F_xx=F_yy=2`, `Tr F=4`,

so the bilateral boundary law is saturated:

**`Tr F=[sqrt(Delta P_+)+sqrt(Delta P_-)]^2=4`.**

A direct spectrum measurement supplies the curvature resource; a phase-sensitive frequency-bin interferometer or coherent equivalent is required to extract both first-order quadrature Fisher components.

### Scope lock

An externally driven EOM is used here only to test the state-family boundary-curvature law. It is **not** automatically an autonomous clock-signal model, and its electrical RF power is not identified with the flagship synthesis action.

The verified autonomous normalization is retained for WP05:

`A_S^(2)=(hbar nu/4)(Delta T_S,+ + Delta T_S,-)`,

`A_C^(2)=(hbar nu/4)(Delta T_C,+ + Delta T_C,-)`,

and in the clean companion implementation problem

`A_ex^(2)=hbar nu V_min`.

## Authoritative notes

- `notes/WP01_LINEAR_GAUSSIAN_FISHER_NEP_BRIDGE.md`
- `notes/WP02_POISSON_TIMESTAMPS_AND_JITTER.md`
- `notes/WP03_DEAD_TIME_RECOVERY_INFORMATION_BENCHMARKS.md`
- `notes/WP04_OPTICAL_SIDEBAND_SURVIVAL_SYNTHESIS_CROSSOVER.md`

## Publication criterion

Paper 4 now has two potentially publication-level practical cores rather than only a tutorial bridge:

1. conventional dead-time/saturation characterization can provably fail to determine temporal-information transfer;
2. the survival-to-synthesis transition has an exact, measurable optical-sideband realization with a continuous crossover and ideal saturation examples.

The program still requires WP05–WP07 before manuscript drafting.

## Next work

1. **WP05:** explicit controller/clock + textbook resonant-exchange Hamiltonian interpretation of `V_min=(1/2)Tr C` and `A_ex=hbar nu V_min`.
2. **WP06:** integrated falsification matrix and minimum practical theorem stack.
3. **WP07:** dedicated prior-art/significance gate; do not draft a paper before this gate.

## Claim discipline

No novelty claim for conventional NEP, generic Fisher sensing, Poisson FI, timing-jitter transfer, classical paralyzable count laws, renewal spectra, electro-optic sideband generation, SU(2) mode mixing, or standard frequency-bin interferometry. No experimental result may be implied unless actual data are analyzed.

## Documentation rule

Every material derivation, failed derivation, convention correction, prior-art collision, model choice, falsification criterion, or publication-scope decision must be recorded in `notes/` and reflected in `AGENTS.md` and the repository landing files when it changes the frontier.
