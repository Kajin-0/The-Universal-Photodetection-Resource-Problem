# AGENTS — Temporal Information Resource Law Program

**Last synchronized: 2026-08-21**

Active branch: `agent/temporal-information-resource-law`.

Research is analytical/theoretical, falsification-first. Paper 1 Rev11 and Paper 2 Rev7 are frozen.

## Grand question

> For a physically realizable measurement of temporal structure, what fundamental resources constrain source-to-record temporal Fisher-information transfer?

## Read first

1. `grand_challenge/notes/WP18_TWO_SECTOR_COLLECTIVE_HOLEVO_CLOSURE.md`
2. `grand_challenge/notes/WP17_SINGLE_MEASUREMENT_OPERATIONAL_MODE_BUDGET.md`
3. `grand_challenge/notes/WP16_DEEP_PRIORITY_AUDIT_RANDOM_TIME_QFI_AND_HARDY_HILBERT_COLLISION.md`
4. `grand_challenge/notes/WP15_GENERAL_DENSITY_PROOF_OF_SHARP_PI_AREA_INEQUALITY.md`
5. `grand_challenge/notes/WP14_COHERENT_FIELD_BASELINE_ENERGY_NO_GO.md`
6. `grand_challenge/notes/WP13_SECOND_QUANTIZED_SCOPE_AND_POISSON_EVENT_EMBEDDING.md`
7. `grand_challenge/notes/WP12_SHARP_CONTINUUM_QUANTUM_MODE_AREA_LAW.md`
8. `grand_challenge/notes/WP11_WP10_FACTOR_AUDIT_AND_PRIOR_ART.md`
9. `grand_challenge/notes/WP10_QUANTUM_RANDOM_TIME_MODE_BUDGET.md`

## Current theorem hierarchy

### WP10/WP12/WP15 — separately optimized QFI envelope

Periodic:

`G_Q(k)=2 sum_n q_nq_{n+k}/(q_n+q_{n+k})`,

`sum_{k>=1}G_Q(k)<=2nbar`.

Continuum:

`int_R G_Q(nu)dnu<=pi Ebar^+/hbar`.

This is a modewise SLD-QFI envelope, not generally jointly attainable.

WP16 establishes that the sharp `pi/4` continuum operator norm is classical Hardy–Hilbert mathematics, not a novelty claim.

### WP17 — sharp fixed/separable operational law

For one fixed arbitrary POVM, with `F_M^(k)` the cosine/sine classical Fisher block,

`boxed: sum_{k>=1}Tr F_M^(k)<=nbar`.

The theorem requires no covariance or reference-free restriction on the POVM and extends to adaptive/separable measurement of independent quantum-marked events.

Continuum:

`boxed: int_R R_M(nu)dnu<=2Ebar^+/hbar`.

A full-quadrature band guarantee implies

`boxed: Ebar^+>=hBq0`.

The Cauchy/exponential covariant timestamp family saturates the continuum coefficient.

Thus the `pi/2` gap between the QFI coefficient `pi` and fixed/separable operational coefficient `2` is an incompatibility gap.

### WP18 — exact collective closure for the two-sector model

Take

`q_0=1-p`, `q_1=p`, `j=p(1-p)`.

The twirled two-sector state is a mixed qubit. Its random-time cosine/sine derivatives are transverse Bloch directions with SLD QFI matrix

`J=jI_2`.

Direct Holevo optimization gives

`boxed: C_H(I)=2[1+|1-2p|]/[p(1-p)]`.

The asymptotically attainable isotropic source-normalized collective retention is

`boxed: q_coll=min(p,1-p)`.

For the resource-relevant branch `p<=1/2`,

`boxed: q_coll=p=nbar`.

Therefore arbitrary collective measurements can improve over separable readout but cannot exceed the WP17 energy budget in the minimal model; they exactly saturate it for low upper-sector occupation.

For sectors separated by harmonic `k`, `nbar=kp` and the same result gives

`q_coll<=nbar/k`,

or equivalently at the collective optimum on `p<=1/2`,

`Ebar^+=h f_k q_coll`.

The generic mixed-qubit Holevo result is prior art (Suzuki; Conlon et al.); the candidate contribution is the random-time/resource mapping.

## Current highest-value open problem

WP18 closes only one mode supported by two energy sectors. It does **not** prove a multimode collective sum/area law.

The next target is:

> Does arbitrary collective measurement on many independently twirled multilevel excitations obey an asymptotic resource inequality equivalent to `sum_k R_coll(k)<=nbar`, and hence `int_R R_coll<=2E/hbar`?

Recommended attack order:

1. three-sector models with modes `k=1,2`;
2. finite-copy collective POVM/Holevo numerical optimization;
3. search for a Holevo-dual inequality weighted by generator excitation;
4. test D-invariant/block structure of the full tangent model;
5. quantum local asymptotic normality / Gaussian-mode reduction if needed.

## Physical scope

The random-time theorem class includes total-energy sectors, fixed-number multiphoton/entangled/multimode pulses, and independent quantum-marked Poisson events. WP14 excludes arbitrary parameter-dependent coherent waveform synthesis unless the encoding/control resource is counted.

## Prior-art discipline

Do not claim novelty for generic QFI, random-unitary probability estimation, U(1) modes, multiparameter incompatibility, Gill–Massar/Nagaoka/Holevo theory, covariant time POVMs, Hardy/Gagliardo–Nirenberg/Hardy–Hilbert inequalities, Mellin methods, or time-energy uncertainty relations.

Priority remains uncertified for the specific random-time mode formulas, energy-weighted operational sum rules, and their photodetection interpretation.

## Immediate gates

1. **Multimode collective gate** — now the dominant theorem problem.
2. Continue exact priority search for WP10/WP17/WP18 mappings.
3. Harden the quantum-marked Poisson-to-field embedding.
4. Determine explicit classical-analysis provenance of the harmonic-mean density functional if available.
5. Draft no foundational manuscript until these gates survive.

## Documentation rule

Every material result must be recorded in a WP note, reflected in active landing/handoff files, and mirrored onto `main`. The repository—not chat history—must remain sufficient for recovery.