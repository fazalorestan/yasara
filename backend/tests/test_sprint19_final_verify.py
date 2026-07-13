from app.version_v1.engine.final_verifier import FinalReleaseVerifierV1

def test_final_verify_ready_with_warnings():
    result = FinalReleaseVerifierV1().verify()
    assert result.ready is True
    assert result.total_checks >= 1
    assert any("live_trading" in warning for warning in result.warnings)
