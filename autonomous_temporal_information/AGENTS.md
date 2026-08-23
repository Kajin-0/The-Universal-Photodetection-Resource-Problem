# AGENTS — Autonomous Temporal Information Law

**Branch:** `agent/autonomous-temporal-information-law`

The frozen Rev11 paper remains on `agent/temporal-information-resource-law` and must not be rewritten absent a concrete defect.

## Mission

Determine the physical resource constraining temporal information when clock/reference, signal, controller, detector, and memory are finite internal systems and no external timing operation is free.

Research is analytical/theoretical, falsification-first, and documentation-first. Standard asymmetry/reference-frame theory, Page--Wootters, numerical-radius/Ando theory, POVM convex duality, shorted operators, SDP/SOCP theory, PSD-cone curvature, rank-changing QFI/Bures geometry, Gill--Massar/Holevo compatibility, and energy-constrained metrology are infrastructure unless a distinct operational temporal-information theorem is isolated.

## Current status

**WP18 — sharp autonomous dual synthesis-action law: analytic PASS and independently validated.**

The central hierarchy is now:

1. finite-radius temporal information -> pre-existing spectral survival;
2. zero-radius temporal information -> second-order kernel spectral synthesis;
3. noncommuting support -> shorted/operator geometry;
4. spectral action -> positive endpoint-cost weighting;
5. common-record accessibility -> separate measurement-compatibility geometry;
6. autonomous exact exchange -> matched resources on both sides of the clock--signal cut in both finite-radius and zero-radius regimes.

## Essential theorem stack

### WP02 / WP03 / WP06

Finite-radius exact-gap law:

`(R_lin^2/4)[Tr F_N/N] <= T(nu)`.

Autonomous exchange:

`(R_lin^2/4)[Tr F_N/N] <= min{T_C(nu),T_S(nu)}`.

### WP04 / WP05

Structured globally stationary retention has exact sine-chain envelopes and sharp near-lossless coefficient `pi` under hard and mean total-energy constraints.

### WP07 / WP08

At `R_lin=0`, one-sided boundary synthesis obeys

`Tr F_N/N <= J <= Delta T_U`.

Orthogonal mode sums admit a positive frequency/energy weighted synthesis budget.

### WP09

Bilateral boundary synthesis obeys

`sqrt[Tr F_N/N] <= sqrt(J_X)+sqrt(J_Y)`.

The factor-two departure from additive endpoint synthesis is exactly sharp.

### WP10

For energy-invariant support and one-sided mixed survival+synthesis,

`Tr F_N/N <= 4T_pre/R_B^2 + Delta T_syn`.

### WP11 / WP12

For arbitrary coherent support use

`B=PAP`, `K_+=QAP`, `K_-=QA^dagger P`.

Shorting/principal-angle geometry is required. Shared kernel curvature satisfies

`Z_+ + Z_- <= C_Delta`.

The exact allocation functional `Phi_a` is a one-dimensional minimization over an SDP value.

### WP13 / WP14

Positive spectral action:

`A_G^(2)=(1/4)Tr(GC_Delta)`.

The pure bilateral effective endpoint price is harmonic.

For rank-one synthesized ranges, the exact allocation geometry is controlled by the principal angle in the inverse shorted-curvature metric, not the ordinary Hilbert-space angle.

### WP15

The shared-kernel qutrit has exact hierarchy

`12 > 43/4 > 55/8`

for physical resource, SLD trace, and accessible one-copy common-record Fisher respectively.

### WP16 — generic rank-one-kernel common-record law

For

`rho0=P/r`, `rank(Q)=1`,

`A=[[B,b],[a^dagger,0]]`,

define

`kappa=||a||^2+||b||^2+2|a^dagger b|`

and support-only common-record optimum `R(B)`.

Then

`boxed: sqrt(Tr F_1)<=sqrt(R(B))+sqrt(r kappa)`.

For qutrits,

`R(B)=4w(B)^2`,

so

`Tr F_1<=[2w(B)+sqrt(2kappa)]^2`.

The signed three-cycle saturates at `9`, whereas naive additivity gives `5`.

A second model with the same two scalar invariants has WP11 ceiling `6`, proving exact accessibility requires additional phase/orientation geometry.

WP16 also gives the exact Fisher-witness dual

`F_CR=inf_Y Tr Y`

subject to

`|<phi|A|phi>|^2<=<phi|rho|phi><phi|Y|phi>`

for all vectors, equivalently a semi-infinite weighted numerical-radius LMI family.

### WP17 — killed Pareto sidequest

If exact `C_Delta` is known, scalar action `Tr(GC_Delta)` is redundant. If only the action is known, optimization over unknown curvature collapses exactly to WP13. Do not invent a generic operator+its-own-action Pareto theorem without an independent physical constraint.

### WP18 — autonomous dual synthesis action

For a globally stationary exact exchange

`[H_S,A_nu]=+hbar nu A_nu`,

`[H_C,A_nu]=-hbar nu A_nu`,

clean zero-radius boundary synthesis obeys, for every finite `N` and arbitrary collective POVM,

`boxed: A_C^(2)+A_S^(2) >= (hbar nu/4)[Tr F_N/N]`

in the bilateral case, where local actions are positive absolute-gap endpoint-curvature costs.

If only one support orientation is synthesized,

`boxed: A_C^(2)+A_S^(2) >= (hbar nu/2)[Tr F_N/N]`.

Both coefficients are exactly sharp.

Bilateral extremizer: the fixed-total-energy shell

`|2,0>, |1,1>, |0,2>`

with baseline `|1,1>` and

`A_nu=c(|0,2><1,1|+|1,1><2,0|)`.

A Fourier measurement gives `Tr F_1=4c^2` and saturates the `hbar nu/4` total action coefficient while global time-translation asymmetry remains identically zero.

Read:
`notes/WP18_AUTONOMOUS_DUAL_SYNTHESIS_ACTION_LAW.md`.

## Current frontier

1. Extend WP18 to arbitrary coherent/noncommuting baseline support using WP11/WP12 geometry on both local Hamiltonians.
2. Determine whether the clock and signal share one tighter joint curvature allocation rather than two separately added local reductions.
3. Derive multi-gap autonomous synthesis-action budgets.
4. Perform a hostile priority/significance audit of WP03+WP18 against relational metrology, quantitative WAY, Page--Wootters, and current energy-constrained metrology.
5. Only then consider a new manuscript.

## Numerical gates

In addition to WP02--WP15 validators, current new gates are:

- `numerics/verify_rank_one_kernel_common_record_minkowski.py`
- `numerics/verify_autonomous_dual_synthesis_action_law.py`

Every nontrivial future theorem must receive an independent validator before being marked PASS.

## Documentation rule

Every material theorem, failed conjecture, priority collision, or killed direction must be recorded immediately in this directory and reflected in `README.md`, `AGENTS.md`, and `ROADMAP.md`. The repository, not chat history, is authoritative.
