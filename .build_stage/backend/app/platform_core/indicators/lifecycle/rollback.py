class IndicatorLifecycleRollbackContract:
    def rollback_plan(self, indicator: str):
        return {
            "ready": True,
            "indicator": indicator,
            "steps": [
                "disable_indicator",
                "restore_previous_state",
                "revalidate_manifest",
                "rebuild_registry_snapshot",
                "emit_lifecycle_audit_event",
            ],
            "destructive": False,
            "execution_allowed": False,
            "mode": "contract_only",
        }

indicator_lifecycle_rollback_contract = IndicatorLifecycleRollbackContract()
