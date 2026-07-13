from app.platform_core.apscheduler_dependency_gate.readiness import APSchedulerDependencyGateReadinessGate

def test_readiness(): assert APSchedulerDependencyGateReadinessGate().run()['ready'] is True
