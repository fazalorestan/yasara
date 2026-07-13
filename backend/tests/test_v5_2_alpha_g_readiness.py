from app.platform_core.in_process_backend_runner.readiness import InProcessBackendRunnerReadinessGate

def test_readiness(): assert InProcessBackendRunnerReadinessGate().run()['ready'] is True
