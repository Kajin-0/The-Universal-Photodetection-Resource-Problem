# Autonomous Temporal Information Law

**Branch:** `agent/autonomous-temporal-information-law`

The frozen Rev11 paper remains untouched on `agent/temporal-information-resource-law`.

## Grand challenge

Determine what physical resource constrains temporal information when clock/reference, signal, controller, detector, and memory are finite internal systems and no ideal external timing operation is supplied for free.

The branch is analytical/theoretical and falsification-first. The repository, not chat history, is authoritative.

## Current theorem hierarchy

### WP02 — finite-radius robust survival

For an exact temporal gap `nu`, finite `N`, and arbitrary collective POVM,

`(R_lin^2/4)[Tr F_N/N] <= T(nu)`.

Local Fisher strength must be weighted by a physical tangent radius.

### WP03 / WP06 — autonomous dual survival

For a globally stationary exchange tangent

`[H_S,A_nu]=+hbar nu A_nu`,

`[H_C,A_nu]=-hbar nu A_nu`,

`K_N=(R_lin^2/4)[Tr F_N/N] <= min{T_C(nu),T_S(nu)}`.

WP06 removes separate local stationarity and allows arbitrary pre-existing coherent/history-state baselines.

### WP04 / WP05 — exact structured autonomous retention

Hard total-excitation cap:

`R_M(k)<=cos^2{pi/[floor(L/k)+2]}`.

Mean total excitation has the exact piecewise-linear envelope built from

`g_L=cos^2[pi/(L+2)]`.

Sine-chain extremizers make the near-lossless coefficient `pi` exactly sharp.

### WP07 / WP08 — zero-radius quadratic synthesis

For one baseline-empty endpoint,

`Tr F_N/N <= J <= Delta T_U(0)`.

For orthogonal modes and one common record,

`sum_k w_k Tr F_(N,k)/N <= sum_k w_k Delta_k T_k(0)`.

This closes the coherent-sideband baseline-energy loophole by charging second-order spectral synthesis.

### WP09 — bilateral synthesis Minkowski law

For opposite support orientations,

`sqrt[Tr F_N/N] <= sqrt(J_X)+sqrt(J_Y)`.

For clean empty upper/lower endpoints,

`Tr F_N/N <= [sqrt(Delta T_+)+sqrt(Delta T_-)]^2`.

An exact qutrit Fourier model proves ordinary additive endpoint accounting false by factor two.

### WP10 — one-sided mixed survival+synthesis

For energy-invariant baseline support,

`Tr F_N/N <= 4T_pre/R_B^2 + Delta T_syn`.

The corresponding `hbar nu/4` local energy/action coefficient is exactly sharp.

### WP11 — noncommuting-support shorted geometry

For arbitrary coherent support,

`B=PAP`, `K_+=QAP`, `K_-=QA^dagger P`,

and

`sqrt[Tr F_N/N]`

`<=min{sqrt(J_B^+ + J_+) + sqrt(J_-),`

`      sqrt(J_B^- + J_-) + sqrt(J_+)}`.

Compressed energy endpoint projectors require shorting/principal-angle factors. A four-level exact-gap counterexample proves omission of that geometry gives a false observable Fisher bound.

### WP12 — exact shared-curvature operator allocation

Second-order positivity gives

`Z_+ + Z_- <= C_Delta`.

The exact curvature-only allocation

`Phi_a(C;R_+,R_-)=sup [sqrt(a+Tr Z_+) + sqrt(Tr Z_-)]^2`

has a one-dimensional variational representation over an SDP value. This removes WP11's double charging of shared curvature.

### WP13 — positive spectral-action law

For one positive kernel cost operator `G`,

`A_G^(2)=(1/4)Tr(G C_Delta)`.

If `g_+,g_-` are the minimum restricted costs on the two synthesized ranges,

`g_+J_+ + g_-J_- <= 4A_G^(2)`.

For pure bilateral synthesis the effective price is harmonic:

`g_parallel=(1/g_+ + 1/g_-)^(-1)`.

### WP14 — rank-one curvature-metric principal angle

For rank-one synthesized ranges, the exact WP12 allocation is controlled by capacities in the inverse shorted-curvature metric and a curvature-whitened overlap `c`, not by the ordinary Hilbert-space angle.

The matrix resource contains irreducible information lost by scalar action compression.

### WP15 — exact shared-kernel qutrit common-record optimum

The benchmark has exact hierarchy

`physical resource 12 > SLD trace 43/4 > accessible Fisher 55/8`.

An explicit quadratic witness proves

`sup_(one-copy POVMs) Tr F_1=55/8`.

Thus physical resource, quantum-statistical geometry, and common-record accessibility are distinct layers.

### WP16 — generic rank-one-kernel common-record theorem

Let

`rho0=P/r`, `rank(Q)=1`,

`A=[[B,b],[a^dagger,0]]`.

Define

`kappa=||a||^2+||b||^2+2|a^dagger b|`

and let `R(B)` be the support-only common-record optimum.

Then

`sqrt(Tr F_1)<=sqrt(R(B))+sqrt(r kappa)`.

For qutrits,

`R(B)=4w(B)^2`,

so

`Tr F_1<=[2w(B)+sqrt(2kappa)]^2`.

A signed three-cycle saturates the bound at `9`, while naive regular-plus-singular addition gives only `5`. A second model with the same two scalar invariants has ceiling `6`, proving additional phase/orientation geometry is required for an exact model-specific optimum.

WP16 also gives the exact Fisher-witness convex dual and its weighted numerical-radius LMI form.

### WP17 — operator/action Pareto redundancy no-go

If exact `C_Delta` is known, the scalar action `Tr(GC_Delta)` is a derived statistic and adds no constraint. If only the scalar action is retained, optimizing over unspecified curvature collapses exactly to WP13.

Do not pursue a generic `operator + its own action` Pareto theorem without an additional independent physical constraint.

### WP18 — sharp autonomous dual synthesis action

In a globally stationary exact exchange with clean zero-radius boundary synthesis, define positive absolute-gap actions on both local subsystems.

Bilateral case:

`A_C^(2)+A_S^(2) >= (hbar nu/4)[Tr F_N/N]`.

One-sided case:

`A_C^(2)+A_S^(2) >= (hbar nu/2)[Tr F_N/N]`.

Both coefficients are exactly sharp in fixed-total-energy exchange shells. Global time-translation asymmetry is zero throughout the extremizing nonlinear families.

### WP19 — arbitrary coherent support: autonomous mixed resource/action law

For a general exact exchange with `[P,H_C]` and/or `[P,H_S]` nonzero, use the WP11 support decomposition.

Two-sided pre-existing internal resources are bounded by the minimum of the signal-side and clock-side shorted endpoint ceilings, producing `a_+` and `a_-`.

Define one positive combined clock+signal endpoint-incidence operator

`G_CS=hbar nu Q[Pi_(S,U)+Pi_(S,D)+Pi_(C,U)+Pi_(C,D)]Q`

and the **kernel-resolved endpoint-incidence action**

`A_CS^(2)=(1/4)Tr(G_CS C_Delta)`.

Let `g_+,g_-` be its restricted costs on the two synthesized ranges. Then

`g_+J_+ + g_-J_- <=4A_CS^(2)`.

Using the exact WP13 action envelope `Psi`,

`Tr F_N/N`

`<=min{Psi_(a_+)(4A_CS^(2);g_+,g_-),`

`      Psi_(a_-)(4A_CS^(2);g_-,g_+)}`.

This bridges the WP03 finite-radius and WP18 zero-radius autonomous regimes for arbitrary coherent support.

**Interpretive caveat:** in the noncommuting-support regime `A_CS^(2)` is the endpoint incidence of the **kernel curvature** `Q Delta rho Q`; it is not generally the full local endpoint-population Laplacian or signed mean-energy curvature.

The WP12 shared-kernel qutrit embeds into a fixed-total-energy clock--signal shell and gives exactly

`a_+=a_-=5/4`, `g_+=g_-=13 hbar nu/4`, `4A_CS=247 hbar nu/16`,

for which the WP19 envelope is exactly `12`. Hence the complete `12 > 43/4 > 55/8` hierarchy occurs inside one globally stationary relational experiment.

### WP20 — multi-gap autonomous spectral-action sum

For zero-radius pure-boundary exact exchange modes `A_k` in one common `C^2` multiparameter family, define

`C_Sigma=Q sum_k(partial_(x_k)^2+partial_(y_k)^2)rho Q`.

Second-order positivity gives the shared operator inequality

`C_Sigma >= sum_k[Z_(k,+)+Z_(k,-)]`.

For any single positive cost operator `G`, set

`A_G,Sigma^(2)=(1/4)Tr(G C_Sigma)`.

Let `gamma_k` be the harmonic restricted cost for a bilateral mode, or the single restricted cost for a one-sided mode. Then

`boxed: sum_k gamma_k [Tr F_(N,k)/N] <=4A_G,Sigma^(2)`.

The bound holds even if different modes are granted different optimal POVMs, and therefore also for one common record.

In the clean mode-separated autonomous case, choose cost `2hbar nu_k` on each paired endpoint. Then

`A_G,Sigma^(2)>=sum_k (hbar nu_k/4)[Tr F_(N,k)/N]`.

This complete frequency-weighted sum is simultaneously sharp with **one common measurement**. In the fixed-total-excitation shell

`|n>=|m-n>_C|m+n>_S`, `n=-m,...,m`,

use baseline `|0>` and

`A_k=c_k(|k><0|+|0><-k|)`.

The `(2m+1)`-point discrete Fourier basis gives

`Tr F_(1,k)=4c_k^2`

for every `k` simultaneously and saturates the full weighted action sum.

## Current frontier

The clean local/autonomous hierarchy is now fairly complete. Highest-value next actions are:

1. hostile priority/significance audit of WP03 and WP18--WP20 against Page--Wootters resource theory, relative-phase/fixed-number multiphase metrology, quantitative WAY, waveform Holevo limits, and 2025--2026 energy-constrained metrology;
2. determine whether a mixed finite-radius + multi-gap theorem adds anything beyond a nonlinear sum of WP19 envelopes; kill it if not;
3. consider a controlled continuum limit only with explicit regularity assumptions;
4. decide whether the autonomous theorem chain is publication-grade before adding further abstract matrix work.

## Validation

Independent validators include the complete WP02--WP15 set plus:

- `numerics/verify_rank_one_kernel_common_record_minkowski.py`
- `numerics/verify_autonomous_dual_synthesis_action_law.py`
- `numerics/verify_noncommuting_autonomous_mixed_resource_action_law.py`
- `numerics/verify_multigap_autonomous_spectral_action_sum_law.py`

## Priority discipline

Page--Wootters/shared-asymmetry resource theory, quantum reference frames, relative-phase and multiphase metrology, Fourier/covariant measurements, waveform Holevo theory, numerical-radius/Ando theory, shorted operators, SDP/SOCP duality, PSD-cone curvature, rank-changing QFI/Bures geometry, and energy-constrained metrology are established. Candidate novelty is restricted to the frequency-resolved **rank-changing temporal-resource bridge laws** and their two-sided autonomous synthesis-action consequences.

Priority remains **unverified, not certified**.

Read `AGENTS.md`, `ROADMAP.md`, and WP01--WP20 before continuing. Record every material theorem, counterexample, priority collision, or killed direction immediately; do not rely on chat history.
