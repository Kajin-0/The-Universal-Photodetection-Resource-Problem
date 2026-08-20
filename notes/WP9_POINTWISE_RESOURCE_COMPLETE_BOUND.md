# WP9 — Pointwise finite-band electromagnetic/coupling/apparatus theorem

**Date:** 2026-08-20

## Purpose

`WP9_FINITE_BAND_QUANTUM_SPECTRAL_COMPOSITION.md` optimizes a **band-averaged** information objective and therefore has a spectral-allocation branch structure. A cleaner theorem is available when the engineering task requires a minimum retained information fraction at **every frequency in the task band**.

In that case the apparatus resource determines a minimum optical transfer probability pointwise. The WP5 finite-band electromagnetic capture bound and WP7 interaction-action cap can then be composed directly.

---

## 1. General pointer-QFI form

For coherent optical displacement at one resolved frequency, detector pointer directional QFI `J_D`, and passive source-to-detector probability `tau`, the SLD-Stam theorem gives

\[
\eta(\omega)
\le
f_J(\tau)
=\frac{\tau J_D}
{2(1-\tau)+\tau J_D}.
\]

Require

\[
\eta(\omega)\ge q
\]

for every frequency in the task band, with `0<q<1`.

Solving `q <= f_J(tau)` gives the necessary transfer probability

\[
\boxed{
\tau(\omega)
\ge
\tau_q(J_D)
\equiv
\frac{2q}
{J_D(1-q)+2q}.
}
\]

This is monotone decreasing in the available apparatus QFI resource.

---

## 2. Arbitrary-state excitation-budget specialization

For a detector pointer with total excitation budget `N`,

\[
J_D\le\frac2{\xi(N)},
\qquad
\xi(N)=(\sqrt{N+1}-\sqrt N)^2.
\]

Therefore any detector satisfying the pointwise target must have

\[
\boxed{
\tau(\omega)
\ge
\tau_q(N)
=
\frac{q\,\xi(N)}
{1-q+q\,\xi(N)}.
}
\]

This expression is globally tight for the passive-linear single-collective-mode energy-constrained model.

It is equivalent to the inverted energy relation in `WP8_EXACT_ENERGY_ACTION_TRADEOFF.md`.

---

## 3. Interaction-action condition

WP7 gives a pointwise transfer cap

\[
\tau(\omega)
\le
\tau_{\max}
=\sin^2\Gamma_{\max}.
\]

Thus a necessary condition for the pointwise information task is

\[
\boxed{
\tau_{\max}
\ge
\tau_q(J_D).
}
\]

Equivalently,

\[
\boxed{
\Gamma_{\max}
\ge
\arcsin\sqrt{\tau_q(J_D)}.
}
\]

For the exact excitation-budget case this reduces algebraically to

\[
\Gamma_{\max}
\ge
\arctan
\sqrt{\frac{q\xi(N)}{1-q}},
\]

consistent with WP8.

---

## 4. Finite-band electromagnetic condition

Let WP5 provide the band-average passive capture/transfer ceiling

\[
\frac1{2\Omega_s}
\int_{-\Omega_s}^{\Omega_s}
\tau(\Omega)d\Omega
\le
B_{\rm opt}(\Omega_s).
\]

If the pointwise information requirement holds, then

\[
\tau(\Omega)\ge\tau_q(J_D)
\]

everywhere in the band. Hence its average must also obey

\[
\bar\tau\ge\tau_q(J_D).
\]

Therefore

\[
\boxed{
B_{\rm opt}(\Omega_s)
\ge
\tau_q(J_D)
}
\]

is a necessary electromagnetic condition.

This result is independent of how the coupling is spectrally allocated because the task itself forbids sacrificing any frequency.

---

## 5. Narrow-band T-operator bandwidth ceiling

In the reciprocal electrically-small narrow-sideband regime,

\[
B_{\rm opt}(\Omega_s)
\le
\min\left\{1,\frac{\Omega_{\rm EM}}{\Omega_s}\right\},
\]

where

\[
\Omega_{\rm EM}
=\frac{\pi V}{4cA}
\min(\omega_p^2,\omega_0^2t_0).
\]

If the nontrivial branch applies, the pointwise information target therefore requires

\[
\frac{\Omega_{\rm EM}}{\Omega_s}
\ge
\tau_q(J_D).
\]

Thus

\[
\boxed{
\Omega_s
\le
\frac{\Omega_{\rm EM}}
{\tau_q(J_D)}
=
\Omega_{\rm EM}
\frac{J_D(1-q)+2q}
{2q}.
}
\]

This is a direct finite-band **electromagnetic + apparatus-metrological-resource** ceiling.

Together with the action condition,

\[
\boxed{
\Omega_s
\le
\Omega_{\rm EM}
\frac{J_D(1-q)+2q}{2q},
\qquad
\Gamma_{\max}
\ge
\arcsin\sqrt{
\frac{2q}{J_D(1-q)+2q}
}.
}
\]

Both conditions are necessary.

---

## 6. Excitation-budget closed form

Substituting

\[
J_D=2/\xi(N)
\]

as the strongest possible apparatus QFI at fixed excitation gives

\[
\boxed{
\Omega_s
\le
\Omega_{\rm EM}
\frac{1-q+q\xi(N)}
{q\xi(N)}.
}
\]

The accompanying action condition is

\[
\boxed{
\Gamma_{\max}
\ge
\arctan
\sqrt{\frac{q\xi(N)}{1-q}}.
}
\]

At `N=0`, `xi=1`:

\[
\Omega_s\le\Omega_{\rm EM}/q,
\qquad
\Gamma_{\max}\ge\arcsin\sqrt q.
\]

At large `N`, `xi(N)~1/(4N)`, so the EM bandwidth ceiling grows approximately linearly with the preloaded apparatus excitation:

\[
\Omega_s
\lesssim
4N\Omega_{\rm EM}\frac{1-q}{q}
+\Omega_{\rm EM}.
\]

This extensive improvement is not free: WP8 gives the corresponding preparation-energy/free-energy cost.

---

## 7. Equilibrium thermal-pointer specialization

For a harmonic pointer initially at thermal equilibrium,

\[
J_D=2t_\beta,
\qquad
t_\beta=\tanh\frac{\beta\hbar\omega_D}{2}.
\]

Hence

\[
\boxed{
\tau_q^{\rm th}
=
\frac{q}
{q+t_\beta(1-q)}.
}
\]

The necessary conditions become

\[
\boxed{
\Gamma_{\max}
\ge
\arcsin\sqrt{
\frac{q}{q+t_\beta(1-q)}
},
}
\]

and

\[
\boxed{
\Omega_s
\le
\Omega_{\rm EM}
\frac{q+t_\beta(1-q)}{q}.
}
\]

At zero temperature, `t_beta -> 1`, recovering

\[
\Omega_s\le\Omega_{\rm EM}/q.
\]

At high temperature, `t_beta -> 0`, the required optical transfer approaches unity and the finite-band ceiling approaches

\[
\Omega_s\le\Omega_{\rm EM}.
\]

Thus thermal pointer noise removes the `1/q` slack available to a vacuum pointer when one demands pointwise information preservation.

---

## 8. Arbitrary-state free-energy specialization

Any rigorous free-energy QFI upper envelope

\[
J_D\le J_{\rm cap}(D_0,\vartheta)
\]

may be inserted into

\[
\tau_q(J_D)
=\frac{2q}{J_D(1-q)+2q}.
\]

Useful choices include:

1. the direct generator-moment envelope `J_{P^2}(D_0,vartheta)` from `WP8_DIRECT_GENERATOR_FREE_ENERGY_UPPER_BOUND.md`;
2. the older maximum-excitation envelope `2/xi[N_+(D_0,vartheta)]`;
3. future tighter bounds from the exact WP8 global dual.

Because `tau_q` decreases with `J_D`, replacing the true pointer QFI by an upper envelope gives a valid necessary condition.

---

## 9. Interpretation

For a pointwise task, three physically distinct resources must all clear the same bottleneck:

\[
\boxed{
\text{apparatus resource}
\Rightarrow\tau_q
\le
\begin{cases}
\text{pointwise interaction capability},\\
\text{finite-band EM capture budget}.
\end{cases}
}
\]

The apparatus can reduce the optical transfer fraction needed to preserve information, but it cannot remove the need for finite optical coupling or finite electromagnetic oscillator/static-response budget.

This is a cleaner resource-completeness statement than the band-average theorem when an application genuinely requires uniform information response over the full bandwidth.

---

## 10. Limitations

The theorem assumes:

- coherent displacement encoding;
- passive linear transfer into one effective pointer channel per frequency;
- a pointwise information requirement, not merely average performance;
- a frequency-independent pointer-resource cap over the narrow task band;
- the WP5 passive reciprocal electromagnetic class for the displayed `Omega_EM` form.

It does not yet include active gain, non-Markovian strong coupling, or a shared dynamical apparatus state reused across temporal frequencies.
