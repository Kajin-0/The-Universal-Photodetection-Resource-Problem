# PRX Quantum Target Decision and Submission Checklist

**Updated:** 2026-08-22

**Science frontier:** WP28

**Preferred submission manuscript:** **Rev11 — Spectral Resource Laws for Temporal Fisher Information**.

## Decision

### First target: PRX Quantum — Research Article

PRX Quantum is well justified on an **exceptional connection / exceptional insight** case. Rev11 combines:

- a finite-copy arbitrary-POVM Fisher-tail ceiling in the exact periodic experiment;
- a new extension of that ceiling to **arbitrary semibounded pure-point Hamiltonians at exact Bohr gaps**, with no global equal-spacing or commensurability assumption;
- controlled continuum spectral-survival law for arbitrary finite Borel spectral measures;
- a Herglotz/Toeplitz consistency law for one fixed one-copy measurement;
- the same common-measurement law along exact gap multiples for arbitrary pure-point Hamiltonians;
- divergent near-lossless energetic cost with a sharp `(1-R)^(-1/2)` exponent;
- complete one-copy saturation classification by geometric mixtures / Hausdorff moments in the full contiguous pure-sector model;
- a completely monotone continuum equality cone;
- quantitative near-tightness for a truncated-Gaussian single photon;
- source-to-record inheritance for independent quantum-marked Poisson sources.

### Fallback

Physical Review A — Regular Article.

Do not force a PRL rewrite by hiding assumptions or proof structure.

## Claim hierarchy

### Exact periodic finite-copy theorem

`Tr F_N^(k)/N <= min(D_k,U_k) <= T_k`

for any finite number of independently encoded copies and any joint POVM, including entangled collective measurements.

### Fixed-Hamiltonian pure-point Bohr-gap theorem

For

`H=E_* I + hbar sum_alpha omega_alpha P_alpha`, `omega_alpha>=0`,

fix `nu>0` and use long windows `T_M=2pi M/nu`. The limiting tangent selects exact pairs `omega_beta-omega_alpha=nu` and factorizes through a partial isometry. Hence

`Tr F_N^(nu)/N <= min(D_nu,U_nu) <= S(nu)=Pr(Omega>=nu)`

for every finite `N` and arbitrary joint POVM.

**No global equal-spacing or commensurability assumption is required.**

Do not claim that arbitrary Bohr-frequency decomposition or random-time dephasing is new; those are prior art. The contribution is the measurement-accessible Fisher coefficient and semibounded tail ceiling.

### Controlled continuum survival law

`R(nu)<=Pr(Omega>=nu)`.

The spectral measure may be atomic, absolutely continuous, singular-continuous, or mixed. `Ebar+=hbar<Omega>` is mean excess energy above the participating lower edge. `hfR` and the area law are first-moment corollaries.

### Fixed-one-copy common-measurement law

For one fixed one-copy POVM,

`R_M(k)=int cos(k theta)J_M(dtheta)`.

The retention sequence is positive definite and its Toeplitz matrices are PSD. Zero-population completion cannot create Fisher information.

For an arbitrary pure-point Hamiltonian the same structure applies across exact multiples `m nu` of a chosen gap.

With `q=R_M(nu)`,

`Ebar+>=hbar nu A(q)`,

`A(q)~1/sqrt(2(1-q))`.

This divergence statement must retain the **fixed one-copy/common-POVM** qualifier.

For the controlled continuum Herglotz extension, the normalized positive-definite limit must be **continuous at the origin** before Bochner is invoked.

### Sharp exponent

The finite sine profile under canonical phase measurement gives

`R_L(1)=cos^2(pi/(L+1))`,

`nbar_L=(L-1)/2`,

and therefore

`nbar_L~pi/[2sqrt(1-R_L(1))]`.

The inverse-square-root exponent is sharp. Do **not** claim the globally optimal prefactor.

### Complete extremizers — narrower converse

Only on the full contiguous pure-sector one-copy chain with positive populations:

`first-harmonic saturation`

`<=> geometric-mixture populations`

`<=> Hausdorff-moment tails`

`<=> one source-adapted POVM saturates every harmonic simultaneously`.

No converse is claimed for arbitrary anharmonic/sparse spectra, arbitrary mixed sector blocks, or arbitrary entangled `N>1` collective equality cases.

## Prior-art discipline

Do not claim novelty for:

- arbitrary Bohr-frequency / `U(1)` mode decomposition or weighted twirling;
- random-time dephasing itself;
- Herglotz or Bochner theorems;
- Hausdorff or Bernstein-Widder moment theory;
- geometric/exponential mixtures;
- canonical phase POVMs;
- finite sine states;
- generic QFI/Holevo/RLD/SLD machinery;
- generic Poisson/CPTP data processing.

**Priority remains unverified, not certified.**

## Rev11 package

Generation chain:

`Rev1 -> Rev2 -> Rev3 -> Rev4 -> Rev5 -> Rev6 -> Rev7 -> Rev8 -> Rev9 spectral theory -> Rev9 abstract compression -> Rev10 referee closure -> Rev11 anharmonic extension`.

Rev11 generator:

`grand_challenge/manuscript/apply_rev11_anharmonic_extension.py`

Validation scripts:

- `grand_challenge/numerics/verify_operational_tail_bound.py`
- `grand_challenge/numerics/verify_truncated_gaussian_photon_example.py`
- `grand_challenge/numerics/verify_complete_monotone_saturation.py`
- `grand_challenge/numerics/verify_herglotz_high_retention.py`
- `grand_challenge/numerics/verify_sine_profile_divergence_sharpness.py`
- `grand_challenge/numerics/verify_anharmonic_pure_point_gap_extension.py`

The separately optimized SLD-QFI section was removed from Rev11 rather than allowing the new theorem to simply inflate the manuscript.

Dedicated CI generates Rev11, runs all six validators, compiles the PRX source, and rejects unresolved references, overfull boxes, loss of the anharmonic theorem, loss of the arbitrary-measure continuum clarification, null-sector completion regressions, loss of Bochner continuity-at-zero, loss of sharp-exponent/local-Fisher qualifiers, or reappearance of the retired QFI section.

## Submission materials and publication gate

- [x] Rev11 cover letter updated.
- [x] Rev11 Popular Summary updated.
- [x] AI-use / Data Availability disclosure draft retained.
- [x] WP28 theorem/audit note committed.
- [x] Rev11 deterministic generator and dedicated theorem/figure inputs committed.
- [x] Anharmonic incommensurate-spectrum validator committed and passed locally.
- [x] Full local `pdflatex -> BibTeX -> pdflatex -> pdflatex` compile gate passed.
- [x] Rev11 final rendered-page visual inspection: **12/12 pages PASS at 200 dpi**.
- [x] Rev11 final PDF/source package checksums recorded.
- [x] Fresh compile from self-contained source package: **PASS**.
- [x] Original/fresh source-package PDF render comparison: **0 changed pixels on all 12 pages**.

Final local PDF:

- pages: **12**;
- size: **452,384 bytes**;
- SHA-256: `5e0ac0132a7f4a3f7b07e9c4ba86b046b23bc89c1f7635efe9f737019396d0f0`.

Source ZIP:

- size: **29,931 bytes**;
- SHA-256: `208fd7a2e932507366797658c84dff1666257477143a433bf81d7741a8d0c8a1`.

Detailed preflight:

`grand_challenge/notes/MANUSCRIPT_REV11_ANHARMONIC_PREFLIGHT_2026-08-22.md`.

The current connector does not expose the relevant branch-push GitHub Actions run. Do not represent the remote run as inspected; the full equivalent local generation/build/render gate passed and this is not a separate research-completion blocker.

Administrative facts not supplied by the user remain placeholders. Do not invent affiliation, funding, conflicts, or submission history.

## Current action

**Freeze Rev11.** Do not add the optional finite-amplitude trace-distance result, optimize constants, or broaden the extremizer converse unless a concrete mathematical defect, priority collision, substantive referee objection, build/render regression, or unavoidable journal-format issue appears.
