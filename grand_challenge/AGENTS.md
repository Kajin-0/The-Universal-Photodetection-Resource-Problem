# AGENTS — Temporal Information Resource Law Program

**Last synchronized: 2026-08-22**

Active branch: `agent/temporal-information-resource-law`.

Research is analytical/theoretical and falsification-first. Paper 1 Rev11 and Paper 2 Rev7 remain frozen.

## Current status

- **Science frontier:** WP28.
- **Preferred PRX Quantum manuscript:** **Rev11 — frozen**.
- **Working title:** **Spectral Resource Laws for Temporal Fisher Information**.
- **Primary target:** PRX Quantum, Research Article.
- **Fallback:** Physical Review A, Regular Article.
- **Priority:** unverified, not certified.

Rev11 converts the strongest post-Rev10 adversarial objection into a theorem-level strengthening: the arbitrary-POVM modewise Fisher-tail mechanism does **not** require a globally equally spaced Hamiltonian. For an arbitrary semibounded pure-point Hamiltonian, long-window random-time averaging isolates exact Bohr gaps and the same partial-isometry factorization gives a spectral-tail Fisher ceiling. The fixed-one-copy Herglotz/divergence law extends along integer multiples of any chosen Bohr gap. The peripheral separately optimized SLD-QFI section was removed to make room for this result without bloating the manuscript.

Final Rev11 local publication gate: **PASS** — 12 pages, zero unresolved references/citations, zero overfull boxes, all pages rendered at 200 dpi and inspected, all six numerical validators pass. The self-contained source package recompiles to a visually pixel-identical 12-page PDF; differing PDF hashes arise from nondeterministic metadata, not content.

## Workflow rule

Carry theorem development, hostile review, literature audit, numerical validation, manuscript drafting, figures, build verification, journal targeting, and submission-package engineering as far as possible. Do not reintroduce a separate human-verification research gate. A human receives and submits the finished package. Never invent affiliation, funding, conflicts, submission history, or other unknown administrative facts.

## Read first

1. `grand_challenge/notes/MANUSCRIPT_REV11_ANHARMONIC_PREFLIGHT_2026-08-22.md`
2. `grand_challenge/notes/WP28_ANHARMONIC_PURE_POINT_GAP_EXTENSION_AND_CONTINUUM_ATTACK.md`
3. `grand_challenge/notes/MANUSCRIPT_REV10_REFEREE_CLOSURE_PREFLIGHT_2026-08-22.md`
4. `grand_challenge/notes/WP27_SHARP_HIGH_RETENTION_EXPONENT_AND_REV10_REFEREE_CLOSURE.md`
5. `grand_challenge/notes/WP26_HERGLOTZ_COMMON_MEASUREMENT_RETENTION.md`
6. `grand_challenge/notes/WP25_COMPLETE_MONOTONE_SATURATION_CLASSIFICATION.md`
7. `grand_challenge/notes/WP23_RIGOROUS_COMPOUND_POISSON_TO_BOSONIC_FIELD_CHANNEL_MAP.md`
8. `grand_challenge/notes/WP22_CONTINUUM_LIMIT_RIGOR_FOR_OPERATIONAL_SURVIVAL_LAW.md`
9. `grand_challenge/notes/WP20_DIRECT_FINITE_COPY_PROOF_AND_HOSTILE_AUDIT_OF_WP19.md`

# I. Exact periodic finite-copy theorem

For exact periodic random-time encoding with sector probabilities `q_n`, define

`T_k=sum_(m>=k)q_m`.

For any finite number `N` of independently encoded excitations and **any joint POVM**, including arbitrary entangled collective measurements,

`Tr F_N^(k)/N <= min(D_k,U_k) <= T_k`.

Thus

`sum_(k>=1)R_N(k)<=nbar`.

This exact compact formulation is especially useful for simultaneous all-harmonic and extremizer statements.

# II. Arbitrary semibounded pure-point Bohr-gap theorem

Let

`H=E_* I + hbar sum_alpha omega_alpha P_alpha`, `omega_alpha>=0`,

with no commensurability assumption. Fix `nu>0` and use windows

`T_M=2 pi M/nu`.

Long-window averaging dephases unequal energies at baseline and selects only exact Bohr pairs

`omega_beta-omega_alpha=nu`.

The limiting positive-gap tangent is

`A_nu=sum_(alpha,beta: omega_beta-omega_alpha=nu) sqrt(q_alpha q_beta)|phi_beta><phi_alpha|`.

Define the partial isometry

`V_nu=sum_(paired alpha,beta)|phi_beta><phi_alpha|`.

Then

`A_nu=rho0^(1/2)V_nu rho0^(1/2)`

and for every finite `N` and arbitrary joint POVM,

`Tr F_N^(nu)/N <= min(D_nu,U_nu) <= S(nu)=Pr(Omega>=nu)`.

**No global equal spacing or commensurability is required.** If there is no exact Bohr pair at `hbar nu`, the limiting tangent and Fisher response at that gap vanish.

Arbitrary Bohr-frequency decomposition itself is established modes-of-asymmetry / spectral theory. The candidate contribution is the arbitrary-measurement Fisher coefficient and semibounded tail ceiling.

# III. Controlled continuum survival law

For an **arbitrary Borel probability measure** `mu` on `[0,infinity)` with finite first moment, controlled periodic-to-continuum limits satisfy

`R(nu)<=mu([nu,infinity))=Pr(Omega>=nu)`.

No density or smoothness is assumed. Atomic, absolutely continuous, singular-continuous, and mixed measures are allowed.

`Ebar+=hbar<Omega>` is mean excess energy above the participating lower edge. The area and pointwise relations

`int_R R <= 2Ebar+/hbar`,

`Ebar+ >= hbar nu R(nu)=h f R(2pi f)`

are first-moment corollaries.

The genuine continuum qualification is convergence of the chosen physical periodic measurement schemes; the theorem is local in the waveform perturbation and not a global finite-amplitude risk theorem.

# IV. Fixed one-copy common-measurement spectral consistency

For one fixed one-copy POVM in the periodic model,

`R_M(k)=int cos(k theta) J_M(dtheta)`.

Every Toeplitz matrix `[R_M(i-j)]` is PSD. Zero-population completion cannot create Fisher information because `rho0^(1/2)` and the posterior operator measure annihilate every appended null sector.

For `q=R_M(k)` and `theta_q=arccos q`,

`R_M(mk)>=cos(m theta_q)`

on the positive-cosine range. Combining this forced retention ladder with semibounded tails gives

`Ebar+>=hbar nu A(q)`,

`A(q)~1/sqrt(2(1-q))` as `q->1`.

Exact unit retention at nonzero frequency is impossible for a normalized semibounded source.

For an arbitrary pure-point Hamiltonian, partitioning the spectrum into residue classes modulo a chosen `nu` gives the same Herglotz/Toeplitz law across exact gaps `m nu`, and the same near-lossless energy divergence.

For the controlled continuum Herglotz extension, invoke Bochner only when the normalized positive-definite limit is **continuous at the origin**.

# V. Sharp high-retention exponent

The finite sine profile

`a_n=sqrt(2/(L+1)) sin((n+1)pi/(L+1))`

under canonical phase measurement satisfies

`R_L(1)=cos^2(pi/(L+1))`,

`nbar_L=(L-1)/2`,

so

`nbar_L ~ pi/[2 sqrt(1-R_L(1))]`.

Therefore the `(1-R)^(-1/2)` divergence exponent is **sharp**. Do not claim the optimal asymptotic prefactor. The sine state is established phase-estimation prior art; its role here is only as an achievability witness for the new retention-energy law.

# VI. Complete one-copy extremizers — narrower scope

On the **full contiguous pure-sector chain with positive populations**, the following are equivalent:

1. some POVM attains first-harmonic tail equality;
2. the sector population law is a mixture of geometric pmfs;
3. the tail sequence is a Hausdorff moment sequence;
4. one source-adapted POVM saturates every harmonic simultaneously.

With finite mean the all-mode budget is saturated as well. Product measurements give finite-copy sufficiency. **Do not broaden this converse to arbitrary anharmonic spectra, sparse spectra, arbitrary mixed sector blocks, or arbitrary entangled `N>1` equality cases.**

Controlled continuum limits of exponential mixtures give the completely monotone equality cone.

# VII. Physical embedding and boundary

Independent quantum-marked Poisson events inherit the modewise survival law. Arbitrary subsequent **parameter-independent** source-to-field/detector CPTP processing cannot evade the upstream ceiling; this includes bosonic overlap, propagation, loss, mode mixing, coherent detector memory, ancillas, and arbitrary final measurement.

The coherent-sideband no-go remains the explicit boundary: baseline mean energy alone cannot constrain arbitrary parameter-dependent waveform-state synthesis. Broader waveform laws require encoding/control/action resource accounting.

# VIII. Prior-art discipline

Do not claim novelty for:

- arbitrary Bohr-frequency or `U(1)` mode decompositions / weighted twirling;
- random-time dephasing itself;
- Herglotz/Bochner theorems;
- Hausdorff/Bernstein-Widder moment theory;
- geometric or exponential mixtures;
- unilateral-shift eigenvectors;
- canonical phase POVMs or sine states;
- generic QFI/Holevo/RLD/SLD machinery;
- generic Poisson/CPTP data processing.

Candidate contribution: arbitrary-POVM Fisher-tail coefficients, their extension to exact Bohr gaps of arbitrary semibounded pure-point Hamiltonians, fixed-measurement positive-definite retention geometry, sharp near-lossless energy divergence, complete one-copy extremizer classification in the contiguous model, and source-to-record inheritance.

**Priority remains unverified, not certified.**

# IX. Rev11 generation and validation

Generation chain:

`Rev1 -> Rev2 -> Rev3 -> Rev4 -> Rev5 -> Rev6 -> Rev7 -> Rev8 -> Rev9 spectral theory -> Rev9 abstract compression -> Rev10 referee closure -> Rev11 anharmonic extension`.

Generator:

`grand_challenge/manuscript/apply_rev11_anharmonic_extension.py`

Key Rev11 inputs:

- `rev11_anharmonic_extension.tex`
- `rev11_spectral_theorems.tex`
- `figure1_operational_architecture_body_rev11.tex`
- `references_rev11.bib`

Numerical gates:

- `verify_operational_tail_bound.py`
- `verify_truncated_gaussian_photon_example.py`
- `verify_complete_monotone_saturation.py`
- `verify_herglotz_high_retention.py`
- `verify_sine_profile_divergence_sharpness.py`
- `verify_anharmonic_pure_point_gap_extension.py`

Final local preflight:

- full LaTeX/BibTeX build: **PASS**;
- pages: **12**;
- PDF size: **452,384 bytes**;
- PDF SHA-256: `5e0ac0132a7f4a3f7b07e9c4ba86b046b23bc89c1f7635efe9f737019396d0f0`;
- unresolved references/citations: **0**;
- overfull boxes: **0**;
- all pages rendered at 200 dpi and visually inspected: **PASS**;
- source ZIP SHA-256: `208fd7a2e932507366797658c84dff1666257477143a433bf81d7741a8d0c8a1`;
- fresh source-package compile: **PASS**;
- original vs source-package recompile at 200 dpi: **0 changed pages / 0 changed pixels**.

The dedicated workflow now builds Rev11 and regression-tests the anharmonic theorem, continuum-measure scope, null-sector invariance, Bochner continuity, sharp-exponent statement, local-Fisher scope, and removal of the peripheral QFI section. The connector does not expose the relevant branch-push Actions run, so do not claim remote-run inspection.

## Freeze rule

**Rev11 is frozen as the preferred PRX Quantum manuscript.** Do not add the optional finite-amplitude trace-distance observation, optimize constants, or broaden the extremizer theorem by default. Reopen only for a concrete mathematical defect, priority collision, substantive referee objection, build/render regression, or unavoidable journal-format requirement.

## Documentation rule

Every material theorem/status change must be recorded in the repository and mirrored onto `main`. The repository—not chat history—is authoritative.
