from app.market_tools_v1.volatility import VolatilityMonitorV1

def test_volatility_monitor_level():
    result = VolatilityMonitorV1().calculate([100, 110, 90])
    assert result.level in {"medium", "high"}
