from dataclasses import dataclass, field
from typing import Any

@dataclass
class PluginManifest:
    plugin_id: str
    name: str
    version: str
    api_version: str = "v1"
    enabled: bool = True
    capabilities: list[str] = field(default_factory=list)
    metadata: dict[str, Any] = field(default_factory=dict)

@dataclass
class PluginMetadata:
    plugin_id: str
    vendor: str = "yasara"
    license_required: bool = False
    sandbox_required: bool = True
