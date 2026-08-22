# Research Roadmap

**Updated:** 2026-08-22

**Active branch:** `agent/temporal-information-resource-law`

Paper 1 Rev11 and Paper 2 Rev7 are frozen.

**Grand Challenge science checkpoint:** WP24.

**Preferred manuscript:** **Rev7 PRX Quantum**.

# Established hierarchy

## G1 — finite-copy operational Fisher-tail law

For exact periodic random-time encoding,

`Tr F_N^(k)/N <= min(D_k,U_k) <= T_k`,

for any finite `N` and any joint POVM, including arbitrary entangled collective measurements.

Summing gives

`sum_(k>=1) R_N(k) <= nbar`.

## G2 — controlled periodic-to-continuum survival law

For controlled periodic-to-continuum limits,

`R(nu) <= Pr(Omega>=nu)`.

This is the principal continuum statement.

`Ebar+=hbar<Omega>` is excess energy above the participating lower edge. The area and pointwise relations are first-moment corollaries:

`int_R R <= 2Ebar+/hbar`,

`Ebar+ >= hbar nu R(nu) = h f R(2pi f)`.

## G3 — sharpness

The geometric/canonical-phase family saturates every discrete harmonic simultaneously and yields the exponential/Cauchy controlled-continuum equality family.

## G4 — nonextremal photon relevance

Rev7 adds one transform-limited truncated-Gaussian single-photon example. Canonical covariant timing reaches about 96.6% of the survival ceiling at `0.5 sigma` and 88.5% at `sigma`. Closed forms and convergence from lower-bin periodic approximants are validated numerically.

## G5 — independent Poisson source to field

For an independent quantum-marked Poisson source, arbitrary **parameter-independent** field formation and detector processing cannot evade the normalized bound because the final POVM pulls back to the upstream event register.

## G6 — secondary QFI envelope

WP10/WP12/WP15 remain valid but secondary. The modewise SLD-QFI area coefficient is not the jointly accessible operational theorem; WP16 records the Hardy--Hilbert mathematical provenance.

## G7 — arbitrary waveform synthesis

WP14/Rev7 retain the coherent-sideband **NO-GO**: baseline mean energy alone cannot constrain arbitrary parameter-dependent waveform-state synthesis.

# Novelty/prior-art boundary

Modes-of-asymmetry theory already identifies `U(1)` energy-gap modes and weighted-twirl Fourier structure. The Grand Challenge contribution is instead the **classical Fisher information ceiling for any actual POVM**, expressed through participating population tails and valid for arbitrary finite-copy collective measurements.

Do not claim novelty for weighted twirling, canonical phase POVMs, number/energy-constrained phase estimation, generic QFI/Holevo machinery, random-unitary estimation, waveform QFI, positive-frequency/Hardy--Hilbert mathematics, or generic Poisson/CPTP data processing.

**Priority remains unverified, not certified.**

# Rev7 gate — PASSED

Rev7 directly answers the highest-value criticisms from the latest adversarial review:

1. continuum theorem now explicitly labeled controlled periodic-to-continuum;
2. resource consistently identified as excess energy above the active lower edge;
3. survival law promoted above the elementary `hf` first-moment corollary;
4. modes-of-asymmetry distinction sharpened;
5. one nonextremal transform-limited single-photon example added;
6. Figure 1 updated to reflect the same claim discipline.

Final local preflight:

- full LaTeX/BibTeX build: **PASS**;
- **8 pages**;
- unresolved citations/references: **0**;
- overfull boxes: **0**;
- all 8 pages rendered at 200 dpi and visually inspected: **PASS**;
- final local PDF SHA-256: `d168c3901faa6f29bda0eba71abe8049cc9819d91843273beeeeffb9443818ae`;
- photon-example analytic and periodic-approximant validation: **PASS**.

Detailed record:

`grand_challenge/notes/MANUSCRIPT_REV7_REFEREE_HARDENING_2026-08-22.md`.

# Journal ladder

1. **PRX Quantum — Research Article**: first target.
2. **Physical Review A — Regular Article**: preferred fallback.
3. Physical Review Research: secondary alternative.
4. PRL: only after a deliberate Letter rewrite; do not hide hypotheses/proofs to force the format.

# Current work order

**Freeze Rev7.**

Do not add more theorem scope, detector technologies, source classes, squeezed/correlated extensions, or examples by default. Reopen only for:

- a concrete theorem defect;
- historical-priority collision;
- build/rendering defect;
- new referee-level objection;
- unavoidable journal-format requirement.

The paper and submission materials should be completed as far as possible autonomously. Do not introduce “human verification” as a research/manuscript gate. A human submits the finished package; unknown administrative facts remain placeholders rather than being invented.

# Documentation discipline

Every material theorem, prior-art collision, manuscript defect, or publication-status change must update the detailed notes, active landing/handoff files, and `main`.
