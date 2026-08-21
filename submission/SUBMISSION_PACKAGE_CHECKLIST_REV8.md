# Rev8 Submission Package Checklist

**Target:** Physical Review Applied — Regular Article

**Status:** Science frozen; administrative compliance remaining.

## Core manuscript assets

- [x] `manuscript/event_resource_theorem_rev7.tex` — frozen Rev8 input / Rev7 predecessor
- [x] `manuscript/appendix_rare_fast_counterexample_rev7.tex` — frozen Rev8 input
- [x] `manuscript/apply_rev8_referee_surgical.py` — assertion-based Rev8 transform
- [x] `manuscript/REV8_SHA256SUMS.txt` — expected generated-source hashes
- [x] generated `event_resource_theorem_rev8.tex`
- [x] generated `appendix_rare_fast_counterexample_rev8.tex`
- [x] `manuscript/section_waveform_operator_rev7.tex`
- [x] `manuscript/section_operational_bandwidth_rev7.tex`
- [x] `manuscript/figure_resource_hierarchy_rev7.tex`
- [x] `manuscript/figure_jitter_no_go.tex`
- [x] `manuscript/references.bib`
- [x] generated Rev8 source hashes verified against recorded expected hashes
- [x] full Rev8 LaTeX+bibliography+cross-reference build verified from independently verified Rev7 artifact
- [x] affected Rev8 pages visually inspected

## Submission support files

- [x] `submission/COVER_LETTER_PRAPPLIED_REV8.md`
- [x] `submission/PRAPPLIED_100_WORD_JUSTIFICATION_REV8.txt`
- [x] `submission/DATA_AVAILABILITY_REV8.txt`
- [x] `submission/AI_DISCLOSURE_DRAFT_REV8.md`
- [x] `submission/PRAPPLIED_PACKAGE_VALIDATION_REV8.md`

## Rev8 referee-hardening gate

- [x] enforce `acp >= bqs` in rare-fast Appendix A
- [x] prove `f_R >= r_R` exactly for every `R>0`
- [x] qualify `R_2/B_FI/H` as the finite-area square-integrable-density branch
- [x] define stationary directed one-way activity convention
- [x] compile and visually inspect affected pages

## Bibliography / claims

- [x] bibliography/citation audit carried forward from validated Rev7 package; references are unchanged in Rev8
- [x] reference titles present / bibliography requirement previously audited
- [x] hostile Rev7 re-review independently rechecked the principal theorem stack; Rev8 adds no new citations

## Figures / layout

- [x] Rev8 manuscript compiles
- [x] no new Rev8 overfull layout defect
- [x] Rev8 PRApplied copy is 25 pages and affected pages plus Data Availability / Appendix transition were visually inspected
- [ ] optionally repair inherited approximately `2.45667 pt` appendix overfull line if it can be done without altering meaning
- [ ] inspect again after personal author metadata and finalized AI acknowledgment are inserted

## Required before actual submission

### Author metadata

- [ ] replace `Anonymous` author name
- [ ] replace `Anonymous` affiliation with affiliation where the research was conducted
- [ ] designate corresponding author
- [ ] active corresponding-author email
- [ ] authenticated ORCID
- [ ] confirm author list/order and contributions

### APS policy / factual declarations

- [ ] finalize truthful substantive-AI disclosure
- [ ] insert finalized AI disclosure into acknowledgment section
- [x] Data Availability Statement prepared and validated
- [ ] confirm conflict-of-interest statement if relevant
- [ ] confirm funding/acknowledgment disclosures if relevant
- [ ] confirm related manuscripts, preprints, or prior APS submission history

### Editorial portal

- [x] Regular Article selected
- [x] primary journal rationale documented
- [x] 100-word PRApplied justification drafted
- [x] cover letter drafted
- [ ] recommended referees, if desired
- [ ] excluded referees/conflicts, if needed
- [ ] copy exact final title/abstract into submission portal

## Final gate

Do not submit until all unchecked items that actually apply are resolved. None of the remaining items requires reopening the theorem stack.
