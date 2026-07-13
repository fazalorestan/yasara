from pathlib import Path
import shutil
import time

ROOT = Path(__file__).resolve().parents[1]
app = ROOT / "frontend" / "src" / "App.tsx"
backup = ROOT / "frontend" / "src" / f"App.pre_sprint43_{int(time.time())}.tsx"

def main():
    if app.exists():
        shutil.copy2(app, backup)
    app.write_text(
        'import { EnterpriseTradingOS } from "./components/enterprise/EnterpriseTradingOS";\n\n'
        'export function App() {\n'
        '  return <EnterpriseTradingOS />;\n'
        '}\n',
        encoding="utf-8",
    )
    print(f"backup={backup}")
    print(f"updated={app}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
