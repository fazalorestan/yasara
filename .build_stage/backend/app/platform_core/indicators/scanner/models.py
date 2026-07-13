from dataclasses import dataclass, field
from typing import Any

@dataclass
class IndicatorScannerItem:
    symbol: str
    indicator: str = "yasara"
    direction: str = "WAIT"
    score: int = 0
    grade: str = "D"
    badge: str = "WAIT"
    reasons: list[str] = field(default_factory=list)
    metadata: dict[str, Any] = field(default_factory=dict)

@dataclass
class IndicatorScannerResult:
    indicator: str = "yasara"
    items: list[IndicatorScannerItem] = field(default_factory=list)
    mode: str = "analysis_only"
