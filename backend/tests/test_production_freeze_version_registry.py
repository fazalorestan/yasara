from app.production_freeze_v1.version_registry import VersionRegistryBuilderV1

def test_version_registry():
    registry = VersionRegistryBuilderV1().build()
    assert any(e.version == "1.0.0" and e.channel == "stable" for e in registry.entries)
