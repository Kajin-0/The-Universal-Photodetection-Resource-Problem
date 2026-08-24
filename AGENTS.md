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
7. `manuscript/autonomous_temporal_information/MANUSCRIPT_HANDOFF.md`
8. `manuscript/dynamical_implementation_cost/MANUSCRIPT_HANDOFF.md`

## Mature paper architecture — preserve

1. PRXQ flagship: *Two spectral-resource regimes for autonomous temporal information*.
2. Broad random-time/timestamp spectral-information paper.
3. PRA dynamical completion: *Exact minimum unitary coupling cost of prescribed rank-changing quantum-state curvature*.

Do not concatenate these papers and do not copy their full proof stacks into Paper 4.

## Paper 4 current frontier

### WP01

Linear stationary Gaussian weak-signal detector:

`Tr F/T=2|R(f)|^2/S_n(f)=2/NEP(f)^2`.

### WP02

Ideal Poisson fractional-modulation timestamps:

`Tr F/T=lambda_0`,

with independent jitter factor `|Phi_J(Omega)|^2`.

### WP03

Conventional dead-time/saturation characterization is insufficient. Deterministic Type-II recovery at `lambda tau=1` is DC-information blind but retains every nonzero mode. Arbitrary finite-mean iid recovery shares `r=lambda exp(-lambda m)`, yet `G_DC=0` at the common maximum iff recovery is deterministic. Explicit equal-mean/equal-variance/equal-saturation recovery laws have different timestamp information.

### WP04

Exact seeded carrier/sideband model:

`rho_p=(1-p)|c><c|+p|s><s|`.

With mixing coefficient `kappa`,

`R_lin^2=p(1-p)/[kappa^2(1-2p)^2]`,

and for `p>0`

`(R_lin^2/4)Tr F<=p`.

At the empty-sideband boundary `p=0`,

`Delta P_s(0)=4kappa^2`,

`Tr F<=Delta P_s(0)`,

and

**`lim_(p->0+)4p/R_lin^2=Delta P_s(0)`.**

A fixed four-outcome frequency-bin POVM saturates the one-sided boundary law.

Ordinary weak phase modulation gives two baseline-empty first sidebands with

`Delta P_+=Delta P_-=1`

and a fixed three-mode phase-sensitive analyzer attains

**`Tr F=4=[sqrt(Delta P_+)+sqrt(Delta P_-)]^2`.**

This is an exact ideal saturation example of the bilateral boundary-curvature theorem using standard optical sidebands.

Do not infer autonomous action or RF work from the externally driven EOM. WP05 must include the controller/clock explicitly before using `A_ex=hbar nu V_min` physically.

## Immediate work order

1. WP05 — textbook resonant-exchange/controller interpretation of the PRA coupling cost.
2. WP06 — integrated falsification matrix and minimal practical result stack.
3. WP07 — dedicated prior-art/significance gate before manuscript drafting.

## Claim discipline

No prize-level framing. No novelty claim for standard NEP, Fisher sensing, Poisson/dead-time formulas, renewal spectra, electro-optic sideband generation, SU(2) mode mixing, or standard frequency-bin interferometry. Assign novelty only after WP07.

## Documentation rule

After every material advance, update the corresponding practical note and handoff. When the frontier moves, also update root `README.md`, `AGENTS.md`, `ROADMAP.md`, and `docs/CURRENT_RESEARCH_STATE.md`.
