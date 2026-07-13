from app.platform_core.broker.capabilities import broker_capability_contract
from app.platform_core.broker.execution_guard import broker_execution_guard
from app.platform_core.broker.models import BrokerOrderResult, BrokerPosition, BrokerWalletBalance
from app.platform_core.broker.safety import broker_safety_policy

class BrokerLayerFoundationService:
    def capabilities(self): return broker_capability_contract.capabilities()
    def safety_policy(self): return broker_safety_policy.policy()
    def preflight_order(self, payload: dict): return broker_execution_guard.check(payload)
    def submit_order_contract(self, payload: dict):
        guard = broker_execution_guard.check(payload)
        reason = guard["reason"] if guard["validation"]["valid"] else ",".join(guard["validation"]["errors"])
        return BrokerOrderResult(accepted=False, status="blocked", reason=reason, execution_allowed=False).__dict__
    def sample_position(self): return BrokerPosition(symbol="BTCUSDT", side="long", quantity=0.1, entry_price=50000.0).__dict__
    def sample_wallet(self): return BrokerWalletBalance(asset="USDT", total=1000.0, available=1000.0).__dict__
broker_layer_foundation_service = BrokerLayerFoundationService()
