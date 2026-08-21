# Physical Review Applied package validation — Rev10

**Status:** technically validated; personal/administrative metadata pending.

Rev10 preserves the complete Rev9 theorem stack and adds one applied worked example based on a published detector IRF. No theorem, proof, or resource inequality changed.

## Worked literature example

Source: A. Spinelli, M. A. Ghioni, S. D. Cova, and L. M. Davis, *Avalanche Detector with Ultraclean Response for Time-Resolved Photon Counting*, IEEE Journal of Quantum Electronics 34, 817–821 (1998), DOI `10.1109/3.668769`.

Approximate graphical digitization of the normalized Fig. 3 traces gives:

- DJ-SPAD: reported FWHM `35 ps`; Gaussian-from-FWHM `9.49 GHz`; figure-digitized `B_FI = 9.160 GHz`.
- MCP: reported FWHM `25 ps`; Gaussian-from-FWHM `13.29 GHz`; figure-digitized `B_FI = 5.977 GHz`.
- Thus FWHM ranks the MCP first, while full-shape `B_FI` ranks the DJ-SPAD first; `B_FI(DJ)/B_FI(MCP) = 1.533`.

The digitized points and a dependency-free analysis script are included in `manuscript/`. The example is explicitly labeled approximate figure digitization, not a reconstruction of the authors' raw TCSPC event data.

## Canonical Rev10 build

- pages: 32
- generated main-source SHA-256: `9d9e8b1a773121dd69e0a378cf235e90e7d89dc01ebe426222a78a8c20500501`
- worked-section SHA-256: `8dfb0e0a2031f49082c202b8e17f89d6a76d526096176f6679ce7d4636fa425d`
- digitized CSV SHA-256: `fd2501d51963c58e4c0df1785a4858bdd1bba8b9dece28da080c2f04980d8082`
- analysis-script SHA-256: `13b57700b1add6944e032a56a8b823403e639f06a7055d9304f1b438e67b54ba`
- PDF SHA-256: `fe261ba21db5ac04f76e57dd61bc37b105616fe4c3ccabc5bd6b211145055c29`

No undefined citations or cross-references remain. The only material overfull warning is the inherited approximately `2.45667 pt` `timing-concentration` line in Appendix A. The new worked-example table/page and shifted neighboring pages were visually inspected.

## PRApplied submission build

- pages: 33
- submission-TeX SHA-256: `49bff3155aab944c4336c97c774a7aa5ca9758e489eb048e6f929b78b2ba7eda`
- PDF SHA-256: `5ff01f6c9d50fcf6e7e0fd59be34e65911a9abd7459a6a348df3e2c70f63e467`
- final package ZIP SHA-256: `6670b3e1bd1c0ef133e052bb74c515ca670c6337be43d3805f09f0e627ce201f`

The final package includes the validated PRApplied manuscript source/PDF, the worked-example digitization and analysis script, bibliography/figure inputs, Data Availability statement, cover-letter draft, exact 100-word justification, and AI-disclosure draft. `FINAL_PACKAGE_SHA256_REV10.txt` is kept outside the ZIP to avoid self-reference.

The submission copy updates Data Availability truthfully: no new experiments were performed, but the manuscript now analyzes an approximate digitization of a published figure; the digitized points and script are supplied with the source. The worked-example pages, Data Availability/Appendix transition, and final reference pages were visually inspected.

## Remaining submission blockers

Only factual human metadata/compliance remain: author identity/order, affiliation, email, ORCID, truthful AI-verification wording, and applicable funding/conflict/prior-submission declarations.
