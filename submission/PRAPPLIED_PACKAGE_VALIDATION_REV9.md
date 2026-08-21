# Physical Review Applied package validation — Rev9

**Status:** technically validated; personal/administrative metadata pending.

Rev9 preserves the Rev8 theorem stack and adds operational/translational grounding. A final empirical-anchor subsection now cites five full-text historical SPAD timing papers supplied and checked directly; these experiments motivate the timing phenomenology but are not assumptions of the theorem stack.

## Canonical manuscript build

- pages: 31
- bytes: 390412
- PDF SHA-256: `ef566682d6b47eb0d133bca497f76503fc57817b98846ee4241e7a45fb4bd08d`
- generated main-source SHA-256: `8ae3e4eb89e3af48823e62332481dbb63912281aa75b653cf46f35166b892611`
- practical-section SHA-256: `b4702642705b01ef811e95f5a3d2d0686bb951122c337fd438d0b53fa0a18c3f`
- empirical-section SHA-256: `512d1d6b43c89933bf723476fa3bae6f0ed54d4d45688f3784602a70a8f12af4`

## PRApplied submission build

- pages: 32
- bytes: 391123
- PDF SHA-256: `770bd2c58a5adcef0c88c6275a29e2a9a74441b02dca63415af6da394815533e`
- submission-TeX SHA-256: `6d71ea050b047000eed027e3fa1b0d6523c9aa4a52f5315b370fe3b4e6b1d0c0`

Full LaTeX, bibliography, and cross-reference compilation succeeded. No undefined citations or references remain. The only material overfull box is the inherited approximately `2.45667 pt` `timing-concentration` line from the rare-fast Appendix.

The empirical-anchor pages, Data Availability / Appendix transition, and final two reference pages were visually inspected after the rebuild. No clipping, overlap, malformed equations, or broken references were found.

## Full-text empirical grounding now checked

The following supplied papers were read directly and cited only for claims they support:

- Cova et al. (1989), DOI `10.1063/1.1140324`: TCPC timing histogram, measurement-chain timing contributions, and sub-FWHM inference via statistical/convolution analysis.
- Lacaita and Mastrapasqua (1990), DOI `10.1049/el:19901324`: detector-diameter and absorption-position dependence of avalanche timing.
- Lacaita et al. (1993), DOI `10.1063/1.108870`: stochastic photon-assisted avalanche spreading as a timing-jitter mechanism.
- Spinelli et al. (1998), DOI `10.1109/3.668769`: Gaussian-like fast IRF component, diffusion tails, and the practical importance of tail/secondary-bump suppression beyond FWHM.
- Assanelli et al. (2011), DOI `10.1109/JQE.2010.2068038`: injection-position, discriminator-threshold, and avalanche-propagation contributions to timing jitter.

## Remaining submission blockers

Only factual human metadata/compliance remain: author identity/order, affiliation, email, ORCID, truthful AI-verification wording, and applicable funding/conflict/prior-submission declarations.

The final package ZIP hash is recorded separately in repository file `submission/FINAL_PACKAGE_SHA256_REV9.txt`, which is intentionally excluded from the ZIP to avoid a self-referential hash.
