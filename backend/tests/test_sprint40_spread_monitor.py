from app.market_tools_v1.spread import SpreadInputV1, SpreadMonitorV1

def test_spread_monitor_calculates_percent():
    result = SpreadMonitorV1().calculate(SpreadInputV1(symbol="BTC/USDT", bid=99, ask=101))
    assert result.spread == 2
    assert result.spread_percent == 2
