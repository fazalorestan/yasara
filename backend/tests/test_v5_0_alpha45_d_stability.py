from app.platform_core.production_runtime.stability_checks import RuntimeStabilityCheckService

def test_stability(): assert RuntimeStabilityCheckService().checks()['stable'] is True
