# AGENTS — Practical Temporal-Information Benchmarks

**Active branch:** `agent/practical-temporal-information-benchmarks`

The repository, not chat history, is authoritative.

## Mission

Create a fourth paper that translates the three temporal-information theory papers into standard detector physics, independently measurable quantities, and explicit falsification tests. The mature companion theorem/proof layers remain frozen.

## Read first

1. `README.md`
2. `notes/WP11_R3_RENDER_AUDIT_AND_R4_PRESENTATION_FREEZE.md`
3. `notes/WP10_R2_BUILD_AND_SECOND_HOSTILE_AUDIT.md`
4. `notes/WP09_HOSTILE_MANUSCRIPT_AUDIT_AND_SPECTATOR_INDEPENDENT_CROSSOVER.md`
5. `notes/WP07A_CLOSE_PRIOR_ART_BOUNDARY_SUPERRESOLUTION.md`
6. `notes/WP08_FINAL_PREMANUSCRIPT_STACK_AND_SPEC_INCOMPLETENESS.md`
7. `manuscript/practical_temporal_information/README.md`
8. `manuscript/practical_temporal_information/MANUSCRIPT_ARCHITECTURE.md`
9. root `docs/CURRENT_RESEARCH_STATE.md`

## Current status — R4 frozen

WP07: **PASS WITH NARROWED CLAIMS**.

WP08: **PASS**.

WP09: **PASS AFTER SPECTATOR GENERALIZATION**.

WP10 second hostile scientific/build audit: **PASS AFTER R2/R3 REPAIRS**.

WP11 exact artifact/render audit: **PASS**.

Current publication-facing manuscript freeze: **R4**.

Final R4 verification:

- run `32684526293`;
- job `97307019940`;
- artifact `9505218922`;
- archive digest `sha256:9905a2cbd4366d57731fc8f4a99c6f72a513629a8727257a43131e02efb96cce`;
- PDF 8 pages, 266068 bytes;
- PDF SHA-256 `794cb1c52326dc1965e14ea8ccd15530b41b2e523ca501e88f081cf69d741a01`.

All generation/isolation/compile/warning/artifact gates passed. All eight pages were rendered and inspected. R3→R4 pixel differences occur only at former hyperlink-border locations. Disposable PR #35 was closed **unmerged**. There are currently zero open PRs.

## Frozen Paper-4 theorem

Select stationary free-Hamiltonian modes `|c>`, `|s>` separated by `hbar Omega` and let

`rho_p=a_p|c><c|+p|s><s|+sigma_p`,

with `[rho_p,H]=0`, stationary inert spectators, `a_p>p`, `a_p->q>0`, and an incoherent/phase-randomized sideband population seed `p`.

For a calibrated converter acting only on the selected pair,

`R_lin^2=a_p p/[kappa^2(a_p-p)^2]`,

and the frozen flagship theorem specializes exactly to

`(R_lin^2/4)Tr F<=p`.

At zero seed,

`Delta P_s(0)=4 kappa^2 q`,

so

**`lim_(p->0+)4p/R_lin^2=4 kappa^2 q=Delta P_s(0)`.**

A completed equatorial POVM attains

`Tr F=4 q kappa^2=Delta P_s(0)`.

Do not weaken the explicit hypotheses: stationary baseline, definite selected spectral gap, incoherent seed, inert selected-mode spectators, calibrated local converter.

## Novelty boundary

Do not claim novelty for finite FI from quadratically vanishing probabilities/eigenvalues. Gefen--Rotem--Retzker (2019) and Safranek (2017) cover that general boundary mechanism.

Candidate distinct content is the finite-seed/finite-radius continuation

`4p/R_lin^2 -> Delta P_s(0)`

plus its independent measurement/falsification architecture.

Priority remains **unverified, not certified**.

## Provenance discipline

The Type-II memory theorem belongs to the frozen random-time companion. Paper 4 only operationalizes it.

The exact prescribed-curvature coupling theorem belongs to the frozen PRA companion. Paper 4 only supplies a standard equal-frequency resonant benchmark.

The NEP/FI relation, Poisson/jitter bridge, colored-noise detector example, phase modulation, and beam-splitter physics are standard/illustrative material and must not be sold as fundamental novelty.

## Falsification hierarchy

1. **Level I:** detector/state/model reduction failure.
2. **Level II:** resource-law challenge only after independent verification of theorem hypotheses and resource quantities.
3. **Level III:** failure of an ideal saturating model/equality.

The support test uses independent products:

- baseline + tangent tomography -> `R_lin`;
- zero-seed quadratic population fit -> `Delta P_s(0)`;
- separate phase-sensitive likelihood -> Fisher matrix.

## Deterministic manuscript chain

`draft -> R1 mechanical -> R2 theorem -> R3 hostile-review -> R4 presentation`.

R4 is frozen. Any scientific change now requires a new explicit revision layer and a concrete blocking reason.

## Immediate work order

**WP12 — publication figures.**

Create at most four deterministic scientific figures:

1. same conventional detector specs, different FI spectra;
2. same Type-II saturation, different timestamp information — clearly attributed to companion work;
3. stationary support-seed survival→synthesis crossover — principal figure;
4. equal-frequency resonant exchange + falsification/calibration map.

Each figure must have a script/source, explicit units/normalization, no decorative AI imagery, and an independent numerical/algebraic check. Do not alter manuscript science while designing figures.

After figures: integrate them through an isolated revision, compile/render/hostile-review again, then do publication compression and current APS policy checks.

## Documentation rule

Update the relevant WP note and this handoff after every material result. When the frontier changes, also update root `README.md`, `AGENTS.md`, `ROADMAP.md`, and `docs/CURRENT_RESEARCH_STATE.md`.
