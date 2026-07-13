from pydantic import BaseModel, Field

class PluginManifestV1(BaseModel):
    plugin_id: str
    name: str
    version: str = "1.0.0"
    permissions: list[str] = Field(default_factory=list)

class PluginRegistryV1:
    def __init__(self):
        self.plugins: dict[str, PluginManifestV1] = {}

    def register(self, plugin: PluginManifestV1) -> PluginManifestV1:
        self.plugins[plugin.plugin_id] = plugin
        return plugin

    def list(self) -> list[PluginManifestV1]:
        return list(self.plugins.values())
