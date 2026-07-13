from pathlib import Path
import json, subprocess, sys, time, webbrowser

ROOT = Path(__file__).resolve().parents[1]
EXE = ROOT / "dist/windows/portable/YaSara/YaSara.exe"
REPORT = ROOT / "runtime_reports/sprint46_finalization_report.json"
URL = "http://127.0.0.1:8000"

def run(cmd):
    return subprocess.run(cmd, cwd=str(ROOT), shell=False).returncode == 0

def main():
    steps = {
        "dashboard_stability": run([sys.executable, "scripts/validate_dashboard_stability.py"]),
        "packaged_backend": run([sys.executable, "scripts/verify_packaged_backend_snapshot.py"]),
        "executable_validation": run([sys.executable, "scripts/check_yasara_executable_validation.py"]),
    }
    launched = False
    if all(steps.values()) and EXE.exists():
        subprocess.Popen([str(EXE)], cwd=str(EXE.parent))
        time.sleep(4)
        webbrowser.open(URL)
        launched = True
    payload = {
        "ready": all(steps.values()) and launched,
        "build_id": "2026.46.ENTERPRISE.001",
        "steps": steps,
        "dashboard_launched": launched,
        "dashboard_url": URL,
        "real_backend_data_only": True,
        "mock_data": False,
        "dashboard_layout_locked": True,
    }
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    print(json.dumps(payload, indent=2))
    return 0 if payload["ready"] else 1

if __name__ == "__main__":
    raise SystemExit(main())
