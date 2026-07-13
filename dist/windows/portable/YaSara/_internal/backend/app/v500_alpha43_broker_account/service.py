from app.platform_core.broker_layer.account_contract import broker_account_contract_service
from app.platform_core.broker_layer.account_readiness import broker_account_readiness_gate
from app.platform_core.broker_layer.account_report import broker_account_report
from app.platform_core.broker_layer.account_safety import broker_account_safety_policy
from app.platform_core.broker_layer.balance_contract import broker_balance_contract_service
from app.platform_core.broker_layer.capability_matrix import broker_capability_matrix_service
from app.platform_core.broker_layer.position_contract import broker_position_contract_service
from app.v500_alpha43_broker_account.models import BrokerAccountSummaryV500Alpha43
class BrokerAccountFacadeV500Alpha43:
    def summary(self): return BrokerAccountSummaryV500Alpha43()
    def account_contract(self): return broker_account_contract_service.contract()
    def dry_account(self): return broker_account_contract_service.dry_account()
    def balances(self): return broker_balance_contract_service.balances()
    def positions(self): return broker_position_contract_service.positions()
    def capability_matrix(self): return broker_capability_matrix_service.matrix()
    def safety(self): return broker_account_safety_policy.policy()
    def report(self): return broker_account_report.report()
    def readiness(self): return broker_account_readiness_gate.run()
    def contract(self): return {"ready": True, "broker_layer": "package_b_account_capability", "execution_allowed": False}
broker_account_facade_v500_alpha43 = BrokerAccountFacadeV500Alpha43()
