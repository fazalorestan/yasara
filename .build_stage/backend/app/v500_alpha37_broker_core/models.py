from pydantic import BaseModel

class BrokerCoreSummaryV500Alpha37(BaseModel):
    ready: bool = True
    phase: str = "v5_0_alpha_37_broker_abstraction_package_a"
    scope: str = "broker_core_capability_detection"
    unified_broker_contract: bool = True
    broker_registry: bool = True
    capability_detection: bool = True
    broker_health: bool = True
    execution_safety_contract: bool = True
    real_execution_enabled: bool = False
    auto_trading_enabled: bool = False
    backward_compatible: bool = True
    test_pack_size: int = 60
