from app.version_v1.engine.final_verifier import FinalReleaseVerifierV1

def test_stable_final_release_verify_ready():
    result = FinalReleaseVerifierV1().verify()
    assert result.ready is True
    assert result.passed_checks == result.total_checks
    assert any("Live trading" in warning or "live_trading" in warning for warning in result.warnings)
