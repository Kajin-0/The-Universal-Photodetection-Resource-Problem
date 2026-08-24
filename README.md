# The Universal Photodetection Resource Problem

**Status synchronized:** 2026-08-23

The repository is authoritative; chat history is not.

## Mature papers — preserve separately

1. **PRX Quantum flagship:** *Two spectral-resource regimes for autonomous temporal information* — R3 frozen theorem/proof baseline, R4 current journal-facing bridge layer.
2. **Broad random-time/timestamp paper:** independent spectral-information/memory track.
3. **PRA dynamical completion:** *Exact minimum unitary coupling cost of prescribed rank-changing quantum-state curvature*.

A fourth practical/falsifiability program is active on branch `agent/practical-temporal-information-benchmarks`.

Working title:

> **Operational benchmarks for temporal information in photodetection**

Workspace: `practical_temporal_information/`.

## Paper 4 result stack

### WP01 — analog Gaussian bridge

For peak optical-power quadratures and one-sided output noise PSD,

`F_xx/T=F_yy/T=|R(f)|^2/S_n(f)=1/NEP(f)^2`,

`Tr F/T=2/NEP(f)^2`.

The full weak-waveform Fisher metric is weighted by `1/NEP(f)^2`, so responsivity bandwidth and information bandwidth need not coincide.

### WP02 — ideal timestamps and jitter

For fractional modulation of an ideal Poisson event stream,

`Tr F/T=lambda_0`.

For optical-power coordinates this exactly matches ideal shot-noise NEP. Independent timing jitter multiplies the spectrum by `|Phi_J(Omega)|^2`.

### WP03 — dead time/recovery

For deterministic paralyzable recovery at `lambda tau=1`, the complete timestamp channel has `G(0)=0` but retains nonzero information at every nonzero frequency. At `f=1/(2tau)`, `G>=0.51697536`; high-frequency `G->1/e`.

For arbitrary finite-mean iid recovery with mean `m`, every law shares

`r(lambda)=lambda exp(-lambda m)`,

but at the common maximum

**`G_DC=0 iff recovery is deterministic`.**

An exact same-mean/same-variance example shows identical mean, variance/CV, maximum count rate, and entire saturation curve can coexist with sharply different timestamp correlations and accessible Fisher information.

### WP04 — optical survival-to-synthesis crossover

Use carrier/sideband baseline

`rho_p=(1-p)|c><c|+p|s><s|`, `0<=p<1/2`,

with calibrated lossless mixing coefficient `kappa`.

The exact sideband population is

`P_s=p+(1-2p)sin^2(kappa sqrt(x^2+y^2))`.

For `p>0`,

**`R_lin^2=p(1-p)/[kappa^2(1-2p)^2]`**

and finite-radius survival gives

**`(R_lin^2/4)Tr F<=p`.**

At `p=0`, the sideband becomes baseline empty,

**`Delta P_s(0)=4kappa^2`**

and the rank-boundary theorem gives

**`Tr F<=Delta P_s(0)`.**

The crossover is exact:

**`lim_(p->0+)4p/R_lin^2=Delta P_s(0)=4kappa^2`.**

A fixed four-outcome frequency-bin POVM saturates the boundary value.

Ordinary ideal weak phase modulation provides an even more familiar bilateral example. The first upper/lower sidebands satisfy

`Delta P_+=Delta P_-=1`,

and a fixed three-mode phase-sensitive analyzer attains

**`Tr F=4=[sqrt(Delta P_+)+sqrt(Delta P_-)]^2`.**

Thus standard optical sideband generation gives an exact ideal saturation example of the rank-boundary curvature law.

A direct spectrum measurement determines the sideband-curvature resource; a phase-sensitive interferometric/coherent measurement is required for both Fisher quadratures.

An externally driven EOM is **not** automatically the autonomous clock-signal model, and its RF power is not identified with the synthesis action. WP05 will include the controller explicitly.

## Current significance assessment

Paper 4 now has two likely nontrivial practical cores:

1. conventional saturation/low-order recovery characterization can provably fail to determine temporal-information transfer;
2. the survival-to-synthesis transition has an exact measurable optical-sideband realization with a continuous limiting law and ideal saturation examples.

WP01/WP02 provide a common analog/timestamp measurement language around those results.

No manuscript drafting yet. WP05–WP07 remain required.

## Immediate work order

1. WP05 — textbook autonomous resonant-exchange/controller interpretation of `V_min=(1/2)Tr C` and `A_ex=hbar nu V_min`.
2. WP06 — integrated falsification matrix and minimal practical result stack.
3. WP07 — dedicated prior-art/significance gate before manuscript drafting.
4. Update practical notes and all landing files after every material advance.

## Claim discipline

Priority remains **unverified, not certified**. No prize-level framing. No novelty claim for standard NEP/detectivity, matched filtering, generic Fisher sensing, Poisson/dead-time formulas, renewal spectra, electro-optic sideband generation, SU(2) mode mixing, or standard frequency-bin interferometry.

## Frozen publication packages

PRXQ R4 verification: run `32674844366` PASS; artifact `9502376602`; 20-page main / 25-page supplement; render QA PASS.

PRA R1 verification: run `32673160217` PASS; artifact `9501942180`; 11-page main / 10-page supplement; render QA PASS.
