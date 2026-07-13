from app.platform_core.windows_real_exe.report import WindowsRealExeBuildPipelineReportService

def test_report(): assert WindowsRealExeBuildPipelineReportService().report()['ready'] is True
