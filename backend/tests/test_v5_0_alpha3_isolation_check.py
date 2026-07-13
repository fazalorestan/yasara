from app.platform_core.indicators.sandbox.isolation_check import IndicatorIsolationChecker

def test_v500_alpha3_isolation_check():
    c = IndicatorIsolationChecker()
    assert c.check({"imports":[]})["ready"] is True
    assert c.check({"imports":["live_trading"]})["ready"] is False
