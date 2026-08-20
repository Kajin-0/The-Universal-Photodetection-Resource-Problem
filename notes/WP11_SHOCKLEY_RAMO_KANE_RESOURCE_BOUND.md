# WP11 — Shockley-Ramo and Kane mapping of the electrical transduction resource

**Date:** 2026-08-20

## Purpose

`WP11_MINIMAL_FINITE_LEVEL_SEMICONDUCTOR_DETECTOR.md` identifies the ideal internal transduction rate `kappa` with an electrical-current operator capacity,

\[
\|\hat I\|=e|\kappa|.
\]

This note maps that operator capacity into actual semiconductor quantities. The result is a detector-physics resource pair:

\[
\boxed{
\text{carrier/band velocity scale}
+
\text{electrical weighting-field geometry}
\Rightarrow
\text{finite induced-current/transduction scale}.
}
\]

It also exposes a new no-go: material velocity alone does not bound electrical signal bandwidth if the electrode weighting field is allowed to become arbitrarily localized.

---

# 1. Shockley-Ramo electrical signal operator

For an electrode with weighting potential `phi_w(r)`, define the induced-charge observable for one carrier of charge `q` as

\[
\boxed{
Q_w=q\,\phi_w(\hat{\mathbf r}).
}
\]

The corresponding current is

\[
\boxed{
I_w=\frac{i}{\hbar}[H,Q_w].
}
\]

In the semiclassical/quasistatic limit this reduces to the Shockley-Ramo relation

\[
\boxed{
i_w=q\,\mathbf v\cdot\mathbf E_w,}
\]

where

\[
\mathbf E_w=-\nabla\phi_w.
\]

Primary detector references:

- Z. He, *Review of the Shockley-Ramo theorem and its application in semiconductor gamma-ray detectors*, Nucl. Instrum. Meth. A 463, 250–267 (2001), DOI `10.1016/S0168-9002(01)00223-6`.
- The theorem is routinely used to calculate semiconductor detector induced current, charge, weighting-potential effects, and the small-pixel effect.

---

# 2. Velocity + weighting-field current bound

Let the accessible semiconductor transport subspace have velocity-operator capacity

\[
\boxed{
v_{\mathcal S}=\|\Pi_{\mathcal S}\,\hat{\mathbf v}\,\Pi_{\mathcal S}\|.}
\]

Define the maximum weighting-field magnitude

\[
\boxed{
E_{w,\max}=\sup_{\mathbf r}|\nabla\phi_w(\mathbf r)|.
}
\]

Then

\[
\boxed{
\|I_w\|
\le
|q|\,v_{\mathcal S}E_{w,\max}.
}
\]

Define an effective electrical weighting length

\[
\boxed{
\ell_w\equiv E_{w,\max}^{-1}.
}
\]

Hence

\[
\boxed{
\|I_w\|
\le
\frac{|q|v_{\mathcal S}}{\ell_w}.
}
\]

For a one-electron binary pointer with `||I||=e|kappa|`,

\[
\boxed{
|\kappa|
\le
\frac{v_{\mathcal S}}{\ell_w}.
}
\]

For ideal planar parallel-plate weighting potential,

\[
\phi_w(x)=x/L,
\]

so

\[
\boxed{\ell_w=L}
\]

and

\[
\boxed{|\kappa|\le v_{\mathcal S}/L.}
\]

---

# 3. Independent finite-energy-span bound

The general finite-level theorem from the companion note gives

\[
\|I\|
\le
\frac{W_{\mathcal S}\Delta Q_{\mathcal S}}{2\hbar}.
\]

For a binary one-electron pointer, `Delta Q=e`, therefore

\[
\boxed{|\kappa|\le W_{\mathcal S}/(2\hbar).}
\]

Combining the band/geometry and finite-energy bounds gives

\[
\boxed{
|\kappa|
\le
\kappa_*
\equiv
\min\left[
\frac{W_{\mathcal S}}{2\hbar},
\frac{v_{\mathcal S}}{\ell_w}
\right].
}
\]

These are physically distinct resources:

- `W_S` is an accessible electrical-state energy span;
- `v_S` is a material/band-structure transport scale;
- `ell_w` is an electrode/readout-geometry scale.

---

# 4. New no-go: carrier velocity alone does not bound electrical signal speed

It is tempting to identify a material velocity `v_max` as the ultimate electrical speed resource. Shockley-Ramo shows why that is insufficient.

For one-dimensional motion,

\[
i(t)=qv(t)\frac{d\phi_w}{dx}.
\]

Suppose the weighting potential rises from approximately 0 to 1 over a spatial layer of width `epsilon`. A carrier moving at fixed speed `v` through that layer produces a pulse with characteristic

\[
|i|\sim |q|v/\epsilon,
\]

and duration

\[
\Delta t\sim\epsilon/v.
\]

As

\[
\epsilon\to0,
\]

the current amplitude and pulse bandwidth can grow without bound even though `v` remains fixed. The pulse area remains finite because

\[
\int i(t)dt=q\Delta\phi_w.
\]

Therefore

\[
\boxed{
\text{finite carrier velocity alone}
\not\Rightarrow
\text{finite electrical signal bandwidth}.
}
\]

A finite weighting-field spatial scale, finite electrical-state energy span, circuit response, or another UV geometry regularizer is necessary.

This is physically realized in milder form by the **small-pixel effect**: pixelated semiconductor detectors have weighting potentials that are nearly flat in the bulk and rise rapidly near the collecting pixel. The signal is correspondingly concentrated near the electrode. This behavior is standard Shockley-Ramo detector physics, not a novel claim.

---

# 5. Weighting-length repair

If the weighting potential is Lipschitz with

\[
|\nabla\phi_w|\le1/\ell_w
\]

and carrier speed obeys

\[
|\mathbf v|\le v_{\mathcal S},
\]

then

\[
\boxed{
\left|\frac{d\phi_w}{dt}\right|
\le
\frac{v_{\mathcal S}}{\ell_w}.
}
\]

To accumulate an induced-charge fraction `r` of a one-carrier full weighting-potential swing,

\[
|\Delta\phi_w|\ge r,
\]

one necessarily needs

\[
\boxed{
t\ge r\frac{\ell_w}{v_{\mathcal S}}.}
\]

This is a detector-native electrical rise-time lower bound.

It is not identical to a conventional 3-dB transit-time formula, but it has the same resource structure:

\[
\text{time}\sim\frac{\text{electrical weighting distance}}{\text{carrier velocity}}.
\]

Conventional high-speed photodiode models likewise treat carrier transit time and RC delay as separate bandwidth limits.

---

# 6. Kane-model material scale

For semiconductor bands described by a `k.p` Hamiltonian, the velocity operator is obtained from the crystal Hamiltonian as

\[
\hat v=\frac1\hbar\frac{\partial H}{\partial k}
\]

with the usual projection/operator subtleties in multiband models.

The interband linear-in-`k` velocity scale is set by the Kane momentum matrix element. In a simple two-band block

\[
H(k)=\frac{E_g}{2}\sigma_z+P_{\rm eff}k\,\sigma_x,
\]

one has

\[
\boxed{\|v\|=|P_{\rm eff}|/\hbar.}
\]

In realistic zincblende Kane models angular-momentum factors modify the exact relation between the tabulated Kane parameter and a particular band velocity; use the actual projected velocity operator of the chosen model rather than a scalar shortcut.

Ado, Titov, Duine, and Brataas, SciPost Phys. 17, 009 (2024), explicitly emphasize careful treatment of position and velocity operators in the 8-band Kane model.

---

# 7. HgCdTe example: microscopic ballistic velocity scale

For narrow-gap HgCdTe near the Kane-fermion regime, magneto-spectroscopy reports an approximately composition/temperature-insensitive characteristic Kane velocity

\[
\boxed{v_K\approx(1.07\pm0.05)\times10^6\ {\rm m\,s^{-1}}}
\]

and notes consistency with the accepted Kane parameter

\[
E_P\approx18.8\ {\rm eV}.
\]

Reference:

- F. Teppe et al., *Temperature-driven massless Kane fermions in HgCdTe crystals*, Nat. Commun. 7, 12576 (2016).

This gives an illustrative **ballistic microscopic** internal electrical scale

\[
\boxed{\kappa_{\rm Kane}\sim v_K/\ell_w.}
\]

For planar `ell_w=L`, this is simply `v_K/L`.

Important: this is not a predicted HgCdTe photodetector bandwidth. It is an upper material/geometry scale within the simplified coherent/ballistic mapping. Real detector speed is further reduced by scattering, trapping, recombination, diffusion, electric-field profile, contacts, capacitance, load impedance, amplifier noise, and readout architecture.

---

# 8. Composition with the exact three-node information law

The companion WP11 model gives

\[
\eta_{\mathcal I}^{\max}
=\frac{4g^2\kappa^2}{(g^2+\kappa^2)^2}.
\]

If the semiconductor/electrode physics supplies

\[
|\kappa|\le\kappa_*,
\]

then optimizing the internal coupling under that cap gives

\[
\boxed{
\eta_{\mathcal I}^{\max}
\le
\begin{cases}
1, & |g|\le\kappa_*,\\[5pt]
\dfrac{4g^2\kappa_*^2}{(g^2+\kappa_*^2)^2}, & |g|>\kappa_*.
\end{cases}
}
\]

where

\[
\boxed{
\kappa_*
=\min\left[
\frac{W_{\mathcal S}}{2\hbar},
\frac{v_{\mathcal S}}{\ell_w}
\right].
}
\]

Therefore perfect coherent optical-to-charge transfer requires at minimum that the electrical subsystem be capable of matching the optical coupling:

\[
\boxed{
|g|\le
\min\left[
\frac{W_{\mathcal S}}{2\hbar},
\frac{v_{\mathcal S}}{\ell_w}
\right].
}
\]

This is the first UPRP result in which the internal finite-level transduction rate is replaced by identifiable semiconductor/electrode quantities rather than an unspecified `gamma_max`.

**Status:** PROVED within the stated minimal coherent + Shockley-Ramo/Kane mapping assumptions.

---

# 9. Relation to conventional transit-time bandwidth

Conventional photodiode theory already contains architecture-specific relations of the form

\[
\tau_{\rm tr}\sim L/v,
\qquad
f_{\rm tr}\sim C/\tau_{\rm tr},
\]

and combines transit-time and RC limits. High-speed UTC/MUTC photodiode analyses explicitly use absorber/collector drift distances and carrier velocities to estimate intrinsic bandwidth.

Therefore UPRP must **not** claim that `v/L` transit scaling is new.

The project-specific contribution is different:

1. derive an exact source-normalized information-transfer law in a finite-level optical->exciton->charge model;
2. identify the internal transduction matrix element with a current operator;
3. prove a general finite-level current-capacity inequality;
4. show why carrier velocity alone is not resource-complete because weighting-field geometry can hide arbitrarily short electrical scales;
5. place these quantities into the broader optical-capture + apparatus-preparation + thermokinetic resource hierarchy.

---

# 10. New resource hierarchy for the electrical layer

The electrical/readout part now has the structure

\[
\boxed{
\text{finite charge span}
+
\text{finite electrical energy span}
+
\text{finite band/velocity scale}
+
\text{finite weighting-field geometry scale}
\Rightarrow
\text{finite induced-current/transduction scale}.
}
\]

This is separate from the optical frontend resources of WP5.

---

# 11. Immediate next questions

1. Replace the ideal binary charge state by a finite carrier-transport chain and determine whether the `v/ell_w` bound remains tight.
2. Connect `v_S` to a full finite-band 8-band Kane subspace for HgCdTe without using an invalid unbounded low-energy `k.p` extrapolation.
3. Add irreversible localization/scattering and determine when coherent matching `g=kappa` becomes the usual dissipative impedance-matching condition.
4. Include the external RC/readout circuit as a separate information channel and prove how its passive electrical bandwidth composes with the intrinsic current bound.
5. Stress-test avalanche/multiplication architectures, where multiple carriers change the charge-span resource and pump/bias free energy must be counted explicitly.
