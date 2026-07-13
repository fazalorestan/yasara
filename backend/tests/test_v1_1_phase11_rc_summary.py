from app.v11_release_candidate.rc_summary import V11ReleaseCandidateSummaryBuilder

def test_v11_release_candidate_summary():
    summary = V11ReleaseCandidateSummaryBuilder().build()
    assert summary.ready is True
    assert summary.modules_ready == summary.modules_total
    assert "release_candidate_manifest" in summary.capabilities
