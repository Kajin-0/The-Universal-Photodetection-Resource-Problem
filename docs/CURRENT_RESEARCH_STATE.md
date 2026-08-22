# Current Research State

**Last synchronized:** 2026-08-22

**Active branch:** `agent/temporal-information-resource-law`

Paper 1 Rev11 and Paper 2 Rev7 are frozen.

**Grand Challenge science checkpoint:** WP24.

**Preferred manuscript:** **Rev7 PRX Quantum**.

## Read first

1. `grand_challenge/AGENTS.md`
2. `grand_challenge/notes/MANUSCRIPT_REV7_REFEREE_HARDENING_2026-08-22.md`
3. `grand_challenge/notes/WP24_INTEGRATED_HOSTILE_REVIEW_AND_SYMMETRY_PRIOR_ART_BOUNDARY.md`
4. `grand_challenge/notes/WP23_RIGOROUS_COMPOUND_POISSON_TO_BOSONIC_FIELD_CHANNEL_MAP.md`
5. `grand_challenge/notes/WP22_CONTINUUM_LIMIT_RIGOR_FOR_OPERATIONAL_SURVIVAL_LAW.md`
6. `grand_challenge/notes/WP20_DIRECT_FINITE_COPY_PROOF_AND_HOSTILE_AUDIT_OF_WP19.md`

# Strongest theorem

For exact periodic random-time encoding,

`Tr F_N^(k)/N <= min(D_k,U_k) <= T_k`,  `T_k=sum_(m>=k)q_m`,

for any finite number of independently encoded copies and any joint POVM, including arbitrary entangled collective measurements.

Consequently,

`sum_(k>=1) R_N(k) <= nbar`.

# Controlled continuum statement

For controlled periodic-to-continuum limits,

`R(nu) <= Pr(Omega>=nu)`.

This survival law is the main continuum result.

`Ebar+ = hbar <Omega>` is mean excitation/excess energy above the participating lower edge, not a common carrier offset. The area and `hfR` inequalities are first-moment corollaries:

`int_R R <= 2 Ebar+/hbar`,

`Ebar+ >= hbar nu R(nu) = h f R(2pi f)`.

Do not broaden the controlled-limit theorem or advertise `hfR` as the independent core result.

# Sharpness and physical relevance

The geometric/canonical-phase family saturates every discrete harmonic simultaneously and gives the exponential-spectrum/Cauchy-time equality family in the controlled continuum limit.

Rev7 adds a transform-limited truncated-Gaussian single-photon example. Canonical timing reaches about 96.6% of the survival ceiling at half a Gaussian width and 88.5% at one width. The closed forms and convergence from exact lower-bin periodic approximants are numerically validated.

# Prior-art boundary

Modes-of-asymmetry theory already identifies `U(1)` gap components and weighted-twirl Fourier structure. Rev7's novelty boundary is operational:

> the paper bounds the **classical Fisher information extractable by any actual POVM** about a perturbation of the random-time mixing law, using a sharp population-tail coefficient, for arbitrary finite-copy collective measurements.

Established `U(1)` mode theory, canonical phase POVMs, energy-constrained phase estimation, generic QFI/Holevo machinery, random-unitary estimation, waveform QFI, Hardy--Hilbert/positive-frequency mathematics, and generic Poisson/CPTP processing are not novelty claims.

**Priority remains unverified, not certified.**

# Physical source scope

WP23 transfers the normalized bound to independent quantum-marked Poisson events followed by arbitrary **parameter-independent** field formation and detector processing through POVM pullback.

WP14/Rev7 retain the coherent-sideband no-go: baseline mean energy cannot constrain arbitrary parameter-dependent waveform-state synthesis.

# Preferred manuscript — Rev7

Working title: **A Sharp Energy-Survival Law for Temporal Fisher Information**.

Rev7 responds to an external adversarial review by:

- making the continuum qualification explicit everywhere;
- defining the resource consistently as excess energy;
- promoting the survival law over the first-moment `hf` corollary;
- sharpening the modes-of-asymmetry distinction;
- adding one nonextremal transform-limited single-photon example;
- revising Figure 1 to match those claims.

Final local preflight:

- full LaTeX/BibTeX build: **PASS**;
- pages: **8**;
- PDF size: **403,102 bytes**;
- SHA-256: `d168c3901faa6f29bda0eba71abe8049cc9819d91843273beeeeffb9443818ae`;
- unresolved references/citations: **0**;
- overfull boxes: **0**;
- 8-page 200-dpi visual inspection: **PASS**;
- photon analytic/numerical consistency: **PASS**.

Dedicated CI now generates Rev7, runs the theorem validator and photon-example validator, compiles the PRX package, and applies reference/layout/style gates. Direct branch-push run inspection remains unavailable through the connector.

# Target

**PRX Quantum — Research Article** first.

**Physical Review A — Regular Article** fallback.

# Workflow status

The manuscript is finished to the fullest extent currently justified. **Freeze Rev7** unless a concrete theorem defect, historical-priority collision, build defect, or new referee-level objection appears.

Do not introduce “human verification” as a research/manuscript completion gate. Unknown administrative submission facts may remain placeholders rather than being invented. A human submits the finished package.

## Documentation rule

Every material state change must be mirrored onto `main`; the repository, not chat history, is authoritative.
