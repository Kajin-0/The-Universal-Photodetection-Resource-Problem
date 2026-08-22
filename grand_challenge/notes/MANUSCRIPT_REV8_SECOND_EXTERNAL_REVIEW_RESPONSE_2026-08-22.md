# Rev8 response to second external review

**Date:** 2026-08-22

**Input:** external review of Rev7 supplied by the user.

## Overall assessment

The review is strongly favorable and independently endorses the core finite-copy theorem, the N-copy extension, the exact equality family, the compound-Poisson/CPTP inheritance, and the explicit waveform-synthesis no-go boundary. Its remaining caveats are principally scope/positioning issues rather than theorem defects.

The review characterizes the paper as a technically careful specialist contribution suitable for PRA or PRX Quantum and explicitly notes that the finite-copy Cauchy--Schwarz proof and collective-measurement extension hold together.

## Changes accepted

One additional clarification was judged useful and low risk:

> The theorem is local in the waveform-perturbation parameters: it bounds Fisher information at the uniform random-time baseline and does not by itself constitute a global finite-amplitude estimation-error or risk bound.

This sentence is added in Rev8 Discussion. It makes explicit a limitation already implicit in the local Fisher-information formulation.

No theorem, proof, coefficient, source hypothesis, equality family, Poisson embedding, or continuum inequality is changed.

## Review statements already addressed by Rev7

The review's other substantive caveats are already explicitly handled in Rev7:

- the physical source class must factor through fixed-excitation random-time encoding;
- the continuum statement is a controlled periodic-to-continuum theorem rather than an unconditional theorem for arbitrary continuous-spectrum experiments;
- the relevant resource is excess excitation energy above the participating lower edge, not total laboratory/carrier energy;
- the operational survival law is distinguished from the separately optimized SLD-QFI envelope;
- established U(1) mode/asymmetry theory is credited as prior art;
- arbitrary parameter-dependent waveform-state synthesis is excluded by an explicit sideband counterexample;
- the truncated-Gaussian single-photon example gives a smooth nonextremal check against the survival ceiling.

## One factual issue in the review that is NOT adopted

The review describes the equality family as a "Lorentzian-spectrum/Cauchy-arrival-time pair familiar from ordinary spontaneous emission." That is not the equality family proved in the manuscript.

The manuscript's controlled-continuum equality family is:

- **exponential excess-frequency probability measure**;
- **Cauchy canonical timing density**.

Ordinary Weisskopf--Wigner spontaneous emission is instead commonly associated, approximately, with:

- **Lorentzian emission spectrum** around the transition frequency;
- **exponential temporal decay**.

The review's spontaneous-emission analogy therefore reverses the relevant Fourier-pair structure and must not be copied into the manuscript or cover letter.

## Current-literature check

The cited 2026 paper by Patrick Folge, Laura Serino, Ladislav Mista, Benjamin Brecht, Christine Silberhorn, Jaroslav Rehacek, and Zdenek Hradil is real:

**"Quantum-limited detection of the arrival time and the carrier frequency of time-dependent signals," Optica 13, 548--557 (2026), DOI 10.1364/OPTICA.579459.**

It is directly relevant to contemporary joint time-frequency quantum metrology and supports the manuscript's claim that the single-photon example sits in an active 2026 research context. It is not treated as prior art for the present survival-function theorem.

## Rev8 validation

Rev8 is generated deterministically from the already verified Rev7 source by `apply_rev8_local_scope_clarification.py`.

Local full build:

- `pdflatex -> BibTeX -> pdflatex -> pdflatex`: PASS;
- pages: 8;
- unresolved citations/references: 0;
- overfull boxes: 0;
- fatal/undefined controls: 0;
- all-page render: PASS;
- visual diff against Rev7: changes only on pages 7--8 from the one-sentence Discussion insertion and resulting bibliography reflow.

## Decision

**Rev8 is the preferred PRX Quantum manuscript.**

The second external review does not justify reopening theorem development. Rev8 should be frozen unless a concrete mathematical defect, historical-priority collision, citation defect, build problem, or genuinely substantive referee objection appears.
