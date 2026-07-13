from pathlib import Path
import shutil
import time

ROOT = Path(__file__).resolve().parents[1]
YASARA = ROOT / "yasara.py"
BEGIN = "# YASARA_RELEASE_COMMAND_BEGIN"
END = "# YASARA_RELEASE_COMMAND_END"

BLOCK = '''# YASARA_RELEASE_COMMAND_BEGIN
def _yasara_release_command_dispatch():
    import runpy
    import sys
    from pathlib import Path

    if len(sys.argv) > 1 and sys.argv[1] == "release":
        target = Path(__file__).resolve().parent / "scripts" / "yasara_release.py"
        if not target.exists():
            raise SystemExit(f"Release script not found: {target}")
        sys.argv = [str(target), *sys.argv[2:]]
        runpy.run_path(str(target), run_name="__main__")
        raise SystemExit(0)

_yasara_release_command_dispatch()
# YASARA_RELEASE_COMMAND_END'''


def remove_old(text: str) -> str:
    if BEGIN in text and END in text:
        start = text.index(BEGIN)
        finish = text.index(END) + len(END)
        return (text[:start] + text[finish:]).lstrip("\n")
    return text


def main() -> int:
    if not YASARA.exists():
        print(f"Missing: {YASARA}")
        return 2

    backup = YASARA.with_name(
        f"yasara.pre_release_command_{int(time.time())}.py"
    )
    shutil.copy2(YASARA, backup)

    current = remove_old(YASARA.read_text(encoding="utf-8"))
    YASARA.write_text(BLOCK + "\n\n" + current, encoding="utf-8")

    print(f"backup={backup}")
    print("command=python yasara.py release")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
