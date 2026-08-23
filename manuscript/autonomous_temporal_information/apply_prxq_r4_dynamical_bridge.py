#!/usr/bin/env python3
"""Generate a narrow PRX Quantum R4 bridge revision from the frozen R3 paper.

R3 remains the scientific baseline. R4 changes only the late scope/discussion
layer to connect the kinematic boundary synthesis action to the separately
proved unitary-coupling variational theorem. No R3 theorem or proof is changed.
"""
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "autonomous_temporal_resource_law_prxq_r3.tex"
OUT = HERE / "autonomous_temporal_resource_law_prxq_r4.tex"

OLD_SCOPE = r"""The present resource is different in scope. Equations~\eqref{eq:dual-survival} and \eqref{eq:dual-action-bilateral} concern a frequency-resolved relational mode that can be globally time-translation symmetric. The finite-radius law charges pre-existing local spectral survival. At a rank-changing boundary, an entropy-type shared-asymmetry resource is generally nonanalytic in amplitude, whereas the positive endpoint-incidence action supplies a finite quadratic necessary coefficient. The action is kinematic: it is computed from the local Hessian of the encoded state family. We do not claim that it equals the total physical energy required to synthesize that family dynamically."""

NEW_SCOPE = r"""The present resource is different in scope. Equations~\eqref{eq:dual-survival} and \eqref{eq:dual-action-bilateral} concern a frequency-resolved relational mode that can be globally time-translation symmetric. The finite-radius law charges pre-existing local spectral survival. At a rank-changing boundary, an entropy-type shared-asymmetry resource is generally nonanalytic in amplitude, whereas the positive endpoint-incidence action supplies a finite quadratic necessary coefficient. Its definition remains kinematic: it is computed from the local Hessian of the encoded state family.

A separate companion unitary-dilation variational analysis asks whether this prescribed boundary curvature has a minimum implementation strength. For a feasible metric-contracted target-kernel Hessian $C$, that problem has the exact solution
\begin{equation}
\boxed{
V_{\min}(C)=\frac12\Tr C,
\qquad
\Aact_{\rm ex}^{(2)}=\hbar\nu\,V_{\min}
}
\label{eq:dynamical-bridge}
\end{equation}
in the clean single-gap autonomous specialization \cite{CompanionUnitaryCost2026}. Thus the boundary action used here is kinematic in definition but admits an exact minimum-coupling interpretation within that implementation class. This companion result is not used in any proof above. It does not identify the action with thermodynamic work, peak or operator-norm coupling, controller bandwidth, ancilla dimension, or the optimum attainable with an externally fixed controller spectrum."""

OLD_DISCUSSION = r"""The result is not a universal implementation-energy theorem and not a replacement for asymmetry resource theory. It is a local, frequency-resolved necessary-resource theorem for finite-dimensional encoded relative temporal information. Important open problems remain: deriving a dynamical implementation cost that produces the kinematic action, extending the sharp spectral sum to controlled continua, and determining whether covariance-changing Gaussian families require an additional resource beyond endpoint curvature."""

NEW_DISCUSSION = r"""The result is not a universal implementation-energy theorem and not a replacement for asymmetry resource theory. It is a local, frequency-resolved necessary-resource theorem for finite-dimensional encoded relative temporal information. The companion variational result closes one question left open by the kinematic framework: within its unitary-dilation implementation class, the clean endpoint action is exactly $\hbar\nu$ times the least state-weighted quadratic coupling required to realize the prescribed rank-changing curvature. Important open problems remain: extending the sharp spectral sum to controlled continua and determining whether covariance-changing Gaussian families require an additional resource beyond endpoint curvature."""


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected one match, found {count}")
    return text.replace(old, new, 1)


def main() -> None:
    text = SRC.read_text(encoding="utf-8")
    text = replace_once(text, OLD_SCOPE, NEW_SCOPE, "late scope bridge")
    text = replace_once(text, OLD_DISCUSSION, NEW_DISCUSSION, "discussion bridge")
    OUT.write_text(text, encoding="utf-8")
    print(f"generated {OUT.name} from frozen {SRC.name}")


if __name__ == "__main__":
    main()
