# Current Research State

**Last synchronized:** 2026-08-21

**Active scientific branch:** `agent/temporal-information-resource-law`

The repository, not chat history, is authoritative.

## Project status

1. **Paper 1 / Rev11** — frozen and technically validated.
2. **Paper 2 / Rev7** — frozen preferred science draft.
3. **Grand Challenge** — active theorem stack through **WP17**.

## Replacement-agent recovery

Read:

1. `grand_challenge/AGENTS.md`
2. `grand_challenge/notes/WP17_SINGLE_MEASUREMENT_OPERATIONAL_MODE_BUDGET.md`
3. `grand_challenge/notes/WP16_DEEP_PRIORITY_AUDIT_RANDOM_TIME_QFI_AND_HARDY_HILBERT_COLLISION.md`
4. `grand_challenge/notes/WP15_GENERAL_DENSITY_PROOF_OF_SHARP_PI_AREA_INEQUALITY.md`
5. `grand_challenge/notes/WP14_COHERENT_FIELD_BASELINE_ENERGY_NO_GO.md`
6. `grand_challenge/notes/WP13_SECOND_QUANTIZED_SCOPE_AND_POISSON_EVENT_EMBEDDING.md`
7. `grand_challenge/notes/WP12_SHARP_CONTINUUM_QUANTUM_MODE_AREA_LAW.md`
8. `grand_challenge/notes/WP11_WP10_FACTOR_AUDIT_AND_PRIOR_ART.md`
9. `grand_challenge/notes/WP10_QUANTUM_RANDOM_TIME_MODE_BUDGET.md`

# Current theorem hierarchy

## Modewise QFI envelope — WP10/WP12/WP15

Periodic:

`G_Q(k)=2 sum_n q_nq_{n+k}/(q_n+q_{n+k})`,

`sum_{k>=1}G_Q(k)<=2nbar`.

Continuum:

`int_R G_Q(nu)dnu <=pi Ebar^+/hbar`.

This remains a valid separately optimized quantum envelope.

WP16 establishes that the sharp `pi/4` operator constant in the continuum proof is established Hardy–Hilbert mathematics and must not be claimed as new mathematics.

## Sharp fixed-measurement/separable operational law — WP17

For one fixed arbitrary POVM, with `F_M^(k)` the cosine/sine classical Fisher block,

`boxed: sum_{k>=1}Tr F_M^(k)<=nbar`.

No covariance or reference-free assumption is imposed on the POVM. The proof uses POVM positivity and Cauchy–Schwarz.

The bound extends to arbitrary adaptive/separable measurements of independent quantum-marked events by the classical Fisher chain rule.

Continuum:

`boxed: int_0^infinity R_M(nu)dnu<=omega_bar`,

`boxed: int_R R_M(nu)dnu<=2Ebar^+/hbar`.

A full two-quadrature band guarantee

`F_M(nu)>=(q0/2)I_2`, `|f|<=B`,

requires

`boxed: Ebar^+>=hBq0`.

The coefficient is sharp. The Cauchy/exponential covariant timestamp family saturates the continuum area law.

Therefore, for single-copy/separable readout, the factor `pi/2` between the QFI and operational area constants is an incompatibility gap.

# Remaining collective loophole

WP17 does not yet constrain arbitrary entangled collective measurements across multiple independently twirled event excitations. The baseline twirled state is generally mixed, and collective mixed-state measurements can outperform separable multiparameter bounds.

The immediate operational problem is to compute the Holevo/collective limit, beginning with the two-sector qubit random-time model, and determine whether `2E/hbar` remains the universal operational coefficient.

# Physical source scope

WP13 covers total-energy sectors, fixed-number multiphoton/entangled/multimode excitations, independent quantum-marked Poisson events, and parameter-independent downstream field mapping.

WP14 blocks extension to arbitrary coherent waveform state engineering based only on baseline mean energy.

# Priority status

Generic random-unitary mixing-weight estimation, U(1) asymmetry, multiparameter incompatibility, Gill–Massar/Holevo theory, QFI, covariant POVMs, and Hardy–Hilbert mathematics are prior art.

No exact predecessor has yet been located for the specific random-time `G_Q(k)` formula, `2nbar` QFI sum rule, WP17 `nbar` operational trace budget, or the corresponding temporal-information resource interpretation. **Priority remains uncertified.**

# Immediate gates

1. Collective mixed-state/Holevo analysis of the two-sector model, then general modes.
2. Continue exact priority search for WP10/WP17.
3. Strengthen realistic incoherent optical-field embedding.
4. Clarify direct provenance of the harmonic-mean density inequality.
5. Only then decide on a foundational manuscript.

# Documentation rule

Every material theorem/gate change must update the WP notes, `grand_challenge/AGENTS.md`, top-level landing docs, and `main`. Do not allow secondary entry points to become stale.