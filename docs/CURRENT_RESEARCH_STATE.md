# Current Research State

**Last synchronized:** 2026-08-21

**Default branch role:** landing/index only.

**Active scientific branch:** `agent/temporal-information-resource-law`

The repository, not chat history, is authoritative.

## Project status

1. **Paper 1 / Rev11** — scientifically frozen and technically validated; submission metadata/compliance only.
2. **Paper 2 / Rev7** — preferred frozen science draft; locally build-verified and visually inspected.
3. **Grand Challenge** — current theoretical frontier; theorem stack through **WP15**.

## Replacement-agent recovery

Switch to `agent/temporal-information-resource-law`, then read:

1. `grand_challenge/AGENTS.md`
2. `grand_challenge/notes/WP15_GENERAL_DENSITY_PROOF_OF_SHARP_PI_AREA_INEQUALITY.md`
3. `grand_challenge/notes/WP14_COHERENT_FIELD_BASELINE_ENERGY_NO_GO.md`
4. `grand_challenge/notes/WP13_SECOND_QUANTIZED_SCOPE_AND_POISSON_EVENT_EMBEDDING.md`
5. `grand_challenge/notes/WP12_SHARP_CONTINUUM_QUANTUM_MODE_AREA_LAW.md`
6. `grand_challenge/notes/WP11_WP10_FACTOR_AUDIT_AND_PRIOR_ART.md`
7. `grand_challenge/notes/WP10_QUANTUM_RANDOM_TIME_MODE_BUDGET.md`
8. active-branch `ROADMAP.md`.

Do not resume the historical main-branch HgCdTe/Kane WP24 program unless a later theorem explicitly requires it.

# Current grand question

> For a physically realizable measurement of temporal structure, what fundamental resources constrain source-to-record temporal Fisher-information transfer?

# Strongest current theorem — WP15

For normalized `q(omega)>=0` with finite first moment

`omega_bar=int_0^infinity omega q(omega)domega`,

the random-time temporal Fourier-mode quantum retention is

`G_Q(nu)=2 int_0^infinity q(omega)q(omega+nu)/[q(omega)+q(omega+nu)]domega`, `nu>0`,

with even extension.

WP15 proves, for every finite-first-moment density and without smoothness assumptions,

`boxed: int_0^infinity G_Q(nu)dnu <= (pi/2) omega_bar`,

therefore

`boxed: int_R G_Q(nu)dnu <= pi E_bar^+/hbar`.

For a guaranteed band with `G_Q(2*pi*f)>=q0` for `|f|<=B`,

`boxed: E_bar^+ >= (2/pi) h B q0`.

The constant is sharp as a supremum. The proof reduces the area functional to a positive Mellin-convolution operator with exact norm `pi/4`; truncated critical densities proportional to `(1+omega)^(-2)` approach equality.

# Discrete precursor — WP10/WP11

For periodic temporal mode `k`:

`G_Q(k)=2 sum_n q_n q_{n+k}/(q_n+q_{n+k})`.

Resource sums:

`sum_{k>=1}G_Q(k)<=2 nbar`,

`sum_{k!=0}G_Q(k)<=4 nbar`.

These constants are sharp as suprema.

# Covariant timestamp subclass — WP06-WP08

For reference-free covariant timestamp readout:

`int_R G_timestamp(nu)dnu <= 2 E_det^+/hbar`,

or

`E_det^+ >= h B q`.

WP08 lifts this through arbitrary downstream parameter-independent classical detector memory and shows finite-energy quantum timing regularizes the ideal classical Type-II high-frequency plateau from Paper 2.

# Scope boundary — WP14

The strongest current theorem concerns **random temporal-distribution encoding of a fixed semibounded-energy excitation**.

It does **not** extend using baseline mean energy alone to arbitrary state-valued waveform synthesis. WP14 constructs a coherent-field counterexample where an arbitrarily high-frequency infinitesimal sideband is encoded at first order while additional energy appears only at second order. A broader theorem requires an explicit encoding/control/action resource.

# Prior-art status

Generic QFI, time-covariant POVMs, waveform-QFI kernels, time-translation asymmetry, Hardy/Gagliardo-Nirenberg inequalities, rearrangement/Mellin methods, and time-energy uncertainty relations are prior art.

Targeted searches have not yet located the exact random-time mode formula, the `2 nbar` sum rule, or the sharp continuum `pi E/hbar` source-to-record transfer law. **Priority is not certified.**

# Immediate gates

1. Deep priority audit for exact equivalents of WP10/WP12/WP15.
2. Determine operational/joint-measurement attainability of the integrated `pi` coefficient.
3. Strengthen the quantum-marked Poisson/event-to-field embedding for realistic incoherent optical source models.
4. Only after those gates decide whether WP10-WP15 warrant a standalone foundational manuscript.

# Documentation requirement

Every project-level state change must be reflected both on the active branch and in the default-branch landing documents. The user should never need to guess which branch contains the current scientific state.