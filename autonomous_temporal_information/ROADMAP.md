# Roadmap — Autonomous Temporal Information Law

**Branch:** `agent/autonomous-temporal-information-law`

## Goal

Seek a foundational physical resource principle for temporal information when clock, signal, controller, detector, and memory are finite internal quantum systems. The finished Rev11 random-time law remains frozen on its parent branch.

## Completed foundations

### WP02 / WP03 / WP06 — finite-radius survival and autonomous dual survival — PASS

`(R_lin^2/4)[Tr F_N/N] <= T(nu)`

and for a globally stationary exchange tangent

`(R_lin^2/4)[Tr F_N/N] <= min{T_C(nu),T_S(nu)}`.

### WP04 / WP05 — exact structured autonomous retention — PASS

Hard and mean total-energy constraints have exact sine-chain envelopes and sharp near-lossless coefficient `pi`.

### WP07 / WP08 — zero-radius quadratic synthesis — PASS

One-sided boundary:

`Tr F_N/N <= J <= Delta T_U`.

Orthogonal mode sums admit positive spectral synthesis budgets.

### WP09 — bilateral synthesis — PASS

`sqrt[Tr F_N/N] <= sqrt(J_X)+sqrt(J_Y)`.

The factor-two departure from additive synthesis is exactly sharp.

### WP10 — one-sided mixed survival+synthesis — PASS

For energy-invariant support,

`Tr F_N/N <= 4T_pre/R_B^2 + Delta T_syn`.

### WP11 / WP12 — noncommuting support and exact shared-curvature allocation — PASS

Shorting/principal-angle geometry is necessary. Shared curvature satisfies

`Z_+ + Z_- <= C_Delta`.

The exact allocation is one scalar minimization over an SDP dual.

### WP13 / WP14 — positive spectral action and rank-one curvature geometry — PASS

`A_G^(2)=(1/4)Tr(GC_Delta)`.

Bilateral action costs combine harmonically. Rank-one allocation is controlled by an inverse-curvature principal angle rather than ordinary Hilbert-space overlap.

### WP15 — exact shared-kernel common-record optimum — PASS

Benchmark hierarchy:

`physical resource 12 > SLD trace 43/4 > accessible Fisher 55/8`.

### WP16 — generic rank-one-kernel common-record theorem — PASS

For

`rho0=P/r`, `rank(Q)=1`,

`A=[[B,b],[a^dagger,0]]`,

let

`kappa=||a||^2+||b||^2+2|a^dagger b|`

and `R(B)` be the support-only common-record optimum.

Then

`boxed: sqrt(Tr F_1)<=sqrt(R(B))+sqrt(r kappa)`.

For qutrits,

`R(B)=4w(B)^2`,

so

`Tr F_1<=[2w(B)+sqrt(2kappa)]^2`.

The signed three-cycle saturates at `9`; naive additivity predicts only `5`. A second model with the same scalar invariants has ceiling `6`, proving exact accessibility needs additional phase/orientation geometry.

WP16 also gives the exact common-record Fisher-witness dual and its semi-infinite weighted numerical-radius LMI representation.

### WP17 — operator/action Pareto redundancy — NO-GO

If exact `C_Delta` is known, `Tr(GC_Delta)` is redundant. If only action is known, optimization over unspecified curvature collapses exactly to WP13. Do not pursue a generic operator+its-own-action Pareto theorem without new independent physics.

### WP18 — autonomous dual synthesis-action law — PASS

For a globally stationary exact exchange

`[H_S,A_nu]=+hbar nu A_nu`,

`[H_C,A_nu]=-hbar nu A_nu`,

clean zero-radius boundary synthesis gives

`boxed: A_C^(2)+A_S^(2) >= (hbar nu/4)[Tr F_N/N]`

for bilateral synthesis and

`boxed: A_C^(2)+A_S^(2) >= (hbar nu/2)[Tr F_N/N]`

for one-sided synthesis.

Both coefficients are exactly sharp.

The bilateral extremizer is the fixed-total-energy chain

`|2_C,0_S> <-> |1_C,1_S> <-> |0_C,2_S>`

with a Fourier readout. The entire nonlinear family stays inside one total-energy eigenspace, so global time-translation asymmetry is zero while nonzero relative temporal Fisher information remains.

This closes the principal `R_lin=0` autonomous loophole left by WP03 in the clean boundary regime.

## Current frontier — WP19 and beyond

### A. WP19: noncommuting-support autonomous dual action — highest priority

Remove WP18's clean endpoint assumption.

Use the full exact exchange tangent but allow arbitrary coherent baseline support

`P=supp(rho0)`, `[P,H_C]` and/or `[P,H_S]` nonzero.

Required tasks:

1. apply WP11/WP12 shorted endpoint geometry from the signal Hamiltonian viewpoint;
2. apply the conjugate geometry from the clock viewpoint;
3. determine whether the two local reductions are independent or are coupled through the same global kernel curvature operator;
4. derive the tightest universal two-sided action theorem without double counting shared curvature;
5. preserve WP18 coefficients in the clean limits.

### B. Multi-gap autonomous synthesis-action budget

For exact exchanges at gaps `nu_k`, seek a common positive spectral-action sum law across modes using one common collective record when appropriate.

### C. Measurement-accessibility geometry

WP16 gives a sharp universal regular/singular Minkowski envelope but not an exact formula for every model. The exact missing invariant is phase/orientation geometry. Continue only if it feeds the autonomous theorem or publication story; avoid a detached matrix-analysis sidequest.

### D. Gaussian covariance-changing synthesis

Test whether squeezing/covariance-changing temporal families fit the same survival -> curvature -> action hierarchy.

### E. Deep priority/significance audit

Explicitly compare WP03+WP18 against:

- Page--Wootters and finite relational clocks;
- relative-phase metrology in fixed-number sectors;
- asymmetry/reference-frame resource theory;
- quantitative WAY and energy-conserving measurement bounds;
- Frerot--Roscilde symmetry-sector metrology;
- Chen--Yang 2026 energy-constrained metrology;
- thermodynamic/energy-cost metrology;
- rank-changing QFI and singular Fisher geometry.

Do not claim novelty for any standard ingredient.

## Publication / significance gate

The branch is now closer to a manuscript-worthy theorem family, but do **not** draft yet.

Require:

1. WP19 or a proof that the clean WP18 theorem is the maximal general autonomous statement;
2. hostile mathematical review of WP11--WP18;
3. deep 2025--2026 priority audit;
4. explicit comparison between WP03 finite-radius dual survival and WP18 zero-radius dual synthesis action;
5. a clear statement of what is genuinely new versus standard asymmetry, Page--Wootters, numerical-radius, and SDP machinery.

## Validation

Current validators include all WP02--WP15 scripts plus:

- `numerics/verify_rank_one_kernel_common_record_minkowski.py`
- `numerics/verify_autonomous_dual_synthesis_action_law.py`

Every nontrivial theorem must receive an independent validator before PASS status.

## Documentation discipline

Every material theorem, failed conjecture, priority collision, or killed direction must be recorded immediately and reflected in `README.md`, `AGENTS.md`, and this file. The repository, not chat history, is authoritative.
