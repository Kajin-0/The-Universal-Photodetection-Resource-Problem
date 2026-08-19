# The Universal Photodetection Resource Problem

## Research question

**Does a material-independent physical bound exist on the rate at which a finite-temperature photodetector can extract information from an optical field, as a function of its thermodynamic, kinetic, optical, and quantum resources?**

The objective of this repository is to derive the tightest such bound if it exists, or to construct a physically admissible counterexample if it does not.

This is a theoretical/analytical research program. The primary target is not another material-specific detectivity calculation, but a theorem (or no-go result) that identifies which combinations of sensitivity, bandwidth, temperature, photon flux, dissipation, and dynamical activity are fundamentally compatible with physics.

## Central formulation

Represent a stationary linear photodetector as an optical-to-electrical stochastic transducer

\[
Y(\omega)=\chi_{YP}(\omega)P(\omega)+N(\omega),
\]

with output-noise power spectral density \(S_Y(\omega)\). Define the input-referred information kernel

\[
K(\omega)
=\frac{|\chi_{YP}(\omega)|^2}{S_Y(\omega)}
=\frac{1}{\operatorname{NEP}^2(\omega)}.
\]

For a parameterized optical waveform \(P(t;\theta)\), an important candidate performance functional is the Fisher-information rate

\[
\dot{\mathcal F}_{\theta}
=\int_{-\infty}^{\infty}\frac{d\omega}{2\pi}
\frac{|\partial_\theta P(\omega)|^2}{\operatorname{NEP}^2(\omega)},
\]

subject to explicit PSD, observation-time, and waveform-normalization conventions.

The open problem is to determine whether there is a nontrivial universal inequality of the form

\[
\dot{\mathcal F}_{\theta}
\le
\mathcal B\!\left(T,\hbar\omega_{\rm opt},\Phi_\gamma,\dot\Sigma,\mathcal A,\eta_{\rm abs},\ldots\right),
\]

where the right-hand side contains only physically meaningful resources and not a specific detector material or architecture.

## Why the answer is not assumed

Three outcomes are scientifically acceptable:

1. **Universal bound:** prove a nontrivial inequality linking photodetection information rate to physical resources.
2. **No universal bound under the proposed resources:** construct a physically admissible detector family that violates every finite candidate bound.
3. **Missing-resource result:** show that a bound fails with, for example, entropy production alone but becomes valid after including dynamical activity, optical flux, coherence/asymmetry, or another resource.

The project must not assume in advance that a simple sensitivity-bandwidth-temperature product exists.

## First tractable model class

Begin with finite-state, stationary, continuous-time Markov photodetectors

\[
\dot{\mathbf p}=W(P)\mathbf p,
\qquad
W(P)=W_0+P W_1+O(P^2),
\]

with a measured counting/current observable

\[
I(t)=\sum_{ij} q_{ij}\,dN_{ij}(t).
\]

Initial admissibility requirements:

- local detailed balance for thermal transitions;
- explicit optical transitions and photon-energy bookkeeping;
- a stationary dark state;
- causal response;
- finite steady-state entropy-production rate;
- finite dynamical activity;
- an explicitly defined output record and noise PSD;
- arbitrary finite number of internal states.

The first theorem/counterexample target is a bound on a normalized frequency-integrated response-to-noise functional derived from \(\chi_{IP}(\omega)\) and \(S_I(\omega)\).

## Research phases

- **Phase 0 — Definition and novelty closure:** make every resource, normalization, and admissibility assumption mathematically precise; continuously audit nearby literature.
- **Phase 1 — Classical finite-state Markov detectors:** derive exact response/noise expressions and test thermodynamic/kinetic inequalities.
- **Phase 2 — Extremal and counterexample search:** identify saturating networks or prove candidate resource sets insufficient.
- **Phase 3 — Semiclassical transport:** connect the theorem to generation-recombination, transit-time, photoconductive gain, junction, and avalanche models.
- **Phase 4 — Quantum extension:** formulate Lindblad/trajectory versions including coherence, backaction, and generalized activity.
- **Phase 5 — Infrared consequence:** determine what, if anything, the theorem implies for room-temperature high-performance MWIR/LWIR detection.

## Repository map

- `PROBLEM.md` — formal problem statement, success criteria, and failure modes.
- `AGENTS.md` — durable handoff instructions and current research state for future agents.
- `ROADMAP.md` — work packages and decision gates.
- `docs/FORMALISM.md` — notation and starting mathematical framework.
- `docs/LITERATURE_MAP.md` — closest known literature and novelty-risk map.
- `docs/NOVELTY_AND_FALSIFICATION.md` — explicit novelty claims that may and may not be made.
- `notes/RESEARCH_LOG.md` — chronological record of results, failed conjectures, and decisions.

## Research discipline

A conjecture is not a result. Every proposed universal inequality must be tested against trivial rescalings, passive amplification, coarse graining, changes of observation convention, equilibrium limits, zero-dissipation limits, high-activity limits, and explicit counterexample families before being promoted to a theorem candidate.

The repository should retain failed approaches. Negative results are part of the research trail and are essential for handoff continuity.
