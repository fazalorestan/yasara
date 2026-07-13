from app.rc1_hardening_v1.release_gate import ReleaseGateBuilderV1

def test_release_gate_passed():
    report = ReleaseGateBuilderV1().build()
    assert report.passed is True
