from pydantic import BaseModel, Field
from typing import Literal


class SignalEngineSummaryV42(BaseModel):
    ready: bool = True
    phase: str = "v4_2_multilayer_signal_engine_foundation"
    product_progress_percent: int = 90
    remaining_to_professional_product_percent: int = 10
    constitution_version: str = "YASARA_MASTER_REQUIREMENTS_FINAL_V4"
    constitution_compliant: bool = True
    safety: str = "signal_only_no_real_execution"


class SignalRequestV42(BaseModel):
    symbol: str = "BTCUSDT"
    exchange: str = "binance"
    timeframe: str = "1m"
    build_type: Literal["personal", "commercial"] = "personal"
    autotrade_checkbox_enabled: bool = False
    has_exchange_api_key: bool = False
    license_key: str = ""
    risk_guard_enabled: bool = True
    kill_switch_active: bool = False
    feature_flags: dict = Field(default_factory=lambda: {
        "market_context": True,
        "indicator_engine": True,
        "smart_money": True,
        "ai_indicators": True,
        "risk_gate": True,
        "autotrade_gate": True,
    })
