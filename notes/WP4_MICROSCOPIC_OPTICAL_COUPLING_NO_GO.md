# WP4 — Microscopic Optical-Coupling Completion and No-Go Theorem

**Date:** 2026-08-19

## Objective

Replace the abstract reverse optical gateway rate `d` in `WP3_GATEWAY_RESOURCE_THEOREM.md` by a microscopic light–matter coupling model and determine whether temperature, photon energy, photon throughput, stationary activity, and entropy production are sufficient to impose a finite photodetection speed limit.

**Main result:** they are not. Even after fixing the optical detailed-balance ratio associated with a fixed photon energy and optical reservoir occupation/temperature, one can construct a fully reversible three-state Markov photodetector family with bounded total activity, bounded entropy-production rate, finite nonzero optical throughput, finite nonzero detection probability, and timing bandwidth diverging linearly with a microscopic light–matter coupling scale.

Therefore an absolute optical coupling resource must appear in any finite universal speed bound.

---

# 1. Microscopic bosonic-reservoir map

For a weakly coupled two-level optical transition of frequency `omega_0` interacting with a stationary bosonic reservoir, the Born–Markov–secular form has upward/downward rates

\[
\Gamma_\uparrow=\gamma(\omega_0)n(\omega_0),
\qquad
\Gamma_\downarrow=\gamma(\omega_0)[n(\omega_0)+1],
\]

where `gamma(omega_0)` is the local light–matter spectral coupling scale and `n(omega_0)` is the reservoir occupation.

For a thermal photon bath,

\[
n_T(\omega_0)=\frac{1}{e^{\beta\hbar\omega_0}-1},
\]

and

\[
\frac{\Gamma_\uparrow}{\Gamma_\downarrow}
=\frac{n_T}{n_T+1}
=e^{-\beta\hbar\omega_0}.
\]

Thus fixed `T` and fixed `hbar omega_0` fix the **ratio** of optical rates, but not their absolute common scale `gamma(omega_0)`.

This is the key microscopic distinction missed by a theorem stated only in terms of detailed balance.

For example, at `lambda = 10 um` and `T=300 K`,

\[
\beta\hbar\omega\approx4.796,
\qquad
n_T\approx8.33\times10^{-3},
\]

so

\[
\Gamma_\uparrow/\Gamma_\downarrow\approx8.26\times10^{-3}.
\]

The ratio is fixed, but the absolute rates can still be rescaled by changing the light–matter coupling / optical LDOS unless that resource is constrained.

---

# 2. Detailed-balance-preserving rare-fast family

Consider three states:

- `0`: ready state;
- `1`: post-absorption optical gateway;
- `2`: downstream/readout/reset state.

Define the reversible transition rates

\[
0\xrightleftharpoons[bR]{aR}1,
\qquad
1\xrightleftharpoons[q]{cR}2,
\qquad
2\xrightleftharpoons[sR]{p}0,
\]

with fixed constants

\[
a,b,c,p,q,s>0,
\qquad R>0.
\]

The signal-facing optical detailed-balance ratio is

\[
\boxed{\frac{u_R}{d_R}=\frac{a}{b},}
\]

which is independent of `R`.

Hence, if desired, one may impose

\[
\frac{a}{b}=e^{-\beta\hbar\omega_0}
\]

for a fixed thermal optical reservoir. Equivalently, write

\[
aR=\gamma_R n_T,
\qquad
bR=\gamma_R(n_T+1),
\]

with

\[
\gamma_R\propto R.
\]

The family changes only the absolute microscopic coupling scale while preserving the optical thermodynamic ratio.

---

# 3. Exact stationary distribution

The stationary balance equations are

\[
0=bR\pi_1+p\pi_2-(a+s)R\pi_0,
\]

\[
0=aR\pi_0+q\pi_2-(b+c)R\pi_1.
\]

Write

\[
\pi_0=\frac{x}{R}\pi_2,
\qquad
\pi_1=\frac{y}{R}\pi_2.
\]

Then `x,y` satisfy the `R`-independent system

\[
(a+s)x-by=p,
\]

\[
-ax+(b+c)y=q.
\]

Define

\[
\Delta=(a+s)(b+c)-ab
=ac+s(b+c)>0.
\]

Then

\[
\boxed{x=\frac{p(b+c)+bq}{\Delta}>0,}
\]

\[
\boxed{y=\frac{(a+s)q+ap}{\Delta}>0.}
\]

Normalization gives the **exact** stationary probabilities

\[
\boxed{
\pi_0(R)=\frac{x}{R+x+y},
\qquad
\pi_1(R)=\frac{y}{R+x+y},
\qquad
\pi_2(R)=\frac{R}{R+x+y}.
}
\]

Therefore

\[
\pi_0,\pi_1=O(R^{-1}),
\qquad
\pi_2\to1.
\]

Both states carrying `O(R)` transition rates become proportionally rare.

---

# 4. Finite nonzero optical throughput

The forward optical absorption traffic is

\[
f_R=aR\pi_0
=\frac{axR}{R+x+y}.
\]

Hence

\[
\boxed{f_R\to ax>0.}
\]

Thus for sufficiently large `R`, the family satisfies a fixed nonzero useful-throughput condition

\[
f_R\ge f_*>0
\]

for any `f_*<ax`.

This eliminates the trivial loophole in which speed increases only because the detector stops absorbing photons.

---

# 5. Total stationary activity remains bounded

The state escape rates are

\[
\lambda_0=(a+s)R,
\qquad
\lambda_1=(b+c)R,
\qquad
\lambda_2=p+q.
\]

Using the repository convention

\[
\mathcal A_R=\sum_j\pi_j\lambda_j,
\]

we obtain

\[
\mathcal A_R
=
\frac{R}{R+x+y}
\left[x(a+s)+y(b+c)+p+q\right].
\]

Therefore

\[
\boxed{
\mathcal A_R\to
x(a+s)+y(b+c)+p+q<\infty.
}
\]

All diverging bare rates are hidden on states whose stationary occupation decreases as `1/R`.

**Status:** PROVED.

---

# 6. Entropy production remains bounded — even edge by edge

The stationary directed traffics on the three reversible edge pairs are proportional to

\[
ax \leftrightarrow by,
\qquad
cy \leftrightarrow q,
\qquad
p \leftrightarrow sx,
\]

all multiplied by the common prefactor

\[
\frac{R}{R+x+y}.
\]

The stationary cycle current is

\[
J_0=ax-by.
\]

Using the balance equations,

\[
\boxed{
J_0=ax-by=cy-q=p-sx.
}
\]

Hence the actual cycle current is

\[
J_R=\frac{R}{R+x+y}J_0,
\]

which has a finite limit.

The cycle affinity is

\[
\boxed{
\mathcal F
=\ln\frac{(aR)(cR)p}{(bR)q(sR)}
=\ln\frac{acp}{bqs},
}
\]

also independent of `R`.

Therefore the dimensionless steady EPR is

\[
\boxed{
\sigma_R
=J_R\mathcal F
\to
J_0\ln\frac{acp}{bqs},
}
\]

with the usual orientation chosen so the product is nonnegative.

Stronger still, every individual edge EPR contribution remains finite because each pair of stationary one-way traffics tends to finite constants and each traffic ratio is `R`-independent.

Thus this counterexample cannot be repaired merely by replacing total EPR by a finite set of edge-resolved EPRs.

**Status:** PROVED.

---

# 7. Timing speed diverges

After an optical absorption event `0 -> 1`, the total first-exit rate from the gateway state is

\[
\boxed{
\lambda_1(R)=(b+c)R.
}
\]

The first-exit waiting time is

\[
T_1\sim\mathrm{Exp}[(b+c)R],
\]

so

\[
\mathbb E[T_1]=\frac{1}{(b+c)R},
\qquad
\operatorname{sd}(T_1)=\frac{1}{(b+c)R}.
\]

If `1 -> 2` is the electrical detection branch, the probability that the first exit is a successful detection is

\[
\boxed{
\eta_{\rm branch}=\frac{c}{b+c},
}
\]

which is independent of `R` and strictly positive.

Conditioned on that successful branch, the waiting-time distribution retains the same exponential clock because jump time and destination are independent for competing exponential hazards.

Therefore the event timing transfer factor contains

\[
H_R(\omega)
=\frac{(b+c)R}{(b+c)R+i\omega},
\]

and its characteristic timing bandwidth grows as

\[
\boxed{
\Omega_{\rm timing}\sim(b+c)R\to\infty.
}
\]

Thus the detector can retain a fixed nonzero detection probability and fixed nonzero optical throughput while its post-absorption timing scale becomes arbitrarily fast.

**Status:** PROVED.

---

# 8. No-go theorem

## Theorem — thermodynamic ratios do not set an absolute photodetection speed scale

Within the finite-state reversible Markov event-detector class, no finite universal upper bound on post-absorption timing bandwidth can be a function only of

\[
\{T,\hbar\omega_0,f_*,\mathcal A,\sigma,\eta_{\rm branch}\}
\]

or, more generally, of quantities that remain unchanged under a common rescaling of the absolute light–matter coupling while only stationary traffic is constrained.

The family above keeps:

- optical frequency fixed;
- optical detailed-balance ratio fixed;
- optical temperature/occupation ratio fixed;
- forward optical throughput finite and nonzero;
- total activity finite;
- total EPR finite;
- every edge EPR finite;
- successful detection branch probability finite and nonzero;

while

\[
\Omega_{\rm timing}\to\infty.
\]

Therefore a finite universal speed theorem requires at least one resource that controls the **absolute microscopic transition scale**.

Candidate resources include

\[
\gamma(\omega_0),
\quad
J_{\rm EM}(\omega_0),
\quad
\rho_{\rm LDOS}(\omega_0)|d_{01}|^2,
\quad
\|H_{\rm int}\|,
\quad
\operatorname{Var}(H_{\rm int}),
\quad
\text{or a suitable electromagnetic/material sum-rule budget}.
\]

**Status:** PROVED for the stated Markov class.

---

# 9. Microscopic completion of the WP3 theorem

Suppose a separate physical assumption supplies an upper bound

\[
\gamma(\omega_0)\le\gamma_{\max}.
\]

For a bosonic reservoir with occupation `n`,

\[
d=\Gamma_\downarrow
=\gamma(\omega_0)[n+1]
\le
\gamma_{\max}[n+1].
\]

Then the WP3 gateway theorem immediately becomes

\[
\lambda_1
\le
\Lambda_{\rm micro}
\equiv
\frac{\mathcal A\,\gamma_{\max}[n+1]}{f_*}
\,g^{-1}\!\left(\frac{\Sigma}{f_*}\right).
\]

For the event-transducer class,

\[
\boxed{
\eta_{\mathcal I}(\omega)
\le
\eta_q
\frac{\Lambda_{\rm micro}^2}
{\Lambda_{\rm micro}^2+\omega^2}.
}
\]

For a thermal optical bath,

\[
n=n_T(\omega_0,T).
\]

This is the correct microscopic form of the restricted theorem: the absolute optical coupling cap is a necessary independent input.

---

# 10. Can the TRK/oscillator-strength sum rule supply `gamma_max`?

For a free-space electric-dipole transition,

\[
\Gamma_0
=\frac{\omega_0^3|\mathbf d_{01}|^2}
{3\pi\epsilon_0\hbar c^3}.
\]

Using the conventional isotropic oscillator strength

\[
f_{01}
=\frac{2m_e\omega_0}{3\hbar e^2}
|\mathbf d_{01}|^2,
\]

and the Thomas–Reiche–Kuhn sum rule

\[
\sum_f f_{0f}=N_e
\]

for a stable ground/occupied initial manifold, any one positive-frequency transition satisfies

\[
f_{01}\le N_e.
\]

Therefore

\[
|\mathbf d_{01}|^2
\le
\frac{3\hbar e^2N_e}{2m_e\omega_0},
\]

and hence

\[
\boxed{
\Gamma_0
\le
\Gamma_{\rm TRK}^{\rm fs}
=
\frac{N_e e^2\omega_0^2}
{2\pi\epsilon_0m_ec^3}
=
2N_e\alpha\frac{\hbar\omega_0}{m_ec^2}\omega_0.
}
\]

This is a useful **free-space per-electron/oscillator-strength corollary**, not a universal photodetector bound.

At `lambda=10 um`, the one-electron value is approximately

\[
\Gamma_{\rm TRK}^{\rm fs}/N_e
\approx6.67\times10^5\ {\rm s^{-1}},
\]

corresponding to about `1.50 us` inverse-rate scale.

At `lambda=1.55 um`, the same one-electron bound is approximately

\[
2.78\times10^7\ {\rm s^{-1}}
\]

(`36 ns` inverse-rate scale), and at `500 nm` about

\[
2.67\times10^8\ {\rm s^{-1}}
\]

(`3.75 ns`).

### Why this is not yet universal

1. `N_e` is extensive; allowing arbitrarily many participating charges removes a per-device bound.
2. Photonic environments modify spontaneous emission through the electromagnetic Green tensor / LDOS (Purcell physics).
3. Resonators, slow-light structures, plasmonic confinement, and collective coupling introduce additional photonic resources not bounded by the matter TRK sum rule alone.
4. In solids, interband continua and collective oscillator strength require careful many-body normalization.
5. In strong/ultrastrong coupling, a simple golden-rule `Gamma_0` description is insufficient and gauge-consistent light–matter Hamiltonians must be used.

Thus TRK supplies an important **matter-side budget**, but a universal device theorem also needs an electromagnetic-environment budget.

---

# 11. Cavity single-mode interpretation

For a simple electric-dipole single-mode cavity model,

\[
g=\frac{|\mathbf d\cdot\mathbf E_{\rm zpf}|}{\hbar},
\qquad
E_{\rm zpf}\sim
\sqrt{\frac{\hbar\omega}{2\epsilon_0V_{\rm eff}}}.
\]

Combining with the TRK bound gives schematically

\[
g^2
\lesssim
\frac{3N_e e^2}{4m_e\epsilon_0V_{\rm eff}}
\]

up to polarization/orientation conventions.

This makes the missing structure explicit:

- TRK bounds matter oscillator strength;
- `V_eff` / LDOS / Green-tensor response controls the photonic concentration of vacuum field;
- neither alone is a complete universal detector-speed resource.

Letting `V_eff` shrink without an electromagnetic/material constraint again makes the coupling bound vacuous.

---

# 12. Relation to current 2026 speed-limit literature

Nishiyama and Hasegawa, **Unified speed limits in classical and quantum dynamics via temporal Fisher information**, Phys. Rev. E 114, 014120 (2026), identify interaction-Hamiltonian energetic fluctuations as a quantum open-system speed resource. This is structurally consistent with the present no-go result: entropy production alone cannot provide the absolute microscopic timescale.

This does not make the present result redundant. Their temporal Fisher information concerns speed of state evolution; the present construction concerns optical-input-to-electrical-event transduction and shows explicitly, in detector-native language, why fixed optical detailed balance plus bounded stationary thermodynamic costs still fail without an absolute light–matter coupling resource.

Relevant optical-side literature also shows that spontaneous-emission rates depend strongly on the photonic environment/LDOS and that broadband near-field optical response requires separate material/geometry constraints. Therefore a final quantum UPRP theorem should likely combine a matter oscillator-strength budget with an electromagnetic-response budget or directly use an interaction-Hamiltonian/coupling functional.

---

# 13. Revised research target

The broad question should now be split into two theorems.

## No-go theorem

Prove as generally as possible that

\[
\boxed{
\text{thermodynamic ratios + stationary dissipation/activity}
\not\Rightarrow
\text{absolute photodetection speed limit}
}
\]

without a microscopic coupling/response scale.

The three-state family above already proves this for a nontrivial reversible Markov event-detector class while preserving optical detailed balance.

## Completion theorem

Identify the weakest microscopic resource `C_LM` such that

\[
\boxed{
\{C_{LM},\Sigma,\mathcal A,f_*,\text{source task}\}
\Rightarrow
\text{finite optical-information bandwidth bound}.
}
\]

Candidate forms of `C_LM`:

1. weak-coupling spectral rate `gamma_max(omega)`;
2. projected electromagnetic LDOS times oscillator-strength budget;
3. integrated optical susceptibility / f-sum-rule budget plus a bandwidth constraint;
4. interaction-Hamiltonian variance or norm in a full quantum input-output formulation.

The most promising quantum-general route is (4), with (2)/(3) used to translate the abstract coupling resource into photodetector-native material/geometry quantities.

---

# 14. Immediate next work

1. Formalize the no-go theorem independently of the specific three-state parametrization if possible.
2. Derive a Green-tensor/LDOS expression for `gamma(omega)` and identify the weakest known electromagnetic sum-rule bound that can control it over a finite signal bandwidth.
3. Test whether optical LDOS power-bandwidth bounds plus TRK can produce a finite **integrated photodetection information** bound.
4. Construct the quantum input-output version with a coupling resource based on `Var(H_int)` or output-field QFI.
5. Compare against Dechant (2026), Gu–Liu (2026), Nishiyama–Hasegawa (2026), and fundamental optical-response bounds before any novelty claim.
