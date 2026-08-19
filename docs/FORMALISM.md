# Starting Formalism

## 1. Scope

This document defines the initial mathematical language. It is not a finished theory. Definitions should be replaced when a more invariant formulation is found.

## 2. Linear stationary detector

Let an optical perturbation \(P(t)\) drive a detector whose measured classical record is \(Y(t)\). In the linear stationary regime,

\[
\delta \langle Y(\omega)\rangle
=\chi_{YP}(\omega)\,\delta P(\omega).
\]

For stationary output fluctuations

\[
\delta Y(t)=Y(t)-\langle Y\rangle,
\]

define a two-sided PSD convention

\[
\langle \delta Y(\omega)\delta Y(\omega')^*\rangle
=2\pi\delta(\omega-\omega')S_Y(\omega).
\]

All later formulas must state whether this convention has been changed.

Define the input-referred kernel

\[
K(\omega)=\frac{|\chi_{YP}(\omega)|^2}{S_Y(\omega)}.
\]

If \(Y\to gY\), then

\[
\chi_{YP}\to g\chi_{YP},\qquad S_Y\to |g|^2S_Y,
\]

so \(K\) is invariant under deterministic scalar output gain.

For conventional voltage/current readout, if NEP is defined consistently,

\[
K(\omega)=\frac{1}{\mathrm{NEP}^2(\omega)}.
\]

This is an input-referred statement and does not by itself include an optical-source noise floor unless source fluctuations are included in the stochastic input model.

## 3. Information objective

For an optical signal \(P(t;\theta)\), a Gaussian additive-output model motivates

\[
\mathcal F_\theta(T_{\rm obs})
\sim
\int\frac{d\omega}{2\pi}
\frac{|\partial_\theta P_{T_{\rm obs}}(\omega)|^2
|\chi_{YP}(\omega)|^2}{S_Y(\omega)}.
\]

A well-defined asymptotic rate requires a family of signals whose spectral power scales linearly with observation time. The compact expression

\[
\dot{\mathcal F}_\theta
=
\int\frac{d\omega}{2\pi}
|\partial_\theta P(\omega)|^2 K(\omega)
\]

must therefore be interpreted only after signal normalization is fixed.

### Dimensional warning

A “universal” inequality written directly for \(\dot{\mathcal F}_\theta\) is meaningless unless the units and normalization of \(\theta\) and \(P\) are fixed. Candidate invariant alternatives include normalized Fisher information per photon/energy or an operator norm of the input-to-statistical-distance map.

## 4. Finite-state Markov model

Let \(p_i(t)=\Pr[X_t=i]\) and use the column-vector convention

\[
\dot{\mathbf p}(t)=W(t)\mathbf p(t),
\]

where for \(i\ne j\), \(W_{ij}\ge0\) is the transition rate \(j\to i\), and probability conservation requires

\[
\mathbf 1^T W=0.
\]

At zero optical perturbation,

\[
W(t)=W_0+\delta P(t)W_1+O(\delta P^2).
\]

Assume a unique stationary state

\[
W_0\pi=0,
\qquad
\mathbf 1^T\pi=1.
\]

Define

\[
\Pi=\pi\mathbf 1^T,
\qquad
Q=I-\Pi.
\]

## 5. Linear state response

Write

\[
\mathbf p(t)=\pi+\delta \mathbf p(t).
\]

To first order,

\[
\delta\dot{\mathbf p}
=W_0\delta\mathbf p+W_1\pi\,\delta P(t).
\]

For \(\omega\ne0\), formally

\[
\delta\mathbf p(\omega)
=(i\omega I-W_0)^{-1}W_1\pi\,\delta P(\omega).
\]

Because \(\mathbf 1^T W_1=0\), the drive lies in the probability-conserving subspace. At \(\omega=0\), the stationary zero mode must be removed using \(Q\) and a Drazin/group inverse.

A useful reduced resolvent is

\[
R(\omega)=Q(i\omega I-W_0)^{-1}Q
\]

for nonzero \(\omega\), with a suitable continuous extension at zero frequency.

Then

\[
\delta\mathbf p(\omega)=R(\omega)W_1\pi\,\delta P(\omega).
\]

## 6. General jump-current observable

Let \(N_{ij}(t)\) count jumps \(j\to i\), and assign an increment \(q_{ij}\). Define

\[
dQ_t=\sum_{i\ne j}q_{ij}\,dN_{ij}(t).
\]

The mean stationary current is

\[
\bar I
=
\sum_{i\ne j}q_{ij}W_{0,ij}\pi_j.
\]

Define a state-conditioned mean output vector \(c\) with

\[
c_j=\sum_{i\ne j}q_{ij}W_{0,ij}.
\]

If the optical perturbation also directly changes counted edge rates, define

\[
c^{(1)}_j=\sum_{i\ne j}q_{ij}W_{1,ij}.
\]

The first-order current susceptibility should then take the schematic form

\[
\chi_{IP}(\omega)
=
\mathbf 1^T J_1\pi
+
\mathbf 1^T J_0 R(\omega)W_1\pi,
\]

where \(J_0\) and \(J_1\) are current-weighted operators. The exact convention must be derived carefully rather than relying on this schematic equation.

## 7. Counting-field formulation

Introduce a tilted generator

\[
W(\chi)_{ij}
=
W_{ij}e^{i\chi q_{ij}},\qquad i\ne j,
\]

with diagonals chosen according to the counting convention. Derivatives at \(\chi=0\) define current-weighted operators

\[
W^{(1)}=\left.\partial_{i\chi}W(\chi)\right|_{0},
\qquad
W^{(2)}=\left.\partial_{i\chi}^2W(\chi)\right|_{0}.
\]

These provide a systematic route to mean current and finite-frequency noise.

A target generic PSD form is

\[
S_I(\omega)
=
S_{\rm shot}
+2\,\mathrm{Re}\left[
\mathbf 1^T W^{(1)}R(\omega)W^{(1)}\pi
\right]
+\text{convention corrections},
\]

where the signs, factor of two, and subtraction of stationary projections must be derived and checked against solvable examples. This equation is a **derivation target**, not yet a proved repository result.

## 8. Thermodynamic edge variables

For each reversible thermal edge pair \(i\leftrightarrow j\), define one-way stationary traffic

\[
a_{ij}=W_{ij}\pi_j,
\qquad
a_{ji}=W_{ji}\pi_i.
\]

Net edge current:

\[
J_{ij}=a_{ij}-a_{ji}.
\]

Edge activity:

\[
A_{ij}=a_{ij}+a_{ji}.
\]

A conventional steady-state entropy-production rate is

\[
\dot S_{\rm i}
=\frac{k_B}{2}
\sum_{i\ne j}
J_{ij}
\ln\frac{W_{ij}\pi_j}{W_{ji}\pi_i},
\]

with equivalent non-double-counted edge-pair conventions possible.

If \(\dot\Sigma\) is defined dimensionlessly in units of \(k_B\), this must be stated explicitly. The repository must not mix entropy/time and dimensionless entropy-production rate.

Total dynamical activity can be defined schematically as

\[
\mathcal A
=\sum_{i\ne j}W_{ij}\pi_j,
\]

or with reversible pairs counted once. Again, convention must be fixed before theorem statements.

## 9. Optical reservoir bookkeeping

An abstract perturbation \(W_1\delta P\) is too permissive for a fundamental photodetector theorem unless optical energy/flux constraints are added.

At minimum, optical transitions should specify:

- transition energy \(\Delta E\);
- optical carrier frequency \(\omega_{\rm opt}\);
- absorbed-photon flux;
- stimulated/absorption rates as functions of optical occupation or flux;
- whether spontaneous emission is included;
- whether the optical field is prescribed or treated as a reservoir/dynamical quantum system.

The source and detector must not be allowed to exchange unbounded resources through an unconstrained \(W_1\).

## 10. Dimension/invariance checklist

Every candidate bound must explicitly list units for

- \(P\), \(Y\), \(\chi\), \(S_Y\), \(K\);
- \(\mathcal F\), \(\dot{\mathcal F}\);
- \(\Phi_\gamma\), \(\dot S_{\rm i}\), \(\mathcal A\);
- bandwidth/frequency variables.

It must also be checked under

\[
Y\to gY,
\qquad
P\to aP,
\qquad
\theta\to b\theta,
\]

so that arbitrary coordinate choices cannot create or destroy a claimed physical limit.

## 11. Immediate derivation target

The next substantive mathematical milestone is a **fully checked general formula for finite-frequency response and noise of the Markov jump detector**, followed by exact two-state validation.
