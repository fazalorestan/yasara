from app.platform_core.config_center.runtime_config import RuntimeConfigStore

def test_v435_runtime_config():
    r = RuntimeConfigStore()
    r.set("x", "1")
    assert r.get("x") == "1"
