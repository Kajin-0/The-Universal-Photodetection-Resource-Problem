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

> For a physically realizable measurement of temporal structure, what fundamental resources constrain source-to-record temporal Fisher-information transfer?

Paper 2 supplies the classical autonomous-channel Fisher spectrum. The grand-challenge program asks what stricter limits follow from quantum/physical realizability.

## Read first — authoritative order

1. `grand_challenge/notes/WP10_QUANTUM_RANDOM_TIME_MODE_BUDGET.md`
2. `grand_challenge/notes/WP09_EXTERNAL_TIME_REFERENCE_NO_GO_AND_ASYMMETRY_BOUNDARY.md`
3. `grand_challenge/notes/WP08_ARBITRARY_MEMORY_LIFT_AND_QUANTUM_REGULARIZATION.md`
4. `grand_challenge/notes/WP07_ENERGY_EDGE_AND_COVARIANT_POVM_PROOF_REPAIR.md`
5. `grand_challenge/notes/WP06_POSITIVE_ENERGY_TEMPORAL_FISHER_AREA_LAW.md`
6. `grand_challenge/notes/WP05_OPERATIONAL_CLOSURE_AND_LOCAL_LANDAUER_BASELINE.md`
7. `grand_challenge/notes/WP04_QUANTUM_WAVEFORM_PRIOR_ART_COLLISION.md`
8. `grand_challenge/notes/WP03_COVARIANT_TIMESTAMP_REGULARITY_AND_QFI_BOUND.md`
9. `grand_challenge/notes/WP02_QUANTUM_TIMING_BANDWIDTH_CANDIDATE.md`
10. `grand_challenge/notes/WP01_LANDSCAPE_AND_FIRST_NO_GOS.md`
11. `grand_challenge/README.md`

## Current strongest theorem candidate — WP10

### Random-time Fourier-mode encoding

Use a periodic time coordinate of period `T`, `omega0=2*pi/T`, and a nonnegative excitation ladder

`H=hbar*omega0*N`, `N=sum_{n>=0}nP_n`.

A latent event time `t` shifts a quantum excitation by `U_t=exp(-i omega0 N t)`. The uniform event-time prior is weakly modulated in cosine/sine mode `k`.

For a pure excitation with energy-sector populations `q_n`, the SLD QFI matrix for the two real quadratures is exactly

`F_Q^(k)=S_k I_2`,

`S_k=sum_n q_n q_{n+k}/(q_n+q_{n+k})`.

The latent classical event-time Fisher matrix is `(1/2)I_2`. Hence the maximal source-normalized quantum retention of mode `k` is

`boxed: G_Q(k)=2 sum_n q_n q_{n+k}/(q_n+q_{n+k})`.

It satisfies

`0<=G_Q(k)<=1`.

For mixed states with the same energy-sector probabilities, purification plus QFI monotonicity gives the same population expression as an upper bound.

### Sharp mode-sum / mean-energy law

Let

`nbar=sum_n n q_n`.

Then

`boxed: sum_{k>=1}G_Q(k)<=2 nbar`,

and, counting the even negative-frequency partners,

`boxed: sum_{k!=0}G_Q(k)<=4 nbar`.

The constant is sharp as a supremum: `q_0=1-epsilon`, `q_1=epsilon` gives ratio `->1` as `epsilon->0`.

If the first `K` positive modes all obey `G_Q(k)>=q`, then

`boxed: nbar>=Kq/2`.

With `B=K/T` and `Ebar=h nbar/T`,

`boxed: Ebar >= (h/2) B q`.

### Arbitrary quantum detector/memory inheritance

The modulation parameter is encoded in the quantum mixed state **before any detector is chosen**. Appending an arbitrary parameter-independent apparatus/reference state does not change QFI. Any joint quantum channel, coherent memory, amplification, saturation, feedback internal to the parameter-independent channel, and final measurement are downstream of QFI.

Therefore for every final classical record `Y`, mode by mode,

`boxed: G_Y(k)<=G_Q(k)`.

Thus the mean-energy mode-sum law survives arbitrary subsequent quantum detector processing. No timestamp-first/classical-memory factorization is required.

This is the current highest-ceiling result.

### Why WP09 does not defeat WP10

WP09 shows fixed mean energy does not bound QFI for a **deterministic global time shift** if a high-energy tail and an external phase reference are allowed.

WP10 estimates Fourier amplitudes of a **random latent event-time distribution**. Uniform baseline randomization twirls the quantum state. Rare high-energy tails contribute only through overlap/harmonic-mean terms with other occupied sectors, yielding the finite linear mean-energy mode budget. An external phase reference may help attain QFI but cannot create additional parameter information beyond the encoded-state QFI.

## Earlier theorem stack — WP06/WP07/WP08

For a reference-free covariant continuous timestamp readout with detected excess energy above the participating lower spectral edge `E_*`, WP06/WP07 prove the sharp area law

`boxed: int G_timestamp(nu)dnu <= 2E_det^+/hbar`,

or

`boxed: eta B_FI<=E_det^+/h`,

with flat-band inverse law

`boxed: E_det^+>=hBq`.

The sharp equality family is a one-pole positive-frequency Hardy amplitude / Cauchy timestamp density.

WP08 proves this bound is inherited by arbitrary **downstream classical detector memory** at arbitrary flux through Fisher-operator data processing. It also implies that Paper 2's ideal deterministic Type-II `1/e` infinite-frequency plateau must eventually be quantum-regularized after a finite-energy physical timing layer.

WP10 is broader in detector scope but currently rigorous only for the periodic random-time encoding model.

## WP09 boundary — external time reference

Fixed mean energy alone cannot bound arbitrary deterministic time-shift QFI. The family

`|psi_epsilon>=sqrt(1-epsilon)|0>+sqrt(epsilon)|Ebar/epsilon>`

has fixed mean `Ebar` but time-shift QFI diverging as `1/epsilon`.

This identifies time-translation asymmetry/external clock reference as the missing resource for unrestricted deterministic-shift metrology. Do not claim the WP06 timestamp bound for arbitrary noncovariant measurements.

## Major prior-art boundaries

Do not claim novelty for:

- Fisher/QFI data processing;
- standard SLD QFI harmonic-mean denominators;
- U(1)/time-translation mode decomposition;
- mode preservation under covariant processing;
- generic waveform QFI kernels/spectral QCRBs;
- covariant time POVMs / Naimark dilation;
- time-translation asymmetry as a resource;
- sharp Hardy/Gagliardo--Nirenberg inequality;
- generic time-energy uncertainty relations;
- generic FI-vs-dissipation/activity bounds;
- thermodynamic channel work costs;
- Poisson displacement/thinning/marking.

Important close sources:

- Marvian & Spekkens, PRA 90, 062110 (2014), modes of asymmetry;
- Lostaglio et al., PRX 5, 021001 (2015), quantum coherence/asymmetry under thermodynamic symmetries;
- Tsang, Wiseman, Caves, PRL 106, 090401 (2011), waveform QFI kernel;
- Pocovnicu, Analysis & PDE 4, 379--404 (2011), sharp positive-frequency inequality;
- Kiukas--Ruschhaupt--Werner arrival-time/covariant POVM work;
- Hall, Entropy 24, 1679 (2022), mean-resource/Renyi Heisenberg bounds;
- WAY/resource-theory asymmetry literature noted in WP09.

Targeted searches have **not yet located** the exact WP10 formula

`G_Q(k)=2 sum_n q_nq_{n+k}/(q_n+q_{n+k})`

as a random-time waveform-retention law, nor the sharp summed theorem

`sum_{k>=1}G_Q(k)<=2nbar`

or inverse `Ebar>=(h/2)Bq`. Priority is not certified.

## Immediate hostile gates

1. Independently audit every factor of two in WP10, including cosine/sine QFIM and source-FI normalization.
2. Deep-search asymmetry, phase-diffusion, random-unitary-channel and reference-frame literature for the exact mode-QFI/mode-sum theorem.
3. Prove the mixed-state bound publication-grade, including degenerate energy sectors and QFIM monotonicity.
4. Distinguish SLD-QFIM upper bounds from simultaneous attainability of cosine/sine quadratures.
5. Prove a controlled periodic-to-continuum limit. Candidate continuum form:
   `G_Q(nu)=2 int_0^infinity q(w)q(w+nu)/(q(w)+q(w+nu)) dw`,
   with `int_R G_Q<=4 Ebar^+/hbar`.
6. Map the independent quantum-marked Poisson extension onto physically relevant second-quantized optical fields; do not assume distinguishable-event tensor factors cover every overlapping bosonic state.
7. Determine whether the factor-of-two gap between arbitrary-measurement WP10 and covariant-timestamp WP07 is fundamental and operationally saturable.
8. Only after these gates decide whether a standalone manuscript is justified.

## Documentation rule

After every material theorem, counterexample, proof repair, prior-art collision, numerical result, or strategy change:

1. update/create `grand_challenge/notes/WP*.md` immediately;
2. update this file when the active theorem/gates change;
3. do not rely on chat history as the only record.
