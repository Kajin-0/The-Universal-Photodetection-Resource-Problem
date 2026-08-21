# Paper 2 Rev6 external adversarial review response — applied readability only

**Date:** 2026-08-21

## Review outcome

An external adversarial review of Rev6 was strongly favorable and did not identify a central mathematical failure. The review judged the paper significant, with the strongest contributions being:

1. the autonomous arbitrary-memory temporal Fisher-spectrum synthesis;
2. deterministic Type-II static Fisher blindness with information surviving at every nonzero temporal frequency and high-frequency residue `1/e`;
3. the finite-mean theorem that deterministic recovery is the unique static Fisher singularity at the common Type-II count maximum;
4. the exact mean/variance resource-incompleteness counterexample.

The review's recommended disposition was minor-to-moderate revision, favorable overall.

## Changes worth making

Only three manuscript changes are justified before submission-stage freeze.

### 1. Add one dimensionful Type-II scale conversion

Use a deliberately technology-neutral example with

`tau = 10 ns`.

Then

`lambda_* = 1/tau = 100 MHz`,

and the theorem point

`omega*tau = pi`

corresponds to

`f = omega/(2*pi) = 1/(2*tau) = 50 MHz`.

At this finite modulation frequency the rigorous normalized Fisher lower bound remains

`G >= 0.516975...`,

while the high-frequency asymptote is `1/e`.

This example is purely a dimensional translation of the exact dimensionless theorem. It must not imply that a particular detector technology obeys the ideal Type-II model.

### 2. Tighten the word `complete`

Where the manuscript describes the general spectral object as `complete`, qualify it as complete **within the admitted classical Poisson weak-intensity waveform tangent model and accessible-record definition**. The theorem does not cover quantum phase information, nonclassical sources, or arbitrary optical encodings.

### 3. Add a short experimental outlook, not an experimental requirement

A genuinely paralyzable detector operated near `lambda*tau=1` could in principle be tested with both a quasi-static flux perturbation and a small finite-frequency modulation. The theory predicts first-order static blindness of the timestamp experiment while finite-frequency information remains.

This belongs only in the outlook/discussion. It is not a required next step for the current analytical program and does not reopen the project's no-experiment research constraint.

## Changes explicitly rejected

Do **not** add:

- more recovery distributions;
- third- or higher-moment matching examples;
- nonparalyzable calculations;
- detector arrays;
- quantum-source extensions;
- another general Fisher operator;
- thermodynamic resource theory;
- experimental simulations.

These would dilute the current paper's arc.

## Revision decision

Create **Rev7** as a narrow applied-readability/scope-protection revision generated reproducibly from Rev6. No theorem statement, proof conclusion, numerical dataset, or figure data should change.

After Rev7:

1. rebuild with the full revision chain;
2. require resolved citations/references and zero box overflows;
3. visually inspect pages affected by the new text;
4. update the canonical handoffs;
5. freeze science again unless a concrete defect appears.
