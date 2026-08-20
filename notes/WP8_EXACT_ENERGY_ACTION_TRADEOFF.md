# WP8 — Exact apparatus-energy versus interaction-action tradeoff

**Date:** 2026-08-20

## Purpose

The globally tight arbitrary-pointer energy theorem can be inverted analytically. This gives the minimum preloaded detector excitation required to transfer a specified fraction of coherent optical displacement information when optical-to-detector transfer is incomplete.

The result makes the hidden-apparatus-resource no-go quantitatively explicit.

---

## 1. Starting theorem

For coherent optical displacement, passive source-to-detector transfer probability `tau`, and arbitrary detector pointer with total mean excitation budget `N`,

\[
\eta
\equiv
\frac{F_{\rm elec}}{F_{\rm in}}
\le
\frac{\tau}
{\tau+(1-\tau)\xi(N)},
\]

where

\[
\xi(N)
=(\sqrt{N+1}-\sqrt N)^2.
\]

This bound is globally tight under the passive-linear single-collective-mode assumptions.

---

## 2. Exact inversion for target information fraction

Require

\[
\eta\ge q,
\qquad 0<q<1.
\]

If

\[
\tau\ge q,
\]

then a vacuum pointer (`N=0`, `xi=1`) is already sufficient in principle, so

\[
N_{\min}=0.
\]

Now suppose

\[
0<\tau<q.
\]

The information inequality requires

\[
\xi(N)
\le
\frac{\tau(1-q)}{q(1-\tau)}
\equiv y<1.
\]

Parameterize

\[
N=\sinh^2 r,
\qquad
\xi(N)=e^{-2r}.
\]

The minimum resource occurs at equality,

\[
r_{\min}=\frac12\ln\frac1y.
\]

Using

\[
\sinh^2\!\left(\frac12\ln\frac1y\right)
=\frac{(1-y)^2}{4y},
\]

gives

\[
\boxed{
N_{\min}(q,\tau)
=
\frac{(q-\tau)^2}
{4q(1-q)\tau(1-\tau)},
\qquad 0<\tau<q.
}
\]

Together,

\[
\boxed{
N_{\min}(q,\tau)
=
\begin{cases}
0,&\tau\ge q,\\[4pt]
\dfrac{(q-\tau)^2}
{4q(1-q)\tau(1-\tau)},&0<\tau<q.
\end{cases}
}
\]

**Status:** PROVED and achievable under the same model assumptions as the energy theorem.

The saturating implementation is an optimally squeezed-vacuum pointer with exactly `N_min` excitations, beam-splitter transfer `tau`, and aligned homodyne measurement.

---

## 3. Interaction-action form

WP7 gives

\[
\tau\le\sin^2\Gamma,
\qquad
0\le\Gamma\le\pi/2.
\]

For fixed action, the largest possible `tau` minimizes the required apparatus resource. Therefore if

\[
\sin^2\Gamma<q,
\]

one necessarily has

\[
\boxed{
N
\ge
\frac{[q-\sin^2\Gamma]^2}
{4q(1-q)\sin^2\Gamma\cos^2\Gamma}.
}
\]

If `sin^2 Gamma >= q`, no preloaded excitation is fundamentally necessary in the ideal model.

This is an exact **interaction-action/apparatus-energy tradeoff**.

---

## 4. Weak-coupling asymptotic law

For

\[
\Gamma\ll1,
\]

\[
\sin^2\Gamma=\Gamma^2+O(\Gamma^4).
\]

At fixed target `q`,

\[
\boxed{
N_{\min}
=
\frac{q}{4(1-q)}\frac1{\Gamma^2}
+O(1).
}
\]

Equivalently,

\[
\boxed{
N\Gamma^2
\ge
\frac{q}{4(1-q)}+o(1)
}
\]

as `Gamma -> 0` for any sequence maintaining information fraction `q`.

Thus arbitrarily weak coupling can only be compensated by an apparatus excitation diverging as `Gamma^{-2}`.

---

## 5. Dimensional preparation-energy form

For a harmonic pointer of frequency `omega_D`, define excitation energy above vacuum

\[
E_D=\hbar\omega_D N.
\]

Then at weak interaction action,

\[
\boxed{
E_D
\gtrsim
\frac{\hbar\omega_D}{4}
\frac{q}{1-q}
\frac1{\Gamma^2}.
}
\]

This leading coefficient agrees with the large-resource free-energy scaling obtained independently in the WP8 free-energy analysis.

---

## 6. Coupling-rate/time form

If

\[
\|V(t)\|_2\le g_{\max}
\]

for an interaction duration `t`, then

\[
\Gamma\le g_{\max}t.
\]

In the weak-action regime,

\[
\boxed{
N
\gtrsim
\frac{q}{4(1-q)}
\frac1{g_{\max}^2t^2}.
}
\]

Equivalently, with finite `N`, the transfer time cannot be reduced below the exact action condition

\[
\boxed{
t
\ge
\frac1{g_{\max}}
\arctan
\sqrt{\frac{q\xi(N)}{1-q}}.
}
\]

---

## 7. Finite-temperature free-energy corollary: restricted monotone regime

Let the pointer thermal occupation be

\[
n_\beta=(e^{\vartheta}-1)^{-1},
\qquad
\vartheta=\beta\hbar\omega_D.
\]

For states with mean excitation `N >= n_beta`, the minimum relative entropy to the thermal reference at fixed `N` is

\[
d_\vartheta(N)
=\vartheta N-g(N)-\ln(1-e^{-\vartheta}),
\]

which is increasing on this branch.

Therefore, whenever the required excitation satisfies

\[
N_{\min}(q,\tau)\ge n_\beta,
\]

any detector attaining the target must obey the preparation free-energy lower bound

\[
\boxed{
\beta\Delta F
\ge
d_\vartheta[N_{\min}(q,\tau)].
}
\]

This corollary is rigorous but not generally tight because directional QFI depends on more than mean excitation. The direct WP8 free-energy/QFI envelopes are stronger when available.

---

## 8. Interpretation

The exact theorem makes one of the UPRP resource-completeness statements quantitative:

\[
\boxed{
\text{weak optical coupling}
\quad\text{and}\quad
\text{finite apparatus preparation resource}
\quad\text{cannot both be taken to zero at fixed information transfer.}
}
\]

The hidden-resource counterexample is therefore repaired by an explicit resource product law rather than merely by adding an unspecified `N` to the theorem statement.
