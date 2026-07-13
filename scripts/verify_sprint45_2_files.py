from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]

checks = {
    "router": ROOT / "backend/app/api/v1/router.py",
    "app": ROOT / "frontend/src/App.tsx",
    "enterprise": ROOT / "frontend/src/components/enterprise/EnterpriseTradingOS.tsx",
}

failed = False
for name, path in checks.items():
    print(f"\n--- {name}: {path} ---")
    if not path.exists():
        print("MISSING")
        failed = True
        continue
    text = path.read_text(encoding="utf-8")
    if name == "router":
        print("direct_route_import=", "from app.api.v1.routes import" in text)
        print("legacy_launcher_reference=", "v418_launcher_v1" in text)
        print("auto_registry=", "runtime_auto_router_registry.register_all" in text)
        failed |= "from app.api.v1.routes import" in text or "v418_launcher_v1" in text
    elif name == "app":
        print("legacy_compat_import=", "legacyDashboardContract" in text)
        print("enterprise_root=", "return <EnterpriseTradingOS />" in text)
        failed |= "legacyDashboardContract" in text
    else:
        print("replaceAll=", "replaceAll(" in text)
        failed |= "replaceAll(" in text

raise SystemExit(1 if failed else 0)
