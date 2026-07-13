from app.platform_core.licensing.readiness.gate import LicenseFinalReadinessGate
def test_v500_alpha14_gate():
    r = LicenseFinalReadinessGate().run()
    assert r["ready"] is True
    assert r["score"] == 100.0
