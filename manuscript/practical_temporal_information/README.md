# Practical temporal-information manuscript workspace

**Branch:** `agent/practical-temporal-information-benchmarks`

## Provisional journal target

**Physical Review Applied — Regular Article.**

The target is provisional. Journal preferences must not drive theorem changes.

## Working title

> **Operational temporal-information benchmarks for photodetection**

Alternative retained for later title comparison:

> **Temporal-information benchmarks beyond static sensitivity and detector bandwidth**

## Current manuscript freeze — R4

The scientific text is frozen through R3; R4 is presentation-only.

Deterministic chain:

`draft -> R1 mechanical -> R2 theorem -> R3 hostile-review -> R4 presentation`.

Files:

- `operational_temporal_information_draft.tex` — first complete REVTeX baseline;
- `apply_r1_compile_fix.py` — mechanical REVTeX compatibility transform;
- generated `operational_temporal_information_r1.tex`;
- `apply_r2_support_strengthening.py`;
- `sections/support_crossover_r2.tex` — hardened theorem/protocol section;
- generated `operational_temporal_information_r2.tex`;
- `check_practical_r2.py` — R2 scientific isolation gate;
- `apply_r3_hostile_review_repairs.py`;
- generated `operational_temporal_information_r3.tex`;
- `check_practical_r3.py` — exact R3 whole-file gate;
- `apply_r4_presentation_cleanup.py`;
- generated `operational_temporal_information_r4.tex`;
- `check_practical_r4.py` — presentation-only isolation gate;
- `references.bib`;
- `MANUSCRIPT_ARCHITECTURE.md`.

## Exact R4 verification

Run `32684526293`, job `97307019940`: all gates PASS.

Artifact `9505218922`:

- archive size `322116` bytes;
- digest `sha256:9905a2cbd4366d57731fc8f4a99c6f72a513629a8727257a43131e02efb96cce`.

Exact R4 PDF:

- 8 pages;
- 266068 bytes;
- SHA-256 `794cb1c52326dc1965e14ea8ccd15530b41b2e523ca501e88f081cf69d741a01`.

All pages rendered at 180 dpi and inspected. No clipping, overlap, broken glyphs, black squares, equation overflow, unresolved references/citations, or overfull boxes. R3→R4 visual changes are restricted to removal of hyperlink borders.

Disposable PR #35 is closed unmerged; no open PRs remain.

## Scientific center

The paper should be understood first as detector physics and only second as an application of the broader temporal-information resource program.

Opening problem:

> DC sensitivity, response bandwidth, saturation curves, and timing jitter are useful detector specifications, but they do not generally determine how much information a detector transfers about a time-dependent optical signal.

Principal candidate original result:

For stationary selected modes separated by `hbar Omega`,

`rho_p=a_p|c><c|+p|s><s|+sigma_p`,

with stationary inert spectators and an incoherent/phase-randomized sideband seed,

`R_lin^2=a_p p/[kappa^2(a_p-p)^2]`,

and

**`lim_(p->0+)4p/R_lin^2=4kappa^2 q=Delta P_s(0)`.**

The finite-seed bound is `(R_lin^2/4)Tr F<=p`; the zero-seed boundary is attainable with `Tr F=Delta P_s(0)`.

The practical test reconstructs `R_lin` from baseline/tangent tomography, curvature from an independent zero-seed quadratic fit, and FI from a separate phase-sensitive measurement.

## Novelty boundary

Do not claim novelty for finite FI from quadratically vanishing boundary probabilities/eigenvalues. Gefen--Rotem--Retzker (2019) and Safranek (2017) are explicit close prior art.

Candidate distinct content is the finite-seed finite-radius continuation and the integrated operational/falsification architecture. Priority remains unverified/not certified.

## Claim hierarchy

### Candidate original Paper-4 content

- stationary selected-mode support-seed survival→synthesis crossover;
- practical independent-measurement/falsification architecture;
- ideal weak phase-modulation boundary saturator as an explicit realization under the locked convention.

### Cited companion results

- random-time/Type-II information incompleteness theorem;
- exact prescribed-curvature unitary-coupling theorem.

Do not reproduce their proofs or inherit their novelty claims.

### Standard bridge/background

- NEP/Fisher relation under explicit Gaussian/PSD conventions;
- ideal Poisson timestamp and independent-jitter relation;
- equal-DC-NEP/equal-bandwidth colored-noise counterexample;
- standard equal-frequency resonant beam-splitter Hamiltonian.

## Active task — figures, not theorem expansion

Create at most four deterministic journal figures with committed scripts and numerical checks. Do not edit R4 science while producing them.

After the figure package passes independently, integrate figures through a new isolated manuscript revision and rerun compile/render/hostile-review.

Only after figure integration should publication-style compression, author metadata, cover material, and fresh APS policy checks begin.
