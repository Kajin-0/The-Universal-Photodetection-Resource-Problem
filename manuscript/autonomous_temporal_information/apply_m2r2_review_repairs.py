#!/usr/bin/env python3
"""Generate the M2R2 audited manuscript and supplement from M2R1.

R2 implements the four substantive repairs from the external adversarial review:
1. distinguish the baseline score-Fisher tangent block at rank-changing points;
2. state orthogonal/isotropic reparameterization behavior;
3. compress the arbitrary-support mixed theorem in the main text;
4. keep the detailed branch formulas in Supplemental Material.

No research theorem or coefficient is changed.
"""
from __future__ import annotations

import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
MAIN_IN = HERE / "autonomous_temporal_resource_law_m2r1.tex"
MAIN_OUT = HERE / "autonomous_temporal_resource_law_m2r2.tex"
SUPP_IN = HERE / "autonomous_temporal_resource_law_supplement_m2r1.tex"
SUPP_OUT = HERE / "autonomous_temporal_resource_law_supplement_m2r2.tex"

BOUNDARY_SCOPE = r"""
At a rank-changing point Eq.~\eqref{eq:FItrace} is a \emph{baseline score-Fisher tangent block}, which we denote by $F^{\rm tan}$. Outcomes with $p_y(0)=0$ are absent from this first-order score sum even if they acquire probability at order $x^2+y^2$. Consequently $F^{\rm tan}$ need not coincide there with a continuous Bures metric or with directional limiting classical or quantum Fisher information obtained from such newly appearing outcomes \cite{Safranek2017}. The boundary theorems below constrain precisely this regular first-order two-quadrature tangent information; they do not claim to bound every nonregular second-order distinguishability effect. At regular points $F^{\rm tan}$ is the ordinary classical Fisher block.

The fixed quadrature normalization is nevertheless not an arbitrary coordinate artifact. Orthogonal rotations of the cosine--sine plane leave all traces used below unchanged. Under a common scalar rescaling $(x',y')=s(x,y)$, one has $F^{\rm tan}\mapsto s^{-2}F^{\rm tan}$ and $\Rlin\mapsto s\Rlin$, while every quadratic synthesis action defined from the parameter Hessian scales as $s^{-2}$. Hence $\Rlin^2\Tr F^{\rm tan}$ and the synthesis-action/Fisher ratios are invariant under orthogonal rotations and common scalar rescalings, although no invariance under arbitrary anisotropic reparameterizations is asserted.
""".strip()

MIXED_SECTION = r"""\section{Arbitrary coherent support: mixed survival and synthesis}
\label{sec:mixed}

The clean interior and boundary limits above are not the whole story: a coherent rank-deficient baseline can have both a support-preserving component and newly synthesized kernel components, while its support need not commute with the local Hamiltonians. Let $P=\supp\rhozero$, $Q=\id-P$, and decompose the exact exchange tangent as
\begin{equation}
B=PA_\nu P,\qquad K_+=QA_\nu P,\qquad K_-=QA_\nu^\dagger P,
\label{eq:mixed-decomp}
\end{equation}
where two-sided first-order physicality gives $QA_\nu Q=0$. Define
\begin{equation}
Z_+=K_+\rhozero^+K_+^\dagger,\qquad
Z_-=K_-\rhozero^+K_-^\dagger.
\end{equation}
The support-preserving term is bounded by two orientation-dependent scalar survival ceilings $a_\pm$, obtained by shorting the participating endpoint compressions onto the information-bearing ranges of $B\rhozero^+B^\dagger$ and $B^\dagger\rhozero^+B$. A branch exists only when the relevant shorting constant is positive; the complete definitions and all degenerate branches are given in the Supplemental Material \cite{AndersonTrapp1975}.

The newly synthesized components are charged once by the canonical positive endpoint-incidence operator
\begin{equation}
G_{\mathrm{ex}}=2\hbar\nu\,Q(\Pi_{\mathrm{out}}+\Pi_{\mathrm{in}})Q,
\quad
\Pi_{\mathrm{out}}=\supp(A_\nu A_\nu^\dagger),\quad
\Pi_{\mathrm{in}}=\supp(A_\nu^\dagger A_\nu),
\label{eq:Gex}
\end{equation}
through
\begin{equation}
\Aact_{\mathrm{ex}}^{(2)}=\frac14\Tr(G_{\mathrm{ex}}C_\Delta),
\qquad
C_\Delta=Q(\partial_x^2+\partial_y^2)\rho(0)Q,
\qquad e=4\Aact_{\mathrm{ex}}^{(2)}.
\label{eq:Aex}
\end{equation}
For each nonzero synthesized orientation let $g_\pm$ be the minimum eigenvalue of the compression of $G_{\rm ex}$ to $\supp Z_\pm$. If a nonzero orientation has $g_\pm=0$, this scalar action cannot control that direction and the operator-valued curvature must be retained.

For $a,e\ge0$ and $p,q>0$, define
\begin{equation}
\Psi_a(e;p,q)=
\begin{cases}
(\sqrt a+\sqrt{e/q})^2,&e\le ap^2/q,\\[1mm]
(e+pa)(p^{-1}+q^{-1}),&e\ge ap^2/q.
\end{cases}
\label{eq:Psi}
\end{equation}

\begin{theorem}[Noncommuting autonomous mixed resource law]
\label{thm:mixed}
When both synthesized orientations are nonzero with $g_+,g_->0$, every finite-$N$ collective POVM obeys, for each available finite internal branch,
\begin{equation}
\boxed{
\frac{\Tr \Fcl_N}{N}
\le
\min\!\left\{
\Psi_{a_+}(e;g_+,g_-),
\Psi_{a_-}(e;g_-,g_+)
\right\},
}
\label{eq:mixed-master}
\end{equation}
where unavailable internal branches are omitted from the minimum. The corresponding one-sided, support-only, and zero-cost cases are stated explicitly in the Supplemental Material.
\end{theorem}

\emph{Proof core.} The measurement side is the two-orientation Minkowski bound
\begin{equation}
\sqrt{\frac{\Tr F^{\rm tan}_N}{N}}
\le
\min\!\left\{
\sqrt{J_B^++J_+}+\sqrt{J_-},
\sqrt{J_B^-+J_-}+\sqrt{J_+}
\right\}.
\end{equation}
Shorting supplies the available $a_\pm$ bounds, while second-order positivity and $G_{\rm ex}$ give the single budget $g_+J_++g_-J_-\le e$. Maximizing either Minkowski branch under that budget yields Eq.~\eqref{eq:Psi}. The detailed shorting constants, degenerate branches, and optimization are deferred to the Supplemental Material.

This technical completion preserves the clean physical limits: pure support survival reduces to the finite-radius law, one-sided pure-boundary synthesis recovers the $\hbar\nu/2$ autonomous coefficient, and bilateral pure-boundary synthesis recovers $\hbar\nu/4$. In the shared-kernel qutrit benchmark the resource ceiling is $12$, compared with SLD-QFI trace $43/4$ and exact common-record tangent-Fisher supremum $55/8$, separating physical resource, quantum-statistical geometry, and measurement accessibility.

"""


def generate_main() -> None:
    text = MAIN_IN.read_text(encoding="utf-8")
    old_macro = r"\newcommand{\Fcl}{F}"
    if text.count(old_macro) != 1:
        raise RuntimeError("expected one Fcl macro")
    text = text.replace(old_macro, r"\newcommand{\Fcl}{F^{\mathrm{tan}}}", 1)

    anchor = "For $N$ independently encoded copies, $\\Fcl_N$ denotes the Fisher matrix of an arbitrary joint POVM; no separability or asymptotic assumption is imposed unless stated explicitly. For multiple modes, the coordinate space is the direct sum of these cosine--sine planes with its Euclidean metric. Accordingly, the Fisher and Hessian traces below refer to this fixed physical quadrature normalization; invariance under arbitrary anisotropic reparameterizations is not claimed."
    if text.count(anchor) != 1:
        raise RuntimeError("quadrature-metric anchor changed")
    text = text.replace(anchor, anchor + "\n\n" + BOUNDARY_SCOPE, 1)

    pattern = re.compile(
        r"\\section\{Arbitrary coherent support: mixed survival and synthesis\}.*?(?=\\section\{Multi-gap spectral-action sum\})",
        flags=re.DOTALL,
    )
    text, n = pattern.subn(lambda _m: MIXED_SECTION, text, count=1)
    if n != 1:
        raise RuntimeError(f"expected one mixed section replacement, got {n}")

    MAIN_OUT.write_text(text, encoding="utf-8")
    print(f"generated {MAIN_OUT.name}")


def generate_supplement() -> None:
    text = SUPP_IN.read_text(encoding="utf-8")
    anchor = "This Supplemental Material gives self-contained proof cores for the resource statements used in the main text."
    note = (
        " Throughout the supplement, $F_N$ denotes the same baseline score-Fisher tangent block "
        "$F_N^{\\rm tan}$ defined in the main text; at rank-changing points it is not identified "
        "with directional limiting Fisher information from zero-baseline-probability outcomes."
    )
    if text.count(anchor) != 1:
        raise RuntimeError("supplement opening anchor changed")
    text = text.replace(anchor, anchor + note, 1)
    SUPP_OUT.write_text(text, encoding="utf-8")
    print(f"generated {SUPP_OUT.name}")


def main() -> None:
    generate_main()
    generate_supplement()


if __name__ == "__main__":
    main()
