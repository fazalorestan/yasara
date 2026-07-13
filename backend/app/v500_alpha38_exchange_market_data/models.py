from pydantic import BaseModel

class ExchangeMarketDataSummaryV500Alpha38(BaseModel):
    ready: bool = True
    phase: str = "v5_0_alpha_38_exchange_abstraction_package_b"
    scope: str = "exchange_market_data_symbols"
    symbol_registry: bool = True
    market_metadata: bool = True
    ticker_snapshot: bool = True
    orderbook_snapshot: bool = True
    candle_contract: bool = True
    market_data_safety: bool = True
    real_exchange_connection: bool = False
    real_execution_enabled: bool = False
    auto_trading_enabled: bool = False
    backward_compatible: bool = True
    test_pack_size: int = 60
