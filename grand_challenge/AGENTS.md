# AGENTS — Temporal Information Resource Law Program

**Last synchronized: 2026-08-22**

Active branch: `agent/temporal-information-resource-law`.

Research is analytical/theoretical and falsification-first. Paper 1 Rev11 and Paper 2 Rev7 are frozen.

**Grand Challenge science checkpoint:** WP24 integrated hostile review PASS.

**Frozen science content:** Rev4.

**Preferred publication content:** Rev5 — exact Rev4 science plus one conceptual architecture figure and hidden hyperlink decorations.

**Current journal-target package:** **Rev6 PRX Quantum**, a style-only conversion from Rev5 using the REVTeX `prx` option. PRX Quantum is the first target; Physical Review A Regular Article is the preferred fallback.

## Workflow rule — do not reintroduce a human-verification gate

The research/manuscript workflow must be carried through to the fullest extent autonomously: theorem development, hostile review, literature/prior-art audit, numerical validation, manuscript drafting, figure generation, build verification, journal targeting, and submission-package engineering.

Do **not** add “human verification” as a research or manuscript-completion step. The finished product is handed to a human for submission. Administrative fields that cannot be known without user-supplied facts may remain clearly marked, but they are not a scientific verification gate and must not block completion of the paper itself.

Do not claim facts that were never supplied (author affiliation, funding, conflicts, submission history, etc.). Where a publisher requires an AI-use disclosure, prepare the most complete truthful disclosure possible from the documented workflow; do not invent a human-verification statement.

## Read first

1. `grand_challenge/notes/MANUSCRIPT_REV6_PRXQ_PACKAGING_PREFLIGHT_2026-08-22.md`
2. `grand_challenge/submission/PRX_QUANTUM_TARGET_AND_CHECKLIST_2026-08-22.md`
3. `grand_challenge/submission/APS_AI_AND_DATA_DISCLOSURE_DRAFTS.md`
4. `grand_challenge/notes/MANUSCRIPT_REV5_PUBLICATION_PREFLIGHT_2026-08-22.md`
5. `grand_challenge/notes/MANUSCRIPT_REV4_LOCAL_BUILD_AND_HOSTILE_REVIEW_2026-08-22.md`
6. `grand_challenge/notes/MANUSCRIPT_REV4_BIBLIOGRAPHY_PROVENANCE_AUDIT_2026-08-22.md`
7. `grand_challenge/notes/WP24_INTEGRATED_HOSTILE_REVIEW_AND_SYMMETRY_PRIOR_ART_BOUNDARY.md`
8. `grand_challenge/notes/WP23_RIGOROUS_COMPOUND_POISSON_TO_BOSONIC_FIELD_CHANNEL_MAP.md`
9. `grand_challenge/notes/WP22_CONTINUUM_LIMIT_RIGOR_FOR_OPERATIONAL_SURVIVAL_LAW.md`
10. `grand_challenge/notes/WP20_DIRECT_FINITE_COPY_PROOF_AND_HOSTILE_AUDIT_OF_WP19.md`

# Strongest theorem — finite-copy operational survival law

For the exact periodic random-time model with sector probabilities `q_n`, define

`T_k=sum_(m>=k)q_m`.

For any finite number `N` of independently encoded excitations and **any joint POVM**, including arbitrary entangled collective measurements,

`Tr F_N^(k) <= N min(D_k,U_k) <= N T_k`.

Therefore

`R_N(k):=Tr F_N^(k)/N <= T_k`,

and

`sum_(k>=1)R_N(k)<=nbar`.

WP20 gives a direct finite-copy Hilbert--Schmidt Cauchy--Schwarz proof. No detector covariance, separability, Holevo asymptotics, or SLD attainability assumption is used.

## Operational normalization

The latent cosine/sine source Fisher block is `(1/2)I_2`. Thus `R_N(k)` is the **phase-average of the source-normalized scalar Fisher retention**. If scalar retention at least `q` must hold for every sinusoidal phase, the same tail/energy ceiling applies. A pre-known single quadrature is a different task.

# Controlled continuum theorem — WP22

For a positive excitation-frequency probability measure `mu` with finite first moment, exact lower-bin periodic approximants imply for controlled large-period limits

`R(nu)<=mu([nu,infinity))=P(Omega>=nu)`.

Hence

`int_R R(nu)dnu<=2Ebar^+/hbar`,

and

`Ebar^+>=hbar nu R(nu)=h f R(2pi f)`.

Do not broaden this into an unqualified direct theorem for every fixed nonperiodic continuum experiment.

# Equality family

For geometric sectors `q_n=(1-r)r^n`, the canonical phase POVM gives `R(k)=r^k=T_k` for every harmonic simultaneously. In the controlled continuum limit the spectrum is exponential. With `beta=2a`, the associated Cauchy timestamp has characteristic function `exp(-a|nu|)` and Fisher retention `exp(-2a|nu|)`.

# Independent Poisson source to bosonic field — WP23

For independent quantum-marked Poisson events with mean `Lambda`, event-number side information yields

`Tr F_compound^(k)<=Lambda T_k`.

Any subsequent parameter-independent source-to-field/detector CPTP map can be pulled back onto the upstream event register, so bosonic overlap, mode mixing, coherent detector memory, ancillas, and final measurement cannot evade the normalized tail law.

This is an explicit independent-event source class. Poisson photocount statistics alone do not imply it.

# Secondary QFI envelope

WP10/WP12/WP15 remain mathematically correct:

`G_Q(k)=2 sum_n q_nq_(n+k)/(q_n+q_(n+k))`,

`sum_(k>=1)G_Q(k)<=2nbar`,

`int_R G_Q(nu)dnu<=pi Ebar^+/hbar`.

This is a separately optimized SLD-QFI metric envelope, not the headline operational theorem. WP16 establishes that the `pi/4` analytic operator constant is classical Hardy--Hilbert prior art.

# Scope / prior-art boundary

WP14 excludes baseline-energy-only bounds for arbitrary parameter-dependent waveform-state synthesis; the frozen manuscript contains an explicit coherent-sideband counterexample.

Do not claim novelty for weighted `U(1)` twirling, energy-gap modes, canonical phase POVMs, phase estimation under number/energy constraints, generic QFI/SLD/RLD/Holevo bounds, arbitrary collective information inequalities, random-unitary probability estimation, waveform QFI, positive-frequency Gagliardo--Nirenberg inequalities, Hardy--Hilbert beta constants, or generic Poisson/CPTP machinery.

The candidate contribution is narrowly:

> the arbitrary-measurement **classical-Fisher tail/survival law** for Fourier perturbations of a latent random-time distribution, its paired-population/mean-energy evaluation, and its source-to-record consequences.

Targeted searches have not found an exact predecessor. **Priority remains unverified, not certified.**

# Manuscript / submission status

Working title: **A Sharp Energy-Survival Law for Temporal Fisher Information**.

Deterministic chain:

`Rev1 -> Rev2 mechanical -> Rev3 hostile-review repair -> Rev4 science/claim polish -> Rev5 publication figure/link pass -> Rev6 PRX style package`.

Rev5 publication verification:

- complete local LaTeX/BibTeX build: PASS;
- pages: 7;
- unresolved citations/references: 0;
- overfull boxes: 0;
- undefined controls/fatal TeX errors: 0;
- seven-page visual inspection: PASS;
- Figure 1 readability/scope value: PASS;
- bibliography provenance audit: PASS after correction.

Rev6 PRX packaging verification:

- only `pra -> prx` REVTeX journal option changed;
- pages remain 7;
- no overfull boxes or fatal controls in local target-style reproduction;
- visual page-flow regression: none found;
- dedicated CI now generates and compiles Rev6;
- fresh numerical hostile check: 11,825 one-copy and 936 global two-copy random POVMs, no violation; geometric equality verified at machine precision.

The current GitHub connector does not expose the relevant branch-push Actions run, so do not claim direct remote-job inspection.

# Journal target

**First target: PRX Quantum, Research Article.**

Rationale: direct scope fit to quantum metrology/sensing, fundamental quantum information/resource concepts, and photon sources/detectors; no Research Article length limit; strongest defensible pitch is exceptional insight/connection rather than generic photodetection novelty.

**Fallback: Physical Review A, Regular Article.**

PRL is a stretch only after a deliberate Letter rewrite; do not force the current seven-page theorem into the PRL format by hiding essential hypotheses/proofs.

PRX Quantum is fully open access; APS lists a 2026 APC of USD 3,590, subject to institutional agreements/eligible waivers.

# APS AI/data compliance

Prepare the publisher-required disclosure from the documented facts of the workflow. Substantive AI use in this project includes scientific reasoning/literature synthesis, derivation/proof checking, code assistance, manuscript drafting/editing, and conceptual figure development.

Do not introduce a separate “human verification” gate. Do not invent a statement that a human independently verified steps that were not reported. The human receives the finished package and handles submission/administrative attestations.

Data Availability should acknowledge that no experimental data were created while citing a stable public location for the numerical-validation and manuscript/figure source code.

# Publication status

**Science gate: PASSED at WP24 / Rev4.**

**Publication-content preflight: PASSED at Rev5.**

**PRX Quantum style-package preflight: PASSED at Rev6.**

Do not accumulate another theorem or polish revision by default unless a concrete scientific, priority, build, or submission-format defect appears.

## Remaining submission-only fields

These do not block the finished manuscript itself and should not be reframed as scientific verification steps:

1. final author name/order and affiliation(s);
2. contact email and optional ORCID(s);
3. truthful funding/conflict/submission-history metadata;
4. preprint/e-print status if any;
5. stable repository/archive citation for Data Availability;
6. referee recommendations/exclusions if desired;
7. APC coverage/institutional agreement.

The research/manuscript job is complete to the fullest extent possible without inventing administrative facts. A human submits the finished package.

## Documentation rule

Every material theorem/status change must be recorded in a note, reflected in active landing/handoff files, and mirrored onto `main`. The repository—not chat history—must remain sufficient for recovery.