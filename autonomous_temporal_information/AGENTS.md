# AGENTS — Autonomous Temporal Information Law

**Branch:** `agent/autonomous-temporal-information-law`

The frozen Rev11 paper remains on `agent/temporal-information-resource-law` and must not be rewritten absent a concrete defect.

## Mission

Determine the physical resource constraining temporal information when clock/reference, signal, controller, detector, and memory are finite physical systems and no ideal externally timed operation is free.

Research is analytical/theoretical, falsification-first, and documentation-first. The repository, not chat history, is authoritative.

## Current status

**WP20 is the latest theorem work package.** A hostile significance/priority gate after WP20 gives a **PROVISIONAL PASS for a narrowly scoped theorem paper**, while broad novelty claims fail. No WP21 should be created until WP18--WP20 pass a dedicated hostile mathematical audit.

Read first:

1. `notes/FOUNDATIONAL_SIGNIFICANCE_PRIORITY_GATE_AFTER_WP20.md`
2. `notes/WP20_MULTIGAP_AUTONOMOUS_SPECTRAL_ACTION_SUM_LAW.md`
3. `notes/WP19_HOSTILE_AUDIT_AND_PRIOR_ART_BOUNDARY.md`
4. `notes/WP19_NONCOMMUTING_AUTONOMOUS_MIXED_RESOURCE_ACTION_LAW.md`
5. `notes/WP18_AUTONOMOUS_DUAL_SYNTHESIS_ACTION_LAW.md`
6. WP11--WP16 if noncommuting-support or accessibility details are needed.

## Essential theorem hierarchy

### WP02 / WP03 / WP06 — finite-radius survival

For exact temporal gap `nu`, finite `N`, arbitrary collective POVM,

`(R_lin^2/4)[Tr F_N/N] <= T(nu)`.

For globally stationary exact exchange,

`(R_lin^2/4)[Tr F_N/N] <= min{T_C(nu),T_S(nu)}`.

This is the pre-existing-resource regime.

### WP04 / WP05 — structured autonomous retention

Hard and mean total-excitation constraints have exact sine-chain envelopes and sharp near-lossless coefficient `pi`.

### WP07 / WP08 / WP09 — zero-radius synthesis

At a rank-deficient physical boundary, `R_lin=0` does not imply zero local information. For an exact nonlinear family, second-order endpoint synthesis replaces zeroth-order baseline population.

One-sided:

`Tr F_N/N <= J <= Delta T_U`.

Bilateral:

`sqrt[Tr F_N/N] <= sqrt(J_+)+sqrt(J_-)`.

Naive additive bilateral synthesis is false by an exact factor-two qutrit extremizer.

### WP10 / WP11 / WP12 — mixed and noncommuting support

Energy-invariant support gives a sharp additive finite-radius+synthesis law.

For arbitrary coherent support use

`B=PAP`, `K_+=QAP`, `K_-=QA^dagger P`.

Shorting/principal-angle geometry is genuinely necessary. Shared kernel curvature satisfies

`Z_+ + Z_- <= C_Delta`,

and the exact curvature allocation is a one-dimensional minimization over an SDP value.

### WP13 / WP14 — positive spectral action and operator overlap

`A_G^(2)=(1/4)Tr(G C_Delta)`.

Bilateral scalar action prices combine harmonically. Rank-one shared-curvature allocation is governed by capacities and a principal angle in the inverse shorted-curvature metric.

### WP15 / WP16 — accessibility layer

Resource, QFI/SLD, and common-record information are different objects.

Shared-kernel benchmark:

`12 > 43/4 > 55/8`.

Generic rank-one-kernel maximally mixed support:

`sqrt(Tr F_1)<=sqrt(R(B))+sqrt(r kappa)`,

`kappa=||a||^2+||b||^2+2|a^dagger b|`.

For qutrits `R(B)=4w(B)^2`.

### WP17 — killed direction

Do not pursue a generic `exact curvature + its own scalar action` Pareto law. It is redundant absent another independent physical constraint.

### WP18 — sharp autonomous zero-radius synthesis action

For globally stationary exact exchange

`[H_S,A_nu]=+hbar nu A_nu`,

`[H_C,A_nu]=-hbar nu A_nu`,

bilateral clean boundary synthesis obeys

`A_C^(2)+A_S^(2)>=(hbar nu/4)[Tr F_N/N]`.

One-sided clean synthesis obeys

`A_C^(2)+A_S^(2)>=(hbar nu/2)[Tr F_N/N]`.

Both coefficients are exactly sharp inside fixed-total-energy shells. Global `H_C+H_S` asymmetry is exactly zero in the extremizing nonlinear families.

### WP19 — arbitrary coherent-support autonomous bridge

Define two-sided shorted pre-existing resource ceilings `a_+,a_-` and one combined positive clock+signal endpoint-incidence cost operator `G_CS`.

The kernel-resolved action is

`A_CS^(2)=(1/4)Tr(G_CS C_Delta)`.

With restricted costs `g_+,g_-`,

`Tr F_N/N`

`<=min{Psi_(a_+)(4A_CS;g_+,g_-),`

`      Psi_(a_-)(4A_CS;g_-,g_+)}`.

Do not call general `A_CS` the full endpoint-population Laplacian, signed mean-energy curvature, or total protocol energy.

### WP20 — multi-gap autonomous sum

For zero-radius pure-boundary exchange modes in one common multiparameter family,

`C_Sigma>=sum_k[Z_(k,+)+Z_(k,-)]`.

For any `G>=0`,

`sum_k gamma_k Tr F_(N,k)/N <= 4A_(G,Sigma)^(2)`.

Clean bilateral gaps give

`A_(G,Sigma)^(2)>=sum_k(hbar nu_k/4)Tr F_(N,k)/N`.

The full weighted sum is simultaneously saturated by one discrete Fourier measurement in a fixed-total-energy shell.

## Significance gate

### Broad novelty — FAIL

The following are prior infrastructure, not paper claims:

- Page--Wootters relational time;
- shared/mutual asymmetry and internal coherence;
- modes of asymmetry and Bohr-frequency decomposition;
- QFI as energetic coherence / asymmetry resource;
- quantitative WAY and coherence cost under conservation laws;
- relative-phase / multiphase estimation and Fourier/covariant measurements;
- waveform QCRB/Holevo theory;
- total-protocol energy-constrained metrology;
- PSD-cone second-order geometry;
- singular QFI/Bures geometry;
- shorted operators, principal angles, numerical radius, SDP/SOCP duality.

### Narrow candidate contribution — PROVISIONAL PASS

The surviving paper story is the operational **finite-radius / zero-radius resource bridge** for globally stationary relative temporal modes:

- finite radius -> two-sided pre-existing spectral survival;
- zero radius -> two-sided positive second-order spectral synthesis action;
- arbitrary finite-copy POVMs;
- exact sharp fixed-shell coefficients;
- noncommuting-support operator extension;
- sharp frequency-weighted boundary sum.

Priority remains **unverified, not certified**.

Key literature that must be cited and distinguished includes:

- Marvian--Spekkens, PRA 90, 062110 (2014), modes of asymmetry;
- Carmo--Soares-Pinto, PRA 103, 052420 (2021), Page--Wootters shared asymmetry;
- Tajima--Shiraishi--Saito, PR Research 2, 043374 (2020), coherence cost under conservation laws;
- Marvian, PRL 129, 190502 (2022), QFI energetic-coherence cost;
- Gardner et al., PRL 132, 130801 (2024), waveform Holevo limit;
- Chen--Yang, PRL 136, 070801 (2026), total energy-constrained metrology.

## Immediate work order — hostile mathematical audit

Do **not** create WP21 until all items below are resolved and recorded.

1. Re-derive WP18 directly from WP07/WP09 conventions; audit every factor `2` and `4`.
2. Re-derive the one-sided and bilateral fixed-shell extremizers and verify normalization/positivity on a genuine open parameter neighborhood.
3. Re-derive finite-copy scaling for the synthesis laws instead of assuming the earlier proof transfers unchanged.
4. Audit WP19 endpoint projector overlap and multiplicity in `G_CS`; preserve the kernel-incidence interpretation.
5. Re-derive WP20 by summing the second-order PSD constraints over a genuine common multiparameter family.
6. Check that the common Fourier readout simultaneously saturates every Fisher block with the branch's exact two-quadrature convention.
7. Check that multi-gap cost assignment does not accidentally double count a state in a way inconsistent with the stated *positive endpoint-incidence* resource.
8. Record any defect immediately. If no defect is found, write a hostile mathematical audit note and then decide manuscript formation.

## Numerical gates

All existing validators remain required, especially:

- `numerics/verify_autonomous_dual_synthesis_action_law.py`
- `numerics/verify_noncommuting_autonomous_mixed_resource_action_law.py`
- `numerics/verify_multigap_autonomous_spectral_action_sum_law.py`

Numerics validate algebra; they do not replace the hostile analytic rederivation.

## Documentation rule

Every material theorem, failed conjecture, priority collision, or killed direction must be recorded immediately and reflected in `README.md`, `AGENTS.md`, and `ROADMAP.md`. The repository, not chat history, is authoritative.
