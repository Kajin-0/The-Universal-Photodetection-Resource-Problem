# AGENTS — Practical Temporal-Information Benchmarks

**Active branch:** `agent/practical-temporal-information-benchmarks`

The repository, not chat history, is authoritative.

## Mission

Create a fourth paper that translates the temporal-information resource program into standard detector physics and explicit falsification tests. Do not modify the frozen theorem/proof layers of the three mature papers unless a genuine defect is exposed.

## Read first

1. `README.md`
2. `notes/WP09_HOSTILE_MANUSCRIPT_AUDIT_AND_SPECTATOR_INDEPENDENT_CROSSOVER.md`
3. `notes/WP08_FINAL_PREMANUSCRIPT_STACK_AND_SPEC_INCOMPLETENESS.md`
4. `notes/WP07_PRIOR_ART_AND_SIGNIFICANCE_GATE.md`
5. `notes/WP04_OPTICAL_SIDEBAND_SURVIVAL_SYNTHESIS_CROSSOVER.md`
6. `notes/WP03_DEAD_TIME_RECOVERY_INFORMATION_BENCHMARKS.md`
7. `notes/WP05_RESONANT_EXCHANGE_UNITARY_COUPLING_BRIDGE.md`
8. `manuscript/practical_temporal_information/README.md`
9. root `docs/CURRENT_RESEARCH_STATE.md`

## Current status

WP07 prior-art gate: **PASS WITH NARROWED CLAIMS**.

WP08 final pre-manuscript gate: **PASS**.

WP09 hostile manuscript audit: **CONDITIONAL PASS**. No coefficient or theorem-use defect was found, but the central crossover should be generalized from the normalized two-level baseline to a selected carrier/sideband pair embedded in an arbitrary inert spectator sector before scientific freeze.

The first full manuscript draft exists and has its own static/CI gate. Initial CI passed the static provenance gate and exposed one purely mechanical REVTeX table incompatibility; a deterministic R1 transform removes only the incompatible `ruledtabular` wrapper before compilation.

## Strengthened Paper-4 theorem after WP09

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

## Claim hierarchy

### Candidate original Paper-4 science

- spectator-independent selected-mode support-seed crossover above;
- ideal weak phase-modulation boundary saturator under the locked convention;
- integrated falsification architecture.

Priority remains unverified/not certified; targeted WP07 search found no direct collision.

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

1. finish mechanical R1 build verification;
2. generate a scientific R2 that replaces the narrow crossover subsection with the WP09 spectator-independent theorem while preserving the detector-first architecture;
3. compile/render R2 and run a second hostile manuscript audit;
4. only then begin figure production and publication-style compression.

Do not create new detector-model sidequests.

## Prior-art exclusions

Do not claim novelty for dead-time information theory, variable/random dead time, inter-arrival characterization, paralyzable correlation distortion, sideband Fisher metrology, seeded/vacuum interferometry, generic rank-boundary QFI curvature, beam-splitter metrology, standard NEP, or generic Fisher sensing.

## Documentation rule

After every material result or scope change, update the corresponding note and this handoff. When the frontier changes, also update root `README.md`, `AGENTS.md`, `ROADMAP.md`, and `docs/CURRENT_RESEARCH_STATE.md`.
