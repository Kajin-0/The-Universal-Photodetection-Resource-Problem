# M2 hostile theorem-language and dimensional audit

**Date:** 2026-08-23

**Branch:** `agent/autonomous-temporal-information-law`

## Verdict

The headline coefficients and proof mechanisms survive. The audit found **four statement/scope corrections** that should be made before the M2 sources are treated as referee-facing. None is a theorem failure.

## 1. Finite-dimensional scope must be explicit

WP11 is explicitly a finite-dimensional master theorem. The manuscript uses Moore--Penrose inverses on supports, compression minimum eigenvalues, finite-dimensional shorting constants, and rank-deficient PSD-cone Schur complements without supplying the functional-analytic domain hypotheses needed for arbitrary infinite dimension.

The intended physical program concerns finite internal clock/signal systems, so the safe manuscript scope is:

> Work throughout with finite-dimensional clock and signal Hilbert spaces. Infinite-dimensional extensions require separate domain, closed-range, and spectral-regularity hypotheses and are not claimed.

This does not weaken the intended result.

## 2. Mixed `Psi` theorem needs explicit degenerate-orientation cases

The displayed bilateral WP19 reduction

`Psi_a(e;p,q)`

assumes `p=g_+>0` and `q=g_->0` on **nonzero** synthesized ranges.

The earlier M2 prose said the formula "reduces" when `K_+=K_-=0`, but literally `g_+` and `g_-` are undefined on absent ranges.

Let

`e=4 A_ex^(2)`.

The correct finite-copy arbitrary-POVM specializations from the measurement-side master inequality are:

### Bilateral synthesis

If `J_+,J_->0` and `g_+,g_->0`,

`F/N <= min{Psi_(a_+)(e;g_+,g_-), Psi_(a_-)(e;g_-,g_+)}`.

### Plus-only synthesis (`J_-=0`)

If `g_+>0`,

`F/N <= min{ a_+ + e/g_+, [sqrt(a_-)+sqrt(e/g_+)]^2 }`.

### Minus-only synthesis (`J_+=0`)

If `g_->0`,

`F/N <= min{ [sqrt(a_+)+sqrt(e/g_-)]^2, a_- + e/g_- }`.

### No synthesis

If `J_+=J_-=0`,

`F/N <= min{a_+,a_-}`.

In the clean pure-boundary one-sided limit `a_+=a_-=0`, `g=2 hbar nu`, this gives

`A_ex^(2) >= (hbar nu/2)(F/N)`,

exactly matching WP18.

### Zero-cost obstruction

If a **nonzero** synthesized orientation has restricted price `g=0`, no finite scalar action-only bound can control that orientation. This is the WP13 null-direction obstruction and must be stated explicitly.

## 3. Shorting constants can vanish

For the support-preserving term, a shorting constant such as

`lambda_(S,U)=sup{lambda: P Pi_(S,U) P >= lambda R_B^+}`

may be zero.

If the corresponding internal tangent norm is nonzero, that endpoint does not provide a finite scalar survival ceiling. In formulas, the associated `4T/(R_B^2 lambda)` contribution should be treated as `+infinity` rather than divided by zero. A finite `a_+` or `a_-` can still arise from the opposite local side if its shorting constant is positive.

If `B=0`, set `a_+=a_-=0` directly.

## 4. Multi-gap price must handle null directions

For mode `k`, the harmonic price

`gamma_k=(1/g_(k,+)+1/g_(k,-))^-1`

is a positive information price only when all nonzero synthesized orientations have positive restricted cost.

If a nonzero orientation has `g=0`, set

`gamma_k=0`

in the scalar sum theorem. The resulting mode contribution is deliberately vacuous: the chosen `G` does not charge that information-bearing direction. A different positive cost operator or the full operator-valued curvature must be retained to obtain a nonzero bound.

## 5. Parameter-space metric / dimensional consistency

The two real coordinates `(x,y)` are the physically fixed cosine/sine quadratures of the chosen complex tangent. Multi-gap coordinates `(x_k,y_k)` inherit the direct-sum Euclidean quadrature metric.

The Fisher traces and Hessian traces therefore refer to this fixed metric. No invariance under arbitrary anisotropic reparameterizations is claimed.

Dimensional check:

- `F`: inverse parameter squared;
- `R_lin^2 F`: dimensionless;
- `Delta T`: inverse parameter squared;
- `g`: energy;
- `A^(2)=(1/4)Tr(G C_Delta)`: energy / parameter squared;
- `g F` and `hbar nu F`: energy / parameter squared.

Thus all displayed inequalities are dimensionally homogeneous.

## 6. Other hostile checks passed

- fixed-energy qubit counterexample coefficient `Tr F=4c^2` and `R_lin^2=p(1-p)/c^2`;
- finite-copy weighted-norm scaling by exactly `N`;
- WP07 one-sided coefficient `J<=Delta T`;
- WP09 bilateral Minkowski coefficient;
- WP18 total autonomous coefficients `hbar nu/4` bilateral and `hbar nu/2` one-sided;
- canonical `G_ex=2 hbar nu Q(Pi_out+Pi_in)Q` and qutrit `diag(2,4,2)` benchmark;
- WP20 full Fourier Fisher matrix `F_xx=F_yy=2c_k^2 delta_kl`, cross blocks zero;
- `Psi_a` dimensions and crossover condition `e=a p^2/q`.

## Required source action

Create an audited canonical M2 revision incorporating items 1--5 into both the main theorem language and modular supplement proofs. Do not create a new research WP for these changes.
