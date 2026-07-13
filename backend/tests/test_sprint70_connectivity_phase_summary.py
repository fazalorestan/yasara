from app.connectivity_v1.phase1_summary import ConnectivityPhaseSummaryBuilderV1

def test_connectivity_phase_summary_ready():
    summary = ConnectivityPhaseSummaryBuilderV1().build()
    assert summary.ready is True
    assert "unified_streaming" in summary.modules
