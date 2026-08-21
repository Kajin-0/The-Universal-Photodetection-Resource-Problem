# Paper 2 — General Fisher-Channel Resource Theory for Photodetection

## Status

**Active research program.** Paper 1 / Rev11 is scientifically frozen by default and remains the preferred first-paper submission candidate. This directory begins a separate second-paper program.

The ambition is deliberately higher than Paper 1: remove the independent-event / one-primary-registration restriction without giving up an exact universal local-information ordering theorem.

## Central research question

> For an arbitrary photodetector viewed as a parameter-independent stochastic channel from the complete incident optical record to the complete accessible detector record, what operator exactly describes the local temporal Fisher information retained by the detector, and what does time-translation symmetry force that operator to look like?

The immediate target is a theorem of the following form.

### Candidate organizing theorem

Let a stationary Poisson optical input of baseline flux `Phi0` be weakly modulated by arbitrary square-integrable temporal waveforms. Let the detector be **any autonomous stochastic channel** from the entire incident photon trajectory to an accessible output record. The detector may have dead time, saturation, recovery, afterpulsing, hidden-state memory, state-dependent capture, multiple output events, analog marks, and arbitrary high-flux history dependence.

Under differentiability/regularity assumptions, the complete output local Fisher metric should be representable as

\[
F_{\rm out}[u,v]
=\frac{\Phi_0}{2\pi}\int_{\mathbb R}
G_{\Phi_0}(\omega)\,U^*(\omega)V(\omega)\,d\omega,
\]

with a measurable retention spectrum

\[
0\le G_{\Phi_0}(\omega)\le1\quad\text{a.e.}
\]

**without any independent-event delay kernel.**

The proposed proof route is not to model each detector architecture. It is:

1. use the classical identity that a parameter-independent Markov channel maps an input score to its conditional expectation given the output record;
2. package this as a positive contraction operator on the source tangent/score Hilbert space;
3. use detector autonomy / time-translation covariance to show that this operator commutes with translations;
4. invoke the Fourier-multiplier theorem for bounded translation-invariant operators on `L^2`;
5. identify Paper 1's marked-delay spectrum as the low-overlap independent-event special case.

If correct, this would imply that the existence of a complete scalar temporal Fisher spectrum is **not** a consequence of independent detection events. It is a consequence of a multiplicity-one temporal source tangent space plus stationarity.

## Why this could be substantially broader than Paper 1

Paper 1 assumes autonomous low-overlap independent primary events and obtains

\[
G(\omega)=\int|H_m(\omega)|^2\kappa(dm).
\]

Paper 2 asks whether the same *spectral completeness* survives when that explicit kernel representation disappears. The target class includes, in principle:

- SPAD dead time and pile-up;
- SNSPD recovery and history-dependent efficiency;
- afterpulsing and trap memory;
- state-dependent capture;
- high-flux saturation;
- multiple primary registrations;
- arbitrary hidden Markov / semi-Markov detector dynamics;
- complete analog or digital output records.

The spectrum would generally depend on operating point / baseline flux, hence `G_{Phi0}(omega)`.

## Novelty discipline

The following ingredients are **known mathematics and must not be claimed as new**:

- Fisher-information monotonicity under parameter-independent Markov kernels;
- the output-score identity `score_out = E(score_in | output)` under standard regularity;
- conditional expectation as an `L^2` orthogonal projection/contraction;
- bounded translation-invariant operators on `L^2(R)` being Fourier multipliers;
- general Blackwell / sufficient-statistic theory.

Potential novelty must come from the **combined photodetection theorem**, its exact temporal specialization, recovery of Paper 1 as a special case, new high-flux consequences, and any new resource bounds or explicit detector examples that follow.

## Current work packages

1. `notes/WP01_GENERAL_FISHER_CHANNEL_OPERATOR.md` — general detector-channel contraction operator.
2. `notes/WP02_STATIONARY_POISSON_SPECTRAL_THEOREM.md` — autonomy implies an exact scalar temporal Fisher multiplier even with arbitrary detector memory.
3. `notes/WP03_PRIOR_ART_AND_NOVELTY_AUDIT.md` — hostile novelty audit against statistics, information geometry, stationary-process FI, and high-flux photodetection literature.
4. `notes/RESEARCH_LOG_ROUND01.md` — durable chronological handoff.

## Research rule

Do not manufacture a "breakthrough" by renaming standard statistics. The second paper is worth writing only if a genuinely new organizing theorem, nontrivial corollary, sharp bound, or unexpected high-flux result survives adversarial prior-art review.
