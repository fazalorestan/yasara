from pathlib import Path
import py_compile
import sys

ROOTS = [Path("backend/app"), Path("desktop"), Path("scripts")]

def main() -> int:
    errors = []
    checked = 0
    for root in ROOTS:
        if not root.exists():
            continue
        for path in root.rglob("*.py"):
            checked += 1
            try:
                py_compile.compile(str(path), doraise=True)
            except Exception as exc:
                errors.append({"path": str(path), "error": str(exc)})
    print(f"python_files_checked={checked}")
    print(f"python_compile_errors={len(errors)}")
    for item in errors:
        print(f"{item['path']}: {item['error']}")
    return 1 if errors else 0

if __name__ == "__main__":
    raise SystemExit(main())
