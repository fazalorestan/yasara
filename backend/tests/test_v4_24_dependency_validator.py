from app.v423_plugin_catalog.models import PluginManifestV423
from app.v424_plugin_registry_sync.dependency_validator import PluginDependencyValidatorV424

def test_v424_dependency_validator():
    manifests = [PluginManifestV423(name="a", version="1"), PluginManifestV423(name="b", version="1", dependencies=["a"])]
    result = PluginDependencyValidatorV424().validate(manifests)
    assert result["ready"] is True
