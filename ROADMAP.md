# Research Roadmap

**Updated:** 2026-08-21

**Active scientific branch:** `agent/temporal-information-resource-law`

- Paper 1 Rev11: frozen.
- Paper 2 Rev7: frozen.
- Grand Challenge: active theorem stack through **WP17**.

# Current result hierarchy

## G8 — periodic random-time QFI budget — WP10/WP11

`G_Q(k)=2 sum_n q_nq_{n+k}/(q_n+q_{n+k})`,

`sum_{k>=1}G_Q(k)<=2nbar`.

This is a modewise SLD-QFI envelope with incompatible mode/quadrature optima.

## G11 — continuum QFI area — WP12/WP15

`int_R G_Q(nu)dnu<=pi Ebar^+/hbar`.

Flat-band QFI envelope:

`Ebar^+>=(2/pi)hBq0`.

WP16: the sharp `pi/4` operator constant is classical Hardy–Hilbert prior art.

## G13 — single-measurement operational budget — WP17

**PASSED for arbitrary fixed POVM and adaptive/separable independent-event readout.**

For the cosine/sine classical Fisher block `F_M^(k)` of one fixed POVM,

`boxed: sum_{k>=1}Tr F_M^(k)<=nbar`.

Continuum:

`boxed: int_R R_M(nu)dnu<=2Ebar^+/hbar`.

Full-quadrature flat-band guarantee:

`boxed: Ebar^+>=hBq0`.

The coefficient is sharp; the Cauchy/exponential covariant timestamp family saturates the continuum area law.

Interpretation: for single-copy/separable readout, the `pi/2` gap between WP15's QFI coefficient `pi` and WP17's operational coefficient `2` is an incompatibility gap.

# Remaining active gates

## G14 — collective mixed-state readout

**OPEN; highest-priority operational gate.**

WP17 does not cover entangled collective measurements across multiple independently twirled event excitations. Because the baseline twirled state is generally mixed, standard Gill–Massar separable tradeoffs do not by themselves exclude a collective advantage.

Work order:

1. solve the two-sector qubit model with the Holevo bound / quantum local asymptotic limit;
2. determine whether the per-event operational coefficient `2E/hbar` survives collective readout;
3. if it survives, seek a general proof for the full energy-sector model;
4. if it fails, quantify the collective advantage and revise the resource hierarchy.

## Priority audit

Continue searching random-unitary/group-distribution estimation for exact equivalents of WP10 and WP17. Generic random-unitary probability estimation, U(1) mode decomposition, QFI, and multiparameter complementarity are already occupied.

## Source embedding

Strengthen the independent quantum-marked Poisson model into realistic incoherent bosonic optical-field language.

# Manuscript gate

Do **not** draft the foundational manuscript yet.

Required:

1. collective-measurement gate resolved or sharply bounded;
2. exact priority audit survives;
3. source-to-field mapping hardened;
4. Hardy–Hilbert and other standard ingredients properly attributed;
5. WP14 arbitrary-waveform no-go retained as a scope boundary.

# Candidate manuscript spine if gates survive

- random-time distribution encoding;
- exact discrete mode QFI and `2nbar` envelope;
- fixed-measurement operational `nbar` theorem;
- continuum operational `2E/hbar` law and sharp equality family;
- separately optimized QFI `pi E/hbar` envelope and incompatibility interpretation;
- collective-measurement boundary;
- Poisson/photodetection embedding;
- coherent-waveform no-go.

# Documentation discipline

Every material result must update the WP note, active handoff, landing files, and `main`.