# The Universal Photodetection Resource Problem

**Current status: 2026-08-22**

`main` is the landing/index branch. Detailed Grand Challenge derivations and manuscript generation live on `agent/temporal-information-resource-law`.

## Project split

1. **Paper 1 / Rev11** — frozen and technically validated.
2. **Paper 2 / Rev7** — frozen preferred science draft.
3. **Grand Challenge** — science checkpoint **WP24**; preferred PRX Quantum manuscript **Rev7**.

Authoritative handoff: active-branch `grand_challenge/AGENTS.md`.

# Grand Challenge result

For exact periodic random-time encoding with sector populations `q_n`, any finite-copy joint measurement obeys

`Tr F_N^(k)/N <= min(D_k,U_k) <= T_k`,

where `T_k=sum_(m>=k)q_m`.

Thus

`sum_(k>=1) R_N(k) <= nbar`.

The result includes arbitrary entangled collective measurements.

## Controlled periodic-to-continuum law

For controlled periodic-to-continuum limits,

`R(nu) <= Pr(Omega>=nu)`.

This survival law is the principal continuum result. `Omega` is excess generator frequency above the participating lower edge, and

`Ebar+=hbar<Omega>`

is mean excess energy, not a common carrier offset.

The area and `hfR` relations are first-moment corollaries:

`int_R R <= 2Ebar+/hbar`,

`Ebar+ >= hbar nu R(nu) = h f R(2pi f)`.

## Sharpness and physical relevance

The geometric/canonical-phase family saturates every discrete harmonic simultaneously and gives the exponential-spectrum/Cauchy-time equality family in the controlled continuum limit.

Rev7 additionally analyzes a transform-limited truncated-Gaussian single photon. Canonical covariant timing reaches about **96.6%** of the survival ceiling at half a Gaussian width and **88.5%** at one width.

## Scope

WP23 carries the normalized bound through arbitrary **parameter-independent** source-to-bosonic-field and detector processing for an independent quantum-marked Poisson event source.

WP14/Rev7 retain the coherent-sideband no-go: baseline mean energy cannot constrain arbitrary parameter-dependent waveform-state synthesis.

# Prior-art boundary

`U(1)` modes of asymmetry and weighted twirling already identify available energy-gap components. The candidate contribution is operational instead:

> a sharp bound on the **classical Fisher information extractable by any actual POVM** about a perturbation of the random-time mixing law, expressed through participating population tails and valid for arbitrary finite-copy collective measurements.

Canonical phase POVMs, energy-constrained phase estimation, generic QFI/Holevo machinery, random-unitary estimation, waveform QFI, Hardy--Hilbert/positive-frequency mathematics, and generic Poisson/CPTP processing are prior art.

**Priority remains unverified, not certified.**

# Preferred manuscript — Rev7

Working title: **A Sharp Energy-Survival Law for Temporal Fisher Information**.

Rev7 follows an external adversarial review and directly repairs the strongest remaining PRX Quantum positioning risks:

- continuum result labeled explicitly controlled periodic-to-continuum;
- resource defined as excess energy above the participating edge;
- survival law made primary and `hfR` demoted to a first-moment corollary;
- distinction from modes-of-asymmetry theory sharpened;
- one nonextremal transform-limited single-photon example added;
- Figure 1 revised accordingly.

Final local preflight:

- full LaTeX/BibTeX build: **PASS**;
- **8 pages**;
- unresolved references/citations: **0**;
- overfull boxes: **0**;
- all 8 pages rendered at 200 dpi and visually inspected: **PASS**;
- local PDF SHA-256: `d168c3901faa6f29bda0eba71abe8049cc9819d91843273beeeeffb9443818ae`.

# Journal target

**First target:** PRX Quantum — Research Article.

**Fallback:** Physical Review A — Regular Article.

# Recovery

Switch to `agent/temporal-information-resource-law` and read:

1. `grand_challenge/AGENTS.md`
2. `grand_challenge/notes/MANUSCRIPT_REV7_REFEREE_HARDENING_2026-08-22.md`
3. `docs/CURRENT_RESEARCH_STATE.md`
4. `ROADMAP.md`

# Workflow rule

Do not reintroduce “human verification” as a research/manuscript completion gate. The finished package is produced as far as possible and handed to a human for submission. Unknown administrative facts remain placeholders rather than being invented.

`main` must always advertise the active branch and current frontier.
