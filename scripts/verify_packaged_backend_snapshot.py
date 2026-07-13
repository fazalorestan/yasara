from pathlib import Path
import hashlib
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "backend/app/api/v1/router.py"
STAGE = ROOT / ".build_stage/backend/app/api/v1/router.py"
PACKAGED = ROOT / "dist/windows/portable/YaSara/_internal/backend/app/api/v1/router.py"


def digest(path: Path):
    h = hashlib.sha256()
    h.update(path.read_bytes())
    return h.hexdigest()


def inspect(path: Path):
    if not path.exists():
        return {"exists": False}
    text = path.read_text(encoding="utf-8", errors="replace")
    return {
        "exists": True,
        "sha256": digest(path),
        "auto_registry": "runtime_auto_router_registry.register_all" in text,
        "direct_route_import": "from app.api.v1.routes import" in text,
        "legacy_launcher": "v418_launcher_v1" in text,
    }


report = {
    "source": inspect(SOURCE),
    "stage": inspect(STAGE),
    "packaged": inspect(PACKAGED),
}

hashes = [
    item.get("sha256")
    for item in report.values()
    if item.get("exists") and item.get("sha256")
]
report["hash_match"] = len(hashes) == 3 and len(set(hashes)) == 1
report["ready"] = (
    report["hash_match"]
    and report["packaged"].get("auto_registry")
    and not report["packaged"].get("direct_route_import")
    and not report["packaged"].get("legacy_launcher")
)

print(json.dumps(report, indent=2))
raise SystemExit(0 if report["ready"] else 1)
