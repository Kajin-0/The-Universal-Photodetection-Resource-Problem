# WP8 — Finite-temperature free-energy closure of the Gaussian pointer resource

**Date:** 2026-08-19

## Purpose

WP7 proved that cross-coupling action alone cannot bound coherent-state QFI transfer if the detector can contain arbitrarily strong pre-existing squeezing. It then repaired that loophole using an explicit pointer-energy budget.

This note replaces that ad hoc energy budget by a genuine finite-temperature thermodynamic preparation resource: the detector pointer's nonequilibrium free energy above its thermal reference state.

The result is exact for the single harmonic Gaussian pointer class and gives the first direct UPRP inequality trading

\[
\text{preparation free energy}
+\text{coupling action}
\longrightarrow
\text{electrical QFI transfer}.
\]

---

# 1. Harmonic pointer and thermal reference

Use dimensionless quadratures

\[
[X,P]=i,
\qquad
H_D=\frac{\hbar\omega_D}{2}(X^2+P^2).
\]

Let

\[
\tau_\beta=\frac{e^{-\beta H_D}}{Z_\beta}
\]

be the thermal reference state at inverse temperature `beta`.

Define

\[
\boxed{
a\equiv\frac{\beta\hbar\omega_D}{2}.}
\]

Then

\[
\tau_\beta
=\frac{e^{-a(X^2+P^2)}}{Z_a},
\qquad
Z_a=\frac1{2\sinh a}.
\]

The nonequilibrium free-energy excess is

\[
\boxed{
\Delta F_\beta(\rho)
=F_\beta(\rho)-F_\beta(\tau_\beta)
=k_BT\,D(\rho\|\tau_\beta).
}
\]

Write the dimensionless preparation resource

\[
\boxed{D_0\equiv\beta\Delta F_\beta.}
\]

A theta-independent coherent displacement of the pointer consumes energy but does not change covariance/QFI for a subsequently transferred displacement. Therefore, when minimizing quadrature noise under a free-energy cap, one may center the state without increasing its relative entropy to the centered thermal reference. We hence take zero first moments without loss for this optimization.

---

# 2. Gibbs variational quadrature-noise bound

Quantum relative entropy obeys the Gibbs/Donsker-Varadhan variational inequality

\[
D(\rho\|\tau)
\ge
\operatorname{Tr}(\rho K)
-
\ln\operatorname{Tr}e^{\ln\tau+K}
\]

for any Hermitian `K` for which the exponential is trace class.

Choose

\[
K=-sX^2,
\qquad s>0.
\]

Then

\[
\ln\tau_\beta+K
=-(a+s)X^2-aP^2-\ln Z_a.
\]

The quadratic oscillator

\[
(a+s)X^2+aP^2
\]

has symplectic frequency

\[
y=\sqrt{a(a+s)},
\]

so

\[
\operatorname{Tr}e^{-(a+s)X^2-aP^2}
=\frac1{2\sinh y}.
\]

Therefore

\[
\operatorname{Tr}e^{\ln\tau_\beta-sX^2}
=\frac{\sinh a}{\sinh y}.
\]

The variational inequality becomes

\[
D(\rho\|\tau_\beta)
\ge
-s\langle X^2\rangle_\rho
+
\ln\frac{\sinh y}{\sinh a}.
\]

If

\[
D(\rho\|\tau_\beta)\le D_0,
\]

then

\[
\langle X^2\rangle_\rho
\ge
\frac{
\ln[\sinh\sqrt{a(a+s)}/\sinh a]-D_0
}{s}.
\]

Optimizing over `s>0` yields the state-independent noise floor

\[
\boxed{
v_F(D_0,a)
\equiv
\sup_{s>0}
\frac{
\ln\!\left[
\dfrac{\sinh\sqrt{a(a+s)}}{\sinh a}
\right]-D_0
}{s}.
}
\]

For centered states,

\[
\boxed{\operatorname{Var}(X)\ge v_F(D_0,a).}
\]

Because the thermal reference is phase-rotation invariant, the same bound applies to every quadrature direction. In particular, the smallest covariance eigenvalue of any centered single-mode Gaussian pointer obeys

\[
\boxed{v_{\min}\ge v_F(D_0,a).}
\]

**Status:** PROVED.

---

# 3. Tight parametric optimizer

The variational inequality is saturated by the exponentially tilted state

\[
\boxed{
\rho_s
=\frac{
 e^{-(a+s)X^2-aP^2}
}{Z_s},
\qquad
Z_s=\frac1{2\sinh y},
\qquad
y=\sqrt{a(a+s)}.
}
\]

This is a squeezed thermal Gaussian state.

Its squeezed quadrature variance is

\[
\boxed{
v_x(y)
=\frac{a}{2y}\coth y.
}
\]

Using

\[
s=\frac{y^2-a^2}{a},
\qquad y\ge a,
\]

its relative entropy to the thermal reference is

\[
\boxed{
D(y)
=
\ln\frac{\sinh y}{\sinh a}
-
\frac{y^2-a^2}{2y}\coth y.
}
\]

Thus the optimal noise floor admits the parametric representation:

1. solve
\[
D(y)=D_0,
\qquad y\ge a;
\]
2. then
\[
\boxed{
v_F(D_0,a)=\frac{a}{2y}\coth y.}
\]

At `D_0=0`, `y=a` and the optimizer is the thermal state. Increasing `D_0` increases `y` and decreases the optimally achievable quadrature noise.

For the single-mode Gaussian optimization, this construction is tight: every point on the free-energy/noise frontier is attained by a squeezed thermal state.

**Status:** PROVED for the single-mode Gaussian pointer class.

---

# 4. QFI transfer through a passive coupling

Let the optical source be a coherent displacement family with source quadrature mean

\[
\langle X_F\rangle=\theta,
\]

so

\[
F_{\rm in}=2.
\]

Let a passive beam-splitter-type transfer send displacement probability `tau` into the detector mode. The detector covariance becomes

\[
V_{D,\rm out}
=\frac\tau2 I+(1-\tau)V_D.
\]

The transferred displacement derivative has squared magnitude `tau`.

For a Gaussian family whose parameter occurs only in the mean, the SLD QFI is

\[
F_D=(\partial_\theta d)^T V^{-1}(\partial_\theta d).
\]

Optimally aligning the transferred displacement with the minimum-noise quadrature gives

\[
F_D
\le
\frac{\tau}
{\tau/2+(1-\tau)v_{\min}}.
\]

Using `v_min>=v_F` and `F_in=2`,

\[
\boxed{
\frac{F_D}{F_{\rm in}}
\le
\frac{\tau}
{\tau+2(1-\tau)v_F(D_0,a)}.
}
\]

Any electrical measurement is downstream of the detector state, so

\[
\boxed{
\frac{F_{\rm elec}}{F_{\rm in}}
\le
\frac{\tau}
{\tau+2(1-\tau)v_F(\beta\Delta F_\beta,a)}.
}
\]

For the optimized Gaussian pointer, beam-splitter transfer, and aligned homodyne readout, equality is attained.

**Status:** PROVED and saturable for the single-effective-mode Gaussian pointer class.

---

# 5. Coupling-action + free-energy theorem

WP7 proved for passive linear mode coupling that

\[
\tau\le\sin^2\Gamma,
\qquad
\Gamma=\int_0^t\|V(s)\|_2ds,
\]

for `0<=Gamma<=pi/2`.

The QFI-transfer bound is monotone increasing in `tau`, hence

\[
\boxed{
\frac{F_{\rm elec}}{F_{\rm in}}
\le
\frac{\sin^2\Gamma}
{\sin^2\Gamma
+2\cos^2\Gamma\,v_F(\beta\Delta F_\beta,a)}
}
\]

for `0<=Gamma<=pi/2`.

Equivalently, to achieve target transfer fraction `q`, a necessary condition is

\[
q\le
\frac{\tan^2\Gamma}
{\tan^2\Gamma+2v_F},
\]

so

\[
\boxed{
\Gamma
\ge
\arctan\sqrt{
\frac{2q\,v_F(\beta\Delta F_\beta,a)}{1-q}
}.
}
\]

If `||V(t)||_2<=g_max`, then

\[
\boxed{
t
\ge
\frac1{g_{\max}}
\arctan\sqrt{
\frac{2q\,v_F(\beta\Delta F_\beta,a)}{1-q}
}.
}
\]

This is the current strongest finite-temperature quantum preparation-resource speed theorem in UPRP.

---

# 6. Limiting cases

## 6.1 Zero preparation free energy

For

\[
\Delta F_\beta=0,
\]

the only allowed state on the optimal frontier is the thermal state, `y=a`, giving

\[
\boxed{
v_F(0,a)=\frac12\coth a.}
\]

Therefore

\[
\boxed{
\frac{F_{\rm elec}}{F_{\rm in}}
\le
\frac{\tau}
{\tau+(1-\tau)\coth a}.
}
\]

At zero temperature (`a->infinity`) this reduces to the vacuum/coherent-apparatus result `F_out/F_in<=tau`.

## 6.2 Low-temperature limit

For `a>>1`, take

\[
y=a e^{2r}.
\]

Then `coth y≈1` and

\[
v_F\approx\frac12e^{-2r}.
\]

The relative entropy becomes

\[
D(y)
\approx
2a\sinh^2r.
\]

Since `2a=beta hbar omega_D`,

\[
\Delta F_\beta
\approx
\hbar\omega_D\sinh^2r.
\]

Thus the finite-temperature theorem reduces to the earlier zero-temperature energy-repaired squeezed-vacuum theorem.

## 6.3 Large preparation free energy

At fixed `a` and `D_0>>1`, the optimal parameter satisfies asymptotically

\[
y\sim2D_0
\]

up to subleading logarithmic/constant corrections. Therefore

\[
\boxed{
v_F(D_0,a)
\sim\frac{a}{4D_0}
=\frac{\hbar\omega_D}{8\Delta F_\beta}.}
\]

Hence

\[
2v_F\sim\frac{\hbar\omega_D}{4\Delta F_\beta}.
\]

At weak coupling, maintaining fixed nonzero transfer fraction requires

\[
\Delta F_\beta=\Omega(\Gamma^{-2}),
\]

recovering the same hidden-resource scaling found from the squeezed-pointer counterexample.

## 6.4 High-temperature limit

For `a<<1`, write

\[
y=ak,
\qquad k\ge1.
\]

Using `sinh x≈x` and `coth(ak)≈1/(ak)`,

\[
\boxed{
D_0
\approx
\ln k-rac12(1-k^{-2}),
}
\]

and

\[
\boxed{
v_F
\approx
\frac1{2ak^2}.}
\]

The thermal noise is `v_th≈1/(2a)=k_BT/(hbar omega_D)`, so preparation free energy suppresses the optimized quadrature noise by the factor `k^{-2}` determined implicitly by the first equation.

---

# 7. Why contemporaneous entropy production is insufficient

The resource `Delta F_beta` is a **preparation** resource. A pointer can be squeezed or otherwise prepared before the detection interval. Its preparation cost need not appear in the detector's contemporaneous steady-state entropy-production rate.

Therefore replacing `Delta F_beta` by steady EPR would reintroduce the hidden-resource loophole exposed in WP7.

A resource-complete theorem must distinguish at least:

- stored/prepared nonequilibrium resource in the apparatus;
- cross-coupling strength/action during measurement;
- ongoing dissipative/thermokinetic costs during reset/amplification/readout.

---

# 8. Broader non-Gaussian bound

WP7 also proved for arbitrary detector pointer states under passive linear coupling

\[
\frac{F_{\rm elec}}{F_{\rm in}}
\le
\min\{1,\tau\mathcal R_D\},
\qquad
\mathcal R_D=2\sup_c\operatorname{Var}(P_c).
\]

A relative-entropy variational estimate gives, for a single harmonic mode,

\[
\operatorname{Var}(P)
\le
\inf_{0<s<a}
\frac{
D_0+
\ln\!\left[
\dfrac{\sinh a}{\sinh\sqrt{a(a-s)}}
\right]
}{s},
\]

after centering the state.

This produces a fully non-Gaussian but generally loose free-energy cap on `R_D`.

The tight Gaussian noise-floor theorem above is stronger for Gaussian pointer states because it bounds the directly limiting squeezed quadrature rather than the conjugate-generator variance.

---

# 9. Open non-Gaussian question

The major remaining mathematical question is whether the tight harmonic-denominator structure

\[
\frac{F_{\rm out}}{F_{\rm in}}
\le
\frac{\tau}{\tau+2(1-\tau)v_F}
\]

extends to arbitrary non-Gaussian pointer states under a free-energy constraint.

A promising route is a bosonic Fisher-information/Stam inequality for beam-splitter convolution. However, the established quantum entropy-power literature uses a **divergence-based translation Fisher information**, not automatically the SLD/Bures QFI used in UPRP. These metrics must not be identified without proof.

Relevant primary sources:

- König & Smith, *The entropy power inequality for quantum systems*, IEEE Trans. Inf. Theory 60, 1536 (2014), arXiv:1205.3409: quantum de Bruijn identity with a divergence-based QFI and beam-splitter Fisher-information inequalities.
- De Palma & Trevisan, *The conditional Entropy Power Inequality for bosonic quantum systems*, Commun. Math. Phys. 360, 639 (2018), arXiv:1706.00440: conditional Fisher-information Stam inequality.
- Hiai & Ruskai, *Contraction coefficients for noisy quantum channels*, J. Math. Phys. 57, 015211 (2016): different quantum information metrics can have different contraction behavior.

**Do not use the quantum Stam inequality as an SLD theorem until the metric relation is established.**

---

# 10. Next actions

1. Determine the precise relation, if any, between the divergence/BKM translation Fisher information used in bosonic Stam inequalities and SLD displacement QFI for the detector families relevant here.
2. Test thermal, squeezed thermal, Fock, and non-Gaussian pointer states to determine whether a universal ordering is strong enough to transfer the Stam inequality to SLD QFI.
3. If the metric transfer fails, preserve an explicit counterexample and retain the Gaussian free-energy theorem as the strongest tight result.
4. Extend the free-energy closure to multimode harmonic apparatus with a total preparation-free-energy budget.
5. Compose the resulting quantum preparation/coupling bound with WP5 finite-band electromagnetic capture and WP3 ongoing thermokinetic constraints where their assumptions overlap.
6. Continue theorem-level novelty audit before any publication claim.
