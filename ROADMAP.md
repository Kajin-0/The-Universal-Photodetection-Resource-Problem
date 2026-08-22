# Research Roadmap

**Updated:** 2026-08-21

**Active scientific branch:** `agent/temporal-information-resource-law`

## Program split

- **Paper 1 / Rev11:** frozen; submission metadata/compliance only.
- **Paper 2 / Rev7:** frozen science draft; no open theorem-development gate.
- **Grand Challenge:** active program seeking fundamental quantum resource laws for temporal information transfer.

The current frontier is `grand_challenge/`, not the older Paper-2 work packages.

# Grand Challenge objective

Determine whether physically realizable temporal measurement obeys sharp, architecture-independent information-transfer resource laws, while explicitly classifying which broader formulations fail.

The program is falsification-first. A theorem is promoted only after counterexample and priority audits.

# Closed/redirected directions

## G0 — entropy-production-only resource law

**REJECTED as universal.** Existing sensory-network and quantum-clock results show entropy production alone does not universally control temporal information/precision.

## G1 — generic frequency-domain FI/response thermodynamic law

**LITERATURE-COVERED / TOO BROAD.** Frequency-domain response uncertainty and dynamical-activity relations already exist.

## G2 — generic quantum waveform Fisher spectrum

**LITERATURE-COVERED.** Continuous-time waveform QFI kernels/spectral QCRBs are established.

## G3 — detector thermodynamic cost determined by `G`

**REJECTED.** The same logical information-transfer spectrum can be embedded in physically different Hamiltonian/work-cost implementations; `G` alone is thermodynamically incomplete.

## G4 — baseline mean energy bounds arbitrary waveform state engineering

**REJECTED by WP14.** Infinitesimal high-frequency coherent sidebands can be generated at first order while added energy enters at second order. A broader waveform theorem requires an encoding/control/action resource.

# Active theorem chain

## G5 — covariant timestamp positive-energy law — WP06/WP07

**PASSED for covariant timestamp class.**

`int_R G_timestamp(nu)dnu <= 2 E_det^+/hbar`.

Flat-band inverse form:

`E_det^+ >= h B q`.

The energy is measured above the lower spectral edge participating in the detected state, making the statement invariant to arbitrary Hamiltonian energy offsets.

## G6 — arbitrary downstream detector memory — WP08

**PASSED for downstream parameter-independent classical processing.**

The covariant timestamp bound is inherited by arbitrary later detector memory/coarse graining through FI data processing. Finite quantum timing energy therefore regularizes the ideal classical Type-II infinite-frequency plateau.

## G7 — external time-reference boundary — WP09

**PASSED as a no-go/boundary result.**

Mean energy does not bound deterministic global time-shift QFI if an external phase/time reference and sparse high-energy coherence are allowed. Random-event-time encoding removes this free absolute-phase resource and motivates the next theorem class.

## G8 — discrete random-time quantum mode budget — WP10/WP11

**PASSED analytically; priority audit open.**

For periodic temporal Fourier mode `k`:

`G_Q(k)=2 sum_n q_n q_{n+k}/(q_n+q_{n+k})`.

Resource sums:

`sum_{k>=1}G_Q(k)<=2 nbar`,

`sum_{k!=0}G_Q(k)<=4 nbar`.

Constants are sharp as suprema. Mixed-state and arbitrary downstream detector/measurement extensions follow by purification and QFI monotonicity.

## G9 — continuum random-time mode law — WP12

**PASSED for regular densities; generalized by WP15.**

For `nu>0`:

`G_Q(nu)=2 int_0^infinity q(omega)q(omega+nu)/[q(omega)+q(omega+nu)]domega`.

The conjectured/derived integrated resource coefficient is `pi` in two-sided angular-frequency area.

## G10 — second-quantized/Poisson embedding — WP13

**PASSED at current theorem scope; further physical mapping open.**

Total-energy sectors include fixed-photon-number multiphoton/entangled/multimode pulses. Independent quantum-marked Poisson events inherit the source-normalized bound by additivity; downstream parameter-independent field mappings and detector memory cannot increase QFI.

## G11 — general-density sharp `pi` area theorem — WP15

**PASSED analytically; current strongest result.**

For every normalized `q(omega)>=0` with finite first moment `omega_bar`:

`boxed: int_0^infinity G_Q(nu)dnu <= (pi/2) omega_bar`,

hence

`boxed: int_R G_Q(nu)dnu <= pi E_bar^+/hbar`.

Flat-band inverse law:

`boxed: E_bar^+ >= (2/pi) h B q0`.

WP15 removes smoothness assumptions using rearrangement, layer cake, and an exact positive Mellin-convolution operator of norm `pi/4`. The constant is sharp as a supremum, approached by truncated critical densities proportional to `(1+omega)^(-2)`.

# Current publication gate

Do **not** draft the grand-challenge paper yet.

A manuscript decision requires all of:

1. **Priority survival:** no exact prior theorem/formula equivalent to WP10/WP12/WP15.
2. **Operational interpretation:** clarify whether a single measurement can approach the integrated `pi` coefficient, since different temporal-mode SLDs are generally incompatible.
3. **Physical source mapping:** strengthen the independent quantum-marked Poisson/event model into realistic incoherent optical-field language without adding hidden resources.
4. **Claim discipline:** retain the WP14 boundary; do not state the theorem for arbitrary state-valued waveform encoding.

If these gates survive, the likely manuscript spine is:

- random-time encoding problem and why ordinary time-shift/QFI intuition is insufficient;
- exact discrete mode-retention formula and `2 nbar` sum rule;
- sharp continuum `pi E/hbar` area law;
- Planck-scale inverse bandwidth/resource inequality;
- second-quantized/Poisson photodetection embedding;
- covariant timestamp subclass and comparison with Paper 2's classical memory plateau;
- explicit no-go for arbitrary coherent waveform encoding.

# Immediate work order

1. Deep priority audit in random-unitary/group-distribution estimation, phase-noise estimation, Rényi/time-observable inequalities, and harmonic-analysis literature.
2. Analyze joint-measurement/attainability of the integrated QFI-area coefficient.
3. Harden source-to-field embedding for realistic incoherent optical events.
4. Only then make a manuscript decision.

# Documentation discipline

Every material theorem, proof repair, no-go, prior-art collision, numerical result, or gate change must update:

- `grand_challenge/notes/WP*.md`;
- `grand_challenge/AGENTS.md`;
- top-level `README.md`, `AGENTS.md`, `docs/CURRENT_RESEARCH_STATE.md`, and this roadmap when project-level state changes;
- the default `main` landing documents so the active branch/checkpoint is visible without branch hunting.