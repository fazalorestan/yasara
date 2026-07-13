from app.platform_core.exchanges.capabilities import exchange_capability_matrix

class ConnectorCapabilityNegotiator:
    def negotiate(self, exchange_id: str, requested: list[str] | None = None):
        capabilities = exchange_capability_matrix.get(exchange_id) or {}
        requested = requested or ["spot", "rest", "ohlcv", "orderbook", "trades", "ticker"]
        supported = [item for item in requested if capabilities.get(item) is True]
        missing = [item for item in requested if item not in supported]
        return {
            "ready": len(missing) == 0,
            "exchange_id": exchange_id,
            "supported": supported,
            "missing": missing,
            "execution_allowed": False,
        }

connector_capability_negotiator = ConnectorCapabilityNegotiator()
