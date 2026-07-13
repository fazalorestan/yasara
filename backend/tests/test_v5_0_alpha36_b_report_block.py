from app.platform_core.plugin_sdk.runtime_report import PluginRuntimeReportService

def test_v500_alpha36_b_report_block(): assert PluginRuntimeReportService().report()['execution_allowed'] is False