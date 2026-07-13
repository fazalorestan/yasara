from pathlib import Path

def test_sprint47_hotfix_002_router_registry_only():
    root = Path(__file__).resolve().parents[2]
    text = (root / "backend/app/api/v1/router.py").read_text(encoding="utf-8")
    assert "runtime_auto_router_registry.register_all" in text
    assert "from app.api.v1.routes import" not in text
    assert "v418_launcher_v1" not in text
