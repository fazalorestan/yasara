from app.platform_core.plugin_sdk.enterprise.service import PluginEnterpriseService

def test_v500_alpha36_d_service_runtime_acceptance():
 r=PluginEnterpriseService().runtime_acceptance(); assert r is not None
