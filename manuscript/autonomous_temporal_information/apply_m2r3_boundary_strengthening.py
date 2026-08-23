#!/usr/bin/env python3
"""Generate M2R3 from the cleaned M2R2 sources.

R3 addresses the remaining adversarial boundary-estimation criticism without
changing the established survival or synthesis coefficients:
1. make the scalar traces coordinate-covariant by carrying the physical
   quadrature metric under arbitrary invertible linear reparameterizations;
2. add a clean pure-boundary SLD-QFI action corollary;
3. show by spectator curvature why the full rank-changing Bures metric is not
   determined by the selected first-order temporal mode alone.
"""
from pathlib import Path

HERE = Path(__file__).resolve().parent
MAIN_IN = HERE / "autonomous_temporal_resource_law_m2r2.tex"
MAIN_OUT = HERE / "autonomous_temporal_resource_law_m2r3.tex"
SUPP_IN = HERE / "autonomous_temporal_resource_law_supplement_m2r2.tex"
SUPP_OUT = HERE / "autonomous_temporal_resource_law_supplement_m2r3.tex"

OLD_COORD = r"""The fixed quadrature normalization is nevertheless not an arbitrary coordinate artifact. Orthogonal rotations of the cosine--sine plane leave all traces used below unchanged. Under a common scalar rescaling $(x',y')=s(x,y)$, one has $F^{\rm tan}\mapsto s^{-2}F^{\rm tan}$ and $\Rlin\mapsto s\Rlin$, while every quadratic synthesis action defined from the parameter Hessian scales as $s^{-2}$. Hence $\Rlin^2\Tr F^{\rm tan}$ and the synthesis-action/Fisher ratios are invariant under orthogonal rotations and common scalar rescalings, although no invariance under arbitrary anisotropic reparameterizations is asserted."""

NEW_COORD = r"""The fixed quadrature normalization is nevertheless not an arbitrary coordinate artifact. More generally, the scalar traces are contractions with the physical Euclidean metric on the cosine--sine amplitude plane. Under an invertible linear reparameterization $\boldsymbol\theta'=M\boldsymbol\theta$, the Fisher tensor and parameter metric transform as $F'=M^{-T}FM^{-1}$ and $g'=M^{-T}gM^{-1}$, so $\operatorname{tr}(g'^{-1}F')=\operatorname{tr}(g^{-1}F)$. The Hessian contraction $g^{ij}\partial_i\partial_j\rho$ transforms in the same way for linear coordinate changes. The formulas below use the canonical physical quadratures for which $g=I_2$. Orthogonal rotations and common scalar rescalings are therefore immediate special cases; assigning the identity metric again after an anisotropic rescaling is a change of physical parameter normalization, not a mere relabeling of coordinates."""

QFI_SCOPE = r"""
\subsection{Boundary SLD-QFI and the nonregular remainder}
\label{sec:boundary-qfi}

The common-record inequalities above use the baseline score-Fisher block $F^{\rm tan}$, but support-to-kernel quantum tangent information is not left uncharged. Let $H^{\rm SLD}$ denote the standard SLD-QFI matrix of the two first derivatives at the baseline. For a pure-boundary tangent $A=X+Y^\dagger$, the finite-dimensional SLD formula gives
\begin{equation}
\boxed{\Tr H^{\rm SLD}=2(J_++J_-).}
\label{eq:sld-pure-boundary}
\end{equation}
Combining this identity with the same two local endpoint-curvature inequalities used in the autonomous action theorem yields the clean quantum-statistical corollary
\begin{equation}
\boxed{
\Aact_C^{(2)}+\Aact_S^{(2)}
\ge\frac{\hbar\nu}{4}\Tr H^{\rm SLD}.
}
\label{eq:sld-action-main}
\end{equation}
The coefficient is sharp in both fixed-total-energy constructions. In the one-sided model the common-record score-Fisher coefficient remains twice as strong because one fixed measurement cannot simultaneously attain both SLD quadratures; the quantum-statistical action coefficient itself stays $\hbar\nu/4$.

What is deliberately not assigned to the selected first-order temporal mode is arbitrary independent second-order boundary distinguishability. At a rank-changing point, four times the Bures metric obeys \cite{Safranek2017}
\begin{equation}
H_c=H^{\rm SLD}+2\sum_{\lambda_k=0}\mathcal H_k,
\label{eq:bures-rank-correction}
\end{equation}
where $\mathcal H_k$ is the parameter Hessian of a zero eigenvalue. The second term is path curvature, not first-derivative tangent data. Indeed, one may add population $\alpha(x^2+y^2)$ to an otherwise unused empty spectator level, subtract the same amount from an occupied support level, and choose the spectator outside the temporal endpoint-incidence support. This leaves $A$, $F^{\rm tan}$, $H^{\rm SLD}$, and the mode-specific endpoint action unchanged, while increasing $\Tr H_c$ by $8\alpha$. Hence no finite bound on the full boundary Bures metric can depend only on the selected first-order temporal tangent and a cost that prices only its endpoint sectors. A full Bures bound must additionally charge all second-order parameter curvature. The Supplemental Material gives the SLD calculation and spectator construction explicitly.

""".strip()


def main() -> None:
    text = MAIN_IN.read_text(encoding="utf-8")
    if text.count(OLD_COORD) != 1:
        raise RuntimeError(f"expected one R2 coordinate paragraph, found {text.count(OLD_COORD)}")
    text = text.replace(OLD_COORD, NEW_COORD, 1)

    anchor = r"\subsection{Fixed-total-energy sharpness}"
    if text.count(anchor) != 1:
        raise RuntimeError(f"expected one fixed-shell anchor, found {text.count(anchor)}")
    text = text.replace(anchor, QFI_SCOPE + "\n\n" + anchor, 1)
    MAIN_OUT.write_text(text, encoding="utf-8")

    supp = SUPP_IN.read_text(encoding="utf-8")
    if "boundary_qfi_nonregular_scope.tex" not in supp:
        raise RuntimeError("R3 supplement input for boundary QFI proof is missing")
    SUPP_OUT.write_text(supp, encoding="utf-8")

    print(f"generated {MAIN_OUT.name} and {SUPP_OUT.name}")


if __name__ == "__main__":
    main()
