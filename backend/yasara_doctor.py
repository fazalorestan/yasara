from pathlib import Path
import importlib
import traceback
import json

ROOT = Path(__file__).resolve().parent


def scan_literal_newlines():
    bad = []

    for f in ROOT.rglob("*.py"):

        try:
            text = f.read_text(encoding="utf-8")
        except Exception:
            continue

        if "\\n" in text:
            bad.append(str(f))

    return bad


def scan_imports():

    app = ROOT / "app"

    modules = []

    for py in app.rglob("*.py"):

        rel = py.relative_to(ROOT)

        mod = ".".join(rel.with_suffix("").parts)

        if mod.endswith("__init__"):
            mod = mod[:-9]

        modules.append(mod)

    failed = []

    for m in sorted(modules):

        try:
            importlib.import_module(m)

        except Exception:

            failed.append(
                {
                    "module": m,
                    "error": traceback.format_exc()
                }
            )

    return failed


def main():

    report = {}

    report["literal_newline_files"] = scan_literal_newlines()

    report["import_errors"] = scan_imports()

    report["literal_newline_count"] = len(report["literal_newline_files"])

    report["import_error_count"] = len(report["import_errors"])

    print(json.dumps(report, indent=2))

    (ROOT / "doctor_report.json").write_text(
        json.dumps(report, indent=2),
        encoding="utf-8"
    )


if __name__ == "__main__":
    main()