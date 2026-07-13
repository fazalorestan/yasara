from app.platform_core.release_registry.build_history import build_history_registry
from app.platform_core.release_registry.release_registry import release_registry_service
from app.platform_core.release_registry.version_matrix import version_matrix_service

class ReleaseDashboardProvider:
    def dashboard(self):
        releases = release_registry_service.releases()
        history = build_history_registry.history()
        matrix = version_matrix_service.matrix()
        return {
            "ready": True,
            "current_version": releases["current_version"],
            "current_build_id": releases["current_build_id"],
            "release_channel": releases["release_channel"],
            "release_count": releases["release_count"],
            "latest_build_id": history["latest_build_id"],
            "last_successful_build": history["last_successful_build"],
            "last_failed_build": history["last_failed_build"],
            "version_matrix_compatible": matrix["compatible"],
            "source": "release_registry",
            "hardcoded_dashboard": False,
        }

release_dashboard_provider = ReleaseDashboardProvider()
