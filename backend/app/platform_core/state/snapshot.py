from app.platform_core.clock import utc_now_iso
from app.platform_core.state.models import RuntimeSnapshot
from app.platform_core.state.state_store import plugin_state_store

class RuntimeSnapshotManager:
    def create_snapshot(self, snapshot_id: str = "runtime_latest", metadata: dict | None = None):
        snapshot = RuntimeSnapshot(
            snapshot_id=snapshot_id,
            plugins=plugin_state_store.list_states(),
            metadata=metadata or {"mode": "report_only"},
        )
        return snapshot

    def export_snapshot(self, snapshot_id: str = "runtime_latest"):
        snapshot = self.create_snapshot(snapshot_id)
        return {
            "snapshot_id": snapshot.snapshot_id,
            "plugins": snapshot.plugins,
            "metadata": snapshot.metadata,
            "created_at": snapshot.created_at,
            "exported_at": utc_now_iso(),
            "mode": "contract_only",
        }

runtime_snapshot_manager = RuntimeSnapshotManager()
