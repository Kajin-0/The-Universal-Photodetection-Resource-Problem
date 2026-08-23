# AGENTS — Autonomous Temporal Information Law

**Branch:** `agent/autonomous-temporal-information-law`

The repository, not chat history, is authoritative. Research is analytical/theoretical; numerical validation is allowed. Do not make experiments, fabrication, procurement, or laboratory campaigns necessary next steps.

## Current phase

The PRX Quantum R3 manuscript is **build-verified, standalone, and science-frozen**.

The stronger post-R3 theorem chain is also now scientifically frozen at **WP32**, hostile-audited in **WP33**, and has been developed as a separate final PRA R1 publication-facing manuscript package.

**WP31 is superseded.** Its classical-mixture insight survives, but its claim that `H_E=0` handles arbitrary prescribed curvature was false when excess curvature occupies an unpopulated target-energy shell.

Priority remains **unverified, not certified**.

## Read first

1. `../manuscript/dynamical_implementation_cost/MANUSCRIPT_HANDOFF.md`
2. `../manuscript/dynamical_implementation_cost/PRA_R1_FINAL_PUBLICATION_AUDIT_2026-08-23.md`
3. `notes/WP33_HOSTILE_AUDIT_WP32_AND_PRIORITY_BOUNDARY.md`
4. `notes/WP32_REPAIRED_INFINITE_DIMENSIONAL_ENERGY_CONSERVING_2JET_COST.md`
5. `notes/WP31_EXACT_INFINITE_DIMENSIONAL_ENERGY_CONSERVING_2JET_COST.md` — erratum/history only
6. `notes/WP30_INFINITE_DIMENSIONAL_DYNAMICAL_2JET_COST_AND_ENERGY_DOMAIN_BOUNDARY.md`
7. `notes/WP29_INFINITE_DIMENSIONAL_BOUNDARY_SYNTHESIS_ACTION_LAW.md`
8. `notes/WP28_INFINITE_DIMENSIONAL_FINITE_RADIUS_SURVIVAL_LAW.md`
9. `notes/WP27_APPROXIMATE_EXCHANGE_BOUNDARY_SYNTHESIS_ACTION_LAW.md`
10. `notes/WP23_EXACT_PRESCRIBED_2JET_DYNAMICAL_IMPLEMENTATION_COST.md`
11. `../manuscript/autonomous_temporal_information/MANUSCRIPT_HANDOFF.md`

## Frozen R3 theorem story

R3 distinguishes two resource regimes for globally stationary relative temporal information:

- finite affine radius -> pre-existing spectral survival;
- rank-changing zero radius -> positive second-order endpoint synthesis action.

Clean exact-exchange action coefficients are `hbar nu/4` bilateral and `hbar nu/2` one-sided. R3 also contains the SLD-QFI boundary corollary, spectator-curvature no-go, coherent-support mixed bridge, exact `Psi_a` envelope, qutrit hierarchy `12 > 43/4 > 55/8`, and multi-gap shared-Hessian theorem.

Do **not** automatically modify R3 merely because stronger theory exists.

## Post-R3 theorem chain

### WP21--WP23 — dynamical implementation cost

For a unitary dilation in the finite-cost implementation class,

`Q partial_j^2 rho Q = 2 Tr_E[(Q⊗I)K_j Omega_0 K_j(Q⊗I)]`.

For a prescribed feasible metric-contracted target-kernel Hessian `C`,

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

A stationary trace-class baseline has a countable joint `rho_0/H_T` eigenbasis on its occupied support. Split one occupied baseline eigenstate into countably many **classically incoherent ancilla-labelled copies**. Replicate its horizontal tangent proportionally across the copies, and attach arbitrary excess-curvature eigenmodes using nonnegative ancilla input/output energies

`a_r=max(0,F_r-E_*)`, `b_r=max(0,E_*-F_r)`

so each branch remains in one exact total-energy eigenspace.

The global direct-sum generator may be unbounded, but the baseline is a trace-class classical mixture. Finite quadratic cost gives summable first- and mixed-second trace-norm derivative majorants, so no fourth-moment condition is needed.

Therefore

`boxed:
inf_(semibounded exactly energy-conserving finite-cost unitary dilations)
V_impl=(1/2)Tr C.`

For clean exact exchange,

`boxed: A_ex^(2)=hbar nu V_min.`

Unlike WP31, WP32 also handles spectator curvature in target-energy shells unoccupied at baseline.

### WP33 — hostile theorem audit verdict

**PASS** under WP32's stated finite-information assumptions.

The audit explicitly verifies:

- strong stationarity + trace-class compactness -> countable occupied pure-point energy support;
- energy preservation of horizontal tangent columns;
- strong energy preservation of `C_min` and the excess curvature;
- exact first-order invisibility of orthogonal ancilla flags;
- exact curvature and cost reproduction;
- self-adjoint direct-sum generators;
- trace-norm `C^2` dominated convergence with only quadratic cost;
- finite baseline ancilla mean energy can also be imposed by a suitable choice of split weights.

## Separate dynamical-cost manuscript — final state

Journal-facing title:

> **Exact minimum dynamical cost of prescribed rank-changing quantum-state curvature**

The audited D2 manuscript is the frozen theorem/proof baseline. PRA R1 is a deterministic publication-facing transform.

Canonical files:

- `../manuscript/dynamical_implementation_cost/dynamical_rank_boundary_implementation_cost_pra_r1.tex`;
- `../manuscript/dynamical_implementation_cost/dynamical_rank_boundary_implementation_cost_supplement_pra_r1.tex`;
- `../manuscript/dynamical_implementation_cost/MANUSCRIPT_HANDOFF.md`;
- `../manuscript/dynamical_implementation_cost/PRA_R1_FINAL_PUBLICATION_AUDIT_2026-08-23.md`.

Final observable workflow run `32667189807`: **PASS** for D2 generation/static theorem gate, PRA transforms, committed-source freshness, theorem/proof freeze, main/supplement compilation, final LaTeX-quality gate, and artifact upload.

Final artifact `9500374374`, SHA-256 `7bc86f37407f1a4875e0f4a6cd3aaa14db4cf61166afd2efd5df8c1f3fa7e7b4`, contains the 11-page main and 10-page supplement. The exact final PDFs were render-inspected cleanly.

The final publication-facing hostile audit found no theorem defect or direct known collision. It added an explicit distinction from Huang et al. (2026), arXiv:2605.27907, which concerns the **Riemannian curvature of the Bures metric** near rank-changing states rather than the prescribed state-family kernel Hessian contraction `C` optimized here.

The PRA layer also includes a methods-level `AI-Assisted Research and Verification` disclosure for substantive OpenAI ChatGPT / GPT-5.6-series use and software-aware Data Availability wording for internal numerical-validation scripts. These are publication-layer statements only and do not modify D2 theorem/proof text.

## Validators

Key permanent validators include WP21, WP22, WP23, WP24, WP25, WP27, WP28/WP29, WP31 special-case shell convergence, and

`numerics/verify_wp32_repaired_energy_conserving_2jet_cost.py`

for mixed/degenerate baselines plus random excess curvature in **unoccupied** energy shells.

The manuscript CI additionally enforces deterministic regeneration of the promoted PRA sources, theorem/proof freeze against D2, publication-identity locks, required prior-art/disclosure markers, reference integrity, and final LaTeX quality.

## Prior-art discipline

Do not claim novelty for Bures/Uhlmann horizontal lifts, QFI convex-roof variance, Riemannian Bures curvature, generic QSL/control norms, covariant/energy-conserving Stinespring dilation, infinite-dimensional QFI/Bures geometry, classical nonregular boundary statistics, or standard PSD-cone/operator inequalities.

The narrow candidate post-R3 contribution is the **exact minimum state-weighted quadratic coupling cost for an independently prescribed feasible rank-changing target-kernel curvature under globally conserving relational dynamics**, together with the autonomous spectral endpoint identity.

## Current work order

1. keep R3, D2, and PRA R1 frozen;
2. do not add theorem material merely to enlarge the manuscript;
3. at actual submission time, re-check then-current APS requirements and replace anonymous author/affiliation metadata in the submission package only;
4. reopen the theorem stack only for a genuine proof defect, direct prior-art collision, referee requirement, or changed journal policy;
5. if new theory is desired, start it as a separate program rather than silently extending PRA R1. Highest-value deferred directions remain noisy/CPTP implementation cost, approximate-exchange dynamical cost, unbounded-relative-tangent quadratic-form theory, and Gaussian/CV specialization.

## Manuscript integrity

Every public-facing paper must be scientifically standalone. Never include personal repository URLs, repository names, usernames, development history, or dependencies on internal research files.
