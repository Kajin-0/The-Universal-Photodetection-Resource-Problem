# Research Roadmap

**Updated:** 2026-08-22

**Active scientific branch:** `agent/temporal-information-resource-law`

Paper 1 Rev11 and Paper 2 Rev7 are frozen. Grand Challenge checkpoint: **WP24**.

# Established hierarchy

## G1 — operational discrete survival law — WP20/WP24

For sector probabilities `q_n` and harmonic `k`,

`T_k=sum_(m>=k)q_m`.

For any finite number `N` of independently encoded excitations and any joint POVM,

`boxed: Tr F_N^(k)<=N T_k`.

A tighter support-sensitive form is

`boxed: Tr F_N^(k)/N<=min(D_k,U_k)<=T_k`.

Summing,

`boxed: sum_(k>=1)R_N(k)<=nbar`.

This closes the arbitrary-collective measurement gate by a direct finite-copy proof.

## G2 — continuum operational survival law — WP22

For a positive excitation-frequency spectral probability measure `mu` with finite mean,

`boxed: R(nu)<=mu([nu,infinity))`.

Therefore

`boxed: int_R R(nu)dnu<=2Ebar^+/hbar`,

and

`boxed: Ebar^+>=hbar nu R(nu)=h f R(2pi f)`.

The lower-bin periodic approximation makes the theorem rigorous without smoothness assumptions.

## G3 — exact sharpness

Geometric sector populations with the canonical phase POVM saturate every discrete harmonic simultaneously:

`R(k)=T_k=r^k`.

The continuum exponential spectrum / Cauchy timestamp family saturates

`R(nu)=P(Omega>=|nu|)`

and the area coefficient.

## G4 — independent Poisson source to physical field — WP23

For an independent quantum-marked compound-Poisson source followed by any parameter-independent source-to-bosonic-field and detector channel,

`boxed: R_final(k)<=T_k`

and the continuum survival law is inherited unchanged.

The proof uses event-number side information plus Heisenberg pullback of the final POVM through the CPTP source/detector map.

## G5 — separately optimized QFI envelope — WP10/WP12/WP15

Still correct but secondary:

`sum_(k>=1)G_Q(k)<=2nbar`,

`int_R G_Q(nu)dnu<=pi Ebar^+/hbar`.

The `pi` coefficient is a modewise SLD-QFI envelope, not the jointly attainable operational law. WP16 identifies the sharp `pi/4` analytic operator norm as classical Hardy--Hilbert mathematics.

## G6 — arbitrary coherent waveform synthesis — WP14

**NO-GO.** Baseline mean energy alone does not constrain arbitrary state-valued coherent waveform engineering. A broader theorem needs explicit encoding/control/action resource accounting.

# Prior-art status — WP21/WP24

The following are occupied:

- `U(1)` modes of asymmetry / energy-gap decomposition;
- weighted phase/time twirling multiplying gap modes by mixing-distribution Fourier coefficients;
- canonical phase POVMs/Fourier moments;
- photon-number/energy-constrained phase estimation;
- arbitrary collective Fisher/Holevo/RLD/SLD bounds;
- random-unitary probability estimation;
- QFI/asymmetry resource theory;
- Hardy--Hilbert/Mellin mathematics;
- compound Poisson and CPTP/Stinespring machinery.

Marvian--Spekkens, Phys. Rev. A 90, 062110 (2014), is especially close to the kinematic encoding map.

Targeted searches have not found the exact operational Fisher tail theorem

`Tr F_N^(k)/N<=sum_(m>=k)q_m`,

its mean-generator harmonic sum, or continuum survival form.

**Priority remains unverified, not certified.**

# Publication gate

WP24 integrated hostile review: **PASS**.

The prior three blockers are resolved within the stated source class:

1. collective/joint measurement — WP20;
2. continuum rigor — WP22;
3. independent event-to-bosonic-field mapping — WP23.

The project has reached a reasonable manuscript-formation threshold. Exact priority cannot be certified by finite search, so the correct strategy is conservative positioning plus continued historical auditing during drafting.

# Immediate work order

1. Finish synchronization of active landing documents and `main` through WP24.
2. Create a standalone manuscript architecture with the operational survival law as Theorem 1.
3. Draft a compact prior-work map explicitly crediting Marvian--Spekkens, phase-estimation/number constraints, arbitrary-measurement Fisher bounds, and random-unitary estimation.
4. Build the manuscript around:
   - random-time mixing-distribution problem;
   - direct finite-copy tail theorem;
   - all-mode mean-energy sum rule;
   - continuum survival/area/pointwise Planck laws;
   - exact geometric/exponential equality family;
   - independent Poisson-to-bosonic-field embedding;
   - secondary SLD-QFI envelope and incompatibility gap;
   - WP14 arbitrary-waveform no-go.
5. Perform a new hostile review of the assembled manuscript before any journal/package work.

# Documentation discipline

Every material theorem, no-go, proof repair, priority collision, or manuscript-strategy change must update the detailed WP notes, handoff/landing files, and `main`.