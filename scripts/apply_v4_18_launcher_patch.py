from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
YASARA = ROOT / "yasara.py"

if not YASARA.exists():
    raise SystemExit("yasara.py not found")

text = YASARA.read_text(encoding="utf-8")

if "from scripts.yasara_one_command_launcher import start as yasara_start" not in text:
    insert = "from scripts.yasara_one_command_launcher import start as yasara_start\n"
    text = insert + text

if '"start"' not in text and "'start'" not in text:
    text = text.replace(
        'choices=["patch", "test", "run-backend", "run-frontend"]',
        'choices=["patch", "test", "run-backend", "run-frontend", "start"]'
    )
    text = text.replace(
        "choices=['patch', 'test', 'run-backend', 'run-frontend']",
        "choices=['patch', 'test', 'run-backend', 'run-frontend', 'start']"
    )

if 'a.command == "start"' not in text and "a.command == 'start'" not in text:
    marker = 'elif a.command == "run-frontend": run_frontend()'
    if marker in text:
        text = text.replace(marker, marker + '\n    elif a.command == "start": yasara_start(open_browser=True)')
    else:
        marker = "elif a.command == 'run-frontend': run_frontend()"
        if marker in text:
            text = text.replace(marker, marker + "\n    elif a.command == 'start': yasara_start(open_browser=True)")
        else:
            text += '''

# v4.18 fallback command hook
if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "start":
        yasara_start(open_browser=True)
'''

YASARA.write_text(text, encoding="utf-8")
print("YaSara v4.18 launcher patch applied. Use: python yasara.py start")
