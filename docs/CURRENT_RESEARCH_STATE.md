# Current Research State

**Last synchronized:** 2026-08-21

**Active scientific branch:** `agent/temporal-information-resource-law`

Paper 1 Rev11 and Paper 2 Rev7 are frozen. The Grand Challenge is active through **WP18**.

## Read first

1. `grand_challenge/AGENTS.md`
2. `grand_challenge/notes/WP18_TWO_SECTOR_COLLECTIVE_HOLEVO_CLOSURE.md`
3. `grand_challenge/notes/WP17_SINGLE_MEASUREMENT_OPERATIONAL_MODE_BUDGET.md`
4. `grand_challenge/notes/WP16_DEEP_PRIORITY_AUDIT_RANDOM_TIME_QFI_AND_HARDY_HILBERT_COLLISION.md`
5. `grand_challenge/notes/WP15_GENERAL_DENSITY_PROOF_OF_SHARP_PI_AREA_INEQUALITY.md`
6. `grand_challenge/notes/WP14_COHERENT_FIELD_BASELINE_ENERGY_NO_GO.md`
7. `grand_challenge/notes/WP13_SECOND_QUANTIZED_SCOPE_AND_POISSON_EVENT_EMBEDDING.md`
8. `grand_challenge/notes/WP12_SHARP_CONTINUUM_QUANTUM_MODE_AREA_LAW.md`
9. `grand_challenge/notes/WP10_QUANTUM_RANDOM_TIME_MODE_BUDGET.md`

## Current theorem hierarchy

### QFI envelope

Periodic:

`G_Q(k)=2 sum_n q_nq_{n+k}/(q_n+q_{n+k})`,

`sum_{k>=1}G_Q(k)<=2nbar`.

Continuum:

`int_R G_Q(nu)dnu<=pi Ebar^+/hbar`.

This is a separately optimized modewise SLD envelope. WP16 establishes that the sharp `pi/4` operator norm used in WP15 is classical Hardy–Hilbert mathematics.

### Fixed/separable operational theorem — WP17

For one fixed arbitrary POVM,

`boxed: sum_{k>=1}Tr F_M^(k)<=nbar`.

The theorem extends to adaptive/separable independent-event detection.

Continuum:

`boxed: int_R R_M(nu)dnu<=2Ebar^+/hbar`.

A two-quadrature flat-band guarantee implies

`boxed: Ebar^+>=hBq0`.

The coefficient is sharp and attained by the Cauchy/exponential covariant timestamp family.

### Two-sector collective theorem — WP18

For `q_0=1-p`, `q_1=p`, let `j=p(1-p)`. The random-time cosine/sine model is a two-parameter mixed-qubit transverse estimation problem with SLD QFI `J=jI_2`.

Direct Holevo optimization gives

`C_H(I)=2[1+|1-2p|]/[p(1-p)]`.

The asymptotically attainable isotropic source-normalized collective retention is

`boxed: q_coll=min(p,1-p)`.

For `p<=1/2`,

`boxed: q_coll=p=nbar`.

Thus the first collective-measurement hostile test passes exactly: collective readout improves over separable readout but does not violate the energy resource coefficient; it saturates it on the low-excitation branch.

For a gap of `k` sectors, `nbar=kp` and `q_coll<=nbar/k`.

The generic mixed-qubit Holevo calculation is prior art; the candidate contribution is the temporal random-distribution/resource mapping.

## Current highest-value problem

The remaining operational frontier is **multimode collective measurement** for multilevel excitations.

Target statement to prove or falsify:

`sum_{k>=1}R_coll(k)<=nbar`

for the asymptotically attainable collective information of all random-time modes, which would imply

`int_R R_coll(nu)dnu<=2Ebar^+/hbar`.

Start with three sectors and modes `k=1,2`, then seek a Holevo-dual/general proof.

## Other gates

- continue exact priority audit for WP10/WP17/WP18 mappings;
- strengthen the independent quantum-marked Poisson-to-field embedding;
- determine explicit analysis provenance of the harmonic-mean density functional;
- retain WP14's no-go against arbitrary coherent waveform synthesis.

Do not draft a foundational manuscript yet.

## Documentation rule

Every material result must update the WP note, active handoff/landing documents, and `main`.