# AGENTS — Temporal Information Resource Law Program

**Last synchronized: 2026-08-22**

Active branch: `agent/temporal-information-resource-law`.

Research is analytical/theoretical and falsification-first. Paper 1 Rev11 and Paper 2 Rev7 remain frozen.

## Current status

- **Science frontier:** WP27.
- **Preferred PRX Quantum manuscript:** **Rev10 — frozen**.
- **Working title:** **Spectral Resource Laws for Temporal Fisher Information**.
- **Primary target:** PRX Quantum, Research Article.
- **Fallback:** Physical Review A, Regular Article.
- **Priority:** unverified, not certified.

Rev9 changed the significance class by adding common-measurement cross-frequency structure and a complete one-copy extremizer classification. Rev10 closes the final external-review issues: Bochner continuity at zero, explicit one-copy/common-POVM scope, and a proof that the near-lossless `(1-R)^(-1/2)` energy-divergence exponent is sharp using a finite-chain sine-profile witness.

The full Rev10 local publication gate passed: 11 pages, zero unresolved references/citations, zero overfull boxes, all pages rendered at 200 dpi and inspected, and the sine-profile sharpness validator passed. The GitHub connector does not expose branch-push Actions runs, so no direct remote-run result is claimed or required as a new completion gate.

## Workflow rule

Carry theorem development, hostile review, literature audit, numerical validation, manuscript drafting, figures, build verification, journal targeting, and submission-package engineering as far as possible. Do not reintroduce a separate human-verification research gate. A human receives and submits the finished package. Do not invent affiliation, funding, conflicts, submission history, or other unknown administrative facts.

## Read first

1. `grand_challenge/notes/MANUSCRIPT_REV10_REFEREE_CLOSURE_PREFLIGHT_2026-08-22.md`
2. `grand_challenge/notes/WP27_SHARP_HIGH_RETENTION_EXPONENT_AND_REV10_REFEREE_CLOSURE.md`
3. `grand_challenge/notes/MANUSCRIPT_REV9_SPECTRAL_RESOURCE_PREFLIGHT_2026-08-22.md`
4. `grand_challenge/notes/WP26_HERGLOTZ_COMMON_MEASUREMENT_RETENTION.md`
5. `grand_challenge/notes/WP25_COMPLETE_MONOTONE_SATURATION_CLASSIFICATION.md`
6. `grand_challenge/notes/WP24_INTEGRATED_HOSTILE_REVIEW_AND_SYMMETRY_PRIOR_ART_BOUNDARY.md`
7. `grand_challenge/notes/WP23_RIGOROUS_COMPOUND_POISSON_TO_BOSONIC_FIELD_CHANNEL_MAP.md`
8. `grand_challenge/notes/WP22_CONTINUUM_LIMIT_RIGOR_FOR_OPERATIONAL_SURVIVAL_LAW.md`
9. `grand_challenge/notes/WP20_DIRECT_FINITE_COPY_PROOF_AND_HOSTILE_AUDIT_OF_WP19.md`

# I. Finite-copy operational survival law

For exact periodic random-time encoding with sector probabilities `q_n`, define

`T_k = sum_(m>=k) q_m`.

For any finite number `N` of independently encoded excitations and **any joint POVM**, including arbitrary entangled collective measurements,

`Tr F_N^(k) <= N min(D_k,U_k) <= N T_k`.

Thus

`R_N(k) := Tr F_N^(k)/N <= T_k`,

and

`sum_(k>=1) R_N(k) <= nbar`.

This is the most general operational theorem in the paper. It does not require detector covariance, separable measurement, Holevo asymptotics, or SLD attainability.

# II. Controlled continuum survival law

For a positive excess-frequency measure `mu` with finite first moment, controlled periodic-to-continuum limits satisfy

`R(nu) <= mu([nu,infinity)) = Pr(Omega>=nu)`.

The resource

`Ebar+ = hbar <Omega>`

is mean excitation/excess energy above the participating lower edge, not common carrier energy. The relations

`int_R R(nu)dnu <= 2 Ebar+/hbar`,

`Ebar+ >= hbar nu R(nu) = h f R(2 pi f)`

are first-moment corollaries. The theorem is local in the waveform-perturbation parameters and is not a global finite-amplitude risk theorem.

# III. Fixed one-copy common-measurement spectral consistency

For **one fixed one-copy POVM** used to evaluate all harmonics, define `R_M(0)=1` and extend evenly. Then

`R_M(k) = int cos(k theta) J_M(dtheta)`

for a symmetric probability measure `J_M` on the circle. Therefore every Toeplitz matrix

`[R_M(i-j)]`

is positive semidefinite.

The information retained at different temporal harmonics by one actual detector record cannot be chosen independently.

For `q=R_M(k)` and `theta_q=arccos q`,

`R_M(mk) >= cos(m theta_q)`

while `m theta_q <= pi/2`.

Combining this forced retention ladder with the semibounded energy tails gives

`nbar >= k A(q)`,

`Ebar+ >= hbar nu A(q)`,

where

`A(q)=sum_(m=1)^(floor(pi/(2 arccos q))) cos(m arccos q)`.

As `q -> 1`,

`A(q) ~ 1/sqrt(2(1-q))`.

Hence, for the fixed-one-copy/common-POVM setting,

`Ebar+ >= hbar nu / sqrt(2(1-R)) [1+o(1)]`.

Exact unit retention at nonzero harmonic is impossible for a normalized semibounded source.

For the continuum Herglotz extension, invoke Bochner only when the controlled limit is normalized positive definite **and continuous at the origin**.

# IV. Sharpness of the high-retention exponent

WP27/Rev10 uses the finite sine profile

`a_n = sqrt(2/(L+1)) sin((n+1) pi/(L+1))`, `n=0,...,L-1`.

With the canonical phase POVM,

`R_L(1)=cos^2(pi/(L+1))`,

`nbar_L=(L-1)/2`,

so exactly

`nbar_L = pi/[2 arccos sqrt(R_L(1))] - 1`

and asymptotically

`nbar_L ~ pi/[2 sqrt(1-R_L(1))]`.

Therefore the `(1-R)^(-1/2)` divergence exponent is **sharp**. Do not claim the optimal asymptotic prefactor: the universal lower constant and sine-family achievability constant do not coincide.

The sine state itself is established phase-estimation prior art (Berry--Wiseman 2000); its new role here is only as a sharpness witness for the retention--energy law.

# V. Complete one-copy extremizers

On the full contiguous pure-sector chain with `q_n>0`, the following are equivalent:

1. some POVM attains `Tr F_1^(1)=T_1`;
2. `q_n` is a mixture of geometric pmfs,
   `q_n=int (1-r)r^n pi(dr)`;
3. `T_k` is a Hausdorff moment sequence,
   `T_k=int r^k pi(dr)`;
4. one common source-adapted POVM saturates `Tr F_1^(k)=T_k` for every harmonic simultaneously.

With finite mean, the all-mode budget is saturated too. The product POVM gives finite-copy sufficiency. **No converse is claimed for arbitrary entangled `N>1` collective POVMs, sparse spectra, or arbitrary mixed sector blocks.**

Controlled continuum limits of exponential mixtures give the completely monotone equality cone. Gamma mixing gives algebraic exact equality laws.

# VI. Physical embedding and boundary

Independent quantum-marked Poisson events inherit the modewise survival law. Any subsequent **parameter-independent** source-to-field/detector CPTP map is data processing, so bosonic overlap, propagation, loss, mode mixing, coherent detector memory, ancillas, and arbitrary final measurement cannot evade the normalized source ceiling within this source class.

WP14 retains the coherent-sideband no-go: baseline mean energy alone cannot bound arbitrary parameter-dependent waveform-state synthesis. Broader waveform laws require encoding/control/action resource accounting.

# VII. Prior-art boundary

Do not claim novelty for:

- `U(1)` mode decomposition or weighted twirling;
- Herglotz/Bochner theorems;
- Hausdorff moment or Bernstein--Widder theory;
- geometric/exponential mixtures;
- unilateral-shift eigenvectors;
- canonical phase POVMs or sine states;
- energy-constrained phase estimation;
- generic QFI/Holevo/RLD/SLD machinery;
- generic Poisson/CPTP data processing.

Candidate contribution is the operational combination: arbitrary-POVM Fisher-tail coefficients, fixed-measurement positive-definite retention geometry, semibounded-energy near-lossless divergence, sharp exponent, complete one-copy saturation classification, and source-to-record inheritance.

**Priority remains unverified, not certified.**

# Rev10 generation and validation

Generation chain:

`Rev1 -> Rev2 -> Rev3 -> Rev4 -> Rev5 -> Rev6 -> Rev7 -> Rev8 -> Rev9 spectral theory -> Rev9 abstract compression -> Rev10 referee closure`.

Rev10 generator:

`grand_challenge/manuscript/apply_rev10_referee_closure.py`

Numerical gates:

- `verify_operational_tail_bound.py`
- `verify_truncated_gaussian_photon_example.py`
- `verify_complete_monotone_saturation.py`
- `verify_herglotz_high_retention.py`
- `verify_sine_profile_divergence_sharpness.py`

Final local Rev10 preflight:

- full LaTeX/BibTeX build: **PASS**;
- pages: **11**;
- PDF size: **444,063 bytes**;
- PDF SHA-256: `a5c2d9e12bba045b76bbfb710428e5424e2c5cb5eb83d6aec6215a5996dbc6fb`;
- unresolved references/citations: **0**;
- overfull boxes: **0**;
- all pages rendered at 200 dpi and visually inspected: **PASS**;
- sine-profile sharpness validator: **PASS**;
- minimal source ZIP SHA-256: `cfa2452f9ce4e99d0cd56f931151f6bb166fd90d4332d86faf3ea2485dec1db9`.

The dedicated GitHub Actions workflow generates and compiles Rev10 and explicitly rejects loss of the continuity-at-zero hypothesis, one-copy/common-POVM scope, sharp-exponent proposition, local-Fisher qualifier, and prior Herglotz hostile-audit fixes. The current connector does not expose the branch-push run, so do not claim direct remote-run inspection.

## Freeze rule

**Rev10 is frozen as the preferred PRX Quantum manuscript.** Do not optimize the asymptotic constant, add another example, or broaden the source class by default. Reopen only for a concrete referee objection, mathematical defect, priority collision, build defect, or unavoidable journal-format requirement.

## Documentation rule

Every material theorem/status change must be recorded in the repository and mirrored onto `main`. The repository—not chat history—is authoritative.
