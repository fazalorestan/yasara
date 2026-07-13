from dataclasses import dataclass, field
from typing import Any

@dataclass
class CandleInput:
    time: int
    open: float
    high: float
    low: float
    close: float
    volume: float

@dataclass
class IndicatorRuntimeInput:
    symbol: str = "BTCUSDT"
    timeframe: str = "4H"
    candles: list[CandleInput] = field(default_factory=list)
    settings: dict[str, Any] = field(default_factory=dict)

@dataclass
class IndicatorOverlayOutput:
    name: str
    value: float
    kind: str = "line"
    color: str = "default"

@dataclass
class IndicatorSignalOutput:
    direction: str = "WAIT"
    confidence: int = 0
    reason: str = "no_signal"
    execution_allowed: bool = False

@dataclass
class IndicatorRuntimeOutput:
    indicator: str = "yasara"
    version: str = "v1.0"
    overlays: list[IndicatorOverlayOutput] = field(default_factory=list)
    signals: list[IndicatorSignalOutput] = field(default_factory=list)
    panels: dict[str, Any] = field(default_factory=dict)
    mode: str = "analysis_only"
