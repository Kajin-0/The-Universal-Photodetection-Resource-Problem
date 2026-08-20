from pathlib import Path

PATH = Path(__file__).resolve().parent / "event_resource_theorem_rev6.tex"
text = PATH.read_text(encoding="utf-8")

old = "\\boxed{\n\\text{stationary aggregate thermodynamic budgets alone do not determine the temporal information scale}.}"
new = (
    "\\boxed{\n"
    "\\begin{gathered}\n"
    "\\text{stationary aggregate thermodynamic budgets alone}\\\\\n"
    "\\text{do not determine the temporal information scale}\n"
    "\\end{gathered}}"
)

count = text.count(old)
if count != 1:
    raise RuntimeError(f"thermodynamic boxed-conclusion layout: expected exactly one match, found {count}")

PATH.write_text(text.replace(old, new, 1), encoding="utf-8")
print(f"Applied layout fix to {PATH.name}")
