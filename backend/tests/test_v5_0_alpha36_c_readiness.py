from app.platform_core.plugin_sdk.versioning_readiness import PluginVersioningReadinessGate

def test_v500_alpha36_c_readiness(): assert PluginVersioningReadinessGate().run()['ready'] is True