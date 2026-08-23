# Manuscript handoff — autonomous temporal information

**Date:** 2026-08-23

**Branch:** `agent/autonomous-temporal-information-law`

## Canonical manuscript state

The current journal-facing manuscript is **PRX Quantum R3**, build-verified, standalone, and science-frozen while the post-R3 research chain is audited.

The old M2R1 handoff is obsolete.

Canonical generated submission roots:

- `autonomous_temporal_resource_law_prxq_r3.tex`
- `autonomous_temporal_resource_law_supplement_m2r3.tex`
- `references.bib`

Generation/audit scripts:

- `apply_m2r2_review_repairs.py`
- `apply_submission_cleanup_r2.py`
- `apply_m2r3_boundary_strengthening.py`
- `apply_prxq_frontmatter_r3.py`
- `check_m2_tex_static.py`

Workflow:

`.github/workflows/autonomous-temporal-manuscript-check.yml`

The R3 GitHub Actions gate passed generation, standalone-identity scanning, static TeX integrity, main compilation, supplement compilation, and artifact packaging.

## Manuscript integrity lock

The paper and supplement must be scientifically standalone.

Never include:

- personal GitHub URLs;
- usernames;
- repository names;
- internal work-package labels exposed to readers;
- development history;
- statements requiring the reader to consult internal notes or code repositories.

The standalone identity-leak gate must remain active.

## R3 scientific claim

The paper is about **two physical spectral-resource regimes** for globally stationary relative temporal information, not a generic new resource theory of time.

### Finite affine radius

Pre-existing spectral survival backs the robust local temporal mode:

`(R_lin^2/4)[Tr F_N^tan/N] <= T(nu)`.

For an autonomous clock--signal exchange, the same information must be backed on both local sides.

### Rank-changing zero radius

A nonlinear physical family may remain informative even when the affine radius vanishes. Positive second-order endpoint synthesis becomes the resource.

Clean exact-exchange action laws:

- bilateral `A_C^(2)+A_S^(2) >= (hbar nu/4)[Tr F_N^tan/N]`;
- one-sided `A_C^(2)+A_S^(2) >= (hbar nu/2)[Tr F_N^tan/N]`.

R3 strengthens the boundary section with

`A_C^(2)+A_S^(2) >= (hbar nu/4)Tr H_SLD`

for the pure-boundary SLD tangent and with the spectator-curvature no-go showing that arbitrary additional Bures boundary curvature is not determined by the selected first-order temporal mode.

R3 also includes:

- the coherent-support mixed survival/synthesis theorem;
- the audited piecewise `Psi_a(e;p,q)` envelope;
- the exact qutrit hierarchy `12 > 43/4 > 55/8`;
- the multi-gap shared-Hessian spectral-action sum;
- coordinate-covariant parameter-metric language;
- explicit scope distinction from structured random-time encoding results;
- standalone Data Availability and AI-use disclosures with no repository dependency.

## Build status

The final R3 Actions verification passed:

1. R2 referee-repair generation;
2. final submission cleanup;
3. R3 boundary-QFI strengthening;
4. PRX Quantum R3 front-matter/figure generation;
5. static TeX + standalone identity gate;
6. main manuscript compile;
7. supplement compile;
8. artifact packaging.

Do not regress to older `_m2`, `_m2r1`, or R2 roots for submission work.

## Post-R3 research is separate from the frozen manuscript

Research was explicitly reopened after external critique to address:

1. kinematic versus dynamical implementation cost;
2. exact-resonance idealization;
3. finite-dimensionality;
4. classical nonregular-statistics positioning.

That program now runs through **WP31** and has produced results materially stronger than the R3 scope.

### WP21--WP23: dynamical implementation completion

For a smooth unitary dilation,

`Q partial_j^2 rho Q
 =2 Tr_E[(Q⊗I)K_j Omega_0 K_j(Q⊗I)]`.

For a prescribed feasible metric-contracted target-kernel Hessian `C`,

`V_min=(1/2)Tr C`.

For clean exact exchange,

`V_min=A_ex^(2)/(hbar nu)`.

The finite-dimensional optimum is exactly total-energy conserving.

### WP24--WP27: audit and robustness

- `Psi_a` was independently re-derived and numerically verified; no defect found.
- Classical nonregular boundary statistics are mandatory prior art, not quantum novelty.
- WP25 gives finite-radius approximate-gap robustness.
- WP27 gives rank-boundary approximate-exchange robustness with explicit residual score-amplitude penalties.

### WP28--WP31: infinite-dimensional completion

- WP28: finite-radius theorem for trace-class baselines and bounded relative tangents on separable Hilbert spaces.
- WP29: rank-boundary synthesis/action theorem for Hilbert--Schmidt right-relative tangents.
- WP30: exact unconstrained infinite-dimensional prescribed-2-jet implementation minimum.
- WP31: exact **semibounded, total-energy-conserving** infinite-dimensional implementation minimum even for unbounded occupied target-energy support, using an incoherent shell mixture and zero-energy ancilla.

WP31 gives

`inf V_impl=(1/2)Tr C`

over exactly energy-conserving smooth unitary dilations and hence

`V_min=A_ex^(2)/(hbar nu)`

in the clean single-gap endpoint geometry.

## Current publication decision gate

**Do not automatically insert WP21--WP31 into R3.**

The new theorem chain is now large enough that indiscriminate integration would likely make the existing paper less focused.

Before changing the manuscript:

1. hostile-audit WP31's stationary trace-class energy-support lemma;
2. hostile-audit its trace-norm `C^2` dominated-convergence step;
3. run the expanded mixed/degenerate-shell validator;
4. perform a targeted priority search for state-specific prescribed-second-order-jet Stinespring/purification cost results;
5. compare two architectures:
   - **R4:** add only the strongest dynamical theorem and perhaps concise robustness/infinite-dimensional corollaries;
   - **follow-up:** keep R3 focused and build a separate article around WP21--WP31.

Until that gate is complete, R3 remains the canonical paper.

## Prior-art lock

Do not claim novelty for:

- Page--Wootters relational time or asymmetry modes;
- generic Fisher/QFI/Bures/Holevo theory;
- Bures/Uhlmann horizontal purification geometry or `QFI/4` minimum purification speed;
- generic quantum speed limits or integrated Hamiltonian/control norms;
- classical nonregular boundary asymptotics;
- energy-conserving/covariant Stinespring dilation theory;
- infinite-dimensional QFI/Bures functional analysis;
- numerical-radius, shorted-operator, Schur/PSD-cone, or Cauchy--Schwarz mathematics.

The candidate post-R3 novelty is narrowly the endpoint-action / prescribed-kernel-2-jet minimum implementation-cost identity under globally conserving relational dynamics and its controlled detuning/infinite-dimensional extensions. Priority remains unverified.

## Current work order

1. complete WP31 hostile/prior-art audit;
2. decide R4 versus follow-up;
3. only after that decision modify journal-facing source;
4. if further theorem work is warranted, prioritize noisy/CPTP implementation cost or unbounded-relative-tangent quadratic-form extensions rather than adding more bookkeeping to R3.