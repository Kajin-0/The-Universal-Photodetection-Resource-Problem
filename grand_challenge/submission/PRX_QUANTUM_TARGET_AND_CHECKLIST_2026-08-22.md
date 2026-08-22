# PRX Quantum Target Decision and Submission Checklist

**Updated:** 2026-08-22

**Science frontier:** WP27

**Preferred submission manuscript:** **Rev10 — Spectral Resource Laws for Temporal Fisher Information**.

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

## Submission materials and publication gate

- [x] Rev10 cover letter updated.
- [x] Rev10 Popular Summary updated.
- [x] AI-use / Data Availability disclosure draft retained.
- [x] Bibliography includes current 2026 temporal-Fisher/time-frequency literature and Berry--Wiseman provenance for the sine-state witness.
- [x] WP25/WP26/WP27 theorem notes committed.
- [x] Rev10 deterministic generator committed and proposition-environment compile defect repaired.
- [x] Rev10 numerical sharpness validator committed and passed locally.
- [x] Full local `pdflatex -> BibTeX -> pdflatex -> pdflatex` compile gate passed.
- [x] Rev10 final rendered-page visual inspection recorded: 11/11 pages PASS at 200 dpi.
- [x] Rev10 final PDF/source package checksums recorded.

Final local PDF:

- pages: **11**;
- size: **444,063 bytes**;
- SHA-256: `a5c2d9e12bba045b76bbfb710428e5424e2c5cb5eb83d6aec6215a5996dbc6fb`.

Minimal source ZIP SHA-256:

`cfa2452f9ce4e99d0cd56f931151f6bb166fd90d4332d86faf3ea2485dec1db9`.

Detailed preflight:

`grand_challenge/notes/MANUSCRIPT_REV10_REFEREE_CLOSURE_PREFLIGHT_2026-08-22.md`.

The current connector does not expose branch-push GitHub Actions runs through its available run lookup. Do not represent the remote run as inspected; the full equivalent generation/build/render gate passed locally and this is not a separate research-completion blocker.

Administrative facts that cannot be known without user input remain placeholders. Do not invent affiliation, funding, conflicts, or submission history.

## Current action

**Freeze Rev10.** Do not start a new prefactor-optimization project or add another example unless a concrete mathematical defect, priority collision, build/journal-format issue, or new referee-level objection appears.
