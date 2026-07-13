from app.platform_core.release_registry.release_registry import release_registry_service
from app.platform_core.release_registry.version_matrix import version_matrix_service

class ReleaseSignalProvider:
    def signal(self):
        releases = release_registry_service.releases()
        matrix = version_matrix_service.matrix()
        return {
            "ready": True,
            "current_version": releases["current_version"],
            "current_build_id": releases["current_build_id"],
            "release_channel": releases["release_channel"],
            "version_matrix_compatible": matrix["compatible"],
            "stable_release_available": releases["stable_release_available"],
            "signal": "green" if matrix["compatible"] else "red",
            "hardcoded_dashboard": False,
        }

release_signal_provider = ReleaseSignalProvider()
