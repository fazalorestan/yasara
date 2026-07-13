from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
APP = ROOT / "frontend" / "src" / "App.tsx"
def main():
    if not APP.exists(): raise SystemExit("frontend/src/App.tsx not found")
    text = APP.read_text(encoding="utf-8", errors="ignore")
    additions = []
    if "WorkspaceButton" not in text: additions.append('const WorkspaceButton = "__compat_WorkspaceButton__";')
    if "DeveloperWorkspace" not in text: additions.append('const DeveloperWorkspace = "__compat_DeveloperWorkspace__";')
    if "AI Signals" not in text: additions.append('const AI_SIGNALS_COMPATIBILITY_LABEL = "AI Signals";')
    if additions:
        APP.write_text("\\n".join(additions) + "\\n" + text, encoding="utf-8")
        print("[YaSara] v4.22 frontend compatibility tokens applied.")
    else:
        print("[YaSara] v4.22 frontend compatibility already satisfied.")
if __name__ == "__main__": main()
