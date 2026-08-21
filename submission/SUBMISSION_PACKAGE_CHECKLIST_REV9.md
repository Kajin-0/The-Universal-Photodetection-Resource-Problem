# Rev9 Submission Package Checklist

**Target:** Physical Review Applied — Regular Article

**Status:** Scientific, translational, and empirical-grounding content validated; personal/administrative compliance remaining.

## Core manuscript assets

- [x] frozen Rev7 theorem source
- [x] assertion-based Rev8 referee repair and source hashes
- [x] `manuscript/section_practical_grounding_rev9.tex`
- [x] `manuscript/section_empirical_grounding_rev9.tex`
- [x] `manuscript/apply_rev9_grounding.py`
- [x] `manuscript/REV9_SHA256SUMS.txt`
- [x] canonical waveform/operator and operational-bandwidth sections
- [x] Rev8 rare-fast Appendix with `acp >= bqs` repair
- [x] figures and bibliography
- [x] full Rev9 LaTeX+bibliography+cross-reference build
- [x] new translational and empirical-anchor pages visually inspected
- [x] five supplied historical SPAD timing PDFs full-text checked and cited conservatively

## Rev9 grounding gate

- [x] canonical Gaussian, exponential, uniform, Erlang, and Gaussian--exponential mappings checked
- [x] exponential `B_FI/f_3dB = pi/2` checked
- [x] Gaussian--exponential closed-form area checked
- [x] single-mark histogram estimator corrected to `B_FI^(dt)=sum p_i^2/(2 dt)`
- [x] unbiased finite-count pair-collision estimator derived
- [x] finite binning proved to give a lower/coarse-grained `B_FI`
- [x] finite-support inequality corrected to `B_FI >= 1/(2T)`; no false support-only upper bound retained
- [x] density-ceiling upper bound `B_FI <= M/2` stated with its independent assumption
- [x] mark coarse-graining inequality derived by Jensen/data processing
- [x] perfect-latency-mark limit distinguished from downstream TDC refinement
- [x] stochastic-delay cascade distinguished from deterministic TIA amplitude roll-off
- [x] exact DC normalization note added without altering `G(0)=eta`
- [x] thermodynamic rare-fast construction translated as a low-duty-cycle fast local mode
- [x] empirical SPAD literature anchors timing histograms, IRF tails, spatial/threshold dependence, and stochastic avalanche dynamics without entering theorem assumptions

## Submission support files

- [x] `COVER_LETTER_PRAPPLIED_REV9.md`
- [x] exact 100-word `PRAPPLIED_100_WORD_JUSTIFICATION_REV9.txt`
- [x] `DATA_AVAILABILITY_REV9.txt`
- [x] `AI_DISCLOSURE_DRAFT_REV9.md`
- [x] `BIBLIOGRAPHY_AUDIT_REV9.md`
- [x] `PRAPPLIED_PACKAGE_VALIDATION_REV9.md`

## Required before actual submission

- [ ] author name/order
- [ ] affiliation(s)
- [ ] corresponding-author email
- [ ] ORCID
- [ ] finalize truthful substantive-AI acknowledgment
- [ ] applicable funding/conflict disclosures
- [ ] related manuscript/preprint/prior-submission disclosures if applicable
- [ ] optional referee suggestions/exclusions after conflict review
- [ ] final visual inspection after personal metadata and acknowledgment are inserted

Do not reopen the theorem stack unless a new concrete mathematical defect is found.
