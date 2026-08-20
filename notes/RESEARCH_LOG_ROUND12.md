# Research Log — Round 12

**Date:** 2026-08-20

## Purpose

Durable checkpoint after the autonomous-event theorem stack moved from theorem discovery into manuscript hardening.

The repository, not chat history, is authoritative. Detailed HgCdTe/Kane WP17–24 remains frozen.

---

# 1. Publication target remains the autonomous marked-event branch

The strongest theorem class is an autonomous/time-translation-invariant, independent-event, one-primary-registration photodetector driven by weak coherent/direct-detection intensity modulation.

Per incident photon, use the marked subprobability kernel

\[
K(dm,d\tau)=\kappa(dm)\mu_m(d\tau),
\]

with primary-event probability

\[
\eta=\kappa(\mathsf M)\le1.
\]

The complete accessible primary-event mark must be retained. The per-photon kernel is assumed independent of the small source modulation parameter; the source parameter modulates arrival intensity only.

Exact source-normalized FI transfer:

\[
\boxed{
G(\omega)=\int_{\mathsf M}|H_m(\omega)|^2\kappa(dm).
}
\]

Background addition and downstream processing cannot increase FI.

Primary theorem note: `notes/WP32_GENERAL_MARKED_POISSON_EVENT_KERNEL_THEOREM.md`.

---

# 2. Timing-resource hierarchy survived hostile audit

## Atomic level

Wiener:

\[
\boxed{
\lim_{\Omega\to\infty}
\frac1{2\Omega}\int_{-\Omega}^{\Omega}G(\omega)d\omega
=
\int\kappa(dm)\sum_jp_j(m)^2.
}
\]

Purely non-atomic conditional timing gives zero asymptotic flat-band average transfer. This does not imply pointwise decay for every singular continuous law.

## Collision resource

For square-integrable conditional delay densities,

\[
\boxed{
\mathfrak R_2
=2\int\kappa(dm)\int f_m(t)^2dt,
}
\]

and Parseval gives

\[
\boxed{
\int G(\omega)d\omega=\pi\mathfrak R_2.
}
\]

Hence

\[
\boxed{
\bar\eta_I(\Omega)
\le\min\left[\eta,\frac{\pi\mathfrak R_2}{2\Omega}\right].
}
\]

## Microscopic hazard capacity

If

\[
h_m(t)\le\Lambda(m),
\]

define

\[
\boxed{
\mathfrak H=\int\Lambda(m)\kappa(dm).
}
\]

Then

\[
\boxed{\mathfrak R_2\le\mathfrak H.}
\]

A cleaner proof identified during manuscript audit is

\[
\int f^2=\int h^2S^2
\le\Lambda\int hS^2
=\Lambda/2,
\]

because

\[
d(S^2)/dt=-2hS^2.
\]

A global worst-case hazard is only a stronger corollary. Rare arbitrarily fast branches can be harmless if their capture weight vanishes sufficiently rapidly.

---

# 3. WP33 — exact fixed-mean/fixed-variance jitter no-go

The earlier WP26 family was strengthened so every selected family member can have the exact same prescribed mean and variance.

Take

\[
f_{\epsilon,n,\lambda}
=(1-\epsilon)ne^{-nt}+\epsilon\lambda e^{-\lambda t}.
\]

Writing `x=1/lambda`, solve exactly

\[
\operatorname{Var}X=\sigma^2
\]

with

\[
\boxed{
 x_{\epsilon,n}
=\frac{
\sqrt{(2-\epsilon)n^2\sigma^2-2(1-\epsilon)}
+\sqrt\epsilon(1-\epsilon)
}
{
\sqrt\epsilon\,n(2-\epsilon)
}.
}
\]

Then shift deterministically to impose any target mean `mu0`; the shift changes only the Fourier phase and leaves `|H|` unchanged.

Along `n->infinity`, then `epsilon->0`,

\[
|H(\omega)|^2\to1
\]

uniformly on every prescribed finite frequency band while

\[
\boxed{
\mathbb ED=\mu_0,
\qquad
\operatorname{Var}D=\sigma^2
}
\]

for every family member.

Thus

\[
\boxed{
\{\text{exact mean},\text{ exact RMS jitter}\}
\not\Rightarrow
\text{finite information bandwidth}.
}
\]

Do not claim that an arbitrary exact FWHM is held fixed by this construction. FWHM remains non-resource-complete without shape assumptions, but WP33 specifically proves the mean/variance statement.

Primary note: `notes/WP33_EXACT_FIXED_MEAN_VARIANCE_JITTER_NO_GO.md`.

---

# 4. Hostile proof audit conclusions

Primary audit: `docs/MANUSCRIPT_HOSTILE_PROOF_AUDIT_ROUND2.md`.

No fatal mathematical defect was found in WP32/WP33 or the restricted thermodynamic bridge under their stated assumptions.

Mandatory scope statements:

1. Poisson/direct-detection weak intensity modulation.
2. Per-photon kernel independent of the source parameter.
3. Autonomous/time-translation-invariant detector processing.
4. Low-overlap independent events.
5. At most one sufficient primary event per incident photon in the theorem class.
6. Complete accessible primary-event mark retained.
7. Weighted spectral theorem is not arbitrary correlated multiparameter estimation.
8. Thermodynamic mark bridge requires finite-state time-homogeneous Markov memorylessness; semi-Markov/age-memory detectors are not silently included.

---

# 5. Thermodynamic result remains correctly scoped

WP29 gives, for the reversible WP3 gateway,

\[
\lambda_1
\le
\Lambda_*
=
\frac{\mathcal A d}{f_*}
 g^{-1}(\Sigma/f_*).
\]

Mark-robust autonomous downstream timing obeys

\[
h_D(t|M)\le\lambda_1.
\]

Therefore

\[
\boxed{
\bar\eta_I(\Omega)
\le
C\min\left[
1,
\frac{\pi\mathcal A d}{2f_*\Omega}
 g^{-1}(\Sigma/f_*)
\right].
}
\]

The rare-fast appendix proves aggregate stationary EPR/activity/throughput plus a fixed optical detailed-balance ratio do not bound the local speed scale if hidden microscopic nonoptical scales are allowed to diverge.

Important limitation: the rare-fast family does **not** keep every nonoptical bare edge affinity fixed. The correct conclusion is that the stated aggregate stationary thermodynamic resources are incomplete, not that every imaginable edge-resolved thermodynamic resource is insufficient.

---

# 6. Manuscript state

Current manuscript target:

`manuscript/event_resource_theorem_rev3.tex`

Rev3 incorporates:

- exact marked-event theorem;
- standard Poisson/Wiener citations at theorem locations;
- atomic timing theorem;
- collision and weighted-hazard bounds;
- clean hazard proof;
- exact WP33 mean/variance no-go;
- synchronous clock no-go;
- explicit finite-state Markov memorylessness in the thermodynamic bridge;
- explicit rare-fast appendix inclusion;
- conservative novelty wording relative to TCSPC/IRF and finite-frequency response literature.

Bibliography:

`manuscript/references.bib`

Rare-fast appendix:

`manuscript/appendix_rare_fast_counterexample.tex`

A branch CI workflow now targets Rev3:

`.github/workflows/manuscript-check.yml`

Connector access currently does not expose the push-triggered Actions run, so compile success has not yet been independently read back through the connector. Do not claim a verified successful compile until a run/result is actually inspected.

---

# 7. Literature positioning

Verified closest prior work includes:

- Köllner & Wolfrum 1992: photon requirements/lifetime estimation;
- Talaga 2009: information-theoretical TCSPC with IRF convolution, information loss, effective bandwidth, sensitivity-bandwidth discussion;
- Bouchet et al. 2019: Fisher-information lifetime precision with finite IRF/background;
- Trinh & Esposito 2021: FI analysis of IRF/photon-statistics biochemical resolution;
- Dechant 2026: general finite-frequency fluctuation-response inequality.

Therefore do **not** claim:

- first information-theoretic detector timing analysis;
- first detector sensitivity-bandwidth tradeoff;
- first use of IRF spectra as bandwidth;
- generic finite-frequency response/noise bounds.

Current defensible candidate contribution:

> A resource-completeness theorem for source-modulation information transfer in autonomous marked photodetection event channels, including exact atomic and collision-intensity timing resources plus explicit no-go/repair results for conventional jitter moments, free synchronous control, and aggregate stationary thermodynamics.

Novelty remains provisional but no equivalent complete theorem stack has been identified in targeted searches.

---

# 8. Immediate next actions

1. Obtain an actual LaTeX compile result for Rev3 and repair any build errors.
2. Add only figures that clarify theorem content; do not add decorative plots.
3. Perform a final line-by-line claim/citation audit of Rev3.
4. Decide whether the autonomous event theorem is ready for a first manuscript submission path.
5. Defer non-Poisson/nonclassical source extension unless a referee-style review demonstrates it is necessary.
6. Keep HgCdTe WP17–24 frozen.

**Status:** autonomous proper-event theorem mathematics substantially closed; manuscript hardening in progress.
