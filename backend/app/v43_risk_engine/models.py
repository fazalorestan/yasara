from pydantic import BaseModel, Field


class RiskEngineSummaryV43(BaseModel):
    ready: bool = True
    phase: str = "v4_3_advanced_risk_engine_foundation"
    product_progress_percent: int = 92
    remaining_to_professional_product_percent: int = 8
    constitution_version: str = "YASARA_MASTER_REQUIREMENTS_FINAL_V4"
    constitution_compliant: bool = True
    safety: str = "risk_calculation_only_no_real_execution"


class RiskProfileV43(BaseModel):
    equity: float = 10000
    risk_per_trade_percent: float = 1.0
    daily_risk_limit_percent: float = 3.0
    weekly_risk_limit_percent: float = 7.0
    monthly_risk_limit_percent: float = 15.0
    max_drawdown_percent: float = 20.0
    max_leverage: float = 5.0
    recovery_mode_enabled: bool = True


class RiskStateV43(BaseModel):
    daily_loss_percent: float = 0
    weekly_loss_percent: float = 0
    monthly_loss_percent: float = 0
    current_drawdown_percent: float = 0
    open_positions: int = 0
    portfolio_heat_percent: float = 0
    kill_switch_active: bool = False


class RiskRequestV43(BaseModel):
    symbol: str = "BTCUSDT"
    exchange: str = "binance"
    entry_price: float = 50000
    stop_loss_price: float = 49000
    take_profit_price: float = 53000
    win_rate: float = 0.55
    reward_risk: float = 2.0
    profile: RiskProfileV43 = Field(default_factory=RiskProfileV43)
    state: RiskStateV43 = Field(default_factory=RiskStateV43)
