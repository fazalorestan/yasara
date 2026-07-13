from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[1]
APP=ROOT/"frontend/src/App.tsx"
REPORT=ROOT/"runtime_reports/sprint47_dashboard_validation.json"
MARKERS=["Market Workspace","AI Decision Engine","Risk Panel","Watchlist","Positions","Orders","Portfolio Allocation","Performance","Quick Actions"]
def main():
    text=APP.read_text(encoding="utf-8",errors="ignore") if APP.exists() else ""
    checks={
        "app_exists":APP.exists(),
        "approved_markers":all(x.lower() in text.lower() for x in MARKERS),
        "generic_shell_not_root":"return <EnterpriseTradingOS />" not in text,
        "provider_hub_api_exists":(ROOT/"frontend/src/api/dashboardProviderHub.ts").exists(),
    }
    payload={"ready":all(checks.values()),"build_id":"2026.47.ENTERPRISE.001","checks":checks}
    REPORT.parent.mkdir(parents=True,exist_ok=True)
    REPORT.write_text(json.dumps(payload,indent=2),encoding="utf-8")
    print(json.dumps(payload,indent=2))
    return 0 if payload["ready"] else 1
if __name__=="__main__":
    raise SystemExit(main())
