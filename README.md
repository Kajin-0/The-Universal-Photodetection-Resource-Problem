# The Universal Photodetection Resource Problem

**Current status: 2026-08-21**

`main` is the repository landing/index branch. Detailed active derivations live on `agent/temporal-information-resource-law`.

The project consists of two frozen papers plus one active high-risk theoretical program.

## Current branches and deliverables

### Paper 1 — Rev11 frozen

Autonomous low-overlap marked-event photodetection resource theorem. Scientifically frozen and technically validated; remaining work is factual/personal submission metadata and compliance statements.

Primary science branch: `agent/uprp-core-theorem-round10`.

### Paper 2 — Rev7 frozen

**Fisher Spectra and Information Singularities in Photodetectors with Memory**.

Paper 2 extends temporal Fisher analysis to arbitrary parameter-independent autonomous detector channels with memory and develops the deterministic/random Type-II information-singularity results. Rev7 is the preferred frozen science draft and has been locally build-verified and visually inspected.

Primary science branch: `agent/uprp-core-theorem-round10`.

### Grand Challenge — ACTIVE

The current scientific frontier is on:

`agent/temporal-information-resource-law`

The authoritative handoff there is:

`grand_challenge/AGENTS.md`

The active question is:

> **For a physically realizable measurement of temporal structure, what fundamental quantum resources constrain source-to-record temporal Fisher-information transfer?**

The **theorem stack is through WP15**. The **latest research checkpoint is WP16**, a deep priority audit.

## Strongest current grand-challenge result

For a normalized positive excitation-frequency density `q(omega)` with finite first moment `omega_bar`, define the random-time Fourier-mode quantum retention

`G_Q(nu)=2 int_0^infinity q(omega)q(omega+nu)/[q(omega)+q(omega+nu)]domega`, `nu>0`,

with even extension.

WP15 proves for every finite-first-moment density:

`boxed: int_0^infinity G_Q(nu)dnu <= (pi/2) omega_bar`,

or equivalently

`boxed: int_R G_Q(nu)dnu <= pi E_bar^+/hbar`.

For a guaranteed flat temporal-information band,

`G_Q(2*pi*f)>=q0` for every `|f|<=B`,

this implies

`boxed: E_bar^+ >= (2/pi) h B q0`.

The constant is sharp as a supremum.

## WP16 priority correction

WP16 establishes that the sharp WP15 operator norm

`||T||=pi/4`, for `L(s,t)=2st/(s+t)^3`,

is an explicit specialization of classical parameterized Hardy–Hilbert integral inequalities. With `lambda=3`, `f(x)=xr(x)`, `g(y)=yr(y)`, the classical best constant is `B(3/2,3/2)=pi/8`; the factor `2` in the WP15 kernel produces `pi/4`.

Therefore **do not claim mathematical novelty for the `pi/4` operator norm, Mellin/Hilbert inequality, or Beta/Gamma sharp constant**.

The remaining priority question is quantum-statistical: targeted searches have not yet found an exact predecessor for estimating a Fourier coefficient of a latent random `U(1)` translation distribution with

`G_Q(k)=2 sum_n q_n q_{n+k}/(q_n+q_{n+k})`

or the summed law

`sum_{k>=1}G_Q(k)<=2 nbar`.

**Quantum priority is not certified.**

## Important scope boundary

The strongest theorem applies to **random temporal-distribution encoding of a fixed semibounded-energy excitation**. It is not currently a theorem for arbitrary parameter-dependent quantum waveform synthesis.

WP14 gives an explicit coherent-field no-go showing that baseline mean energy alone cannot bound arbitrary high-frequency waveform tangents; a broader theorem would need an encoding/control/action resource.

## Current gates

Before a new foundational manuscript is drafted:

1. search specifically for estimation of Fourier coefficients/mixing weights of `U(1)` random-unitary channels and probability measures on compact groups;
2. determine whether the harmonic-mean density inequality itself appears explicitly in classical analysis; its sharp operator constant is already classical;
3. determine operational attainability of the integrated `pi` coefficient by one measurement family;
4. strengthen the independent quantum-marked Poisson/event-to-field embedding;
5. preserve the WP14 source-encoding boundary and claim discipline.

## Where to read the live state

Switch to branch:

`agent/temporal-information-resource-law`

Then read:

1. `grand_challenge/AGENTS.md`
2. `grand_challenge/notes/WP16_DEEP_PRIORITY_AUDIT_RANDOM_TIME_QFI_AND_HARDY_HILBERT_COLLISION.md`
3. `grand_challenge/notes/WP15_GENERAL_DENSITY_PROOF_OF_SHARP_PI_AREA_INEQUALITY.md`
4. `docs/CURRENT_RESEARCH_STATE.md`
5. `ROADMAP.md`

## Documentation policy

The default `main` branch is the repository landing/index branch and must always advertise the current active branch and checkpoint. Detailed in-progress derivations may remain on agent branches, but the project-level state must never again be hidden from the default repository view.