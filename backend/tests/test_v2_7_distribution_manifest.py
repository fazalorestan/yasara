from app.v27_distribution.service import FinalDistributionServiceV27

def test_v27_distribution_manifest():
    m = FinalDistributionServiceV27().manifest()
    assert m["version"] == "2.7.0"
    assert m["ready"] is True
    assert m["live_trading_enabled"] is False
