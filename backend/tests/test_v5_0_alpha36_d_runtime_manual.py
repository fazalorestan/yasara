from app.platform_core.plugin_sdk.enterprise.runtime_acceptance import PluginEnterpriseRuntimeAcceptance

def test_v500_alpha36_d_runtime_manual(): assert PluginEnterpriseRuntimeAcceptance().contract()['manual_apply_required'] is False
