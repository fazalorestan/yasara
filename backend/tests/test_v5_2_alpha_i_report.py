from app.platform_core.cryptography_runtime_dependency_fix.report import CryptographyRuntimeDependencyFixReportService

def test_report(): assert CryptographyRuntimeDependencyFixReportService().report()['ready'] is True
