# AGENTS.md

## Purpose

Durable project handoff for The Universal Photodetection Resource Problem. The repository, not chat history, is authoritative.

## Active branch

`agent/practical-temporal-information-benchmarks`

The three mature temporal-information papers remain scientifically frozen. The active fourth program translates them into standard detector measurements and explicit falsification tests.

## Read first

1. `docs/CURRENT_RESEARCH_STATE.md`
2. `practical_temporal_information/AGENTS.md`
3. `practical_temporal_information/notes/WP01_LINEAR_GAUSSIAN_FISHER_NEP_BRIDGE.md`
4. `practical_temporal_information/notes/WP02_POISSON_TIMESTAMPS_AND_JITTER.md`
5. `practical_temporal_information/notes/WP03_DEAD_TIME_RECOVERY_INFORMATION_BENCHMARKS.md`
6. `practical_temporal_information/notes/WP04_OPTICAL_SIDEBAND_SURVIVAL_SYNTHESIS_CROSSOVER.md`
7. `practical_temporal_information/notes/WP05_RESONANT_EXCHANGE_UNITARY_COUPLING_BRIDGE.md`

## Paper 4 current stack

- **WP01:** `Tr F/T=2/NEP(f)^2` for linear stationary Gaussian optical-power quadratures.
- **WP02:** ideal Poisson fractional-modulation timestamps give `Tr F/T=lambda_0`; independent timing jitter gives factor `|Phi_J(Omega)|^2`.
- **WP03:** mean dead time, recovery variance/CV, maximum count rate, and even the complete homogeneous saturation curve do not determine temporal-information transfer.
- **WP04:** seeded-to-empty optical sidebands realize the finite-radius survival -> rank-boundary synthesis transition with
  `lim_(p->0+)4p/R_lin^2=Delta P_s(0)`; ordinary ideal phase modulation saturates the bilateral boundary-curvature law.
- **WP05:** standard resonant beam-splitter physics realizes the exact implementation theorem inside a fixed total-energy shell.

WP05 standard model:

`H_0=hbar nu(N_C+N_S)`, baseline `|1,1>`, endpoints `|2,0>,|0,2>`.

For `U=exp[-i g t(xB_x+yB_y)]`,

`V_impl=8(g t)^2`,

`Tr C=16(g t)^2`,

`V_min=(1/2)Tr C=8(g t)^2`,

`A_ex=hbar nu V_min=8 hbar nu(g t)^2`.

The total bare-energy distribution remains exactly fixed. For a fixed-duration physical Hamiltonian family,

`V_impl=(t^2/hbar^2)sum_j Var(H_j)`.

Do not call this work, consumed RF energy, average interaction energy, operator norm, peak coupling, controller bandwidth, or fixed-controller-spectrum optimum.

## Immediate work order

1. WP06 — integrated falsification matrix, rank scientific value, define minimum practical manuscript stack, demote tutorial-only material.
2. WP07 — dedicated prior-art/significance gate before manuscript drafting.

## Claim discipline

No prize-level framing. No novelty claim for standard NEP, generic Fisher sensing, Poisson/dead-time formulas, renewal spectra, sideband generation, SU(2)/beam-splitter physics, or standard frequency-bin interferometry. Assign novelty only after WP07.

## Documentation rule

After every material advance, update the corresponding practical note and handoff. When the frontier moves, also update root `README.md`, `AGENTS.md`, `ROADMAP.md`, and `docs/CURRENT_RESEARCH_STATE.md`.
