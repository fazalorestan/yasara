from app.v52_alpha_in_process_backend_runner.service import InProcessBackendRunnerFacadeV52Alpha

def test_facade_readiness(): assert InProcessBackendRunnerFacadeV52Alpha().readiness() is not None
