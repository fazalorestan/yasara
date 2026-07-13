from app.platform_core.extension_host.dependency_graph import PluginDependencyGraph
from app.v423_plugin_catalog.models import PluginManifestV423

def test_v427_dependency_graph():
    g = PluginDependencyGraph()
    r = g.build([PluginManifestV423(name="a", version="1"), PluginManifestV423(name="b", version="1", dependencies=["a"])])
    assert "a" in r["nodes"]
    assert g.dependents_of("a") == ["b"]
