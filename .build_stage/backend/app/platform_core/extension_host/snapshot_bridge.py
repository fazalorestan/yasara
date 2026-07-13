from app.platform_core.extension_host.host import extension_host
from app.platform_core.state.snapshot import runtime_snapshot_manager
from app.platform_core.state.state_store import plugin_state_store

class ExtensionHostSnapshotBridge:
    def capture(self):
        loaded = extension_host.load_catalog()
        for plugin in loaded.get("plugins", []):
            plugin_state_store.set_state(plugin, {
                "host_registered": True,
                "runtime_state": "registered",
                "source": "extension_host_snapshot_bridge",
            })
        return runtime_snapshot_manager.export_snapshot("extension_host_snapshot")

extension_host_snapshot_bridge = ExtensionHostSnapshotBridge()
