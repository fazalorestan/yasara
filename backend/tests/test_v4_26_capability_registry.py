from app.platform_core.capabilities import CapabilityRegistry

def test_v426_capability_registry():
    r = CapabilityRegistry()
    item = r.register("p", ["analysis", "risk"])
    assert item["plugin"] == "p"
    assert r.get("p") == ["analysis", "risk"]
