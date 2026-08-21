# Supplemental Grounding Literature Audit — Rev9

**Status:** no missing-paper blocker. Rev9's theorem stack does not depend on any inaccessible paper identified in this audit. Five historically important SPAD timing papers that were previously only nice-to-have have now been supplied as full PDFs and checked directly. Their physically relevant claims are incorporated conservatively in `manuscript/section_empirical_grounding_rev9.tex`.

## Full-text historical SPAD papers now obtained and checked

### 1. Cova et al. (1989) — TCPC histogram and sub-FWHM inference
S. Cova, A. Lacaita, M. Ghioni, G. Ripamonti, and T. A. Louis, *20-ps timing resolution with single-photon avalanche diodes*, Review of Scientific Instruments 60, 1104–1110 (1989).

DOI: `10.1063/1.1140324`

Directly verified from full text:

- the TCPC measurement is described as a histogram of photon-detection delays;
- instrumental timing spread contains separate source, optical-pulse, detector, and associated-circuit contributions;
- the authors explicitly note that reconvolution/statistical analysis can estimate decay constants substantially shorter than the instrumental FWHM.

Use in Rev9: physical grounding for the histogram estimator, the measurement-chain caveat, and the statement that a scalar FWHM is not itself an information metric.

### 2. Lacaita and Mastrapasqua (1990) — spatially dependent avalanche timing
A. Lacaita and M. Mastrapasqua, *Strong dependence of time resolution on detector diameter in single photon avalanche diodes*, Electronics Letters 26, 2053–2054 (1990).

DOI: `10.1049/el:19901324`

Directly verified from full text:

- the avalanche-current leading edge depends on the point where the avalanche is initiated;
- discriminator-crossing delay therefore depends on photon absorption position;
- timing resolution worsens with sensitive-area diameter because the avalanche must spread across a larger active region;
- focused illumination near the center improves the observed timing performance.

Use in Rev9: concrete physical example of a latency-predictive spatial/internal variable and of timing information lost when such a variable is not retained.

### 3. Lacaita et al. (1993) — stochastic photon-assisted avalanche spreading
A. Lacaita, S. Cova, A. Spinelli, and F. Zappa, *Photon-assisted avalanche spreading in reach-through photodiodes*, Applied Physics Letters 62, 606–608 (1993).

DOI: `10.1063/1.108870`

Directly verified from full text:

- secondary photons emitted by hot carriers and reabsorbed elsewhere in the detector can drive lateral avalanche spreading;
- the randomness of this process degrades photon timing;
- a Monte Carlo model reproduced the measured transient well;
- at one discriminator threshold the computed timing jitter was 370 ps FWHM versus 425 ps measured.

Use in Rev9: concrete example of an unresolved stochastic microscopic internal process setting the conditional registration-delay law.

### 4. Spinelli et al. (1998) — IRF shape beyond FWHM
A. Spinelli, M. A. Ghioni, S. D. Cova, and L. M. Davis, *Avalanche detector with ultraclean response for time-resolved photon counting*, IEEE Journal of Quantum Electronics 34, 817–821 (1998).

DOI: `10.1109/3.668769`

Directly verified from full text:

- ordinary SPAD IRFs are described as having a regular Gaussian-like fast component plus a slower diffusion tail;
- the slow tail originates from carriers photogenerated in neutral regions that diffuse into the depletion layer;
- the paper emphasizes that tailing and secondary bumps can obscure weak/delayed temporal structure even when the FWHM is small;
- the new DJ-SPAD reduced the residual tail to a small fast exponential component, while comparison devices exhibited substantially longer exponential tails.

Use in Rev9: direct experimental grounding for the canonical Gaussian/exponential timing-law library and for retaining full IRF shape rather than a scalar width.

### 5. Assanelli et al. (2011) — threshold and injection-position dependence
M. Assanelli, A. Ingargiola, I. Rech, A. Gulinatti, and M. Ghioni, *Photon-Timing Jitter Dependence on Injection Position in Single-Photon Avalanche Diodes*, IEEE Journal of Quantum Electronics 47, 151–159 (2011).

DOI: `10.1109/JQE.2010.2068038`

Directly verified from full text:

- photon-timing jitter depends on avalanche injection position;
- timing also depends strongly on discriminator threshold;
- fixing the photon injection position does not eliminate timing dispersion;
- avalanche-propagation statistics and device resistance remain important contributors.

Use in Rev9: grounds both the mark-resource discussion and the distinction between intrinsic primary-event timing and threshold/readout coarse graining.

---

## Other strong modern grounding references

### Gaussian + exponential timing-jitter model in an actual single-photon detector
Mariia Sidorova et al., *Jitter in photon-number-resolved detection by superconducting nanowires*, APL Photonics 10, 086113 (2025).

DOI: `10.1063/5.0273752`

### Independent exponentially modified Gaussian timing-histogram example
Gregor G. Taylor et al., *Mid-infrared timing jitter of superconducting nanowire single-photon detectors*, Applied Physics Letters 121, 214001 (2022).

DOI: `10.1063/5.0128129`

### TCSPC temporal binning as a real analysis variable
Alex J. Walsh et al., *Temporal binning of time-correlated single photon counting data improves exponential decay fits and imaging speed*, Biomedical Optics Express 7, 1385–1399 (2016).

DOI: `10.1364/BOE.7.001385`

### Electrical pulse shape/amplitude as experimentally useful side information
Timon Schapeler et al., *Electrical trace analysis of superconducting nanowire photon-number-resolving detectors*, Physical Review Applied 22, 014024 (2024).

DOI: `10.1103/PhysRevApplied.22.014024`

### Broad modern SPAD timing / TCSPC context
Claudio Bruschini et al., *Single-photon avalanche diode imagers in biophotonics: review and outlook*, Light: Science & Applications 8, 87 (2019).

DOI: `10.1038/s41377-019-0191-5`

### Stochastic-thermodynamics activity context
Naoto Shiraishi, Ken Funo, and Keiji Saito, *Speed Limit for Classical Stochastic Processes*, Physical Review Letters 121, 070601 (2018).

DOI: `10.1103/PhysRevLett.121.070601`

Christian Maes, *Frenesy: Time-symmetric dynamical activity in nonequilibria*, Physics Reports 850, 1–33 (2020).

DOI: `10.1016/j.physrep.2020.01.002`

---

## Manuscript decision

The historical full texts were more useful than expected because they map almost one-to-one onto the new Rev9 operational concepts. The manuscript therefore now cites all five in a short subsection, `section_empirical_grounding_rev9.tex`, without changing any theorem or proof.

The added subsection is deliberately interpretive:

1. Cova 1989 — timing histogram / measurement-chain decomposition / FWHM limitation;
2. Spinelli 1998 — Gaussian-like core plus diffusion tail and tail-sensitive IRF quality;
3. Lacaita 1990 + Assanelli 2011 — spatial/internal variables and threshold-dependent timing;
4. Lacaita 1993 — unresolved stochastic avalanche dynamics as a microscopic timing mechanism.

No experimental result is used as an assumption in the theorem stack.

## Conclusion

**The literature-support gap is closed.** There is no remaining paper that must be obtained before submission. Additional literature should be added only if a referee requests a specific precedent or if a new factual claim is introduced. The current manuscript is now both mathematically self-contained and explicitly anchored to established detector timing phenomenology.
