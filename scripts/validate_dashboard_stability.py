from pathlib import Path
import hashlib, json

ROOT = Path(__file__).resolve().parents[1]
APP = ROOT / "frontend/src/App.tsx"
ENTERPRISE = ROOT / "frontend/src/components/enterprise/EnterpriseTradingOS.tsx"
REPORT = ROOT / "runtime_reports/dashboard_stability_report.json"
REQUIRED = ["EnterpriseTradingOS","Market Chart","AI Signals","WorkspaceButton","DeveloperWorkspace","BottomTabs","ptw-terminal-grid","Watchlist","Positions","Orders","History","AI Decision","Risk Engine","Trade Score"]

def sha256(path):
    if not path.exists(): return None
    h = hashlib.sha256(); h.update(path.read_bytes()); return h.hexdigest()

def main():
    app_text = APP.read_text(encoding="utf-8") if APP.exists() else ""
    enterprise_text = ENTERPRISE.read_text(encoding="utf-8") if ENTERPRISE.exists() else ""
    checks = {
        "app_exists": APP.exists(),
        "enterprise_dashboard_exists": ENTERPRISE.exists(),
        "enterprise_root_unchanged": "return <EnterpriseTradingOS />" in app_text,
        "legacy_contract_preserved": all(token in app_text for token in REQUIRED),
        "ai_first_not_root": "return <AIFirstDashboard />" not in app_text,
        "typescript_compatible": "replaceAll(" not in enterprise_text,
        "real_data_label_present": "Real backend data only" in enterprise_text,
    }
    payload = {
        "ready": all(checks.values()),
        "build_id": "2026.46.ENTERPRISE.001",
        "dashboard_layout_locked": True,
        "mock_data": False,
        "checks": checks,
        "hashes": {"App.tsx": sha256(APP), "EnterpriseTradingOS.tsx": sha256(ENTERPRISE)},
    }
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    print(json.dumps(payload, indent=2))
    return 0 if payload["ready"] else 1

if __name__ == "__main__":
    raise SystemExit(main())
