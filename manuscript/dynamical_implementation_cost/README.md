# Dynamical implementation cost — follow-up manuscript workspace

## Status

**New standalone follow-up manuscript workspace.**

The PRX Quantum R3 two-regime manuscript remains frozen and untouched. This workspace develops the separate WP21--WP32 dynamical/infinite-dimensional story.

## Scientific center

The paper should answer one question:

> What is the least state-weighted dynamical coupling required to realize a prescribed rank-changing local quantum-state 2-jet, and how does that cost specialize to an autonomous temporal exchange under exact total-energy conservation?

Central theorem:

`V_min=(1/2)Tr C`

for a prescribed feasible metric-contracted target-kernel Hessian `C`.

Clean autonomous temporal specialization:

`V_min=A_ex^(2)/(hbar nu)`.

## Scope lock

The paper is **not** a new generic theory of quantum implementation cost, thermodynamic work, Bures geometry, covariant Stinespring dilation, quantum speed limits, or infinite-dimensional quantum metrology.

Mandatory prior-art separation:

- Bures/Uhlmann and QFI horizontal/purification minimization are first-order prior art;
- Fujiwara--Imai/channel-extension Kraus-gauge geometry is first-order/channel-metrology prior art;
- Scutaru and later covariant-channel work establish covariant/energy-conserving Stinespring dilation;
- PSD-cone second-order tangent geometry is optimization prior art;
- classical boundary nonregularity is prior art.

Candidate distinct result: exact optimization when a **nonminimal positive target-kernel Hessian is independently prescribed**, including exact energy-conserving and infinite-dimensional realization, plus the autonomous spectral endpoint identity.

## Read first

1. `../../autonomous_temporal_information/notes/FOLLOWUP_DYNAMICAL_THEOREM_STACK.md`
2. `../../autonomous_temporal_information/notes/FOLLOWUP_DYNAMICAL_SIGNIFICANCE_PRIORITY_GATE.md`
3. `../../autonomous_temporal_information/notes/FOLLOWUP_DYNAMICAL_FINAL_PRIORITY_SEARCH_2026-08-23.md`
4. `../../autonomous_temporal_information/notes/WP33_HOSTILE_AUDIT_WP32_AND_PRIORITY_BOUNDARY.md`
5. `../../autonomous_temporal_information/notes/WP32_REPAIRED_INFINITE_DIMENSIONAL_ENERGY_CONSERVING_2JET_COST.md`
6. `../../autonomous_temporal_information/notes/WP23_EXACT_PRESCRIBED_2JET_DYNAMICAL_IMPLEMENTATION_COST.md`

## Working files

- `dynamical_rank_boundary_implementation_cost_draft.tex` — main theorem-first draft.
- `dynamical_rank_boundary_implementation_cost_supplement.tex` — supplement skeleton.
- `references.bib` — standalone bibliography.
- `MANUSCRIPT_HANDOFF.md` — durable manuscript state.

## Work order

1. fix notation and main theorem assumptions;
2. write the finite-dimensional coupling identity and exact prescribed-2-jet theorem first;
3. state the infinite-dimensional energy-conserving extension with only a proof core in the main text;
4. add the autonomous temporal specialization and fixed-energy no-work example;
5. move WP32 functional-analysis details to the supplement;
6. only then write the introduction/abstract in publication style;
7. run an independent hostile theorem-language audit before journal formatting.

## Manuscript integrity

The manuscript and supplement must be completely scientifically standalone. They must contain no personal repository URL, username, repository name, work-package labels, or requirement that the reader consult internal research files.