# AGENTS — Temporal Information Resource Law Program

**Last synchronized: 2026-08-22**

Active branch: `agent/temporal-information-resource-law`.

Research is analytical/theoretical and falsification-first. Paper 1 Rev11 and Paper 2 Rev7 are frozen.

**Grand Challenge science checkpoint:** WP24 integrated hostile review PASS.

**Preferred science content:** Rev4.

**Preferred publication draft:** **Rev5** — exact Rev4 science plus one conceptual architecture figure and hidden hyperlink decorations; locally build-verified, visually inspected, bibliography-audited, and frozen unless a concrete theorem, priority, build, or referee-level defect is found.

## Read first

1. `grand_challenge/notes/MANUSCRIPT_REV5_PUBLICATION_PREFLIGHT_2026-08-22.md`
2. `grand_challenge/notes/MANUSCRIPT_REV4_LOCAL_BUILD_AND_HOSTILE_REVIEW_2026-08-22.md`
3. `grand_challenge/notes/MANUSCRIPT_REV4_BIBLIOGRAPHY_PROVENANCE_AUDIT_2026-08-22.md`
4. `grand_challenge/notes/WP24_INTEGRATED_HOSTILE_REVIEW_AND_SYMMETRY_PRIOR_ART_BOUNDARY.md`
5. `grand_challenge/notes/WP23_RIGOROUS_COMPOUND_POISSON_TO_BOSONIC_FIELD_CHANNEL_MAP.md`
6. `grand_challenge/notes/WP22_CONTINUUM_LIMIT_RIGOR_FOR_OPERATIONAL_SURVIVAL_LAW.md`
7. `grand_challenge/notes/WP20_DIRECT_FINITE_COPY_PROOF_AND_HOSTILE_AUDIT_OF_WP19.md`
8. `grand_challenge/notes/WP14_COHERENT_FIELD_BASELINE_ENERGY_NO_GO.md`

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

WP14 excludes baseline-energy-only bounds for arbitrary parameter-dependent waveform-state synthesis; Rev4/Rev5 contain an explicit coherent-sideband counterexample.

Do not claim novelty for weighted `U(1)` twirling, energy-gap modes, canonical phase POVMs, phase estimation under number/energy constraints, generic QFI/SLD/RLD/Holevo bounds, arbitrary collective information inequalities, random-unitary probability estimation, waveform QFI, positive-frequency Gagliardo--Nirenberg inequalities, Hardy--Hilbert beta constants, or generic Poisson/CPTP machinery.

The candidate contribution is narrowly:

> the arbitrary-measurement **classical-Fisher tail/survival law** for Fourier perturbations of a latent random-time distribution, its paired-population/mean-energy evaluation, and its source-to-record consequences.

Targeted searches have not found an exact predecessor. **Priority remains unverified, not certified.**

# Preferred manuscript — Rev5

Working title: **A Sharp Energy-Survival Law for Temporal Fisher Information**.

Deterministic chain:

`Rev1 -> Rev2 mechanical -> Rev3 hostile-review repair -> Rev4 science/claim polish -> Rev5 publication figure/link pass`.

Final Rev5 verification:

- full local `pdflatex -> BibTeX -> pdflatex -> pdflatex`: PASS;
- pages: **7**;
- final local PDF: **393,530 bytes**;
- unresolved citations/references: **0**;
- overfull boxes: **0**;
- undefined controls/fatal TeX errors: **0**;
- APS-incompatible `boxed` markup: **0**;
- `hyperref` decorations hidden: PASS;
- all seven pages rendered at 160 dpi and visually inspected: PASS;
- Figure 1 readable and materially useful without increasing page count;
- bibliography page visually clean;
- deterministic numerical theorem validator committed;
- DOI/title/provenance bibliography audit completed.

Figure 1 summarizes the theorem architecture: latent random-time law -> fixed excitation -> arbitrary parameter-independent field/detector channel -> accessible record -> Fisher tail/energy law, while explicitly marking arbitrary waveform-state synthesis as outside scope.

The current GitHub connector does not expose the relevant branch-push Actions run, so do not claim direct remote-job inspection. Equivalent full local build verification is complete.

# Publication status

**Science gate: PASSED at WP24 / Rev4.**

**Publication preflight: PASSED at Rev5.**

Rev5 is now frozen. Reopen or create Rev6 only for a concrete theorem defect, historical-priority collision, build/rendering defect, referee-level clarity objection, or factual submission requirement that genuinely needs a source change.

## Immediate work order

1. do not accumulate another theorem or polish revision by default;
2. inspect remote Rev5 CI only if it becomes accessible;
3. proceed to journal targeting/submission engineering;
4. retain conservative priority language;
5. add author/funding/disclosure metadata only from factual user-supplied information.

## Documentation rule

Every material theorem/status change must be recorded in a note, reflected in active landing/handoff files, and mirrored onto `main`. The repository—not chat history—must remain sufficient for recovery.
