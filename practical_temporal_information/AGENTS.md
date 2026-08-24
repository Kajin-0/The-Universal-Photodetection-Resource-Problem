# AGENTS — Practical Temporal-Information Benchmarks

**Active branch:** `agent/practical-temporal-information-benchmarks`

The repository, not chat history, is authoritative.

## Mission

Create a fourth paper that translates the temporal-information resource program into standard detector physics and explicit falsification tests. Do not modify the frozen theorem/proof layers of the three mature papers unless a genuine defect is exposed.

## Read first

1. `README.md`
2. `notes/WP09_HOSTILE_MANUSCRIPT_AUDIT_AND_SPECTATOR_INDEPENDENT_CROSSOVER.md`
3. `notes/WP07A_CLOSE_PRIOR_ART_BOUNDARY_SUPERRESOLUTION.md`
4. `notes/WP08_FINAL_PREMANUSCRIPT_STACK_AND_SPEC_INCOMPLETENESS.md`
5. `notes/WP07_PRIOR_ART_AND_SIGNIFICANCE_GATE.md`
6. `notes/WP04_OPTICAL_SIDEBAND_SURVIVAL_SYNTHESIS_CROSSOVER.md`
7. `notes/WP03_DEAD_TIME_RECOVERY_INFORMATION_BENCHMARKS.md`
8. `notes/WP05_RESONANT_EXCHANGE_UNITARY_COUPLING_BRIDGE.md`
9. `manuscript/practical_temporal_information/README.md`
10. root `docs/CURRENT_RESEARCH_STATE.md`

## Current status

WP07 prior-art gate: **PASS WITH NARROWED CLAIMS**.

WP08 final pre-manuscript gate: **PASS**.

WP09 hostile manuscript audit: **CONDITIONAL PASS** pending final clean R2 build/render and second hostile read. The main scientific repair has already been implemented: the support crossover is generalized to a selected carrier/sideband pair embedded in arbitrary inert spectators.

WP07A adds a crucial novelty boundary: Gefen--Rotem--Retzker (2019) and the rank-changing QFI literature already establish that an outcome/eigenvalue vanishing quadratically at a boundary can retain finite Fisher information. Paper 4 must not claim that mechanism as new. Its candidate contribution is the **finite-seed continuation from the interior**, including the exact affine physical radius and its radius-normalized convergence to the boundary curvature.

The first full manuscript draft exists and has isolated R1/R2 generation plus static gates. REVTeX rejected both paragraph-width tabular columns and labeled `description` items in the falsification section, so the generated R1 now uses conservative ordinary paragraph blocks. No scientific content was removed.

A hostile source check also found and repaired a manuscript-only notation defect: the radius requires the product `a_p p`, now written explicitly as `a_p\,p`; the R2 gate rejects the erroneous string `a_pp`.

## Strengthened Paper-4 theorem

Let

`rho_p = a_p |c><c| + p |s><s| + sigma_p`,

where `sigma_p>=0` is supported on spectator modes, `a_p>p`, `a_p->q>0` as `p->0+`, and the calibrated local converter acts only on the selected carrier/sideband pair.

Then

`P_s(p;r)=p+(a_p-p) sin^2(kappa r)`,

and the exact affine radius is

`R_lin^2 = a_p p/[kappa^2(a_p-p)^2]`.

The finite-radius survival law gives

`(R_lin^2/4)Tr F <= p`.

At zero seed,

`Delta P_s(0)=4 kappa^2 q`.

Therefore

**`lim_(p->0+) 4p/R_lin^2 = 4 kappa^2 q = Delta P_s(0)`.**

This is independent of the detailed spectator population and of how normalization compensation is distributed among spectator modes, provided the selected carrier occupation tends to `q` and the local converter leaves spectators inert.

The original `a_p=1-p`, `sigma_p=0`, `q=1` model remains the simplest plotted special case.

## Novelty boundary

Do **not** claim novelty for:

- finite FI from a quadratically vanishing probability/eigenvalue;
- projection-noise suppression at a null outcome;
- generic rank-changing/boundary QFI behavior;
- sideband Fisher metrology or seeded/vacuum interferometry.

The candidate distinct result is the exact finite-seed spectral-survival regularization

`4p/R_lin^2 -> Delta P_s(0)`

and its selected-mode spectator-independent realization.

Priority remains unverified/not certified.

## Claim hierarchy

### Candidate original Paper-4 science

- selected-mode support-seed crossover above;
- ideal weak phase-modulation boundary saturator under the locked convention;
- integrated falsification architecture.

### Cited upstream benchmarks

- Type-II memory/information theorem from the frozen random-time paper;
- prescribed-curvature implementation theorem from the frozen PRA paper.

Do not duplicate their proofs or novelty claims.

### Standard bridges

- linear Gaussian `Tr F/T=2/NEP(f)^2`;
- ideal Poisson timestamps and independent-jitter attenuation;
- WP08 equal-DC-NEP/equal-response-bandwidth but unequal-FI-spectrum example;
- standard resonant beam-splitter implementation benchmark.

## Falsification hierarchy

Always distinguish:

1. **Level I — detector-model/reduction failure**;
2. **Level II — resource-law challenge only after independent verification of theorem hypotheses**;
3. **Level III — failure of an ideal saturating model/equality**.

## Immediate work order

1. complete the latest prior-art-hardened R2 CI run;
2. download and render the exact successful artifact if green;
3. hostile-audit the rendered R2 and theorem/provenance language;
4. close disposable PR #35 unmerged after final verification;
5. only then begin figure production and publication-style compression.

Do not create new detector-model sidequests.

## Documentation rule

After every material result or scope change, update the corresponding note and this handoff. When the frontier changes, also update root `README.md`, `AGENTS.md`, `ROADMAP.md`, and `docs/CURRENT_RESEARCH_STATE.md`.
