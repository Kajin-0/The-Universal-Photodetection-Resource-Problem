# Supplemental Grounding Literature Audit — Rev9

**Status:** no missing-paper blocker. Rev9's theorem stack does not depend on any inaccessible paper identified in this audit. The items below are supplemental support for the operational/engineering interpretation only.

## Best directly relevant support (full text or adequate open version located)

### 1. Gaussian + exponential timing-jitter model in an actual single-photon detector
Mariia Sidorova et al., *Jitter in photon-number-resolved detection by superconducting nanowires*, APL Photonics 10, 086113 (2025).

DOI: `10.1063/5.0273752`

Why useful: directly models measured detector arrival-time histograms with Gaussian and exponential jitter components (an exponentially modified Gaussian), closely matching the canonical Gaussian–exponential timing-law row in Rev9.

### 2. Independent experimental example of exponentially modified Gaussian timing histograms
Gregor G. Taylor et al., *Mid-infrared timing jitter of superconducting nanowire single-photon detectors*, Applied Physics Letters 121, 214001 (2022).

DOI: `10.1063/5.0128129`

Why useful: measured SNSPD timing histograms are fit with an exponentially modified Gaussian to account for non-Gaussian tails. This is a strong device-physics grounding reference for Rev9's canonical timing library.

### 3. TCSPC temporal binning as a real analysis variable
Alex J. Walsh et al., *Temporal binning of time-correlated single photon counting data improves exponential decay fits and imaging speed*, Biomedical Optics Express 7, 1385–1399 (2016).

DOI: `10.1364/BOE.7.001385`

Why useful: demonstrates that temporal binning is an explicit experimental/data-analysis operation in TCSPC. Rev9's inequality `B_FI^(Delta t) <= B_FI` is a different, exact collision/Fisher statement, but this paper gives strong laboratory context for why binning deserves explicit treatment.

### 4. Electrical pulse shape/amplitude as experimentally useful side information
Timon Schapeler et al., *Electrical trace analysis of superconducting nanowire photon-number-resolving detectors*, Physical Review Applied 22, 014024 (2024).

DOI: `10.1103/PhysRevApplied.22.014024`

Why useful: experimentally shows that rising-edge structure and pulse amplitude contain information beyond a binary click. This is directly aligned with Rev9's statement that an accessible pulse-shape/internal-state mark can preserve information that would otherwise be lost under coarse graining.

### 5. Device-level timing-jitter / IRF context for SPADs
Claudio Bruschini et al., *Single-photon avalanche diode imagers in biophotonics: review and outlook*, Light: Science & Applications 8, 87 (2019).

DOI: `10.1038/s41377-019-0191-5`

Why useful: broad modern review of SPAD timing, TCSPC, detector jitter, and time-resolved applications. Good general grounding citation if the manuscript needs one device-engineering review near the operational section.

### 6. Pulse shape, capacitance, slew rate, and timing jitter
Rasmus Flaschmann et al., *The dependence of timing jitter of superconducting nanowire single-photon detectors on the multi-layer sample design and slew rate*, Nanoscale 15, 1086–1091 (2023).

DOI: `10.1039/D2NR04494C`

Why useful: experimentally connects device structure, pulse shape, capacitive behavior, slew rate, and timing jitter. Supports the paper's insistence that readout/electrical response must be handled through the actual observation model rather than identified blindly with information bandwidth.

### 7. Dynamical activity as a kinetic/time-scale resource in stochastic thermodynamics
Naoto Shiraishi, Ken Funo, and Keiji Saito, *Speed Limit for Classical Stochastic Processes*, Physical Review Letters 121, 070601 (2018).

DOI: `10.1103/PhysRevLett.121.070601`

Why useful: establishes a thermodynamic speed-limit context in which dynamical activity is explicitly tied to a time scale. Rev9's rare-fast counterexample is different: it shows that aggregate stationary activity does not by itself bound the conditional post-capture local timing scale without an absolute microscopic rate resource.

### 8. Review of time-symmetric dynamical activity / frenesy
Christian Maes, *Frenesy: Time-symmetric dynamical activity in nonequilibria*, Physics Reports 850, 1–33 (2020).

DOI: `10.1016/j.physrep.2020.01.002`

Why useful: useful terminology/context reference for traffic, escape rates, and dynamical activity in Markov processes. Not needed for the proof.

---

## Older / nice-to-have papers where a clean publisher full text was not necessary for this audit

These are **not required** for Rev9's correctness. If the author can readily obtain PDFs, they could provide historical physical grounding for SPAD timing-tail mechanisms and timing resolution.

### A. Detector-size dependence of SPAD timing resolution
A. L. Lacaita and M. Mastrapasqua, *Strong dependence of time resolution on detector diameter in single photon avalanche diodes*, Electronics Letters 26, 2053–2054 (1990).

DOI: `10.1049/el:19901324`

### B. Random photon-assisted avalanche spreading as a timing-jitter mechanism
A. Lacaita, S. Cova, A. Spinelli, and F. Zappa, *Photon-assisted avalanche spreading in reach-through photodiodes*, Applied Physics Letters 62, 606–608 (1993).

DOI: `10.1063/1.108870`

### C. Tail-suppressed detector response for time-resolved photon counting
A. Spinelli, M. A. Ghioni, S. D. Cova, and L. M. Davis, *Avalanche detector with ultraclean response for time-resolved photon counting*, IEEE Journal of Quantum Electronics 34, 817–821 (1998).

DOI: `10.1109/3.668769`

### D. Spatial injection position and SPAD photon-timing jitter
M. Assanelli et al., *Photon-Timing Jitter Dependence on Injection Position in Single-Photon Avalanche Diodes*, IEEE Journal of Quantum Electronics 47, 151–159 (2011).

DOI: `10.1109/JQE.2010.2068038`

### E. Classic high-resolution SPAD timing paper
S. Cova et al., *20-ps timing resolution with single-photon avalanche diodes*, Review of Scientific Instruments 60, 1104–1110 (1989).

DOI: `10.1063/1.1140324`

---

## Conclusion

No supplemental paper found here is needed to rescue or complete a Rev9 proof. The strongest value is translational citation support:

1. Sidorova 2025 / Taylor 2022 for Gaussian-plus-exponential timing tails;
2. Walsh 2016 for real TCSPC temporal binning;
3. Schapeler 2024 for pulse-shape marks carrying measurable side information;
4. Bruschini 2019 for broad SPAD/TCSPC device context;
5. Shiraishi 2018 / Maes 2020 for dynamical-activity terminology and thermodynamic context.

Do not broaden the manuscript merely to cite all of these. Add only the minimal subset if a final reference-grounding pass is desired.