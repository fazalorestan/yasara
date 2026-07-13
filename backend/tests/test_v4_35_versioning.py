from app.platform_core.config_center.versioning import ConfigVersionRegistry

def test_v435_versioning():
    v = ConfigVersionRegistry()
    item = v.commit("test", {"a": 1})
    assert item["version"] == "cfg-1"
    assert v.history()
