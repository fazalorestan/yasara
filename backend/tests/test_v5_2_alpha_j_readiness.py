from app.platform_core.auto_dependency_discovery_build_gate.readiness import AutoDependencyDiscoveryBuildGateReadinessGate

def test_readiness(): assert AutoDependencyDiscoveryBuildGateReadinessGate().run()['ready'] is True
