from app.platform_core.desktop_app.desktop_report import DesktopHostReport, desktop_host_report

def test_compat(): assert DesktopHostReport().report()['ready'] and desktop_host_report.report()['ready']
