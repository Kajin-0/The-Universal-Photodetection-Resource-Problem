# WP20 — Dark-mechanism nonuniversality of the optimal Kane gap

**Date:** 2026-08-20

## Purpose

WP18 shows that, at zero temperature, increasing the positive Kane gap monotonically worsens the optical absorption-depth/ballistic transport information rate. WP19 shows how a radiative detailed-balance dark floor can create a competing benefit from increasing the gap.

This note proves a simple but important no-go statement:

> **There is no universal optimal `E_g/(k_B T)` determined by temperature and optical photon energy alone.**

The optimum shifts with the dark-generation mechanism/prefactor, signal photon flux, and required temporal frequency.

---

# 1. Normalize the Kane transport factor

For target photon energy `hbar omega_0`, define

\[
y=\frac{E_g}{\hbar\omega_0},
\qquad 0\le y<1.
\]

WP18 gives the weak-loss finite-gap transport factor

\[
G_K(y)
=F_K(y)u_0(y),
\]

with

\[
G_K(0)=13.
\]

Define

\[
\boxed{h(y)=G_K(y)/13.}
\]

Then

\[
h(0)=1,
\qquad
h(y)\to0\quad(y\to1^-).
\]

Direct differentiation gives

\[
\boxed{h'(0)=-6/13.}
\]

Let

\[
\Gamma(y)=\Gamma_0 h(y),
\]

where `Gamma_0` is the gapless optical-depth/transport rate scale.

---

# 2. Generic activated dark channel

Consider one dark mechanism with

\[
\boxed{
d(y)=d_0e^{-by},}
\]

where

\[
b=\zeta\frac{\hbar\omega_0}{k_BT}.
\]

The activation exponent `zeta` is mechanism dependent. For example, different idealized diffusion/generation-recombination/Auger-type scalings can contain different effective activation powers. The present theorem does not assign a universal value.

Let the useful incident photon rate be `Phi_s` and define

\[
A=\frac{d_0}{\Phi_s}.
\]

For clarity take ideal DC capture `eta_c=1`; adding finite capture changes prefactors but not the conclusion.

---

# 3. Finite-frequency event-information functional

At modulation angular frequency `Omega`, define

\[
r=\frac{\Omega}{\Gamma_0}.
\]

Using the Poisson dark-count dilution factor and the Lorentzian depth-delay model,

\[
\boxed{
\eta_I(y)
=
\frac{1}{1+Ae^{-by}}
\frac{h(y)^2}{h(y)^2+r^2}.
}
\]

This expression isolates the competition:

- larger gap decreases dark events;
- larger gap also decreases the useful optical-depth/transport rate.

---

# 4. Exact stationarity equation

Differentiate:

\[
\boxed{
\frac{d\ln\eta_I}{dy}
=
 b\frac{Ae^{-by}}{1+Ae^{-by}}
+2\frac{h'(y)}{h(y)}
\frac{r^2}{h(y)^2+r^2}.
}
\]

An interior optimum `y_*` must satisfy

\[
\boxed{
 b\frac{Ae^{-by_*}}{1+Ae^{-by_*}}
=
-2\frac{h'(y_*)}{h(y_*)}
\frac{r^2}{h(y_*)^2+r^2}.
}
\]

Every quantity on the left/right has direct resource meaning.

---

# 5. Initial-gap criterion

Using

\[
h(0)=1,
\qquad h'(0)=-6/13,
\]

one obtains

\[
\boxed{
\left.\frac{d\ln\eta_I}{dy}\right|_{y=0}
=
\frac{bA}{1+A}
-
\frac{12}{13}
\frac{r^2}{1+r^2}.
}
\]

Therefore a sufficient condition for opening a small positive gap to improve finite-frequency information is

\[
\boxed{
\frac{bA}{1+A}
>
\frac{12}{13}
\frac{r^2}{1+r^2}.
}
\]

If this holds, while `eta_I->0` as `y->1^-`, continuity guarantees at least one interior maximum.

---

# 6. Nonuniversality theorem

The initial-gap criterion depends on

\[
A=d_0/\Phi_s,
\qquad
b=\zeta\hbar\omega_0/(k_BT),
\qquad
r=\Omega/\Gamma_0.
\]

Changing any of the following changes the optimum:

1. dark-current prefactor `d_0`;
2. activation exponent/mechanism `zeta`;
3. incident signal photon rate `Phi_s`;
4. demanded temporal frequency `Omega`;
5. optical carrier energy;
6. temperature.

Hence

\[
\boxed{
\{T,\hbar\omega_0\}
\not\Rightarrow
\text{unique optimal }E_g.
}
\]

More strongly, even

\[
\boxed{
\{T,\hbar\omega_0,\Gamma_0\}
\not\Rightarrow
\text{unique optimal }E_g
}
\]

without dark-generation resources and source flux.

**Status:** PROVED within the broad activated-dark family.

---

# 7. Why this matters for UPRP

A common intuition is that a universal room-temperature LWIR material should have a special gap ratio `E_g/(k_BT)`. The theorem shows that such a ratio cannot be universal if the objective includes finite-frequency detectability: the optimum depends on how dark events are generated and on the signal/task resources.

This does not rule out a universal **lower bound** based on a specific unavoidable dark mechanism. That is the role of the radiative detailed-balance floor in WP19.

---

# 8. Multiple dark mechanisms

For

\[
d_{\rm tot}(y)=\sum_j d_{0j}e^{-b_jy},
\]

the event-information factor becomes

\[
\eta_I(y)
=\frac{1}{1+d_{\rm tot}(y)/\Phi_s}
\frac{h^2}{h^2+r^2}.
\]

The logarithmic derivative contains the weighted effective activation slope

\[
-\frac{d}{dy}\ln[1+d_{\rm tot}/\Phi_s],
\]

which depends on all mechanism weights. There is no reduction to temperature alone.

---

# 9. Relation to actual HgCdTe dark mechanisms

Real HgCdTe may involve diffusion, generation-recombination, Auger-1/Auger-7, trap-assisted tunneling, band-to-band tunneling, surface leakage, and contact contributions.

Those models can be inserted later as examples. Their mechanism dependence is exactly why they must not be silently absorbed into a supposed universal `E_g/k_BT` optimum.

---

# 10. Next step

Use WP19's radiative detailed-balance floor as the controlled baseline and evaluate its dimensionless optimum. Then add one nonradiative channel at a time and quantify how the optimum moves.

The relevant output should be a **resource phase diagram**, not one universal magic band gap.

---

# Status

**PROVED mechanism-nonuniversality result for the stated event-information model.**