# AGENTS — Temporal Information Resource Law Program

## Purpose

Durable handoff for the high-risk/high-ceiling theoretical program launched from Paper 2. This program is deliberately separate from the frozen Paper-2 manuscript.

Active branch: `agent/temporal-information-resource-law`.

## Non-negotiable scope

- Analytical/theoretical research only.
- Numerical counterexample searches are allowed.
- Do not require experiments, fabrication, procurement, or laboratory optimization as active next steps.
- Paper 2 Rev7 remains frozen unless a concrete defect is found.
- Do not assume a Nobel-scale result exists. The program is falsification-first.

## Grand question

> For a physically realizable measurement of temporal structure, what fundamental resources constrain the source-to-record temporal Fisher-information transfer spectrum?

Paper 2 supplies the classical local observable

`F_out[u,v] = Phi0/(2*pi) int G(nu) U*(nu)V(nu) dnu`,

with `0 <= G <= 1` a.e. for parameter-independent autonomous classical Poisson detector channels.

The grand-challenge program asks what additional restrictions follow from physical realizability.

## Read first — current authoritative order

1. `grand_challenge/notes/WP06_POSITIVE_ENERGY_TEMPORAL_FISHER_AREA_LAW.md`
2. `grand_challenge/notes/WP05_OPERATIONAL_CLOSURE_AND_LOCAL_LANDAUER_BASELINE.md`
3. `grand_challenge/notes/WP04_QUANTUM_WAVEFORM_PRIOR_ART_COLLISION.md`
4. `grand_challenge/notes/WP03_COVARIANT_TIMESTAMP_REGULARITY_AND_QFI_BOUND.md`
5. `grand_challenge/notes/WP02_QUANTUM_TIMING_BANDWIDTH_CANDIDATE.md`
6. `grand_challenge/notes/WP01_LANDSCAPE_AND_FIRST_NO_GOS.md`
7. `grand_challenge/README.md`

## Current strongest theorem candidate — WP06

Let `Omega=(H-E0)/hbar >=0` generate an unknown time shift of a quantum excitation, and let a fixed covariant event-time sub-POVM have click effect

`Q=int M(dt)`, `0<=Q<=I`, `[Q,Omega]=0`.

For state `rho`, define

`eta=Tr[rho Q]`,

`omega_det=Tr[rho Q Omega]`,

`E_det=hbar omega_det`.

The covariant POVM admits a positive-frequency Hardy-space timing amplitude. Pocovnicu's sharp positive-frequency Gagliardo--Nirenberg inequality, extended to vector-valued multiplicity, gives

`int p(t)^2 dt <= eta omega_det/pi`.

For the corresponding event timing transfer spectrum

`G(nu)=eta |F(nu)|^2`,

this yields the sharp spectral-area candidate

`boxed: int_{R} G(nu)dnu <= 2 omega_det = 2 E_det/hbar`.

Therefore

`boxed: int G <= 2 E_exc/hbar`,

where `E_exc=Tr[rho(H-E0)]`.

In Paper-1 timing-bandwidth notation,

`boxed: eta B_FI <= E_det/h`.

If the click effect is energy independent, `Q=eta I`, then

`boxed: B_FI <= E_exc/h`.

If `G(2*pi*f)>=q` for all `|f|<=B`, then

`boxed: E_det >= h B q`.

The scalar ideal bound is sharp. Equality is attained by a one-pole Hardy amplitude, corresponding to a Cauchy timestamp density and exponential positive-energy spectrum:

`f_a(t)=a/[pi(t^2+a^2)]`,

`G_a(nu)=exp(-2a|nu|)` for `eta=1`.

### Mandatory caution

The sharp Hardy inequality and covariant time POVM machinery are prior art. Novelty, if any, is the **event-channel Fisher spectral-area interpretation, exact efficiency/detected-energy bookkeeping, and inverse information-bandwidth resource law**. Priority is not certified.

This is an end-to-end quantum timing resource theorem, not yet a detector-internal dissipation law.

## Previous routes closed or downgraded

### Entropy production / thermodynamic cost

Rejected as universal scalar resource. Information-acquisition rate is not generically bounded by entropy production; actual dissipation is implementation-dependent; thermodynamic channel capacity additionally depends on Hamiltonians/physical embedding. WP01/WP05 document the no-gos.

### Generic quantum waveform Fisher spectrum

Substantially preempted by Tsang--Wiseman--Caves (PRL 106, 090401, 2011) and later continuous quantum sensing. Do not claim novelty for a quantum waveform QFI kernel/spectrum. See WP04.

### QFI/energy-variance timestamp bound

WP03 remains valid/useful:

`B_FI <= sqrt(F_Q)/(4 sqrt(3)) <= Delta H/(2 sqrt(3) hbar)`.

But WP06's positive-energy mean-resource law is currently the more distinctive frontier.

### Information singularities

Remain a useful diagnostic, but generic static non-identifiability restored by dynamic excitation overlaps classical system-identification/persistent-excitation theory. Do not make this the lead grand theorem absent a stronger classification result.

## Decisive literature boundaries

Do not claim novelty for:

- Fisher data processing / QFI monotonicity;
- arbitrary waveform QFI kernels/spectral QCRBs;
- covariant time POVMs / Naimark dilation;
- QFI as time-translation asymmetry resource;
- sharp Gagliardo--Nirenberg/Hardy inequality itself;
- generic time-energy uncertainty relations;
- generic FI-vs-dissipation/dynamical-activity bounds;
- thermodynamic work cost of abstract quantum channels;
- finite-time Landauer bounds.

Important close sources include:

- Pocovnicu, Analysis & PDE 4, 379--404 (2011), sharp `H_+^{1/2}` GN inequality;
- Skulimowski, Phys. Lett. A 297, 129--136 (2002), covariant time POVMs;
- Tsang, Wiseman, Caves, PRL 106, 090401 (2011), waveform QCRB/QFI kernel;
- Hall, Entropy 24, 1679 (2022), strong Heisenberg/Renyi energy-time tradeoffs;
- Faist et al./Faist--Renner/Faist--Berta--Brandao, thermodynamic channel costs;
- Barato--Hartich--Seifert, PRE 87, 042104 (2013), no simple universal information-vs-dissipation law;
- recent response/activity/clock literature recorded in WP01/WP05.

## Immediate hostile gates for WP06

1. **Energy-origin audit:** determine precisely whether `E0` must be the global Hamiltonian lower edge, the lower edge of an invariant support subspace, or another gauge-invariant excitation reference. For optical wavepackets, distinguish carrier energy from temporal-envelope/sideband resource.
2. **Covariant POVM theorem:** write the intertwiner/direct-integral representation with theorem-grade hypotheses and prove the first-moment identity/bound `omega_det=Tr[rho Q Omega]`.
3. **Mixed states:** formalize purification without changing the energy moment.
4. **General marks:** extend finite/countable mark proof to general measurable mark spaces.
5. **Prior-art collision:** search specifically for a collision/Renyi-2 time-density bound of the form `int p(t)^2 <= <Omega>/pi` and its quantum timing interpretation.
6. **Sharpness:** verify physical attainability of the Cauchy timestamp/exponential positive-energy extremal and characterize equality under inefficiency/multiplicity.
7. **End-to-end normalization:** independently rederive `int G=4*pi*eta B_FI` and all Fourier/Planck constants.
8. **Memory extension:** only after gates 1--7, test whether a trajectory-level area law survives detector memory.

Do not draft a new paper or describe WP06 as Nobel-level until these gates are closed.

## Documentation rule

After every material theorem, counterexample, proof repair, prior-art collision, numerical result used in an argument, or strategy change:

1. update/create `grand_challenge/notes/WP*.md` immediately;
2. update this file when the active theorem/gates change;
3. do not rely on chat history as the only record.
