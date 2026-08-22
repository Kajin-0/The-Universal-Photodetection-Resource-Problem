from pathlib import Path

src = Path("energy_survival_temporal_fisher_rev6_prxq.tex")
dst = Path("energy_survival_temporal_fisher_rev7_prxq.tex")

text = src.read_text(encoding="utf-8")


def replace_once(old: str, new: str):
    global text
    count = text.count(old)
    assert count == 1, f"Expected exactly one match, found {count}: {old[:140]!r}"
    text = text.replace(old, new, 1)


# 0. Rev7-specific Figure 1 keeps the continuum qualification and excess-energy
# meaning visible without retroactively changing the frozen Rev5/Rev6 artwork.
replace_once(
    r"\input{figure1_operational_architecture_body.tex}",
    r"\input{figure1_operational_architecture_body_rev7.tex}",
)

# 1. Abstract: keep the continuum hypothesis and excess-energy meaning visible,
# and make clear that the survival law—not its Markov/first-moment corollary—is
# the principal theorem.
replace_once(
    "For controlled large-period limits it gives the pointwise survival law $R(\\nu)\\leq\\Pr(\\Omega\\geq\\nu)$, the sharp area bound $\\int_{\\mathbb R}R(\\nu)\\dd\\nu\\leq2\\bar E^+/\\hbar$, and the pointwise resource inequality $\\bar E^+\\geq\\hbar\\nu R(\\nu)=hfR(2\\pi f)$.",
    "For controlled periodic-to-continuum limits it gives the pointwise survival law $R(\\nu)\\leq\\Pr(\\Omega\\geq\\nu)$.  Here $\\bar E^+$ denotes mean excitation energy above the participating lower edge, not a common carrier-energy offset.  The sharp area bound $\\int_{\\mathbb R}R(\\nu)\\dd\\nu\\leq2\\bar E^+/\\hbar$ and the pointwise inequality $\\bar E^+\\geq\\hbar\\nu R(\\nu)=hfR(2\\pi f)$ are first-moment corollaries of this survival law.",
)
replace_once(
    "A geometric energy distribution with the canonical phase measurement saturates every discrete harmonic simultaneously, and its continuum limit is the exponential-energy/Cauchy-time equality family.",
    "A geometric energy distribution with the canonical phase measurement saturates every discrete harmonic simultaneously, and its controlled continuum limit is the exponential-energy/Cauchy-time equality family.  A nonextremal truncated-Gaussian single-photon wavepacket is also close to the survival ceiling under canonical covariant timing.",
)

# 2. Introduction: sharpen the novelty boundary against modes of asymmetry and
# emphasize the all-mode/survival theorem rather than the elementary hf moment
# consequence.
old_intro = (
    "Harmonic decompositions of $U(1)$-asymmetric states and weighted group twirling are established tools: in particular, a weighted twirl multiplies each energy-gap mode by the corresponding Fourier coefficient of the mixing distribution~\\cite{MarvianSpekkens2014Modes}.  Phase estimation under energy or photon-number constraints is likewise well developed~\\cite{BuzekDerkaMassar1999,ImaiHayashi2009,Hayashi2011}, as are generic quantum-statistical bounds for arbitrary measurements~\\cite{BraunsteinCaves1994,Gill2005} and estimation of random-unitary channel weights~\\cite{FujiwaraImai2003}.  Our question is narrower: how much \\emph{classical Fisher information about a local Fourier perturbation of the mixing distribution} can any downstream measurement retain?"
)
new_intro = (
    "Harmonic decompositions of $U(1)$-asymmetric states and weighted group twirling are established tools: in particular, a weighted twirl multiplies each energy-gap mode by the corresponding Fourier coefficient of the mixing distribution~\\cite{MarvianSpekkens2014Modes}.  Phase estimation under energy or photon-number constraints is likewise well developed~\\cite{BuzekDerkaMassar1999,ImaiHayashi2009,Hayashi2011}, as are generic quantum-statistical bounds for arbitrary measurements~\\cite{BraunsteinCaves1994,Gill2005} and estimation of random-unitary channel weights~\\cite{FujiwaraImai2003}.  Modes-of-asymmetry theory therefore identifies the kinematic gap components available under the symmetry.  Our question is operationally different: how much \\emph{classical Fisher information about a local Fourier perturbation of the mixing distribution} can any actual downstream POVM extract, and can that amount be bounded sharply using only the participating energy populations?"
)
replace_once(old_intro, new_intro)

replace_once(
    "Summing the harmonic tails gives the mean excitation exactly, while a periodic-to-continuum construction produces a pointwise survival-function law for the phase-averaged two-quadrature retention and a Planck-scale energy--frequency constraint.",
    "Summing the harmonic tails gives the mean excitation exactly, while a controlled periodic-to-continuum construction produces a pointwise survival-function law for the phase-averaged two-quadrature retention.  The associated Planck-scale energy--frequency inequality is then an immediate first-moment consequence of that stronger survival statement, not the independent source of the result.",
)

# 3. Continuum section: make the controlled-limit character impossible to miss.
replace_once(
    r"\section{Continuum survival-function law}",
    r"\section{Controlled periodic-to-continuum survival law}",
)
replace_once(
    r"\begin{theorem}[Continuum survival bound]",
    r"\begin{theorem}[Controlled-limit survival bound]",
)
replace_once(
    r"\begin{corollary}[Area and pointwise energy laws]",
    r"\begin{corollary}[Area and first-moment energy corollaries]",
)
replace_once(
    "where $\\bar E^+=\\hbar\\bar\\omega$ and the second line uses the even extension.  Moreover,",
    "where $\\bar E^+=\\hbar\\bar\\omega$ is the mean excitation energy above the participating lower edge (not a common laboratory or carrier-energy offset), and the second line uses the even extension.  Moreover,",
)
replace_once(
    "The pointwise statement follows from",
    "The pointwise statement is the elementary first-moment tail consequence of the operational survival law:",
)

# 4. Insert one nonextremal, physically interpretable single-photon example.
# It is deliberately analytic and adds no new theorem claim.
anchor = (
    "Canonical phase/time measurements and their Fourier structure are established; their role here is to exhibit exact equality rather than to supply a novelty claim.\n\n"
)
assert anchor in text, "Expected equality-family anchor not found"
example = r"""\section{Nonextremal single-photon wavepacket}
\label{sec:gaussian-photon}

The equality family is mathematically extremal, so it is useful to check that the survival ceiling is also informative for a nonextremal photon wavepacket.  Single-photon time--frequency variables and quantum-limited arrival-time measurements are standard quantum-optical settings~\cite{FabreKellerMilman2022,FolgeEtAl2026}.  Let $\omega_*$ denote the participating lower optical frequency and write the excess frequency as $\Omega=\omega-\omega_*\geq0$.  In the one-photon sector,
\begin{equation}
 |1_\psi\rangle=\int_0^\infty \psi(\Omega)
 a^\dagger(\omega_*+\Omega)|0\rangle\,\dd\Omega .
 \label{eq:single-photon-state}
\end{equation}
The common energy $\hbar\omega_*$ contributes only a global phase to this sector, so the relevant resource is the excess energy $\bar E^+=\hbar\langle\Omega\rangle$.

Consider a Gaussian spectral density centered one Gaussian width above the active edge and truncated only by semiboundedness,
\begin{equation}
 q_\sigma(\Omega)
 =\frac{\sqrt{2/\pi}}{\sigma Z}
 \exp\!\left[-\frac{(\Omega-\sigma)^2}{2\sigma^2}\right],
 \quad
 Z=\operatorname{erfc}(-1/\sqrt2),
 \label{eq:truncated-gaussian}
\end{equation}
for $\Omega\geq0$.  Its survival function is
\begin{equation}
 S_\sigma(\nu)
 =\frac{\operatorname{erfc}[(\nu-\sigma)/(\sqrt2\sigma)]}{Z}.
 \label{eq:gaussian-survival}
\end{equation}
For the canonical covariant time measurement, obtained as the controlled limit of the discrete canonical phase POVM, the two-quadrature retention is the squared spectral Hellinger affinity,
\begin{align}
 R_{\rm time}(\nu)
 &=\left[\int_0^\infty
 \sqrt{q_\sigma(\Omega)q_\sigma(\Omega+\nu)}\,\dd\Omega\right]^2\\
 &=\e^{-\nu^2/(4\sigma^2)}
 \left[\frac{\operatorname{erfc}[(\nu/2-\sigma)/(\sqrt2\sigma)]}{Z}\right]^2 .
 \label{eq:gaussian-retention}
\end{align}
Thus the theorem gives $R_{\rm time}(\nu)\leq S_\sigma(\nu)$, while the actual timing measurement lies close to the ceiling over the central bandwidth.  At $\nu=0.5\sigma$, $S_\sigma=0.82185$ and $R_{\rm time}=0.79375$, or $96.6\%$ of the ceiling; at $\nu=\sigma$, the corresponding values are $0.59429$ and $0.52604$, or $88.5\%$.  The mean excess frequency is $\langle\Omega\rangle=1.28760\,\sigma$.  This example is not an equality construction; it shows that the population-tail bound can remain quantitatively restrictive for a smooth, nonextremal single-photon spectrum.

"""
text = text.replace(anchor, anchor + example, 1)

# 5. Discussion/conclusion: defend the modes-of-asymmetry distinction and the
# excess-energy meaning explicitly; demote hf to a corollary.
replace_once(
    "Established modes-of-asymmetry theory explains why those Fourier coefficients couple to corresponding energy gaps~\\cite{MarvianSpekkens2014Modes}.  The new statistical step is the operational inequality that converts the $k$-gap tangent into an accessible Fisher ceiling determined by paired populations and, universally, by the upper energy tail.",
    "Established modes-of-asymmetry theory explains which energy-gap components accompany those Fourier coefficients~\\cite{MarvianSpekkens2014Modes}.  The present theorem is not a restatement of that support condition: it bounds the \\emph{classical Fisher information of any actual POVM}, including finite-copy entangled collective measurements, by a sharp coefficient determined solely by paired populations and, universally, by the upper energy tail.  The geometric family further shows that one common measurement can saturate the full harmonic hierarchy.",
)
replace_once(
    "The central result can be read directly from Eq.~\\eqref{eq:survival-law}: retaining phase-averaged two-quadrature temporal Fisher information at angular frequency $\\nu$ requires spectral probability weight at least $\\hbar\\nu$ above the participating lower energy edge.  A uniform guarantee over all sinusoidal phases is a stronger requirement and therefore obeys the same bound.",
    "The central result can be read directly from Eq.~\\eqref{eq:survival-law}: retaining phase-averaged two-quadrature temporal Fisher information at angular frequency $\\nu$ requires surviving spectral probability above an excess-frequency gap $\\nu$ from the participating lower edge.  The additive edge itself is irrelevant; the resource is excitation energy above that edge.  A uniform guarantee over all sinusoidal phases is a stronger requirement and therefore obeys the same bound.",
)
replace_once(
    "In the controlled large-period continuum limit, the same construction gives an exponential excitation spectrum and Cauchy timing density, providing an exact bridge between the energy survival function and a physically interpretable timestamp channel.",
    "In the controlled large-period continuum limit, the same construction gives an exponential excitation spectrum and Cauchy timing density, providing an exact bridge between the energy survival function and a physically interpretable timestamp channel.  Section~\\ref{sec:gaussian-photon} shows that a smooth truncated-Gaussian single-photon spectrum also approaches the survival ceiling closely under canonical covariant timing.",
)

replace_once(
    "The resulting controlled-limit continuum law,\n\\begin{equation}\n R(\\nu)\\leq\\Pr(\\Omega\\geq\\nu),\n\\end{equation}\nimplies both a sharp integrated budget $\\int_{\\mathbb R}R\\leq2\\bar E^+/\\hbar$ and the pointwise Planck-scale constraint $\\bar E^+\\geq hfR(2\\pi f)$.",
    "The resulting controlled periodic-to-continuum law,\n\\begin{equation}\n R(\\nu)\\leq\\Pr(\\Omega\\geq\\nu),\n\\end{equation}\nis the principal continuum statement.  Its first-moment consequences are the sharp integrated budget $\\int_{\\mathbb R}R\\leq2\\bar E^+/\\hbar$ and the pointwise inequality $\\bar E^+\\geq hfR(2\\pi f)$, where $\\bar E^+$ is excess energy above the participating lower edge.",
)

# Guardrails.
assert r"\input{figure1_operational_architecture_body_rev7.tex}" in text
assert r"\section{Controlled periodic-to-continuum survival law}" in text
assert "first-moment corollaries" in text
assert "Nonextremal single-photon wavepacket" in text
assert "FabreKellerMilman2022" in text and "FolgeEtAl2026" in text
assert r"R_{\rm time}(\nu)" in text
assert "96.6\\%" in text and "88.5\\%" in text
assert "not a restatement" in text
assert r"\boxed{" not in text

# Rev7 is referee hardening: no change to the finite-copy theorem, its proof,
# the controlled-limit survival inequality, or any numerical constant therein.
dst.write_text(text, encoding="utf-8")
print(f"Wrote {dst}")
