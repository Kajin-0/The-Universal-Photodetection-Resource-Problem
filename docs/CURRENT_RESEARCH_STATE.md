# Current Research State

**Date:** 2026-08-21

Active branch: `agent/uprp-core-theorem-round10`

## Project-level status

1. **Paper 1 / Rev11:** scientifically frozen and technically validated for Physical Review Applied; only factual/personal submission metadata remain.
2. **Paper 2:** active theoretical program on arbitrary autonomous detector channels, hidden-memory Fisher spectra, Type-II recovery information singularities, and temporal information resources.

The active scientific frontier is Paper 2.

## Read first

1. `AGENTS.md`
2. `paper2/AGENTS_PAPER2.md`
3. `paper2/notes/WP24_ATOMIC_SCORE_RESIDUE_PRIOR_ART_AUDIT.md`
4. `paper2/notes/WP23_CAUSAL_SCORE_MARTINGALE_AND_ATOMIC_MEMORY_PATHS.md`
5. `paper2/notes/WP22_CONDITIONAL_SCORE_ATOM_THEOREM_AND_SELECTOR_COROLLARY.md`
6. `paper2/notes/WP21_HISTORICAL_INVERSE_OUTPUT_IDENTIFIABILITY_AUDIT.md`
7. `paper2/notes/WP19_EXACT_VARIANCE_INSUFFICIENCY_COUNTEREXAMPLE.md`
8. `paper2/notes/WP18_LAPLACE_PROOF_REPAIR_FOR_RECOVERY_SINGULARITY.md`
9. `paper2/notes/WP17_PUBLICATION_GRADE_WP10_FORMALIZATION.md`
10. `paper2/notes/WP07_CONTINUOUS_PARALYZABLE_SPECTRAL_SURVIVAL.md`

# Paper 1 — frozen Rev11

Preferred candidate remains Rev11. Do not reopen science absent a concrete defect or referee request.

# Paper 2 — current core

## WP10/WP17 — autonomous-channel Fisher spectrum

For homogeneous Poisson baseline `Phi0`, the incident waveform score is

`S_u=int u(t)[N(dt)-Phi0dt]`.

For any parameter-independent detector channel,

`S_u^out=E[S_u|Y]`.

Autonomy/time-translation covariance turns the induced positive contraction on `L2(R)` into a scalar Fourier multiplier:

`F_out[u,v]=Phi0/(2*pi) int G_{Phi0,K}(omega)U*(omega)V(omega)domega`,

with `0<=G<=1` a.e.

WP17 closes the principal DQM/trajectory-space/multiplier/narrowband formal gaps.

## WP07 — deterministic Type-II spectral survival

At deterministic paralyzable saturation `lambda*tau=1`:

`G_1(0)=0`,

`G_1(omega)>0` for every nonzero frequency,

`G_1(infinity)=1/e`.

At `omega*tau=pi`, the analytic lower bound is `0.516975...`; exact complete-record Volterra numerics give about `0.52814`.

This remains the strongest concrete physical spectral result.

## WP18 — generalized iid recovery Fisher singularity

All iid recovery laws with mean `m` have the same classical count curve

`r(lambda)=lambda exp(-lambda m)`.

Under renewal DQM/window regularity,

`G_DC=(r/lambda)I_D`.

At `lambda*m=1`, count/rate FI vanishes. The bounded-Laplace-statistic proof gives

`G_DC=0 iff T=m almost surely`

under the stated regularity.

**This is now the active proof-hardening target.** The next step is to separate the broad nonzero bounded-statistic sensitivity statement from the stronger finite Fisher-rate statement for atomic/heavy-tailed laws.

## WP19 — exact mean/variance insufficiency

Two explicit recovery laws have identical mean `1`, variance `1/4`, CV `0.5`, and identical conventional saturation curve, but different registered-timestamp information experiments. A common coarse-graining has zero FI for one law and normalized FI `~0.00443520488427` for the other; converged full static FI differs by about `8.78%`.

Thus mean + variance/CV + conventional mean curve are not resource-complete.

## WP21 — historical inverse-output audit

Generic output-flow identifiability is classical from at least the 1960s and textbook material by 1982. Afanaseva & Mikhailova (1973) remains a direct Type-II-lineage historical blocker whose theorem text is inaccessible.

Do not claim generic queue-output identifiability, hidden-service reconstruction, or exceptional information-degenerate service laws as new.

## WP22/WP23 — conditional-score atomic residue

WP22: if the conditional-score covariance is

`Gamma_M=a delta_0+nu`,

with finite-TV `nu` and no zero atom, the proportional high-frequency Cesaro Fisher residue is

`a/lambda`.

WP23: causality alone does not force `a=r`; exact delayed score paths can contribute additional atomic timing energy. The correct interpretation is total **atomic timing-path energy in the conditional score**.

For regular selectors with diffuse/non-atomic posterior memory, the immediate exact-timestamp path gives `a=r` and residue `r/lambda`.

## WP24 — atomic-residue novelty audit

The audit is **closed for manuscript strategy**.

Every mathematical ingredient has strong prior art:

- score covariance / Bartlett identities;
- counting-process innovation-martingale Fisher information;
- functional point-process Fisher kernels (including Clark 2022/2026);
- Bartlett spectra and high-frequency point-process shot-noise plateaus;
- Fourier-Stieltjes/Cesaro/Wiener/Rajchman atom theory;
- frequency-domain Fisher information in system identification;
- frequency-resolved neural/spike-train information.

No located source states the full UPRP chain in terms of the **conditional incident-source score after arbitrary detector processing**, but the construction is close enough to a synthesis of standard ingredients that WP22/WP23 should be treated as **bridge/structural theory, not a standalone mathematical breakthrough**.

Priority language remains disabled.

# Current novelty hierarchy

1. **WP10/WP17:** organizing photodetection-channel Fisher-spectrum synthesis.
2. **WP07:** strongest concrete physical novelty candidate.
3. **WP18:** strongest class-wide physical theorem candidate.
4. **WP19:** strong exact resource incompleteness/no-go result.
5. **WP22/WP23:** useful structural bridge; standalone novelty downgraded by WP24.

# Immediate next gates

1. **Harden WP18 for atomic and heavy-tailed recovery laws.**
2. Split the theorem into a minimal bounded-statistic sensitivity/identifiability result and a stronger finite positive `G_DC` result requiring DQM/FI-rate regularity.
3. Determine minimal conditions for `G_DC=(r/lambda)I_D` and treat finite-window censoring/boundary terms rigorously.
4. Determine what remains valid for finite-mean but infinite-variance recovery, infinite interval FI, or DQM failure.
5. After this gate, decide whether the WP10/WP07/WP18/WP19 core, with WP22/WP23 as bridge theory, has earned manuscript drafting.

# Documentation requirement

Material theorem results, proof repairs, prior-art collisions, numerical results used in arguments, and changes in next-gate decisions must be committed immediately. Keep `paper2/AGENTS_PAPER2.md` and this file synchronized with the active frontier.
