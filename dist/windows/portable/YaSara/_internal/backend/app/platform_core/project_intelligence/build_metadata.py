from datetime import datetime, timezone
from app.platform_core.project_intelligence.version_state import version_state_registry

class BuildMetadataService:
    def metadata(self):
        version = version_state_registry.snapshot()
        return {
            "ready": True,
            "version": version["version"],
            "build": version["build"],
            "channel": version["channel"],
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "personal_execution_engine_enabled": version["personal_execution_engine_enabled"],
            "commercial_execution_engine_enabled": version["commercial_execution_engine_enabled"],
            "commercial_api_key_required": version["commercial_api_key_required"],
        }

build_metadata_service = BuildMetadataService()
