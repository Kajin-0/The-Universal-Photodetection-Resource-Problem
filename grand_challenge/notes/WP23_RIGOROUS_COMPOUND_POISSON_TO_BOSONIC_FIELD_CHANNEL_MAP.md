# WP23 — Rigorous compound-Poisson to bosonic-field channel map

**Date:** 2026-08-22

## Status

**The principal WP13 source-to-field gate is closed for the independent-event source class.**

The correct construction does not require a universal abstract `symmetrization channel` from distinguishable particles to a common bosonic field. Instead, the independently labeled event register is used as an **upstream information extension**. Any particular physical source/emission apparatus whose parameter dependence is confined to those event marks defines a parameter-independent CPTP channel from that extension to the outgoing field. Pulling the detector measurement backward through that channel reduces the entire field/detector experiment to a POVM on the upstream event register, where WP20 applies exactly.

For temporal harmonic `k`, if one-event excitation-energy tail is

`T_k=sum_{m>=k}q_m`,

then an independent compound-Poisson source with mean event number `mu` obeys

`boxed: Tr F_final^(k) <= mu T_k`

for **any** parameter-independent source-to-field dynamics and any subsequent detector, coherent memory, ancilla, adaptive processing, and final measurement.

Since the latent Poisson source-label Fisher trace for the cosine/sine pair is `mu`, the source-normalized final retention obeys

`boxed: R_final(k)<=T_k`.

Thus bosonic wavepacket overlap and loss of event labels cannot evade the operational survival-function resource law.

---

## 1. One-event encoded state

Let `H_e` be the Hilbert space of one physical excitation/mark, including any internal degrees of freedom required to describe a fixed pulse or emitted excitation.

For the periodic random-time model, let

`rho_epsilon`

be the one-event density operator after averaging the fixed excitation over the latent event-time distribution with weak temporal Fourier perturbation `epsilon`.

At `epsilon=0`, write the total-generator sector probabilities as

`q_n=Tr(P_n rho0)`.

WP20 gives, for any POVM on any finite number `N` of independent copies,

`Tr F_N^(k)<=N T_k`,

where

`T_k=sum_{m>=k}q_m`.

This remains true for mixed one-event states by purification.

---

## 2. Compound-Poisson event register

Introduce the unsymmetrized event-register Hilbert space

`K_B = directsum_(N=0)^infinity H_e^tensor N`,

with `H_e^tensor0=C`.

This is sometimes called full/Boltzmann Fock space; here it is only a bookkeeping space for **labeled independent source events**, not the physical optical Fock space.

Let the event number be Poisson with mean `mu`, independent of the zero-mean temporal Fourier perturbation:

`p_mu(N)=exp(-mu)mu^N/N!`.

Define the compound source state

`Sigma_epsilon = directsum_N p_mu(N) rho_epsilon^tensor N`.

The direct-sum blocks are orthogonal and the Poisson weights are parameter independent.

The assumption that `mu` is parameter independent is exactly the statement that the Fourier perturbation redistributes event times over the period without changing the integrated event count. A DC/count-rate parameter is a different statistical direction and is not covered by this normalization.

---

## 3. Direct Fisher bound before field formation

Take an arbitrary POVM on `K_B` and ask for its cosine/sine Fisher block at harmonic `k`.

Give the observer the event number `N` as additional classical side information. This can only increase Fisher information because forgetting `N` is a parameter-independent coarse graining.

Conditional on `N`, WP20 gives

`Tr F_(given N)^(k)<=N T_k`.

Because the block weights `p_mu(N)` are parameter independent, the Fisher information of the number-revealed direct-sum experiment is the probability-weighted sum of the conditional Fisher informations:

`Tr F_revealN^(k)`

`=sum_N p_mu(N) Tr F_N^(k)`

`<=sum_N p_mu(N) N T_k`

`=mu T_k`.

Therefore every POVM on the unlabeled compound state satisfies

`boxed: Tr F_Sigma^(k)<=mu T_k`.

No QFI additivity theorem is required.

---

## 4. Latent classical Poisson normalization

For a Poisson process over one period with intensity

`lambda_epsilon(t)=lambda0[1+epsilon_c cos(k omega0 t)+epsilon_s sin(k omega0 t)]`,

the integrated mean event count is `mu=lambda0 T`, independent of the nonzero harmonic parameters.

At the uniform baseline,

`F_in,cc=F_in,ss=mu/2`,

and the cross term vanishes. Hence

`Tr F_in^(k)=mu`.

Define source-normalized full two-quadrature operational retention by

`R_final(k)=Tr F_final^(k)/mu`.

The compound-event theorem therefore reads

`boxed: R_final(k)<=T_k`.

The same normalization used in WP19/WP20 is recovered exactly.

---

## 5. Physical outgoing field as a parameter-independent channel

Let `F_s(h)` denote the physical bosonic Fock space of the outgoing optical/radiative modes of interest.

A particular source apparatus, with a fixed initial environment/apparatus state and fixed dynamics after the random-time marks have been encoded, defines a CPTP map

`Gamma: T(K_B) -> T(F_s(h) tensor H_aux)`.

`H_aux` may contain any retained source, matter, environment, polarization, spatial, frequency, or ancillary degrees of freedom that are made available downstream.

The physical field state is

`tau_epsilon = Gamma(Sigma_epsilon)`.

The map `Gamma` may represent, without changing the proof:

- emission of the labeled excitations into a common bosonic field;
- temporal/spatial wavepacket overlap;
- bosonic interference;
- mode mixing;
- loss;
- passive or active parameter-independent optical processing;
- nonlinear but CPTP source-field dynamics;
- retention or discarding of source/apparatus degrees of freedom.

No explicit canonical symmetrizer is required. The theorem is conditional only on the physical process being a fixed quantum channel once the event-time parameter is encoded upstream.

---

## 6. Pullback of an arbitrary detector measurement

Let the entire downstream detector—including coherent quantum memory, arbitrary ancillas in parameter-independent states, adaptive controls that do not themselves depend on the unknown parameter, and the final classical readout—be represented by a POVM `M(dy)` on the output of `Gamma` (equivalently absorb all detector dynamics into a single final POVM by the Heisenberg picture).

The induced outcome law is

`p_epsilon(dy)=Tr[Gamma(Sigma_epsilon) M(dy)]`.

Using the adjoint channel,

`p_epsilon(dy)=Tr[Sigma_epsilon Gamma^*(M(dy))]`.

Because `Gamma` is CPTP, `Gamma^*` is unital completely positive, so

`M_tilde(dy)=Gamma^*(M(dy))`

is a valid POVM on the compound event register.

Therefore every final field/detector statistical experiment is exactly a POVM experiment on `Sigma_epsilon`.

WP20 plus the compound-Poisson averaging then gives immediately

`boxed: Tr F_final^(k)<=mu T_k`.

This is a direct classical-Fisher statement; no intermediate use of QFI monotonicity is needed.

---

## 7. Why wavepacket overlap cannot help

When two or more emitted wavepackets overlap in the same bosonic modes, event labels may become physically inaccessible and multiphoton amplitudes may interfere.

Within the present source class this occurs **after** the independently encoded event register has been formed. It is therefore part of `Gamma`.

The final detector could even be granted every output degree of freedom produced by `Gamma`; its measurement is still a pulled-back POVM on the upstream register. Hence overlap cannot increase the accessible temporal-harmonic Fisher trace beyond `mu T_k`.

This statement is stronger and cleaner than saying merely that `QFI cannot increase`: it applies directly to the operational WP20 tail bound.

---

## 8. Stinespring realization

Any physical CPTP map `Gamma` has a Stinespring form

`Gamma(Sigma)=Tr_E[U (Sigma tensor sigma_A) U^dagger]`

for a fixed apparatus/environment state `sigma_A` and parameter-independent isometry/unitary `U` after enlarging the environment if necessary.

Thus the assumption behind the pullback is simply:

> the unknown temporal waveform parameter enters through the independent event-time encoding `Sigma_epsilon`, while the subsequent source/emission/detector hardware is fixed.

If a pump, local oscillator, feedback controller, or source Hamiltonian is itself modulated synchronously by the unknown waveform, that additional parameter-dependent resource lies outside `Gamma` and must be included in the source encoding. This is exactly the WP14 control/action boundary.

---

## 9. Continuous-time/continuum version

Apply WP22 to the one-event excitation spectral probability measure `mu_E(domega)` with survival function

`S_E(nu)=mu_E([nu,infinity))`.

For periodic approximants, the compound-Poisson field theorem gives

`R_final,delta(k)<=T_k^(delta)`.

Any controlled continuum limit therefore obeys

`boxed: R_final(nu)<=S_E(nu)`.

Consequently

`boxed: int_0^infinity R_final(nu)dnu <= omega_bar`,

and two-sided

`boxed: int_R R_final(nu)dnu <=2Ebar_event^+/hbar`.

The total mean excess energy over a window is `mu Ebar_event^+`; the total latent Poisson Fisher trace is `mu`, so the source-normalized law is independent of flux.

The pointwise inverse law is

`boxed: Ebar_event^+ >= hbar nu R_final(nu)`.

---

## 10. Scope: what counts as an independent event source

The theorem applies when all parameter dependence can be generated as follows:

1. draw a classical event number from a parameter-independent Poisson law for nonzero Fourier modes;
2. independently encode each event by the same random-time quantum statistical model;
3. pass the resulting compound event register through fixed quantum dynamics into the field and detector.

Examples may include spontaneous or incoherent emissions that are appropriately represented as independent marked events, provided the microscopic derivation actually supports this factorization.

The theorem does **not** follow merely from observing Poisson photocount statistics at one detector.

---

## 11. Explicit exclusions

The construction does not cover, without further work:

- phase-coherent laser/coherent states whose amplitude waveform is encoded directly in the field;
- squeezed or other indefinite-number sources with parameter-dependent inter-number coherences not generated by independent random event marks;
- correlated emission processes where event times/quantum marks are not independent conditional on the waveform;
- parameter-dependent source-to-field couplings, pumps, local oscillators, or control fields;
- feedback that changes the encoding map as a function of the unknown parameter rather than only processing already encoded outputs.

These are not counterexamples; they are different source resource classes.

---

## 12. Relation to WP14

WP14 showed that arbitrary state-valued waveform synthesis cannot be bounded by baseline mean energy alone because an external/control encoding map can create high-frequency first-order tangents at second-order energy cost.

WP23 makes the corresponding positive assumption explicit:

- random temporal information is encoded in the independent event marks first;
- all later field formation and detection is parameter independent.

Thus the theorem is not circular. The resource boundary is the point at which parameter dependence enters the physical state.

---

## 13. Prior-art boundary

The following ingredients are standard:

- compound Poisson/direct-sum constructions;
- tensor-product independent quantum experiments;
- Fisher information data processing;
- Heisenberg pullback of POVMs through CPTP maps;
- Stinespring dilation;
- bosonic Fock-space field descriptions.

Do not claim novelty for these ingredients.

The candidate contribution is their combination with the WP20 semibounded random-time survival theorem to obtain a source-to-final-record photodetection statement that remains valid after arbitrary bosonic field formation and coherent detector memory.

No exact predecessor of this combined operational theorem has been located; priority remains unverified.

---

## 14. Decision

WP13's informal bosonic-field argument is repaired.

Publication-grade scope statement:

> For an independent quantum-marked Poisson source whose waveform parameter enters only through the event-time distribution of fixed semibounded-energy excitations, every subsequent parameter-independent source-to-field and detector process is a quantum channel. Pulling the final measurement back to the compound event register and applying the finite-copy survival theorem gives `R_final(nu)<=P(Omega>=nu)` and therefore `int R_final<=2Ebar_event^+/hbar`, regardless of bosonic wavepacket overlap or coherent detector memory.

The major remaining tasks are now:

1. integrated hostile review of WP20--WP23;
2. one final deep priority audit centered on the exact survival theorem and source-to-record interpretation;
3. if both survive, form the standalone foundational manuscript.