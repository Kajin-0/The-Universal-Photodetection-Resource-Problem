# Novelty Audit — Round 6: Targeted Mathematical Search

**Date:** 2026-08-20

## Purpose

Final narrow search for an equation-level collision with the WP32/WP33 autonomous marked-event theorem. This round searched by mathematical mechanism rather than photodetector terminology:

- Poisson random displacement + Fisher information;
- random-delay Poisson channels;
- characteristic functions + timing-jitter Fisher information;
- hazard-rate Fisher-information identities;
- L2 norms of delay densities / information bandwidth;
- characteristic-function inequalities involving Fisher information.

## Results

### Efron & Johnstone — *Fisher's Information in Terms of the Hazard Rate*

Annals of Statistics 18(1), 38–62 (1990), DOI `10.1214/aos/1176347492`.

This work expresses Fisher information of a **parametric lifetime distribution itself** through derivatives of its hazard rate. It is important adjacent probability/statistics literature, but it is not the same object as WP32/WP25:

- Efron–Johnstone: parameter is inside the lifetime density/hazard;
- UPRP event theorem: parameter modulates the incident Poisson source, while the detector delay kernel is parameter independent;
- UPRP's hazard enters as a resource bounding the L2 concentration of the detector timing kernel, not through a derivative `partial_theta h`.

No collision identified.

### Zhang — *Inequalities for characteristic functions involving Fisher information*

Comptes Rendus Mathématique 344(5), 327–330 (2007), DOI `10.1016/j.crma.2007.01.008`.

This work relates characteristic functions of a probability distribution to Fisher information of that **distribution**. It is mathematically adjacent to the appearance of `H(omega)` in UPRP, but the roles differ:

- Zhang bounds characteristic functions using distributional Fisher information;
- UPRP derives an exact source-FI transfer `G(omega)=∫|H_m|²κ(dm)` from Poisson marking/displacement;
- UPRP's integrated bound comes from Parseval plus timing-kernel L2 concentration/hazard resources.

No equivalent marked photodetection theorem identified.

### Poisson-channel / compound-Poisson Fisher-information literature

Searches surfaced work such as Madiman, Johnson & Kontoyiannis on scaled Fisher information, compound Poisson approximation, and Poisson channels. The Fisher-information notion there concerns discrete/Poisson approximation/channel identities and is not the source-modulation timing-transfer functional used by UPRP.

No equation-level collision identified.

### Random-delay / remote-estimation communication literature

Targeted searches did not locate a theorem matching the chain

`Poisson source modulation -> independent marked random delay -> exact |H|² source-FI transfer -> Wiener atomic residue -> Parseval/L2 timing budget -> local hazard completion`.

This remains the most relevant communication-theory novelty gap to monitor, but the present search found no equivalent complete theorem.

## Prior art that remains closer physically

The strongest physically adjacent publications remain:

1. Köllner & Wolfrum (1992): photon requirements for fluorescence-lifetime estimation.
2. Talaga (2009): information-theoretical TCSPC including IRF convolution, information loss, digitization, and sensitivity-bandwidth considerations.
3. Bouchet et al. (2019): Fisher-information lifetime precision with IRF/background.
4. Trinh & Esposito (2021): FI analysis of IRF/photon-statistics resolution.
5. Dechant (2026): general finite-frequency fluctuation-response inequality.

These works require conservative positioning but do not currently reproduce the WP32/WP33 theorem stack.

## Current defensible novelty statement

Do **not** claim novelty for hazard functions, Poisson marking/displacement, characteristic functions, Wiener theory, Parseval, IRF bandwidth, timing-jitter information loss, or Fisher information of lifetime distributions individually.

Current defensible candidate contribution:

> A resource-completeness theorem for source-modulation Fisher-information transfer through autonomous marked photodetection event channels, combining an exact marked random-delay transfer law with atomic high-band residuals, a timing-collision spectral budget, microscopic local-hazard completion, and explicit no-go/repair constructions for exact low-order jitter moments, free synchronous temporal references, and aggregate stationary thermodynamic resources.

## Status

**No direct equation-level prior theorem located in the targeted searches performed so far. Novelty remains provisional, but the remaining risk is now primarily hidden older literature rather than an identified collision.**
