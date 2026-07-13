from pydantic import BaseModel, Field

class UserSettingsV21(BaseModel):
    theme: str = "professional"
    workspace: str = "terminal"
    default_exchange: str = "binance"
    default_symbol: str = "BTCUSDT"
    language: str = "fa"
    live_trading_enabled: bool = False

class WatchlistItemV21(BaseModel):
    symbol: str
    exchange: str = "binance"
    favorite: bool = False

class WatchlistStateV21(BaseModel):
    items: list[WatchlistItemV21] = Field(default_factory=list)

class RealDataSummaryV21(BaseModel):
    ready: bool = True
    phase: str = "v2_1_real_data_activation_phase_1"
    operational_progress_percent: int = 60
    remaining_to_full_operational_percent: int = 40
    safety: str = "live_trading_disabled"
