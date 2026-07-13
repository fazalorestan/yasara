from pathlib import Path

def test_router_is_auto_registry():
    text=(Path(__file__).resolve().parents[2]/"backend/app/api/v1/router.py").read_text(encoding="utf-8")
    assert "runtime_auto_router_registry.register_all" in text
    assert "from app.api.v1.routes import" not in text
