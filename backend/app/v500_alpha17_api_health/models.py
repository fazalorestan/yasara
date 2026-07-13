from pydantic import BaseModel

class APIHealthSummaryV500Alpha17(BaseModel):
    ready: bool = True
    phase: str = "v5_0_alpha_17_api_smoke_test_health_framework"
    scope: str = "api_smoke_health"
    real_exchange_connection: bool = False
    broker_execution_enabled: bool = False
    auto_trading_enabled: bool = False
    backward_compatible: bool = True
    test_pack_size: int = 20
