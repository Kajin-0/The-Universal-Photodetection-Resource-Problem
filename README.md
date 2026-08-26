# The Universal Photodetection Resource Problem

**Status synchronized:** 2026-08-25

The repository is authoritative; chat history is not.

## Publication architecture

Preserve the mature papers separately:

1. PRX Quantum flagship — *Two spectral-resource regimes for autonomous temporal information*.
2. Broad random-time/timestamp spectral-information paper.
3. PRA dynamical completion — *Exact minimum unitary coupling cost of prescribed rank-changing quantum-state curvature*.

Active branch:

`agent/practical-temporal-information-benchmarks`

Fourth-paper working title:

> **Operational temporal-information benchmarks for photodetection**

Provisional target: **Physical Review Applied**.

## Paper 4 — R5 frozen

The fourth paper has completed theorem development, two hostile scientific audits, deterministic source isolation, standalone figure generation, figure integration, clean CI compilation, and full-manuscript render QA.

Final R5 verification:

- run `32915363157` — PASS;
- job `98017843874` — PASS;
- source commit `55ec3af3bd9d57830c03f65655180936eb85eda9`;
- artifact `9588018384`;
- archive digest `sha256:06e1de8d8f5e44f9d62e6ebd06362d2cfbc93132014718398e57b877c784c281`;
- PDF: 10 pages, 429432 bytes;
- PDF SHA-256 `fd451a59ca5b70731b61f7ce237bd06a1d5f7105305e064cfe21bbb588e6bf48`.

All ten pages were independently rendered at 200 dpi and inspected. R5 equals frozen R4 plus exactly four frozen figure/caption blocks; removing those blocks restores R4 byte-for-byte.

## Frozen WP12 figure package

Standalone figure CI:

- run `32914889053` — PASS;
- job `98016438281` — PASS;
- artifact `9587797682`;
- artifact digest `sha256:261acabd321706ad73dfb873bf9ca4fbc7f81722a80f316be4318578eb43bf91`.

Every R5 build re-generates the four vector PDFs with pinned dependencies and checks their exact canonical SHA-256 identities before manuscript integration.

## Principal candidate Paper-4 result

Select stationary free-Hamiltonian modes `|c>`, `|s>` with `E_s-E_c=hbar Omega` and use

`rho_p=a_p|c><c|+p|s><s|+sigma_p`,

with `[rho_p,H]=0`, stationary inert spectators, `a_p>p`, `a_p->q>0`, an incoherent/phase-randomized sideband population seed, and a calibrated converter acting only on the selected pair.

Then

`R_lin^2=a_p p/[kappa^2(a_p-p)^2]`,

and the frozen flagship finite-radius theorem specializes exactly to

`(R_lin^2/4)Tr F<=p`.

At zero seed,

`Delta P_s(0)=4kappa^2 q`,

hence

**`lim_(p->0+)4p/R_lin^2=4kappa^2 q=Delta P_s(0)`.**

A completed equatorial POVM attains

`Tr F=4qkappa^2=Delta P_s(0)`.

The practical comparison is deliberately noncircular: baseline/tangent tomography determines `R_lin`, an independent zero-seed quadratic fit determines `Delta P_s(0)`, and a separate phase-sensitive likelihood determines the Fisher matrix.

## Novelty boundary

Finite Fisher information from quadratically vanishing boundary probabilities/eigenvalues is already established in the boundary-QFI/superresolution literature, including Gefen--Rotem--Retzker (2019) and Safranek (2017).

Paper 4 therefore claims only the narrower finite-seed finite-radius continuation and its detector-facing independent-measurement/falsification architecture. Priority remains **unverified, not certified**.

## Companion-derived benchmarks

- Generalized Type-II recovery: fixed mean recovery fixes `r=lambda exp(-lambda m)` but not timestamp information; deterministic recovery is uniquely DC-information-singular at the common maximum. This belongs to the frozen random-time companion.
- Equal-frequency resonant implementation: `V_min=(1/2)Tr C=8(gt)^2`, with `A_ex=hbar nu V_min`, is a standard benchmark of the frozen PRA theorem.

Standard NEP/FI, Poisson/jitter, colored-noise, phase-modulation, and beam-splitter material is illustrative/background, not fundamental novelty.

## Falsification hierarchy

1. **Level I:** detector/state/implementation model failure.
2. **Level II:** resource-law challenge only after independent verification of theorem assumptions and resource quantities.
3. **Level III:** failure of an ideal saturating benchmark/equality.

## Current work order

The theorem and figure-development phases are closed.

Next permitted work:

1. hostile-read R5 for removable tutorial/redundant prose;
2. if worthwhile, define a deterministic text-only R6 with an explicit allowed-edit map;
3. preserve the frozen theorem/equation/proof stack and all four frozen figure blocks unless a genuine defect is found;
4. compile/render/adversarially audit R6;
5. then fresh-check APS/PRA policies and prepare submission metadata.

No prize-level framing and no implied experimental validation without data.

## Frozen companion publication packages

PRXQ R4: run `32674844366` PASS; artifact `9502376602`.

PRA R1: run `32673160217` PASS; artifact `9501942180`.
