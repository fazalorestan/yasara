from app.platform_core.plugin_sdk.enterprise.service import PluginEnterpriseService

def test_v500_alpha36_d_service_quality_score():
 r=PluginEnterpriseService().quality_score(); assert r is not None
