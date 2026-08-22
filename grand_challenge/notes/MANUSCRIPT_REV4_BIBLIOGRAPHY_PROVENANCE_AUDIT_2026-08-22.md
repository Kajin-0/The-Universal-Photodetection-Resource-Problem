# Grand Challenge Rev4 — Bibliography / Provenance Audit

**Date:** 2026-08-22

**Scope:** DOI/title/author/journal metadata and the specific role of each citation in the Rev4 manuscript.

**Result:** **PASS after one concrete metadata correction and one metadata upgrade.** No scientific theorem or priority conclusion changed.

---

## 1. Marvian and Spekkens — modes of asymmetry

Citation key: `MarvianSpekkens2014Modes`

Verified:

- Iman Marvian and Robert W. Spekkens;
- *Modes of asymmetry: The application of harmonic analysis to symmetric quantum dynamics and quantum reference frames*;
- Physical Review A 90, 062110 (2014);
- DOI `10.1103/PhysRevA.90.062110`.

Role in manuscript: direct prior art for `U(1)` mode decomposition and weighted twirling / Fourier-mode action. This source materially narrows the novelty claim and must remain prominently cited.

Status: **correct**.

---

## 2. Bužek, Derka, Massar — optimal quantum clocks

Citation key: `BuzekDerkaMassar1999`

Verified:

- V. Bužek, R. Derka, S. Massar;
- *Optimal Quantum Clocks*;
- Physical Review Letters 82, 2207–2210 (1999);
- DOI `10.1103/PhysRevLett.82.2207`.

Role: established phase/time estimation under energy-span/resource constraints.

Status: **correct**.

---

## 3. Imai and Hayashi — Fourier phase estimation

Citation key: `ImaiHayashi2009`

Verified:

- Hiroshi Imai and Masahito Hayashi;
- *Fourier analytic approach to phase estimation in quantum systems*;
- New Journal of Physics 11, 043034 (2009);
- DOI `10.1088/1367-2630/11/4/043034`.

Role: direct Fourier-analytic phase-estimation prior art; supports conservative positioning of the random-time problem.

Status: **correct**.

---

## 4. Hayashi — photon-number-constrained phase estimation

Citation key: `Hayashi2011`

Verified from the National Institute of Informatics publication:

- Masahito Hayashi;
- *Phase estimation with photon number constraint*;
- Progress in Informatics 8, 81–87 (2011);
- DOI `10.2201/NiiPi.2011.8.9`;
- arXiv `1011.2546`.

Role: prior art for phase estimation under photon-number constraints and for the distinction between Fisher bounds and globally attainable estimation performance.

Status: **correct**.

---

## 5. Fujiwara and Imai — random-unitary probability estimation

Citation key: `FujiwaraImai2003`

Verified:

- Akio Fujiwara and Hiroshi Imai;
- *Quantum parameter estimation of a generalized Pauli channel*;
- Journal of Physics A: Mathematical and General 36, 8093–8103 (2003);
- DOI `10.1088/0305-4470/36/29/314`.

The paper explicitly treats the channel parameter as coordinates of a probability simplex and analyzes the SLD Fisher information of those random-unitary weights.

Role: establishes that generic quantum estimation of random-unitary mixture probabilities is prior art.

Status: **correct**.

---

## 6. Braunstein and Caves — generic quantum Fisher geometry

Citation key: `BraunsteinCaves1994`

Verified:

- Samuel L. Braunstein and Carlton M. Caves;
- *Statistical distance and the geometry of quantum states*;
- Physical Review Letters 72, 3439–3443 (1994);
- DOI `10.1103/PhysRevLett.72.3439`.

Role: generic QFI/optimal-measurement geometry prior art; not a novelty component.

Status: **correct**.

---

## 7. Tsang, Wiseman, Caves — waveform estimation

Citation key: `TsangWisemanCaves2011`

Verified:

- Mankei Tsang, Howard M. Wiseman, Carlton M. Caves;
- *Fundamental Quantum Limit to Waveform Estimation*;
- Physical Review Letters 106, 090401 (2011);
- DOI `10.1103/PhysRevLett.106.090401`.

Role: establishes general quantum waveform-QFI machinery and supports the manuscript's explicit boundary between random-time distribution encoding and arbitrary parameter-dependent waveform-state synthesis.

Status: **correct**.

---

## 8. Gill — arbitrary joint quantum measurements

Citation key: `Gill2005`

The original bibliography used the 2005 arXiv preprint only. The audit verified a published chapter version:

- Richard D. Gill;
- *Conciliation of Bayes and Pointwise Quantum State Estimation: Asymptotic information bounds in quantum statistics*;
- in *Quantum Stochastics and Information: Statistics, Filtering and Control*;
- editors V. P. Belavkin and M. I. Guţă;
- World Scientific (2008), pp. 239–261;
- DOI `10.1142/9789812832962_0011`;
- arXiv `math/0512443`.

Role: close generic prior art for information bounds under arbitrary collective measurements. The Rev4 theorem no longer logically depends on Holevo/Gill asymptotics because WP20 has a direct finite-copy proof, but Gill remains appropriate contextual prior art.

Status: **upgraded to published metadata**.

---

## 9. Pocovnicu — sharp positive-frequency Gagliardo–Nirenberg inequality

Citation key: `Pocovnicu2011`

A concrete metadata defect was found.

The bibliography previously paired DOI

`10.2140/apde.2011.4.379`

with the title *Explicit formula for the solution of the Szegő equation on the real line and applications*. That title belongs to a different 2011 Pocovnicu paper in Discrete and Continuous Dynamical Systems, DOI `10.3934/dcds.2011.31.607`.

The DOI actually used by the manuscript corresponds to:

- Oana Pocovnicu;
- *Traveling waves for the cubic Szegő equation on the real line*;
- Analysis & PDE 4(3), 379–404 (2011);
- DOI `10.2140/apde.2011.4.379`.

This is also the **correct scientific source** for the manuscript's claim. Proposition 1.5 states the sharp positive-frequency Gagliardo–Nirenberg inequality, and the paper later proves that proposition by Fourier-space Cauchy–Schwarz.

Therefore the error was bibliographic metadata only: the DOI/source was scientifically appropriate, but its title had been copied from Pocovnicu's other 2011 paper.

Status: **corrected**.

---

## 10. Yang — parameterized Hardy–Hilbert best constant

Citation key: `Yang2001HardyHilbert`

Verified:

- Bicheng Yang;
- *On Hardy–Hilbert's Integral Inequality*;
- Journal of Mathematical Analysis and Applications 261(1), 295–306 (2001);
- DOI `10.1006/jmaa.2001.7525`.

The publisher abstract explicitly states that the paper gives a parameterized generalization of the Hardy–Hilbert integral inequality with a **best constant factor involving the beta function**.

Role: classical mathematical provenance for the WP15/WP16 Mellin/Hardy–Hilbert constant. The manuscript does not claim this constant as new mathematics.

Status: **correct**.

---

# Build verification after bibliography repair

After correcting Pocovnicu and upgrading Gill, the complete local Rev4 sequence was rerun:

`pdflatex -> BibTeX -> pdflatex -> pdflatex`.

Result:

- exit status: PASS;
- pages: 7;
- unresolved citations/references: 0;
- overfull boxes: 0;
- undefined controls/fatal TeX errors: 0.

APS BibTeX emitted one internal style warning (`jnrlst ... set 1`), but bibliography generation completed and all entries resolved. This warning does not indicate missing or malformed reference metadata.

---

# Decision

The Rev4 bibliography is now materially stronger than the initial manuscript bibliography.

No citation discovered in this audit preempts the specific operational survival theorem. The audit does, however, reinforce the required novelty discipline:

- weighted `U(1)` twirling and gap modes are Marvian–Spekkens prior art;
- phase estimation under energy/number constraints is established;
- random-unitary probability estimation is established;
- arbitrary-measurement quantum information bounds are established;
- waveform QFI is established;
- the sharp positive-frequency and Hardy–Hilbert analysis ingredients are established.

The candidate contribution remains the **specific arbitrary-measurement classical-Fisher tail law for Fourier perturbations of a latent random-time distribution and its source-to-record energy-survival consequences**.
