from app.platform_core.broker_layer.account_contract import broker_account_contract_service
from app.platform_core.broker_layer.account_safety import broker_account_safety_policy
from app.platform_core.broker_layer.balance_contract import broker_balance_contract_service
from app.platform_core.broker_layer.capability_matrix import broker_capability_matrix_service
from app.platform_core.broker_layer.position_contract import broker_position_contract_service

class BrokerAccountReport:
    def report(self):
        return {"ready": True, "account_contract": broker_account_contract_service.contract(), "dry_account": broker_account_contract_service.dry_account(), "balances": broker_balance_contract_service.balances(), "positions": broker_position_contract_service.positions(), "capability_matrix": broker_capability_matrix_service.matrix(), "safety": broker_account_safety_policy.policy(), "real_account_read_enabled": False, "real_broker_connection_enabled": False, "real_execution_enabled": False, "auto_trading_enabled": False, "execution_allowed": False}
broker_account_report = BrokerAccountReport()
# -------------------------------------------------
# Backward Compatibility
# -------------------------------------------------

BrokerAccountReportService = BrokerAccountReport

broker_account_report_service = broker_account_report
