from pydantic import BaseModel, Field

class PluginPermissionV1(BaseModel):
    name: str
    description: str = ""

class PluginSDKManifestV1(BaseModel):
    plugin_id: str
    name: str
    version: str = "1.0.0"
    permissions: list[PluginPermissionV1] = Field(default_factory=list)

class PluginSDKValidatorV1:
    def validate(self, manifest: PluginSDKManifestV1) -> bool:
        return bool(manifest.plugin_id and manifest.name and manifest.version)
