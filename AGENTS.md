# AGENTS.md

## Purpose

Durable handoff for The Universal Photodetection Resource Problem. The repository, not chat history, is authoritative.

## Active branch

`agent/practical-temporal-information-benchmarks`

The three mature temporal-information papers remain scientifically frozen. The fourth practical/falsifiability paper is frozen at **R5** with its four-figure package integrated.

## Read first

1. `docs/CURRENT_RESEARCH_STATE.md`
2. `practical_temporal_information/AGENTS.md`
3. `practical_temporal_information/notes/WP13_R5_FIGURE_INTEGRATION_FREEZE.md`
4. `practical_temporal_information/notes/WP12_PUBLICATION_FIGURE_PACKAGE.md`
5. `practical_temporal_information/notes/WP11_R3_RENDER_AUDIT_AND_R4_PRESENTATION_FREEZE.md`
6. `practical_temporal_information/notes/WP10_R2_BUILD_AND_SECOND_HOSTILE_AUDIT.md`
7. `manuscript/practical_temporal_information/README.md`

## Current Paper-4 freeze

Working title:

> **Operational temporal-information benchmarks for photodetection**

R5 verification:

- run `32915363157` PASS;
- job `98017843874` PASS;
- source commit `55ec3af3bd9d57830c03f65655180936eb85eda9`;
- artifact `9588018384`;
- archive digest `sha256:06e1de8d8f5e44f9d62e6ebd06362d2cfbc93132014718398e57b877c784c281`;
- PDF 10 pages / 429432 bytes;
- PDF SHA-256 `fd451a59ca5b70731b61f7ce237bd06a1d5f7105305e064cfe21bbb588e6bf48`.

The exact artifact was rendered at 200 dpi and all ten pages inspected. R5's checker proves that deleting its four exact frozen figure/caption blocks restores R4 byte-for-byte.

WP12 figures are separately frozen: run `32914889053`, artifact `9587797682`; R5 CI hash-checks all four canonical vector PDFs before integration.

## Frozen Paper-4 theorem

For stationary selected modes with `E_s-E_c=hbar Omega`,

`rho_p=a_p|c><c|+p|s><s|+sigma_p`,

where `[rho_p,H]=0`, spectators are stationary/inert, `a_p>p`, `a_p->q>0`, and `p` is an incoherent/phase-randomized sideband population seed,

`R_lin^2=a_p p/[kappa^2(a_p-p)^2]`.

The frozen flagship theorem specializes to

`(R_lin^2/4)Tr F<=p`.

At zero seed,

`Delta P_s(0)=4kappa^2 q`,

so

**`lim_(p->0+)4p/R_lin^2=4kappa^2 q=Delta P_s(0)`.**

The boundary is attainable with `Tr F=Delta P_s(0)`.

Do not loosen assumptions or extend this theorem without a concrete blocking defect.

## Novelty boundary

Finite FI from quadratically vanishing boundary probabilities/eigenvalues is prior art. Paper 4's candidate distinct content is the controlled finite-seed/finite-radius continuation plus the independent measurement/falsification architecture. Priority remains **unverified, not certified**.

## Provenance

- Type-II memory theorem / matched-recovery timestamp benchmark: frozen random-time companion.
- Prescribed-curvature unitary-coupling theorem: frozen PRA companion.
- NEP/FI, Poisson/jitter, colored-noise detector example, phase modulation, and beam-splitter mechanics: standard/illustrative.

Never duplicate companion proofs or inherit their novelty claims.

## Falsification hierarchy

1. Level I — detector/state/implementation model failure.
2. Level II — resource-law challenge only after independent verification of theorem assumptions and resource quantities.
3. Level III — failure of an ideal saturating benchmark/equality.

## Deterministic Paper-4 manuscript chain

`draft -> R1 mechanical -> R2 theorem -> R3 hostile-review -> R4 presentation -> R5 figures`

R5 is frozen.

## Immediate work order

Do not start new theorem or figure sidequests.

1. hostile-read R5 for redundant/tutorial prose;
2. if compression materially improves the paper, implement it as an isolated text-only R6 with an explicit allowed-edit map;
3. preserve all frozen figure blocks and theorem/equation/proof content unless a genuine defect is found;
4. compile, render, and adversarially audit any R6;
5. then fresh-check current APS/PRA policy and perform submission packaging.

## Documentation rule

Every material change must update its WP note, practical handoff, root `README.md`, this file, `ROADMAP.md`, and `docs/CURRENT_RESEARCH_STATE.md`.
