from app.platform_core.embedded_backend_health_resolver.report import embedded_backend_health_resolver_report_service
class EmbeddedBackendHealthResolverReadinessGate:
    def run(self):
        r = embedded_backend_health_resolver_report_service.report()
        return {'ready': r['ready'] and r['backend_log_capture'] and not r['auto_trading_enabled'], 'checks': r}
embedded_backend_health_resolver_readiness_gate = EmbeddedBackendHealthResolverReadinessGate()
