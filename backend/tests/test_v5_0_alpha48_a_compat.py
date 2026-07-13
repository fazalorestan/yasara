from app.platform_core.windows_app.report import WindowsAppBootstrapReport, windows_app_bootstrap_report

def test_compat(): assert WindowsAppBootstrapReport().report()['ready'] and windows_app_bootstrap_report.report()['ready']
