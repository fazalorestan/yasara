from dataclasses import dataclass, field
from typing import Any

@dataclass
class OptimizationConfig:
    strategy_id: str
    symbol: str
    objective: str = "net_pnl"
    max_trials: int = 20
    execution_allowed: bool = False

@dataclass
class ParameterRange:
    name: str
    values: list[Any]

@dataclass
class OptimizationTrial:
    trial_id: str
    parameters: dict[str, Any]
    score: float
    metrics: dict[str, Any] = field(default_factory=dict)
