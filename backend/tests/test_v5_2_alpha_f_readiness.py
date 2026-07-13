from app.platform_core.embedded_backend_health_resolver.readiness import EmbeddedBackendHealthResolverReadinessGate

def test_readiness(): assert EmbeddedBackendHealthResolverReadinessGate().run()['ready'] is True
