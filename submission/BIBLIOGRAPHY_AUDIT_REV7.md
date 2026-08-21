# Rev7 Bibliography and Citation Audit

**Date checked:** 2026-08-20

**Target:** Physical Review Applied

**Manuscript:** `manuscript/event_resource_theorem_rev7.tex`

## Result

**PASSED.** No citation-driven scientific correction to Rev7 was identified.

All ten bibliography entries contain titles. The article metadata and DOI values used by the manuscript were checked against publisher, PubMed/PMC, APS, Optica, university-library, or standard bibliographic records. The literature-positioning sentences in the Introduction and `Relation to detector metrics and prior work` section were also checked against what the cited papers actually establish.

---

## Article references

### Köllner and Wolfrum (1992)

Key: `KollnerWolfrum1992`

- Title: *How many photons are necessary for fluorescence-lifetime measurements?*
- Journal: Chemical Physics Letters 200, 199--204 (1992)
- DOI: `10.1016/0009-2614(92)87068-Z`
- Metadata status: **VERIFIED**
- Manuscript use: photon requirements / lifetime-estimation information context.
- Claim status: **SUPPORTED**. The paper explicitly analyzes the number of detected photons required to reach a desired lifetime-estimation accuracy.

### Talaga (2009)

Key: `Talaga2009`

- Title: *Information-theoretical analysis of time-correlated single-photon counting measurements of single molecules*
- Journal: J. Phys. Chem. A 113, 5251--5263 (2009)
- DOI: `10.1021/jp8082908`
- Metadata status: **VERIFIED**
- Manuscript use: TCSPC information loss, IRF effects, sensitivity--bandwidth tradeoff, and frequency-domain IRF power-spectrum context.
- Claim status: **SUPPORTED**. The paper explicitly states that finite IRF reduces information, discusses a hardware tradeoff between detection sensitivity and bandwidth, and plots effective bandwidth using the power spectra of experimental and idealized IRFs.

### Bouchet, Krachmalnicoff, and Izeddin (2019)

Key: `Bouchet2019`

- Title: *Cramér--Rao analysis of lifetime estimations in time-resolved fluorescence microscopy*
- Journal: Optics Express 27, 21239--21252 (2019)
- DOI: `10.1364/OE.27.021239`
- Metadata status: **VERIFIED**
- Manuscript use: Fisher-information lifetime bounds including finite IRF and background.
- Claim status: **SUPPORTED**.

### Trinh and Esposito (2021)

Key: `TrinhEsposito2021`

- Title: *Biochemical resolving power of fluorescence lifetime imaging: untangling the roles of the instrument response function and photon-statistics*
- Journal: Biomedical Optics Express 12, 3775--3788 (2021)
- DOI: `10.1364/BOE.428070`
- Metadata status: **VERIFIED**
- Manuscript use: Fisher-information analysis of the joint roles of IRF and photon statistics.
- Claim status: **SUPPORTED**.

### Koppell and Kasevich (2021)

Key: `KoppellKasevich2021`

- Title: *Information transfer as a framework for optimized phase imaging*
- Journal: Optica 8, 493--501 (2021)
- DOI: `10.1364/OPTICA.412129`
- Metadata status: **VERIFIED**
- Manuscript use: conservative prior-art statement that Fisher-information-based information transfer functions exist in another optical setting.
- Claim status: **SUPPORTED**. The paper explicitly uses Fisher information to define an information transfer function for phase-imaging design.

### Deng, Van Thourhout, and Hens (2026)

Key: `Deng2026`

- Title: *Understanding and Equivalence of Response Time Measurements in Photodetectors*
- Journal: ACS Photonics 13, 1752--1756 (2026)
- DOI: `10.1021/acsphotonics.6c00438`
- Metadata status: **VERIFIED**
- Manuscript use: current photodetector-metrology support for the statement that square-pulse, ultrafast-transient, and `-3 dB` response measurements need not be equivalent outside specified regimes.
- Claim status: **SUPPORTED**. The paper explicitly analyzes those three methods, states that they probe distinct physical processes, and identifies when they are equivalent or divergent.

### Dechant (2026)

Key: `Dechant2026`

- Title: *Finite-Frequency Fluctuation-Response Inequality*
- Journal: Physical Review Letters 136, 207101 (2026)
- DOI: `10.1103/3hs9-dz3d`
- Metadata status: **VERIFIED**
- Manuscript use: prior art for finite-frequency response/fluctuation inequalities and broadband SNR bounds in Markovian dynamics.
- Claim status: **SUPPORTED**. The paper derives a finite-frequency fluctuation-response inequality for general Markovian dynamics and a frequency-integrated/broadband SNR upper bound.

---

## Book references

### Kingman (1993)

Key: `Kingman1993`

- J. F. C. Kingman, *Poisson Processes*, Oxford University Press / Clarendon Press, Oxford (1993).
- Metadata status: **VERIFIED / STANDARD PRINT CITATION**.
- Note: some modern publisher records surface a late-1992 publication date, while standard bibliographies and course references cite the 1993 OUP/Clarendon edition. The manuscript's 1993 citation is conventional and defensible; no correction is required.
- Manuscript use: Poisson marking/displacement background.

### Daley and Vere-Jones (2003)

Key: `DaleyVereJones2003`

- *An Introduction to the Theory of Point Processes, Volume I: Elementary Theory and Methods*, 2nd ed., Springer, New York (2003).
- DOI: `10.1007/b97277`
- Metadata status: **VERIFIED**
- Manuscript use: point-process background.

### Katznelson (2004)

Key: `Katznelson2004`

- Y. Katznelson, *An Introduction to Harmonic Analysis*, 3rd ed., Cambridge University Press, Cambridge (2004).
- Metadata status: **VERIFIED**
- Manuscript use: classical Wiener theorem / harmonic-analysis background.

---

# Citation-to-claim adversarial check

## Introduction

The literature paragraph is appropriately conservative:

- Köllner/Wolfrum is not presented as deriving the current detector theorem; only as early Fisher/Cramér--Rao lifetime-estimation context.
- Talaga is properly credited for IRF convolution/information loss and sensitivity--bandwidth discussion.
- Bouchet and Trinh/Esposito are properly credited for finite-IRF / photon-statistics Fisher-information analysis.
- Koppell/Kasevich prevents an overclaim that Fisher-information transfer functions are generically new.
- Deng et al. supports the motivation that conventional response-time measurements can probe different dynamics.

No priority language needs strengthening.

## Relation to detector metrics and prior work

The sentence

> Talaga's TCSPC analysis already emphasized IRF-induced information loss, detector sensitivity--bandwidth tradeoffs, and the frequency-domain power spectrum of detector IRFs

is **supported directly** by the 2009 article and should be retained.

The sentence describing Deng et al. as showing that square-pulse, ultrafast-pulse, and `-3 dB` response-time measurements need not be equivalent outside specific regimes is **supported directly**.

The Dechant paragraph is also appropriately delimited: it credits finite-frequency response/fluctuation and broadband SNR inequalities while explicitly distinguishing those quantities from the manuscript's first-registration Parseval identity. No collision was found with the Rev7 theorem claim.

---

# Bibliography-format conclusions

- **All current entries have title fields.** This satisfies the important Physical Review Applied reference-title requirement at the source level.
- No obviously unused entry was found; every current key appears in the manuscript's cited literature/background stack.
- No DOI correction is required.
- Adding book DOIs for Kingman or Katznelson would be optional metadata enrichment, not a correctness repair.
- Do not alter the bibliography merely to make it look newer or denser; the present literature set is intentionally narrow and claim-targeted.

## Gate status

- Bibliographic metadata: **PASSED**
- Reference-title presence: **PASSED**
- Citation-to-claim consistency: **PASSED**
- Priority/novelty restraint: **PASSED**

No theorem or manuscript prose change is required from this audit.
