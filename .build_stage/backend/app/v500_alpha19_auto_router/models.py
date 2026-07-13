from pydantic import BaseModel

class AutoRouterSummaryV500Alpha19(BaseModel):
    ready: bool = True
    phase: str = "v5_0_alpha_19_auto_router_discovery"
    scope: str = "api_router_discovery_foundation"
    manual_router_patch_required: bool = False
    auto_trading_enabled: bool = False
    real_exchange_connection: bool = False
    backward_compatible: bool = True
    test_pack_size: int = 20
