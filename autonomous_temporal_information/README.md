# Autonomous Temporal Information Law

**Branch:** `agent/autonomous-temporal-information-law`

The frozen Rev11 paper remains untouched on `agent/temporal-information-resource-law`.

## Grand challenge

Determine what physical resource constrains temporal information when clock/reference, signal, controller, detector, and memory are finite internal systems and no ideal external timing operation is supplied for free.

The branch is analytical/theoretical, falsification-first, and documentation-first. The repository, not chat history, is authoritative.

## Core theorem hierarchy

### Finite-radius regime — WP02 / WP03 / WP06

For an exact temporal gap `nu`, finite `N`, and arbitrary collective POVM,

`(R_lin^2/4)[Tr F_N/N] <= T(nu)`.

For a globally stationary clock--signal exchange,

`(R_lin^2/4)[Tr F_N/N] <= min{T_C(nu),T_S(nu)}`.

Thus local Fisher strength alone is not a resource: it must be weighted by a physical affine tangent radius. The autonomous form requires matched pre-existing spectral support on both sides of the relational cut.

### Structured autonomous retention — WP04 / WP05

Hard and mean total-excitation constraints have exact sine-chain retention envelopes, with sharp near-lossless coefficient `pi`.

### Zero-radius boundary regime — WP07 / WP08 / WP09

When `R_lin=0` but an exact nonlinear physical family exists, second-order endpoint synthesis replaces pre-existing population as the resource.

One-sided:

`Tr F_N/N <= J <= Delta T_U(0)`.

Bilateral:

`sqrt[Tr F_N/N] <= sqrt(J_+)+sqrt(J_-)`.

The factor-two failure of naive additive endpoint cost is exactly sharp.

### Mixed and noncommuting support — WP10 / WP11 / WP12

For energy-invariant support, finite-radius and one-sided synthesis costs add sharply.

For arbitrary coherent support, decompose

`B=PAP`, `K_+=QAP`, `K_-=QA^dagger P`.

Shorted/principal-angle geometry is necessary: omitting it gives an explicit false observable Fisher bound.

Second-order positivity supplies one shared kernel-curvature resource

`Z_+ + Z_- <= C_Delta`.

The exact induced allocation is a one-dimensional variational problem over an SDP value, preventing double charging of the same curvature operator.

### Positive spectral action and curvature geometry — WP13 / WP14

For `G>=0`,

`A_G^(2)=(1/4)Tr(G C_Delta)`.

Restricted endpoint costs charge synthesized Fisher directions, and bilateral costs combine harmonically.

For rank-one overlapping synthesized ranges, the exact allocation is governed by capacities and a principal angle in the **inverse shorted-curvature metric**, not by the ordinary Hilbert-space angle.

### Measurement accessibility — WP15 / WP16

Physical resource, SLD/QFI geometry, and common-record accessible Fisher are distinct layers.

The shared-kernel qutrit has the exact hierarchy

`12 > 43/4 > 55/8`.

For a general maximally mixed rank-`r` support with rank-one kernel,

`sqrt(Tr F_1) <= sqrt(R(B)) + sqrt(r kappa)`,

`kappa=||a||^2+||b||^2+2|a^dagger b|`.

For qutrits `R(B)=4w(B)^2`. A signed three-cycle saturates the universal law at `9`, while another model with the same scalar capacities has ceiling `6`; measurement-layer phase/orientation geometry is irreducible.

### Killed redundant direction — WP17

A generic `exact curvature + its own scalar action` Pareto law is redundant. If `C_Delta` is known, `Tr(GC_Delta)` is derived; if only the scalar action is retained, optimization collapses to WP13. Do not revive this without additional independent physics.

### Autonomous zero-radius action — WP18

For a globally stationary exact exchange

`[H_S,A_nu]=+hbar nu A_nu`,

`[H_C,A_nu]=-hbar nu A_nu`,

clean bilateral boundary synthesis obeys

`A_C^(2)+A_S^(2) >= (hbar nu/4)[Tr F_N/N]`.

One-sided boundary synthesis obeys the stronger

`A_C^(2)+A_S^(2) >= (hbar nu/2)[Tr F_N/N]`.

Both coefficients are exactly sharp in fixed-total-energy shells. Global time-translation asymmetry and signed total-energy curvature vanish in the extremizing families.

### Arbitrary coherent-support autonomous bridge — WP19

Define two-sided shorted pre-existing resources `a_+,a_-` and one combined positive clock+signal endpoint-incidence cost operator `G_CS`.

The **kernel-resolved endpoint-incidence action** is

`A_CS^(2)=(1/4)Tr(G_CS C_Delta)`.

With restricted costs `g_+,g_-`,

`Tr F_N/N`

`<= min{Psi_(a_+)(4A_CS;g_+,g_-),`

`       Psi_(a_-)(4A_CS;g_-,g_+)}`.

This bridges the finite-radius dual-survival and zero-radius dual-synthesis regimes for arbitrary coherent support.

**Interpretive caveat:** outside the clean endpoint case, `A_CS^(2)` is the endpoint incidence of the **kernel curvature**. It is not generally the full endpoint-population Laplacian, signed mean-energy curvature, or total protocol energy.

The WP12 shared-kernel qutrit embeds into one fixed-total-energy clock--signal shell and WP19 reproduces its resource ceiling `12` exactly.

### Multi-gap autonomous spectral-action sum — WP20

For zero-radius pure-boundary modes in one common `C^2` multiparameter family,

`C_Sigma = Q sum_k(partial_(x_k)^2+partial_(y_k)^2)rho Q`

obeys

`C_Sigma >= sum_k[Z_(k,+)+Z_(k,-)]`.

For any positive spectral cost `G`,

`sum_k gamma_k [Tr F_(N,k)/N] <= 4A_(G,Sigma)^(2)`.

In the clean bilateral autonomous case,

`A_(G,Sigma)^(2) >= sum_k (hbar nu_k/4)[Tr F_(N,k)/N]`.

The complete weighted sum is simultaneously sharp with **one common Fourier measurement** in a fixed-total-excitation shell.

## Significance / priority gate after WP20

Read:

`notes/FOUNDATIONAL_SIGNIFICANCE_PRIORITY_GATE_AFTER_WP20.md`.

### Broad novelty claim — FAIL

Do not claim a new resource theory of time, a new Page--Wootters mechanism, a new theory of energetic coherence, or a new general energy-constrained metrology framework.

Major established prior art includes:

- Page--Wootters shared/mutual asymmetry and internal coherence;
- modes of asymmetry / Bohr-mode resource theory;
- QFI as an energetic-coherence resource and formation cost;
- quantitative WAY / conservation-law coherence costs;
- fixed-number relative-phase and multiphase metrology;
- waveform QCRB/Holevo limits;
- total-protocol energy-constrained quantum metrology;
- PSD-cone curvature, singular QFI/Bures geometry, shorted operators, SDP/SOCP duality, and numerical-radius theory.

### Narrow theorem paper — PROVISIONAL PASS

Target only the following falsifiable story:

> A globally stationary relative temporal mode has two complementary resource regimes. Finite-radius information requires two-sided pre-existing spectral survival. Rank-changing zero-radius information requires two-sided positive second-order spectral synthesis action. Both laws are finite-copy and arbitrary-POVM, clean coefficients are sharp in fixed-total-energy shells, arbitrary coherent support requires nontrivial operator geometry, and the boundary law admits a sharp multi-frequency sum.

Targeted searches through 2026-08-23 did not locate a predecessor with this complete operational scope and constants. **Priority remains unverified, not certified.**

### Key nonreductions found in the audit

1. Global asymmetry cannot reproduce WP18 because it is identically zero in the fixed-shell extremizers.
2. Entropy-type Page--Wootters shared asymmetry is nonanalytic at the rank-changing boundary, scaling as `r^2 log(1/r)` rather than carrying the finite WP18 quadratic action coefficient.
3. Quantitative WAY results concern resources for implementing conservation-law-conflicting operations/measurements; WP18's full clock--signal exchange conserves total energy exactly.
4. Chen--Yang (PRL 136, 070801, 2026) constrain total protocol energy, while WP18--WP20 use a local frequency-resolved kinematic endpoint-incidence action.
5. Waveform Holevo theory addresses the statistical measurement layer, while WP18--WP20 constrain the physical state-family resource before measurement optimization.

These distinctions justify further review, not a priority claim.

## Current gate

**Do not create WP21 yet.** The next required work is a dedicated hostile mathematical audit of WP18--WP20 and their dependencies:

1. independently rederive every factor `2` and `4` in the two-quadrature conventions;
2. audit finite-copy scaling rather than inheriting it from earlier work packages;
3. verify the fixed-shell nonlinear extremizers are physical on a genuine open parameter neighborhood;
4. verify WP20's common multiparameter Hessian and frequency sum without hidden double counting;
5. verify WP19's endpoint-incidence interpretation under overlapping endpoint projectors;
6. only after that decide whether manuscript formation should start.

## Validation

Independent validators include the full WP02--WP20 suite, including:

- `numerics/verify_rank_one_kernel_common_record_minkowski.py`
- `numerics/verify_autonomous_dual_synthesis_action_law.py`
- `numerics/verify_noncommuting_autonomous_mixed_resource_action_law.py`
- `numerics/verify_multigap_autonomous_spectral_action_sum_law.py`

## Documentation rule

Every material theorem, failed conjecture, priority collision, or killed direction must be recorded immediately in this directory and reflected in `README.md`, `AGENTS.md`, and `ROADMAP.md`. Do not depend on chat history.
