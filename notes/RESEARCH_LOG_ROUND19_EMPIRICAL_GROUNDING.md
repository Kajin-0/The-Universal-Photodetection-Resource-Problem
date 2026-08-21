# Research Log — Round 19: Full-text empirical grounding closure

**Date:** 2026-08-20

## Trigger

After the Rev9 translational grounding pass, five older SPAD timing papers previously identified as useful historical/device-physics support were supplied in full. The goal was not to search for new theorem ingredients, but to determine whether the operational claims in Rev9 were genuinely aligned with established detector phenomenology.

## Full texts checked

### Cova et al. (1989)
*20-ps timing resolution with single-photon avalanche diodes*

DOI: `10.1063/1.1140324`

Directly supports:

- TCPC timing data as a digitized histogram of event delays;
- distinct timing contributions from synchronization, optical pulse width, detector jitter, and timing electronics;
- statistical/convolution inference of decay constants shorter than the instrumental FWHM.

Manuscript use: histogram estimator context and the distinction between a scalar FWHM and information retained by the complete timing record.

### Lacaita and Mastrapasqua (1990)
*Strong dependence of time resolution on detector diameter in single photon avalanche diodes*

DOI: `10.1049/el:19901324`

Directly supports:

- avalanche-current leading-edge dependence on initiation/absorption position;
- position-dependent discriminator-crossing delay;
- timing degradation with increasing active-area diameter due to avalanche spreading;
- improved timing under central focused illumination.

Manuscript use: a concrete latency-predictive spatial/internal variable for the mark-resource discussion.

### Lacaita et al. (1993)
*Photon-assisted avalanche spreading in reach-through photodiodes*

DOI: `10.1063/1.108870`

Directly supports:

- photon-assisted lateral avalanche spreading through secondary photons emitted by hot carriers;
- stochasticity of that mechanism as a timing-jitter source;
- quantitative agreement between a stochastic model and measured timing, including 370 ps computed versus 425 ps measured FWHM at one threshold.

Manuscript use: technology-specific example of an unresolved stochastic microscopic process setting the event-delay law.

### Spinelli et al. (1998)
*Avalanche detector with ultraclean response for time-resolved photon counting*

DOI: `10.1109/3.668769`

Directly supports:

- regular Gaussian-like fast SPAD IRF components;
- slower diffusion tails from carriers generated in neutral regions;
- practical importance of tail/secondary-bump suppression beyond FWHM;
- substantial changes in tail constants among detector architectures.

Manuscript use: direct physical anchor for the canonical Gaussian/exponential timing-law library and the claim that full IRF shape matters.

### Assanelli et al. (2011)
*Photon-Timing Jitter Dependence on Injection Position in Single-Photon Avalanche Diodes*

DOI: `10.1109/JQE.2010.2068038`

Directly supports:

- injection-position dependence of timing jitter;
- strong discriminator-threshold dependence;
- residual timing statistics even under fixed-position optical injection;
- importance of avalanche propagation statistics and device resistance.

Manuscript use: supports both the mark-resource interpretation and the distinction between intrinsic timing information and threshold/readout coarse graining.

## Manuscript action

A short subsection was added:

`manuscript/section_empirical_grounding_rev9.tex`

It is inserted after the Rev9 operational translation section. It cites all five papers and explicitly states that the experiments are phenomenological anchors, **not theorem assumptions**.

Five BibTeX entries were added to `manuscript/references.bib` and audited against the supplied PDFs.

No theorem, proof, equation, model-class assumption, or novelty claim changed.

## Validation

Updated generated Rev9 source SHA-256:

`8ae3e4eb89e3af48823e62332481dbb63912281aa75b653cf46f35166b892611`

Empirical subsection SHA-256:

`512d1d6b43c89933bf723476fa3bae6f0ed54d4d45688f3784602a70a8f12af4`

Canonical Rev9 PDF:

- pages: 31
- bytes: 390412
- SHA-256: `ef566682d6b47eb0d133bca497f76503fc57817b98846ee4241e7a45fb4bd08d`

PRApplied Rev9 PDF:

- pages: 32
- bytes: 391123
- SHA-256: `770bd2c58a5adcef0c88c6275a29e2a9a74441b02dca63415af6da394815533e`

PRApplied submission TeX SHA-256:

`6d71ea050b047000eed027e3fa1b0d6523c9aa4a52f5315b370fe3b4e6b1d0c0`

Final package ZIP SHA-256:

`4cde598d5aa88a4d1c66269148690aad4f5e5b4fe535bf49204901d1f7bdb665`

Full LaTeX/bibliography/cross-reference build passed. No undefined citations or references remain. The only material overfull warning remains the inherited approximately 2.45667 pt Appendix line around `timing-concentration`.

The empirical pages, Data Availability/Appendix transition, and final reference pages were rendered and visually inspected with no clipping or overlap.

## Conclusion

**The empirical/literature grounding gate is closed.**

The five supplied papers strengthened Rev9 exactly where desired: they show that the abstract timing resources correspond to experimentally observed IRF tails, stochastic avalanche growth, spatially conditioned latency, threshold-dependent timing, and histogram-valued TCSPC records.

They do not change the theorem stack.

No additional paper needs to be obtained before submission. Continue literature mining only if a referee asks for a specific precedent or a new factual claim is introduced.
