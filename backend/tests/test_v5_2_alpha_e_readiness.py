from app.platform_core.embedded_backend_bootstrap.readiness import EmbeddedBackendBootstrapReadinessGate

def test_readiness(): assert EmbeddedBackendBootstrapReadinessGate().run()['ready'] is True
