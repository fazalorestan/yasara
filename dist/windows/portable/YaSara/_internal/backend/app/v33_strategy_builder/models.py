from pydantic import BaseModel, Field
from typing import Literal


class StrategyBuilderSummaryV33(BaseModel):
    ready: bool = True
    phase: str = "v3_3_strategy_builder_core"
    product_progress_percent: int = 65
    remaining_to_professional_product_percent: int = 35
    safety: str = "strategy_simulation_only_live_trading_disabled"


class StrategyConditionV33(BaseModel):
    left: str
    operator: Literal["gt", "gte", "lt", "lte", "eq", "neq"] = "gt"
    right: float | str | bool


class StrategyRuleV33(BaseModel):
    rule_id: str
    name: str
    conditions: list[StrategyConditionV33] = Field(default_factory=list)
    action: Literal["buy", "sell", "hold", "block"] = "hold"
    enabled: bool = True


class StrategyDefinitionV33(BaseModel):
    strategy_id: str
    name: str
    symbol: str = "BTCUSDT"
    exchange: str = "binance"
    timeframe: str = "1m"
    rules: list[StrategyRuleV33] = Field(default_factory=list)
    status: Literal["draft", "active", "archived"] = "draft"
    live_trading_enabled: bool = False


class StrategyContextV33(BaseModel):
    symbol: str = "BTCUSDT"
    exchange: str = "binance"
    timeframe: str = "1m"
    fields: dict = Field(default_factory=dict)
