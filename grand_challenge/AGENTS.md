# AGENTS — Temporal Information Resource Law Program

**Last synchronized: 2026-08-22**

Active branch: `agent/temporal-information-resource-law`.

Research is analytical/theoretical and falsification-first. Paper 1 Rev11 and Paper 2 Rev7 are frozen.

**Grand Challenge science checkpoint:** WP24 integrated hostile review PASS.

**Preferred Grand Challenge manuscript:** Rev4 — locally build-verified, visually inspected, bibliography-audited, and frozen unless a concrete theorem, priority, build, or referee-level defect is found.

## Grand question

> For a physically realizable measurement of temporal structure, what fundamental resources constrain source-to-record temporal Fisher-information transfer?

## Read first

1. `grand_challenge/notes/MANUSCRIPT_REV4_LOCAL_BUILD_AND_HOSTILE_REVIEW_2026-08-22.md`
2. `grand_challenge/notes/MANUSCRIPT_REV4_BIBLIOGRAPHY_PROVENANCE_AUDIT_2026-08-22.md`
3. `grand_challenge/notes/WP24_INTEGRATED_HOSTILE_REVIEW_AND_SYMMETRY_PRIOR_ART_BOUNDARY.md`
4. `grand_challenge/notes/WP23_RIGOROUS_COMPOUND_POISSON_TO_BOSONIC_FIELD_CHANNEL_MAP.md`
5. `grand_challenge/notes/WP22_CONTINUUM_LIMIT_RIGOR_FOR_OPERATIONAL_SURVIVAL_LAW.md`
6. `grand_challenge/notes/WP21_TARGETED_PRIORITY_AUDIT_SURVIVAL_FUNCTION_LAW.md`
7. `grand_challenge/notes/WP20_DIRECT_FINITE_COPY_PROOF_AND_HOSTILE_AUDIT_OF_WP19.md`
8. `grand_challenge/notes/WP19_FULL_COLLECTIVE_SURVIVAL_FUNCTION_RESOURCE_LAW.md`
9. `grand_challenge/notes/WP16_DEEP_PRIORITY_AUDIT_RANDOM_TIME_QFI_AND_HARDY_HILBERT_COLLISION.md`
10. `grand_challenge/notes/WP14_COHERENT_FIELD_BASELINE_ENERGY_NO_GO.md`

WP17/WP18 are useful historical steps toward WP20 but are no longer needed for the strongest proof.

# Current strongest theorem — operational survival law

For a periodic semibounded excitation with total-generator sector probabilities `q_n`, define

`T_k=sum_(m>=k)q_m`.

For **any finite number N of independently random-time-encoded excitations and any joint POVM**, including arbitrary entangled collective measurements,

`Tr F_N^(k) <= N T_k`.

Here `F_N^(k)` is the `2 x 2` classical Fisher block for the cosine/sine amplitudes of temporal harmonic `k` at the uniform random-time baseline.

Therefore

`R_N(k):=Tr F_N^(k)/N <= T_k`,

and

`sum_(k>=1)R_N(k)<=nbar`.

WP20 gives a direct finite-copy Hilbert--Schmidt Cauchy--Schwarz proof. No covariance restriction on the detector, Holevo asymptotics, SLD attainability, or separable-measurement assumption is used.

## Bilateral support refinement

With the paired partial energy shift `V_k`, define

`D_k=Tr(rho P_dom,k)`,

`U_k=Tr(rho P_ran,k)`.

Then

`R_N(k)<=min(D_k,U_k)<=T_k`.

The coarse tail `T_k` is the universal semibounded-energy form; the paired-support form can be tighter for gaps or finite upper support.

## Operational normalization

`R_N(k)=Tr F_N^(k)/N` is the **two-quadrature / phase-averaged** source-normalized Fisher retention because the latent source block is `(1/2)I_2`.

If a detector guarantees scalar retention at least `q` for every sinusoidal phase, then `R_N(k)>=q`, so the same survival/energy ceiling applies. A pre-known single quadrature is a different task and must not be assigned the same coefficient without a separate argument.

# Continuum theorem — WP22 / Rev4 scope

Let `mu` be the positive excitation-frequency spectral probability measure, with finite first moment

`omega_bar=int omega mu(domega)`.

The exact theorem is first stated on the periodic/equally spaced sector model. Using exact lower-bin periodic approximants, **controlled large-period continuum limits** satisfy

`R(nu)<=S_mu(nu):=mu([nu,infinity))`.

Thus

`int_0^infinity R(nu)dnu<=omega_bar`,

and two-sided

`int_R R(nu)dnu<=2Ebar^+/hbar`.

The pointwise inverse law is

`Ebar^+>=hbar nu R(nu)=h f R(2pi f)`.

Hence a phase-averaged or phase-uniform guaranteed retention `q0` at ordinary frequency `B` requires

`Ebar^+>=h B q0`.

Do not rewrite this as an unqualified direct theorem for an arbitrary fixed nonperiodic detector experiment; the manuscript explicitly states the controlled-limit construction.

# Exact equality family

For geometric sectors

`q_n=(1-r)r^n`,

the canonical phase POVM gives

`R(k)=r^k=T_k`

for every harmonic simultaneously, so

`sum_(k>=1)R(k)=nbar`.

Under `r=exp(-beta delta)`, the continuum limit is

`mu(domega)=beta exp(-beta omega)domega`,

`R(nu)=exp(-beta|nu|)=S_mu(|nu|)`.

With `beta=2a`, the corresponding Cauchy timestamp has characteristic function `exp(-a|nu|)` and Fisher retention `exp(-2a|nu|)`.

# Independent Poisson source to physical bosonic field — WP23

For a compound-Poisson source with mean event count `Lambda`, represent independently encoded event marks on the direct-sum event register

`Sigma_epsilon=directsum_N p_Lambda(N) rho_epsilon^tensor N`.

For nonzero temporal Fourier modes, the Poisson number weights are parameter independent. Revealing `N` can only increase FI, so WP20 gives

`Tr F_compound^(k)<=Lambda T_k`.

Any physical source-to-field/emission process whose parameter dependence is already encoded in those event marks is a parameter-independent CPTP map `Gamma` from the upstream event register to the outgoing bosonic field and other downstream degrees of freedom.

Pulling the final detector POVM backward through `Gamma` gives a POVM on the event register. Therefore arbitrary bosonic wavepacket overlap, mode mixing, coherent detector memory, ancillas, and final measurement cannot evade

`R_final(k)<=T_k`

or the controlled-limit continuum survival law.

This does **not** follow merely from Poisson photocount statistics; it is a theorem for an independent quantum-marked event source class.

# Secondary theorem — separately optimized QFI envelope

WP10/WP12/WP15 remain mathematically correct:

`G_Q(k)=2 sum_n q_nq_(n+k)/(q_n+q_(n+k))`,

`sum_(k>=1)G_Q(k)<=2nbar`,

and

`int_R G_Q(nu)dnu<=pi Ebar^+/hbar`.

But this is a separately optimized SLD-QFI envelope, not the headline operational theorem. WP20 proves that one actual detector, even with arbitrary finite-copy collective readout, obeys the smaller sharp operational coefficient `2E/hbar`.

WP16 establishes that the `pi/4` Mellin/operator constant in the continuum QFI proof is classical Hardy--Hilbert mathematics.

# Scope boundary — WP14

The operational survival theorem concerns **random temporal-distribution encoding of a fixed excitation** in the stated periodic/controlled-limit source class.

Baseline mean energy does not constrain arbitrary parameter-dependent coherent waveform synthesis. Rev4 includes the explicit sideband family

`|psi_epsilon> = |alpha>_c tensor |epsilon gamma>_s`,

with `F_Q(0)=4|gamma|^2` independent of sideband detuning while the added sideband energy is quadratic in `epsilon`. A broader state-valued waveform theorem requires explicit encoding/control/action resource accounting.

# Prior-art boundary — WP21/WP24 and Rev4 bibliography audit

Do not claim novelty for:

- `U(1)` energy-gap/modes-of-asymmetry decompositions;
- weighted random phase/time twirling multiplying gap modes by Fourier coefficients;
- canonical phase POVMs or exponential phase moments;
- phase/time estimation under photon-number/energy constraints;
- generic arbitrary-measurement Fisher/Holevo/RLD/SLD bounds;
- random-unitary probability estimation;
- QFI/asymmetry resource theory;
- Hardy--Hilbert/Mellin/rearrangement methods;
- compound Poisson models, Stinespring dilation, or CPTP data processing.

Especially close is Marvian--Spekkens, Phys. Rev. A 90, 062110 (2014): weighted `U(1)` twirling already acts modewise by Fourier coefficients of the mixing law.

The candidate contribution is narrower:

> the arbitrary-measurement classical-Fisher ceiling for perturbations of the latent random-time distribution, whose `k`-mode resource evaluates to paired population mass and hence to the semibounded survival tail, with sharp mean-energy and source-to-record consequences.

Targeted searches have not found an exact predecessor of

`Tr F_N^(k)/N <= sum_(m>=k)q_m`,

its all-mode mean-generator sum rule, or

`R(nu)<=P(Omega>=nu)`.

**Priority remains unverified, not certified.**

# Preferred manuscript — Rev4

Generation chain:

1. `grand_challenge/manuscript/energy_survival_temporal_fisher_rev1.tex`
2. `apply_rev2_mechanical.py`
3. `apply_rev3_hostile_review.py`
4. `apply_rev4_final_polish.py`

Dedicated CI: `.github/workflows/grand-challenge-manuscript-check.yml`.

Rev4 local verification:

- full `pdflatex -> BibTeX -> pdflatex -> pdflatex` PASS;
- 7 pages;
- unresolved citations/references: 0;
- overfull boxes: 0;
- undefined controls/fatal TeX errors: 0;
- rendered and visually inspected: PASS;
- deterministic random-POVM numerical theorem validator committed;
- bibliography DOI/title/provenance audit completed.

Concrete build defects repaired included theorem/proof declarations, APS-incompatible `boxed` markup, an undefined `cK` macro, BibTeX case handling, two-column theorem-heading overflow, and a wrong Pocovnicu title/DOI pairing. The Pocovnicu DOI was scientifically the correct sharp-inequality source; only its title metadata had been wrong.

The GitHub connector does not expose the relevant branch-push workflow run, so do not claim direct remote-job inspection. Equivalent full local build verification is complete.

# Current publication status

**Science manuscript formation gate: PASSED.**

Rev4 is the preferred frozen science draft. Reopen science only for a concrete theorem defect, historical-priority collision, build failure, or referee-level objection.

## Immediate work order

1. do not accumulate another theorem by default;
2. inspect remote Rev4 CI if/when the run becomes accessible;
3. add a figure only if it materially improves comprehension—no decorative figure requirement;
4. prepare journal/submission metadata only from factual user-supplied information;
5. keep priority language conservative until external historical priority is genuinely certified.

## Documentation rule

Every material result or status change must be recorded in a note, reflected in active landing/handoff files, and mirrored onto `main`. The repository—not chat history—must remain sufficient for full recovery.
