from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "event_resource_theorem_rev4.tex"
DST = HERE / "event_resource_theorem_rev5.tex"

text = SRC.read_text(encoding="utf-8")


def replace_once(old: str, new: str, label: str) -> None:
    global text
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected exactly one match, found {count}")
    text = text.replace(old, new, 1)


# 1. Explicitly call out Fig. 1 in the prose and use the Rev5 hierarchy asset.
replace_once(
    "\\input{figure_resource_hierarchy}\n\n"
    "\\section{Autonomous marked event channel}",
    "Figure~\\ref{fig:resourceHierarchy} summarizes the intrinsic timing-resource hierarchy used below.\n\n"
    "\\input{figure_resource_hierarchy_rev5}\n\n"
    "\\section{Autonomous marked event channel}",
    "resource-hierarchy prose callout",
)

# 2. WP35 correction: complete mark conditioning can expose competing-exit holding rates.
#    The safe generic finite-state CTMC uniform resource is the total pre-registration
#    escape-rate ceiling, not merely the successful-registration edge intensity.
#    The generic quantum-jump sentence is deliberately removed from this manuscript.
replace_once(
    "For a classical Markov detector, a sufficient uniform $\\Lambda$ is the maximum total intensity of all first-registration transitions from any pre-registration state. "
    "For quantum-jump registration, a sufficient bound is $\\|\\sum_\\alpha L_\\alpha^\\dagger L_\\alpha\\|_\\infty$. "
    "These are local rate/operator resources, not stationary activities.",
    "For a finite-state continuous-time Markov detector, a sufficient uniform bound is the maximum total escape rate "
    "$q_{\\max}=\\max_{x\\in S_{\\rm pre}}\\sum_{y\\ne x}W_{yx}$ from any pre-registration state, "
    "provided the accessible mark does not independently record the realized pre-registration holding times. "
    "This local bare-rate scale is distinct from stationary dynamical activity.",
    "WP35 Markov-rate correction",
)

# 3. Explicitly call out Fig. 2 in the fixed-mean/fixed-variance no-go discussion.
replace_once(
    "\\input{figure_jitter_no_go}\n\n"
    "\\section{External temporal reference is an independent resource}",
    "Figure~\\ref{fig:jitterNoGo} shows representative members of this exact fixed-mean, fixed-variance family and the resulting migration of substantial transfer to larger normalized frequency.\n\n"
    "\\input{figure_jitter_no_go}\n\n"
    "\\section{External temporal reference is an independent resource}",
    "jitter-no-go prose callout",
)

# 4. Final citation audit: keep the Dechant comparison at the level directly supported
#    by the cited finite-frequency fluctuation-response paper.
replace_once(
    "Recent finite-frequency fluctuation--response inequalities bound response precision by dynamical activity or related resources in Markov systems \\cite{Dechant2026}. "
    "Those results are pointwise response/noise inequalities and use different broadband quantities. "
    "Equation~\\eqref{eq:parseval} instead follows from the first-registration timing measure. "
    "We do not claim generic finite-frequency response--noise inequalities as new.",
    "Recent finite-frequency fluctuation--response inequalities constrain steady-state finite-frequency response and fluctuations in general Markovian dynamics and yield broadband signal-to-noise bounds \\cite{Dechant2026}. "
    "Those results concern response/noise inequalities and use different broadband quantities. "
    "Equation~\\eqref{eq:parseval} instead follows from the first-registration timing measure. "
    "We do not claim generic finite-frequency response--noise inequalities as new.",
    "Dechant comparison wording",
)

DST.write_text(text, encoding="utf-8")
print(f"Generated {DST.name} from {SRC.name}")
