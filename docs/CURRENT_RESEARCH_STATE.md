# Current Research State

**Last synchronized:** 2026-08-22

**Active scientific branch:** `agent/temporal-information-resource-law`

Paper 1 Rev11 and Paper 2 Rev7 are frozen. The Grand Challenge science checkpoint is **WP24**. **Rev4 is the frozen science-content checkpoint; Rev5 is the preferred frozen publication draft.**

## Read first

1. `grand_challenge/AGENTS.md`
2. `grand_challenge/notes/MANUSCRIPT_REV5_PUBLICATION_PREFLIGHT_2026-08-22.md`
3. `grand_challenge/notes/MANUSCRIPT_REV4_LOCAL_BUILD_AND_HOSTILE_REVIEW_2026-08-22.md`
4. `grand_challenge/notes/MANUSCRIPT_REV4_BIBLIOGRAPHY_PROVENANCE_AUDIT_2026-08-22.md`
5. `grand_challenge/notes/WP24_INTEGRATED_HOSTILE_REVIEW_AND_SYMMETRY_PRIOR_ART_BOUNDARY.md`
6. `grand_challenge/notes/WP23_RIGOROUS_COMPOUND_POISSON_TO_BOSONIC_FIELD_CHANNEL_MAP.md`
7. `grand_challenge/notes/WP22_CONTINUUM_LIMIT_RIGOR_FOR_OPERATIONAL_SURVIVAL_LAW.md`
8. `grand_challenge/notes/WP20_DIRECT_FINITE_COPY_PROOF_AND_HOSTILE_AUDIT_OF_WP19.md`
9. `grand_challenge/notes/WP14_COHERENT_FIELD_BASELINE_ENERGY_NO_GO.md`

# Strongest theorem — operational survival law

For the exact periodic random-time model with sector probabilities `q_n`, define

`T_k=sum_(m>=k)q_m`.

For **any finite N and any joint POVM** on `N` independently encoded excitations,

`Tr F_N^(k)<=N T_k`.

More sharply,

`R_N(k):=Tr F_N^(k)/N<=min(D_k,U_k)<=T_k`.

Summing positive harmonics,

`sum_(k>=1)R_N(k)<=nbar`.

WP20 provides a direct finite-copy Hilbert--Schmidt Cauchy--Schwarz proof including arbitrary entangled collective measurements. The Holevo route of WP19 is superseded.

## Normalization

The latent source cosine/sine Fisher block is `(1/2)I_2`, so `R_N(k)` is the **phase-average of the source-normalized scalar Fisher retention**. A uniform scalar-retention guarantee over every sinusoidal phase obeys the same ceiling. A pre-known single quadrature is a different task.

# Controlled continuum limit — WP22

For a positive excitation-frequency spectral probability measure `mu` with finite mean

`omega_bar=int omega mu(domega)`,

exact lower-bin periodic approximants give, for controlled large-period limits,

`R(nu)<=mu([nu,infinity))=P(Omega>=nu)`.

Therefore

`int_0^infinity R(nu)dnu<=omega_bar`,

`int_R R(nu)dnu<=2Ebar^+/hbar`,

and

`Ebar^+>=hbar nu R(nu)=h f R(2pi f)`.

The manuscript explicitly retains the controlled-limit qualification; do not broaden it into an unqualified direct theorem for every nonperiodic continuous-spectrum detector experiment.

# Equality family

For geometric sectors

`q_n=(1-r)r^n`,

the canonical phase POVM satisfies

`R(k)=r^k=T_k`

for every harmonic simultaneously and saturates the full sum rule.

The controlled continuum limit is exponential in excitation frequency. With `beta=2a`, the corresponding Cauchy timing density has characteristic function `exp(-a|nu|)` and Fisher retention `exp(-2a|nu|)`.

# Independent Poisson event source to physical field — WP23

For an independent quantum-marked compound-Poisson source with mean event count `Lambda`, revealing the parameter-independent event number gives

`Tr F^(k)<=Lambda T_k`.

Any subsequent parameter-independent source/emission/field/detector process is a CPTP map. Pulling the final POVM back through that map proves the same source-normalized tail law after arbitrary bosonic overlap, mode mixing, coherent detector memory, ancillas, and final readout.

This is an explicit independent-event source class. Poisson photocount statistics alone do not imply its assumptions.

# Secondary QFI envelope

WP10/WP12/WP15 remain mathematically correct:

`sum_(k>=1)G_Q(k)<=2nbar`,

`int_R G_Q(nu)dnu<=pi Ebar^+/hbar`.

They are separately optimized SLD-QFI metric envelopes, not the main jointly accessible detector theorem. WP16 identifies the sharp `pi/4` analytic operator norm as classical Hardy--Hilbert mathematics.

# Prior-art boundary

WP21/WP24 and the bibliography audit substantially narrow novelty.

Established prior art includes weighted `U(1)` twirling and energy-gap modes, Fourier/number-constrained phase estimation, canonical phase POVMs, arbitrary collective quantum-information bounds, random-unitary probability estimation, waveform QFI, sharp positive-frequency Gagliardo--Nirenberg analysis, Hardy--Hilbert beta-function best constants, and compound-Poisson/CPTP data processing.

The candidate contribution is specifically the **arbitrary-measurement classical-Fisher ceiling for Fourier perturbations of a latent random-time distribution**, its paired-population/upper-tail evaluation, mean-energy harmonic budget, and source-to-record photodetection consequences.

Targeted searches have not located the exact tail/survival theorem. **Priority remains unverified, not certified.**

# Scope boundary

WP14 remains mandatory. Baseline mean energy cannot bound arbitrary parameter-dependent coherent waveform synthesis. The frozen science content includes an explicit coherent-sideband counterexample; broader waveform theorems need encoding/control/action resource accounting.

# Preferred publication manuscript — Rev5

Working title: **A Sharp Energy-Survival Law for Temporal Fisher Information**.

Generation chain:

`Rev1 -> Rev2 mechanical -> Rev3 hostile-review repair -> Rev4 science/claim polish -> Rev5 publication figure/hidelinks`.

**Rev4 freezes the science content. Rev5 changes no theorem, proof, coefficient, source hypothesis, or novelty claim.** Rev5 adds one conceptual two-column figure explaining the parameter-entry/source-to-record architecture and hides hyperlink decorations.

Rev5 verification:

- full local `pdflatex -> BibTeX -> pdflatex -> pdflatex`: PASS;
- 7 pages, 393.5 kB in the final reproduced build;
- unresolved citations/references: 0;
- overfull boxes: 0;
- undefined controls/fatal errors: 0;
- residual APS-incompatible `boxed` markup: 0;
- seven-page render/visual inspection: PASS;
- Figure 1 readability/scope value: PASS;
- deterministic random-POVM theorem validation: PASS;
- DOI/title/provenance bibliography audit: PASS after correction.

The remote branch-push GitHub Actions run is not directly visible through the current connector. Equivalent full local build verification is complete; do not claim remote-job inspection unless it later becomes available.

# Publication gate

**PASSED.**

Rev5 is the preferred frozen publication draft. Reopen science only for a concrete theorem defect, priority collision, build failure, or referee-level objection.

## Immediate next action

1. no new theorem accumulation by default;
2. journal targeting and submission engineering;
3. prepare submission metadata/compliance only from factual information;
4. retain conservative priority language;
5. inspect remote CI only if it becomes accessible.

## Documentation rule

Every material result/status change must update the detailed note, active handoff/landing documents, and `main`. The repository—not chat history—is authoritative.