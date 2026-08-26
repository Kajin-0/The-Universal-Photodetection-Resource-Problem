# Practical temporal-information manuscript workspace

**Branch:** `agent/practical-temporal-information-benchmarks`

## Provisional journal target

**Physical Review Applied — Regular Article.**

The target is provisional. Journal preferences must not drive theorem changes.

## Working title

> **Operational temporal-information benchmarks for photodetection**

Alternative retained for later title comparison:

> **Temporal-information benchmarks beyond static sensitivity and detector bandwidth**

## Current manuscript freeze — R5

Deterministic chain:

`draft -> R1 mechanical -> R2 theorem -> R3 hostile-review -> R4 presentation -> R5 figures`

R5 is the canonical figure-integrated manuscript baseline.

### Source layers

- `operational_temporal_information_draft.tex` — first complete REVTeX baseline;
- `apply_r1_compile_fix.py` — mechanical REVTeX compatibility transform;
- `apply_r2_support_strengthening.py` + `sections/support_crossover_r2.tex` — hardened stationary-spectator theorem/protocol;
- `check_practical_r2.py` — R2 scientific isolation gate;
- `apply_r3_hostile_review_repairs.py` — stale-reference and equal-frequency benchmark repairs;
- `check_practical_r3.py` — R3 exact isolation gate;
- `apply_r4_presentation_cleanup.py` — hyperlink-border presentation only;
- `check_practical_r4.py` — R4 presentation isolation;
- `figures/` — frozen deterministic WP12 figure package;
- `r5_figure_blocks.py` — exact four figure/caption blocks;
- `apply_r5_figure_integration.py` — additive R5 transform;
- `check_practical_r5.py` — removes all four blocks and requires exact recovery of R4;
- `references.bib`;
- `MANUSCRIPT_ARCHITECTURE.md`.

## Exact R5 verification

Run `32915363157`, job `98017843874`: all gates PASS.

Source commit:

`55ec3af3bd9d57830c03f65655180936eb85eda9`

Artifact `9588018384`:

- archive size `615446` bytes;
- digest `sha256:06e1de8d8f5e44f9d62e6ebd06362d2cfbc93132014718398e57b877c784c281`.

Exact R5 PDF:

- 10 pages;
- 429432 bytes;
- SHA-256 `fd451a59ca5b70731b61f7ce237bd06a1d5f7105305e064cfe21bbb588e6bf48`.

All ten pages were rendered independently at 200 dpi and inspected. No clipping, overlap, broken glyphs, black squares, equation overflow, unresolved references/citations, overfull boxes, or figure/caption collisions remain.

## Frozen figure package

WP12 standalone verification:

- run `32914889053` PASS;
- artifact `9587797682`;
- digest `sha256:261acabd321706ad73dfb873bf9ca4fbc7f81722a80f316be4318578eb43bf91`.

R5 manuscript CI re-generates the four vector PDFs in the pinned environment and checks their exact canonical SHA-256 identities before integrating them.

Do not redesign figures or alter their numerical values during ordinary text cleanup.

## Scientific center

The paper should be read first as detector physics and second as an application of the broader temporal-information resource program.

Principal candidate original result:

For stationary selected modes separated by `hbar Omega`,

`rho_p=a_p|c><c|+p|s><s|+sigma_p`,

with stationary inert spectators and an incoherent/phase-randomized sideband seed,

`R_lin^2=a_p p/[kappa^2(a_p-p)^2]`,

and

**`lim_(p->0+)4p/R_lin^2=4kappa^2 q=Delta P_s(0)`.**

The finite-seed bound is `(R_lin^2/4)Tr F<=p`; the zero-seed boundary is attainable with `Tr F=Delta P_s(0)`.

The practical test obtains `R_lin`, zero-seed curvature, and Fisher information from independent measurements.

## Novelty boundary

Do not claim novelty for finite FI from quadratically vanishing boundary probabilities/eigenvalues. Gefen--Rotem--Retzker (2019) and Safranek (2017) are explicit close prior art.

Candidate distinct content is the finite-seed finite-radius continuation and the integrated operational/falsification architecture. Priority remains unverified/not certified.

## Claim hierarchy

### Candidate original Paper-4 content

- stationary selected-mode support-seed survival→synthesis crossover;
- practical independent-measurement/falsification architecture;
- ideal weak phase-modulation boundary saturator under the locked convention.

### Cited companion results

- random-time/Type-II information incompleteness theorem and matched-recovery benchmark;
- exact prescribed-curvature unitary-coupling theorem.

### Standard bridge/background

- NEP/Fisher relation under explicit Gaussian/PSD conventions;
- ideal Poisson timestamp and independent-jitter relation;
- equal-DC-NEP/equal-bandwidth colored-noise example;
- standard equal-frequency resonant beam-splitter Hamiltonian.

## Active task — hostile compression audit

R5 science and figures are frozen. Do not add new material.

Next:

1. read R5 as a PRA referee/editor and identify repeated/tutorial prose only;
2. create R6 only if the reduction is materially useful;
3. R6 must be a deterministic text-only transform with an explicit allowed-edit map;
4. preserve all four R5 figure blocks exactly;
5. preserve theorem/proposition/equation/proof content and disclosures unless a genuine defect is discovered;
6. compile, warning-check, render, and adversarially review R6 independently;
7. after final text freeze, fresh-check current APS/PRA submission policy and prepare author/companion metadata.

Latest authoritative notes:

- `practical_temporal_information/notes/WP12_PUBLICATION_FIGURE_PACKAGE.md`
- `practical_temporal_information/notes/WP13_R5_FIGURE_INTEGRATION_FREEZE.md`
