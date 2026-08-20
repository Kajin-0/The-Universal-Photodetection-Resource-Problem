# Novelty Audit — Round 2: Finite-Band Optical Information

**Date:** 2026-08-19

## Purpose

This audit addresses the closest literature to WP5, where UPRP attempts to connect electromagnetic sum rules and finite optical bandwidth to optical-to-electrical information transfer.

The main conclusion is that the novelty window is narrower than initially expected but remains nonempty.

---

# 1. Amaolo et al. (2026): maximum Shannon capacity of photonic structures

Alessio Amaolo et al., **Maximum Shannon capacity of photonic structures**, *npj Nanophotonics* 3, 14 (2026), DOI `10.1038/s44310-025-00104-2`.

## What it already does

The paper:

- maps communication source/receiver degrees of freedom to electromagnetic currents and Green functions;
- optimizes Shannon mutual-information capacity over current allocations and arbitrarily structured photonic environments;
- uses Maxwell constraints and photonic optimization to bound achievable channel singular values / capacity;
- explicitly connects information theory and full-wave electromagnetic structural limits.

Therefore the following claim is **occupied**:

> “We are the first to combine information theory with fundamental electromagnetic limits of structured photonic systems.”

UPRP must not make that claim.

## Explicit opening left by the paper

The authors state that their current results are derived at a **single frequency** and identify extension to finite bandwidths using spectral sum rules or delay-bandwidth products as future work. They also identify macroscopic-QED extensions as future work and note that more sophisticated thermal/shot-noise models could be incorporated.

This is exceptionally relevant to UPRP because our main task is temporal photodetection over a finite modulation/sideband band.

## Distinction from UPRP

Amaolo et al. optimize a communication channel whose receiver observable is an electromagnetic field/current representation with a prescribed noise model. UPRP instead asks about a physical photodetector transducer:

\[
\text{incident optical field}
\to
\text{absorbed/internal excitation}
\to
\text{nonequilibrium detector dynamics}
\to
\text{electrical record},
\]

where detector-generated thermal, shot, dark, and kinetic noise are part of the physics and where information is quantified relative to the incident optical QFI.

The current surviving distinction is therefore:

1. finite temporal/sideband bandwidth;
2. actual optical capture/absorption;
3. endogenous finite-temperature transduction noise;
4. explicit thermodynamic/kinetic resource accounting;
5. eventually quantum rather than classical Shannon-only information.

**Novelty risk:** VERY HIGH, but not fatal.

---

# 2. Zhang, Monticone, Miller (2023): matrix-valued oscillator representation

Lang Zhang, Francesco Monticone, Owen D. Miller, **All electromagnetic scattering bodies are matrix-valued oscillators**, *Nature Communications* 14, 7724 (2023), DOI `10.1038/s41467-023-43221-2`.

## What it already does

For any passive linear scattering body, the paper derives a T-operator oscillator representation constrained by passivity and both high- and low-frequency sum rules. In schematic form,

\[
\mathbb T(\omega)
=\int_0^\infty
\frac{\mathbb X(\omega_i)+(\omega_i/\omega)\mathbb Y(\omega_i)}
{\omega_i^2-\omega^2-i0^+\omega}
d\omega_i,
\]

with

\[
\mathbb X(\omega_i)\succeq0,
\qquad
-\mathbb X\preceq\mathbb Y\preceq\mathbb X,
\]

and total-strength constraints including

\[
\int_0^\infty\mathbb X(\omega_i)d\omega_i
\preceq\omega_p^2\mathbb I_D,
\]

\[
\int_0^\infty\frac{\mathbb X(\omega_i)}{\omega_i^2}d\omega_i
\preceq\mathbb T_{0,D}.
\]

This is substantially more rigorous and general than assuming an ad hoc scalar extinction sum rule for an arbitrary photonic body.

## Consequence for UPRP

UPRP should treat this T-operator representation as the primary arbitrary-scatterer electromagnetic resource framework.

The potentially distinct step is not deriving another scattering sum rule, but projecting the existing operator constraints onto:

\[
\text{normalized incident optical information mode}
\to
\text{absorptive/capture subspace}
\]

and then composing that capture-information ceiling with the internal photodetector thermokinetic theorem.

**Novelty risk:** HIGH for any generic broadband scattering-bound claim; LOWER for the detector-QFI composition.

---

# 3. Shim et al. (2019): arbitrary-bandwidth LDOS power-bandwidth limits

Hyungki Shim, Lingling Fan, Steven G. Johnson, Owen D. Miller, **Fundamental Limits to Near-Field Optical Response over Any Bandwidth**, *Phys. Rev. X* 9, 011043 (2019), DOI `10.1103/PhysRevX.9.011043`.

## What it already does

The paper derives arbitrary-bandwidth upper bounds for near-field optical response, including LDOS, from causality and energy conservation, with explicit material and geometric figures of merit.

This means the following claim is occupied:

> “Finite optical bandwidth prevents arbitrarily large near-field light–matter enhancement.”

## UPRP distinction

LDOS is emitter-centered. A photodetector is incident-channel driven. UPRP should use LDOS only where reciprocity/localized-gateway assumptions justify it, and should prefer an incident-channel capture operator when seeking an architecture-independent frontend theorem.

**Novelty risk:** HIGH for LDOS/power-bandwidth claims; LOW as a supporting resource theorem.

---

# 4. Mishchenko (2008): warning about blanket extinction sum rules

Michael I. Mishchenko, **Broadband electromagnetic scattering by particles**, *JOSA A* 25, 2893 (2008), DOI `10.1364/JOSAA.25.002893`.

The paper argues that commonly stated extinction-cross-section sum rules were not, in that context, rigorously derived directly from macroscopic Maxwell scattering and should not be accepted merely from heuristic causality arguments.

## Consequence for UPRP

Do not write

\[
\int\sigma_{\rm ext}(\omega)d\omega=C N_e
\]

as an unrestricted theorem for arbitrary structured photodetectors unless it is explicitly derived from a rigorous modern scattering operator framework with clearly stated normalization and assumptions.

The microscopic electric-dipole/TRK absorption formula remains useful in its proper regime, but the arbitrary-device theorem should use the T-operator constraints of Zhang et al. or another equally rigorous first-principles route.

**Status:** important rigor constraint.

---

# 5. What is now clearly not novel

Do not claim novelty for any of the following:

- information theory applied to electromagnetic/photonic channels;
- Maxwell-constrained Shannon capacity at a single frequency;
- optical spectral sum rules;
- T-operator oscillator-strength constraints;
- finite-band LDOS/power-bandwidth limits;
- general QFI data processing;
- detector thermodynamic precision/jitter tradeoffs;
- generic finite-frequency fluctuation-response inequalities.

---

# 6. Surviving candidate novelty

The strongest defensible candidate is:

> **A finite-band, photodetection-specific no-go/completion theory for transfer of quantum Fisher information from an incident optical field to a finite-temperature electrical detector record, showing that stationary thermodynamic resources do not fix an absolute speed scale, identifying microscopic light–matter coupling as a necessary resource, bounding incident-channel capture using rigorous electromagnetic spectral constraints, and composing that frontend bound with internal detector thermokinetic constraints.**

The pieces individually overlap existing literature. The possible novelty is the **specific composition and no-go structure**.

---

# 7. Publication-level novelty test still required

Before claiming a paper-ready result, search specifically for combinations of:

- photodetector + quantum Fisher information + oscillator-strength sum rule;
- photodetection + finite-band electromagnetic bounds;
- detector DQE + spectral sum rules;
- absorption-channel QFI + passivity/causality bounds;
- Maxwell-constrained finite-band Shannon/Fisher information;
- light–matter coupling resource + photodetector timing bandwidth;
- temporal sideband information + absorption sum rules.

The 2026 Amaolo paper makes this audit mandatory because it is conceptually adjacent and explicitly points to finite-band sum-rule information bounds as a future direction.

---

# 8. Current confidence assessment

- **WP4 Markov missing-coupling no-go:** strong and mathematically explicit.
- **WP3 restricted gateway completion:** strong under its assumptions.
- **WP5 coherent incident-channel QFI capture lemma:** strong under passive-linear assumptions.
- **All-frequency microscopic TRK capture corollary:** mathematically useful but very loose and narrow in scope.
- **Arbitrary-scatterer finite-band capture-QFI theorem:** OPEN.
- **Full quantum detector completion:** OPEN.
- **Final novelty claim:** PROVISIONAL until the targeted combination search above is closed.
