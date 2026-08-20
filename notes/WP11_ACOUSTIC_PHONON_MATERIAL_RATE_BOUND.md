# WP11 — Acoustic-phonon material localization-rate bound

**Date:** 2026-08-20

## Purpose

The structured-reservoir notes identify reservoir spectral shape/correlation time as an independent detector resource. This note maps that abstract resource into the simplest standard semiconductor bath: 3D longitudinal-acoustic phonons coupled by a deformation potential.

The goal is not a universal phonon model. It is to show explicitly how a phenomenological localization rate can be replaced by material constants plus electronic localization geometry.

---

# 1. Deformation-potential coupling

For one longitudinal-acoustic branch with linear dispersion

\[
\omega_{\mathbf q}=c_s q,
\]

a standard deformation-potential matrix element between localized electronic states has the form

\[
\boxed{
M_{\mathbf q}
=D\sqrt{\frac{\hbar q}{2\rho V c_s}}\,F(\mathbf q),
}
\]

where

- `D` is the relevant deformation-potential constant (or an effective difference of electron/hole constants for an excitonic transition);
- `rho` is mass density;
- `c_s` is longitudinal sound speed;
- `V` is the normalization volume;
- `F(q)` is the electronic form factor.

For normalized wave functions,

\[
\boxed{|F(\mathbf q)|\le1.}
\]

Semiconductor quantum-dot literature commonly obtains a super-Ohmic acoustic-phonon spectral density proportional to `omega^3` multiplied by a geometry-dependent high-frequency form factor/cutoff.

---

# 2. Golden-rule emission-rate envelope

For an electronic energy drop

\[
E>0,
\]

phonon emission selects

\[
q_E=E/(\hbar c_s).
\]

Using

\[
\sum_{\mathbf q}\to
\frac{V}{(2\pi)^3}\int d^3q
\]

and Fermi's golden rule,

\[
\Gamma_{\rm em}
=\frac{2\pi}{\hbar}
\sum_{\mathbf q}|M_{\mathbf q}|^2
[n_B(E,T)+1]
\delta(E-\hbar c_sq).
\]

For an isotropic single longitudinal branch this gives

\[
\boxed{
\Gamma_{\rm em}(E,T)
=
\frac{D^2E^3}{2\pi\rho\hbar^4c_s^5}
|F(q_E)|^2
[n_B(E,T)+1]
}
\]

under the stated normalization convention.

Therefore

\[
\boxed{
\Gamma_{\rm em}(E,T)
\le
\frac{D^2E^3}{2\pi\rho\hbar^4c_s^5}
[n_B(E,T)+1].
}
\]

The absorption counterpart is

\[
\boxed{
\Gamma_{\rm abs}(E,T)
\le
\frac{D^2E^3}{2\pi\rho\hbar^4c_s^5}
n_B(E,T).
}
\]

Numerical prefactors depend on branch counting and precise deformation-potential convention, but the resource scaling `D^2 E^3/(rho hbar^4 c_s^5)` and form-factor cutoff are the robust content.

**Status:** PROVED within the isotropic linear-dispersion single-LA-branch deformation-potential model.

---

# 3. Spectral-density interpretation

The corresponding bath spectral density has the structure

\[
\boxed{
J_{\rm LA}(\omega)
\propto
\frac{D^2}{\rho\hbar c_s^5}
\omega^3|F(\omega/c_s)|^2.
}
\]

Thus:

- low frequency: 3D deformation-potential coupling is super-Ohmic (`~omega^3`);
- high frequency: electronic localization makes `F(q)` decay and supplies a finite spectral bandwidth;
- changing confinement geometry changes the spectral maximum and correlation time.

This behavior is standard in semiconductor quantum-dot phonon theory.

Literature anchors include deformation-potential QD phonon spectral densities of the form

\[
J(\omega)=A\omega^3e^{-\omega^2/\omega_c^2}
\]

and microscopic electron/hole form-factor versions.

---

# 4. Geometry supplies the spectral regularizer

For a Gaussian localized electronic envelope of characteristic size `a`, a typical form factor behaves schematically as

\[
|F(q)|^2\sim e^{-q^2a^2/C}
\]

with an order-unity convention-dependent constant `C`.

Then the phonon spectral cutoff scales as

\[
\boxed{\omega_c\sim c_s/a.}
\]

This connects the abstract spectral-regularity resource of `WP11_RESERVOIR_SPECTRAL_REGULARITY_NO_GO.md` directly to a semiconductor localization length.

A smaller electronic localization length allows broader phonon spectral support; a larger localized state narrows the bath coupling spectrum.

Therefore the phonon event-rate resource is not material-only:

\[
\boxed{
\text{deformation potential + density + sound speed + electronic localization geometry}.
}
\]

---

# 5. Need for a finite transition-energy/cutoff resource

If one discards the form factor and allows transition energy `E -> infinity`, the continuum envelope grows as `E^3` and is not a uniform rate bound.

A physical completion therefore requires at least one of:

- finite electronic transition-energy span;
- Debye/Brillouin-zone phonon cutoff;
- explicit electronic form factor/localization length;
- full lattice dispersion beyond the linear continuum approximation.

This repeats the UPRP resource pattern:

\[
\boxed{
\text{coupling constant alone}
\not\Rightarrow
\text{finite localization rate}.
}
\]

---

# 6. Debye-cutoff envelope

If the linear acoustic branch is restricted to

\[
q\le q_D,
\qquad
E\le E_D=\hbar c_s q_D,
\]

then the zero-temperature one-branch deformation-potential envelope obeys

\[
\boxed{
\Gamma_{\rm em}
\le
\frac{D^2q_D^3}{2\pi\rho\hbar c_s^2}
}
\]

before additional form-factor suppression.

At finite temperature multiply the energy-resolved expression by the appropriate Bose factor; a useful uniform finite-T bound also needs the allowed energy interval because `n_B(E)` diverges as `E -> 0` while the full deformation-potential rate remains regular due to the `E^3` factor.

---

# 7. Composition with timestamp information

If phonon-assisted localization is well approximated as an independent exponential event stage with rate `Gamma_ph`, then

\[
\boxed{
\eta_I^{\rm ph}(\Omega)
=
\frac{\Gamma_{\rm ph}^2}
{\Gamma_{\rm ph}^2+\Omega^2}.
}
\]

The material/geometry rate envelope therefore yields a corresponding information-bandwidth envelope.

For multiple independent geometry and localization delays,

\[
\eta_I
=\eta_{\rm pre}|H_{\rm geom}|^2
\frac{\Gamma_{\rm ph}^2}
{\Gamma_{\rm ph}^2+\Omega^2}.
\]

---

# 8. Limitations

This note does not cover:

- polar optical phonons;
- piezoelectric acoustic coupling;
- intervalley scattering;
- non-linear phonon dispersion;
- strong electron-phonon coupling/polaron formation;
- multiphonon processes;
- nonequilibrium hot-phonon populations;
- arbitrary extended transport states.

Those may dominate specific IR photodetectors. The value here is the explicit demonstration that a realistic semiconductor reservoir naturally carries both **material** and **spatial localization** resources.

---

# 9. Next step

Use material-specific HgCdTe electron-phonon couplings only if reliable parameters and a clearly defined microscopic transition are available. Otherwise keep the theorem generic and use this branch to establish which classes of material constants are needed for a finite localization information rate.
