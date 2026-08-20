# WP21 — Dimensionless radiative-Kane information phase diagram

**Date:** 2026-08-20

## Purpose

WP19 combines finite-gap Kane absorption/transport with the van Roosbroeck-Shockley radiative generation floor. WP20 proves that no universal optimal gap can exist once mechanism-dependent dark channels are allowed.

This note rewrites the *radiative-limited* model in dimensionless form, derives the large-gap asymptotic, and gives a representative phase diagram showing how the information-optimal gap depends on source flux and temporal task.

The numerical examples are intentionally idealized. They use the simplified six-band Kane model, a radiative-only dark floor, a fixed refractive index, and an illustrative chemical potential `mu=0`. They are not predictions of an actual HgCdTe detector.

---

# 1. Dimensionless variables

Define

\[
\boxed{
x_0=\frac{\hbar\omega_0}{k_BT}}
\]

for the target optical carrier,

\[
\boxed{
x_g=\frac{E_g}{k_BT}}
\]

for the band gap,

\[
\boxed{y_0=\frac{x_g}{x_0}=\frac{E_g}{\hbar\omega_0}}
\]

and normalized chemical potential

\[
\boxed{\bar\mu=\frac{\mu}{k_BT}}.
\]

The target interband spectral factor is

\[
\boxed{
F_0=F_{K,T}(x_0;x_g,\bar\mu).
}
\]

The optimistic flat-to-conduction group-velocity factor is

\[
\boxed{
u_0(y_0)=\frac{2\sqrt{1-y_0}}{2-y_0}.}
\]

---

# 2. Thermal photon-flux-density scale

Define

\[
\boxed{
\phi_T(x_0,T,n)
=\frac{n^2}{\pi^2c^2}
\frac{(k_BT/\hbar)^4}{\omega_0}.
}
\]

This has units of photon flux per area.

Normalize the incident useful signal photon flux density as

\[
\boxed{
\psi=\frac{\phi_s}{\phi_T}.
}
\]

This is the natural source-strength parameter for the radiative detailed-balance model.

For reference, at

- `T=300 K`,
- `lambda_0=10.6 um`,
- `n=3.2`,

one has

\[
x_0=4.52446,
\]

\[
\boxed{
\phi_T\simeq1.546\times10^{23}\ {\rm m^{-2}s^{-1}}.
}
\]

Multiplying by one target photon energy gives the equivalent irradiance scale

\[
\boxed{
I_T=\phi_T\hbar\omega_0
\simeq2.90\times10^3\ {\rm W/m^2}
=0.290\ {\rm W/cm^2}.
}
\]

Thus `psi=1` means a signal photon flux density comparable to this radiative thermal phase-space scale; it is not a claim about a standard laboratory irradiance.

---

# 3. Dimensionless radiative dark ratio

Let

\[
\eta_c=1-e^{-s},
\qquad
\boxed{s=-\ln(1-\eta_c).}
\]

WP19 gives

\[
\delta_{\rm rad}
=\frac{s}{\eta_c}
\frac{R_{\rm rad}}{a_0\phi_s}.
\]

Using the definition of `phi_T`, this becomes exactly

\[
\boxed{
\delta_{\rm rad}
=
\frac{s}{\eta_c\psi}
\frac{\mathcal I_K(x_g,\bar\mu)}{F_0}.
}
\]

All explicit factors `alpha_fs`, `v_K`, area, and the overall Kane optical matrix-element prefactor have disappeared.

The radiative dark dilution factor is therefore

\[
\boxed{
D_{\rm rad}
=\frac1{1+\delta_{\rm rad}}.
}
\]

---

# 4. Dimensionless transport variable

Define the normalized temporal task frequency

\[
\boxed{
\rho=\frac{\Omega}{\omega_0}.
}
\]

In the weak-loss Kane model,

\[
a_0v_{\rm col}
\le
\frac{\alpha_{\rm fs}}{12n}
\omega_0F_0u_0(y_0).
\]

Using the optimistic equality as the radiative-Kane ceiling, define

\[
\boxed{
r
=\frac{\Omega}{a_0v_{\rm col}}
=\frac{12n\rho}
{\alpha_{\rm fs}F_0u_0(y_0)}.
}
\]

Thus the transport side retains the fine-structure scale.

---

# 5. Exact finite-slab transfer function

For a single-pass slab with target capture `eta_c`, WP19 gives

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

The complete radiative-limited source-information transfer is therefore

\[
\boxed{
\eta_{\mathcal I}
(x_g; x_0,\psi,\rho,\eta_c,n,\bar\mu)
=
\frac{\eta_c}
{1+\dfrac{s}{\eta_c\psi}\dfrac{\mathcal I_K}{F_0}}
\,
\frac{
1+(1-\eta_c)^2
-2(1-\eta_c)\cos(rs)
}
{\eta_c^2(1+r^2)}.
}
\]

with

\[
r=\frac{12n\rho}{\alpha_{\rm fs}F_0u_0}.
\]

This is the central dimensionless phase-diagram equation.

**Status:** derived exactly from the WP19 restricted model.

---

# 6. Resource-dependence theorem

The optimum gap

\[
x_g^*=\arg\max_{0\le x_g<x_0}\eta_{\mathcal I}
\]

is a function of

\[
\boxed{
(x_0,\psi,\rho,\eta_c,n,\bar\mu)
}
\]

before any nonradiative dark mechanism is included.

Therefore even the radiative floor does not produce a universal magic value of `E_g/(k_BT)` independent of source/task resources.

This is a stronger concrete version of the WP20 nonuniversality message.

---

# 7. Large-gap radiative asymptotic

Assume

\[
x_g\gg1
\]

and a chemical potential that does not track the band edge strongly enough to prevent the lower states from becoming occupied and upper states empty. Then the relevant Pauli factors approach unity near the thermal absorption edge.

Write

\[
x=x_g+t,
\qquad t=O(1).
\]

Near threshold,

\[
y=\frac{x_g}{x}
=1-\frac{t}{x_g}+O(x_g^{-2}).
\]

The zero-temperature Kane factor has the threshold expansion

\[
\boxed{
F_K(y)
\sim
C_0\sqrt{1-y},
\qquad
C_0=12+3\sqrt2.
}
\]

Therefore

\[
F_K(x_g/x)
\sim
C_0\sqrt{\frac{t}{x_g}}.
\]

The Bose factor gives

\[
(e^x-1)^{-1}\sim e^{-x_g}e^{-t}.
\]

Hence

\[
\mathcal I_K(x_g)
\sim
C_0x_g^{5/2}e^{-x_g}
\int_0^\infty t^{1/2}e^{-t}dt.
\]

Using

\[
\Gamma(3/2)=\sqrt\pi/2,
\]

one obtains

\[
\boxed{
\mathcal I_K(x_g)
\sim
(12+3\sqrt2)\frac{\sqrt\pi}{2}
\,x_g^{5/2}e^{-x_g}.
}
\]

This explicitly displays the activated radiative suppression multiplied by the 3D direct-edge phase-space factor.

**Status:** PROVED asymptotically under the stated occupation assumptions.

---

# 8. Why the radiative dark ratio has a finite-gap competition

For fixed target optical carrier `x_0`, increasing `x_g` initially suppresses the thermal integral `I_K` approximately exponentially.

But as

\[
x_g\to x_0^-,
\]

the target interband factor

\[
F_0\to0
\]

because the target photon approaches the absorption edge. Therefore the absorber thickness required to maintain fixed capture efficiency,

\[
L=s/a_0\propto1/F_0,
\]

diverges in the simplified single-pass model.

Consequently the ratio

\[
\mathcal I_K/F_0
\]

need not decrease monotonically all the way to the target edge. An interior minimum is physically expected and occurs in the illustrative example below.

This is the radiative detailed-balance version of the dark-current versus absorption-depth tradeoff.

---

# 9. Illustrative 300 K, 10.6 um phase diagram

Use:

- `T=300 K`,
- `lambda_0=10.6 um`, so `x_0=4.52446`,
- `n=3.2`,
- `eta_c=0.9`,
- illustrative `mu_bar=0`,
- radiative dark generation only,
- optimistic Kane group-velocity collection.

**Caveat:** `mu_bar=0` is not a quantitatively self-consistent intrinsic-HgCdTe chemical potential in the ideal flat-heavy-hole model. Heavy-hole curvature/cutoff is required for that. The table is a structural phase-diagram example only.

Numerical optimization of the exact dimensionless expression gives:

| `psi` | task frequency | optimal `x_g=E_g/kT` | maximum `eta_I` |
|---:|---:|---:|---:|
| 0.01 | DC | 3.635 | 0.00100 |
| 0.01 | 10 GHz | 3.459 | 0.00094 |
| 0.01 | 20 GHz | 3.156 | 0.00081 |
| 0.01 | 50 GHz | 2.256 | 0.00042 |
| 0.1 | DC | 3.635 | 0.00989 |
| 0.1 | 10 GHz | 3.458 | 0.00926 |
| 0.1 | 20 GHz | 3.153 | 0.00799 |
| 0.1 | 50 GHz | 2.251 | 0.00416 |
| 1 | DC | 3.635 | 0.0900 |
| 1 | 10 GHz | 3.445 | 0.0843 |
| 1 | 20 GHz | 3.124 | 0.0730 |
| 1 | 50 GHz | 2.201 | 0.0385 |
| 10 | DC | 3.635 | 0.474 |
| 10 | 10 GHz | 3.329 | 0.446 |
| 10 | 20 GHz | 2.892 | 0.395 |
| 10 | 50 GHz | 1.878 | 0.225 |
| 100 | DC | 3.635 | 0.826 |
| 100 | 10 GHz | 2.751 | 0.792 |
| 100 | 20 GHz | 1.991 | 0.731 |
| 100 | 50 GHz | 1.401 | 0.448 |

The trend is unambiguous:

\[
\boxed{
\text{higher demanded temporal frequency}
\Rightarrow
\text{smaller information-optimal gap}
}
\]

within this radiative-only example, because the transport penalty increasingly outweighs the dark-generation benefit.

At DC the optimum is independent of `psi` in this restricted one-dark-mechanism model because maximizing

\[
[1+C(\psi)\mathcal I_K/F_0]^{-1}
\]

is equivalent to minimizing `I_K/F_0`; `psi` changes the achievable information fraction but not the minimizer.

At nonzero frequency the optimum becomes source-flux dependent because dark dilution and transit dispersion compete simultaneously.

---

# 10. Finite-temperature occupation effect

At finite temperature the target absorption factor need not decrease immediately when a small positive gap is opened.

For example, in the illustrative `mu_bar=0` case at `x_0=4.524`, the target `F_0` rises slightly before eventually falling. This occurs because changing the gap also changes the Pauli occupation differences of the flat-to-conduction and cone-to-cone transitions.

Therefore the zero-temperature theorem

\[
G_K(y)\text{ decreases monotonically with }y
\]

must **not** be extrapolated blindly to finite temperature at fixed chemical potential.

The finite-temperature optimum depends on the occupation resource `mu_bar` and on whatever microscopic model fixes the chemical potential.

---

# 11. What is universal and what is not

Within the radiative-limited simplified-Kane class:

### Structurally robust

- radiative dark generation is tied to the equilibrium absorption spectrum by detailed balance;
- the explicit Kane optical prefactor cancels from `R_rad/a_0` at fixed target capture;
- finite-frequency transport retains a fine-structure-scale `alpha_fs` dependence;
- the optimum gap depends on the temporal task and source flux;
- increasing demanded speed shifts the optimum toward smaller gaps in the illustrated regime.

### Not universal

- the numerical optimum `x_g`;
- the assumed chemical potential;
- radiative dominance;
- the refractive index approximation;
- the collection probability and velocity;
- the optimum after Auger, SRH, tunneling, or surface leakage are included.

---

# 12. Novelty posture

Detailed-balance radiative generation, direct-gap phase-space asymptotics, Kane optical conductivity, and absorption/transit-time tradeoffs are all prior physics.

The candidate UPRP contribution is the **source-information resource phase diagram** and the proof that no detector-independent optimal gap exists without specifying source/task/dark resources.

No novelty claim should be made for the numerical phase diagram until theorem-level literature comparison is complete.

---

# 13. Next work

1. Regularize the heavy-hole sector and chemical potential using finite heavy-hole curvature or a finite 8-band Kane model.
2. Recompute `F_{K,T}`, `I_K`, and the phase diagram self-consistently at fixed carrier density or intrinsic neutrality.
3. Add one nonradiative dark mechanism at a time and quantify movement of the optimum.
4. Explore a lower bound based on external blackbody/background photon modes rather than volumetric internal radiative generation, including photon recycling/escape.
5. Determine whether an analytic bound can be stated on the optimum location or its monotonic movement with normalized task frequency.

---

# Status

**DERIVED dimensionless phase diagram and large-gap asymptotic for the restricted radiative-Kane model.**