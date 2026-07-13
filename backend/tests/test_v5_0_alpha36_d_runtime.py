from app.platform_core.plugin_sdk.enterprise.runtime_acceptance import PluginEnterpriseRuntimeAcceptance

def test_v500_alpha36_d_runtime(): assert PluginEnterpriseRuntimeAcceptance().contract()['requires_http_200'] is True
