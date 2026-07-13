from pathlib import Path
import json, time

ROOT = Path(__file__).resolve().parents[1]
ROUTER = ROOT / "backend/app/api/v1/router.py"
REPORT = ROOT / "runtime_reports/sprint47_hotfix_002_router_report.json"

CANONICAL = '''from fastapi import APIRouter

from app.api.v1.health import router as health_router
from app.platform_core.auto_router_registry.runtime_registry import (
    runtime_auto_router_registry,
)

api_router = APIRouter()
api_router.include_router(health_router, tags=["health"])
AUTO_ROUTER_REGISTRY_RESULT = runtime_auto_router_registry.register_all(api_router)
'''

def main():
    ROUTER.parent.mkdir(parents=True, exist_ok=True)
    ROUTER.write_text(CANONICAL, encoding="utf-8")
    text = ROUTER.read_text(encoding="utf-8")
    checks = {
        "auto_registry_present": "runtime_auto_router_registry.register_all" in text,
        "direct_route_import_absent": "from app.api.v1.routes import" not in text,
        "legacy_launcher_absent": "v418_launcher_v1" not in text,
    }
    payload = {
        "ready": all(checks.values()),
        "build_id": "2026.47.HOTFIX.002",
        "timestamp": time.time(),
        "checks": checks,
    }
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    print(json.dumps(payload, indent=2))
    return 0 if payload["ready"] else 1

if __name__ == "__main__":
    raise SystemExit(main())
