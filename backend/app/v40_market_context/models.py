from pydantic import BaseModel, Field
from typing import Literal


class MarketContextSummaryV40(BaseModel):
    ready: bool = True
    phase: str = "v4_0_market_context_engine_autotrade_gate"
    product_progress_percent: int = 86
    remaining_to_professional_product_percent: int = 14
    constitution_version: str = "YASARA_MASTER_REQUIREMENTS_FINAL_V4"
    constitution_compliant: bool = True
    safety: str = "analysis_and_gate_only_no_real_execution"


class MarketContextRequestV40(BaseModel):
    symbol: str = "BTCUSDT"
    exchange: str = "binance"
    timeframes: list[str] = Field(default_factory=lambda: ["1m", "5m", "15m", "1h", "4h"])


class EngineResultV40(BaseModel):
    engine: str
    confidence: float = 0
    bias: Literal["bullish", "bearish", "neutral"] = "neutral"
    weight: float = 1.0
    reasons: list[str] = Field(default_factory=list)


class AutoTradeGateRequestV40(BaseModel):
    build_type: Literal["personal", "commercial"] = "personal"
    license_key: str = ""
    exchange: str = "bitunix"
    has_exchange_api_key: bool = False
    risk_guard_enabled: bool = True
    kill_switch_active: bool = False
    checkbox_enabled: bool = False
