from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
APP = ROOT / "frontend" / "src" / "App.tsx"
REPORT = ROOT / "runtime_reports" / "sprint47_dashboard_validation.json"
PROVIDER_HUB = ROOT / "frontend" / "src" / "api" / "dashboardProviderHub.ts"

BUILD_ID = "2026.48.ENTERPRISE.003"

REQUIRED_TEXT_MARKERS = (
    "Market Workspace",
    "Watchlist",
    "Positions",
    "Orders",
)

REQUIRED_COMPONENT_MARKERS = (
    "AIDecisionEngine",
    "RiskPanel",
    "PortfolioAllocation",
    "PerformancePanel",
    "QuickActions",
)

REQUIRED_LAYOUT_MARKERS = (
    'className="ent-app"',
    'className="ent-main"',
    'className="ent-workspace"',
    'className="ent-left-stack"',
    'className="ent-mid-stack"',
    'className="ent-right-stack"',
)

LEGACY_CONTRACT_BEGIN = "/* YASARA_LEGACY_UI_CONTRACT_BEGIN */"
LEGACY_CONTRACT_END = "/* YASARA_LEGACY_UI_CONTRACT_END */"


def _strip_legacy_contract(text: str) -> str:
    start = text.find(LEGACY_CONTRACT_BEGIN)
    end = text.find(LEGACY_CONTRACT_END)
    if start == -1 or end == -1 or end < start:
        return text
    end += len(LEGACY_CONTRACT_END)
    return text[:start] + text[end:]


def _contains_all(text: str, markers: tuple[str, ...]) -> bool:
    lowered = text.lower()
    return all(marker.lower() in lowered for marker in markers)


def main() -> int:
    app_exists = APP.is_file()
    text = APP.read_text(encoding="utf-8", errors="ignore") if app_exists else ""
    active_text = _strip_legacy_contract(text)

    checks = {
        "app_exists": app_exists,
        "approved_text_markers": _contains_all(active_text, REQUIRED_TEXT_MARKERS),
        "approved_component_markers": _contains_all(
            active_text, REQUIRED_COMPONENT_MARKERS
        ),
        "approved_layout_markers": _contains_all(
            active_text, REQUIRED_LAYOUT_MARKERS
        ),
        "legacy_root_not_active": "return <EnterpriseTradingOS />" not in active_text,
        "provider_hub_api_exists": PROVIDER_HUB.is_file(),
    }

    payload = {
        "ready": all(checks.values()),
        "build_id": BUILD_ID,
        "checks": checks,
        "paths": {
            "app": str(APP),
            "provider_hub": str(PROVIDER_HUB),
            "report": str(REPORT),
        },
    }

    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0 if payload["ready"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
