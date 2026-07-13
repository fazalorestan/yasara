from app.platform_core.auto_dependency_discovery_build_gate.report import AutoDependencyDiscoveryBuildGateReportService

def test_report(): assert AutoDependencyDiscoveryBuildGateReportService().report()['executable_validation'] is True
