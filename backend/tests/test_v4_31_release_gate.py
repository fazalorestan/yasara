from app.platform_core.release.readiness_gate import ReleaseReadinessGate

def test_v431_release_gate():
    g = ReleaseReadinessGate().run()
    assert g["ready"] is True
    assert g["score"] >= 80
