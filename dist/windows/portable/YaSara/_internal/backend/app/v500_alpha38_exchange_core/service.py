from app.platform_core.exchange_layer.readiness import exchange_layer_core_readiness_gate
from app.platform_core.exchange_layer.service import exchange_layer_core_service
from app.v500_alpha38_exchange_core.models import ExchangeCoreSummaryV500Alpha38
class ExchangeCoreFacadeV500Alpha38:
    def summary(self): return ExchangeCoreSummaryV500Alpha38()
    def contract(self): return exchange_layer_core_service.contract()
    def exchanges(self): return exchange_layer_core_service.exchanges()
    def default_exchange(self): return exchange_layer_core_service.default_exchange()
    def capabilities(self): return exchange_layer_core_service.capabilities()
    def market_types(self): return exchange_layer_core_service.market_types()
    def health(self): return exchange_layer_core_service.health()
    def safety(self): return exchange_layer_core_service.safety()
    def status(self): return exchange_layer_core_service.status()
    def readiness(self): return exchange_layer_core_readiness_gate.run()
exchange_core_facade_v500_alpha38 = ExchangeCoreFacadeV500Alpha38()
