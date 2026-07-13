from app.platform_core.plugin_sdk.enterprise.security import PluginEnterpriseSecurityGate

def test_v500_alpha36_d_security_block(): assert PluginEnterpriseSecurityGate().evaluate()['execution_allowed'] is False
