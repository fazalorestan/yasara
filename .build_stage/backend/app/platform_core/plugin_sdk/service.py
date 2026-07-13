from app.platform_core.plugin_sdk.compatibility import plugin_compatibility_service
from app.platform_core.plugin_sdk.loader import plugin_loader_contract
from app.platform_core.plugin_sdk.manifest import plugin_manifest_service
from app.platform_core.plugin_sdk.metadata import plugin_metadata_service
from app.platform_core.plugin_sdk.registry import plugin_registry_service
from app.platform_core.plugin_sdk.safety import plugin_safety_contract

class PluginSDKCoreService:
    def manifest(self): return {"ready": True, "manifest": plugin_manifest_service.sample_manifest()}
    def validate(self): return plugin_manifest_service.validate(plugin_manifest_service.sample_manifest())
    def metadata(self): return plugin_metadata_service.metadata(plugin_manifest_service.sample_manifest())
    def registry(self): return plugin_registry_service.list_plugins()
    def loader_contract(self): return plugin_loader_contract.load_contract(plugin_manifest_service.sample_manifest())
    def compatibility(self): return plugin_compatibility_service.check(plugin_manifest_service.sample_manifest())
    def safety(self): return plugin_safety_contract.evaluate(plugin_manifest_service.sample_manifest())
    def status(self):
        validation = self.validate()
        compatibility = self.compatibility()
        safety = self.safety()
        return {
            "ready": validation["valid"] and compatibility["compatible"] and safety["safe"],
            "validation_ready": validation["valid"],
            "compatible": compatibility["compatible"],
            "safe": safety["safe"],
            "execution_allowed": False,
        }

plugin_sdk_core_service = PluginSDKCoreService()
