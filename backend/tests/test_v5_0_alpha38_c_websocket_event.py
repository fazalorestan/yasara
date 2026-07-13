from app.platform_core.exchange_layer.websocket_simulation import ExchangeWebSocketSimulationService

def test_v500_alpha38_c_websocket_event(): assert ExchangeWebSocketSimulationService().simulated_event()['real_websocket'] is False