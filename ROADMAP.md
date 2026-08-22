# Research Roadmap

**Updated:** 2026-08-22

`main` is the repository landing/index branch.

**Active scientific branch:** `agent/temporal-information-resource-law`

Paper 1 Rev11 and Paper 2 Rev7 are frozen. Grand Challenge science checkpoint: **WP24**. Preferred Grand Challenge manuscript: **Rev4**, frozen unless a concrete defect appears.

## Current operational theorem

For exact periodic random-time encoding with sector probabilities `q_n`, define

`T_k=sum_(m>=k)q_m`.

Any finite-copy joint measurement obeys

`Tr F_N^(k)<=N min(D_k,U_k)<=N T_k`,

hence

`sum_(k>=1)R_N(k)<=nbar`.

`R_N(k)` is the two-quadrature / phase-averaged source-normalized Fisher retention.

Controlled large-period limits obey

`R(nu)<=P(Omega>=nu)`,

`int_R R(nu)dnu<=2Ebar^+/hbar`,

`Ebar^+>=hbar nu R(nu)=h f R(2pi f)`.

The coefficient is exactly attainable by the geometric/exponential canonical phase-time family.

## Physical embedding

WP23 extends the theorem to independent quantum-marked compound-Poisson sources followed by arbitrary parameter-independent formation of a common bosonic field and arbitrary detector processing.

## Secondary QFI envelope

WP10/WP12/WP15 remain valid modewise SLD-QFI metric bounds with two-sided area `pi E/hbar`; they are secondary to the jointly operational `2E/hbar` law.

## Boundaries

- WP14: arbitrary coherent waveform state engineering is not bounded by baseline mean energy alone.
- WP16: the `pi/4` analytic operator norm is established Hardy--Hilbert mathematics.
- WP21/WP24: weighted `U(1)` twirling/modes of asymmetry, canonical phase, energy-constrained phase estimation, general collective information bounds, random-unitary estimation, and waveform QFI are prior art.
- Continuum statements remain controlled large-period limits of exact periodic models.

The candidate contribution is the operational classical-Fisher tail/survival theorem and its source-to-record consequences. **Priority remains unverified, not certified.**

## Manuscript gate — PASSED

Working title: **A Sharp Energy-Survival Law for Temporal Fisher Information**.

Rev4 on the active branch has passed:

- full local LaTeX/BibTeX build;
- seven-page visual inspection;
- unresolved-reference/citation and overfull-box gates;
- deterministic one-/two-copy random-POVM sanity checks;
- DOI/title/provenance bibliography audit.

A real Pocovnicu title mismatch was corrected while retaining the scientifically correct DOI/source. Gill was upgraded to the published 2008 chapter metadata.

The current connector does not expose the branch-push GitHub Actions run; direct remote-job inspection is not claimed. Equivalent full local build verification is complete.

## Immediate work order — publication engineering

1. **Freeze Rev4 science.** Reopen only for a concrete theorem, priority, build, or referee defect.
2. Inspect remote Rev4 CI if it becomes accessible.
3. Add at most one conceptual figure, and only if it materially improves comprehension.
4. Keep novelty claims conservative while historical priority remains uncertified.
5. Prepare submission metadata/compliance only from factual user-supplied information.

## Documentation policy

Detailed derivations and manuscript generation live on `agent/temporal-information-resource-law`; `main` must always show the active branch and latest checkpoint.
