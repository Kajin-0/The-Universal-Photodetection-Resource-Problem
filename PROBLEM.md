# Formal Problem Statement

## 1. Scientific objective

Determine whether there exists a nontrivial, architecture-independent bound on the information acquisition performance of a finite-temperature photodetector in terms of a finite set of physical resources.

The project is explicitly agnostic between a theorem and a no-go result.

## 2. Detector abstraction

A photodetector is treated as a causal stochastic map from an incident optical field or optical power process to a measurable classical record.

For the initial linear stationary theory,

\[
Y(\omega)=\chi_{YP}(\omega)P(\omega)+N(\omega),
\]

where:

- \(P\) is a precisely defined optical input variable;
- \(Y\) is the complete accessible output record or a specified sufficient statistic;
- \(\chi_{YP}\) is the causal linear response;
- \(N\) is stationary output noise with spectral density \(S_Y\).

Define

\[
K(\omega)=\frac{|\chi_{YP}(\omega)|^2}{S_Y(\omega)}.
\]

This quantity is invariant to a deterministic multiplicative output gain \(Y\mapsto gY\), provided both response and output noise are transformed consistently.

## 3. Candidate information objective

Let the optical signal depend on a parameter \(\theta\). In a Gaussian linear model, the output-record Fisher-information rate motivates

\[
\dot{\mathcal F}_\theta
=\int \frac{d\omega}{2\pi}
|\partial_\theta P(\omega)|^2K(\omega).
\]

This expression is not yet accepted as the unique universal objective. A major first task is to define constraints on \(P(t;\theta)\) so that the optimization does not become a statement about unlimited source energy or bandwidth.

Possible normalized objectives include:

1. Fisher information per incident photon;
2. Fisher information per absorbed photon;
3. Fisher information per unit incident optical energy;
4. channel capacity or mutual-information rate under a specified optical-energy constraint;
5. a weighted norm of \(K(\omega)\) with a fixed input-function norm;
6. a detector-only operator norm mapping optical perturbations to statistical distinguishability.

The correct choice is OPEN.

## 4. Candidate universal statement

Seek conditions under which

\[
\mathcal J_{\rm det}
\le
\mathcal B(R_1,R_2,\ldots,R_n)
\]

for every physically admissible detector in a specified class, where \(\mathcal J_{\rm det}\) is a normalized information-acquisition functional and the resources \(R_i\) may include

- temperature \(T\);
- optical carrier energy \(\hbar\omega_{\rm opt}\);
- incident or absorbed photon flux \(\Phi_\gamma\);
- entropy-production rate \(\dot\Sigma\);
- dynamical activity \(\mathcal A\);
- optical absorption/coupling efficiency \(\eta_{\rm abs}\);
- number of independent channels or detector area/volume;
- available free-energy or bias-power rate;
- coherence/asymmetry terms for quantum systems;
- reservoir coupling strength or memory resources outside the Markov limit.

The resource set itself is part of the unknown.

## 5. Nontriviality requirements

A useful bound must satisfy all of the following:

- not depend on arbitrary output units or amplifier gain;
- remain valid under addition of hidden internal states allowed by the model class;
- have explicit extensivity scaling under parallel detector replication;
- distinguish source-resource limits from detector-resource limits;
- survive physically allowed coarse graining or state clearly which complete record is required;
- be finite in the regime in which it is claimed to constrain performance;
- reduce correctly in equilibrium and reversible limits;
- identify the assumptions under which non-Markovianity, coherence, feedback, or squeezing are excluded or included.

## 6. First model class: finite-state Markov detector

Let \(X_t\in\{1,\ldots,n\}\) be a continuous-time Markov jump process with generator

\[
W(P)=W_0+P W_1+O(P^2).
\]

At \(P=0\), assume a stationary state \(\pi\) satisfying

\[
W_0\pi=0,\qquad \mathbf 1^T\pi=1.
\]

A measured current is constructed from counted transitions,

\[
I(t)=\sum_{i\ne j}q_{ij}\,dN_{ij}(t),
\]

where \(q_{ij}\) is the output increment associated with transition \(j\to i\).

Thermal transitions obey local detailed balance relative to specified reservoirs. Optical transitions must have explicit energy and photon-flux bookkeeping rather than being represented as an unconstrained abstract rate perturbation.

## 7. First mathematical tasks

### Task A — Exact linear response

Derive a general expression for \(\chi_{IP}(\omega)\) using the Markov resolvent

\[
(i\omega I-W_0)^{-1}
\]

with the stationary zero mode treated by a Drazin/group inverse or equivalent projection.

### Task B — Exact output noise

Derive \(S_I(\omega)\) for arbitrary counted edges, including the instantaneous shot-noise term and dynamical correlations.

### Task C — Thermodynamic quantities

Write \(\dot\Sigma\) and \(\mathcal A\) in the same edge notation, making units and reservoir assignments explicit.

### Task D — Candidate inequality search

Determine whether combinations of response uncertainty relations, TURs/KURs, fluctuation-response inequalities, and Cramér-Rao/data-processing inequalities produce a nontrivial upper bound on \(K(\omega)\), a frequency integral of \(K\), or a normalized information rate.

### Task E — Counterexample program

Construct low-state-count networks and scalable families designed to violate candidate inequalities.

## 8. Success criteria

### Result class A — Universal theorem

A proof valid for all detectors in a precisely stated class, with explicit equality/saturation conditions or a demonstrably nontrivial gap.

### Result class B — Impossibility theorem

Proof that no finite bound can depend only on a proposed resource set. Ideally identify a minimal counterexample family and the missing resource.

### Result class C — Hierarchy of bounds

A sequence of increasingly general results, for example:

\[
\text{finite-state Markov}
\subset
\text{semiclassical transport}
\subset
\text{Markovian quantum}
\subset
\text{general open quantum}.
\]

This is likely more realistic than one theorem covering all photodetectors immediately.

## 9. Infrared consequence to be addressed only after the general theory

Once a valid theorem/resource hierarchy exists, ask whether it yields a nontrivial statement about high-performance room-temperature MWIR/LWIR photodetection.

The project must not assume that cryogenic cooling is fundamentally necessary. The theorem must decide what follows from physics and what is merely a property of known material/device mechanisms.

## 10. Current status

**OPEN.** No theorem, no impossibility proof, and no accepted final performance functional yet.
