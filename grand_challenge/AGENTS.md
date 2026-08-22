# AGENTS — Temporal Information Resource Law Program

**Last synchronized: 2026-08-22**

Active branch: `agent/temporal-information-resource-law`.

Research is analytical/theoretical and falsification-first. Paper 1 Rev11 and Paper 2 Rev7 are frozen.

## Grand question

> For a physically realizable measurement of temporal structure, what fundamental resources constrain source-to-record temporal Fisher-information transfer?

## Read first

1. `grand_challenge/notes/WP24_INTEGRATED_HOSTILE_REVIEW_AND_SYMMETRY_PRIOR_ART_BOUNDARY.md`
2. `grand_challenge/notes/WP23_RIGOROUS_COMPOUND_POISSON_TO_BOSONIC_FIELD_CHANNEL_MAP.md`
3. `grand_challenge/notes/WP22_CONTINUUM_LIMIT_RIGOR_FOR_OPERATIONAL_SURVIVAL_LAW.md`
4. `grand_challenge/notes/WP21_TARGETED_PRIORITY_AUDIT_SURVIVAL_FUNCTION_LAW.md`
5. `grand_challenge/notes/WP20_DIRECT_FINITE_COPY_PROOF_AND_HOSTILE_AUDIT_OF_WP19.md`
6. `grand_challenge/notes/WP19_FULL_COLLECTIVE_SURVIVAL_FUNCTION_RESOURCE_LAW.md`
7. `grand_challenge/notes/WP16_DEEP_PRIORITY_AUDIT_RANDOM_TIME_QFI_AND_HARDY_HILBERT_COLLISION.md`
8. `grand_challenge/notes/WP15_GENERAL_DENSITY_PROOF_OF_SHARP_PI_AREA_INEQUALITY.md`
9. `grand_challenge/notes/WP14_COHERENT_FIELD_BASELINE_ENERGY_NO_GO.md`
10. `grand_challenge/notes/WP13_SECOND_QUANTIZED_SCOPE_AND_POISSON_EVENT_EMBEDDING.md`

WP17/WP18 are useful historical steps toward WP20 but are no longer needed for the strongest proof.

# Current strongest theorem — operational survival law

For a periodic semibounded excitation with total-generator sector probabilities `q_n`, define

`T_k=sum_(m>=k)q_m`.

For **any finite number N of independently random-time-encoded excitations and any joint POVM**, including arbitrary entangled collective measurements,

`boxed: Tr F_N^(k) <= N T_k`.

Here `F_N^(k)` is the `2 x 2` classical Fisher block for the cosine/sine amplitudes of temporal harmonic `k` at the uniform random-time baseline.

Therefore

`boxed: R_N(k):=Tr F_N^(k)/N <= T_k`,

and

`boxed: sum_(k>=1)R_N(k)<=nbar`.

WP20 gives a direct finite-copy Hilbert--Schmidt Cauchy--Schwarz proof. No covariance restriction on the detector, Holevo asymptotics, SLD attainability, or separable-measurement assumption is used.

## Bilateral support refinement

With the paired partial energy shift `V_k`, define

`D_k=Tr(rho P_dom,k)`,

`U_k=Tr(rho P_ran,k)`.

Then

`boxed: R_N(k)<=min(D_k,U_k)<=T_k`.

The coarse tail `T_k` is the universal semibounded-energy form; the paired-support form can be tighter for gaps or finite upper support.

# Continuum theorem — WP22

Let `mu` be the positive excitation-frequency spectral probability measure, with finite first moment

`omega_bar=int omega mu(domega)`.

Using exact lower-bin periodic approximants, every modewise continuum limit satisfies

`boxed: R(nu)<=S_mu(nu):=mu([nu,infinity))`.

Thus

`boxed: int_0^infinity R(nu)dnu<=omega_bar`,

and two-sided

`boxed: int_R R(nu)dnu<=2Ebar^+/hbar`.

The pointwise inverse law is

`boxed: Ebar^+>=hbar nu R(nu)=h f R(2pi f)`.

Hence a guaranteed retention `q0` at ordinary frequency `B` requires

`boxed: Ebar^+>=h B q0`.

No smooth spectral density is required. Atoms, singular-continuous components, and mixtures are allowed through the measure formulation.

# Exact equality family

For geometric sectors

`q_n=(1-r)r^n`,

the canonical phase POVM gives

`R(k)=r^k=T_k`

for **every harmonic simultaneously**, so

`sum_(k>=1)R(k)=nbar`.

Under `r=exp(-beta delta)`, the continuum limit is

`mu(domega)=beta exp(-beta omega)domega`,

`R(nu)=exp(-beta|nu|)=S_mu(|nu|)`.

With `beta=2a`, this is the Cauchy timestamp equality family from WP06/WP07. Therefore the operational coefficient `2E/hbar` is exactly attainable.

# Independent Poisson source to physical bosonic field — WP23

For a compound-Poisson source with mean event count `mu`, represent the independently encoded event marks on the direct-sum event register

`Sigma_epsilon=directsum_N p_mu(N) rho_epsilon^tensor N`.

For nonzero temporal Fourier modes, the Poisson number weights are parameter independent. Revealing `N` can only increase FI, so WP20 gives

`boxed: Tr F_compound^(k)<=mu T_k`.

Any physical source-to-field/emission process whose parameter dependence is already encoded in those event marks is a parameter-independent CPTP map `Gamma` from the upstream event register to the outgoing bosonic field and other downstream degrees of freedom.

Pulling the final detector POVM backward through `Gamma` gives a POVM on the event register. Therefore arbitrary bosonic wavepacket overlap, mode mixing, coherent detector memory, ancillas, and final measurement cannot evade

`boxed: R_final(k)<=T_k`

or the continuum survival law.

This does **not** follow merely from Poisson photocount statistics; it is a theorem for an independent quantum-marked event source class.

# Secondary theorem — separately optimized QFI envelope

WP10/WP12/WP15 remain mathematically correct:

`G_Q(k)=2 sum_n q_nq_(n+k)/(q_n+q_(n+k))`,

`sum_(k>=1)G_Q(k)<=2nbar`,

and

`int_R G_Q(nu)dnu<=pi Ebar^+/hbar`.

But this is a separately optimized SLD-QFI envelope, not the headline operational theorem. WP20 proves that one actual detector, even with arbitrary finite-copy collective readout, obeys the smaller sharp operational coefficient `2E/hbar`.

WP16 establishes that the `pi/4` Mellin/operator constant in the continuum QFI proof is classical Hardy--Hilbert mathematics.

# Scope boundary — WP14

The operational survival theorem concerns **random temporal-distribution encoding of a fixed semibounded-energy excitation**.

Baseline mean energy does not constrain arbitrary parameter-dependent coherent waveform synthesis. WP14 constructs a high-frequency coherent-sideband counterexample. A broader state-valued waveform theorem requires explicit encoding/control/action resource accounting.

# Prior-art boundary — strengthened by WP21/WP24

Do not claim novelty for:

- `U(1)` energy-gap/modes-of-asymmetry decompositions;
- weighted random phase/time twirling multiplying gap modes by Fourier coefficients;
- canonical phase POVMs or exponential phase moments;
- phase/time estimation under photon-number/energy constraints;
- generic arbitrary-measurement Fisher/Holevo/RLD/SLD bounds;
- random-unitary probability estimation;
- QFI/asymmetry resource theory;
- Hardy--Hilbert/Mellin/rearrangement methods;
- compound Poisson models, Stinespring dilation, or CPTP data processing.

Especially close is Marvian--Spekkens, Phys. Rev. A 90, 062110 (2014): for weighted `U(1)` twirling they already show `sigma^(k)=p_(-k)rho^(k)` and develop modewise asymmetry monotones.

The candidate contribution is narrower:

> the arbitrary-measurement Fisher ceiling for perturbations of the latent random-time distribution, whose `k`-mode resource evaluates to a paired population mass and hence to the semibounded survival tail, with sharp mean-energy and source-to-record photodetection consequences.

Targeted searches have not found an exact predecessor of

`Tr F_N^(k)/N <= sum_(m>=k)q_m`,

its all-mode mean-generator sum rule, or

`R(nu)<=P(Omega>=nu)`.

**Priority remains unverified, not certified.**

# Current publication status

WP24 integrated hostile review: **PASS**, after the support-gap repair and narrowed prior-art language.

The former scientific blockers are now addressed:

1. collective/joint-measurement attainability — closed by WP20;
2. continuum rigor — closed at the periodic-approximation level by WP22;
3. independent event-to-bosonic-field mapping — closed by WP23.

The remaining external-risk gate is historical priority.

## Immediate work order

1. synchronize all landing documents through WP24 and mirror `main`;
2. create a standalone manuscript architecture centered on the operational survival-function theorem;
3. perform one final focused historical search while drafting, especially number-phase, group-distribution inference, and asymmetry-mode literature;
4. keep the `pi` QFI envelope secondary and the WP14 scope boundary explicit.

## Documentation rule

Every material result must be recorded in a WP note, reflected in active landing/handoff files, and mirrored onto `main`. The repository—not chat history—must remain sufficient for full recovery.