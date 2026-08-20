# WP7 — Energy-repaired Gaussian QFI transfer theorem

**Date:** 2026-08-19

## Scope

This note repairs the squeezed-pointer counterexample in `WP7_COHERENT_GAUSSIAN_QFI_TRANSFER.md` by explicitly bounding the detector pointer's initial Gaussian energy.

The result is tight for a one-signal-mode / one-effective-detector-mode passive linear transducer and identifies the exact trade between:

- coherent optical QFI;
- passive coupling action;
- preloaded detector squeezing/energy;
- electrical Fisher information.

---

# 1. Conventions

Use quadratures

\[
x=(a+a^\dagger)/\sqrt2,
\qquad
p=(a-a^\dagger)/(i\sqrt2),
\]

with `[x,p]=i` and vacuum covariance

\[
V_{\rm vac}=I/2.
\]

The optical source is a coherent displacement family with

\[
\langle x_F\rangle=\theta.
\]

Its QFI is

\[
\boxed{F_{\rm in}=2.}
\]

The detector mode starts in an arbitrary single-mode Gaussian state independent of `theta`, with covariance `V_D` and mean excitation budget

\[
\boxed{N_D\le N.}
\]

Any nonzero theta-independent mean displacement consumes energy without reducing covariance noise, so an optimum under an energy cap can be taken to have zero mean.

For zero mean,

\[
N_D=\frac{\operatorname{Tr}V_D-1}{2}.
\]

---

# 2. Passive coupling parameter

A general two-mode passive transformation can be reduced, up to local phase rotations, to a beam splitter with transfer probability

\[
\tau=\sin^2\phi,
\qquad 0\le\phi\le\pi/2.
\]

For time-dependent passive coupling with cross-block norm `||V(t)||`, the subspace-transfer theorem gives

\[
\tau\le\sin^2\Gamma,
\qquad
\Gamma=\int_0^t\|V(s)\|ds,
\]

for `0<=Gamma<=pi/2`.

Thus it is sufficient to optimize QFI at fixed `tau` and then use `tau<=sin^2 Gamma`.

---

# 3. Detector output Gaussian state

After the beam splitter, the detector displacement derivative has magnitude

\[
|\partial_\theta d_D|=\sqrt\tau.
\]

The detector covariance is

\[
V_{D,\rm out}
=\frac\tau2 I+(1-\tau)V_D.
\]

For a Gaussian family whose parameter appears only in the mean displacement, the SLD QFI is

\[
F_D=(\partial_\theta d_D)^T
V_{D,\rm out}^{-1}
(\partial_\theta d_D).
\]

Therefore

\[
F_D
\le
\frac{\tau}{\lambda_{\min}(V_{D,\rm out})}
=
\frac{\tau}{\tau/2+(1-\tau)\lambda_{\min}(V_D)}.
\]

Because `F_in=2`,

\[
\frac{F_D}{F_{\rm in}}
\le
\frac{\tau}
{\tau+2(1-\tau)\lambda_{\min}(V_D)}.
\]

Equality is obtained when the signal displacement is aligned with the minimum-noise eigenquadrature of the detector covariance.

---

# 4. Tight minimum Gaussian quadrature noise at fixed energy

Let the covariance eigenvalues be

\[
v_-\le v_+.
\]

The single-mode uncertainty principle requires

\[
v_-v_+\ge\frac14.
\]

The energy cap gives

\[
v_-+v_+\le2N+1.
\]

To minimize `v_-`, use the full energy budget and saturate the uncertainty product. Solving

\[
v_-+v_+=2N+1,
\qquad
v_-v_+=1/4
\]

gives

\[
\boxed{
v_-^{\min}(N)
=N+\frac12-\sqrt{N(N+1)}
=\frac12\left(\sqrt{N+1}-\sqrt N\right)^2.
}
\]

Define the dimensionless minimum-noise factor

\[
\boxed{
\xi(N)
\equiv2v_-^{\min}(N)
=\left(\sqrt{N+1}-\sqrt N\right)^2.
}
\]

Equality is achieved by a pure squeezed vacuum aligned to the signal quadrature.

---

# 5. Tight Gaussian QFI-transfer bound at fixed transfer probability

Substitution gives

\[
\boxed{
\frac{F_D}{F_{\rm in}}
\le
\frac{\tau}
{\tau+(1-\tau)\xi(N)}.
}
\]

Every electrical measurement is downstream of the detector state, hence

\[
\boxed{
\frac{F_{\rm elec}}{F_{\rm in}}
\le
\frac{\tau}
{\tau+(1-\tau)\xi(N)}.
}
\]

This bound is tight within the stated one-mode Gaussian class: choose an `x`-squeezed vacuum with mean photon number `N`, align the squeezed quadrature with the transferred signal displacement, use a beam splitter with transfer `tau`, and perform aligned homodyne detection.

**Status:** PROVED and saturable for the stated Gaussian class.

---

# 6. Coupling-action theorem

The right-hand side is monotone increasing in `tau`. Since

\[
\tau\le\sin^2\Gamma,
\]

we obtain, for `0<=Gamma<=pi/2`,

\[
\boxed{
\frac{F_{\rm elec}}{F_{\rm in}}
\le
\frac{\sin^2\Gamma}
{\sin^2\Gamma+\cos^2\Gamma\,\xi(N)}.
}
\]

For larger accumulated action, use the trivial ceiling 1.

This is the **energy-repaired QFI interaction-action theorem** for the single-effective-mode Gaussian photodetection transducer.

---

# 7. Necessary coupling action for target information transfer

If the desired information-transfer fraction is

\[
F_{\rm elec}/F_{\rm in}\ge q,
\qquad0<q<1,
\]

then necessarily

\[
q\le
\frac{\tan^2\Gamma}
{\tan^2\Gamma+\xi(N)}.
\]

Therefore

\[
\boxed{
\tan^2\Gamma
\ge
\frac{q\,\xi(N)}{1-q}
}
\]

and

\[
\boxed{
\Gamma
\ge
\arctan\sqrt{\frac{q\,\xi(N)}{1-q}}.
}
\]

If `||V(t)||<=g_max`, then

\[
\boxed{
t\ge
\frac1{g_{\max}}
\arctan\sqrt{\frac{q\,\xi(N)}{1-q}}.
}
\]

---

# 8. Limiting cases

## Vacuum/coherent apparatus

For `N=0`,

\[
\xi(0)=1.
\]

Hence

\[
F_{\rm elec}/F_{\rm in}\le\sin^2\Gamma,
\]

and

\[
\Gamma\ge\arctan\sqrt{q/(1-q)}
=\arcsin\sqrt q,
\]

recovering the coherent/vacuum theorem exactly.

## Large apparatus energy

For `N>>1`,

\[
\xi(N)
=(\sqrt{N+1}-\sqrt N)^2
\sim\frac1{4N}.
\]

At weak required action,

\[
\Gamma_{\min}
\sim
\sqrt{\frac{q}{4N(1-q)}}.
\]

Thus preloaded detector metrological energy can substitute for coupling action, but only with

\[
\boxed{\Gamma_{\min}\propto N^{-1/2}.}
\]

Equivalently, maintaining fixed `q` as `Gamma->0` requires

\[
\boxed{N\gtrsim\frac{q}{4(1-q)\Gamma^2}.}
\]

This reproduces the squeezed-pointer no-go scaling.

---

# 9. Physical interpretation

The quantum resource hierarchy is now sharper:

\[
\boxed{
\text{source information}
+
\text{cross-coupling action}
+
\text{initial apparatus metrological energy/noise}
\Longrightarrow
\text{QFI-transfer ceiling}.
}
\]

Neither cross-coupling action nor apparatus preparation resource alone is sufficient.

This parallels WP4:

- classical stationary thermodynamic costs did not expose latent absolute transition scales;
- quantum cross-coupling alone does not expose preloaded pointer sharpness/squeezing.

In both cases a hidden resource can make the detector arbitrarily fast/informative unless it is explicitly budgeted.

---

# 10. Relation to thermodynamics

`N` is presently a microscopic apparatus preparation resource, not yet a thermodynamic cost.

For a detector oscillator of frequency `omega_D`, its mean energy is

\[
E_D=\hbar\omega_D(N+1/2).
\]

A fully thermodynamic completion should replace or supplement `N` with a preparation free-energy/ergotropy/asymmetry resource relative to the detector's operating temperature. This is OPEN.

The theorem should not be rewritten directly in terms of steady-state entropy production: a squeezed pointer may be prepared using prior work and then used transiently without its preparation cost appearing in the contemporaneous steady EPR. This is precisely why initial-resource accounting matters.

---

# 11. Novelty caution

Gaussian QFI formulas, squeezing-enhanced displacement sensing, energy-constrained Gaussian metrology, and passive beam-splitter transformations are established theory. The theorem above is not automatically novel merely because it is written in UPRP notation.

Relevant comparison areas include:

- general Gaussian-state QFI and optimal Gaussian measurements;
- displacement sensing with squeezed states under energy constraints;
- weak-coupling ancilla metrology;
- squeezed-environment/readout metrology;
- continuous-variable channel estimation.

The potentially distinct contribution remains the **resource-completeness logic for photodetection** and its composition with the WP4/WP5/WP6 optical and thermokinetic no-go/completion structure.

---

# 12. Next actions

1. Generalize the tight theorem from one effective detector mode to arbitrary multimode Gaussian apparatus with a **total energy budget** and arbitrary passive detector-local processing.
2. Determine whether concentrating all available squeezing into the coupled collective quadrature is globally optimal; if yes, the same `xi(N_total)` bound should survive.
3. Replace initial `N` by a thermodynamic preparation resource where possible.
4. Compose the Gaussian QFI bound with the finite-band EM capture theorem: the total quantum bound should be the minimum of optical capture, coupling/apparatus QFI transfer, and downstream thermokinetic event conversion where all assumptions overlap.
5. Test active Gaussian amplification. Any pump must be included as an additional resource and its quantum noise must be explicit.
