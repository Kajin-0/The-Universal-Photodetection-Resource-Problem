# Manuscript handoff — minimum dynamical coupling cost

**Branch:** `agent/autonomous-temporal-information-law`

## Phase

**D1 — theorem-first standalone manuscript formed; build verification pending.**

This is a separate follow-up paper. The existing R3 temporal-resource manuscript remains frozen and must not be expanded merely because this follow-up exists.

## Canonical manuscript files

- `dynamical_rank_boundary_implementation_cost_draft.tex`
- `dynamical_rank_boundary_implementation_cost_supplement.tex`
- `references.bib`
- `check_tex_static.py`
- `README.md`
- this handoff

Isolated CI:

- `.github/workflows/dynamical-implementation-manuscript-check.yml`

## Scientific center

The paper answers:

> Given a rank-changing quantum-state family with prescribed first-order tangent and prescribed feasible metric-contracted second-order population in the baseline-empty target sector, what is the least state-weighted quadratic dynamical coupling needed to realize that local state jet?

Central theorem:

`V_min = (1/2) Tr C`,

where `C = Q sum_j partial_j^2 rho(0) Q` is the prescribed physical-metric contraction of the target kernel Hessian.

Feasibility requires

`C >= C_min`,

with

`C_min = 2 sum_j Q D_j P rho_0^+ P D_j Q`

in finite dimension, or the Hilbert--Schmidt trace-class analogue in separable infinite dimension.

Exact energy-conserving attainability survives in separable infinite dimension, including unbounded occupied target energies and spectator curvature in target-energy shells empty at baseline. The repaired construction uses classical splitting of baseline branches and nonnegative ancilla input/output energy compensation.

Autonomous temporal specialization:

`A_ex^(2) = hbar nu V_min`.

## Critical proof correction

Never use the superseded shortcut that normalizes a curvature block by baseline population in the same target-energy shell. A prescribed stationary curvature block can be nonzero where the baseline population is zero.

The canonical infinite-dimensional energy-conserving proof instead:

1. uses the countable joint eigenbasis of stationary trace-class `rho_0` and target time translations on occupied support;
2. decomposes excess positive curvature into energy-adapted modes, including modes in unoccupied target-energy shells;
3. splits one occupied baseline eigenstate into countably many classically incoherent ancilla-labelled copies;
4. chooses nonnegative ancilla input/output energies satisfying `E_in+a_r=F_r+b_r`;
5. realizes excess curvature with first-order-invisible orthogonal flags;
6. uses finite quadratic cost to dominate all first and mixed second trace-norm derivatives of the classical branch series.

No fourth-moment condition is needed.

## Novelty / prior-art lock

Do not claim novelty for:

- Bures/Uhlmann or `QFI/4` horizontal purification geometry;
- channel Fisher/Kraus-gauge/fibre-bundle geometry;
- covariant Stinespring dilation;
- generic quantum-speed-limit/control-norm inequalities;
- PSD-cone second-order tangent geometry;
- classical nonregular boundary statistics;
- infinite-dimensional QFI/Bures functional analysis.

Current allowed working novelty sentence, always qualified by unverified priority:

> We determine the exact minimum state-weighted quadratic coupling required to realize a prescribed feasible rank-changing kernel second-order jet of a quantum state, show that the minimum can be attained under exact total-energy conservation even in separable infinite dimension, and identify the frequency-resolved endpoint synthesis action of an autonomous temporal mode as precisely `hbar nu` times this minimum cost.

Priority remains unverified, not certified.

## Main-text architecture

1. define the local state-jet implementation problem;
2. prove the unitary kernel-curvature identity;
3. state PSD-cone feasibility and first-order Bures bridge;
4. prove `V_min=(1/2)Tr C`;
5. impose exact total-energy conservation and state the infinite-dimensional attainability theorem;
6. specialize to autonomous temporal exchange;
7. give the fixed-total-energy zero-net-work example;
8. state coordinate covariance and limitations.

## Supplement architecture

- exact unitary expansion;
- variance decomposition;
- finite-dimensional and trace-class PSD-cone feasibility;
- horizontal minimum;
- orthogonal-flag completion;
- stationary trace-class joint-energy lemma;
- repaired energy-compensation construction for unoccupied target-energy shells;
- direct-sum self-adjointness and trace-norm `C^2` dominated convergence;
- fixed-shell benchmark;
- prior-art boundary notes.

## Manuscript integrity rules

The manuscript and supplement are fully standalone.

Never include:

- personal repository URLs;
- usernames;
- repository/project names;
- internal work-package labels;
- development history;
- instructions that a reader must consult internal research files.

The static gate enforces these restrictions and also fails if the superseded energy-shell shortcut is reintroduced.

## Immediate work order

1. run the isolated CI through an observable PR-triggered workflow;
2. fix the first static or LaTeX failure only, then rerun until green;
3. render and inspect theorem-heavy pages;
4. perform a hostile theorem-language audit against the proof assumptions;
5. only after the build/audit pass, rewrite the abstract/introduction for the selected journal target;
6. do not add new theorem work unless the manuscript audit exposes a genuine gap.
