from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "yasara_release.py"
WRAPPER = ROOT / "yasara-release.cmd"
YASARA = ROOT / "yasara.py"

def main():
    text = YASARA.read_text(encoding="utf-8") if YASARA.exists() else ""
    checks = {
        "release_script_exists": SCRIPT.exists(),
        "wrapper_exists": WRAPPER.exists(),
        "yasara_not_patched": "YASARA_RELEASE_COMMAND_BEGIN" not in text,
    }
    print(json.dumps({"ready":all(checks.values()),"checks":checks}, indent=2))
    return 0 if all(checks.values()) else 1

if __name__ == "__main__":
    raise SystemExit(main())
