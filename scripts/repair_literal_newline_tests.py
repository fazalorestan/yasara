from pathlib import Path

def main():
    root = Path("backend/tests")
    fixed = 0
    for p in root.glob("test_v5_2_alpha_*.py"):
        text = p.read_text(encoding="utf-8", errors="replace")
        if "\\n" in text and "\n" not in text.strip().replace("\\n", ""):
            p.write_text(text.replace("\\n", "\n"), encoding="utf-8")
            fixed += 1
        elif "\\n" in text.splitlines()[0]:
            p.write_text(text.replace("\\n", "\n"), encoding="utf-8")
            fixed += 1
    print(f"fixed_literal_newline_tests={fixed}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
