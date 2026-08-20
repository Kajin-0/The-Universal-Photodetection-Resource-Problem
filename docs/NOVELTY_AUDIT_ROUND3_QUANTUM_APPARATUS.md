# Novelty Audit — Round 3: quantum apparatus thermodynamic/metrological resources

**Date:** 2026-08-20

## Purpose

WP7–WP9 connect photodetection information transfer to passive bosonic coupling, detector-pointer displacement QFI, excitation/free-energy preparation resources, and finite-band electromagnetic capture. This territory overlaps established continuous-variable resource theories and nonclassical quantum metrology. This note records the strongest overlap found so far and narrows the defensible novelty claim.

---

## 1. Narasimhachar et al. (2021): thermodynamic resources in CV systems

Varun Narasimhachar et al., **Thermodynamic resources in continuous-variable quantum systems**, npj Quantum Information 7, 9 (2021), DOI `10.1038/s41534-020-00342-6`.

They introduce **bosonic linear thermal operations (BLTO)**:

- free thermal ancillas at a fixed ambient temperature;
- passive linear energy-conserving interactions between equal-frequency modes;
- discarding modes.

This is very close to the passive-linear apparatus model used in the WP7/WP8 coherent-state branch.

Their paper explicitly identifies:

- generalized thermodynamic temperatures;
- phase-space displacement signal-to-noise ratios as resource monotones;
- Fisher-information-based measures of displacement-sensing usefulness as nonclassical/thermodynamic resources;
- relative entropy to the thermal state as a generalized nonequilibrium Helmholtz free-energy monotone.

They emphasize that such quantities are thermodynamic currencies under BLTO and discuss sensing/metrology as a natural application.

### Novelty consequence

The following statement is **not novel**:

> detector-pointer displacement sensitivity/nonclassicality can be regarded as a thermodynamic resource under passive linear thermal operations.

Nor is it novel merely to combine the words `free energy`, `squeezing`, and `displacement sensing`.

What the 2021 paper does **not appear to provide** is the exact constrained frontier studied here,

\[
\sup_{\rho:\,D(\rho\Vert\tau)\le D_0}J_X^{\rm SLD}(\rho),
\]

its non-Gaussian parity structure, the coupling-action tradeoff, or its photodetection finite-band composition. Those remain candidate distinct contributions, pending deeper citation chaining.

---

## 2. Yadin et al. (2018): operational CV nonclassicality

Benjamin Yadin et al., **Operational Resource Theory of Continuous-Variable Nonclassicality**, Phys. Rev. X 8, 041038 (2018), DOI `10.1103/PhysRevX.8.041038`.

They construct an operational resource theory for nonclassicality under passive linear networks and measurement/feed-forward and define nonclassicality measures based on:

- quadrature fluctuations; and
- quantum Fisher information for quadrature displacements.

Their results apply to generic multimode non-Gaussian states and include no-go/concentration constraints.

### Novelty consequence

The following is already occupied:

- quadrature-displacement QFI as a continuous-variable nonclassicality measure;
- passive-linear monotonicity/concentration limits of such a resource;
- the generic observation that non-Gaussian states can carry displacement-metrology resources.

UPRP must distinguish **transferring incident optical information into a detector/electrical record under explicit coupling and finite-band constraints** from merely quantifying the metrological power of a state.

---

## 3. Kwon et al. (2019): metrological power

Hyukjoon Kwon et al., **Nonclassicality as a Quantifiable Resource for Quantum Metrology**, Phys. Rev. Lett. 122, 040503 (2019), DOI `10.1103/PhysRevLett.122.040503`.

They define a metrological-power measure from multimode quadrature QFI with a direct operational meaning for displacement sensitivity beyond the classical limit. They show it is a nonclassicality monotone under linear optical elements.

### Novelty consequence

Do not claim:

- first use of quadrature QFI to quantify a pointer's displacement-sensing resource;
- first proof that passive linear optics cannot create/increase generic displacement-metrological nonclassicality;
- first link between nonclassicality and displacement QFI.

---

## 4. Quantum Stam / entropy-power literature

König–Smith and subsequent bosonic entropy-power work derive beam-splitter Stam inequalities for a **relative-entropy/divergence-derived quantum Fisher information** used in quantum de Bruijn identities.

The algebraic structure

\[
J_C^{-1}\ge\lambda J_A^{-1}+(1-\lambda)J_B^{-1}
\]

is therefore not new in generic form.

WP8's directional SLD/Bures derivation uses SLD QFI directly via:

1. displacement covariance of a beam splitter;
2. SLD-QFI data processing;
3. product additivity;
4. scalar optimization over input displacement weights.

A targeted search has not yet identified this exact **directional SLD** statement as a named theorem, but absence from search is not a novelty proof.

### Required claim discipline

Even if the directional SLD proof itself is unpublished, it is mathematically close to the established Stam construction. Treat it primarily as enabling machinery unless a theorem-level literature audit shows otherwise.

---

## 5. Other close literature

### Grochowski & Filip (2025)

**Optimal Phase-Insensitive Force Sensing with Non-Gaussian States**, Phys. Rev. Lett. 135, 230802 (2025).

Sparse / `N`-spaced Fock-support states are already known to approach displacement/force-sensing bounds. Therefore parity/sparse support is not generically novel.

### Marvian (2022)

PRL 129, 190502 (2022) gives an operational thermodynamic interpretation of QFI as a coherence-preparation cost for time-translation asymmetry.

This is conceptually close to “QFI is a thermodynamic resource” but uses a different symmetry/generator structure. It must be mapped carefully against phase-space displacement QFI.

---

## 6. Surviving candidate contribution after this audit

The defensible novelty target is narrower than previous wording.

Candidate contribution:

> **A photodetection-specific resource-completeness theorem: stationary thermodynamic costs and optical detailed balance do not determine detector speed; absolute microscopic coupling and pre-existing detector metrological resources are separately necessary. For passive coherent photodetection, explicit coupling-action, finite-temperature preparation, and finite-band electromagnetic constraints can then be composed into quantitative optical-to-electrical information-transfer ceilings.**

Within that larger result, potentially distinct mathematical pieces include:

1. the explicit Markov fixed-detailed-balance rare-fast no-go family;
2. the exact photodetection coupling-action/apparatus-energy tradeoff;
3. the relative-entropy/free-energy constrained **SLD displacement-QFI frontier problem**;
4. the analytic Gaussian-optimality counterexample using parity-conditioned thermal states;
5. exact parity-sector free-energy frontiers and the Gaussian-to-non-Gaussian crossover;
6. the finite-band composition of T-operator electromagnetic capture with apparatus QFI and coupling action.

Each item still requires theorem-level citation chaining before a paper claims originality.

---

## 7. Strongly prohibited novelty claims

Do **not** write any of the following in a manuscript without major qualification:

- “We first show that squeezing/nonclassicality is a thermodynamic resource.”
- “We first connect free energy to displacement sensing.”
- “We introduce QFI as a measure of CV nonclassicality.”
- “We derive the first quantum Stam inequality for a beam splitter.”
- “We first show passive linear optics cannot increase displacement metrological power.”
- “Parity or sparse Fock states are newly discovered as good displacement probes.”

---

## 8. Next audit targets

1. Citation-chain Narasimhachar et al. (2021), especially papers citing their sensing/metrology discussion.
2. Inspect Yadin et al. (2018) and Kwon et al. (2019) supplements for exact inequalities that may subsume the WP8 energy theorem.
3. Search specifically for relative-entropy-to-thermal-state constrained maximization of quadrature SLD QFI.
4. Search for directional SLD/Bures Stam inequalities under bosonic convolution.
5. Search resource-theory literature for free-energy cost of creating metrological power under Gaussian/thermal operations.
6. Compare WP9 spectral-allocation curvature transition against classical/quantum water-filling and optical communications literature.
