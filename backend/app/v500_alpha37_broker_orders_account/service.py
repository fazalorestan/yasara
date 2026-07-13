from app.platform_core.broker_layer.account import broker_account_snapshot_service
from app.platform_core.broker_layer.account_report import broker_account_report_service
from app.platform_core.broker_layer.order_preview import broker_order_preview_service
from app.platform_core.broker_layer.order_validation import broker_order_validation_service
from app.platform_core.broker_layer.orders import broker_order_contract_service
from app.platform_core.broker_layer.orders_readiness import broker_orders_readiness_gate
from app.v500_alpha37_broker_orders_account.models import BrokerOrdersAccountSummaryV500Alpha37

class BrokerOrdersAccountFacadeV500Alpha37:
    def summary(self): return BrokerOrdersAccountSummaryV500Alpha37()
    def sample_order(self): return {"ready": True, "order": broker_order_contract_service.sample_order()}
    def normalize_order(self): return broker_order_contract_service.normalize(broker_order_contract_service.sample_order())
    def validate_order(self): return broker_order_validation_service.validate(broker_order_contract_service.normalize(broker_order_contract_service.sample_order())["order"])
    def balances(self): return broker_account_snapshot_service.balances()
    def positions(self): return broker_account_snapshot_service.positions()
    def snapshot(self): return broker_account_snapshot_service.snapshot()
    def order_preview(self): return broker_order_preview_service.preview()
    def report(self): return broker_account_report_service.report()
    def readiness(self): return broker_orders_readiness_gate.run()
    def contract(self): return {"ready": True, "broker_layer": "package_b_orders_account", "execution_allowed": False}

broker_orders_account_facade_v500_alpha37 = BrokerOrdersAccountFacadeV500Alpha37()
