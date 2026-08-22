# The Universal Photodetection Resource Problem

**Status synchronized: 2026-08-21**

## Project split

1. **Paper 1 / Rev11** — scientifically frozen and technically validated.
2. **Paper 2 / Rev7** — preferred frozen science draft.
3. **Grand Challenge** — active on `agent/temporal-information-resource-law`.

The theorem stack is now through **WP17**. The authoritative handoff is `grand_challenge/AGENTS.md`.

## Grand question

> For a physically realizable measurement of temporal structure, what fundamental resources constrain source-to-record temporal Fisher-information transfer?

## Modewise quantum envelope — WP10/WP12/WP15

For random temporal-distribution encoding of a fixed semibounded-energy excitation,

`G_Q(k)=2 sum_n q_n q_{n+k}/(q_n+q_{n+k})`

in the periodic model, with

`sum_{k>=1}G_Q(k)<=2 nbar`.

For a continuum density `q(omega)` of finite mean `omega_bar`,

`G_Q(nu)=2 int_0^infinity q(omega)q(omega+nu)/[q(omega)+q(omega+nu)]domega`,

and

`int_R G_Q(nu)dnu <= pi E_bar^+/hbar`.

The corresponding separately optimized QFI flat-band envelope is

`E_bar^+ >= (2/pi) hBq0`.

WP16 establishes that the `pi/4` operator norm used in the sharp continuum proof is classical Hardy–Hilbert mathematics; it is not a mathematical novelty claim.

## Sharp operational law — WP17

For **one fixed arbitrary POVM** used to recover all cosine/sine temporal modes, let `F_M^(k)` denote the `2 x 2` classical Fisher block. Then

`boxed: sum_{k>=1} Tr F_M^(k) <= nbar`.

The source block is `(1/2)I_2`, so `Tr F_M^(k)` is the total source-normalized Fisher retention of the two real quadratures.

The constant is sharp as a supremum. The theorem requires no covariance or reference-free condition on the final POVM and extends to arbitrary adaptive/separable measurement of independent quantum-marked events.

Controlled continuum consequence:

`boxed: int_R R_M(nu)dnu <=2 E_bar^+/hbar`,

where `R_M` is the trace retention of the two real mode quadratures.

If one detector guarantees

`F_M(nu) >= (q0/2)I_2`

through `|f|<=B`, then

`boxed: E_bar^+ >= hBq0`.

This coefficient is sharp: the Cauchy/exponential covariant timestamp family from WP06/WP07 saturates the continuum area law.

Thus, for fixed single-copy/separable readout, the `pi/2` gap between the QFI coefficient `pi` and operational coefficient `2` is an **incompatibility gap**, not an established realizable detector advantage.

## Critical remaining loophole

WP17 does not yet cover arbitrary **collective entangled measurements across multiple independently twirled event excitations**. The twirled state is generally mixed, and standard multiparameter theory permits collective mixed-state advantages over separable measurements.

The next gate is to solve the asymptotic Holevo/collective limit, starting with the two-sector qubit model, and determine whether the `2E/hbar` operational area coefficient survives arbitrary collective readout.

## Scope boundary — WP14

Baseline mean energy does not bound arbitrary parameter-dependent coherent waveform synthesis. The current theorem class is random temporal-distribution encoding of a fixed semibounded-energy excitation. A broader waveform theorem requires an explicit encoding/control/action resource.

## Immediate gates

1. Collective mixed-state/Holevo analysis of the random-time model.
2. Deep priority search for exact equivalents of WP10/WP17.
3. Strengthen the quantum-marked Poisson/event-to-field embedding.
4. Determine explicit classical-analysis provenance of the harmonic-mean density functional if available.
5. Draft no foundational manuscript until these survive.

## Read first

1. `grand_challenge/AGENTS.md`
2. `grand_challenge/notes/WP17_SINGLE_MEASUREMENT_OPERATIONAL_MODE_BUDGET.md`
3. `grand_challenge/notes/WP16_DEEP_PRIORITY_AUDIT_RANDOM_TIME_QFI_AND_HARDY_HILBERT_COLLISION.md`
4. `grand_challenge/notes/WP15_GENERAL_DENSITY_PROOF_OF_SHARP_PI_AREA_INEQUALITY.md`
5. `grand_challenge/notes/WP14_COHERENT_FIELD_BASELINE_ENERGY_NO_GO.md`
6. `grand_challenge/notes/WP13_SECOND_QUANTIZED_SCOPE_AND_POISSON_EVENT_EMBEDDING.md`

## Documentation discipline

Every material result must be recorded in a WP note, reflected in the active handoff/landing documents, and mirrored onto `main`. The repository—not chat history—must remain sufficient for recovery.