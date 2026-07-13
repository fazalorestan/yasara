class ExchangeWebSocketSimulationService:
    def simulated_event(self, symbol: str = "BTCUSDT", stream: str = "ticker"):
        return {
            "ready": True,
            "symbol": symbol,
            "stream": stream,
            "event": {"last_price": 50000.0, "source": "simulated_websocket"},
            "real_websocket": False,
            "execution_allowed": False,
        }

exchange_websocket_simulation_service = ExchangeWebSocketSimulationService()
