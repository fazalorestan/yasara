from app.platform_core.licensing.readiness.gate import LicenseFinalReadinessGate
def test_v500_alpha14_gate_execution():
    assert LicenseFinalReadinessGate().run()["execution_allowed"] is False
