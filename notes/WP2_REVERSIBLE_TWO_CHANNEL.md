# WP2 — Reversible Two-Channel Photodetector

**Date:** 2026-08-19

## Purpose

The directed two-state unit test in `WP0_WP1_ROUND1.md` shows that stationary activity alone cannot bound information bandwidth: a reset rate can become arbitrarily fast while the reset state becomes arbitrarily rarely occupied. However, that idealized model does not have finite reverse rates and therefore is not yet a finite-entropy-production detector.

This note introduces the smallest reversible two-reservoir model and asks whether the same escape survives local-detailed-balance-compatible reverse channels.

---

# 1. Model

States:

- \(0\): ready / ground state;
- \(1\): optically excited / occupied state.

There are two physically distinct transition channels connecting the same two states.

## Optical channel

\[
0\xrightarrow{u}1,
\qquad
1\xrightarrow{d}0.
\]

The signal perturbs the upward optical rate,

\[
u(t)=u_0+\kappa\,\delta\Phi(t),
\]

where \(\Phi\) is incident photon flux. In the simple linear absorption specialization,

\[
u_0=\alpha\Phi_0,
\qquad \kappa=\alpha.
\]

The baseline rates \(u,d>0\) are retained so that finite rate ratios and finite stochastic affinity are possible.

## Electrical/readout channel

\[
1\xrightarrow{r}0,
\qquad
0\xrightarrow{s}1.
\]

A forward \(1\to0\) readout event is counted as one electrical detection event. The reverse rate \(s\) is the readout-channel back transition responsible for dark excitation/backflow in the minimal model.

Define total upward and downward state-switching rates

\[
A=u+s,
\qquad
B=d+r,
\qquad
\lambda=A+B.
\]

The Markov generator is

\[
W=
\begin{pmatrix}
-A & B\\
A & -B
\end{pmatrix}.
\]

The stationary probabilities are

\[
\pi_0=\frac{B}{\lambda},
\qquad
\pi_1=\frac{A}{\lambda}.
\]

---

# 2. Mean forward electrical count rate and dark-count limit

Counting only the forward readout jump \(1\to0\),

\[
\boxed{
\bar I=\frac{rA}{\lambda}
=\frac{r(u+s)}{u+s+d+r}.
}
\]

If the externally controlled optical excitation is removed so that the optical contribution to \(u\) vanishes, the reverse readout process \(s\) still produces occupation of state 1 and therefore forward readout events. In the simplified zero-signal limit with \(u\to0\),

\[
\boxed{
I_{\rm dark}=\frac{rs}{s+d+r}.
}
\]

Thus increasing the reverse readout rate to avoid a large directional affinity directly increases dark-event traffic.

---

# 3. Exact finite-frequency susceptibility

The excited-state probability obeys

\[
\dot p_1=A-\lambda p_1.
\]

A perturbation \(\delta u\) produces

\[
\delta\dot p_1
=-\lambda\delta p_1+\pi_0\,\delta u
=-\lambda\delta p_1+\frac{B}{\lambda}\delta u.
\]

With Fourier convention \(f(\omega)=\int dt\,e^{-i\omega t}f(t)\),

\[
\delta p_1(\omega)
=\frac{B}{\lambda(\lambda+i\omega)}\delta u(\omega).
\]

Since \(I=r p_1\),

\[
\boxed{
\chi_{Iu}(\omega)
=\frac{rB}{\lambda(\lambda+i\omega)}.
}
\]

For photon-flux perturbations \(\delta u=\kappa\delta\Phi\),

\[
\boxed{
\chi_{I\Phi}(\omega)
=\frac{\kappa rB}{\lambda(\lambda+i\omega)}.
}
\]

**Status:** PROVED.

---

# 4. Exact forward-count PSD

For the counted forward edge, the jump operator is

\[
\mathcal J=
\begin{pmatrix}
0&r\\
0&0
\end{pmatrix}.
\]

The self-shot term is

\[
S_{\rm shot}=\bar I=\frac{rA}{\lambda}.
\]

The connected positive-lag jump correlation has a single relaxation pole,

\[
C_I(t>0)
=-\frac{r^2A^2}{\lambda^2}e^{-\lambda t}.
\]

Therefore the exact two-sided PSD is

\[
\boxed{
S_I(\omega)
=\frac{rA}{\lambda}
\left[
1-\frac{2rA}{\lambda^2+\omega^2}
\right].
}
\]

Equivalently,

\[
\boxed{
S_I(\omega)
=\frac{rA\left(\lambda^2+\omega^2-2rA\right)}
{\lambda(\lambda^2+\omega^2)}.
}
\]

Positivity is automatic because \(r\le B\), hence

\[
\lambda^2-2rA
=(A+B)^2-2rA
\ge A^2+B^2>0.
\]

**Status:** PROVED and independently checked against the general resolvent formula.

---

# 5. Exact response-to-noise kernel

Combining the response and PSD,

\[
\boxed{
K_\Phi(\omega)
=\frac{\kappa^2 rB^2}
{A\lambda\left(\lambda^2+\omega^2-2rA\right)}.
}
\]

For coherent/Poisson illumination, define information-transfer efficiency

\[
\eta_{\mathcal I}(\omega)=\Phi_0 K_\Phi(\omega).
\]

If \(u=\alpha\Phi_0\) and \(\kappa=\alpha\), then

\[
\Phi_0\kappa^2=\alpha u,
\]

so

\[
\boxed{
\eta_{\mathcal I}(\omega)
=\frac{\alpha u\,rB^2}
{A\lambda\left(\lambda^2+\omega^2-2rA\right)}.
}
\]

Define

\[
\boxed{
\Omega_{\mathcal I}^2
=\lambda^2-2rA>0.
}
\]

Then the complete information-efficiency spectrum is a Lorentzian,

\[
\boxed{
\eta_{\mathcal I}(\omega)
=\eta_{\mathcal I}(0)
\frac{\Omega_{\mathcal I}^2}{\Omega_{\mathcal I}^2+\omega^2}.
}
\]

The DC value is

\[
\boxed{
\eta_{\mathcal I}(0)
=\frac{\alpha u\,rB^2}
{A\lambda\Omega_{\mathcal I}^2}.
}
\]

The information-equivalent bandwidth is exactly

\[
\boxed{
B_{\mathcal I}
=\int_{-\infty}^{\infty}\frac{d\omega}{2\pi}\eta_{\mathcal I}(\omega)
=\frac{\eta_{\mathcal I}(0)\Omega_{\mathcal I}}{2}
}
\]

or, explicitly,

\[
\boxed{
B_{\mathcal I}
=\frac{\alpha u\,rB^2}
{2A\lambda\sqrt{\lambda^2-2rA}}.
}
\]

**Status:** PROVED.

---

# 6. Thermodynamic quantities

Because the two state pairs are connected by two distinct reservoirs/channels, the stationary cycle current is

\[
\boxed{
J_{\rm cyc}
=\frac{ur-ds}{\lambda}.
}
\]

The corresponding cycle affinity is

\[
\boxed{
\mathcal F
=\ln\frac{ur}{ds}.
}
\]

When the effective rates satisfy local detailed balance with their respective reservoirs, \(\mathcal F\) is the dimensionless total thermodynamic force around the cycle.

The steady dimensionless entropy-production rate is

\[
\boxed{
\sigma
=J_{\rm cyc}\mathcal F
=\frac{ur-ds}{\lambda}\ln\frac{ur}{ds}\ge0.
}
\]

The total stationary state-jump activity is

\[
\boxed{
\mathcal A_{\rm tot}
=\frac{2AB}{A+B}
=\frac{2(u+s)(d+r)}{u+s+d+r}.
}
\]

This activity counts actual state-switching events. It does not directly equal the largest bare escape rate.

**Status:** PROVED for the two-channel Markov network with the standard stochastic-thermodynamic channel decomposition.

---

# 7. Fast-reset asymptotics

Hold the optical rates \(u,d>0\) and optical coupling \(\alpha>0\) fixed. Let the forward reset/readout rate \(r\to\infty\). Allow the reverse readout rate \(s=s(r)>0\) to scale arbitrarily.

The question is whether the detector can obtain unbounded information bandwidth while both activity and entropy-production rate remain bounded.

## 7.1 If reverse traffic remains bounded

Suppose \(s(r)\) remains bounded. Then

\[
A=u+s=O(1),
\qquad B=d+r\sim r,
\qquad \lambda\sim r.
\]

Hence

\[
B_{\mathcal I}\sim
\frac{\alpha u}{2(u+s)}r,
\]

so information bandwidth grows linearly with reset rate.

The total activity remains bounded,

\[
\mathcal A_{\rm tot}\to2(u+s).
\]

However,

\[
J_{\rm cyc}\to u,
\]

and

\[
\mathcal F
=\ln\frac{ur}{ds}
=\ln r+O(1),
\]

so

\[
\boxed{
\sigma\sim u\ln r\to\infty.
}
\]

Thus the apparent activity-only loophole is paid for by diverging thermodynamic affinity/entropy production.

## 7.2 If reverse traffic grows without bound

If \(s(r)\to\infty\), then both total upward and total downward kinetic scales become large along any path with \(r\to\infty\). Since

\[
\mathcal A_{\rm tot}=\frac{2AB}{A+B},
\]

which is twice the harmonic-mean-type combination of \(A\) and \(B\),

\[
\boxed{
\mathcal A_{\rm tot}\to\infty
}
\]

whenever \(A=u+s\to\infty\) and \(B=d+r\to\infty\).

Therefore using reverse traffic to prevent a large forward/backward affinity incurs diverging activity and dark-event traffic instead.

---

# 8. Fast-reset resource lemma

## Lemma

For fixed \(u,d>0\), consider any sequence of reversible two-channel detectors with \(r_n\to\infty\) and arbitrary \(s_n>0\). Then it is impossible for both

\[
\sup_n\mathcal A_{{\rm tot},n}<\infty
\]

and

\[
\sup_n\sigma_n<\infty
\]

to hold.

Equivalently,

\[
\boxed{
r_n\to\infty
\quad\Longrightarrow\quad
\mathcal A_{{\rm tot},n}\to\infty
\ \text{along a subsequence, or}\ 
\sigma_n\to\infty
\ \text{along a subsequence}.
}
\]

### Proof

Assume \(\mathcal A_{\rm tot}\) stays bounded while \(r\to\infty\). Since \(B=d+r\to\infty\) and

\[
\mathcal A_{\rm tot}=\frac{2AB}{A+B},
\]

bounded activity forces \(A=u+s\) to remain bounded; otherwise if \(A\to\infty\) together with \(B\to\infty\), their harmonic-mean combination diverges. Hence \(s\) is bounded.

With bounded \(s\),

\[
J_{\rm cyc}=\frac{ur-ds}{u+s+d+r}\to u>0,
\]

while

\[
\mathcal F=\ln\frac{ur}{ds}\to\infty.
\]

Therefore

\[
\sigma=J_{\rm cyc}\mathcal F\to\infty,
\]

contradicting bounded entropy production. QED.

**Status:** PROVED for the reversible two-channel two-state model.

---

# 9. Interpretation

This is the first nontrivial result of the UPRP program.

The result does **not** yet establish a universal detector theorem. It establishes, in the smallest reversible transducer model, a precise mechanism behind a speed-resource tradeoff:

- a very fast forward reset can be made rarely occupied, hiding its magnitude from stationary activity;
- suppressing the reverse reset while doing so creates a large directional affinity and entropy-production cost;
- increasing the reverse reset to avoid that affinity creates large bidirectional traffic, dark excitation, and activity.

Schematically,

\[
\boxed{
\text{fast reset}
\Rightarrow
\text{large activity/dark traffic}
\quad\text{or}\quad
\text{large thermodynamic affinity/dissipation}.
}
\]

This is exactly the kind of mechanism the full project is seeking, but only for a minimal model.

---

# 10. Important limitation: no linear \(B_{\mathcal I}\) bound follows

In the bounded-\(s\) fast-reset limit,

\[
B_{\mathcal I}\propto r,
\qquad
\sigma\propto\ln r.
\]

Therefore a simple linear inequality such as

\[
B_{\mathcal I}\le C_1\mathcal A_{\rm tot}+C_2\sigma
\]

cannot be universal even within this minimal family with fixed \(u,d\): the left-hand side can grow exponentially relative to the entropy-production rate.

Any valid resource ceiling may therefore be nonlinear, may need a bare kinetic-capacity variable, or may require stronger microscopic constraints that relate kinetic prefactors to thermodynamic forces.

**Status:** VERIFIED asymptotic obstruction to a simple linear activity-plus-entropy bandwidth bound.

---

# 11. Next adversarial questions

1. Can one derive an explicit optimal upper envelope \(B_{\mathcal I}^{\max}(\mathcal A_{\rm tot},\sigma;u,d,\alpha)\) for this model?
2. Does allowing three or more states permit a sequence with bounded \(\mathcal A_{\rm tot}\) and \(\sigma\) but divergent \(B_{\mathcal I}\), defeating the two-resource pair entirely?
3. Can fast rates be hidden on increasingly rare transient states so that both activity and entropy remain bounded while response bandwidth grows?
4. Does a kinetic-capacity resource such as a maximum escape rate, spectral norm of the generator, logarithmic Sobolev constant, or suitable path-space Fisher metric become necessary?
5. What microscopic quantum/optical constraints relate arbitrarily large reset prefactors to coupling strength, bath spectral density, energy scale, or device size?

The most dangerous next counterexample is therefore a **multi-state rare-fast-state construction** designed to hide large bare rates from both stationary activity and entropy production.
