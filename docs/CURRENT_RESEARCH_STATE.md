# Current Research State

**Last synchronized:** 2026-08-23

**Active branch:** `agent/practical-temporal-information-benchmarks`

## Frozen upstream scientific layers

The three mature temporal-information papers remain scientifically frozen in their theorem/proof layers. WP31 is superseded; WP32 remains canonical and WP33 remains PASS under stated assumptions.

## Active frontier — practical/falsifiability Paper 4

Working title:

> **Operational benchmarks for temporal information in photodetection**

Purpose: translate the temporal Fisher/resource program into ordinary detector observables and explicit falsification tests.

Workspace: `practical_temporal_information/`.

## WP01 — linear Gaussian detector

For peak optical-power quadratures and one-sided output PSD,

`F_xx/T=F_yy/T=|R(f)|^2/S_n(f)=1/NEP(f)^2`,

`Tr F/T=2/NEP(f)^2`.

Thus inverse-square NEP is the weak-waveform Fisher weighting in the linear stationary Gaussian regime, and response bandwidth need not equal information bandwidth.

## WP02 — ideal timestamps and timing jitter

For fractional sinusoidal modulation of an ideal Poisson event rate,

`Tr F/T=lambda_0`.

For optical-power coordinates this exactly equals the analog shot-noise result. Independent timestamp jitter gives factor `|Phi_J(Omega)|^2`.

## WP03 — dead time/recovery

For deterministic paralyzable recovery at `lambda tau=1`, the complete timestamp channel has `G(0)=0` but `G(omega)>0` at every nonzero frequency. At `f=1/(2tau)`, `G>=0.51697536`; high-frequency `G->1/e`.

For arbitrary finite-mean iid recovery with mean `m`, every law shares

`r=lambda exp(-lambda m)`,

but at the common maximum

`G_DC=0 iff recovery is deterministic`.

Explicit same-mean/same-variance recovery laws with the same entire saturation curve have different pair correlations and accessible timestamp FI. Therefore standard saturation and low-order recovery summaries do not determine temporal-information transfer.

## WP04 — optical sideband survival-to-synthesis crossover

### Seeded two-bin exact model

Baseline:

`rho_p=(1-p)|c><c|+p|s><s|`, `0<=p<1/2`.

Lossless local frequency-bin mixing coefficient: `kappa`.

Exact sideband population:

`P_s=p+(1-2p)sin^2(kappa sqrt(x^2+y^2))`.

For `p>0`,

**`R_lin^2=p(1-p)/[kappa^2(1-2p)^2]`.**

The finite-radius survival theorem becomes

**`(R_lin^2/4)Tr F<=p`.**

At `p=0`, the sideband is a kernel direction and

**`Delta P_s(0)=4kappa^2`,**

so the one-sided boundary theorem gives

**`Tr F<=Delta P_s(0)`.**

The transition is exact and continuous at the level of the Fisher ceiling:

**`lim_(p->0+)4p/R_lin^2=Delta P_s(0)=4kappa^2`.**

A fixed four-outcome frequency-bin POVM saturates the empty-sideband boundary value.

### Ordinary weak phase modulation

For ideal single-carrier phase modulation, the first upper/lower sidebands obey

`Delta P_+(0)=Delta P_-(0)=1`.

A fixed three-mode phase-sensitive analyzer attains

`F_xx=F_yy=2`,

and therefore

**`Tr F=4=[sqrt(Delta P_+)+sqrt(Delta P_-)]^2`.**

Thus standard optical sideband generation supplies an exact ideal saturation example of the bilateral rank-boundary curvature law.

Direct sideband spectroscopy determines the population-curvature resource; both temporal quadratures require a phase-sensitive interferometric/coherent Fisher measurement.

An externally driven EOM is not automatically an autonomous clock-signal system. Its consumed RF power is not identified with the synthesis action.

The exact flagship normalization, checked against the final verified R4 source artifact, is

`A_S^(2)=(hbar nu/4)(Delta T_S,+ + Delta T_S,-)`,

`A_C^(2)=(hbar nu/4)(Delta T_C,+ + Delta T_C,-)`,

and in the clean companion unitary-dilation specialization

`A_ex^(2)=hbar nu V_min`.

WP05 will add an explicit controller/clock before applying this dynamical interpretation.

## Significance assessment after WP04

Paper 4 now has two likely nontrivial practical cores:

1. detector memory: standard saturation/low-order recovery characterization can provably fail to determine temporal-information transfer;
2. spectral support: the survival/synthesis transition has an exact measurable optical-sideband realization with a continuous crossover and ideal saturation.

WP01–WP02 provide a common analog/timestamp benchmark language around those results.

## Immediate next work

1. WP05 — textbook autonomous resonant-exchange/controller interpretation of the unitary-coupling theorem.
2. WP06 — integrated falsification matrix and minimal practical result stack.
3. WP07 — dedicated prior-art/significance gate before manuscript drafting.

## Claim discipline

No novelty claim for standard NEP, generic Fisher sensing, Poisson/dead-time formulas, renewal spectra, electro-optic sideband generation, SU(2) mode mixing, or standard frequency-bin interferometry. No prize-level framing. No experimental validation may be implied without data.

Every material Paper-4 advance must update the practical notes and all top-level landing files so a future agent can continue without chat history.
