from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
ROUTER = ROOT / "backend/app/api/v1/router.py"

def main():
    text = ROUTER.read_text(encoding="utf-8") if ROUTER.exists() else ""
    checks = {
        "router_exists": ROUTER.exists(),
        "auto_registry": "runtime_auto_router_registry.register_all" in text,
        "no_direct_route_import": "from app.api.v1.routes import" not in text,
        "no_v418_reference": "v418_launcher_v1" not in text,
    }
    payload = {"ready": all(checks.values()), "checks": checks}
    print(json.dumps(payload, indent=2))
    return 0 if payload["ready"] else 1

if __name__ == "__main__":
    raise SystemExit(main())
