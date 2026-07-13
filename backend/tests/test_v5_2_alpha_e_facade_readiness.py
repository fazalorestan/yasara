from app.v52_alpha_embedded_backend_bootstrap.service import EmbeddedBackendBootstrapFacadeV52Alpha

def test_facade_readiness(): assert EmbeddedBackendBootstrapFacadeV52Alpha().readiness() is not None
