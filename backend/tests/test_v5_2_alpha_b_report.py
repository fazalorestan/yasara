from app.platform_core.first_real_exe_build.report import FirstRealExeBuildReportService

def test_report(): assert FirstRealExeBuildReportService().report()['ready'] is True
