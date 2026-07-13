from dataclasses import dataclass, field
from typing import Any

@dataclass
class IndicatorManifest:
    name: str
    version: str
    enabled_by_default: bool = False
    overlay: bool = True
    owner: str = "yasara-core"
    capabilities: list[str] = field(default_factory=list)
    metadata: dict[str, Any] = field(default_factory=dict)

@dataclass
class ChartOverlayContract:
    indicator: str
    overlays: list[str] = field(default_factory=list)
    signals: list[str] = field(default_factory=list)
    panels: list[str] = field(default_factory=list)
    mode: str = "contract_only"
