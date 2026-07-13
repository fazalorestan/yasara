from app.platform_core.release.plugin_readiness import PluginReadinessMatrix

def test_v431_plugin_readiness():
    m = PluginReadinessMatrix().matrix()
    assert m["ready"] is True
    assert m["plugin_count"] >= 5
