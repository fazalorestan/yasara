from app.platform_core.auto_dependency_discovery_build_gate.report import auto_dependency_discovery_build_gate_report_service
class AutoDependencyDiscoveryBuildGateReadinessGate:
    def run(self):
        r = auto_dependency_discovery_build_gate_report_service.report()
        return {'ready': r['ready'] and r['dependency_discovery'] and r['executable_validation'] and not r['auto_trading_enabled'], 'checks': r}
auto_dependency_discovery_build_gate_readiness_gate = AutoDependencyDiscoveryBuildGateReadinessGate()
