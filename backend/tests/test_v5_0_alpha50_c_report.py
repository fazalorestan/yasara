from app.platform_core.windows_packaging_enablement.safety_report import GuardedPackagingSafetyReportService

def test_report(): assert GuardedPackagingSafetyReportService().report()['ready'] is True
