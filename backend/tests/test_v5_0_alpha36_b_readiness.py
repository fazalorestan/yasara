from app.platform_core.plugin_sdk.runtime_readiness import PluginRuntimeReadinessGate

def test_v500_alpha36_b_readiness(): assert PluginRuntimeReadinessGate().run()['ready'] is True