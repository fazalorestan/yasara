from app.main import app

def test_app_imports_and_has_routes():
    paths = {route.path for route in app.routes}
    assert "/health" in paths
    assert any(path.startswith("/api/v1/paper-trading-v1") for path in paths)
