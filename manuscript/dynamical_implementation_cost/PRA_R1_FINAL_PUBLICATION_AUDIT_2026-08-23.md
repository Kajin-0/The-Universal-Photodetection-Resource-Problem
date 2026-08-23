# PRA R1 final publication-facing audit — 2026-08-23

## Verdict

**PASS for the current PRA R1 publication-facing package.**

No new theorem defect was found. No direct known prior-art collision was identified for the exact optimization problem

`V_min(C;D,rho_0) = (1/2) Tr C`

with independently prescribed feasible metric-contracted target-kernel curvature, exact total-energy-conserving attainability, and the autonomous endpoint identity

`A_ex^(2) = hbar nu V_min`.

This is not a priority certificate. Priority remains **unverified, not certified**.

## Frozen scientific baseline

The audited D2 theorem/proof layer remains frozen.

The PRA R1 transform is permitted to change only publication-facing material:

- title;
- abstract;
- introduction/prior-art framing;
- AI-assisted research disclosure;
- acknowledgments;
- Data Availability;
- supplement title.

The main theorem body is statically compared to D2 from the fixed setup paragraph through the acknowledgments boundary. The publication supplement is required to equal the audited D2 supplement byte-for-byte from `\author{Anonymous}` onward.

## Hostile prior-art boundary check

The main novelty risks considered were:

1. first-order Bures/Uhlmann purification geometry and `QFI/4` minimization;
2. channel/Kraus-gauge and noisy-metrology purification minimizations;
3. PSD-cone/parabolic second-order tangent geometry;
4. covariant or energy-conserving Stinespring dilation;
5. quantum-speed-limit/control-norm inequalities;
6. infinite-dimensional Bures/QFI functional analysis;
7. recent rank-changing Bures-curvature work.

No item above was found to state the paper's exact prescribed-curvature implementation-cost theorem.

### 2026 rank-changing Bures-curvature result

Huang et al., arXiv:2605.27907 (2026), studies the **Riemannian curvature of the Bures metric itself** near rank-changing density matrices, including singular geometric behavior.

That object is close enough in terminology to require explicit separation, but it is mathematically different from this paper's prescribed quantity:

`C = Q sum_j partial_j^2 rho(0) Q`,

which is the physical-parameter-metric contraction of the second derivative of a particular state family projected into the baseline kernel.

Action taken:

- added bibliography key `HuangEtAl2026`;
- added an explicit distinction in the PRA R1 introduction;
- added a static-gate marker requiring the citation so this separation cannot silently regress.

## Claim boundary

Do **not** claim novelty for:

- Bures/Uhlmann or SLD-QFI horizontal purification geometry;
- Riemannian curvature of the Bures metric;
- channel Fisher/Kraus-gauge/fibre-bundle geometry;
- covariant Stinespring dilation as such;
- generic energy-conserving dilation theory as such;
- generic quantum speed limits;
- generic PSD-cone second-order tangent geometry;
- classical nonregular boundary statistics;
- infinite-dimensional Bures/QFI functional analysis.

Allowed working novelty claim, still subject to external priority uncertainty:

> We determine the exact minimum state-weighted quadratic coupling required to realize a prescribed feasible rank-changing kernel second-order curvature of a quantum state, show that the minimum can be attained under exact total-energy conservation even in separable infinite dimension, and identify the frequency-resolved endpoint synthesis action of an autonomous temporal mode as precisely `hbar nu` times this minimum cost.

## APS policy audit

Two publication-policy issues were corrected.

### Substantive AI use

The research process used OpenAI ChatGPT / GPT-5.6-series models substantively for:

- derivation exploration;
- adversarial algebra checks;
- literature organization;
- generation and debugging of internal numerical-validation code;
- manuscript preparation.

Because this is broader than prose editing, the final PRA R1 main includes a dedicated unnumbered section:

`AI-Assisted Research and Verification`.

It records:

- the provider/tool/model family;
- the substantive research uses;
- that AI outputs were provisional;
- that the author directed the scientific questions and proof strategy;
- independent checking against explicit analytic derivations, constructive examples, numerical validators, and primary literature;
- full author responsibility.

Acknowledgments remain anonymous-review safe and do not duplicate the substantive disclosure.

### Data / software availability

The earlier sentence “No data were created or analyzed” was too categorical because internal numerical-validation scripts were generated and used.

The final statement instead says:

- no **empirical** data were created or analyzed;
- internal numerical-validation scripts were used only to cross-check analytic identities;
- those scripts are not required to reproduce the analytic results;
- the analytic support is contained in the Article and Supplemental Material;
- the validation scripts are available from the author upon reasonable request.

The static gate requires this policy-aware wording.

## Final deterministic verification

Final observable workflow run:

- run `32667189807`;
- verified canonical package commit `d100d526b823ed6a7807d0d4cb344b3ba92a5f42` plus a one-line disposable PR trigger;
- D2 generation/static theorem gate: **PASS**;
- PRA main transform: **PASS**;
- PRA supplement transform: **PASS**;
- committed-source freshness (`git diff --exit-code`): **PASS**;
- publication identity/title/theorem/proof/disclosure/prior-art gate: **PASS**;
- main compile: **PASS**;
- supplement compile: **PASS**;
- final LaTeX quality gate: **PASS**;
- artifact upload: **PASS**.

Final artifact:

- ID `9500374374`;
- SHA-256 `7bc86f37407f1a4875e0f4a6cd3aaa14db4cf61166afd2efd5df8c1f3fa7e7b4`;
- main PDF: 11 pages, 227654 bytes;
- supplement PDF: 10 pages, 229237 bytes.

## Visual regression

The exact final PDFs from artifact `9500374374` were rendered at 180 dpi.

Inspection result:

- title page clean;
- main/supplement titles match;
- equations and theorem boxes remain within page bounds;
- no clipping or overlap;
- no broken glyphs;
- no visually malformed bibliography entries;
- AI-assisted research / acknowledgments / Data Availability page clean at full-resolution inspection;
- supplement proof layout unchanged apart from the corrected title.

## Freeze decision

Treat this PRA R1 package as the canonical journal-facing state.

Do not add theorem material merely to enlarge the paper. Reopen the frozen scientific layer only if a genuine proof defect, direct prior-art collision, referee requirement, or changed journal policy requires a substantive revision.
