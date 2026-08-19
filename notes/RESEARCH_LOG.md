# Research Log

This file is append-only in spirit. Correct earlier entries by adding a later correction rather than silently erasing important failed reasoning.

---

## 2026-08-19 — Project initialization

### Question

Can there be a universal, material-independent physical bound on the rate at which a finite-temperature photodetector extracts information from an optical field, expressed in terms of thermodynamic, kinetic, optical, and quantum resources?

### Initial hypothesis

A detector may be represented in the stationary linear regime by

\[
Y(\omega)=\chi_{YP}(\omega)P(\omega)+N(\omega),
\]

with input-referred response-to-noise kernel

\[
K(\omega)=\frac{|\chi_{YP}(\omega)|^2}{S_Y(\omega)}
=\frac{1}{\mathrm{NEP}^2(\omega)}.
\]

For parameterized optical signals, Fisher-information rate is a candidate way to quantify useful sensitivity across bandwidth.

### Immediate caveat discovered

The raw Fisher-information-rate expression is not yet suitable for a universal theorem because it depends on the normalization/units of the optical parameter and can mix source resources with detector resources.

**Status:** VERIFIED conceptual issue.

### Consequence

The first task is not to guess a sensitivity-bandwidth-temperature product. It is to construct an invariant, normalized detector performance functional.

### Candidate resource set

Initial variables under consideration:

\[
T,\quad
\hbar\omega_{\rm opt},\quad
\Phi_\gamma,\quad
\dot\Sigma,\quad
\mathcal A,\quad
\eta_{\rm abs},\quad
N_{\rm ch},\quad
\text{bias/free-energy rate},\ldots
\]

No claim is made that this set is sufficient or minimal.

### First solvable model class

Finite-state continuous-time Markov jump photodetectors with local detailed balance, explicit optical transition bookkeeping, stationary dark state, causal response, finite entropy production, finite activity, and an explicit output current/counting record.

**Status:** DECISION.

### Literature warning from initial audit

The broad territory is already occupied by several important lines of work:

- Young, Sarovar, Léonard (2018): fully quantum photodetector frameworks and coherence/backaction performance tradeoffs;
- Hasegawa (2020/2021): quantum thermodynamic uncertainty relations for continuous measurement/general open systems;
- Schwarzhans et al. (2025): detector quality versus nonequilibrium thermodynamic resources;
- Liu and Gu (2026): response kinetic uncertainty relation for monitored Markovian open quantum systems;
- Blasi et al. (2026): quantum KURs/generalized activity at strong coupling;
- Vu, Honma, Saito (2026): general open-quantum-system precision limits.

**Status:** VERIFIED existence/relevance at abstract level. Full theorem-level comparison remains OPEN.

### Refined novelty hypothesis

The plausible gap is not “detectors have fundamental tradeoffs.” The target is instead:

> a photodetection-specific, architecture-independent bound on normalized optical information acquisition in detector-native response/noise variables with explicit optical and thermokinetic resource accounting, or a rigorous proof that no such finite bound exists for a proposed resource set.

**Status:** CONJECTURE / novelty hypothesis only.

### Key adversarial insight

Entropy production alone is not assumed to be sufficient. High-activity/low-affinity processes, detector replication, hidden resources, and source-resource leakage are immediate counterexample directions.

**Status:** OPEN until explicit models are calculated.

### Next mathematical action

Derive and independently verify exact expressions for:

1. \(\chi_{IP}(\omega)\) for an arbitrary finite-state Markov jump detector;
2. \(S_I(\omega)\) for an arbitrary counted transition current;
3. \(\dot\Sigma\) and \(\mathcal A\) in the same edge notation;
4. the complete two-state example as a unit test.

Then test whether existing response/KUR/TUR inequalities can bound \(K(\omega)\) or an invariant normalized integral of it.

**Status:** OPEN — immediate next work.
