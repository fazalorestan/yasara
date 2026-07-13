from pydantic import BaseModel, Field
from app.enterprise_v1.plugin_sdk import PluginSDKManifestV1, PluginSDKValidatorV1

class LoadedPluginV1(BaseModel):
    manifest: PluginSDKManifestV1
    loaded: bool = True

class PluginLoaderV1:
    def __init__(self):
        self.validator = PluginSDKValidatorV1()

    def load(self, manifest: PluginSDKManifestV1) -> LoadedPluginV1:
        if not self.validator.validate(manifest):
            raise ValueError("Invalid plugin manifest")
        return LoadedPluginV1(manifest=manifest)
