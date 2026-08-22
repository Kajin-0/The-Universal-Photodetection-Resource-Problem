# Roadmap — Autonomous Temporal Information Law

**Branch:** `agent/autonomous-temporal-information-law`

## Goal

Seek a foundational autonomous resource principle for temporal information. The finished Rev11 random-time law is a special-source result and remains frozen on its parent branch.

## Stage A — destroy naive formulations

### WP01 — prior-art and model boundary

Status: **PASS**.

Established collisions:

- modes-of-asymmetry/reference-frame support laws are prior art;
- mode trace-norm monotones are prior art;
- QFI/Fisher asymmetry resource measures are prior art;
- autonomous finite clocks/control are prior art;
- generic energy-constrained multistep metrology is active prior art.

Novelty must be a quantitative temporal-information performance/resource law, not mode existence.

### WP02 — local-Fisher no-go and robust tangent radius

Status: **ANALYTIC PASS; numerical adversarial checks PASS; priority unverified**.

Main no-go:

At fixed baseline mean excess energy, arbitrary local state synthesis can place fixed Fisher information at arbitrarily high Bohr frequency by shrinking the physical neighborhood of the tangent. Therefore **local Fisher information alone is too local** for a universal energy-frequency law.

New quantity:

`R_lin` = largest disk radius over which the two-quadrature linearized tangent remains a positive density operator.

For stationary `rho0` and exact positive-gap tangent `A_nu`,

`R_lin = 1 / w(rho0^(-1/2) A_nu rho0^(-1/2))`,

where `w` is numerical radius.

For arbitrary finite `N` and any joint POVM,

`(R_lin^2/4) [Tr F_N^(nu)/N] <= min(D_nu,U_nu) <= T(nu)`.

Hence

`Ebar+ >= (hbar nu R_lin^2/4) [Tr F_N^(nu)/N]`.

The two-level fixed-energy/high-frequency counterexample asymptotically saturates this robust energy law.

This is the current strongest theorem of the new branch.

## Stage B — finite-reference temporal-information conversion

### WP03 — reference-assisted parameter-to-time conversion

Status: **NEXT / ACTIVE**.

Minimal systems:

- `D`: time-symmetric data/program register carrying unknown parameter;
- `R`: finite quantum reference/clock/controller;
- `S`: target temporal signal/memory;
- globally time-translation-covariant, parameter-independent processing.

Established infrastructure:

`dot rho_out^(nu) = Phi(eta_R^(nu) tensor dot tau_D)`.

Do **not** claim this as new; it follows from Marvian--Spekkens mode theory.

Research targets:

1. Determine how `R_lin` transforms under reference-assisted covariant processing.
2. Find an operational performance functional for parameter information converted into temporal mode `nu`.
3. Derive a finite-reference upper bound stronger than mere mode trace-norm monotonicity.
4. Determine whether near-perfect temporal conversion at fixed `nu` forces divergence of a physical clock/reference resource.
5. Search for exact or asymptotically optimal reference states.

Candidate mathematical tools:

- tangent numerical radius;
- trace-norm mode monotones;
- monotone quantum Fisher metrics;
- channel/measurement simulation norms;
- positive-definite characteristic functions;
- semibounded moment/tail inequalities.

### WP04 — nonlinear synthesis loophole

Parallel target:

`R_lin=0` families can remain physical through curvature/second-order population (coherent-sideband type synthesis).

Determine the weakest additional physical datum that restores a theorem:

- fixed finite parameter amplitude;
- finite distinguishability at nonzero amplitude;
- bounded curvature/state acceleration;
- explicit preparation/control dynamics;
- energy/action paid by the controller.

A purely local finite-derivative law may itself be impossible; test this aggressively.

## Stage C — autonomous control/action

### WP05 — control-generator resource

A state-only law cannot be universal if arbitrary static interaction Hamiltonians of unbounded spectral scale are free.

Determine the correct charged dynamical quantity among or beyond:

- Hamiltonian spectral diameter;
- mean excess energy;
- energy variance/QFI;
- time-integrated interaction norm (action);
- thermodynamic free energy / entropy production;
- spectral asymmetry distribution.

Avoid assuming the answer.

### WP06 — unified state + control temporal resource law

Attempt a theorem for the complete apparatus:

`source + clock + controller + detector + memory`.

The ideal endpoint would bound temporal statistical information by a total resource that cannot be hidden in a classical timing reference or free external control.

## Stage D — beyond local Fisher

### WP07 — finite distinguishability

Move from local Fisher geometry to trace distance / hypothesis-testing error for finite waveform amplitudes.

### WP08 — mutual information / temporal channel capacity

If earlier stages succeed, formulate a temporal-information capacity law with physically explicit clock/control resources.

## Stage E — significance and publication gate

Only after a theorem survives hostile review:

- exhaustive priority audit;
- exact equality/near-equality constructions;
- independent numerical adversarial checks;
- identify experimentally testable consequence;
- decide whether the result merits a distinct foundational manuscript.

## Stop conditions

Do not continue a route if it reduces to:

- known mode-support monotonicity;
- generic QFI data processing;
- a standard quantum speed limit;
- generic energy-time uncertainty;
- an existing finite-clock simulation-error theorem;
- merely adding preparation/control energy without a new structural law.

Record negative results. A killed conjecture is part of the research program, not a documentation failure.
