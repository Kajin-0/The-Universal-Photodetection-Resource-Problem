# WP01 — Landscape audit and first no-go constraints

**Date:** 2026-08-21

## Objective

Before proposing a universal physical cost for the temporal Fisher spectrum `G(omega)`, identify existing theory that already occupies obvious formulations and kill candidate laws that are too broad.

## Starting point inherited from Paper 2

For a homogeneous Poisson source and any parameter-independent autonomous classical detector channel `K`, the local weak-waveform Fisher form is

`F_out[u,v] = Phi0/(2*pi) int G_K(omega) U*(omega)V(omega) domega`,

with `0 <= G_K <= 1` a.e.

This is a property of the stochastic input-output channel. It does not by itself specify a microscopic thermodynamic implementation.

## Literature collisions

### 1. Entropy production is not a universal information-acquisition rate bound

Barato, Hartich, and Seifert, *Phys. Rev. E* **87**, 042104 (2013), DOI `10.1103/PhysRevE.87.042104`, explicitly analyze autonomous sensory networks and find that there is **no universal bound** forcing information-acquisition rate to be smaller than thermodynamic entropy production.

Therefore reject any starting conjecture of the form

`information rate <= entropy production rate`

without substantial additional assumptions.

### 2. Markov response precision is already bounded by dynamical activity

Liu and Gu, *Communications Physics* **8**, 62 (2025), DOI `10.1038/s42005-025-01982-w`, derive response kinetic uncertainty relations for broad Markov jump processes. Their path Fisher information satisfies a bound of the form

`I(theta) <= a_max^2 A`,

where `A` is dynamical activity and `a_max` controls logarithmic rate sensitivity.

Therefore a generic Markov statement that FI/response precision costs dynamical activity is not a new target.

### 3. Frequency-domain response/dissipation uncertainty theory already exists

Kwon et al., arXiv:2605.05038 (2026), *Nonequilibrium Fluctuation-Response Theory in the Frequency Domain*, derive exact frequency-domain fluctuation-response identities plus kinetic and thermodynamic uncertainty relations for Markov jump and overdamped Langevin systems.

Therefore reject a project framed merely as “derive frequency-resolved FI/response versus dissipation.”

### 4. Autonomous quantum detector thermodynamics is already active

Schwarzhans et al., *PRX Quantum* **7**, 033001 (2026), DOI `10.1103/wm5p-tjtg`, construct a minimal autonomous quantum detector thermal machine and study entropy-production tradeoffs involving efficiency, gain, jitter, dead time, and dark counts.

Their results are model-specific rather than a universal Fisher-spectrum theorem, but they occupy the obvious “detector performance costs entropy production” narrative.

### 5. Quantum measurement accessibility gaps are classical territory in quantum metrology

It is standard that classical Fisher information from a chosen POVM can be strictly below quantum Fisher information; measurement-induced FI hierarchies and continuous retrieval of output-field QFI are established topics. Therefore the statement

`chosen readout FI < QFI`

is not itself a novel target.

### 6. Time-translation asymmetry/QFI is already a developed resource theory

QFI is a monotone/resource measure for time-translation asymmetry and quantum clock quality. Any attempt to use “clock QFI” as the missing temporal resource must produce a new theorem tied specifically to waveform information transfer through an autonomous measurement apparatus, not simply restate asymmetry monotonicity.

## First channel-level no-go observations

### A. `G(omega)` cannot determine thermodynamic cost

`G` is determined by the stochastic input-output channel. Thermodynamic cost is implementation-dependent.

Given any physical realization of a channel `K`, append an independent autonomous dissipative subsystem whose state/output is ignored. The observable channel `K`, hence `G`, is unchanged while total entropy production can be increased arbitrarily.

Thus there can be no universal equality or upper bound identifying thermodynamic cost from `G` alone.

### B. Detector-internal housekeeping dissipation cannot have a positive universal lower bound from `G` unless the measurement boundary is specified

The identity/transparent timing channel preserves all source information (`G=1`) as an abstract autonomous channel. If timestamping, durable memory, amplification, and reset are treated as external resources, the intrinsic channel can be passive.

Therefore a positive detector-internal cost law `R >= C[G] > 0` is ill-posed unless the physical accounting boundary includes enough of the readout cycle to exclude this counterexample.

### C. A fixed physical resource does not determine information transfer

Parameter-independent downstream coarse graining can reduce `G` all the way to zero without changing the upstream detector physics. Thus a resource amount alone cannot specify the retained-information spectrum unless the accessible-record definition is part of the object.

## Consequence

The grand question must be reformulated around an **operationally closed measurement cycle**, not merely an input-output stochastic channel.

Minimum bookkeeping candidates:

1. ready-state preparation / reset;
2. autonomous timing reference or explicitly external clock;
3. amplification / gain requirement;
4. record distinguishability and durability;
5. finite throughput / cycle time;
6. what energy/information carried by the incident event is allowed to power;
7. precise system boundary over which entropy production is counted.

## High-value surviving directions

1. A no-go/realization theorem showing exactly which additional operational assumptions are necessary before any thermodynamic cost of `G` can exist.
2. A classification theorem for information singularities that does not rely on thermodynamics.
3. A closed-cycle resource theorem including record/reset/time-reference resources, if a nontrivial universal bound survives.
4. A quantum extension only if it yields a specifically temporal/trajectory phenomenon beyond generic CFI-QFI gaps.

## Decision

Do **not** begin by guessing an entropy-production integral bound. First prove the channel/implementation separation cleanly and identify the smallest operational closure under which a nonzero resource lower bound is even meaningful.
