from dataclasses import dataclass, field
from typing import Any

@dataclass
class IndicatorCatalogItem:
    name: str
    display_name: str
    version: str
    author: str = "yasara-core"
    trust_level: str = "trusted"
    installed: bool = False
    enabled: bool = False
    compatible: bool = True
    capabilities: list[str] = field(default_factory=list)
    metadata: dict[str, Any] = field(default_factory=dict)
