from app.platform_core.build_pipeline.artifact_registry import build_artifact_registry
from app.platform_core.build_pipeline.hash_generator import build_hash_generator
from app.platform_core.build_pipeline.metadata_registry import build_metadata_registry

class BuildDashboardProvider:
    def dashboard(self):
        metadata = build_metadata_registry.metadata()
        artifacts = build_artifact_registry.artifacts()
        build_hash = build_hash_generator.hash()
        return {
            "ready": True,
            "build_id": metadata["build_id"],
            "build_number": metadata["build_number"],
            "build_status": "foundation_ready",
            "build_hash": build_hash["build_hash"],
            "artifact_count": artifacts["artifact_count"],
            "last_successful_build": metadata["last_successful_build"],
            "last_failed_build": metadata["last_failed_build"],
            "source": "build_pipeline_registries",
            "hardcoded_dashboard": False,
        }

build_dashboard_provider = BuildDashboardProvider()
