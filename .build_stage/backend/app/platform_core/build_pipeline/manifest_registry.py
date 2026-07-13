class BuildManifestRegistry:
    def manifest(self):
        return {
            "ready": True,
            "project": "YaSara OS",
            "version": "v5.0-alpha.47",
            "package": "A",
            "build_id": "2026.47.A.001",
            "artifact_strategy": "registered_artifacts",
            "one_zip_per_package": True,
            "backward_compatible": True,
        }

build_manifest_registry = BuildManifestRegistry()
