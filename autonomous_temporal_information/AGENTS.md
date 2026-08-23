# AGENTS — Autonomous Temporal Information Law

**Branch:** `agent/autonomous-temporal-information-law`

The repository, not chat history, is authoritative. Research is analytical/theoretical; numerical validation is allowed. Do not make experiments, fabrication, procurement, or laboratory campaigns necessary next steps.

## Current phase

The PRX Quantum R3 manuscript is **build-verified, standalone, and science-frozen**.

The stronger post-R3 theorem chain is also scientifically frozen at **WP32**, hostile-audited in **WP33**, and has been developed as a separate final reviewer-repaired PRA R1 publication package.

**WP31 is superseded.** Its classical-mixture insight survives, but its claim that `H_E=0` handles arbitrary prescribed curvature was false when excess curvature occupies an unpopulated target-energy shell.

Priority remains **unverified, not certified**.

## Read first

1. `../manuscript/dynamical_implementation_cost/MANUSCRIPT_HANDOFF.md`
2. `../manuscript/dynamical_implementation_cost/PRA_R1_FINAL_PUBLICATION_AUDIT_2026-08-23.md`
3. `../docs/CURRENT_RESEARCH_STATE.md`
4. `notes/WP33_HOSTILE_AUDIT_WP32_AND_PRIORITY_BOUNDARY.md`
5. `notes/WP32_REPAIRED_INFINITE_DIMENSIONAL_ENERGY_CONSERVING_2JET_COST.md`
6. `notes/WP31_EXACT_INFINITE_DIMENSIONAL_ENERGY_CONSERVING_2JET_COST.md` — erratum/history only
7. `notes/WP30_INFINITE_DIMENSIONAL_DYNAMICAL_2JET_COST_AND_ENERGY_DOMAIN_BOUNDARY.md`
8. `notes/WP29_INFINITE_DIMENSIONAL_BOUNDARY_SYNTHESIS_ACTION_LAW.md`
9. `notes/WP28_INFINITE_DIMENSIONAL_FINITE_RADIUS_SURVIVAL_LAW.md`
10. `notes/WP27_APPROXIMATE_EXCHANGE_BOUNDARY_SYNTHESIS_ACTION_LAW.md`
11. `notes/WP23_EXACT_PRESCRIBED_2JET_DYNAMICAL_IMPLEMENTATION_COST.md`
12. `../manuscript/autonomous_temporal_information/MANUSCRIPT_HANDOFF.md`

## Frozen R3 theorem story

R3 distinguishes two resource regimes for globally stationary relative temporal information:

- finite affine radius -> pre-existing spectral survival;
- rank-changing zero radius -> positive second-order endpoint synthesis action.

Clean exact-exchange action coefficients are `hbar nu/4` bilateral and `hbar nu/2` one-sided. R3 also contains the SLD-QFI boundary corollary, spectator-curvature no-go, coherent-support mixed bridge, exact `Psi_a` envelope, qutrit hierarchy `12 > 43/4 > 55/8`, and multi-gap shared-Hessian theorem.

Do **not** automatically modify R3 merely because stronger theory exists.

## Post-R3 theorem chain

### WP21--WP23 — unitary implementation cost

For a unitary dilation in the finite-cost implementation class,

`Q partial_j^2 rho Q = 2 Tr_E[(Q⊗I)K_j Omega_0 K_j(Q⊗I)]`.

For prescribed feasible metric-contracted target-kernel Hessian `C`,

`V_min=(1/2)Tr C`.

In the clean single-gap endpoint geometry,

`A_ex^(2)=hbar nu V_min`.

WP23 proves the finite-dimensional exactly energy-conserving version.

### WP24--WP27 — audit and resonance robustness

- `Psi_a(e;p,q)` independently re-derived and brute-force verified: no defect.
- classical boundary nonregularity is prior art, not quantum novelty.
- WP25: finite-radius approximate-gap leakage theorem.
- WP27: rank-boundary approximate-exchange action theorem with explicit off-resonant score-amplitude penalties.

### WP28--WP30 — infinite-dimensional extension

- WP28: finite-radius survival for trace-class baselines with bounded relative tangents.
- WP29: rank-boundary synthesis/action for Hilbert--Schmidt right-relative tangents.
- WP30: unrestricted infinite-dimensional dilation minimum `V_min=(1/2)Tr C`.

### WP32 — repaired exact infinite-dimensional energy-conserving curvature theorem

Assume:

- separable target Hilbert space;
- semibounded self-adjoint `H_T`;
- trace-class baseline strongly stationary under `H_T`;
- pure-boundary derivatives strongly preserving target energy;
- `Q D_j P rho_0^(-1/2)` Hilbert--Schmidt;
- prescribed positive trace-class kernel curvature `C>=C_min` strongly preserving target energy.

A stationary trace-class baseline has a countable joint `rho_0/H_T` eigenbasis on its occupied support. Split one occupied baseline eigenstate into countably many classically incoherent ancilla-labelled copies, replicate its horizontal tangent proportionally across the copies, and attach arbitrary excess-curvature eigenmodes using nonnegative ancilla input/output energies

`a_r=max(0,F_r-E_*)`, `b_r=max(0,E_*-F_r)`

so each branch remains in one exact total-energy eigenspace.

The global direct-sum generator may be unbounded, but finite state-weighted quadratic cost gives summable first- and mixed-second trace-norm derivative majorants. No fourth-moment condition is needed.

Therefore

`inf_(semibounded exactly energy-conserving finite-cost unitary dilations) V_impl=(1/2)Tr C`.

For clean exact exchange,

`A_ex^(2)=hbar nu V_min`.

Unlike WP31, WP32 handles spectator curvature in target-energy shells unoccupied at baseline.

### WP33 — hostile theorem audit

**PASS** under WP32's stated finite-information assumptions.

The audit verifies strong-stationarity/pure-point support, energy preservation of tangent columns and `C_min`, exact flag invisibility, exact curvature/cost reproduction, self-adjoint direct-sum generators, trace-norm `C^2` dominated convergence with quadratic cost, and finite baseline ancilla mean energy by suitable split weights.

## Separate follow-up manuscript — final reviewer-repaired state

Journal-facing title:

> **Exact minimum unitary coupling cost of prescribed rank-changing quantum-state curvature**

The regenerated D2 manuscript is the theorem/proof baseline. PRA R1 is the deterministic journal-facing transform.

A final extreme adversarial review found no blocking mathematical error and produced three implemented refinements:

1. **Theorem 2 covariance range:** the theorem now explicitly cites `Eqs. (17)-(19)` for stationarity/covariance of `rho_0`, every `D_j`, and `C`.
2. **Optimizer scope:** the final paper states that the infinite-dimensional attaining generator may be unbounded; the ancillary Hamiltonian is optimized rather than externally fixed; no bound is claimed on peak/operator-norm coupling, ancilla dimension, controller bandwidth, or controller spectral complexity; exact attainment is not asserted for an externally fixed controller spectrum.
3. **Title precision:** “dynamical cost” was narrowed to **“unitary coupling cost”** because the optimized object is specifically `V_impl=sum_j Var_{Omega_0}(K_j)`.

No theorem coefficient or construction changed.

Canonical files:

- `../manuscript/dynamical_implementation_cost/dynamical_rank_boundary_implementation_cost_pra_r1.tex`;
- `../manuscript/dynamical_implementation_cost/dynamical_rank_boundary_implementation_cost_supplement_pra_r1.tex`;
- `../manuscript/dynamical_implementation_cost/MANUSCRIPT_HANDOFF.md`;
- `../manuscript/dynamical_implementation_cost/PRA_R1_FINAL_PUBLICATION_AUDIT_2026-08-23.md`.

Final observable verification:

- workflow run `32673160217` — **PASS**;
- D2 generation/static theorem gate — **PASS**;
- PRA main/supplement transforms — **PASS**;
- committed-source freshness — **PASS**;
- title/scope/theorem/proof/publication gate — **PASS**;
- main and supplement compilation — **PASS**;
- final LaTeX-quality gate — **PASS**;
- artifact upload — **PASS**.

Final artifact:

- ID `9501942180`;
- SHA-256 `4236d6f514b2f290d302062ab4c7a599c03c817da259f3d9715b787a4d37d640`;
- main 11 pages;
- supplement 10 pages.

The exact PDFs were rendered at 180 dpi and visually inspected. The new title, Theorem 2 equation-range wording, expanded limitations paragraph, equations, bibliography, AI/Data Availability page, and supplement all render cleanly.

## Prior-art discipline

Do not claim novelty for Bures/Uhlmann horizontal lifts, SLD-QFI horizontal geometry, Riemannian Bures curvature, QFI convex-roof variance, generic QSL/control norms, covariant/energy-conserving Stinespring dilation, infinite-dimensional QFI/Bures geometry, classical nonregular boundary statistics, or standard PSD-cone/operator inequalities.

Huang et al. (2026), arXiv:2605.27907, concerns Riemannian Bures curvature near rank-changing states, not the prescribed state-family kernel Hessian contraction `C` optimized here.

The narrow candidate post-R3 contribution is the **exact minimum state-weighted quadratic unitary-coupling cost for independently prescribed feasible rank-changing target-kernel curvature under globally conserving relational dynamics**, together with the autonomous spectral endpoint identity.

Priority remains **unverified, not certified**.

## Publication-policy lock

The PRA main contains:

- `AI-Assisted Research and Verification` for substantive OpenAI ChatGPT / GPT-5.6-series use;
- explicit author verification/responsibility language;
- software-aware Data Availability wording for internal validation scripts.

Re-check then-current APS requirements immediately before submission.

## Current work order

1. keep R3, D2, and reviewer-repaired PRA R1 frozen;
2. do not add theorem material merely to enlarge the manuscript;
3. at actual submission time, re-check then-current APS requirements and replace anonymous author/affiliation metadata only in the submission package;
4. reopen the theorem stack only for a genuine proof defect, direct prior-art collision, referee requirement, or changed journal policy;
5. if new theory is desired, start it as a separate program rather than silently extending PRA R1.

## Manuscript integrity

Every public-facing paper must be scientifically standalone. Never include personal repository URLs, repository names, usernames, development history, or dependencies on internal research files.
