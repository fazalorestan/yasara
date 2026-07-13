from app.platform_core.plugin_sdk.enterprise.service import PluginEnterpriseService

def test_v500_alpha36_d_service_performance():
 r=PluginEnterpriseService().performance(); assert r is not None
