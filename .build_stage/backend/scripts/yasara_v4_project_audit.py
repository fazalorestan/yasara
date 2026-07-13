from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[2]
BACKEND = ROOT / "backend"
FRONTEND = ROOT / "frontend"
REPORT = ROOT / "docs" / "constitution" / "PROJECT_V4_AUDIT_REPORT.md"

required_files = [
    ROOT / "feature_registry.yaml",
    ROOT / "dependency_graph.yaml",
    ROOT / "docs" / "data_flow.md",
    ROOT / "technical_debt_log.md",
    BACKEND / "app" / "api" / "v1" / "router.py",
    FRONTEND / "src" / "App.tsx",
]

frontend_components = [
    "SmartMoneyStatus",
    "MarketAnalysisStatus",
    "StrategyBuilderStatus",
    "AdvancedAiIndicatorStatus",
    "LiveExchangeStatus",
]

def status_line(ok):
    return "✅" if ok else "❌"

def main():
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    lines = ["# YaSara v4 Constitution Audit Report", ""]
    lines.append("## Required Files")
    for p in required_files:
        lines.append(f"- {status_line(p.exists())} `{p.relative_to(ROOT)}`")

    app_file = FRONTEND / "src" / "App.tsx"
    lines.append("")
    lines.append("## Frontend Operational Components")
    if app_file.exists():
        app_text = app_file.read_text(encoding="utf-8")
        for name in frontend_components:
            lines.append(f"- {status_line(name in app_text)} `{name}` activated in App.tsx")
    else:
        lines.append("- ❌ `frontend/src/App.tsx` missing")

    router_file = BACKEND / "app" / "api" / "v1" / "router.py"
    lines.append("")
    lines.append("## Router Checks")
    if router_file.exists():
        router_text = router_file.read_text(encoding="utf-8")
        for token in ["v351_constitution_audit_v1", "v35_smart_money_v1", "v34_market_analysis_v1", "v33_strategy_builder_v1"]:
            lines.append(f"- {status_line(token in router_text)} `{token}`")
    else:
        lines.append("- ❌ router.py missing")

    lines.append("")
    lines.append("## Recommendations")
    lines.append("- Run `python backend/scripts/sync_operational_frontend_status.py` to activate missing status components.")
    lines.append("- Run full tests after every patch.")
    lines.append("- Do not start execution_engine until Personal-only build isolation exists.")
    lines.append("- Complete Phase A meta-infrastructure next.")

    REPORT.write_text("\\n".join(lines), encoding="utf-8")
    print(REPORT)

if __name__ == "__main__":
    main()
