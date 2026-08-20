# WP29 — Thermodynamic Bridge to the Registration-Intensity Information-Bandwidth Theorem

**Date:** 2026-08-20

## Purpose

Compose the earlier reversible-gateway thermokinetic theorem (WP3/WP4) with the new proper-event information-bandwidth theorem (WP25/WP28).

The objective is to answer the original UPRP question in the cleanest currently justified form:

> When do temperature/thermodynamic resources actually imply a finite photodetection information bandwidth, and when do they provably fail to do so?

The answer is conditional. Stationary thermodynamic resources can bound information bandwidth only after they are combined with an **absolute microscopic local rate scale**. In the single-gateway Markov class, WP3 converts that rate scale plus EPR/activity/throughput into a bound on the conditional first-registration hazard required by WP25.

---

# 1. Detector class

Assume a finite-state autonomous continuous-time Markov photodetector with a distinguished optical gateway

\[
0\xrightleftharpoons[d]{u}1,
\]

where state 1 is the first post-capture state.

Assume:

1. stationary net optical absorption;
2. forward optical traffic
   \[
   f=u\pi_0\ge f_*>0;
   \]
3. total dimensionless steady EPR
   \[
   \sigma_{\rm tot}\le\Sigma;
   \]
4. total stationary one-way activity
   \[
   \mathcal A_{\rm tot}\le\mathcal A;
   \]
5. fixed finite reverse optical rate `d`;
6. no primary electrical registration can occur before the first exit from state 1;
7. after that first exit, all further dynamics are autonomous and parameter-independent except through the already captured event;
8. capture probability for an incident signal photon is bounded by
   \[
   \eta_c\le C\le1.
   \]

Accessible event marks may include exit channel identity and arbitrary downstream autonomous information.

---

# 2. WP3 thermodynamic occupancy lemma

Let

\[
r_{\rm opt}=d\pi_1
\]

be reverse optical traffic and define

\[
z=\frac{f}{r_{\rm opt}}\ge1.
\]

The optical-edge EPR is

\[
\sigma_{\rm opt}
=f\left(1-\frac1z\right)\ln z.
\]

Define

\[
g(z)=\left(1-\frac1z\right)\ln z.
\]

Since `g` is monotone increasing on `z>=1`, total EPR and minimum forward throughput imply

\[
g(z)\le\frac{\Sigma}{f_*}.
\]

Define

\[
\boxed{
Z_*=g^{-1}\!\left(\frac{\Sigma}{f_*}\right).
}
\]

Then

\[
z\le Z_*
\]

and therefore

\[
\boxed{
\pi_1\ge\frac{f_*}{dZ_*}.
}
\]

This blocks the rare-fast mechanism in which an arbitrarily fast state is made arbitrarily improbable.

---

# 3. WP3 activity-to-local-rate lemma

Let

\[
\lambda_1=\sum_{j\ne1}W_{j1}
\]

be the total first-exit rate from state 1.

Because activity contains the contribution `pi_1 lambda_1`,

\[
\pi_1\lambda_1\le\mathcal A.
\]

Using the occupancy lower bound,

\[
\boxed{
\lambda_1
\le
\Lambda_*
\equiv
\frac{\mathcal A d Z_*}{f_*}
=
\frac{\mathcal A d}{f_*}
\,g^{-1}\!\left(\frac{\Sigma}{f_*}\right).
}
\]

This quantity has units of inverse time.

---

# 4. New mark-robust hazard lemma

The WP25 theorem requires a bound on the conditional primary-registration hazard after conditioning on all accessible event marks.

Let

\[
T_1\sim\mathrm{Exp}(\lambda_1)
\]

be the first waiting time to leave state 1.

For a continuous-time Markov chain, `T_1` is independent of the exit destination and of all subsequent dynamics. Let `M` denote any accessible autonomous downstream event mark and let

\[
Y_M\ge0
\]

be the additional delay after the first gateway exit, conditional on `M`.

Then

\[
D\mid M=T_1+Y_M
\]

with `T_1` independent of `Y_M`.

For any conditional distribution of `Y_M`,

\[
S_D(t\mid M)
=
\Pr(Y_M>t\mid M)
+
\int_0^t
 e^{-\lambda_1(t-y)}\,dF_{Y_M}(y),
\]

while the absolutely continuous registration density contributed by the exponential first stage is

\[
f_D(t\mid M)
=
\lambda_1
\int_0^t
 e^{-\lambda_1(t-y)}\,dF_{Y_M}(y).
\]

Therefore

\[
f_D(t\mid M)
\le
\lambda_1 S_D(t\mid M),
\]

and hence

\[
\boxed{
h_D(t\mid M)\le\lambda_1}
\]

for every accessible autonomous mark `M` and every time at which the hazard is defined.

Thus

\[
\boxed{
\Lambda_{\rm cond}
\equiv
\operatorname*{ess\,sup}_{M,t}h_D(t\mid M)
\le\lambda_1
\le\Lambda_*.
}
\]

**Status:** PROVED for the stated autonomous Markov gateway class.

---

# 5. Composition with WP25: flat-band theorem

WP25 gives, for a proper autonomous marked event detector with capture ceiling `C` and conditional hazard ceiling `Lambda_cond`,

\[
\bar\eta_I(\Omega_s)
\le
C\min\left[
1,
\frac{\pi\Lambda_{\rm cond}}{2\Omega_s}
\right].
\]

Using `Lambda_cond <= Lambda_*`,

\[
\boxed{
\bar\eta_I(\Omega_s)
\le
C\min\left[
1,
\frac{\pi}{2\Omega_s}
\frac{\mathcal A d}{f_*}
\,g^{-1}\!\left(\frac{\Sigma}{f_*}\right)
\right].
}
\]

Equivalently, if a flat-band task requires

\[
\bar\eta_I(\Omega_s)\ge q>0,
\]

then necessarily

\[
q\le C
\]

and

\[
\boxed{
\Omega_s
\le
\frac{\pi C\mathcal A d}{2qf_*}
\,g^{-1}\!\left(\frac{\Sigma}{f_*}\right).
}
\]

Writing `Omega_s=2 pi B`,

\[
\boxed{
B
\le
\frac{C\mathcal A d}{4qf_*}
\,g^{-1}\!\left(\frac{\Sigma}{f_*}\right).
}
\]

This is a genuine thermokinetic information-bandwidth theorem, but only for the explicitly restricted detector class and only because the absolute reverse gateway rate `d` is part of the resource specification.

---

# 6. Stronger single-gateway frequency shape

WP3 contains more structure than the generic hazard theorem. Because every registration delay contains the independent exponential factor `T_1`,

\[
H_D(\omega\mid M)
=
\frac{\lambda_1}{\lambda_1+i\omega}G_M(\omega),
\qquad |G_M|\le1.
\]

Therefore, before averaging over accessible marks,

\[
|H_D(\omega\mid M)|^2
\le
\frac{\lambda_1^2}{\lambda_1^2+\omega^2}.
\]

Using `lambda_1<=Lambda_*`, the stronger pointwise envelope is

\[
\boxed{
\eta_I(\omega)
\le
C
\frac{\Lambda_*^2}{\Lambda_*^2+\omega^2}.
}
\]

For the flat band,

\[
\boxed{
\bar\eta_I(\Omega_s)
\le
C\frac{\Lambda_*}{\Omega_s}
\tan^{-1}\left(\frac{\Omega_s}{\Lambda_*}\right).
}
\]

At large `Omega_s/Lambda_*`, this approaches

\[
C\frac{\pi\Lambda_*}{2\Omega_s},
\]

exactly matching the asymptotic prefactor of the general WP25 Parseval/hazard theorem.

Thus WP25 is the more general structural theorem, while the original gateway model supplies a sharper low/intermediate-frequency special case.

---

# 7. Composition with WP28: arbitrary source spectrum

Let `w(omega)` be the normalized incident source-information spectrum and let

\[
\mathcal W(A)
=
\sup_{E:\,|E|\le A}
\int_Ew(\omega)d\omega
\]

be its spectral concentration function.

WP28 gives

\[
\bar\eta_I[w]
\le C\mathcal W(\pi\Lambda_{\rm cond}).
\]

Therefore the thermodynamic gateway assumptions imply

\[
\boxed{
\bar\eta_I[w]
\le
C\,\mathcal W\!\left(
\pi
\frac{\mathcal A d}{f_*}
 g^{-1}\!\left(\frac{\Sigma}{f_*}\right)
\right).
}
\]

This is the source-spectrum-native version of the thermokinetic theorem; it does not require defining a conventional bandwidth.

---

# 8. Temperature enters only through a microscopic rate law

Temperature does not by itself appear in the abstract composition.

For a weakly coupled thermal bosonic optical reservoir at transition frequency `omega_0`, one may have

\[
d=\gamma(\omega_0)[n_T(\omega_0)+1],
\]

with

\[
n_T(\omega_0)=
\frac1{e^{\beta\hbar\omega_0}-1}.
\]

If the microscopic coupling spectrum is separately bounded,

\[
\gamma(\omega_0)\le\gamma_{\max},
\]

then

\[
\boxed{
\Lambda_*
\le
\frac{\mathcal A\gamma_{\max}[n_T(\omega_0)+1]}{f_*}
 g^{-1}\!\left(\frac{\Sigma}{f_*}\right).
}
\]

The corresponding information-bandwidth bounds follow immediately.

This explicitly demonstrates the correct logic:

\[
\boxed{
T+\text{thermodynamic budgets}
+\text{absolute microscopic coupling}
\Longrightarrow
\text{finite information bandwidth}.
}
\]

Temperature and stationary thermodynamics alone do not supply the absolute rate scale.

---

# 9. WP4 impossibility theorem in the new language

WP4 constructs reversible Markov detector families in which:

- optical detailed-balance ratios are fixed;
- photon energy/temperature labels are fixed;
- useful throughput remains finite;
- total activity remains bounded;
- total EPR remains bounded;

while a microscopic optical/internal rate scale diverges.

In the new language, those families show that the conditional local registration intensity can become arbitrarily large unless an absolute microscopic rate/coupling resource is bounded.

Therefore no finite function of only

\[
(T,\hbar\omega_0,f_*,\mathcal A,\Sigma,C)
\]

can universally bound the information bandwidth of this abstract reversible Markov class.

Symbolically,

\[
\boxed{
\{T,\hbar\omega_0,f_*,\mathcal A,\Sigma,C\}
\not\Rightarrow
\Lambda_{\rm cond}<\infty
\not\Rightarrow
\text{finite information bandwidth}.
}
\]

An absolute local microscopic rate/coupling scale is necessary.

**Status:** the no-go is inherited from WP4 and now interpreted directly in the WP25 resource language.

---

# 10. Minimal thermodynamic conclusion

For the autonomous proper-event Markov class, the project can now state the following clean result.

## No-go

Stationary thermodynamic resources—temperature, detailed balance, entropy production, activity, and throughput—do not by themselves bound optical-to-electrical information bandwidth.

## Conditional repair

If one also supplies an absolute microscopic gateway/local-rate scale, then EPR + activity + throughput can convert that scale into a finite conditional registration-hazard bound, which WP25/WP28 converts into a finite source-information bandwidth.

The role of thermodynamics is therefore **multiplicative/conditional**, not standalone.

This is substantially closer to the original UPRP objective than a material-specific sensitivity-bandwidth product.

---

# 11. Scope and caveats

This theorem does not apply without modification to:

- externally clocked/synchronous detectors with a free temporal reference;
- continuous coherent pointers that can store phase before event registration;
- arbitrary non-Poisson/nonclassical source statistics;
- parameter-dependent event marks not generated by an autonomous time-translation-invariant channel;
- architectures with direct optical-to-electrical feedthrough that bypasses the bounded gateway.

WP27 gives an explicit free-clock counterexample. WP7/WP8 cover the coherent continuous-pointer branch.

---

# 12. Current status

**PROVED:** WP3 thermodynamic gateway occupancy/rate bound, the mark-robust exponential-gateway hazard lemma, and composition with WP25/WP28.

**PROVED NO-GO:** WP4 shows the absolute local rate/coupling resource cannot be removed in the abstract reversible Markov class.

**OPEN:** theorem-level novelty audit for the complete composed statement; extension beyond Poisson/coherent direct-detection source statistics; whether a broader autonomous non-Markov theorem can replace the explicit Markov gateway assumptions while preserving a thermodynamic route to `Lambda`.