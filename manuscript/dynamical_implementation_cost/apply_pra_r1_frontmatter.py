#!/usr/bin/env python3
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "dynamical_rank_boundary_implementation_cost_d2.tex"
OUT = HERE / "dynamical_rank_boundary_implementation_cost_pra_r1.tex"

NEW_TITLE = r"\title{Exact minimum unitary coupling cost of prescribed rank-changing quantum-state curvature}"

NEW_ABSTRACT = r"""\begin{abstract}
At a rank-changing boundary of quantum state space, a first-order tangent fixes only a minimum amount of second-order population that must enter the baseline-empty sector; additional positive curvature may be prescribed independently. We determine the least state-weighted quadratic coupling required to implement that complete local datum. For a prescribed feasible metric-contracted kernel Hessian $C$, every finite-cost unitary dilation obeys $V_{\min}=\tfrac12\operatorname{Tr}C$, and the bound is attained by combining the Bures-horizontal first-order motion with an orthogonal ancillary flag that realizes arbitrary excess curvature without changing the first derivative. Under stationary energy covariance, the same optimum is attainable with exact total-energy conservation and a semibounded ancillary Hamiltonian, including for separable infinite-dimensional targets with unbounded occupied energy support. For an autonomous temporal exchange at Bohr frequency $\nu$, the frequency-resolved endpoint synthesis action is exactly $\hbar\nu V_{\min}$. Thus nonzero implementation coupling can be required even when the total bare-energy distribution is unchanged. The result concerns a prescribed contraction of the kernel second-order curvature; it is neither a thermodynamic-work bound nor a new first-order quantum-Fisher variational principle.
\end{abstract}"""

OLD_INTRO = r"""Rank-deficient statistical models are nonregular: probability can enter outcomes that are empty at the baseline only at second order, and standard first-order likelihood geometry need not determine the boundary behavior \cite{Chernoff1954,Shapiro1985,SelfLiang1987,Safranek2017}. In quantum state space the positivity constraint adds an operator-valued restriction. If a baseline density operator $\rhozero$ has support projector $P$ and kernel projector $Q=I-P$, a pure-boundary first derivative has only support--kernel blocks. Positivity then forces a minimum positive kernel curvature, but a physical family may contain additional second-order population not fixed by the first derivative.

First-order purification and channel geometry are well developed. The Bures/SLD metric is a minimum purification metric \cite{BraunsteinCaves1994}, channel Fisher information admits fibre/Kraus-gauge formulations \cite{FujiwaraImai2008}, and purification-based bounds are central in noisy metrology \cite{EscherEtAl2011,DemkowiczKolodynskiGuta2012}. Covariant Stinespring dilation is likewise established \cite{Scutaru1979}. Our question is different: the positive second-order kernel population is specified independently, and we minimize the dynamical coupling needed to realize the resulting local state jet."""

NEW_INTRO = r"""At a rank-changing boundary, first-order distinguishability and second-order physical realizability separate. Probability may enter outcomes that are empty at the baseline only at second order, a generic source of nonregular statistical behavior \cite{Chernoff1954,Shapiro1985,SelfLiang1987}. For quantum states, positivity additionally constrains how support--kernel coherences may be completed by population in the kernel; rank changes also produce familiar subtleties in quantum-Fisher and Bures geometry \cite{Safranek2017}.

Recent work has analyzed the Riemannian curvature of the Bures metric itself near rank-changing density matrices, including conical singularities in higher-dimensional state spaces \cite{HuangEtAl2026}. That geometric curvature is distinct from the quantity prescribed here: $C$ is the metric-contracted second derivative of a particular state family projected into the baseline kernel.

The minimum cost of a \emph{first-order} quantum tangent is already part of established purification geometry. The Bures/SLD metric is obtained by minimizing purification motion \cite{BraunsteinCaves1994}; related fibre/Kraus-gauge formulations underlie channel Fisher information and noisy-metrology bounds \cite{FujiwaraImai2008,EscherEtAl2011,DemkowiczKolodynskiGuta2012}. Covariant Stinespring dilation is likewise established \cite{Scutaru1979}. These results do not determine the cost of an independently prescribed, nonminimal positive second-order population in the target kernel.

Here we solve that local second-order implementation problem exactly. If $C$ denotes the prescribed physical-metric contraction of the target kernel Hessian, positivity requires $C\succeq C_{\min}$, where $C_{\min}$ is fixed by the first derivative. We prove that every finite-cost unitary dilation obeys $V_{\rm impl}\ge\tfrac12\Tr C$ and construct a dilation attaining equality for every feasible $C$. The construction separates the horizontal first-order motion from an ancillary flag carrying precisely the excess $C-C_{\min}$. Exact total-energy conservation does not increase the optimum: a semibounded conserving dilation exists even in separable infinite dimension with unbounded occupied target energies. An autonomous temporal exchange then converts the general result into the spectral identity $\mathcal A_{\rm ex}^{(2)}=\hbar\nu V_{\min}$."""

OLD_ACK = r"""\begin{acknowledgments}
Acknowledgments omitted for anonymous review.
\end{acknowledgments}

\bibliography{references}"""

NEW_ACK = r"""\section*{AI-Assisted Research and Verification}
OpenAI ChatGPT (GPT-5.6-series models, including GPT-5.6 Sol) was used substantively during derivation exploration, adversarial algebra checks, literature organization, generation and debugging of internal numerical-validation code, and manuscript preparation. AI outputs were treated as provisional. The author directed the scientific questions and proof strategy, independently checked the resulting claims against explicit analytic derivations, constructive examples, numerical validators, and primary literature, and takes full responsibility for the content.

\begin{acknowledgments}
Acknowledgments omitted for anonymous review.
\end{acknowledgments}

\section*{Data Availability}
No empirical data were created or analyzed in this theoretical study. Internal numerical-validation scripts were used only to cross-check analytic identities and are not required to reproduce the reported results. The analytic results needed to support the conclusions are contained in the Article and Supplemental Material. The validation scripts are available from the author upon reasonable request.

\bibliography{references}"""


def replace_once(text: str, old: str, new: str, label: str) -> str:
    n = text.count(old)
    if n != 1:
        raise RuntimeError(f"{label}: expected one match, found {n}")
    return text.replace(old, new, 1)


def replace_environment(text: str, begin: str, end: str, new: str, label: str) -> str:
    i = text.find(begin)
    j = text.find(end, i + len(begin))
    if i < 0 or j < 0:
        raise RuntimeError(f"{label}: environment not found")
    j += len(end)
    if text.find(begin, j) >= 0:
        raise RuntimeError(f"{label}: multiple environments found")
    return text[:i] + new + text[j:]


def main() -> None:
    text = SRC.read_text(encoding="utf-8")
    title_start = text.find(r"\title{")
    title_end = text.find("}\n", title_start)
    if title_start < 0 or title_end < 0:
        raise RuntimeError("title not found")
    text = text[:title_start] + NEW_TITLE + text[title_end + 1:]
    text = replace_environment(text, r"\begin{abstract}", r"\end{abstract}", NEW_ABSTRACT, "abstract")
    text = replace_once(text, OLD_INTRO, NEW_INTRO, "introduction")
    text = replace_once(text, OLD_ACK, NEW_ACK, "AI disclosure/acknowledgments/data availability")
    OUT.write_text(text, encoding="utf-8")
    print(f"generated {OUT.name}")


if __name__ == "__main__":
    main()
