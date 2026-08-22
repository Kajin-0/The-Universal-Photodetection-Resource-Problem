# Current Research State

**Last synchronized:** 2026-08-21

**Active scientific branch:** `agent/temporal-information-resource-law`

This is the first-stop replacement-agent summary. The repository, not chat history, is authoritative.

## Project status

1. **Paper 1 / Rev11:** scientifically frozen and technically validated; submission metadata/compliance only.
2. **Paper 2 / Rev7:** preferred frozen science draft; locally build-verified, preflighted, source-diff inspected, and visually inspected.
3. **Grand Challenge:** active theoretical frontier. Current authoritative handoff is `grand_challenge/AGENTS.md` and the active theorem stack is through **WP15**.

## Read first

1. `grand_challenge/AGENTS.md`
2. `grand_challenge/notes/WP15_GENERAL_DENSITY_PROOF_OF_SHARP_PI_AREA_INEQUALITY.md`
3. `grand_challenge/notes/WP14_COHERENT_FIELD_BASELINE_ENERGY_NO_GO.md`
4. `grand_challenge/notes/WP13_SECOND_QUANTIZED_SCOPE_AND_POISSON_EVENT_EMBEDDING.md`
5. `grand_challenge/notes/WP12_SHARP_CONTINUUM_QUANTUM_MODE_AREA_LAW.md`
6. `grand_challenge/notes/WP11_WP10_FACTOR_AUDIT_AND_PRIOR_ART.md`
7. `grand_challenge/notes/WP10_QUANTUM_RANDOM_TIME_MODE_BUDGET.md`
8. `grand_challenge/notes/WP09_EXTERNAL_TIME_REFERENCE_NO_GO_AND_ASYMMETRY_BOUNDARY.md`
9. `grand_challenge/notes/WP08_ARBITRARY_MEMORY_LIFT_AND_QUANTUM_REGULARIZATION.md`
10. `paper2/AGENTS_PAPER2.md` only if Paper-2 context is needed.

# Current grand question

> For a physically realizable measurement of temporal structure, what fundamental resources constrain source-to-record temporal Fisher-information transfer?

The program is falsification-first. It does not assume that a single thermodynamic or energetic scalar controls all temporal information tasks.

# Strongest current result — WP12/WP15

For a normalized positive excitation-frequency density `q(omega)` with finite mean

`omega_bar = int_0^infinity omega q(omega)domega`,

the random-time temporal-mode quantum retention is

`G_Q(nu)=2 int_0^infinity q(omega)q(omega+nu)/[q(omega)+q(omega+nu)]domega`, `nu>0`,

with even extension.

WP15 proves without smoothness assumptions:

`boxed: int_0^infinity G_Q(nu)dnu <= (pi/2) omega_bar`,

and therefore

`boxed: int_R G_Q(nu)dnu <= pi E_bar^+/hbar`.

If a source guarantees

`G_Q(2*pi*f)>=q0` for every `|f|<=B`,

then

`boxed: E_bar^+ >= (2/pi) h B q0`.

This is currently the strongest detector-independent Planck-scale temporal-information resource law in the program.

## Proof status

WP15 gives a publication-grade general-density proof:

- rearrangement reduces to decreasing densities;
- the superlevel-length function `r(s)` satisfies `omega_bar=(1/2)||r||_2^2`;
- the exact kernel identity converts the area functional into `<r,Tr>`;
- the positive Mellin-convolution operator has multiplier `|Gamma(3/2+i xi)|^2` and exact norm `pi/4`;
- the constant is sharp as a supremum, approached by truncated critical densities proportional to `(1+omega)^(-2)`.

# Discrete precursor — WP10/WP11

For periodic random-time modes:

`G_Q(k)=2 sum_n q_n q_{n+k}/(q_n+q_{n+k})`.

The mode budget obeys

`sum_{k>=1}G_Q(k)<=2 nbar`,

`sum_{k!=0}G_Q(k)<=4 nbar`.

The constants are sharp as suprema. Mixed-state extensions follow through purification/QFI monotonicity. Per-mode cosine/sine SLDs need not be jointly compatible, so integrated QFI upper bounds are not automatically jointly attainable.

# Physical source scope — WP13/WP14

The theorem includes fixed-photon-number multiphoton/entangled/multimode excitations by using the total time-translation generator and its total-energy sectors.

For independent quantum-marked Poisson events, QFI and excess energy are additive in event number, so the source-normalized mode budget is inherited by any downstream parameter-independent field mapping, coherent detector memory, and measurement.

However, WP14 proves a major no-go: baseline mean energy alone cannot constrain **arbitrary waveform state engineering**. Infinitesimal high-frequency coherent sidebands can appear at first order in the encoded amplitude while added energy enters only at second order. Any broader theorem must include an encoding-map/control/action resource.

# Covariant timestamp subclass — WP06-WP08

For a reference-free covariant timestamp measurement:

`boxed: int_R G_timestamp(nu)dnu <= 2 E_det^+/hbar`,

or equivalently

`boxed: E_det^+ >= h B q`.

The correct energy is measured above the participating lower spectral edge, making the theorem gauge invariant under `H -> H+cI`.

WP08 lifts this timestamp law through arbitrary downstream classical detector memory and shows that finite-energy quantum timing removes the exact infinite-frequency atomic plateau allowed by Paper 2's ideal classical Type-II model.

# Important no-gos already established

Do not restart these failed universal-law directions:

- entropy production alone does not universally bound information acquisition;
- generic frequency-domain response/dynamical-activity uncertainty relations already exist;
- temporal waveform QFI kernels already exist;
- detector thermodynamic cost is not determined by `G` alone;
- finite-QFI or classical-vs-quantum accessibility gaps alone are not sufficiently novel;
- baseline mean energy does not bound arbitrary state-valued waveform encoding.

# Prior-art boundary

Do not claim novelty for generic QFI/SLD theory, waveform-QFI kernels, covariant time POVMs, time-translation asymmetry, Hardy/Gagliardo-Nirenberg inequalities, rearrangement/layer-cake/Mellin methods, or time-energy uncertainty relations.

Targeted searches have not yet found an exact equivalent of the WP10 random-time mode formula, the discrete `2 nbar` sum rule, or the sharp WP12/WP15 continuum `pi E/hbar` integrated-transfer law. **Priority remains unverified.**

# Immediate gates

1. Deep historical/modern priority audit for exact equivalents of WP10/WP12/WP15.
2. Operational attainability: determine whether one measurement can approach the integrated `pi` coefficient despite incompatible per-mode SLDs.
3. Strengthen the independent quantum-marked Poisson-to-field embedding for realistic incoherent optical sources.
4. Decide whether WP10-WP15 justify a standalone foundational manuscript if the first three gates survive.
5. Do not broaden to arbitrary waveform encoding unless the extra control/action resource can be stated noncircularly.

# Frozen Paper 2

Preferred Paper-2 draft remains Rev7: **Fisher Spectra and Information Singularities in Photodetectors with Memory**. Science is frozen unless a concrete defect/referee issue appears.

# Documentation rule

After every material theorem, proof repair, no-go, prior-art collision, numerical result, or strategy change:

- update the relevant `grand_challenge/notes/WP*.md` immediately;
- update `grand_challenge/AGENTS.md` whenever the active theorem hierarchy/gates change;
- update top-level `README.md`, `AGENTS.md`, this file, and `ROADMAP.md` for every project-level frontier change;
- keep `main` visibly synchronized with the active branch and latest checkpoint.

Do not let the current research state exist only on an agent branch or in chat.