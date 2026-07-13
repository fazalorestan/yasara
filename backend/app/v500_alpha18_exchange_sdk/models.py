from pydantic import BaseModel

class ExchangeSDKSummaryV500Alpha18(BaseModel):
    ready: bool = True
    phase: str = "v5_0_alpha_18_exchange_connector_sdk_lifecycle"
    scope: str = "exchange_connector_sdk"
    sdk_version: str = "1.0"
    real_exchange_connection: bool = False
    broker_execution_enabled: bool = False
    auto_trading_enabled: bool = False
    backward_compatible: bool = True
    test_pack_size: int = 20
