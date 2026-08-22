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

1. `grand_challenge/notes/WP08_ARBITRARY_MEMORY_LIFT_AND_QUANTUM_REGULARIZATION.md`
2. `grand_challenge/notes/WP07_ENERGY_EDGE_AND_COVARIANT_POVM_PROOF_REPAIR.md`
3. `grand_challenge/notes/WP06_POSITIVE_ENERGY_TEMPORAL_FISHER_AREA_LAW.md`
4. `grand_challenge/notes/WP05_OPERATIONAL_CLOSURE_AND_LOCAL_LANDAUER_BASELINE.md`
5. `grand_challenge/notes/WP04_QUANTUM_WAVEFORM_PRIOR_ART_COLLISION.md`
6. `grand_challenge/notes/WP03_COVARIANT_TIMESTAMP_REGULARITY_AND_QFI_BOUND.md`
7. `grand_challenge/notes/WP02_QUANTUM_TIMING_BANDWIDTH_CANDIDATE.md`
8. `grand_challenge/notes/WP01_LANDSCAPE_AND_FIRST_NO_GOS.md`
9. `grand_challenge/README.md`

## Current strongest theorem stack — WP06/WP07/WP08

### A. Gauge-invariant positive-energy event-time area law

Let a time-covariant event sub-POVM have total click effect `Q<=I` for a state `rho`. Let the detected energy measure have lower participating spectral edge `E_*`, event probability

`eta=Tr[rho Q]`,

and finite detected excess-energy moment

`E_det^+=Tr[rho Q(H-E_*)]`.

Under the absolutely-continuous-spectrum covariant-time hypotheses, the event timing distribution admits a positive-frequency vector Hardy amplitude. Pocovnicu's sharp positive-frequency Gagliardo--Nirenberg inequality then gives

`boxed: int_R G_primary(nu)dnu <= 2 E_det^+/hbar`.

Equivalent forms:

`boxed: eta B_FI <= E_det^+/h`,

and if `G_primary(2*pi*f)>=q` for all `|f|<=B`,

`boxed: E_det^+ >= h B q`.

The result is gauge invariant under `H -> H+cI` because `E_*` shifts with `H`.

### B. Sharpness

For an ideal covariant timestamp, the extremal family is a one-pole positive-frequency Hardy amplitude. Its conditional timestamp density is Cauchy,

`f_a(t)=a/[pi(t^2+a^2)]`,

with

`G(nu)=exp(-2a|nu|)`

for unit efficiency. It saturates

`int G = 2 E^+/hbar`

and

`B_FI=E^+/h`.

### C. General marks

The area law extends to arbitrary standard-Borel accessible marks by direct-integral disintegration and a fiberwise vector Hardy inequality. Mark resolution cannot evade the total detected excess-energy bound.

### D. Arbitrary downstream detector memory — WP08

Suppose the physical architecture factorizes as

`incident Poisson excitation centers -> independent covariant quantum timing/mark layer Z -> arbitrary parameter-independent autonomous classical memory channel K -> accessible record Y`.

Independent thinning/marking/displacement keeps `Z` Poisson at arbitrary incident flux. The primary Fisher multiplier is the exact event-timing multiplier `G_Z`.

Fisher data processing gives

`A_Y <= A_Z`.

Since both operators are translation invariant,

`boxed: G_Y(nu) <= G_Z(nu) a.e.`

Therefore

`boxed: int G_Y(nu)dnu <= 2 E_det^+/hbar`,

and the inverse flat-band law `E_det^+ >= hBq` survives **arbitrary downstream classical detector memory**, including dead time, saturation, afterpulsing, state-dependent capture, hidden state, nonlinear history dependence, and output coarse graining.

### E. Quantum regularization of Paper-2's classical plateau

Paper 2's ideal deterministic Type-II model has `G -> 1/e` at infinite frequency because mathematically exact latent point events are primitive. WP08 proves that this cannot be the literal infinite-frequency behavior after a finite-excess-energy covariant quantum timing layer:

`0<=G_final<=G_primary`,

and `G_primary(nu)->0` by Riemann--Lebesgue. Hence the physical final spectrum must eventually decay. The classical `1/e` plateau can survive only as an intermediate-frequency regime when the quantum timing scale is much faster than the dead-time scale.

This is the current most important bridge between Paper 2 and the grand-challenge program.

## Mandatory caution / current boundary

WP08 is **not** yet a theorem for arbitrary coherently intertwined quantum detector memory.

The source-only mean-energy bound can also fail if the measurement apparatus supplies a free external clock/time-translation-asymmetry resource. The positive-energy law is a covariant timing-readout theorem, not a bound on arbitrary noncovariant phase-referenced measurements.

A fully universal quantum-memory theorem would have to either:

1. assume global time-translation covariance with no free apparatus asymmetry; or
2. explicitly include apparatus clock/asymmetry resources in the budget.

## Previous routes closed or downgraded

### Entropy production / thermodynamic cost

Rejected as universal scalar resource. Information-acquisition rate is not generically bounded by entropy production; actual dissipation is implementation-dependent; thermodynamic channel capacity additionally depends on Hamiltonians/physical embedding. WP01/WP05 document the no-gos.

### Generic quantum waveform Fisher spectrum

Substantially preempted by Tsang--Wiseman--Caves (PRL 106, 090401, 2011) and later continuous quantum sensing. Do not claim novelty for a quantum waveform QFI kernel/spectrum. See WP04.

### QFI/energy-variance timestamp bound

WP03 remains valid/useful:

`B_FI <= sqrt(F_Q)/(4 sqrt(3)) <= Delta H/(2 sqrt(3) hbar)`.

But WP06--WP08's positive-mean-energy area law is the more distinctive frontier.

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
- finite-time Landauer bounds;
- Poisson displacement/thinning/marking.

Important close sources include:

- Pocovnicu, Analysis & PDE 4, 379--404 (2011), sharp `H_+^{1/2}` GN inequality;
- Kiukas--Ruschhaupt--Werner, covariant arrival-time/dilation work (2009--2013);
- Kiukas et al., J. Phys. A 45, 185301 (2012), exact energy-time uncertainty for absorptive arrival times;
- Tsang, Wiseman, Caves, PRL 106, 090401 (2011), waveform QCRB/QFI kernel;
- Hall, Entropy 24, 1679 (2022), strong Heisenberg/Renyi energy-time tradeoffs;
- Faist et al./Faist--Renner/Faist--Berta--Brandao, thermodynamic channel costs;
- Barato--Hartich--Seifert, PRE 87, 042104 (2013), no simple universal information-vs-dissipation law;
- recent response/activity/clock literature recorded in WP01/WP05.

Targeted searches have not yet located the exact source-to-record statements

`int G dnu <= 2 E_det^+/hbar`

or

`E_det^+ >= hBq`,

nor the WP08 arbitrary-downstream-memory inheritance theorem. **Priority is not certified.**

## Immediate hostile gates

1. **External-clock/no-covariance counterexample:** formalize a fixed-mean-energy family with unbounded time-shift QFI and show why it does not contradict the covariant area law.
2. **Global-covariance question:** determine whether a theorem can survive coherently intertwined quantum memory when the entire apparatus starts time-translation invariant and the full instrument is covariant.
3. **Deep prior-art audit:** search continuous-spectrum Rényi-2/collision-entropy time-energy inequalities and any equivalent integrated transfer-area formulation.
4. **Equality under multiplicity/inefficiency:** make the equality characterization theorem-grade.
5. **Low-energy-tail robustness:** study alternatives to the essential lower edge `E_*` when arbitrarily small low-energy tails make the exact theorem loose.
6. **Type-II crossover:** derive quantitative non-factorized bounds/crossover scales for a deterministic Type-II memory stage preceded by finite-energy timing blur.
7. Only after these decide whether WP06--WP08 justify a standalone manuscript.

## Documentation rule

After every material theorem, counterexample, proof repair, prior-art collision, numerical result used in an argument, or strategy change:

1. update/create `grand_challenge/notes/WP*.md` immediately;
2. update this file when the active theorem/gates change;
3. do not rely on chat history as the only record.
