from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "event_resource_theorem_rev5.tex"
DST = HERE / "event_resource_theorem_rev6.tex"
APP_SRC = HERE / "appendix_rare_fast_counterexample.tex"
APP_DST = HERE / "appendix_rare_fast_counterexample_rev6.tex"

text = SRC.read_text(encoding="utf-8")
appendix = APP_SRC.read_text(encoding="utf-8")


def replace_once(buf: str, old: str, new: str, label: str) -> str:
    count = buf.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected exactly one match, found {count}")
    return buf.replace(old, new, 1)


# 1. Exact-DC normalization clarification.  Eq. (2) uses the nonzero-frequency
#    long-time average <cos^2>=1/2; at exact DC the same factor changes in both
#    incident and output FI, leaving the normalized transfer G(0)=eta.
text = replace_once(
    text,
    "\\end{equation}\nFor this paper we normalize every electrical-record Fisher information by Eq.~\\eqref{eq:inputFI}. The source model is intentionally classical/direct-detection specific; no claim is made here for arbitrary optical phase encodings or nonclassical input states.",
    "\\end{equation}\nEquation~\\eqref{eq:inputFI} assumes $\\omega\\ne0$, so the long-time average of $\\cos^2(\\omega t)$ is $1/2$. At exact DC ($\\omega=0$), the incident Fisher-information rate is instead $\\Phi_0$; the same factor changes in the output Fisher information, so the normalized transfer remains $G(0)=\\eta$, obtained directly (or equivalently by continuous extension of the transfer ratio).\nFor this paper we normalize every electrical-record Fisher information by Eq.~\\eqref{eq:inputFI} for nonzero modulation frequency, with the exact-DC convention just stated. The source model is intentionally classical/direct-detection specific; no claim is made here for arbitrary optical phase encodings or nonclassical input states.",
    "exact-DC normalization clarification",
)

# 2. Make the finite-state q_max statement self-contained rather than asserted.
text = replace_once(
    text,
    "For a finite-state continuous-time Markov detector with pre-registration state set $S_{\\rm pre}$, a sufficient uniform bound is the maximum total escape rate $q_{\\max}=\\max_{x\\in S_{\\rm pre}}\\sum_{y\\ne x}W_{yx}$, provided the accessible mark does not independently record the realized pre-registration holding times. This local bare-rate scale is distinct from stationary dynamical activity.",
    "For a finite-state continuous-time Markov detector with pre-registration state set $S_{\\rm pre}$, define $\\lambda_x=\\sum_{y\\ne x}W_{yx}$ and $q_{\\max}=\\max_{x\\in S_{\\rm pre}}\\lambda_x$. Condition first on an initial pre-registration state $x$. Its first holding time $T_x\\sim\\operatorname{Exp}(\\lambda_x)$ is independent of the exit destination and subsequent Markov trajectory. Under the stated restriction that the accessible mark does not independently record the realized holding time, $D\\mid(M,x)=T_x+Y_{M,x}$ with $Y_{M,x}\\ge0$. Hence $f_{D\\mid M,x}(t)\\le\\lambda_x S_{D\\mid M,x}(t)$ by the same exponential-convolution calculation used below, so $h_D(t\\mid M,x)\\le\\lambda_x\\le q_{\\max}$. If the initial pre-registration state is random after capture, mixing over $x$ preserves $f\\le q_{\\max}S$. Thus $q_{\\max}$ is a sufficient uniform conditional-hazard ceiling. This local bare-rate scale is distinct from stationary dynamical activity.",
    "q_max proof",
)

# 3. Keep the FWHM statement strictly within what has been proved.
text = replace_once(
    text,
    "Likewise, an FWHM or other scalar width is not a complete substitute for the timing law without additional shape assumptions.",
    "The same caution applies to scalar widths such as FWHM unless additional shape assumptions are imposed; no fixed-FWHM counterexample is claimed here.",
    "FWHM wording",
)

# 4. Replace probabilistic-reversibility terminology with explicit bidirectional
#    transition support and add the isolated-event bridge before applying the
#    stationary thermodynamic rate bound to the independent-event theorem.
text = replace_once(
    text,
    "Consider a restricted reversible \\emph{finite-state, time-homogeneous continuous-time Markov} optical gateway",
    "Consider a restricted bidirectionally connected \\emph{finite-state, time-homogeneous continuous-time Markov} optical gateway. Here bidirectionally connected means that every transition used in the thermodynamic accounting has reverse-transition support; it does not mean stationary detailed-balance reversibility. The optical gateway is",
    "thermodynamic terminology",
)

text = replace_once(
    text,
    "\\label{eq:Lstar}\n\\end{equation}\n\nSuppose no primary electrical registration can occur before the first exit from state 1.",
    "\\label{eq:Lstar}\n\\end{equation}\n\nEquation~\\eqref{eq:Lstar} is inferred from stationary baseline traffic and thermodynamic budgets, but its use in the event theorem requires an isolated-event reduction. We therefore condition on an optical capture that places the gateway in state 1 and use the subsequent autonomous CTMC only to generate the per-photon post-capture delay law $\\mu_m$ in Eq.~\\eqref{eq:kernel}. The application below assumes the low-overlap regime in which successive incident photons are sufficiently separated that stationary occupancy and recovery do not make capture probability or the post-capture kernel depend on prior source events. If capture or recovery is history dependent, Eq.~\\eqref{eq:kernel} is not the correct model and Eq.~\\eqref{eq:thermo} is not claimed.\n\nSuppose no primary electrical registration can occur before the first exit from state 1.",
    "isolated-event thermodynamic bridge",
)

text = replace_once(
    text,
    "Appendix~\\ref{app:rare-fast} gives a reversible three-state family",
    "Appendix~\\ref{app:rare-fast} gives a bidirectionally connected three-state family",
    "rare-fast main-text terminology",
)

# Rev6 uses a versioned appendix so Rev5 remains a frozen historical source.
text = replace_once(
    text,
    "\\input{appendix_rare_fast_counterexample}",
    "\\input{appendix_rare_fast_counterexample_rev6}",
    "versioned rare-fast appendix input",
)

appendix = replace_once(
    appendix,
    "This appendix gives a self-contained reversible three-state family showing that stationary thermodynamic resources do not bound the local temporal scale.",
    "This appendix gives a self-contained bidirectionally connected three-state family showing that stationary thermodynamic resources do not bound the local temporal scale. Here bidirectionally connected means that each transition in the thermodynamic network has reverse-transition support; the stationary process need not satisfy detailed balance and generally has nonzero currents and entropy production.",
    "rare-fast appendix terminology",
)

DST.write_text(text, encoding="utf-8")
APP_DST.write_text(appendix, encoding="utf-8")
print(f"Generated {DST.name} from {SRC.name}")
print(f"Generated {APP_DST.name} from {APP_SRC.name}")
