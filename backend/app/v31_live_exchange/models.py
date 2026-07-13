from pydantic import BaseModel


class LiveExchangeSummaryV31(BaseModel):
    ready: bool = True
    phase: str = "v3_1_live_exchange_websocket_foundation"
    product_progress_percent: int = 48
    remaining_to_professional_product_percent: int = 52
    safety: str = "live_market_data_only_live_trading_disabled"


class LiveSubscriptionV31(BaseModel):
    exchange: str = "binance"
    symbol: str = "BTCUSDT"
    channels: list[str] = ["ticker", "orderbook", "candles"]
    timeframe: str = "1m"
