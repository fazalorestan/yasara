from app.platform_core.production_readiness.architecture_stability import ArchitectureStabilityGuard

def test_architecture(): assert ArchitectureStabilityGuard().evaluate()['architecture_stable'] is True
