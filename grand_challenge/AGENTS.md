# AGENTS — Temporal Information Resource Law Program

**Last synchronized: 2026-08-21**

## Purpose

Durable handoff for the active high-risk/high-ceiling theoretical program launched from Paper 2.

Active branch: `agent/temporal-information-resource-law`.

## Non-negotiable scope

- Analytical/theoretical research only.
- Numerical counterexample searches are allowed.
- Do not require experiments, fabrication, procurement, or laboratory optimization as active next steps.
- Paper 2 Rev7 remains frozen unless a concrete defect is found.
- Falsification-first: do not overclaim novelty or universality.

## Grand question

> For a physically realizable measurement of temporal structure, what fundamental resources constrain source-to-record temporal Fisher-information transfer?

## Read first — authoritative order

1. `grand_challenge/notes/WP17_SINGLE_MEASUREMENT_OPERATIONAL_MODE_BUDGET.md`
2. `grand_challenge/notes/WP16_DEEP_PRIORITY_AUDIT_RANDOM_TIME_QFI_AND_HARDY_HILBERT_COLLISION.md`
3. `grand_challenge/notes/WP15_GENERAL_DENSITY_PROOF_OF_SHARP_PI_AREA_INEQUALITY.md`
4. `grand_challenge/notes/WP14_COHERENT_FIELD_BASELINE_ENERGY_NO_GO.md`
5. `grand_challenge/notes/WP13_SECOND_QUANTIZED_SCOPE_AND_POISSON_EVENT_EMBEDDING.md`
6. `grand_challenge/notes/WP12_SHARP_CONTINUUM_QUANTUM_MODE_AREA_LAW.md`
7. `grand_challenge/notes/WP11_WP10_FACTOR_AUDIT_AND_PRIOR_ART.md`
8. `grand_challenge/notes/WP10_QUANTUM_RANDOM_TIME_MODE_BUDGET.md`
9. `grand_challenge/notes/WP09_EXTERNAL_TIME_REFERENCE_NO_GO_AND_ASYMMETRY_BOUNDARY.md`
10. `grand_challenge/notes/WP08_ARBITRARY_MEMORY_LIFT_AND_QUANTUM_REGULARIZATION.md`
11. `grand_challenge/notes/WP07_ENERGY_EDGE_AND_COVARIANT_POVM_PROOF_REPAIR.md`
12. `grand_challenge/notes/WP06_POSITIVE_ENERGY_TEMPORAL_FISHER_AREA_LAW.md`

## Current strongest theorem stack

### WP10/WP11 — modewise QFI envelope

For a periodic random-time mode `k`, pure-state sector probabilities `q_n` give

`G_Q(k)=2 sum_n q_n q_{n+k}/(q_n+q_{n+k})`.

The separately optimized QFI mode sums obey

`sum_{k>=1}G_Q(k)<=2 nbar`,

`sum_{k!=0}G_Q(k)<=4 nbar`.

These remain valid mode-by-mode quantum envelopes. Cosine/sine SLDs are generally incompatible.

### WP12/WP15 — sharp continuum QFI envelope

For normalized `q(w)>=0` with finite first moment `wbar`,

`G_Q(nu)=2 int_0^infinity q(w)q(w+nu)/[q(w)+q(w+nu)]dw`, `nu>0`,

with even extension, and

`int_0^infinity G_Q(nu)dnu <= (pi/2)wbar`,

`int_R G_Q(nu)dnu <= pi Ebar^+/hbar`.

The QFI flat-band envelope gives

`Ebar^+ >= (2/pi)hBq0`.

WP16 establishes that the sharp `pi/4` operator norm used in WP15 is classical Hardy–Hilbert mathematics, not a mathematical novelty claim.

### WP17 — sharp single-measurement/separable operational law

WP17 resolves the main single-measurement incompatibility question.

For **one fixed arbitrary POVM** used to recover all random-time Fourier modes, let `F_M^(k)` be the `2 x 2` classical Fisher matrix for the cosine/sine parameters of mode `k`. Then

`boxed: sum_{k>=1} Tr F_M^(k) <= nbar`.

The source Fisher block is `(1/2)I_2`, so its trace is `1`; `Tr F_M^(k)` is the total source-normalized retention of both real quadratures.

The proof uses only POVM positivity, Radon–Nikodym matrix densities, and Cauchy–Schwarz. It requires no covariance or reference-free restriction on the final POVM.

The constant is sharp as a supremum, approached by a two-sector state and canonical phase POVM.

The theorem extends by the classical FI chain rule to arbitrary **adaptive/separable measurements** of independent quantum-marked events, and hence to a Poisson number of such events. Subsequent parameter-independent classical memory cannot increase FI.

Controlled continuum consequence:

`boxed: int_0^infinity R_M(nu)dnu <= wbar`,

`boxed: int_R R_M(nu)dnu <=2 Ebar^+/hbar`,

where `R_M` is the trace retention of the two real mode quadratures.

If a fixed detector guarantees

`F_M(nu) >= (q0/2)I_2`

through `|f|<=B`, then

`boxed: Ebar^+ >= hBq0`.

This operational coefficient is sharp. The Cauchy/exponential covariant timestamp family from WP06/WP07 exactly saturates the continuum area law.

### Interpretation of the `pi/2` gap

For single-copy/separable readout, the ratio between the QFI area coefficient `pi` and the sharp operational coefficient `2` is an **incompatibility gap**, not an established detector advantage.

The covariant timestamp class already attains the optimal fixed-measurement coefficient `2`.

## Remaining collective-measurement loophole

WP17 does **not** yet cover a detector that coherently stores multiple independently twirled event excitations and performs an entangled collective measurement across them.

This boundary is substantive. Gill–Massar-type tradeoffs apply to arbitrary measurements for pure-state models but, for mixed states, generally only to separable measurements; collective mixed-state measurements can outperform separable limits. The random-time baseline state is generally mixed after twirling.

The next operational gate is therefore:

> Determine the asymptotic Holevo/collective-measurement limit for the random-time Fourier-mode model, starting with the two-sector qubit case, and test whether the sharp `2E/hbar` operational area coefficient survives arbitrary collective readout.

## Physical source scope — WP13/WP14

Included:

- total-energy-sector formulation;
- fixed-photon-number multiphoton/entangled/multimode pulses;
- independent quantum-marked Poisson events;
- arbitrary subsequent parameter-independent field mapping and detector processing, subject to the measurement-class distinction above.

Excluded without extra resource accounting:

- arbitrary parameter-dependent waveform state engineering. WP14 shows baseline mean energy alone cannot bound coherent high-frequency sideband tangents.

## Prior-art discipline

Do not claim novelty for:

- generic SLD/QFI or QFI monotonicity;
- random-unitary mixture estimation generally;
- U(1)/time-translation mode decomposition;
- waveform QFI kernels;
- covariant time POVMs;
- time-translation asymmetry;
- generic multiparameter incompatibility / Gill–Massar / Holevo theory;
- Hardy/Gagliardo–Nirenberg or Hardy–Hilbert inequalities;
- rearrangement/layer-cake/Mellin methods;
- generic time-energy uncertainty relations.

Targeted searches have not yet located the specific random-time formulas `G_Q(k)`, the `2 nbar` QFI sum rule, the WP17 `nbar` fixed-measurement trace budget, or their temporal-information resource interpretation. Priority remains uncertified.

## Immediate hostile gates

1. **Collective Gate:** solve the asymptotic collective mixed-state measurement problem, beginning with the two-sector qubit model and the Holevo bound.
2. **Priority Gate:** continue exact-equivalent searches in random-unitary/group-distribution estimation for WP10/WP17.
3. **Source Gate:** strengthen the independent quantum-marked Poisson-to-field mapping for realistic incoherent optical sources.
4. **Analysis provenance:** determine whether the harmonic-mean density functional inequality appears explicitly in classical analysis; its sharp operator constant is already classical.
5. Only after these gates decide whether WP10–WP17 justify a standalone foundational manuscript.

## Documentation rule

After every material theorem, counterexample, proof repair, prior-art collision, numerical result, or strategy change:

1. update/create `grand_challenge/notes/WP*.md` immediately;
2. update this file when the theorem/gates change;
3. update active-branch top-level `README.md`, `AGENTS.md`, `docs/CURRENT_RESEARCH_STATE.md`, `ROADMAP.md`, and secondary entry points when needed;
4. mirror the active branch/checkpoint into the landing files on `main`;
5. do not rely on chat history as the only record.