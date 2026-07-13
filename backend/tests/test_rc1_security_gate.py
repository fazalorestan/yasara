from app.rc1_v1.security_gate import SecurityGateBuilderV1

def test_rc1_security_gate():
    report = SecurityGateBuilderV1().build()
    assert report.passed is True
    assert "no_embedded_secrets" in report.checks
