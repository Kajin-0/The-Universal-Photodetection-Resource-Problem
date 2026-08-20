# WP19 — Kane radiative detailed-balance + transport information model

**Date:** 2026-08-20

## Purpose

WP18 shows that opening a positive Kane gap monotonically worsens the best-case optical absorption-depth/ballistic transport rate at fixed photon energy. A finite detector-level optimum can therefore arise only after a dark-generation/noise resource is included.

Rather than insert one empirical HgCdTe dark-current formula, this note first adds the **radiative detailed-balance floor** supplied by the van Roosbroeck–Shockley relation. This ties equilibrium radiative generation to the same absorption coefficient that determines target-photon capture.

The resulting model is still restricted: a real HgCdTe detector may be dominated by Auger, SRH, tunneling, surface leakage, contacts, or other dark mechanisms. Those can only be added as extra dark channels. The purpose here is to identify the clean radiative-limited structure.

---

# 1. van Roosbroeck–Shockley equilibrium generation

For an isotropic homogeneous direct-gap semiconductor at temperature `T`, the equilibrium radiative recombination/generation rate per unit volume can be written

\[
\boxed{
R_{\rm rad}(T)
=\int_{\omega_g}^{\infty}
\frac{n^2(\omega)\omega^2}{\pi^2c^2}
\,a(\omega,T)
\,n_B(\omega,T)\,d\omega,
}
\]

where

\[
n_B(\omega,T)=\frac1{e^{\hbar\omega/k_BT}-1}
\]

and `a(omega,T)` is the equilibrium net absorption coefficient.

This is established semiconductor detailed-balance physics and must be cited as prior art.

Useful references:

- W. van Roosbroeck and W. Shockley, Phys. Rev. 94, 1558 (1954).
- T. Markvart, WIREs Energy and Environment 11, e430 (2022), detailed-balance review.

---

# 2. Finite-temperature Kane interband absorption factor

Let

\[
x=\frac{\hbar\omega}{k_BT},
\qquad
x_g=\frac{E_g}{k_BT},
\qquad
y=\frac{x_g}{x}.
\]

The zero-temperature Kane spectral factor from WP18 is

\[
F_K(y)
=12\sqrt{1-y}+(1+2y^2)\sqrt{1-y^2}.
\]

At finite temperature and chemical potential `mu`, the two channels acquire Pauli occupation differences.

For the flat-to-conduction transition,

\[
E_i=-E_g/2,
\qquad
E_f=\hbar\omega-E_g/2,
\]

so define

\[
\Delta f_0(x,x_g,\bar\mu)
=f(-x_g/2-\bar\mu)
-f(x-x_g/2-\bar\mu),
\]

where

\[
f(z)=\frac1{e^z+1},
\qquad
\bar\mu=\mu/(k_BT).
\]

For lower-cone to upper-cone transitions,

\[
E_i=-\hbar\omega/2,
\qquad
E_f=+\hbar\omega/2,
\]

so

\[
\Delta f_c(x,\bar\mu)
=f(-x/2-\bar\mu)-f(x/2-\bar\mu).
\]

Define the finite-temperature interband factor

\[
\boxed{
F_{K,T}(x;x_g,\bar\mu)
=12\sqrt{1-y}\,\Delta f_0
+(1+2y^2)\sqrt{1-y^2}\,\Delta f_c,
}
\]

for `x>=x_g`, and zero below threshold.

At low temperature/intrinsic filling, the occupation differences approach unity and `F_{K,T}->F_K`.

---

# 3. Weak-loss finite-temperature Kane absorption

Within the same weak-loss/background-index approximation as WP18,

\[
\boxed{
a_K(\omega,T)
\simeq
\frac{\alpha_{\rm fs}}{12n(\omega)v_K}
\,\omega\,
F_{K,T}(x;x_g,\bar\mu).
}
\]

This formula isolates the Kane interband part only.

---

# 4. Radiative generation integral

Assume for the moment a slowly varying representative refractive index `n` over the thermally important spectral range.

Substituting the Kane absorption into van Roosbroeck–Shockley gives

\[
\boxed{
R_{\rm rad}^{K}
=\frac{n\alpha_{\rm fs}}
{12\pi^2c^2v_K}
\left(\frac{k_BT}{\hbar}\right)^4
\mathcal I_K(x_g,\bar\mu),
}
\]

where

\[
\boxed{
\mathcal I_K(x_g,\bar\mu)
=\int_{x_g}^{\infty}
\frac{x^3F_{K,T}(x;x_g,\bar\mu)}{e^x-1}
\,dx.
}
\]

This provides a closed dimensionless representation of the radiative thermal generation rate in the simplified Kane model.

**Status:** derived by direct substitution into the established detailed-balance relation.

---

# 5. Finite planar detector with required capture efficiency

Consider a single-pass homogeneous planar absorber of area `A` and thickness `L`, with target optical carrier `omega_0` and target absorption coefficient

\[
a_0=a_K(\omega_0,T).
\]

Ignore front-surface reflection for the moment or treat it separately as an optical capture factor.

The target-photon bulk capture efficiency is

\[
\boxed{
\eta_c=1-e^{-a_0L}.
}
\]

Thus the minimum thickness required for a prescribed `eta_c` is

\[
\boxed{
L=\frac{s}{a_0},
\qquad
s=-\ln(1-\eta_c).
}
\]

Assume every equilibrium thermally generated radiative pair in the active depleted volume is collected as a dark event. Then the radiative dark-event rate is

\[
d_{\rm rad}=ALR_{\rm rad}^{K}.
\]

For incident signal photon flux density `phi_s` at the target carrier,

\[
\Phi_s=A\phi_s,
\]

and the useful DC signal-event rate is

\[
\eta_c\Phi_s.
\]

The radiative-dark / useful-signal ratio is therefore

\[
\boxed{
\delta_{\rm rad}
\equiv
\frac{d_{\rm rad}}{\eta_c\Phi_s}
=
\frac{s}{\eta_c}
\frac{R_{\rm rad}^{K}}
{a_0\phi_s}.
}
\]

Area cancels exactly.

---

# 6. Second Kane cancellation: optical matrix element drops out of radiative-dark/signal ratio

Let

\[
x_0=\frac{\hbar\omega_0}{k_BT},
\qquad
F_0=F_{K,T}(x_0;x_g,\bar\mu).
\]

The target absorption is

\[
a_0
=\frac{\alpha_{\rm fs}}{12nv_K}
\omega_0F_0.
\]

Hence

\[
\boxed{
\frac{R_{\rm rad}^{K}}{a_0}
=
\frac{n^2}{\pi^2c^2}
\frac{(k_BT/\hbar)^4}{\omega_0}
\frac{\mathcal I_K(x_g,\bar\mu)}{F_0}.
}
\]

Both the explicit Kane velocity and the fine-structure factor cancel.

Therefore

\[
\boxed{
\delta_{\rm rad}
=
\frac{-\ln(1-\eta_c)}{\eta_c}
\frac{n^2}{\pi^2c^2\phi_s}
\frac{(k_BT/\hbar)^4}{\omega_0}
\frac{\mathcal I_K(x_g,\bar\mu)}{F_0}.
}
\]

This is a useful resource result:

> in this radiative-limited single-pass Kane model, once absorber thickness is chosen to achieve a fixed target capture efficiency, the equilibrium radiative-dark/signal ratio is controlled by thermal photon phase space, gap/occupation factors, refractive index, and incident signal photon flux density — not by the explicit Kane velocity or the overall interband matrix-element prefactor.

This cancellation follows from detailed balance; do not assume it survives nonradiative dark mechanisms.

---

# 7. Exact truncated absorption-depth delay transfer function

For finite thickness `L`, conditional target-photon absorption depth is

\[
p_Z(z)
=\frac{a_0e^{-a_0z}}{\eta_c},
\qquad 0\le z\le L.
\]

Assume deterministic collection velocity `v_col` and event delay

\[
D=z/v_{\rm col}.
\]

Then

\[
H(\Omega)
=\mathbb E[e^{-i\Omega D}]
=\frac{a_0}{\eta_c}
\frac{1-e^{-(a_0+i\Omega/v_{\rm col})L}}
{a_0+i\Omega/v_{\rm col}}.
\]

Define

\[
r=\frac{\Omega}{a_0v_{\rm col}},
\qquad
s=a_0L=-\ln(1-\eta_c).
\]

Then

\[
\boxed{
H(r)
=\frac{1-(1-\eta_c)e^{-irs}}
{\eta_c(1+ir)}.
}
\]

Therefore

\[
\boxed{
|H(r)|^2
=
\frac{
1+(1-\eta_c)^2
-2(1-\eta_c)\cos(rs)
}
{\eta_c^2(1+r^2)}.
}
\]

At `eta_c->1`, this reduces to the semi-infinite Lorentzian of WP17.

---

# 8. Radiative-limited source-information transfer

Assume independent Poisson useful signal events and independent Poisson radiative dark events.

For weak fractional modulation of the incident signal flux, the source-normalized event-record Fisher-information transfer is

\[
\boxed{
\eta_{\mathcal I}(\Omega)
=
\frac{\eta_c}{1+\delta_{\rm rad}}
|H(\Omega)|^2.
}
\]

This explicitly factors:

1. target capture efficiency;
2. equilibrium radiative dark dilution;
3. unresolved absorption-depth/transit-delay dispersion.

The model contains no arbitrary detector area.

---

# 9. Transport scale for the finite-gap Kane carrier

For the dominant flat-to-conduction channel, WP18 gives

\[
\boxed{
 v_{\rm col}\le
v_Ku_0(y_0),
\qquad
u_0(y)=\frac{2\sqrt{1-y}}{2-y},
}
\]

where

\[
y_0=E_g/(\hbar\omega_0)=x_g/x_0.
\]

Thus the optimistic target depth-to-delay rate is

\[
\boxed{
a_0v_{\rm col}
\le
\frac{\alpha_{\rm fs}}{12n}
\omega_0
F_0u_0(y_0).
}
\]

This is the speed side of the tradeoff; unlike the radiative-dark/signal ratio, it retains the fine-structure scale.

---

# 10. What this says about an optimal band gap

At fixed target photon energy:

- increasing `E_g` reduces `F_0` and `u_0`, worsening high-frequency transit information;
- increasing `E_g/k_BT` suppresses the thermal detailed-balance integral `I_K`, improving radiative dark performance.

Therefore an interior optimum in total finite-frequency information can occur in this model.

However, its location necessarily depends on additional resources including

\[
\phi_s,\quad T,\quad \omega_0,\quad \eta_c,\quad n,\quad \bar\mu,
\]

and on any nonradiative dark mechanisms.

Thus there is **no universal optimal `E_g/(k_BT)` determined by temperature alone**.

---

# 11. Mechanism-dependent nonradiative dark channels

Real HgCdTe commonly includes Auger, SRH, diffusion, tunneling, surface, and contact leakage.

For the event-information formula they enter through

\[
d_{\rm total}
=d_{\rm rad}+d_{\rm Auger}+d_{\rm SRH}+\cdots
\]

and therefore

\[
\eta_{\mathcal I}(\Omega)
=\frac{\eta_c^2\Phi_s}
{\eta_c\Phi_s+d_{\rm total}}
|H(\Omega)|^2.
\]

The radiative model is an optimistic baseline, not a claim that HgCdTe is radiatively limited.

---

# 12. Important caveats

1. The ideal flat heavy-hole band makes the thermodynamic density of states UV-sensitive. A realistic intrinsic chemical potential requires heavy-hole curvature / finite Kane cutoff. Keep `mu` explicit until that regularization is supplied.
2. The van Roosbroeck–Shockley relation uses the equilibrium absorption spectrum. Finite-temperature Pauli factors must not be omitted if quantitative accuracy is claimed.
3. Photon recycling, optical escape, depletion geometry, and carrier collection probability can modify the relation between volumetric equilibrium generation and measured dark events.
4. Treating generated pairs as independent Poisson dark events is an event-detector approximation.
5. Nonradiative detailed-balance partners can dominate in HgCdTe and introduce additional microscopic resources.

---

# 13. Next work

1. Evaluate the dimensionless radiative integral `I_K(x_g,mu)` and the full finite-slab information functional numerically over `E_g/(hbar omega_0)` for representative `hbar omega_0/k_BT`.
2. Determine whether the radiative-limited optimum is unique and derive asymptotic formulas for `x_g>>1`.
3. Add a generic activated dark channel `d_nr=d_0 exp(-zeta E_g/kT)` and prove explicitly that the optimum shifts with the dark prefactor/mechanism.
4. Compare with established HgCdTe Auger/SRH scalings only as a model example, not as a universal theorem.
5. Explore whether a detailed-balance lower bound can be stated directly in terms of optical etendue/mode count rather than active volume.

---

# Status

**DERIVED restricted radiative-limited model.**

The van Roosbroeck–Shockley relation is prior art. The Kane substitution, cancellations, and source-information composition require novelty audit before any publication claim.