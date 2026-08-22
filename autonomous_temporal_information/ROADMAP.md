# Roadmap — Autonomous Temporal Information Law

**Branch:** `agent/autonomous-temporal-information-law`

## Goal

Seek a foundational autonomous resource principle for temporal information. The finished Rev11 random-time law is a special-source result and remains frozen on its parent branch.

## Stage A — destroy naive formulations

### WP01 — prior-art and model boundary

Status: **ACTIVE / largely complete**.

Tasks:

- distinguish new target from modes-of-asymmetry/reference-frame theory;
- distinguish it from quantum speed limits, generic QFI asymmetry monotones, autonomous clock thermodynamics, and energy-constrained multistep metrology;
- define what must count as a physical clock/control/reference resource;
- identify whether any state-only formulation is impossible when arbitrary Hamiltonian strength is free.

### WP02 — state-only no-go and minimal autonomous counterexamples

Target theorem/no-go:

> No nontrivial upper bound on internally generated temporal frequency can depend only on the initial state resource if arbitrary time-independent interaction Hamiltonians with unbounded spectral scale are admitted for free.

Use the smallest possible autonomous systems first (qubit / two-qubit models), then formulate a representation-independent statement.

Deliverables:

- exact counterexample family;
- statement of the minimum dynamical resource any universal theorem must charge;
- adversarial search for loopholes (energy expectation, energy variance, interaction energy, operator norm, spectral diameter, action).

## Stage B — finite-reference temporal-information conversion

### WP03 — reference-assisted parameter-to-time conversion experiment

Minimal systems:

- `D`: time-symmetric data/program register carrying unknown parameter;
- `R`: finite quantum reference/clock/controller;
- `S`: target temporal signal/memory;
- globally time-translation-covariant, parameter-independent processing.

Established infrastructure:

`dot rho_out^(nu) = Phi(eta_R^(nu) tensor dot tau_D)`.

Do **not** claim this as new; it follows from Marvian--Spekkens mode theory.

Research target:

define an operational temporal-information performance functional that is:

1. frequency resolved;
2. monotone under free autonomous processing;
3. finite and informative for physically useful pure clock states;
4. linked to actual classical Fisher information, finite discrimination, or channel simulation error;
5. quantitatively constrained by a clock/reference resource.

Candidate mathematical tools:

- trace-norm mode monotones;
- Petz/monotone quantum Fisher metrics;
- Bures/Hellinger geometry;
- channel distinguishability / diamond norm;
- positive-definite characteristic functions;
- semibounded moment/tail inequalities.

### WP04 — sharp finite-clock performance law

Desired form:

`performance_at_nu <= C_nu(reference state, reference Hamiltonian)`.

Then seek a resource moment law, e.g.

`total reference resource >= Phi(nu, performance)`.

Critical success criterion:

`performance -> 1` at fixed nonzero `nu` should force divergence of an explicitly physical resource, unless a finite exact implementation is possible and thereby falsifies the conjecture.

## Stage C — add autonomous control/action

### WP05 — control-generator resource

If covariant operations alone are too restrictive, explicitly include a finite autonomous controller and its interaction Hamiltonian.

Determine the correct charged quantity among or beyond:

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
- merely adding the energy of preparation/control without a new structural law.

Record negative results. A killed conjecture is part of the research program, not a failure of documentation.
