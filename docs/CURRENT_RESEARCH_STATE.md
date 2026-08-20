# Current Research State

**Date:** 2026-08-19

## Strongest proved result

A reversible finite-state Markov photodetector can preserve:

- fixed optical detailed-balance ratio;
- fixed photon energy / optical temperature ratio;
- finite nonzero forward optical throughput;
- finite total stationary activity;
- finite total entropy-production rate;
- finite edge-resolved entropy-production rates;
- finite nonzero successful detection probability;

while its post-absorption timing bandwidth diverges without bound if the absolute light–matter coupling scale is allowed to diverge.

Therefore thermodynamic ratios and stationary thermodynamic costs do **not** determine an absolute photodetection speed scale.

The missing resource is an absolute microscopic coupling/transition scale.

## Strongest conditional positive result

If a microscopic optical coupling cap `gamma_max(omega_0)` is supplied, the fixed-gateway event-detector theorem gives a finite escape-rate and information-bandwidth ceiling:

\[
\Lambda_{\rm micro}
=
\frac{\mathcal A\gamma_{\max}[n+1]}{f_*}
\,g^{-1}(\Sigma/f_*).
\]

For the restricted event-transducer class,

\[
\eta_{\mathcal I}(\omega)
\le
\eta_q\frac{\Lambda_{\rm micro}^2}
{\Lambda_{\rm micro}^2+\omega^2}.
\]

## Current physics interpretation

The optical coupling resource naturally separates into

\[
\text{matter oscillator strength}
\times
\text{electromagnetic environment response}.
\]

TRK/f-sum rules constrain the matter side. LDOS / Green-tensor / optical power-bandwidth limits constrain the electromagnetic side. Neither is sufficient alone for a per-device universal theorem without explicit extensive/geometric resource constraints.

## Next theorem target

Combine:

1. a finite optical temporal information task;
2. TRK/f-sum matter budget;
3. finite-band LDOS/absorption electromagnetic budget;
4. thermokinetic gateway/activity/EPR constraints;
5. data processing for the complete electrical output record.

Target structure:

\[
\bar\eta_{\mathcal I}(\Omega_s)\ge r
\Rightarrow
\Omega_s\le
F(C_{\rm matter},C_{\rm EM},\mathcal A,\Sigma,f_*,T,\omega_0,r).
\]

## Files to read next

- `AGENTS.md`
- `notes/RESEARCH_LOG_ROUND2.md`
- `notes/WP4_MICROSCOPIC_OPTICAL_COUPLING_NO_GO.md`
- `notes/WP5_OPTICAL_POWER_BANDWIDTH_COMPOSITION.md`
- `docs/LITERATURE_MAP.md`
