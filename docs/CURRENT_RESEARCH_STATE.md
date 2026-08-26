# Current Research State

**Last synchronized:** 2026-08-25

**Active branch:** `agent/practical-temporal-information-benchmarks`

## Frozen upstream scientific layers

The three mature temporal-information papers remain scientifically frozen:

1. PRX Quantum flagship — *Two spectral-resource regimes for autonomous temporal information*;
2. random-time/timestamp spectral-information paper;
3. PRA dynamical completion — *Exact minimum unitary coupling cost of prescribed rank-changing quantum-state curvature*.

WP31 remains superseded; WP32 is the canonical implementation theorem and WP33 remains PASS under its stated assumptions.

## Paper 4 — practical/falsifiability bridge

Working title:

> **Operational temporal-information benchmarks for photodetection**

Provisional journal target: **Physical Review Applied**.

The Paper-4 theorem and figure-development phases are closed. Current canonical manuscript baseline: **R5**.

## Frozen principal theorem

Let `H` be the free optical Hamiltonian and select `|c>`, `|s>` with

`E_s-E_c=hbar Omega`.

Use the stationary baseline

`rho_p=a_p|c><c|+p|s><s|+sigma_p`,

with:

- `[rho_p,H]=0`;
- stationary positive spectator block `sigma_p`;
- `a_p>p`, `a_p->q>0` as `p->0+`;
- incoherent/phase-randomized sideband population seed `p`;
- calibrated local converter acting only on the selected pair.

Then

`R_lin^2=a_p p/[kappa^2(a_p-p)^2]`,

and the frozen flagship theorem specializes exactly to

`(R_lin^2/4)Tr F<=p`.

At zero seed,

`Delta P_s(0)=4kappa^2 q`,

so

**`lim_(p->0+)4p/R_lin^2=4kappa^2 q=Delta P_s(0)`.**

A completed equatorial POVM gives

`Tr F=4qkappa^2=Delta P_s(0)`.

The operational test is noncircular:

1. baseline + tangent tomography -> `R_lin`;
2. independent zero-seed quadratic population fit -> `Delta P_s(0)`;
3. separate phase-sensitive likelihood -> Fisher matrix.

## Novelty boundary

Gefen--Rotem--Retzker (2019) and Safranek (2017) already establish the general mechanism of finite FI from quadratically vanishing boundary probabilities/eigenvalues.

Paper 4 therefore claims only the narrower finite-seed finite-radius continuation and its independent detector-facing measurement/falsification architecture. Priority remains **unverified, not certified**.

## Companion and standard content

- Generalized Type-II memory theorem and matched-recovery timestamp benchmark: frozen random-time companion.
- Prescribed-curvature minimum unitary-coupling theorem: frozen PRA companion.
- `Tr F/T=2/NEP(f)^2`, ideal Poisson/jitter relations, colored-noise specification example, weak phase modulation, and resonant beam-splitter mechanics: standard/illustrative background.

These provenance boundaries must remain explicit.

## Deterministic manuscript chain

Workspace:

`manuscript/practical_temporal_information/`

Chain:

`draft -> R1 mechanical -> R2 theorem -> R3 hostile-review -> R4 presentation -> R5 figures`

- R1 removes REVTeX-incompatible table/list mechanics only.
- R2 changes only the support section to the hardened stationary-spectator theorem/protocol.
- R3 changes only stale references plus the equal-frequency resonance clarification.
- R4 adds only hidden hyperlink presentation.
- R5 adds exactly four frozen WP12 figure/caption blocks.

Every layer has an explicit isolation gate.

## WP12 figure freeze

Standalone figure package:

- run `32914889053` PASS;
- job `98016438281` PASS;
- artifact `9587797682`;
- digest `sha256:261acabd321706ad73dfb873bf9ca4fbc7f81722a80f316be4318578eb43bf91`.

The four vector-PDF identities are hash-locked and are rechecked before every R5 build.

## Exact R5 freeze

Workflow run `32915363157`, job `98017843874`: **PASS**.

Source commit:

`55ec3af3bd9d57830c03f65655180936eb85eda9`

Artifact:

- ID `9588018384`;
- name `practical-temporal-information-r5`;
- archive size `615446` bytes;
- archive digest `sha256:06e1de8d8f5e44f9d62e6ebd06362d2cfbc93132014718398e57b877c784c281`.

Exact PDF:

- 10 pages;
- 429432 bytes;
- SHA-256 `fd451a59ca5b70731b61f7ce237bd06a1d5f7105305e064cfe21bbb588e6bf48`.

The exact artifact PDF was rendered independently at 200 dpi and every page inspected. No clipping, overlap, broken glyphs, equation overflow, unresolved references/citations, overfull boxes, or figure/caption collisions remain. Data Availability and AI-assisted-research disclosures remain intact.

Authoritative freeze note:

`practical_temporal_information/notes/WP13_R5_FIGURE_INTEGRATION_FREEZE.md`

## Active work

No new theorem or figure development.

Next:

1. hostile-read R5 for redundant/tutorial prose;
2. create a deterministic text-only R6 only if compression materially improves the paper;
3. preserve the frozen theorem/equation/proof stack and all four frozen figure blocks unless a genuine defect is found;
4. compile/render/adversarially audit any R6;
5. then fresh-check APS/PRA policies and prepare submission metadata, companion citation status, and cover material.

## Claim discipline

No novelty claim for standard NEP, generic Fisher sensing, Poisson/dead-time formulas, random dead time, interval characterization, electro-optic sidebands, seeded/vacuum interferometry, beam-splitter Hamiltonians, standard interferometry, or generic boundary-QFI behavior. No prize-level framing and no implied experimental validation without data.
