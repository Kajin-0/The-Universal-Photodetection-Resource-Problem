# WP01 — Foundational scope and prior-art boundary

**Date:** 2026-08-22

**Branch:** `agent/autonomous-temporal-information-law`

**Status:** PASS as a problem-definition gate. Several naive "breakthrough" formulations are already prior art and are explicitly excluded from novelty claims.

## 1. Motivation

Rev11 proves strong spectral resource laws for a fixed excitation whose unknown temporal structure enters through a random-time distribution. It also identifies the exact boundary: arbitrary parameter-dependent waveform-state synthesis can create a high-frequency tangent without being constrained by baseline source mean energy alone.

The new program asks whether that apparent escape route disappears when the timing/control apparatus itself is made physical rather than supplied as a free external clock.

The intended question is therefore not "can energetic coherence act as a clock?" or "do covariant channels preserve asymmetry modes?" Those are established. The intended question is whether there is a sharp **temporal statistical-information performance law** for a complete finite autonomous apparatus.

## 2. Prior-art collisions found immediately

### 2.1 Modes of asymmetry already solve the qualitative support problem

Marvian and Spekkens, *Modes of asymmetry: The application of harmonic analysis to symmetric quantum dynamics and quantum reference frames*, Phys. Rev. A 90, 062110 (2014), DOI `10.1103/PhysRevA.90.062110`, decompose states, measurements, and channels into symmetry modes.

For a reference-frame state `eta_R` used with a covariant joint channel to simulate an asymmetric channel `E`, their Lemma 17 gives the channel-mode component from the matching reference-frame mode. Their Proposition 18 implies schematically

`Modes(E) subseteq Modes(eta_R)`.

They also define mode-specific trace-norm asymmetry monotones.

Therefore the following are **not new**:

- a finite time reference must possess a mode needed by a simulated time-asymmetric channel/measurement;
- time-translation-covariant processing cannot create an absent mode;
- trace norms of state modes give quantitative asymmetry monotones.

These results are structural infrastructure for this program.

### 2.2 QFI / Fisher geometry is already an asymmetry resource

Kudo and Tajima, Phys. Rev. A 107, 062418 (2023), DOI `10.1103/PhysRevA.107.062418`, establish Fisher information matrix resource properties for connected Lie-group asymmetry.

Yamaguchi and Tajima, Phys. Rev. Lett. 131, 200203 (2023), DOI `10.1103/PhysRevLett.131.200203`, treat energetic coherence conversion with QFI/information-spectrum methods.

Thus "QFI is the clock resource" by itself is not a viable novelty claim.

### 2.3 Autonomous clocks and autonomous control are established

Relevant examples include:

- Woods, Silva, Oppenheim, arXiv:1607.04591, finite Quasi-Ideal clocks and autonomous quantum control;
- Erker et al., Phys. Rev. X 7, 031022 (2017), DOI `10.1103/PhysRevX.7.031022`, thermodynamic cost/accuracy of autonomous clocks;
- Woods and Horodecki, Phys. Rev. X 13, 011016 (2023), DOI `10.1103/PhysRevX.13.011016`, autonomous implementation of quantum devices/control;
- Malabarba, Short, Kammerlander, arXiv:1412.1338, clock-driven autonomous quantum thermal machines;
- current continuous-variable symmetry work such as Gaussian time-translation-covariant operations, Phys. Rev. Lett. 137, 070201 (2026), DOI `10.1103/9kmm-52nx`.

Therefore simply replacing an external time-dependent Hamiltonian by a finite quantum clock is not sufficient novelty.

### 2.4 Reference frames can simulate asymmetric operations

Quantum reference-frame/resource-theory literature already studies using asymmetric states to simulate noncovariant channels and measurements, including explicit energy-conserving constructions. Åberg's catalytic-coherence protocol and subsequent work are part of this neighborhood.

The new work must therefore quantify **temporal-information performance** in a way not already captured by generic channel-simulation accuracy or resource-state mode support.

## 3. Minimal conversion experiment

Use a deliberately stripped-down model.

- `D`: data/program register. The unknown parameter `theta` is encoded in `tau_theta`. To isolate temporal-resource conversion, take the time-translation generator on `D` to be degenerate so `tau_theta` contains only mode zero.
- `R`: physical clock/reference/controller in state `eta_R`, with generator `H_R`.
- `S`: target signal/output/memory with generator `H_S`.
- `Phi`: parameter-independent CPTP map covariant under joint time translations.
- Readout: no ideal asymmetric measurement may be supplied for free. If a timing reference is needed at readout, it must remain inside the explicit apparatus.

For time-translation mode `nu`, established covariance immediately implies

`dot rho_out^(nu) = Phi( eta_R^(nu) tensor dot tau_D )`

(up to including fixed symmetric ancillas).

This is a restatement/application of modes-of-asymmetry machinery, **not a new theorem**.

The research target is to turn this structural identity into a sharp operational inequality involving actual information performance.

## 4. What would count as a new theorem

Candidate target:

`I_temporal(nu) <= C_nu(eta_R,H_R)`

where `I_temporal(nu)` is an operationally defined amount of parameter information appearing specifically in temporal mode `nu` after arbitrary free autonomous processing.

Necessary properties of a useful `I_temporal`:

1. frequency resolved;
2. linked to an actual measurement task (classical FI, finite discrimination, or channel distinguishability), not merely an operator norm chosen for convenience;
3. obeys data processing;
4. does not become infinite/trivial for the pure coherent clock states that are operationally useful;
5. admits a resource moment/tail law capable of proving a high-fidelity divergence if such a divergence is true.

## 5. First foundational no-go: arbitrary Hamiltonian strength cannot be free

A universal state-only temporal-frequency law is immediately suspect if arbitrary time-independent interactions with unbounded norm are admitted at zero cost.

Minimal example:

Take one qubit initially in a fixed state independent of a scale `Lambda` and evolve under

`H_Lambda = hbar Lambda sigma_x`.

For a suitable fixed observable/state pair, the output contains oscillations at angular frequency proportional to `Lambda`. Sending `Lambda -> infinity` produces arbitrarily fast internal temporal variation without changing the initial state resource.

Therefore any theorem attempting to upper-bound all autonomous temporal frequencies using only a functional of the initial state is false unless:

- the allowed Hamiltonians are restricted by a symmetry/conservation condition; or
- the Hamiltonian/control generator is itself charged as a resource.

WP02 will make this statement rigorous and test stronger variants where one fixes mean initial energy, variance, or other state quantities.

## 6. Candidate resource layers

The program should distinguish rather than prematurely collapse:

### State/reference resource

Examples: energetic coherence, mode spectrum, asymmetry, energy survival, QFI/skew information.

### Generator/control resource

Examples: spectral diameter, interaction norm, mean interaction energy, time-integrated norm/action, bandwidth of the autonomous Hamiltonian.

### Thermodynamic resource

Examples: free energy, entropy production, nonequilibrium bias, power.

### Statistical-information resource

The parameter information originally supplied in `D`; this cannot be created by data processing and should not be confused with the resource needed to move it into a high temporal mode.

A foundational law may require more than one layer.

## 7. Working hypothesis after WP01

The most promising target is not a scalar "energy-time uncertainty" relation. It is a **spectral conversion law**:

> Converting ordinary parameter information into temporal information at mode `nu` requires a matching physical asymmetry/control resource in the autonomous apparatus, and the achievable statistical performance is quantitatively bounded by that finite resource.

A stronger long-term conjecture is that near-perfect conversion at fixed nonzero `nu` requires a divergent total resource after both reference-state and dynamical-control costs are accounted for. This is a conjecture only; existing finite-clock constructions make it essential to prove rather than assume the divergence.

## 8. Immediate next work

WP02:

1. prove the state-only no-go rigorously;
2. determine which Hamiltonian quantities prevent the scaling counterexample;
3. formulate the cleanest free-operation class for WP03;
4. search for a performance metric whose quantitative bound is not already a direct corollary of Marvian--Spekkens trace-norm mode monotonicity.

## 9. Novelty discipline

Do not claim novelty for:

- modes-of-asymmetry decomposition;
- mode-support inclusion for simulated channels/measurements;
- mode trace-norm monotones;
- QFI as an asymmetry measure;
- finite quantum clocks per se;
- autonomous realization of externally timed operations per se;
- generic energy-constrained metrology;
- generic quantum speed limits;
- standard energy-time uncertainty relations.

The repository must remain explicit about these collisions as the work progresses.
