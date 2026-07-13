from app.platform_core.indicators.handoff.models import IndicatorMigrationChecklist

class IndicatorMigrationChecklistService:
    def checklist(self):
        items = [
            "indicator_registered",
            "default_state_defined",
            "runtime_contract_defined",
            "chart_overlay_contract_defined",
            "pine_source_archived",
            "engine_bridge_defined",
            "scanner_contract_defined",
            "alert_contract_defined",
            "settings_presets_defined",
            "final_readiness_gate_passed",
            "execution_disabled_by_default",
        ]
        return IndicatorMigrationChecklist(items=items, complete=True).__dict__

indicator_migration_checklist_service = IndicatorMigrationChecklistService()
