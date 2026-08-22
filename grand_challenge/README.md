# The Universal Physical Cost of Temporal Information Acquisition

This directory contains a high-risk theoretical program launched from the frozen Paper-2 result on Fisher spectra of autonomous detector channels.

## Starting point

Paper 2 establishes that an arbitrary parameter-independent autonomous classical detector channel driven by a homogeneous Poisson source has a local weak-waveform Fisher operator that is a bounded temporal Fourier multiplier `G(omega)`, with `0 <= G <= 1` almost everywhere.

The central question here is whether **physical realizability** imposes deeper constraints on the attainable spectrum than data processing and autonomy alone.

## Grand question

> What physical resource, if any, is necessary to realize a specified temporal information-transfer spectrum in an autonomous measurement apparatus with memory?

Candidate resources include dissipation, dynamical activity, power, finite transition-rate scales, asymmetry/time-reference resources, amplification, reset capacity, and record durability. None is presumed correct.

## Falsification-first policy

The first objective is to prove **no-go results** against overly broad candidate laws. In particular, existing literature already rules out naive universal identification of information acquisition rate with entropy-production rate, and recent work covers frequency-domain response/dissipation uncertainty relations in Markov/Langevin systems.

A result is interesting only if it survives close prior art and explicit adversarial model classes.

## High-ceiling targets

1. A universal classification theorem for temporal-information singularities in physical measurement channels.
2. A sharp resource law that survives classical hidden-memory, diffusion, non-Markovian, and quantum counterexamples under explicit operational assumptions.
3. A quantum/classical accessibility gap: information present in the detector/field state but absent from a conventional accessible record at a singular operating point.
4. Necessary-and-sufficient conditions for an autonomous measurement apparatus to realize a target `G(omega)`.

## Current status

See `notes/WP01_LANDSCAPE_AND_FIRST_NO_GOS.md` and `AGENTS.md`.
