from app.platform_core.broker_layer.readiness import broker_layer_core_readiness_gate
from app.platform_core.broker_layer.service import broker_layer_core_service
from app.v500_alpha37_broker_core.models import BrokerCoreSummaryV500Alpha37

class BrokerCoreFacadeV500Alpha37:
    def summary(self): return BrokerCoreSummaryV500Alpha37()
    def contract(self): return broker_layer_core_service.contract()
    def brokers(self): return broker_layer_core_service.brokers()
    def default_broker(self): return broker_layer_core_service.default_broker()
    def capabilities(self): return broker_layer_core_service.capabilities()
    def health(self): return broker_layer_core_service.health()
    def safety(self): return broker_layer_core_service.safety()
    def status(self): return broker_layer_core_service.status()
    def readiness(self): return broker_layer_core_readiness_gate.run()

broker_core_facade_v500_alpha37 = BrokerCoreFacadeV500Alpha37()
