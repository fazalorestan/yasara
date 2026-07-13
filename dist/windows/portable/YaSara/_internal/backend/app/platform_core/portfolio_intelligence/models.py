from dataclasses import dataclass, field
from typing import Any

@dataclass
class PortfolioAsset:
    symbol: str
    value: float
    target_weight: float
    current_weight: float = 0.0
    metadata: dict[str, Any] = field(default_factory=dict)

@dataclass
class PortfolioProfile:
    portfolio_id: str
    name: str
    base_currency: str = "USDT"
    risk_mode: str = "balanced"
