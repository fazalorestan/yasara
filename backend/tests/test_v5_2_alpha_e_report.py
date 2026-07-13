from app.platform_core.embedded_backend_bootstrap.report import EmbeddedBackendBootstrapReportService

def test_report(): assert EmbeddedBackendBootstrapReportService().report()['ready'] is True
