# The Universal Photodetection Resource Problem

**Status synchronized: 2026-08-22**

## Project split

1. **Paper 1 / Rev11** — frozen.
2. **Paper 2 / Rev7** — frozen.
3. **Grand Challenge** — science frontier **WP28**; **Rev11 frozen as the preferred PRX Quantum manuscript**.

Active branch: `agent/temporal-information-resource-law`.

Authoritative handoff: `grand_challenge/AGENTS.md`.

# Grand Challenge — Spectral Resource Laws for Temporal Fisher Information

## Exact periodic theorem

For exact periodic random-time encoding with sector probabilities `q_n`, any finite `N` and **any joint POVM**, including entangled collective measurements, obey

`Tr F_N^(k)/N <= min(D_k,U_k) <= T_k`,

where `T_k=sum_(m>=k)q_m`.

Thus `sum_(k>=1)R_N(k)<=nbar`.

## Rev11: the mechanism is not a harmonic-ladder artifact

For an arbitrary semibounded pure-point Hamiltonian

`H=E_* I + hbar sum_alpha omega_alpha P_alpha`,

with no equal-spacing or commensurability assumption, fix a requested modulation frequency `nu`. Long-window random-time averaging isolates exact Bohr pairs `omega_beta-omega_alpha=nu` and gives

`A_nu=rho0^(1/2)V_nu rho0^(1/2)`.

Therefore the same arbitrary-measurement proof yields

`Tr F_N^(nu)/N <= min(D_nu,U_nu) <= S(nu)=Pr(Omega>=nu)`

for every finite `N` and arbitrary joint POVM.

If no exact Bohr pair exists at `hbar nu`, the limiting local Fisher response at that gap vanishes. Anharmonicity can strengthen the restriction rather than invalidate it.

## Continuum survival law

Controlled periodic-to-continuum limits satisfy

`R(nu)<=Pr(Omega>=nu)`.

The spectral measure may be atomic, absolutely continuous, singular-continuous, or mixed; no density or smoothness is assumed.

`Ebar+=hbar<Omega>` is mean excess energy above the participating lower edge. The area and `hfR` relations are first-moment corollaries.

## One physical measurement has global spectral geometry

For **one fixed one-copy POVM**, the periodic retention sequence is Herglotz/positive definite:

`R_M(k)=int cos(k theta)J_M(dtheta)`.

The same structure applies across exact multiples `m nu` of a chosen Bohr gap for an arbitrary semibounded pure-point Hamiltonian. Zero-population completion is an algebraic dilation only and cannot create Fisher information.

Combining the Herglotz constraint with semibounded tails gives

`Ebar+>=hbar nu A(R_M(nu))`,

with `A(q)~1/sqrt(2(1-q))` as `q->1`.

A finite sine-profile family proves the `(1-R)^(-1/2)` divergence exponent is **sharp**; the optimal prefactor is not claimed.

## Complete one-copy extremizers

The exact converse remains deliberately narrower. On the full contiguous pure-sector chain:

`first-harmonic equality`

`<=> geometric-mixture populations`

`<=> Hausdorff-moment survival tails`

`<=> one source-adapted POVM saturates every harmonic simultaneously`.

Controlled continuum limits of exponential mixtures give the completely monotone equality cone.

## Physical source-to-record scope

Independent quantum-marked Poisson sources inherit the modewise law through arbitrary **parameter-independent** source-to-field and detector processing. Arbitrary parameter-dependent waveform-state synthesis remains outside the theorem; the coherent-sideband counterexample is the explicit boundary.

# Rev11 final preflight

Rev11 replaced the peripheral separately optimized SLD-QFI section with the fixed-Hamiltonian Bohr-gap theorem.

Final local gate:

- full LaTeX/BibTeX build: **PASS**;
- **12 pages**;
- unresolved citations/references: **0**;
- overfull boxes: **0**;
- all pages rendered at 200 dpi and visually inspected: **PASS**;
- all six numerical validators: **PASS**;
- PDF SHA-256: `5e0ac0132a7f4a3f7b07e9c4ba86b046b23bc89c1f7635efe9f737019396d0f0`;
- source ZIP SHA-256: `208fd7a2e932507366797658c84dff1666257477143a433bf81d7741a8d0c8a1`;
- fresh source-package compile: **PASS**;
- 200-dpi comparison against fresh source-package compile: **0 changed pixels on all 12 pages**.

Detailed preflight:
`grand_challenge/notes/MANUSCRIPT_REV11_ANHARMONIC_PREFLIGHT_2026-08-22.md`.

The current connector does not expose the relevant branch-push Actions run; no direct remote-run result is claimed.

# Prior-art boundary

Arbitrary Bohr-frequency decompositions, random-time dephasing, `U(1)` modes, Herglotz/Bochner mathematics, moment theory, canonical phase measurements, sine states, and generic QFI/CPTP machinery are prior art.

The candidate contribution is the operational arbitrary-POVM Fisher-tail coefficient, its exact-Bohr-gap extension, the fixed-measurement spectral consistency/energy law, sharp near-lossless exponent, contiguous-chain extremizer classification, and source-to-record inheritance.

**Priority remains unverified, not certified.**

# Journal target

**First target:** PRX Quantum — Research Article.

**Fallback:** Physical Review A — Regular Article.

# Current work order

**Freeze Rev11.** Reopen only for a concrete mathematical defect, priority collision, substantive referee objection, build/render regression, or unavoidable journal-format requirement.

Do not reintroduce “human verification” as a research/manuscript completion gate. The finished package is produced as far as possible and then submitted by a human.
