from pydantic import BaseModel
class BrokerAccountSummaryV500Alpha43(BaseModel):
    ready: bool = True
    phase: str = "v5_0_alpha_43_broker_layer_package_b"
    scope: str = "broker_account_capability_layer"
    account_contract: bool = True
    balance_contract: bool = True
    position_contract: bool = True
    capability_matrix: bool = True
    account_safety_policy: bool = True
    real_account_read_enabled: bool = False
    real_broker_connection_enabled: bool = False
    real_execution_enabled: bool = False
    auto_trading_enabled: bool = False
    backward_compatible: bool = True
    test_pack_size: int = 60
