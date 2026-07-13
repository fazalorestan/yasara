from pathlib import Path

ROOTS = [
    Path("backend/app"),
    Path("backend/tests"),
    Path("desktop"),
    Path("scripts"),
]

def looks_corrupted(text: str) -> bool:
    if "\\n" not in text:
        return False
    first = text.splitlines()[0] if text.splitlines() else text
    return "\\n" in first or text.count("\\n") > text.count("\n") * 2

def main() -> int:
    fixed = 0
    for root in ROOTS:
        if not root.exists():
            continue
        for path in root.rglob("*.py"):
            text = path.read_text(encoding="utf-8", errors="replace")
            if looks_corrupted(text):
                path.write_text(text.replace("\\n", "\n"), encoding="utf-8")
                fixed += 1
    print(f"fixed_literal_newline_python_files={fixed}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
