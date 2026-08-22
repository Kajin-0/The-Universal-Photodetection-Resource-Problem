# Current Research State

**Last synchronized:** 2026-08-21

**Active scientific branch:** `agent/temporal-information-resource-law`

This is the first-stop replacement-agent summary. The repository, not chat history, is authoritative.

## Project status

1. **Paper 1 / Rev11:** scientifically frozen and technically validated; submission metadata/compliance only.
2. **Paper 2 / Rev7:** preferred frozen science draft; locally build-verified, preflighted, source-diff inspected, and visually inspected.
3. **Grand Challenge:** active theoretical frontier. The theorem stack remains through **WP15**; the latest research checkpoint is **WP16**, a deep priority audit.

## Read first

1. `grand_challenge/AGENTS.md`
2. `grand_challenge/notes/WP16_DEEP_PRIORITY_AUDIT_RANDOM_TIME_QFI_AND_HARDY_HILBERT_COLLISION.md`
3. `grand_challenge/notes/WP15_GENERAL_DENSITY_PROOF_OF_SHARP_PI_AREA_INEQUALITY.md`
4. `grand_challenge/notes/WP14_COHERENT_FIELD_BASELINE_ENERGY_NO_GO.md`
5. `grand_challenge/notes/WP13_SECOND_QUANTIZED_SCOPE_AND_POISSON_EVENT_EMBEDDING.md`
6. `grand_challenge/notes/WP12_SHARP_CONTINUUM_QUANTUM_MODE_AREA_LAW.md`
7. `grand_challenge/notes/WP11_WP10_FACTOR_AUDIT_AND_PRIOR_ART.md`
8. `grand_challenge/notes/WP10_QUANTUM_RANDOM_TIME_MODE_BUDGET.md`
9. `grand_challenge/notes/WP09_EXTERNAL_TIME_REFERENCE_NO_GO_AND_ASYMMETRY_BOUNDARY.md`
10. `grand_challenge/notes/WP08_ARBITRARY_MEMORY_LIFT_AND_QUANTUM_REGULARIZATION.md`
11. `paper2/AGENTS_PAPER2.md` only if Paper-2 context is needed.

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

This remains the strongest detector-independent Planck-scale temporal-information resource law in the program.

## Proof status

WP15 gives a general finite-first-moment proof:

- rearrangement reduces to decreasing densities;
- the superlevel-length function `r(s)` satisfies `omega_bar=(1/2)||r||_2^2`;
- the exact positive-kernel identity converts the area functional into `<r,Tr>`;
- `L(s,t)=2st/(s+t)^3` has exact `L2` norm `pi/4`;
- the constant is sharp as a supremum, approached by truncated critical densities proportional to `(1+omega)^(-2)`.

# WP16 priority correction — sharp operator constant is classical

WP16 establishes an explicit prior-art collision for the analytic core after the layer-cake reduction.

Classical parameterized Hardy–Hilbert theory gives, for `lambda>0`, the sharp weighted inequality with kernel `(x+y)^(-lambda)` and best constant `B(lambda/2,lambda/2)`. Setting

`lambda=3`, `f(x)=x r(x)`, `g(y)=y r(y)`

gives

`B(3/2,3/2)=pi/8`,

and the factor `2` in the WP15 kernel yields exactly

`boxed: ||T||=pi/4`.

Therefore the `pi/4` norm, Mellin/Hilbert operator bound, and Beta/Gamma sharp constant are **established mathematics and must not be claimed as novel**.

This does not change the theorem or its coefficients. It narrows the possible novelty to the quantum statistical experiment and physical synthesis.

Targeted quantum searches still have not located an exact predecessor for estimating a Fourier coefficient of a latent random `U(1)` translation distribution with

`G_Q(k)=2 sum_n q_nq_{n+k}/(q_n+q_{n+k})`

or the all-positive-mode budget

`sum_{k>=1}G_Q(k)<=2 nbar`.

**Quantum priority remains unverified.** The next priority search must target estimation of group-distribution Fourier coefficients / random-unitary mixing weights rather than generic phase-diffusion metrology.

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
- baseline mean energy does not bound arbitrary state-valued waveform encoding;
- the WP15 `pi/4` operator constant is not new mathematics.

# Prior-art boundary

Do not claim novelty for generic QFI/SLD theory, waveform-QFI kernels, covariant time POVMs, time-translation asymmetry, Hardy/Gagliardo–Nirenberg inequalities, Hardy–Hilbert best-constant inequalities, rearrangement/layer-cake/Mellin methods, or time-energy uncertainty relations.

Close literature now explicitly includes Yang's Hilbert-type integral-operator work in addition to Tsang–Wiseman–Caves, Marvian–Spekkens, Pocovnicu, Kiukas–Ruschhaupt–Werner, Hall, WAY/asymmetry, phase-diffusion/dephasing estimation, and random-unitary/noise-channel estimation.

# Immediate gates

1. **Priority Gate 1A:** search exact equivalents in estimation of Fourier coefficients/mixing weights of `U(1)` random-unitary channels and probability measures on compact groups.
2. **Priority Gate 1B:** determine whether the harmonic-mean density inequality appears explicitly in analysis literature; its operator constant is already classical.
3. **Operational attainability:** determine whether one measurement can approach the integrated `pi` coefficient despite incompatible per-mode SLDs.
4. Strengthen the independent quantum-marked Poisson-to-field embedding for realistic incoherent optical sources.
5. Decide whether WP10–WP15 justify a standalone foundational manuscript only if the first four gates survive.
6. Do not broaden to arbitrary waveform encoding unless the extra control/action resource can be stated noncircularly.

# Frozen Paper 2

Preferred Paper-2 draft remains Rev7: **Fisher Spectra and Information Singularities in Photodetectors with Memory**. Science is frozen unless a concrete defect/referee issue appears.

# Documentation rule

After every material theorem, proof repair, no-go, prior-art collision, numerical result, or strategy change:

- update the relevant `grand_challenge/notes/WP*.md` immediately;
- update `grand_challenge/AGENTS.md` whenever the active theorem hierarchy/gates change;
- update top-level `README.md`, `AGENTS.md`, this file, and `ROADMAP.md` for every project-level frontier change;
- keep `PROBLEM.md` and `grand_challenge/README.md` from becoming misleading secondary entry points;
- keep `main` visibly synchronized with the active branch and latest checkpoint.

Do not let the current research state exist only on an agent branch or in chat.