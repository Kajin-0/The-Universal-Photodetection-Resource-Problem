# PRA R1 final publication-facing audit — 2026-08-23

## Verdict

**PASS for the final PRA R1 publication-facing package after an additional extreme adversarial review.**

No blocking mathematical error was identified. The central theorem remains

`V_min(C;D,rho_0) = (1/2) Tr C`,

with exact total-energy-conserving attainability under the stated ancilla assumptions and autonomous specialization

`A_ex^(2) = hbar nu V_min`.

Priority remains **unverified, not certified**.

## Final journal-facing title

> **Exact minimum unitary coupling cost of prescribed rank-changing quantum-state curvature**

The earlier title used “dynamical cost.” The final adversarial review correctly noted that the optimized object is specifically the local state-weighted quadratic unitary-coupling functional

`V_impl = sum_j Var_{Omega_0}(K_j)`.

The title was therefore narrowed to “unitary coupling cost” so it does not imply optimization over every possible notion of dynamical cost.

## Frozen scientific baseline and final textual repair

The audited D2 theorem/proof construction remains the scientific baseline. One mandatory textual correction from the final adversarial review was propagated deterministically through D2 and PRA R1:

- the energy-conserving theorem previously cited only the final equation in the three-line stationarity/covariance block;
- the baseline equation now has its own label;
- Theorem 2 now explicitly assumes `Eqs. (17)-(19)`.

This changes no theorem assumption, coefficient, proof, or construction; it only makes the rendered cross-reference state the assumptions actually used.

The PRA publication transform remains statically compared against the regenerated D2 theorem body. The publication supplement remains title-only relative to the audited D2 supplement from `\author{Anonymous}` onward.

## Final scope clarification from hostile review

The infinite-dimensional attaining construction deliberately optimizes over a freely designable ancillary Hamiltonian and permits an unbounded direct-sum generator when the state-weighted quadratic cost is finite.

The final main text now states explicitly that:

- the generator may be unbounded;
- the ancillary Hamiltonian is part of the optimization rather than externally fixed;
- no bound on peak or operator-norm coupling is claimed;
- no bound on ancilla dimension is claimed;
- no bound on controller bandwidth or controller spectral complexity is claimed;
- exact attainment is not asserted for an externally fixed controller spectrum.

This is a scope clarification, not a weakening of the stated optimization theorem.

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

Huang et al., arXiv:2605.27907 (2026), studies the **Riemannian curvature of the Bures metric itself** near rank-changing density matrices.

That object is distinct from this paper's prescribed quantity

`C = Q sum_j partial_j^2 rho(0) Q`,

which is the physical-parameter-metric contraction of the second derivative of a particular state family projected into the baseline kernel.

The PRA R1 introduction states this separation explicitly and the static gate requires it.

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

The final PRA R1 includes a dedicated `AI-Assisted Research and Verification` section for substantive OpenAI ChatGPT / GPT-5.6-series assistance in derivation exploration, adversarial algebra checks, literature organization, internal numerical-validation code, and manuscript preparation. It states that AI outputs were provisional, that the author directed the scientific questions/proof strategy and independently checked the resulting claims, and that the author takes full responsibility.

Data Availability states that no empirical data were created or analyzed, that internal numerical-validation scripts were used only to cross-check analytic identities and are not required to reproduce the analytic results, and that the scripts are available from the author upon reasonable request.

These are publication-layer statements and do not change the theorem.

## Final deterministic verification after adversarial-review repairs

Observable PR-triggered workflow:

- run `32673160217`;
- canonical base commit at verification: `1e03374d8ee20ca0a058b2b054acf463db3c3e08`;
- disposable PR head adds only a CI marker;
- D2 generation/static theorem gate: **PASS**;
- PRA main transform: **PASS**;
- PRA supplement transform: **PASS**;
- committed-source freshness (`git diff --exit-code`): **PASS**;
- final hostile-review publication/title/scope/theorem/proof gate: **PASS**;
- main compile: **PASS**;
- supplement compile: **PASS**;
- final LaTeX quality gate: **PASS**;
- artifact upload: **PASS**.

Final artifact:

- ID `9501942180`;
- SHA-256 `4236d6f514b2f290d302062ab4c7a599c03c817da259f3d9715b787a4d37d640`;
- main PDF: **11 pages**, `227942` bytes;
- supplement PDF: **10 pages**, `229240` bytes.

## Final visual regression

The exact PDFs from artifact `9501942180` were rendered at 180 dpi and inspected.

Inspection result:

- new “unitary coupling cost” main title clean and balanced;
- supplement title matches exactly;
- Theorem 2 visibly reads `Eqs. (17)-(19)`;
- expanded ancilla/peak-coupling limitations paragraph fits cleanly;
- equations and theorem boxes remain within page bounds;
- no clipping or overlap;
- no broken glyphs;
- no malformed bibliography entries;
- AI-assisted research / acknowledgments / Data Availability page remains clean;
- supplement proof layout unchanged apart from the title.

## Freeze decision

Treat this revised PRA R1 package as the canonical journal-facing state.

Do not add theorem material merely to enlarge the paper. Reopen the scientific layer only for a genuine proof defect, direct prior-art collision, referee requirement, or changed journal policy.
