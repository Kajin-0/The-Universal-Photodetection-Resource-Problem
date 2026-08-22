# Current Research State

**Last synchronized:** 2026-08-22

**Active scientific branch:** `agent/temporal-information-resource-law`

Paper 1 Rev11 and Paper 2 Rev7 are frozen. The Grand Challenge is active through **WP24**.

## Read first

1. `grand_challenge/AGENTS.md`
2. `grand_challenge/notes/WP24_INTEGRATED_HOSTILE_REVIEW_AND_SYMMETRY_PRIOR_ART_BOUNDARY.md`
3. `grand_challenge/notes/WP23_RIGOROUS_COMPOUND_POISSON_TO_BOSONIC_FIELD_CHANNEL_MAP.md`
4. `grand_challenge/notes/WP22_CONTINUUM_LIMIT_RIGOR_FOR_OPERATIONAL_SURVIVAL_LAW.md`
5. `grand_challenge/notes/WP20_DIRECT_FINITE_COPY_PROOF_AND_HOSTILE_AUDIT_OF_WP19.md`
6. `grand_challenge/notes/WP21_TARGETED_PRIORITY_AUDIT_SURVIVAL_FUNCTION_LAW.md`
7. `grand_challenge/notes/WP14_COHERENT_FIELD_BASELINE_ENERGY_NO_GO.md`

# Strongest theorem — operational survival law

For periodic random-time encoding of a fixed semibounded-energy excitation with sector probabilities `q_n`, define

`T_k=sum_(m>=k)q_m`.

For **any finite N and any joint POVM** on `N` independently encoded excitations,

`boxed: Tr F_N^(k)<=N T_k`.

Thus

`boxed: R_N(k)=Tr F_N^(k)/N<=T_k`,

and

`boxed: sum_(k>=1)R_N(k)<=nbar`.

A support-sensitive refinement is

`boxed: R_N(k)<=min(D_k,U_k)<=T_k`,

where `D_k` and `U_k` are the paired domain/range population masses separated by `k`.

WP20 provides a direct finite-copy Hilbert--Schmidt Cauchy--Schwarz proof, including arbitrary entangled collective measurements. The original Holevo route of WP19 is superseded.

# Continuum — WP22

For a positive excitation-frequency spectral probability measure `mu` with finite mean

`omega_bar=int omega mu(domega)`,

exact lower-bin periodic approximants give the pointwise continuum ceiling

`boxed: R(nu)<=mu([nu,infinity))=P(Omega>=nu)`.

Therefore

`boxed: int_0^infinity R(nu)dnu<=omega_bar`,

and two-sided

`boxed: int_R R(nu)dnu<=2Ebar^+/hbar`.

Pointwise,

`boxed: Ebar^+>=hbar nu R(nu)=h f R(2pi f)`.

So retention `q0` at ordinary frequency `B` requires

`boxed: Ebar^+>=hBq0`.

The theorem does not require a smooth density and handles atomic/singular spectral measures through the periodic approximation formulation.

# Equality family

For

`q_n=(1-r)r^n`,

the canonical phase POVM satisfies

`R(k)=r^k=T_k`

for every harmonic simultaneously, hence saturates the full sum rule.

The continuum limit is the exponential excitation spectrum / Cauchy timestamp family

`R(nu)=exp(-beta|nu|)`.

Thus the operational coefficient `2E/hbar` is exact and attainable.

# Independent Poisson event source to physical field — WP23

For a compound-Poisson source of independent quantum-marked events, revealing event number gives

`Tr F^(k)<=mu T_k`.

Any subsequent source/emission/field/detector process that is parameter independent after the event-time encoding is a CPTP map. Pulling the final POVM back through that map proves the same source-normalized tail law after arbitrary bosonic overlap, mode mixing, coherent detector memory, ancillas, and final readout.

This is an explicit source class; Poisson detector counts alone do not imply the theorem's assumptions.

# Secondary QFI envelope

WP10/WP12/WP15 remain mathematically correct:

`sum_(k>=1)G_Q(k)<=2nbar`,

`int_R G_Q(nu)dnu<=pi Ebar^+/hbar`.

They are separately optimized SLD-QFI envelopes, not the main jointly attainable detector theorem. WP16 identifies the sharp `pi/4` continuum operator norm as classical Hardy--Hilbert mathematics.

# Prior-art boundary

WP21/WP24 substantially narrow novelty.

Marvian--Spekkens, Phys. Rev. A 90, 062110 (2014), already establish `U(1)` gap-mode decomposition and weighted twirling

`sigma^(k)=p_(-k)rho^(k)`.

Phase estimation under energy/photon-number constraints, canonical phase measurements, arbitrary collective Fisher/Holevo bounds, random-unitary probability estimation, QFI/asymmetry, and the mathematical inequalities used in earlier WPs are also established.

The candidate contribution is specifically the **operational Fisher ceiling for Fourier perturbations of the random-time mixing distribution**, its population-tail evaluation, sharp all-mode mean-energy law, and source-to-record photodetection consequence.

Targeted searches have not located the exact tail/survival theorem. **Priority remains unverified, not certified.**

# Scope boundary

WP14 remains mandatory: baseline mean energy cannot bound arbitrary parameter-dependent coherent waveform synthesis. The theorem applies when temporal parameters enter through the random event-time distribution of a fixed excitation and all later processing is parameter independent.

# Publication gate

WP24 integrated hostile review: **PASS**, after repairing the support-gap notation and narrowing prior-art claims.

The former scientific gates are addressed:

1. arbitrary collective readout — WP20;
2. continuum limit — WP22;
3. independent event-to-bosonic-field map — WP23.

The project has reached a reasonable standalone manuscript-formation threshold with conservative novelty language.

## Immediate next action

1. complete repository synchronization through WP24;
2. create a standalone manuscript architecture centered on the operational survival theorem;
3. continue one final focused historical search during drafting;
4. retain WP14's source-class boundary and keep the `pi` QFI envelope secondary.

## Documentation rule

Every material result must update the detailed WP note, active handoff/landing documents, and `main`. The repository, not chat history, is authoritative.