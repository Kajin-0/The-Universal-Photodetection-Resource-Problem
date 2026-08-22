# The Universal Photodetection Resource Problem

**Status synchronized: 2026-08-21**

## Project split

1. **Paper 1 / Rev11** — frozen and technically validated.
2. **Paper 2 / Rev7** — frozen preferred science draft.
3. **Grand Challenge** — ACTIVE on `agent/temporal-information-resource-law`, theorem stack through **WP18**.

Authoritative handoff: `grand_challenge/AGENTS.md`.

## Current theorem hierarchy

### Modewise QFI envelope — WP10/WP12/WP15

`G_Q(k)=2 sum_n q_nq_{n+k}/(q_n+q_{n+k})`, with

`sum_{k>=1}G_Q(k)<=2nbar`.

Continuum:

`int_R G_Q(nu)dnu<=pi Ebar^+/hbar`.

This is a separately optimized QFI envelope. WP16 shows the sharp `pi/4` operator constant is classical Hardy–Hilbert prior art.

### Sharp fixed/separable operational law — WP17

For one fixed arbitrary POVM,

`sum_{k>=1}Tr F_M^(k)<=nbar`.

For adaptive/separable independent-event detection the same source-normalized law survives by the classical FI chain rule.

Continuum:

`int_R R_M(nu)dnu<=2Ebar^+/hbar`.

A full-quadrature band guarantee requires

`Ebar^+>=hBq0`.

The coefficient is sharp and saturated by the Cauchy/exponential covariant timestamp family.

### Minimal collective closure — WP18

For a two-sector state with `q_0=1-p`, `q_1=p`, the asymptotic Holevo optimum for simultaneous cosine/sine estimation is

`boxed: q_coll=min(p,1-p)`.

For `p<=1/2`,

`boxed: q_coll=p=nbar`.

Thus collective measurements can beat separable readout but cannot exceed the mean-excitation resource ceiling in the minimal model; on the resource-sharp branch they exactly saturate it.

The generic mixed-qubit Holevo calculation is prior art. The candidate contribution is the mapping to the random-time Fourier-mode resource problem.

## Current highest-value gate

The unsolved problem is now **multimode collective readout**:

> Does arbitrary collective measurement on many independently twirled multilevel excitations obey `sum_k R_coll(k)<=nbar`, and hence the continuum operational law `int_R R_coll<=2E/hbar`?

The immediate attack is three energy sectors with modes `k=1,2`, followed by a Holevo-dual/general proof attempt.

## Scope boundary

WP14 blocks any claim that baseline mean energy controls arbitrary coherent waveform state engineering. The current theorem concerns random temporal-distribution encoding of a fixed semibounded-energy excitation.

## Read first

1. `grand_challenge/AGENTS.md`
2. `grand_challenge/notes/WP18_TWO_SECTOR_COLLECTIVE_HOLEVO_CLOSURE.md`
3. `grand_challenge/notes/WP17_SINGLE_MEASUREMENT_OPERATIONAL_MODE_BUDGET.md`
4. `grand_challenge/notes/WP16_DEEP_PRIORITY_AUDIT_RANDOM_TIME_QFI_AND_HARDY_HILBERT_COLLISION.md`
5. `grand_challenge/notes/WP15_GENERAL_DENSITY_PROOF_OF_SHARP_PI_AREA_INEQUALITY.md`
6. `grand_challenge/notes/WP14_COHERENT_FIELD_BASELINE_ENERGY_NO_GO.md`
7. `grand_challenge/notes/WP13_SECOND_QUANTIZED_SCOPE_AND_POISSON_EVENT_EMBEDDING.md`

## Documentation discipline

Every material result must be recorded in the repository and mirrored onto `main`; do not rely on chat history.