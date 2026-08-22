# PRX Quantum Target Decision and Submission Checklist

**Updated:** 2026-08-22

**Science frontier:** WP27

**Preferred submission manuscript:** **Rev10 — Spectral Resource Laws for Temporal Fisher Information** once the Rev10 CI/build/render gate passes.

## Decision

### First target: PRX Quantum — Research Article

PRX Quantum is now well justified on an **exceptional connection / exceptional insight** case. The manuscript combines:

- a sharp finite-copy arbitrary-POVM Fisher-tail ceiling;
- controlled continuum spectral-survival law;
- a Herglotz/Toeplitz consistency law for one fixed one-copy measurement across all harmonics;
- divergent near-lossless energetic cost;
- proof that the `(1-R)^(-1/2)` divergence exponent is sharp;
- complete one-copy saturation classification by geometric mixtures / Hausdorff moments;
- a completely monotone continuum equality cone;
- quantitative tightness for a smooth truncated-Gaussian single photon;
- source-to-record inheritance for independent quantum-marked Poisson sources.

### Fallback

Physical Review A — Regular Article.

Do not force a PRL rewrite by hiding assumptions or proof structure.

## Claim hierarchy

### Finite-copy theorem

For exact periodic random-time encoding,

`Tr F_N^(k)/N <= min(D_k,U_k) <= T_k`

for any finite number of independently encoded copies and any joint POVM, including entangled collective measurements.

### Controlled continuum survival law

`R(nu) <= Pr(Omega>=nu)`.

`Ebar+=hbar<Omega>` is mean excess energy above the participating lower edge. `hfR` and the area law are first-moment corollaries.

### Fixed-one-copy common-measurement law

For one fixed one-copy POVM,

`R_M(k)=int cos(k theta) J_M(dtheta)`.

Therefore the retention sequence is positive definite and its Toeplitz matrices are PSD.

With `q=R_M(nu)`,

`Ebar+ >= hbar nu A(q)`,

`A(q) ~ 1/sqrt(2(1-q))`.

This divergence statement must always retain the **fixed one-copy/common-POVM** qualifier.

For the continuum Herglotz extension, the controlled limit must be normalized positive definite **and continuous at the origin** before Bochner is invoked.

### Sharp exponent

The finite sine profile

`a_n=sqrt(2/(L+1)) sin((n+1)pi/(L+1))`

under canonical phase measurement has

`R_L(1)=cos^2(pi/(L+1))`,

`nbar_L=(L-1)/2`,

hence

`nbar_L ~ pi/[2 sqrt(1-R_L(1))]`.

Therefore the inverse-square-root divergence exponent is sharp. Do **not** claim the globally optimal asymptotic constant.

### Complete extremizers

On the full contiguous pure-sector one-copy chain with positive populations:

`first-harmonic saturation`

`<=> geometric-mixture populations`

`<=> Hausdorff-moment tails`

`<=> one source-adapted POVM saturates every harmonic simultaneously`.

No converse is claimed for arbitrary entangled `N>1` collective POVMs, sparse spectra, or arbitrary mixed sector blocks.

## Prior-art discipline

Do not claim novelty for:

- `U(1)` mode decomposition / weighted twirling;
- Herglotz or Bochner theorems;
- Hausdorff or Bernstein--Widder moment theory;
- geometric/exponential mixtures;
- canonical phase POVMs;
- finite sine states;
- generic QFI/Holevo/RLD/SLD machinery;
- generic Poisson/CPTP data processing.

Berry--Wiseman 2000 is cited for the established sine-state phase-estimation construction. Its role here is only as a sharpness witness for the new retention--energy divergence law.

**Priority remains unverified, not certified.**

## Rev10 package

Generation chain:

`Rev1 -> Rev2 -> Rev3 -> Rev4 -> Rev5 -> Rev6 -> Rev7 -> Rev8 -> Rev9 spectral theory -> Rev9 abstract compression -> Rev10 referee closure`.

Rev10 generator:

`grand_challenge/manuscript/apply_rev10_referee_closure.py`

Validation scripts:

- `grand_challenge/numerics/verify_operational_tail_bound.py`
- `grand_challenge/numerics/verify_truncated_gaussian_photon_example.py`
- `grand_challenge/numerics/verify_complete_monotone_saturation.py`
- `grand_challenge/numerics/verify_herglotz_high_retention.py`
- `grand_challenge/numerics/verify_sine_profile_divergence_sharpness.py`

Dedicated CI generates Rev10, compiles the PRX source, and rejects unresolved references, overfull boxes, loss of the local-Fisher qualifier, loss of one-copy/common-POVM scope, missing continuity-at-zero before Bochner, missing sharp-exponent proposition, or regression to the invalid recycled-cosine-lobe claim.

## Submission materials

- [x] Rev10 cover letter updated.
- [x] Rev10 Popular Summary updated.
- [x] AI-use / Data Availability disclosure draft retained.
- [x] Bibliography includes current 2026 temporal-Fisher/time-frequency literature and Berry--Wiseman provenance for the sine-state witness.
- [x] WP25/WP26/WP27 theorem notes committed.
- [x] Rev10 deterministic generator committed.
- [x] Rev10 numerical sharpness validator committed.
- [ ] Rev10 CI compile gate confirmed.
- [ ] Rev10 final rendered-page visual inspection recorded.
- [ ] Rev10 final PDF/source package checksum recorded.

Administrative facts that cannot be known without user input remain placeholders. Do not invent affiliation, funding, conflicts, or submission history.

## Current action

Complete the three unchecked mechanical gates above. If they pass, **freeze Rev10**. Do not start a new prefactor-optimization project or add another example unless a concrete mathematical or referee-level issue appears.
