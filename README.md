# The Universal Photodetection Resource Problem

**Current status: 2026-08-22**

`main` is the repository landing/index branch. Detailed derivations live on `agent/temporal-information-resource-law`.

## Project split

1. **Paper 1 / Rev11** — frozen and technically validated.
2. **Paper 2 / Rev7** — frozen preferred science draft.
3. **Grand Challenge** — ACTIVE on `agent/temporal-information-resource-law`; latest checkpoint **WP24**.

Authoritative active handoff: `grand_challenge/AGENTS.md` on the active branch.

# Strongest current theorem

For random temporal-distribution encoding of a fixed semibounded-energy excitation with periodic total-generator sector probabilities `q_n`, define

`T_k=sum_(m>=k)q_m`.

For **any finite number N of independently encoded excitations and any joint POVM**, including arbitrary entangled collective measurements,

`boxed: Tr F_N^(k)<=N T_k`.

Therefore

`boxed: R_N(k)=Tr F_N^(k)/N<=T_k`,

and

`boxed: sum_(k>=1)R_N(k)<=nbar`.

The active branch WP20 gives a direct finite-copy Cauchy--Schwarz proof. A support-sensitive refinement is

`R_N(k)<=min(D_k,U_k)<=T_k`.

## Continuum

For a general positive excitation-frequency spectral probability measure `mu` with finite mean,

`boxed: R(nu)<=mu([nu,infinity))=P(Omega>=nu)`.

Hence

`boxed: int_R R(nu)dnu<=2Ebar^+/hbar`,

and pointwise

`boxed: Ebar^+>=hbar nu R(nu)=h f R(2pi f)`.

Retention `q0` at ordinary frequency `B` therefore requires

`boxed: Ebar^+>=hBq0`.

The geometric sector / exponential continuum canonical phase-time family attains the bound exactly.

# Physical source-to-record scope

WP23 proves the same normalized law for an independent quantum-marked compound-Poisson source followed by arbitrary parameter-independent source-to-bosonic-field formation, wavepacket overlap, coherent detector memory, ancillas, and final measurement. The final POVM pulls back through the CPTP field/detector channel to the upstream event register.

This is an independent-event source theorem, not a theorem for every field with Poisson photocount statistics.

# Secondary QFI envelope

WP10/WP12/WP15 remain correct as separately optimized modewise SLD-QFI bounds:

`sum_(k>=1)G_Q(k)<=2nbar`,

`int_R G_Q(nu)dnu<=pi Ebar^+/hbar`.

They are now secondary to the sharp jointly operational `2E/hbar` law. WP16 records that the `pi/4` continuum operator norm is established Hardy--Hilbert mathematics.

# Scope boundary

WP14 proves baseline mean energy does not constrain arbitrary parameter-dependent coherent waveform synthesis. The positive theorem requires random-time distribution encoding of a fixed excitation with parameter-independent downstream processing.

# Prior-art boundary

Marvian--Spekkens, Phys. Rev. A **90**, 062110 (2014), already establish `U(1)` energy-gap modes and weighted twirling `sigma^(k)=p_(-k)rho^(k)`. Canonical phase measurements, photon-number-constrained phase estimation, arbitrary collective Fisher/Holevo bounds, random-unitary estimation, and asymmetry resource theory are also prior art.

The candidate contribution is narrowly the arbitrary-measurement **Fisher** ceiling for Fourier perturbations of the latent random-time mixing distribution, its population-tail/mean-energy law, and source-to-record photodetection consequence.

Targeted searches have not located the exact tail/survival theorem. **Priority remains unverified, not certified.**

# Current gate

WP24 integrated hostile review: **PASS**, after support-gap repair and prior-art narrowing.

The collective-measurement, continuum, and independent event-to-bosonic-field gates are addressed. The project has reached a reasonable standalone-manuscript formation threshold with conservative novelty language.

## Replacement-agent recovery

Switch to `agent/temporal-information-resource-law`, then read:

1. `grand_challenge/AGENTS.md`
2. `grand_challenge/notes/WP24_INTEGRATED_HOSTILE_REVIEW_AND_SYMMETRY_PRIOR_ART_BOUNDARY.md`
3. `grand_challenge/notes/WP23_RIGOROUS_COMPOUND_POISSON_TO_BOSONIC_FIELD_CHANNEL_MAP.md`
4. `grand_challenge/notes/WP22_CONTINUUM_LIMIT_RIGOR_FOR_OPERATIONAL_SURVIVAL_LAW.md`
5. `grand_challenge/notes/WP20_DIRECT_FINITE_COPY_PROOF_AND_HOSTILE_AUDIT_OF_WP19.md`
6. `docs/CURRENT_RESEARCH_STATE.md`
7. `ROADMAP.md`

## Documentation policy

`main` must always advertise the active branch and latest checkpoint. Detailed in-progress derivations may remain on the active branch, but project-level state must never again be hidden from the default view.