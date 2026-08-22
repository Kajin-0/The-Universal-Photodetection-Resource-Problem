# WP09 — External time-reference no-go and the asymmetry boundary

**Date:** 2026-08-21

## Status

**Necessary no-go / scope theorem for WP06--WP08.**

A source-only mean-positive-energy bound cannot hold for arbitrary noncovariant, phase-referenced quantum measurements. The positive-energy Fisher-area law is therefore fundamentally a theorem for **time-covariant/reference-free timing readout** (and arbitrary downstream classical processing), not for every conceivable detector supplied with a free external clock.

The missing resource is time-translation asymmetry / energetic coherence of the apparatus or reference frame.

---

## 1. Fixed-mean-energy family with unbounded time-shift QFI

Let a source system have Hamiltonian with two relevant eigenstates

`H|0>=0`,

`H|E_epsilon>= (Ebar/epsilon)|E_epsilon>`.

For `0<epsilon<1`, define

`|psi_epsilon> = sqrt(1-epsilon)|0> + sqrt(epsilon)|E_epsilon>`.

The mean excitation energy is exactly fixed:

`<H> = epsilon*(Ebar/epsilon)=Ebar`.

For the time-shift family

`|psi_epsilon(theta)> = exp(-iH theta/hbar)|psi_epsilon>`,

the pure-state QFI is

`F_Q = 4 Var(H)/hbar^2`.

Now

`Var(H) = epsilon(1-epsilon)(Ebar/epsilon)^2`

`       = Ebar^2(1-epsilon)/epsilon`.

Therefore

`boxed: F_Q = [4 Ebar^2/hbar^2] (1-epsilon)/epsilon -> infinity`

as `epsilon->0`, while the mean excitation energy remains `Ebar`.

Hence **mean source energy alone cannot upper-bound arbitrary local time-shift Fisher information.**

This does not contradict WP06/WP07 because those theorems bound the spectral area of a covariant continuous time-output distribution, not the locally optimized FI of an arbitrary noncovariant measurement.

---

## 2. A phase-referenced measurement can access the divergent QFI

For a one-parameter pure-state unitary family, an SLD-optimal projective measurement at a chosen operating point `theta0` attains the QFI locally.

The required projectors involve coherent superpositions of distinct energy eigenspaces with a phase defined relative to `theta0`. Such a measurement is not a reference-free covariant time POVM on `R`; it selects an external temporal phase origin.

Operationally, an apparatus implementing this measurement must possess a clock/phase reference or another state that breaks time-translation symmetry.

Thus a free external reference can convert a sparse high-energy tail into arbitrarily large local time-shift sensitivity at fixed mean source energy.

---

## 3. Resource-theory interpretation

The resource theory of asymmetry identifies states invariant under time translations as free states and time-translation-covariant operations as free operations. States with energetic coherence provide the asymmetry needed to implement operations/measurements that select a temporal phase origin.

The WAY theorem/resource-theory formulation makes the same point in measurement language: conservation/symmetry restrictions constrain measurement of asymmetric observables unless the apparatus supplies an appropriate asymmetric resource.

Relevant established literature includes:

- Ahmadi, Jennings, Rudolph, *The WAY theorem and the quantum resource theory of asymmetry* (2013-era work; arXiv:1209.0921);
- operational resource-theory treatments of Wigner--Yanase/QFI-type asymmetry measures;
- later work establishing QFI/Fisher matrices as time-translation/Lie-group asymmetry monotones.

Therefore **do not claim novelty for identifying time-asymmetry as a resource**. The role of WP09 is to identify the exact physical boundary of the new temporal Fisher-area theorem.

---

## 4. Minimal covariance condition behind WP06--WP08

WP06/WP07 assume a time-covariant event observable:

`e^{iHs/hbar} F(A) e^{-iHs/hbar} = F(A-s)`.

This condition means the measurement has no privileged external origin of time. The output timestamp simply shifts when the source state is shifted.

Under this covariance and a semibounded participating energy spectrum, the output timing amplitude lies in a one-sided Hardy space and the sharp mean-energy area law follows.

WP09 shows covariance is not cosmetic: removing it admits counterexamples at fixed mean energy.

Accordingly the theorem should be described as a

> **reference-free covariant temporal-information resource law**

rather than an unrestricted energy-vs-Fisher theorem.

---

## 5. Consequence for arbitrary quantum-memory ambitions

A source-only extension to an arbitrary quantum detector with memory is impossible unless one excludes free apparatus time-asymmetry.

A viable fully quantum theorem must choose one of two formulations.

### Form A — globally covariant apparatus

Assume:

1. the detector/reference initial state is time-translation invariant with respect to its internal Hamiltonian;
2. system--apparatus dynamics are globally time-translation covariant / energy conserving in the relevant sense;
3. the final classical record transforms covariantly under time translation.

Then no external time-asymmetry resource is imported. It is plausible that a source-energy or total participating positive-energy area law can survive, but this is not yet proved for arbitrary memory-bearing instruments.

### Form B — explicit joint resource budget

Allow an asymmetric apparatus/reference state `sigma_A`, but include its time-translation resource explicitly. Candidate budgets could involve:

- apparatus QFI / skew information;
- asymmetry cost or coherence cost;
- spectral asymmetry rates;
- a direct positive-energy Hardy resource when the reference is itself a positive-frequency clock.

A universal theorem, if one exists, would then bound output temporal Fisher transfer by a **joint source + apparatus timing resource**.

No such final budget has been derived yet.

---

## 6. Why ordinary apparatus energy is insufficient

The relevant apparatus resource cannot be just mean energy or dissipation.

A high-energy stationary state commuting with its Hamiltonian carries no time-reference phase and cannot by itself implement a noncovariant timing measurement. Conversely, a comparatively modest coherent superposition can carry strong temporal asymmetry.

Thus the resource needed to close the noncovariant loophole is specifically **energy coherence/time-translation asymmetry**, not energy magnitude alone.

This is consistent with the earlier grand-challenge no-gos against entropy production, power, and scalar thermodynamic costs.

---

## 7. Relation to WP03 QFI bound

The family above has fixed mean energy but divergent variance/QFI. This explains why the WP03 bound

`B_FI <= sqrt(F_Q)/(4 sqrt(3))`

and the WP06 mean-energy area bound constrain different operational classes/aspects.

WP03 uses local time-shift QFI and does not require a covariant time-output distribution. WP06 exploits semibounded-energy analyticity of a covariant continuous timestamp and therefore controls an integrated spectral-area quantity by the mean positive energy.

Neither theorem subsumes the other without additional assumptions.

---

## 8. Decision

The external-clock counterexample **does not weaken WP06--WP08**; it sharpens their physical meaning.

Current strongest justified claim:

> For a reference-free covariant event-timing measurement with finite detected excess energy, the integrated temporal Fisher-transfer spectrum is sharply bounded by `2E_det^+/hbar`, and arbitrary subsequent autonomous classical detector memory inherits the same bound.

The next high-value gate is now precise:

> Does an analogous area law hold for a **globally time-translation-covariant quantum detector with coherently intertwined memory**, when the apparatus begins in a symmetric state and no external temporal reference is supplied?

That is the appropriate route toward a genuinely universal quantum-memory theorem.
