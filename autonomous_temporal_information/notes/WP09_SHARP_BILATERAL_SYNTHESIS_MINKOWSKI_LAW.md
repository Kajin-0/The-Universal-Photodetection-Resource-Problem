# WP09 — Sharp bilateral-synthesis Minkowski law and failure of additive endpoint cost

**Date:** 2026-08-22

**Branch:** `agent/autonomous-temporal-information-law`

**Status:** analytic PASS for the measurement-side mixed-orientation bound at arbitrary rank-deficient baselines, arbitrary finite-copy collective POVMs, and for the clean case of two orthogonal baseline-empty endpoint sectors. A three-level exact-gap model proves the coefficient sharp at one copy and disproves the naive additive endpoint-curvature law by a factor of two. Triangle/Minkowski inequalities, Fisher-symmetric measurements, and multiparameter compatibility are prior art; candidate novelty is the temporal-resource interpretation and the identification of a **square-root endpoint geometry** as unavoidable in bilateral spectral synthesis. Priority remains **unverified, not certified**.

## 1. Problem left by WP07/WP08

WP07 solved a one-sided boundary tangent:

`A=P_U A P`,

where the domain lies in the baseline support `P=supp(rho0)` and the range lies in a previously empty endpoint sector.

Then

`Tr F_N/N <= J_U <= Delta T_U`.

But an exact positive-gap operator can also have the opposite support orientation:

- one term raises from a populated lower state into an empty upper state;
- another term raises from an empty lower state into a populated upper state.

Both terms are positive-frequency components of the **same** temporal mode.

The corresponding measurement amplitudes can interfere in a common POVM outcome. Therefore it was not legitimate to assume that the two endpoint synthesis costs simply add at the Fisher-information level.

WP09 determines the sharp universal measurement geometry for this bilateral boundary case.

## 2. General support decomposition of a physical complex tangent

Let `rho0` be an arbitrary density operator with

`P=supp(rho0)`,

`Q=I-P`.

Let `A` be the complex two-quadrature tangent:

`D_c=(A+A^dagger)/2`,

`D_s=(A-A^dagger)/(2i)`.

For a two-sided differentiable physical family, positivity implies

`Q D_c Q=0`,

`Q D_s Q=0`,

and therefore

`Q A Q=0`.

Thus

`A=A P + P A Q`.

Define two operators that are both right-supported on `P`:

`X=A P`,

`Y=Q A^dagger P=(P A Q)^dagger`.

Then

> `A=X+Y^dagger`.

Define the two weighted tangent norms

`J_X=Tr(X rho0^+ X^dagger)`,

`J_Y=Tr(Y rho0^+ Y^dagger)`.

These quantities exist on `supp(rho0)` whenever the corresponding tangent is finite.

## 3. One-copy Minkowski Fisher bound

For a POVM `{M_y}`, define

`p_y=Tr(rho0 M_y)`,

`a_y=Tr(X M_y)`,

`b_y=Tr(Y M_y)`.

Since `M_y` is Hermitian,

`Tr(A M_y)=a_y+b_y^*`.

The two-quadrature Fisher trace is

`Tr F_1=sum_y |a_y+b_y^*|^2/p_y`.

For any right-supported operator `Z=ZP`, weighted Hilbert--Schmidt Cauchy--Schwarz gives

`sum_y |Tr(ZM_y)|^2/p_y <= Tr(Z rho0^+ Z^dagger)`.

Hence the score vectors

`u_y=a_y/sqrt(p_y)`,

`v_y=b_y^*/sqrt(p_y)`

obey

`||u||_2<=sqrt(J_X)`,

`||v||_2<=sqrt(J_Y)`.

By the Hilbert-space triangle inequality,

> **One-copy mixed-support Fisher law**
>
> `boxed: sqrt(Tr F_1) <= sqrt(J_X)+sqrt(J_Y)`.

Equivalently,

> `boxed: Tr F_1 <= (sqrt(J_X)+sqrt(J_Y))^2`.

The cross term is physical. It cannot generally be removed.

## 4. Arbitrary finite-copy collective extension

For `N` independently encoded copies,

`rho_N=rho0^(tensor N)`

and

`A_N=sum_(j=1)^N rho0^(tensor(j-1)) tensor A tensor rho0^(tensor(N-j))`.

Let

`P_N=P^(tensor N)`,

`Q_N=I-P_N`,

`X_N=A_N P_N`,

`Y_N=Q_N A_N^dagger P_N`.

Then

`A_N=X_N+Y_N^dagger`.

Because `Tr A=0` and `Q A Q=0`,

`Tr X=0`.

Also `Tr Y=0` because `Y` is support-to-kernel off diagonal.

The cross-copy terms therefore vanish in the weighted quadratic forms:

`Tr(X_N rho_N^+ X_N^dagger)=N J_X`,

`Tr(Y_N rho_N^+ Y_N^dagger)=N J_Y`.

Applying the one-copy argument to an arbitrary joint POVM on the `N` copies gives

> **Finite-copy collective Minkowski law**
>
> `boxed: sqrt[Tr F_N/N] <= sqrt(J_X)+sqrt(J_Y)`.

Thus

> `boxed: Tr F_N/N <= (sqrt(J_X)+sqrt(J_Y))^2`.

No separability, asymptotic attainability, or SLD assumption is used.

## 5. Clean bilateral endpoint-synthesis specialization

Now impose the resource structure relevant to the zero-radius problem.

Let `P_+` and `P_-` be mutually orthogonal projectors satisfying

`P_+ P=P_- P=0`.

Assume

`X=P_+ X P`,

`Y=P_- Y P`.

Interpret:

- `P_+`: a previously empty **upper** endpoint reached by the positive-frequency tangent;
- `P_-`: a previously empty **lower** endpoint whose conjugate amplitude participates in the same positive-frequency tangent.

Define

`T_+(x,y)=Tr[P_+ rho(x,y)]`,

`T_-(x,y)=Tr[P_- rho(x,y)]`.

The support-to-kernel derivative blocks are

`K_c=Q D_c P=(X+Y)/2`,

`K_s=Q D_s P=(X-Y)/(2i)`.

Because `P_+P_-=0`, projecting the second-order PSD-cone condition onto each endpoint separately gives

`Delta T_+(0)>=J_X`,

`Delta T_-(0)>=J_Y`.

Therefore

> **Bilateral quadratic spectral-synthesis law**
>
> `boxed: sqrt[Tr F_N/N]`
>
> `<= sqrt(J_X)+sqrt(J_Y)`
>
> `<= sqrt[Delta T_+(0)]+sqrt[Delta T_-(0)]`.

Equivalently,

> `boxed: Tr F_N/N`
>
> `<= [sqrt(Delta T_+)+sqrt(Delta T_-)]^2`.

The endpoint synthesis resources combine by **square-root addition**, not ordinary addition.

## 6. Exact three-level positive-gap extremizer

Take a three-level ladder

`H=hbar nu diag(0,1,2)`

with baseline

`rho0=|1><1|`.

The lower and upper endpoint states `|0>` and `|2>` are absent from the baseline.

Choose the exact positive-gap tangent

`A=c(|2><1|+|1><0|)`.

Both terms raise the energy by exactly `hbar nu`.

Here

`X=A P=c|2><1|`,

`Y=Q A^dagger P=c|0><1|`,

so

`J_X=J_Y=c^2`.

### Exact physical nonlinear family

Define

`|psi(x,y)>`

`=sqrt[1-(c^2/2)(x^2+y^2)] |1>`

` +(c/2)(x+i y)|0>`

` +(c/2)(x-i y)|2>`.

For sufficiently small `x,y`, this is an exactly normalized physical state and its complex tangent at the origin is precisely the `A` above.

The endpoint populations are

`T_-=c^2(x^2+y^2)/4`,

`T_+=c^2(x^2+y^2)/4`.

Therefore

`Delta T_-(0)=c^2`,

`Delta T_+(0)=c^2`.

The bilateral bound predicts

`Tr F_1 <= (c+c)^2=4c^2`.

## 7. Three-outcome Fourier measurement saturates the bound

Let

`phi_m=2 pi m/3`, `m=0,1,2`,

and define the orthonormal Fourier basis

`|v_m>=(e^(-i phi_m)|0>+|1>+e^(i phi_m)|2>)/sqrt(3)`.

Measure the projectors

`M_m=|v_m><v_m|`.

At the baseline,

`p_m=1/3`.

Moreover,

`z_m=Tr(A M_m)=2c e^(-i phi_m)/3`.

Hence

`Tr F_1`

`=sum_m |z_m|^2/p_m`

`=4c^2`.

Therefore

> `boxed: Tr F_1=(sqrt(J_X)+sqrt(J_Y))^2`
>
> `=[sqrt(Delta T_+)+sqrt(Delta T_-)]^2`.

The universal Minkowski coefficient is exactly sharp already at one copy.

No finite-copy theorem can improve it without introducing additional structure.

## 8. Naive additive endpoint law is false by exactly a factor of two

For the same extremizer,

`Delta T_+ + Delta T_-=2c^2`.

But the attainable Fisher trace is

`Tr F_1=4c^2`.

Thus the tempting bound

`Tr F <= Delta T_+ + Delta T_-`

is false.

The violation factor is exactly

`4c^2/(2c^2)=2`.

The reason is coherent score interference: the upward-created and downward-created endpoint amplitudes add before the modulus square in each measurement outcome.

This resolves the principal uncertainty identified after WP08:

> a universal mixed-endpoint scalar law cannot combine bilateral synthesis costs by ordinary addition.

## 9. Equal-gap synthesis-action corollary

Define the positive bilateral gap-weighted synthesis resource

`E_bi,syn^(2):=(hbar nu/4)[Delta T_+ + Delta T_-]`.

From

`(sqrt(a)+sqrt(b))^2 <= 2(a+b)`,

one obtains

> `Tr F_N/N <= 2[Delta T_+ + Delta T_-]`.

Therefore

> **Equal-gap bilateral energy/action law**
>
> `boxed: E_bi,syn^(2) >= (hbar nu/8)[Tr F_N/N]`.

The symmetric three-level extremizer saturates this coefficient exactly.

This is a **positive spectral-synthesis action** based on absolute endpoint-gap weights. It should not be confused with signed total mean-energy curvature: populating the lower endpoint can reduce the system's ordinary mean energy while still requiring a physical synthesis process and, in an autonomous exchange setting, a compensating resource elsewhere.

The unilateral WP07 coefficient is `hbar nu/4`; bilateral coherent synthesis reduces the best universal coefficient to `hbar nu/8` because two endpoint amplitudes can interfere constructively.

## 10. Unequal positive endpoint costs

Let the two synthesized endpoint sectors carry arbitrary positive resource costs `epsilon_+` and `epsilon_-` per unit quadratic population and define

`E_syn=(1/4)[epsilon_+ Delta T_+ + epsilon_- Delta T_-]`.

Weighted Cauchy--Schwarz gives

`[sqrt(Delta T_+)+sqrt(Delta T_-)]^2`

`<= [epsilon_+ Delta T_+ + epsilon_- Delta T_-]`

`   x (1/epsilon_+ + 1/epsilon_-)`.

Hence

> `E_syn >= (epsilon_parallel/4)[Tr F_N/N]`,

where

> `epsilon_parallel := (1/epsilon_+ + 1/epsilon_-)^(-1)`.

The effective cost combines harmonically, exactly because the score amplitudes combine linearly before squaring.

This is a resource-weighting identity, not an assertion that ordinary subsystem energies always supply positive `epsilon_-` for a lower spectral endpoint.

## 11. Prior-art boundary

Do not claim novelty for:

- the triangle/Minkowski inequality;
- Hilbert--Schmidt Cauchy--Schwarz;
- multiparameter measurement compatibility;
- Fisher-symmetric or locally informationally complete measurements for pure states;
- Fourier-basis qutrit measurements;
- PSD-cone second-order geometry.

There is established literature on Fisher-symmetric measurements for local pure-state estimation and on compatibility conditions in multiparameter quantum metrology. The qutrit Fourier POVM is only an explicit extremizer for the present resource inequality, not a new measurement principle.

Targeted searches have not surfaced the specific statement that **oppositely oriented baseline-empty endpoints of one exact temporal gap obey a sharp square-root synthesis law and invalidate additive spectral-synthesis accounting by factor two**. This remains a candidate contribution, not a certified priority claim.

## 12. Consequence for the grand program

The resource geometry is now more structured than the earlier two-regime summary suggested.

### One-sided pre-existing tangent

`robust Fisher <= zeroth-order spectral survival`.

### One-sided boundary synthesis

`Fisher <= second-order endpoint synthesis`.

### Bilateral boundary synthesis

`sqrt(Fisher) <= sqrt(upper synthesis)+sqrt(lower synthesis)`.

Thus the natural resource composition law changes when two coherent endpoint pathways feed the same temporal score.

This is not a nuisance of the proof. The three-level exact-gap extremizer shows it is physically sharp.

## 13. What remains open

WP09 resolves the **bilateral zero-radius** cross-term problem but not the fully mixed finite-radius/boundary problem.

The main remaining target is now narrower:

> combine a genuinely pre-existing finite-radius exact-gap component with one or two boundary-synthesis components when the baseline support does not commute with the Hamiltonian/resource endpoint projector.

Key issues:

1. support projection of an exact-gap operator need not preserve the exact-gap property for a coherent baseline;
2. the in-support and out-of-support pieces can be geometrically locked by principal angles between baseline support and energy endpoint subspaces;
3. a universal theorem may require a matrix/shorted-operator resource rather than a scalar sum;
4. any proposed law must reduce to WP06, WP07, and the sharp WP09 Minkowski coefficient in their respective limits.

That is now the highest-value unresolved mathematical problem.
