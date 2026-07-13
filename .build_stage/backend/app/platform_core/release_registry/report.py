from app.platform_core.release_registry.artifact_integrity import artifact_integrity_contract
from app.platform_core.release_registry.artifact_store import artifact_store_contract
from app.platform_core.release_registry.build_history import build_history_registry
from app.platform_core.release_registry.release_dashboard_provider import release_dashboard_provider
from app.platform_core.release_registry.release_notes import release_notes_registry
from app.platform_core.release_registry.release_registry import release_registry_service
from app.platform_core.release_registry.version_matrix import version_matrix_service

class ArtifactReleaseReportService:
    def report(self):
        return {
            "ready": True,
            "artifact_store": artifact_store_contract.store(),
            "release_registry": release_registry_service.releases(),
            "version_matrix": version_matrix_service.matrix(),
            "build_history": build_history_registry.history(),
            "release_notes": release_notes_registry.notes(),
            "artifact_integrity": artifact_integrity_contract.integrity(),
            "dashboard": release_dashboard_provider.dashboard(),
            "packaging_enabled": False,
            "hardcoded_dashboard": False,
            "real_execution_enabled": False,
            "real_broker_connection_enabled": False,
            "commercial_execution_engine_enabled": False,
            "commercial_api_key_required": False,
        }

artifact_release_report_service = ArtifactReleaseReportService()
ArtifactReleaseReport = ArtifactReleaseReportService
artifact_release_report = artifact_release_report_service
