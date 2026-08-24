# Current Research State

**Last synchronized:** 2026-08-23

**Active branch:** `agent/practical-temporal-information-benchmarks`

## Frozen upstream scientific layers

The three mature temporal-information papers remain scientifically frozen in their theorem/proof layers:

1. PRX Quantum flagship — *Two spectral-resource regimes for autonomous temporal information*;
2. random-time/timestamp spectral-information paper;
3. PRA dynamical completion — *Exact minimum unitary coupling cost of prescribed rank-changing quantum-state curvature*.

WP31 remains superseded; WP32 is the canonical implementation theorem and WP33 remains PASS under stated assumptions.

## Active Paper 4 — practical/falsifiability bridge

Working title:

> **Operational temporal-information benchmarks for photodetection**

Provisional journal target: **Physical Review Applied**.

The Paper-4 theorem/manuscript expansion phase is now closed at **R4**. Active work has moved to deterministic publication figures.

## Completed Paper-4 gates

- WP01–WP06: detector-language bridges, memory/support/implementation benchmarks, scope and falsification architecture.
- WP07: prior-art/significance — **PASS WITH NARROWED CLAIMS**.
- WP07A: close boundary-FI prior art identified and novelty claim narrowed.
- WP08: final pre-manuscript stack — **PASS**.
- WP09: first hostile manuscript audit — theorem generalized to stationary selected carrier/sideband pair with inert spectators.
- WP10: second hostile audit — coefficient/provenance checks PASS; stationarity, incoherent seed, noncircular `R_lin` reconstruction, reference migration, and equal-frequency resonance assumptions repaired.
- WP11: exact R3/R4 build/render audit — **PASS**.

## Frozen principal Paper-4 theorem

Let `H` be the free optical Hamiltonian and select `|c>`, `|s>` with

`E_s-E_c=hbar Omega`.

Use the stationary baseline

`rho_p=a_p|c><c|+p|s><s|+sigma_p`,

with:

- `[rho_p,H]=0`;
- stationary positive spectator block `sigma_p` on the orthogonal spectator subspace;
- `a_p>p` and `a_p->q>0` as `p->0+`;
- incoherent/phase-randomized sideband population seed `p`;
- calibrated local lossless converter acting only on the selected pair.

Then

`P_s(p;r)=p+(a_p-p)sin^2(kappa r)`,

and the exact affine physical radius is

`R_lin^2=a_p p/[kappa^2(a_p-p)^2]`.

Direct audit against the frozen flagship shows its endpoint projector is the range-support projector of the particular `+Omega` tangent. Thus `P_U,Omega=|s><s|` and `U_Omega=p` exactly, even with allowed spectators. Therefore

`(R_lin^2/4)Tr F<=p`.

At the zero-seed boundary,

`Delta P_s(0)=4kappa^2 q`,

hence

**`lim_(p->0+)4p/R_lin^2=4kappa^2 q=Delta P_s(0)`.**

A completed equatorial POVM gives

`F_xx=F_yy=2qkappa^2`, `F_xy=0`,

so

`Tr F=4qkappa^2=Delta P_s(0)`.

## Noncircular operational test

Paper 4 now separates the measurements:

1. baseline + first-derivative/tangent tomography -> `R_lin`;
2. zero-seed second-order sideband-population fit -> `Delta P_s(0)`;
3. independent phase-sensitive likelihood -> Fisher matrix.

This avoids defining the radius from the same curvature data used to test the crossover.

## Novelty boundary

Gefen--Rotem--Retzker (2019) and Safranek (2017) already establish the general mechanism of finite Fisher information from quadratically vanishing boundary probabilities/eigenvalues. Paper 4 does not claim that mechanism.

Candidate distinct content is the finite-seed finite-radius continuation

`4p/R_lin^2 -> Delta P_s(0)`

plus the detector-facing independent-measurement and falsification architecture.

Priority remains **unverified, not certified**.

## Other retained content

### Standard analog/timestamp bridge

`Tr F/T=2/NEP(f)^2`

under the locked one-sided-PSD / peak-quadrature convention.

Ideal fractional Poisson timestamps give `Tr F/T=lambda0`; independent timing jitter gives factor `|Phi_J(Omega)|^2`.

WP08 shows equal DC NEP and equal response bandwidth can coexist with a `13/3≈4.33` FI ratio at the nominal bandwidth.

### Frozen Paper-2 memory benchmark

For arbitrary finite-mean iid Type-II recovery, fixing mean recovery fixes the homogeneous saturation curve

`r=lambda exp(-lambda m)`

but not timestamp information. At the common maximum deterministic recovery is uniquely information-singular. This remains a cited companion result, not Paper-4 novelty.

### Frozen PRA implementation benchmark

For equal-frequency resonant modes,

`H_0=hbar nu(N_C+N_S)`,

the fixed `N_tot=2` shell gives

`V_min=8(gt)^2=(1/2)Tr C`,

`A_ex=hbar nu V_min`.

The exchange operators commute with `H_0`; unequal bare frequencies require an explicit pump/controller for global energy conservation. This is a practical benchmark of the companion theorem.

## Deterministic manuscript revisions

Workspace:

`manuscript/practical_temporal_information/`

Chain:

`draft -> R1 mechanical -> R2 theorem -> R3 hostile-review -> R4 presentation`.

- R1 removes REVTeX-incompatible table/list machinery only.
- R2 changes only the support-crossover section to the hardened stationary-spectator theorem/protocol.
- R3 changes only three stale references plus the equal-frequency resonance clarification.
- R4 adds only `\\hypersetup{hidelinks}`.

Every layer has an exact isolation gate.

## Exact R4 freeze

Workflow run `32684526293`, job `97307019940`: **PASS**.

Artifact:

- ID `9505218922`;
- name `practical-temporal-information-r4`;
- archive size `322116` bytes;
- archive digest `sha256:9905a2cbd4366d57731fc8f4a99c6f72a513629a8727257a43131e02efb96cce`.

Exact PDF:

- 8 pages;
- 266068 bytes;
- SHA-256 `794cb1c52326dc1965e14ea8ccd15530b41b2e523ca501e88f081cf69d741a01`.

All eight pages rendered at 180 dpi and inspected: no clipping, overlap, broken glyphs, black squares, equation overflow, unresolved references/citations, or overfull boxes. Direct R3→R4 render diff changes only former hyperlink-border rectangles.

Disposable PR #35 was closed **unmerged**. There are currently zero open PRs.

## Active work — WP12 publication figures

Do not reopen theorem expansion.

Produce at most four deterministic scientific figures:

1. equal conventional detector specs / unequal FI spectra;
2. common Type-II saturation / different timestamp information, clearly attributed to companion work;
3. stationary support-seed survival→synthesis crossover, including independent radius/curvature/FI measurement routes;
4. equal-frequency resonant implementation + calibration/falsification map.

Each figure requires committed generation source, analytic/numerical checks, journal-legible rendering, and visual QA. Integrate only after the figure package passes independently.

After figure integration: compile, render, hostile-review again, then perform publication compression and fresh APS policy/submission checks.

## Claim discipline

No novelty claim for standard NEP, generic Fisher sensing, Poisson/dead-time formulas, random dead time, interval characterization, electro-optic sidebands, seeded/vacuum interferometry, beam-splitter Hamiltonians, standard interferometry, or generic boundary-QFI behavior. No prize-level framing and no implied experimental validation without data.

Every material advance must update its handoff and all top-level landing files.
