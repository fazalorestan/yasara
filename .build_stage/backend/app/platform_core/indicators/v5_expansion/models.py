from dataclasses import dataclass, field
from typing import Any

@dataclass
class GenericIndicatorPluginContract:
    name: str
    version: str
    display_name: str
    overlay: bool = True
    enabled_by_default: bool = False
    capabilities: list[str] = field(default_factory=list)
    required_contracts: list[str] = field(default_factory=list)
    metadata: dict[str, Any] = field(default_factory=dict)
