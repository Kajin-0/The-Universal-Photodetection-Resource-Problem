# Physical Review Applied package validation — Rev11

**Status:** technically validated; personal/administrative metadata pending.

Rev11 preserves the complete Rev10 theorem stack and worked detector example. It adds a positioning clarification connecting the single-mark Fisher-equivalent bandwidth to conventional one-sided equivalent noise bandwidth (ENBW), plus a practical multinomial-bootstrap uncertainty prescription for the binned histogram estimator. No theorem, proof, resource inequality, or worked-example number changed.

## ENBW positioning correction

For one unresolved mark, H(0)=1 and

B_FI = ∫_0^∞ |H(2πf)|² df,

which is mathematically the conventional one-sided ENBW of the normalized timing transfer function. Rev11 states this explicitly and cites Motchenbacher & Connelly (1993). It also states what is distinct here: H is a stochastic registration-delay characteristic function; the retained-mark G is not generally the ENBW of the mark-discarded scalar timing law; its spectral area equals the collision resource; and the event-channel theory supplies Fisher ordering, microscopic hazard bounds, and inverse resource costs.

## Histogram uncertainty note

Rev11 adds a multinomial plug-in bootstrap prescription for finite-count uncertainty of the binned pair-collision estimator and explicitly excludes systematic instrument/deconvolution uncertainties from that bootstrap interval.

## Canonical Rev11 build

- pages: 33
- generated main-source SHA-256: `fe966f4ab3fa067bb94d200ed09605a1ed3a2cdef9b4488fd0d18a55e95ccb6e`
- practical-section SHA-256: `ae596eb3866fb0d4d628cb0b527e281d802badc6262e68d3618366bb49903ce3`
- references SHA-256: `ee964383107b38fca64bb75f51c18bcc68a20724e57597a100a7db5dd25b9046`
- PDF SHA-256: `9eedbf562ed5fa70b78a8c1c63627e1c578f149074f7f25f3fd3988c8668ecef`

No undefined citations or cross-references remain. The only material overfull warning is the inherited approximately 2.45667 pt `timing-concentration` line in Appendix A. The new ENBW page, histogram-estimator page, and final references were visually inspected.

## PRApplied submission build

- pages: 33
- submission-TeX SHA-256: `f6b3953c977427c08fe1bad5e0926512fba4989a98133ea1e636d942fc0092a2`
- PDF SHA-256: `d9e4a3330543106a272d4aa7b26cf6187bbd2f6ef170db4a8927b06edb824db7`
- package ZIP SHA-256: `b9f1abff76bbcc7a97ca8b2c3038f1e44e5adbb68f230cdb7d13c02431b6183e`

The Data Availability statement remains the Rev10 published-figure-analysis statement. The ENBW page, Data Availability/Appendix transition, and references were visually inspected.

## Remaining submission blockers

Only factual human metadata/compliance remain: author identity/order, affiliation, email, ORCID, truthful AI-verification wording, and applicable funding/conflict/prior-submission declarations.
