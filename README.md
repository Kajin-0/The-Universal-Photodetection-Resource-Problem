# The Universal Photodetection Resource Problem

**Status synchronized: 2026-08-22**

## Project split

1. **Paper 1 / Rev11** — frozen and technically validated.
2. **Paper 2 / Rev7** — frozen preferred science draft.
3. **Grand Challenge** — science checkpoint **WP24**; preferred manuscript **Rev4**, locally build-verified and frozen unless a concrete defect appears.

Active Grand Challenge branch: `agent/temporal-information-resource-law`.

Authoritative handoff: `grand_challenge/AGENTS.md`.

# Strongest current result — operational survival-function law

For periodic random-time encoding of a fixed excitation with total-generator sector probabilities `q_n`, define

`T_k=sum_(m>=k)q_m`.

For **any finite number N of independent encoded excitations and any joint POVM**, including arbitrary entangled collective measurements,

`Tr F_N^(k) <= N T_k`.

Thus the per-event two-quadrature / phase-averaged temporal-mode retention obeys

`R_N(k)=Tr F_N^(k)/N<=T_k`,

and

`sum_(k>=1)R_N(k)<=nbar`.

A support-sensitive refinement is

`R_N(k)<=min(D_k,U_k)<=T_k`.

WP20 proves this directly by Hilbert--Schmidt Cauchy--Schwarz; no detector covariance, separability, Holevo asymptotics, or SLD attainability assumption is required.

## Continuum form — WP22

For a positive excitation-frequency spectral probability measure `mu` with finite mean `omega_bar`, **controlled large-period limits of the exact periodic models** satisfy

`R(nu)<=mu([nu,infinity))=P(Omega>=nu)`.

Therefore

`int_R R(nu)dnu<=2Ebar^+/hbar`,

and pointwise

`Ebar^+>=hbar nu R(nu)=h f R(2pi f)`.

A phase-averaged retention `q0`, or a scalar-retention guarantee `q0` for every sinusoidal phase, at ordinary frequency `B` requires

`Ebar^+>=hBq0`.

No smooth density is required in the spectral measure used by the periodic approximation.

## Exact equality family

For geometric energy sectors

`q_n=(1-r)r^n`,

the canonical phase POVM gives

`R(k)=r^k=T_k`

for every harmonic simultaneously and saturates the sum rule.

The controlled continuum limit is an exponential excitation spectrum with

`R(nu)=exp(-beta|nu|)`.

With `beta=2a`, the associated Cauchy timestamp has characteristic function `exp(-a|nu|)` and Fisher retention `exp(-2a|nu|)`.

## Independent Poisson source to common bosonic field — WP23

For an independent quantum-marked Poisson event source with mean event count `Lambda`, revealing the parameter-independent event number gives

`Tr F^(k)<=Lambda T_k`.

Any subsequent physical emission/source-to-field process and detector are a parameter-independent CPTP channel plus measurement once the random-time parameter is encoded upstream. Pulling the final POVM back through that channel proves that bosonic wavepacket overlap, mode mixing, coherent detector memory, ancillas, and arbitrary final measurement cannot evade the same source-normalized tail law.

This is a theorem for the independent-event source class, not for every quantum field with Poisson photocount statistics.

# Secondary QFI envelope — WP10/WP12/WP15

The separately optimized SLD-QFI results remain correct:

`G_Q(k)=2 sum_n q_nq_(n+k)/(q_n+q_(n+k))`,

`sum_(k>=1)G_Q(k)<=2nbar`,

and

`int_R G_Q(nu)dnu<=pi Ebar^+/hbar`.

They are interpreted as an incompatible modewise quantum-metric envelope, not as the main operational broadband theorem. WP16 records that the sharp `pi/4` continuum operator constant is classical Hardy--Hilbert mathematics.

# Scope boundary — WP14

The theorem concerns random temporal-distribution encoding of a fixed excitation in the stated periodic/controlled-limit source class. Baseline mean energy does not constrain arbitrary parameter-dependent coherent waveform synthesis; a broader theorem requires explicit encoding/control/action resource accounting.

# Prior-art boundary — WP21/WP24

Weighted `U(1)` twirling, energy-gap modes, canonical phase measurements, phase estimation under photon-number constraints, arbitrary-measurement Fisher/Holevo bounds, random-unitary probability estimation, and asymmetry resource theory are prior art.

Marvian--Spekkens (Phys. Rev. A 90, 062110, 2014) already show that weighted `U(1)` twirling acts modewise through Fourier coefficients of the mixing distribution.

The candidate contribution is narrower: the arbitrary-measurement **classical Fisher** ceiling for Fourier perturbations of that mixing distribution, its explicit paired-population/upper-tail value, the all-mode mean-energy sum rule, and the source-to-record photodetection interpretation.

Targeted searches have not found an exact predecessor of the tail/survival theorem. **Priority remains unverified, not certified.**

# Preferred Grand Challenge manuscript — Rev4

Working title:

**A Sharp Energy-Survival Law for Temporal Fisher Information**

Generation chain:

`Rev1 -> apply_rev2_mechanical.py -> apply_rev3_hostile_review.py -> apply_rev4_final_polish.py`.

Rev4 status:

- full local LaTeX/BibTeX build: PASS;
- 7 pages;
- unresolved citations/references: 0;
- overfull boxes: 0;
- undefined controls/fatal TeX errors: 0;
- all pages rendered and visually inspected: PASS;
- deterministic one-/two-copy random-POVM theorem validation committed;
- DOI/title-level bibliography audit completed;
- one real bibliography error repaired: Pocovnicu DOI `10.2140/apde.2011.4.379` is *Traveling waves for the cubic Szegő equation on the real line*, which is also the correct sharp positive-frequency inequality source.

The GitHub connector does not expose the relevant branch-push Actions run, so direct remote-job inspection remains unavailable; equivalent full local build verification is complete.

**Rev4 is frozen unless a concrete theorem, priority, build, or referee-level defect is found.**

## Read first

1. `grand_challenge/AGENTS.md`
2. `grand_challenge/notes/MANUSCRIPT_REV4_LOCAL_BUILD_AND_HOSTILE_REVIEW_2026-08-22.md`
3. `grand_challenge/notes/MANUSCRIPT_REV4_BIBLIOGRAPHY_PROVENANCE_AUDIT_2026-08-22.md`
4. `grand_challenge/notes/WP24_INTEGRATED_HOSTILE_REVIEW_AND_SYMMETRY_PRIOR_ART_BOUNDARY.md`
5. `grand_challenge/notes/WP23_RIGOROUS_COMPOUND_POISSON_TO_BOSONIC_FIELD_CHANNEL_MAP.md`
6. `grand_challenge/notes/WP22_CONTINUUM_LIMIT_RIGOR_FOR_OPERATIONAL_SURVIVAL_LAW.md`
7. `grand_challenge/notes/WP20_DIRECT_FINITE_COPY_PROOF_AND_HOSTILE_AUDIT_OF_WP19.md`

## Immediate work order

Do not accumulate another theorem by default. The next work is publication engineering: remote CI inspection if accessible, optional figure only if it materially improves comprehension, and factual submission metadata when supplied.

## Documentation discipline

Every material result or status change must be recorded in the repository and mirrored onto `main`; do not rely on chat history.
