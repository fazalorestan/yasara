from app.platform_core.extension_host.snapshot_bridge import extension_host_snapshot_bridge
from app.platform_core.state.restore import runtime_restore_contract
from app.platform_core.state.snapshot import runtime_snapshot_manager
from app.platform_core.state.state_store import plugin_state_store
from app.v428_plugin_state_snapshot.models import PluginStateSnapshotSummaryV428

class PluginStateSnapshotServiceV428:
    def summary(self):
        return PluginStateSnapshotSummaryV428()

    def set_state(self, plugin: str = "market_structure_pro", state: dict | None = None):
        record = plugin_state_store.set_state(plugin, state or {"status": "ready", "mode": "report_only"})
        return {"ready": True, "record": record.__dict__}

    def states(self):
        return {"ready": True, "states": plugin_state_store.list_states()}

    def snapshot(self):
        return {"ready": True, "snapshot": runtime_snapshot_manager.export_snapshot()}

    def restore_report(self, snapshot: dict):
        return runtime_restore_contract.restore_report(snapshot)

    def extension_host_snapshot(self):
        return {"ready": True, "snapshot": extension_host_snapshot_bridge.capture()}
