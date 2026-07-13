from app.v11_distribution.phase13_summary import V11FinalDistributionSummaryBuilder

def test_final_distribution_summary():
    summary = V11FinalDistributionSummaryBuilder().build()
    assert summary.ready is True
    assert "windows_portable_output" in summary.capabilities
    assert "mobile_pwa_output" in summary.capabilities
