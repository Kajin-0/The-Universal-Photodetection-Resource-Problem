from pathlib import Path

BASE = Path(__file__).resolve().parent
SRC = BASE / "event_resource_theorem_rev6.tex"
DST = BASE / "event_resource_theorem_rev7.tex"
APP6 = BASE / "appendix_rare_fast_counterexample_rev6.tex"
APP7 = BASE / "appendix_rare_fast_counterexample_rev7.tex"

text = SRC.read_text(encoding="utf-8")


def replace_once(old: str, new: str) -> None:
    global text
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"expected exactly one occurrence, found {count}: {old[:120]!r}")
    text = text.replace(old, new, 1)


replace_once(
    r"\title{Temporal Information Resources in Autonomous Photodetection Event Channels}",
    r"\title{Temporal Information Transfer and Resource Bounds in Autonomous Photodetection Event Channels}",
)

old_abstract = r"""Photodetector speed is commonly summarized by rise time, transit time, timing jitter, or an electrical $-3\,$dB bandwidth. These quantities need not coincide with loss of information about an incident optical waveform. We formulate temporal photodetection as source-normalized information transfer through an autonomous marked event channel in the weak coherent/direct-detection regime. For sinusoidal optical-flux modulation, the exact Fisher-information transfer is a capture-weighted average of squared characteristic functions of the mark-conditioned registration-delay laws. Wiener theory gives the exact asymptotic high-bandwidth residue in terms of atomic timing mass. For square-integrable delay densities, Parseval's identity yields an exact integrated spectral budget governed by a capture-weighted timing-collision resource. A capture-weighted local registration-hazard budget provides a microscopic sufficient bound and an explicit inverse-bandwidth ceiling. We construct a smooth family with exactly fixed mean delay and exactly fixed timing variance while information transfer approaches the capture ceiling uniformly on every prescribed finite frequency band. A separate synchronous-control counterexample shows that an unbounded temporal reference can preserve arrival-phase information despite arbitrarily slow final registration. Finally, for a restricted bidirectionally connected finite-state Markov optical gateway, stationary entropy production, activity, and throughput imply a finite information-bandwidth bound only when an absolute microscopic transition-rate scale is also supplied; a complementary rare-fast family shows that stationary thermodynamic aggregates alone do not determine the temporal information scale. The result is a resource hierarchy for autonomous event photodetection rather than a universal sensitivity--bandwidth--temperature product."""

new_abstract = r"""Photodetector speed is commonly summarized by rise time, transit time, timing jitter, or an electrical $-3\,$dB bandwidth. These quantities need not coincide with loss of information about an incident optical waveform. We formulate temporal photodetection as source-normalized information transfer through an autonomous marked event channel in the weak coherent/direct-detection regime. For arbitrary finite-dimensional weak temporal flux perturbations, the exact primary-record Fisher matrix is a frequency integral weighted by
$G(\omega)=\int |H_m(\omega)|^2\kappa(dm)$, a capture-weighted average of squared characteristic functions of the mark-conditioned registration-delay laws. Thus $G$ is the spectral multiplier of the complete local weak-waveform Fisher operator; pointwise ordering of two $G$ spectra is necessary and sufficient for one detector to Fisher-dominate the other for every admissible weak temporal waveform task. Sinusoidal modulation is its Fourier-mode specialization. Wiener theory gives the exact asymptotic high-bandwidth residue in terms of atomic timing mass. For square-integrable delay densities, Parseval's identity yields an exact integrated spectral budget and the DC-normalized Fisher-equivalent bandwidth $B_{\rm FI}=\mathfrak R_2/(4\eta)$. A capture-weighted local registration-hazard budget supplies the microscopic bound $B_{\rm FI}\le\mathfrak H/(4\eta)$ and explicit inverse resource costs. We then prove that fixed mean and variance, a free source-synchronous clock, and stationary thermodynamic aggregates are each insufficient timing resources in distinct senses. A restricted finite-state Markov gateway becomes bounded only after an absolute microscopic transition-rate scale is supplied. The result is a temporal-information resource theory for autonomous event photodetection rather than a universal sensitivity--bandwidth--temperature product."""
replace_once(old_abstract, new_abstract)

replace_once(
    r"""We therefore do not claim the general observation that timing response limits photon information. The question here is narrower: which detector-side resources are sufficient to bound \emph{source-normalized} temporal information transfer in an autonomous event detector, and which familiar detector metrics are provably insufficient?

We restrict the first theorem to independent-event weak coherent/direct detection.""",
    r"""We therefore do not claim the general observation that timing response limits photon information. Fisher-information-based information transfer functions have also been used in optical phase imaging \cite{KoppellKasevich2021}; our use of $G(\omega)$ is specific to the marked photodetection delay channel and its temporal resource hierarchy. Recent photodetector metrology likewise emphasizes that square-pulse response, ultrafast transient response, and $-3\,$dB bandwidth can probe different dynamics and need not report the same response time \cite{Deng2026}. The question here is narrower: which detector-side resources are sufficient to bound \emph{source-normalized} temporal information transfer in an autonomous event detector, and which familiar detector metrics are provably insufficient?

We restrict the theorem stack to independent-event weak coherent/direct detection.""",
)

replace_once(
    r"\input{figure_resource_hierarchy_rev5}",
    r"\input{figure_resource_hierarchy_rev7}",
)

replace_once(
    r"\begin{theorem}[Exact marked-event information transfer]",
    r"\begin{theorem}[Exact sinusoidal marked-event information transfer]",
)

anchor_after_theorem = r"""At zero frequency, $G(0)=\eta$. The mark is defined to contain every primary-event variable available to the final estimator. Intentionally discarding a mark is downstream coarse graining and can only reduce FI.

\section{Atomic timing and the exact high-band residue}"""
replace_once(
    anchor_after_theorem,
    r"""At zero frequency, $G(0)=\eta$. The mark is defined to contain every primary-event variable available to the final estimator. Intentionally discarding a mark is downstream coarse graining and can only reduce FI.

\input{section_waveform_operator_rev7}

\section{Atomic timing and the exact high-band residue}""",
)

replace_once(
    r"""Equation~\eqref{eq:flat} is recovered for uniform $w$ on $[-\Omega,\Omega]$. Equation~\eqref{eq:arbsource} is not asserted to cover arbitrary correlated multiparameter estimation across frequency.

\section{Microscopic completion by local registration intensity}""",
    r"""Equation~\eqref{eq:flat} is recovered for uniform $w$ on $[-\Omega,\Omega]$. Equation~\eqref{eq:arbsource} is a scalar weighted-task consequence of the spectral budget; arbitrary correlated finite-dimensional weak temporal estimation is covered directly by the Fisher-operator result Eq.~\eqref{eq:waveformFI}.

\section{Microscopic completion by local registration intensity}""",
)

qmax_anchor = r"""For a finite-state continuous-time Markov detector with pre-registration state set $S_{\rm pre}$, define $\lambda_x=\sum_{y\ne x}W_{yx}$ and $q_{\max}=\max_{x\in S_{\rm pre}}\lambda_x$. Condition first on an initial pre-registration state $x$. Its first holding time $T_x\sim\operatorname{Exp}(\lambda_x)$ is independent of the exit destination and subsequent Markov trajectory. Under the stated restriction that the accessible mark does not independently record the realized holding time, $D\mid(M,x)=T_x+Y_{M,x}$ with $Y_{M,x}\ge0$. Hence $f_{D\mid M,x}(t)\le\lambda_x S_{D\mid M,x}(t)$ by the same exponential-convolution calculation used below, so $h_D(t\mid M,x)\le\lambda_x\le q_{\max}$. If the initial pre-registration state is random after capture, mixing over $x$ preserves $f\le q_{\max}S$. Thus $q_{\max}$ is a sufficient uniform conditional-hazard ceiling. This local bare-rate scale is distinct from stationary dynamical activity.

\section{Exactly fixed mean and RMS jitter do not bound information bandwidth}"""
replace_once(
    qmax_anchor,
    r"""For a finite-state continuous-time Markov detector with pre-registration state set $S_{\rm pre}$, define $\lambda_x=\sum_{y\ne x}W_{yx}$ and $q_{\max}=\max_{x\in S_{\rm pre}}\lambda_x$. Condition first on an initial pre-registration state $x$. Its first holding time $T_x\sim\operatorname{Exp}(\lambda_x)$ is independent of the exit destination and subsequent Markov trajectory. Under the stated restriction that the accessible mark does not independently record the realized holding time, $D\mid(M,x)=T_x+Y_{M,x}$ with $Y_{M,x}\ge0$. Hence $f_{D\mid M,x}(t)\le\lambda_x S_{D\mid M,x}(t)$ by the same exponential-convolution calculation used below, so $h_D(t\mid M,x)\le\lambda_x\le q_{\max}$. If the initial pre-registration state is random after capture, mixing over $x$ preserves $f\le q_{\max}S$. Thus $q_{\max}$ is a sufficient uniform conditional-hazard ceiling. This local bare-rate scale is distinct from stationary dynamical activity.

\input{section_operational_bandwidth_rev7}

\section{Exactly fixed mean and RMS jitter do not bound information bandwidth}""",
)

replace_once(
    r"""Talaga's TCSPC analysis already emphasized IRF-induced information loss, detector sensitivity--bandwidth tradeoffs, and the frequency-domain power spectrum of detector IRFs \cite{Talaga2009}. K\"ollner and Wolfrum quantified photon requirements for lifetime estimation \cite{KollnerWolfrum1992}; later FI analyses explicitly included finite IRFs and photon statistics \cite{Bouchet2019,TrinhEsposito2021}. Our parameter is instead a modulation of the incident source itself, and our claims concern the exact marked-event transfer theorem plus the atomic/collision/hazard resource hierarchy and its no-go/repair statements.""",
    r"""Talaga's TCSPC analysis already emphasized IRF-induced information loss, detector sensitivity--bandwidth tradeoffs, and the frequency-domain power spectrum of detector IRFs \cite{Talaga2009}. K\"ollner and Wolfrum quantified photon requirements for lifetime estimation \cite{KollnerWolfrum1992}; later FI analyses explicitly included finite IRFs and photon statistics \cite{Bouchet2019,TrinhEsposito2021}. Fisher-information transfer functions have also been introduced for phase-imaging measurement design \cite{KoppellKasevich2021}. Our claim is not that Fisher information or information-transfer functions are generically new. Here the same exact marked-delay spectrum $G(\omega)$ is the spectral multiplier of the complete local weak-temporal-waveform Fisher operator, and its pointwise ordering is necessary and sufficient for universal Fisher dominance within the autonomous independent-event detector class. The atomic/collision/hazard hierarchy then constrains that operator through detector-side timing resources.

The distinction from conventional response metrics is also practically current: recent photodetector analysis shows that square-pulse, ultrafast-pulse, and $-3\,$dB response-time measurements need not be equivalent outside specific regimes \cite{Deng2026}. The quantity $B_{\rm FI}$ instead measures the equivalent spectral area of source-normalized Fisher transfer in the present stochastic event model.""",
)

old_discussion = r"""For autonomous event detection, temporal information resources form a hierarchy. Atomic timing mass determines the exact asymptotic high-band residue. The capture-weighted collision intensity $\Rtwo$ fixes the integrated source-information transfer spectrum. The capture-weighted local hazard capacity $\Hcap$ is a microscopic sufficient resource satisfying $\Rtwo\le\Hcap$. Equivalently, preserving absolute average information fraction $q$ over ordinary-frequency half-band $B$ requires the minimum cost $\Hcap\ge4Bq$. Stationary activity and entropy production do not generally control these local timing resources because arbitrarily fast dynamics can hide in rarely occupied states; a restricted thermodynamic repair appears only after an absolute microscopic rate is supplied."""
new_discussion = r"""For autonomous event detection, $G(\omega)$ is more than a single-tone response curve: it is the spectral multiplier of the complete local weak-waveform Fisher-information operator. Consequently, pointwise ordering of $G$ is necessary and sufficient for one detector to dominate another for every admissible weak temporal estimation task in the model. The timing-resource hierarchy then constrains this complete operator. Atomic timing mass determines the exact asymptotic high-band residue. The capture-weighted collision intensity $\Rtwo$ fixes the integrated source-information transfer spectrum and exactly determines the Fisher-equivalent bandwidth $B_{\rm FI}=\Rtwo/(4\eta)$. The capture-weighted local hazard capacity $\Hcap$ is a microscopic sufficient resource satisfying $\Rtwo\le\Hcap$ and $B_{\rm FI}\le\Hcap/(4\eta)$. Equivalently, preserving absolute average information fraction $q$ over ordinary-frequency half-band $B$ requires the minimum cost $\Hcap\ge4Bq$. Stationary activity and entropy production do not generally control these local timing resources because arbitrarily fast dynamics can hide in rarely occupied states; a restricted thermodynamic repair appears only after an absolute microscopic rate is supplied."""
replace_once(old_discussion, new_discussion)

replace_once(
    r"\input{appendix_rare_fast_counterexample_rev6}",
    r"\input{appendix_rare_fast_counterexample_rev7}",
)

required = [
    r"\input{section_waveform_operator_rev7}",
    r"\input{section_operational_bandwidth_rev7}",
    r"B_{\rm FI}",
    r"KoppellKasevich2021",
    r"Deng2026",
    r"appendix_rare_fast_counterexample_rev7",
]
for token in required:
    if token not in text:
        raise RuntimeError(f"missing required Rev7 token: {token}")

if "Equation~\\eqref{eq:arbsource} is not asserted to cover arbitrary correlated multiparameter estimation" in text:
    raise RuntimeError("obsolete weighted-task disclaimer survived Rev7 generation")

DST.write_text(text, encoding="utf-8")
APP7.write_text(APP6.read_text(encoding="utf-8"), encoding="utf-8")
print(f"wrote {DST.name} ({len(text)} chars)")
print(f"wrote {APP7.name}")
