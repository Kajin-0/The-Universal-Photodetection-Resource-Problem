#!/usr/bin/env python3
from pathlib import Path

HERE = Path(__file__).resolve().parent
MAIN_IN = HERE / "dynamical_rank_boundary_implementation_cost_draft.tex"
MAIN_OUT = HERE / "dynamical_rank_boundary_implementation_cost_d2.tex"
SUPP_IN = HERE / "dynamical_rank_boundary_implementation_cost_supplement.tex"
SUPP_OUT = HERE / "dynamical_rank_boundary_implementation_cost_supplement_d2.tex"


def replace_once(text: str, old: str, new: str, label: str) -> str:
    n = text.count(old)
    if n != 1:
        raise RuntimeError(f"{label}: expected one match, found {n}")
    return text.replace(old, new, 1)


def main() -> None:
    main_text = MAIN_IN.read_text(encoding="utf-8")

    main_text = replace_once(
        main_text,
        "We derive an exact kernel-curvature identity for arbitrary smooth unitary dilations and prove that the minimum implementation cost is one half of the prescribed kernel-curvature trace.",
        "We derive an exact kernel-curvature identity for unitary dilations with finite state-weighted quadratic generator cost and prove that the minimum implementation cost is one half of the prescribed kernel-curvature trace.",
        "abstract implementation class",
    )

    old_impl = r"""A unitary implementation may use an arbitrary ancillary/controller Hilbert space $E$ and a global baseline $\Omegazero$ with $\Tr_E\Omegazero=\rhozero$. For tangent generators $K_j=K_j^\dagger$ of the global unitary family at the origin, define the state-weighted quadratic coupling cost
\begin{equation}
 \Vimpl:=\sum_j \Var_{\Omegazero}(K_j).
 \label{eq:Vdef}
\end{equation}
This is a local implementation-strength functional. It is not identified with thermodynamic work, battery depletion, switching work, or reset cost."""
    new_impl = r"""A unitary implementation may use an arbitrary ancillary/controller Hilbert space $E$ and a global baseline $\Omegazero$ with $\Tr_E\Omegazero=\rhozero$. For each coordinate let $K_j=K_j^\dagger$ be the self-adjoint tangent generator on the baseline domain. We require finite second moments $\Tr(\Omegazero K_j^2)<\infty$ and a reduced state family that is trace-norm $C^2$ at the origin. For bounded generators this is the usual operator expansion $\partial_jU(0)=-iK_j$; for the unbounded direct-sum construction below the derivatives are understood statewise, with trace-norm differentiation justified explicitly in the Supplemental Material. Define the state-weighted quadratic coupling cost
\begin{equation}
 \Vimpl:=\sum_j \Var_{\Omegazero}(K_j).
 \label{eq:Vdef}
\end{equation}
This is a local implementation-strength functional. It is not identified with thermodynamic work, battery depletion, switching work, or reset cost."""
    main_text = replace_once(main_text, old_impl, new_impl, "implementation definition")

    old_prop = r"""\begin{proposition}[Unitary kernel-curvature identity]
Let $\Omega(\bm\theta)=U(\bm\theta)\Omegazero U(\bm\theta)^\dagger$ be a smooth unitary implementation with $U(0)=I$ and $\partial_jU(0)=-iK_j$. If $\Tr_E\Omegazero=\rhozero$ and $Q\rhozero Q=0$, then"""
    new_prop = r"""\begin{proposition}[Unitary kernel-curvature identity]
Let $\Omega(\bm\theta)=U(\bm\theta)\Omegazero U(\bm\theta)^\dagger$ be an implementation in the finite-cost class above. If $\Tr_E\Omegazero=\rhozero$ and $Q\rhozero Q=0$, then, for bounded generators and by quadratic-form approximation for the finite-second-moment extension,"""
    main_text = replace_once(main_text, old_prop, new_prop, "kernel proposition")

    old_thm = r"""Let $\rhozero$ be a rank-deficient density operator and let $D_j$ satisfy Eq.~\eqref{eq:pureboundary}. Assume either finite dimension or, in separable infinite dimension, the Hilbert--Schmidt regularity in Eq.~\eqref{eq:CminHS}. Let $\Cker$ be positive trace class and satisfy the feasibility condition $\Cker\succeq\Cmin$. Among all smooth unitary dilations that realize the target first derivatives $D_j$ and the prescribed kernel Hessian contraction $\Cker$,"""
    new_thm = r"""Let $\rhozero$ be rank deficient, and let $D_j$ satisfy Eq.~\eqref{eq:pureboundary}. In separable infinite dimension assume the Hilbert--Schmidt regularity in Eq.~\eqref{eq:CminHS}. Let $\Cker$ be positive trace class with $\Cker\succeq\Cmin$. Among all finite-cost unitary dilations whose reduced families are trace-norm $C^2$ at the origin and that realize the derivatives $D_j$ and kernel Hessian contraction $\Cker$,"""
    main_text = replace_once(main_text, old_thm, new_thm, "central theorem assumptions")

    old_energy = r"""This remains true for separable infinite-dimensional targets with unbounded occupied target-energy support and for stationary excess curvature in target-energy sectors unoccupied at baseline."""
    new_energy = r"""This remains true for separable infinite-dimensional targets with unbounded occupied target-energy support and for stationary excess curvature in target-energy sectors unoccupied at baseline. In that case $U(\bm\theta)$ is a strongly continuous blockwise unitary family; smoothness asserted here refers to the implemented global/reduced state in trace norm on the finite-cost baseline."""
    main_text = replace_once(main_text, old_energy, new_energy, "energy theorem topology")

    MAIN_OUT.write_text(main_text, encoding="utf-8")

    supp = SUPP_IN.read_text(encoding="utf-8")
    old_start = r"""Let $\Omega(\bm\theta)=U(\bm\theta)\Omegazero U(\bm\theta)^\dagger$, with $U(0)=I$ and $\partial_jU(0)=-iK_j$, $K_j=K_j^\dagger$. Write the one-coordinate expansion"""
    new_start = r"""First take a bounded self-adjoint tangent generator $K$. Let $\Omega(\bm\theta)=U(\bm\theta)\Omegazero U(\bm\theta)^\dagger$, with $U(0)=I$ and $\partial_jU(0)=-iK_j$. Write the one-coordinate expansion"""
    supp = replace_once(supp, old_start, new_start, "supp bounded-generator start")

    old_after = r"""This argument also shows why the identity is independent of the second derivative of the unitary curve.

For several coordinates, Eq.~\eqref{eq:sup-kernelidentity} applies to each diagonal second derivative. Contracting with a positive physical parameter metric after a linear coordinate transformation gives the corresponding metric-covariant form."""
    new_after = r"""This argument also shows why the identity is independent of the second derivative of the unitary curve. For an unbounded self-adjoint generator with finite baseline second moment, apply the same identity to bounded spectral truncations of $K$ and pass to the state-weighted quadratic-form limit. The energy-conserving direct-sum construction below is treated more directly by differentiating its trace-class branch series.

For several coordinates, Eq.~\eqref{eq:sup-kernelidentity} applies to each diagonal second derivative. Contracting with a positive physical parameter metric after a linear coordinate transformation gives the corresponding metric-covariant form."""
    supp = replace_once(supp, old_after, new_after, "supp unbounded extension")

    supp = replace_once(
        supp,
        r"\section{Repaired infinite-dimensional energy-conserving construction}",
        r"\section{Energy-conserving infinite-dimensional construction}",
        "long supplement heading",
    )
    supp = replace_once(
        supp,
        r"\section{Trace-norm $C^2$ control of the direct-sum family}",
        r"\section{Trace-norm second-order control of the direct-sum family}",
        "bookmark-safe supplement heading",
    )
    SUPP_OUT.write_text(supp, encoding="utf-8")

    print(f"generated {MAIN_OUT.name}")
    print(f"generated {SUPP_OUT.name}")


if __name__ == "__main__":
    main()
