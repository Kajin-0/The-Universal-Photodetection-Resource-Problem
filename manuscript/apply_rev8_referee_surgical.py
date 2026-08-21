#!/usr/bin/env python3
from pathlib import Path

main = Path("event_resource_theorem_rev7.tex").read_text(encoding="utf-8")
app = Path("appendix_rare_fast_counterexample_rev7.tex").read_text(encoding="utf-8")

old = r"Assume now that every $\mu_m$ has a square-integrable density $f_m(t)$. Define"
new = r"Assume now that every $\mu_m$ has a square-integrable density $f_m(t)$. The hierarchy branches at this regularity assumption: the finite-area resources $\Rtwo$, $B_{\rm FI}$, and $\Hcap$ apply to the absolutely continuous square-integrable timing class, whereas atomic or more singular timing measures are governed first by the Wiener residue result above and need not possess a finite Fisher spectral area.\n\nDefine"
assert main.count(old) == 1
main = main.replace(old, new, 1)

old = r"with stationary forward optical traffic $f=u\pi_0$ and reverse traffic $r=d\pi_1$. Assume $f\ge r$, useful throughput $f\ge f_*>0$, total dimensionless entropy-production rate $\sigma_{\rm tot}\le\Sigma$, and stationary one-way activity $\mathcal A_{\rm tot}\le\mathcal A$."
new = old + r"\nHere one-way activity means the total stationary directed jump traffic\n\begin{equation}\n\boxed{\mathcal A_{\rm tot}\equiv\sum_x\pi_x\sum_{y\ne x}W_{yx},}\n\label{eq:activityDef}\n\end{equation}\nso each directed jump is counted once; this fixes the otherwise possible factor-of-two convention."
assert main.count(old) == 1
main = main.replace(old, new, 1)

old = r"If $\lambda_1$ is the total first-exit rate from state 1, activity gives"
new = r"If $\lambda_1$ is the total first-exit rate from state 1, the state-1 contribution to Eq.~\eqref{eq:activityDef} gives"
assert main.count(old) == 1
main = main.replace(old, new, 1)

assert main.count(r"\input{appendix_rare_fast_counterexample_rev7}") == 1
main = main.replace(r"\input{appendix_rare_fast_counterexample_rev7}", r"\input{appendix_rare_fast_counterexample_rev8}", 1)

old = r"where $a,b,c,q,p,s>0$ are fixed and $R\to\infty$.  The optical rate ratio $a/b$ is independent of $R$, so a fixed optical detailed-balance ratio does not prevent the scaling."
new = r"where $a,b,c,q,p,s>0$ are fixed, satisfy\n\begin{equation}\n\boxed{acp\ge bqs,}\n\label{eq:rareOrientationCondition}\n\end{equation}\nand $R\to\infty$.  The optical rate ratio $a/b$ is independent of $R$, so a fixed optical detailed-balance ratio does not prevent the scaling. Strict inequality in Eq.~\eqref{eq:rareOrientationCondition} may be chosen if a strictly forward-biased optical edge is desired."
assert app.count(old) == 1
app = app.replace(old, new, 1)

old = r"The useful forward optical traffic is likewise finite and nonzero:\n\begin{equation}\nf_R=aR\pi_0\n\longrightarrow\frac{aA_0}{D}>0.\n\end{equation}\n\nNow condition on an optical capture that places the detector in state $1$."
new = r"The useful forward optical traffic is likewise finite and nonzero:\n\begin{equation}\nf_R=aR\pi_0\n\longrightarrow\frac{aA_0}{D}>0.\n\end{equation}\nThe reverse optical traffic is $r_R=bR\pi_1$. For every $R>0$,\n\begin{align}\nf_R-r_R\n&=\frac{R(aA_0-bA_1)}{RD+E}\\\n&=\frac{R(acp-bqs)}{RD+E}\ge0,\n\label{eq:rareOrientationProof}\n\end{align}\nso the family lies exactly in the $f_R\ge r_R$ sector assumed in Sec.~\ref{sec:thermo}, not merely asymptotically. The inequality is strict when $acp>bqs$.\n\nNow condition on an optical capture that places the detector in state $1$."
assert app.count(old) == 1
app = app.replace(old, new, 1)

assert main.count("eq:activityDef") == 2
assert app.count(r"acp\ge bqs") == 2

Path("event_resource_theorem_rev8.tex").write_text(main, encoding="utf-8")
Path("appendix_rare_fast_counterexample_rev8.tex").write_text(app, encoding="utf-8")
print("generated Rev8 surgical repair source")
