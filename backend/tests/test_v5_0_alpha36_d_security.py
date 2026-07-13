from app.platform_core.plugin_sdk.enterprise.security import PluginEnterpriseSecurityGate

def test_v500_alpha36_d_security(): assert PluginEnterpriseSecurityGate().evaluate()['score'] >= 9.5
