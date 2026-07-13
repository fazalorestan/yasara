from pydantic import BaseModel

class RouterAutoRegistrationSummaryV500Alpha301(BaseModel):
    ready: bool = True
    phase: str = "v5_0_alpha_30_1_router_auto_registration"
    scope: str = "router_auto_registration_engine"
    auto_discovery_enabled: bool = True
    auto_registration_contract_enabled: bool = True
    manual_router_patch_required: bool = False
    real_execution_enabled: bool = False
    auto_trading_enabled: bool = False
    backward_compatible: bool = True
    test_pack_size: int = 20
