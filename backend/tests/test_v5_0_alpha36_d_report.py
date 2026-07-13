from app.platform_core.plugin_sdk.enterprise.report import PluginEnterpriseReportBuilder

def test_v500_alpha36_d_report(): assert PluginEnterpriseReportBuilder().build()['ready'] is True
