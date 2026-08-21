# Research Log — Round 17: Rev8 hostile-review closure

**Date:** 2026-08-20

## Trigger

A new extreme adversarial re-review of Rev7 independently rechecked the principal theorem stack and found no blocking error in the main results. It identified one concrete formal defect in Appendix A plus two worthwhile clarifications.

The reviewer explicitly recommended only three surgical changes and then submission.

## Repair 1 — rare-fast optical orientation

Section IX assumes forward optical traffic `f >= r`, but the Rev7 Appendix allowed arbitrary positive `a,b,c,q,p,s`.

For the exact stationary family,

`f_R = a R pi_0`, `r_R = b R pi_1`, and

`a A_0 - b A_1 = acp - bqs`.

Therefore Rev8 restricts the fixed positive parameters to

`acp >= bqs`.

Then for every `R>0`, exactly,

`f_R-r_R = R(acp-bqs)/(RD+E) >= 0`.

This is not merely asymptotic. Strict `acp>bqs` gives strict forward bias. The remainder of the rare-fast construction and its scaling are unchanged.

## Repair 2 — finite-area timing branch

Rev8 now states explicitly at the start of the timing-collision section that the finite-area resources `R_2`, `B_FI`, and `H` apply to the absolutely continuous square-integrable timing class. Atomic or more singular timing measures are governed first by the Wiener residue theorem and need not possess finite Fisher spectral area.

No figure redesign was made.

## Repair 3 — one-way activity convention

Rev8 defines stationary one-way activity as total stationary directed jump traffic,

`A_tot = sum_x pi_x sum_{y != x} W_yx`,

with every directed jump counted once. This removes the possible factor-of-two convention ambiguity. The state-1 contribution is therefore `pi_1 lambda_1 <= A`, exactly as used in the thermodynamic bound.

## What did not change

No theorem class, detector model, Fisher operator result, ordering theorem, band-subspace theorem, Parseval law, hazard inequality, Fisher-equivalent bandwidth, Erlang cascade, fixed-moment no-go, clock no-go, or isolated-event thermodynamic bridge was broadened or otherwise revised.

The hostile reviewer independently reported that these principal derivations survive.

## Reproducible Rev8 generation

Frozen input source:

- `manuscript/event_resource_theorem_rev7.tex`
- `manuscript/appendix_rare_fast_counterexample_rev7.tex`

Assertion-based generator:

- `manuscript/apply_rev8_referee_surgical.py`

Expected generated-source hashes:

- `event_resource_theorem_rev8.tex`: `07068067744c8cff464931739505e49850c97d68a9c5b9fa63324c6251711a09`
- `appendix_rare_fast_counterexample_rev8.tex`: `f9afbdf7e0fd6cc1b57a3a4e00197148e907fc9ed7691a7f9dd42106e16ba665`

Recorded in `manuscript/REV8_SHA256SUMS.txt`.

## Independent local verification

Rev8 was generated from the independently verified Rev7 artifact `9429898246`, not from an unverified copy.

Full LaTeX compilation with bibliography and cross-references succeeded.

Verified Rev8 manuscript PDF:

- pages: 25
- bytes: 364825
- SHA-256: `bb7dba5a12f5b74181968060b0a6776d7847fad69dfb00090c76425d35974f86`

The three affected layout regions were visually inspected:

- finite-area branch paragraph;
- one-way activity definition and thermodynamic bound;
- Appendix orientation condition and exact proof;
- shifted final references page.

No new overlap or clipping was found. The only material TeX overfull warning remains the inherited approximately `2.45667 pt` line involving `timing-concentration`.

## PRApplied package verification

A Rev8 Physical Review Applied submission copy was also generated and compiled.

Submission PDF:

- pages: 25
- bytes: 365072
- SHA-256: `60da4f9a3919ffdf64d450b5397755a75109d4fc2a0a374a8132a93931092c37`

Complete submission ZIP SHA-256:

`92fd38711b4672f036fd4d95acd5e626c63972d0ca31def782c9f2447971e834`

The APS-compatible purely mathematical Data Availability statement is included. The substantive-AI acknowledgment remains intentionally unfinished until the human author supplies a literally truthful description of how the AI-assisted derivations, citations, and manuscript were personally verified.

## CI / temporary validation cleanup

Temporary draft PR `#15` was closed unmerged. The temporary validation branches were neutralized to the clean publication head.

Steady-state `.github/workflows/manuscript-check.yml` is read-only. It:

1. generates Rev8 from frozen Rev7;
2. verifies the generated hashes against `REV8_SHA256SUMS.txt`;
3. compiles Rev8;
4. uploads the verified artifact;
5. performs no self-commit or source mutation.

## Publication posture

**Rev8 closes the hostile-review loop.**

Do not start another broad defensive revision. Reopen the first-paper theory only for a new concrete referee-level defect.

Remaining work is administrative submission finalization: author metadata, affiliation, corresponding-author email/ORCID, truthful AI disclosure, and any applicable funding/conflict/prior-submission declarations.