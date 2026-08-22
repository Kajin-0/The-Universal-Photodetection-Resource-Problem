# WP05 — Operational closure no-go and local temporal Landauer baseline

**Date:** 2026-08-21

## Status

This work package closes the first formulation of the grand challenge.

Two conclusions:

1. **No thermodynamic cost is determined by the temporal Fisher spectrum `G(omega)` alone.** Physical embedding and operational boundary are indispensable.
2. Once a measurement-and-record cycle is explicitly closed, a weak-waveform Landauer-style cost follows, but it is primarily a composition of established information geometry and established information thermodynamics. It is a baseline theorem, not the high-ceiling endpoint.

## 1. Distinguish three quantities

Do not conflate:

- **observable information-transfer spectrum** `G(omega)`: property of the source-to-accessible-record statistical channel;
- **actual entropy production/work** of a particular physical realization;
- **minimum thermodynamic implementation cost/capacity** of a fully specified logical/quantum channel given Hamiltonians, bath, allowed operations, accuracy criterion, etc.

The first does not determine either of the latter two.

## 2. Theorem-level no-go A — actual dissipation is not a functional of `G`

Let a physical realization `R` implement an accessible source-to-record channel `K`, hence Fisher spectrum `G_K`.

Form a product realization `R_c = R tensor S_c`, where `S_c` is an autonomous ancillary subsystem statistically independent of the source and inaccessible to the observer. Choose `S_c` to dissipate at any prescribed rate `c>=0` while leaving the source-to-record law unchanged.

Then for all `c`:

`G_{R_c}(omega)=G_R(omega)`,

while the actual entropy-production rate can be shifted upward by `c`.

Therefore no equality, upper bound, or unique inference of actual dissipation from `G` is possible.

This is simple but important: `G` is an operational channel property, while dissipation depends on implementation details invisible to that channel.

## 3. No-go B — minimum channel work is also not specified by `G`

Modern quantum thermodynamics assigns a minimum asymptotic work cost / thermodynamic capacity to a **fully specified physical process**, including input/output Hamiltonians. Faist--Berta--Brandao show that the thermodynamic capacity is a channel quantity only after those thermodynamic structures are fixed.

`G` does not encode Hamiltonians or equilibrium reference states.

Even the same logical identity map can have zero thermodynamic capacity when input/output systems have matching degenerate Hamiltonians, while a physically different embedding of the same logical map between systems with nontrivial energy gaps can have a different and arbitrarily large work requirement as the energy scale is increased.

Thus `G=1` does not fix thermodynamic capacity. More generally, a temporal FI spectrum is insufficient to determine the minimum work cost of a physical process without energetic structure.

Consequences:

- there is no universal detector-work functional `W_min = C[G]` at the abstract channel level;
- a nonzero lower bound based only on `G` is not well posed across arbitrary physical embeddings;
- any positive theorem must state the thermodynamic boundary and admissible implementation class.

## 4. Measurement itself need not carry a positive universal work cost

Faist et al. (Nature Communications 6, 7669, 2015) explicitly show that a quantum measurement logical process can in principle be implemented at no positive work cost in suitable circumstances; cyclicity is restored only after accounting for preparation/reset of the record memory and use of post-measurement side information.

Sagawa--Ueda likewise separate measurement and erasure costs and show that their distribution depends on the memory energetics; what is universal is an information-thermodynamic balance for the full cycle, not a fixed cost assigned to the abstract act of observing.

Therefore temporal Fisher retention alone cannot imply a detector-internal housekeeping work cost.

## 5. Minimal operational closure

A meaningful closed measurement cycle must specify at least:

1. source/input system and which of its free energy may be consumed;
2. detector ready state;
3. physical memory/register that holds the accessible record;
4. record reliability/distinguishability convention;
5. whether the record is retained externally or erased;
6. side information available during reset;
7. reset/ready-state restoration;
8. time-reference resource (internal clock versus external reference);
9. throughput/finite-time requirement;
10. bath temperature(s), Hamiltonians, and allowed operations.

Without these, a universal thermodynamic cost statement is underdetermined.

## 6. Local random-waveform mutual-information expansion

Although it is not the high-ceiling theorem, there is a clean bridge from Paper 2's Fisher spectrum to information thermodynamics once a signal ensemble is specified.

Let a finite-dimensional weak source perturbation be

`theta = epsilon X`,

where `E[X]=0`, `Cov(X)=C`, and the output experiment is differentiable in quadratic mean at `theta=0` with Fisher matrix `F_out`.

Then the mutual information between the random local parameter and the output satisfies

`I(X;Y) = (epsilon^2/2) Tr(C F_out) + o(epsilon^2)`

(in nats), under the standard regular local-asymptotic expansion.

This is the Bayesian/local-information form of Fisher geometry.

### Stationary waveform limit

For a stationary weak random waveform with spectral density `S_X(omega)` and the autonomous Poisson-channel Fisher spectrum

`F_out[u,v] = Phi0/(2*pi) int G(omega) U*(omega)V(omega) domega`,

the long-time mutual-information rate has leading term

`boxed: I_dot = epsilon^2 Phi0/(4*pi) int S_X(omega) G(omega) domega + o(epsilon^2)`.

The exact convention for `S_X` must be kept consistent with the Fourier normalization used in Paper 2.

This formula makes clear that `G` is not itself an information rate; it becomes one only after a source prior/signal covariance is supplied.

## 7. Closed-cycle Landauer baseline

Suppose now that each measurement cycle writes the acquired information into a physical memory and the entire apparatus is returned to its initial ready/memory state. If reset is performed without retaining side information that lowers the erasure cost, standard information thermodynamics implies that the measurement+reset work cannot undercut the information free-energy cost associated with the correlations created.

In the simplest isothermal symmetric-memory idealization this gives the local leading-order bound

`boxed: W_dot_cycle >= k_B T * epsilon^2 Phi0/(4*pi) int S_X(omega) G(omega) domega + o(epsilon^2)`.

Interpretation:

- this is a **closed-cycle signal-ensemble-dependent work bound**;
- it is not an intrinsic cost of the detector core;
- it vanishes with signal amplitude as `epsilon^2`;
- side information, asymmetric memories, source free energy, or exported records alter the detailed accounting;
- finite-time operation can add extra dissipation beyond the quasistatic information term.

## 8. Prior-art positioning

The components are established:

- local mutual information has Fisher information as its second-order metric;
- Sagawa--Ueda derive thermodynamic measurement/erasure inequalities involving mutual information;
- Faist et al. derive minimal work costs of arbitrary information-processing maps and show measurement can be work-free in principle while reset closes the cycle;
- Faist--Berta--Brandao define thermodynamic capacity and optimal implementations of quantum processes;
- stochastic thermodynamics of computation decomposes Landauer, mismatch, and residual costs.

Therefore the local temporal Landauer equation above should presently be viewed as a useful synthesis/application, not as a major novelty claim.

## 9. What would constitute a genuinely stronger result

A high-ceiling theorem must involve constraints that are absent from quasistatic abstract information thermodynamics, for example simultaneously:

- autonomous continuous operation;
- finite throughput;
- finite record error probability / durable amplification;
- reset to a ready state;
- finite time-reference resource;
- finite dark-count/background requirement;
- temporal waveform information over a specified band.

The candidate target is no longer `work >= kT * information`, which is old. It is a **finite-rate, durable-record, temporally resolved measurement resource law** in which the Fisher spectrum enters nontrivially and cannot be removed by quasistatic/reversible implementations.

## 10. Next gate

Audit whether existing finite-time Landauer, autonomous-detector, and reliable-memory literature already yields a universal joint bound on:

- timing precision/bandwidth;
- throughput/reset time;
- false-positive/error rate;
- dissipation/power.

Schwarzhans et al. obtain exactly this flavor of tradeoff in one autonomous quantum-detector model. The next question is whether any part can be elevated from their model to a model-independent theorem under explicit closed-cycle assumptions.
