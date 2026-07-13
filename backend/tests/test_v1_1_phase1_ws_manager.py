from app.v11_market_data.ws_manager import WebSocketManagerV11

def test_ws_manager_connect_reconnect():
    manager = WebSocketManagerV11()
    manager.connect("binance")
    assert manager.is_connected("binance") is True
    manager.disconnect("binance")
    assert manager.is_connected("binance") is False
    manager.reconnect("binance")
    assert manager.is_connected("binance") is True
