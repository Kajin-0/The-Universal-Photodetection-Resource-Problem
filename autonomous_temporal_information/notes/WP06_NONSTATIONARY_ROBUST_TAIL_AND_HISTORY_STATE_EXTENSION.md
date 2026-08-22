# WP06 — Nonstationary robust spectral-tail theorem and extension to pre-existing relational history states

**Date:** 2026-08-22

**Branch:** `agent/autonomous-temporal-information-law`

**Status:** analytic PASS. This removes the separate-local-stationarity assumption from the robust tail theorem and from the relational dual-survival law. Targeted priority audit pending/deepening; priority remains **unverified, not certified**.

## 1. The caveat inherited from WP02/WP03

WP02 originally assumed the baseline `rho` commuted with the Hamiltonian whose Bohr gap defined the temporal tangent. That made

`B=rho^(-1/2) A_nu rho^(-1/2)`

inherit the same gap support and enabled a simple partial-shift argument.

WP03 therefore assumed the autonomous clock--signal baseline was separately stationary under both local Hamiltonians.

That excluded an important autonomous regime: a Page--Wootters/history-type baseline may be globally stationary while already containing relational coherence between local energy sectors.

WP06 shows that this exclusion is unnecessary for the **robust upper-tail law**.

## 2. General baseline and tangent radius

Let `rho` be an arbitrary density operator, not assumed to commute with `H`.

Let `A` be the complex tangent associated with two real quadratures

`D_c=(A+A^dagger)/2`,

`D_s=(A-A^dagger)/(2i)`.

Assume the linear physical tangent radius

`R_lin>0`,

meaning

`rho+eps_c D_c+eps_s D_s >=0`

for every `eps_c^2+eps_s^2<=R_lin^2`.

Positive radius implies the tangent cannot connect the support of `rho` to its kernel: if `P=supp(rho)`, then

`A=PAP`.

On the support define

`B=rho^(-1/2) A rho^(-1/2)`.

Exactly as in WP02, congruence of the tangent disk with

`I+(beta B+beta^*B^dagger)/2`

implies

`R_lin=1/w(B)`.

Therefore

`||B||<=2/R_lin`.

No stationarity assumption is used in this step.

## 3. Weighted Cauchy--Schwarz bound for an arbitrary POVM

For any POVM effect `M_y`, define

`p_y=Tr(rho M_y)`,

`z_y=Tr(A M_y)`.

Set

`X=M_y^(1/2) rho^(1/2)`,

`Y=M_y^(1/2) A rho^(+1/2)`,

where `rho^+` is the Moore--Penrose inverse on the support.

Because `A=PAP`,

`Tr(X^dagger Y)=Tr(M_y A)=z_y`.

Hilbert--Schmidt Cauchy--Schwarz gives

`|z_y|^2 <= p_y Tr[M_y A rho^+ A^dagger]`.

Thus

`|z_y|^2/p_y <= Tr[M_y A rho^+ A^dagger]`.

Summing all outcomes yields the exact measurement-independent ceiling

> `Tr F_1 <= Tr(A rho^+ A^dagger)`

for the two-quadrature classical Fisher trace in the current normalization.

This intermediate inequality is valid for an arbitrary baseline.

## 4. Tangent robustness controls the weighted tangent operator

Using

`A=rho^(1/2) B rho^(1/2)`,

we obtain

`A rho^+ A^dagger`

`=rho^(1/2) B P B^dagger rho^(1/2)`

`<= ||B||^2 rho`

`<= (4/R_lin^2) rho`.

Again, no commutation between `rho` and `H` is required.

## 5. Upper spectral support recovers the energy tail

Now assume only that the tangent has **upper endpoint support** in an energy tail:

`P_U A=A`,

where `P_U` is any projector. For an exact positive Bohr-gap tangent `nu` of a semibounded Hamiltonian, one may take

`P_U = 1_[E_*+hbar nu,infinity)(H)`.

Define

`X_A=A rho^+ A^dagger`.

Its range lies inside `P_U`, so

`X_A=P_U X_A P_U`.

Combining this support fact with

`X_A<=(4/R_lin^2)rho`

and taking the trace after compression by `P_U` gives

`Tr X_A <= (4/R_lin^2) Tr(P_U rho)`.

Therefore:

> **Nonstationary robust upper-tail theorem, one copy**
>
> `(R_lin^2/4) Tr F_1 <= Tr(P_U rho)`.

For an exact positive gap `nu`,

> `(R_lin^2/4) Tr F_1^(nu) <= T_rho(nu)`
>
> with `T_rho(nu)=Tr[rho 1_[E_*+hbar nu,infinity)(H)]`.

The baseline may have arbitrary coherence between energy sectors.

## 6. Arbitrary finite-copy collective measurements

For `N` independently encoded copies, the complex tangent is

`A_N=sum_j rho^(tensor(j-1)) tensor A tensor rho^(tensor(N-j))`.

The same weighted Cauchy--Schwarz argument gives

`Tr F_N <= Tr(A_N rho_N^+ A_N^dagger)`.

For `j != l`, cross-copy terms factor through

`Tr A * Tr A^dagger=0`

because every state tangent is traceless; in particular any nonzero Bohr mode has zero trace.

Hence

`Tr(A_N rho_N^+ A_N^dagger)`

`=N Tr(A rho^+ A^dagger)`.

Therefore, for every finite `N` and arbitrary entangled collective POVM,

> `(R_lin^2/4)[Tr F_N/N] <= Tr(P_U rho)`.

This is the same per-copy robust tail law as WP02, now without baseline stationarity.

## 7. Energy corollary

For a semibounded Hamiltonian with lower edge `E_*`, an exact `+nu` gap has

`P_U <= 1_[E_*+hbar nu,infinity)(H)`.

Thus

`K_N(nu):=(R_lin^2/4)[Tr F_N^(nu)/N] <= T_rho(nu)`.

If the baseline mean excess energy is finite,

`Ebar+ = Tr[rho(H-E_*)]`,

then

`T_rho(nu)<=Ebar+/(hbar nu)`

and

> `Ebar+ >= hbar nu K_N(nu)`.

The robust energy-frequency-Fisher law therefore survives arbitrary pre-existing energy coherence.

## 8. Relational clock--signal extension

Let `rho_CS` be an arbitrary **globally stationary** clock--signal state,

`[rho_CS,H_C+H_S]=0`,

but do **not** assume

`[rho_CS,H_C]=0` or `[rho_CS,H_S]=0`.

Thus `rho_CS` may already be a relationally coherent Page--Wootters/history state.

Let the parameter tangent exchange a gap:

`[H_S,A_nu]=+hbar nu A_nu`,

`[H_C,A_nu]=-hbar nu A_nu`.

Then the perturbed local experiment remains globally stationary because

`[H_C+H_S,A_nu]=0`.

From the signal viewpoint, `A_nu` has range in the signal upper tail. From the clock viewpoint, `A_nu^dagger` has range in the clock upper tail. The tangent plane and `R_lin` are identical under conjugation.

Therefore the WP03 theorem holds with **no separate-local-stationarity assumption**:

> `K_N(nu) <= min{T_C(nu),T_S(nu)}`
>
> for any finite `N` and arbitrary collective POVM,

where the tails are computed from the local energy spectral projectors in the possibly coherent joint baseline.

Consequently

`Ebar_C^+ + Ebar_S^+ >= 2 hbar nu K_N(nu)`

continues to hold for pre-existing relational history states.

## 9. Conceptual consequence

This closes an important loophole in the autonomous program.

A pre-existing quantum clock can carry relational coherence before the unknown temporal parameter arrives. That coherence can improve ordinary Fisher sensitivity. But once performance is weighted by the physical tangent radius, the exact high-frequency component still requires sufficient upper energy population on **both** sides of the autonomous relation.

Thus the resource law is not an artifact of starting from an incoherent/dephased clock.

Global stationarity plus internal relational coherence is compatible with the theorem.

## 10. Broader operator statement

The proof actually needs less than an exact Bohr mode.

For one copy, if a traceless complex tangent `A` has positive linear radius and its range is contained in any projector `P`, then

`(R_lin^2/4) Tr F_1 <= Tr(P rho)`.

For finite copies the same per-copy statement holds when the tangent is replicated independently and `Tr A=0`.

The energy-survival theorem is obtained by choosing `P` to be the upper spectral endpoint projector forced by a positive-frequency gap.

This may have applications beyond temporal metrology wherever a tangent is constrained to land in a resource-limited subspace.

## 11. Priority boundary

Weighted tangent operators of the form `A rho^+ A^dagger`, quantum Fisher metrics, numerical radius inequalities, and support-based operator bounds are standard ingredients individually.

Targeted searches to date have not identified the combined theorem

`linear physical tangent radius + arbitrary coherent baseline + arbitrary-POVM Fisher + spectral range support + finite-copy collective extension`.

No priority certification is claimed.

## 12. Next work

The strongest remaining loopholes are now narrower:

1. `R_lin=0` nonlinear synthesis, where second-order curvature supplies the population required for physicality;
2. arbitrary autonomous controls that do not preserve a chosen bare clock--signal energy decomposition;
3. collective-N versions of the sharp structured mean-energy cosine law;
4. many-body/network cut-set generalization of the dual relational survival theorem.

The pre-existing Page--Wootters coherence problem is no longer a blocker for the robust local theorem.
