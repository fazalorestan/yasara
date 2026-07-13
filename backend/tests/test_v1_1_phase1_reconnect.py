from app.v11_market_data.reconnect import ReconnectManagerV11

def test_reconnect_delay():
    manager = ReconnectManagerV11()
    assert manager.next_delay(1) == 1.0
    assert manager.next_delay(3) == 4.0
