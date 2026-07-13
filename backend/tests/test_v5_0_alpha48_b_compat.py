from app.platform_core.windows_packaging.report import WindowsPackagingReport, windows_packaging_report

def test_compat(): assert WindowsPackagingReport().report()['ready'] and windows_packaging_report.report()['ready']
