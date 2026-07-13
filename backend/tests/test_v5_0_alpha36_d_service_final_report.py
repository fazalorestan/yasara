from app.platform_core.plugin_sdk.enterprise.service import PluginEnterpriseService

def test_v500_alpha36_d_service_final_report():
 r=PluginEnterpriseService().final_report(); assert r is not None
