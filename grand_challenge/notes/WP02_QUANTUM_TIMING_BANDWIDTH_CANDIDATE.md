# WP02 — Candidate quantum timing-bandwidth bridge theorem

**Date:** 2026-08-21

## Status

Candidate bridge theorem. The mathematical ingredients are substantially classical; novelty is **not established**. Do not promote to a paper claim until the targeted prior-art audit and physical-boundary audit are complete.

## 1. Classical shift model

Let a normalized timestamp have a translation family

`p_theta(t)=f(t-theta)`

with finite shift Fisher information

`I_t = int (f'(t)^2/f(t)) dt`.

Equivalently, writing `f=psi^2` with `||psi||_2=1`,

`I_t = 4 ||psi'||_2^2`.

For the normalized one-branch event-timing channel used in the earlier independent-event theory,

`B_FI = (1/2) int f(t)^2 dt`.

## 2. Sharp density-level inequality

The sharp one-dimensional Gagliardo--Nirenberg inequality

`||psi||_4^4 <= (1/sqrt(3)) ||psi'||_2 ||psi||_2^3`

gives, for `||psi||_2=1`,

`int f^2 <= sqrt(I_t)/(2 sqrt(3))`.

Therefore

`boxed: B_FI <= sqrt(I_t)/(4 sqrt(3))`.

The constant is sharp.

### Equality family

Equality is attained by translates/scalings of the sech profile for `psi`, hence by

`f_a,t0(t) = (a/2) sech^2[a(t-t0)]`, `a>0`.

For this family,

`I_t = 4 a^2/3`,

`int f^2 = a/3`,

`B_FI = a/6`,

which saturates the bound.

## 3. Accessible marks

Suppose the complete timestamp record contains an accessible mark `m`, with normalized mark law `pi(dm)` and conditional timing density `f_m(t-theta)`.

The event-channel Fisher-equivalent bandwidth is

`B_FI = (1/2) int pi(dm) int f_m^2 dt`.

For each mark,

`int f_m^2 <= sqrt(I_m)/(2 sqrt(3))`.

Jensen/Cauchy gives

`B_FI <= [1/(4 sqrt(3))] int pi(dm) sqrt(I_m)`

`<= sqrt(I_mark,time)/(4 sqrt(3))`,

where

`I_mark,time = int pi(dm) I_m`

is the classical Fisher information of the complete marked timestamp for a common shift (assuming the mark probabilities themselves are shift-independent).

Thus the same constant survives complete accessible marking:

`boxed: B_FI <= sqrt(I_record,shift)/(4 sqrt(3))`.

## 4. Quantum measurement corollary

Let the timestamp/mark record be produced by a parameter-independent POVM on a quantum state family `rho_theta` encoding an unknown time shift `theta`. Braunstein--Caves data processing/optimization gives

`I_record,shift <= F_Q[rho_theta]`.

Hence

`boxed: B_FI <= sqrt(F_Q)/(4 sqrt(3))`.

If the shift is unitary,

`rho_theta = exp(-i H theta/hbar) rho exp(+i H theta/hbar)`,

then

`F_Q <= 4 (Delta H)^2/hbar^2`,

with equality for pure states. Therefore

`boxed: B_FI <= Delta H/(2 sqrt(3) hbar)`.

This is a bound on the bandwidth of a covariant timestamp readout of a time-shifted quantum state. It is **not** yet a detector-internal energetic-cost theorem.

## 5. Finite shift-QFI excludes movable timing atoms

A continuously translated classical outcome law containing a positive atomic mass at a moving timestamp cannot be differentiable in quadratic mean with finite shift Fisher information.

Reason: let `mu_theta` be the translate of `mu_0`, and suppose `mu_0` has positive total atomic mass. The set of pairwise differences of atom locations is countable. Choose a sequence `theta_n -> 0` avoiding this difference set. Along that sequence none of the atoms of `mu_0` align with atoms of `mu_theta_n`; a fixed positive singular mass is unmatched, so the Hellinger affinity stays bounded away from one. Thus Hellinger distance is not `O(|theta|)` and the family is not DQM.

Therefore any outcome translation family obtained from a finite-QFI quantum state by a parameter-independent measurement must be non-atomic in its continuously translated timestamp coordinate.

This is a regularity statement about the **outcome shift family**, not yet a theorem that every ideal point-process atom in Paper 2 is forbidden. Paper 2 conditions on a classical latent incident-event time; connecting that latent model to a finite-QFI quantum source requires an explicit source--detector interface.

## 6. Prior-art status

### Established ingredients

- Fisher information of a location family and Hellinger/DQM regularity are classical asymptotic statistics.
- Sharp Gagliardo--Nirenberg inequalities and equivalent Fisher--Renyi/Stam-type inequalities are established mathematics (e.g. Lutwak--Yang--Zhang and sharp GN literature).
- QFI as the maximal classical FI over quantum measurements is Braunstein--Caves (1994).
- QFI is a resource measure for time-translation asymmetry/energetic coherence; modern resource-theory literature makes this explicit.
- Energy--time and phase--number Renyi-entropic uncertainty relations are established (e.g. Hall 2022).

### Not yet located

A targeted search has not yet located the exact event-channel statement

`B_FI <= sqrt(F_Q)/(4 sqrt(3))`

or its marked-timestamp version, nor the use of this chain to diagnose the infinite quantum timing resource implicit in an exact movable timestamp branch.

Absence from this search is **not** priority certification.

## 7. Critical physical caveat

The relevant `F_Q` need not be a detector-internal resource. It can reside in:

- the incident temporal wavepacket / optical sidebands;
- a detector pointer state;
- a joint source--detector state;
- an external clock/reference.

Thus the theorem, as presently formulated, is a **source/readout quantum timing limit**, not a universal detector energy-cost law.

Paper 2's classical high-frequency Type-II residue does not automatically contradict this result. Taking modulation frequency to infinity in an ideal Poisson source can implicitly require unbounded source-side temporal/energy bandwidth.

## 8. Next gates

1. Locate the exact sharp GN/Fisher--Renyi theorem and cite the proper primary mathematical source rather than deriving novelty from it.
2. Make the finite-QFI/no-moving-atoms statement measure-theoretically rigorous using Hellinger fidelity/data processing.
3. Audit whether the exact `B_FI`--QFI inequality already appears in quantum timing/metrology literature.
4. Determine whether a physically useful stronger theorem emerges when the Hamiltonian is bounded below or mean energy is constrained.
5. Determine whether the bound can be lifted from an independent-event timing density to a trajectory-level spectral functional for memory-bearing measurement channels.
6. Do not claim a Nobel-scale result from WP02 alone. Its value is as a bridge and as a diagnostic for the missing quantum resource.
