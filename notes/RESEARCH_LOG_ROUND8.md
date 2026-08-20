# Research Log — Round 8

**Date:** 2026-08-20

## Purpose

Durable checkpoint after the project moved from abstract resource-completeness into a joint optical-capture / semiconductor-transport / finite-temperature dark-generation analysis.

The repository, not chat history, is authoritative. This log records the reasoning transitions and corrections that matter for takeover.

---

# 1. Joint optical/transport gate: total absorption is not enough

WP11 showed that deterministic transit latency is not itself information loss. Unresolved delay dispersion is.

The attempted direct composition of total finite-band optical absorption with carrier velocity failed because **optical matching thickness is not the same as active carrier-generation thickness**. Passive spacers/resonators can provide matching while dissipation occurs in a thin active region.

This identified a missing quantity: localized capture capacity in **electrical delay space**, not total optical volume.

---

# 2. WP15 delay-concentration theorem

For capture efficiency `eta_c` and conditional electrical-event delay `D`, the ideal timestamp-record FI is

\[
\eta_I(\Omega)=\eta_c|\phi_D(\Omega)|^2.
\]

For a flat modulation-information band,

\[
\bar\eta_I
=\eta_c\,\mathbb E[\operatorname{sinc}(\Omega_s(D-D'))].
\]

Define the absolute localized incident-photon capture fraction

\[
M_D(\Delta t)=\eta_c\sup_a\Pr[D\in[a,a+\Delta t]].
\]

For any `x>0`, with

\[
c_x=\sup_{|u|\ge x}|\operatorname{sinc}u|,
\]

proved

\[
\boxed{
\bar\eta_I
\le c_x+(1-c_x)M_D(2x/\Omega_s).
}
\]

Thus target `q>c_x` requires

\[
\boxed{
M_D(2x/\Omega_s)\ge\frac{q-c_x}{1-c_x}.
}
\]

For `x=pi/2`, `c_x=2/pi` and the delay window is `1/(2f_s)`.

Required localized capture fractions:

- `q=0.90`: about 72.5%;
- `q=0.95`: about 86.2%;
- `q=0.99`: about 97.2%.

Primary note: `notes/WP15_DELAY_CONCENTRATION_AND_LOCALIZED_CAPTURE_CAPACITY.md`.

---

# 3. WP16 restricted local-absorption theorem

Using Miller et al.'s prior passive per-volume absorption bound

\[
\sigma_{abs}/V\le k|\chi|^2/\operatorname{Im}\chi,
\]

for a restricted planar class in which the active material itself occupies the delay slice and there is no external passive concentrator, obtained

\[
M_D(\Delta t)
\le\min[1,\mathcal M_Bv\Delta t],
\]

\[
\mathcal M_B=\sup_B k|\chi|^2/\operatorname{Im}\chi.
\]

Hence

\[
\bar\eta_I
\le c_x+(1-c_x)\min[1,2x\mathcal M_Bv/\Omega_s].
\]

This is a valid restricted joint optical-material/transport theorem, but representative LWIR values make it extremely loose (optical/tens-of-THz scale). That motivated a semiconductor-specific band-Hamiltonian closure.

Primary note: `notes/WP16_LOCAL_ABSORPTION_TRANSPORT_INFORMATION_BOUND.md`.

---

# 4. WP17 exact massless 6-band Kane coefficient

For the intrinsic gapless simplified `6 x 6` Kane model,

\[
E_0=0,\qquad E_\pm=\pm\hbar v_Kk,
\]

direct projector/Kubo algebra gives angular matrix weights

\[
\overline M_{0\to+}=1/2,
\qquad
\overline M_{-\to+}=1/3.
\]

The two conductivity pieces are

\[
\sigma_{0+}=\frac{e^2\omega}{4\pi\hbar v_K},
\]

\[
\sigma_{-+}=\frac{e^2\omega}{48\pi\hbar v_K}.
\]

Therefore

\[
\boxed{
\operatorname{Re}\sigma_K
=\frac{13e^2\omega}{48\pi\hbar v_K}.
}
\]

Flat-to-cone : cone-to-cone spectral weight = `12:1`.

This exactly matches Orlita et al.'s prior analytic dielectric function

\[
\epsilon=\epsilon_\infty+
\frac{13}{12}\alpha_{fs}\frac c{v_K}
\left[\frac2\pi\ln(\omega_c/|\omega|)+i\operatorname{sgn}\omega\right].
\]

**Do not claim the conductivity/dielectric coefficient as new.**

The exact conductivity product satisfies

\[
\boxed{
v_K\operatorname{Re}\sigma_K
=\frac{13e^2\omega}{48\pi\hbar}.
}
\]

Physical absorption-depth product `a v_K` is only approximately velocity independent because `n+i kappa=sqrt(epsilon)` also contains `v_K`. In weak loss,

\[
\boxed{
a v_K/\omega\simeq\frac{13}{12n}\alpha_{fs}.}
\]

For Beer-Lambert depth and deterministic collection,

\[
\eta_I(\Omega)
=\eta_c\frac{(av)^2}{(av)^2+\Omega^2}.
\]

Idealized critical-HgCdTe at `10.6 um` gives an optimistic tens-of-GHz scale, not a real detector prediction.

Primary note: `notes/WP17_MASSLESS_KANE_ABSORPTION_TRANSPORT_INFORMATION_THEOREM.md`.

---

# 5. Critical novelty correction: alpha*v bandwidth tradeoff is prior art

Classical vertically illuminated photodiode theory already derives bandwidth-efficiency products of the form

\[
B\eta\propto\alpha_{abs}v
\]

and one located source gives an ideal coefficient around `0.55 alpha v`.

Therefore **do not claim**:

- absorption-depth versus transit-time tradeoff;
- `alpha_abs v` as a new material speed-efficiency figure;
- Kane optical conductivity as new.

Candidate value of WP17 is the exact Kane microscopic coefficient, the source-FI formulation, and its role inside the larger resource-completeness chain.

Issue #11 tracks this novelty gate.

---

# 6. WP18 finite positive Kane gap

Let

\[
y=E_g/(\hbar\omega),\qquad0\le y<1.
\]

Exact zero-temperature interband conductivities in the simplified massive Kane model:

\[
\boxed{
\sigma_{0+}
=\frac{e^2\omega}{4\pi\hbar v_K}\sqrt{1-y},
}
\]

\[
\boxed{
\sigma_{-+}
=\frac{e^2\omega}{48\pi\hbar v_K}
(1+2y^2)\sqrt{1-y^2}.
}
\]

Thus

\[
\operatorname{Re}\sigma_K
=\frac{e^2\omega}{48\pi\hbar v_K}F_K(y),
\]

\[
F_K(y)=12\sqrt{1-y}+(1+2y^2)\sqrt{1-y^2}.
\]

Exact `v_K sigma` cancellation survives the gap.

Fastest dominant flat-to-conduction photoelectron group velocity:

\[
\boxed{
u_0(y)=\frac{2\sqrt{1-y}}{2-y}.}
\]

Weak-loss useful depth/transport factor:

\[
\frac{\Gamma}{\omega}
\lesssim\frac{\alpha_{fs}}{12n}G_K(y),
\qquad
G_K=F_Ku_0.
\]

At `T=0`, `G_K` decreases from `13` at zero gap to zero at the optical threshold. So opening the gap monotonically worsens this capture/ballistic layer. Any full optimum must arise from a dark/noise benefit.

Primary note: `notes/WP18_FINITE_GAP_KANE_ABSORPTION_TRANSPORT_BOUND.md`.

---

# 7. WP19 radiative detailed-balance floor

Use the established van Roosbroeck-Shockley relation

\[
R_{rad}
=\int_{\omega_g}^\infty
\frac{n^2\omega^2}{\pi^2c^2}
a(\omega,T)
\frac{d\omega}{e^{\hbar\omega/k_BT}-1}.
\]

With finite-temperature Kane occupation factors, define

\[
F_{K,T}(x;x_g,\bar\mu)
\]

and

\[
\mathcal I_K(x_g,\bar\mu)
=\int_{x_g}^\infty
\frac{x^3F_{K,T}(x;x_g,\bar\mu)}{e^x-1}dx.
\]

Then

\[
R_{rad}^{K}
=\frac{n\alpha_{fs}}{12\pi^2c^2v_K}
(k_BT/\hbar)^4\mathcal I_K.
\]

For a planar absorber just thick enough to achieve target capture `eta_c`, the radiative-dark/useful-signal ratio is

\[
\delta_{rad}
=\frac{-\ln(1-\eta_c)}{\eta_c}
\frac{n^2}{\pi^2c^2\phi_s}
\frac{(k_BT/\hbar)^4}{\omega_0}
\frac{\mathcal I_K}{F_0}.
\]

**Second Kane cancellation:** explicit `alpha_fs` and `v_K` cancel from this radiative-dark/signal ratio.

Finite-slab delay transfer:

\[
H(r)=\frac{1-(1-\eta_c)e^{-irs}}{\eta_c(1+ir)},
\quad
s=-\ln(1-\eta_c),
\]

and

\[
\eta_I(\Omega)
=\frac{\eta_c}{1+\delta_{rad}}|H|^2.
\]

Primary note: `notes/WP19_KANE_RADIATIVE_DETAILED_BALANCE_INFORMATION_MODEL.md`.

---

# 8. WP20 no universal optimal Eg/kT

For normalized gap `y`, generic activated dark rate

\[
d(y)=d_0e^{-by},
\]

and normalized transport factor `h(y)=G_K(y)/13`,

\[
\eta_I(y)
=\frac1{1+Ae^{-by}}
\frac{h(y)^2}{h(y)^2+r^2}.
\]

Exact logarithmic derivative:

\[
\frac{d\ln\eta_I}{dy}
=b\frac{Ae^{-by}}{1+Ae^{-by}}
+2\frac{h'}h\frac{r^2}{h^2+r^2}.
\]

Since `h'(0)=-6/13`,

\[
\left.\frac{d\ln\eta_I}{dy}\right|_0
=\frac{bA}{1+A}
-\frac{12}{13}\frac{r^2}{1+r^2}.
\]

Thus whether opening a gap helps depends explicitly on dark prefactor/mechanism, source photon flux, temperature, optical carrier, and demanded temporal frequency.

\[
\boxed{
\{T,\hbar\omega_0\}\not\Rightarrow\text{unique optimal }E_g.
}
\]

Primary note: `notes/WP20_DARK_MECHANISM_NONUNIVERSALITY_THEOREM.md`.

---

# 9. WP21 dimensionless radiative-Kane phase diagram

Define

\[
x_0=\hbar\omega_0/k_BT,
\quad
x_g=E_g/k_BT,
\quad
\rho=\Omega/\omega_0,
\]

and thermal photon-flux density scale

\[
\phi_T
=\frac{n^2}{\pi^2c^2}
\frac{(k_BT/\hbar)^4}{\omega_0},
\qquad
\psi=\phi_s/\phi_T.
\]

Then

\[
\boxed{
\delta_{rad}
=\frac{s}{\eta_c\psi}\frac{\mathcal I_K}{F_0},
}
\]

\[
\boxed{
r
=\frac{12n\rho}{\alpha_{fs}F_0u_0}.
}
\]

The full idealized phase diagram therefore depends on

\[
\boxed{(x_0,\psi,\rho,\eta_c,n,\bar\mu)}.
\]

Large-gap radiative asymptotic:

\[
\boxed{
\mathcal I_K(x_g)
\sim
(12+3\sqrt2)\frac{\sqrt\pi}{2}
\,x_g^{5/2}e^{-x_g}.
}
\]

Illustrative `300 K`, `10.6 um`, `eta_c=.9`, `n=3.2`, `mu=0` model:

- DC radiative optimum `x_g ~= 3.635`;
- increasing information frequency shifts optimum toward smaller gap;
- at `psi=100`, optimum moves approximately `3.63 -> 2.75 -> 1.99 -> 1.40` for `0 -> 10 -> 20 -> 50 GHz`.

This is structural only; the ideal flat heavy-hole band makes a self-consistent intrinsic chemical potential UV-sensitive.

Primary note: `notes/WP21_DIMENSIONLESS_RADIATIVE_KANE_PHASE_DIAGRAM.md`.

---

# 10. New highest-priority gap

The six-band flat heavy-hole sector is now the dominant technical limitation of the finite-temperature Kane phase diagram.

Need to regularize it with one of:

1. finite heavy-hole curvature in an 8-band Kane model;
2. a controlled finite cutoff plus charge-neutrality condition;
3. a realistic DOS model sufficient to determine `mu(T,E_g,n_doping)`.

Then recompute the finite-temperature interband occupation factors and radiative integral self-consistently.

The goal is not a realistic TCAD detector. It is to determine which qualitative phase-diagram results survive a physically finite DOS.

---

# 11. Novelty posture at end of Round 8

Prior art definitely occupies:

- conventional absorption-depth/transit-time bandwidth-efficiency tradeoff;
- Kane optical conductivity/dielectric response;
- van Roosbroeck-Shockley detailed balance;
- generic photodiode dark-current/bandwidth optimization;
- optical sum rules and passive material limits.

Potentially distinct project contribution remains the **resource-completeness structure and source-information formulation**:

\[
\text{incident optical FI}
\to\text{localized capture}
\to\text{delay dispersion}
\to\text{semiconductor band transport}
\to\text{dark-event dilution}
\to\text{intrinsic electrical FI},
\]

with explicit no-go results showing why natural smaller resource sets fail.

No final novelty claim yet.
