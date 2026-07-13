from app.platform_core.plugin_sdk.versioning_report import PluginVersioningReportService

def test_v500_alpha36_c_report(): assert PluginVersioningReportService().report()['ready'] is True