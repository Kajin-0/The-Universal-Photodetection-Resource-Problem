# WP23 — Anisotropic Luttinger heavy-hole DOS closure

**Date:** 2026-08-20

## Purpose

WP22 showed that the heavy-hole DOS curvature is a qualitative resource: a scalar `m_hh` below or above about `0.4205 m0` changes the topology of the restricted 300-K/10.6-um radiative optimum. Because experimental/model heavy-hole masses are strongly direction dependent, the correct next quantity is not an arbitrary directional mass but the **three-dimensional DOS-equivalent mass** of the warped heavy-hole band.

This note computes that quantity from a current published HgCdTe Kane/Luttinger parameterization.

---

# 1. Parameter source

Use the HgCdTe material parameterization supplied by

W. Beugeling et al., *kdotpy: k·p theory on a lattice for simulating semiconductor band structures*, SciPost Phys. Codebases 47 (2025), DOI `10.21468/SciPostPhysCodeb.47`.

The published HgCdTe material block gives the alloy/temperature gap and remote-band Luttinger parameters. For Cd fraction `x`, the relevant polynomials are

\[
\boxed{
\gamma_1(x)=4.1-2.8801x+0.3159x^2-0.0658x^3,
}
\]

\[
\boxed{
\gamma_2(x)=0.5-0.7175x-0.0790x^2+0.0165x^3,
}
\]

\[
\boxed{
\gamma_3(x)=1.3-1.3325x+0.0790x^2-0.0165x^3.
}
\]

The same parameterization supplies

\[
E_g(x,T)
\]

and is used below to map each target positive gap to its corresponding composition at 300 K.

These are prior material parameters; no novelty is claimed.

---

# 2. Warped heavy-hole dispersion

For the bulk `Gamma_8` Luttinger Hamiltonian, a fixed propagation direction

\[
\hat k=(n_x,n_y,n_z)
\]

has two doubly degenerate quadratic branches.

Define

\[
Q=\gamma_2(n_x^2+n_y^2-2n_z^2),
\]

\[
R=\sqrt3[-\gamma_2(n_x^2-n_y^2)+2i\gamma_3n_xn_y],
\]

\[
S=2\sqrt3\gamma_3(n_x-in_y)n_z.
\]

Then

\[
\Delta_\gamma(\hat k)
=\sqrt{Q^2+|R|^2+|S|^2}.
\]

The heavy-hole branch is

\[
\boxed{
E_{hh}(k,\hat k)
=-\frac{\hbar^2k^2}{2m_0}
\left[\gamma_1-\Delta_\gamma(\hat k)\right].
}
\]

Hence the directional mass is

\[
\boxed{
\frac{m_{hh}(\hat k)}{m_0}
=\frac1{\gamma_1-\Delta_\gamma(\hat k)}.
}
\]

Checks:

\[
\frac{m_{hh,[001]}}{m_0}
=\frac1{\gamma_1-2\gamma_2},
\]

\[
\frac{m_{hh,[111]}}{m_0}
=\frac1{\gamma_1-2\gamma_3}.
\]

**Status:** standard Luttinger result.

---

# 3. Exact DOS-equivalent mass for a quadratic warped band

For a direction-dependent quadratic coefficient

\[
a(\hat k)=\gamma_1-\Delta_\gamma(\hat k),
\]

the constant-energy radial wavevector scales as

\[
k(E,\hat k)\propto a(\hat k)^{-1/2}.
\]

Therefore the 3D DOS coefficient contains the angular average

\[
\langle a^{-3/2}\rangle_\Omega.
\]

Define `m_hh,DOS` by equating the warped DOS to an isotropic parabolic DOS. Then

\[
\boxed{
\left(\frac{m_{hh,DOS}}{m_0}\right)^{3/2}
=\frac1{4\pi}
\int d\Omega\,[\gamma_1-\Delta_\gamma(\hat k)]^{-3/2}.
}
\]

Equivalently,

\[
\boxed{
\frac{m_{hh,DOS}}{m_0}
=\left\langle
[\gamma_1-\Delta_\gamma(\hat k)]^{-3/2}
\right\rangle_\Omega^{2/3}.
}
\]

This is the correct scalar mass to use in the parabolic heavy-hole carrier-density formula when the sole purpose is to reproduce the full warped-band DOS.

**Status:** DERIVED exactly for a quadratic Luttinger band.

---

# 4. 300-K HgCdTe values across the 10.6-um-relevant gap range

Use the `kdotpy` gap relation to solve for Cd fraction at 300 K.

Numerical angular quadrature gives:

| `E_g` (eV) | Cd fraction `x` | `m_DOS/m0` | `m_[001]/m0` | `m_[111]/m0` |
|---:|---:|---:|---:|---:|
| 0 | 0.11164 | 0.53079 | 0.33962 | 0.67663 |
| 0.03 | 0.13200 | 0.53374 | 0.34279 | 0.67830 |
| 0.06 | 0.15219 | 0.53666 | 0.34594 | 0.67990 |
| 0.09 | 0.17222 | 0.53955 | 0.34908 | 0.68144 |
| 0.117 | 0.19010 | 0.54213 | 0.35190 | 0.68278 |

Thus

\[
\boxed{
m_{hh,DOS}\simeq0.531-0.542m_0}
\]

through the entire positive-gap range relevant to a 10.6-um photon at 300 K.

At the same time the directional mass varies by approximately a factor of two between `[001]` and `[111]`.

---

# 5. Interpretation of the long-standing 0.3–0.7 m0 heavy-hole range

HgCdTe literature/device models commonly quote or use heavy-hole masses spanning approximately `0.3–0.7m0`, with `0.55m0` often used as a convenient scalar value.

The Luttinger calculation above shows why those statements are not contradictory:

- `[001]` curvature is around `0.34–0.35m0`;
- `[111]` curvature is around `0.68m0`;
- the angle-integrated DOS mass is around `0.53–0.54m0`.

Different measurements probe different curvature combinations.

For **intrinsic carrier statistics/charge neutrality**, the DOS mass is the relevant scalar, not an arbitrary directional transport/cyclotron mass.

---

# 6. Consequence for WP22 bifurcation

WP22 found a restricted-model DC bifurcation near

\[
m_{hh}^{crit}\approx0.4205m_0
\]

at 300 K and 10.6 um.

The anisotropic Kane/Luttinger DOS calculation gives

\[
m_{hh,DOS}>0.53m_0
\]

through the full relevant gap interval.

Therefore the physically motivated **DOS branch lies well above the WP22 critical mass**.

This removes the largest scalar-mass ambiguity in the carrier-statistics layer and supports the WP22 conclusion obtained using `0.55m0`: within the restricted radiative-Kane model, self-consistent intrinsic neutrality drives the information optimum to the smallest allowed gap for the tested task/source range.

---

# 7. Updated intrinsic neutrality using composition-dependent DOS mass

Using `m_hh,DOS(E_g)` rather than a constant `0.55m0` gives at 300 K:

| `E_g` (eV) | `mu` (eV) | `mu-E_g` (meV) | `n_i` (cm^-3) |
|---:|---:|---:|---:|
| ~0 | 0.10375 | +103.75 | 1.74e17 |
| 0.03 | 0.10972 | +79.72 | 1.40e17 |
| 0.06 | 0.11670 | +56.70 | 1.08e17 |
| 0.09 | 0.12488 | +34.88 | 7.92e16 |
| 0.117 | 0.13333 | +16.33 | 5.76e16 |

These differ only modestly from the constant-`0.55m0` calculations, confirming that the standard scalar approximation was already close to the actual warped DOS for this purpose.

---

# 8. Recomputed restricted phase diagram

Replacing constant `m_hh` by the composition-dependent anisotropic DOS mass leaves the qualitative result unchanged.

At `T=300 K`, `lambda_0=10.6 um`, `eta_c=0.9`, `n=3.2`, intrinsic neutrality, and the WP21 radiative-only model, global numerical optimization puts the optimum at

\[
\boxed{x_g\to0}
\]

for tested

- `psi = 0.01` through `100`, and
- task frequencies from DC through `100 GHz`.

Example `psi=100` maxima:

| task | optimum | `eta_I,max` |
|---:|---:|---:|
| DC | `x_g -> 0` | ~0.806 |
| 10 GHz | `x_g -> 0` | ~0.788 |
| 20 GHz | `x_g -> 0` | ~0.739 |
| 50 GHz | `x_g -> 0` | ~0.466 |
| 100 GHz | `x_g -> 0` | ~0.115 |

Again these are **restricted radiative-only material-layer values**, not detector predictions.

---

# 9. What has and has not been closed

## Closed more strongly

The flat-heavy-hole thermodynamic pathology is no longer an obstacle to intrinsic carrier statistics.

A published anisotropic HgCdTe Kane/Luttinger parameterization gives a finite, composition-dependent heavy-hole DOS and a self-consistent chemical potential.

The result strongly supports the `m_hh≈0.55m0` neutrality branch rather than the low-mass branch.

## Still open

This is **not yet a full 8-band optical calculation**.

The optical conductivity still uses the simplified Kane matrix/phase-space factors with the self-consistent occupations. A complete closure should diagonalize the full bulk Kane Hamiltonian and calculate

\[
\operatorname{Re}\sigma(\omega,T,\mu)
\]

from its actual bands and velocity matrix elements.

That calculation should include:

1. quadratic remote-band terms;
2. valence-band warping (`gamma2 != gamma3`);
3. the split-off `Gamma_7` band;
4. composition-dependent `P`, `F`, and band offsets where required;
5. charge neutrality using the same Hamiltonian used for optics.

At 10.6 um the split-off band is far in energy and is expected mainly to renormalize low-energy parameters, but this should be demonstrated rather than assumed in a final theorem.

---

# 10. Main resource conclusion

The heavy-hole sector illustrates another important UPRP distinction:

\[
\boxed{
\text{directional transport mass}
\neq
\text{thermodynamic DOS mass}.
}
\]

A resource theorem that inserts a single unspecified `effective mass` is ambiguous.

For HgCdTe, the actual anisotropic band structure can simultaneously support a light directional mass and a substantially larger DOS mass. The latter controls charge neutrality, Pauli blocking, and therefore the radiative-information phase diagram.

---

# Status

**PROVED/DERIVED:** exact warped-quadratic DOS-mass formula and its evaluation using a published HgCdTe Kane/Luttinger parameterization.

**VERIFIED numerically:** composition-dependent DOS mass `~0.531–0.542m0` across the 300-K 10.6-um positive-gap interval and persistence of the gapless-boundary optimum in the restricted radiative model.

**NEXT:** regularized bulk Kane optical conductivity using the same quadratic/warped band Hamiltonian.