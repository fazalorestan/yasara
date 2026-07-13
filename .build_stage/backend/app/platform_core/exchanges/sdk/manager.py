from app.platform_core.exchanges.sdk.base import BaseExchangeConnector
from app.platform_core.exchanges.sdk.lifecycle import exchange_connector_lifecycle

class ExchangeConnectorManager:
    def __init__(self):
        self._connectors = {}

    def register_connector(self, exchange_id: str):
        connector = BaseExchangeConnector(exchange_id)
        connector.state = exchange_connector_lifecycle.REGISTERED
        self._connectors[exchange_id] = connector
        return connector.status()

    def enable_connector(self, exchange_id: str):
        connector = self._connectors.get(exchange_id) or BaseExchangeConnector(exchange_id)
        connector.initialize()
        connector.state = exchange_connector_lifecycle.READY
        self._connectors[exchange_id] = connector
        return connector.status()

    def disable_connector(self, exchange_id: str):
        connector = self._connectors.get(exchange_id) or BaseExchangeConnector(exchange_id)
        connector.disconnect()
        self._connectors[exchange_id] = connector
        return connector.status()

    def reload_connector(self, exchange_id: str):
        self.remove_connector(exchange_id)
        self.register_connector(exchange_id)
        return self.enable_connector(exchange_id)

    def remove_connector(self, exchange_id: str):
        connector = self._connectors.pop(exchange_id, None)
        if connector:
            connector.shutdown()
        return {"ready": True, "removed": connector is not None, "exchange_id": exchange_id}

    def list_connectors(self):
        return {k: v.status() for k, v in self._connectors.items()}

    def connector_state(self, exchange_id: str):
        connector = self._connectors.get(exchange_id)
        return connector.status() if connector else {"ready": False, "exchange_id": exchange_id, "state": "missing"}

exchange_connector_manager = ExchangeConnectorManager()
