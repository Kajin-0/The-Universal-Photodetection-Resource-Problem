# Research Log Round 12 — Addendum: WP34 Resource-Cost Theorem

**Date:** 2026-08-20

## Numbering correction

`WP33` is already reserved for the exact fixed-mean/fixed-variance jitter no-go:

`notes/WP33_EXACT_FIXED_MEAN_VARIANCE_JITTER_NO_GO.md`.

The inverse timing-resource theorem is therefore **WP34**, not WP33:

`notes/WP34_MINIMUM_TIMING_RESOURCE_COST_THEOREM.md`.

The accidentally created duplicate `WP33_MINIMUM_TIMING_RESOURCE_COST_THEOREM.md` was removed.

---

## WP34 result

WP32 gives, for normalized absolutely continuous source spectral-FI density `w`,

\[
\bar\eta_I[w]
\le
\eta\,\mathcal W\!\left(\frac{\pi\mathfrak R_2}{\eta}\right)
\le
\eta\,\mathcal W\!\left(\frac{\pi\mathfrak H}{\eta}\right).
\]

If a task demands

\[
\bar\eta_I[w]\ge q,
\qquad q\le\eta,
\]

then necessarily

\[
\boxed{
\mathfrak R_2
\ge
\frac{\eta}{\pi}\mathcal W^{-1}(q/\eta)
}
\]

and

\[
\boxed{
\mathfrak H
\ge
\frac{\eta}{\pi}\mathcal W^{-1}(q/\eta).
}
\]

For a flat two-sided band `|omega|<=Omega`,

\[
\boxed{
\mathfrak R_2\ge\frac{2\Omega q}{\pi},
\qquad
\mathfrak H\ge\frac{2\Omega q}{\pi}.
}
\]

Writing ordinary-frequency half-band `B=Omega/(2pi)`:

\[
\boxed{
\mathfrak R_2\ge4Bq,
\qquad
\mathfrak H\ge4Bq.
}
\]

For a uniform per-captured-event hazard ceiling `Lambda`, because `mathfrak H<=eta Lambda`,

\[
\boxed{
\Lambda\ge\frac{4Bq}{\eta}.
}
\]

If `q=r eta` is retention relative to captured DC information,

\[
\boxed{\Lambda\ge4Br.}
\]

Constant-hazard exponential registration asymptotically attains the flat-band coefficient in the large-band regime.

---

## Manuscript audit state

`manuscript/event_resource_theorem_rev3.tex` was inspected directly in chunks after Round 12.

Verified:

- standard Poisson citations are present at the marked-event theorem;
- Wiener citation is present at the atomic theorem;
- exact marked-kernel normalization remains correct;
- `int G d omega = pi R2` prefactor remains correct;
- hazard proof is clean;
- exact fixed-mean/fixed-variance formula is algebraically correct;
- thermodynamic bridge explicitly states finite-state time-homogeneous Markov scope;
- rare-fast appendix is included and labeled;
- bibliography contains all cite keys used in the inspected manuscript;
- no remaining theorem inconsistency was identified.

An actual LaTeX compile has **not** been independently verified through the connector. The repository contains `.github/workflows/manuscript-check.yml`, but available connector workflow-run lookup does not expose ordinary push-triggered runs in a usable way. Do not claim compile success until a run/artifact is actually inspected.

---

## Recommended manuscript insertion

WP34 should appear as a short corollary immediately after the collision/hazard bounds. The cleanest headline is

\[
\boxed{\mathfrak H\ge4Bq}
\]

for a flat source-information band, with definitions adjacent to the equation.

It should be presented as the operational inverse of the main theorem, not as an independent mathematical discovery.
