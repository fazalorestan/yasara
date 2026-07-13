from app.platform_core.indicators.handoff.compatibility import indicator_compatibility_matrix
from app.platform_core.indicators.handoff.migration_checklist import indicator_migration_checklist_service
from app.platform_core.indicators.handoff.release_manifest import indicator_release_manifest_service
from app.platform_core.indicators.handoff.v5_contract import indicator_v5_plugin_contract

class IndicatorPlatformHandoffService:
    def handoff(self):
        return {
            "ready": True,
            "release_manifest": indicator_release_manifest_service.manifest(),
            "v5_contract": indicator_v5_plugin_contract.contract(),
            "migration_checklist": indicator_migration_checklist_service.checklist(),
            "compatibility": indicator_compatibility_matrix.matrix(),
            "execution_allowed": False,
            "mode": "analysis_only",
        }

indicator_platform_handoff_service = IndicatorPlatformHandoffService()
