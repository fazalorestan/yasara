from app.v11_market_data.health import MarketHealthMonitorV11
from app.v11_market_data.models import ConnectionStateV11

def test_health_monitor():
    monitor = MarketHealthMonitorV11()
    health = monitor.heartbeat("binance")
    assert health.state == ConnectionStateV11.CONNECTED
    assert monitor.is_ready() is True
