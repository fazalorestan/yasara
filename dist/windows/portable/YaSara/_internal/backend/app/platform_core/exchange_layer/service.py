from app.platform_core.exchange_layer.capabilities import exchange_capability_service
from app.platform_core.exchange_layer.contract import exchange_contract_service
from app.platform_core.exchange_layer.health import exchange_health_service
from app.platform_core.exchange_layer.markets import exchange_market_type_service
from app.platform_core.exchange_layer.registry import exchange_registry_service
from app.platform_core.exchange_layer.safety import exchange_safety_contract
class ExchangeLayerCoreService:
    def contract(self): return exchange_contract_service.contract()
    def exchanges(self): return exchange_registry_service.list_exchanges()
    def default_exchange(self): return exchange_registry_service.get("binance.sandbox")
    def capabilities(self): return exchange_capability_service.matrix(self.exchanges()["exchanges"])
    def market_types(self): return exchange_market_type_service.supported_market_types()
    def health(self): return {"ready": True, "items": [exchange_health_service.health(e) for e in self.exchanges()["exchanges"]]}
    def safety(self): return exchange_safety_contract.policy()
    def status(self): return {"ready": True, "exchanges_ready": self.exchanges()["ready"], "capabilities_ready": self.capabilities()["ready"], "health_ready": self.health()["ready"], "real_exchange_connection": False, "execution_allowed": False}
exchange_layer_core_service = ExchangeLayerCoreService()
