from app.platform_core.plugin_sdk.enterprise.readiness import PluginEnterpriseReadinessGate

def test_v500_alpha36_d_readiness(): assert PluginEnterpriseReadinessGate().run()['ready'] is True
