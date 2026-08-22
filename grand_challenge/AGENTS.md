# AGENTS — Temporal Information Resource Law Program

**Last synchronized: 2026-08-22**

Active branch: `agent/temporal-information-resource-law`.

Research is analytical/theoretical and falsification-first. Paper 1 Rev11 and Paper 2 Rev7 remain frozen.

## Current status

- **Science checkpoint:** WP24 integrated hostile review PASS.
- **Preferred PRX Quantum manuscript:** **Rev8**.
- **Primary target:** PRX Quantum, Research Article.
- **Fallback:** Physical Review A, Regular Article.
- **Priority:** unverified, not certified.

Rev8 is a one-sentence scope clarification on top of the referee-hardened Rev7. It changes no theorem, proof, coefficient, continuum inequality, equality family, source hypothesis, photon example, or novelty claim.

## Workflow rule

Carry theorem development, hostile review, literature audit, numerical validation, manuscript drafting, figures, build verification, journal targeting, and submission-package engineering to the fullest extent possible. Do not reintroduce a separate human-verification research gate. A human receives and submits the finished package. Do not invent administrative facts such as affiliation, funding, conflicts, or submission history.

## Read first

1. `grand_challenge/notes/MANUSCRIPT_REV8_SECOND_EXTERNAL_REVIEW_RESPONSE_2026-08-22.md`
2. `grand_challenge/notes/MANUSCRIPT_REV7_REFEREE_HARDENING_2026-08-22.md`
3. `grand_challenge/notes/WP24_INTEGRATED_HOSTILE_REVIEW_AND_SYMMETRY_PRIOR_ART_BOUNDARY.md`
4. `grand_challenge/notes/WP23_RIGOROUS_COMPOUND_POISSON_TO_BOSONIC_FIELD_CHANNEL_MAP.md`
5. `grand_challenge/notes/WP22_CONTINUUM_LIMIT_RIGOR_FOR_OPERATIONAL_SURVIVAL_LAW.md`
6. `grand_challenge/notes/WP20_DIRECT_FINITE_COPY_PROOF_AND_HOSTILE_AUDIT_OF_WP19.md`
7. `grand_challenge/submission/PRX_QUANTUM_COVER_LETTER_DRAFT.md`
8. `grand_challenge/submission/PRX_QUANTUM_POPULAR_SUMMARY_DRAFT.md`

# Core theorem

For exact periodic random-time encoding with sector probabilities `q_n`, define

`T_k = sum_(m>=k) q_m`.

For any finite number `N` of independently encoded excitations and **any joint POVM**, including arbitrary entangled collective measurements,

`Tr F_N^(k) <= N min(D_k,U_k) <= N T_k`.

Thus

`R_N(k) := Tr F_N^(k)/N <= T_k`,

and

`sum_(k>=1) R_N(k) <= nbar`.

`R_N(k)` is the two-quadrature / phase-averaged source-normalized Fisher retention. WP20 gives the direct Hilbert--Schmidt Cauchy--Schwarz proof. No covariance, separability, Holevo asymptotics, or SLD attainability assumption is used.

# Controlled periodic-to-continuum law

For a positive excess-frequency measure `mu` with finite first moment, controlled periodic-to-continuum limits satisfy

`R(nu) <= mu([nu,infinity)) = Pr(Omega>=nu)`.

This survival law is the principal continuum theorem. The resource

`Ebar+ = hbar <Omega>`

is **mean excitation/excess energy above the participating lower edge**, not a common carrier offset. The integrated and pointwise relations

`int_R R(nu)dnu <= 2 Ebar+ / hbar`,

`Ebar+ >= hbar nu R(nu) = h f R(2 pi f)`

are first-moment corollaries.

Rev8 makes one further scope point explicit: the theorem is **local in the waveform-perturbation parameters**. It bounds Fisher information at the uniform random-time baseline and does not by itself give a global finite-amplitude estimation-error or risk bound.

# Equality and nonextremal photon example

For geometric sectors `q_n=(1-r)r^n`, one canonical phase POVM gives

`R(k)=T_k=r^k`

for every harmonic simultaneously. The controlled continuum equality family is **exponential excess-frequency / Cauchy timing**.

Do **not** describe this as the ordinary spontaneous-emission Fourier pair. Approximate Weisskopf--Wigner spontaneous emission is commonly Lorentzian in emission frequency and exponential in temporal decay; that is a different pair.

Rev7/Rev8 also contain a transform-limited truncated-Gaussian single-photon example with zero spectral phase. Canonical covariant timing gives approximately:

- `nu=0.5 sigma`: `R/S = 0.96581`;
- `nu=sigma`: `R/S = 0.88516`.

The formulas and periodic-approximant convergence are validated by `grand_challenge/numerics/verify_truncated_gaussian_photon_example.py`.

# Prior-art boundary

Established modes-of-asymmetry theory identifies the `U(1)` gap components available under symmetry. The present theorem instead bounds the **classical Fisher information extractable by any actual POVM** about a perturbation of the random-time mixing law, with a sharp coefficient determined by participating populations.

Do not claim novelty for `U(1)` modes/twirling, canonical phase POVMs, energy-constrained phase estimation, generic QFI/Holevo/RLD/SLD machinery, random-unitary estimation, waveform QFI, positive-frequency inequalities, Hardy--Hilbert constants, or generic Poisson/CPTP data processing.

**Priority remains unverified, not certified.**

# Physical embedding and boundary

For independent quantum-marked Poisson events with mean `Lambda`, event-number side information gives `Tr F_compound^(k) <= Lambda T_k`. Any subsequent **parameter-independent** source-to-field/detector CPTP map pulls the final POVM back to the event register, covering bosonic overlap, propagation, loss, mode mixing, coherent detector memory, ancillas, and arbitrary final measurement within the stated source class.

WP14 retains the explicit coherent-sideband no-go: baseline mean energy alone cannot bound arbitrary parameter-dependent waveform-state synthesis. Broader waveform theorems require encoding/control/action resource accounting.

# Preferred manuscript — Rev8

Working title: **A Sharp Energy-Survival Law for Temporal Fisher Information**.

Generation chain:

`Rev1 -> Rev2 -> Rev3 -> Rev4 -> Rev5 -> Rev6 PRX packaging -> Rev7 referee hardening -> Rev7 layout repair -> Rev8 local-scope clarification`.

Rev8 local preflight:

- full `pdflatex -> BibTeX -> pdflatex -> pdflatex`: **PASS**;
- pages: **8**;
- unresolved citations/references: **0**;
- overfull boxes: **0**;
- fatal/undefined controls: **0**;
- all 8 pages rendered at 200 dpi: **PASS**;
- visual diff against Rev7 changes only pages 7--8 from the added Discussion sentence and bibliography reflow;
- SHA-256 of local Rev8 PDF: `22f64f4760531aa5304d98c418a185bd187d7d07b666f6e1f7b7c1de94a5242a`.

The 2026 Folge et al. reference is verified as *Optica* 13, 548--557 (2026), DOI `10.1364/OPTICA.579459`, and is relevant contemporary time-frequency quantum-metrology literature rather than prior art for the survival theorem.

## Freeze recommendation

**Rev8 is the preferred PRX Quantum manuscript.** Do not add more theory or examples by default. Reopen only for a concrete mathematical defect, historical-priority collision, citation/build defect, or genuinely substantive referee objection.

## Documentation rule

Every material theorem/status change must be recorded in the repository and mirrored onto `main`. The repository, not chat history, is authoritative.
