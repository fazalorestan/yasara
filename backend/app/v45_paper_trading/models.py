from pydantic import BaseModel, Field
from typing import Literal


class PaperTradingSummaryV45(BaseModel):
    ready: bool = True
    phase: str = "v4_5_paper_trading_execution_simulator"
    product_progress_percent: int = 96
    remaining_to_professional_product_percent: int = 4
    constitution_version: str = "YASARA_MASTER_REQUIREMENTS_FINAL_V4"
    constitution_compliant: bool = True
    safety: str = "paper_trading_only_no_real_execution"


class PaperOrderRequestV45(BaseModel):
    symbol: str = "BTCUSDT"
    exchange: str = "binance"
    side: Literal["buy", "sell"] = "buy"
    order_type: Literal["market", "limit"] = "market"
    quantity: float = 0.01
    price: float | None = None
    reduce_only: bool = False
    source: str = "manual"


class SignalPaperRequestV45(BaseModel):
    symbol: str = "BTCUSDT"
    exchange: str = "binance"
    timeframe: str = "1m"
    allow_paper_autotrade: bool = True
    license_key: str = ""
    has_exchange_api_key: bool = False
    autotrade_checkbox_enabled: bool = False


class PaperAccountResetV45(BaseModel):
    balance: float = 10000.0
