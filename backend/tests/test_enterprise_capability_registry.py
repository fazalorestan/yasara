from app.enterprise_v1.capability_registry import CapabilityRegistryV1, CapabilityV1

def test_capability_registry():
    registry = CapabilityRegistryV1()
    registry.register(CapabilityV1(key="ai", category="trading"))
    assert registry.list_enabled()[0].key == "ai"
