# WP17 — Massless Kane absorption–transport information theorem

**Date:** 2026-08-20

## Purpose

WP15–WP16 establish that information bandwidth in a surface-illuminated detector is constrained by the ability to localize optical capture into a narrow electrical-delay window. The generic passivity bound in WP16 is rigorous but very loose for LWIR HgCdTe.

This note specializes to the analytically solvable gapless `6 x 6` Kane Hamiltonian relevant to critical-composition HgCdTe. In this model the same Kane velocity controls both interband optical matrix elements and ballistic carrier transport. That shared microscopic origin produces a much sharper absorption-depth/transport information scale.

The result is restricted to the idealized massless Kane model and is **not** a full room-temperature HgCdTe detector bound. Thermal dark carriers, finite gap, scattering, recombination, contacts, electrostatics, and readout remain separate resource layers.

---

# 1. Gapless simplified Kane Hamiltonian

Neglect the split-off Gamma_7 band and quadratic-in-momentum corrections. At the critical point `E_g=0`, the simplified Kane Hamiltonian is

\[
H_K=\hbar v_K\,\mathbf k\cdot\mathbf J,
\]

where `J_i` are the non-spin-1 Kane matrices. The spectrum is

\[
\boxed{E_0=0,\qquad E_\pm=\pm\hbar v_K k,}
\]

and every band is doubly degenerate.

Orlita et al. experimentally/theoretically find `v_K ~ 1.06e6 m/s`; Teppe et al. later report a nearly composition- and temperature-independent value `(1.07 +/- 0.05)e6 m/s` near the transition.

Primary literature:

- M. Orlita et al., Nature Physics 10, 233–238 (2014), DOI `10.1038/nphys2857`.
- F. Teppe et al., Nature Communications 7, 12576 (2016), DOI `10.1038/ncomms12576`.
- J. D. Malcolm and E. J. Nicol, Phys. Rev. B 92, 035118 (2015), DOI `10.1103/PhysRevB.92.035118`.

---

# 2. Exact zero-field interband conductivity coefficient

At `T=0`, intrinsic filling with chemical potential `0+` fills the lower cone and the flat heavy-hole band while leaving the upper cone empty.

For an x-polarized optical field define `A_x = v_x/v_K`. With projectors `P_+`, `P_0`, `P_-` onto the upper, flat, and lower bands, direct algebra with the 6x6 Kane matrices gives for momentum direction `n = k/k`:

\[
\boxed{
\operatorname{Tr}(P_+A_xP_0A_x)
=\frac34(1-n_x^2),
}
\]

\[
\boxed{
\operatorname{Tr}(P_+A_xP_-A_x)
=\frac12(1-n_x^2).
}
\]

Angular averaging `\langle1-n_x^2\rangle=2/3` gives

\[
\boxed{
\overline M_{0\to+}=\frac12,
\qquad
\overline M_{-\to+}=\frac13.
}
\]

The transition energies are

\[
\Delta E_{0\to+}=\hbar v_K k,
\qquad
\Delta E_{-\to+}=2\hbar v_K k.
\]

For a 3D linear band, the shell integral contributes an additional `a^{-3}` when `Delta E=a hbar v k`. Consequently

\[
\operatorname{Re}\sigma_{0\to+}
=\frac{e^2\omega}{4\pi\hbar v_K}
=\frac{12e^2\omega}{48\pi\hbar v_K},
\]

whereas

\[
\operatorname{Re}\sigma_{-\to+}
=\frac{e^2\omega}{48\pi\hbar v_K}.
\]

Therefore

\[
\boxed{
\operatorname{Re}\sigma_K(\omega)
=\frac{13e^2}{48\pi\hbar v_K}\,\omega.
}
\]

The spectral-weight fractions are exactly

\[
\boxed{
\text{flat-to-cone}:\text{cone-to-cone}=12:1.
}
\]

This analytically explains Malcolm–Nicol's observation that the major zero-field absorption weight comes from flat-to-cone transitions.

**Status:** PROVED by direct Kane-matrix/Kubo evaluation.

---

# 3. Independent literature confirmation through the dielectric function

Orlita et al. analytically derive for the same intrinsic massless Kane model, below the high-energy cutoff `omega_c`,

\[
\boxed{
\epsilon(\omega)
=\epsilon_\infty
+B\left[
\frac{2}{\pi}\ln\frac{\omega_c}{|\omega|}
+i\,\operatorname{sgn}\omega
\right],
}
\]

with

\[
\boxed{
B=\frac{13}{12}\alpha_{\rm fs}\frac{c}{v_K}.
}
\]

Since

\[
\operatorname{Re}\sigma
=\epsilon_0\omega\operatorname{Im}\epsilon,
\]

this gives exactly

\[
\operatorname{Re}\sigma
=\frac{13e^2\omega}{48\pi\hbar v_K},
\]

confirming Sec. 2.

This conductivity formula and the dielectric function are **prior art**. UPRP must not claim them as new.

---

# 4. Exact bulk absorption coefficient in the Kane model

Write

\[
\epsilon_1(\omega)
=\epsilon_\infty
+\frac{2B}{\pi}\ln\frac{\omega_c}{|\omega|},
\qquad
\epsilon_2=B
\]

for positive optical frequency.

Let

\[
\tilde n=n+i\kappa=\sqrt{\epsilon_1+i\epsilon_2}.
\]

Then

\[
\boxed{
\kappa(\omega)
=\sqrt{
\frac{\sqrt{\epsilon_1^2+B^2}-\epsilon_1}{2}
}.
}
\]

The intensity absorption coefficient is

\[
\boxed{
a_K(\omega)=\frac{2\kappa(\omega)\omega}{c}.
}
\]

Therefore the exact Kane absorption-depth/ballistic-transport rate scale is

\[
\boxed{
\Gamma_K(\omega)
=a_K(\omega)v_K
=2\kappa(\omega)\frac{v_K}{c}\,\omega.
}
\]

---

# 5. Exact versus approximate velocity cancellation

The conductivity product satisfies the **exact** cancellation

\[
\boxed{
v_K\operatorname{Re}\sigma_K(\omega)
=\frac{13e^2}{48\pi\hbar}\omega.
}
\]

However, the physical absorption coefficient depends on `sqrt(epsilon)`, and `epsilon_2` itself contains `c/v_K`. Thus `a_K v_K` is not exactly independent of `v_K`.

In the weak-loss/background-index regime

\[
\epsilon_2\ll\epsilon_1,
\qquad n\simeq\sqrt{\epsilon_1},
\]

one has

\[
\kappa\simeq\frac{B}{2n},
\]

so

\[
\boxed{
\Gamma_K(\omega)
\simeq
\frac{13}{12n}\alpha_{\rm fs}\,\omega.
}
\]

Here the Kane velocity cancels to leading order.

**Important correction:** describe the velocity cancellation as exact for `sigma v_K` and approximate for the actual absorption-depth rate `a_K v_K` unless the weak-loss approximation is explicitly stated.

---

# 6. Exponential absorption-depth delay law

Consider an ideal semi-infinite homogeneous Kane absorber illuminated from the electrical collection side.

Conditional on successful bulk absorption, Beer-Lambert absorption gives

\[
p_Z(z)=a_K e^{-a_Kz},\qquad z\ge0.
\]

Assume deterministic collection velocity

\[
0<v_{\rm col}\le v_K
\]

and delay

\[
D=z/v_{\rm col}.
\]

Then

\[
\boxed{
\phi_D(\Omega)
=\mathbb E[e^{-i\Omega D}]
=\frac{a_Kv_{\rm col}}
{a_Kv_{\rm col}+i\Omega}.
}
\]

For total incident-to-event capture probability `eta_c`, the ideal Poisson event-record information transfer is

\[
\boxed{
\eta_{\mathcal I}(\Omega)
=\eta_c
\frac{(a_Kv_{\rm col})^2}
{(a_Kv_{\rm col})^2+\Omega^2}.
}
\]

This is a Lorentzian information spectrum generated by the exponential absorption-depth distribution.

**Status:** PROVED within the Beer-Lambert/constant-velocity/event-record assumptions.

---

# 7. Best-case massless-Kane material ceiling

Because

\[
v_{\rm col}\le v_K,
\]

additional transport limitations can only reduce the depth-to-delay rate scale relative to the ideal ballistic value.

Thus, within the homogeneous massless-Kane active-material class,

\[
\boxed{
\eta_{\mathcal I}(\Omega)
\le
\eta_c
\frac{\Gamma_K^2}
{\Gamma_K^2+\Omega^2},
}
\]

with

\[
\Gamma_K=2\kappa(\omega_0)(v_K/c)\omega_0.
\]

This should be interpreted as a best-case **capture-depth + ballistic-transport layer** ceiling, not as a complete detector theorem.

---

# 8. Edge-band information conditions

## 8.1 Absolute incident-information target

If the requirement is

\[
\eta_{\mathcal I}(\Omega_s)\ge q,
\]

then necessarily `eta_c>=q` and

\[
\boxed{
\Omega_s
\le
\Gamma_K
\sqrt{\frac{\eta_c-q}{q}}.
}
\]

The optimistic `eta_c=1` ceiling is

\[
\boxed{
\frac{\Omega_s}{\omega_0}
\le
2\kappa(\omega_0)\frac{v_K}{c}
\sqrt{\frac{1-q}{q}}.
}
\]

## 8.2 Retention relative to DC detector information

If instead one asks to retain fraction `r` of the detector's own zero-frequency information,

\[
\eta_{\mathcal I}(\Omega_s)
\ge r\,\eta_{\mathcal I}(0),
\]

then

\[
\boxed{
\Omega_s
\le
\Gamma_K\sqrt{\frac{1-r}{r}}.
}
\]

This separates capture efficiency from transit-dispersion retention.

---

# 9. Weak-loss fine-structure form

Using

\[
\Gamma_K/\omega_0
\simeq
\frac{13}{12n}\alpha_{\rm fs},
\]

the optimistic edge condition becomes

\[
\boxed{
\frac{\Omega_s}{\omega_0}
\lesssim
\frac{13}{12n}\alpha_{\rm fs}
\sqrt{\frac{1-q}{q}}.
}
\]

Equivalently, because the ratio of angular frequencies equals the ratio of ordinary frequencies,

\[
\boxed{
\frac{f_s}{f_0}
\lesssim
\frac{13}{12n}\alpha_{\rm fs}
\sqrt{\frac{1-q}{q}}.
}
\]

This is the clearest form of the Kane absorption-depth/ballistic-information compensation.

The small dimensionless factor is set by the electromagnetic fine-structure constant divided by the optical index, multiplied by the Kane flat-band coefficient `13/12`.

---

# 10. Numerical critical-HgCdTe illustration at 10.6 um

Use only as an **idealized massless-Kane illustration**, not a practical detector prediction.

Representative inputs from Orlita et al.:

\[
v_K=1.06\times10^6\ {\rm m/s},
\]

\[
\epsilon_\infty\simeq6,
\qquad
\hbar\omega_c\simeq1.5\ {\rm eV}.
\]

At

\[
\lambda_0=10.6\ \mu{\rm m},
\qquad
\hbar\omega_0\simeq0.117\ {\rm eV},
\]

the analytic dielectric model gives approximately

\[
\epsilon_1\simeq9.63,
\qquad
\epsilon_2\simeq2.24,
\]

\[
n\simeq3.12,
\qquad
\kappa\simeq0.358.
\]

Thus

\[
\Gamma_K/\omega_0
=2\kappa v_K/c
\simeq2.53\times10^{-3}.
\]

For an optimistic absolute capture `eta_c=1` and edge information target `q=0.90`,

\[
\frac{f_s}{f_0}
\lesssim8.44\times10^{-4}.
\]

Since

\[
f_0\simeq28.28\ {\rm THz},
\]

this gives

\[
\boxed{f_s\lesssim23.9\ {\rm GHz}.}
\]

Orlita et al. report an experimental extinction coefficient `kappa=0.47 +/- 0.02` over the linear absorption regime; using that measured value in the same ideal transport model gives a scale around `31 GHz` for the same 90% edge-retention criterion.

These numbers are **not** predictions of a real HgCdTe detector bandwidth. They intentionally omit dark carriers, scattering, recombination, finite gap, electrostatics, contacts, capacitance, and readout.

---

# 11. Why this is potentially stronger than WP16

WP16 used the generic passive material figure

\[
k|\chi|^2/\operatorname{Im}\chi,
\]

which can be extremely large and gave optical-scale/tens-of-THz ceilings for representative LWIR parameters.

The Kane model ties absorption and transport to the same microscopic `k.p` matrix element. The resulting rate is instead of order

\[
\boxed{
\Gamma_K\sim\alpha_{\rm fs}\omega_0,
}
\]

up to order-unity Kane/index factors.

This moves the restricted bound into the tens-of-GHz regime for a 10-um optical carrier.

---

# 12. Conventional photodiode tradeoff versus UPRP statement

The engineering tradeoff between absorption depth, quantum efficiency, and carrier transit time is longstanding prior art. Conventional photodiode literature contains formulas in which bandwidth scales with combinations such as `alpha_abs v`.

Therefore UPRP must **not** claim discovery of the generic absorption-depth/transit-time tradeoff.

The candidate distinct contribution is narrower:

1. use source-normalized optical-to-electrical Fisher information rather than amplitude response;
2. derive the exact Kane-band coefficient from the same microscopic Hamiltonian controlling transport;
3. identify the fine-structure-scale cancellation/compensation;
4. place this result inside the larger resource-completeness chain with optical capture, dark counts, thermokinetic conversion, and readout coarse graining.

Novelty remains provisional pending a theorem-level literature audit.

---

# 13. Important limitations

The theorem does not yet include:

- positive or negative finite Kane mass/gap;
- Fermi blocking and finite carrier density;
- finite temperature occupation factors;
- heavy-hole curvature;
- finite split-off energy beyond the six-band approximation;
- carrier scattering or velocity saturation below `v_K`;
- electron/hole asymmetry in actual collection;
- surface reflection/AR/cavity effects except through `eta_c`;
- dark counts / equilibrium thermal generation;
- recombination and trapping;
- electrical weighting-field geometry;
- external readout noise.

In particular, **gapless HgCdTe is not a realistic low-dark-noise LWIR detector material at room temperature**. This result isolates the optical-capture/ballistic-transport layer only.

---

# 14. Next mathematical tasks

1. Derive the finite-mass simplified Kane optical conductivity and corresponding `a(E_g,omega)v` product.
2. Include Fermi-Dirac occupation factors and establish the finite-temperature correction.
3. Compose with the existing dark-count information factor

\[
\eta_{\rm dark}
=\eta_c/[1+d/(\eta_c\Phi_0)].
\]

4. Determine whether a finite-gap high-operating-temperature Kane detector exhibits a nontrivial optimum between reduced thermal dark generation and increased optical absorption depth / reduced transport speed.
5. Audit prior photodiode theory for any explicit derivation of the `13/12 alpha_fs` Kane absorption-depth/transit-speed product or equivalent detector-bandwidth law.
6. Only after that novelty gate, evaluate whether this supports a publishable UPRP theorem or is best used as a physically revealing example.

---

# Status

**PROVED under the ideal intrinsic massless 6-band Kane + Beer-Lambert + ballistic event-record assumptions.**

**NOVELTY:** provisional. The underlying Kane dielectric/conductivity is prior art; the photodetection-information composition requires further audit.