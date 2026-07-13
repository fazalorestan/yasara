from app.connectivity_v1.websocket_core import ConnectionState, WebSocketConnectionConfigV1, WebSocketConnectionManagerV1

def test_websocket_connection_state_flow():
    manager = WebSocketConnectionManagerV1(WebSocketConnectionConfigV1(name="bitunix", url="wss://example"))
    assert manager.mark_connecting().state == ConnectionState.CONNECTING
    assert manager.mark_connected().state == ConnectionState.CONNECTED
    assert manager.mark_reconnecting().reconnect_attempts == 1
