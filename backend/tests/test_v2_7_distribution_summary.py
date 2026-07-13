from app.v27_distribution.service import FinalDistributionServiceV27

def test_v27_distribution_summary():
    s = FinalDistributionServiceV27().summary()
    assert s["ready"] is True
    assert s["distribution_ready"] is True
    assert s["operational_progress_percent"] == 100
