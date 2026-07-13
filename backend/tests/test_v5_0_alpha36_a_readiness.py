from app.platform_core.plugin_sdk.readiness import PluginSDKCoreReadinessGate

def test_v500_alpha36_a_readiness(): assert PluginSDKCoreReadinessGate().run()['ready'] is True
