# Research Roadmap

**Updated:** 2026-08-22

**Active scientific branch:** `agent/temporal-information-resource-law`

Paper 1 Rev11 and Paper 2 Rev7 are frozen. Grand Challenge science checkpoint: **WP24**. **Rev4 freezes the science content; Rev5 is the preferred frozen publication draft.**

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

**NO-GO.** Baseline mean energy alone does not constrain arbitrary state-valued coherent waveform engineering. The frozen science content includes an explicit coherent-sideband counterexample. A broader theorem requires an encoding/control/action resource.

# Prior-art status

Occupied areas include `U(1)` modes of asymmetry / weighted group twirling, canonical phase measurements and phase Fourier moments, photon-number/energy-constrained phase estimation, arbitrary-measurement Fisher/Holevo/RLD/SLD bounds, random-unitary probability estimation, waveform QFI, positive-frequency sharp Gagliardo--Nirenberg inequalities, Hardy--Hilbert best-constant mathematics, and compound-Poisson/CPTP/Stinespring data processing.

The candidate contribution remains the exact operational Fisher tail theorem

`Tr F_N^(k)/N<=sum_(m>=k)q_m`,

its paired-support refinement, mean-generator harmonic budget, and controlled continuum survival/source-to-record consequences.

**Priority remains unverified, not certified.**

# Manuscript gate — PASSED

Science-content checkpoint: `energy_survival_temporal_fisher_rev4.tex`.

Preferred publication draft: `energy_survival_temporal_fisher_rev5.tex` generated deterministically from Rev1 through Rev5.

Rev5 adds only one conceptual two-column architecture figure and hidden hyperlink decorations. It changes no theorem, proof, coefficient, source hypothesis, or novelty claim relative to Rev4.

Rev5 has passed:

- integrated scientific hostile review inherited from Rev4/WP24;
- full local LaTeX/BibTeX compilation;
- unresolved-reference/citation gate;
- overfull-box gate;
- seven-page visual inspection;
- Figure 1 readability and scope-value review;
- deterministic numerical theorem sanity checks;
- DOI/title/provenance bibliography audit.

The remote push-triggered GitHub Actions job is not exposed by the current connector; equivalent full local build verification is complete.

# Current work order — journal targeting and submission engineering

1. **Freeze Rev5.** Reopen science only for a concrete theorem, priority, build, or referee defect.
2. Select the strongest realistic journal whose scope matches foundational quantum measurement / quantum optics / information theory.
3. Verify the journal's current article type, length/style requirements, preprint policy, data/code statements, AI/disclosure requirements, and cover-letter expectations from primary journal sources.
4. Build a submission checklist and cover-letter draft with conservative novelty language.
5. Prepare author/affiliation/ORCID/funding/conflict/AI-use metadata only from factual user-supplied information; never invent administrative facts.
6. Maintain the exact scope qualifiers: two-quadrature/phase-averaged retention, controlled continuum limit, independent-event source class, and WP14 waveform no-go.
7. If a reviewer or new historical source exposes a priority collision, update WP24/prior-art notes before changing manuscript claims.

# Documentation discipline

Every material theorem, no-go, proof repair, priority collision, manuscript defect, or publication-status change must update the detailed notes, handoff/landing files, and `main`.