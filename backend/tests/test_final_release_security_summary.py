from app.final_release_v1.final_security_summary import FinalSecuritySummaryBuilderV1

def test_final_security_summary():
    summary = FinalSecuritySummaryBuilderV1().build()
    assert summary.passed is True
    assert "no_embedded_secrets" in summary.controls
