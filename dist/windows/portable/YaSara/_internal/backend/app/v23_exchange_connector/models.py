from pydantic import BaseModel


class ExchangeCapabilityV23(BaseModel):
    exchange: str
    rest_enabled: bool = True
    websocket_ready: bool = True
    ohlc_enabled: bool = True
    orderbook_enabled: bool = True
    live_trading_enabled: bool = False


class ExchangeConnectorSummaryV23(BaseModel):
    ready: bool = True
    phase: str = "v2_3_exchange_connector_ohlc_activation"
    operational_progress_percent: int = 85
    remaining_to_full_operational_percent: int = 15
    safety: str = "market_data_connectors_only_live_trading_disabled"
