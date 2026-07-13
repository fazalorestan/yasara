from app.platform_core.plugin_sdk.enterprise.service import PluginEnterpriseService

def test_v500_alpha36_d_final_score(): assert PluginEnterpriseService().final_status()['quality_score'] >= 9.5
