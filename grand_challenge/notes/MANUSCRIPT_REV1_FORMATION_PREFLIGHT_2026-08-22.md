# Grand Challenge Manuscript Rev1 Formation / Preflight

**Date:** 2026-08-22

**Scientific checkpoint:** WP24 integrated hostile review PASS

**Manuscript status:** Rev1 science skeleton created; deterministic Rev2 mechanical-build generator created; dedicated CI added. Actual push-triggered CI run has not yet been directly inspected through the available connector, so the manuscript is **not yet build-verified**.

---

## Files created

- `grand_challenge/MANUSCRIPT_ARCHITECTURE.md`
- `grand_challenge/manuscript/energy_survival_temporal_fisher_rev1.tex`
- `grand_challenge/manuscript/references.bib`
- `grand_challenge/manuscript/apply_rev2_mechanical.py`
- `.github/workflows/grand-challenge-manuscript-check.yml`
- `grand_challenge/numerics/verify_operational_tail_bound.py`

---

## Working title

> **A Sharp Energy-Survival Law for Temporal Fisher Information**

The title deliberately avoids `universal` because WP14 excludes arbitrary state-valued waveform synthesis under baseline-energy-only accounting.

---

## Manuscript center of gravity

The paper is no longer architected around the WP15 `pi E/hbar` SLD-QFI envelope.

The main theorem is the jointly operational finite-copy result

`Tr F_N^(k)/N <= min(D_k,U_k) <= T_k`,

with

`T_k=sum_(m>=k)q_m`.

The continuum headline is

`R(nu)<=P(Omega>=nu)`,

with

`int_R R(nu)dnu<=2Ebar^+/hbar`

and

`Ebar^+>=hbar nu R(nu)=h f R(2pi f)`.

The geometric/exponential canonical phase/time family is the exact equality construction.

The independent compound-Poisson-to-bosonic-field theorem is the photodetection embedding.

WP10/WP12/WP15 are retained as a secondary separately optimized SLD-QFI envelope. WP14 is retained as the explicit source-class boundary.

---

## Rev1 science content already written

Rev1 contains substantive prose and equations rather than section placeholders:

1. introduction and conservative prior-art positioning;
2. periodic random-time statistical experiment and input-FI normalization;
3. purified energy-sector representation;
4. paired partial-shift tangent factorization;
5. finite-copy arbitrary-joint-POVM theorem;
6. full direct Hilbert--Schmidt Cauchy--Schwarz proof;
7. all-mode mean-excitation corollary;
8. general-measure continuum theorem;
9. two-sided area and pointwise Planck-scale corollaries;
10. geometric/canonical-phase exact equality family;
11. exponential-spectrum/Cauchy-time continuum equality;
12. compound-Poisson event register;
13. CPTP source-to-field / final-POVM pullback;
14. secondary SLD-QFI envelope;
15. arbitrary coherent-waveform no-go boundary;
16. discussion and conclusion.

---

## Prior-art positioning already embedded

Rev1 explicitly credits rather than claims:

- Marvian--Spekkens weighted `U(1)` twirling / modes of asymmetry;
- Bužek--Derka--Massar optimal quantum clocks;
- Imai--Hayashi Fourier phase estimation;
- Hayashi photon-number-constrained phase estimation;
- Braunstein--Caves generic quantum Fisher information;
- Gill arbitrary collective-measurement information bounds;
- Fujiwara--Imai random-unitary channel probability estimation;
- Tsang--Wiseman--Caves waveform QFI;
- Pocovnicu positive-frequency sharp analysis relevant to the earlier timestamp/QFI line.

A final targeted literature search during manuscript formation again found close phase-noise, phase-diffusion, phase-distribution, and synchronization-Fisher work but did not locate the exact population-tail Fisher theorem. Priority remains unverified.

---

## Numerical validation

An independent numerical test was performed before committing the reusable script.

Random finite-dimensional rank-one frame POVMs were sampled for:

- one-copy experiments;
- global two-copy measurements;
- dimensions through at least four for one copy and three for two copies;
- random population distributions;
- cases with missing intermediate energy sectors.

Every sampled Fisher trace obeyed

`Tr F_N^(k) <= N min(D_k,U_k)`.

In the exploratory run, the largest random-search ratios to the tight bound were approximately:

- one copy: `0.934`;
- two-copy global POVMs: `0.849`.

These numbers have no theorem status; random POVMs are not expected to find the optimal measurement systematically. The committed script uses a fixed seed, performs a broader deterministic sweep, and separately verifies the geometric/canonical-phase equality formula.

---

## Mechanical preflight issue found and repaired

A local REVTeX 4.2 micro-test established that:

- `theorem` is not predefined;
- `proof` opening is not predefined;
- REVTeX already defines `endproof`.

Therefore Rev1 as initially written would not be a self-contained build source.

The deterministic Rev2 generator now:

1. declares `theorem` and `corollary` with `newtheorem`;
2. supplies only the missing opening `proof` command;
3. does **not** load `amsthm`, consistent with APS REVTeX production guidance;
4. unwraps every balanced `boxed{...}` presentation command while preserving the enclosed mathematics, because APS production guidance excludes `boxed` markup.

This is a mechanical repair only; the generator is assertion-based and does not alter theorem statements, equations, citations, or prose apart from removing the visual box wrapper.

---

## CI

Dedicated workflow:

`.github/workflows/grand-challenge-manuscript-check.yml`

It:

1. checks out the active branch;
2. runs `apply_rev2_mechanical.py`;
3. compiles `energy_survival_temporal_fisher_rev2.tex` with `xu-cheng/latex-action@v3`;
4. fails on unresolved citations/references;
5. fails on overfull boxes;
6. uploads Rev2 PDF/source, Rev1 source, generator, and bibliography.

The available GitHub connector exposes pull-request-triggered workflow lookup but not the relevant push-run listing for this branch. No actual run/log has therefore been inspected yet. Do not call Rev2 build-verified until that run or an equivalent full local compile is inspected.

---

## Source-level hostile checks completed

The following were rechecked during manuscript formation:

- input cosine/sine FI normalization: each quadrature `1/2`, trace `1` per event;
- complex tangent convention gives `|z_y|^2/p_y` for the Fisher-trace contribution;
- N-copy tangent factorization is exact;
- cross-copy terms vanish because `Tr(rho0 V_k)=0`;
- support gaps require a partial isometry, already repaired in WP20;
- applying the proof to `A_k` and `A_k^dagger` yields `min(D_k,U_k)`;
- geometric canonical-phase equality gives `R(k)=r^k`;
- lower-bin exponential discretization is exactly geometric for every spacing;
- compound-Poisson normalization gives input Fisher trace equal to mean event count `mu`;
- final detector POVMs pull back through the parameter-independent CPTP source/detector channel;
- the continuum formulation does not invoke a nonexistent normalized uniform distribution on the real line.

No new scientific defect was found in these checks.

---

## Remaining preflight gates before calling a frozen Rev2 science draft

1. Inspect the actual full LaTeX/BibTeX CI log and artifact.
2. Repair any concrete LaTeX or layout defect only.
3. Perform a manuscript-level hostile read of the assembled prose, especially:
   - exact theorem hypotheses;
   - continuum-limit wording;
   - independent-event source scope;
   - prior-art claim boundaries;
   - possible ambiguity between excitation-sector index, event count, and photon number.
4. Decide whether Fig. 1 and Fig. 2 materially improve the paper before adding them.
5. Only after the hostile read decide whether the manuscript is ready for journal-target formatting.

No additional theorem accumulation is recommended by default.