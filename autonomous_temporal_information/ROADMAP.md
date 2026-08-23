# Roadmap — Autonomous Temporal Information Law

**Branch:** `agent/autonomous-temporal-information-law`

## Current state

The PRX Quantum R3 two-regime manuscript is build-verified, standalone, and **science-frozen**.

The post-R3 research program has now reached a corrected theorem at **WP32** and a hostile audit at **WP33**.

**WP31 is superseded.**

## Completed post-R3 arc

### D1 — implementation coupling identity

For smooth unitary dilations, the target kernel Hessian is exactly the squared implementation coupling into the empty target sector.

### D2 — first-order minimum

For a prescribed pure-boundary tangent,

`V_min=(1/4)Tr H_SLD`.

### D3 — prescribed kernel 2-jet minimum

For any feasible positive metric-contracted target-kernel Hessian `C`,

`V_min=(1/2)Tr C`.

In clean exact exchange,

`V_min=A_ex^(2)/(hbar nu)`.

### D4 — resonance robustness

WP25 and WP27 replace exact-gap all-or-nothing assumptions by explicit commutator-residual penalties in the finite-radius and rank-boundary regimes.

### D5 — infinite-dimensional information laws

WP28 and WP29 extend the finite-radius and rank-boundary resource laws to separable infinite-dimensional systems under bounded-relative / Hilbert--Schmidt finite-information regularity.

### D6 — infinite-dimensional dynamical cost

WP30 proves the unrestricted infinite-dimensional dilation optimum.

WP32 gives the corrected semibounded **exactly energy-conserving** optimum for arbitrary stationary spectator curvature, including target-energy shells unoccupied at baseline:

`boxed:
inf V_impl=(1/2)Tr C.`

The construction uses classical splitting of baseline weights and nonnegative ancilla energy compensation. Finite quadratic cost is enough for trace-norm `C^2` smoothness.

### D7 — hostile audit

WP33: **PASS** under the stated finite-information assumptions.

The audit also fixes the publication boundary:

- covariant Stinespring dilation is prior art;
- Bures/Uhlmann/QFI horizontal geometry is prior art;
- second-order PSD-cone tangent mathematics is prior art;
- classical nonregular boundary statistics are prior art;
- the narrow candidate contribution is the exact **prescribed rank-changing kernel-2-jet implementation cost** and its autonomous spectral endpoint interpretation.

Priority remains unverified.

## Publication architecture

### Current recommendation

**Do not expand R3 into a comprehensive R4.**

WP21--WP32 now form a separate conceptual paper:

1. kinematic endpoint action becomes exact implementation coupling;
2. exact first-order minimum;
3. exact prescribed nonminimal second-order cost;
4. energy-conserving construction;
5. infinite-dimensional completion;
6. robustness to imperfect resonance.

This is a dynamical implementation paper, not merely another section of the two-regime resource paper.

### Follow-up paper gate

Before drafting prose:

1. freeze a minimal theorem stack;
2. remove results that are mathematically correct but peripheral;
3. run a dedicated significance/prior-art audit;
4. identify the strongest single conceptual theorem;
5. decide which robustness/infinite-dimensional results belong in the main text versus supplement.

## Immediate work order

1. create `FOLLOWUP_DYNAMICAL_THEOREM_STACK.md`;
2. create a dedicated hostile significance/priority gate;
3. perform one more literature search for prescribed second-order state/dilation geometry under energy covariance;
4. if the gate passes, create a new standalone manuscript workspace **separate from R3**;
5. only afterward reopen theorem production.

## Deferred theorem targets

If the follow-up paper exposes a real missing theorem, prioritize:

1. noisy/CPTP implementation cost;
2. approximate-exchange dynamical implementation cost;
3. unbounded-relative-tangent closed quadratic-form theory;
4. Gaussian/CV specialization.

Do not add formal edge-case machinery without a manuscript need.

## Manuscript integrity

Every paper must be scientifically standalone and free of personal repository URLs, usernames, repository names, development history, or reliance on internal files.