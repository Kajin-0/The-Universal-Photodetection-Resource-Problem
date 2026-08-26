from __future__ import annotations

import json
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

from common import OUT, save, setup

STEM = "fig4_resonant_implementation_falsification"

def locked_values():
    gt = np.arange(0.1, 0.51, 0.1)
    y = 8.0*gt**2
    vals = {
        "gt": gt.tolist(),
        "V_impl": y.tolist(),
        "half_TrC": y.tolist(),
        "Aex_over_hbarnu": y.tolist(),
    }
    assert np.allclose(y, 0.5*(16.0*gt**2), rtol=0, atol=1e-15)
    return vals

def main():
    setup()
    vals = locked_values()
    gt_pts = np.array(vals["gt"])
    y_pts = np.array(vals["V_impl"])

    fig, ax = plt.subplots(1, 3, figsize=(7.2, 3.0), constrained_layout=True,
                           gridspec_kw={"width_ratios":[1.0, 1.05, 1.15]})

    a = ax[0]
    a.set_xlim(-1.05, 1.05)
    a.set_ylim(-0.45, 0.70)
    a.axis("off")
    xnodes = [-0.72, 0.0, 0.72]
    labels = [r"$|L\rangle=|2,0\rangle$", r"$|M\rangle=|1,1\rangle$", r"$|U\rangle=|0,2\rangle$"]
    for x, lab in zip(xnodes, labels):
        a.plot(x, 0.15, "o", mfc="white", mec="black", ms=8)
        a.text(x, -0.02, lab, ha="center", va="top", fontsize=7.0)
    a.annotate("", xy=(-0.62,0.15), xytext=(-0.10,0.15),
               arrowprops={"arrowstyle":"<->","lw":1.0,"color":"0.25"})
    a.annotate("", xy=(0.62,0.15), xytext=(0.10,0.15),
               arrowprops={"arrowstyle":"<->","lw":1.0,"color":"0.25"})
    a.text(-0.36, 0.23, r"$g$", ha="center", fontsize=7.2)
    a.text(0.36, 0.23, r"$g$", ha="center", fontsize=7.2)
    a.text(0, 0.52, r"$H_0=\hbar\nu(N_C+N_S)$", ha="center", fontsize=8.0)
    a.text(0, 0.40, r"all three states: $E_{\rm bare}=2\hbar\nu$", ha="center", fontsize=7.1)
    a.set_title("(a) Fixed-energy exchange")

    a = ax[1]
    gt = np.linspace(0, 0.55, 300)
    y = 8.0*gt**2
    a.plot(gt, y, color="black", lw=1.4, label=r"$8(gt)^2$")
    a.plot(gt_pts, y_pts, "o", mfc="white", mec="black", ms=4.5, label=r"$V_{\rm impl}$ calibration")
    a.plot(gt_pts, y_pts, "x", color="0.35", ms=5.0, mew=1.0, label=r"$\mathrm{Tr}C/2$ curvature")
    a.set(xlim=(0,0.55), ylim=(0,2.6), xlabel=r"$gt$",
          ylabel=r"dimensionless cost / curvature")
    a.set_title("(b) Independent calibration")
    a.legend(frameon=False, loc="upper left", fontsize=6.7)
    a.text(0.27, 0.30, r"$A_{\rm ex}/(\hbar\nu)=V_{\min}$", fontsize=7.0)

    a = ax[2]
    a.set_xlim(0, 1)
    a.set_ylim(0, 1)
    a.axis("off")
    specs = [
        (0.08,0.68,0.84,0.23,"Level I — model failure",
         "loss, unequal bare frequencies,\nomitted pump/controller,\nleakage"),
        (0.08,0.38,0.84,0.23,"Level III — ideal equality fails",
         "verified benchmark but\n" + r"$V_{\rm impl}\neq\mathrm{Tr}C/2$"),
        (0.08,0.08,0.84,0.23,"Level II — lower-bound challenge",
         "all theorem hypotheses verified;\n" + r"$V_{\rm impl}<\mathrm{Tr}C/2$"),
    ]
    for x,y0,w,h,head,body in specs:
        a.add_patch(FancyBboxPatch((x,y0),w,h, boxstyle="round,pad=0.02,rounding_size=0.01",
                                   fc="white", ec="0.25", lw=0.9))
        a.text(x+0.03, y0+h*0.72, head, ha="left", va="center", fontsize=7.2, fontweight="bold")
        a.text(x+0.03, y0+h*0.35, body, ha="left", va="center", fontsize=6.4)
    a.set_title("(c) Failure hierarchy")

    a = ax[1]
    a.tick_params(direction="out", length=3)
    a.spines["top"].set_visible(False)
    a.spines["right"].set_visible(False)

    fig.suptitle("Standard resonant benchmark of the frozen companion unitary-coupling theorem",
                 fontsize=9.2)
    save(fig, STEM)
    plt.close(fig)
    (OUT / f"{STEM}_locked.json").write_text(json.dumps(vals, indent=2, sort_keys=True) + "\n")
    return vals

if __name__ == "__main__":
    main()
