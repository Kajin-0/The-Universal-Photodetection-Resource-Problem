# Research Roadmap

**Updated:** 2026-08-22

**Active scientific branch:** `agent/temporal-information-resource-law`

Paper 1 Rev11 and Paper 2 Rev7 are frozen. Grand Challenge science checkpoint: **WP24**. Preferred Grand Challenge manuscript: **Rev4**, frozen unless a concrete defect appears.

# Established theorem hierarchy

## G1 — finite-copy operational survival law — WP20/WP24

For exact periodic random-time encoding with sector probabilities `q_n`, harmonic `k`, and

`T_k=sum_(m>=k)q_m`,

any finite `N` and any joint POVM obey

`Tr F_N^(k)<=N min(D_k,U_k)<=N T_k`.

Thus

`R_N(k)=Tr F_N^(k)/N<=T_k`,

and

`sum_(k>=1)R_N(k)<=nbar`.

This closes the arbitrary finite-copy collective-measurement gate by a direct Hilbert--Schmidt Cauchy--Schwarz proof.

`R_N(k)` is the two-quadrature / phase-averaged source-normalized retention. A uniform scalar-retention guarantee over every sinusoidal phase obeys the same ceiling.

## G2 — controlled continuum survival law — WP22

For a positive excitation-frequency spectral probability measure `mu` with finite mean, controlled large-period limits of exact lower-bin periodic approximants satisfy

`R(nu)<=mu([nu,infinity))`.

Therefore

`int_R R(nu)dnu<=2Ebar^+/hbar`,

and

`Ebar^+>=hbar nu R(nu)=h f R(2pi f)`.

The continuum result is intentionally stated as a controlled periodic-limit theorem, not as an unqualified direct theorem for every fixed nonperiodic experiment.

## G3 — exact sharpness

Geometric sector populations with the canonical phase POVM saturate every discrete harmonic simultaneously:

`R(k)=T_k=r^k`.

The controlled continuum exponential-spectrum / Cauchy-timestamp family saturates the survival and area bounds. For Cauchy scale `a`, the characteristic function is `exp(-a|nu|)` and the Fisher retention is `exp(-2a|nu|)`.

## G4 — independent Poisson source to physical field — WP23

For independent quantum-marked Poisson events with mean `Lambda`, event-number side information plus POVM pullback through the parameter-independent source/field/detector CPTP map yields

`R_final(k)<=T_k`.

This covers arbitrary downstream bosonic overlap, mode mixing, coherent detector memory, ancillas, and final joint measurement within the explicit independent-event source class.

## G5 — separately optimized QFI envelope — WP10/WP12/WP15

Still correct but secondary:

`sum_(k>=1)G_Q(k)<=2nbar`,

`int_R G_Q(nu)dnu<=pi Ebar^+/hbar`.

This is a modewise SLD-QFI metric envelope, not the jointly accessible operational law. WP16 identifies the sharp `pi/4` analytic operator norm as classical Hardy--Hilbert mathematics.

## G6 — arbitrary coherent waveform synthesis — WP14

**NO-GO.** Baseline mean energy alone does not constrain arbitrary state-valued coherent waveform engineering. Rev4 contains an explicit coherent-sideband counterexample. A broader theorem requires an encoding/control/action resource.

# Prior-art status

Occupied areas include:

- `U(1)` modes of asymmetry / weighted group twirling;
- canonical phase measurements and phase Fourier moments;
- photon-number/energy-constrained phase estimation;
- arbitrary-measurement Fisher/Holevo/RLD/SLD bounds;
- random-unitary probability estimation;
- waveform QFI;
- positive-frequency sharp Gagliardo--Nirenberg inequalities;
- Hardy--Hilbert best-constant mathematics;
- compound-Poisson and CPTP/Stinespring data processing.

The candidate contribution remains the exact operational Fisher tail theorem

`Tr F_N^(k)/N<=sum_(m>=k)q_m`,

its paired-support refinement, mean-generator harmonic budget, and controlled continuum survival/source-to-record consequences.

**Priority remains unverified, not certified.**

# Manuscript gate — PASSED

Preferred draft: `energy_survival_temporal_fisher_rev4.tex`, generated deterministically from Rev1.

Rev4 has passed:

- integrated scientific hostile review;
- full local LaTeX/BibTeX compilation;
- unresolved-reference/citation gate;
- overfull-box gate;
- seven-page visual inspection;
- deterministic numerical theorem sanity checks;
- DOI/title/provenance bibliography audit.

The bibliography audit found and corrected one genuine metadata defect: DOI `10.2140/apde.2011.4.379` is Pocovnicu's *Traveling waves for the cubic Szegő equation on the real line*. That paper remains the correct source because it contains the sharp positive-frequency Gagliardo--Nirenberg inequality. Gill's citation was upgraded from the 2005 arXiv preprint to the published 2008 World Scientific chapter while retaining the arXiv identifier.

The remote push-triggered GitHub Actions job is not exposed by the current connector; equivalent full local build verification is complete.

# Current work order — publication engineering, not theorem accumulation

1. **Freeze Rev4 science.** Reopen only for a concrete theorem, priority, build, or referee defect.
2. Inspect remote Rev4 CI if it becomes accessible.
3. Decide whether **one** conceptual figure materially improves comprehension; do not add decorative figures by default.
4. Maintain conservative novelty language while historical priority remains uncertified.
5. Prepare journal submission metadata/compliance only from factual user-supplied information.
6. If a reviewer or new source exposes a collision, update WP24/prior-art notes before changing claims.

# Documentation discipline

Every material theorem, no-go, proof repair, priority collision, manuscript defect, or publication-status change must update the detailed notes, handoff/landing files, and `main`.
