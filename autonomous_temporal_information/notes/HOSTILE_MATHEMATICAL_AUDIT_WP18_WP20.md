# Hostile mathematical audit — WP18 through WP20

**Date:** 2026-08-23

**Branch:** `agent/autonomous-temporal-information-law`

**Verdict:** **PASS after two targeted corrections/clarifications.** No sharp coefficient, finite-copy scaling, physicality, or common-Hessian defect was found. One harmless sine-coordinate sign mismatch in the WP18 one-sided extremizer was corrected. One definition-quality ambiguity in WP19's endpoint-incidence cost was removed by replacing chosen local endpoint projectors with canonical joint domain/range projectors of the exact-gap tangent.

This audit was required by the post-WP20 publication gate. It is independent of the earlier numerical validators at the level of the analytic derivations below.

## 1. Two-quadrature convention and Fisher normalization

The branch convention is

`D_c=(A+A^dagger)/2`,

`D_s=(A-A^dagger)/(2i)`.

For a POVM effect `M_y`, define

`z_y=Tr(A M_y)`,

`p_y=Tr(rho M_y)`.

Then

`Tr(D_c M_y)=Re z_y`,

`Tr(D_s M_y)=Im z_y`.

Therefore

`Tr F_1`

`=sum_y { [Re z_y]^2+[Im z_y]^2 }/p_y`

`=sum_y |z_y|^2/p_y`.

This confirms that no factor `2` or `4` is missing in the measurement-side WP07/WP09/WP18 formulas.

## 2. WP18 finite-copy scaling rederived

In the pure-boundary regime

`PAP=0`, `QAQ=0`,

write

`A=X+Y^dagger`,

`X=AP=QAP`,

`Y=QA^dagger P`.

Both `X` and `Y` are support-to-kernel and have zero trace.

For `N` copies,

`A_N=sum_j rho^(tensor(j-1)) tensor A tensor rho^(tensor(N-j))`.

With `P_N=P^(tensor N)`, the right-supported pieces are sums of single-copy insertions of `X` and `Y`.

Using

`rho rho^+ rho=rho`,

`XP=X`, `YP=Y`,

and `Tr X=Tr Y=0`,

the weighted quadratic forms have no cross-copy terms:

`J_(X,N)=N J_X`,

`J_(Y,N)=N J_Y`.

The weighted score Cauchy--Schwarz inequality and Minkowski therefore give

`boxed: sqrt[Tr F_N/N] <= sqrt(J_X)+sqrt(J_Y)`

for every finite `N` and arbitrary collective POVM.

The one-sided reduction is

`Tr F_N/N<=J_X`.

Thus the WP18 action inequalities legitimately use one-copy endpoint curvature against per-copy collective Fisher information.

## 3. WP18 second-order factors

For one clean endpoint orientation, the two-quadrature PSD-cone curvature theorem gives

`J<=Delta T`.

Defining

`A_X^(2)=(hbar nu/4) Delta T`

therefore gives one local subsystem

`A_X^(2)>=(hbar nu/4)Tr F_N/N`.

Because an autonomous exchange has a matching endpoint on the other subsystem, the one-sided total law is

`boxed: A_C^(2)+A_S^(2)>=(hbar nu/2)Tr F_N/N`.

For bilateral synthesis, WP09 gives

`Tr F_N/N <= (sqrt(Delta T_+)+sqrt(Delta T_-))^2`

and

`(sqrt(a)+sqrt(b))^2<=2(a+b)`.

Hence each subsystem obeys

`A_X^(2)>=(hbar nu/8)Tr F_N/N`,

and the two subsystems give

`boxed: A_C^(2)+A_S^(2)>=(hbar nu/4)Tr F_N/N`.

The factors `1/2` and `1/4` therefore follow uniquely from the branch conventions.

## 4. WP18 exact-family physicality

### Bilateral shell

Use

`|L>=|2,0>`, `|M>=|1,1>`, `|U>=|0,2>`,

`A=c(|U><M|+|M><L|)`.

The family

`|psi(x,y)>`

`=sqrt[1-(c^2/2)(x^2+y^2)]|M>`

` +(c/2)(x+i y)|L>`

` +(c/2)(x-i y)|U>`

is exactly normalized on the open disk

`x^2+y^2<2/c^2`.

Direct differentiation gives exactly the stated `D_c,D_s`.

The entire disk lies in one eigenspace of `H_C+H_S`; global stationarity is exact, not perturbative.

Each local endpoint population is

`c^2(x^2+y^2)/4`,

so every endpoint Laplacian is `c^2`.

The Fourier POVM has baseline probabilities `1/3` and gives

`Tr F_1=4c^2`.

Thus

`A_C^(2)+A_S^(2)=hbar nu c^2=(hbar nu/4)Tr F_1`.

### One-sided shell

For

`A=2c|U><D|`,

the convention-consistent family is

`|psi(x,y)>=sqrt[1-c^2(x^2+y^2)]|D>+c(x-i y)|U>`.

The earlier note used `x+i y`, which gives `partial_y rho=-D_s`. This is merely the coordinate reversal `y->-y`; every Fisher/action value was unchanged. The note and validator have now been corrected.

The family is physical on

`x^2+y^2<1/c^2`,

has endpoint Laplacian `4c^2`, and a fixed equatorial POVM gives `Tr F_1=4c^2`, saturating the total coefficient `hbar nu/2`.

## 5. WP19 canonical endpoint-incidence action

The original WP19 theorem used a sum of four participating local endpoint projectors. The inequality was valid, but broad projector choices could unnecessarily inflate the positive action.

For a single exact exchange mode the canonical objects are

`Pi_out=supp(A A^dagger)`,

`Pi_in=supp(A^dagger A)`.

Exact exchange implies

`[H_C,Pi_out]=[H_S,Pi_out]=0`,

`[H_C,Pi_in]=[H_S,Pi_in]=0`.

They are therefore canonical joint endpoint-role projectors.

Each joint endpoint incidence represents one absolute local gap on the signal and one on the clock. The audited cost operator is

`boxed: G_ex=2 hbar nu Q(Pi_out+Pi_in)Q`.

The audited kernel action is

`A_ex^(2)=(1/4)Tr(G_ex C_Delta)`.

If a state lies in both `Pi_in` and `Pi_out`, it is counted twice because it actually serves two roles in the exchange ladder. This is role multiplicity, not arbitrary projector double counting.

The shared-kernel qutrit has

`Pi_out=diag(0,1,1)`,

`Pi_in=diag(1,1,0)`,

so

`2(Pi_out+Pi_in)=diag(2,4,2)`,

exactly reproducing the original benchmark action operator.

All benchmark numbers remain unchanged:

`a_+=a_-=5/4`,

`g_+=g_-=13 hbar nu/4`,

`4A_ex=247 hbar nu/16`,

and the WP19 envelope is exactly `12`.

## 6. WP20 common Hessian rederived

For one genuine common multiparameter family, define

`C_Sigma=Q sum_k(partial_(x_k)^2+partial_(y_k)^2)rho Q`.

For a single mode,

`K_(k,c)=(X_k+Y_k)/2`,

`K_(k,s)=(X_k-Y_k)/(2i)`.

The two second-order PSD inequalities give

`Q partial_(x_k)^2 rho Q>=2K_(k,c)rho^+K_(k,c)^dagger`,

`Q partial_(y_k)^2 rho Q>=2K_(k,s)rho^+K_(k,s)^dagger`.

Adding them cancels the `X_k/Y_k` cross terms exactly and yields

`C_(Delta,k)>=Z_(k,+)+Z_(k,-)`.

Summing the **operator inequalities before scalarization** gives

`boxed: C_Sigma>=sum_k[Z_(k,+)+Z_(k,-)]`.

No mixed second derivatives are required because `C_Sigma` is the trace of the parameter Hessian over the chosen orthonormal coordinate directions.

## 7. WP20 general positive-cost theorem

For any one positive kernel operator `G`,

`4A_(G,Sigma)^(2)=Tr(G C_Sigma)`

`>=sum_k[Tr(GZ_(k,+))+Tr(GZ_(k,-))]`.

Let `g_(k,+/-)` be the minimum restricted costs on the corresponding ranges.

Modewise Minkowski plus weighted Cauchy--Schwarz gives

`gamma_k Tr F_(N,k)/N`

`<=g_(k,+)J_(k,+)+g_(k,-)J_(k,-)`,

where bilateral `gamma_k` is the harmonic cost and a one-sided `gamma_k` is the single orientation cost.

Summing gives

`boxed: sum_k gamma_k Tr F_(N,k)/N <=4A_(G,Sigma)^(2)`.

The finite-copy validity follows modewise from the audited WP18/WP09 scaling and does not require a common optimal measurement.

## 8. WP20 exact fixed-shell common family

In the shell

`|n>=|m-n>_C|m+n>_S`, `n=-m,...,m`,

use baseline `|0>` and

`A_k=c_k(|k><0|+|0><-k|)`.

The exact family

`|psi>`

`=sqrt[1-(1/2)sum_k c_k^2(x_k^2+y_k^2)]|0>`

` +sum_k(c_k/2)(x_k+i y_k)|-k>`

` +sum_k(c_k/2)(x_k-i y_k)|k>`

is physical on the open ellipsoid

`(1/2)sum_k c_k^2(x_k^2+y_k^2)<1`.

It is globally stationary everywhere because the entire shell has one total energy.

Direct differentiation gives the stated `A_k` convention exactly.

The kernel Hessian is

`boxed: C_Sigma=sum_k c_k^2(|-k><-k|+|k><k|)`.

The strengthened validator now reconstructs this matrix by finite differences of the actual nonlinear family rather than inserting it by hand.

## 9. Full Fourier Fisher matrix

Let `d=2m+1` and

`|v_j>=(1/sqrt(d))sum_(n=-m)^m e^(i n phi_j)|n>`,

`phi_j=2pi j/d`.

At baseline, `p_j=1/d`.

For mode `k`,

`z_(j,k)=<v_j|A_k|v_j>=(2c_k/d)e^(-ik phi_j)`.

Hence the cosine and sine score components are discrete harmonics.

Because `1<=k,l<=m` and `d=2m+1`, discrete Fourier orthogonality gives

`sum_j cos(k phi_j)cos(l phi_j)=(d/2)delta_(kl)`,

`sum_j sin(k phi_j)sin(l phi_j)=(d/2)delta_(kl)`,

`sum_j cos(k phi_j)sin(l phi_j)=0`.

Therefore the **complete** common-record Fisher matrix is block diagonal:

`F_(x_k x_l)=2c_k^2 delta_(kl)`,

`F_(y_k y_l)=2c_k^2 delta_(kl)`,

`F_(x_k y_l)=0`.

Thus

`Tr F_(1,k)=4c_k^2`

for every mode simultaneously.

The strengthened validator now checks this full matrix, not only the traces.

## 10. Frequency cost and overlap audit

In the clean star-shell extremizer the mode endpoint ranges `|+k>` and `|-k>` are mutually distinct, so the positive operator

`G=2 hbar omega0 sum_(n!=0)|n| |n><n|`

assigns exactly

`2hbar nu_k`

to each orientation of mode `k`.

Therefore the harmonic mode price is `hbar nu_k`, and

`A_(G,Sigma)^(2)=sum_k hbar nu_k c_k^2`

while

`sum_k(hbar nu_k/4)Tr F_(1,k)=sum_k hbar nu_k c_k^2`.

The full weighted sum is exactly saturated.

For **overlapping mode ranges in a general model**, there is no claim that a simple sum of mode-labelled endpoint projectors is a unique physical action. WP20's general theorem intentionally begins with one supplied positive operator `G`; target frequency weights require a feasible operator-design problem. A minimal feasible `G` may be found by the stated SDP. The simple frequency-diagonal interpretation is claimed sharply only in the clean mode-separated geometry.

This resolves the potential multi-gap double-counting objection.

## 11. Final audit verdict

### Defects found

1. **WP18 one-sided sine-coordinate sign:** corrected. No theorem value changed.
2. **WP19 endpoint-cost projector choice:** canonicalized using `supp(AA^dagger)` and `supp(A^dagger A)`. No theorem value changed.

### Defects not found

No error was found in:

- the WP18 bilateral or one-sided coefficients;
- finite-copy normalization by `N`;
- fixed-shell physicality or global stationarity;
- the WP18 sharp measurements;
- the WP19 shared-curvature action inequality;
- the qutrit resource value `12`;
- the WP20 shared-Hessian operator inequality;
- the clean frequency-weighted coefficient;
- simultaneous common-record saturation of all WP20 mode blocks.

### Gate

**HOSTILE MATHEMATICAL GATE: PASS.**

The branch is now mathematically ready to freeze a minimal publication theorem stack, subject still to ordinary peer review and the explicitly unverified priority status.
