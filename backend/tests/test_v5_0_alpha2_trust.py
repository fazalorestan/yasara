from app.platform_core.indicators.marketplace.trust import IndicatorTrustPolicy

def test_v500_alpha2_trust():
    r=IndicatorTrustPolicy().evaluate({"name":"x","trust_level":"trusted"}); assert r["allow_install"] is True and r["allow_execution"] is False
