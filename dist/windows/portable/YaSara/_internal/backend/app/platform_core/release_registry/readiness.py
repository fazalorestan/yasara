from app.platform_core.release_registry.report import artifact_release_report_service

class ArtifactReleaseReadinessGate:
    def run(self):
        report = artifact_release_report_service.report()
        ready = (
            report["ready"]
            and report["artifact_store"]["integrity_required"]
            and report["release_registry"]["release_count"] >= 1
            and report["version_matrix"]["compatible"]
            and report["release_notes"]["changelog_present"]
            and report["artifact_integrity"]["tamper_detected"] is False
            and report["hardcoded_dashboard"] is False
            and report["commercial_execution_engine_enabled"] is False
        )
        return {
            "ready": ready,
            "checks": {
                "artifact_store_ready": report["artifact_store"]["ready"],
                "release_registry_ready": report["release_registry"]["ready"],
                "version_matrix_compatible": report["version_matrix"]["compatible"],
                "build_history_ready": report["build_history"]["ready"],
                "release_notes_ready": report["release_notes"]["ready"],
                "artifact_integrity_ready": report["artifact_integrity"]["ready"],
                "dashboard_ready": report["dashboard"]["ready"],
                "hardcoded_dashboard": False,
                "commercial_execution_engine_enabled": False,
                "commercial_api_key_required": False,
                "real_execution_enabled": False,
                "real_broker_connection_enabled": False,
            },
        }

artifact_release_readiness_gate = ArtifactReleaseReadinessGate()
