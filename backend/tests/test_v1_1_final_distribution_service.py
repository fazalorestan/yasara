from app.v11_distribution.service import FinalDistributionServiceV11

def test_final_distribution_service():
    summary = FinalDistributionServiceV11().summary()
    assert summary.ready is True
    assert summary.progress_percent == 100
    assert len(summary.windows_outputs) >= 3
    assert len(summary.mobile_outputs) >= 3
