from pydantic import BaseModel
class ExchangeCoreSummaryV500Alpha38(BaseModel):
    ready: bool = True
    phase: str = "v5_0_alpha_38_exchange_abstraction_package_a"
    scope: str = "exchange_core_capability_detection"
    unified_exchange_contract: bool = True
    exchange_registry: bool = True
    capability_detection: bool = True
    market_type_support: bool = True
    exchange_health: bool = True
    exchange_safety_contract: bool = True
    real_exchange_connection: bool = False
    real_execution_enabled: bool = False
    auto_trading_enabled: bool = False
    backward_compatible: bool = True
    test_pack_size: int = 60
