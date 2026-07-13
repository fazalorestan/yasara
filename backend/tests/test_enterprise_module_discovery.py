from app.enterprise_v1.module_discovery import ModuleDiscoveryV1

def test_module_discovery():
    names = [m.name for m in ModuleDiscoveryV1().discover_static()]
    assert "enterprise_v1" in names
