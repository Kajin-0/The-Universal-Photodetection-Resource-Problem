# WP04 — Quantum waveform-Fisher spectrum prior-art collision

**Date:** 2026-08-21

## Question tested

Could the grand-challenge advance be obtained simply by lifting Paper 2's temporal Fisher spectrum to quantum waveform estimation?

## Answer

**No. This direction is substantially occupied.**

## Direct predecessor

Tsang, Wiseman, and Caves, *Fundamental Quantum Limit to Waveform Estimation*, Phys. Rev. Lett. **106**, 090401 (2011), DOI `10.1103/PhysRevLett.106.090401`, derive a quantum Cramer--Rao bound for an arbitrary time-dependent waveform.

Their continuous-time quantum Fisher kernel has the form of a two-time symmetrized covariance of the Heisenberg-picture waveform-coupling generator. In stationary settings they Fourier-transform the covariance and obtain a frequency-domain spectral uncertainty principle.

Thus all of the following are prior art in substance:

- functional/matrix QFI for a waveform;
- a two-time QFI kernel;
- stationarity -> frequency-domain representation;
- spectral QCRB / spectral uncertainty principles for continuous sensing.

Recent work further treats stochastic waveforms and noisy/non-Markovian continuously monitored quantum sensors, including output-field QFI.

## Consequence for this program

Do not pursue or claim novelty for:

> autonomous quantum waveform estimation has a QFI kernel/spectrum.

That would at best be a repackaging of established quantum metrology.

## Distinction that remains potentially open

Paper 2 is not primarily an estimation-error QCRB. It defines a **source-normalized information-transfer fraction** for a stochastic measurement channel:

`incident local Fisher metric -> accessible-record Fisher metric`.

A quantum analogue would have to be specifically about the **contraction of temporal information through a measurement channel relative to the incident field/state**, not merely the QFI of the sensor state with respect to a waveform.

Even that quantum-channel contraction may be mostly a synthesis of monotonicity of quantum statistical metrics plus time-translation symmetry, so it should not be treated as the high-ceiling target without an additional physical consequence.

## Revised frontier

The grand-challenge frontier is now narrowed to one or more of:

1. **closed-cycle physical resource accounting** for realizing a prescribed information-transfer spectrum;
2. a **new classification theorem for information singularities** across broad measurement channels;
3. a nontrivial **source-to-record quantum information-transfer law** with consequences not contained in Tsang's waveform QCRB;
4. a theorem identifying exactly which ideal classical timing-channel features require unbounded source/reference quantum resources.

## Decision

WP03 remains a potentially useful sharp bridge theorem for a covariant timestamp, but a trajectory-level quantum Fisher spectrum is not by itself a new-paper destination.
