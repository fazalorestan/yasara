from app.platform_core.kernel.plugin_registry import PluginManifest, plugin_registry
from app.platform_core.kernel.plugin_lifecycle import plugin_lifecycle
from app.platform_core.kernel.health_registry import health_registry
from app.platform_core.kernel.event_bus import PlatformEvent, event_bus
from app.platform_core.contracts.events import PLUGIN_LOADED
from app.v423_plugin_catalog.loader import PluginManifestLoaderV423
from app.v423_plugin_catalog.governance_bridge import GovernanceContextV423, PluginGovernanceBridgeV423
from app.v424_plugin_registry_sync.dependency_validator import PluginDependencyValidatorV424

class PluginRegistrySyncServiceV424:
    def __init__(self):
        self.loader = PluginManifestLoaderV423()
        self.validator = PluginDependencyValidatorV424()
        self.governance = PluginGovernanceBridgeV423()

    def _to_core_manifest(self, manifest):
        return PluginManifest(
            name=manifest.name,
            version=manifest.version,
            dependencies=manifest.dependencies,
            feature_flags=manifest.feature_flags,
            required_permissions=manifest.required_permissions,
            required_licenses=manifest.required_licenses,
            routes=manifest.routes,
            services=manifest.services,
            tests=manifest.tests,
            documentation=manifest.documentation,
            metadata={
                **manifest.metadata,
                "category": manifest.category,
                "source": "v4_24_sync",
            },
        )

    def sync(self):
        manifests = self.loader.load_all()
        validation = self.validator.validate(manifests)
        synced = []

        for manifest in manifests:
            core_manifest = self._to_core_manifest(manifest)
            plugin_lifecycle.discover(core_manifest)
            plugin_lifecycle.validate(core_manifest.name)
            plugin_lifecycle.load(core_manifest.name)
            synced.append(core_manifest.name)
            event_bus.publish(PlatformEvent(
                name=PLUGIN_LOADED,
                source="plugin_registry_sync_v424",
                payload={"plugin": core_manifest.name, "version": core_manifest.version},
            ))

        health_registry.set("plugin_registry_sync_v424", True, f"{len(synced)} plugins synced")

        return {
            "ready": True,
            "synced_count": len(synced),
            "synced_plugins": synced,
            "dependency_validation": validation,
            "mode": "report_only",
            "no_new_trading_features": True,
        }

    def lifecycle_report(self):
        plugins = plugin_registry.list()
        return {
            "ready": True,
            "plugin_count": len(plugins),
            "plugins": {
                name: {
                    "state": item["state"],
                    "version": item["manifest"].version,
                    "dependencies": item["manifest"].dependencies,
                    "feature_flags": item["manifest"].feature_flags,
                    "required_permissions": item["manifest"].required_permissions,
                    "required_licenses": item["manifest"].required_licenses,
                }
                for name, item in plugins.items()
            },
        }

    def governance_report(self):
        manifests = self.loader.load_all()
        context = GovernanceContextV423()
        return {
            "ready": True,
            "mode": "report_only",
            "results": [self.governance.evaluate(m, context) for m in manifests],
        }
