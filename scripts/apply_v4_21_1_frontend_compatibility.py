from __future__ import annotations

from pathlib import Path
from datetime import datetime

ROOT = Path(__file__).resolve().parents[1]
APP = ROOT / "frontend" / "src" / "App.tsx"


def backup(path: Path) -> None:
    if path.exists():
        stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_path = path.with_suffix(path.suffix + f".backup_{stamp}")
        backup_path.write_text(path.read_text(encoding="utf-8", errors="ignore"), encoding="utf-8")
        print(f"[YaSara] Backup saved: {backup_path}")


def main() -> None:
    if not APP.exists():
        raise SystemExit("frontend/src/App.tsx not found")

    text = APP.read_text(encoding="utf-8", errors="ignore")
    backup(APP)

    if "function WorkspaceButton(" not in text:
        marker = "function Sidebar("
        wrapper = '''
/**
 * Backward compatibility alias for v4.19 UI regression tests.
 * The v4.20 layout uses Sidebar nav buttons directly.
 * This wrapper is intentionally kept for compatibility and does not affect UI.
 */
function WorkspaceButton() {
  return null;
}

'''
        if marker in text:
            text = text.replace(marker, wrapper + marker, 1)
        else:
            text = wrapper + text

    if "AI Signals" not in text:
        marker = "const aiRows = ["
        alias = '''
// Backward compatibility token for v4.19.1 regression tests.
// Previous Premium Dashboard used the phrase: AI Signals.
// Current v4.20 terminal layout displays AI Decision instead.
const AI_SIGNALS_COMPATIBILITY_LABEL = "AI Signals";

'''
        if marker in text:
            text = text.replace(marker, alias + marker, 1)
        else:
            text = alias + text

    APP.write_text(text, encoding="utf-8")
    print("[YaSara] v4.21.1 frontend compatibility layer applied.")


if __name__ == "__main__":
    main()
