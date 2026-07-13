from pydantic import BaseModel

class BrokerCoreSummaryV500Alpha43(BaseModel):
    ready: bool = True
    phase: str = "v5_0_alpha_43_broker_layer_package_a"
    scope: str = "broker_core_adapter_contract"
    broker_registry: bool = True
    broker_adapter_contract: bool = True
    broker_capability_contract: bool = True
    broker_safety_policy: bool = True
    real_broker_connection_enabled: bool = False
    real_execution_enabled: bool = False
    auto_trading_enabled: bool = False
    backward_compatible: bool = True
    test_pack_size: int = 60
