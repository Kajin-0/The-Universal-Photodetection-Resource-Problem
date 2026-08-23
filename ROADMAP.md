# Research Roadmap

**Updated:** 2026-08-23

**Active branch:** `agent/autonomous-temporal-information-law`

Paper 1 Rev11, Paper 2 Rev7, and the random-time spectral-resource Rev11 manuscript are frozen.

The active autonomous temporal-information program has reached **WP31**. Its PRX Quantum R3 manuscript is build-verified and science-frozen while the stronger post-R3 theorem chain is audited.

## Established autonomous hierarchy

### A1 — finite-radius survival

`(R_lin^2/4)[Tr F_N^tan/N] <= T(nu)`

for finite `N` and arbitrary collective POVM.

Autonomous exchange gives the two-sided local-tail version.

### A2 — rank-boundary synthesis

At zero affine radius, the resource moves to positive second-order endpoint synthesis.

Clean autonomous action coefficients:

- bilateral `hbar nu/4`;
- one-sided `hbar nu/2`.

R3 also contains the SLD-QFI action corollary, spectator-curvature no-go, coherent-support mixed bridge, qutrit resource/QFI/accessibility hierarchy, and multi-gap shared-Hessian sum.

### A3 — exact dynamical implementation meaning

WP21 shows that kernel curvature is exactly the squared implementation coupling into empty sectors.

WP22 gives the exact first-order minimum `V_min=(1/4)Tr H_SLD` for the pure-boundary tangent.

WP23 upgrades this to a prescribed feasible metric-contracted kernel 2-jet:

`boxed: V_min=(1/2)Tr C`.

For clean exact exchange,

`boxed: V_min=A_ex^(2)/(hbar nu)`.

The finite-dimensional minimum is exactly total-energy conserving.

### A4 — exact-gap robustness

WP25 gives the finite-radius leakage-corrected theorem for approximate Bohr gaps.

WP27 gives the rank-boundary counterpart with near-resonant endpoint curvature plus explicit off-resonant score-amplitude penalties.

Therefore exact resonance is not an all-or-nothing assumption in either main regime.

### A5 — infinite-dimensional survival and synthesis

WP28 extends finite-radius survival to separable infinite-dimensional systems under bounded relative tangent regularity.

WP29 extends rank-boundary synthesis under Hilbert--Schmidt right-relative tangent regularity.

### A6 — infinite-dimensional dynamical cost

WP30 proves

`inf_(smooth unitary dilations)V_impl=(1/2)Tr C`

without imposing energy conservation.

WP31 closes the exact-energy-conservation domain issue even when the stationary trace-class state has unbounded occupied target-energy support. Use a classically mixed energy-shell dilation, shellwise optimal generators, and a zero-energy ancilla. Finite quadratic cost is enough for trace-norm `C^2` smoothness.

Hence

`boxed:
inf_(semibounded exactly energy-conserving smooth unitary dilations)
V_impl=(1/2)Tr C`

and, in the clean endpoint geometry,

`boxed: V_min=A_ex^(2)/(hbar nu)`.

## Audit status

- Original theorem stack through WP20: hostile mathematical audit **PASS**.
- `Psi_a` mixed envelope: independently re-derived and brute-force validated.
- WP23 prescribed-2-jet theorem: dedicated hostile audit **PASS** at the finite-dimensional statement level.
- WP25/WP27 robustness laws: dedicated random validators pass.
- WP28/WP29 truncation validator passes.
- WP31 shell-dilation validator is committed and targets the unbounded-generator / finite-state-weighted-cost regime.
- Priority remains **unverified, not certified**.

## Prior-art discipline

Do not claim novelty for Page--Wootters/modes of asymmetry, generic Fisher/QFI/Bures/Holevo theory, Bures/Uhlmann horizontal lifts, classical nonregular boundary statistics, covariant/energy-conserving Stinespring dilation theory, generic quantum speed limits/control norms, infinite-dimensional QFI/Bures functional analysis, or standard operator inequalities.

The narrow post-R3 candidate contribution is the **frequency-resolved endpoint synthesis action as the exact minimum state-weighted quadratic implementation-coupling cost for a prescribed feasible rank-changing local kernel 2-jet under globally conserving relational dynamics**, with controlled detuning and infinite-dimensional extensions.

## Current gate

Pause theorem proliferation long enough to make the current result publication-grade.

### Immediate work order

1. hostile-audit WP31's compactness/stationary-energy-support lemma;
2. hostile-audit its trace-norm `C^2` dominated-convergence step;
3. extend the WP31 validator to mixed and degenerate shell baselines with random PSD excess curvature;
4. perform a targeted priority search for prescribed-second-order-jet Stinespring/purification implementation-cost results;
5. decide between:
   - **R4 integration** of only the strongest post-R3 result(s), or
   - a **separate dynamical/infinite-dimensional follow-up paper** centered on WP21--WP31.

### Next theorem targets only after that gate

1. noisy/CPTP implementation cost;
2. unbounded-relative-tangent quadratic-form theory;
3. approximate-exchange dynamical cost combining WP27 with WP31;
4. Gaussian/CV specialization only after the abstract infinite-dimensional results are stabilized.

## Manuscript integrity

Every public-facing paper must be scientifically standalone. Never include personal repository URLs, usernames, repository names, development history, or dependencies on internal research files.

## Documentation discipline

Every material theorem, counterexample, proof repair, validator, prior-art collision, or publication decision must update the active research notes, autonomous landing files, and top-level landing files.