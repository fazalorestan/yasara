from pydantic import BaseModel
class BrokerOrdersAccountSummaryV500Alpha37(BaseModel):
    ready: bool = True
    phase: str = "v5_0_alpha_37_broker_abstraction_package_b"
    scope: str = "broker_orders_account_snapshot"
    order_contract: bool = True
    order_validation: bool = True
    account_snapshot: bool = True
    balances: bool = True
    positions: bool = True
    dry_run_order_preview: bool = True
    real_execution_enabled: bool = False
    auto_trading_enabled: bool = False
    backward_compatible: bool = True
    test_pack_size: int = 60
