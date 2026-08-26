from __future__ import annotations

FIGURE_BLOCKS = [
    (
        r"\subsection{Ideal photon timestamps and independent timing jitter}",
        r"""\begin{figure*}[t]
\centering
\includegraphics[width=\textwidth]{figures/generated/fig1_same_specs_different_information.pdf}
\caption{Same conventional specifications, different temporal information in a standard illustrative detector model. (a) The two detectors share the same single-pole signal transfer $|H(f)|^2=[1+(f/f_c)^2]^{-1}$ and therefore the same responsivity $3$-dB frequency. (b) Detector A has white output noise while detector B has a low-frequency Lorentzian excess term rolling toward a lower white floor; both have the same dc noise and hence the same dc NEP. (c) Their normalized single-quadrature Fisher-information spectra nevertheless differ: at $f=f_c$, $J_B/J_A=13/3$, while detector B remains above one half of its dc Fisher information until $f/f_c=2.9703$. This panel is an explicit specification-incompleteness example, not a new detector theorem.}
\label{fig:spec_incompleteness}
\end{figure*}""",
    ),
    (
        r"\section{Spectral support: from survival to synthesis}",
        r"""\begin{figure*}[t]
\centering
\includegraphics[width=\textwidth]{figures/generated/fig2_same_saturation_different_timestamps.pdf}
\caption{Frozen companion-memory benchmark: identical conventional recovery summaries need not determine timestamp information. (a) Recovery laws A and B have the same mean $m$, variance $m^2/4$, and coefficient of variation $1/2$. (b) Consequently they have exactly the same generalized Type-II saturation curve $rm=\rho e^{-\rho}$ with $\rho=\lambda m$. (c) At the common maximum $\rho=1$, the registered-event pair correlations at lag $0.75m$ are nevertheless $g_A^{(2)}=0.727496$ and $g_B^{(2)}=0.318872$. (d) Even the one-bit statistic $Z=\mathbf{1}\{D\le0.4m\}$ has source-normalized Fisher witness $G_{Z,A}=0$ but $G_{Z,B}=0.00443520$. The timestamp results are imported from the companion random-time analysis; the present paper uses them as an operational characterization benchmark rather than claiming a new dead-time theorem.}
\label{fig:memory_benchmark}
\end{figure*}""",
    ),
    (
        r"\section{Standard Hamiltonian implementation benchmark}",
        r"""\begin{figure*}[t]
\centering
\includegraphics[width=\textwidth]{figures/generated/fig3_support_survival_synthesis_crossover.pdf}
\caption{Support-controlled survival-to-synthesis crossover for the visualization path $a_p=1-p$, $\sigma_p=0$, and $q=\kappa=1$. (a) A nonzero sideband seed lies in the baseline support; removing the seed makes the selected sideband a kernel direction. (b) The affine physical disks for $p=0.15$, $0.05$, and $0.01$ shrink with $R_{\rm lin}=0.5101$, $0.2422$, and $0.1015$, respectively. (c) The finite-seed quantity $4p/R_{\rm lin}^2=4(1-2p)^2/(1-p)$ tends to the zero-seed sideband-population curvature $\Delta P_s(0)=4$. (d) A noncircular test obtains $R_{\rm lin}$ from baseline/tangent tomography, $\Delta P_s(0)$ from an independent zero-seed quadratic fit, and $\operatorname{Tr}F$ from a separate phase-sensitive likelihood. The theorem in the text is broader than the plotted special path and permits the stated class of stationary inert spectators with general $q$ and $\kappa$.}
\label{fig:support_crossover}
\end{figure*}""",
    ),
    (
        r"\section{What would falsify the framework?}",
        r"""\begin{figure*}[t]
\centering
\includegraphics[width=\textwidth]{figures/generated/fig4_resonant_implementation_falsification.pdf}
\caption{Standard equal-frequency resonant implementation benchmark of the frozen companion unitary-coupling theorem. (a) For $H_0=\hbar\nu(N_C+N_S)$, the states $|2,0\rangle$, $|1,1\rangle$, and $|0,2\rangle$ occupy one fixed total-bare-energy shell and are connected by ordinary exchange coupling. (b) Independent coupling-angle and endpoint-curvature calibrations coincide on $V_{\rm impl}=\operatorname{Tr}C/2=8(gt)^2$, with $\mathcal A_{\rm ex}^{(2)}/(\hbar\nu)=V_{\min}$. (c) A failure should first be assigned to the appropriate level: implementation/model failure (Level I), failure of the ideal benchmark to saturate the equality (Level III), or, only after the theorem hypotheses are independently verified, a lower-bound challenge with $V_{\rm impl}<\operatorname{Tr}C/2$ (Level II). The benchmark is not thermodynamic work and is not claimed as new beam-splitter physics.}
\label{fig:resonant_benchmark}
\end{figure*}""",
    ),
]

EXPECTED_FIGURE_PATHS = [
    "figures/generated/fig1_same_specs_different_information.pdf",
    "figures/generated/fig2_same_saturation_different_timestamps.pdf",
    "figures/generated/fig3_support_survival_synthesis_crossover.pdf",
    "figures/generated/fig4_resonant_implementation_falsification.pdf",
]

EXPECTED_LABELS = [
    "fig:spec_incompleteness",
    "fig:memory_benchmark",
    "fig:support_crossover",
    "fig:resonant_benchmark",
]
