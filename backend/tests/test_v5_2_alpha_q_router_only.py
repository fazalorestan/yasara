from pathlib import Path

def test_router_uses_registry_only():
    text = (Path(__file__).resolve().parents[2] / "backend/app/api/v1/router.py").read_text(encoding="utf-8")
    assert "runtime_auto_router_registry.register_all" in text
    assert "from app.api.v1.routes import" not in text
    assert ".include_router(v418_launcher_v1.router)" not in text
