from app.platform_core.release.security_readiness import SecurityReadinessReport

def test_v431_security_readiness():
    r = SecurityReadinessReport().report()
    assert r["ready"] is True
    assert r["checks"]["live_trading_default_disabled"] is True
