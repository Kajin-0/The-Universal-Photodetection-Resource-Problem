# WP3 — Fixed Optical Gateway Resource Theorem

**Date:** 2026-08-19

## Scope

This note derives the first positive sensitivity-speed-resource theorem in the project. It does **not** apply to every conceivable photodetector. It applies to a physically interpretable class of event-type Markov photodetectors with a reversible signal-facing gateway and no instantaneous optical-to-electrical feedthrough.

The result is valuable for two reasons:

1. it shows precisely how the three-state rare-fast counterexample is blocked once the signal-facing optical reservoir is fixed; and
2. it identifies a concrete combination of optical throughput, entropy production, stationary activity, and reverse optical rate that bounds the first post-absorption kinetic rate and therefore timing bandwidth.

**Status:** theorem proved under the assumptions stated below. Novelty relative to the full first-passage/sensing literature remains OPEN.

---

# 1. Detector class and assumptions

Consider a finite-state continuous-time Markov detector with a distinguished ready state \(0\) and post-absorption gateway state \(1\).

The signal-facing optical transition is reversible:

\[
0\xrightleftharpoons[d]{u}1,
\qquad u,d>0,
\]

where \(d\) is fixed by the specified optical reservoir/device model.

Let the stationary probabilities be \(\pi_0,\pi_1\).

Define the stationary forward and reverse optical traffic

\[
f=u\pi_0,
\qquad
r_{\rm opt}=d\pi_1.
\]

Assume the detector operates in the net-absorption regime

\[
f\ge r_{\rm opt}>0.
\]

Let

\[
\Sigma
\]

be an upper bound on the **total dimensionless steady entropy-production rate** of the full reversible Markov network, including the optical gateway contribution, and let

\[
\mathcal A
\]

be an upper bound on the total one-way stationary jump activity

\[
\mathcal A_{\rm tot}
=\sum_j\pi_j\lambda_j,
\qquad
\lambda_j=\sum_{i\neq j}W_{ij}.
\]

Finally impose a minimum useful forward optical throughput

\[
\boxed{f\ge f_*>0.}
\]

This condition prevents the detector from obtaining arbitrary speed by becoming almost never ready to absorb a photon.

---

# 2. Optical-edge entropy-production lemma

The entropy-production rate associated with the reversible optical edge is

\[
\sigma_{\rm opt}
=(f-r_{\rm opt})
\ln\frac{f}{r_{\rm opt}}.
\]

Each reversible-edge contribution is nonnegative, so

\[
0\le\sigma_{\rm opt}\le\sigma_{\rm tot}\le\Sigma.
\]

Define the forward/reverse flux ratio

\[
z=\frac{f}{r_{\rm opt}}\ge1.
\]

Then

\[
\sigma_{\rm opt}
=f\left(1-\frac1z\right)\ln z.
\]

Define

\[
g(z)=\left(1-\frac1z\right)\ln z,
\qquad z\ge1.
\]

Its derivative is

\[
g'(z)=\frac{\ln z+z-1}{z^2}\ge0,
\]

with strict positivity for \(z>1\). Thus \(g\) is invertible on \([1,\infty)\).

From \(f\ge f_*\) and \(\sigma_{\rm opt}\le\Sigma\),

\[
g(z)
=\frac{\sigma_{\rm opt}}{f}
\le\frac{\Sigma}{f_*}.
\]

Define

\[
\boxed{
Z_*\equiv
g^{-1}\!\left(\frac{\Sigma}{f_*}\right).
}
\]

Then

\[
\boxed{z\le Z_*.}
\]

Therefore the reverse optical traffic cannot become arbitrarily small:

\[
r_{\rm opt}=\frac{f}{z}
\ge\frac{f_*}{Z_*}.
\]

Since \(r_{\rm opt}=d\pi_1\),

\[
\boxed{
\pi_1
\ge
\frac{f_*}{d Z_*}.
}
\]

## Interpretation

At fixed reverse optical rate \(d\), finite entropy production plus nonzero absorption throughput prevents the post-absorption state from being made arbitrarily rare. This directly blocks the rare-fast mechanism used in `WP2_THREE_STATE_RARE_FAST_COUNTEREXAMPLE.md`.

**Status:** PROVED.

---

# 3. Activity then bounds the gateway escape rate

Let

\[
\lambda_1=\sum_{i\neq1}W_{i1}
\]

be the total escape rate from the post-absorption gateway state.

Because total activity contains the state-1 contribution,

\[
\pi_1\lambda_1\le\mathcal A_{\rm tot}\le\mathcal A.
\]

Using the lower bound on \(\pi_1\),

\[
\boxed{
\lambda_1
\le
\Lambda_*
\equiv
\frac{\mathcal A\,d\,Z_*}{f_*}.
}
\]

This is the central kinetic consequence:

\[
\boxed{
\lambda_1
\le
\frac{\mathcal A d}{f_*}
\,g^{-1}\!\left(\frac{\Sigma}{f_*}\right).
}
\]

The bound has correct dimensions of inverse time.

**Status:** PROVED.

---

# 4. Event-transducer timing lemma

Now restrict further to a low-flux/single-event detector class in which:

1. an absorbed photon places the detector in state 1;
2. the electrical detection record cannot occur before the detector first exits state 1;
3. there is no direct optical-to-electrical feedthrough;
4. different photon events can be treated independently (renewal/low-overlap regime).

For a continuous-time Markov chain, the waiting time to first exit state 1 is exactly exponential:

\[
T_1\sim\mathrm{Exp}(\lambda_1).
\]

Any detection delay can be written

\[
D=T_1+D',
\]

where \(D'\ge0\) is the additional downstream delay. The Markov property makes \(T_1\) independent of the exit destination and subsequent trajectory.

The delay transfer function is

\[
H_D(\omega)=\mathbb E[e^{-i\omega D}].
\]

Therefore

\[
H_D(\omega)
=\frac{\lambda_1}{\lambda_1+i\omega}
\,G(\omega),
\]

with

\[
|G(\omega)|\le1.
\]

Hence

\[
\boxed{
|H_D(\omega)|^2
\le
\frac{\lambda_1^2}{\lambda_1^2+\omega^2}.
}
\]

The first post-absorption escape imposes an unavoidable Lorentzian timing-information envelope. Additional stochastic internal dynamics can only reduce its magnitude.

**Status:** PROVED for the stated event-transducer class.

---

# 5. Information-efficiency bound

Let \(\eta_q\le1\) be the zero-frequency event detection probability/quantum efficiency after an incident photon is presented to the detector under the specified operating condition.

For independent Poisson/coherent photon events passed through thinning plus random delay, the output modulation transfer is multiplied by \(H_D(\omega)\), while independent dark counts or additional noise can only reduce Fisher information.

Thus

\[
\boxed{
\eta_{\mathcal I}(\omega)
\le
\eta_q|H_D(\omega)|^2
\le
\eta_q
\frac{\lambda_1^2}{\lambda_1^2+\omega^2}.
}
\]

Using \(\lambda_1\le\Lambda_*\) and monotonicity in \(\lambda_1\),

\[
\boxed{
\eta_{\mathcal I}(\omega)
\le
\eta_q
\frac{\Lambda_*^2}{\Lambda_*^2+\omega^2},
}
\]

where

\[
\boxed{
\Lambda_*
=
\frac{\mathcal A d}{f_*}
\,g^{-1}\!\left(\frac{\Sigma}{f_*}\right).
}
\]

This is the first complete resource-to-information-spectrum inequality obtained in UPRP.

**Status:** PROVED under the gateway + event-transducer assumptions.

---

# 6. Finite-band task theorem

For a flat information task over \(|\omega|\le\Omega_s\),

\[
\bar\eta_{\mathcal I}(\Omega_s)
=\frac{1}{2\Omega_s}
\int_{-\Omega_s}^{\Omega_s}d\omega\,
\eta_{\mathcal I}(\omega).
\]

Integrating the Lorentzian ceiling gives

\[
\boxed{
\bar\eta_{\mathcal I}(\Omega_s)
\le
\eta_q
\frac{\Lambda_*}{\Omega_s}
\arctan\frac{\Omega_s}{\Lambda_*}.
}
\]

This is a finite, source-task-normalized sensitivity-speed-resource bound.

Equivalently, to achieve a target fraction

\[
\bar\eta_{\mathcal I}(\Omega_s)
\ge r\eta_q,
\qquad 0<r<1,
\]

a necessary condition is

\[
\frac{\Lambda_*}{\Omega_s}
\ge h^{-1}(r),
\]

where

\[
h(y)=y\arctan(1/y).
\]

Therefore

\[
\boxed{
\Omega_s
\le
\frac{\Lambda_*}{h^{-1}(r)}.
}
\]

Substituting the thermokinetic bound,

\[
\boxed{
\Omega_s
\le
\frac{\mathcal A d}{f_*}
\frac{g^{-1}(\Sigma/f_*)}{h^{-1}(r)}.
}
\]

This equation is the current strongest candidate UPRP theorem within the restricted model class.

---

# 7. Numerical meaning of the finite-band factor

The required ratio \(\Lambda_*/\Omega_s=h^{-1}(r)\) is:

| Required band-averaged information fraction \(r\) | \(h^{-1}(r)\) | Necessary \(\Omega_s/\Lambda_*\le\) |
|---:|---:|---:|
| 0.50 | 0.42898 | 2.3311 |
| 0.80 | 1.05359 | 0.9491 |
| 0.90 | 1.65966 | 0.6025 |
| 0.95 | 2.46518 | 0.4057 |
| 0.99 | 5.72149 | 0.1748 |

Thus retaining 90% of the available low-frequency event information on average over a flat task band requires a gateway escape scale at least approximately

\[
\Lambda_*\gtrsim1.66\,\Omega_s.
\]

Retaining 99% requires approximately

\[
\Lambda_*\gtrsim5.72\,\Omega_s.
\]

---

# 8. Pointwise edge-of-band version

If instead the requirement is

\[
\eta_{\mathcal I}(\Omega_s)
\ge r\eta_q,
\]

then the Lorentzian bound gives

\[
r
\le
\frac{\Lambda_*^2}{\Lambda_*^2+\Omega_s^2}.
\]

Hence

\[
\boxed{
\Omega_s
\le
\Lambda_*\sqrt{\frac{1-r}{r}}.
}
\]

Examples:

- \(r=0.5\): \(\Omega_s\le\Lambda_*\);
- \(r=0.9\): \(\Omega_s\le\Lambda_*/3\);
- \(r=0.99\): \(\Omega_s\le0.1005\Lambda_*\).

This is a cleaner analogue of a detector 3-dB bandwidth statement.

---

# 9. Timing-jitter corollary

Because

\[
D=T_1+D'
\]

with independent \(T_1\sim\mathrm{Exp}(\lambda_1)\),

\[
\mathrm{Var}(D)
=\frac{1}{\lambda_1^2}+\mathrm{Var}(D')
\ge\frac{1}{\lambda_1^2}.
\]

Therefore the rms timing jitter obeys

\[
\boxed{
\sigma_t\ge\frac1{\lambda_1}\ge\frac1{\Lambda_*}.
}
\]

or

\[
\boxed{
\sigma_t
\ge
\frac{f_*}{\mathcal A d\,g^{-1}(\Sigma/f_*)}.
}
\]

This provides an explicit timing-resolution consequence of the same resource inequality.

**Novelty warning:** detector jitter/dissipation tradeoffs already exist in the literature, especially Schwarzhans et al. (PRX Quantum 7, 033001, 2026). This corollary must be compared theorem-by-theorem before any novelty claim.

---

# 10. Why the three-state counterexample fails under these assumptions

The rare-fast counterexample achieved

\[
\pi_1\sim R^{-1}
\]

while the output edge rate grew as \(R\). It did so by also letting the reverse signal-facing rate grow as \(cR\).

Here \(d\) is fixed. If one attempted \(\pi_1\sim R^{-1}\) while maintaining finite forward optical throughput \(f\ge f_*>0\), then

\[
\frac{f}{d\pi_1}\sim R,
\]

and the optical-edge EPR would scale as

\[
\sigma_{\rm opt}\sim f\ln R\to\infty.
\]

Thus the gateway theorem formalizes exactly why a fixed reversible optical channel closes that loophole.

---

# 11. Critical limitations

The theorem does **not** yet cover:

- photoconductors where the electrical observable responds continuously to post-absorption occupancy rather than a later detection event;
- direct-feedthrough models in which the counted electrical edge itself is optically modulated;
- strongly overlapping/saturated photon events;
- coherent non-Markovian detector dynamics;
- nonthermal coherent optical reservoirs unless their entropy/information accounting is specified consistently;
- detectors whose signal couples through many optical gateway states rather than one distinguished edge;
- quantum detectors where Hamiltonian evolution before the first irreversible jump carries useful information.

The theorem also counts the optical gateway contribution inside total stochastic EPR. If one defines a resource budget that deliberately excludes the optical source/channel, the bound must be reformulated.

---

# 12. Novelty status

**Do not claim this result is novel yet.** Relevant adjacent literature includes:

- finite-frequency FRIs and R-KUR/R-TUR relations;
- thermodynamic speed limits for Markov processes;
- first-passage thermodynamic uncertainty relations;
- temporal-Fisher-information speed limits;
- detector thermodynamics linking entropy production to jitter/dead time/dark counts;
- timing-jitter models for single-photon detectors.

What may be distinct is the specific chain

\[
\text{optical throughput + optical-edge reversibility + EPR}
\Rightarrow
\text{gateway occupancy floor}
\Rightarrow
\text{activity-imposed escape-rate ceiling}
\Rightarrow
\text{first-passage timing filter}
\Rightarrow
\text{photodetection information-bandwidth ceiling}.
\]

This requires a targeted theorem-level novelty audit.

---

# 13. Next theoretical extensions

1. Generalize from one gateway state to an optical entrance subspace/set of states using cut-set traffic and entropy production.
2. Replace the event-delay assumption with a general Markov electrical current and determine whether an analogous resolvent bound follows.
3. Determine whether the gateway EPR must include optical-source irreversibility or can be rewritten using detector-only heat/work resources plus incident photon free energy.
4. Extend to multiple parallel optical channels while preserving extensivity.
5. Compare quantitatively with Schwarzhans et al. and the 2026 temporal-Fisher speed-limit paper.
6. Seek the quantum analogue where \(\lambda_1\) is replaced by a Hamiltonian/Liouvillian/coupling scale.