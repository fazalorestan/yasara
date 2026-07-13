from app.platform_core.embedded_backend_health_resolver.report import EmbeddedBackendHealthResolverReportService

def test_report(): assert EmbeddedBackendHealthResolverReportService().report()['ready'] is True
