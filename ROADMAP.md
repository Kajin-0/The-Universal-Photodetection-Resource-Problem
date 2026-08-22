# Research Roadmap

**Updated:** 2026-08-21

**Active scientific branch:** `agent/temporal-information-resource-law`

Paper 1 Rev11 and Paper 2 Rev7 are frozen. Grand Challenge theorem stack: **WP18**.

## Established hierarchy

### WP10/WP12/WP15 — modewise QFI envelope

`sum_{k>=1}G_Q(k)<=2nbar`,

`int_R G_Q(nu)dnu<=pi Ebar^+/hbar`.

This is a separately optimized SLD-QFI envelope. WP16 identifies the sharp `pi/4` operator constant as classical Hardy–Hilbert prior art.

### WP17 — fixed/separable operational law

For one fixed arbitrary POVM,

`sum_{k>=1}Tr F_M^(k)<=nbar`.

For adaptive/separable independent-event detection the same source-normalized budget survives.

Continuum:

`int_R R_M(nu)dnu<=2Ebar^+/hbar`,

with flat-band inverse law

`Ebar^+>=hBq0`.

The coefficient is sharp.

### WP18 — two-sector collective closure

For `q_0=1-p`, `q_1=p`, asymptotically optimal collective measurement gives

`q_coll=min(p,1-p)`.

For `p<=1/2`,

`q_coll=p=nbar`.

Thus collective measurement can recover incompatibility loss but does not exceed the energy resource ceiling in the minimal model.

## Highest-priority active gate — multimode collective theorem

Prove or falsify an asymptotic collective bound of the form

`boxed: sum_{k>=1}R_coll(k)<=nbar`

for multilevel random-time encoding.

If true, the sharp fully collective continuum operational law would be

`int_R R_coll(nu)dnu<=2Ebar^+/hbar`,

with the same `Ebar^+>=hBq0` Planck-scale coefficient already attained by covariant timestamps.

### Attack order

1. Three energy sectors, modes `k=1,2`.
2. Exact SLD commutator/Holevo geometry.
3. Finite-copy collective numerical optimization where tractable.
4. Search for a Holevo-dual inequality weighted by generator excitation.
5. Test D-invariant decomposition of energy-gap tangent sectors.
6. Quantum local asymptotic normality if direct finite-dimensional analysis stalls.

## Parallel gates

- Continue exact prior-art search for the random-time QFI and operational sum rules.
- Harden the independent quantum-marked Poisson-to-bosonic-field mapping.
- Locate explicit classical-analysis provenance of the harmonic-mean density functional.
- Preserve WP14's arbitrary-waveform no-go.

## Manuscript gate

Do not draft the foundational paper until the multimode collective question is resolved or sharply bounded, priority survives, and the optical source embedding is publication-grade.

## Documentation discipline

Every material theorem, no-go, proof repair, priority collision, or strategy change must update the active WP notes, handoff/landing files, and `main`.