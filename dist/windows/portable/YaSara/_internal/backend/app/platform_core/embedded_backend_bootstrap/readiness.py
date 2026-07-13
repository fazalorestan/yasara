from app.platform_core.embedded_backend_bootstrap.report import embedded_backend_bootstrap_report_service
class EmbeddedBackendBootstrapReadinessGate:
    def run(self):
        r=embedded_backend_bootstrap_report_service.report()
        return {'ready':r['ready'] and r['health_url'].startswith('http://127.0.0.1') and not r['auto_trading_enabled'],'checks':r}
embedded_backend_bootstrap_readiness_gate=EmbeddedBackendBootstrapReadinessGate()
