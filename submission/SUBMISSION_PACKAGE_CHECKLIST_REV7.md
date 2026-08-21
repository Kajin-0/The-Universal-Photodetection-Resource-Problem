# Rev7 Submission Package Checklist

**Target:** Physical Review Applied — Regular Article

**Status:** Science frozen; submission package mechanically/visually validated; personal and administrative compliance remains.

## Core manuscript assets

- [x] `manuscript/event_resource_theorem_rev7.tex` — canonical first-paper source
- [x] `manuscript/section_waveform_operator_rev7.tex`
- [x] `manuscript/section_operational_bandwidth_rev7.tex`
- [x] `manuscript/appendix_rare_fast_counterexample_rev7.tex`
- [x] `manuscript/figure_resource_hierarchy_rev7.tex`
- [x] `manuscript/figure_jitter_no_go.tex`
- [x] `manuscript/references.bib`
- [x] full Rev7 LaTeX build verified twice in CI
- [x] independent artifact uploaded and checked against canonical source

## Submission support files

- [x] `submission/SUBMISSION_STRATEGY_REV7.md`
- [x] `submission/COVER_LETTER_PRAPPLIED_REV7.md`
- [x] `submission/PRAPPLIED_100_WORD_JUSTIFICATION_REV7.txt`
- [x] `submission/DATA_AVAILABILITY_REV7.txt`
- [x] `submission/AI_DISCLOSURE_DRAFT_REV7.md`
- [x] `submission/BIBLIOGRAPHY_AUDIT_REV7.md`
- [x] `submission/PRAPPLIED_PACKAGE_VALIDATION_REV7.md`
- [x] assertion-based submission generator `manuscript/make_prapplied_submission.py`

## Required before actual submission

### Author metadata

- [ ] replace `Anonymous` author name
- [ ] replace `Anonymous` affiliation with affiliation where the research was conducted
- [ ] designate corresponding author
- [ ] active author email(s)
- [ ] authenticated ORCID for corresponding author
- [ ] confirm author list/order and contributions

### APS policy compliance

- [ ] finalize truthful substantive-AI disclosure, including how the human author directed and verified AI output
- [ ] insert finalized AI disclosure into manuscript acknowledgment section
- [x] Data Availability Statement drafted and inserted by the validated submission generator
- [ ] confirm conflict-of-interest statement if relevant
- [ ] confirm funding/acknowledgment disclosures if relevant
- [ ] confirm any related manuscripts, preprints, or prior APS submission history

### Bibliography

- [x] verify every cited source against DOI/bibliographic metadata
- [x] confirm reference titles are present
- [x] confirm current bibliography entries are actually used / intentionally retained
- [x] final citation-to-claim adversarial pass
- [x] no citation-driven scientific correction required

### Figures/layout

- [x] canonical Rev7 compiles cleanly
- [x] generated Physical Review Applied copy compiles cleanly
- [x] no new visually apparent Rev7 submission-package layout defect
- [x] final visual inspection of all 24 pages after Data Availability insertion
- [x] exact submission PDF/TeX hashes and artifact digest recorded
- [ ] optionally repair inherited approximately `2.45667 pt` appendix overfull line if this can be done without altering meaning; this is not a submission blocker

### Editorial package

- [x] Regular Article selected
- [x] primary journal rationale documented
- [x] 100-word PRApplied justification drafted
- [x] cover letter drafted
- [ ] recommended referees, if desired
- [ ] excluded referees/conflicts, if needed
- [ ] copy exact final title/abstract into submission portal

## Mechanical validation record

- [x] temporary validation PR #14 created only for CI
- [x] GitHub Actions run `32434850102` passed canonical and submission-copy compilation
- [x] submission artifact ID `9430408451`
- [x] artifact ZIP SHA-256 `0ce70d971c0038fe5eb13eccb95b4ede45272e4a2dcb8297d212eff579e2418f`
- [x] submission PDF SHA-256 `e80562d69146514dede7c201c6aff29040002296ae10e4e8ff9876120dc6a2b8`
- [x] submission TeX SHA-256 `3a26badedf7c1155801447f0dd803d2f93da09a574361998c26cea8dfabe4979`
- [x] source diff confirms only compliance insertion before `\\appendix`
- [x] canonical theorem source remains unchanged

## Final submission gate

Do not submit until all unchecked items that actually apply are resolved. The remaining required items are personal/administrative; none requires reopening the theorem stack.
