from app.platform_core.project_intelligence.build_metadata import build_metadata_service
from app.platform_core.project_intelligence.build_state import build_state_registry

class DesktopBuildInformationProvider:
    def build_info(self):
        metadata = build_metadata_service.metadata()
        state = build_state_registry.snapshot()
        return {
            "ready": True,
            "version": metadata["version"],
            "build": metadata["build"],
            "channel": metadata["channel"],
            "last_build_time": state["last_build_time"],
            "last_build_status": state["last_build_status"],
            "source": "build_metadata_and_state_registry",
            "hardcoded_dashboard": False,
        }

desktop_build_information_provider = DesktopBuildInformationProvider()
