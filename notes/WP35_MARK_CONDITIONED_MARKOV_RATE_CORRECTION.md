# WP35 — Mark-Conditioned Markov Rate Correction

**Date:** 2026-08-20

## Purpose
Correct the microscopic classical-Markov interpretation of the WP25/WP32 conditional-hazard resource after a final manuscript-level adversarial audit.

The general marked-event theorem, Wiener theorem, collision resource, hazard inequality, WP33 no-go, WP34 inverse cost, and WP29 gateway theorem are unchanged.

The correction concerns only which **bare Markov rate** is a safe generic sufficient bound on the mark-conditioned registration hazard.

---

## 1. Why registration-edge intensity alone is insufficient

Suppose a pre-registration state `x` has two competing exits:

- successful registration edge of rate `r`;
- nonregistration/failure edge of rate `R`.

The total holding rate is

\[
q_x=r+R.
\]

Conditional on the next exit being the registration edge, the holding time is still

\[
T_x\sim\operatorname{Exp}(r+R),
\]

because CTMC holding time is independent of exit destination.

Thus the delay hazard conditioned on the successful mark is

\[
h(t\mid M=\text{success})=r+R,
\]

which can be arbitrarily larger than the registration-edge intensity `r`.

Therefore

\[
\boxed{
\max_x\{\text{registration-edge intensity from }x\}
}
\]

is **not** a valid generic uniform bound for complete mark-conditioned timing.

This does not contradict the capture-weighted theorem: as `R->infinity`, successful-mark probability is `r/(r+R)`, so the large conditional hazard can be compensated by vanishing mark weight.

---

## 2. Correct finite-state CTMC sufficient bound

Let `S_pre` be the finite set of pre-registration states. For each state `x`, define the **total escape rate**

\[
q_x
=\sum_{y\neq x}W_{yx},
\]

where the sum includes every allowed transition out of `x`, including registration and nonregistration/internal transitions.

Define

\[
\boxed{
q_{\max}=\max_{x\in S_{\rm pre}}q_x.
}
\]

Consider a primary-event mark `M` that may identify exit route or later autonomous jump-path information but does not itself reveal the realized pre-registration holding times.

For a fixed initial state `x`, the first holding time satisfies

\[
T_x\sim\operatorname{Exp}(q_x)
\]

and is independent of the embedded jump-chain destination and all subsequent autonomous trajectory information.

Therefore, after conditioning on any allowed mark,

\[
D\mid M=T_x+Y_M,
\qquad Y_M\ge0,
\]

with `T_x` independent of `Y_M`.

The exponential-convolution lemma used in WP29 gives

\[
\boxed{
h_D(t\mid M)\le q_x\le q_{\max}.}
\]

If capture initializes a mixture of pre-registration states and the mark partially resolves that mixture, each component obeys the same `q_max` ceiling and survival-weighted mixing preserves the bound.

Hence

\[
\boxed{
\Lambda_{\rm CTMC}=q_{\max}
}
\]

is a safe generic finite-state classical-Markov sufficient resource for the uniform conditional-hazard theorem, under the stated mark restriction.

**Status: PROVED.**

---

## 3. Relation to WP29

WP29 is already consistent with this correction.

There the captured photon places the detector in a distinguished gateway state `1`, whose **total first-exit rate** is

\[
\lambda_1=\sum_{y\neq1}W_{y1}.
\]

The downstream mark is explicitly restricted not to record the realized gateway dwell time. Therefore

\[
h_D(t\mid M)\le\lambda_1
\]

is exactly the special-case total-escape-rate theorem above.

No WP29 formula changes.

---

## 4. Why the stronger capture-weighted resource remains preferable

A global `q_max` can be unnecessarily pessimistic. The exact event theorem is organized instead around

\[
\mathfrak H
=\int\Lambda(m)\kappa(dm).
\]

Rare marks can carry large conditional hazard without large information cost when their capture/event weights are correspondingly small.

The two-exit example illustrates this directly:

\[
P(M=\text{success})=\frac{r}{r+R},
\qquad
\Lambda(M=\text{success})=r+R,
\]

so their product is

\[
P(M=\text{success})\Lambda(M=\text{success})=r.
\]

Thus mark conditioning makes the **uniform** rate scale large while the capture-weighted hazard contribution stays finite.

This is precisely why WP32 superseded a worst-case-only formulation.

---

## 5. Quantum-jump sentence removed from first manuscript

Earlier notes casually stated that

\[
\left\|\sum_\alpha L_\alpha^\dagger L_\alpha\right\|_\infty
\]

is a generic mark-conditioned hazard bound for quantum-jump registration.

That statement is safe only under additional trajectory assumptions (for example, when the relevant sum represents the complete competing jump intensity before registration and mark conditioning does not expose additional pre-registration timing records).

The current first manuscript is a classical weak-coherent/Poisson event-channel theorem and does not require this quantum microscopic extension.

Therefore the manuscript should **remove the generic quantum-jump claim** rather than overstate it. A quantum-trajectory completion belongs to the separate quantum detector branch if later needed.

---

## 6. Manuscript consequence

Replace the Rev4 sentence

> For a classical Markov detector, a sufficient uniform `Lambda` is the maximum total intensity of all first-registration transitions from any pre-registration state. For quantum-jump registration, a sufficient bound is `||sum L^dagger L||_infinity`.

with the conservative statement:

> For a finite-state continuous-time Markov detector, a sufficient uniform bound is the maximum **total escape rate** from any pre-registration state, provided the accessible mark does not independently record the realized pre-registration holding times. This local bare-rate scale is distinct from stationary dynamical activity.

The general theorem and all constants remain unchanged.

---

## Status

**COUNTEREXAMPLE to registration-edge-only uniform bound: PROVED**

**TOTAL-ESCAPE-RATE CTMC SUFFICIENT BOUND: PROVED**

**GENERIC QUANTUM-JUMP EXTENSION IN FIRST MANUSCRIPT: REMOVED / DEFERRED**
