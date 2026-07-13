from __future__ import annotations

from pathlib import Path
from datetime import datetime
import re

ROOT = Path(__file__).resolve().parents[1]
APP = ROOT / "frontend" / "src" / "App.tsx"


def main() -> None:
    if not APP.exists():
        raise SystemExit("frontend/src/App.tsx not found")

    text = APP.read_text(encoding="utf-8", errors="ignore")
    backup = APP.with_suffix(APP.suffix + f".backup_v4222_{datetime.now().strftime('%Y%m%d_%H%M%S')}")
    backup.write_text(text, encoding="utf-8")

    # Convert escaped newlines to real newlines.
    text = text.replace("\\n", "\n")

    # Remove const aliases that collide with function declarations.
    text = re.sub(r'^\s*const\s+WorkspaceButton\s*=\s*["\'][^"\']*["\'];\s*\n', '', text, flags=re.MULTILINE)

    # Remove duplicate DeveloperWorkspace / AI Signals constants, keep one clean copy.
    text = re.sub(r'^\s*const\s+DeveloperWorkspace\s*=\s*["\'][^"\']*["\'];\s*\n', '', text, flags=re.MULTILINE)
    text = re.sub(r'^\s*const\s+AI_SIGNALS_COMPATIBILITY_LABEL\s*=\s*["\']AI Signals["\'];\s*\n', '', text, flags=re.MULTILINE)

    # If a function WorkspaceButton already exists, keep it.
    # If not, add a harmless function compatibility wrapper.
    prefix_lines = [
        'const DeveloperWorkspace = "__compat_DeveloperWorkspace__";',
        'const AI_SIGNALS_COMPATIBILITY_LABEL = "AI Signals";',
    ]

    if "function WorkspaceButton(" not in text:
        workspace_fn = '''
function WorkspaceButton() {
  return null;
}

'''
        marker = "function Sidebar("
        if marker in text:
            text = text.replace(marker, workspace_fn + marker, 1)
        else:
            text = workspace_fn + text

    # Add non-colliding tokens at the top.
    text = "\n".join(prefix_lines) + "\n" + text.lstrip()

    # Normalize excessive blank lines.
    text = re.sub(r'\n{4,}', '\n\n\n', text)

    APP.write_text(text, encoding="utf-8")
    print("[YaSara] v4.22.2 frontend compatibility cleanup applied.")
    print(f"[YaSara] Backup saved: {backup}")


if __name__ == "__main__":
    main()
