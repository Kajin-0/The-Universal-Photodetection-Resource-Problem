from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "event_resource_theorem_rev3.tex"
DST = HERE / "event_resource_theorem_rev4.tex"

text = SRC.read_text(encoding="utf-8")


def replace_once(old: str, new: str, label: str) -> None:
    global text
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected exactly one match, found {count}")
    text = text.replace(old, new, 1)


# 1. Packages required only by the theorem figures.
replace_once(
    "\\usepackage{microtype}\n",
    "\\usepackage{microtype}\n"
    "\\usepackage{graphicx}\n"
    "\\usepackage{tikz}\n"
    "\\usepackage{pgfplots}\n"
    "\\pgfplotsset{compat=1.18}\n",
    "figure packages",
)

# 2. Put the resource-hierarchy figure immediately after the theorem scope is stated.
replace_once(
    "We restrict the first theorem to independent-event weak coherent/direct detection. "
    "Coherent continuous pointers, nonclassical source states, history-dependent high-flux counters, "
    "and externally synchronized detectors require additional resource accounting and are outside the main theorem class.\n\n"
    "\\section{Autonomous marked event channel}",
    "We restrict the first theorem to independent-event weak coherent/direct detection. "
    "Coherent continuous pointers, nonclassical source states, history-dependent high-flux counters, "
    "and externally synchronized detectors require additional resource accounting and are outside the main theorem class.\n\n"
    "\\input{figure_resource_hierarchy}\n\n"
    "\\section{Autonomous marked event channel}",
    "resource-hierarchy figure insertion",
)

# 3. Promote the inverse resource-cost statement to an explicit corollary.
needle = (
    "The weighted form is strictly sharper: an arbitrarily fast branch does not matter if its capture weight becomes correspondingly negligible.\n\n"
    "For constant hazard $f(t)=\\Lambda e^{-\\Lambda t}$,"
)
corollary = r'''The weighted form is strictly sharper: an arbitrarily fast branch does not matter if its capture weight becomes correspondingly negligible.

\begin{corollary}[Minimum timing-resource cost]
For a flat source-information task on $|\omega|\le\Omega$, let
\begin{equation}
B\equiv\frac{\Omega}{2\pi}
\end{equation}
be the ordinary-frequency half-band. Achieving absolute average transfer
\begin{equation}
\bar\eta_I(\Omega)\ge q>0
\end{equation}
requires $q\le\eta$ and
\begin{equation}
\boxed{\Rtwo\ge4Bq,\qquad \Hcap\ge4Bq.}
\label{eq:resourceCost}
\end{equation}
If the markwise hazards share a uniform ceiling $\Lambda(m)\le\Lambda$, then $\Hcap\le\eta\Lambda$ and therefore
\begin{equation}
\boxed{\Lambda\ge\frac{4Bq}{\eta}.}
\label{eq:uniformResourceCost}
\end{equation}
For a target retention $q=r\eta$ relative to the captured DC information, this reduces to $\Lambda\ge4Br$.
\end{corollary}

For constant hazard $f(t)=\Lambda e^{-\Lambda t}$,'''
replace_once(needle, corollary, "inverse resource-cost corollary")

# 4. Place the only quantitative plot directly after the exact fixed-moment no-go.
replace_once(
    "This does not say that a complete specified IRF is irrelevant. It rejects low-order moments as architecture-independent timing resources. "
    "Likewise, an FWHM or other scalar width is not a complete substitute for the timing law without additional shape assumptions.\n\n"
    "\\section{External temporal reference is an independent resource}",
    "This does not say that a complete specified IRF is irrelevant. It rejects low-order moments as architecture-independent timing resources. "
    "Likewise, an FWHM or other scalar width is not a complete substitute for the timing law without additional shape assumptions.\n\n"
    "\\input{figure_jitter_no_go}\n\n"
    "\\section{External temporal reference is an independent resource}",
    "jitter-no-go figure insertion",
)

# 5. Add one sentence to the Discussion highlighting the operational inverse theorem.
replace_once(
    "The capture-weighted local hazard capacity $\\Hcap$ is a microscopic sufficient resource satisfying $\\Rtwo\\le\\Hcap$. "
    "Stationary activity and entropy production do not generally control these local timing resources",
    "The capture-weighted local hazard capacity $\\Hcap$ is a microscopic sufficient resource satisfying $\\Rtwo\\le\\Hcap$. "
    "Equivalently, preserving absolute average information fraction $q$ over ordinary-frequency half-band $B$ requires the minimum cost $\\Hcap\\ge4Bq$. "
    "Stationary activity and entropy production do not generally control these local timing resources",
    "discussion resource-cost sentence",
)

DST.write_text(text, encoding="utf-8")
print(f"Generated {DST.name} from {SRC.name}")
