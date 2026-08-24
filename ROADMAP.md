# Research Roadmap

**Updated:** 2026-08-23

**Active branch:** `agent/practical-temporal-information-benchmarks`

## Mature papers — frozen separately

1. PRX Quantum flagship — survival/synthesis conceptual law.
2. Broad random-time/timestamp spectral-information paper.
3. PRA exact unitary-coupling completion.

## Active Paper 4

Working title:

> **Operational temporal-information benchmarks for photodetection**

## Completed research gates

- **WP01:** linear Gaussian detector -> `Tr F/T=2/NEP(f)^2`.
- **WP02:** ideal Poisson timestamps -> `Tr F/T=lambda0`; independent jitter -> `|Phi_J|^2`.
- **WP03:** practical translation of the frozen Type-II memory theorem.
- **WP04:** exact seeded-to-empty sideband survival/synthesis crossover and ideal phase-modulation boundary saturation.
- **WP05:** standard fixed-energy resonant beam splitter realizes `V_min=(1/2)Tr C` and `A_ex=hbar nu V_min`.
- **WP06:** minimum manuscript architecture and falsification hierarchy.
- **WP07:** prior-art/significance gate — PASS WITH NARROWED CLAIMS.
- **WP08:** final pre-manuscript theorem/benchmark stack — PASS.
- **WP09:** first hostile manuscript audit — CONDITIONAL PASS with one substantive theorem strengthening.

## WP09 strengthening

The selected sideband need not be the only populated mode. For

`rho_p=a_p|c><c|+p|s><s|+sigma_p`,

where `sigma_p` is an arbitrary positive spectator block, `a_p->q>0`, and the calibrated converter acts only on the carrier/sideband pair,

`R_lin^2=a_p p/[kappa^2(a_p-p)^2]`,

`Delta P_s(0)=4kappa^2 q`,

so

**`lim_(p->0+)4p/R_lin^2=Delta P_s(0)`.**

This removes the principal hostile-review concern that the crossover is an artifact of a pure/normed two-level baseline. It remains a model theorem for a lossless selected-mode converter with inert spectators, not a universal theorem for arbitrary lossy channels.

The finite-radius coefficient was rechecked directly against the frozen flagship proof:

`(R_lin^2/4)Tr F <= Tr(P_U rho_0)`.

For the seeded sideband `Tr(P_U rho_0)=p`; no coefficient repair is needed.

## Manuscript state

The first full REVTeX draft exists in `manuscript/practical_temporal_information/`.

Its initial PR-triggered CI passed the static provenance/claim gate and failed only because REVTeX `ruledtabular` cannot wrap the paragraph-width falsification-table columns. A deterministic R1 transform now removes only that wrapper before compilation.

## Active work order

1. finish R1 mechanical build verification;
2. generate scientific R2 replacing the narrow crossover proposition with the WP09 spectator-independent statement;
3. compile/render R2;
4. run a second hostile manuscript-level audit;
5. if R2 passes, produce at most four publication figures and compress for Physical Review Applied style.

## Claim hierarchy

### Candidate original Paper-4 science

- WP09 selected-mode support-seed crossover;
- ideal weak phase-modulation boundary saturator;
- integrated falsification architecture.

### Cited upstream results

- Type-II memory theorem from the frozen random-time paper;
- exact unitary-coupling theorem from the frozen PRA paper.

### Standard bridges

- NEP/FI relation;
- Poisson/jitter relation;
- WP08 colored-noise detector counterexample;
- standard resonant beam-splitter realization.

## Claim discipline

No novelty claim for standard NEP/detectivity, generic Fisher sensing, Poisson/dead-time formulas, renewal spectra, variable/random dead time, interval characterization, electro-optic sidebands, seeded/vacuum interferometry, beam-splitter physics, standard interferometry, or generic rank-boundary QFI. No implied experimental validation without data. No prize-level framing.

## Documentation cadence

Update the manuscript handoff and all landing files after every material manuscript/science change.
