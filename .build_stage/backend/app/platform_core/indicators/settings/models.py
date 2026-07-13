from dataclasses import dataclass, field
from typing import Any

@dataclass
class YasaraIndicatorSettings:
    ema_fast: int = 21
    ema_mid: int = 55
    ema_slow: int = 200
    rsi_len: int = 14
    macd_fast: int = 12
    macd_slow: int = 26
    macd_signal: int = 9
    min_score: int = 60
    show_emas: bool = True
    show_smc: bool = True
    show_fvg: bool = True
    show_entry_sl_tp: bool = True
    mode: str = "default"

@dataclass
class YasaraPreset:
    name: str
    version: str = "v1.0"
    settings: dict[str, Any] = field(default_factory=dict)
    description: str = ""

@dataclass
class SettingsValidationResult:
    valid: bool
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
