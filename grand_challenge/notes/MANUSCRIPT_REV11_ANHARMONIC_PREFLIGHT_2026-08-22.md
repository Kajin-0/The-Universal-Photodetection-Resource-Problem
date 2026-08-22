# Manuscript Rev11 anharmonic-extension preflight — 2026-08-22

## Status

**PASS. Rev11 is the preferred PRX Quantum manuscript.**

Working title: **Spectral Resource Laws for Temporal Fisher Information**.

Rev11 was triggered by an adversarial critique claiming that the finite-copy Fisher-tail proof was an artifact of a globally equally spaced Hamiltonian, that singular-continuous spectral measures undermine the continuum limit, and that the zero-population completion used in the Herglotz proof introduces fictitious degrees of freedom.

The audit did not expose a failure of the existing results. The strongest objection instead produced a genuine theorem-level extension.

## 1. New fixed-Hamiltonian Bohr-gap theorem

Let a participating semibounded pure-point Hamiltonian have distinct excess frequencies `omega_alpha>=0`, with no commensurability assumption. Fix a modulation angular frequency `nu>0` and average the random-time experiment over windows

`T_M=2 pi M/nu`.

In the large-window limit the baseline completely dephases unequal energies and the local sinusoidal tangent selects only exact Bohr pairs

`omega_beta-omega_alpha=nu`.

The positive-gap tangent is

`A_nu=sum_(alpha,beta: omega_beta-omega_alpha=nu) sqrt(q_alpha q_beta)|phi_beta><phi_alpha|`.

Defining

`V_nu=sum_(alpha,beta: omega_beta-omega_alpha=nu, q_alpha q_beta>0)|phi_beta><phi_alpha|`,

translation by `nu` is one-to-one, so `V_nu` is a partial isometry and

`A_nu=rho0^(1/2)V_nu rho0^(1/2)`.

Therefore the Hilbert--Schmidt proof extends unchanged:

`Tr F_N^(nu)/N <= min(D_nu,U_nu) <= S(nu)`

for every finite `N` and every joint POVM, including arbitrary entangled collective measurements, where

`S(nu)=Pr(Omega>=nu)`.

**Global equal spacing and commensurability are not required for the modewise Fisher-tail mechanism.**

If no exact Bohr pair is separated by `hbar nu`, then the limiting tangent vanishes and the corresponding limiting local Fisher response is zero.

## 2. Common-measurement extension for anharmonic pure-point spectra

For fixed `nu`, partition the spectrum into residue classes modulo `nu`. Completing missing integer positions by zero-population placeholders permits one shift `V` satisfying

`A_(m nu)=rho0^(1/2)V^m rho0^(1/2)`

for every integer `m>=1`.

The Rev10 posterior/Herglotz argument then gives a positive-definite retention sequence for one fixed one-copy POVM across the exact gaps `m nu`. Monotonicity of the physical spectral tail gives

`Ebar+/hbar = int_0^infinity S(x)dx >= nu sum_(m>=1)S(m nu)`.

Combining these facts reproduces

`Ebar+ >= hbar nu A(q)`

and the same sharp near-lossless scaling

`Ebar+ = Omega((1-q)^(-1/2))`.

The complete geometric-mixture/Hausdorff extremizer classification remains intentionally restricted to the full contiguous pure-sector chain.

## 3. Continuum-measure objection

The continuum theorem does **not** assume a smooth spectral density. Rev11 now says this explicitly.

For any Borel probability measure `mu` on `[0,infinity)` with finite first moment,

`q_n^(delta)=mu([n delta,(n+1)delta))`

and

`T_k^(delta)=mu([k delta,infinity))`.

Tail convergence follows from monotonicity and continuity from above of finite measures. Atomic, absolutely continuous, singular-continuous, and mixed spectral measures are all allowed.

The genuine continuum qualification remains the controlled convergence of the physical periodic measurement schemes; no normalized uniform probability measure exists on noncompact time `R`.

## 4. Zero-population completion objection

The appended sectors used to form a common shift are algebraic placeholders only.

If `|g>` has zero baseline population, then

`rho0^(1/2)|g>=0`.

Hence the posterior operator measure

`tau(B)=rho0^(1/2)M(B)rho0^(1/2)`

annihilates `|g>` for every outcome set. Positivity implies the posterior density operators have zero support there almost everywhere. The completion cannot create score or Fisher information.

This clarification is now explicit in the Herglotz section.

## 5. Local-Fisher scope

The critique that Fisher information is local is correct but not a newly exposed defect. Rev11 retains the explicit statement that the theorem concerns the local statistical experiment at the uniform random-time baseline and is not by itself a global finite-amplitude risk theorem.

A separate trace-distance extension was identified in WP28 but was not added to Rev11 because the fixed-Hamiltonian theorem is the higher-value strengthening and the manuscript should remain disciplined.

## 6. Prior-art boundary

The literature search recovered the expected neighboring structures:

- Marvian--Spekkens: arbitrary Bohr-frequency / modes-of-asymmetry decomposition is established prior art.
- Boixo--Knill--Somma: random evolution times acting as energy dephasing through Fourier/characteristic-function weights is established prior art.

Rev11 does **not** claim either construction as new.

The candidate contribution is the arbitrary-measurement Fisher coefficient at an exact Bohr gap, its semibounded population-tail ceiling, and the common-measurement energy consequence.

Targeted searches did not surface an exact predecessor for this operational Fisher-tail theorem. **Priority remains unverified, not certified.**

## 7. Editorial change

The separately optimized SLD-QFI envelope section was removed from the main manuscript. It was mathematically valid but peripheral after the Herglotz, extremizer, and anharmonic results were established. The new fixed-Hamiltonian theorem replaces it rather than simply increasing theorem count without discipline.

Figure 1 was revised to distinguish:

1. the exact periodic modewise law;
2. the fixed-Hamiltonian pure-point Bohr-gap law;
3. the controlled continuum survival law;
4. the fixed one-copy common-measurement Herglotz law.

## 8. Numerical hostile audit

`grand_challenge/numerics/verify_anharmonic_pure_point_gap_extension.py` uses a deliberately globally incommensurate spectrum and checks:

1. long-window dephasing and exact-gap selection;
2. `A_nu=rho0^(1/2)V_nu rho0^(1/2)`;
3. random-POVM Fisher traces against the paired-population ceiling;
4. the physical energy-tail ceiling;
5. Toeplitz PSD for one fixed measurement across gap multiples.

**PASS.**

The existing operational-tail, truncated-Gaussian, complete-monotone, Herglotz, and sine-profile validators remain part of the CI chain.

## 9. Final local publication gate

Final Rev11 PDF:

`energy_survival_temporal_fisher_rev11_prxq.pdf`

- full `pdflatex -> BibTeX -> pdflatex -> pdflatex`: **PASS**;
- pages: **12**;
- PDF size: **452,384 bytes**;
- PDF SHA-256: `5e0ac0132a7f4a3f7b07e9c4ba86b046b23bc89c1f7635efe9f737019396d0f0`;
- unresolved citations/references: **0**;
- overfull boxes: **0**;
- fatal/undefined controls: **0**;
- all 12 pages rendered at 200 dpi and visually inspected: **PASS**;
- revised Figure 1: **PASS**;
- new theorem pages: **PASS**.

Self-contained source package:

`energy_survival_temporal_fisher_rev11_prxq_source.zip`

- ZIP size: **29,931 bytes**;
- ZIP SHA-256: `208fd7a2e932507366797658c84dff1666257477143a433bf81d7741a8d0c8a1`;
- fresh compile from extracted package: **PASS**;
- fresh PDF pages/size: **12 / 452,384 bytes**;
- fresh PDF SHA-256 differs (`1071f1af22e68aca13e5faf82074a82d1b9395c43b998536367062180f3bf854`) because the LaTeX/PDF metadata are not bitwise deterministic;
- 200-dpi render comparison of original and fresh PDFs: **0 changed pages, 0 changed pixels on all 12 pages**.

Thus the source package is visually reproducible even though the produced PDF is not byte-identical.

The dedicated GitHub Actions workflow now generates Rev11, runs all six numerical validators, compiles the PRX source, and rejects regressions in the anharmonic theorem, continuum-measure scope, null-sector invariance, Bochner hypothesis, sharp-exponent proposition, local-Fisher qualifier, or removal of the peripheral QFI section. Direct branch-push run inspection is not exposed by the current connector, so no remote-run result is claimed.

## 10. Freeze decision

**Freeze Rev11 as the preferred PRX Quantum manuscript.**

Do not add the finite-amplitude trace-distance observation, optimize the near-lossless prefactor, or broaden the extremizer classification by default. Reopen only for a concrete mathematical defect, priority collision, substantive referee objection, build/render regression, or unavoidable journal-format requirement.
