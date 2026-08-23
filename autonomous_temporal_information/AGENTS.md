# AGENTS — Autonomous Temporal Information Law

**Branch:** `agent/autonomous-temporal-information-law`

The frozen Rev11 paper remains on `agent/temporal-information-resource-law` and must not be rewritten absent a concrete defect.

## Mission

Determine the physical resource constraining temporal information when clock/reference, signal, controller, detector, and memory are finite internal systems and no ideal external timing operation is free.

Research is analytical/theoretical, falsification-first, and documentation-first. Standard asymmetry/reference-frame theory, Page--Wootters, relative-phase and multiphase metrology, waveform Holevo theory, numerical-radius/Ando theory, POVM convex duality, shorted operators, SDP/SOCP theory, PSD-cone curvature, rank-changing QFI/Bures geometry, Gill--Massar/Holevo compatibility, and energy-constrained metrology are infrastructure unless a distinct operational temporal-information theorem is isolated.

## Current status

**WP20 — multi-gap autonomous spectral-action sum law: analytic PASS and independently validated.**

The branch now has a coherent hierarchy:

1. finite-radius information -> pre-existing spectral survival;
2. zero-radius information -> second-order spectral synthesis;
3. bilateral synthesis -> score-space Minkowski geometry;
4. noncommuting support -> shorted/operator geometry;
5. positive spectral action -> endpoint-cost weighting;
6. common-record accessibility -> a separate measurement-compatibility layer;
7. autonomous exact exchange -> matched clock+signal resources in both finite-radius and zero-radius regimes;
8. multiple zero-radius exchange frequencies -> one shared Hessian spectral-action budget.

## Essential theorem stack

### WP02 / WP03 / WP06

`(R_lin^2/4)[Tr F_N/N] <= T(nu)`.

For globally stationary exact exchange,

`(R_lin^2/4)[Tr F_N/N] <= min{T_C(nu),T_S(nu)}`.

### WP04 / WP05

Structured globally stationary retention has exact sine-chain hard/mean-energy envelopes and sharp near-lossless coefficient `pi`.

### WP07 / WP08

At `R_lin=0`, one-sided boundary synthesis obeys

`Tr F_N/N <= J <= Delta T_U`.

Orthogonal mode sums admit a positive frequency-weighted synthesis budget.

### WP09

Bilateral boundary synthesis obeys

`sqrt[Tr F_N/N] <= sqrt(J_X)+sqrt(J_Y)`.

The factor-two failure of additive endpoint synthesis is exactly sharp.

### WP10

Energy-invariant-support one-sided mixed law:

`Tr F_N/N <= 4T_pre/R_B^2 + Delta T_syn`.

### WP11 / WP12

For arbitrary coherent support use

`B=PAP`, `K_+=QAP`, `K_-=QA^dagger P`.

Shorting/principal-angle geometry is necessary. Shared kernel curvature satisfies

`Z_+ + Z_- <= C_Delta`.

The exact allocation `Phi_a` is a one-dimensional minimization over an SDP value.

### WP13 / WP14

Positive spectral action:

`A_G^(2)=(1/4)Tr(GC_Delta)`.

Bilateral action costs combine harmonically. Rank-one allocation geometry is controlled by the principal angle in the inverse shorted-curvature metric.

### WP15

Exact shared-kernel qutrit hierarchy:

`12 > 43/4 > 55/8`

for physical resource, SLD trace, and one-copy common-record Fisher supremum.

### WP16

For rank-one kernel and maximally mixed support,

`sqrt(Tr F_1)<=sqrt(R(B))+sqrt(r kappa)`,

`kappa=||a||^2+||b||^2+2|a^dagger b|`.

For qutrits `R(B)=4w(B)^2`. A signed three-cycle saturates the universal bound at `9`; naive additivity gives only `5`. Exact accessibility needs additional phase/orientation geometry.

WP16 also gives the exact Fisher-witness convex dual and weighted numerical-radius LMI.

### WP17 — NO-GO

A generic `exact curvature + its own scalar action` Pareto law is redundant. Do not pursue it without an independent physical constraint.

### WP18

Clean zero-radius globally stationary exchange:

bilateral

`A_C^(2)+A_S^(2)>=(hbar nu/4)[Tr F_N/N]`,

one-sided

`A_C^(2)+A_S^(2)>=(hbar nu/2)[Tr F_N/N]`.

Both coefficients are exactly sharp in fixed-total-energy shells with zero global asymmetry.

### WP19

For arbitrary coherent support, define two-sided shorted pre-existing resources `a_+,a_-` and one combined positive clock+signal endpoint-incidence operator `G_CS`.

The general resource is the **kernel-resolved endpoint-incidence action**

`A_CS^(2)=(1/4)Tr(G_CS C_Delta)`.

With restricted costs `g_+,g_-`,

`Tr F_N/N`

`<=min{Psi_(a_+)(4A_CS;g_+,g_-),`

`      Psi_(a_-)(4A_CS;g_-,g_+)}`.

Do not call general `A_CS` the full endpoint-population Laplacian or signed mean-energy curvature.

The shared-kernel qutrit embeds into a fixed-total-energy exchange shell and WP19 reproduces the WP12 resource ceiling `12` exactly.

Read:
- `notes/WP19_NONCOMMUTING_AUTONOMOUS_MIXED_RESOURCE_ACTION_LAW.md`
- `notes/WP19_HOSTILE_AUDIT_AND_PRIOR_ART_BOUNDARY.md`

### WP20

For zero-radius pure-boundary modes in one multiparameter family,

`C_Sigma=Q sum_k(partial_(x_k)^2+partial_(y_k)^2)rho Q`

obeys

`C_Sigma>=sum_k[Z_(k,+)+Z_(k,-)]`.

For any `G>=0`,

`A_G,Sigma^(2)=(1/4)Tr(G C_Sigma)`

and effective mode costs `gamma_k`,

`boxed: sum_k gamma_k Tr F_(N,k)/N <=4A_G,Sigma^(2)`.

Clean bilateral endpoint costs give

`A_G,Sigma^(2)>=sum_k (hbar nu_k/4)Tr F_(N,k)/N`.

This is simultaneously sharp with one common Fourier measurement in the fixed-total-energy shell

`|n>=|m-n>_C|m+n>_S`,

baseline `|0>`,

`A_k=c_k(|k><0|+|0><-k|)`.

The same Fourier basis yields `Tr F_(1,k)=4c_k^2` for every gap at once.

Read:
`notes/WP20_MULTIGAP_AUTONOMOUS_SPECTRAL_ACTION_SUM_LAW.md`.

## Current frontier

**Do not automatically create WP21.** First perform a hostile significance/priority gate.

Highest-value tasks:

1. compare WP03 and WP18--WP20 directly against Page--Wootters shared-asymmetry resource theory, quantum reference frames, fixed-number relative-phase/multiphase metrology, quantitative WAY, and current energy-constrained metrology;
2. determine whether a mixed finite-radius + multi-gap theorem is genuinely stronger than summing nonlinear WP19 envelopes; kill it if not;
3. examine a controlled continuum limit only if it gives a nontrivial spectral action measure;
4. decide whether the autonomous theorem chain is publication-grade before adding more operator mathematics.

## Numerical gates

All previous WP validators remain required. New gates:

- `numerics/verify_rank_one_kernel_common_record_minkowski.py`
- `numerics/verify_autonomous_dual_synthesis_action_law.py`
- `numerics/verify_noncommuting_autonomous_mixed_resource_action_law.py`
- `numerics/verify_multigap_autonomous_spectral_action_sum_law.py`

## Documentation rule

Every material theorem, failed conjecture, priority collision, or killed direction must be recorded immediately and reflected in `README.md`, `AGENTS.md`, and `ROADMAP.md`. The repository, not chat history, is authoritative.
