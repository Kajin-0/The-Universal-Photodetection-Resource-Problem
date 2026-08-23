# WP13 — Positive spectral-action allocation law

**Date:** 2026-08-22

**Branch:** `agent/autonomous-temporal-information-law`

**Status:** analytic PASS for the sharp scalar consequence of a single positive spectral-cost operator applied to the WP12 shared kernel curvature. The resulting action-budget envelope is closed form, finite-copy and arbitrary-POVM through the inherited WP11 measurement theorem, and physically sharp in the clean bilateral exact-gap family. Generic attainability with a nonzero internal component is not claimed. Energy-constrained quantum metrology, semidefinite resource optimization, weighted Cauchy--Schwarz, and harmonic-cost formulas are prior art ingredients; the candidate contribution is the frequency-resolved rank-changing temporal-information synthesis law and its exact connection to WP07--WP13. Priority remains **unverified, not certified**.

## 1. Problem left by WP12

WP12 retained the exact shared second-order kernel curvature

`C_Delta >= Z_+ + Z_-`

and removed the double counting caused by charging the same curvature independently to the two synthesized temporal orientations.

Its resource, however, was still the unweighted positive operator `C_Delta`.

The next question is whether the same operator allocation can be priced by a **positive spectral energy/action** without reverting to two independent endpoint curvature charges.

The answer is yes if one uses one positive cost operator on the kernel.

## 2. Positive spectral cost operator

Let

`P=supp(rho0)`, `Q=I-P`.

For an exact positive temporal gap, let `Pi_U,Pi_D` denote the participating upper and lower energy endpoint projectors as in WP11.

Their kernel contractions are

`W_U=Q Pi_U Q`,

`W_D=Q Pi_D Q`.

Choose arbitrary positive endpoint prices `epsilon_U,epsilon_D>0` and define

> `G = epsilon_U W_U + epsilon_D W_D`
>
> `  = Q(epsilon_U Pi_U + epsilon_D Pi_D)Q`.

More generally, every theorem below holds for any positive operator `G>=0` acting on `Q`.

Define the quadratic spectral synthesis action

> `A_G^(2) := (1/4) Tr(G C_Delta)`.

Because both the coefficient and the cost operator are positive, this is nonnegative even when one of the two temporal orientations corresponds to a lower ordinary subsystem-energy endpoint.

For a symmetric exact-gap resource one natural choice is

`epsilon_U=epsilon_D=hbar nu`,

so

> `G_nu = hbar nu Q(Pi_U+Pi_D)Q`.

This is a positive **transition-gap action**, not signed subsystem mean energy.

## 3. Shared curvature is charged only once

WP12 gives

`C_Delta >= Z_+ + Z_-`,

where

`Z_+=K_+ rho0^+ K_+^dagger`,

`Z_-=K_- rho0^+ K_-^dagger`.

Since `G>=0`,

`Tr(G C_Delta)`

`>= Tr[G(Z_++Z_-)]`

`= Tr(G Z_+) + Tr(G Z_-)`.

Therefore

> `boxed: 4 A_G^(2) >= Tr(G Z_+) + Tr(G Z_-)`.

Unlike the separate WP11 quantities `Gamma_U` and `Gamma_D`, this expression cannot count the same curvature operator twice: there is one `G` and one `C_Delta`.

## 4. Exact restricted spectral costs

Let

`R_+=supp(Z_+)`,

`R_-=supp(Z_-)`.

Define the exact minimum spectral costs on the information-bearing synthesized ranges

> `g_+ := lambda_min[R_+ G R_+ |_(R_+)]`,
>
> `g_- := lambda_min[R_- G R_- |_(R_-)]`.

Equivalently,

`R_+ G R_+ >= g_+ R_+`,

`R_- G R_- >= g_- R_-`.

Because `Z_+=R_+ Z_+ R_+` and similarly for `Z_-`,

`Tr(G Z_+) >= g_+ Tr Z_+ = g_+ J_+`,

`Tr(G Z_-) >= g_- Tr Z_- = g_- J_-`.

Hence

> **Spectral-action budget**
>
> `boxed: g_+ J_+ + g_- J_- <= 4 A_G^(2)`.

This compression eigenvalue is the exact quantity needed for trace charging. It can be strictly less conservative than demanding a full-space Loewner inequality `G>=gR`, because only the compression of `G` to the range of `Z` enters `Tr(GZ)`.

## 5. Zero-cost obstruction

If `g_+=0` while the `+` synthesized orientation is allowed, then no finite scalar bound on `J_+` can follow from `A_G^(2)` alone.

Indeed, choose a unit vector `|v>` in `R_+` with `<v|G|v>=0`, let

`Z_+=t |v><v|`, `Z_-=0`, `C_Delta=Z_+`.

Then

`A_G^(2)=0`

for every `t`, while

`J_+=t`

is unbounded.

The same holds for `g_-=0`.

Thus positive spectral coverage of every information-bearing synthesized direction is not a technical convenience; it is necessary for an action-only theorem.

## 6. Exact action-budget optimization

Take the upper-oriented WP11 measurement expression

`[sqrt(a+J_+) + sqrt(J_-)]^2`,

where `a>=0` is either the exact internal weighted norm `J_B^+` or any valid resource ceiling on it.

Set

`e := 4 A_G^(2)`,

`p := g_+`,

`q := g_-`,

and assume `p,q>0`.

The sharpest consequence of the scalar action budget alone is

`Psi_a(e;p,q)`

`= max_(j_+,j_->=0)`

`  [sqrt(a+j_+) + sqrt(j_-)]^2`

subject to

`p j_+ + q j_- <= e`.

This is exactly solvable.

The unconstrained weighted-Cauchy equality point is feasible iff

`e >= a p^2/q`.

Therefore

> **Exact spectral-action envelope**
>
> `boxed: Psi_a(e;p,q) =`
>
> `(sqrt(a)+sqrt(e/q))^2`, if `e <= a p^2/q`,
>
> `(e+p a)(1/p+1/q)`, if `e >= a p^2/q`.

At the crossover both formulas and their first derivatives agree.

### Optimal allocations

For the low-action branch,

`j_+*=0`,

`j_-*=e/q`.

For the high-action branch,

`j_+*=[q e-a p^2]/[p(p+q)]`,

`j_-*=p(e+p a)/[q(p+q)]`.

The latter satisfies

`p sqrt(a+j_+*) = q sqrt(j_-*)`,

which is the equality condition for the weighted Cauchy--Schwarz step.

## 7. Variational / conic formulation

The WP12 square-root identity gives

`[sqrt(a+j_+)+sqrt(j_-)]^2`

`= inf_(0<eta<1) [(a+j_+)/eta + j_-/(1-eta)]`.

For fixed `eta`, the energy-weighted linear allocation is

`h^G_(alpha,beta)(e)`

`= max alpha Tr Z_+ + beta Tr Z_-`

subject to

- `Z_+>=0`, `Z_->=0`;
- `Z_+=R_+ Z_+ R_+`, `Z_-=R_- Z_- R_-`;
- `Tr[G(Z_++Z_-)]<=e`.

Its dual uses one scalar multiplier `tau>=0`:

`min tau e`

subject to

`R_+(tau G-alpha I)R_+ >=0`,

`R_-(tau G-beta I)R_- >=0`.

Therefore

`tau*=max{alpha/p,beta/q}`

and

`h^G_(alpha,beta)(e)=e max{alpha/p,beta/q}`.

Consequently

> `boxed: Psi_a(e;p,q)`
>
> `= inf_(0<eta<1) {a/eta`
>
> `+ e max[1/(eta p),1/((1-eta)q)]}`,

whose analytic minimization gives Sec. 6.

Thus the requested energy-weighted allocation SDP collapses to a closed-form one-dimensional problem once only the scalar action `Tr(G C_Delta)` is retained.

## 8. Finite-copy arbitrary-POVM master law

WP11 gives, for every finite `N` and arbitrary joint POVM,

`sqrt[Tr F_N/N]`

`<= min{`

`sqrt(J_B^+ + J_+) + sqrt(J_-),`

`sqrt(J_B^- + J_-) + sqrt(J_+)}`.

Let

`a_U>=J_B^+`,

`a_D>=J_B^-`

be any valid internal resource ceilings, for example the WP11 shorted-endpoint bounds.

Then

> **WP13 spectral-action master law**
>
> `boxed: Tr F_N/N`
>
> `<= min{`
>
> `Psi_(a_U)(4A_G^(2);g_+,g_-),`
>
> `Psi_(a_D)(4A_G^(2);g_-,g_+)}`.

This theorem is finite-copy and arbitrary-POVM because all measurement dependence was removed upstream in WP11.

## 9. Pure synthesis: harmonic endpoint cost

Set `a=0`.

The envelope becomes

> `boxed: Psi_0(e;p,q)=e(1/p+1/q)`.

Define the harmonic effective spectral cost

> `epsilon_parallel := (1/p+1/q)^(-1)`.

Then

> `boxed: A_G^(2) >= (epsilon_parallel/4)[Tr F_N/N]`.

This is the positive spectral-action analogue of WP09's unequal endpoint-cost law, now with the actual noncommuting-support spectral cost operator compressed onto the synthesized information-bearing ranges.

## 10. Clean exact-gap reductions

### One-sided WP07

If only `K_+` is present and the clean synthesized endpoint lies fully in a baseline-empty upper spectral sector, choose

`G=hbar nu R_+`.

Then `g_+=hbar nu` and

`Tr F_N/N <= 4A_G^(2)/(hbar nu)`.

Hence

> `boxed: A_G^(2) >= (hbar nu/4)[Tr F_N/N]`,

which is WP07's sharp energy-weighted synthesis coefficient.

### Bilateral WP09

For clean empty upper/lower endpoint sectors, choose

`G=hbar nu(R_++R_-)`.

Then

`g_+=g_-=hbar nu`.

With `a=0`,

`Tr F_N/N <= 8 A_G^(2)/(hbar nu)`,

so

> `boxed: A_G^(2) >= (hbar nu/8)[Tr F_N/N]`.

The WP09 bilateral factor two is therefore exactly the harmonic combination of two equal spectral costs.

### One-sided mixed WP10

If the support commutes with energy, `K_-=0`, and

`a=4T_pre/R_B^2`,

then

`Tr F_N/N <= a + 4A_G^(2)/(hbar nu)`.

Multiplying by `hbar nu/4` gives

> `boxed: hbar nu T_pre/R_B^2 + A_G^(2)`
>
> `>= (hbar nu/4)[Tr F_N/N]`,

exactly the WP10 action law.

### WP12 shared-subspace crossover

If `R_+=R_-=R` and `G=epsilon R` on that subspace, then

`p=q=epsilon`,

`e=epsilon s`,

where `s` is the available shorted curvature trace.

WP13 reduces to

`Psi_a=(sqrt(a)+sqrt(s))^2` for `s<=a`,

`Psi_a=2(a+s)` for `s>=a`,

exactly the WP12 coincident-subspace formula.

Thus WP12's factor-two crossover is the equal-cost specialization of the spectral-action law.

## 11. Sharp unequal-cost qutrit extremizer

Take

`H=hbar nu diag(0,1,2)`

up to an irrelevant overall scale and baseline

`rho0=|1><1|`.

Choose arbitrary positive synthesized norms `j_+,j_-` and exact positive-gap tangent

`A=sqrt(j_+) |2><1| + sqrt(j_-) |1><0|`.

An exact normalized physical family is

`|psi(x,y)>`

`=sqrt[1-(j_++j_-)(x^2+y^2)/4]|1>`

` +(sqrt(j_-)/2)(x+i y)|0>`

` +(sqrt(j_+)/2)(x-i y)|2>`.

At the origin,

`Z_+=j_+ |2><2|`,

`Z_-=j_- |0><0|`,

and the minimal kernel curvature is

`C_Delta=Z_++Z_-`.

Let the spectral cost operator be

`G=p |2><2| + q |0><0|`,

so

`4A_G^(2)=p j_+ + q j_-`.

Use the three-outcome Fourier measurement

`|v_m>=(e^(-i phi_m)|0>+|1>+e^(i phi_m)|2>)/sqrt(3)`,

`phi_m=2 pi m/3`.

Then

`Tr F_1=(sqrt(j_+)+sqrt(j_-))^2`.

Choose the action-optimal ratio

`j_-/j_+=p^2/q^2`.

The Fourier measurement then attains

> `boxed: Tr F_1`
>
> `=4A_G^(2)(1/p+1/q)`.

Therefore the harmonic action coefficient in Sec. 9 is physically sharp for arbitrary positive endpoint prices, already at one copy and with one fixed three-outcome measurement.

## 12. Noncommuting-support benchmark

Return to WP11's four-level model

`H=hbar omega diag(0,1,2,3)`,

`nu=2omega`,

`rho0=(|0><0|+|r><r|)/2`,

`|r>=(1/2)|2>+(sqrt(3)/2)|3>`,

`A=|2><0|`.

The synthesized range is the kernel direction `|q>` with

`Q Pi_U Q=(3/4)|q><q|`.

For the symmetric gap-action choice

`G_nu=hbar nu Q(Pi_U+Pi_D)Q`,

the lower endpoint contributes zero on this kernel direction and

> `g_+=(3/4)hbar nu`.

With

`J_+=3/2`,

the minimal synthesis action is therefore

`A_G^(2)=(1/4)g_+J_+`.

Using the exact internal ceiling

`a_U=J_B^+=1/2`,

the one-sided WP13 law gives

`Tr F_N/N <= 1/2 + J_+ =2`,

exactly reproducing the WP11 weighted-tangent ceiling without first replacing the spectral contraction by a global scalar Loewner constant.

This illustrates why the restricted compression cost is the natural action quantity.

## 13. Multimode one-sided reduction

Suppose several orthogonal baseline-empty synthesized modes have projectors `R_k`, positive costs `epsilon_k`, weighted tangent operators `Z_k`, and

`C_Delta >= sum_k Z_k`.

Choose

`G=sum_k epsilon_k R_k`.

Then

`Tr(G C_Delta) >= sum_k epsilon_k Tr Z_k`.

Combining with WP08 modewise Fisher bounds gives

`sum_k epsilon_k Tr F_(N,k)/N <= Tr(G C_Delta)`.

With `epsilon_k=hbar nu_k`,

> `boxed: sum_k hbar nu_k Tr F_(N,k)/(4N)`
>
> `<= A_G^(2)`,

recovering WP08 as the one-sided multimode specialization of the operator spectral-action framework.

## 14. Prior-art boundary

Do not claim novelty for:

- energy-constrained quantum metrology in general;
- SDP/conic optimization of metrological resources;
- weighted Cauchy--Schwarz or harmonic-mean effective costs;
- QFI/Fisher bounds under photon-number or mean-energy constraints;
- Holevo waveform-estimation bounds;
- shorted operators or principal-angle compression mathematics.

A particularly relevant recent paper is Longyun Chen and Yuxiang Yang, **Optimal Quantum Metrology under Energy Constraints**, Phys. Rev. Lett. 136, 070801 (2026), DOI `10.1103/6ghs-frtx`, which develops a broad process-level framework in which probe preparation, control, and measurement energy are constrained. That work is prior-art-adjacent and must be treated explicitly in any later manuscript.

Also relevant is the established Holevo treatment of linear waveform estimation, including Phys. Rev. Lett. 132, 130801 (2024).

The candidate contribution here is narrower:

> a rank-changing temporal mode has a positive second-order spectral-action cost obtained by applying one endpoint-cost operator to the shared kernel curvature; the resulting arbitrary-POVM Fisher ceiling is governed by the compressed spectral costs on the synthesized score ranges, with an exactly sharp harmonic bilateral coefficient and exact reductions to the earlier survival/synthesis laws.

Targeted searches have not identified this specific local curvature/action statement. Priority remains **unverified, not certified**.

## 15. Consequence for the program

WP07--WP13 now form one coherent local hierarchy:

- finite-radius information: pre-existing spectral survival x tangent robustness;
- one-sided zero-radius information: positive quadratic spectral synthesis action;
- bilateral zero-radius information: harmonic combination of the two positive endpoint costs;
- noncommuting support: compressed spectral costs encode endpoint/support geometry;
- shared curvature: one positive cost operator prevents double counting;
- multimode one-sided synthesis: the same operator action reduces to the WP08 frequency-weighted sum law.

The scalar energy law is therefore not fundamental by itself. It is a corollary of a positive operator curvature resource plus its spectral cost operator.

## 16. Next work

Highest-value next targets:

1. derive the rank-one `R_+,R_-` WP12 allocation with arbitrary principal angle and fixed `C_Delta` in closed form;
2. determine whether the remaining WP12 `12` versus SLD-QFI `10.75` gap is exactly a Holevo compatibility penalty;
3. lift `G_nu` and the action allocation simultaneously to clock and signal sides of a globally stationary exchange tangent;
4. test covariance-changing Gaussian families against the same positive spectral-action variable;
5. deepen the priority audit against the 2026 energy-constrained metrology literature before manuscript formation.
