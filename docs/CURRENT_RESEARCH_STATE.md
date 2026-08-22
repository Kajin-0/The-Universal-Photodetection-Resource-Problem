# Current Research State

**Last synchronized:** 2026-08-22

**Default branch role:** landing/index only.

**Active scientific branch:** `agent/temporal-information-resource-law`

Paper 1 Rev11 and Paper 2 Rev7 are frozen. The Grand Challenge latest checkpoint is **WP24**.

## Replacement-agent recovery

Switch to `agent/temporal-information-resource-law`, then read:

1. `grand_challenge/AGENTS.md`
2. `grand_challenge/notes/WP24_INTEGRATED_HOSTILE_REVIEW_AND_SYMMETRY_PRIOR_ART_BOUNDARY.md`
3. `grand_challenge/notes/WP23_RIGOROUS_COMPOUND_POISSON_TO_BOSONIC_FIELD_CHANNEL_MAP.md`
4. `grand_challenge/notes/WP22_CONTINUUM_LIMIT_RIGOR_FOR_OPERATIONAL_SURVIVAL_LAW.md`
5. `grand_challenge/notes/WP20_DIRECT_FINITE_COPY_PROOF_AND_HOSTILE_AUDIT_OF_WP19.md`
6. `grand_challenge/notes/WP21_TARGETED_PRIORITY_AUDIT_SURVIVAL_FUNCTION_LAW.md`
7. active-branch `ROADMAP.md`.

Do not resume historical HgCdTe/Kane work unless a later theorem explicitly requires it.

# Strongest current theorem

For periodic random-time encoding of a fixed semibounded-energy excitation with sector probabilities `q_n`, define

`T_k=sum_(m>=k)q_m`.

For any finite number `N` of independently encoded excitations and **any joint POVM**,

`boxed: Tr F_N^(k)<=N T_k`.

Thus

`boxed: R_N(k)=Tr F_N^(k)/N<=T_k`,

and

`boxed: sum_(k>=1)R_N(k)<=nbar`.

A support-sensitive form is

`R_N(k)<=min(D_k,U_k)<=T_k`.

WP20 proves the result directly by Hilbert--Schmidt Cauchy--Schwarz for arbitrary finite-copy collective measurements.

# Continuum

For a positive excitation-frequency spectral probability measure `mu` with finite mean,

`boxed: R(nu)<=mu([nu,infinity))`.

Consequently

`boxed: int_R R(nu)dnu<=2Ebar^+/hbar`,

and

`boxed: Ebar^+>=hbar nu R(nu)=h f R(2pi f)`.

The geometric/exponential canonical phase-time family attains the bound exactly.

# Source-to-field scope

WP23 extends the same normalized theorem to an independent quantum-marked compound-Poisson event source followed by arbitrary parameter-independent physical source-to-bosonic-field dynamics, wavepacket overlap, coherent detector memory, ancillas, and final measurement.

This is not a theorem for every source with Poisson count statistics.

# Secondary QFI envelope

WP10/WP12/WP15 remain correct as separately optimized SLD-QFI bounds:

`sum_(k>=1)G_Q(k)<=2nbar`,

`int_R G_Q(nu)dnu<=pi Ebar^+/hbar`.

They are secondary to the sharp operational `2E/hbar` law. WP16 records the classical Hardy--Hilbert provenance of the `pi/4` analytic constant.

# Scope and prior-art boundaries

WP14 excludes arbitrary coherent waveform synthesis based only on baseline energy.

Marvian--Spekkens, Phys. Rev. A 90, 062110 (2014), already establish `U(1)` gap modes and weighted twirling `sigma^(k)=p_(-k)rho^(k)`. Canonical phase measurements, energy-constrained phase estimation, arbitrary collective Fisher/Holevo bounds, random-unitary estimation, and asymmetry resource theory are also prior art.

The candidate contribution is narrowly the **operational Fisher tail/survival law** for perturbations of the latent random-time mixing distribution and its sharp mean-energy/source-to-record consequences.

Targeted searches have not located an exact predecessor. **Priority remains unverified, not certified.**

# Publication status

WP24 integrated hostile review: **PASS** after support-gap repair, continuum hardening, explicit field embedding, and prior-art narrowing.

The project has reached a reasonable standalone-manuscript formation threshold.

## Immediate next action

Create a manuscript architecture centered on the operational survival-function theorem while continuing focused historical priority checking.

## Documentation requirement

Every project-level state change must be reflected both on the active branch and in these default-branch landing documents.