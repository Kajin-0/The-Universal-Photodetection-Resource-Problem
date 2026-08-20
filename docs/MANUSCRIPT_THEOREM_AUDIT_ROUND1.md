# Manuscript Theorem Audit — Round 1

**Date:** 2026-08-20

## Purpose
Check normalization, prefactors, extensivity, and logical dependencies in the first LaTeX manuscript draft against WP25–WP32 before treating the draft as scientifically stable.

---

# 1. Input Poisson Fisher-information normalization

For

\[
\Phi_\theta(t)=\Phi_0[1+\theta\cos\omega t],
\]

at `theta=0`,

\[
\frac1T F_{in}
=\frac1T\int_0^T
\frac{(\Phi_0\cos\omega t)^2}{\Phi_0}dt
\to\frac{\Phi_0}{2}.
\]

The manuscript factor `Phi0/2` is correct.

For a real coherent-field amplitude `alpha_theta=sqrt(Phi_theta)`, pure-state coherent QFI gives the same local rate for this intensity-modulation parameter, so the stated source normalization is consistent within scope.

**Status:** VERIFIED.

---

# 2. Marked event-kernel FI formula

For subprobability mark measure `kappa(dm)` and conditional delay characteristic function `H_m(omega)`, the output Poisson baseline at mark `m` is `Phi0 kappa(dm)` and the harmonic derivative has magnitude `Phi0 |H_m| kappa(dm)`.

Time averaging contributes `1/2`, giving

\[
\dot F_{out}
=\frac{\Phi_0}{2}
\int|H_m|^2\kappa(dm).
\]

Therefore

\[
\boxed{G(\omega)=\int|H_m|^2\kappa(dm)}
\]

is correct, with

\[
G(0)=\eta=\kappa(M).
\]

**Status:** VERIFIED.

---

# 3. Parseval / collision-resource prefactor

Using

\[
H_m(\omega)=\int f_m(t)e^{-i\omega t}dt,
\]

Parseval is

\[
\int\frac{d\omega}{2\pi}|H_m(\omega)|^2
=\int f_m(t)^2dt.
\]

Define

\[
\mathfrak R_2
=2\int\kappa(dm)\int f_m^2dt.
\]

Then

\[
\int G(\omega)d\omega
=2\pi\int\kappa\int f_m^2
=\pi\mathfrak R_2.
\]

Thus

\[
\boxed{
\bar\eta_I(\Omega)
\le\min\left[\eta,\frac{\pi\mathfrak R_2}{2\Omega}\right]
}
\]

has the correct factor of `pi/2`.

**Status:** VERIFIED.

---

# 4. Arbitrary-source spectral-concentration bound

Given

\[
0\le G(\omega)\le\eta,
\qquad
\int G\le\pi\mathfrak R_2,
\]

the bathtub principle maximizes `int w G` by setting `G=eta` on a set of measure

\[
A=\pi\mathfrak R_2/\eta.
\]

Hence

\[
\boxed{
\bar\eta_I[w]
\le
\eta\mathcal W\!\left(\frac{\pi\mathfrak R_2}{\eta}\right)
}
\]

is correct for an absolutely continuous normalized spectral-FI density `w`.

**Scope note:** discrete spectral measures require a measure-theoretic reformulation of `W`; not needed for the first manuscript if the source is stated to possess a spectral density.

**Status:** VERIFIED WITH SCOPE NOTE.

---

# 5. Hazard-to-L2 bound

For normalized absolutely continuous conditional delay density,

\[
f=hS,
\quad
S=e^{-u},
\quad
u(t)=\int_0^t h(s)ds,
\]

bounded hazard `h<=Lambda` gives

\[
\int f^2dt
=\int h^2 e^{-2u}dt
\le
\Lambda\int h e^{-2u}dt
=\Lambda/2.
\]

Therefore markwise

\[
2\int f_m^2dt\le\Lambda(m),
\]

and after capture weighting

\[
\boxed{\mathfrak R_2\le\mathfrak H}
\]

with

\[
\mathfrak H=\int\Lambda(m)\kappa(dm).
\]

**Status:** VERIFIED.

---

# 6. Uniform exponential tightness

For

\[
f(t)=\Lambda e^{-\Lambda t},
\]

\[
H(\omega)=\frac{\Lambda}{\Lambda+i\omega}.
\]

The flat-band average is

\[
\frac1{2\Omega}\int_{-\Omega}^{\Omega}|H|^2d\omega
=\frac{\Lambda}{\Omega}\arctan(\Omega/\Lambda),
\]

which asymptotically equals

\[
\frac{\pi\Lambda}{2\Omega}.
\]

Thus the uniform-hazard high-band prefactor is asymptotically sharp.

**Status:** VERIFIED.

---

# 7. Wiener atomic residual

For each conditional finite probability measure `mu_m`, classical Wiener theory yields

\[
\lim_{\Omega\to\infty}\frac1{2\Omega}
\int_{-\Omega}^{\Omega}|H_m(\omega)|^2d\omega
=\sum_jp_j(m)^2.
\]

Because `0<=|H_m|^2<=1` and `kappa` has finite mass, dominated convergence justifies integration over marks.

The manuscript's capture-weighted atomic residual is correct.

**Status:** VERIFIED.

---

# 8. RMS-jitter counterexample

For

\[
f_{\epsilon,n}
=(1-\epsilon)\operatorname{Exp}(n)
+\epsilon\operatorname{Exp}(\lambda_\epsilon),
\]

as `n->infinity`,

\[
E[D]\to\epsilon/\lambda_\epsilon,
\]

\[
\operatorname{Var}D
\to
\frac{\epsilon(2-\epsilon)}{\lambda_\epsilon^2}.
\]

Choosing

\[
\boxed{
\lambda_\epsilon
=\frac{\sqrt{\epsilon(2-\epsilon)}}{\sigma}
}
\]

gives `Var D -> sigma^2`.

For every fixed finite band,

\[
H_{\epsilon,n}(\omega)
=(1-\epsilon)\frac{n}{n+i\omega}
+\epsilon\frac{\lambda_\epsilon}{\lambda_\epsilon+i\omega}
\to1
\]

by taking `n->infinity` and then `epsilon->0`.

**Status:** VERIFIED.

---

# 9. Free-clock counterexample

For an arrival-phase mark

\[
M=\omega t\pmod{2\pi}
\]

under

\[
\Phi_\theta=\Phi_0(1+\theta\cos\omega t),
\]

the conditional phase density is

\[
p_\theta(M)=\frac1{2\pi}(1+\theta\cos M).
\]

At `theta=0`, per captured event,

\[
F_M
=\int\frac{(\partial_\theta p)^2}{p}dM
=\frac12,
\]

matching incident Poisson timing FI per photon.

**Status:** VERIFIED.

---

# 10. Thermodynamic gateway dimensions and prefactor

WP29 defines

\[
Z_*=g^{-1}(\Sigma/f_*),
\qquad
g(z)=(1-z^{-1})\ln z.
\]

With activity `A` in `1/time`, reverse gateway rate `d` in `1/time`, and throughput `f_*` in `1/time`,

\[
\Lambda_*
=\frac{\mathcal A d Z_*}{f_*}
\]

has units `1/time`.

The resulting flat-band uniform-hazard corollary

\[
\bar\eta_I
\le
C\min\left[
1,
\frac{\pi\mathcal A d}{2f_*\Omega}
 g^{-1}(\Sigma/f_*)
\right]
\]

is dimensionally and algebraically correct.

**Status:** VERIFIED.

---

# 11. Mark-robust gateway hazard bridge

After capture, the gateway holding time is

\[
T_1\sim\operatorname{Exp}(\lambda_1)
\]

and is independent of exit destination in a CTMC. Under the manuscript assumption that downstream autonomous marks depend only on the exit route/subsequent dynamics, not on an additional record of the hidden gateway dwell time,

\[
D|M=T_1+Y_M
\]

with independence.

Then

\[
f_D(t|M)
=\lambda_1\int_0^t e^{-\lambda_1(t-y)}dF_{Y_M}(y)
\]

and the survival includes the same convolution term plus `P(Y_M>t|M)`, so

\[
\boxed{h_D(t|M)\le\lambda_1.}
\]

**Scope condition to state clearly:** an accessible mark that directly records the hidden gateway dwell time would invalidate this independence/conditioning step; such a mark amounts to an additional timing record and belongs to the broader marked-kernel resource accounting.

**Status:** VERIFIED WITH EXPLICIT SCOPE CONDITION.

---

# 12. Rare-fast thermodynamic counterexample

The explicit three-state family has now been derived in `manuscript/appendix_rare_fast_counterexample.tex`.

Rates:

\[
0\xrightleftharpoons[bR]{aR}1,
\quad
1\xrightleftharpoons[q]{cR}2,
\quad
2\xrightleftharpoons[sR]{p}0.
\]

Exact stationary distribution:

\[
\pi_0=\frac{bp+bq+cp}{RD+E},
\]

\[
\pi_1=\frac{ap+aq+qs}{RD+E},
\]

\[
\pi_2=\frac{RD}{RD+E},
\]

with

\[
D=ac+bs+cs,
\]

\[
E=ap+aq+bp+bq+cp+qs.
\]

All stationary one-way flows and edge affinity logarithms have finite `R->infinity` limits, so activity and EPR remain bounded, while the post-capture state-1 holding rate is

\[
(b+c)R\to\infty.
\]

The successful first-exit probability `c/(b+c)` remains finite and the successful-registration waiting time is exponential with rate `(b+c)R`.

This makes the no-go self-contained and confirms the intended rare-fast mechanism.

**Status:** VERIFIED.

---

# 13. Extensivity

For independent marked detector channels, `kappa`, `G`, `mathfrak R2`, and `mathfrak H` are additive. When the incident source FI is partitioned among independent channels, total source-normalized FI is the corresponding source-weighted average.

Identical replication therefore scales incident and electrical FI equally and does not beat the normalized theorem.

**Status:** VERIFIED.

---

# 14. Main remaining manuscript issues

No prefactor or normalization error was found.

Before submission-quality drafting, address:

1. integrate the explicit rare-fast appendix into the main LaTeX build;
2. cite standard Poisson marking/displacement and Wiener references directly in theorem sections;
3. state the source spectral-density assumption near the arbitrary-spectrum theorem;
4. make the gateway mark-independence condition explicit;
5. decide whether to keep the thermodynamic completion in the main text or move most algebra to an appendix;
6. add figures illustrating atomic vs continuous timing and the fixed-jitter counterexample.

**Overall status: THEOREM CONSTANTS AND NORMALIZATIONS VERIFIED; DRAFT SCIENTIFICALLY CONSISTENT WITH NOTED SCOPE CONDITIONS.**