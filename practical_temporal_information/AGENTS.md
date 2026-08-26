# AGENTS — Practical Temporal-Information Benchmarks

**Active branch:** `agent/practical-temporal-information-benchmarks`

The repository, not chat history, is authoritative.

## Read first

1. `README.md`
2. `notes/WP13_R5_FIGURE_INTEGRATION_FREEZE.md`
3. `notes/WP12_PUBLICATION_FIGURE_PACKAGE.md`
4. `notes/WP11_R3_RENDER_AUDIT_AND_R4_PRESENTATION_FREEZE.md`
5. `notes/WP10_R2_BUILD_AND_SECOND_HOSTILE_AUDIT.md`
6. `notes/WP09_HOSTILE_MANUSCRIPT_AUDIT_AND_SPECTATOR_INDEPENDENT_CROSSOVER.md`
7. `manuscript/practical_temporal_information/README.md`
8. root `docs/CURRENT_RESEARCH_STATE.md`

## Current status — R5 frozen

Working title:

> **Operational temporal-information benchmarks for photodetection**

Current canonical manuscript baseline: **R5**.

Final verification:

- run `32915363157` PASS;
- job `98017843874` PASS;
- source commit `55ec3af3bd9d57830c03f65655180936eb85eda9`;
- artifact `9588018384`;
- archive digest `sha256:06e1de8d8f5e44f9d62e6ebd06362d2cfbc93132014718398e57b877c784c281`;
- exact PDF: 10 pages, 429432 bytes;
- PDF SHA-256 `fd451a59ca5b70731b61f7ce237bd06a1d5f7105305e064cfe21bbb588e6bf48`.

All ten pages were rendered at 200 dpi and inspected. R5 is byte-isolated from R4: removing the four exact figure/caption blocks restores R4 exactly.

WP12 figure package is separately frozen at run `32914889053`, artifact `9587797682`; every R5 build re-generates and hash-checks the four canonical vector PDFs before integration.

## Frozen Paper-4 theorem

For stationary selected modes with `E_s-E_c=hbar Omega`,

`rho_p=a_p|c><c|+p|s><s|+sigma_p`,

where `[rho_p,H]=0`, spectators are stationary/inert, `a_p>p`, `a_p->q>0`, and `p` is an incoherent/phase-randomized sideband population seed,

`R_lin^2=a_p p/[kappa^2(a_p-p)^2]`.

The frozen flagship theorem specializes exactly to

`(R_lin^2/4)Tr F<=p`.

At zero seed,

`Delta P_s(0)=4kappa^2 q`,

hence

**`lim_(p->0+)4p/R_lin^2=4kappa^2 q=Delta P_s(0)`.**

The completed boundary POVM attains `Tr F=Delta P_s(0)`.

Do not loosen the explicit hypotheses or expand this theorem without a genuine blocking defect.

## Novelty boundary

Finite FI from quadratically vanishing boundary probabilities/eigenvalues is prior art (Gefen--Rotem--Retzker 2019; Safranek 2017). Candidate distinct content is the finite-seed/finite-radius continuation and the independent measurement/falsification architecture. Priority remains **unverified, not certified**.

## Provenance discipline

- Type-II memory theorem and matched-recovery values: frozen random-time companion.
- Exact prescribed-curvature coupling theorem: frozen PRA companion.
- NEP/FI, Poisson/jitter, colored-noise example, phase modulation, and beam-splitter mechanics: standard/illustrative.

Do not duplicate companion proofs or transfer their novelty claims into Paper 4.

## Falsification hierarchy

1. **Level I:** detector/state/implementation model failure.
2. **Level II:** resource-law challenge only after independently verifying theorem assumptions and resource quantities.
3. **Level III:** failure of an ideal saturating benchmark/equality.

## Deterministic manuscript chain

`draft -> R1 mechanical -> R2 theorem -> R3 hostile-review -> R4 presentation -> R5 figures`

Every layer has an explicit isolation gate. R5 is frozen.

## Immediate work order

Do **not** start new theorem or figure sidequests.

Next:

1. hostile-read R5 for redundancy/tutorial excess;
2. if compression is worthwhile, create an isolated text-only R6 with an allowed-edit map;
3. preserve all four figure blocks exactly;
4. preserve theorem/proposition/equation/proof content unless a genuine defect is found;
5. compile/render/adversarially audit any R6;
6. then perform fresh APS/PRA policy checks and submission packaging.

## Documentation rule

Every material result or scope change must update the corresponding WP note, this handoff, root `README.md`, root `AGENTS.md`, `ROADMAP.md`, and `docs/CURRENT_RESEARCH_STATE.md`.
