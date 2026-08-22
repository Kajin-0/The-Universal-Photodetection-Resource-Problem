# The Universal Photodetection Resource Problem

**Status synchronized: 2026-08-22**

## Project split

1. **Paper 1 / Rev11** — frozen and technically validated.
2. **Paper 2 / Rev7** — frozen preferred science draft.
3. **Grand Challenge** — ACTIVE on `agent/temporal-information-resource-law`; current checkpoint **WP24**.

Authoritative handoff: `grand_challenge/AGENTS.md`.

# Strongest current result — operational survival-function law

For periodic random-time encoding of a fixed semibounded-energy excitation with total-generator sector probabilities `q_n`, define

`T_k=sum_(m>=k)q_m`.

For **any finite number N of independent encoded excitations and any joint POVM**, including arbitrary entangled collective measurements,

`boxed: Tr F_N^(k) <= N T_k`.

Thus the per-event two-quadrature temporal-mode retention obeys

`boxed: R_N(k)<=T_k`,

and summing over positive harmonics gives

`boxed: sum_(k>=1)R_N(k)<=nbar`.

WP20 proves this directly by Hilbert--Schmidt Cauchy--Schwarz; no detector covariance, separability, Holevo asymptotics, or SLD attainability assumption is required.

A support-sensitive refinement is

`R_N(k)<=min(D_k,U_k)<=T_k`,

where `D_k` and `U_k` are the probability masses in the paired source/range sectors separated by `k`.

## Continuum form — WP22

For a general positive excitation-frequency spectral probability measure `mu` with finite mean `omega_bar`, every controlled continuum limit satisfies

`boxed: R(nu)<=mu([nu,infinity))=P(Omega>=nu)`.

Therefore

`boxed: int_R R(nu)dnu<=2Ebar^+/hbar`,

and pointwise

`boxed: Ebar^+>=hbar nu R(nu)=h f R(2pi f)`.

A guaranteed retention `q0` at ordinary frequency `B` requires

`boxed: Ebar^+>=hBq0`.

No smooth density is required.

## Exact equality family

For geometric energy sectors

`q_n=(1-r)r^n`,

the canonical phase POVM gives

`R(k)=r^k=T_k`

for every harmonic simultaneously and saturates the sum rule.

The continuum limit is an exponential excitation spectrum with

`R(nu)=exp(-beta|nu|)`,

which is the Cauchy timestamp equality family. Thus the operational coefficient `2E/hbar` is sharp and attainable.

## Independent Poisson source to common bosonic field — WP23

For an independent quantum-marked Poisson event source, the event number can be revealed as side information to obtain

`Tr F^(k)<=mu T_k`.

Any subsequent physical emission/source-to-field process and detector are a parameter-independent CPTP channel plus measurement once the random-time parameter is encoded upstream. Pulling the final POVM back through that channel proves that bosonic wavepacket overlap, mode mixing, coherent detector memory, ancillas, and arbitrary final measurement cannot evade the same source-normalized tail law.

This is a theorem for the independent-event source class, not for every quantum field with Poisson photocount statistics.

# Secondary QFI envelope — WP10/WP12/WP15

The separately optimized SLD-QFI results remain correct:

`G_Q(k)=2 sum_n q_nq_(n+k)/(q_n+q_(n+k))`,

`sum_(k>=1)G_Q(k)<=2nbar`,

and

`int_R G_Q(nu)dnu<=pi Ebar^+/hbar`.

They are now interpreted as an incompatible modewise quantum envelope, not as the main operational broadband theorem. WP16 records that the sharp `pi/4` continuum operator constant is classical Hardy--Hilbert mathematics.

# Scope boundary — WP14

The theorem concerns **random temporal-distribution encoding of a fixed semibounded-energy excitation**. Baseline mean energy does not constrain arbitrary parameter-dependent coherent waveform synthesis; a broader theorem requires explicit encoding/control/action resource accounting.

# Prior-art boundary — WP21/WP24

Weighted `U(1)` twirling, energy-gap modes, canonical phase measurements, phase estimation under photon-number constraints, arbitrary-measurement Fisher/Holevo bounds, random-unitary probability estimation, and asymmetry resource theory are all prior art.

Marvian--Spekkens (Phys. Rev. A 90, 062110, 2014) already show that weighted `U(1)` twirling multiplies the `k`th energy-gap mode by the `k`th Fourier coefficient of the mixing distribution.

The candidate contribution is narrower: the arbitrary-measurement **Fisher** ceiling for perturbations of that mixing distribution, its explicit population-tail value, the all-mode mean-energy sum rule, and the photodetection source-to-record interpretation.

Targeted searches have not found an exact predecessor of the tail/survival theorem. **Priority remains unverified, not certified.**

# Current status

WP24 integrated hostile review: **PASS**, after a support-gap repair and stronger prior-art fencing.

The former main scientific gates are now addressed:

- arbitrary collective measurement — WP20;
- continuum limit — WP22;
- independent event to physical bosonic field — WP23.

The project has reached a reasonable standalone-manuscript formation threshold with conservative novelty language.

## Read first

1. `grand_challenge/AGENTS.md`
2. `grand_challenge/notes/WP24_INTEGRATED_HOSTILE_REVIEW_AND_SYMMETRY_PRIOR_ART_BOUNDARY.md`
3. `grand_challenge/notes/WP23_RIGOROUS_COMPOUND_POISSON_TO_BOSONIC_FIELD_CHANNEL_MAP.md`
4. `grand_challenge/notes/WP22_CONTINUUM_LIMIT_RIGOR_FOR_OPERATIONAL_SURVIVAL_LAW.md`
5. `grand_challenge/notes/WP20_DIRECT_FINITE_COPY_PROOF_AND_HOSTILE_AUDIT_OF_WP19.md`
6. `grand_challenge/notes/WP21_TARGETED_PRIORITY_AUDIT_SURVIVAL_FUNCTION_LAW.md`

## Documentation discipline

Every material result must be recorded in the repository and mirrored onto `main`; do not rely on chat history.