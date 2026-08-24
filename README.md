# The Universal Photodetection Resource Problem

**Status synchronized:** 2026-08-23

The repository is authoritative; chat history is not.

## Mature papers — preserve separately

1. **PRX Quantum flagship:** *Two spectral-resource regimes for autonomous temporal information* — R3 frozen theorem/proof baseline, R4 journal-facing bridge layer.
2. **Broad random-time/timestamp paper:** independent spectral-information/memory track.
3. **PRA dynamical completion:** *Exact minimum unitary coupling cost of prescribed rank-changing quantum-state curvature*.

A fourth practical/falsifiability program is active on branch `agent/practical-temporal-information-benchmarks`.

Working title:

> **Operational benchmarks for temporal information in photodetection**

Workspace: `practical_temporal_information/`.

## Practical result stack

### WP01 — analog Gaussian

`Tr F/T=2|R(f)|^2/S_n(f)=2/NEP(f)^2` under the locked peak-quadrature / one-sided-PSD convention.

### WP02 — ideal timestamps

`Tr F/T=lambda_0` for fractional Poisson modulation; optical-power form exactly matches ideal shot-noise NEP. Independent timing jitter contributes `|Phi_J(Omega)|^2`.

### WP03 — detector memory

Conventional saturation is not an information-transfer law. Deterministic Type-II recovery at `lambda tau=1` is DC-information blind while every nonzero temporal mode survives. For arbitrary finite-mean iid recovery, all distributions with mean `m` share `r=lambda exp(-lambda m)`, yet `G_DC=0` at the common maximum iff recovery is deterministic. Exact equal-mean/equal-variance/equal-saturation laws have different timestamp information.

### WP04 — optical survival-to-synthesis

A seeded carrier/sideband model has

`R_lin^2=p(1-p)/[kappa^2(1-2p)^2]`

and

`(R_lin^2/4)Tr F<=p`.

At the empty-sideband boundary,

`Delta P_s=4kappa^2`, `Tr F<=Delta P_s`,

with exact crossover

`lim_(p->0+)4p/R_lin^2=Delta P_s`.

Ordinary ideal weak phase modulation gives `Delta P_+=Delta P_-=1` and a fixed phase-sensitive analyzer attaining

`Tr F=4=[sqrt(Delta P_+)+sqrt(Delta P_-)]^2`.

### WP05 — standard Hamiltonian implementation

Two resonant bosonic modes with

`H_0=hbar nu(N_C+N_S)`

and the standard beam-splitter exchange are restricted to the fixed-energy `N_tot=2` manifold

`|2,0>, |1,1>, |0,2>`.

For

`U(x,y)=exp[-i g t(xB_x+yB_y)]`

and baseline `|1,1>`,

`Var(K_x)=Var(K_y)=4(g t)^2`,

so

**`V_impl=8(g t)^2`.**

The independently observable endpoint curvatures are

`Delta P_L=Delta P_U=8(g t)^2`,

hence

**`Tr C=16(g t)^2`,**

**`V_min=(1/2)Tr C=8(g t)^2`.**

The autonomous spectral action is

**`A_ex^(2)=hbar nu V_min=8 hbar nu(g t)^2`.**

The complete total bare-energy distribution remains fixed at `2hbar nu` throughout.

For a fixed-duration physical interaction family,

**`V_impl=(t^2/hbar^2)sum_j Var(H_j)`.**

This is a generator-variance/coupling-strength quantity, not work, consumed RF power, mean interaction energy, operator norm, peak coupling, controller bandwidth, or fixed-controller-spectrum optimum.

## Current significance assessment

The likely Paper-4 core is now:

1. **memory result:** standard saturation and low-order dead-time summaries can provably miss temporal-information transfer;
2. **support result:** seeded versus empty sidebands realize the finite-radius survival / rank-boundary synthesis transition with an exact measurable crossover;
3. **implementation result:** the boundary curvature has a standard fixed-energy resonant-exchange realization whose exact minimum coupling can be checked by independent coupling and endpoint-curvature calibration.

WP01/WP02 are likely supporting bridge material rather than the central novelty.

## Immediate work order

1. WP06 — rank the results, create the integrated falsification matrix, and define the **minimum** practical paper stack.
2. WP07 — dedicated prior-art/significance gate before manuscript drafting.
3. Update all documentation after each material change.

## Claim discipline

Priority remains **unverified, not certified**. No prize-level framing. No novelty claim for standard NEP, generic Fisher sensing, Poisson/dead-time formulas, renewal spectra, electro-optic sidebands, beam-splitter Hamiltonians, or standard interferometry.

## Frozen publication packages

PRXQ R4: run `32674844366` PASS; artifact `9502376602`.

PRA R1: run `32673160217` PASS; artifact `9501942180`.
