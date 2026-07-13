from app.platform_core.state.state_store import plugin_state_store

class RuntimeRestoreContract:
    def validate_snapshot(self, snapshot: dict):
        required = ["snapshot_id", "plugins"]
        missing = [key for key in required if key not in snapshot]
        return {
            "ready": True,
            "valid": len(missing) == 0,
            "missing": missing,
            "mode": "contract_only",
        }

    def restore_report(self, snapshot: dict):
        validation = self.validate_snapshot(snapshot)
        restored = []
        if validation["valid"]:
            for plugin, record in snapshot.get("plugins", {}).items():
                state = record.get("state", {}) if isinstance(record, dict) else {}
                plugin_state_store.set_state(plugin, state)
                restored.append(plugin)
        return {
            "ready": True,
            "validation": validation,
            "restored_plugins": restored,
            "mode": "report_only",
        }

runtime_restore_contract = RuntimeRestoreContract()
