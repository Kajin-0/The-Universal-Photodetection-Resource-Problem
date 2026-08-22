# Grand Challenge — Temporal Information Resource Law

**Science checkpoint: WP24 — 2026-08-22**

**Preferred PRX Quantum manuscript: Rev7.**

## Grand question

> For a physically realizable measurement of temporal structure, what fundamental resources constrain source-to-record temporal Fisher-information transfer?

## Strongest theorem

For exact periodic random-time encoding with sector probabilities `q_n`, define

`T_k=sum_(m>=k)q_m`.

For any finite `N` and any joint POVM,

`Tr F_N^(k) <= N min(D_k,U_k) <= N T_k`.

Hence

`R_N(k)=Tr F_N^(k)/N <= T_k`,

`sum_(k>=1)R_N(k) <= nbar`.

The theorem includes arbitrary finite-copy entangled collective measurements.

## Controlled periodic-to-continuum survival law

For controlled periodic-to-continuum limits,

`R(nu) <= Pr(Omega>=nu)`.

This is the principal continuum result. `Omega` is excess generator frequency above the participating lower edge; the common edge/carrier offset is irrelevant.

The energy relations

`int_R R <= 2Ebar+/hbar`,

`Ebar+ >= hbar nu R(nu) = h f R(2pi f)`

are first-moment corollaries, with `Ebar+=hbar<Omega>`.

## Sharpness and nonextremal photon example

The geometric/canonical-phase family gives `R(k)=T_k=r^k` for every harmonic simultaneously and yields the exponential/Cauchy equality family in the controlled continuum limit.

Rev7 adds one transform-limited truncated-Gaussian single-photon example. Canonical covariant timing reaches approximately 96.6% of the survival ceiling at `nu=0.5 sigma` and 88.5% at `nu=sigma`.

## Physical scope

WP23 transfers the normalized law to independent quantum-marked Poisson events followed by arbitrary **parameter-independent** source-to-field and detector processing.

WP14/Rev7 retain the coherent-sideband no-go: arbitrary parameter-dependent waveform-state synthesis cannot be bounded by baseline mean energy alone.

## Prior-art boundary

`U(1)` modes of asymmetry and weighted twirling are prior art. Their role is kinematic: they identify available energy-gap components. The candidate contribution here is operational:

> a sharp bound on the **classical Fisher information extractable by any actual POVM** about Fourier perturbations of the random-time mixing law, expressed through participating population tails and valid for arbitrary finite-copy collective measurements.

Canonical phase POVMs, energy-constrained phase estimation, generic QFI/Holevo machinery, random-unitary estimation, waveform QFI, Hardy--Hilbert/positive-frequency mathematics, and generic Poisson/CPTP data processing are also prior art.

**Priority remains unverified, not certified.**

## Preferred manuscript — Rev7

Working title: **A Sharp Energy-Survival Law for Temporal Fisher Information**.

Rev7 was produced in direct response to an external adversarial review. It:

- makes the continuum theorem explicitly controlled periodic-to-continuum;
- defines the resource as excess energy above the participating edge;
- makes the survival law primary and `hfR` a first-moment corollary;
- sharpens the distinction from modes-of-asymmetry theory;
- adds one nonextremal transform-limited single-photon example;
- revises Figure 1 to match those claims.

Final local preflight:

- full LaTeX/BibTeX build: **PASS**;
- **8 pages**;
- PDF size: **403,102 bytes**;
- SHA-256: `d168c3901faa6f29bda0eba71abe8049cc9819d91843273beeeeffb9443818ae`;
- unresolved citations/references: **0**;
- overfull boxes: **0**;
- all pages rendered at 200 dpi and visually inspected: **PASS**;
- new photon example and periodic-approximant convergence: **PASS**.

## Read first

1. `AGENTS.md`
2. `notes/MANUSCRIPT_REV7_REFEREE_HARDENING_2026-08-22.md`
3. `notes/WP24_INTEGRATED_HOSTILE_REVIEW_AND_SYMMETRY_PRIOR_ART_BOUNDARY.md`
4. `notes/WP23_RIGOROUS_COMPOUND_POISSON_TO_BOSONIC_FIELD_CHANNEL_MAP.md`
5. `notes/WP22_CONTINUUM_LIMIT_RIGOR_FOR_OPERATIONAL_SURVIVAL_LAW.md`
6. `notes/WP20_DIRECT_FINITE_COPY_PROOF_AND_HOSTILE_AUDIT_OF_WP19.md`

## Journal target

**First target:** PRX Quantum — Research Article.

**Fallback:** Physical Review A — Regular Article.

## Current work order

**Freeze Rev7.** Do not add more theory or examples by default. Reopen only for a concrete theorem defect, historical-priority collision, build defect, unavoidable journal-format issue, or new referee-level objection.

Do not reintroduce “human verification” as a research/manuscript gate. The finished package is handed to a human for submission; unknown administrative facts remain placeholders rather than being invented.

The repository handoff files must remain sufficient for recovery; do not rely on chat history.
