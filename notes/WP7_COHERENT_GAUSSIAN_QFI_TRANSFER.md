# WP7 — Coherent Gaussian QFI transfer: positive theorem and squeezed-pointer no-go

**Date:** 2026-08-19

## Purpose

The generic WP7 trace-distance theorem does not imply an SLD/QFI theorem. This note specializes QF to the physically central case of coherent optical displacement/sideband encoding and passive linear bosonic coupling.

Two results emerge:

1. with a coherent/vacuum detector-side pointer, coherent-state QFI transfer is bounded exactly by a single-particle cross-coupling action;
2. if the detector may contain unbounded pre-existing squeezing, that bound fails catastrophically even for coherent optical inputs and arbitrarily weak coupling.

This identifies a new necessary quantum resource: **initial apparatus metrological resource / pointer noise (or an equivalent energy/squeezing bound).**

---

# 1. Passive linear bosonic transducer

Let `a` collect optical signal modes and `b` collect detector-side bosonic modes. Consider a passive number-conserving quadratic Hamiltonian

\[
H(t)=\hbar
\begin{pmatrix}a^\dagger&b^\dagger\end{pmatrix}
\begin{pmatrix}
h_F(t)&V(t)\\
V^\dagger(t)&h_D(t)
\end{pmatrix}
\binom a b.
\]

The single-particle propagator `U(t)` satisfies

\[
\dot U(t)=-ih(t)U(t).
\]

Local blocks `h_F,h_D` do not transfer the optical displacement between the two mode sets. In an interaction picture they are removed, while the singular values/operator norm of the cross block `V(t)` are unchanged.

Define the dimensionless single-particle cross-coupling action

\[
\boxed{
\Gamma(t)=\int_0^t\|V(s)\|_2\,ds.
}
\]

Unlike the full Fock-space operator norm of a bilinear bosonic interaction, `||V||_2` is finite and is the physically relevant mode-conversion rate.

---

# 2. Subspace-transfer lemma

Take any normalized single-particle amplitude vector initially entirely in the optical subspace,

\[
\psi(0)=\binom{x}{0},
\qquad \|x\|=1.
\]

Let

\[
p_D(t)=\|\psi_D(t)\|^2.
\]

In the local interaction picture,

\[
\dot\psi_D=-iV^\dagger\psi_F,
\qquad
\dot\psi_F=-iV\psi_D.
\]

Therefore

\[
|\dot p_D|
=2|\operatorname{Im}\langle\psi_D,V^\dagger\psi_F\rangle|
\le
2\|V\|\sqrt{p_D(1-p_D)}.
\]

For `0<p_D<1`,

\[
\frac{d}{dt}\arcsin\sqrt{p_D}
=\frac{\dot p_D}{2\sqrt{p_D(1-p_D)}}
\le\|V\|.
\]

Since `p_D(0)=0`,

\[
\arcsin\sqrt{p_D(t)}\le\Gamma(t).
\]

Hence, for `Gamma<=pi/2`,

\[
\boxed{p_D(t)\le\sin^2\Gamma(t).}
\]

For arbitrary time the robust statement is

\[
\boxed{
p_D(t)\le
\sin^2\!\left(\min\{\Gamma(t),\pi/2\}\right).
}
\]

Taking the supremum over initial optical directions gives the block-propagator norm bound

\[
\boxed{
\|U_{DF}(t)\|_2^2
\le
\sin^2\!\left(\min\{\Gamma(t),\pi/2\}\right).
}
\]

**Status:** PROVED.

This is a subspace population/rotation speed bound; generic quantum speed-limit literature overlaps conceptually, so no novelty is claimed for the mathematical lemma itself.

---

# 3. Coherent-state QFI transfer theorem for a coherent/vacuum apparatus

Let the optical signal be a multimode coherent family

\[
|\alpha(\theta)\rangle_F,
\]

and let the detector-side modes start in an arbitrary fixed coherent state `|beta_0>` independent of `theta`.

Passive linear unitary evolution maps products of coherent states to products of coherent states. The detector output displacement is

\[
\beta_D(\theta,t)
=U_{DF}(t)\alpha(\theta)+\text{theta-independent term}.
\]

For a coherent-state family,

\[
F_Q=4\|\partial_\theta\alpha\|^2.
\]

Thus

\[
F_D(t)
=4\|U_{DF}(t)\partial_\theta\alpha\|^2.
\]

Therefore

\[
\frac{F_D(t)}{F_{\rm in}}
=
\frac{\|U_{DF}\partial_\theta\alpha\|^2}
{\|\partial_\theta\alpha\|^2}
\le\|U_{DF}\|_2^2.
\]

Combining with the subspace-transfer lemma,

\[
\boxed{
\frac{F_D(t)}{F_{\rm in}}
\le
\sin^2\!\left(\min\{\Gamma(t),\pi/2\}\right).
}
\]

Any electrical measurement is a downstream quantum-to-classical channel, so classical Fisher information obeys

\[
\boxed{
\frac{F_{\rm elec}(t)}{F_{\rm in}}
\le
\sin^2\!\left(\min\{\Gamma(t),\pi/2\}\right).
}
\]

If `||V(t)||<=g_max`, transferring fraction `r` of coherent-state displacement QFI requires

\[
\boxed{
t\ge\frac{\arcsin\sqrt r}{g_{\max}}}
\qquad(0<r<1).
\]

For a two-mode beam splitter with constant coupling `g`, equality is attained:

\[
F_D/F_{\rm in}=\sin^2(gt).
\]

**Status:** PROVED for coherent-state displacement encoding + passive linear coupling + detector modes initially in a fixed coherent state.

---

# 4. Why the theorem is not universal: squeezed-pointer counterexample

The coherent/vacuum apparatus assumption is a genuine resource assumption, not a technical convenience.

Consider one optical mode `F` and one detector mode `D` with quadratures

\[
x=(a+a^\dagger)/\sqrt2,
\qquad
p=(a-a^\dagger)/(i\sqrt2),
\]

so vacuum has

\[
\operatorname{Var}x=\operatorname{Var}p=1/2.
\]

Encode the parameter as the mean optical quadrature

\[
\langle x_F\rangle=\theta
\]

in a coherent state. The input QFI is

\[
\boxed{F_{\rm in}=2.}
\]

Prepare the detector mode in an `x`-squeezed vacuum with squeezing parameter `r`:

\[
\operatorname{Var}(x_D)=\frac12e^{-2r}.
\]

Couple the modes by a beam splitter of angle `phi`:

\[
x_D'=-\sin\phi\,x_F+\cos\phi\,x_D.
\]

Then

\[
\partial_\theta\langle x_D'\rangle=-\sin\phi,
\]

and

\[
\operatorname{Var}(x_D')
=\frac12\left(\sin^2\phi+\cos^2\phi e^{-2r}\right).
\]

Homodyne measurement of `x_D'` has Fisher information

\[
F_{\rm hom}
=\frac{(\partial_\theta\langle x_D'\rangle)^2}
{\operatorname{Var}(x_D')}
=
\frac{2\sin^2\phi}
{\sin^2\phi+\cos^2\phi e^{-2r}}.
\]

For this one-parameter Gaussian displacement family the aligned homodyne measurement attains the detector-state QFI, so

\[
\boxed{
\frac{F_D}{F_{\rm in}}
=
\frac{F_{\rm elec}}{F_{\rm in}}
=
\frac{\sin^2\phi}
{\sin^2\phi+\cos^2\phi e^{-2r}}.
}
\]

For every fixed nonzero `phi`,

\[
\boxed{
\lim_{r\to\infty}F_D/F_{\rm in}=1.
}
\]

Thus arbitrarily weak but nonzero coupling can transfer arbitrarily close to all of the local optical QFI if the detector pointer can be prepared with arbitrarily small quadrature noise.

**Status:** COUNTEREXAMPLE / PROVED.

---

# 5. Hidden resource scaling

A squeezed vacuum contains mean photon number

\[
N_D=\sinh^2r,
\]

and

\[
e^{-2r}=(\sqrt{N_D+1}-\sqrt{N_D})^2.
\]

For target QFI-transfer fraction `q`, the exact required squeezing satisfies

\[
e^{-2r}
=\tan^2\phi\,\frac{1-q}{q}.
\]

At weak coupling `phi<<1` and large squeezing,

\[
e^{2r}
\sim\frac{q}{(1-q)\phi^2},
\]

so

\[
\boxed{
N_D\sim\frac{q}{4(1-q)\phi^2}.
}
\]

Therefore maintaining a fixed nonzero QFI-transfer fraction while the coupling action tends to zero requires detector pointer energy to diverge as `1/phi^2`.

This makes the hidden resource explicit.

---

# 6. Revised quantum no-go statement

Even after restricting the source to ordinary coherent optical displacement states,

\[
\boxed{
\text{cross-coupling action alone}
\not\Rightarrow
\text{a nontrivial QFI-transfer ceiling}
}
\]

if the detector is allowed unbounded pre-existing metrological resources such as squeezing / conjugate-quadrature variance / pointer energy.

A fully quantum UPRP theorem must therefore include, explicitly or implicitly, an **initial apparatus resource budget** in addition to source and interaction resources.

Candidate apparatus resources:

- total detector-mode energy above a reference vacuum/thermal state;
- minimum pointer-noise covariance;
- maximum detector QFI for translations generated by the coupling-conjugate observable;
- squeezing resource;
- ergotropy/free energy if the apparatus preparation is treated thermodynamically.

Do not choose one as universal until counterexample testing is complete.

---

# 7. Relation to prior work / novelty caution

The use of squeezing as a metrological resource, weakly coupled ancillas/meters, Gaussian-state QFI, and interaction-strength quantum speed limits are established topics. Recent and relevant examples include Gaussian quantum metrology, squeezed-environment readout, displacement sensing with squeezed states, and weak-coupling ancilla metrology.

Therefore neither the beam-splitter calculation nor the statement “squeezing improves sensitivity” is a novelty claim.

The potentially useful UPRP contribution is structural:

1. classical stationary thermodynamic resources fail without an absolute microscopic coupling scale (WP4);
2. in the quantum QFI problem, even an explicit cross-coupling scale fails without an apparatus-preparation/metrological resource;
3. a restricted passive-linear coherent/vacuum theorem is exactly solvable and saturable;
4. this tells us what must be included in any honest fully quantum photodetection resource theorem.

---

# 8. Next action

Derive a **resource-repaired Gaussian theorem** with a finite detector initial-energy/squeezing budget. The cleanest first target is a one-mode or multimode passive linear transducer with:

- coherent optical displacement input;
- detector Gaussian state with bounded mean energy or bounded covariance eigenvalues;
- cross-coupling action `Gamma`;
- arbitrary detector-local passive processing and final electrical measurement.

Determine the tight maximum possible `F_elec/F_in` as a function of coupling action and apparatus energy/noise. Then test whether that apparatus energy can be related to finite-temperature/free-energy resources rather than inserted ad hoc.
