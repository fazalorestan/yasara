from pydantic import BaseModel

class MarketDataSummaryV500Alpha15(BaseModel):
    ready: bool = True
    phase: str = "v5_0_alpha_15_market_data_layer_foundation"
    scope: str = "market_data_foundation"
    real_exchange_connection: bool = False
    broker_execution_enabled: bool = False
    auto_trading_enabled: bool = False
    backward_compatible: bool = True
    test_pack_size: int = 20
