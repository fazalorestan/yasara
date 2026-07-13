from app.platform_core.plugin_sdk.enterprise.report import PluginEnterpriseReportBuilder

def test_v500_alpha36_d_report_packages(): assert len(PluginEnterpriseReportBuilder().build()['packages']) == 4
