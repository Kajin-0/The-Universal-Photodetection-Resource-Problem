# WP10 — R2/R3 build closure and second hostile manuscript audit

**Date:** 2026-08-23

**Status:** ACTIVE. The R2 theorem layer is scientifically isolated and hardened. The publication-facing candidate has advanced to R3, which contains only audited post-R2 reviewer repairs. Final CI/artifact/render closure is pending.

## Purpose

Close the first publication-facing build of the practical fourth paper after WP09/WP07A, then perform a second hostile scientific audit before figure production or broad prose compression.

## Scientific core

The candidate Paper-4 theorem is the selected carrier/sideband seed-regularization result with stationary inert spectators,

`rho_p = a_p |c><c| + p |s><s| + sigma_p`,

with `[rho_p,H]=0`, selected gap `E_s-E_c=hbar Omega`, `a_p>p`, `a_p->q>0`, and a calibrated local converter acting only on that pair. The exact affine radius is

`R_lin^2 = a_p p/[kappa^2(a_p-p)^2]`,

and

**`lim_(p->0+) 4p/R_lin^2 = 4 kappa^2 q = Delta P_s(0)`.**

The seed is explicitly an incoherent/phase-randomized population seed. A fixed coherent sideband amplitude is outside the exact theorem because it changes the baseline off-diagonal structure/support geometry.

The manuscript does **not** claim novelty for finite Fisher information from quadratically vanishing boundary populations; Gefen--Rotem--Retzker (2019) and Safranek (2017) are cited for that known boundary mechanism. Candidate novelty is the finite-seed finite-radius continuation into the boundary curvature plus its detector-facing falsification protocol.

## Deterministic source architecture

1. `operational_temporal_information_draft.tex` — frozen first full draft baseline.
2. `apply_r1_compile_fix.py` — mechanical APS compatibility only.
3. `operational_temporal_information_r1.tex` — generated mechanical baseline.
4. `apply_r2_support_strengthening.py` — replaces only the support-crossover section body.
5. `sections/support_crossover_r2.tex` — audited scientific theorem section.
6. `operational_temporal_information_r2.tex` — generated theorem revision.
7. `check_practical_r2.py` — byte-isolates R2 to the support section and checks theorem hypotheses/claim boundaries.
8. `apply_r3_hostile_review_repairs.py` — post-R2 reviewer repair only.
9. `operational_temporal_information_r3.tex` — current publication-facing candidate.
10. `check_practical_r3.py` — reconstructs the expected R3 byte-for-byte from R2 and rejects any other textual drift.

## R1 mechanical failures and repairs

The original REVTeX falsification table used paragraph-width `p{...}` columns and failed with `Extra \\or`; removing `ruledtabular` did not help. A `description` replacement also failed under REVTeX grid machinery. R1 therefore uses conservative `\\noindent\\textbf{...}` paragraph blocks.

A later transform bug computed `table*` byte offsets and then changed preceding text, leaving a fragment of the float. Commit `d12306bd933122927530c9374eb6ff495038d608` fixed the ordering and added a regression guard forbidding residual `table*`, `tabular`, or `ruledtabular` markup.

## Scientific source defect caught during build work

The first WP09 TeX section wrote `a_pp` where the derivation requires the product `a_p p`. This was a source typo, not a derivation change. The correct radius is

`R_lin^2 = a_p p/[kappa^2(a_p-p)^2]`.

The R2 gate rejects recurrence.

## Direct coefficient audit against frozen PRXQ flagship

The frozen flagship Theorem 1 states

`(R_lin^2/4) [Tr F_N^tan/N] <= min{D_nu,U_nu}`.

For the selected carrier-to-upper-sideband mode the upper-endpoint baseline population is `U_nu=p`, so for one copy

**`(R_lin^2/4) Tr F <= p`**

is coefficient-correct. No factor-of-two/four repair is required.

## Second hostile-audit findings and disposition

### A — stationary baseline / definite spectral mode: REPAIRED IN R2

R2 now explicitly states `[rho_p,H]=0`, `E_s-E_c=hbar Omega`, stationary spectators, and a definite `+Omega` tangent mode. Degeneracy-preserving spectator coherence is allowed; generic inter-energy spectator coherence is outside the exact model.

### B — noncircular `R_lin` reconstruction: REPAIRED IN R2

R2 now requires baseline plus first-derivative/tangent tomography to determine the largest affine-positive disk independently of the zero-seed curvature. The three independent data products are:

1. baseline/tangent tomography -> `R_lin`;
2. zero-seed second-order population fit -> `Delta P_s(0)`;
3. separate phase-sensitive likelihood -> Fisher matrix.

Failure of the radius--curvature identity first tests the selected model; FI excess under independently verified theorem hypotheses is the Level-II resource-law test.

### C — active-block POVM attainability: PASS

The four equatorial active-subspace effects sum to the selected two-mode identity; adding the spectator projector produces a normalized POVM. Baseline probabilities are `q/4` for each active outcome plus `1-q` for the spectator outcome. Direct differentiation gives

`F_xx=F_yy=2 q kappa^2`, `F_xy=0`,

hence

**`Tr F=4 q kappa^2=Delta P_s(0)`.**

### D — coherent versus incoherent seed: REPAIRED IN R2

The model now explicitly requires an incoherent/phase-randomized population seed and says a fixed coherent seed is outside the exact theorem.

### E — resonant fixed-energy benchmark assumption: REPAIRED IN R3

WP05 always used two modes of the same angular frequency `nu` with

`H_0=hbar nu(N_C+N_S)`.

The draft called the model resonant but did not write this equality before saying the `N_tot=2` manifold is a fixed bare-energy shell. R3 now states the equal-frequency Hamiltonian explicitly, states that the exchange operators commute with `H_0`, and adds the caveat that unequal bare frequencies require an explicit pump/controller for global energy conservation.

### F — stale references after isolated R2 replacement: REPAIRED IN R3

R2 intentionally changed only the support section and therefore left three old equation references in frozen downstream prose. An attempted double-label alias failed because `amsmath` does not permit multiple labels on one equation. R2 was restored to one label per equation. R3 migrates exactly the three stale references to:

- `eq:survival_bound_general`;
- `eq:boundary_bound_general`;
- `eq:main_crossover_general`.

## CI history relevant to WP10

Disposable PR #35 exists only to expose pull-request CI and must not be merged.

- Runs through `32680286663`: scientific/provenance gates passed; failures were REVTeX mechanics.
- Run `32683887550`, job `97305284455`: R2 **compiled successfully** to a 7-page, 262497-byte PDF. Warning gate failed only because of the three stale downstream references.
- Run `32684118791`, job `97305916355`: R2 scientific gates passed; compile failed solely because the temporary multiple-label alias workaround was invalid under `amsmath`. That workaround has been removed.
- Current verification target: **R3**, triggered from disposable PR #35 after commits `e2d14e8...`, `611feda...`, `519aafb...`, `442b034...`, and workflow commit `2dacbe1...`.

## Remaining hostile-audit questions

1. Does final R3 compile with no unresolved refs/citations or overfull boxes?
2. Does rendered R3 present the stationary/incoherent-seed/tomography qualifications legibly without burying the main result?
3. Does the equal-frequency Hamiltonian paragraph remove any possible implication that an unequal-frequency reduced beam splitter conserves bare energy by itself?
4. Are Type-II memory and unitary-coupling results visibly attributed to companion papers, with no novelty leakage?
5. Is the conventional equal-DC-NEP/equal-bandwidth counterexample presented as an illustrative specification-incompleteness example rather than a new theorem?
6. Does the paper remain publishably useful if referees regard the crossover theorem as narrow? The fallback value must be the integrated operational/falsification architecture, not recycled companion results.

## Immediate work order

1. obtain a green R3 CI build;
2. download the exact artifact and record run/job/artifact IDs, bytes, page count, and SHA-256;
3. render and visually inspect every page;
4. perform final hostile read of the rendered R3;
5. repair only genuine blocking defects;
6. close PR #35 unmerged after final verification;
7. synchronize `practical_temporal_information/README.md`, `practical_temporal_information/AGENTS.md`, root `README.md`, root `AGENTS.md`, `ROADMAP.md`, and `docs/CURRENT_RESEARCH_STATE.md`;
8. only then begin the four publication figures and compression/submission packaging.
