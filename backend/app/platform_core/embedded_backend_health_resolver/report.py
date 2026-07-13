class EmbeddedBackendHealthResolverReportService:
    def report(self):
        return {'ready': True, 'build_id': '2026.52.F.001', 'health_candidates': ['/api/v1/health','/health','/docs','/openapi.json'], 'timeout_seconds': 45, 'backend_log_capture': True, 'runtime_report': 'runtime_reports/launcher_report.json', 'signal_only_default': True, 'auto_trading_enabled': False}
embedded_backend_health_resolver_report_service = EmbeddedBackendHealthResolverReportService()
