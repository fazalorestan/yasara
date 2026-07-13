from pydantic import BaseModel

class LauncherSwaggerAPISearchSummaryV500Alpha20(BaseModel):
    ready: bool = True
    phase: str = "v5_0_alpha_20_launcher_swagger_api_search"
    scope: str = "launcher_swagger_api_search"
    startup_self_test: bool = True
    swagger_sync: bool = True
    api_search: bool = True
    auto_trading_enabled: bool = False
    real_exchange_connection: bool = False
    backward_compatible: bool = True
    test_pack_size: int = 20
