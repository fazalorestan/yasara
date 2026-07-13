from app.platform_core.plugin_sdk.enterprise.quality_score import PluginEnterpriseQualityScoreService

def test_v500_alpha36_d_quality(): assert PluginEnterpriseQualityScoreService().calculate()['ready'] is True
