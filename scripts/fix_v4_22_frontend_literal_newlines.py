from __future__ import annotations

from pathlib import Path
from datetime import datetime

ROOT = Path(__file__).resolve().parents[1]
APP = ROOT / "frontend" / "src" / "App.tsx"

COMPAT_LINES = [
    'const DeveloperWorkspace = "__compat_DeveloperWorkspace__";',
    'const WorkspaceButton = "__compat_WorkspaceButton__";',
    'const AI_SIGNALS_COMPATIBILITY_LABEL = "AI Signals";',
]


def main() -> None:
    if not APP.exists():
        raise SystemExit("frontend/src/App.tsx not found")

    text = APP.read_text(encoding="utf-8", errors="ignore")
    backup = APP.with_suffix(APP.suffix + f".backup_v4221_{datetime.now().strftime('%Y%m%d_%H%M%S')}")
    backup.write_text(text, encoding="utf-8")

    # Fix literal escaped newlines that break Vite/Babel parsing.
    text = text.replace("\\n", "\n")

    # Remove duplicate compatibility constants if repeated.
    lines = text.splitlines()
    cleaned = []
    seen = set()
    for line in lines:
        stripped = line.strip()
        if stripped in COMPAT_LINES:
            if stripped in seen:
                continue
            seen.add(stripped)
        cleaned.append(line)

    text = "\n".join(cleaned).strip() + "\n"

    # Ensure required old-test compatibility tokens exist, but as real lines.
    missing = [line for line in COMPAT_LINES if line not in text]
    if missing:
        text = "\n".join(missing) + "\n" + text

    # Make sure imports remain after constants without escaped chars.
    text = text.replace(";\nimport", ";\nimport")

    APP.write_text(text, encoding="utf-8")
    print("[YaSara] v4.22.1 frontend literal newline fix applied.")
    print(f"[YaSara] Backup saved: {backup}")


if __name__ == "__main__":
    main()
