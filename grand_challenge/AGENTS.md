# AGENTS — Temporal Information Resource Law Program

**Last synchronized: 2026-08-22**

Active branch: `agent/temporal-information-resource-law`.

Research is analytical/theoretical and falsification-first. Paper 1 Rev11 and Paper 2 Rev7 are frozen.

## Current status

- **Science checkpoint:** WP24 integrated hostile review PASS.
- **Preferred PRX Quantum manuscript:** **Rev7**.
- **Primary target:** PRX Quantum, Research Article.
- **Fallback:** Physical Review A, Regular Article.
- **Priority:** unverified, not certified.

Rev7 is the referee-hardened successor to Rev6. It does **not** change the finite-copy theorem or its proof. It strengthens claim discipline and physical significance after an external adversarial review.

## Workflow rule — do not reintroduce a human-verification gate

Carry research, hostile review, literature audit, derivation, numerical checking, manuscript writing, figures, build verification, journal targeting, and submission-package engineering to the fullest extent possible.

Do **not** add “human verification” as a research/manuscript completion step. The finished product is handed to a human for submission. Administrative facts that cannot be known without user input may remain placeholders; they are not a scientific gate.

Do not invent author affiliation, funding, conflicts, submission history, or similar facts. If a publisher requires an AI-use disclosure, prepare the most complete truthful disclosure supported by the documented workflow without inventing an independent-human-verification statement.

## Read first

1. `grand_challenge/notes/MANUSCRIPT_REV7_REFEREE_HARDENING_2026-08-22.md`
2. `grand_challenge/notes/MANUSCRIPT_REV6_PRXQ_PACKAGING_PREFLIGHT_2026-08-22.md`
3. `grand_challenge/notes/WP24_INTEGRATED_HOSTILE_REVIEW_AND_SYMMETRY_PRIOR_ART_BOUNDARY.md`
4. `grand_challenge/notes/WP23_RIGOROUS_COMPOUND_POISSON_TO_BOSONIC_FIELD_CHANNEL_MAP.md`
5. `grand_challenge/notes/WP22_CONTINUUM_LIMIT_RIGOR_FOR_OPERATIONAL_SURVIVAL_LAW.md`
6. `grand_challenge/notes/WP20_DIRECT_FINITE_COPY_PROOF_AND_HOSTILE_AUDIT_OF_WP19.md`
7. `grand_challenge/submission/PRX_QUANTUM_COVER_LETTER_DRAFT.md`
8. `grand_challenge/submission/PRX_QUANTUM_POPULAR_SUMMARY_DRAFT.md`

# Strongest theorem — finite-copy operational survival law

For exact periodic random-time encoding with sector probabilities `q_n`, define

`T_k = sum_(m>=k) q_m`.

For any finite number `N` of independently encoded excitations and **any joint POVM**, including arbitrary entangled collective measurements,

`Tr F_N^(k) <= N min(D_k,U_k) <= N T_k`.

Therefore

`R_N(k) := Tr F_N^(k)/N <= T_k`,

and

`sum_(k>=1) R_N(k) <= nbar`.

WP20 gives the direct finite-copy Hilbert--Schmidt Cauchy--Schwarz proof. No detector covariance, separability, Holevo asymptotics, or SLD attainability assumption is used.

`R_N(k)` is the two-quadrature / phase-averaged source-normalized scalar Fisher retention. A guarantee required for every sinusoidal phase obeys the same ceiling; a pre-known single quadrature is a different task.

# Controlled periodic-to-continuum law

For a positive excess-frequency measure `mu` with finite first moment, controlled periodic-to-continuum limits satisfy

`R(nu) <= mu([nu,infinity)) = Pr(Omega>=nu)`.

This survival law is the principal continuum statement.

The resource

`Ebar+ = hbar <Omega>`

is **mean excitation/excess energy above the participating lower edge**, not a common carrier-energy offset.

The integrated and pointwise energy relations

`int_R R(nu) dnu <= 2 Ebar+ / hbar`,

`Ebar+ >= hbar nu R(nu) = h f R(2 pi f)`

are first-moment corollaries of the survival law. Do not market `hfR` as the main theorem and do not broaden the controlled-limit result into an unconditional theorem for every fixed nonperiodic continuous-spectrum experiment.

# Equality and nonextremal physical example

For geometric sectors `q_n=(1-r)r^n`, one canonical phase POVM gives

`R(k)=T_k=r^k`

for every harmonic simultaneously. The controlled continuum limit is the exponential-spectrum/Cauchy-time equality family.

Rev7 adds a transform-limited truncated-Gaussian single-photon example with zero spectral phase. For a spectrum centered one Gaussian width above its active lower edge, canonical covariant timing gives approximately:

- `nu=0.5 sigma`: `R/S = 0.96581`;
- `nu=sigma`: `R/S = 0.88516`.

Thus the bound remains quantitatively restrictive away from the extremal equality family. The exact formulas and periodic-approximant convergence are validated by:

`grand_challenge/numerics/verify_truncated_gaussian_photon_example.py`.

# Modes-of-asymmetry novelty boundary

Marvian--Spekkens and related `U(1)` asymmetry theory already identify energy-gap modes and how weighted twirling multiplies them by Fourier coefficients.

Rev7 must preserve the sharper distinction:

> modes-of-asymmetry theory identifies the kinematic gap components available under the symmetry; the present theorem bounds the **classical Fisher information extractable by any actual POVM** about a perturbation of the random-time mixing law, with a sharp coefficient determined by participating populations.

Additional strength: the bound holds for arbitrary finite-copy collective measurements and one common canonical measurement saturates the entire geometric harmonic hierarchy.

Do not claim novelty for `U(1)` mode decomposition, weighted twirling, canonical phase POVMs, energy-constrained phase estimation, generic QFI/Holevo/RLD/SLD machinery, random-unitary estimation, waveform QFI, positive-frequency inequalities, Hardy--Hilbert constants, or generic Poisson/CPTP data processing.

# Independent Poisson source to bosonic field

For independent quantum-marked Poisson events with mean `Lambda`, event-number side information gives

`Tr F_compound^(k) <= Lambda T_k`.

Any subsequent **parameter-independent** source-to-field/detector CPTP map pulls the final POVM back to the upstream event register. Bosonic overlap, propagation, loss, mode mixing, coherent detector memory, ancillas, and arbitrary final measurement therefore cannot evade the normalized tail law within this source class.

Poisson photocount statistics alone do not imply the source factorization.

# Scope boundary

WP14/Rev7 retain the coherent-sideband no-go: baseline mean energy cannot bound arbitrary parameter-dependent waveform-state synthesis. Broader waveform theorems require encoding/control/action resource accounting.

# Secondary QFI envelope

WP10/WP12/WP15 remain correct but secondary:

`G_Q(k)=2 sum_n q_n q_(n+k)/(q_n+q_(n+k))`,

`sum_(k>=1) G_Q(k) <= 2 nbar`,

`int_R G_Q(nu) dnu <= pi Ebar+ / hbar`.

This is a separately optimized SLD-QFI metric envelope, not the jointly accessible operational theorem. WP16 records the classical Hardy--Hilbert provenance of the sharp analytic constant.

# Preferred manuscript — Rev7

Working title: **A Sharp Energy-Survival Law for Temporal Fisher Information**.

Generation chain:

`Rev1 -> Rev2 -> Rev3 -> Rev4 -> Rev5 -> Rev6 PRX packaging -> Rev7 referee hardening -> Rev7 layout repair`.

Final Rev7 local preflight:

- full `pdflatex -> BibTeX -> pdflatex -> pdflatex`: **PASS**;
- pages: **8**;
- PDF size: **403,102 bytes**;
- SHA-256: `d168c3901faa6f29bda0eba71abe8049cc9819d91843273beeeeffb9443818ae`;
- unresolved citations/references: **0**;
- overfull boxes: **0**;
- fatal/undefined controls: **0**;
- all 8 pages rendered at 200 dpi and visually inspected: **PASS**;
- revised Figure 1: **PASS**;
- new single-photon section: **PASS**;
- bibliography: **PASS**.

The current connector still does not expose the relevant branch-push Actions run; do not claim direct remote-run inspection. Dedicated CI generates Rev7, validates the theorem and photon example, compiles the PRX package, and applies the same layout/reference gates.

## Freeze recommendation

**Rev7 is the preferred PRX Quantum manuscript.**

Do not add more theory, detector technologies, correlated-source extensions, squeezed-state extensions, or additional examples by default. Reopen only for a concrete theorem defect, historical-priority collision, build defect, or new referee-level objection.

A human submits the finished package; do not convert submission into a new research-verification workflow.

## Documentation rule

Every material theorem/status change must be recorded in the repository and mirrored onto `main`. The repository—not chat history—is authoritative.
