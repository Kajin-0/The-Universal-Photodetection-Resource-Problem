# The Universal Photodetection Resource Problem

**Status synchronized: 2026-08-22**

## Project split

1. **Paper 1 / Rev11** — frozen.
2. **Paper 2 / Rev7** — frozen.
3. **Grand Challenge** — science frontier **WP27**; Rev10 referee-closure manuscript in final build gate.

Active branch: `agent/temporal-information-resource-law`.

Authoritative handoff: `grand_challenge/AGENTS.md`.

# Grand Challenge — spectral resource laws for temporal Fisher information

For exact periodic random-time encoding with sector probabilities `q_n`, any finite number `N` of independently encoded excitations and **any joint POVM**, including entangled collective measurements, obey

`Tr F_N^(k)/N <= min(D_k,U_k) <= T_k`,

where

`T_k=sum_(m>=k)q_m`.

Therefore

`sum_(k>=1) R_N(k) <= nbar`.

The controlled periodic-to-continuum theorem is

`R(nu) <= Pr(Omega>=nu)`,

with `Ebar+=hbar<Omega>` the mean excess energy above the participating lower edge. The familiar `hfR` inequality is only a first-moment corollary.

## New Rev9/Rev10 layer: one detector record has global spectral geometry

For **one fixed one-copy POVM**, the complete harmonic retention sequence is a Herglotz sequence:

`R_M(k)=int cos(k theta) J_M(dtheta)`.

Thus every Toeplitz matrix `[R_M(i-j)]` is positive semidefinite: the temporal-information retained at different harmonics by one actual measurement cannot be selected independently.

Combining this cross-harmonic consistency with the semibounded energy tails gives

`Ebar+ >= hbar nu A(R_M(nu))`,

with

`A(q) ~ 1/sqrt(2(1-q))` as `q->1`.

Hence near-unit retention at any nonzero frequency requires divergent mean excess energy in the fixed-one-copy/common-measurement setting.

Rev10 proves the exponent is **sharp**. For the finite sine profile

`a_n=sqrt(2/(L+1)) sin((n+1)pi/(L+1))`,

canonical phase measurement gives

`R_L(1)=cos^2(pi/(L+1))`,

`nbar_L=(L-1)/2`,

so

`nbar_L ~ pi/[2 sqrt(1-R_L(1))]`.

The lower and upper constructions therefore match in the `(1-R)^(-1/2)` exponent. The optimal prefactor is not claimed.

## Complete one-copy extremizers

On the full contiguous pure-sector chain, exact first-harmonic saturation is equivalent to

`q_n=int (1-r)r^n pi(dr)`,

or equivalently

`T_k=int r^k pi(dr)`.

Thus:

`first-harmonic equality`

`<=> geometric-mixture populations`

`<=> Hausdorff-moment survival tails`

`<=> one common source-adapted POVM saturates every harmonic simultaneously`.

Controlled continuum limits of exponential mixtures give the completely monotone equality cone, including algebraic exact-retention laws.

## Physical source-to-record scope

Independent quantum-marked Poisson sources inherit the modewise survival law through arbitrary **parameter-independent** source-to-field and detector processing. Bosonic overlap, propagation, loss, mode mixing, coherent detector memory, ancillas, and final joint measurement cannot evade the source ceiling within this source class.

The theorem does not cover arbitrary parameter-dependent waveform-state synthesis; the coherent-sideband counterexample remains the explicit boundary.

# Rev10 referee closure

The external Rev9 re-review found no central mathematical failure and recommended only two mandatory-looking repairs plus one optional significance enhancement. Rev10 implements all three:

- Bochner is invoked only after continuity at the origin is assumed;
- the high-retention divergence is consistently labeled **fixed one-copy/common-POVM**;
- a finite-chain sine-profile family proves the divergence exponent is sharp.

The sine state itself is established phase-estimation prior art; only its role as a sharpness witness for this new retention--energy law is used here.

# Journal target

**First target:** PRX Quantum — Research Article.

**Fallback:** Physical Review A — Regular Article.

**Priority remains unverified, not certified.**

# Current work order

Complete the Rev10 CI/build/render gate, then freeze Rev10. Do not start a new asymptotic-constant optimization project or add further examples unless a concrete referee objection, theorem defect, priority collision, or journal-format requirement appears.

Do not reintroduce “human verification” as a research/manuscript completion gate. The finished package is produced as far as possible and then submitted by a human.
