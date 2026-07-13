from app.platform_core.exchanges.capabilities import exchange_capability_matrix
from app.platform_core.exchanges.connector_contract import exchange_connector_contract
from app.platform_core.exchanges.health import exchange_health_monitor
from app.platform_core.exchanges.metadata import exchange_metadata_registry
from app.platform_core.exchanges.readiness import exchange_connector_readiness_gate
from app.platform_core.exchanges.registry import exchange_registry

class ExchangeConnectorFrameworkService:
    def list_exchanges(self):
        return {"ready": True, "exchanges": exchange_registry.seed_defaults()}

    def exchange(self, exchange_id: str):
        return {"ready": True, "exchange": exchange_registry.get(exchange_id)}

    def capabilities(self, exchange_id: str | None = None):
        if exchange_id:
            return {"ready": True, "capabilities": exchange_capability_matrix.get(exchange_id)}
        return {"ready": True, "capabilities": exchange_capability_matrix.seed_defaults()}

    def metadata(self, exchange_id: str | None = None):
        if exchange_id:
            return {"ready": True, "metadata": exchange_metadata_registry.get(exchange_id)}
        return {"ready": True, "metadata": exchange_metadata_registry.seed_defaults()}

    def health(self):
        exchanges = exchange_registry.seed_defaults()
        return {"ready": True, "health": exchange_health_monitor.seed_defaults(list(exchanges.keys()))}

    def connector_contract(self):
        return exchange_connector_contract.contract()

    def readiness(self):
        return exchange_connector_readiness_gate.run()

exchange_connector_framework_service = ExchangeConnectorFrameworkService()
