# Roadmap — Autonomous Temporal Information Law

**Branch:** `agent/autonomous-temporal-information-law`

## Goal

Seek a foundational physical resource principle for temporal information when clock, signal, controller, detector, and memory are finite internal quantum systems. The finished Rev11 random-time law remains frozen on its parent branch.

## Completed theorem chain

### WP02 / WP03 / WP06 — finite-radius survival — PASS

`(R_lin^2/4)[Tr F_N/N] <= T(nu)`.

For globally stationary exact exchange,

`(R_lin^2/4)[Tr F_N/N] <= min{T_C(nu),T_S(nu)}`.

### WP04 / WP05 — exact structured autonomous retention — PASS

Hard and mean total-energy constraints have exact sine-chain envelopes and sharp near-lossless coefficient `pi`.

### WP07 / WP08 — zero-radius synthesis — PASS

One-sided boundary:

`Tr F_N/N <= J <= Delta T_U`.

Orthogonal modes admit frequency-weighted quadratic synthesis budgets.

### WP09 — bilateral synthesis — PASS

`sqrt[Tr F_N/N] <= sqrt(J_X)+sqrt(J_Y)`.

The exact qutrit extremizer proves additive endpoint synthesis false by factor two.

### WP10 — one-sided mixed law — PASS

For energy-invariant support,

`Tr F_N/N <= 4T_pre/R_B^2 + Delta T_syn`.

### WP11 / WP12 — noncommuting support and shared-curvature allocation — PASS

Shorting/principal-angle geometry is necessary. The exact second-order resource is one shared operator constraint

`Z_+ + Z_- <= C_Delta`.

The induced allocation `Phi_a` has an exact SDP-dual representation.

### WP13 / WP14 — positive action and curvature metric — PASS

`A_G^(2)=(1/4)Tr(G C_Delta)`.

Bilateral costs combine harmonically. Rank-one allocation is governed by inverse-curvature principal-angle geometry.

### WP15 / WP16 — measurement accessibility — PASS

Shared-kernel benchmark:

`physical resource 12 > SLD 43/4 > accessible Fisher 55/8`.

Generic rank-one-kernel common-record law:

`sqrt(Tr F_1)<=sqrt(R(B))+sqrt(r kappa)`.

### WP17 — operator/action Pareto target — NO-GO

Exact curvature plus its own scalar action is redundant. Direction killed absent an independent physical constraint.

### WP18 — clean autonomous dual synthesis action — PASS

For globally stationary zero-radius exact exchange:

bilateral

`A_C^(2)+A_S^(2)>=(hbar nu/4)[Tr F_N/N]`,

one-sided

`A_C^(2)+A_S^(2)>=(hbar nu/2)[Tr F_N/N]`.

Both coefficients are exactly sharp in fixed-total-energy shells with zero global time-translation asymmetry.

### WP19 — noncommuting autonomous mixed resource/action — PASS

For arbitrary coherent support, use two-sided shorted pre-existing resources `a_+,a_-` and one combined positive clock+signal **kernel endpoint-incidence action**

`A_CS^(2)=(1/4)Tr(G_CS C_Delta)`.

With restricted costs `g_+,g_-`,

`Tr F_N/N`

`<=min{Psi_(a_+)(4A_CS;g_+,g_-),`

`      Psi_(a_-)(4A_CS;g_-,g_+)}`.

The shared-kernel qutrit embeds into a fixed-total-energy exchange shell and the resource envelope is exactly `12`.

### WP20 — multi-gap autonomous spectral-action sum — PASS

For zero-radius pure-boundary modes in one common multiparameter family,

`C_Sigma>=sum_k[Z_(k,+)+Z_(k,-)]`.

For any positive cost `G`,

`sum_k gamma_k Tr F_(N,k)/N <=4A_(G,Sigma)^(2)`.

For clean bilateral exact exchanges,

`A_(G,Sigma)^(2)>=sum_k(hbar nu_k/4)Tr F_(N,k)/N`.

A single fixed Fourier measurement simultaneously saturates every mode and the full weighted sum in a fixed-total-energy shell.

## Significance / priority gate after WP20 — PROVISIONAL PASS

Authoritative note:

`notes/FOUNDATIONAL_SIGNIFICANCE_PRIORITY_GATE_AFTER_WP20.md`.

### Broad novelty claim — FAIL

Do not claim a new resource theory of time, Page--Wootters mechanism, asymmetry theory, multiphase metrology framework, or energy-constrained metrology theory.

### Narrow theorem package — PROVISIONAL PASS

The candidate paper story is:

> Globally stationary relative temporal information has two complementary resource regimes. Finite-radius information requires two-sided pre-existing spectral survival; rank-changing zero-radius information requires two-sided positive second-order spectral synthesis action. The laws are finite-copy and arbitrary-POVM, clean constants are sharp in fixed-total-energy shells, arbitrary coherent support requires nontrivial operator geometry, and the boundary law has a sharp frequency-weighted multi-gap sum.

Targeted searches through 2026-08-23 did not locate a direct predecessor with comparable scope and constants. Priority remains **unverified, not certified**.

### Required prior-art boundary

A future paper must explicitly distinguish itself from:

- Marvian--Spekkens modes of asymmetry, PRA 90, 062110 (2014);
- Carmo--Soares-Pinto Page--Wootters shared asymmetry, PRA 103, 052420 (2021);
- Tajima--Shiraishi--Saito conservation-law coherence cost, PR Research 2, 043374 (2020);
- Marvian QFI energetic-coherence formation cost, PRL 129, 190502 (2022);
- rank-changing QFI/Bures geometry;
- Gardner et al. waveform Holevo limit, PRL 132, 130801 (2024);
- Chen--Yang total protocol energy-constrained metrology, PRL 136, 070801 (2026);
- fixed-number relative-phase/multiphase and Fourier/covariant measurements;
- WAY/reference-frame theory, shorted operators, SDP/SOCP, and numerical-radius mathematics.

## Current mandatory gate — hostile mathematical audit

**No WP21 and no manuscript drafting until this audit is complete.**

### A. WP18 independent rederivation

1. Re-derive the two-quadrature Fisher convention from `D_c=(A+A^dagger)/2`, `D_s=(A-A^dagger)/(2i)`.
2. Re-derive one-sided and bilateral WP07/WP09 curvature bounds with the exact factor conventions.
3. Independently derive the clock and signal endpoint actions and the coefficients `hbar nu/2` and `hbar nu/4`.
4. Verify fixed-shell extremizers are exactly normalized/positive on an open parameter disk and truly globally stationary.
5. Verify the stated measurement achieves the claimed Fisher trace without a singular probability convention.

### B. Finite-copy scaling

Re-derive the `N`-copy complex tangent and show all weighted norms scale by exactly `N`. Check that the collective-POVM law therefore holds for every finite `N` without hidden i.i.d.-measurement assumptions.

### C. WP19 interpretation

1. Audit overlapping local endpoint projectors and multiplicities in `G_CS`.
2. Check `G_CS>=0` and that the shared global kernel curvature is charged only once.
3. Maintain the distinction between kernel endpoint-incidence action, full endpoint-population Laplacian, signed subsystem energy, and total protocol energy.
4. Reconstruct the fixed-shell shared-kernel benchmark independently.

### D. WP20 common Hessian and sum

1. Start from one genuine common `2m`-parameter `C^2` state family.
2. Sum the second-order PSD inequalities before any scalar endpoint reduction.
3. Verify the single `C_Sigma` inequality and positive spectral cost trace.
4. Audit frequency-dependent cost assignment when endpoint states participate in multiple mode labels; any multiplicity must have an explicit endpoint-incidence interpretation.
5. Recompute the common Fourier readout and show `Tr F_(1,k)=4c_k^2` simultaneously for all `k` under the branch convention.
6. Confirm the full weighted action sum is exactly saturated.

### E. Decision after audit

If any factor, physicality, or resource-interpretation defect appears, patch it before proceeding.

If the theorem chain survives intact:

1. record a hostile mathematical audit note;
2. freeze a minimal theorem stack for publication;
3. decide whether WP15/WP16 belong in the main paper or supplement;
4. only then begin manuscript formation.

## Deferred directions

Do not pursue unless directly needed for the publication story:

- mixed finite-radius + multi-gap theorem;
- controlled continuum limit;
- Gaussian covariance-changing synthesis;
- further exact common-record geometry.

## Validation

All current validators remain active, particularly:

- `verify_autonomous_dual_synthesis_action_law.py`
- `verify_noncommuting_autonomous_mixed_resource_action_law.py`
- `verify_multigap_autonomous_spectral_action_sum_law.py`

Numerical validation is supporting evidence only; the current gate requires independent analytic rederivation.

## Documentation discipline

Every material theorem, failed conjecture, priority collision, or validation result must be recorded immediately and reflected in `README.md`, `AGENTS.md`, and this file. The repository, not chat history, is authoritative.
