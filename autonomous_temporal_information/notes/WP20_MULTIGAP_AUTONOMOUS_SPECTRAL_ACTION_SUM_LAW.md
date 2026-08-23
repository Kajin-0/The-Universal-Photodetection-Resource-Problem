# WP20 — Multi-gap autonomous spectral-action sum law with a common sharp readout

**Date:** 2026-08-22

**Branch:** `agent/autonomous-temporal-information-law`

**Status:** analytic PASS for finite collections of zero-radius pure-boundary exact exchange modes in one `C^2` multiparameter family. The theorem charges all frequencies against one total kernel Hessian and one positive spectral-cost operator. It holds for arbitrary finite-copy collective measurements and, in particular, for one common record across all modes. A fixed-total-energy exchange shell with a single discrete-Fourier measurement simultaneously saturates every frequency block and the complete weighted sum. Generic multiparameter phase estimation, Fourier phase measurements, PSD-cone curvature, and waveform Fisher bounds are prior art. Candidate novelty is restricted to the frequency-resolved **autonomous rank-changing spectral-action sum law** and its simultaneous sharpness in a globally stationary family. Priority remains **unverified, not certified**.

## 1. Multi-gap globally stationary family

Let a finite set of positive exchange frequencies be indexed by `k in K`.

For each mode let the complex tangent `A_k` satisfy

`[H_S,A_k]=+hbar nu_k A_k`,

`[H_C,A_k]=-hbar nu_k A_k`.

Hence

`[H_C+H_S,A_k]=0`.

Let

`P=supp(rho0)`, `Q=I-P`.

Assume a genuine multiparameter `C^2` family

`rho({x_k,y_k})`

with complex tangent convention

`D_(k,c)=(A_k+A_k^dagger)/2`,

`D_(k,s)=(A_k-A_k^dagger)/(2i)`.

WP20 treats the pure boundary regime

`P A_k P=0`

for every mode. First-order positivity also gives

`Q A_k Q=0`.

Define

`X_k=A_k P`,

`Y_k=Q A_k^dagger P`,

so

`A_k=X_k+Y_k^dagger`.

Set

`Z_(k,+)=X_k rho0^+ X_k^dagger`,

`Z_(k,-)=Y_k rho0^+ Y_k^dagger`,

`J_(k,+)=Tr Z_(k,+)`,

`J_(k,-)=Tr Z_(k,-)`.

## 2. One total kernel Hessian controls all modes

Define the total parameter-space Laplacian of the kernel block

> `C_Sigma`
>
> `=Q sum_k [partial_(x_k)^2 rho + partial_(y_k)^2 rho] Q`
>
> at the common baseline point.

For each individual real coordinate, second-order PSD-cone geometry gives

`Q partial_(x_k)^2 rho Q >= 2 K_(k,c) rho0^+ K_(k,c)^dagger`,

`Q partial_(y_k)^2 rho Q >= 2 K_(k,s) rho0^+ K_(k,s)^dagger`,

where

`K_(k,c)=Q D_(k,c) P=(X_k+Y_k)/2`,

`K_(k,s)=Q D_(k,s) P=(X_k-Y_k)/(2i)`.

The cross terms cancel exactly:

`2[K_(k,c)rho0^+K_(k,c)^dagger`

` +K_(k,s)rho0^+K_(k,s)^dagger]`

`=Z_(k,+)+Z_(k,-)`.

Therefore modewise

`C_(Delta,k)>=Z_(k,+)+Z_(k,-)`

and, summing over all modes,

> **Shared multi-gap curvature law**
>
> `boxed: C_Sigma >= sum_k [Z_(k,+)+Z_(k,-)]`.

This is stronger bookkeeping than introducing unrelated curvature budgets for each frequency: every mode is charged against one positive total Hessian of the actual multiparameter family.

## 3. One positive spectral-cost operator

Let `G>=0` be any positive operator on the global kernel space.

Define the total synthesis action

> `A_G,Sigma^(2)=(1/4)Tr(G C_Sigma)`.

For each nonzero synthesized range

`R_(k,+)=supp Z_(k,+)`,

`R_(k,-)=supp Z_(k,-)`,

define restricted costs

`g_(k,+)=lambda_min[R_(k,+) G R_(k,+) |_(R_(k,+))]`,

`g_(k,-)=lambda_min[R_(k,-) G R_(k,-) |_(R_(k,-))]`.

Then positivity gives

`4A_G,Sigma^(2)`

`>=sum_k {Tr(G Z_(k,+))+Tr(G Z_(k,-))}`

`>=sum_k [g_(k,+)J_(k,+)+g_(k,-)J_(k,-)]`.

Thus one cost operator prices the complete frequency family without charging `C_Sigma` separately mode by mode.

## 4. Modewise arbitrary-POVM Fisher geometry

For each mode and every finite `N`, WP09 gives

`sqrt[Tr F_(N,k)/N]`

`<=sqrt(J_(k,+))+sqrt(J_(k,-))`.

This holds for an arbitrary collective POVM on the `N` copies.

It therefore holds if every mode is allowed a different optimal POVM, and a fortiori if all Fisher blocks come from one fixed common measurement record.

For a bilateral mode with both restricted costs positive, weighted Cauchy--Schwarz gives

`[sqrt(J_+)+sqrt(J_-)]^2`

`<=[g_+J_+ + g_-J_-](1/g_+ + 1/g_-)`.

Define the harmonic mode cost

> `g_(k,parallel)`
>
> `=(1/g_(k,+)+1/g_(k,-))^(-1)`.

Then

`g_(k,parallel) Tr F_(N,k)/N`

`<=g_(k,+)J_(k,+)+g_(k,-)J_(k,-)`.

For a one-sided mode, define its effective cost simply as the cost of its nonzero orientation.

## 5. Multi-gap spectral-action theorem

Summing the modewise Fisher inequalities and using the shared curvature law gives:

> **Multi-gap autonomous spectral-action sum law**
>
> `boxed: sum_k gamma_k [Tr F_(N,k)/N]`
>
> `<=4 A_G,Sigma^(2)`,

where

- `gamma_k=g_(k,parallel)` for bilateral synthesis;
- `gamma_k=g_(k,+)` for plus-only synthesis;
- `gamma_k=g_(k,-)` for minus-only synthesis.

The theorem remains valid when the `F_(N,k)` come from one and the same common collective POVM.

If some nonzero synthesized orientation has zero restricted cost under `G`, no finite positive `gamma_k` follows from that cost operator; this is the same null-direction obstruction as WP13.

## 6. Target-weight design form

Suppose one wants a prescribed positive Fisher weight `w_k` for each mode.

Any `G>=0` satisfying

`gamma_k>=w_k`

for all modes immediately gives

> `sum_k w_k Tr F_(N,k)/N <= Tr(G C_Sigma)`.

Thus the choice of spectral action can itself be formulated as an operator-design problem: choose the smallest positive `G` whose compressions give the desired harmonic mode prices.

A simple sufficient condition for bilateral mode `k` is

`R_(k,+) G R_(k,+)>=2w_k R_(k,+)`,

`R_(k,-) G R_(k,-)>=2w_k R_(k,-)`,

because equal orientation prices `2w_k` have harmonic cost `w_k`.

For fixed target weights and fixed ranges, minimizing `Tr(G C_Sigma)` under these linear matrix inequalities is an SDP. The SDP machinery itself is standard and is not claimed as new.

## 7. Clean autonomous frequency weighting

In a clean mode-separated exchange geometry, suppose each bilateral mode `k` lands in two orthogonal endpoint sectors and each endpoint incidence costs

- `hbar nu_k` on the signal;
- `hbar nu_k` on the clock.

Choose `G` so that it acts as

`2 hbar nu_k I`

on each of the two synthesized ranges of mode `k`.

Then

`g_(k,+)=g_(k,-)=2 hbar nu_k`

and therefore

`gamma_k=hbar nu_k`.

The theorem becomes

> **Clean bilateral frequency-weighted law**
>
> `boxed: sum_k hbar nu_k [Tr F_(N,k)/N]`
>
> `<=4 A_G,Sigma^(2)`.

Equivalently,

> `boxed: A_G,Sigma^(2)`
>
> `>=sum_k (hbar nu_k/4)[Tr F_(N,k)/N]`.

This is the multi-gap autonomous analogue of WP08, now counting the matched clock+signal exchange action.

## 8. Simultaneously sharp fixed-total-energy shell

The clean sum coefficient is exactly sharp with **one common measurement**.

Take equally spaced local Hamiltonians

`H_C=hbar omega0 N_C`,

`H_S=hbar omega0 N_S`.

Fix an integer `m>=1` and work inside the total-excitation shell

`N_C+N_S=2m`.

Define the orthonormal shell basis

> `|n>:=|m-n>_C |m+n>_S`,
>
> `n=-m,...,m`.

Every basis vector has total energy

`2m hbar omega0`.

Choose baseline

`rho0=|0><0|`.

For each `k=1,...,m`, let

> `A_k=c_k(|k><0|+|0><-k|)`.

Then

`[H_S,A_k]=+hbar k omega0 A_k`,

`[H_C,A_k]=-hbar k omega0 A_k`.

Thus

`nu_k=k omega0`.

### Exact common nonlinear family

Define

`|psi({x_k,y_k})>`

`=sqrt[1-(1/2)sum_k c_k^2(x_k^2+y_k^2)] |0>`

` +sum_k (c_k/2)(x_k+i y_k)|-k>`

` +sum_k (c_k/2)(x_k-i y_k)|k>`.

For a sufficiently small parameter ball this is exactly normalized and physical.

It remains inside one total-energy eigenspace for every parameter value, so global time-translation asymmetry is identically zero.

For mode `k`, the two endpoint populations are

`c_k^2(x_k^2+y_k^2)/4`,

so their Laplacians are both `c_k^2`.

The total kernel Hessian is

> `C_Sigma=sum_k c_k^2(|-k><-k|+|k><k|)`.

Choose

> `G=2 hbar omega0 sum_(n!=0) |n| |n><n|`.

Then each endpoint of mode `k` has combined clock+signal cost

`2 hbar k omega0=2 hbar nu_k`.

Therefore

`A_G,Sigma^(2)`

`=(1/4)Tr(G C_Sigma)`

`=sum_k hbar nu_k c_k^2`.

## 9. One Fourier readout saturates every gap simultaneously

Let

`d=2m+1`

and define the discrete Fourier basis

> `|v_j>=(1/sqrt(d)) sum_(n=-m)^m e^(i n phi_j)|n>`,
>
> `phi_j=2 pi j/d`, `j=0,...,d-1`.

At the baseline,

`p_j=|<v_j|0>|^2=1/d`.

For every mode `k`,

`<v_j|A_k|v_j>`

`=(2c_k/d)e^(-i k phi_j)`.

Hence

`|<v_j|A_k|v_j>|^2=4c_k^2/d^2`.

The Fisher trace of mode `k` from this **same fixed Fourier measurement** is

`Tr F_(1,k)`

`=sum_j [4c_k^2/d^2]/(1/d)`

`=4c_k^2`.

Therefore every mode individually saturates its clean bilateral coefficient, and simultaneously

`sum_k (hbar nu_k/4) Tr F_(1,k)`

`=sum_k hbar nu_k c_k^2`

`=A_G,Sigma^(2)`.

Thus:

> `boxed: A_G,Sigma^(2)`
>
> `=sum_k (hbar nu_k/4)Tr F_(1,k)`

for one common measurement.

No multiparameter incompatibility penalty appears in this extremizer.

## 10. Why this is stronger than a list of modewise examples

The sharp construction is one physical multiparameter family, one baseline, one total-energy shell, and one measurement.

All frequencies are present simultaneously and the same measurement saturates all Fisher blocks.

Therefore the weighted sum coefficient cannot be improved by invoking common-record incompatibility.

The theorem is still local in parameter space and should not be confused with a finite-amplitude waveform-capacity theorem.

## 11. Relation to WP03, WP08, WP18, and WP19

- WP03: finite-radius autonomous temporal modes are charged by two-sided pre-existing survival.
- WP08: zero-radius one-sided modes have a frequency-weighted quadratic synthesis budget.
- WP18: one zero-radius autonomous exchange mode requires matched two-sided action.
- WP19: arbitrary coherent support mixes finite-radius survival and synthesis action for one exact exchange mode.
- WP20: multiple zero-radius autonomous exchange modes share one total kernel Hessian and obey a sharp frequency-weighted action sum.

This completes the clean multi-frequency corner of the local resource hierarchy.

## 12. Prior-art boundary

Do not claim novelty for:

- multiparameter phase estimation;
- discrete Fourier/covariant phase measurements;
- fixed-total-number relative-phase interferometry;
- waveform Fisher information;
- positive Hessian/PSD-cone tangent geometry;
- SDP design of positive operator weights.

Candidate novelty is the specific theorem that **rank-changing relative temporal Fisher blocks at multiple exact exchange gaps are jointly bounded by one positive kernel spectral-action budget, with the complete frequency-weighted sum simultaneously saturated in a globally stationary fixed-total-energy family**.

Priority remains unverified.

## 13. Next work

1. hostile prior-art audit against multiparameter fixed-number phase estimation and quantum waveform estimation;
2. determine whether a mixed finite-radius + multi-gap theorem has a useful form or merely sums nonlinear WP19 envelopes;
3. test continuous-mode limits only under explicit convergence assumptions;
4. reassess publication significance of the autonomous theorem chain WP03/WP18--WP20 before creating further work packages.
