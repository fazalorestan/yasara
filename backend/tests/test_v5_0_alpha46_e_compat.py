from app.platform_core.desktop_app.foundation_report import DesktopFoundationReport, desktop_foundation_report

def test_compat(): assert DesktopFoundationReport().report()["ready"] and desktop_foundation_report.report()["ready"]
