# AGENTS — Autonomous Temporal Information Law

**Branch:** `agent/autonomous-temporal-information-law`

**Started:** 2026-08-22

This branch is a distinct theoretical program. The Rev11 random-time paper on `agent/temporal-information-resource-law` remains frozen and must not be rewritten from this branch unless a concrete defect is discovered.

## Grand question

> When the signal, clock/reference frame, controller, probe, detector, and memory are all finite physical systems and no ideal externally timed operation is free, what physical resource constrains the creation, transmission, and recovery of temporal information at frequency `nu`?

The target is not merely another bandwidth or quantum-speed-limit inequality. The desired endpoint is a general autonomous **temporal-information resource law** in which externally supplied timing/control is explicitly represented as a physical resource.

## Research standard

- Analytical/theoretical only.
- Falsification-first: attack every proposed law with minimal counterexamples before generalizing it.
- Existing asymmetry/reference-frame results are infrastructure, not novelty claims.
- Record all theorem attempts, counterexamples, literature collisions, and numerical checks immediately in this directory.
- Do not rely on chat history for recovery.
- Do not claim Nobel-level significance prospectively; judge significance only after a theorem survives proof and priority review.

## Current frontier

**WP01 — foundational scope and prior-art boundary.**

The first literature gate establishes that the qualitative statement

`a quantum reference frame can simulate only channel/measurement modes contained in the reference-frame state`

is already prior art: Marvian and Spekkens, *Phys. Rev. A* 90, 062110 (2014), DOI `10.1103/PhysRevA.90.062110`, especially their mode decomposition of states/channels and reference-frame simulation result.

Likewise, finite autonomous quantum clocks/control are established topics, including:

- Woods, Silva, Oppenheim, *Autonomous quantum machines and the finite-sized Quasi-Ideal clock*, arXiv:1607.04591;
- Erker et al., *Phys. Rev. X* 7, 031022 (2017), autonomous clock thermodynamic cost;
- Woods and Horodecki, *Phys. Rev. X* 13, 011016 (2023), autonomous implementation of quantum devices/control;
- Yamaguchi and Tajima, *Phys. Rev. Lett.* 131, 200203 (2023), energetic coherence/asymmetry conversion;
- Kudo and Tajima, *Phys. Rev. A* 107, 062418 (2023), Fisher information as an asymmetry resource measure;
- Hu et al., *Phys. Rev. Lett.* 137, 070201 (2026), Gaussian time-translation-covariant operations.

Therefore **mode existence**, generic asymmetry monotonicity, QFI as an asymmetry measure, and the mere idea of adding a finite clock/controller are not candidate breakthroughs.

## Immediate scientific target

Find a quantitative **information-performance law** rather than a support law.

Minimal conversion setting:

1. `D` — a time-symmetric data/program register carrying an unknown parameter;
2. `R` — finite clock/reference/controller with generator `H_R` and asymmetric state `eta_R`;
3. `S` — signal/output system;
4. a parameter-independent globally time-translation-covariant channel `Phi` on `D+R+S`;
5. no free asymmetric final measurement: any readout reference must be included in `R`/apparatus.

For a time-translation mode `nu`, covariance gives the exact structural identity

`dot rho_out^(nu) = Phi( eta_R^(nu) tensor dot tau_D )`

when the data register carries only zero-frequency asymmetry. This is an immediate consequence of established modes-of-asymmetry theory, so it is **baseline infrastructure only**.

The open target is an inequality of the schematic form

`temporal statistical information generated at nu <= quantitative finite-reference resource at nu`,

ideally followed by a semibounded-energy/action law and a divergent resource requirement as temporal fidelity approaches one.

## Critical no-go to test

A state-only law cannot be universal if arbitrary static interaction Hamiltonians are free. Scaling a time-independent interaction Hamiltonian by an arbitrarily large constant scales its internally generated oscillation frequencies while leaving the initial state unchanged. Any genuinely universal autonomous law must therefore account for at least one **dynamical generator/control resource** (Hamiltonian spectral scale, action, interaction norm, or equivalent), unless the allowed operations are restricted by a covariance/energy-conservation principle.

This no-go is a high-priority theorem/counterexample target for WP02.

## Read first

1. `autonomous_temporal_information/notes/WP01_FOUNDATIONAL_SCOPE_AND_PRIOR_ART_BOUNDARY.md`
2. `autonomous_temporal_information/ROADMAP.md`
3. frozen parent-program handoff: `grand_challenge/AGENTS.md`

## Documentation rule

Every material result must update this file and `autonomous_temporal_information/ROADMAP.md`. When a result becomes stable enough to change the project-level frontier, mirror the status onto the repository landing files. Until then, keep Rev11 advertised as the finished Grand Challenge paper and this program as the new exploratory branch.
