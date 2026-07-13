from app.v27_distribution.service import FinalDistributionServiceV27

def test_v27_distribution_safety():
    assert FinalDistributionServiceV27().manifest()["live_trading_enabled"] is False
