from app.platform_core.desktop_app.ui_report import DesktopUIReport, desktop_ui_report

def test_compat(): assert DesktopUIReport().report()['ready'] and desktop_ui_report.report()['ready']
